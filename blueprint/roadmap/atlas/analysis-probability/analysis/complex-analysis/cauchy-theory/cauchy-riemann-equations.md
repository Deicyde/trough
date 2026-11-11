---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Complex.ConjNowhereDifferentiableWanted.not_differentiableAt_conj, MathlibExt.Analysis.Complex.HolomorphicConjConstWanted.exists_eqOn_const_of_differentiableOn_conj
statement: formalized
---

# Cauchy–Riemann equations

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/cauchy-riemann-equations/index.html).

## Complex conjugation is nowhere complex-differentiable

Let $f : \mathbb{C} \to \mathbb{C}$
be the function $f(z) = \bar z$. Then $f$ is not complex-differentiable at any point
$z \in \mathbb{C}$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Functions of a complex variable; General properties of functions of one complex variable), problem `ma_proofbench_l1_57`.

Stated but not proved: `MathlibExt.Analysis.Complex.ConjNowhereDifferentiableWanted.not_differentiableAt_conj` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/ConjNowhereDifferentiableWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Complex/ConjNowhereDifferentiableWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/cauchy-riemann-equations/index.html#not-differentiable-at-conj).

## A holomorphic function with holomorphic conjugate is constant

Let
$U \subseteq \mathbb{C}$ be a connected open set and let $f : \mathbb{C} \to \mathbb{C}$ be
holomorphic on $U$. If the conjugate function $z \mapsto \overline{f(z)}$ is also holomorphic on
$U$, then $f$ is constant on $U$: there is $c \in \mathbb{C}$ with $f(z) = c$ for all $z \in U$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Functions of a complex variable; General properties of functions of one complex variable), problem `ma_proofbench_l1_04`.

Stated but not proved: `MathlibExt.Analysis.Complex.HolomorphicConjConstWanted.exists_eqOn_const_of_differentiableOn_conj` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/HolomorphicConjConstWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Complex/HolomorphicConjConstWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/cauchy-riemann-equations/index.html#exists-eq-on-const-of-differentiable-on).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cauchy–Riemann equations](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/cauchy-riemann-equations/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/complex-analysis/cauchy-theory/cauchy-riemann-equations)
