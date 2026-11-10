---
declaration: theorem
origin: cited
lean: TauCeti.setIntegral_normalHalfSpace_fderiv_apply
statement: formalized
proof: formalized
---

# The divergence theorem on a half-space (`TauCeti.setIntegral_normalHalfSpace_fderiv_apply`)

For a compactly supported `C¹` function `g` on
`ℝ × E` and a direction `v`, the integral of the directional derivative `∂_v g` over the half-space
`{x | a < x.fst}` is the boundary integral of `g` over `{a} × E`, weighted by `⟪v, -e₁⟫ = -v.fst`,
the normal component of `v` along the outward unit normal.

```lean
TauCeti.setIntegral_normalHalfSpace_fderiv_apply.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  {g : WithLp 2 (ℝ × E) → ℝ} (hg : ContDiff ℝ 1 g) (hgc : HasCompactSupport g) (a : ℝ)
  (v : WithLp 2 (ℝ × E)) :
  ∫ (x : WithLp 2 (ℝ × E)) in ↑(TauCeti.normalHalfSpace a), (fderiv ℝ g x) v =
    -(v.fst * ∫ (y : E), g (WithLp.toLp 2 (a, y)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.setIntegral_normalHalfSpace_fderiv_apply`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Trace/IntegrationByParts.html#TauCeti.setIntegral_normalHalfSpace_fderiv_apply).

## Sources

- [Tau Ceti documentation: `TauCeti.setIntegral_normalHalfSpace_fderiv_apply`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Trace/IntegrationByParts.html#TauCeti.setIntegral_normalHalfSpace_fderiv_apply)
- [Source of `TauCeti.setIntegral_normalHalfSpace_fderiv_apply` in TauCeti/Analysis/Sobolev/Trace/IntegrationByParts.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Sobolev/Trace/IntegrationByParts.lean#L71)
