---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.EllipticCurveGeom.existsUnique_hom_of_mapsZero
statement: formalized
proof: formalized
---

# Katz–Mazur 2.5.1, unique lifting

Every pointed morphism of schemes `f : E ⟶ E'` over `S`
underlies a unique homomorphism `E.toCommGrp ⟶ E'.toCommGrp` of elliptic curves over `S`.

```lean
TauCeti.AlgebraicGeometry.EllipticCurveGeom.existsUnique_hom_of_mapsZero.{u}
  {S : AlgebraicGeometry.Scheme} {E E' : TauCeti.AlgebraicGeometry.EllipticCurveGeom S}
  (f : E.carrier ⟶ E'.carrier)
  (hf : CategoryTheory.CategoryStruct.comp f E'.structureMap = E.structureMap)
  (h0 : CategoryTheory.CategoryStruct.comp E.zero f = E'.zero) :
  ∃! F, CategoryTheory.Over.Hom.left F.hom.hom.hom = f
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.EllipticCurveGeom.existsUnique_hom_of_mapsZero`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/Geom/Hom/Pointed.html#TauCeti.AlgebraicGeometry.EllipticCurveGeom.existsUnique_hom_of_mapsZero).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.EllipticCurveGeom.existsUnique_hom_of_mapsZero`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/Geom/Hom/Pointed.html#TauCeti.AlgebraicGeometry.EllipticCurveGeom.existsUnique_hom_of_mapsZero)
- [Source of `TauCeti.AlgebraicGeometry.EllipticCurveGeom.existsUnique_hom_of_mapsZero` in TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/Geom/Hom/Pointed.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/Geom/Hom/Pointed.lean#L137)
- [Tau Ceti roadmap status: Modular curves and the moduli of elliptic curves with level structure](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ModularCurves/STATUS.md)
