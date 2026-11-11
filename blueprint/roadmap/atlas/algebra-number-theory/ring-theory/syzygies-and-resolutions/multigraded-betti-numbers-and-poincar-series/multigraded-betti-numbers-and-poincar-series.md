---
declaration: section
origin: cited
lean: MetaMathlibExt.MultigradedPolynomialModule.exists_finset_homogeneous_generators, MetaMathlibExt.MultigradedFreeResolution.baseChangedDegreePiece_finite, MetaMathlibExt.MultigradedFreeResolution.baseChangedDegreeDecomposition, MetaMathlibExt.multigradedBettiNumber_eq_of_baseChange, MetaMathlibExt.exists_finite_multigraded_free_resolution, MetaMathlibExt.multigradedPoincareCoefficients_hasFiniteSupport_of_finiteResolution, MetaMathlibExt.MultigradedFreeModule.baseChange_mem_degreeSpan, MetaMathlibExt.MultigradedFreeResolution.baseChangedDifferential_preservesDegree
statement: formalized
proof: formalized
---

# Multigraded Betti numbers and Poincaré series: its own results

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/index.html).

## Finite homogeneous generating sets

Let $K$ be a field, let $R = K[x_1, \dots, x_n]$,
and let $M$ be a multigraded polynomial module over $R$, with degree-$\alpha$ components
$M_\alpha$ for $\alpha \in \mathbb{Z}^n$, that is finitely generated as an $R$-module. Then
there is a finite set $s \subseteq M$ of homogeneous elements, each lying in $M_\alpha$ for some
$\alpha \in \mathbb{Z}^n$, that generates $M$ as an $R$-module.

## Sources

- Braun-Davis, JIS 23 (2020), span 856-877; see https://cs.uwaterloo.ca/journals/JIS/VOL23/Braun/braun4.tex

Formalized by `MetaMathlibExt.MultigradedPolynomialModule.exists_finset_homogeneous_generators`, a theorem declared in [MathlibExt/RingTheory/GradedAlgebra/FiniteHomogeneousGenerators.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/GradedAlgebra/FiniteHomogeneousGenerators.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/index.html#exists-finset-homogeneous-generators).

## Finite bases give finite-dimensional multidegree pieces

Let $K$ be a field, let
$R = K[x_1, \dots, x_n]$, let $M$ be a multigraded polynomial module over $R$, and let $F$ be a
multigraded free resolution of $M$ whose term $F_i$ has the homogeneous basis
$(e_j)_{j \in \iota_i}$. Write $K \otimes_R F$ for the chain complex of $K$-vector spaces obtained
from $F$ by extending scalars along the evaluation $R \to K$ at $x = 0$. If $\iota_i$ is finite,
then for every $\alpha \in \mathbb{Z}^n$ the degree-$\alpha$ piece of $(K \otimes_R F)_i$, the
$K$-span of the vectors $1 \otimes e_j$ with $e_j$ of degree $\alpha$, is finite-dimensional
over $K$.

## Sources

- Benjamin Braun and Brian Davis, "Antichain Simplices," Journal of Integer Sequences 23 (2020), lines 862–867, <https://cs.uwaterloo.ca/journals/JIS/VOL23/Braun/braun4.tex>.

Formalized by `MetaMathlibExt.MultigradedFreeResolution.baseChangedDegreePiece_finite`, a theorem declared in [MathlibExt/RingTheory/GradedAlgebra/MultigradedBaseChangedDegreePieceFinite.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/GradedAlgebra/MultigradedBaseChangedDegreePieceFinite.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/index.html#base-changed-degree-piece-finite).

## Multidegree decomposition of the base-changed resolution

Let $K$ be a field, let
$R = K[x_1, \dots, x_n]$, let $M$ be a multigraded polynomial module over $R$, and let $F$ be a
multigraded free resolution of $M$ whose term $F_i$ has the homogeneous basis
$(e_j)_{j \in \iota_i}$. Write $K \otimes_R F$ for the chain complex of $K$-vector spaces obtained
from $F$ by extending scalars along the evaluation $R \to K$ at $x = 0$, and for
$\alpha \in \mathbb{Z}^n$ call the $K$-span of the vectors $1 \otimes e_j$ with $e_j$ of degree
$\alpha$ the degree-$\alpha$ piece of $(K \otimes_R F)_i$. For every $i \ge 0$, this is the
decomposition of $(K \otimes_R F)_i$ as the internal direct sum of its degree-$\alpha$ pieces
over $\alpha \in \mathbb{Z}^n$.

## Sources

- Braun-Davis, JIS 23 (2020), lines 856-867. See https://cs.uwaterloo.ca/journals/JIS/VOL23/Braun/braun4.tex

Formalized by `MetaMathlibExt.MultigradedFreeResolution.baseChangedDegreeDecomposition`, a definition declared in [MathlibExt/RingTheory/GradedAlgebra/MultigradedBaseChangedTermDecomposition.lean, line 23](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/GradedAlgebra/MultigradedBaseChangedTermDecomposition.lean#L23). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/index.html#base-changed-degree-decomposition).

## Betti numbers do not depend on the choice of base change data

Let $K$ be a field,
let $R = K[x_1, \dots, x_n]$, and let $M$ be a $\mathbb{Z}^n$-graded $R$-module with a fixed
multigraded free resolution $P_\bullet \to M$. Any two choices of multigraded base change
data for $P_\bullet$ define the same multigraded Betti numbers, in every multidegree
$\alpha \in \mathbb{Z}^n$ and every homological index $i \in \mathbb{N}$.

## Sources

- Benjamin Braun and Brian Davis, “Antichain Simplices,” Journal of Integer Sequences 23 (2020), <https://cs.uwaterloo.ca/journals/JIS/VOL23/Braun/braun4.tex>, exact lines 866--874. This covers only the fixed-resolution coherence step; independence across resolutions, finite support, Poincaré polynomiality, and Hilbert syzygy are deliberately not claimed here.

Formalized by `MetaMathlibExt.multigradedBettiNumber_eq_of_baseChange`, a theorem declared in [MathlibExt/RingTheory/GradedAlgebra/MultigradedBettiInvariance.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/GradedAlgebra/MultigradedBettiInvariance.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/index.html#multigraded-betti-number-eq-of-base-chan).

## Existence of finite multigraded free resolutions

Let $K$ be a field, let
$R = K[x_1, \dots, x_n]$, and let $M$ be a multigraded $R$-module that is finitely generated over
$R$. Then there are a projective resolution $P_\bullet \to M$ over $R$, index types $\iota_i$ for
$i \in \mathbb{N}$, a multigraded free resolution structure on $P_\bullet$ for the given grading
of $M$ in which $P_i$ has basis indexed by $\iota_i$, and a number $b \in \mathbb{N}$ such that
every $\iota_i$ is finite and $\iota_i$ is empty for every $i > b$.

The proof uses stagewise minimal homogeneous free covers, the determinant trick,
dimension shifting, and Hilbert's syzygy theorem.

## Sources

- Hoffman–Wang, https://export.arxiv.org/e-print/math/0601101v1 lines 592-612 (finite free graded resolution). The Braun–Davis JIS passage https://cs.uwaterloo.ca/journals/JIS/VOL23/Braun/braun4.tex lines 856-876 supplies the motivating Hilbert-syzygy / Poincaré-series context only. No `≤ n` bound is claimed here.

Formalized by `MetaMathlibExt.exists_finite_multigraded_free_resolution`, a theorem declared in [MathlibExt/RingTheory/GradedAlgebra/MultigradedHilbertSyzygy.lean, line 1286](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/GradedAlgebra/MultigradedHilbertSyzygy.lean#L1286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/index.html#exists-finite-multigraded-free-resolutio).

## Finite support of the multigraded Poincaré coefficients

Let $K$ be a field, let
$R = K[x_1, \dots, x_n]$, let $M$ be a multigraded $R$-module, and let $D$ be base-change data
for a multigraded free resolution $F_\bullet$ of $M$ in which $F_i$ has a homogeneous basis
indexed by $\iota_i$. Suppose every $\iota_i$ is finite and, for some $b \in \mathbb{N}$,
$\iota_i$ is empty for every $i > b$. Then the multigraded Poincaré coefficient family of $D$ is
nonzero at only finitely many $(i, \alpha) \in \mathbb{N} \times \mathbb{Z}^n$.

## Sources

- Benjamin Braun and Brian Davis, “Antichain Simplices,” Journal of Integer Sequences 23 (2020), <https://cs.uwaterloo.ca/journals/JIS/VOL23/Braun/braun4.tex>, exact line 876. This is the conditional finite-resolution bridge behind that line, not the full Hilbert syzygy existence theorem: it assumes the finite terminating resolution and derives finite coefficient support, without assuming finite support, eventual Betti vanishing, or a polynomial realization, and without constructing the resolution.

Formalized by `MetaMathlibExt.multigradedPoincareCoefficients_hasFiniteSupport_of_finiteResolution`, a theorem declared in [MathlibExt/RingTheory/GradedAlgebra/MultigradedPoincareFiniteSupport.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/GradedAlgebra/MultigradedPoincareFiniteSupport.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/index.html#multigraded-poincare-coefficients-has-fi).

## Base change of a homogeneous element along zero evaluation

Let $K$ be a field,
$R = K[x_1, \dots, x_n]$, and let $F$ be a multigraded free $R$-module with basis
$(b_j)_{j \in \iota}$, where each $b_j$ is homogeneous of degree $d_j \in \mathbb{Z}^n$.
Make $K$ an $R$-algebra through the zero evaluation $R \to K$, which sends every
variable to $0$. If $x \in F$ is homogeneous of degree $\alpha \in \mathbb{Z}^n$, then
$1 \otimes x \in K \otimes_R F$ lies in the $K$-linear span of the vectors $1 \otimes b_j$
with $d_j = \alpha$.

## Sources

- Benjamin Braun and Brian Davis, "Antichain Simplices," Journal of Integer Sequences 23 (2020), lines 862–867, <https://cs.uwaterloo.ca/journals/JIS/VOL23/Braun/braun4.tex>, which split a graded free resolution and take the degree-`α` component after tensoring with `K`.

Formalized by `MetaMathlibExt.MultigradedFreeModule.baseChange_mem_degreeSpan`, a theorem declared in [MathlibExt/RingTheory/GradedAlgebra/MultigradedZeroEvalBaseChange.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/GradedAlgebra/MultigradedZeroEvalBaseChange.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/index.html#base-change-mem-degree-span).

## The base-changed differential preserves multidegree

Let $K$ be a field, let
$R = K[x_1, \dots, x_n]$, let $M$ be a multigraded polynomial module over $R$, and let $F$ be a
multigraded free resolution of $M$ whose term $F_i$ has the homogeneous basis
$(e_j)_{j \in \iota_i}$. Write $K \otimes_R F$ for the chain complex of $K$-vector spaces obtained
from $F$ by extending scalars along the evaluation $R \to K$ at $x = 0$, and for
$\alpha \in \mathbb{Z}^n$ call the $K$-span of the vectors $1 \otimes e_j$ with $e_j$ of degree
$\alpha$ the degree-$\alpha$ piece of $(K \otimes_R F)_i$. Then for every $i \ge 0$ and every
$\alpha \in \mathbb{Z}^n$, the differential $(K \otimes_R F)_{i+1} \to (K \otimes_R F)_i$ maps
the degree-$\alpha$ piece of $(K \otimes_R F)_{i+1}$ into the degree-$\alpha$ piece of
$(K \otimes_R F)_i$.

## Sources

- Benjamin Braun and Brian Davis, "Antichain Simplices," Journal of Integer Sequences 23 (2020), lines 862–867, <https://cs.uwaterloo.ca/journals/JIS/VOL23/Braun/braun4.tex>.

Formalized by `MetaMathlibExt.MultigradedFreeResolution.baseChangedDifferential_preservesDegree`, a theorem declared in [MathlibExt/RingTheory/GradedAlgebra/MultigradedBaseChangedDifferential.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/GradedAlgebra/MultigradedBaseChangedDifferential.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/index.html#base-changed-differential-preserves-degr).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multigraded Betti numbers and Poincaré series](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series)
