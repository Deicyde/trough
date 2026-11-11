---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.ModuliProblem.gammaIsoGammaNaive
statement: formalized
---

# Drinfeld and naive `[Γ(N)]`-structures coincide where `N` is invertible (Katz–Mazur, §3.7)

over a base `B` on which `N` is invertible, `gammaToGammaNaive` and `gammaNaiveToGamma` are
mutually inverse isomorphisms between `[Γ(N)]` and `[Γ(N)]_naive`.

```lean
TauCeti.AlgebraicGeometry.ModuliProblem.gammaIsoGammaNaive.{u} (B : AlgebraicGeometry.Scheme)
  (N : ℕ) [NeZero N] (hN : ∀ (b : ↥B), ↑N ≠ 0) :
  TauCeti.AlgebraicGeometry.ModuliProblem.gamma B N ≅
    TauCeti.AlgebraicGeometry.ModuliProblem.gammaNaive B N
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The global dimension of a regular local ring is its Krull dimension](../../ring-theory/part-01/purity-of-the-branch-locus/the-global-dimension-of-a-regular-local-ring-is.md)
- [The Jacobian criterion for étaleness](../../ring-theory/part-02/other-results/part-02/the-jacobian-criterion-for-etaleness.md)
- [Serre's theorem (`TauCeti.IsRegularLocalRing.of_hasProjectiveDimensionLE`)](../../ring-theory/part-01/purity-of-the-branch-locus/serres-theorem-tauceti-isregularlocalring-of-has.md)
- [TauCeti.globalDimension](../../ring-theory/part-01/purity-of-the-branch-locus/tauceti-globaldimension.md)
- [Vieta's formula at a pair of parameters, cleared of the inverse of the cubic's leading coefficient](../elliptic-curve/vietas-formula-at-a-pair-of-parameters-cleared-o.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.ModuliProblem.gammaIsoGammaNaive`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/ModularCurve/Comparison.html#TauCeti.AlgebraicGeometry.ModuliProblem.gammaIsoGammaNaive).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.ModuliProblem.gammaIsoGammaNaive`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/ModularCurve/Comparison.html#TauCeti.AlgebraicGeometry.ModuliProblem.gammaIsoGammaNaive)
- [Source of `TauCeti.AlgebraicGeometry.ModuliProblem.gammaIsoGammaNaive` in TauCeti/AlgebraicGeometry/ModularCurve/Comparison.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/ModularCurve/Comparison.lean#L299)
- [Tau Ceti roadmap status: Modular curves, following Katz–Mazur](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ModularCurves/STATUS.md)
