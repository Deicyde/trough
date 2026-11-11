---
declaration: theorem
origin: cited
lean: ZLattice.two_pow_div_factorial_mul_covolume_le_prod_successiveMin_mul_measureReal
statement: formalized
proof: formalized
---

# Minkowski's second theorem (`ZLattice.two_pow_div_factorial_mul_covolume_le_prod_successiveMin_mul_measureReal`)

**Minkowski's second theorem**, lower bound, in terms of the successive minima and with real
measures: `2ⁿ / n! · covolume L μ ≤ λ₀ ⋯ λₙ₋₁ · μ.real K`.

```lean
ZLattice.two_pow_div_factorial_mul_covolume_le_prod_successiveMin_mul_measureReal.{u_1}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [MeasurableSpace E] [BorelSpace E]
  (L : Submodule ℤ E) [DiscreteTopology ↥L] [IsZLattice ℝ L]
  (μ : MeasureTheory.Measure E := by volume_tac) [μ.IsAddHaarMeasure] {K : ConvexBody E}
  (hK : 0 ∈ interior ↑K) (hKs : ∀ x ∈ K, -x ∈ K) :
  2 ^ Module.finrank ℝ E / ↑(Module.finrank ℝ E).factorial * ZLattice.covolume L μ ≤
    (∏ i, ZLattice.successiveMin L K i) * μ.real ↑K
```

## Depends on

- [ZLattice.successiveMin](../../part-01/heights-units-and-s-units-of-number-fields/zlattice-successivemin.md)

## Proof depends on

- [Minkowski's second theorem, upper bound, in terms of the successive minima](../../part-01/heights-units-and-s-units-of-number-fields/minkowskis-second-theorem-upper-bound-in-terms-o.md)

## Lean

Formalized in Tau Ceti as [`ZLattice.two_pow_div_factorial_mul_covolume_le_prod_successiveMin_mul_measureReal`](https://taucetiproject.org/docs/TauCeti/NumberTheory/GeometryOfNumbers/MinkowskiSecond.html#ZLattice.two_pow_div_factorial_mul_covolume_le_prod_successiveMin_mul_measureReal).

## Sources

- [Tau Ceti documentation: `ZLattice.two_pow_div_factorial_mul_covolume_le_prod_successiveMin_mul_measureReal`](https://taucetiproject.org/docs/TauCeti/NumberTheory/GeometryOfNumbers/MinkowskiSecond.html#ZLattice.two_pow_div_factorial_mul_covolume_le_prod_successiveMin_mul_measureReal)
- [Source of `ZLattice.two_pow_div_factorial_mul_covolume_le_prod_successiveMin_mul_measureReal` in TauCeti/NumberTheory/GeometryOfNumbers/MinkowskiSecond.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/GeometryOfNumbers/MinkowskiSecond.lean#L755)
- [Tau Ceti roadmap status: Successive minima and Minkowski's theorems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SuccessiveMinima/STATUS.md)
