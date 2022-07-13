# 特許法等の解析
特許法を始めとする法令や方式審査便覧等を自然言語処理などを用いて、これらの複雑度（準用や引用）を解析するためのリポジトリです。

## 法令の取得先
[e-gov](https://www.e-gov.go.jp/)が提供するe-GOV法令APIを想定しています。

## 方式審査便覧の取得先
[特許庁ホームページ](https://www.jpo.go.jp/system/laws/rule/guideline/hoshiki-shinsa-binran/index.html)のPDFから取得することを想定しています。

## 手順
実行環境は、Dockerによりコンテナ化しています。

以下の手順で、コンテナを起動してください。
1. `docker image build -t python_3.8 .`
1. `docker run --name python_3.8 -v ~/app/jpo/analyze-patent-law:/usr/app -it python_3.8 /bin/bash`
1. `docker container exec -it python_3.8 bash`
1. `python3 main.py`