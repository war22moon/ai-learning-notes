# 100天AI行业学习推送归档

> 本归档由应用内每日学习推送记录自动生成，请勿手动编辑生成文件。
> 如需重建，请运行 `python scripts/init_daily_push_archive.py`。

每日 AI 行业学习推送的结构化归档数据，由 scripts/init_daily_push_archive.py 读取并生成 daily-pushes/ 下的独立 Markdown 页面与索引。

## 推送索引

| Day | 时间 | 主题 | 标签 | 链接 |
|---|---|---|---|---|
| Day 1 | 2026-06-16 18:03 | 推理引擎选型：vLLM vs SGLang vs TensorRT-LLM（推理成本=商业成本） | 推理引擎、vLLM、SGLang、TensorRT-LLM、推理成本、TCO | [推理引擎选型：vLLM vs SGLang vs TensorRT-LLM（推理成本=商业成本）](day-01-inference-engine-selection.md) |
| Day 2 | 2026-06-17 09:04 | MCP v2（Model Context Protocol）为何从“集成便利”走向“生产基础设施” | MCP、MCP v2、Stateless core、OAuth、Agent、工具调用 | [MCP v2（Model Context Protocol）为何从“集成便利”走向“生产基础设施”](day-02-mcp-v2-production-infrastructure.md) |
| Day 3 | 2026-06-17 18:08 | AI Gateway（以 Envoy AI Gateway 为例）：把多模型调用、MCP 工具流量、安全与可观测做成平台能力 | AI Gateway、Envoy AI Gateway、多模型路由、可观测、MCP、多租户 | [AI Gateway（以 Envoy AI Gateway 为例）：把多模型调用、MCP 工具流量、安全与可观测做成平台能力](day-03-envoy-ai-gateway-platform.md) |
| Day 4 | 2026-06-17 22:09 | AI Gateway v0.7.0（以 Envoy AI Gateway 为例）：用 hostname 路由 + 配额 + 授权，把多模型与工具流量做成平台能力 | AI Gateway、Envoy AI Gateway、v0.7.0、hostname 路由、QuotaPolicy、SSE | [AI Gateway v0.7.0（以 Envoy AI Gateway 为例）：用 hostname 路由 + 配额 + 授权，把多模型与工具流量做成平台能力](day-04-envoy-ai-gateway-v0-7-0.md) |
| Day 5（上午） | 2026-06-18 09:04 | Token成本治理三板斧：Prompt Caching + Batch API + 模型路由（从“省钱”走向“可运营”） | Token 成本、Prompt Caching、Batch API、模型路由、FinOps、成本治理 | [Token成本治理三板斧：Prompt Caching + Batch API + 模型路由（从“省钱”走向“可运营”）](day-05-token-cost-governance-three-levers.md) |
| Day 5（傍晚） | 2026-06-18 18:03 | 把限流与成本治理做成平台能力：Rate limits + Usage/Cost API（以 Anthropic 为例） | Rate limits、Spend limits、Token bucket、Usage Report、Cost Report、Anthropic | [把限流与成本治理做成平台能力：Rate limits + Usage/Cost API（以 Anthropic 为例）](day-05-rate-limits-usage-cost-api-anthropic.md) |
| Day 5（晚间） | 2026-06-18 22:12 | “Spend Limit”不是限流：把成本预算做成 AI Gateway 的第一公民（以 Cloudflare AI Gateway 为例） | Spend limit、AI Gateway、Cloudflare、预算、成本治理、Metadata | [“Spend Limit”不是限流：把成本预算做成 AI Gateway 的第一公民（以 Cloudflare AI Gateway 为例）](day-05-spend-limit-cloudflare-ai-gateway.md) |

## 说明

- 时间均为 Asia/Shanghai 时区。
- 每篇页面保留学习笔记的原始结构（为什么今天要懂它 / 一句话解释 / 核心概念 / 术语卡片 / 今日行动建议等），并附来源链接。
- 部分早期推送引用了未来日期的材料或存在同日选题重复，相关情况已在对应页面顶部以“说明”标注，未做静默改写。

[返回仓库首页](../README.md)
