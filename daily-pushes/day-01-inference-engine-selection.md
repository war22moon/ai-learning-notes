---
title: "推理引擎选型：vLLM vs SGLang vs TensorRT-LLM（推理成本=商业成本）"
day: "Day 1"
date: 2026-06-16
time: 18:03
timezone: Asia/Shanghai
tags:
  - "推理引擎"
  - "vLLM"
  - "SGLang"
  - "TensorRT-LLM"
  - "推理成本"
  - "TCO"
---

# 推理引擎选型：vLLM vs SGLang vs TensorRT-LLM（推理成本=商业成本）

**Day 1** ｜ 2026-06-16 18:03（Asia/Shanghai）

标签：`推理引擎` `vLLM` `SGLang` `TensorRT-LLM` `推理成本` `TCO`

## 为什么今天要懂它

对售前/产品/项目管理来说，LLM“能不能规模化落地”往往不是模型能力，而是推理成本与 SLA。推理引擎选型会直接影响吞吐、延迟、需要多少 GPU，以及最终毛利率。YOMXXX 的对比指出：推理已成为企业 AI 算力支出的大头，且同卡同模不同引擎吞吐可能差约三成，等价于 GPU 数量与月账单差三成（[YOMXXX](https://yomxxx.com/posts/2026-06-04-llm-inference-engine-comparison-2026-tools)）。

## 一句话解释

推理引擎就是“把模型变成可对外提供 API 的生产线”，它决定你每秒能产出多少 token、p95 延迟能否达标，以及每百万 token 的真实成本。

## 核心概念（面向业务的四个指标）

1) **吞吐（tokens/s）**：单位 GPU 能服务多少并发/多少批量任务。
2) **延迟（尤其 p95）**：能否做实时对话/客服/交互式 Copilot。
3) **资源效率（显存 / KV cache / 批处理）**：同一张卡能挂多少会话。
4) **成本口径**：别只看“GPU 每小时单价”，要看“每百万 token 成本”。NVIDIA 强调 **cost per token** 是推理 TCO 的关键指标，并给出 Blackwell 相对 Hopper 的对比表（[NVIDIA AI Inference](https://www.nvidia.com/en-us/solutions/ai/inference/)）。

## 产业链/玩家/产品动态（你需要认识的 5 个选项）

- **vLLM**：生态最大、OpenAI 兼容接口开箱即用，适合作为生产默认起点（[YOMXXX](https://yomxxx.com/posts/2026-06-04-llm-inference-engine-comparison-2026-tools)）。
- **SGLang**：主打吞吐；YOMXXX 举例 H200 上吞吐可比 vLLM 高约 **33%**（[YOMXXX](https://yomxxx.com/posts/2026-06-04-llm-inference-engine-comparison-2026-tools)）。适合高并发、批处理、离线生成等“吞吐=钱”的场景。
- **TensorRT-LLM**：NVIDIA 系极致优化，强调高负载下 p95 延迟与性能，但需要编译/调参、锁定 NVIDIA 生态（[YOMXXX](https://yomxxx.com/posts/2026-06-04-llm-inference-engine-comparison-2026-tools)）。
- **Modular MAX**：面向异构硬件（CUDA/ROCm/Metal）的编译路线，适合想摆脱单一硬件锁定的团队（[YOMXXX](https://yomxxx.com/posts/2026-06-04-llm-inference-engine-comparison-2026-tools)）。
- **llama.cpp**：本地/边缘/消费级设备与量化生态强，适合端侧与私有化轻量部署（[YOMXXX](https://yomxxx.com/posts/2026-06-04-llm-inference-engine-comparison-2026-tools)）。

## 典型服务/商业模式怎么受影响

- **按量计费 API / 企业 SaaS**：吞吐提升≈单位 GPU 收入上限提升；p95 延迟降低≈更高定价能力。
- **私有化交付/项目制**：vLLM 更稳交付风险低；TensorRT-LLM/SGLang 更“性能工程”，但可能显著降低硬件预算。
- **AI 工厂/算力运营**：报价建议从“每卡小时”转为“每百万 token 成本 + SLA”，因为 NVIDIA 也用这一口径解释 Blackwell 的经济性（[NVIDIA AI Inference](https://www.nvidia.com/en-us/solutions/ai/inference/)）。

## 对云服务/云游戏/AI 创业的启发

- 云游戏本质是“延迟+吞吐”生意：若做实时语音/NPC/陪玩/生成式剧情，**p95 延迟**是体验红线；离线内容生成/UGC 工具则吞吐为王。
- 创业早期建议：先用 **vLLM** 跑通业务与数据闭环，再用真实流量压测决定是否切 **SGLang（吞吐瓶颈）**或评估 **TensorRT-LLM（硬 SLA 延迟瓶颈）**（[YOMXXX](https://yomxxx.com/posts/2026-06-04-llm-inference-engine-comparison-2026-tools)）。
- 当新硬件持续压低“每百万 token 成本”时，产品侧要同步升级为更长上下文、更强推理、多代理流程，才能把省下的成本转成体验或价格优势（[NVIDIA AI Inference](https://www.nvidia.com/en-us/solutions/ai/inference/)）。

## 术语卡片（5 个）

- **Continuous Batching（连续批处理）**：动态拼批提高 GPU 利用率（vLLM 关键能力之一）（[YOMXXX](https://yomxxx.com/posts/2026-06-04-llm-inference-engine-comparison-2026-tools)）。
- **KV Cache**：注意力机制“历史记忆”缓存，显存大户，决定并发上限。
- **p95 延迟**：95% 请求都能满足的延迟上界，决定交互体验与 SLA。
- **Cost per Token**：每生成单位 token 的综合成本，适合做 TCO 与定价口径（[NVIDIA AI Inference](https://www.nvidia.com/en-us/solutions/ai/inference/)）。
- **推理 TCO**：推理总拥有成本（GPU、网络、运维、软件栈效率等）（[NVIDIA AI Inference](https://www.nvidia.com/en-us/solutions/ai/inference/)）。

## 今日行动建议（15–30 分钟）

1) 用一句话写清你的业务“瓶颈优先级”：**吞吐优先**还是**延迟优先**？
2) 画一个简单决策树：先 vLLM 上线→压测→吞吐瓶颈切 SGLang / 延迟硬 SLA 评估 TensorRT-LLM（参考 [YOMXXX](https://yomxxx.com/posts/2026-06-04-llm-inference-engine-comparison-2026-tools)）。
3) 把你当前/目标的计费口径改成“三指标”：**每百万 token 成本 + p95 延迟 + 并发上限**，不再只盯 GPU 小时单价。

## 延伸阅读

- 推理引擎横评与决策树（[YOMXXX](https://yomxxx.com/posts/2026-06-04-llm-inference-engine-comparison-2026-tools)）
- NVIDIA 以 cost per token 解释推理经济学与 Blackwell 指标（[NVIDIA AI Inference](https://www.nvidia.com/en-us/solutions/ai/inference/)）

## 来源链接

- [YOMXXX：推理引擎横评](https://yomxxx.com/posts/2026-06-04-llm-inference-engine-comparison-2026-tools)
- [NVIDIA AI Inference](https://www.nvidia.com/en-us/solutions/ai/inference/)

---

[返回归档索引](README.md) ｜ [返回仓库首页](../README.md)
