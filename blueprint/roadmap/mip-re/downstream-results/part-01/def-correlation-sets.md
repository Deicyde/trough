---
declaration: definition
origin: cited
lean: MIPRE.Game.payoff, MIPRE.TensorProductStrategy.correlation, MIPRE.Cq, MIPRE.Cqa, MIPRE.Cqc
statement: formalized
---

# Correlation sets

Fix finite sets ${\mathcal{X}}, {\mathcal{Y}}, {\mathcal{A}}, {\mathcal{B}}$. A *correlation* is a function $p : {\mathcal{X}} \times {\mathcal{Y}} \times {\mathcal{A}} \times {\mathcal{B}} \to \mathbb{R}$, written $p(a,b|x,y)$, and its *payoff* in a game $\mathfrak{G}$ on these alphabets is $\sum_{x,y,a,b} \mu(x,y)\, D(x,y,a,b)\, p(a,b|x,y)$. The set $C_q$ consists of the correlations $\langle\psi| A^x_a \otimes B^y_b |\psi\rangle$ of finite-dimensional tensor-product strategies (Definition [Tensor-product strategy](../../foundations/part-01/def-tensor-strategy.md)); $C_{qa}$ is its closure in $\mathbb{R}^{{\mathcal{X}} \times {\mathcal{Y}} \times {\mathcal{A}} \times {\mathcal{B}}}$; and $C_{qc}$ consists of the correlations $\langle\psi| E^x_a F^y_b |\psi\rangle$ of commuting-operator strategies (Definition [Commuting-operator strategy](../../parallel-repetition/def-co-strategy-bipartite.md)). The value of a strategy of either kind is the payoff of its correlation.

## Depends on

- [Tensor-product strategy](../../foundations/part-01/def-tensor-strategy.md)
- [Commuting-operator strategy](../../parallel-repetition/def-co-strategy-bipartite.md)

## Lean

Formalized as [`MIPRE.Game.payoff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Game.payoff), [`MIPRE.TensorProductStrategy.correlation`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TensorProductStrategy.correlation), [`MIPRE.Cq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cq), [`MIPRE.Cqa`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cqa), [`MIPRE.Cqc`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cqc).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 348](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L348)
