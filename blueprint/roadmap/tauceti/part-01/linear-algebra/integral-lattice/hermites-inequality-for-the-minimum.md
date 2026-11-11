---
declaration: theorem
origin: cited
lean: TauCeti.IntegralLattice.IsPosDef.minimum_le_rpow_mul_determinant_rpow, TauCeti.IntegralLattice.IsPosDef.three_pow_mul_minimum_pow_le
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

## Proof depends on

- [Hermite's inequality](../bilinear-form/hermites-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice.IsPosDef.minimum_le_rpow_mul_determinant_rpow`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/PosDef/Hermite.html#TauCeti.IntegralLattice.IsPosDef.minimum_le_rpow_mul_determinant_rpow).

## Other forms

**Hermite's inequality for the minimum, without roots.** Formalized in Tau Ceti as [`TauCeti.IntegralLattice.IsPosDef.three_pow_mul_minimum_pow_le`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/PosDef/Hermite.html#TauCeti.IntegralLattice.IsPosDef.three_pow_mul_minimum_pow_le).

```lean
TauCeti.IntegralLattice.IsPosDef.three_pow_mul_minimum_pow_le.{u} {V : Type u} [AddCommGroup V]
  [_root_.Module ℚ V] {L : TauCeti.IntegralLattice V} (hL : L.IsPosDef) :
  3 ^ (Module.finrank ℤ ↥L.carrier).choose 2 * ↑L.minimum ^ Module.finrank ℤ ↥L.carrier ≤
    4 ^ (Module.finrank ℤ ↥L.carrier).choose 2 * L.determinant
```

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice.IsPosDef.minimum_le_rpow_mul_determinant_rpow`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/PosDef/Hermite.html#TauCeti.IntegralLattice.IsPosDef.minimum_le_rpow_mul_determinant_rpow)
- [Source of `TauCeti.IntegralLattice.IsPosDef.minimum_le_rpow_mul_determinant_rpow` in TauCeti/LinearAlgebra/IntegralLattice/PosDef/Hermite.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/IntegralLattice/PosDef/Hermite.lean#L79)
