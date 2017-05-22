from math import log

##def count_tf(word,texts): #в тексте должен быть уже массив слов; texts это
##    return text.count(word) / len(text) ## массив массивов?
##
##def count_id(word,texts):
##    n = len(texts) / (1+sum([1 for text in texts if word in text])) #сразу обратная
    
def count_tfidf(word,text,texts):
    tf = text.count(word) / len(text)
    idf = len(texts) / (1+sum([1 for t in texts if word in t]))
    return log(tf,10)*log(idf,10 )



