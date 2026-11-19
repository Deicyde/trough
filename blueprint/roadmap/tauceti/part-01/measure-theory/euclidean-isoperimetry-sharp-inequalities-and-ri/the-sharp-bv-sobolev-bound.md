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

Its statement uses no other declaration mapped here.

## Proof depends on

- [Brunn–Minkowski for a shell](brunn-minkowski-for-a-shell.md)
- [Minkowski's integral inequality](../integral/part-02/minkowskis-integral-inequality.md)
- [The Morse--Sard theorem](../../analysis/part-01/analytic-heegaard-floer-homology/the-morse-sard-theorem.md)
- [Rademacher's theorem for locally Lipschitz functions](../../analysis/part-03/calculus/part-02/rademachers-theorem-for-locally-lipschitz-functi.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.eLpNorm_le_inv_mul_totalVariationOn`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/Sobolev/Sharp.html#TauCeti.eLpNorm_le_inv_mul_totalVariationOn).

## Sources

- [Tau Ceti documentation: `TauCeti.eLpNorm_le_inv_mul_totalVariationOn`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/Sobolev/Sharp.html#TauCeti.eLpNorm_le_inv_mul_totalVariationOn)
- [Source of `TauCeti.eLpNorm_le_inv_mul_totalVariationOn` in TauCeti/Analysis/BoundedVariation/Sobolev/Sharp.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/BoundedVariation/Sobolev/Sharp.lean#L102)
- [Tau Ceti roadmap status: Euclidean isoperimetry, sharp inequalities, and rigidity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Isoperimetry/STATUS.md)
