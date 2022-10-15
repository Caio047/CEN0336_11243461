#!/usr/bin/env python3

# Import libraries
import sys
import re

# Assign the user arguments into variables
DNA = sys.argv[1]
n1 = sys.argv[2]
n2 = sys.argv[3]
n3 = sys.argv[4]
n4 = sys.argv[5]

# Check whether the input arguments are valid
not_nt = re.findall("[^atcgATCG]", DNA) # Regular expression to find any characters other than ATCG, thus invalidating the input as a DNA sequence if any is found.
if len(not_nt) > 0:
	print("ERROR: The first argument is not a DNA sequence")
	sys.exit()
elif bool(n1.isdigit()) is False or int(n1) < 0 or int(n1) > len(DNA):
	print("ERROR: The second given argument is not a positive integer smaller than the DNA sequence. Try again.")
	sys.exit()
elif bool(n2.isdigit()) is False or int(n2) < 0 or int(n2) > len(DNA):
	print("ERROR: The third given argument is not a positive integer smaller than the DNA sequence")
	sys.exit()
elif bool(n3.isdigit()) is False or int(n3) < 0 or int(n3) > len(DNA):
	print("ERROR: The fourth given argument is not a positive integer smaller than the DNA sequence")
	sys.exit()
elif bool(n4.isdigit()) is False or int(n4) < 0 or int(n4) > len(DNA):
	print("ERROR: The fifth given argument is not a positive integer smaller than the DNA sequence")
	sys.exit()

# Extract the CDS 1 and check whether it starts with "ATG"
CDS_1 = DNA[int(n1)-1:int(n2)]
if bool(CDS_1.startswith("ATG")) is False:
	print("ERROR: Given the second argument, the extracted sequence does not start with ATG.")
	sys.exit()

# Extract the CDS 2 and check whether it ends with stop codons (i.e., TAG, TAA or TGA)
CDS_2 = DNA[int(n3)-1:int(n4)]
if bool(CDS_2.endswith("TAG")) is False and bool(CDS_2.endswith("TAA")) is False and bool(CDS_2.endswith("TGA")) is False:
	print("ERROR: Given the fifth argument, the extracted sequence does not end with a stop codon")
	sys.exit()

# Concatenate CDS_1 and CDS_2 and print the complete CDS
print("\n" + CDS_1 + CDS_2)
