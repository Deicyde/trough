---
declaration: section
origin: cited
lean: MetaMathlibExt.multigradedPoincarePolynomial, MetaMathlibExt.multigradedPoincarePolynomial_coeff
statement: formalized
proof: formalized
---

# Multigraded Poincaré polynomial

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/multigraded-poincar-polynomial/index.html).

## Multigraded Poincaré polynomial

Let $K$ be a field, let $R = K[x_1, \dots, x_n]$, let
$M$ be a multigraded $R$-module, and let $D$ be base-change data for a multigraded free
resolution $F_\bullet$ of $M$ in which $F_i$ has a homogeneous basis indexed by a finite set
$\iota_i$, with $\iota_i$ empty for every $i > b$ for a fixed $b \in \mathbb{N}$. The
multigraded Poincaré polynomial of $D$ is the element of the monoid algebra
$\mathbb{N}[\mathbb{N} \times \mathbb{Z}^n]$ whose coefficient at $(i, \alpha)$ is the
multigraded Betti number $\beta_{i,\alpha}(D)$ of $D$ in homological degree $i$ and multidegree
$\alpha$; the hypotheses on the $\iota_i$ make these coefficients finitely supported.

Formalized by `MetaMathlibExt.multigradedPoincarePolynomial`, a definition declared in [MathlibExt/RingTheory/GradedAlgebra/MultigradedPoincarePolynomial.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/GradedAlgebra/MultigradedPoincarePolynomial.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/multigraded-poincar-polynomial/index.html#multigraded-poincare-polynomial).

## Coefficients of the multigraded Poincaré polynomial

Let $K$ be a field, let
$R = K[x_1, \dots, x_n]$, let $M$ be a multigraded $R$-module, and let $D$ be base-change data
for a multigraded free resolution $F_\bullet$ of $M$ in which $F_i$ has a homogeneous basis
indexed by a finite set $\iota_i$, with $\iota_i$ empty for every $i > b$ for a fixed
$b \in \mathbb{N}$. For every $i \in \mathbb{N}$ and $\alpha \in \mathbb{Z}^n$, the coefficient
at $(i, \alpha)$ of the multigraded Poincaré polynomial of $D$ is the multigraded Betti number
$\beta_{i,\alpha}(D)$ of $D$ in homological degree $i$ and multidegree $\alpha$.

Formalized by `MetaMathlibExt.multigradedPoincarePolynomial_coeff`, a theorem declared in [MathlibExt/RingTheory/GradedAlgebra/MultigradedPoincarePolynomial.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/GradedAlgebra/MultigradedPoincarePolynomial.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/multigraded-poincar-polynomial/index.html#multigraded-poincare-polynomial-coeff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multigraded Poincaré polynomial](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/multigraded-poincar-polynomial/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/multigraded-poincar-polynomial)
