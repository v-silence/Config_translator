import json
import sys
import re
import argparse
from typing import Any, Dict, List


class ConfigTranslator:
    def __init__(self):
        self.constants = {}
        self.identifier_pattern = re.compile(r'^[a-zA-Z][_a-zA-Z0-9]*$')

    def validate_identifier(self, name: str) -> bool:
        return bool(self.identifier_pattern.match(name))

    def format_value(self, value: Any) -> str:
        if isinstance(value, (int, float)):
            return str(value)
        elif isinstance(value, str):
            return f"'{value}'"
        elif isinstance(value, list):
            elements = ', '.join(self.format_value(v) for v in value)
            return f"#({elements})"
        elif isinstance(value, dict):
            pairs = ', '.join(f"{k} => {self.format_value(v)}"
                              for k, v in value.items()
                              if self.validate_identifier(k))
            return f"{{{pairs}}}"
        return str(value)

    def process_constants(self, data: Dict) -> str:
        result = []
        if "_constants" in data:
            for name, value in data["_constants"].items():
                if self.validate_identifier(name):
                    self.constants[name] = value
                    result.append(f"{name}: {self.format_value(value)}")
            del data["_constants"]


        result.append(self.format_value(data))
        return '\n'.join(result)


def main():
    parser = argparse.ArgumentParser(description='JSON to Custom Config converter')
    parser.add_argument('-i', '--input', required=True, help='Input JSON file path')
    parser.add_argument('-o', '--output', required=True, help='Output file path')
    args = parser.parse_args()

    try:
        with open(args.input, 'r') as infile:
            json_data = json.load(infile)

        translator = ConfigTranslator()
        result = translator.process_constants(json_data)


        with open(args.output, 'w') as outfile:
            outfile.write(result)

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON in '{args.input}': {e}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError as e:
        print(f"Error: {e.strerror}: {e.filename}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
