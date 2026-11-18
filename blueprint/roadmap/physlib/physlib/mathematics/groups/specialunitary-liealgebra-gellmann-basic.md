---
declaration: module
origin: cited
lean: SULieAlgebra.GellMannIndex, SULieAlgebra.gellMannIndex_card, SULieAlgebra.gellMannMatrices, SULieAlgebra.gellMannMatrices_symm_isSymm, SULieAlgebra.gellMannMatrices_antisymm_transpose, SULieAlgebra.gellMannMatrices_diag_isDiag, SULieAlgebra.gellMannMatrices_symm_val_eq, SULieAlgebra.gellMannMatrices_antisymm_val_eq
statement: formalized
proof: formalized
---

# The generalized Gell-Mann matrices (Physlib)

The module `Physlib.Mathematics.Groups.SpecialUnitary.LieAlgebra.GellMann.Basic`, [Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean): 32 declarations, 17 with a docstring.

> The generalized Gell-Mann matrices, orthogonality, the basis and the structure constants they form.

## i. Overview

> The generalized Gell-Mann matrices are the standard basis of `su(n)`, generalizing the Pauli
> matrices (`n = 2`) and the Gell-Mann matrices (`n = 3`). They are labelled by `GellMannIndex n`,
> which has `n² - 1` elements, of three kinds (A):
>
> - for `p < q` the symmetric matrix `E_pq + E_qp`,
> - for `p < q` the antisymmetric matrix `-i E_pq + i E_qp`,
> - for `1 ≤ m ≤ n - 1` the diagonal matrix `√(2 / (m (m + 1))) (E_00 + ⋯ + E_(m-1)(m-1) - m E_mm)`.
>
> They are orthogonal under the contraction, `adjointContr (λ_i ⊗ λ_j) = tr (λ_i λ_j) = 2 δ_ij`, and
> so linearly independent (B).
>
> As there are as many as the dimension `n² - 1` of `su(n)`, they form a basis, whose coordinates
> are the contractions `adjointContr (λ_i ⊗ x) / 2`, and its base change is a basis of the
> complexification (C). In this basis the bracket defines the structure constants
> `[λ_a, λ_b] = 2 i f_abc λ_c`, which are totally antisymmetric (D).

## ii. Key results

> - `SULieAlgebra.GellMannIndex` : the labels of the generalized Gell-Mann matrices.
> - `SULieAlgebra.gellMannMatrices` : the generalized Gell-Mann matrices.
> - `SULieAlgebra.adjointContr_gellMannMatrices` : the Gell-Mann matrices are orthogonal.
> - `SULieAlgebra.gellMannBasis` : the Gell-Mann basis of `su(n)`.
> - `SULieAlgebra.gellMannBasisℂ` : the Gell-Mann basis of the complexification of `su(n)`.
> - `SULieAlgebra.gellMannStructureConst` : the structure constants, `[λ_a, λ_b] = 2 i f_abc λ_c`.

## iv. References

> * https://mathworld.wolfram.com/GeneralizedGell-MannMatrix.html

## A. The indexing type of the Gell-Mann matrices

**`SULieAlgebra.GellMannIndex`**, an inductive, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean#L80).

> The indexing type of the Gell-Mann matrices.

```lean
inductive GellMannIndex (n : ℕ)
  | symm (p : Fin n) (q : Fin n) (h : p < q) : GellMannIndex n
  | antisymm (p : Fin n) (q : Fin n) (h : p < q) : GellMannIndex n
  | diag (l : Fin (n - 1)) : GellMannIndex n
deriving DecidableEq, Repr, Fintype
```

### A.1. The cardinality of `GellMannIndex`

**`SULieAlgebra.gellMannIndex_card`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean#L94).

> There are `n² - 1` generalized Gell-Mann matrices: `n (n - 1) / 2` symmetric ones, as many
> antisymmetric ones, and `n - 1` diagonal ones.

```lean
lemma gellMannIndex_card {n : ℕ} : Fintype.card (GellMannIndex n) = n ^ 2 - 1
```

## B. The generalized Gell-Mann matrices

**`SULieAlgebra.gellMannMatrices`**, a def, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean#L143).

> The generalized Gell-Mann matrices, as elements of `su(n)`:
>
> - for `p < q`, the symmetric matrix `E_pq + E_qp`,
> - for `p < q`, the antisymmetric matrix `-i E_pq + i E_qp`,
> - for `l : Fin (n - 1)`, with `m = l + 1`, the diagonal matrix
>   `√(2 / (m (m + 1))) (E_00 + ⋯ + E_(m-1)(m-1) - m E_mm)`.

```lean
noncomputable def gellMannMatrices {n : ℕ} : GellMannIndex n → SULieAlgebra n ℂ
```

### B.1. Symmetry properties

**`SULieAlgebra.gellMannMatrices_symm_isSymm`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean#L178).

> The symmetric generalized Gell-Mann matrices are symmetric.

```lean
lemma gellMannMatrices_symm_isSymm {n : ℕ} (p q : Fin n) (h : p < q) :
    Matrix.IsSymm (gellMannMatrices (.symm p q h)).1
```

**`SULieAlgebra.gellMannMatrices_antisymm_transpose`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean#L183).

> The antisymmetric generalized Gell-Mann matrices are antisymmetric.

```lean
lemma gellMannMatrices_antisymm_transpose {n : ℕ} (p q : Fin n) (h : p < q) :
    (gellMannMatrices (.antisymm p q h)).1ᵀ = -(gellMannMatrices (.antisymm p q h)).1
```

**`SULieAlgebra.gellMannMatrices_diag_isDiag`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean#L189).

> The diagonal generalized Gell-Mann matrices are diagonal.

```lean
lemma gellMannMatrices_diag_isDiag {n : ℕ} (l : Fin (n - 1)) :
    Matrix.IsDiag (gellMannMatrices (.diag l)).1
```

### B.2. Explicit forms

**`SULieAlgebra.gellMannMatrices_symm_val_eq`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean#L199).

```lean
lemma gellMannMatrices_symm_val_eq {n : ℕ} (p q : Fin n) (h : p < q) :
    (gellMannMatrices (.symm p q h)).1 = single p q 1 + single q p 1
```

**`SULieAlgebra.gellMannMatrices_antisymm_val_eq`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean#L202).

```lean
lemma gellMannMatrices_antisymm_val_eq {n : ℕ} (p q : Fin n) (h : p < q) :
    (gellMannMatrices (.antisymm p q h)).1 = single p q (-Complex.I) + single q p Complex.I
```

**`SULieAlgebra.gellMannMatrices_diag_val_eq`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean#L206).

```lean
lemma gellMannMatrices_diag_val_eq {n : ℕ} (l : Fin (n - 1)) :
    (gellMannMatrices (.diag l)).1 = diagonal fun x => (√(2 / ((l.1 + 1) * (l.1 + 2))) : ℝ) *
      if x.1 ≤ l.1 then 1 else if x.1 = l.1 + 1 then -(l.1 + 1 : ℂ) else 0
```

### B.3. Orthogonality

#### B.3.1. Between different types

**`SULieAlgebra.adjointContr_gellMannMatrices_symm_antisymm_eq_zero`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean#L223).

```lean
lemma adjointContr_gellMannMatrices_symm_antisymm_eq_zero {n : ℕ} (p q : Fin n) (h : p < q)
    (p' q' : Fin n) (h' : p' < q') :
    adjointContr (gellMannMatrices (.symm p q h) ⊗ₜ gellMannMatrices (.antisymm p' q' h')) = 0
```

**`SULieAlgebra.adjointContr_gellMannMatrices_symm_diag_eq_zero`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean#L231).

```lean
lemma adjointContr_gellMannMatrices_symm_diag_eq_zero {n : ℕ} (p q : Fin n) (h : p < q)
    (l : Fin (n - 1)) :
    adjointContr (gellMannMatrices (.symm p q h) ⊗ₜ gellMannMatrices (.diag l)) = 0
```

**`SULieAlgebra.adjointContr_gellMannMatrices_antisymm_symm_eq_zero`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean#L237).

```lean
lemma adjointContr_gellMannMatrices_antisymm_symm_eq_zero {n : ℕ} (p q : Fin n) (h : p < q)
    (p' q' : Fin n) (h' : p' < q') :
    adjointContr (gellMannMatrices (.antisymm p q h) ⊗ₜ gellMannMatrices (.symm p' q' h')) = 0
```

**`SULieAlgebra.adjointContr_gellMannMatrices_antisymm_diag_eq_zero`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean#L245).

```lean
lemma adjointContr_gellMannMatrices_antisymm_diag_eq_zero {n : ℕ} (p q : Fin n) (h : p < q)
    (l : Fin (n - 1)) :
    adjointContr (gellMannMatrices (.antisymm p q h) ⊗ₜ gellMannMatrices (.diag l)) = 0
```

**`SULieAlgebra.adjointContr_gellMannMatrices_diag_symm_eq_zero`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean#L251).

```lean
lemma adjointContr_gellMannMatrices_diag_symm_eq_zero {n : ℕ} (l : Fin (n - 1)) (p q : Fin n)
    (h : p < q) :
    adjointContr (gellMannMatrices (.diag l) ⊗ₜ gellMannMatrices (.symm p q h)) = 0
```

**`SULieAlgebra.adjointContr_gellMannMatrices_diag_antisymm_eq_zero`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean#L257).

```lean
lemma adjointContr_gellMannMatrices_diag_antisymm_eq_zero {n : ℕ} (l : Fin (n - 1)) (p q : Fin n)
    (h : p < q) :
    adjointContr (gellMannMatrices (.diag l) ⊗ₜ gellMannMatrices (.antisymm p q h)) = 0
```

#### B.3.2. Between the same type

**`SULieAlgebra.adjointContr_gellMannMatrices_symm_orthogonal`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean#L269).

```lean
lemma adjointContr_gellMannMatrices_symm_orthogonal {n : ℕ} (p q : Fin n) (h : p < q)
    (p' q' : Fin n) (h' : p' < q') :
    adjointContr (gellMannMatrices (.symm p q h) ⊗ₜ gellMannMatrices (.symm p' q' h')) =
      if p = p' ∧ q = q' then 2 else 0
```

**`SULieAlgebra.adjointContr_gellMannMatrices_antisymm_orthogonal`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean#L279).

```lean
lemma adjointContr_gellMannMatrices_antisymm_orthogonal {n : ℕ} (p q : Fin n) (h : p < q)
    (p' q' : Fin n) (h' : p' < q') :
    adjointContr (gellMannMatrices (.antisymm p q h) ⊗ₜ gellMannMatrices (.antisymm p' q' h')) =
      if p = p' ∧ q = q' then 2 else 0
```

**`SULieAlgebra.adjointContr_gellMannMatrices_diag_self`**, a lemma, [line 290](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean#L290).

> The diagonal Gell-Mann matrices are normalized, `tr (λ_l λ_l) = 2`.

```lean
lemma adjointContr_gellMannMatrices_diag_self {n : ℕ} (l : Fin (n - 1)) :
    adjointContr (gellMannMatrices (.diag l) ⊗ₜ gellMannMatrices (.diag l)) = 2
```

**`SULieAlgebra.adjointContr_gellMannMatrices_diag_orthogonal`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean#L316).

```lean
lemma adjointContr_gellMannMatrices_diag_orthogonal {n : ℕ} (l l' : Fin (n - 1)) :
    adjointContr (gellMannMatrices (.diag l) ⊗ₜ gellMannMatrices (.diag l')) =
      if l = l' then 2 else 0
```

#### B.3.3. The full orthogonality relation

**`SULieAlgebra.adjointContr_gellMannMatrices`**, a lemma, [line 345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean#L345).

> The generalized Gell-Mann matrices are orthogonal under the trace pairing,
> with normalization `tr (λ_i λ_j) = 2 δ_ij`.

```lean
lemma adjointContr_gellMannMatrices {n : ℕ} (i j : GellMannIndex n) :
    adjointContr (gellMannMatrices i ⊗ₜ gellMannMatrices j) = if i = j then 2 else 0
```

### B.4. Linear independence

**`SULieAlgebra.linearIndependent_gellMannMatrices`**, a lemma, [line 367](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean#L367).

> The generalized Gell-Mann matrices are linearly independent over `ℝ`, being orthogonal under
> the contraction.

```lean
lemma linearIndependent_gellMannMatrices {n : ℕ} :
    LinearIndependent ℝ (gellMannMatrices (n := n))
```

## C. The Gell-Mann basis

### C.1. The basis of `su(n)`

**`SULieAlgebra.gellMannBasis`**, a def, [line 386](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean#L386).

> The generalized Gell-Mann basis of `su(n)`.

```lean
noncomputable def gellMannBasis {n : ℕ} : Module.Basis (GellMannIndex n) ℝ (SULieAlgebra n ℂ)
```

**`SULieAlgebra.gellMannBasis_apply`**, a lemma, [line 391](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean#L391).

```lean
lemma gellMannBasis_apply {n : ℕ} (i : GellMannIndex n) : gellMannBasis i = gellMannMatrices i
```

**`SULieAlgebra.gellMannBasis_repr_apply`**, a lemma, [line 396](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean#L396).

> The coordinates in the Gell-Mann basis are the contractions with the Gell-Mann matrices,
> `x = ∑ (adjointContr (λ_i ⊗ x) / 2) λ_i`.

```lean
lemma gellMannBasis_repr_apply {n : ℕ} (x : SULieAlgebra n ℂ) (i : GellMannIndex n) :
    gellMannBasis.repr x i = adjointContr (gellMannMatrices i ⊗ₜ x) / 2
```

### C.2. The basis of the complexification

**`SULieAlgebra.gellMannBasisℂ`**, a def, [line 411](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean#L411).

> The generalized Gell-Mann basis `1 ⊗ λ_i` of the complexification `ℂ ⊗[ℝ] su(n)`.

```lean
noncomputable def gellMannBasisℂ {n : ℕ} : Module.Basis (GellMannIndex n) ℂ (Complexification n)
```

**`SULieAlgebra.gellMannBasisℂ_apply`**, a lemma, [line 414](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean#L414).

```lean
lemma gellMannBasisℂ_apply {n : ℕ} (i : GellMannIndex n) :
    gellMannBasisℂ i = 1 ⊗ₜ gellMannMatrices i
```

**`SULieAlgebra.toMatrixℂ_gellMannBasisℂ`**, a lemma, [line 419](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean#L419).

```lean
lemma toMatrixℂ_gellMannBasisℂ {n : ℕ} (i : GellMannIndex n) :
    toMatrixℂ (gellMannBasisℂ i) = (gellMannMatrices i).1
```

**`SULieAlgebra.gellMannBasisℂ_repr_apply`**, a lemma, [line 425](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean#L425).

> The coordinates in the complex Gell-Mann basis are the contractions with the Gell-Mann
> matrices, `A = ∑ (adjointℂContr (λ_i ⊗ A) / 2) λ_i`.

```lean
lemma gellMannBasisℂ_repr_apply {n : ℕ} (A : Complexification n) (i : GellMannIndex n) :
    gellMannBasisℂ.repr A i = adjointℂContr (gellMannBasisℂ i ⊗ₜ A) / 2
```

## D. The structure constants

**`SULieAlgebra.gellMannStructureConst`**, a def, [line 443](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean#L443).

> The structure constants of `su(n)` in the Gell-Mann basis, with the physics normalisation
> `[λ_a, λ_b] = 2 i ∑ c, f_abc λ_c`, read off by the contraction:
> `f_abc = tr ([λ_a, λ_b] λ_c) / (4 i) = -(1 / 4) adjointContr (⁅λ_a, λ_b⁆ ⊗ λ_c)`.

```lean
noncomputable def gellMannStructureConst {n : ℕ} (a b c : GellMannIndex n) : ℝ
```

**`SULieAlgebra.lie_gellMannMatrices`**, a lemma, [line 448](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean#L448).

> The bracket of two Gell-Mann matrices in terms of the structure constants,
> `⁅λ_a, λ_b⁆ = -2 ∑ c, f_abc λ_c`, the bracket `⁅x, y⁆ = i (x y - y x)` carrying a factor `i`.

```lean
lemma lie_gellMannMatrices {n : ℕ} (a b : GellMannIndex n) :
    ⁅gellMannMatrices a, gellMannMatrices b⁆ =
      ∑ c, (-2 * gellMannStructureConst a b c) • gellMannMatrices c
```

**`SULieAlgebra.gellMannStructureConst_swap`**, a lemma, [line 457](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean#L457).

> The structure constants are antisymmetric in their first two indices.

```lean
lemma gellMannStructureConst_swap {n : ℕ} (a b c : GellMannIndex n) :
    gellMannStructureConst b a c = -gellMannStructureConst a b c
```

**`SULieAlgebra.gellMannStructureConst_cycle`**, a lemma, [line 466](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean#L466).

> The structure constants are invariant under cyclic permutations of their indices, the
> contraction being invariant under the bracket. With `gellMannStructureConst_swap`, they are
> totally antisymmetric.

```lean
lemma gellMannStructureConst_cycle {n : ℕ} (a b c : GellMannIndex n) :
    gellMannStructureConst b c a = gellMannStructureConst a b c
```

## Depends on

- [The contraction of adjoint indices of `SU(n)`](specialunitary-liealgebra-contractions.md)

## Sources

- [Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Basic.lean)
