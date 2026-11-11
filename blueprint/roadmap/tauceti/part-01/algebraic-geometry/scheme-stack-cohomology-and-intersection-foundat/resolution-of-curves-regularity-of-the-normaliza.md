---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.isRegular_normalization_fromSpecStalk_genericPoint
statement: formalized
proof: formalized
---

# Resolution of curves: regularity of the normalization

Let `Y` be an integral locally
Noetherian scheme of dimension at most one, and suppose that the normalization of `Y` in its
function field, along `Spec k(Y) ⟶ Y`, is finite over `Y`. Then this normalization is a regular
scheme.

```lean
TauCeti.AlgebraicGeometry.isRegular_normalization_fromSpecStalk_genericPoint.{u}
  {Y : AlgebraicGeometry.Scheme} [AlgebraicGeometry.IsIntegral Y]
  [AlgebraicGeometry.IsLocallyNoetherian Y] (hY : topologicalKrullDim ↥Y ≤ 1)
  [AlgebraicGeometry.IsFinite
      (AlgebraicGeometry.Scheme.Hom.fromNormalization (Y.fromSpecStalk (genericPoint ↥Y)))] :
  TauCeti.AlgebraicGeometry.IsRegular
    (AlgebraicGeometry.Scheme.Hom.normalization (Y.fromSpecStalk (genericPoint ↥Y)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.isRegular_normalization_fromSpecStalk_genericPoint`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Normalization/Regular.html#TauCeti.AlgebraicGeometry.isRegular_normalization_fromSpecStalk_genericPoint).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.isRegular_normalization_fromSpecStalk_genericPoint`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Normalization/Regular.html#TauCeti.AlgebraicGeometry.isRegular_normalization_fromSpecStalk_genericPoint)
- [Source of `TauCeti.AlgebraicGeometry.isRegular_normalization_fromSpecStalk_genericPoint` in TauCeti/AlgebraicGeometry/Normalization/Regular.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/Normalization/Regular.lean#L108)
- [Tau Ceti roadmap status: Scheme, stack, cohomology and intersection foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SchemeAndStackFoundations/STATUS.md)
