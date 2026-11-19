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
- [Source of `TauCeti.IsGoodDixonPrime.isSemisimpleRing` in TauCeti/RepresentationTheory/CharacterTable/Dixon/Prime.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RepresentationTheory/CharacterTable/Dixon/Prime.lean#L154)
