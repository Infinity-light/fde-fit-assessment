"""FDE 适配度测评：四个维度分数 -> 总分、等级、最该补的一项。

用法：python score.py --t 3 --a 2.5 --p 2 --b 3
每个维度 0-4 分，可用 0.5。规则与 references/rubric.md 一致。
"""
import argparse
import json
import sys

DIMS = {
    "T": ("技术基本功（入场券）", 20),
    "A": ("AI 原生思维（面对工程）", 25),
    "P": ("产品思维（面对业务人员）", 25),
    "B": ("经营者思维（面对企业主）", 30),
}
# 并列时的优先顺序：经营结果是成绩单
TIE_ORDER = ["B", "P", "A", "T"]
LEVELS = [
    (85, "L5", "带队"),
    (70, "L4", "独当"),
    (55, "L3", "交付"),
    (40, "L2", "上手"),
    (0, "L1", "了解"),
]
LEVEL_RANK = {code: i for i, (_, code, _) in enumerate(reversed(LEVELS))}


def bar(score):
    full = int(score)
    half = 1 if score - full >= 0.5 else 0
    return "■" * full + "▨" * half + "□" * (4 - full - half)


def compute(scores):
    total = round(sum(scores[k] / 4 * w for k, (_, w) in DIMS.items()))
    level = next((code, name) for th, code, name in LEVELS if total >= th)
    caps = []
    if scores["T"] < 2:
        caps.append(("L3", "技术基本功低于 2 分：技术是入场券"))
    if min(scores["A"], scores["P"], scores["B"]) < 2:
        caps.append(("L3", "三种思维有一项低于 2 分"))
    if level[0] == "L5" and not (scores["B"] >= 3.5 and scores["T"] >= 3):
        caps.append(("L4", "L5 需经营者思维 ≥3.5 且技术基本功 ≥3"))
    applied = []
    for cap, why in caps:
        if LEVEL_RANK[level[0]] > LEVEL_RANK[cap]:
            level = next((c, n) for _, c, n in LEVELS if c == cap)
            applied.append(why)
    if scores["T"] < 2:
        weakest = "T"
    else:
        low = min(scores[k] for k in DIMS)
        weakest = next(k for k in TIE_ORDER if scores[k] == low)
    return {
        "total": total,
        "level": f"{level[0]} · {level[1]}",
        "caps_applied": applied,
        "weakest": DIMS[weakest][0],
        "dims": {DIMS[k][0]: f"{scores[k]:g} / 4  {bar(scores[k])}" for k in DIMS},
    }


def main():
    ap = argparse.ArgumentParser()
    for k in DIMS:
        ap.add_argument(f"--{k.lower()}", type=float, required=True)
    args = ap.parse_args()
    scores = {k: getattr(args, k.lower()) for k in DIMS}
    for k, v in scores.items():
        if not 0 <= v <= 4 or (v * 2) != int(v * 2):
            sys.exit(f"{k} 分数须在 0-4 之间、以 0.5 为步长：{v}")
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(compute(scores), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
