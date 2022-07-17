# 特許法等の解析
特許法を始めとする法令や審査基準、便覧等を自然言語処理などを用いて、これらの複雑度（準用や引用）を解析するためのリポジトリです。

解析がある程度、完了したら、[e-gov](https://elaws.e-gov.go.jp/)よりも使いやすい、以下の機能を有するWEBサービスを構築することを考えています。
1. 準用先、引用元にリンクを貼る
1. 要約文の作成
1. 単純なテキストマッチングではない、検索支援機能
1. Q&Aの自動生成


## 法令の取得先
[e-gov](https://www.e-gov.go.jp/)が提供するe-GOV法令APIを想定しています。

## 審査基準等の取得先
それぞれ特許庁ホームページ掲載のPDFから取得します。
- [特許・実用新案審査基準](https://www.jpo.go.jp/system/laws/rule/guideline/patent/tukujitu_kijun/index.html)
- [特許・実用新案審査ハンドブック](https://www.jpo.go.jp/system/laws/rule/guideline/patent/handbook_shinsa/index.html)
- [意匠審査基準](https://www.jpo.go.jp/system/laws/rule/guideline/design/shinsa_kijun/index.html)
- [商標審査基準](https://www.jpo.go.jp/system/laws/rule/guideline/trademark/kijun/index.html)
- [商標審査便覧](https://www.jpo.go.jp/system/laws/rule/guideline/trademark/binran/index.html)

## 便覧等の取得先
審査基準同様、特許庁ホームページ掲載のPDFから取得します。
- [商標審査便覧](https://www.jpo.go.jp/system/laws/rule/guideline/trademark/binran/index.html)
- [方式審査便覧](https://www.jpo.go.jp/system/laws/rule/guideline/hoshiki-shinsa-binran/index.html)
- [審判便覧](https://www.jpo.go.jp/system/trial_appeal/sinpan-binran.html)

## 手順
実行環境は、Dockerによりコンテナ化しています。

以下の手順で、コンテナを起動してください。
1. `docker image build -t python3 .`
1. `docker run --name python3 -v ~/app/jpo/analyze-patent-law:/usr/app -it python3 /bin/bash`
1. `docker container exec -it python3 bash`
1. `python3 main.py`