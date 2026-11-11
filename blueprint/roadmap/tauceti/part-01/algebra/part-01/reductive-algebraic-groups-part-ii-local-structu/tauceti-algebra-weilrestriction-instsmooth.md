---
declaration: theorem
origin: cited
lean: TauCeti.Algebra.WeilRestriction.instSmooth
statement: formalized
proof: formalized
---

# TauCeti.Algebra.WeilRestriction.instSmooth

Weil restriction along a finite projective algebra preserves smoothness.

```lean
TauCeti.Algebra.WeilRestriction.instSmooth.{u_1, u_2, u_3} (A : Type u_1) (B : Type u_2)
  (C : Type u_3) [CommRing A] [CommRing B] [CommRing C] [Algebra A B] [Algebra B C]
  [Module.Finite A B] [Module.Projective A B] [Algebra.FinitePresentation B C]
  [Algebra.Smooth B C] : Algebra.Smooth A (TauCeti.Algebra.WeilRestriction A B C)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Algebra.WeilRestriction.instSmooth`](https://taucetiproject.org/docs/TauCeti/RingTheory/WeilRestriction/Smooth.html#TauCeti.Algebra.WeilRestriction.instSmooth).

## Sources

- [Tau Ceti documentation: `TauCeti.Algebra.WeilRestriction.instSmooth`](https://taucetiproject.org/docs/TauCeti/RingTheory/WeilRestriction/Smooth.html#TauCeti.Algebra.WeilRestriction.instSmooth)
- [Source of `TauCeti.Algebra.WeilRestriction.instSmooth` in TauCeti/RingTheory/WeilRestriction/Smooth.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/WeilRestriction/Smooth.lean#L59)
- [Tau Ceti roadmap status: Reductive algebraic groups, part II — local structure and arithmetic models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ReductiveGroupsPartII/STATUS.md)
