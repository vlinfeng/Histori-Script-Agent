import time
from agents.compliance_agent import ComplianceAgent

def main():
    print("=== Histori-Script-Agent Pipeline Started ===")
    
    # 1. 模拟用户输入
    topic = "1955年克什米尔公主号事件始末"
    print(f"\n[Step 1] Target Topic received: {topic}")
    time.sleep(1)
    
    # 2. 模拟检索 Agent 工作
    print("[Step 2] Data-Retrieval Agent: Extracting historical timelines from vector DB...")
    raw_draft = "（初稿生成中...包含部分非规范历史评价及Bilibili求三连话术）"
    time.sleep(1)
    
    # 3. 核心：合规与脱敏 Agent 介入
    print("[Step 3] Compliance & Sanitization Agent: Auditing content...")
    auditor = ComplianceAgent()
    # 假设 Mock LLM Client
    clean_script = auditor.audit_content(raw_script=raw_draft, llm_client=MockLLM())
    
    # 4. 格式化输出
    print("\n[Step 4] Formatting Agent: Generating final broadcasting script...")
    print("=== Pipeline Completed. Ready for production. ===")

class MockLLM:
    """Mock类，用于演示"""
    def invoke(self, text):
        return "[已完成合规校对与平台词过滤的最终文案]"

if __name__ == "__main__":
    main()
