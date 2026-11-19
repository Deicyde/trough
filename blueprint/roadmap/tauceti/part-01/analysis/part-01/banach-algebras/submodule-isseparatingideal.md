---
declaration: structure
origin: cited
lean: Submodule.IsSeparatingIdeal
statement: formalized
---

# Submodule.IsSeparatingIdeal

A *separating ideal* of a topological algebra `B` is a closed two-sided ideal `J`, given as a
scalar submodule, such that for every sequence `b` in `B` the nests of closed subspaces
`closure (b 0 ⋯ b (n - 1) J)` and `closure (J b (n - 1) ⋯ b 0)` are eventually constant. The
products are formed in `Module.End R B` from left and right multiplication operators.

```lean
Submodule.IsSeparatingIdeal.{u_1, u_2} {R : Type u_1} {B : Type u_2} [CommSemiring R]
  [NonUnitalSemiring B] [_root_.Module R B] [IsScalarTower R B B] [SMulCommClass R B B]
  [TopologicalSpace B] [ContinuousAdd B] [ContinuousConstSMul R B] (J : Submodule R B) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Submodule.IsSeparatingIdeal`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Algebra/SeparatingIdeal/Basic.html#Submodule.IsSeparatingIdeal).

## Sources

- [Tau Ceti documentation: `Submodule.IsSeparatingIdeal`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Algebra/SeparatingIdeal/Basic.html#Submodule.IsSeparatingIdeal)
- [Source of `Submodule.IsSeparatingIdeal` in TauCeti/Analysis/Normed/Algebra/SeparatingIdeal/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Algebra/SeparatingIdeal/Basic.lean#L64)
- [Tau Ceti roadmap status: Banach algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/BanachAlgebras/STATUS.md)
