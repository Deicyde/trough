---
declaration: def
origin: cited
lean: TauCeti.ClassFieldTheory.ClassFormation.tateIso
statement: formalized
---

# Tate's theorem for a class formation

, in every integer degree: the generic theorem applied
to the fundamental class, with the three hypotheses discharged by the three individually named
consequences of the axioms. This is Artin–Tate's Main Theorem (Chapter XIV §4, Theorem 1).

```lean
TauCeti.ClassFieldTheory.ClassFormation.tateIso {G : Type} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [CompactSpace G] [TotallyDisconnectedSpace G]
  {F : TauCeti.ClassFieldTheory.Formation G} (cf : TauCeti.ClassFieldTheory.ClassFormation F)
  (L : TauCeti.ClassFieldTheory.NormalLayer G) (r : ℤ) : ↑(L.TrivialTateH r) ≃+ ↑(L.TateH F (r + 2))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.ClassFormation.tateIso`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Formation/Tate/Theorem.html#TauCeti.ClassFieldTheory.ClassFormation.tateIso).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.ClassFormation.tateIso`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Formation/Tate/Theorem.html#TauCeti.ClassFieldTheory.ClassFormation.tateIso)
- [Source of `TauCeti.ClassFieldTheory.ClassFormation.tateIso` in TauCeti/NumberTheory/ClassFieldTheory/Formation/Tate/Theorem.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/Formation/Tate/Theorem.lean#L165)
- [Tau Ceti roadmap status: Class field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ClassFieldTheory/STATUS.md)
