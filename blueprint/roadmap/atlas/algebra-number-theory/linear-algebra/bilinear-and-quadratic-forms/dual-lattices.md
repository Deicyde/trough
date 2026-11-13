---
declaration: section
origin: cited
lean: Submodule.isLocalizedModule_subtype_of_span_eq_top, LinearMap.BilinForm.dualSubmoduleToDual_surjective, LinearMap.BilinForm.dualSubmoduleToDual_bijective, LinearMap.BilinForm.dualSubmodule_fg, LinearMap.BilinForm.dualSubmodule_span_eq_top, LinearMap.BilinForm.dualSubmodule_isLattice, LinearMap.BilinForm.dualSubmodule_isLattice_and_dualSubmoduleToDual_bijective, LinearMap.BilinForm.dualSubmoduleLinearEquiv
statement: formalized
proof: formalized
---

# Dual lattices

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/dual-lattices/index.html).

## A spanning submodule localizes to the whole space

Let $A$ be a commutative ring with
fraction field $K$, let $V$ be a $K$-vector space, viewed as an $A$-module through $A \to K$, and
let $M$ be an $A$-submodule of $V$ that spans $V$ over $K$. Then $V$, together with the inclusion
$M \hookrightarrow V$, is the localization of the $A$-module $M$ at the non-zero-divisors of $A$.

Concretely, every non-zero-divisor $s$ of $A$ acts bijectively on $V$, and every $v \in V$
satisfies $s v \in M$ for some non-zero-divisor $s$ of $A$.

Formalized by `Submodule.isLocalizedModule_subtype_of_span_eq_top`, a theorem declared in [MathlibExt/LinearAlgebra/BilinearForm/DualLattice.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/BilinearForm/DualLattice.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/dual-lattices/index.html#is-localized-module-subtype-of-span-eq-t).

## Surjectivity of the dual pairing

Let $A$ be an integral domain with fraction field $K$,
let $V$ be a finite-dimensional $K$-vector space, viewed as an $A$-module through $A \subseteq K$,
let $B$ be a nondegenerate bilinear form on $V$, and let $M$ be an $A$-submodule of $V$ that
spans $V$ over $K$. Then the map from
$M^\vee = \{x \in V : B(x, y) \in A \text{ for all } y \in M\}$ to $\operatorname{Hom}_A(M, A)$
sending $x$ to the functional $y \mapsto B(x, y)$ is surjective.

Formalized by `LinearMap.BilinForm.dualSubmoduleToDual_surjective`, a theorem declared in [MathlibExt/LinearAlgebra/BilinearForm/DualLattice.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/BilinearForm/DualLattice.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/dual-lattices/index.html#dual-submodule-to-dual-surjective).

## Bijectivity of the dual pairing

Let $A$ be an integral domain with fraction field $K$,
let $V$ be a finite-dimensional $K$-vector space, viewed as an $A$-module through $A \subseteq K$,
let $B$ be a nondegenerate bilinear form on $V$, and let $M$ be an $A$-submodule of $V$ that
spans $V$ over $K$. Then the map from
$M^\vee = \{x \in V : B(x, y) \in A \text{ for all } y \in M\}$ to $\operatorname{Hom}_A(M, A)$
sending $x$ to the functional $y \mapsto B(x, y)$ is bijective.

Formalized by `LinearMap.BilinForm.dualSubmoduleToDual_bijective`, a theorem declared in [MathlibExt/LinearAlgebra/BilinearForm/DualLattice.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/BilinearForm/DualLattice.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/dual-lattices/index.html#dual-submodule-to-dual-bijective).

## The dual of a lattice is finitely generated

Let $A$ be a Noetherian integral domain with
fraction field $K$, let $V$ be a $K$-vector space, viewed as an $A$-module through
$A \subseteq K$, and let $B$ be a nondegenerate bilinear form on $V$. Let $M$ be a finitely
generated $A$-submodule of $V$ that spans $V$ over $K$. Then the dual submodule
$M^\vee = \{x \in V : B(x, y) \in A \text{ for all } y \in M\}$ is a finitely generated
$A$-submodule of $V$.

Formalized by `LinearMap.BilinForm.dualSubmodule_fg`, a theorem declared in [MathlibExt/LinearAlgebra/BilinearForm/DualLattice.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/BilinearForm/DualLattice.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/dual-lattices/index.html#dual-submodule-fg).

## The dual of a finitely generated submodule spans

Let $A$ be a commutative ring with
fraction field $K$, let $V$ be a $K$-vector space, viewed as an $A$-module through $A \to K$, and
let $B$ be a bilinear form on $V$. If $M$ is a finitely generated $A$-submodule of $V$, then its
dual submodule $M^\vee = \{x \in V : B(x, y) \in A \text{ for all } y \in M\}$ spans $V$ over
$K$.

Formalized by `LinearMap.BilinForm.dualSubmodule_span_eq_top`, a theorem declared in [MathlibExt/LinearAlgebra/BilinearForm/DualLattice.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/BilinearForm/DualLattice.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/dual-lattices/index.html#dual-submodule-span-eq-top).

## The dual of a lattice is a lattice

Let $A$ be a Noetherian integral domain with fraction
field $K$, let $V$ be a $K$-vector space, viewed as an $A$-module through $A \subseteq K$, and let
$B$ be a nondegenerate bilinear form on $V$. If $M$ is an $A$-lattice in $V$, that is, a finitely
generated $A$-submodule that spans $V$ over $K$, then so is its dual submodule
$M^\vee = \{x \in V : B(x, y) \in A \text{ for all } y \in M\}$.

Formalized by `LinearMap.BilinForm.dualSubmodule_isLattice`, a theorem declared in [MathlibExt/LinearAlgebra/BilinearForm/DualLattice.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/BilinearForm/DualLattice.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/dual-lattices/index.html#dual-submodule-is-lattice).

## The dual lattice and the dual module

Let $A$ be a Noetherian integral domain with
fraction field $K$, let $V$ be a finite-dimensional $K$-vector space, viewed as an $A$-module
through $A \subseteq K$, and let $B$ be a nondegenerate bilinear form on $V$. Let $M$ be an
$A$-lattice in $V$, that is, a finitely generated $A$-submodule that spans $V$ over $K$, and let
$M^\vee = \{x \in V : B(x, y) \in A \text{ for all } y \in M\}$. Then $M^\vee$ is an $A$-lattice
in $V$, and the map $M^\vee \to \operatorname{Hom}_A(M, A)$ sending $x$ to the functional
$y \mapsto B(x, y)$ is bijective.

Formalized by `LinearMap.BilinForm.dualSubmodule_isLattice_and_dualSubmoduleToDual_bijective`, a theorem declared in [MathlibExt/LinearAlgebra/BilinearForm/DualLattice.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/BilinearForm/DualLattice.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/dual-lattices/index.html#dual-submodule-is-lattice-and-dual-submo).

## The dual submodule is the dual module

Let $A$ be an integral domain with fraction field
$K$, let $V$ be a finite-dimensional $K$-vector space, viewed as an $A$-module through
$A \subseteq K$, let $B$ be a nondegenerate bilinear form on $V$, and let $M$ be an $A$-submodule
of $V$ that spans $V$ over $K$. Write
$M^\vee = \{x \in V : B(x, y) \in A \text{ for all } y \in M\}$. This is the isomorphism of
$A$-modules $M^\vee \cong \operatorname{Hom}_A(M, A)$ that sends $x$ to the functional
$y \mapsto B(x, y)$.

Formalized by `LinearMap.BilinForm.dualSubmoduleLinearEquiv`, a definition declared in [MathlibExt/LinearAlgebra/BilinearForm/DualLattice.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/BilinearForm/DualLattice.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/dual-lattices/index.html#dual-submodule-linear-equiv).

## Double dual of a reflexive lattice

Let $A$ be an integral domain with fraction field $K$,
let $V$ be a finite-dimensional $K$-vector space, viewed as an $A$-module through $A \subseteq K$,
and let $B$ be a nondegenerate bilinear form on $V$. Let $M$ be an $A$-lattice in $V$, that is, a
finitely generated $A$-submodule that spans $V$ over $K$, and suppose that $M$ is reflexive as an
$A$-module. Let $M^\vee = \{x \in V : B(x, y) \in A \text{ for all } y \in M\}$. Then
$\{x \in V : B(y, x) \in A \text{ for all } y \in M^\vee\} = M$.

This is the lattice analogue of the corresponding statement for the $A$-span of a $K$-basis of
$V$: no basis is needed when $M$ is reflexive as an $A$-module.

Formalized by `LinearMap.BilinForm.dualSubmodule_flip_dualSubmodule_of_isLattice`, a theorem declared in [MathlibExt/LinearAlgebra/BilinearForm/DualLatticeReflexive.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/BilinearForm/DualLatticeReflexive.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/dual-lattices/index.html#dual-submodule-flip-dual-submodule-of-is).

## Double dual of a lattice over a Dedekind domain

Let $A$ be a Dedekind domain with
fraction field $K$, let $V$ be a finite-dimensional $K$-vector space, viewed as an $A$-module
through $A \subseteq K$, and let $B$ be a nondegenerate symmetric bilinear form on $V$. For an
$A$-submodule $N$ of $V$ write $N^\vee = \{x \in V : B(x, y) \in A \text{ for all } y \in N\}$.
If $M$ is an $A$-lattice in $V$, that is, a finitely generated $A$-submodule that spans $V$ over
$K$, then $(M^\vee)^\vee = M$.

No reflexivity hypothesis on $M$ is needed: over a Dedekind domain a finitely generated
torsion-free module is flat, hence projective, hence reflexive.

## Sources

- ATLAS NumberTheoryI, Proposition 5.16.

Formalized by `LinearMap.BilinForm.dualSubmodule_dualSubmodule_of_isLattice`, a theorem declared in [MathlibExt/LinearAlgebra/BilinearForm/DualLatticeReflexive.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/BilinearForm/DualLatticeReflexive.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/dual-lattices/index.html#dual-submodule-dual-submodule-of-is-latt).

## Dual submodules commute with localization

Let $A$ be an integral domain with fraction
field $K$, let $V$ be a $K$-vector space that is also an $A$-module compatibly with $A \to K$, and
let $B$ be a $K$-bilinear form on $V$. For a subring $R \subseteq K$ and an $R$-submodule $N$ of
$V$, write $N^\vee_R = \{x \in V : B(x, y) \in R \text{ for all } y \in N\}$ for the dual of $N$
over $R$. Let $S$ be a submonoid of $A$ consisting of non-zero-divisors, and let
$A_S = \{a/s : a \in A,\ s \in S\} \subseteq K$ be the localization of $A$ at $S$. Then for every
finitely generated $A$-submodule $M$ of $V$, the dual over $A_S$ of the $A_S$-span of $M$ equals
the $A_S$-span of the dual $M^\vee_A$ of $M$ over $A$.

Formalized by `LinearMap.BilinForm.dualSubmodule_span_localization`, a theorem declared in [MathlibExt/LinearAlgebra/BilinearForm/DualLocalization.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/BilinearForm/DualLocalization.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/dual-lattices/index.html#dual-submodule-span-localization).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dual lattices](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/dual-lattices/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/dual-lattices)
