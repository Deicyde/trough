---
declaration: theorem
origin: cited
lean: WeierstrassCurve.finite_selmerGroup
statement: formalized
proof: formalized
---

# The `m`-Selmer group of an elliptic curve over a number field is finite (Silverman X.4.2)

The local conditions are the images of the Kummer maps over the completions at all finite
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

- [Dedekind's different theorem, first part (Stichtenoth, Theorem 3.5.1(a))](../../field-theory/function-field/part-01/dedekinds-different-theorem-first-part-stichteno.md)
- [Dedekind's different theorem, the tame case](../../number-theory/part-02/local-field/dedekinds-different-theorem-the-tame-case.md)
- [Euler's theorem on an `n`-th root of unity](../../group-theory/other-results/eulers-theorem-on-an-n-th-root-of-unity.md)
- [The first half of Dedekind's different theorem](../../number-theory/part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [The fundamental identity](../../field-theory/function-field/part-01/the-fundamental-identity.md)
- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](../../field-theory/function-field/part-01/the-fundamental-inequality-stichtenoth-theorem-3.md)
- [The Hurwitz genus formula (Stichtenoth, Theorem 3.4.13)](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/the-hurwitz-genus-formula-stichtenoth-theorem-3.md)
- [Krull–Akizuki for Mathlib's `integralClosure`](../../ring-theory/part-02/other-results/part-01/krull-akizuki-for-mathlibs-integralclosure.md)
- [Riemann's theorem](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/riemanns-theorem.md)
- [TauCeti.algebraicExtensionNormedField](../../number-theory/part-01/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.Ring.IsJapanese](../../ring-theory/part-01/scheme-stack-cohomology-and-intersection-foundat/tauceti-ring-isjapanese.md)
- [Vieta's formula at a pair of parameters, cleared of the inverse of the cubic's leading coefficient](../elliptic-curve/part-01/vietas-formula-at-a-pair-of-parameters-cleared-o.md)
- [The weak approximation theorem](../../field-theory/function-field/part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.finite_selmerGroup`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/Selmer/Finite.html#WeierstrassCurve.finite_selmerGroup).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.finite_selmerGroup`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/Selmer/Finite.html#WeierstrassCurve.finite_selmerGroup)
- [Source of `WeierstrassCurve.finite_selmerGroup` in TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/Selmer/Finite.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/Selmer/Finite.lean#L54)
- [Tau Ceti roadmap status: Elliptic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/EllipticCurves/STATUS.md)
