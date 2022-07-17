from pprint import pprint
import requests
from xml.etree import ElementTree
import law_loader
import MeCab
import unidic

# 使う予定の法令等
# {
#   '特許法': '昭和三十四年法律第百二十一号',
#   '特許法施行規則': '昭和三十五年通商産業省令第十号',
#   '実用新案法': '昭和三十四年法律第百二十三号',
#   '実用新案法施行規則': '昭和三十五年通商産業省令第十一号',
#   '意匠法': '昭和三十四年法律第百二十五号',
#   '意匠法施行規則': '昭和三十五年通商産業省令第十二号',
#   '商標法': '昭和三十四年法律第百二十七号',
#   '商標法施行規則': '昭和三十五年通商産業省令第十三号',
#   '工業所有権に関する手続等の特例に関する法律': '平成二年法律第三十号',
#   '工業所有権に関する手続等の特例に関する法律施行規則': '平成二年通商産業省令第四十一号',
#   '特許登録令': '昭和三十五年政令第三十九号'
# }

law_dict = {
  '特許法': '昭和三十四年法律第百二十一号',
  '特許法施行規則': '昭和三十五年通商産業省令第十号',
  '特許登録令': '昭和三十五年政令第三十九号',
  '実用新案法': '昭和三十四年法律第百二十三号',
  '実用新案法施行規則': '昭和三十五年通商産業省令第十一号',
  '実用新案登録令': '昭和三十五年政令第四十号',
  '意匠法': '昭和三十四年法律第百二十五号',
  '意匠法施行規則': '昭和三十五年通商産業省令第十二号',
  '意匠登録令': '昭和三十五年政令第四十一号',
  '商標法': '昭和三十四年法律第百二十七号',
  '商標法施行規則': '昭和三十五年通商産業省令第十三号',
  '商標登録令': '昭和三十五年政令第四十二号',
  '工業所有権に関する手続等の特例に関する法律': '平成二年法律第三十号',
  '工業所有権に関する手続等の特例に関する法律施行規則': '平成二年通商産業省令第四十一号'
}

loader = law_loader.LawLoader(category=1)
for law_number in law_dict.values():
  url = f'https://elaws.e-gov.go.jp/api/1/lawdata/{law_number}'
  response = requests.get(url).content.decode(encoding="utf-8")
  print(response)


# loader = law_loader.LawLoader(category=2)
# row_numbers = loader.get_law_number('特許法')
# text = ''
# for row_number in row_numbers.values():
#   raw = loader.get_raw(row_number)
#   # pprint(raw, compact=False)
#   text += ' '.join(raw)
#   # print(raw)

# # print(text)

# tagger = MeCab.Tagger()
# nouns = [line for line in tagger.parse(text).splitlines() if "名詞" in line.split()[-1]]

# # print(result)
# for str in nouns:
#   print(str.split())