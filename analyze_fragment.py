import sys

def helper_fragment(main_frag, frag):
	'''
	DESCRIPTION
	-----------
	given a string main_frag, this function tries to string match 
	a portion of the beginning of frag and makes sure that it matches with something
	inside of main_frag. Then it does the same thing for the beginning of main_frag
	and the end of the actual frag, so that you can make sure that's good too. 
	The goal is to try to find the largest beginning substring 
	of frag that falls into main_frag, and just append the part of frag that does 
	not intersect with main_frag

	INPUT PARAMETERS
	----------------
	main_frag: String
		The actual string (Genomic Sequence) that you are uploading into the web application
	frag: String 
		The subportion of the string that you will be adding to the 
	
	OUTPUT PARAMETERS 
	-----------------
	remainder_tuple: tuple
		[0]: Where the new string should be placed in the genome
		[1]: The part of the genomic sequence frag that does not lie inside
		of the main_frag
		[2]: The number of common elements
	'''
	if frag in main_frag: 
		return ('back', "", len(frag))
	i = len(frag)
	while i > 0 and frag[:i] not in main_frag[-i:]:
		i -= 1
	back_string = frag[i:]
	back_tuple = ("back", back_string, i)	

	j = 0
	while j < len(frag) and frag[-j:] not in main_frag[:j]:
		j += 1

	front_string = frag[:-j]
	front_tuple = ("front", front_string, j)
	if len(front_tuple[1]) < len(back_tuple[1]) and front_tuple[1] != '':
		return front_tuple
	else: 
		return back_tuple
		
def get_maximum_intersection(f1, f_arr):
	'''
	DESCRIPTION
	------------
	Given some fragment f1, you want to get the tuple that has the largest intersection 
	over it. This is done by figuring out which has the largest overlap. 

	INPUT PARAMETERS
	----------------
	f1: String
		This is the main fragment that you're comparing everything to
	f_arr: list of Strings
		This is the list of all of your other fragments

	OUTPUT PARAMETERS
	-----------------
	remainder_tuple: tuple
		[0]: Where the new string should be placed in the genome
		[1]: The part of the genomic sequence frag that does not lie inside
		of the main_frag
		[2]: The number of common elements
		[3]: The actual fragment you're trying to get rid of in your array
	'''
	remainder_tuple = helper_fragment(f1, f_arr[0]) + (f_arr[0],)
	for frag in f_arr: 
		if frag != f1: 
			cur_tuple = helper_fragment(f1, frag)
			if cur_tuple[2] > remainder_tuple[2]:
				remainder_tuple = cur_tuple + (frag,)
	return remainder_tuple 


def stitch_fragments_helper(f_arr):
	'''
	DESCRIPTION
	-----------
	This basically goes through all of your individual fragments in your f_arr
	and gets the parts that don't overlap to get the complete genome. 
	
	INPUT PARAMETERS
	----------------
	f_arr: List of Strings
		containts all of the DNA fragments

	OUTPUT PARAMETERS
	-----------------
	res: String
		The complete returned DNA sequence
	'''
	while len(f_arr) > 1:
		frag = f_arr[0]
		current_tuple = get_maximum_intersection(frag, f_arr[1:])
		new_frag = frag
		if current_tuple[0] == "back":
			new_frag += current_tuple[1]
		else: 
			new_frag = current_tuple[1] + new_frag
		f_arr.remove(frag)
		f_arr.remove(current_tuple[3])
		f_arr.append(new_frag)
	res = f_arr[0]
	return res

def stitch_fragments_helper_2(f_arr):
	'''
	DESCRIPTION
	-----------
	This basically goes through all of your individual fragments in your f_arr
	and gets the parts that don't overlap to get the complete genome. 
	
	INPUT PARAMETERS
	----------------
	f_arr: List of Strings
		containts all of the DNA fragments

	OUTPUT PARAMETERS
	-----------------
	res: String
		The complete returned DNA sequence
	'''
	res = ""
	for frag in f_arr:
		where, remainder_dna, overlap = helper_fragment(res, frag)
		if where == "back":
			res += remainder_dna
		else: 
			res = remainder_dna + res
	return res

def read_file_contents(filename):
	'''
	DESCRIPTION
	-----------
	This function actually reads the file contents into
	an array that is split by the FASTA format. 

	INPUT PARAMETERS
	----------------
	filename: String
		the name of the input file that you are putting in

	OUTPUT PARAMETERS 
	-----------------
	new_contents: String 
		the full string output of the complete genome that we are processing
	'''
	txt = open(filename)
	contents = "".join(str(txt.read()).split("\r")).split("\n")
	split_list = []
	for i in range(len(contents)):
		if ">" in contents[i]:
			split_list.append(i)
	new_contents = []
	for j in range(1, len(split_list)):
		start = split_list[j - 1]
		end = split_list[j]
		new_contents.append("".join(contents[start + 1: end]))
	start = split_list[len(split_list) - 1]
	new_contents.append("".join(contents[start + 1:]))
	return new_contents
	
def stitch_fragments(input_file, output_file):
	'''
	DESCRIPTION
	-----------
	Takes in an input file, process it with read_content_files, 
	and then outpus the processed genome to the output_file

	INPUT PARAMETERS
	----------------
	input_file: String
		the name of the input file
	output_file: String
		the name of the output file

	OUTPUT PARAMETERS
	-----------------
	None (outputted to a text_file)
	'''
	if ".txt" in input_file and ".txt" in output_file:
		f_arr = read_file_contents(input_file)
		genome_str = stitch_fragments_helper(f_arr)
		if genome_str != "":
			text_file = open("outputs/" + output_file, "w")
			text_file.write(genome_str)
			text_file.close()

if __name__ == '__main__':
	arg1 = str(sys.argv[1])
	arg2 = str(sys.argv[2])
	stitch_fragments(arg1, arg2)


