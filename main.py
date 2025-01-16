import os
import sys
import argparse

from text_generator import TextGenerator

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="OpenAI APIを使用してテキストを生成します。"
    )
    parser.add_argument(
        "--prompt_file",
        required=True,
        help="プロンプトファイルのパスを指定します。",
    )
    parser.add_argument(
        "--output_file",
        required=True,
        help="生成されたテキストを保存するJSONファイルのパスを指定します。",
    )
    parser.add_argument(
        "--system_prompt_file",
        required=False,
        default="",
        help="システムプロンプトを指定するオプションです。",
    )
    parser.add_argument(
        "--schema_json",
        required=False,
        default="",
        help="JSONスキーマを定義したJSONファイルを指定するオプションです。",
    )
    parser.add_argument(
        "--schema_model",
        required=False,
        default="",
        help="BaseModelでJSONスキーマを定義したファイルを指定するオプションです。",
    )

    args = parser.parse_args()

    # 環境変数からAPIキーを取得
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print(
            "エラー: OPENAI_API_KEYが設定されていません。.envファイルを作成してください。"
        )
        sys.exit(1)

    api_model = os.getenv("OPENAI_MODEL")
    if not api_model:
        api_model = "gpt-4o-mini"

    # TextGeneratorを初期化してテキストを生成
    generator = TextGenerator(
        api_key, api_model, args.prompt_file, args.output_file, args.system_prompt_file
    )

    # JSONスキーマが指定されている場合は、スキーマファイルパスをgeneratorにセットする
    if args.schema_json != "":
        generator.set_schema_json(args.schema_json)

    if args.schema_model != "":
        generator.set_schema_model(args.schema_model)

    try:
        generator.run()
    except Exception as e:
        print(f"エラー: {e}")
        sys.exit(1)

    # 出力メッセージを表示
    print(f"処理結果が [{args.output_file}] に保存されました。")
