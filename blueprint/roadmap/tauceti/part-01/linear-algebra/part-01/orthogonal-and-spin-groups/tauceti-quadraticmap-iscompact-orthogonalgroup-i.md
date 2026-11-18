---
declaration: theorem
origin: cited
lean: TauCeti.QuadraticMap.isCompact_orthogonalGroup_iff
statement: formalized
proof: formalized
---

# TauCeti.QuadraticMap.isCompact_orthogonalGroup_iff

The orthogonal group of a quadratic form on a finite-dimensional space
over a locally compact nontrivially normed field is compact exactly when the form is anisotropic.

```lean
TauCeti.QuadraticMap.isCompact_orthogonalGroup_iff.{u_1, u_2} {K : Type u_1} {V : Type u_2}
  [NontriviallyNormedField K] [WeaklyLocallyCompactSpace K] [AddCommGroup V] [_root_.Module K V]
  [FiniteDimensional K V] (Q : QuadraticForm K V) :
  IsCompact ↑(TauCeti.QuadraticMap.orthogonalGroup Q) ↔ QuadraticMap.Anisotropic Q
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.QuadraticMap.isCompact_orthogonalGroup_iff`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/QuadraticForm/OrthogonalGroup/Compact/Basic.html#TauCeti.QuadraticMap.isCompact_orthogonalGroup_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.QuadraticMap.isCompact_orthogonalGroup_iff`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/QuadraticForm/OrthogonalGroup/Compact/Basic.html#TauCeti.QuadraticMap.isCompact_orthogonalGroup_iff)
- [Source of `TauCeti.QuadraticMap.isCompact_orthogonalGroup_iff` in TauCeti/Topology/Algebra/QuadraticForm/OrthogonalGroup/Compact/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Algebra/QuadraticForm/OrthogonalGroup/Compact/Basic.lean#L152)
- [Tau Ceti roadmap status: Orthogonal and spin groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/OrthogonalSpinGroups/STATUS.md)
