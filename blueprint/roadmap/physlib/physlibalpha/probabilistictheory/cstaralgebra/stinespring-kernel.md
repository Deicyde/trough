---
declaration: module
origin: cited
lean: ProbabilisticTheory.blockMatrixMap, ProbabilisticTheory.blockMatrixMap_apply, ProbabilisticTheory.blockMatrixMap_star, ProbabilisticTheory.blockMatrixMap_mul, ProbabilisticTheory.blockMatrixMap_one, ProbabilisticTheory.blockMatrixMap_add, ProbabilisticTheory.blockMatrixMap_zero, ProbabilisticTheory.blockMatrixRepresentation
statement: formalized
proof: formalized
---

# Completely positive maps as positive kernels

The module `PhyslibAlpha.ProbabilisticTheory.CStarAlgebra.Stinespring.Kernel`, [PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Kernel.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Kernel.lean): 22 declarations, 6 with a docstring.

> Completely positive maps give positive operator-valued kernels; Stinespring witnesses.

## i. Overview

> A completely positive map `J` into the bounded operators on `H` is a positive operator-valued
> kernel: applied to the Gram matrix of finitely many elements of `A`, it gives a positive block
> operator on `Hⁿ`. A Stinespring witness of `J` is a representation `π` on a Hilbert space `K` and an
> operator `V : H → K` with `J a = V⋆ π(a) V`.

## ii. Key results

> - `blockMatrixMap` : a matrix of operators acting on `Hⁿ`.
> - `cpKernel_inner_nonneg_natural'` : completely positive maps give positive kernels.
> - `StinespringWitness` : a Stinespring dilation of `J`.
> - `completelyPositiveMap_map_star_general` : completely positive maps preserve the adjoint.

## iv. References

> * None.

## A. `blockMatrixMap`: the finite block-operator representation

> This part uses only the codomain Hilbert space `H`, no algebra `A` at all.

**`ProbabilisticTheory.blockMatrixMap`**, a def, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Kernel.lean#L61).

> The bounded operator on `PiLp 2 (Fin n → H)` acting block-by-block by `M`.

```lean
def blockMatrixMap {n : ℕ} (M : CStarMatrix (Fin n) (Fin n) (H →L[ℂ] H)) :
    PiLp 2 (fun _ : Fin n => H) →L[ℂ] PiLp 2 (fun _ : Fin n => H)
```

**`ProbabilisticTheory.blockMatrixMap_apply`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Kernel.lean#L72).

```lean
lemma blockMatrixMap_apply {n : ℕ} (M : CStarMatrix (Fin n) (Fin n) (H →L[ℂ] H))
    (x : PiLp 2 (fun _ : Fin n => H)) (i : Fin n) :
    (blockMatrixMap M x).ofLp i = ∑ j, M i j (x.ofLp j)
```

**`ProbabilisticTheory.blockMatrixMap_star`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Kernel.lean#L77).

```lean
lemma blockMatrixMap_star {n : ℕ} (M : CStarMatrix (Fin n) (Fin n) (H →L[ℂ] H)) :
    blockMatrixMap (star M) = (blockMatrixMap M).adjoint
```

**`ProbabilisticTheory.blockMatrixMap_mul`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Kernel.lean#L91).

```lean
lemma blockMatrixMap_mul {n : ℕ} (M N : CStarMatrix (Fin n) (Fin n) (H →L[ℂ] H)) :
    blockMatrixMap (M * N) = blockMatrixMap M ∘L blockMatrixMap N
```

**`ProbabilisticTheory.blockMatrixMap_one`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Kernel.lean#L104).

```lean
lemma blockMatrixMap_one {n : ℕ} :
    blockMatrixMap (1 : CStarMatrix (Fin n) (Fin n) (H →L[ℂ] H)) = ContinuousLinearMap.id ℂ _
```

**`ProbabilisticTheory.blockMatrixMap_add`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Kernel.lean#L118).

```lean
lemma blockMatrixMap_add {n : ℕ} (M N : CStarMatrix (Fin n) (Fin n) (H →L[ℂ] H)) :
    blockMatrixMap (M + N) = blockMatrixMap M + blockMatrixMap N
```

**`ProbabilisticTheory.blockMatrixMap_zero`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Kernel.lean#L132).

```lean
lemma blockMatrixMap_zero {n : ℕ} :
    blockMatrixMap (0 : CStarMatrix (Fin n) (Fin n) (H →L[ℂ] H)) = 0
```

**`ProbabilisticTheory.blockMatrixRepresentation`**, a def, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Kernel.lean#L142).

> `blockMatrixMap`, packaged as a star algebra homomorphism from
> `CStarMatrix (Fin n) (Fin n) (H →L[ℂ] H)`.

```lean
def blockMatrixRepresentation {n : ℕ} :
    CStarMatrix (Fin n) (Fin n) (H →L[ℂ] H) →⋆ₐ[ℂ]
      (PiLp 2 (fun _ : Fin n => H) →L[ℂ] PiLp 2 (fun _ : Fin n => H))
```

**`ProbabilisticTheory.blockMatrixMap_isPositive`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Kernel.lean#L165).

```lean
lemma blockMatrixMap_isPositive {n : ℕ} {M : CStarMatrix (Fin n) (Fin n) (H →L[ℂ] H)}
    (hM : 0 ≤ M) : (blockMatrixMap M).IsPositive
```

**`ProbabilisticTheory.blockMatrixMap_inner_nonneg`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Kernel.lean#L171).

```lean
lemma blockMatrixMap_inner_nonneg {n : ℕ} {M : CStarMatrix (Fin n) (Fin n) (H →L[ℂ] H)}
    (hM : 0 ≤ M) (x : PiLp 2 (fun _ : Fin n => H)) :
    0 ≤ ∑ i, ∑ j, inner ℂ (M i j (x.ofLp j)) (x.ofLp i)
```

## B. The CP-map positivity kernel

> From here on, `A` is a unital C⋆-algebra with the compatible Mathlib order (`[CStarAlgebra A]
> [PartialOrder A] [StarOrderedRing A]`) — the field content of `OperatorAlgebra A`.

**`ProbabilisticTheory.completelyPositiveMap_map_star_general`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Kernel.lean#L185).

> A CP map between C⋆-algebras is automatically star-preserving.

```lean
lemma completelyPositiveMap_map_star_general
    {A B : Type*} [CStarAlgebra A] [PartialOrder A] [StarOrderedRing A]
    [CStarAlgebra B] [PartialOrder B] [StarOrderedRing B]
    (J : A →CP B) (a : A) : star (J a) = J (star a)
```

**`ProbabilisticTheory.rowMatrix`**, a def, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Kernel.lean#L200).

> A square matrix whose only nonzero row is the zeroth row.

```lean
def rowMatrix {n : ℕ} [NeZero n] (a : Fin n → A) :
    CStarMatrix (Fin n) (Fin n) A
```

**`ProbabilisticTheory.gramMatrix`**, a def, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Kernel.lean#L204).

> The Gram matrix of a finite family of elements of a C⋆-algebra.

```lean
def gramMatrix {n : ℕ} [NeZero n] (a : Fin n → A) :
    CStarMatrix (Fin n) (Fin n) A
```

**`ProbabilisticTheory.gramMatrix_apply`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Kernel.lean#L209).

```lean
lemma gramMatrix_apply {n : ℕ} [NeZero n] (a : Fin n → A) (i j : Fin n) :
    gramMatrix a i j = star (a i) * a j
```

**`ProbabilisticTheory.gramMatrix_nonneg`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Kernel.lean#L213).

```lean
lemma gramMatrix_nonneg {n : ℕ} [NeZero n] (a : Fin n → A) : 0 ≤ gramMatrix a
```

**`ProbabilisticTheory.cpGramMatrix_nonneg`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Kernel.lean#L216).

```lean
lemma cpGramMatrix_nonneg {n : ℕ} [NeZero n] (J : A →CP (H →L[ℂ] H)) (a : Fin n → A) :
    0 ≤ (gramMatrix a).map J
```

**`ProbabilisticTheory.cpKernel_inner_nonneg`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Kernel.lean#L220).

```lean
lemma cpKernel_inner_nonneg {n : ℕ} [NeZero n] (J : A →CP (H →L[ℂ] H)) (a : Fin n → A)
    (x : PiLp 2 (fun _ : Fin n => H)) :
    0 ≤ ∑ i, ∑ j, inner ℂ (J (star (a i) * a j) (x.ofLp j)) (x.ofLp i)
```

**`ProbabilisticTheory.cpKernel_inner_nonneg'`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Kernel.lean#L226).

```lean
lemma cpKernel_inner_nonneg' {n : ℕ} (J : A →CP (H →L[ℂ] H)) (a : Fin n → A)
    (x : PiLp 2 (fun _ : Fin n => H)) :
    0 ≤ ∑ i, ∑ j, inner ℂ (J (star (a i) * a j) (x.ofLp j)) (x.ofLp i)
```

**`ProbabilisticTheory.cpKernel_inner_nonneg_natural`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Kernel.lean#L234).

```lean
lemma cpKernel_inner_nonneg_natural {n : ℕ} [NeZero n] (J : A →CP (H →L[ℂ] H)) (a : Fin n → A)
    (x : PiLp 2 (fun _ : Fin n => H)) :
    0 ≤ ∑ i, ∑ j, inner ℂ (x.ofLp i) (J (star (a i) * a j) (x.ofLp j))
```

**`ProbabilisticTheory.cpKernel_inner_nonneg_natural'`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Kernel.lean#L270).

```lean
lemma cpKernel_inner_nonneg_natural' {n : ℕ} (J : A →CP (H →L[ℂ] H)) (a : Fin n → A)
    (x : PiLp 2 (fun _ : Fin n => H)) :
    0 ≤ ∑ i, ∑ j, inner ℂ (x.ofLp i) (J (star (a i) * a j) (x.ofLp j))
```

## C. Stinespring witnesses

**`ProbabilisticTheory.StinespringWitness`**, a structure, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Kernel.lean#L284).

> A Stinespring dilation of `J`: a representation `π` of `A` on a Hilbert space `K` and an
> operator `V : H → K` with `J a = V⋆ π(a) V`.

```lean
structure StinespringWitness (A H K : Type*) [CStarAlgebra A] [PartialOrder A]
    [StarOrderedRing A] [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
    [NormedAddCommGroup K] [InnerProductSpace ℂ K] [CompleteSpace K]
    (J : A →CP (H →L[ℂ] H)) where
  /-- The representation of the input operator algebra on the auxiliary space. -/
  representation : A →⋆ₐ[ℂ] (K →L[ℂ] K)
  /-- The implementing bounded operator from the physical space to the auxiliary space. -/
  implementing : H →L[ℂ] K
  /-- The Stinespring identity: `J a = V⋆ π(a) V`. -/
  map_eq : ∀ a : A,
    J a = ContinuousLinearMap.adjoint implementing ∘L
      (representation a) ∘L implementing
```

**`ProbabilisticTheory.StinespringWitness.map_eq_apply`**, a lemma, [line 301](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Kernel.lean#L301).

```lean
lemma map_eq_apply (a : A) :
    J a = ContinuousLinearMap.adjoint W.implementing ∘L
      (W.representation a) ∘L W.implementing
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Kernel.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Kernel.lean)
