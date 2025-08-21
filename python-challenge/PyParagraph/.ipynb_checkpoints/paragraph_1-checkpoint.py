import os
import re
#import string
paragraph_1_txt = os.path.join("raw_data","paragraph_1.txt")
#open&read txt

num_letter =int()
num_words =int()
num_sentence =int()

with open(paragraph_1_txt) as txtfile:
    txt=txtfile.read()
    txt_reader = txt.split()
# total words count    
    num_words=len(txt_reader)
# total letter count
    for i in range(len(txt_reader)):
        num_letter+=len(txt_reader[i])
ave_letter_count = round(num_letter/num_words,1)       

# total sentence count
sentence = re.split("(?<=[.!?]) +", txt)
num_sentence = len(sentence)
# ave sentence length
ave_sentence_len = round(num_words/num_sentence,1)
        
print("Paragraph 1 Analysis \n")
print("------------------------------\n")
print("Approximate Word Count: " + str(num_words) + "\n")
print("Approximate Sentence Count: " + str(num_sentence)+ "\n")
print("Average Letter Count: " + str(ave_letter_count) + "\n")
print("Average Sentence Length: " + str(ave_sentence_len) + "\n")

#print to text
output_path=os.path.join("paragraph_1_output.txt")
with open(output_path, "w", newline="") as txtfile:

    txtfile.write("Example Analysis \n")
    txtfile.write("--------------------------\n")
    txtfile.write("Approximate Word Count: " + str(num_words) + "\n")
    txtfile.write("Approximate Sentence Count: " + str(num_sentence)+ "\n")
    txtfile.write("Average Letter Count: " + str(ave_letter_count) + "\n")
    txtfile.write("Average Sentence Length: " + str(ave_sentence_len) + "\n")
    txtfile.write("---------------------------\n")