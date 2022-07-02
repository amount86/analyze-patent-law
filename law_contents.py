# 参考：https://qiita.com/Lisphilar/items/39ad23ac7ade21313911

# 標準ライブラリ
from functools import lru_cache
from pprint import pprint
import re
from xml.etree import ElementTree
# pip install requests
import requests

@lru_cache
def get_raw(number):
  """
  Retrieve contents of the law specified with law number from e-Gov API.

  Args:
      number (str): Number of the law, like '平成九年厚生省令第二十八号'

  Returns:
      raw (list[str]): raw contents of J-GCP
  """
  url = f"https://elaws.e-gov.go.jp/api/1/lawdata/{number}"
  r = requests.get(url)
  root = ElementTree.fromstring(r.content.decode(encoding="utf-8"))
  contents = [e.text.strip() for e in root.iter() if e.text]
  return [t for t in contents if t]

law_number_dictionary = {
  '特許法': '昭和三十四年法律第百二十一号',
  '特許法施行規則': '昭和三十五年通商産業省令第十号',
  '実用新案法': '昭和三十四年法律第百二十三号',
  '実用新案法施行規則': '昭和三十五年通商産業省令第十一号',
  '意匠法': '昭和三十四年法律第百二十五号',
  '意匠法施行規則': '昭和三十五年通商産業省令第十二号',
  '商標法': '昭和三十四年法律第百二十七号',
  '商標法施行規則': '昭和三十五年通商産業省令第十三号',
  '工業所有権に関する手続等の特例に関する法律': '平成二年法律第三十号',
  '工業所有権に関する手続等の特例に関する法律施行規則': '平成二年通商産業省令第四十一号',
  '特許登録令': '昭和三十五年政令第三十九号'
}

gcp_raw = get_raw(law_number_dictionary['特許法'])
pprint(gcp_raw, compact=False)