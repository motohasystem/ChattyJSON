import json
import os

from openai_generator import OpenAIGenerator


class TextGenerator:
    def __init__(
        self,
        api_key,
        api_model,
        prompt_file="",
        output_file="",
        system_prompt_file="",
    ):
        self.generator = OpenAIGenerator(api_key, api_model)
        self.schema_json = ""  # JSONスキーマファイルのパス

        self.prompt_file = prompt_file
        self.system_prompt_file = system_prompt_file
        self.output_file = output_file

    def set_schema_json(self, schema_json):
        self.schema_json = schema_json
        self.generator.schema_json = schema_json

    def set_schema_model(self, schema_model):
        self.generator.schema_model = schema_model

    def run(self):
        self.generate_and_save_text(
            prompt_file=self.prompt_file,
            system_prompt_file=self.system_prompt_file,
            output_file=self.output_file,
        )

    def generate_and_save_text(self, prompt_file, system_prompt_file, output_file):
        generated_text = self.generator.generate_text(prompt_file, system_prompt_file)

        if generated_text:
            print("生成されたテキスト:")
            print(generated_text)

            # ファイルを保存するまえに、保存先ディレクトリがなければ作成する
            output_dir = os.path.dirname(output_file)
            try:
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)
            except OSError as e:
                print(f"ディレクトリ作成エラー: {e}")
                return

            # 生成されたテキストをJSON形式で保存
            try:
                with open(output_file, "w", encoding="utf-8") as json_file:
                    json_file.write(
                        json.dumps(
                            json.loads(generated_text), indent=4, ensure_ascii=False
                        )
                    )

                print(f"生成されたテキストが{output_file}に保存されました。")
            except Exception as e:
                print(f"JSONファイル保存エラー: {e}")
        else:
            print("テキスト生成に失敗しました。")
