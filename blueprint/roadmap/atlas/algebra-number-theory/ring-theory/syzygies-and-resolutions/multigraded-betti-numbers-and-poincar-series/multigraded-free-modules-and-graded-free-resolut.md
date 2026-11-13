---
declaration: section
origin: cited
lean: MetaMathlibExt.IsDegreeZero, MetaMathlibExt.MultigradedFreeModule, MetaMathlibExt.MultigradedFreeResolution
statement: formalized
proof: formalized
---

# Multigraded free modules and graded free resolutions

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/multigraded-free-modules-and-graded-free-resolut/index.html).

## Degree-zero homomorphisms of multigraded modules

Let $K$ be a field, let
$R = K[x_1, \dots, x_n]$, and let $M$ and $N$ be multigraded $R$-modules with homogeneous pieces
$M_\alpha$ and $N_\alpha$ for $\alpha \in \mathbb{Z}^n$. An $R$-linear map $f : M \to N$ is
degree-zero when $f(M_\alpha) \subseteq N_\alpha$ for every $\alpha \in \mathbb{Z}^n$.

Formalized by `MetaMathlibExt.IsDegreeZero`, a definition declared in [MathlibExt/RingTheory/GradedAlgebra/MultigradedFreeResolution.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/GradedAlgebra/MultigradedFreeResolution.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/multigraded-free-modules-and-graded-free-resolut/index.html#is-degree-zero).

## Multigraded free module

Let $K$ be a field, let $R = K[x_1, \dots, x_n]$, and let
$\iota$ be an index type. A multigraded free module structure on an $R$-module $F$ consists of a
multigraded $R$-module structure on $F$, with homogeneous pieces $F_\alpha$ for
$\alpha \in \mathbb{Z}^n$, together with an $R$-basis $(b_j)_{j \in \iota}$ of $F$ and a degree
$d_j \in \mathbb{Z}^n$ for each $j \in \iota$ such that $b_j \in F_{d_j}$ for every
$j \in \iota$.

Formalized by `MetaMathlibExt.MultigradedFreeModule`, a structure declared in [MathlibExt/RingTheory/GradedAlgebra/MultigradedFreeResolution.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/GradedAlgebra/MultigradedFreeResolution.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/multigraded-free-modules-and-graded-free-resolut/index.html#multigraded-free-module).

## Multigraded free resolution

Let $K$ be a field, let $R = K[x_1, \dots, x_n]$, let $M$ be
a multigraded $R$-module, let $\cdots \to P_1 \to P_0 \to M$ be a projective resolution of $M$
over $R$, and for each $i \in \mathbb{N}$ let $\iota_i$ be an index type. A multigraded free
resolution structure on this resolution consists of a multigraded free module structure on each
$P_i$ with basis indexed by $\iota_i$, such that every differential $P_{i+1} \to P_i$ and the
augmentation $P_0 \to M$ are degree-zero for these gradings and the given grading of $M$.

Each $P_i$ is regarded as a $K$-vector space by restricting scalars along $K \to R$.

Formalized by `MetaMathlibExt.MultigradedFreeResolution`, a structure declared in [MathlibExt/RingTheory/GradedAlgebra/MultigradedFreeResolution.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/GradedAlgebra/MultigradedFreeResolution.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/multigraded-free-modules-and-graded-free-resolut/index.html#multigraded-free-resolution).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multigraded free modules and graded free resolutions](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/multigraded-free-modules-and-graded-free-resolut/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/multigraded-free-modules-and-graded-free-resolut)
