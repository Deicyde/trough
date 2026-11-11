---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.EllipticCurveGeom.isogenyOfDegree_factorisationDual
statement: formalized
proof: formalized
---

# The factorisation dual of an isogeny of degree `n` is an isogeny of degree `n`

For an
isogeny `f : E ⟶ E'` of degree `n ≠ 0`, the factorisation dual `E' ⟶ E` is again an isogeny of
degree `n`; by `TauCeti.GroupScheme.factorisationDual_factorisationDual`, its own factorisation
dual is `f`.

```lean
TauCeti.AlgebraicGeometry.EllipticCurveGeom.isogenyOfDegree_factorisationDual.{u}
  {S : AlgebraicGeometry.Scheme} {E' E : TauCeti.AlgebraicGeometry.EllipticCurveGeom S}
  (f : E.toCommGrp ⟶ E'.toCommGrp) {n : ℕ} [NeZero n]
  (hf : TauCeti.GroupScheme.IsogenyOfDegree f.hom n) :
  TauCeti.GroupScheme.IsogenyOfDegree (TauCeti.GroupScheme.factorisationDual f hf).hom n
```

## Depends on

- [TauCeti.GroupScheme.factorisationDual](tauceti-groupscheme-factorisationdual.md)

## Proof depends on

- [Deligne's theorem (`TauCeti.AlgebraicGeometry.FiniteFlatCommGroupScheme.pow_eq_one_of_finrank`)](../other-results/delignes-theorem-tauceti-algebraicgeometry-finit.md)
- [The global dimension of a regular local ring is its Krull dimension](../../ring-theory/part-01/purity-of-the-branch-locus/the-global-dimension-of-a-regular-local-ring-is.md)
- [The Jacobian criterion for étaleness](../../ring-theory/part-02/other-results/part-02/the-jacobian-criterion-for-etaleness.md)
- [Serre's theorem (`TauCeti.IsRegularLocalRing.of_hasProjectiveDimensionLE`)](../../ring-theory/part-01/purity-of-the-branch-locus/serres-theorem-tauceti-isregularlocalring-of-has.md)
- [TauCeti.globalDimension](../../ring-theory/part-01/purity-of-the-branch-locus/tauceti-globaldimension.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.EllipticCurveGeom.isogenyOfDegree_factorisationDual`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/Geom/Isogeny.html#TauCeti.AlgebraicGeometry.EllipticCurveGeom.isogenyOfDegree_factorisationDual).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.EllipticCurveGeom.isogenyOfDegree_factorisationDual`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/Geom/Isogeny.html#TauCeti.AlgebraicGeometry.EllipticCurveGeom.isogenyOfDegree_factorisationDual)
- [Source of `TauCeti.AlgebraicGeometry.EllipticCurveGeom.isogenyOfDegree_factorisationDual` in TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/Geom/Isogeny.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/Geom/Isogeny.lean#L148)
- [Tau Ceti roadmap status: Modular curves, following Katz–Mazur](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ModularCurves/STATUS.md)
