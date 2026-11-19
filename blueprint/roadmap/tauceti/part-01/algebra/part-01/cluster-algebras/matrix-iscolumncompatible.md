---
declaration: def
origin: cited
lean: Matrix.IsColumnCompatible
statement: formalized
---

# Matrix.IsColumnCompatible

Column compatibility with weights `w`: `BᵀΛ` has entry `w k` at `(k, row k)`
and zero elsewhere. The weights are not required to be positive or nonzero.

```lean
Matrix.IsColumnCompatible.{u_1, u_2, u_3} {I : Type u_1} {K : Type u_2} {R : Type u_3} [Fintype I]
  [DecidableEq I] [CommRing R] (B : Matrix I K R) (row : K ↪ I) (Λ : Matrix I I R) (w : K → R) :
  Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.IsColumnCompatible`](https://taucetiproject.org/docs/TauCeti/Algebra/Cluster/ExchangeMatrix/Compatibility.html#Matrix.IsColumnCompatible).

## Sources

- [Tau Ceti documentation: `Matrix.IsColumnCompatible`](https://taucetiproject.org/docs/TauCeti/Algebra/Cluster/ExchangeMatrix/Compatibility.html#Matrix.IsColumnCompatible)
- [Source of `Matrix.IsColumnCompatible` in TauCeti/Algebra/Cluster/ExchangeMatrix/Compatibility.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Cluster/ExchangeMatrix/Compatibility.lean#L44)
- [Tau Ceti roadmap status: Cluster algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ClusterAlgebras/STATUS.md)
