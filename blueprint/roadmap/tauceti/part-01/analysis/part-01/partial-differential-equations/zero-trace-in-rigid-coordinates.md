---
declaration: theorem
origin: cited
lean: TauCeti.W1p.mem_w1p0Submodule_iff_frontierTrace_compAffineIsometryEquivL_eq_zero
statement: formalized
proof: formalized
---

# Zero trace in rigid coordinates

Let an affine isometry `g` carry the open set `U ⊆ F`
onto a bounded Lipschitz domain `Ω`, so that `Ω = g.symm⁻¹(U)`. For `1 ≤ p < ∞`, a function
`u ∈ W^{1,p}(U)` lies in `W^{1,p}_0(U)` exactly when the trace of `u ∘ g⁻¹` on `frontier Ω`
vanishes.

```lean
TauCeti.W1p.mem_w1p0Submodule_iff_frontierTrace_compAffineIsometryEquivL_eq_zero.{u_1, u_2}
  {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] {Ω : TopologicalSpace.Opens (WithLp 2 (ℝ × E))} {L : NNReal}
  {p : ENNReal} [Fact (1 ≤ p)] {F : Type u_2} [NormedAddCommGroup F] [InnerProductSpace ℝ F]
  [FiniteDimensional ℝ F] [MeasurableSpace F] [BorelSpace F] {U : TopologicalSpace.Opens F}
  (hp : p ≠ ⊤) (hΩ : (↑Ω).IsLipschitzDomainWith L) (hb : Bornology.IsBounded ↑Ω)
  (g : F ≃ᵃⁱ[ℝ] WithLp 2 (ℝ × E)) (hΩU : ↑Ω = ⇑g.symm ⁻¹' ↑U)
  (u : ↥(TauCeti.W1p MeasureTheory.volume U p)) :
  u ∈ TauCeti.w1p0Submodule MeasureTheory.volume U p ↔
    (TauCeti.W1p.frontierTrace hp hΩ hb) ((TauCeti.W1p.compAffineIsometryEquivL g.symm hΩU) u) = 0
```

## Depends on

- [The trace operator of a bounded Lipschitz domain](the-trace-operator-of-a-bounded-lipschitz-domain.md)

## Proof depends on

- [The divergence theorem on a half-space (`TauCeti.setIntegral_normalHalfSpace_fderiv_apply`)](../../part-03/sobolev/part-01/the-divergence-theorem-on-a-half-space-tauceti-s.md)
- [Extension theorem for bounded Lipschitz domains](../../part-03/sobolev/part-01/extension-theorem-for-bounded-lipschitz-domains.md)
- [Rademacher's theorem for locally Lipschitz functions](../../part-02/calculus/part-02/rademachers-theorem-for-locally-lipschitz-functi.md)
- [TauCeti.Wkp](tauceti-wkp.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.W1p.mem_w1p0Submodule_iff_frontierTrace_compAffineIsometryEquivL_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/LipschitzDomain/Trace/Frontier.html#TauCeti.W1p.mem_w1p0Submodule_iff_frontierTrace_compAffineIsometryEquivL_eq_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.W1p.mem_w1p0Submodule_iff_frontierTrace_compAffineIsometryEquivL_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/LipschitzDomain/Trace/Frontier.html#TauCeti.W1p.mem_w1p0Submodule_iff_frontierTrace_compAffineIsometryEquivL_eq_zero)
- [Source of `TauCeti.W1p.mem_w1p0Submodule_iff_frontierTrace_compAffineIsometryEquivL_eq_zero` in TauCeti/Analysis/Sobolev/LipschitzDomain/Trace/Frontier.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Sobolev/LipschitzDomain/Trace/Frontier.lean#L467)
- [Tau Ceti roadmap status: Partial differential equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PDE/STATUS.md)
