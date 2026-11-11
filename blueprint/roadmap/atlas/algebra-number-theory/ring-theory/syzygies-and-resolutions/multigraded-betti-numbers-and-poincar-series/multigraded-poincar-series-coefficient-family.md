---
declaration: section
origin: cited
lean: MetaMathlibExt.multigradedPoincareCoefficients, MetaMathlibExt.multigradedPoincareCoefficients_apply, MetaMathlibExt.multigradedPoincareCoefficients_eq_of_resolutionComparison
statement: formalized
proof: formalized
---

# Multigraded Poincaré-series coefficient family

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/multigraded-poincar-series-coefficient-family/index.html).

## Multigraded Poincaré coefficients

Let $K$ be a field, let $R = K[x_1, \dots, x_n]$, let
$M$ be a multigraded $R$-module, and let $D$ be base-change data for a multigraded free
resolution of $M$. The multigraded Poincaré coefficient family of $D$ is the function
$\mathbb{N} \times \mathbb{Z}^n \to \mathbb{N}$ sending $(i, \alpha)$ to the multigraded Betti
number $\beta_{i,\alpha}(D)$ of $D$ in homological degree $i$ and multidegree $\alpha$.

A plain function records every coefficient without asserting finite
support, convergence, polynomiality, or rationality.

Formalized by `MetaMathlibExt.multigradedPoincareCoefficients`, a definition declared in [MathlibExt/RingTheory/GradedAlgebra/MultigradedPoincareCoefficients.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/GradedAlgebra/MultigradedPoincareCoefficients.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/multigraded-poincar-series-coefficient-family/index.html#multigraded-poincare-coefficients).

## Multigraded Poincaré coefficients are Betti numbers

Let $K$ be a field, let
$R = K[x_1, \dots, x_n]$, let $M$ be a multigraded $R$-module, and let $D$ be base-change data
for a multigraded free resolution of $M$. For every $i \in \mathbb{N}$ and
$\alpha \in \mathbb{Z}^n$, the multigraded Poincaré coefficient family of $D$ takes the value
$\beta_{i,\alpha}(D)$ at $(i, \alpha)$, where $\beta_{i,\alpha}(D)$ is the multigraded Betti
number of $D$ in homological degree $i$ and multidegree $\alpha$.

Formalized by `MetaMathlibExt.multigradedPoincareCoefficients_apply`, a theorem declared in [MathlibExt/RingTheory/GradedAlgebra/MultigradedPoincareCoefficients.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/GradedAlgebra/MultigradedPoincareCoefficients.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/multigraded-poincar-series-coefficient-family/index.html#multigraded-poincare-coefficients-apply).

## Resolution comparisons preserve multigraded Poincaré coefficients

Let $K$ be a field,
let $R = K[x_1, \dots, x_n]$, let $M$ be a multigraded $R$-module, and let $D$ and $D'$ be
base-change data for two multigraded free resolutions of $M$. Given a multigraded resolution
comparison between $D$ and $D'$, that is, for every $\alpha \in \mathbb{Z}^n$ a chain-homotopy
equivalence between the degree-$\alpha$ component complexes of $D$ and $D'$, the multigraded
Poincaré coefficient families of $D$ and $D'$ are equal.

## Sources

- Benjamin Braun and Brian Davis, “Antichain Simplices,” Journal of Integer Sequences 23 (2020), <https://cs.uwaterloo.ca/journals/JIS/VOL23/Braun/braun4.tex>, exact lines 870--874. This is conditional only: it assumes the comparison and claims no existence, unconditional independence, finite support, polynomiality, rationality, or convergence.

Formalized by `MetaMathlibExt.multigradedPoincareCoefficients_eq_of_resolutionComparison`, a theorem declared in [MathlibExt/RingTheory/GradedAlgebra/MultigradedPoincareCoefficients.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/GradedAlgebra/MultigradedPoincareCoefficients.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/multigraded-poincar-series-coefficient-family/index.html#multigraded-poincare-coefficients-eq-of).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multigraded Poincaré-series coefficient family](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/multigraded-poincar-series-coefficient-family/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/multigraded-poincar-series-coefficient-family)
