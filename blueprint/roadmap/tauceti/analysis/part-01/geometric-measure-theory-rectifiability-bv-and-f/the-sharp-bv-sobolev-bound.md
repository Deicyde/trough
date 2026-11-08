---
declaration: theorem
origin: cited
lean: TauCeti.eLpNorm_le_inv_mul_totalVariationOn
statement: formalized
proof: formalized
---

# The sharp BV Sobolev bound

In dimension `n ≥ 2`, every integrable real-valued
function satisfies `‖u‖ₚ ≤ (n ωₙ^(1/n))⁻¹ |Du|(E)` for `p = n / (n - 1)`.
The total variation may be infinite.

```lean
TauCeti.eLpNorm_le_inv_mul_totalVariationOn.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] {u : E → ℝ}
  {p : NNReal} (hu : MeasureTheory.Integrable u MeasureTheory.volume)
  (hp : (↑(Module.finrank ℝ E)).HolderConjugate p) :
  MeasureTheory.eLpNorm u (↑p) MeasureTheory.volume ≤
    (ENNReal.ofReal
          (↑(Module.finrank ℝ E) *
            MeasureTheory.volume.real (Metric.ball 0 1) ^ (↑(Module.finrank ℝ E))⁻¹))⁻¹ *
      TauCeti.totalVariationOn MeasureTheory.volume ⊤ u
```

## Depends on

- [TauCeti.totalVariationOn](tauceti-totalvariationon.md)

## Proof depends on

- [Brunn–Minkowski for a shell](../../../measure-theory/euclidean-isoperimetry-sharp-inequalities-and-ri/brunn-minkowski-for-a-shell.md)
- [The coarea formula for total variation](the-coarea-formula-for-total-variation.md)
- [Minkowski's integral inequality](../../../measure-theory/integral/part-01/minkowskis-integral-inequality.md)
- [The Morse--Sard theorem](../analytic-heegaard-floer-homology/the-morse-sard-theorem.md)
- [Rademacher's theorem for locally Lipschitz functions](../../part-02/calculus/part-01/rademachers-theorem-for-locally-lipschitz-functi.md)
- [TauCeti.perimeter](tauceti-perimeter.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.eLpNorm_le_inv_mul_totalVariationOn`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/Sobolev/Sharp.html#TauCeti.eLpNorm_le_inv_mul_totalVariationOn).

## Sources

- [Tau Ceti documentation: `TauCeti.eLpNorm_le_inv_mul_totalVariationOn`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/Sobolev/Sharp.html#TauCeti.eLpNorm_le_inv_mul_totalVariationOn)
- [Source of `TauCeti.eLpNorm_le_inv_mul_totalVariationOn` in TauCeti/Analysis/BoundedVariation/Sobolev/Sharp.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/BoundedVariation/Sobolev/Sharp.lean#L103)
