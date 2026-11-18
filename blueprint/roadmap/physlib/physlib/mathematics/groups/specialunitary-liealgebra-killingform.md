---
declaration: module
origin: cited
lean: SULieAlgebra.killingForm_eq_trace, SULieAlgebra.adjointℂContr_eq_killingForm, SULieAlgebra.adjointContr_eq_killingForm
statement: formalized
proof: formalized
---

# The Killing form of `su(n)`

The module `Physlib.Mathematics.Groups.SpecialUnitary.LieAlgebra.KillingForm`, [Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/KillingForm.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/KillingForm.lean): 3 declarations, 3 with a docstring.

> The Killing form of `su(n)` and its complexification, and its relation to the adjoint contraction.

## i. Overview

> The Killing form `K(A, B) = tr (ad A ∘ ad B)` of the complexification is computed by transporting
> `ad A ∘ ad B` to the matrices, where it is `M ↦ -[A, [B, M]]`, the sign coming from the factor `i`
> in the bracket. Its trace is `-2n tr (A B)` (A).
>
> The contractions `adjointℂContr` and `adjointContr` of adjoint indices are therefore `-1 / (2n)`
> times the Killing forms of the complexification and of `su(n)` (B).

## ii. Key results

> - `SULieAlgebra.killingForm_eq_trace` : the Killing form of the complexification is `-2n` times
>   the trace form.
> - `SULieAlgebra.adjointℂContr_eq_killingForm` : the complex contraction is `-1 / (2n)` times the
>   Killing form.
> - `SULieAlgebra.adjointContr_eq_killingForm` : the real contraction is `-1 / (2n)` times the
>   Killing form.

## iv. References

> * None.

## A. The Killing form as a trace

**`SULieAlgebra.killingForm_eq_trace`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/KillingForm.lean#L61).

> The Killing form of the complexification is the trace form of the matrices,
> `K(A, B) = -2n tr (A B)`. The sign comes from the factor `i` in the bracket, which makes
> `ad A ∘ ad B` the map `M ↦ -[A, [B, M]]`.

```lean
lemma killingForm_eq_trace {n : ℕ} (A B : Complexification n) :
    killingForm ℂ (Complexification n) A B = - (2 * n) * (toMatrixℂ A * toMatrixℂ B).trace
```

## B. The contraction as the Killing form

**`SULieAlgebra.adjointℂContr_eq_killingForm`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/KillingForm.lean#L90).

> The contraction is the Killing form on the complexified Lie
> algebra, up to a factor of `-1/(2n)`.

```lean
lemma adjointℂContr_eq_killingForm {n : ℕ} (A B : Complexification n) :
    adjointℂContr (A ⊗ₜ B) = -(1 / (2 * (n : ℂ))) * killingForm ℂ (Complexification n) A B
```

**`SULieAlgebra.adjointContr_eq_killingForm`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/KillingForm.lean#L99).

> The contraction is the Killing form on the Lie algebra, up to a factor of `-1/(2n)`.

```lean
lemma adjointContr_eq_killingForm {n : ℕ} (x y : SULieAlgebra n ℂ) :
    adjointContr (x ⊗ₜ y) = -(1 / (2 * (n : ℝ))) * killingForm ℝ (SULieAlgebra n ℂ) x y
```

## Depends on

- [The contraction of adjoint indices of `SU(n)`](specialunitary-liealgebra-contractions.md)

## Sources

- [Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/KillingForm.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/KillingForm.lean)
