import json
import weaviate
import os
import openai

class RicaiUnitTestGenHelper:
    def __init__(self, openai_key):
        """
        Initializes the RicaiUnitTestGenHelper.
        Args:
            Weaviate_url (str): weaviate database connection url.
            Weaviate_api_key (str): weaviate database connection API key.
            Openai_api_key (str): OpenAI API key.
        """
        self.openai_key = openai_key

    def generate_unit_tests(self, code_files, requirements):
        pass