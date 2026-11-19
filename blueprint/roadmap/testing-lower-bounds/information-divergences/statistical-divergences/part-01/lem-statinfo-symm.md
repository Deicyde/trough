---
declaration: lemma
origin: cited
lean: ProbabilityTheory.statInfo_symm
statement: formalized
proof: formalized
---

# statInfo_symm

For $\mu, \nu \in \mathcal M(\mathcal X)$ and $\xi \in \mathcal M(\{0,1\})$, $\mathcal I_\xi(\mu, \nu) = \mathcal I_{\xi_\leftrightarrow}(\nu, \mu)$ .

## Depends on

- [statInfo](def-statinfo.md)

## Proof depends on

- [bayesBinaryRisk_symm](../../../testing-estimation-risk/simple-binary-hypothesis-testing/lem-bayesbinaryrisk-symm.md)

## Proof

Use Lemma [bayesBinaryRisk_symm](../../../testing-estimation-risk/simple-binary-hypothesis-testing/lem-bayesbinaryrisk-symm.md).

## Lean

Formalized as [`ProbabilityTheory.statInfo_symm`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.statInfo_symm).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/stat_div.tex, line 62](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/stat_div.tex#L62)
