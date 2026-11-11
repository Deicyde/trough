---
declaration: theorem
origin: cited
lean: TauCeti.NumberField.exists_gal_fullCycleType_eq_factorizationType
statement: formalized
proof: formalized
---

# The polynomial form of Dedekind's theorem

Let `f` be a monic integer polynomial and `p`
a prime not dividing the discriminant of `f`. Then some element of the Galois group of `f` over
`ℚ` acts on the complex roots of `f` with full cycle type (cycle lengths counted together with
fixed points) equal to the multiset of degrees of the irreducible factors of `f` modulo `p`.

The statement allows reducible `f`: the factor degrees of all the irreducible factors of `f`
are read off from a single Galois automorphism.

```lean
TauCeti.NumberField.exists_gal_fullCycleType_eq_factorizationType (f : Polynomial ℤ) (hf : f.Monic)
  (p : ℕ) [Fact (Nat.Prime p)] (hp : ¬↑p ∣ f.discr) :
  ∃ σ,
    ((Polynomial.Gal.galActionHom (Polynomial.map (Int.castRingHom ℚ) f) ℂ) σ).fullCycleType =
      f.factorDegrees p
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Dedekind's theorem, with the fixed points counted separately](dedekinds-theorem-with-the-fixed-points-counted.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.exists_gal_fullCycleType_eq_factorizationType`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Frobenius/CycleType.html#TauCeti.NumberField.exists_gal_fullCycleType_eq_factorizationType).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.exists_gal_fullCycleType_eq_factorizationType`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Frobenius/CycleType.html#TauCeti.NumberField.exists_gal_fullCycleType_eq_factorizationType)
- [Source of `TauCeti.NumberField.exists_gal_fullCycleType_eq_factorizationType` in TauCeti/NumberTheory/NumberField/Frobenius/CycleType.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/NumberField/Frobenius/CycleType.lean#L158)
