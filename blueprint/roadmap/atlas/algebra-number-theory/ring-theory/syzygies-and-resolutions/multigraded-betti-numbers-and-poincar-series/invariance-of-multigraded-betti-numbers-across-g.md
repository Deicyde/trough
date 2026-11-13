---
declaration: section
origin: cited
lean: MetaMathlibExt.MultigradedResolutionComparison, MetaMathlibExt.multigradedBettiNumber_eq_of_resolutionComparison
statement: formalized
proof: formalized
---

# Invariance of multigraded Betti numbers across graded free resolutions

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/invariance-of-multigraded-betti-numbers-across-g/index.html).

## Multigraded resolution comparison

Let $K$ be a field, let $R = K[x_1, \dots, x_n]$,
and let $M$ be a $\mathbb{Z}^n$-graded $R$-module with two multigraded free resolutions,
each equipped with multigraded base change data, whose degree-$\alpha$ component complexes
are $C^\alpha$ and $D^\alpha$ for $\alpha \in \mathbb{Z}^n$. A comparison between the two
base change data is a choice, for every $\alpha \in \mathbb{Z}^n$, of a chain-homotopy
equivalence between $C^\alpha$ and $D^\alpha$.

A homotopy equivalence, rather than a bare quasi-isomorphism, is the comparison-theorem
input: it induces an isomorphism on homology. Existence and uniqueness of such a
comparison are not claimed here.

Formalized by `MetaMathlibExt.MultigradedResolutionComparison`, a structure declared in [MathlibExt/RingTheory/GradedAlgebra/MultigradedBettiResolutionInvariance.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/GradedAlgebra/MultigradedBettiResolutionInvariance.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/invariance-of-multigraded-betti-numbers-across-g/index.html#multigraded-resolution-comparison).

## Betti numbers agree across comparable resolutions

Let $K$ be a field, let
$R = K[x_1, \dots, x_n]$, and let $M$ be a $\mathbb{Z}^n$-graded $R$-module with two
multigraded free resolutions, each equipped with multigraded base change data, whose
degree-$\alpha$ component complexes are $C^\alpha$ and $D^\alpha$ for $\alpha \in \mathbb{Z}^n$.
If the two are related by a multigraded resolution comparison, that is, for every $\alpha$
a chain-homotopy equivalence between $C^\alpha$ and $D^\alpha$, then the multigraded Betti
numbers defined by the two base change data agree in every multidegree
$\alpha \in \mathbb{Z}^n$ and every homological index $i \in \mathbb{N}$.

## Sources

- Benjamin Braun and Brian Davis, “Antichain Simplices,” Journal of Integer Sequences 23 (2020), <https://cs.uwaterloo.ca/journals/JIS/VOL23/Braun/braun4.tex>, exact lines 866--874. This is conditional only: it assumes the comparison and claims no existence, uniqueness, minimality, finite support, Poincaré polynomiality or rationality, or Hilbert syzygy.

Formalized by `MetaMathlibExt.multigradedBettiNumber_eq_of_resolutionComparison`, a theorem declared in [MathlibExt/RingTheory/GradedAlgebra/MultigradedBettiResolutionInvariance.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/GradedAlgebra/MultigradedBettiResolutionInvariance.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/invariance-of-multigraded-betti-numbers-across-g/index.html#multigraded-betti-number-eq-of-resolutio).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Invariance of multigraded Betti numbers across graded free resolutions](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/invariance-of-multigraded-betti-numbers-across-g/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/invariance-of-multigraded-betti-numbers-across-g)
