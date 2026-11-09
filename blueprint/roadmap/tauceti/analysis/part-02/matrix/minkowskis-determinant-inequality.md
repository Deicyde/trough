---
declaration: theorem
origin: cited
lean: Matrix.PosSemidef.det_rpow_add_det_rpow_le, LinearMap.IsPositive.det_rpow_add_det_rpow_le
statement: formalized
proof: formalized
---

# Minkowski's determinant inequality

For positive semidefinite real `n × n` matrices `A`
and `B` with `n ≥ 1`, `det A ^ (1 / n) + det B ^ (1 / n) ≤ det (A + B) ^ (1 / n)`.

```lean
Matrix.PosSemidef.det_rpow_add_det_rpow_le.{u_1} {n : Type u_1} [Fintype n] [DecidableEq n]
  [Nonempty n] {A B : Matrix n n ℝ} (hA : A.PosSemidef) (hB : B.PosSemidef) :
  A.det ^ (↑(Fintype.card n))⁻¹ + B.det ^ (↑(Fintype.card n))⁻¹ ≤
    (A + B).det ^ (↑(Fintype.card n))⁻¹
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.PosSemidef.det_rpow_add_det_rpow_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/MinkowskiDeterminant.html#Matrix.PosSemidef.det_rpow_add_det_rpow_le).

## Other forms

**Minkowski's determinant inequality for positive operators.** Formalized in Tau Ceti as [`LinearMap.IsPositive.det_rpow_add_det_rpow_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/MinkowskiDeterminant.html#LinearMap.IsPositive.det_rpow_add_det_rpow_le).

```lean
LinearMap.IsPositive.det_rpow_add_det_rpow_le.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [Nontrivial E] {A B : E →ₗ[ℝ] E}
  (hA : A.IsPositive) (hB : B.IsPositive) :
  LinearMap.det A ^ (↑(Module.finrank ℝ E))⁻¹ + LinearMap.det B ^ (↑(Module.finrank ℝ E))⁻¹ ≤
    LinearMap.det (A + B) ^ (↑(Module.finrank ℝ E))⁻¹
```

## Sources

- [Tau Ceti documentation: `Matrix.PosSemidef.det_rpow_add_det_rpow_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/MinkowskiDeterminant.html#Matrix.PosSemidef.det_rpow_add_det_rpow_le)
- [Source of `Matrix.PosSemidef.det_rpow_add_det_rpow_le` in TauCeti/Analysis/Matrix/MinkowskiDeterminant.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Matrix/MinkowskiDeterminant.lean#L81)
