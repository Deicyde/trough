---
declaration: module
origin: cited
lean: SULieAlgebra.adjointGellMannBasis, SULieAlgebra.adjointGellMannBasis_apply, SULieAlgebra.adjointGellMannBasis_inv, SULieAlgebra.adjointGellMannBasis_transpose_mul_self, SULieAlgebra.toMatrix_adjointℂ_gellMannBasisℂ, SULieAlgebra.adjoint_gellMannMatrices, SULieAlgebra.gellMannBasis_repr_adjoint
statement: formalized
proof: formalized
---

# The adjoint action in the Gell-Mann basis

The module `Physlib.Mathematics.Groups.SpecialUnitary.LieAlgebra.GellMann.Adjoint`, [Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Adjoint.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Adjoint.lean): 7 declarations, 7 with a docstring.

> The matrix of the adjoint action of `SU(n)` on `su(n)` in the generalized Gell-Mann basis.

## i. Overview

> The adjoint action `x ↦ g x g†` of `g ∈ SU(n)` on `su(n)` is, in the Gell-Mann basis, a real
> matrix `R(g)` with entries `re tr (λ_i g λ_j g†) / 2`. As `g ↦ R(g)` is a monoid homomorphism and
> the adjoint action preserves the contraction, `R(g)` is orthogonal (A). It acts on the Gell-Mann
> matrices as `g λ_j g† = ∑ i, R_ij(g) λ_i`, and on the coordinates in the Gell-Mann basis by matrix
> multiplication (B).

## ii. Key results

> - `SULieAlgebra.adjointGellMannBasis` : the matrix of the adjoint action in the Gell-Mann basis.
> - `SULieAlgebra.adjointGellMannBasis_transpose_mul_self` : that matrix is orthogonal.
> - `SULieAlgebra.adjoint_gellMannMatrices` : the adjoint action on the Gell-Mann matrices.

## iv. References

> * https://mathworld.wolfram.com/GeneralizedGell-MannMatrix.html

## A. The matrix of the adjoint action

**`SULieAlgebra.adjointGellMannBasis`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Adjoint.lean#L54).

> The matrix of the adjoint action of `g` in the Gell-Mann basis, a real matrix, as a monoid
> homomorphism from `SU(n)`.

```lean
noncomputable def adjointGellMannBasis {n : ℕ} :
    specialUnitaryGroup (Fin n) ℂ →* Matrix (GellMannIndex n) (GellMannIndex n) ℝ
```

**`SULieAlgebra.adjointGellMannBasis_apply`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Adjoint.lean#L59).

> The entries of the matrix of the adjoint action, `re tr (λ_i g λ_j g†) / 2`.

```lean
lemma adjointGellMannBasis_apply {n : ℕ} (g : specialUnitaryGroup (Fin n) ℂ)
    (i j : GellMannIndex n) : adjointGellMannBasis g i j =
      ((gellMannMatrices i).1 * (g.1 * (gellMannMatrices j).1 * star g.1)).trace.re / 2
```

**`SULieAlgebra.adjointGellMannBasis_inv`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Adjoint.lean#L68).

> The matrix of the adjoint action of `g⁻¹` is the transpose of that of `g`, the adjoint action
> preserving the contraction.

```lean
lemma adjointGellMannBasis_inv {n : ℕ} (g : specialUnitaryGroup (Fin n) ℂ) :
    adjointGellMannBasis g⁻¹ = (adjointGellMannBasis g)ᵀ
```

**`SULieAlgebra.adjointGellMannBasis_transpose_mul_self`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Adjoint.lean#L77).

> The matrix of the adjoint action is orthogonal.

```lean
lemma adjointGellMannBasis_transpose_mul_self {n : ℕ} (g : specialUnitaryGroup (Fin n) ℂ) :
    (adjointGellMannBasis g)ᵀ * adjointGellMannBasis g = 1
```

**`SULieAlgebra.toMatrix_adjointℂ_gellMannBasisℂ`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Adjoint.lean#L83).

> The matrix of the complex adjoint action in the complex Gell-Mann basis is the real matrix of
> the adjoint action.

```lean
lemma toMatrix_adjointℂ_gellMannBasisℂ {n : ℕ} (g : specialUnitaryGroup (Fin n) ℂ) :
    LinearMap.toMatrix gellMannBasisℂ gellMannBasisℂ (adjointℂ g) =
      (adjointGellMannBasis g).map (algebraMap ℝ ℂ)
```

## B. The adjoint action on Gell-Mann matrices and coordinates

**`SULieAlgebra.adjoint_gellMannMatrices`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Adjoint.lean#L97).

> The adjoint action on a Gell-Mann matrix is a combination of Gell-Mann matrices with
> coefficients the entries of the matrix of the adjoint action,
> `g λ_j g† = ∑ i, R_ij(g) λ_i`.

```lean
lemma adjoint_gellMannMatrices {n : ℕ} (g : specialUnitaryGroup (Fin n) ℂ) (j : GellMannIndex n) :
    adjoint g (gellMannMatrices j) = ∑ i, adjointGellMannBasis g i j • gellMannMatrices i
```

**`SULieAlgebra.gellMannBasis_repr_adjoint`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Adjoint.lean#L105).

> The adjoint action on the coordinates in the Gell-Mann basis is multiplication by the matrix of
> the adjoint action, `A^i ↦ R_ij(g) A^j`.

```lean
lemma gellMannBasis_repr_adjoint {n : ℕ} (g : specialUnitaryGroup (Fin n) ℂ)
    (x : SULieAlgebra n ℂ) :
    gellMannBasis.repr (adjoint g x) = adjointGellMannBasis g *ᵥ gellMannBasis.repr x
```

## Depends on

- [The generalized Gell-Mann matrices](specialunitary-liealgebra-gellmann-basic.md)

## Sources

- [Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Adjoint.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/GellMann/Adjoint.lean)
