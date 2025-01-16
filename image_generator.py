# DALL-E-3のAPIを利用して画像生成を行います。


import requests
from openai_generator import OpenAIGenerator


class ImageGenerator:
    def __init__(
        self,
        api_key,
        api_model,
        prompt_file="",
        output_file="",
        system_prompt_file="",
    ):
        self.generator = OpenAIGenerator(api_key, api_model)

        self.prompt_file = prompt_file
        self.system_prompt_file = system_prompt_file
        self.output_file = output_file

        self.size = "1024x1024"
        self.quality = "standard"
        self.n_generate_count = 1

        self.style = "vivid"

    def download_image(self, url, file_path):
        response = requests.get(url)
        with open(file_path, "wb") as file:
            file.write(response.content)

    def run(self):
        # prompt_fileを読み込む
        with open(self.prompt_file, "r", encoding="utf-8") as file:
            prompt = file.read()

        # system_prompt_fileを読み込む
        if self.system_prompt_file:
            with open(self.system_prompt_file, "r", encoding="utf-8") as file:
                system_prompt = file.read()
        else:
            system_prompt = ""

        # OpenAI APIを使用して画像を生成してURLを取得
        result_url = self.generator.call_image_generate(
            system_prompt, prompt, self.size, self.quality, 1, self.style
        )

        # result_urlの画像をダウンロード
        self.download_image(result_url, self.output_file)
