---
declaration: module
origin: cited
lean: DifferentiableAt.matrix_transpose, Time.deriv_matrix_mul, Time.deriv_matrix_transpose, Time.deriv_matrix_apply
statement: formalized
proof: formalized
---

# Time derivatives of matrix-valued functions

The module `Physlib.SpaceAndTime.Time.MatrixDerivatives`, [Physlib/SpaceAndTime/Time/MatrixDerivatives.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/MatrixDerivatives.lean): 4 declarations, 4 with a docstring.

> General lemmas on the time derivative `∂ₜ` of square-matrix-valued functions of time: a product
> rule, the commutation of the derivative with transpose, and the commutation of the derivative with
> taking a matrix entry. These are the tools needed to differentiate a path of matrices.
>
> They rely on the (opt-in) operator-norm structure on matrices — activated here as local instances —
> only to invoke the product rule and to view transpose (through `Matrix.transposeLinearEquiv`) as a
> continuous linear map. Since all norms on a fixed finite-dimensional space induce the same topology,
> differentiability does not depend on this choice.

**`DifferentiableAt.matrix_transpose`**, a lemma, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/MatrixDerivatives.lean#L37).

> The transpose of a differentiable matrix-valued function is differentiable
> (cf. `Continuous.matrix_transpose`).

```lean
lemma DifferentiableAt.matrix_transpose {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
    {A : E → Matrix (Fin d) (Fin d) ℝ} {t : E} (hA : DifferentiableAt ℝ A t) :
    DifferentiableAt ℝ (fun s => (A s)ᵀ) t
```

**`Time.deriv_matrix_mul`**, a lemma, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/MatrixDerivatives.lean#L46).

> Product rule for the time derivative of a product of matrix-valued functions.

```lean
lemma deriv_matrix_mul (A B : Time → Matrix (Fin d) (Fin d) ℝ) (t : Time)
    (hA : DifferentiableAt ℝ A t) (hB : DifferentiableAt ℝ B t) :
    ∂ₜ (fun s => A s * B s) t = A t * ∂ₜ B t + ∂ₜ A t * B t
```

**`Time.deriv_matrix_transpose`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/MatrixDerivatives.lean#L55).

> The time derivative commutes with transpose.

```lean
lemma deriv_matrix_transpose (A : Time → Matrix (Fin d) (Fin d) ℝ) (t : Time)
    (hA : DifferentiableAt ℝ A t) :
    ∂ₜ (fun s => (A s)ᵀ) t = (∂ₜ A t)ᵀ
```

**`Time.deriv_matrix_apply`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/MatrixDerivatives.lean#L66).

> The time derivative commutes with taking a matrix entry.

```lean
lemma deriv_matrix_apply (A : Time → Matrix (Fin d) (Fin d) ℝ) (t : Time)
    (hA : DifferentiableAt ℝ A t) (i j : Fin d) :
    ∂ₜ (fun s => A s i j) t = (∂ₜ A t) i j
```

## Depends on

- [Time Derivatives](derivatives.md)

## Sources

- [Physlib/SpaceAndTime/Time/MatrixDerivatives.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/MatrixDerivatives.lean)
