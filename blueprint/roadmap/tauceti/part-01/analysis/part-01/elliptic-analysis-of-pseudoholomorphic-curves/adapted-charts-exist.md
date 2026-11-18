---
declaration: theorem
origin: cited
lean: TauCeti.exists_adaptedChart
statement: formalized
proof: formalized
---

# Adapted charts exist

Let `γ` be `C^(ℓ+1)` on an open `U` and `J` be `C^ℓ` on an open `Ω`
containing `γ (U)`, with `1 ≤ ℓ`. If at `x₀ ∈ U` the tangent map `Dγ x₀` is injective with
image maximal totally real for `J (γ x₀)`, and `J (γ x₀)² = -1`, then the adapted extension
restricts to a partial homeomorphism around `(x₀, 0)` with source in `U × V`, target in `Ω`,
and which is `C^ℓ` with `C^ℓ` inverse. Its inverse is the adapted chart.

```lean
TauCeti.exists_adaptedChart.{u_1, u_2, u_3} {𝕜 : Type u_1} {V : Type u_2} {W : Type u_3} [RCLike 𝕜]
  [NormedAddCommGroup V] [NormedSpace 𝕜 V] [NormedAddCommGroup W] [NormedSpace 𝕜 W] {γ : V → W}
  {J : W → W →L[𝕜] W} [CompleteSpace V] [CompleteSpace W] {U : Set V} {Ω : Set W} {x₀ : V}
  {ℓ : WithTop ℕ∞} (hU : IsOpen U) (hΩ : IsOpen Ω) (hx₀ : x₀ ∈ U) (hℓ : 1 ≤ ℓ)
  (hγ : ContDiffOn 𝕜 (ℓ + 1) γ U) (hJ : ContDiffOn 𝕜 ℓ J Ω) (hγΩ : Set.MapsTo γ U Ω)
  (hsq : ∀ (v : W), (J (γ x₀)) ((J (γ x₀)) v) = -v) (hinj : Function.Injective ⇑(fderiv 𝕜 γ x₀))
  (htr : TauCeti.IsMaximalTotallyReal (↑(J (γ x₀))) (↑(fderiv 𝕜 γ x₀)).range) :
  ∃ e,
    ↑e = TauCeti.adaptedNormalExtension γ J ∧
      (x₀, 0) ∈ e.source ∧
        e.source ⊆ U ×ˢ Set.univ ∧
          e.target ⊆ Ω ∧ ContDiffOn 𝕜 ℓ (↑e) e.source ∧ ContDiffOn 𝕜 ℓ (↑e.symm) e.target
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The inverse function theorem for a converging family](../../part-03/calculus/part-01/the-inverse-function-theorem-for-a-converging-fa.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_adaptedChart`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/AdaptedChart.html#TauCeti.exists_adaptedChart).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_adaptedChart`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/AdaptedChart.html#TauCeti.exists_adaptedChart)
- [Source of `TauCeti.exists_adaptedChart` in TauCeti/Analysis/Calculus/AdaptedChart.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Calculus/AdaptedChart.lean#L146)
- [Tau Ceti roadmap status: Elliptic analysis of pseudoholomorphic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PseudoholomorphicCurveAnalysis/STATUS.md)
