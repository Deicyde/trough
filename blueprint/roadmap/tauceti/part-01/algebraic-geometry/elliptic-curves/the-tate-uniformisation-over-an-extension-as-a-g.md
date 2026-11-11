---
declaration: def
origin: cited
lean: TauCeti.tateUniformizationBaseChangeEquiv
statement: formalized
---

# The Tate uniformisation over an extension as a group isomorphism `Lˣ / q^ℤ ≃ E_q(L)`, written additively on the source

```lean
TauCeti.tateUniformizationBaseChangeEquiv.{u_1, u_2} {K : Type u_1} [NormedField K]
  [CompleteSpace K] [IsUltrametricDist K] (L : Type u_2) [NormedField L] [NormedAlgebra K L]
  [CompleteSpace L] [IsUltrametricDist L] [DecidableEq L] (q : Kˣ) (hq : ‖↑q‖ < 1) :
  Additive (Lˣ ⧸ Subgroup.zpowers ((Units.map ↑(algebraMap K L)) q)) ≃+
    (WeierstrassCurve.toAffine
        (WeierstrassCurve.Affine.baseChange (TauCeti.tateCurveAt q hq) L)).Point
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.tateUniformizationBaseChangeEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/TateCurve/Surjectivity.html#TauCeti.tateUniformizationBaseChangeEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.tateUniformizationBaseChangeEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/TateCurve/Surjectivity.html#TauCeti.tateUniformizationBaseChangeEquiv)
- [Source of `TauCeti.tateUniformizationBaseChangeEquiv` in TauCeti/AlgebraicGeometry/EllipticCurve/TateCurve/Surjectivity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/TateCurve/Surjectivity.lean#L126)
- [Tau Ceti roadmap status: Elliptic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EllipticCurves/STATUS.md)
