---
declaration: def
origin: cited
lean: TauCeti.DescentDatum.descended
statement: formalized
---

# TauCeti.DescentDatum.descended

The scheme descended from a descent datum `D` on an affine morphism `X ⟶ S'`: the relative
spectrum over `S` of the functions on `X` whose pullbacks along the action and along the second
projection `S' ×_S X ⟶ X` agree.

```lean
TauCeti.DescentDatum.descended.{u} {S S' : AlgebraicGeometry.Scheme} {p : S' ⟶ S}
  [AlgebraicGeometry.IsAffineHom p] {X : CategoryTheory.Over S'}
  [AlgebraicGeometry.IsAffineHom X.hom] (D : TauCeti.DescentDatum p X) : CategoryTheory.Over S
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.DescentDatum.descended`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Descent/AffineMorphism.html#TauCeti.DescentDatum.descended).

## Sources

- [Tau Ceti documentation: `TauCeti.DescentDatum.descended`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Descent/AffineMorphism.html#TauCeti.DescentDatum.descended)
- [Source of `TauCeti.DescentDatum.descended` in TauCeti/AlgebraicGeometry/Descent/AffineMorphism.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Descent/AffineMorphism.lean#L105)
- [Tau Ceti roadmap status: Modular curves, following Katz–Mazur](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ModularCurves/STATUS.md)
