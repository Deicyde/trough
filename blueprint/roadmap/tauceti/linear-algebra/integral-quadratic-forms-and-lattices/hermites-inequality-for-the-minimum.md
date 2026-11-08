---
declaration: theorem
origin: cited
lean: TauCeti.IntegralLattice.IsPosDef.minimum_le_rpow_mul_determinant_rpow, LinearMap.BilinForm.exists_ne_zero_three_pow_mul_pow_le_four_pow_mul_det, TauCeti.IntegralLattice.IsPosDef.three_pow_mul_minimum_pow_le
statement: formalized
proof: formalized
---

# Hermite's inequality for the minimum

A positive definite integral lattice of rank `n`
satisfies `min L ≤ (4 / 3) ^ ((n - 1) / 2) · (det L) ^ (1 / n)`.

```lean
TauCeti.IntegralLattice.IsPosDef.minimum_le_rpow_mul_determinant_rpow.{u} {V : Type u}
  [AddCommGroup V] [_root_.Module ℚ V] {L : TauCeti.IntegralLattice V} (hL : L.IsPosDef) :
  ↑L.minimum ≤
    (4 / 3) ^ ((↑(Module.finrank ℤ ↥L.carrier) - 1) / 2) *
      ↑L.determinant ^ (1 / ↑(Module.finrank ℤ ↥L.carrier))
```

## Depends on

- [TauCeti.IntegralLattice](../integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice.IsPosDef.minimum_le_rpow_mul_determinant_rpow`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/PosDef/Hermite.html#TauCeti.IntegralLattice.IsPosDef.minimum_le_rpow_mul_determinant_rpow).

## Other forms

**Hermite's inequality.** Formalized in Tau Ceti as [`LinearMap.BilinForm.exists_ne_zero_three_pow_mul_pow_le_four_pow_mul_det`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/BilinearForm/Hermite.html#LinearMap.BilinForm.exists_ne_zero_three_pow_mul_pow_le_four_pow_mul_det).

```lean
LinearMap.BilinForm.exists_ne_zero_three_pow_mul_pow_le_four_pow_mul_det.{u_1, u_2} {M : Type u_1}
  [AddCommGroup M] [Nontrivial M] {ι : Type u_2} [Fintype ι] [DecidableEq ι]
  (B : LinearMap.BilinForm ℤ M) (hB : B.IsSymm)
  (hpos : (LinearMap.BilinMap.toQuadraticMap B).PosDef) (b : Module.Basis ι ℤ M) :
  ∃ x,
    x ≠ 0 ∧
      3 ^ (Fintype.card ι).choose 2 * (B x) x ^ Fintype.card ι ≤
        4 ^ (Fintype.card ι).choose 2 * ((LinearMap.BilinForm.toMatrix b) B).det
```

**Hermite's inequality for the minimum, without roots.** Formalized in Tau Ceti as [`TauCeti.IntegralLattice.IsPosDef.three_pow_mul_minimum_pow_le`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/PosDef/Hermite.html#TauCeti.IntegralLattice.IsPosDef.three_pow_mul_minimum_pow_le).

```lean
TauCeti.IntegralLattice.IsPosDef.three_pow_mul_minimum_pow_le.{u} {V : Type u} [AddCommGroup V]
  [_root_.Module ℚ V] {L : TauCeti.IntegralLattice V} (hL : L.IsPosDef) :
  3 ^ (Module.finrank ℤ ↥L.carrier).choose 2 * ↑L.minimum ^ Module.finrank ℤ ↥L.carrier ≤
    4 ^ (Module.finrank ℤ ↥L.carrier).choose 2 * L.determinant
```

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice.IsPosDef.minimum_le_rpow_mul_determinant_rpow`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/PosDef/Hermite.html#TauCeti.IntegralLattice.IsPosDef.minimum_le_rpow_mul_determinant_rpow)
- [Source of `TauCeti.IntegralLattice.IsPosDef.minimum_le_rpow_mul_determinant_rpow` in TauCeti/LinearAlgebra/IntegralLattice/PosDef/Hermite.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/IntegralLattice/PosDef/Hermite.lean#L79)
- [Tau Ceti roadmap status: Integral quadratic forms and lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/IntegralLattices/STATUS.md)
