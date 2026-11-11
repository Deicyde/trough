---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.ModuliProblem.hasProperty_etale_gammaRelRepData
statement: formalized
proof: formalized
---

# The moduli problem `[Γ(N)]` is étale over `Ell/B` when `N` is invertible on `B` (Katz–Mazur, 3.7.1)

where `N` is invertible on `B`, `[Γ(N)]` is isomorphic to `[Γ(N)]_naive`,
whose representing schemes are étale over their bases. Together with
`ModuliProblem.hasProperty_isFinite_gammaRelRepData`, this makes `[Γ(N)]` finite étale over
`Ell/B`.

```lean
TauCeti.AlgebraicGeometry.ModuliProblem.hasProperty_etale_gammaRelRepData.{u}
  (B : AlgebraicGeometry.Scheme) (N : ℕ) [NeZero N] (hN : ∀ (b : ↥B), ↑N ≠ 0) :
  (TauCeti.AlgebraicGeometry.ModuliProblem.gammaRelRepData B N).HasProperty @AlgebraicGeometry.Etale
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Drinfeld and naive `[Γ(N)]`-structures coincide where `N` is invertible (Katz–Mazur, §3.7)](drinfeld-and-naive-n-structures-coincide-where-n.md)
- [The global dimension of a regular local ring is its Krull dimension](../../ring-theory/part-01/purity-of-the-branch-locus/the-global-dimension-of-a-regular-local-ring-is.md)
- [The Jacobian criterion for étaleness](../../ring-theory/part-02/other-results/part-02/the-jacobian-criterion-for-etaleness.md)
- [Serre's theorem (`TauCeti.IsRegularLocalRing.of_hasProjectiveDimensionLE`)](../../ring-theory/part-01/purity-of-the-branch-locus/serres-theorem-tauceti-isregularlocalring-of-has.md)
- [TauCeti.globalDimension](../../ring-theory/part-01/purity-of-the-branch-locus/tauceti-globaldimension.md)
- [Vieta's formula at a pair of parameters, cleared of the inverse of the cubic's leading coefficient](../elliptic-curve/vietas-formula-at-a-pair-of-parameters-cleared-o.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.ModuliProblem.hasProperty_etale_gammaRelRepData`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/ModularCurve/Comparison.html#TauCeti.AlgebraicGeometry.ModuliProblem.hasProperty_etale_gammaRelRepData).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.ModuliProblem.hasProperty_etale_gammaRelRepData`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/ModularCurve/Comparison.html#TauCeti.AlgebraicGeometry.ModuliProblem.hasProperty_etale_gammaRelRepData)
- [Source of `TauCeti.AlgebraicGeometry.ModuliProblem.hasProperty_etale_gammaRelRepData` in TauCeti/AlgebraicGeometry/ModularCurve/Comparison.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/ModularCurve/Comparison.lean#L356)
- [Tau Ceti roadmap status: Modular curves, following Katz–Mazur](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ModularCurves/STATUS.md)
