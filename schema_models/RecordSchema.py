# インポートさせたいモデルは、常に SchemaModel という名称で実装します。

from openai import OpenAI

client = OpenAI()


from typing import Dict, Literal, Union

from pydantic import BaseModel


# pip install -U git+https://github.com/nicholishen/tooldantic.git

# from tooldantic import OpenAiResponseFormatBaseModel as BaseModel


class Field(BaseModel):
    type: Literal[
        "SINGLE_LINE_TEXT",
        "MULTI_LINE_TEXT",
        "RICH_TEXT",
        "NUMBER",
        "CHECK_BOX",
        "RADIO_BUTTON",
        "MULTI_SELECT",
        "DROP_DOWN",
        "USER_SELECT",
        "ORGANIZATION_SELECT",
        "GROUP_SELECT",
        "DATE",
        "TIME",
        "DATETIME",
        "LINK",
    ]  # 許容される type の種類
    value: Union[str, None]  # value は文字列または None を許容


# レコード全体を表すモデル
class SchemaModel(BaseModel):
    record: Dict[str, Field]  # 任意のキー名を持つ Field の辞書
