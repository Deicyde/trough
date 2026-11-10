---
declaration: theorem
origin: cited
lean: TauCeti.IntegralLattice.IsPosDef.minimum_le_mul_determinant_rpow, TauCeti.IntegralLattice.IsPosDef.minimum_pow_mul_pi_pow_le
statement: formalized
proof: formalized
---

# Minkowski's bound for the minimum

A positive definite integral lattice of rank `n`
satisfies `min L ≤ (4 / π) · Γ(n/2 + 1) ^ (2/n) · (det L) ^ (1/n)`.

```lean
TauCeti.IntegralLattice.IsPosDef.minimum_le_mul_determinant_rpow.{u} {V : Type u} [AddCommGroup V]
  [_root_.Module ℚ V] {L : TauCeti.IntegralLattice V} (hL : L.IsPosDef) :
  ↑L.minimum ≤
    4 / Real.pi *
        Real.Gamma (↑(Module.finrank ℤ ↥L.carrier) / 2 + 1) ^ (2 / ↑(Module.finrank ℤ ↥L.carrier)) *
      ↑L.determinant ^ (1 / ↑(Module.finrank ℤ ↥L.carrier))
```

## Depends on

- [TauCeti.IntegralLattice](../integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)

## Proof depends on

- [Minkowski's second theorem](minkowskis-second-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice.IsPosDef.minimum_le_mul_determinant_rpow`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/PosDef/Minkowski.html#TauCeti.IntegralLattice.IsPosDef.minimum_le_mul_determinant_rpow).

## Other forms

**Minkowski's bound for the minimum, without roots.** Formalized in Tau Ceti as [`TauCeti.IntegralLattice.IsPosDef.minimum_pow_mul_pi_pow_le`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/PosDef/Minkowski.html#TauCeti.IntegralLattice.IsPosDef.minimum_pow_mul_pi_pow_le).

```lean
TauCeti.IntegralLattice.IsPosDef.minimum_pow_mul_pi_pow_le.{u} {V : Type u} [AddCommGroup V]
  [_root_.Module ℚ V] {L : TauCeti.IntegralLattice V} (hL : L.IsPosDef) :
  ↑L.minimum ^ Module.finrank ℤ ↥L.carrier * Real.pi ^ Module.finrank ℤ ↥L.carrier ≤
    4 ^ Module.finrank ℤ ↥L.carrier * Real.Gamma (↑(Module.finrank ℤ ↥L.carrier) / 2 + 1) ^ 2 *
      ↑L.determinant
```

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice.IsPosDef.minimum_le_mul_determinant_rpow`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/PosDef/Minkowski.html#TauCeti.IntegralLattice.IsPosDef.minimum_le_mul_determinant_rpow)
- [Source of `TauCeti.IntegralLattice.IsPosDef.minimum_le_mul_determinant_rpow` in TauCeti/LinearAlgebra/IntegralLattice/PosDef/Minkowski.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/IntegralLattice/PosDef/Minkowski.lean#L283)
