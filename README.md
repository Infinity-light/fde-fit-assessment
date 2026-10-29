# FDE 适配度测评 Skill

## 一键复制：把这段话发给你手机上的 AI

点下面代码框右上角的复制按钮，粘贴到你手机上常用的 AI 助手里发送即可（能打开网页链接的 AI 都可以）：

```text
请使用 FDE 适配度测评 Skill 对我进行测评。Skill 在这个公开仓库：https://github.com/Infinity-light/fde-fit-assessment
请先完整读取下面三个文件，严格按 SKILL.md 的流程来：
https://raw.githubusercontent.com/Infinity-light/fde-fit-assessment/main/SKILL.md
https://raw.githubusercontent.com/Infinity-light/fde-fit-assessment/main/references/question_bank.md
https://raw.githubusercontent.com/Infinity-light/fde-fit-assessment/main/references/rubric.md
用“快测”节奏：先请我做一句话自我介绍，然后按出题原则结合我的行业现场出题，一次只问一道情境题，分别考 AI 原生思维、产品思维、经营者思维三种思维；中途不要点评、不要透露标准答案。全部问完后，按评分表给出总分（满分 100）、等级、各维度得分和依据，以及我最该补的一项和一条具体建议。现在开始第一题。
```

> 如果你的 AI 打不开链接，就换一个能联网读网页的 AI，或在电脑上用下面的方式安装 Skill。

---

## 这是什么

和你聊 3–10 分钟，判断你现在离一名合格的 FDE（Forward Deployed Engineer，驻场 AI 工程师）还有多远。

一名合格的 FDE 要有三种思维：

| 思维 | 面对谁 | 看什么 |
|---|---|---|
| AI 原生思维 | 面对工程 | 用 AI 重新设计做法，而不是把 AI 塞进旧流程 |
| 产品思维 | 面对业务人员 | 化繁为简，从真实现场找到真问题，先给最简单的一版 |
| 经营者思维 | 面对企业主 | 站在付钱的一方，用降本、增效、提质这类经营结果验收自己 |

另外，技术基本功是入场券：低于门槛时，等级最高到 L3。

测完给出：总分（100 分制）、等级（L1–L5）、四个维度各自的得分和依据、最该补的一项和一条两周内能动手做的建议。

两种节奏：

- **快测**：4 轮，约 3 分钟（背景 + 三种思维各一道情境题），适合现场演示和手机上试。
- **完整测**：6–8 轮，约 10 分钟，四个维度都问，并按回答自适应追问。

本仓库公开的是测评框架和打分逻辑：四个维度、权重、0–4 分尺子、五个等级、封顶规则、反刷分原则和输出格式。不附固定题库，题目由 AI 按出题原则、结合你的行业现场出。

> 这是快速测评，看的是思路，不是招聘结论。

## 文件

```
SKILL.md                     测评流程：怎么问、怎么追问、怎么打分、结果格式
references/question_bank.md  出题原则：每个维度考什么、怎么按你的背景现场出题、追问方向和高低分信号
references/rubric.md         评分表：0–4 分锚点、权重、等级线、封顶规则、反刷分
scripts/score.py             把四个维度的分数换算成总分、等级和最该补的一项
```

## 安装与调用

### 手机或网页上的 AI

用上面那段提示词即可，不用安装。

### Claude Code

```bash
git clone https://github.com/Infinity-light/fde-fit-assessment ~/.claude/skills/fde-fit-assessment
```

然后在 Claude Code 里说“测一测我适不适合做 FDE”，或输入 `/fde-fit-assessment`。

### Claude 网页版 / 桌面版（Skills）

下载本仓库的 zip，在 设置 → Capabilities → Skills 里上传，然后对 Claude 说“FDE 测评”。

### 其他支持 Skill 或自定义指令的 Agent

把 `SKILL.md` 作为系统指令，把 `references/` 下的两个文件作为知识文件加进去。

### 单独算分

```bash
python scripts/score.py --t 3 --a 2.5 --p 2 --b 3
```

每个维度 0–4 分，可用 0.5；规则与 `references/rubric.md` 一致。

## 许可

MIT
