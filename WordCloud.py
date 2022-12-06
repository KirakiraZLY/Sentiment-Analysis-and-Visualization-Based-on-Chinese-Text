import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud
file = open("posresult_jieba.txt", 'r',encoding="utf-8")
text1 = file.read()
file.close()
file = open("negresult_jieba.txt", 'r',encoding="utf-8")
text2 = file.read()
file.close()
# text_positive = open(r'posresult_jieba.txt', "r",encoding="utf-8").read()
# text_negative = open(r'negresult_jieba.txt', "r",encoding="utf-8").read()

stop_words = open("./stop_words.txt", 'r', encoding="utf-8").read()
import re

text_list1 = text1.split(" ")
stop_words_list = stop_words.split("\n")
final_text_list1 = ''
for seg in text_list1:
    if not ((seg in stop_words_list) or re.search(r"^\S$", seg)):  # 不在stopwords_list, 同时不是单字节
        final_text_list1 += seg
        final_text_list1 += " "

text_list2 = text2.split(" ")
stop_words_list = stop_words.split("\n")
final_text_list2 = ''
for seg in text_list2:
    if not ((seg in stop_words_list) or re.search(r"^\S$", seg)):  # 不在stopwords_list, 同时不是单字节
        final_text_list2 += seg
        final_text_list2 += " "
result1 = ''.join(final_text_list1)
wc = WordCloud(
    font_path="C:/Windows/Fonts/simhei.ttf",
    background_color="white",
    max_words=100,
    max_font_size=80
).generate(result1)
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
wc.to_file('./pics/pos_cloud.png')
result2 = ''.join(final_text_list2)
wc = WordCloud(
    font_path="C:/Windows/Fonts/simhei.ttf",
    background_color="white",
    max_words=100,
    max_font_size=80
).generate(result2)
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
wc.to_file('./pics/neg_cloud.png')
