from abc import ABC
from typing import List

from superagi.tools.base_tool import BaseToolkit, BaseTool
from ricai_unittestgen_generate_tool import RicaiUnitTestGenGenerateTool

class RicaiUnitTestGenToolkit(BaseToolkit, ABC):
    name: str = "RicAI Unit Test Gen Toolkit"
    description: str = "Toolkit containing tools for unit test generation based on provided code and software requirement context"

    def get_tools(self) -> List[BaseTool]:
        return [RicaiUnitTestGenGenerateTool()]

    def get_env_keys(self) -> List[str]:
        return ["OPENAI_API_KEY"]