---
declaration: def
origin: cited
lean: TauCeti.CompatibleCouple.KMethodSpace
statement: formalized
---

# TauCeti.CompatibleCouple.KMethodSpace

The real interpolation space `(X₀, X₁)_{θ,q}` of the `K`-method, as a type: the elements of
`C.kMethod θ q`, normed by the `K`-method norm `‖u‖_{θ,q} = ‖t ↦ t ^ (-θ) K(t, u)‖_{L^q(dt / t)}`
instead of the sum norm. It is a normed space for `1 ≤ q` and a `T₁` ambient space, and a Banach
space when `X₀` and `X₁` are.

```lean
TauCeti.CompatibleCouple.KMethodSpace.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1} {X₀ : Type u_2}
  {X₁ : Type u_3} {V : Type u_4} [NormedField 𝕜] [NormedAddCommGroup X₀] [NormedSpace 𝕜 X₀]
  [NormedAddCommGroup X₁] [NormedSpace 𝕜 X₁] [AddCommGroup V] [_root_.Module 𝕜 V]
  [TopologicalSpace V] [ContinuousAdd V] (C : TauCeti.CompatibleCouple 𝕜 X₀ X₁ V) (θ : ℝ)
  (q : ENNReal) : Type (max u_2 u_3)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CompatibleCouple.KMethodSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Interpolation/RealMethod.html#TauCeti.CompatibleCouple.KMethodSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.CompatibleCouple.KMethodSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Interpolation/RealMethod.html#TauCeti.CompatibleCouple.KMethodSpace)
- [Source of `TauCeti.CompatibleCouple.KMethodSpace` in TauCeti/Analysis/Normed/Interpolation/RealMethod.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Interpolation/RealMethod.lean#L340)
- [Tau Ceti roadmap status: Pseudodifferential operators and elliptic analysis on bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PseudodifferentialOperators/STATUS.md)
