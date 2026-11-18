---
declaration: theorem
origin: cited
lean: TauCeti.eLpNorm_le_totalVariationOn
statement: formalized
proof: formalized
---

# The Sobolev inequality for functions of bounded variation

Let `E` have dimension
`n ≥ 2` and let `p = n / (n - 1)`. Every integrable `u : E → ℝ` satisfies `‖u‖_p ≤ C |Du|(E)`,
where `|Du|(E)` is the total variation of `u` on the whole space, finite or infinite, and `C` is
the constant `MeasureTheory.eLpNormLESNormFDerivOneConst μ p` of the `C¹` Gagliardo–Nirenberg–
Sobolev inequality `MeasureTheory.eLpNorm_le_eLpNorm_fderiv_one`.

```lean
TauCeti.eLpNorm_le_totalVariationOn.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] {p : NNReal} {u : E → ℝ}
  (hu : MeasureTheory.Integrable u μ) (hp : (↑(Module.finrank ℝ E)).HolderConjugate p) :
  MeasureTheory.eLpNorm u (↑p) μ ≤
    ↑(MeasureTheory.eLpNormLESNormFDerivOneConst μ ↑p) * TauCeti.totalVariationOn μ ⊤ u
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Gagliardo–Nirenberg–Sobolev inequality for integrable functions](../../part-04/other-results/the-gagliardo-nirenberg-sobolev-inequality-for-i.md)
- [Rademacher's theorem for locally Lipschitz functions](../calculus/part-02/rademachers-theorem-for-locally-lipschitz-functi.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.eLpNorm_le_totalVariationOn`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/Sobolev/Basic.html#TauCeti.eLpNorm_le_totalVariationOn).

## Sources

- [Tau Ceti documentation: `TauCeti.eLpNorm_le_totalVariationOn`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/Sobolev/Basic.html#TauCeti.eLpNorm_le_totalVariationOn)
- [Source of `TauCeti.eLpNorm_le_totalVariationOn` in TauCeti/Analysis/BoundedVariation/Sobolev/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/BoundedVariation/Sobolev/Basic.lean#L65)
