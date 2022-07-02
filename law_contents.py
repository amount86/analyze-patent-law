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

gcp_raw = get_raw("昭和三十四年法律第百二十一号")
pprint(gcp_raw, compact=False)