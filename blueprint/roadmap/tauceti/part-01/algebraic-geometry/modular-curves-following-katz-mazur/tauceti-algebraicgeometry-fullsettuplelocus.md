---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.fullSetTupleLocus
statement: formalized
---

# TauCeti.AlgebraicGeometry.fullSetTupleLocus

The ideal sheaf of the **scheme of full sets of sections** of `g` indexed by `ι`
(Katz–Mazur 1.9.1): the full-set locus of the universal family of sections over the scheme of
tuples of sections. Its closed subscheme represents the `ι`-indexed full sets of sections
(`fullSetTupleLocus_le_ker_lift_iff`).

```lean
TauCeti.AlgebraicGeometry.fullSetTupleLocus.{u} {Z S : AlgebraicGeometry.Scheme} (g : Z ⟶ S)
  (ι : Type) [Fintype ι] [AlgebraicGeometry.IsFinite g] [AlgebraicGeometry.Flat g]
  [AlgebraicGeometry.LocallyOfFinitePresentation g] :
  (TauCeti.AlgebraicGeometry.sectionTupleScheme g ι).IdealSheafData
```

## Depends on

- [TauCeti.AlgebraicGeometry.fullSetLocus](tauceti-algebraicgeometry-fullsetlocus.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.fullSetTupleLocus`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FullSetOfSections/Locus.html#TauCeti.AlgebraicGeometry.fullSetTupleLocus).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.fullSetTupleLocus`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FullSetOfSections/Locus.html#TauCeti.AlgebraicGeometry.fullSetTupleLocus)
- [Source of `TauCeti.AlgebraicGeometry.fullSetTupleLocus` in TauCeti/AlgebraicGeometry/FullSetOfSections/Locus.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/FullSetOfSections/Locus.lean#L61)
- [Tau Ceti roadmap status: Modular curves, following Katz–Mazur](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ModularCurves/STATUS.md)
