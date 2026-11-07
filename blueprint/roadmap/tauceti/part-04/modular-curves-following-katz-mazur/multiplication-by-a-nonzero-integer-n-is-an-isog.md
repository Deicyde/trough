---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.EllipticCurveGeom.isogenyOfDegree_intCast
statement: formalized
proof: formalized
---

# Multiplication by a nonzero integer `n` is an isogeny of degree `n²`

```lean
TauCeti.AlgebraicGeometry.EllipticCurveGeom.isogenyOfDegree_intCast.{u}
  {S : AlgebraicGeometry.Scheme} (E : TauCeti.AlgebraicGeometry.EllipticCurveGeom S) {n : ℤ}
  (hn : n ≠ 0) : TauCeti.GroupScheme.IsogenyOfDegree (↑n).asHom.hom (n.natAbs ^ 2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.EllipticCurveGeom.isogenyOfDegree_intCast`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/Geom/Isogeny.html#TauCeti.AlgebraicGeometry.EllipticCurveGeom.isogenyOfDegree_intCast).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.EllipticCurveGeom.isogenyOfDegree_intCast`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/Geom/Isogeny.html#TauCeti.AlgebraicGeometry.EllipticCurveGeom.isogenyOfDegree_intCast)
- [Source of `TauCeti.AlgebraicGeometry.EllipticCurveGeom.isogenyOfDegree_intCast` in TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/Geom/Isogeny.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/Geom/Isogeny.lean#L131)
- [Tau Ceti roadmap status: Modular curves, following Katz–Mazur](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ModularCurves/STATUS.md)
