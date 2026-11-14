---
declaration: definition
origin: cited
lean: MIPRE.Tailored.tabOfT, MIPRE.Tailored.margAt, MIPRE.Tailored.margN, MIPRE.Tailored.lenRun, MIPRE.Tailored.lpRun, MIPRE.Tailored.zOf, MIPRE.Tailored.lenList, MIPRE.Tailored.consAt, MIPRE.Tailored.consT, MIPRE.Tailored.vtxEquiv, MIPRE.Tailored.tabT
statement: formalized
---

# The tabulation of a tailored verifier

The *tabulation* of a tailored verifier at index $n$, under the budget $T \cdot (\left\vert {d} \right\vert + 1)^k$, is the tailored game description whose vertices are the doubled questions $\{0, 1\} \times \mathbb{F}_2^{s(n)}$, whose weights count the points of $\mathbb{F}_2^{s(n)}$ landing on each pair of tagged marginals, and whose lengths and constraints are what the answer-length calculator and the linear-constraints processor output, each program run under the budget. On a description string, the verifier is $(\mathcal{S}^\lambda, \mathcal{L}^\lambda, \mathcal{P})$ for the string's parameter $\lambda$ and processor $\mathcal{P}$, and the budget is $n^\lambda \cdot (\left\vert {d} \right\vert+1)^\lambda$.

## Depends on

- [Tailored normal form verifier; II:1758](../part-01/def-tailored-verifier.md)
- [Tailored game descriptions, standalone; II:1243, II:1279](../part-01/def-tailored-game-data.md)
- [$\lambda$-bounded tailored verifiers, and budgets; II:1800](../part-01/def-tailored-bounded.md)
- [Tailored gap compression, value form; II:1852](def-tailored-compression.md)

## Lean

Formalized as [`MIPRE.Tailored.tabOfT`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.tabOfT), [`MIPRE.Tailored.margAt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.margAt), [`MIPRE.Tailored.margN`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.margN), [`MIPRE.Tailored.lenRun`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.lenRun), [`MIPRE.Tailored.lpRun`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.lpRun), [`MIPRE.Tailored.zOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.zOf), [`MIPRE.Tailored.lenList`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.lenList), [`MIPRE.Tailored.consAt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.consAt), [`MIPRE.Tailored.consT`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.consT), [`MIPRE.Tailored.vtxEquiv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.vtxEquiv), [`MIPRE.Tailored.tabT`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.tabT).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 800](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L800)
