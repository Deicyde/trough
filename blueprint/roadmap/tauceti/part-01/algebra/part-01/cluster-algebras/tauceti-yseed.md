---
declaration: structure
origin: cited
lean: TauCeti.YSeed
statement: formalized
---

# TauCeti.YSeed

A Y-seed over a coefficient semifield: a family of coefficients and a square exchange
matrix with its positive symmetrizer. No choice of ambient field or cluster is involved.

```lean
TauCeti.YSeed.{u_1, u_2} (K : Type u_1) (P : Type u_2) [TauCeti.CoefficientSemifield P] :
  Type (max u_1 u_2)
```

## Depends on

- [TauCeti.CoefficientSemifield](tauceti-coefficientsemifield.md)
- [TauCeti.ExchangeMatrix](tauceti-exchangematrix.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.YSeed`](https://taucetiproject.org/docs/TauCeti/Algebra/Cluster/YSeed/Basic.html#TauCeti.YSeed).

## Sources

- [Tau Ceti documentation: `TauCeti.YSeed`](https://taucetiproject.org/docs/TauCeti/Algebra/Cluster/YSeed/Basic.html#TauCeti.YSeed)
- [Source of `TauCeti.YSeed` in TauCeti/Algebra/Cluster/YSeed/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Cluster/YSeed/Basic.lean#L35)
- [Tau Ceti roadmap status: Cluster algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ClusterAlgebras/STATUS.md)
