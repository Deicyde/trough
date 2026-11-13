---
declaration: module
origin: cited
lean: StandardModel.su2AdjointMatrix, StandardModel.su2AdjointMatrix_apply, StandardModel.sum_su2AdjointMatrix_row_mul, StandardModel.su2AdjointMatrix_inv, StandardModel.su3AdjointMatrix, StandardModel.su3AdjointMatrix_apply, StandardModel.sum_su3AdjointMatrix_row_mul, StandardModel.su3AdjointMatrix_inv
statement: formalized
proof: formalized
---

# The adjoint matrices of `SU(2)` and `SU(3)`

The module `PhyslibAlpha.Particles.StandardModel.GaugeGroup.AdjointMatrix`, [PhyslibAlpha/Particles/StandardModel/GaugeGroup/AdjointMatrix.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/AdjointMatrix.lean): 8 declarations, 7 with a docstring.

## i. Overview

> `su2AdjointMatrix U` and `su3AdjointMatrix U` are the real matrices of `X ↦ U X U⁻¹` on
> `su(2)` and `su(3)` in the Pauli and Gell-Mann bases, read off with the trace pairing
> `(X, Y) ↦ ½ tr (X Y)`. They are the `su(2)` and `su(3)` blocks of `GaugeAlgebra.adjointMatrix`,
> which gives their orthonormal rows and their transposition at `U⁻¹`.

## ii. Key results

> - `su2AdjointMatrix` : the adjoint matrix of an element of `SU(2)`: the trace pairing of the Pauli
>   basis of `su(2)` with the Pauli basis conjugated by that element
> - `su2AdjointMatrix_apply` : the entries of the adjoint matrix
> - `sum_su2AdjointMatrix_row_mul` : the rows of the adjoint matrix are orthonormal
> - `su2AdjointMatrix_inv` : the adjoint matrix of the inverse is the transpose

## iv. References

> * None.

## A. The adjoint matrix of `SU(2)`

**`StandardModel.su2AdjointMatrix`**, a def, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/AdjointMatrix.lean#L53).

> The adjoint matrix of an element of `SU(2)`: the trace pairing of the Pauli basis of
> `su(2)` with the Pauli basis conjugated by that element.

```lean
noncomputable def su2AdjointMatrix (U : specialUnitaryGroup (Fin 2) ℂ) :
    Matrix (Fin 3) (Fin 3) ℝ
```

**`StandardModel.su2AdjointMatrix_apply`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/AdjointMatrix.lean#L62).

> The entries of the adjoint matrix.

```lean
lemma su2AdjointMatrix_apply (U : specialUnitaryGroup (Fin 2) ℂ) (i j : Fin 3) :
    su2AdjointMatrix U i j
      = 2⁻¹ * (Matrix.trace (pauliMatrix (Sum.inr i) *
          (U.1 * pauliMatrix (Sum.inr j) * star U.1))).re
```

**`StandardModel.sum_su2AdjointMatrix_row_mul`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/AdjointMatrix.lean#L68).

> The rows of the adjoint matrix are orthonormal.

```lean
lemma sum_su2AdjointMatrix_row_mul (U : specialUnitaryGroup (Fin 2) ℂ) (c d : Fin 3) :
    ∑ a : Fin 3, su2AdjointMatrix U c a * su2AdjointMatrix U d a
      = if c = d then 1 else 0
```

**`StandardModel.su2AdjointMatrix_inv`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/AdjointMatrix.lean#L74).

> The adjoint matrix of the inverse is the transpose.

```lean
lemma su2AdjointMatrix_inv (U : specialUnitaryGroup (Fin 2) ℂ) (a b : Fin 3) :
    su2AdjointMatrix U⁻¹ a b = su2AdjointMatrix U b a
```

## B. The adjoint matrix of `SU(3)`

**`StandardModel.su3AdjointMatrix`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/AdjointMatrix.lean#L88).

> The adjoint matrix of `U ∈ SU(3)`: the trace pairing of the Gell-Mann basis with the
> Gell-Mann basis conjugated by `U`.

```lean
noncomputable def su3AdjointMatrix (U : specialUnitaryGroup (Fin 3) ℂ) :
    Matrix (Fin 8) (Fin 8) ℝ
```

**`StandardModel.su3AdjointMatrix_apply`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/AdjointMatrix.lean#L94).

```lean
lemma su3AdjointMatrix_apply (U : specialUnitaryGroup (Fin 3) ℂ) (i j : Fin 8) :
    su3AdjointMatrix U i j
      = 2⁻¹ * (Matrix.trace (gellMannMatrix i * (U.1 * gellMannMatrix j * star U.1))).re
```

**`StandardModel.sum_su3AdjointMatrix_row_mul`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/AdjointMatrix.lean#L100).

> The rows of the adjoint matrix are orthonormal.

```lean
lemma sum_su3AdjointMatrix_row_mul (U : specialUnitaryGroup (Fin 3) ℂ) (c d : Fin 8) :
    ∑ a : Fin 8, su3AdjointMatrix U c a * su3AdjointMatrix U d a
      = if c = d then 1 else 0
```

**`StandardModel.su3AdjointMatrix_inv`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/AdjointMatrix.lean#L106).

> The adjoint matrix of the inverse is the transpose.

```lean
lemma su3AdjointMatrix_inv (U : specialUnitaryGroup (Fin 3) ℂ) (a b : Fin 8) :
    su3AdjointMatrix U⁻¹ a b = su3AdjointMatrix U b a
```

## Depends on

- [The standard basis of the gauge algebra](gaugealgebra-basis.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/GaugeGroup/AdjointMatrix.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/AdjointMatrix.lean)
