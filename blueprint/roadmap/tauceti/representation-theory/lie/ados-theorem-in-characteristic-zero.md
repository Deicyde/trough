---
declaration: theorem
origin: cited
lean: TauCeti.adoCharZero, TauCeti.exists_faithful_nilrepresentation_charZero, TauCeti.adoCharP
statement: formalized
proof: formalized
---

# Ado's theorem in characteristic zero

Every finite-dimensional Lie algebra over a field of
characteristic zero admits a faithful finite-dimensional representation.

```lean
TauCeti.adoCharZero.{u, v} (K : Type u) (L : Type v) [Field K] [LieRing L] [LieAlgebra K L]
  [FiniteDimensional K L] [CharZero K] :
  ∃ V x x_1, ∃ (_ : FiniteDimensional K V), ∃ ρ, Function.Injective ⇑ρ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Frobenius commutator identity](../../algebra/nilpotent-orbits-springer-resolution-and-subregu/the-frobenius-commutator-identity.md)
- [The Krull intersection theorem for an extended ideal](../../ring-theory/ideal/the-krull-intersection-theorem-for-an-extended-i.md)
- [Levi's theorem](../../algebra/lie/levis-theorem.md)
- [The linear-independence half of the Poincaré--Birkhoff--Witt theorem](../../algebra/lie/the-linear-independence-half-of-the-poincare-bir.md)
- [The Poincaré--Birkhoff--Witt theorem](../../algebra/lie/the-poincare-birkhoff-witt-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.adoCharZero`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Lie/Ado/CharacteristicZero.html#TauCeti.adoCharZero).

## Other forms

**Ado's theorem in characteristic zero, with nilpotence on the nilradical.** Formalized in Tau Ceti as [`TauCeti.exists_faithful_nilrepresentation_charZero`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Lie/Ado/CharacteristicZero.html#TauCeti.exists_faithful_nilrepresentation_charZero).

```lean
TauCeti.exists_faithful_nilrepresentation_charZero.{u, v} (K : Type u) (L : Type v) [Field K]
  [LieRing L] [LieAlgebra K L] [FiniteDimensional K L] [CharZero K] :
  ∃ V x x_1,
    ∃ (_ : FiniteDimensional K V),
      ∃ ρ, Function.Injective ⇑ρ ∧ ∀ x_3 ∈ TauCeti.LieAlgebra.nilradical K L, IsNilpotent (ρ x_3)
```

**Ado's theorem in prime characteristic.** Formalized in Tau Ceti as [`TauCeti.adoCharP`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Lie/Ado/PositiveCharacteristic.html#TauCeti.adoCharP).

```lean
TauCeti.adoCharP.{u, v} (K : Type u) (L : Type v) [Field K] [LieRing L] [LieAlgebra K L]
  [FiniteDimensional K L] (p : ℕ) [Fact (Nat.Prime p)] [CharP K p] :
  ∃ V x x_1, ∃ (_ : FiniteDimensional K V), ∃ ρ, Function.Injective ⇑ρ
```

## Sources

- [Tau Ceti documentation: `TauCeti.adoCharZero`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Lie/Ado/CharacteristicZero.html#TauCeti.adoCharZero)
- [Source of `TauCeti.adoCharZero` in TauCeti/RepresentationTheory/Lie/Ado/CharacteristicZero.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Lie/Ado/CharacteristicZero.lean#L344)
