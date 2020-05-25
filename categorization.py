# 품사 태깅 라이브러리
from konlpy.tag import Okt

# cos similarity 계산을 위한 라이브러리
from numpy import dot
from numpy.linalg import norm
import numpy as np

# initialization Okt
okt = Okt()

# 빈도 추출 함수
def frequency_extractor(doc):
    set_array = set()
    for i in doc:
        for j in i:
            set_array.add(j)
    set_array = list(set_array)

    bow = [[0 for i in range(len(set_array))] for j in range(len(doc))]

    for i in range(len(set_array)):
        for j in range(len(doc)):
            bow[j][i] = doc[j].count(set_array[i])

    return bow

# cosine similarity 함수
def cos_similarity(A, B):
    return dot(A, B)/(norm(A)*norm(B))

# 형용사 분석 및 품사 태깅
doc = [
    okt.nouns(u'저는 사과 좋아요.'),
    okt.nouns(u'저는 바나나 좋아요.'),
    okt.nouns(u'저는 바나나 좋아요 저는 바나나 좋아요 저는 사과 좋아요 저는 사과 좋아요 저는 키위 좋아요.'),
    okt.nouns(u'저는 바나나 좋아요.')
]

bow = frequency_extractor(doc)

print("doc1 and doc2 유사도 : ", cos_similarity(bow[0], bow[1]))
print("doc1 and doc3 유사도 : ", cos_similarity(bow[0], bow[2]))
print("doc2 and doc3 유사도 : ", cos_similarity(bow[1], bow[2]))
print("doc2 and doc4 유사도 : ", cos_similarity(bow[1], bow[3]))