---
declaration: lemma
origin: cited
lean: ProbabilityTheory.statInfo_le_min
statement: formalized
proof: formalized
---

# statInfo_le

For $\mu, \nu \in \mathcal M(\mathcal X)$, $\mathcal I_\xi(\mu, \nu) \le \min\{\xi_0 \mu(\mathcal X), \xi_1 \nu(\mathcal X)\}$ .

## Depends on

- [statInfo](def-statinfo.md)

## Proof

Use Lemma [bayesBinaryRisk_nonneg](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/risk.tex#L641).

## Lean

Formalized as [`ProbabilityTheory.statInfo_le_min`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.statInfo_le_min).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/stat_div.tex, line 48](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/stat_div.tex#L48)
