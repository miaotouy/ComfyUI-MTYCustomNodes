
class ParseJSONNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "json_string": ("STRING", {
                    "multiline": True,
                    "default": "{}"
                }),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING")
    #RETURN_NAMES = ("output_1", "output_2", "output_3", "output_4", "output_5")

    FUNCTION = "parse_json"

    CATEGORY = "MTY Custom Nodes"

    def parse_json(self, json_string):
        import json
        try:
            data = json.loads(json_string)
            outputs = [data.get(key, "") for key in sorted(data.keys())[:5]]
            return tuple(outputs)
        except json.JSONDecodeError:
            return ("", "", "", "", "")

NODE_CLASS_MAPPINGS = {
    "JSON解析": ParseJSONNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "JSON解析": "JSON解析 Node"
}
