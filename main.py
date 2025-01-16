import os
import sys
import argparse

from image_generator import ImageGenerator
from text_generator import TextGenerator


def generate_image(api_key, api_model, args):
    # ImageGeneratorを初期化して画像を生成
    generator = ImageGenerator(
        api_key, api_model, args.prompt_file, args.output_file, args.system_prompt_file
    )

    try:
        generator.run()
    except Exception as e:
        print(f"エラー: {e}")
        sys.exit(1)


def generate_text(api_key, api_model, args):
    # TextGeneratorを初期化してテキストを生成
    generator = TextGenerator(
        api_key, api_model, args.prompt_file, args.output_file, args.system_prompt_file
    )

    # JSONスキーマが指定されている場合は、スキーマファイルパスをgeneratorにセットする
    if args.schema_json != "":
        generator.set_schema_json(args.schema_json)

    try:
        generator.run()
    except Exception as e:
        print(f"エラー: {e}")
        sys.exit(1)


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
        "--image",
        required=False,
        default=False,
        action="store_true",
        help="画像生成を行う場合はTrueを指定します。",
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

    if args.image:
        print("画像生成を行います。")
        image_api_model = os.getenv("OPENAI_IMAGE_MODEL")
        if not image_api_model:
            image_api_model = "dall-e-2"

        generate_image(api_key, image_api_model, args)
    else:
        print("テキスト生成を行います。")
        generate_text(api_key, api_model, args)

    # 出力メッセージを表示
    print(f"処理結果が [{args.output_file}] に保存されました。")
