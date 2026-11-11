---
declaration: theorem
origin: cited
lean: TauCeti.IntegralLattice.IsPosDef.prod_successiveMinimum_mul_pi_pow_le
statement: formalized
proof: formalized
---

# Minkowski's second theorem (`TauCeti.IntegralLattice.IsPosDef.prod_successiveMinimum_mul_pi_pow_le`)

The successive minima `λ₀, …, λ_{n-1}` of a positive definite
integral lattice of rank `n` satisfy `(∏ᵢ λᵢ) · πⁿ ≤ 4ⁿ · Γ(n/2 + 1)² · det L`, that is,
`∏ᵢ λᵢ ≤ cₙⁿ · det L` with `cₙ = (4 / π) · Γ(n/2 + 1) ^ (2/n)` the constant of Minkowski's bound for
the minimum.

```lean
TauCeti.IntegralLattice.IsPosDef.prod_successiveMinimum_mul_pi_pow_le.{u} {V : Type u}
  [AddCommGroup V] [_root_.Module ℚ V] {L : TauCeti.IntegralLattice V} (hL : L.IsPosDef) :
  (∏ i, ↑(L.successiveMinimum i)) * Real.pi ^ Module.finrank ℤ ↥L.carrier ≤
    4 ^ Module.finrank ℤ ↥L.carrier * Real.Gamma (↑(Module.finrank ℤ ↥L.carrier) / 2 + 1) ^ 2 *
      ↑L.determinant
```

## Depends on

- [TauCeti.IntegralLattice](../integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)

## Proof depends on

- [Minkowski's convex body theorem for a realized lattice](minkowskis-convex-body-theorem-for-a-realized-la.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice.IsPosDef.prod_successiveMinimum_mul_pi_pow_le`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/PosDef/Minkowski.html#TauCeti.IntegralLattice.IsPosDef.prod_successiveMinimum_mul_pi_pow_le).

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice.IsPosDef.prod_successiveMinimum_mul_pi_pow_le`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/PosDef/Minkowski.html#TauCeti.IntegralLattice.IsPosDef.prod_successiveMinimum_mul_pi_pow_le)
- [Source of `TauCeti.IntegralLattice.IsPosDef.prod_successiveMinimum_mul_pi_pow_le` in TauCeti/LinearAlgebra/IntegralLattice/PosDef/Minkowski.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/IntegralLattice/PosDef/Minkowski.lean#L215)
