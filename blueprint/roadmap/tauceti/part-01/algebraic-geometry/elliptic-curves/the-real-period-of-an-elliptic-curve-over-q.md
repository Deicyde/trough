---
declaration: def
origin: cited
lean: WeierstrassCurve.minimalRealPeriod
statement: formalized
---

# The real period of an elliptic curve over `ℚ`

the real period `Ω` of the base change to
`ℝ` of its reduced minimal model. Every global minimal equation of `E` has this real period
(`WeierstrassCurve.IsGlobalMinimal.minimalRealPeriod_eq`), and it depends only on the
`ℚ`-isomorphism class of `E` (`WeierstrassCurve.VariableChange.minimalRealPeriod_smul`).

```lean
WeierstrassCurve.minimalRealPeriod (E : WeierstrassCurve ℚ) [E.IsElliptic] : ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.minimalRealPeriod`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/MinimalModel/RealPeriod.html#WeierstrassCurve.minimalRealPeriod).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.minimalRealPeriod`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/MinimalModel/RealPeriod.html#WeierstrassCurve.minimalRealPeriod)
- [Source of `WeierstrassCurve.minimalRealPeriod` in TauCeti/AlgebraicGeometry/EllipticCurve/MinimalModel/RealPeriod.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/MinimalModel/RealPeriod.lean#L66)
- [Tau Ceti roadmap status: Elliptic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EllipticCurves/STATUS.md)
