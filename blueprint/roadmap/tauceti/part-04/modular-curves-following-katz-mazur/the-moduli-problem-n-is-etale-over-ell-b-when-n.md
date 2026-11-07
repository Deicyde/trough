---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.ModuliProblem.hasProperty_etale_gammaRelRepData
statement: formalized
proof: formalized
---

# The moduli problem `[Γ(N)]` is étale over `Ell/B` when `N` is invertible on `B`

(Katz–Mazur, 3.7.1): where `N` is invertible on `B`, `[Γ(N)]` is isomorphic to `[Γ(N)]_naive`,
whose representing schemes are étale over their bases. Together with
`ModuliProblem.hasProperty_isFinite_gammaRelRepData`, this makes `[Γ(N)]` finite étale over
`Ell/B`.

```lean
TauCeti.AlgebraicGeometry.ModuliProblem.hasProperty_etale_gammaRelRepData.{u}
  (B : AlgebraicGeometry.Scheme) (N : ℕ) [NeZero N] (hN : ∀ (b : ↥B), ↑N ≠ 0) :
  (TauCeti.AlgebraicGeometry.ModuliProblem.gammaRelRepData B N).HasProperty @AlgebraicGeometry.Etale
```

## Depends on

- [The integral moduli problem `\[Γ(N)\]` is relatively representable](the-integral-moduli-problem-n-is-relatively-repr.md)

## Proof depends on

- [The `n`-torsion of an elliptic curve is étale where `n` is invertible](the-n-torsion-of-an-elliptic-curve-is-etale-wher.md)
- [Drinfeld and naive `\[Γ(N)\]`-structures coincide where `N` is invertible](drinfeld-and-naive-n-structures-coincide-where-n.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.ModuliProblem.hasProperty_etale_gammaRelRepData`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/ModularCurve/Comparison.html#TauCeti.AlgebraicGeometry.ModuliProblem.hasProperty_etale_gammaRelRepData).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.ModuliProblem.hasProperty_etale_gammaRelRepData`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/ModularCurve/Comparison.html#TauCeti.AlgebraicGeometry.ModuliProblem.hasProperty_etale_gammaRelRepData)
- [Source of `TauCeti.AlgebraicGeometry.ModuliProblem.hasProperty_etale_gammaRelRepData` in TauCeti/AlgebraicGeometry/ModularCurve/Comparison.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/ModularCurve/Comparison.lean#L356)
- [Tau Ceti roadmap status: Modular curves, following Katz–Mazur](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ModularCurves/STATUS.md)
