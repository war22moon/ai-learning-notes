# AI 行业入门学习手册：第 1 周

适用对象：售前解决方案经理、产品经理、项目经理、云服务/云游戏业务从业者  
整理时间：2026-06-18  
学习目标：用非算法工程师也能理解的方式，建立 AI API、模型服务、网关治理、推理基础设施、成本与 SLA 的第一层知识框架。

---

## 使用说明

这本小册子整理了最近一周围绕 AI 行业入门展开的学习内容。它不是论文式技术笔记，而是面向你日常工作可复用的“售前/产品/交付知识框架”。

建议阅读方式：

- 先读每章的“一句话理解”。
- 再看“售前/产品视角”。
- 最后用“可追问问题”检查自己是否真的理解。

---

# 第一章：模型服务的基本链路

## 一句话理解

大模型服务不是“一个模型名字”这么简单，而是一条从硬件、软件栈、模型资产、推理引擎到 API 服务的完整链路。

典型链路：

```text
GPU / NPU
  ↓
驱动与底层计算栈：CUDA / CANN
  ↓
开发框架：PyTorch / Transformers
  ↓
模型资产：权重 + 配置 + Tokenizer + Chat Template
  ↓
推理引擎：vLLM / SGLang / TensorRT-LLM / MindIE
  ↓
模型服务 API：OpenAI-compatible API / MaaS API
  ↓
业务应用：Chatbot / Agent / 知识库 / 代码助手 / 售前工具
```

## 模型资产是什么

模型资产是让一个模型能够被加载、运行、管理和交付的一整套物料包。它通常包括：

- 模型权重：模型真正学到的参数。
- 模型结构配置：层数、隐藏维度、Attention 结构、MoE 配置等。
- Tokenizer：把文字切成 token，再把 token 还原成文字。
- Chat Template：模型对话格式，例如 system/user/assistant 怎么组织。
- 量化版本：FP16、BF16、INT8、4bit 等不同精度。
- License：是否允许商用、私有化、再分发或微调。

## DeepSeek、Qwen、Claude 的不同形态

平时说 DeepSeek、Qwen、Claude，可能是在说品牌、模型家族、具体模型、模型资产或模型服务。

| 名称 | 常见形态 | 你需要注意什么 |
|---|---|---|
| DeepSeek | 可下载模型资产 + API 服务 | 既可私有化部署，也可调用官方/第三方 API |
| Qwen | 可下载模型资产 + 阿里云模型服务 | 开源模型与云服务并存 |
| Claude | API 模型服务为主 | 通常拿不到权重，不能自己用 vLLM 部署 |
| GPT | API 模型服务为主 | 通常通过 OpenAI、Azure 等 API 调用 |
| Llama | 可下载模型资产 | 更适合本地/私有化/开源生态部署 |

## 开发框架、模型资产、推理引擎的关系

一句话：

> 开发框架生产或处理模型资产，推理引擎加载模型资产并把它变成模型服务。

| 层级 | 代表 | 作用 |
---|---|---|
| 开发框架 | PyTorch、Transformers、DeepSpeed | 训练、微调、导出模型 |
| 模型资产 | DeepSeek-R1-Distill-Qwen-32B 等 | 可部署的模型物料包 |
| 推理引擎 | vLLM、SGLang、TensorRT-LLM | 高效加载模型，对外提供 API |
| 模型服务 | OpenAI-compatible API | 业务系统真正调用的接口 |

## 售前/产品视角

客户问“你们支持 DeepSeek 吗”时，不要只回答“支持”。更专业的追问是：

- 支持哪个版本，满血版还是蒸馏版？
- 是调用官方 API，还是私有化部署模型资产？
- 用什么推理引擎部署？
- 支持多长上下文？
- P95 延迟是多少？
- 单实例吞吐是多少？
- 是否支持流式输出、工具调用和 OpenAI 兼容接口？

---

# 第二章：NVIDIA 生态链路

## 一句话理解

NVIDIA 生态可以理解成“AI 推理生产线”：GPU 提供算力，CUDA 让软件调用 GPU，PyTorch 处理模型，vLLM/SGLang/TensorRT-LLM 把模型变成 API 服务。

## 核心组件

| 组件 | 通俗理解 | 主要工作 |
---|---|---|
| NVIDIA GPU | 厨房里的高级炉灶 | 提供 AI 计算能力 |
| CUDA | 炉灶操作系统 | 让软件高效调用 GPU |
| PyTorch | 模型工程师的工作台 | 训练、微调、加载模型 |
| 模型资产 | 已经训练好的“菜谱和参数” | 被推理引擎加载 |
| vLLM | 通用生产推理引擎 | 快速把模型变成 API |
| SGLang | 高吞吐/Agent 友好推理引擎 | 复杂 Agent、结构化生成、高并发 |
| TensorRT-LLM | NVIDIA 官方深度优化路线 | 极致性能，但工程复杂 |

## 三种推理引擎的选型口径

| 推理引擎 | 适合场景 | 售前表达 |
---|---|---|
| vLLM | 快速上线、通用模型 API 平台 | 生态成熟，上手快，适合作为默认生产起点 |
| SGLang | 高吞吐、复杂 Agent、多步推理 | 适合吞吐优先和复杂工作流场景 |
| TensorRT-LLM | 极致延迟和吞吐要求 | 性能强，但需要更多模型转换和调优 |

## 和国产昇腾生态的对照

| NVIDIA 生态 | 昇腾生态大致对应 |
---|---|
| NVIDIA GPU | 昇腾 NPU |
| CUDA | CANN |
| NCCL | HCCL |
| PyTorch CUDA | PyTorch NPU / torch_npu |
| TensorRT-LLM | MindIE / 昇腾推理栈 |
| vLLM | vLLM-Ascend |
| nvidia-smi | npu-smi |

## 售前/产品视角

如果客户问为什么 NVIDIA 生态成熟，可以这样回答：

> NVIDIA 方案的优势在于 CUDA 生态成熟，PyTorch、vLLM、SGLang、TensorRT-LLM 等工具链完善，模型适配快，社区资料多，适合快速部署和持续优化大模型推理服务。

---

# 第三章：国产芯片、昇腾和平头哥

## 一句话理解

国产芯片跑 DeepSeek 已经从“能不能跑”进入“跑得好不好、成本低不低、交付稳不稳”的阶段。

## 昇腾方案怎么理解

昇腾的价值不只是芯片，而是一整套华为 AI 软硬件栈：

- 昇腾 NPU：硬件算力。
- CANN：底层异构计算架构，类似 NVIDIA CUDA。
- MindIE：大模型推理引擎。
- vLLM-Ascend：将开源 vLLM 适配到昇腾。
- HCCL：多卡通信能力。
- npu-smi：设备管理和监控工具。

## “国产化和交付确定性强”是什么意思

这句话不是说昇腾一定性能最高，而是说它在政企、运营商、金融、央国企等场景里更容易形成完整交付闭环：

- 国产化属性明确。
- 供应商和生态集成商体系完整。
- 可做云服务、私有化、一体机、行业方案。
- 采购、部署、验收、运维、售后责任边界更清楚。

## “需要吃透 CANN/MindIE/vLLM-Ascend”是什么意思

如果团队原来只熟悉 NVIDIA 的 CUDA + PyTorch + vLLM，迁移到昇腾时需要重新理解：

- 模型是否适配昇腾。
- CANN、torch_npu、驱动、镜像版本是否匹配。
- 该用 MindIE 还是 vLLM-Ascend。
- 多卡通信 HCCL 怎么配置。
- Attention、MoE、KV Cache、量化算子是否优化。
- 性能不达标时如何 profile 和调参。

## 平头哥怎么理解

平头哥相关芯片更适合放在阿里云生态内理解。公开信息显示其新一代 AI 芯片和阿里云百炼、通义千问等服务结合较深。对外部团队来说，更多感知可能是“阿里云模型服务的底层算力”，而不是直接采购芯片私有化部署。

## 售前/产品视角

不要把国产芯片方案卖成“买几张卡就能跑 DeepSeek”。更准确的表达是：

> 需要以芯片 + 底层软件栈 + 推理引擎 + 模型适配 + 性能调优 + 监控运维 + 生态服务商作为整体方案交付。

---

# 第四章：算子与模型内部结构

## 一句话理解

模型是客户看到的 AI 能力，算子是模型在芯片上真正执行的底层计算动作。

## 模型里的关键算子

| 算子 | 形象理解 | 它做什么 |
---|---|---|
| Embedding | 语义身份证 | 把文字变成数字向量 |
| Attention | 聚光灯/侦探 | 找出当前最相关的上下文 |
| MLP | 分析加工车间 | 对信息做深度加工和推理 |
| Norm | 校准器/质检员 | 保持每层计算稳定 |
| MoE | 专家分诊系统 | 按任务选择部分专家参与计算 |

## Embedding

Embedding 负责把文字、代码或符号转换成模型能处理的数字向量。

形象理解：

> Embedding 像给每个词发一张语义身份证。模型不直接看汉字，而是看身份证上的数字特征。

## Attention

Attention 负责判断当前生成内容时应该重点关注前文哪些信息。

形象理解：

> Attention 像会议主持人或侦探，在大量上下文中找出最相关的线索。

## MLP

MLP 负责把信息进一步加工成判断、推理和表达。

形象理解：

> Attention 像资料检索员，MLP 像分析师。前者找资料，后者形成结论。

## Norm

Norm 负责让模型每一层计算保持稳定，避免内部数字越来越大或越来越小。

形象理解：

> Norm 像工厂里的质检和校准环节。

## MoE

MoE 是混合专家模型。它不是每次激活整个模型，而是让路由器选择部分专家处理当前任务。

形象理解：

> MoE 像医院分诊台，不是让全医院医生都看病，而是根据病情分配给对应科室。

## 和芯片适配的关系

模型适配芯片，本质上就是让这些算子在目标硬件上正确、高效运行。

如果 Attention 优化不好，长上下文就慢。  
如果 MLP 矩阵计算性能差，整体吞吐就低。  
如果 MoE 路由和多卡通信差，DeepSeek 这类 MoE 模型就难跑好。

---

# 第五章：MCP

## 一句话理解

MCP 是让 AI 应用连接外部系统的标准协议，可以理解为 AI 应用的“USB-C 接口”。

MCP 官方介绍是一个开源标准，用来把 AI 应用连接到外部系统，例如本地文件、数据库、搜索工具、业务系统和工作流。参考：[MCP 官方入门文档](https://modelcontextprotocol.io/docs/getting-started/intro)。

## MCP 的核心角色

| 角色 | 通俗理解 | 作用 |
---|---|---|
| Host | AI 应用本体 | 如 Claude Desktop、Cursor、Agent 平台 |
| Client | Host 内部连接组件 | 负责连接某个 MCP Server |
| Server | 外部系统能力封装 | 暴露工具、资源、Prompt |

## MCP Server 的三类能力

| 能力 | 中文理解 | 示例 |
---|---|---|
| Tools | 让 AI 做事 | 创建工单、查询订单、调用封禁接口 |
| Resources | 让 AI 看资料 | 读取知识库、日志、数据库记录 |
| Prompts | 一键发起流程 | 总结会议、生成售前方案、分析故障日志 |

参考：[MCP Server 概念文档](https://modelcontextprotocol.io/docs/learn/server-concepts)。

## 对你的工作有什么价值

如果模型聚合平台未来要进入客户业务系统，MCP 可以成为一种“连接器产品”：

- 连接企业知识库。
- 连接工单系统。
- 连接 CRM。
- 连接监控平台。
- 连接云游戏运营后台。
- 连接模型聚合平台的 Key、余额、用量、模型目录。

## 售前表达

> MCP 不是模型本身，而是 AI 应用调用企业工具和读取企业上下文的标准连接协议。它解决的是 Agent 如何安全、标准化、可治理地进入业务系统的问题。

---

# 第六章：AI Gateway 与 Token 中转站

## 一句话理解

AI Gateway 是面向模型与工具调用的网关层，负责统一入口、协议转换、路由、鉴权、限流、审计、观测和成本治理。

## AI Gateway 做什么

| 能力 | 作用 |
---|---|
| 统一入口 | 业务只接一个 Base URL |
| 协议转换 | OpenAI、Anthropic、Gemini、Bedrock 等格式互转 |
| 模型路由 | 按租户、场景、成本、延迟选择模型 |
| 限流配额 | 控制 RPM、TPM、预算 |
| 可观测 | 记录 token、延迟、错误率、流式中断 |
| 安全治理 | API Key、权限、工具可见性、审计 |

## Envoy AI Gateway 为什么被讲到

Envoy AI Gateway 被选为案例，不代表它一定是同类最好或最广泛使用，而是因为它适合说明传统云原生网关如何演进到 AI Gateway。

Envoy 本身是 CNCF Graduated 项目，定位是高性能代理/网关基础设施。参考：[CNCF Envoy](https://www.cncf.io/projects/envoy/)。

Envoy AI Gateway 的能力包括模型虚拟化、provider fallback、usage-based rate limiting、MCP Gateway、metrics 等。参考：[Envoy AI Gateway Capabilities](https://aigateway.envoyproxy.io/docs/0.7/capabilities/)。

## Token 中转站是不是 AI Gateway

技术上有重叠，但定位不同。

| 类型 | 更偏什么 |
---|---|
| Token 中转站 | 转发、充值、额度、低成本调用 |
| API 聚合平台 | 多模型统一接入、模型目录、计费 |
| AI Gateway | 企业级治理、安全、审计、观测、SLA |
| MaaS/模型服务平台 | 模型供应、托管推理、商业 SLA |

## 中转站常用的开源项目

国内很多中转站会基于开源项目搭建或二次开发，例如：

- One API：常见的开源模型接口管理与分发工具。
- New API：基于 One API 演进，支持更多协议、用户体系、计费和管理能力。
- LiteLLM：国际常见 LLM Gateway，支持虚拟 Key、预算、成本跟踪、回退和负载均衡。

One API / New API 常见能力包括上游渠道接入、API 令牌管理、额度控制、分组和模型权限管理、后台管理面板。参考：[One API Docker 部署实战](https://gitcode.csdn.net/6a1e524410ee7a33f2770931.html)、[New API 项目介绍](https://gitcode.com/markho/new-api)。

## 售前表达

如果客户问“你们是不是 token 中转站”，可以回答：

> 简单中转站主要解决低成本调用和统一入口，而企业级 AI Gateway/模型聚合平台解决的是多模型治理、成本可控、权限审计、安全合规、SLA 和可运维交付。

---

# 第七章：Token 计费与成本治理

## 一句话理解

按 token 计费时，真正要管理的不是“模型单价”，而是每个业务任务消耗多少 token、产生多少价值、能不能稳定控制在可盈利区间内。

## 基础计费公式

```text
总成本 = 输入 token × 输入单价 + 输出 token × 输出单价
```

通常输出 token 比输入 token 更贵，因为输出需要模型逐 token 生成，占用推理时间更长。

## 需要关注的计费折算逻辑

| 维度 | 为什么重要 |
---|---|
| 输入/输出分开计费 | 输出通常更贵 |
| 上下文长度 | system prompt、历史对话、RAG 文档都算输入 |
| 多轮对话 | 历史越长，输入 token 越滚越大 |
| Agent 步数 | 一个任务可能触发多次模型调用 |
| 工具返回 | 工具结果塞回模型也会成为输入 token |
| 重试 | 失败重试会放大成本 |
| cached tokens | 缓存命中可能降低输入成本 |
| reasoning tokens | 部分模型会额外计推理 token |

## Token 成本治理三板斧

### Prompt Caching

Prompt Caching 用于复用相同提示词前缀，降低重复输入成本。OpenAI 文档说明缓存会自动启用，适用于提示词达到 1024 tokens 及以上的请求，并依赖精确前缀匹配。参考：[OpenAI Prompt Caching 文档](https://developers.openai.com/api/docs/guides/prompt-caching)。

### Batch API

Batch API 适合不需要即时响应的任务，例如批量摘要、分类、打标签、离线报告生成。OpenAI Batch API 支持异步提交 JSONL 请求，并在 24 小时内返回结果，适合批处理场景。参考：[OpenAI Batch API 文档](https://platform.openai.com/docs/guides/batch/batch-api)。

### 模型路由

模型路由的核心是 Rightsizing：不要用旗舰模型解决所有问题，而是按任务难度、风险、实时性选择合适模型。

| 任务 | 推荐策略 |
---|---|
| 简单分类/摘要 | 便宜模型 |
| 复杂推理/高风险决策 | 强模型 |
| 离线批量任务 | Batch |
| 高频重复提示词 | Prompt Caching |
| 长上下文文档分析 | 长上下文模型 + 成本限制 |

## 售前表达

> 我们不只提供模型调用，还提供 token 成本治理能力，包括用量计量、预算限制、缓存命中率、批处理占比、模型路由策略和按租户成本报表。

---

# 第八章：流式、非流式与性能指标

## 流式和非流式

| 返回方式 | 通俗理解 | 适合场景 |
---|---|---|
| 非流式 | 答案生成完一次性返回 | 批量分类、后台摘要、短文本任务 |
| 流式 | 一边生成一边返回 | 聊天、代码助手、实时 Agent |

流式通常通过 SSE（Server-Sent Events）实现，用户看到文字逐步出现。

## 流式对指标的影响

流式需要特别关注：

- TTFT：首 token 延迟。
- tokens/s：输出速度。
- 流式中断率。
- 最后 usage 是否准确返回。
- 用户主动停止生成后的计费。

## P90、P95、P99

P95 延迟表示：

> 95% 的请求都能在这个时间以内完成，剩下最慢的 5% 比它更慢。

| 指标 | 含义 | 适用 |
---|---|---|
| P50 | 一半请求比它快 | 典型体验 |
| P90 | 90% 请求比它快 | 大多数用户体验 |
| P95 | 95% 请求比它快 | 常用于 SLA |
| P99 | 99% 请求比它快 | 极端尾部风险 |

## AI API 常见性能指标

| 指标 | 解释 |
---|---|
| TTFT | 从请求到第一个 token 返回 |
| Total Latency | 从请求到完整响应结束 |
| tokens/s | 输出速度 |
| RPM | 每分钟请求数 |
| TPM | 每分钟 token 数 |
| 并发数 | 同时处理的请求数量 |
| 错误率 | 5xx、429、超时等 |
| 流式中断率 | 已开始输出但中途断开 |

## 售前表达

> AI 服务不能只看平均响应时间，应该看 P95 首 token 延迟、P95 完整响应、TPM、RPM、并发、错误率和流式中断率。P95 比平均值更能代表大多数客户的真实体验。

---

# 第九章：限流、配额与用量账本

## 一句话理解

企业级模型平台必须同时管理“调用上限”和“事后账本”：前者控制风险，后者支撑核算和对账。

## 两类限制

| 类型 | 中文理解 | 作用 |
---|---|---|
| Spend limits | 花费上限 | 控制预算 |
| Rate limits | 调用速率上限 | 控制容量 |

Anthropic 官方文档区分了 Spend limits 和 Rate limits，并说明服务端会在组织层生效，也可按 Workspace 配置自定义限制。参考：[Anthropic Rate Limits](https://docs.anthropic.com/en/api/rate-limits)。

## 常见限流维度

| 维度 | 含义 |
---|---|
| RPM | 每分钟请求数 |
| ITPM | 每分钟输入 token 数 |
| OTPM | 每分钟输出 token 数 |
| TPM | 每分钟总 token 数 |
| 并发数 | 同时处理请求数 |
| 预算 | 月度或项目花费上限 |

## Token Bucket

Token bucket 是一种限流算法，可以理解为一个持续补水的桶：

- 每次请求消耗桶里的额度。
- 桶会持续补充到上限。
- 不是每个整点一次性清零。

如果短时间突发太高，即使分钟级限额看起来没超，也可能触发 429。

## 用量和成本 API

Usage Report 是调用事实表，Cost Report 是成本账本。Anthropic 提供 Usage Report 和 Cost Report，用于按模型、工作区、服务层等拆分 token 消耗和成本。参考：[Anthropic 使用量和成本 API](https://docs.anthropic.com/zh-CN/api/usage-cost-api)。

## 售前表达

> 我们建议把配额体系分成组织、工作区、项目、API Key 四层，每层都能设置预算、RPM、TPM、模型白名单和告警阈值。这样客户可以把 AI 成本从“黑盒账单”变成“可分摊、可审计、可对账”的平台能力。

---

# 第十章：AI API SLA 模板

## 一句话理解

AI API SLA 的核心不是把指标写得越高越好，而是把“什么条件下承诺、怎么统计、超了怎么补偿、哪些情况排除”写清楚。

## SLA 指标总览

| 指标类别 | 建议指标 | 适用意义 |
---|---|---|
| 可用性 | 月度可用性 99.5% / 99.9% / 99.95% | 服务是否稳定在线 |
| P95 TTFT | 首 token 延迟 | 交互体感 |
| P95 完整响应 | 总响应时间 | 完整回答速度 |
| 吞吐量 | RPM / TPM / 并发 | 承载能力 |
| 错误率 | 5xx、超时、429 等 | 平台稳定性 |
| 流式中断率 | 流式响应异常中断比例 | 对话体验 |
| 工单响应 | P1/P2/P3 响应时间 | 交付支持能力 |

## SLA 分级

| 等级 | 可用性 | P95 TTFT | 支持 |
---|---|---|---|
| 标准版 | 99.5% | ≤ 5s | 工作日支持 |
| 企业版 | 99.9% | ≤ 3s | 7×12 或 7×24 |
| 政企专属版 | 99.95% | ≤ 1.5s-3s | 7×24 + 专属群 + 应急预案 |

## 补偿机制

建议使用“服务抵扣”而不是“罚款”。

| 月度可用性 | 服务补偿 |
---|---|
| ≥ 99.9% | 无补偿 |
| ≥ 99.5% 且 < 99.9% | 当月服务费 5% 抵扣 |
| ≥ 99.0% 且 < 99.5% | 当月服务费 10% 抵扣 |
| ≥ 95.0% 且 < 99.0% | 当月服务费 20% 抵扣 |
| < 95.0% | 当月服务费 30% 抵扣，并进行专项复盘 |

## 合同条款化表达

关键条款应包括：

- 服务范围。
- 指标定义。
- 有效请求定义。
- 统计周期。
- 数据来源。
- 补偿机制。
- 补偿上限。
- 免责条件。
- 计划维护。
- 客户配合义务。

## 政企客户沟通话术

> AI API 的 SLA 不能只看平均响应时间，我们建议从可用性、P95 延迟、吞吐配额、错误率、流式中断率和故障响应六个维度定义。对于更高 SLA，需要匹配专属资源池、专属模型路由、预留吞吐、故障切换和 7×24 运维机制。

---

# 第十一章：本周概念卡片

## 模型资产

模型的可运行物料包，包括权重、配置、tokenizer、chat template、量化版本和许可证。

## 推理引擎

把模型资产加载到 GPU/NPU，并对外提供高性能 API 服务的软件。

## CUDA

NVIDIA 的底层并行计算平台，让上层框架高效使用 GPU。

## CANN

昇腾的底层异构计算架构，大致对应 NVIDIA 生态里的 CUDA。

## vLLM

通用开源推理引擎，适合快速把模型变成 OpenAI-compatible API。

## SGLang

偏高吞吐和复杂 Agent 工作流的推理引擎。

## TensorRT-LLM

NVIDIA 官方大模型推理优化路线，适合极致性能场景。

## MCP

让 AI 应用连接外部系统的标准协议，提供 Tools、Resources、Prompts。

## AI Gateway

面向模型和工具调用的网关层，负责路由、鉴权、限流、审计、观测和成本治理。

## Token 中转站

模型 API 的轻量中间层，通常做统一入口、Key 管理、充值额度和转发。

## P95

95% 请求都能在这个时间内完成，用于衡量大多数用户体验。

## TTFT

Time To First Token，首 token 延迟。

## TPM

Tokens Per Minute，每分钟 token 数，用于描述 AI 服务吞吐。

## RPM

Requests Per Minute，每分钟请求数。

## Prompt Caching

提示词缓存，用于降低重复前缀输入成本。

## Batch API

异步批处理 API，适合非实时任务。

## MoE

混合专家模型，每次只激活部分专家以平衡能力和成本。

---

# 第十二章：本周最值得复习的 10 个问题

1. DeepSeek、Qwen、Claude 分别可能代表品牌、模型家族、模型资产还是模型服务？
2. 模型资产、开发框架、推理引擎、模型 API 的关系是什么？
3. CUDA + PyTorch + vLLM/SGLang/TensorRT-LLM 分别对应什么工作？
4. 昇腾里的 CANN、MindIE、vLLM-Ascend 分别对应 NVIDIA 生态中的什么角色？
5. Attention、MLP、Norm、MoE、Embedding 分别在模型里起什么作用？
6. MCP 的 Tools、Resources、Prompts 分别是什么？
7. AI Gateway 和 token 中转站的区别是什么？
8. 按 token 计费时，为什么不能只看模型单价？
9. P95、TTFT、TPM、RPM 分别衡量什么？
10. AI API SLA 应该如何写清楚承诺条件、统计口径、补偿机制和免责边界？

---

# 第十三章：下周建议学习路径

## 方向一：模型服务产品化

建议继续学习：

- 模型服务、模型 API、MaaS、模型聚合平台的区别。
- OpenAI-compatible API 为什么重要。
- Base URL、API Key、模型别名、模型映射的产品意义。
- 模型目录、模型白名单、模型权限、模型分组。

## 方向二：企业级 AI Gateway

建议继续学习：

- AI Gateway、API Gateway、MCP Gateway 的区别。
- 虚拟 Key、上游 Key、租户、组织、工作区的关系。
- 路由策略：优先级、权重、回退、按成本路由、按延迟路由。
- 如何做可观测：日志、trace、token usage、cost attribution。

## 方向三：AI 成本与 SLA

建议继续学习：

- 如何把 token 成本映射到客户报价。
- 如何设计试用额度、套餐、阶梯价格和超额计费。
- 如何把 P95 延迟、可用性、吞吐写成 SLA。
- 如何区分平台责任、上游责任、客户侧责任。

## 方向四：芯片与推理基础设施

建议继续学习：

- GPU 显存、KV Cache、上下文长度之间的关系。
- 为什么长上下文贵。
- 为什么 MoE 对多卡通信要求高。
- 国产芯片私有化部署的交付风险清单。

---

# 附录：可直接复用的售前表达

## 关于模型服务

> 我们不只是接入单个模型，而是把多个模型资产和上游模型服务统一成可管理、可计量、可审计的模型服务目录，并通过统一 API 向业务系统提供能力。

## 关于 AI Gateway

> AI Gateway 的价值不是简单转发请求，而是把模型路由、鉴权、配额、成本、审计、观测和故障切换做成平台能力。

## 关于 token 成本

> 模型单价只是成本的一部分，真正要管理的是每个业务任务的总 token 消耗、上下文膨胀、Agent 调用步数、重试损耗和模型路由策略。

## 关于国产化部署

> 国产化 AI 方案需要整体评估芯片、底层软件栈、推理引擎、模型适配、算子优化、多卡通信、监控运维和生态服务商支持，不能只看单卡参数。

## 关于 SLA

> AI API SLA 应该按可用性、P95 延迟、吞吐、错误率、流式中断率和故障响应定义，并明确统计口径、补偿机制和免责条件，避免上线后交付责任不清。

---

# 参考链接

- MCP 官方入门文档：https://modelcontextprotocol.io/docs/getting-started/intro
- MCP Server 概念文档：https://modelcontextprotocol.io/docs/learn/server-concepts
- MCP 架构文档：https://modelcontextprotocol.io/docs/learn/architecture
- CNCF Envoy：https://www.cncf.io/projects/envoy/
- Envoy AI Gateway Capabilities：https://aigateway.envoyproxy.io/docs/0.7/capabilities/
- Envoy AI Gateway Release Notes：https://aigateway.envoyproxy.io/release-notes/
- OpenAI Prompt Caching：https://developers.openai.com/api/docs/guides/prompt-caching
- OpenAI Batch API：https://platform.openai.com/docs/guides/batch/batch-api
- OpenAI API Pricing：https://openai.com/api/pricing/
- Anthropic Rate Limits：https://docs.anthropic.com/en/api/rate-limits
- Anthropic Usage and Cost API：https://docs.anthropic.com/zh-CN/api/usage-cost-api
- One API 部署介绍：https://gitcode.csdn.net/6a1e524410ee7a33f2770931.html
- New API 项目介绍：https://gitcode.com/markho/new-api
- LiteLLM OSS：https://www.litellm.ai/oss

