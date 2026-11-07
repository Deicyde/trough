---
declaration: theorem
origin: cited
lean: TauCeti.IntegralLattice.IsPosDef.minimum_le_rpow_mul_determinant_rpow
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

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice.IsPosDef.minimum_le_rpow_mul_determinant_rpow`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/PosDef/Hermite.html#TauCeti.IntegralLattice.IsPosDef.minimum_le_rpow_mul_determinant_rpow)
- [Source of `TauCeti.IntegralLattice.IsPosDef.minimum_le_rpow_mul_determinant_rpow` in TauCeti/LinearAlgebra/IntegralLattice/PosDef/Hermite.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/IntegralLattice/PosDef/Hermite.lean#L79)
- [Tau Ceti roadmap status: Integral quadratic forms and lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/IntegralLattices/STATUS.md)
