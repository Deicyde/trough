---
declaration: theorem
origin: cited
lean: TauCeti.YSeed.mutation_involutive
statement: formalized
proof: formalized
---

# TauCeti.YSeed.mutation_involutive

Mutation in a fixed direction is an involution on Y-seeds.

```lean
TauCeti.YSeed.mutation_involutive.{u_1, u_4} {K : Type u_1} {P : Type u_4}
  [TauCeti.CoefficientSemifield P] [DecidableEq K] (k : K) :
  Function.Involutive fun s => s.mutation k
```

## Depends on

- [TauCeti.CoefficientSemifield](tauceti-coefficientsemifield.md)
- [TauCeti.ExchangeMatrix](tauceti-exchangematrix.md)
- [TauCeti.YSeed](tauceti-yseed.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.YSeed.mutation_involutive`](https://taucetiproject.org/docs/TauCeti/Algebra/Cluster/YSeed/Basic.html#TauCeti.YSeed.mutation_involutive).

## Sources

- [Tau Ceti documentation: `TauCeti.YSeed.mutation_involutive`](https://taucetiproject.org/docs/TauCeti/Algebra/Cluster/YSeed/Basic.html#TauCeti.YSeed.mutation_involutive)
- [Source of `TauCeti.YSeed.mutation_involutive` in TauCeti/Algebra/Cluster/YSeed/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Cluster/YSeed/Basic.lean#L115)
- [Tau Ceti roadmap status: Cluster algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ClusterAlgebras/STATUS.md)
