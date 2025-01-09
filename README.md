
# ChattyJSON

CLIでChatGPTでJSONファイルを作成したい人に向けたCLIツールです
JSON出力を目的としているため、プロンプト、システムプロンプトに加えて、JSONスキーマの３つ組のファイルで処理を実行できる点が特徴です。
別のソフトウェアの入力としてLLMを通したJSONを大量に用意したいときにご利用ください。

## 使用方法

ChattyJSONは、コマンドラインインターフェース（CLI）を通じて使用できます。
pythonで作成していますので、あらかじめpythonの実行環境をご準備ください。

`main.py`を呼び出すとヘルプを表示します。

  $ python main.py

> usage: main.py [-h] --prompt_file PROMPT_FILE --output_file OUTPUT_FILE [--system_prompt_file SYSTEM_PROMPT_FILE] [--schema_json SCHEMA_JSON]

## 実行準備

事前準備として、`.env`ファイルにOpenAI APIのAPIキーを書き込んでおいてください。
使用するモデルも指定できます。

```
OPENAI_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
OPENAI_MODEL="gpt-4o"
```


## オプションの説明:
  - `-h`: ヘルプメッセージを表示します。
  - `--prompt_file PROMPT_FILE`: プロンプトが含まれるファイルを指定します。
  - `--output_file OUTPUT_FILE`: 出力するJSONファイルの名前を指定します。
  - `--system_prompt_file SYSTEM_PROMPT_FILE`: （オプション）システムプロンプトが含まれるファイルを指定します。
  - `--schema_json SCHEMA_JSON`: （オプション）JSONスキーマを指定します。

### プロンプトについて
プロンプトは、ChattyJSONが生成するJSONファイルの内容を決定するための指示を含むテキストです。ユーザーはこのプロンプトを通じて、生成されるデータの具体的な要件や期待される形式を指定します。プロンプトファイルは必須であり、`--prompt_file`オプションを使用して指定します。

### システムプロンプトについて
システムプロンプトは、生成プロセスにおける追加のコンテキストや制約を提供するために使用されるオプションのファイルです。これにより、生成されるJSONの一貫性や特定のスタイルを維持することができます。システムプロンプトは`--system_prompt_file`オプションを使用して指定します。

### JSONスキーマについて
JSONスキーマは、生成されるJSONデータの構造を定義するための仕様です。スキーマを使用することで、生成されるデータが特定の形式や制約に従うことを保証できます。JSONスキーマはオプションであり、`--schema_json`オプションを使用して指定します。スキーマを指定することで、データの整合性を確保し、予期しないデータ形式の生成を防ぐことができます。


## ライセンス

このプロジェクトは、GNU General Public License v3.0 (GPL-3.0) の下でライセンスされています。詳細については、[LICENSE](LICENSE) ファイルを参照してください。

