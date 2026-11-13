---
declaration: section
origin: cited
lean: MetaMathlibExt.MultigradedFreeResolution.baseChangedDegreeComplex, MetaMathlibExt.MultigradedFreeResolution.baseChangedDegreeInclusion, MetaMathlibExt.MultigradedFreeResolution.baseChangedDegreeInclusion_injective, MetaMathlibExt.MultigradedFreeResolution.baseChangedDegreeInclusion_range, MetaMathlibExt.MultigradedFreeResolution.multigradedBaseChange_nonempty
statement: formalized
proof: formalized
---

# Degree components of the base-changed multigraded resolution

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/degree-components-of-the-base-changed-multigrade/index.html).

## Multidegree component complex of the base-changed resolution

Let $K$ be a field, let
$R = K[x_1, \dots, x_n]$, let $M$ be a multigraded polynomial module over $R$, and let $F$ be a
multigraded free resolution of $M$ whose term $F_i$ has the homogeneous basis
$(e_j)_{j \in \iota_i}$. Write $K \otimes_R F$ for the chain complex of $K$-vector spaces obtained
from $F$ by extending scalars along the evaluation $R \to K$ at $x = 0$, and for
$\alpha \in \mathbb{Z}^n$ call the $K$-span of the vectors $1 \otimes e_j$ with $e_j$ of degree
$\alpha$ the degree-$\alpha$ piece of $(K \otimes_R F)_i$. The degree-$\alpha$ complex is the
chain complex of $K$-vector spaces whose term in homological degree $i$ is the degree-$\alpha$
piece of $(K \otimes_R F)_i$ and whose differentials are the restrictions of the differentials
of $K \otimes_R F$.

## Sources

- Benjamin Braun and Brian Davis, "Antichain Simplices," Journal of Integer Sequences 23 (2020), lines 864–867, <https://cs.uwaterloo.ca/journals/JIS/VOL23/Braun/braun4.tex>.

Formalized by `MetaMathlibExt.MultigradedFreeResolution.baseChangedDegreeComplex`, a definition declared in [MathlibExt/RingTheory/GradedAlgebra/MultigradedBaseChangedDegreeComplex.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/GradedAlgebra/MultigradedBaseChangedDegreeComplex.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/degree-components-of-the-base-changed-multigrade/index.html#base-changed-degree-complex).

## Inclusion of a multidegree component complex

Let $K$ be a field, let
$R = K[x_1, \dots, x_n]$, let $M$ be a multigraded polynomial module over $R$, and let $F$ be a
multigraded free resolution of $M$ whose term $F_i$ has the homogeneous basis
$(e_j)_{j \in \iota_i}$. Write $K \otimes_R F$ for the chain complex of $K$-vector spaces obtained
from $F$ by extending scalars along the evaluation $R \to K$ at $x = 0$, and for
$\alpha \in \mathbb{Z}^n$ call the $K$-span of the vectors $1 \otimes e_j$ with $e_j$ of degree
$\alpha$ the degree-$\alpha$ piece of $(K \otimes_R F)_i$. The inclusion of the degree-$\alpha$
complex is the chain map from the degree-$\alpha$ complex of $K \otimes_R F$ to $K \otimes_R F$
whose component in each homological degree $i$ is the inclusion of the degree-$\alpha$ piece of
$(K \otimes_R F)_i$ into $(K \otimes_R F)_i$.

## Sources

- Benjamin Braun and Brian Davis, "Antichain Simplices," Journal of Integer Sequences 23 (2020), lines 864–867, <https://cs.uwaterloo.ca/journals/JIS/VOL23/Braun/braun4.tex>.

Formalized by `MetaMathlibExt.MultigradedFreeResolution.baseChangedDegreeInclusion`, a definition declared in [MathlibExt/RingTheory/GradedAlgebra/MultigradedBaseChangedDegreeComplex.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/GradedAlgebra/MultigradedBaseChangedDegreeComplex.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/degree-components-of-the-base-changed-multigrade/index.html#base-changed-degree-inclusion).

## Injectivity of the base-changed degree inclusion

Each component of the degree inclusion is injective. Source:
Benjamin Braun and Brian Davis, "Antichain Simplices," Journal of
Integer Sequences 23 (2020), lines 864–867,
`https://cs.uwaterloo.ca/journals/JIS/VOL23/Braun/braun4.tex`.

Formalized by `MetaMathlibExt.MultigradedFreeResolution.baseChangedDegreeInclusion_injective`, a theorem declared in [MathlibExt/RingTheory/GradedAlgebra/MultigradedBaseChangedDegreeComplex.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/GradedAlgebra/MultigradedBaseChangedDegreeComplex.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/degree-components-of-the-base-changed-multigrade/index.html#injectivity-of-the-base-changed-degree-i).

## Range of the base-changed degree inclusion

Each component of the degree inclusion has range exactly the
degree piece `baseChangedDegreePiece`. Source: Benjamin Braun and
Brian Davis, "Antichain Simplices," Journal of Integer Sequences 23
(2020), lines 864–867,
`https://cs.uwaterloo.ca/journals/JIS/VOL23/Braun/braun4.tex`.

Formalized by `MetaMathlibExt.MultigradedFreeResolution.baseChangedDegreeInclusion_range`, a theorem declared in [MathlibExt/RingTheory/GradedAlgebra/MultigradedBaseChangedDegreeComplex.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/GradedAlgebra/MultigradedBaseChangedDegreeComplex.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/degree-components-of-the-base-changed-multigrade/index.html#range-of-the-base-changed-degree-inclusi).

## Existence of multigraded base-change data

Let $K$ be a field, let
$R = K[x_1, \dots, x_n]$, let $M$ be a multigraded polynomial module over $R$, and let $F$ be a
multigraded free resolution of $M$ whose term $F_i$ has the homogeneous basis
$(e_j)_{j \in \iota_i}$, where every index set $\iota_i$ is finite. Write $K \otimes_R F$ for the
chain complex of $K$-vector spaces obtained from $F$ by extending scalars along the evaluation
$R \to K$ at $x = 0$, and for $\alpha \in \mathbb{Z}^n$ call the $K$-span of the vectors
$1 \otimes e_j$ with $e_j$ of degree $\alpha$ the degree-$\alpha$ piece of $(K \otimes_R F)_i$.
Then multigraded base-change data for $F$ exist: each $(K \otimes_R F)_i$ is the direct sum of
its degree-$\alpha$ pieces over $\alpha \in \mathbb{Z}^n$, the differentials of $K \otimes_R F$
preserve these pieces, and for every $\alpha$ there is a chain complex $C^\alpha$ of $K$-vector
spaces with finite-dimensional homology in every degree, together with a chain map
$C^\alpha \to K \otimes_R F$ that is injective in each homological degree $i$ with image the
degree-$\alpha$ piece of $(K \otimes_R F)_i$.

## Sources

- Benjamin Braun and Brian Davis, "Antichain Simplices," Journal of Integer Sequences 23 (2020), lines 862–867, <https://cs.uwaterloo.ca/journals/JIS/VOL23/Braun/braun4.tex>.

Formalized by `MetaMathlibExt.MultigradedFreeResolution.multigradedBaseChange_nonempty`, a theorem declared in [MathlibExt/RingTheory/GradedAlgebra/MultigradedBaseChangedDegreeComplex.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/GradedAlgebra/MultigradedBaseChangedDegreeComplex.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/degree-components-of-the-base-changed-multigrade/index.html#multigraded-base-change-nonempty).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Degree components of the base-changed multigraded resolution](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/degree-components-of-the-base-changed-multigrade/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/degree-components-of-the-base-changed-multigrade)
