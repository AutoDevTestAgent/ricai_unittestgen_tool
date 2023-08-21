import json
import os
import openai

import typer
from pathlib import Path    
from gpt_engineer.ai import AI
from dotenv import load_dotenv

class RicaiUnitTestGenHelper:
    def __init__(self, openai_key):
        """
        Initializes the RicaiUnitTestGenHelper.
        Args:
            Weaviate_url (str): weaviate database connection url.
            Weaviate_api_key (str): weaviate database connection API key.
            Openai_api_key (str): OpenAI API key.
        """
        openai.api_key = openai_key
        if os.getenv("OPENAI_API_KEY") is None:
            load_dotenv()

        self.ai = AI(
            model_name=typer.Argument("gpt-4", help="model id string"),
            temperature=0.1,
        )

    def generate_unit_tests(self, code_files, requirements):
        """
        Generate unit tests based on the specification, that should work.
        """
        files = json.loads(code_files)
        instructions = "You are given a set of code files:\n\n"
        for f in files:
            instructions += f"filename: {f['file_path']}\n\n"
            instructions += f"content: {f['content']}\n\n"
        instructions += "For demo purposes, 3 test cases is enough!"

        messages = [
            self.ai.fuser(f"Instructions: {instructions}"),
            self.ai.fuser(f"Specification:\n\n{requirements}"),
        ]
        unit_test_preprompt = "You are a super smart developer using Test Driven Development to write tests according to a specification, based on code. Please generate UNIT TESTS CODE ONLY (no other texts or explanations) based on the above specification in the codebase language, using appripriate testing libraries (for example, pytest for Python). The tests should be as simple as possible, but still cover all the functionality."

        result_messages = self.ai.next(messages, unit_test_preprompt, step_name="generating unit tests")
        return result_messages[-1].content