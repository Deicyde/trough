---
declaration: theorem
origin: cited
lean: ZLattice.prod_successiveMin_mul_measure_le_two_pow_mul_covolume
statement: formalized
proof: formalized
---

# ZLattice.prod\_successiveMin\_mul\_measure\_le\_two\_pow\_mul\_covolume

**Minkowski's second theorem**, upper bound, in terms of the successive minima. For a full
lattice `L` in a real normed space `E` of dimension `n`, a Haar measure `μ` on `E`, and a convex
body `K` symmetric about `0`, the successive minima `λ i = successiveMin L K i` satisfy
`λ₀ ⋯ λₙ₋₁ · μ K ≤ 2ⁿ · covolume L μ`. If `K` has empty interior, its measure is zero.

```lean
ZLattice.prod_successiveMin_mul_measure_le_two_pow_mul_covolume.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] (L : Submodule ℤ E) [DiscreteTopology ↥L] [IsZLattice ℝ L]
  (μ : MeasureTheory.Measure E := by volume_tac) [μ.IsAddHaarMeasure] {K : ConvexBody E}
  (hKs : ∀ x ∈ K, -x ∈ K) :
  ENNReal.ofReal (∏ i, ZLattice.successiveMin L K i) * μ ↑K ≤
    2 ^ Module.finrank ℝ E * ENNReal.ofReal (ZLattice.covolume L μ)
```

## Depends on

- [ZLattice.successiveMin](zlattice-successivemin.md)

## Lean

Formalized in Tau Ceti as [`ZLattice.prod_successiveMin_mul_measure_le_two_pow_mul_covolume`](https://taucetiproject.org/docs/TauCeti/NumberTheory/GeometryOfNumbers/MinkowskiSecond.html#ZLattice.prod_successiveMin_mul_measure_le_two_pow_mul_covolume).

## Sources

- [Tau Ceti documentation: `ZLattice.prod_successiveMin_mul_measure_le_two_pow_mul_covolume`](https://taucetiproject.org/docs/TauCeti/NumberTheory/GeometryOfNumbers/MinkowskiSecond.html#ZLattice.prod_successiveMin_mul_measure_le_two_pow_mul_covolume)
- [Source of `ZLattice.prod_successiveMin_mul_measure_le_two_pow_mul_covolume` in TauCeti/NumberTheory/GeometryOfNumbers/MinkowskiSecond.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/GeometryOfNumbers/MinkowskiSecond.lean#L606)
- [Tau Ceti roadmap status: Heights, units and S-units of number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/HeightsAndUnits/STATUS.md)
