from konlpy.tag import Okt
from numpy import dot
from numpy.linalg import norm
from sklearn.cluster import AgglomerativeClustering
import os
import shutil


def frequency_extractor(document):  # 빈도 행렬 추출 함수.
    noun = set()  # 세트(집합) 자료 구조 선언.
    for i in document:  # 명사 추출된 문서들의 수만큼 반복.
        for j in i:  # 각 문서들의 명사 수만큼 반복.
            noun.add(j)  # 각 문서들의 명사를 모두 세트(집합)에 추가.
    noun = list(noun)  # 세트(집합)을 이후 인덱스 연산에 활용하기 위해 리스트로 변경.

    # 문서의 수만큼 리스트 생성 후, 세트의 자료 수만큼 2차원 리스트 추가 생성.
    frequency = [[0 for i in range(len(noun))] for j in range(len(document))]

    for i in range(len(noun)):  # 세트의 자료 수만큼 반복.
        for j in range(len(document)):  # 각 문서의 수만큼 반복.
            frequency[j][i] = document[j].count(
                noun[i]
            )  # 문서 속 명사들과 세트 속 명사들을 비교하여 카운트.

    return frequency  # 빈도를 나타내는 말뭉치 반환.


def cos_similarity(a, b):  # 유사도 측정 함수.
    temp = norm(a) * norm(b)
    if temp == 0:
        return 0
    return 1 - dot(a, b) / (norm(a) * norm(b))  # 유사도 측정 식.


def two_dimension_matrix(frequency):
    matrix = [
        [cos_similarity(frequency[i], frequency[j]) for i in range(len(frequency))]
        for j in range(len(frequency))
    ]
    return matrix


def hierarchical_clustering(matrix, n_clusters=2):  # 계층적 군집화 알고리즘 수행 함수.
    return AgglomerativeClustering(n_clusters).fit(matrix).labels_


def noun_extractor(txt_folder):
    okt = Okt()  # Twitter 클래스의 객체 선언.
    doc = []
    print("처리 중...")
    for root, dirs, files in os.walk(txt_folder):  # 폴더 안의 모든 문서를 불러옴.
        for fname in files:
            full_fname = os.path.join(root, fname)
            f = open(full_fname, "r")
            data = f.read()  # 각 문서의 모든 문자를 반환.
            doc.append(okt.nouns(data))  # 반환한 문자를 이용하여 토큰화 수행(명사 추출).
            f.close()
    print("완료")

    return doc


def move_sorted_file(file_list, txt_folder, py_folder, after, clustering_result):
    for i in range(len(file_list)):
        before_dir = f"{txt_folder}\\{file_list[i]}"
        after_dir = f"{py_folder}\\{after}\\{clustering_result[i]}"
        try:
            if not (os.path.isdir(after_dir)):
                os.makedirs(os.path.join(after_dir))
        except OSError as e:
            if e.errno != errno.EEXIST:
                print("Failed to create directory!!!!!")
                raise
        after_dir = f"{after_dir}\\{file_list[i]}"
        shutil.move(before_dir, after_dir)
