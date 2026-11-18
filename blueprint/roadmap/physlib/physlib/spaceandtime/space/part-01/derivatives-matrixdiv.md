---
declaration: module
origin: cited
lean: Space.matrixDiv, Space.matrixDiv_apply, Space.matrixDiv_zero, Space.matrixDiv_const, Space.matrixDiv_add, Space.matrixDiv_smul
statement: formalized
proof: formalized
---

# Matrix divergence on Space

The module `Physlib.SpaceAndTime.Space.Derivatives.MatrixDiv`, [Physlib/SpaceAndTime/Space/Derivatives/MatrixDiv.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MatrixDiv.lean): 6 declarations, 1 with a docstring.

## i. Overview

> In this module we define the matrix divergence operator on matrix-valued
> functions from `Space d`.
>
> For a field `T : Space d → Matrix (Fin d) (Fin d) ℝ`, the matrix divergence is
> the vector field whose `i`th component is
>
> `∑ j, ∂[j] (fun x => T x i j) x`.

## ii. Key results

> - `matrixDiv` : The divergence of a matrix-valued function on `Space d`.

## iv. References

> * None.

## A. The matrix divergence on functions

**`Space.matrixDiv`**, a def, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MatrixDiv.lean#L60).

> The divergence of a matrix-valued spatial field.
>
> For a field `T : Space d → Matrix (Fin d) (Fin d) ℝ`, `matrixDiv T` is the
> vector field whose `i`th component is
>
> `∑ j, ∂[j] (fun x => T x i j) x`.

```lean
noncomputable def matrixDiv (d : ℕ) (T : Space d → Matrix (Fin d) (Fin d) ℝ) :
    Space d → EuclideanSpace ℝ (Fin d)
```

### A.1. Basic equalities

**`Space.matrixDiv_apply`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MatrixDiv.lean#L71).

```lean
lemma matrixDiv_apply (d : ℕ) (T : Space d → Matrix (Fin d) (Fin d) ℝ)
    (x : Space d) (i : Fin d) :
    matrixDiv d T x i = ∑ j, ∂[j] (fun x => T x i j) x
```

### A.2. The matrix divergence on the zero function

**`Space.matrixDiv_zero`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MatrixDiv.lean#L83).

```lean
lemma matrixDiv_zero (d : ℕ) :
    matrixDiv d (0 : Space d → Matrix (Fin d) (Fin d) ℝ) = 0
```

### A.3. The matrix divergence on a constant function

**`Space.matrixDiv_const`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MatrixDiv.lean#L96).

```lean
lemma matrixDiv_const (d : ℕ) (T : Matrix (Fin d) (Fin d) ℝ) :
    matrixDiv d (fun _ : Space d => T) = 0
```

### A.4. The matrix divergence distributes over addition

**`Space.matrixDiv_add`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MatrixDiv.lean#L108).

```lean
lemma matrixDiv_add (d : ℕ) (T1 T2 : Space d → Matrix (Fin d) (Fin d) ℝ)
    (hT1 : Differentiable ℝ T1) (hT2 : Differentiable ℝ T2) :
    matrixDiv d (T1 + T2) = matrixDiv d T1 + matrixDiv d T2
```

### A.5. The matrix divergence distributes over scalar multiplication

**`Space.matrixDiv_smul`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MatrixDiv.lean#L131).

```lean
lemma matrixDiv_smul (d : ℕ) (T : Space d → Matrix (Fin d) (Fin d) ℝ) (k : ℝ)
    (hT : Differentiable ℝ T) :
    matrixDiv d (k • T) = k • matrixDiv d T
```

## Depends on

- [Divergence on Space](derivatives-div.md)

## Sources

- [Physlib/SpaceAndTime/Space/Derivatives/MatrixDiv.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MatrixDiv.lean)
