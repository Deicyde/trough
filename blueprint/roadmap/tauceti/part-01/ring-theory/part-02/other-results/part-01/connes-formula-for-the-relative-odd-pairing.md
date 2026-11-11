---
declaration: theorem
origin: cited
lean: TauCeti.relativeAlgebraicK1.oddPairing_mk_mk
statement: formalized
proof: formalized
---

# Connes' formula for the relative odd pairing

an invertible matrix `u` over `A⁺` with a
relative class pairs with the class of a relative cyclic cocycle `φ` of degree `n = 2m + 1` as
`(1 + i)⁻¹ 2⁻ⁿ Γ(n/2 + 1)⁻¹ (φ#Tr)(u⁻¹ - 1, u - 1, …, u⁻¹ - 1, u - 1)`.

```lean
TauCeti.relativeAlgebraicK1.oddPairing_mk_mk.{u_1, u_2} {A : Type u_1} {M : Type u_2}
  [NonUnitalRing A] [_root_.Module ℂ A] [IsScalarTower ℂ A A] [SMulCommClass ℂ A A] [AddCommGroup M]
  [_root_.Module ℂ M] (m n : ℕ) (u : GL (Fin n) (Unitization ℂ A))
  (hu : (TauCeti.AlgebraicK1.mk (Unitization ℂ A) n) u ∈ TauCeti.relativeAlgebraicK1 ℂ A)
  (φ : ↥(TauCeti.reducedCyclicCocycles ℂ (Unitization ℂ A) M (2 * m + 1))) :
  (Multiplicative.toAdd
        ((TauCeti.relativeAlgebraicK1.oddPairing A M m)
          ⟨(TauCeti.AlgebraicK1.mk (Unitization ℂ A) n) u, hu⟩))
      ((TauCeti.reducedCyclicCohomology.mk ℂ (Unitization ℂ A) M (2 * m + 1)) φ) =
    ((1 + Complex.I)⁻¹ * (2 ^ (2 * m + 1))⁻¹ * (↑(Real.Gamma ((2 * ↑m + 1) / 2 + 1)))⁻¹) •
      ((TauCeti.matrixCochainExtension (Fin n) (2 * m + 1)) ↑↑↑φ) fun k =>
        if Even ↑k then ↑u⁻¹ - 1 else ↑u - 1
```

## Depends on

- [Connes' odd pairing of algebraic `K₁` with cyclic cohomology in degree `2m + 1`](../../../part-01/cyclic-cohomology-spectral-triples-and-noncommut/connes-odd-pairing-of-algebraic-k1-with-cyclic-c.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.relativeAlgebraicK1.oddPairing_mk_mk`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/OddPairing/Relative.html#TauCeti.relativeAlgebraicK1.oddPairing_mk_mk).

## Sources

- [Tau Ceti documentation: `TauCeti.relativeAlgebraicK1.oddPairing_mk_mk`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/OddPairing/Relative.html#TauCeti.relativeAlgebraicK1.oddPairing_mk_mk)
- [Source of `TauCeti.relativeAlgebraicK1.oddPairing_mk_mk` in TauCeti/RingTheory/CyclicCohomology/OddPairing/Relative.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/CyclicCohomology/OddPairing/Relative.lean#L112)
