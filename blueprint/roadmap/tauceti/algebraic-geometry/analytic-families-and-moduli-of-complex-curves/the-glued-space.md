---
declaration: abbrev
origin: cited
lean: TauCeti.NodalGluing.GluedCurve
statement: formalized
---

# The glued space

The quotient of the disjoint union of the normalization components by the
generated relation: the underlying topological space of the nodal curve.  The topology is the
quotient topology, i.e. the finest topology making the quotient map continuous.

```lean
TauCeti.NodalGluing.GluedCurve.{u_1, u_2, u_3} {ι : Type u_1} {Flag : Type u_2} {X : ι → Type u_3}
  (d : TauCeti.NodalGluing.FlagPairData ι Flag X) : Type (max u_3 u_1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NodalGluing.GluedCurve`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/NodalGluing/Basic.html#TauCeti.NodalGluing.GluedCurve).

## Sources

- [Tau Ceti documentation: `TauCeti.NodalGluing.GluedCurve`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/NodalGluing/Basic.html#TauCeti.NodalGluing.GluedCurve)
- [Source of `TauCeti.NodalGluing.GluedCurve` in TauCeti/AlgebraicGeometry/Curves/NodalGluing/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Curves/NodalGluing/Basic.lean#L474)
- [Tau Ceti roadmap status: Analytic families and moduli of complex curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexCurveModuli/STATUS.md)
