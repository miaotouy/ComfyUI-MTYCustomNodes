import json
import re

class ParseJSONNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_text": ("STRING", {
                    "multiline": True,
                    "default": "这是一段包含JSON的文本: {}"
                }),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING")
    #RETURN_NAMES = ("output_1", "output_2", "output_3", "output_4", "output_5")

    FUNCTION = "parse_json"

    CATEGORY = "MTY Custom Nodes"

    def parse_json(self, input_text):
        # 正则表达式匹配JSON对象
        try:
            json_str = re.search(r"\{.*\}", input_text).group()
            data = json.loads(json_str)
            outputs = [data.get(key, "") for key in sorted(data.keys())[:5]]
            return tuple(outputs)
        except (json.JSONDecodeError, AttributeError):
            return ("", "", "", "", "")

NODE_CLASS_MAPPINGS = {
    "JSON解析": ParseJSONNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "JSON解析": "JSON解析 Node"
}
