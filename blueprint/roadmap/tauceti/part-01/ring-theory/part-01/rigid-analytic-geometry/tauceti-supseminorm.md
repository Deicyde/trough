---
declaration: def
origin: cited
lean: TauCeti.supSeminorm
statement: formalized
---

# TauCeti.supSeminorm

The supremum seminorm `|f|sup` of `f : A`: the supremum of its absolute values `|f(x)|` at
the maximal ideals `x` of `A`. It is zero on the zero algebra, which has no maximal ideals.

```lean
TauCeti.supSeminorm.{u_1, u_2} (K : Type u_1) [NontriviallyNormedField K] {A : Type u_2}
  [CommRing A] [Algebra K A] (f : A) : ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.supSeminorm`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/SupSeminorm.html#TauCeti.supSeminorm).

## Sources

- [Tau Ceti documentation: `TauCeti.supSeminorm`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/SupSeminorm.html#TauCeti.supSeminorm)
- [Source of `TauCeti.supSeminorm` in TauCeti/RingTheory/Affinoid/SupSeminorm.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Affinoid/SupSeminorm.lean#L103)
- [Tau Ceti roadmap status: Rigid analytic geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RigidAnalyticGeometry/STATUS.md)
