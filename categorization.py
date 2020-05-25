from konlpy.tag import Kkma
from konlpy.utils import pprint

# initialization Kkma
kkma = Kkma()

pprint(kkma.nouns(u'동의대학교에서 알려드립니다. 이번학기는 코로나로인해 휴강을 합니다.'))