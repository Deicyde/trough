---
declaration: def
origin: cited
lean: TauCeti.tateUniformizationEquiv
statement: formalized
---

# The Tate uniformisation as a group isomorphism `Kˣ / q^ℤ ≃ E_q(K)`, written additively on the source

```lean
TauCeti.tateUniformizationEquiv.{u_1} {K : Type u_1} [NormedField K] [CompleteSpace K]
  [IsUltrametricDist K] [DecidableEq K] (q : Kˣ) (hq : ‖↑q‖ < 1) :
  Additive (Kˣ ⧸ Subgroup.zpowers q) ≃+ (TauCeti.tateCurveAt q hq).toAffine.Point
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.tateUniformizationEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/TateCurve/Surjectivity.html#TauCeti.tateUniformizationEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.tateUniformizationEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/TateCurve/Surjectivity.html#TauCeti.tateUniformizationEquiv)
- [Source of `TauCeti.tateUniformizationEquiv` in TauCeti/AlgebraicGeometry/EllipticCurve/TateCurve/Surjectivity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/TateCurve/Surjectivity.lean#L89)
- [Tau Ceti roadmap status: Elliptic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EllipticCurves/STATUS.md)
