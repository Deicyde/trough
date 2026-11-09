---
declaration: theorem
origin: cited
lean: TauCeti.W1p.exists_eLpNorm_value_le_of_isCompact_closure
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
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [BorelSpace E]
  {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure] {Omega : TopologicalSpace.Opens E}
  {p pstar : ENNReal} [Fact (1 ≤ p)] (hpstar : pstar ≠ ⊤)
  (hexp : pstar⁻¹ + (↑(Module.finrank ℝ E))⁻¹ = p⁻¹) {V : Set E} (hVc : IsCompact (closure V))
  (hVO : closure V ⊆ ↑Omega) {q : ENNReal} (hq : q ≤ pstar) :
  ∃ C,
    ∀ (u : ↥(TauCeti.W1p mu Omega p)),
      MeasureTheory.eLpNorm (↑↑(TauCeti.W1p.value u)) q (mu.restrict V) ≤ ↑C * ‖u‖ₑ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Gagliardo--Nirenberg--Sobolev inequality on `W^{1,p}(E)`](the-gagliardo-nirenberg-sobolev-inequality-on-w.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.W1p.exists_eLpNorm_value_le_of_isCompact_closure`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/W1p/SobolevEmbedding.html#TauCeti.W1p.exists_eLpNorm_value_le_of_isCompact_closure).

## Sources

- [Tau Ceti documentation: `TauCeti.W1p.exists_eLpNorm_value_le_of_isCompact_closure`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/W1p/SobolevEmbedding.html#TauCeti.W1p.exists_eLpNorm_value_le_of_isCompact_closure)
- [Source of `TauCeti.W1p.exists_eLpNorm_value_le_of_isCompact_closure` in TauCeti/Analysis/Sobolev/W1p/SobolevEmbedding.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Sobolev/W1p/SobolevEmbedding.lean#L213)
