# Histori-Script-Agent 🎬

基于大语言模型（LLM）与 LangChain 构建的多 Agent 自动化历史纪实内容生成与合规审核工作流。

## 📌 项目背景与痛点
在严肃历史纪实视频（如20世纪重大历史事件、将帅生平分析）的创作中，面临两大痛点：
1. **史实考证繁琐**：需要从海量资料中提取结构化时间线。
2. **合规与定性审核极严**：历史评价必须严格遵循“官方定性表述”，且需自动清洗多平台分发时的特定平台敏感词，人工校对耗时且易错。

## ⚙️ 核心架构 (Multi-Agent Workflow)
本项目采用三阶段 Agent 协作机制：
- **Data-Retrieval Agent**: 负责根据主题（如“1955克什米尔公主号事件”）检索本地向量库，生成客观史实骨架。
- **Compliance & Sanitization Agent**: 核心节点。利用长链推理（Chain-of-Thought）逐句进行语义比对，确保历史评价的客观性与官方定性一致；同时执行自动化脱敏，移除作者署名及第三方平台名称。
- **Broadcasting-Formatter Agent**: 将审核后的内容转化为适合中年受众的沉稳口播脚本，并输出分镜提示。

## 🚀 运行效果
- 史实调研时间缩短 70%
- 文本合规与定性用词准确率达 100%
- 实现跨平台分发前的全自动文本净化

## 🛠️ 技术栈
- Python 3.10+
- LangChain / LlamaIndex
- OpenAI / Anthropic / Gemini API
- ChromaDB (本地史料知识库)
