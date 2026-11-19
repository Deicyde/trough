---
declaration: theorem
origin: cited
lean: TauCeti.ComoduleCat.instEnoughInjectives
statement: formalized
proof: formalized
---

# TauCeti.ComoduleCat.instEnoughInjectives

Comodules over a flat coalgebra have enough injectives, with no restriction on their
coefficient modules. The carrier universe contains those of the ring and coalgebra.

```lean
TauCeti.ComoduleCat.instEnoughInjectives.{u, v, w} (R : Type u) (C : Type v) [CommRing R]
  [AddCommMonoid C] [_root_.Module R C] [Coalgebra R C] [Module.Flat R C] :
  CategoryTheory.EnoughInjectives (TauCeti.ComoduleCat R C)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ComoduleCat.instEnoughInjectives`](https://taucetiproject.org/docs/TauCeti/Algebra/Coalgebra/Comodule/EnoughInjectives.html#TauCeti.ComoduleCat.instEnoughInjectives).

## Sources

- [Tau Ceti documentation: `TauCeti.ComoduleCat.instEnoughInjectives`](https://taucetiproject.org/docs/TauCeti/Algebra/Coalgebra/Comodule/EnoughInjectives.html#TauCeti.ComoduleCat.instEnoughInjectives)
- [Source of `TauCeti.ComoduleCat.instEnoughInjectives` in TauCeti/Algebra/Coalgebra/Comodule/EnoughInjectives.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Coalgebra/Comodule/EnoughInjectives.lean#L41)
- [Tau Ceti roadmap status: Reductive algebraic groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ReductiveGroups/STATUS.md)
