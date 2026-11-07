---
declaration: theorem
origin: cited
lean: TauCeti.IsJordanCurve.frontier_connectedComponentIn
statement: formalized
proof: formalized
---

# The frontier of a complementary component of a Jordan curve is the whole curve

for
`x ∉ C`, the component of `Cᶜ` containing `x` has frontier `C`.

```lean
TauCeti.IsJordanCurve.frontier_connectedComponentIn {C : Set ℂ} (h : TauCeti.IsJordanCurve C)
  {x : ℂ} (hx : x ∉ C) : frontier (connectedComponentIn Cᶜ x) = C
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Jordan separation theorem](the-jordan-separation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsJordanCurve.frontier_connectedComponentIn`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/PlaneSeparation/JordanCurve.html#TauCeti.IsJordanCurve.frontier_connectedComponentIn).

## Sources

- [Tau Ceti documentation: `TauCeti.IsJordanCurve.frontier_connectedComponentIn`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/PlaneSeparation/JordanCurve.html#TauCeti.IsJordanCurve.frontier_connectedComponentIn)
- [Source of `TauCeti.IsJordanCurve.frontier_connectedComponentIn` in TauCeti/Analysis/Complex/PlaneSeparation/JordanCurve.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/PlaneSeparation/JordanCurve.lean#L173)
- [Tau Ceti roadmap status: Conformal mapping and the geometric theory of holomorphic functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ConformalMapping/STATUS.md)
