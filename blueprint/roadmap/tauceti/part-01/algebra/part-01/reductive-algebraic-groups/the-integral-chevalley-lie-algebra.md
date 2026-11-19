---
declaration: def
origin: cited
lean: RootPairing.ChevalleyLieAlgebra
statement: formalized
---

# The integral Chevalley Lie algebra

**The integral Chevalley Lie algebra** of a root datum `P` over its full cocharacter group `Y`,
realized on `TauCeti.FullCartan Y ι` (`Y × (ι →₀ ℤ)`).

```lean
RootPairing.ChevalleyLieAlgebra.{u_1, u_2, u_3} {ι : Type u_1} {X : Type u_2} {Y : Type u_3}
  [AddCommGroup X] [AddCommGroup Y] [Finite ι] {P : RootPairing ι ℤ X Y}
  (_c : P.ChevalleyConstants) : Type (max u_1 u_3)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`RootPairing.ChevalleyLieAlgebra`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Chevalley/Basic.html#RootPairing.ChevalleyLieAlgebra).

## Sources

- [Tau Ceti documentation: `RootPairing.ChevalleyLieAlgebra`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Chevalley/Basic.html#RootPairing.ChevalleyLieAlgebra)
- [Source of `RootPairing.ChevalleyLieAlgebra` in TauCeti/Algebra/Lie/Chevalley/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Lie/Chevalley/Basic.lean#L187)
- [Tau Ceti roadmap status: Reductive algebraic groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ReductiveGroups/STATUS.md)
