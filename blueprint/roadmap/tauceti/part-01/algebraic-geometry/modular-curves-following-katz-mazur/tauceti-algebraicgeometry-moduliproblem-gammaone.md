---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.ModuliProblem.gammaOneRepresentableBy
statement: formalized
---

# TauCeti.AlgebraicGeometry.ModuliProblem.gammaOneRepresentableBy

For `N ≥ 4` invertible on `B`, the existing fine curve `Y₁(N)` also represents the
integral Drinfeld `[Γ₁(N)]` problem restricted to `B`.

```lean
TauCeti.AlgebraicGeometry.ModuliProblem.gammaOneRepresentableBy.{u} {B : AlgebraicGeometry.Scheme}
  {N : ℕ} [NeZero N] {hN : ∀ (b : ↥B), ↑N ≠ 0} (h4 : 4 ≤ N) :
  CategoryTheory.Functor.RepresentableBy (TauCeti.AlgebraicGeometry.ModuliProblem.gammaOne B N)
    (TauCeti.AlgebraicGeometry.EllObj.yOne B N)
```

## Depends on

- [`Y₁(N)` is a fine moduli scheme for `N ≥ 4`](y1-n-is-a-fine-moduli-scheme-for-n-4.md)

## Proof depends on

- [Deligne's theorem (`TauCeti.AlgebraicGeometry.FiniteFlatCommGroupScheme.pow_eq_one_of_finrank`)](../other-results/delignes-theorem-tauceti-algebraicgeometry-finit.md)
- [The global dimension of a regular local ring is its Krull dimension](../../ring-theory/part-01/purity-of-the-branch-locus/the-global-dimension-of-a-regular-local-ring-is.md)
- [The Jacobian criterion for étaleness](../../ring-theory/part-02/other-results/part-02/the-jacobian-criterion-for-etaleness.md)
- [Serre's theorem (`TauCeti.IsRegularLocalRing.of_hasProjectiveDimensionLE`)](../../ring-theory/part-01/purity-of-the-branch-locus/serres-theorem-tauceti-isregularlocalring-of-has.md)
- [TauCeti.globalDimension](../../ring-theory/part-01/purity-of-the-branch-locus/tauceti-globaldimension.md)
- [Vieta's formula at a pair of parameters, cleared of the inverse of the cubic's leading coefficient](../elliptic-curve/vietas-formula-at-a-pair-of-parameters-cleared-o.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.ModuliProblem.gammaOneRepresentableBy`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/ModularCurve/Comparison.html#TauCeti.AlgebraicGeometry.ModuliProblem.gammaOneRepresentableBy).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.ModuliProblem.gammaOneRepresentableBy`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/ModularCurve/Comparison.html#TauCeti.AlgebraicGeometry.ModuliProblem.gammaOneRepresentableBy)
- [Source of `TauCeti.AlgebraicGeometry.ModuliProblem.gammaOneRepresentableBy` in TauCeti/AlgebraicGeometry/ModularCurve/Comparison.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/ModularCurve/Comparison.lean#L186)
- [Tau Ceti roadmap status: Modular curves, following Katz–Mazur](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ModularCurves/STATUS.md)
