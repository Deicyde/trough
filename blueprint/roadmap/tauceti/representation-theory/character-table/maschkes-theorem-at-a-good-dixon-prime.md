---
declaration: theorem
origin: cited
lean: TauCeti.IsGoodDixonPrime.isSemisimpleRing
statement: formalized
proof: formalized
---

# Maschke's theorem at a good Dixon prime

the modular group algebra `ZMod p [G]` is a
semisimple ring.

```lean
TauCeti.IsGoodDixonPrime.isSemisimpleRing.{u_1} {G : Type u_1} [Group G] {p : ℕ}
  (hp : TauCeti.IsGoodDixonPrime G p) : IsSemisimpleRing (MonoidAlgebra (ZMod p) G)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsGoodDixonPrime.isSemisimpleRing`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/CharacterTable/Dixon/Prime.html#TauCeti.IsGoodDixonPrime.isSemisimpleRing).

## Sources

- [Tau Ceti documentation: `TauCeti.IsGoodDixonPrime.isSemisimpleRing`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/CharacterTable/Dixon/Prime.html#TauCeti.IsGoodDixonPrime.isSemisimpleRing)
- [Source of `TauCeti.IsGoodDixonPrime.isSemisimpleRing` in TauCeti/RepresentationTheory/CharacterTable/Dixon/Prime.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/CharacterTable/Dixon/Prime.lean#L152)
