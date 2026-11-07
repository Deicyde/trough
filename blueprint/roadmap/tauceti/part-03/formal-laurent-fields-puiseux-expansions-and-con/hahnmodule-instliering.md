---
declaration: instance
origin: cited
lean: HahnModule.instLieRing
statement: formalized
---

# HahnModule.instLieRing

Hahn series with coefficients in a Lie ring form a Lie ring under the convolution bracket.

```lean
HahnModule.instLieRing.{u_1, u_2, u_3} {Γ : Type u_1} {R : Type u_2} {L : Type u_3}
  [AddCommMonoid Γ] [PartialOrder Γ] [IsOrderedCancelAddMonoid Γ] [SMul R L] [LieRing L] :
  LieRing (HahnModule Γ R L)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`HahnModule.instLieRing`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HahnModule.html#HahnModule.instLieRing).

## Sources

- [Tau Ceti documentation: `HahnModule.instLieRing`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HahnModule.html#HahnModule.instLieRing)
- [Source of `HahnModule.instLieRing` in TauCeti/Algebra/Lie/HahnModule.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/HahnModule.lean#L132)
- [Tau Ceti roadmap status: Formal Laurent fields, Puiseux expansions and continuous differential calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FormalLaurentPuiseux/STATUS.md)
