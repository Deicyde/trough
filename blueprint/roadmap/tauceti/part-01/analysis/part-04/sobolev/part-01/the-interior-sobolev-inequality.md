---
declaration: theorem
origin: cited
lean: TauCeti.W1p.exists_eLpNorm_value_le_of_isCompact_closure, TauCeti.W1p.exists_eLpNorm_value_le_of_inv_sub_inv_le
statement: formalized
proof: formalized
---

# The interior Sobolev inequality

If `V` has compact closure contained in the open set
`Ω`, `1 ≤ p` and `1/p⋆ + 1/n = 1/p` with `p⋆ < ∞`, then for every `q ≤ p⋆` there is a constant
`C` with `‖u‖_{L^q(V)} ≤ C ‖u‖_{W^{1,p}(Ω)}` for all `u ∈ W^{1,p}(Ω)`. The full Sobolev norm is
needed on the right: on a bounded `Ω`, a nonzero constant has vanishing gradient.

```lean
TauCeti.W1p.exists_eLpNorm_value_le_of_isCompact_closure.{u_1} {E : Type u_1} [MeasurableSpace E]
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [BorelSpace E] {mu : MeasureTheory.Measure E}
  [mu.IsAddHaarMeasure] {Omega : TopologicalSpace.Opens E} {p pstar : ENNReal} [Fact (1 ≤ p)]
  (hpstar : pstar ≠ ⊤) (hexp : pstar⁻¹ + (↑(Module.finrank ℝ E))⁻¹ = p⁻¹) {V : Set E}
  (hVc : IsCompact (closure V)) (hVO : closure V ⊆ ↑Omega) {q : ENNReal} (hq : q ≤ pstar) :
  ∃ C,
    ∀ (u : ↥(TauCeti.W1p mu Omega p)),
      MeasureTheory.eLpNorm (↑↑(TauCeti.W1p.value u)) q (mu.restrict V) ≤ ↑C * ‖u‖ₑ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Gagliardo–Nirenberg–Sobolev inequality in dimension two](the-gagliardo-nirenberg-sobolev-inequality-in-di.md)
- [The Sobolev inequality on `W^{1,p}_0` of a ball](../part-02/the-sobolev-inequality-on-w-1-p-0-of-a-ball.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.W1p.exists_eLpNorm_value_le_of_isCompact_closure`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/W1p/SobolevEmbedding.html#TauCeti.W1p.exists_eLpNorm_value_le_of_isCompact_closure).

## Other forms

**The interior Sobolev inequality for every admissible gain.** Formalized in Tau Ceti as [`TauCeti.W1p.exists_eLpNorm_value_le_of_inv_sub_inv_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/W1p/SobolevEmbedding.html#TauCeti.W1p.exists_eLpNorm_value_le_of_inv_sub_inv_le).

```lean
TauCeti.W1p.exists_eLpNorm_value_le_of_inv_sub_inv_le.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] {Ω : TopologicalSpace.Opens E} {q s : NNReal}
  [Fact (1 ≤ ↑q)] (hqs : q ≤ s) (hgap : (↑q)⁻¹ - (↑s)⁻¹ ≤ (↑(Module.finrank ℝ E))⁻¹) {V : Set E}
  (hVc : IsCompact (closure V)) (hVΩ : closure V ⊆ ↑Ω) :
  ∃ C,
    ∀ (u : ↥(TauCeti.W1p μ Ω ↑q)),
      MeasureTheory.eLpNorm (↑↑(TauCeti.W1p.value u)) (↑s) (μ.restrict V) ≤ ↑C * ‖u‖ₑ
```

## Sources

- [Tau Ceti documentation: `TauCeti.W1p.exists_eLpNorm_value_le_of_isCompact_closure`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/W1p/SobolevEmbedding.html#TauCeti.W1p.exists_eLpNorm_value_le_of_isCompact_closure)
- [Source of `TauCeti.W1p.exists_eLpNorm_value_le_of_isCompact_closure` in TauCeti/Analysis/Sobolev/W1p/SobolevEmbedding.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Sobolev/W1p/SobolevEmbedding.lean#L232)
