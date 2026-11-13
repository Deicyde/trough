---
declaration: module
origin: cited
lean: ConjTensorSpecies.inverseT, ConjTensorSpecies.toMatrix_inverseT, ConjTensorSpecies.toSquareMatrix_inverseT, ConjTensorSpecies.isSymm_toSesqForm_inverseT, ConjTensorSpecies.isPosDef_toSesqForm_inverseT, ConjTensorSpecies.contractInnerT_inverseT, ConjTensorSpecies.inverseT_contractInnerT, ConjTensorSpecies.eq_inverseT_of_contractInnerT_eq_unitTensor
statement: formalized
proof: formalized
---

# The inverse of a rank-two tensor

The module `Physlib.Relativity.Tensors.Conjugation.Inverse`, [Physlib/Relativity/Tensors/Conjugation/Inverse.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Inverse.lean): 11 declarations, 11 with a docstring.

> The inverse `g^{J̄I}` of a tensor `g_{IJ̄}` with one index and one conjugate index, such as a
> Hermitian metric, and the linear equivalence that contracts an index with `g`.

## i. Overview

> The inverse of a tensor `g_{IJ̄}` is the tensor `g^{J̄I}`, with two upper indices, for which
> `g_{IJ̄} g^{J̄K} = δ_I^K` and `g^{J̄I} g_{IK̄} = δ^J̄_K̄`.
>
> The colours of the inverse are `![τ (c 1), τ (c 0)]`, so its barred index comes first, `g^{J̄I}`.
> The usual `g^{IJ̄}` is the same tensor with its two indices swapped. With the barred index first,
> `g_{IJ̄} g^{J̄K}` contracts adjacent indices, so the contraction laws need no reordering of the
> inverse. The matrix `(g^{J̄I})`, with row `J` and column `I`, is the inverse of the matrix
> `(g_{IJ̄})`. `inverseT` is defined by this matrix inversion and is zero when `(g_{IJ̄})` is not
> invertible. The inverse of a Hermitian `g` is Hermitian (A), and the inverse of a
> positive-definite `g` is positive-definite (B). When `(g_{IJ̄})` is invertible, the two contraction
> laws hold and the inverse is unique (C). Then contracting an index with `g` is a linear
> equivalence whose inverse contracts with `g^{J̄I}` (D).

## ii. Key results

> - `ConjTensorSpecies.inverseT` is the inverse `g^{J̄I}` of a tensor `g_{IJ̄}`.
> - `ConjTensorSpecies.toSquareMatrix_inverseT` says that the matrix `(g^{J̄I})` is `(g_{IJ̄})⁻¹`.
> - `ConjTensorSpecies.isSymm_toSesqForm_inverseT` and
>   `ConjTensorSpecies.isPosDef_toSesqForm_inverseT` say that the inverse of a Hermitian or
>   positive-definite `g` is again Hermitian or positive-definite.
> - `ConjTensorSpecies.contractInnerT_inverseT` and `ConjTensorSpecies.inverseT_contractInnerT` are
>   the contraction laws `g_{IJ̄} g^{J̄K} = δ_I^K` and `g^{J̄I} g_{IK̄} = δ^J̄_K̄`.
> - `ConjTensorSpecies.eq_inverseT_of_contractInnerT_eq_unitTensor` says that the inverse is unique.
> - `ConjTensorSpecies.toConjDualAtIndex` contracts an index with `g`, as a linear equivalence
>   whose inverse contracts with `g^{J̄I}`.

## iv. References

> - `Matrix.inv` and `Matrix.inv_def`, in `Mathlib/LinearAlgebra/Matrix/NonsingularInverse.lean`;
> - `Matrix.PosDef.inv`, in `Mathlib/LinearAlgebra/Matrix/PosDef.lean`.

## A. The inverse

**`ConjTensorSpecies.inverseT`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Inverse.lean#L84).

> The inverse `g^{J̄I}` of a tensor `g_{IJ̄}`. Its matrix, with row `J` and column `I`, is
> `(g_{IJ̄})⁻¹`, and it is zero when `(g_{IJ̄})` is not invertible.

```lean
def inverseT {c : Fin 2 → C} (M : S.Tensor c) (hbar : S.bar (c 0) = c 1 := by rfl) :
    S.Tensor ![S.τ (c 1), S.τ (c 0)]
```

**`ConjTensorSpecies.toMatrix_inverseT`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Inverse.lean#L93).

> The component `g^{J̄I}` is the entry `(J, I)` of `(g_{IJ̄})⁻¹`. The upper indices `J̄` and `I`
> are labelled by the lower indices `J` and `I` they contract with.

```lean
lemma toMatrix_inverseT {c : Fin 2 → C} (hbar : S.bar (c 0) = c 1) (M : S.Tensor c) :
    toMatrix (S.inverseT M hbar) =
      (S.toSquareMatrix M hbar)⁻¹.submatrix
        (Equiv.cast (hbar ▸ S.barIdx_eq (c 0)) ∘
          (dualIdxEquiv (rfl : S.τ (c 1) = S.τ (c 1))).symm)
        (dualIdxEquiv (S.τ_τ_apply (c 0)))
```

**`ConjTensorSpecies.toSquareMatrix_inverseT`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Inverse.lean#L103).

> The matrix `(g^{J̄I})`, row `J` from the first, barred index and column `I` from the second, is
> `(g_{IJ̄})⁻¹`.

```lean
lemma toSquareMatrix_inverseT {c : Fin 2 → C} (hbar : S.bar (c 0) = c 1) (M : S.Tensor c) :
    S.toSquareMatrix (S.inverseT M hbar) (S.bar_tau_of_bar hbar) =
      (S.toSquareMatrix M hbar)⁻¹.submatrix
        (Equiv.cast (hbar ▸ S.barIdx_eq (c 0)) ∘
          (dualIdxEquiv (rfl : S.τ (c 1) = S.τ (c 1))).symm)
        (Equiv.cast (hbar ▸ S.barIdx_eq (c 0)) ∘
          (dualIdxEquiv (rfl : S.τ (c 1) = S.τ (c 1))).symm)
```

**`ConjTensorSpecies.isSymm_toSesqForm_inverseT`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Inverse.lean#L121).

> The inverse of a Hermitian tensor is Hermitian. If `(g_{IJ̄})* = g_{JĪ}`, then
> `(g^{J̄I})* = g^{ĪJ}`.

```lean
lemma isSymm_toSesqForm_inverseT {x y : C} {c : Fin 2 → C} (hbar : S.bar (c 0) = c 1)
    (hx : S.τ x = c 0) (hy : S.τ y = S.τ (c 1)) {M : S.Tensor c}
    (hM : (S.toSesqForm x M hbar hx).IsSymm) :
    (S.toSesqForm y (S.inverseT M hbar) (S.bar_tau_of_bar hbar) hy).IsSymm
```

## B. Positive-definiteness

> Over a field, the matrix `(g_{IJ̄})` of a positive-definite `g` is invertible
> (`isUnit_det_toSquareMatrix_of_isPosDef`), so `g` has a true inverse and the contraction laws of C
> hold for it. That inverse is again positive-definite (`isPosDef_toSesqForm_inverseT`).

**`ConjTensorSpecies.isPosDef_toSesqForm_inverseT`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Inverse.lean#L149).

> The inverse of a positive-definite tensor is positive-definite, so `g^{J̄I} t_J̄ t̄_I > 0` for
> every covector `t ≠ 0`.

```lean
lemma isPosDef_toSesqForm_inverseT {x y : C} {c : Fin 2 → C} (hbar : S.bar (c 0) = c 1)
    (hx : S.τ x = c 0) (hy : S.τ y = S.τ (c 1)) {M : S.Tensor c}
    (hM : (S.toSesqForm x M hbar hx).IsPosDef) :
    (S.toSesqForm y (S.inverseT M hbar) (S.bar_tau_of_bar hbar) hy).IsPosDef
```

## C. The contraction laws

> When the matrix `(g_{IJ̄})` is invertible, `g^{J̄I}` satisfies both contraction laws, and it is the
> only tensor that satisfies the first. The unit tensor `δ` is defined over `RCLike` scalars, so
> sections C and D use them.

**`ConjTensorSpecies.contractInnerT_inverseT`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Inverse.lean#L180).

> If the matrix `(g_{IJ̄})` is invertible, `g_{IJ̄} g^{J̄K} = δ_I^K`. The first colour of the unit
> tensor is renamed from `τ (τ (cs 0))` to `cs 0`.

```lean
lemma contractInnerT_inverseT {cs : Fin 2 → C} (hbar : S.bar (cs 0) = cs 1) (M : S.Tensor cs)
    (hM : IsUnit (S.toSquareMatrix M hbar).det) :
    contractInnerT rfl M (S.inverseT M hbar) =
      permT id (IsReindexing.unitTensor_of_tau_eq (S.τ_τ_apply (cs 0)))
        (unitTensor (S := S.toTensorSpecies) (S.τ (cs 0)))
```

**`ConjTensorSpecies.inverseT_contractInnerT`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Inverse.lean#L199).

> If the matrix `(g_{IJ̄})` is invertible, `g^{J̄I} g_{IK̄} = δ^J̄_K̄`.

```lean
lemma inverseT_contractInnerT {cs : Fin 2 → C} (hbar : S.bar (cs 0) = cs 1) (M : S.Tensor cs)
    (hM : IsUnit (S.toSquareMatrix M hbar).det) :
    contractInnerT (S.τ_τ_apply (cs 0)) (S.inverseT M hbar) M =
      unitTensor (S := S.toTensorSpecies) (cs 1)
```

**`ConjTensorSpecies.eq_inverseT_of_contractInnerT_eq_unitTensor`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Inverse.lean#L208).

> If `(g_{IJ̄})` is invertible and `g_{IJ̄} t^{J̄K} = δ_I^K`, then `t` is the inverse
> `g^{J̄K}`.

```lean
lemma eq_inverseT_of_contractInnerT_eq_unitTensor {cs : Fin 2 → C} (hbar : S.bar (cs 0) = cs 1)
    (M : S.Tensor cs) (hM : IsUnit (S.toSquareMatrix M hbar).det)
    {t : S.Tensor ![S.τ (cs 1), S.τ (cs 0)]}
    (ht : contractInnerT rfl M t =
      permT id (IsReindexing.unitTensor_of_tau_eq (S.τ_τ_apply (cs 0)))
        (unitTensor (S := S.toTensorSpecies) (S.τ (cs 0)))) :
    t = S.inverseT M hbar
```

## D. Changing an index to its conjugate dual

> When the matrix `(g_{IJ̄})` is invertible, contracting an index `I` of a tensor with `g` changes it
> to its conjugate dual `J̄`, and contracting with `g^{J̄I}` changes it back. The two contraction laws
> of C make these mutually inverse. For a metric `g_{IJ̄}` with lower indices this lowers an index.
> If `g` has upper indices, the same map raises one.

**`ConjTensorSpecies.toConjDualAtIndex`**, a def, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Inverse.lean#L233).

> The linear equivalence that contracts slot `i` of a tensor with the first index of `M`, when
> the matrix `(M_{IJ̄})` is invertible. Slot `i` changes from `τ (cs 0)` to its conjugate dual
> `cs 1`, and the inverse contracts with `inverseT M`. For a metric `g_{IJ̄}` this lowers an
> unbarred index to a barred one, `t_{J̄} = g_{IJ̄} t^I`.

```lean
def toConjDualAtIndex {cs : Fin 2 → C} (M : S.Tensor cs) (hbar : S.bar (cs 0) = cs 1)
    (hM : IsUnit (S.toSquareMatrix M hbar).det) :
    {n : ℕ} → {c : Fin n → C} → (i : Fin n) → (he : c i = S.τ (cs 0)) →
      S.Tensor c ≃ₗ[k] S.Tensor (Function.update c i (cs 1))
```

**`ConjTensorSpecies.toConjDualAtIndex_apply`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Inverse.lean#L245).

> `toConjDualAtIndex` is the contraction `crossToSlot` of slot `i` with the first index of `M`.

```lean
lemma toConjDualAtIndex_apply {nA : ℕ} {c : Fin (nA + 1) → C} {cs : Fin 2 → C} (M : S.Tensor cs)
    (hbar : S.bar (cs 0) = cs 1) (hM : IsUnit (S.toSquareMatrix M hbar).det)
    (i : Fin (nA + 1)) (he : c i = S.τ (cs 0)) (t : S.Tensor c) :
    S.toConjDualAtIndex M hbar hM i he t =
      crossToSlot i 0 ((congrArg S.τ he).trans (S.τ_τ_apply (cs 0))) M t
```

**`ConjTensorSpecies.toConjDualAtIndex_symm_apply`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Inverse.lean#L255).

> The inverse of `toConjDualAtIndex` is the contraction `crossToSlotInv` of slot `i` with the
> first index of `inverseT M`.

```lean
lemma toConjDualAtIndex_symm_apply {nA : ℕ} {c : Fin (nA + 1) → C} {cs : Fin 2 → C}
    (M : S.Tensor cs) (hbar : S.bar (cs 0) = cs 1) (hM : IsUnit (S.toSquareMatrix M hbar).det)
    (i : Fin (nA + 1)) (he : c i = S.τ (cs 0)) (t : S.Tensor (Function.update c i (cs 1))) :
    (S.toConjDualAtIndex M hbar hM i he).symm t =
      crossToSlotInv (S := S.toTensorSpecies) (d := cs 1) i he rfl (S.inverseT M hbar) t
```

## Depends on

- [Conjugation structure on a tensor species](conjugation-basic.md)
- [Contraction against the unit tensor](../part-03/contraction-unittensorcontraction.md)

## Sources

- [Physlib/Relativity/Tensors/Conjugation/Inverse.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Inverse.lean)
