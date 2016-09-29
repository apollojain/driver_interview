Driver interview
================

Introduction
------------
In the world of genomics, it is sometimes necessary to do genetic processing to ensure that given a bunch of DNA snippets, we get a full genomic sequence. I created a piece of software that can be used in two ways: either through a Flask Application or through command line

How It Works
------------
All of the special sauce is in analyze_fragment.py. The basic idea that we do is that first we read a string from a text file. This is, naturally, seperated by line breaks, so we want to break everything up by line breaks. Then, we figure out which lines have the FASTA format inputs (i.e. >Frag_56). These indicate new inputs. So, we want to join all of the lines between these FASTA inputs to create a bunch of individual DNA molecules (i.e. break the total string by these FASTA inputs into an array of individual DNA sequences). This is all done in the "read_file_contents" function. After this, we want to stitch individual DNA sequences into a complete Genome in the "stitch_fragments_helper." To do this, we iterate through all of the fragments, starting at the first gragment. We want to match the first fragment in the list to the fragment in the remainder of the list that has the highest overlap. We stitch these two fragments by finding the part of the fragment that does not overlap and then placing it at the front or the back, wherever it needs to go. We use the function "helper_fragment" to see the overlap of our genome and the DNA sequence, which is called by "get_maximum_intersection," which finds the fragment f2 with the most overlap with f1 of all the fragments. If the entire current DNA sequence is somewhere in the genome, then you're done. Otherwise, you want to check the back of the genome up to this point and eliminate any overlap with the current DNA sequence. You also want to check the front of the current genome as well and do the same thing. Afterwards, "stitch_fragments_helper" takes the newly stitched fragment, adds it to the back of your array, and then deletes fragments f1 and f2. This is done until the array is empty. 

How to use
------------
Want to use this file through Flask?
First, run
```
pip install -r requirements.txt
```
Now, you have Flask installed on your computer. Next, run
```
python server.py
```
From there, you go to localhost:5000, where you can select the file you want. Then, when you submit, the outputted genome will live inside of your "outputs" folder.

Don't want to deal with the flask interface? In that case, just run the following from command line for a file in in the inputs folder
```
python analyze_fragments.py inputs/practice_input_1.txt practice_output_1.txt
```
This will output a file called "practice_outputs_1.txt" in your outputs folder. 