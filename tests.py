from analyze_fragment import *

print helper_fragment("CCTGCCGGAA", "ATTAGACCTG")[1] == 'ATTAGA'
print helper_fragment('AGACCTGCCG', 'CCTGCCGGAATAC')[1] == 'GAATAC'

stitch_fragments("inputs/practice_input_1.txt", "practice_output_1.txt")
txt = open("outputs/practice_output_1.txt")
s = str(txt.read())
# print s
# print "ATTAGACCTGCCGGAATAC"
print s == "ATTAGACCTGCCGGAATAC"


# stitch_fragments("inputs/practice_input_2.txt", "practice_output_2.txt")
# txt2 = open("outputs/practice_output_2.txt")
# s2 = str(txt2.read())
# print s2
# print s2 == "ATAAAGACGCGCGCGCGAAAAAAAAAAGTTGAATAAGCTGC"

stitch_fragments("inputs/practice_input_3.txt", "practice_output_3.txt")
txt3 = open("outputs/practice_output_3.txt")
s3 = str(txt3.read())
print s3
print s3 == "ATTAGACCTGCCGGAATAC"

