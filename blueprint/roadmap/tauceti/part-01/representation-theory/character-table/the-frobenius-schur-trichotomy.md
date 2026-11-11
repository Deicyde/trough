---
declaration: theorem
origin: cited
lean: TauCeti.Representation.frobeniusSchurIndicator_eq_one_or_eq_zero_or_eq_neg_one
statement: formalized
proof: formalized
---

# The Frobenius-Schur trichotomy

The indicator of an irreducible representation over an
algebraically closed field of characteristic zero takes only the values `1`, `0` and `-1`.

```lean
TauCeti.Representation.frobeniusSchurIndicator_eq_one_or_eq_zero_or_eq_neg_one.{v, w} {k : Type}
  {G : Type v} {V : Type w} [Field k] [CharZero k] [IsAlgClosed k] [Group G] [Fintype G]
  [AddCommGroup V] [_root_.Module k V] [FiniteDimensional k V] (ρ : Representation k G V)
  [ρ.IsIrreducible] :
  TauCeti.Representation.frobeniusSchurIndicator ρ = 1 ∨
    TauCeti.Representation.frobeniusSchurIndicator ρ = 0 ∨
      TauCeti.Representation.frobeniusSchurIndicator ρ = -1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Representation.frobeniusSchurIndicator_eq_one_or_eq_zero_or_eq_neg_one`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/CharacterTable/FrobeniusSchur/Trichotomy.html#TauCeti.Representation.frobeniusSchurIndicator_eq_one_or_eq_zero_or_eq_neg_one).

## Sources

- [Tau Ceti documentation: `TauCeti.Representation.frobeniusSchurIndicator_eq_one_or_eq_zero_or_eq_neg_one`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/CharacterTable/FrobeniusSchur/Trichotomy.html#TauCeti.Representation.frobeniusSchurIndicator_eq_one_or_eq_zero_or_eq_neg_one)
- [Source of `TauCeti.Representation.frobeniusSchurIndicator_eq_one_or_eq_zero_or_eq_neg_one` in TauCeti/RepresentationTheory/CharacterTable/FrobeniusSchur/Trichotomy.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/CharacterTable/FrobeniusSchur/Trichotomy.lean#L400)
