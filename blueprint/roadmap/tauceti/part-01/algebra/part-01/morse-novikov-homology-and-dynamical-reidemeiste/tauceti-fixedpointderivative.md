---
declaration: def
origin: cited
lean: TauCeti.fixedPointDerivative
statement: formalized
---

# TauCeti.fixedPointDerivative

The **fixed-point derivative** of `f : M → M` at a fixed point `x`: the differential
`df_x : T_x M → T_{f x} M`, viewed as an endomorphism of `T_x M` by transporting its target along
`f x = x`. Over `ℝ`, at a nondegenerate fixed point in the interior of the manifold, the sign of
`det (1 - df_x)` is the contribution of `x` to the Lefschetz fixed-point formula.

```lean
TauCeti.fixedPointDerivative.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1} {E : Type u_2} {H : Type u_3}
  {M : Type u_4} [NontriviallyNormedField 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  [TopologicalSpace H] (I : ModelWithCorners 𝕜 E H) [TopologicalSpace M] [ChartedSpace H M]
  (f : M → M) (x : { x // f x = x }) : TangentSpace I ↑x →ₗ[𝕜] TangentSpace I ↑x
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.fixedPointDerivative`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/MFDeriv/FixedPoint.html#TauCeti.fixedPointDerivative).

## Sources

- [Tau Ceti documentation: `TauCeti.fixedPointDerivative`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/MFDeriv/FixedPoint.html#TauCeti.fixedPointDerivative)
- [Source of `TauCeti.fixedPointDerivative` in TauCeti/Geometry/Manifold/MFDeriv/FixedPoint.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/MFDeriv/FixedPoint.lean#L387)
- [Tau Ceti roadmap status: Morse–Novikov homology and dynamical Reidemeister torsion](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MorseNovikov/STATUS.md)
