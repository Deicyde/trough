---
declaration: theorem
origin: cited
lean: WeierstrassCurve.finite_selmerGroup
statement: formalized
proof: formalized
---

# WeierstrassCurve.finite\_selmerGroup

**The `m`-Selmer group of an elliptic curve over a number field is finite** (Silverman
X.4.2). The local conditions are the images of the Kummer maps over the completions at all finite
places. The conclusion holds for every nonzero natural number `m`.

```lean
WeierstrassCurve.finite_selmerGroup.{u_1} {K : Type u_1} [Field K] [NumberField K]
  (W : WeierstrassCurve K) [W.IsElliptic] (m : ℕ) [NeZero m]
  (τ :
    (v : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K)) →
      SeparableClosure K →ₐ[K]
        SeparableClosure (IsDedekindDomain.HeightOneSpectrum.adicCompletion K v)) :
  Finite ↥(W.selmerGroup τ m)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.algebraicExtensionNormedField](../../part-04/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.hurwitz\_genus\_formula](../../part-01/algebraic-curves-function-fields-divisors-and-ri/tauceti-hurwitz-genus-formula.md)
- [TauCeti.Ring.IsJapanese](../../part-06/scheme-stack-cohomology-and-intersection-foundat/tauceti-ring-isjapanese.md)

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.finite_selmerGroup`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/Selmer/Finite.html#WeierstrassCurve.finite_selmerGroup).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.finite_selmerGroup`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/Selmer/Finite.html#WeierstrassCurve.finite_selmerGroup)
- [Source of `WeierstrassCurve.finite_selmerGroup` in TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/Selmer/Finite.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/Selmer/Finite.lean#L54)
- [Tau Ceti roadmap status: Elliptic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/EllipticCurves/STATUS.md)
