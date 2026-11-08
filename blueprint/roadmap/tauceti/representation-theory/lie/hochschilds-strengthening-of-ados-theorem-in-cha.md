---
declaration: theorem
origin: cited
lean: TauCeti.exists_faithful_preserving_ad_nilpotence_charZero
statement: formalized
proof: formalized
---

# Hochschild's strengthening of Ado's theorem in characteristic zero

A finite-dimensional
Lie algebra over a field of characteristic zero has a faithful finite-dimensional representation
that preserves nilpotence of the adjoint action: every `ad`-nilpotent element acts nilpotently.

For semisimple `L` the nilradical is zero, so the nilpotence clause of
`TauCeti.exists_faithful_nilrepresentation_charZero` is empty there, while this one still
constrains every `ad`-nilpotent element.

```lean
TauCeti.exists_faithful_preserving_ad_nilpotence_charZero.{u, v} (K : Type u) (L : Type v) [Field K]
  [LieRing L] [LieAlgebra K L] [FiniteDimensional K L] [CharZero K] :
  ∃ V x x_1,
    ∃ (_ : FiniteDimensional K V),
      ∃ ρ,
        Function.Injective ⇑ρ ∧
          ∀ (x_3 : L), IsNilpotent ((LieAlgebra.ad K L) x_3) → IsNilpotent (ρ x_3)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Ado's theorem in characteristic zero](ados-theorem-in-characteristic-zero.md)
- [Hochschild's nilpotence theorem in characteristic zero](hochschilds-nilpotence-theorem-in-characteristic.md)
- [Levi's theorem](../../algebra/lie/levis-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_faithful_preserving_ad_nilpotence_charZero`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Lie/Ado/CharacteristicZero.html#TauCeti.exists_faithful_preserving_ad_nilpotence_charZero).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_faithful_preserving_ad_nilpotence_charZero`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Lie/Ado/CharacteristicZero.html#TauCeti.exists_faithful_preserving_ad_nilpotence_charZero)
- [Source of `TauCeti.exists_faithful_preserving_ad_nilpotence_charZero` in TauCeti/RepresentationTheory/Lie/Ado/CharacteristicZero.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Lie/Ado/CharacteristicZero.lean#L327)
