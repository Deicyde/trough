---
declaration: module
origin: cited
lean: ProbabilisticTheory.BoundedSesquilinearForm, ProbabilisticTheory.BoundedSesquilinearForm.boundConstant, ProbabilisticTheory.BoundedSesquilinearForm.boundConstant_spec, ProbabilisticTheory.BoundedSesquilinearForm.continuous, ProbabilisticTheory.BoundedSesquilinearForm.continuous_apply, ProbabilisticTheory.BoundedSesquilinearForm.operator, ProbabilisticTheory.BoundedSesquilinearForm.operator_inner
statement: formalized
proof: formalized
---

# Bounded sesquilinear forms

The module `PhyslibAlpha.ProbabilisticTheory.WStarAlgebra.BoundedSesquilinearForm`, [PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/BoundedSesquilinearForm.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/BoundedSesquilinearForm.lean): 7 declarations, 4 with a docstring.

> A bounded sesquilinear form on a Hilbert space is represented by a bounded operator.

## i. Overview

> A bounded sesquilinear form `B` on a Hilbert space, conjugate-linear in the first argument, is
> represented by a bounded operator `T` with `⟪y, T x⟫ = conj (B x y)`.

## ii. Key results

> - `BoundedSesquilinearForm` : a bounded sesquilinear form.
> - `BoundedSesquilinearForm.operator` : the representing operator.
> - `BoundedSesquilinearForm.operator_inner` : `⟪y, T x⟫ = conj (B x y)`.

## iv. References

> * None.

## A. Bounded sesquilinear forms

**`ProbabilisticTheory.BoundedSesquilinearForm`**, a structure, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/BoundedSesquilinearForm.lean#L56).

> A bounded sesquilinear form in the orientation expected by Mathlib's Riesz representation
> theorem.

```lean
structure BoundedSesquilinearForm (H : Type*) [NormedAddCommGroup H] [InnerProductSpace ℂ H]
    [CompleteSpace H] where
  /-- The underlying sesquilinear form. -/
  form : H →ₛₗ[starRingEnd ℂ] H →ₗ[ℂ] ℂ
  /-- The form is bounded by some constant `C`. -/
  bound : ∃ C : ℝ, ∀ x y, ‖form x y‖ ≤ C * ‖x‖ * ‖y‖
```

**`ProbabilisticTheory.BoundedSesquilinearForm.boundConstant`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/BoundedSesquilinearForm.lean#L68).

> A norm bound witnessing `B.bound`.

```lean
noncomputable def boundConstant : ℝ
```

**`ProbabilisticTheory.BoundedSesquilinearForm.boundConstant_spec`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/BoundedSesquilinearForm.lean#L70).

```lean
lemma boundConstant_spec : ∀ x y, ‖B.form x y‖ ≤ B.boundConstant * ‖x‖ * ‖y‖
```

**`ProbabilisticTheory.BoundedSesquilinearForm.continuous`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/BoundedSesquilinearForm.lean#L74).

> The continuous version of a bounded sesquilinear form.

```lean
noncomputable def continuous : H →L⋆[ℂ] H →L[ℂ] ℂ
```

**`ProbabilisticTheory.BoundedSesquilinearForm.continuous_apply`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/BoundedSesquilinearForm.lean#L78).

```lean
lemma continuous_apply (x y : H) : B.continuous x y = B.form x y
```

## B. The representing operator

**`ProbabilisticTheory.BoundedSesquilinearForm.operator`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/BoundedSesquilinearForm.lean#L88).

> The unique bounded operator represented by `B`.

```lean
noncomputable def operator : H →L[ℂ] H
```

**`ProbabilisticTheory.BoundedSesquilinearForm.operator_inner`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/BoundedSesquilinearForm.lean#L91).

```lean
lemma operator_inner (x y : H) :
    ⟪y, B.operator x⟫_ℂ = starRingEnd ℂ (B.form x y)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/BoundedSesquilinearForm.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/BoundedSesquilinearForm.lean)
