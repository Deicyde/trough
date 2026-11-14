---
declaration: lemma
origin: cited
lean: ProbabilityTheory.tv_le
statement: formalized
proof: formalized
---

# tv_le

For $\mu, \nu \in \mathcal M(\mathcal X)$, $\operatorname{TV}(\mu, \nu) \le \min\{\mu(\mathcal X), \nu(\mathcal X)\}$ .

## Depends on

- [TV](def-tv.md)

## Proof depends on

- [statInfo_le](lem-statinfo-le.md)

## Proof

Use Lemma [statInfo_le](lem-statinfo-le.md).

## Lean

Formalized as [`ProbabilityTheory.tv_le`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.tv_le).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/stat_div.tex, line 501](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/stat_div.tex#L501)
