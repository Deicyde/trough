---
declaration: theorem
origin: cited
lean: TauCeti.IsJordanCurve.not_isPreconnected_compl
statement: formalized
proof: formalized
---

# The Jordan separation theorem

The complement of a Jordan curve in the plane is not
preconnected.

```lean
TauCeti.IsJordanCurve.not_isPreconnected_compl {C : Set ℂ} (h : TauCeti.IsJordanCurve C) :
  ¬IsPreconnected Cᶜ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsJordanCurve.not_isPreconnected_compl`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/PlaneSeparation/JordanCurve.html#TauCeti.IsJordanCurve.not_isPreconnected_compl).

## Sources

- [Tau Ceti documentation: `TauCeti.IsJordanCurve.not_isPreconnected_compl`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/PlaneSeparation/JordanCurve.html#TauCeti.IsJordanCurve.not_isPreconnected_compl)
- [Source of `TauCeti.IsJordanCurve.not_isPreconnected_compl` in TauCeti/Analysis/Complex/PlaneSeparation/JordanCurve.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/PlaneSeparation/JordanCurve.lean#L97)
- [Tau Ceti roadmap status: Conformal mapping and the geometric theory of holomorphic functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ConformalMapping/STATUS.md)
