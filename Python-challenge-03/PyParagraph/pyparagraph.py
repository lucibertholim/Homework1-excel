import re as re

#Opening Paragraph 1
document_text = open('raw_data/paragraph_1.txt', 'r')
text_string = document_text.read()

#Counting words

words=re.split("\W+",text_string)

num_word=len(words)

#Counting paragraphs

setences=re.split("(?<=[.!?]) +", text_string)

num_setences=len(setences)

#Counting word letters

letter_count_list=[]
for word in words:
    letter_count_list.append(len(word))
    
sum_letter_count=sum(letter_count_list)
average_letter_count=round((sum_letter_count/num_word), 1)


#Counting sentence lengh

setence_lengh_list=[]
for sentence in setences:
    sentence_word=re.split("\W+",sentence)
    setence_lengh_list.append(len(sentence_word))
    
sum_setence_lengh=sum(setence_lengh_list)
average_setence_lengh=sum_setence_lengh/num_setences


print("Paragraph 1 Analysis")    
print("------------------------------")
print("Approximate Word Count: "+str(num_word))
print("Approximate Sentence Count: "+str(num_setences))
print("Average Letter Count: "+str(average_letter_count))
print("Average Sentence Length:"+str(average_setence_lengh))

#print results to txt        
with open('pyparagraph_result.txt', 'w+') as f:
    print(("Paragraph 1 Analysis"), file=f)      
    print(("------------------------------"), file=f)  
    print(("Approximate Word Count: "+str(num_word)), file=f)  
    print(("Approximate Sentence Count: "+str(num_setences)), file=f)  
    print(("Average Letter Count: "+str(average_letter_count)), file=f)  
    print(("Average Sentence Length:"+str(average_setence_lengh)), file=f)      