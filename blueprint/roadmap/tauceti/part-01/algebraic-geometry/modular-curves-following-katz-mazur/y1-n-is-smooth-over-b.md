---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.EllObj.smooth_yOne_structureMap
statement: formalized
proof: formalized
---

# `Y₁(N)` is smooth over `B`

For `N ≥ 4` invertible on `B`, the structure morphism of the
fine moduli scheme `Y₁(N)` to `B` is smooth; for example `Y₁(N)` is smooth over `ℤ[1/N]`.

```lean
TauCeti.AlgebraicGeometry.EllObj.smooth_yOne_structureMap.{u} (B : AlgebraicGeometry.Scheme) (N : ℕ)
  [NeZero N] (hN : ∀ (b : ↥B), ↑N ≠ 0) (h4 : 4 ≤ N) :
  AlgebraicGeometry.Smooth (TauCeti.AlgebraicGeometry.EllObj.yOne B N).structureMap
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [`Y₁(N)` is a fine moduli scheme for `N ≥ 4`](y1-n-is-a-fine-moduli-scheme-for-n-4.md)
- [The global dimension of a regular local ring is its Krull dimension](../../ring-theory/part-01/purity-of-the-branch-locus/the-global-dimension-of-a-regular-local-ring-is.md)
- [The Jacobian criterion for étaleness](../../ring-theory/part-02/other-results/part-02/the-jacobian-criterion-for-etaleness.md)
- [Serre's theorem (`TauCeti.IsRegularLocalRing.of_hasProjectiveDimensionLE`)](../../ring-theory/part-01/purity-of-the-branch-locus/serres-theorem-tauceti-isregularlocalring-of-has.md)
- [TauCeti.globalDimension](../../ring-theory/part-01/purity-of-the-branch-locus/tauceti-globaldimension.md)
- [Vieta's formula at a pair of parameters, cleared of the inverse of the cubic's leading coefficient](../elliptic-curve/vietas-formula-at-a-pair-of-parameters-cleared-o.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.EllObj.smooth_yOne_structureMap`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/ModularCurve/YOne.html#TauCeti.AlgebraicGeometry.EllObj.smooth_yOne_structureMap).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.EllObj.smooth_yOne_structureMap`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/ModularCurve/YOne.html#TauCeti.AlgebraicGeometry.EllObj.smooth_yOne_structureMap)
- [Source of `TauCeti.AlgebraicGeometry.EllObj.smooth_yOne_structureMap` in TauCeti/AlgebraicGeometry/ModularCurve/YOne.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/ModularCurve/YOne.lean#L761)
- [Tau Ceti roadmap status: Modular curves, following Katz–Mazur](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ModularCurves/STATUS.md)
