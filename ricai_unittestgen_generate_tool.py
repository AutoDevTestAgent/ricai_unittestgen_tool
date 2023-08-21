from typing import Type
from pydantic import BaseModel, Field
from superagi.tools.base_tool import BaseTool
from ricai_unittestgen_helper import RicaiUnitTestGenHelper

class RicaiUnitTestGenGenerateSchema(BaseModel):
    code_files: str = Field(..., description="The code to cover with unit tests")
    requirements: str = Field(..., description="The software requirements (business logic) to use for testing")

class RicaiUnitTestGenGenerateTool(BaseTool):
    """
    RicAI genereate unit tests tool

    Attributes:
        name : The name.
        description : The description.
        args_schema : The args schema.
    """
    name = "RicaiUnitTestGenGenerate"
    description = (
        "A tool for updating the code database with latest code from Github."
    )
    args_schema: Type[BaseModel] = RicaiUnitTestGenGenerateSchema

    class Config:
        arbitrary_types_allowed = True
    
    def _execute(self, code_files: str, requirements: str):
        """
        Execute the RicAI genereate unit tests tool.

        Args:
            code_files: The code to cover with unit tests
            requirements: The software requirements (business logic) to use for testing

        Returns:
            The unit test code. or error message.
        """
        try:
            openai_key = self.get_tool_config("OPENAI_API_KEY")
            
            ricai_unittestgen_helper = RicaiUnitTestGenHelper(openai_key=openai_key)                        
            result = ricai_unittestgen_helper.generate_unit_tests(code_files, requirements)
            return f'Unit tests generated successfully: {result}'
        except Exception as err:
            return f"Error: Unable to generate unit tests for the code - {err}"