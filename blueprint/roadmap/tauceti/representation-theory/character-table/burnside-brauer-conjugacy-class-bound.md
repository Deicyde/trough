---
declaration: theorem
origin: cited
lean: FDRep.exists_pos_finrank_hom_tensorPower_lt_card_conjClasses
statement: formalized
proof: formalized
---

# Burnside–Brauer, conjugacy-class bound

Every nonzero finite-dimensional complex
representation has a nonzero map into a tensor power of a faithful representation, with exponent
strictly smaller than the number of conjugacy classes.

```lean
FDRep.exists_pos_finrank_hom_tensorPower_lt_card_conjClasses.{v} {G : Type v} [Group G] [Finite G]
  (V X : FDRep ℂ G) (hV : Function.Injective ⇑V.ρ) (hX : 0 < Module.finrank ℂ ↑X.V) :
  ∃ n < Nat.card (ConjClasses G), 0 < Module.finrank ℂ (X ⟶ V.tensorPower n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`FDRep.exists_pos_finrank_hom_tensorPower_lt_card_conjClasses`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/CharacterTable/TensorGeneration.html#FDRep.exists_pos_finrank_hom_tensorPower_lt_card_conjClasses).

## Sources

- [Tau Ceti documentation: `FDRep.exists_pos_finrank_hom_tensorPower_lt_card_conjClasses`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/CharacterTable/TensorGeneration.html#FDRep.exists_pos_finrank_hom_tensorPower_lt_card_conjClasses)
- [Source of `FDRep.exists_pos_finrank_hom_tensorPower_lt_card_conjClasses` in TauCeti/RepresentationTheory/CharacterTable/TensorGeneration.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/CharacterTable/TensorGeneration.lean#L203)
