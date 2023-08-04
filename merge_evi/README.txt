■前提
・eviフォルダに保存されてエビデンスをExcelファイル（テスト仕様書兼結果報告書_エビデンス.xlsx）にマージする
・すべてのエビデンスファイルをマージする
・ないエビデンスは例外処理（FileNotFoundError）でスキップする


■WindowsPowerShellでpythonを利用する環境構築手順
下記URLから最新のpythonをインストールする。(2023/08/04現在:python-3.11.4-amd64.exe)
https://www.python.org/downloads/

インストールの流れは下記URLを参照
https://bluebirdofoz.hatenablog.com/entry/2019/01/19/141007

OpenPyXLのダウンロード・インストール手順
pythonインストール後、外部パッケージ「OpenPyXL」をインストール
こちらをインストールすることで、Excelの操作ができるようになる
手順
1.コマンドプロンプトに「pip install openpyxl」と入力する

以上で環境構築完了
参考URL
https://pg-chain.com/python-openpyxl


■手順
1. eviフォルダにエビデンスを保管する
2. Powershellを起動し、[merge_evi.py]を実行する
	python merge_evi.py
3. Excelファイル（evi_sheets.xlsx）の各シート毎にマージされていることを確認する

