import yaml
from langchain.prompts import PromptTemplate

class ComplianceAgent:
    def __init__(self, config_path="config/rules.yaml"):
        with open(config_path, 'r', encoding='utf-8') as file:
            self.rules = yaml.safe_load(file)
            
    def audit_content(self, raw_script: str, llm_client) -> str:
        """
        执行长链推理，核对官方定性表述并清理平台敏感信息。
        """
        prompt = PromptTemplate(
            input_variables=["script", "platforms"],
            template="""
            你是一个严谨的历史内容合规审核专家。请对以下脚本执行两步操作：
            
            1. 语境与定性校对：确保所有历史人物和事件的评价采用中立、客观的官方定性表述，修正任何偏激或非官方的修辞。
            2. 平台脱敏：强制移除文本中所有的作者自称、署名，以及以下第三方平台名称：{platforms}。
            
            待审核脚本：
            {script}
            
            请直接输出审核并重写后的最终安全脚本。
            """
        )
        
        # 提取需要屏蔽的平台列表
        platforms = ", ".join(self.rules['sanitization_rules']['blacklisted_platforms'])
        
        print("[Log] ComplianceAgent: Initiating official phrasing audit and platform sanitization...")
        # 模拟调用 LLM (实际中替换为 invoke/generate)
        response = llm_client.invoke(prompt.format(script=raw_script, platforms=platforms))
        
        return response
