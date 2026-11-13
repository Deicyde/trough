---
declaration: section
origin: cited
lean: MetaMathlibExt.zeroEval, MetaMathlibExt.baseChangedComplex, MetaMathlibExt.baseChangedDegreePiece, MetaMathlibExt.MultigradedBaseChange, MetaMathlibExt.multigradedBettiNumber
statement: formalized
proof: formalized
---

# Multigraded Betti numbers after residue-field base change

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/multigraded-betti-numbers-after-residue-field-ba/index.html).

## Augmentation of the polynomial ring

For a field $K$ and $n \in \mathbb{N}$, the
augmentation $K[x_1, \dots, x_n] \to K$ is the ring homomorphism sending each polynomial
$p$ to its value $p(0, \dots, 0)$: it is the identity on constants and sends every
variable to $0$.

Formalized by `MetaMathlibExt.zeroEval`, a definition declared in [MathlibExt/RingTheory/GradedAlgebra/MultigradedBetti.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/GradedAlgebra/MultigradedBetti.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/multigraded-betti-numbers-after-residue-field-ba/index.html#zero-eval).

## Base change of a resolution to the residue field

Let $K$ be a field, let
$R = K[x_1, \dots, x_n]$, and let $M$ be an $R$-module. Given a projective resolution
$P_\bullet \to M$ over $R$, its base change is the chain complex of $K$-vector spaces
$K \otimes_R P_\bullet$, indexed by $\mathbb{N}$ with differentials lowering the index,
obtained by extending scalars termwise along the augmentation $R \to K$ that sends every
variable to $0$: its $i$th term is $K \otimes_R P_i$ and its differentials are the maps
$\mathrm{id}_K \otimes d$ for the differentials $d$ of $P_\bullet$.

Formalized by `MetaMathlibExt.baseChangedComplex`, a definition declared in [MathlibExt/RingTheory/GradedAlgebra/MultigradedBetti.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/GradedAlgebra/MultigradedBetti.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/multigraded-betti-numbers-after-residue-field-ba/index.html#base-changed-complex).

## Degree pieces of the base-changed resolution

Let $K$ be a field, let
$R = K[x_1, \dots, x_n]$, and let $M$ be a $\mathbb{Z}^n$-graded $R$-module with a
multigraded free resolution $P_\bullet \to M$, in which each $P_i$ has an $R$-basis
$(e_j)_{j \in J_i}$ with $e_j$ homogeneous of degree $\deg e_j \in \mathbb{Z}^n$. For
$i \in \mathbb{N}$ and $\alpha \in \mathbb{Z}^n$, the degree-$\alpha$ piece of the $i$th
term $K \otimes_R P_i$ of the base-changed complex is the $K$-subspace spanned by the
vectors $1 \otimes e_j$ with $j \in J_i$ and $\deg e_j = \alpha$.

Formalized by `MetaMathlibExt.baseChangedDegreePiece`, a definition declared in [MathlibExt/RingTheory/GradedAlgebra/MultigradedBetti.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/GradedAlgebra/MultigradedBetti.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/multigraded-betti-numbers-after-residue-field-ba/index.html#base-changed-degree-piece).

## Multigraded base change data

Let $K$ be a field, let $R = K[x_1, \dots, x_n]$,
and let $M$ be a $\mathbb{Z}^n$-graded $R$-module with a multigraded free resolution
$P_\bullet \to M$. Write $K \otimes_R P_\bullet$ for its base change along the
augmentation $R \to K$ and $(K \otimes_R P_i)_\beta$ for the degree-$\beta$ piece of its
$i$th term. Multigraded base change data for $P_\bullet$ consist of: for each
$i \in \mathbb{N}$, a decomposition of $K \otimes_R P_i$ as the internal direct sum of the
pieces $(K \otimes_R P_i)_\beta$ over $\beta \in \mathbb{Z}^n$, such that for all $i$ and
$\beta$ the differential $K \otimes_R P_{i+1} \to K \otimes_R P_i$ maps
$(K \otimes_R P_{i+1})_\beta$ into $(K \otimes_R P_i)_\beta$; and, for each
$\alpha \in \mathbb{Z}^n$, an $\mathbb{N}$-indexed chain complex $C^\alpha$ of
$K$-vector spaces with a chain map $C^\alpha \to K \otimes_R P_\bullet$ whose $i$th
component is injective with image $(K \otimes_R P_i)_\alpha$ for every $i$, such that
every homology $H_i(C^\alpha)$ exists and is finite-dimensional over $K$.

Formalized by `MetaMathlibExt.MultigradedBaseChange`, a structure declared in [MathlibExt/RingTheory/GradedAlgebra/MultigradedBetti.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/GradedAlgebra/MultigradedBetti.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/multigraded-betti-numbers-after-residue-field-ba/index.html#multigraded-base-change).

## Multigraded Betti number

Let $K$ be a field, let $R = K[x_1, \dots, x_n]$, and
let $M$ be a $\mathbb{Z}^n$-graded $R$-module with a multigraded free resolution
$P_\bullet \to M$. Fix multigraded base change data for $P_\bullet$; for each
$\alpha \in \mathbb{Z}^n$ they supply a chain complex $C^\alpha$ of $K$-vector spaces
embedded in the base-changed complex $K \otimes_R P_\bullet$ with image its degree-$\alpha$
pieces. For $\alpha \in \mathbb{Z}^n$ and $i \in \mathbb{N}$, the multigraded Betti number
of $M$ in multidegree $\alpha$ and homological index $i$, with respect to these data, is
the dimension over $K$ of the homology $H_i(C^\alpha)$.

Formalized by `MetaMathlibExt.multigradedBettiNumber`, a definition declared in [MathlibExt/RingTheory/GradedAlgebra/MultigradedBetti.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/GradedAlgebra/MultigradedBetti.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/multigraded-betti-numbers-after-residue-field-ba/index.html#multigraded-betti-number).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multigraded Betti numbers after residue-field base change](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/multigraded-betti-numbers-after-residue-field-ba/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/multigraded-betti-numbers-after-residue-field-ba)
