---
declaration: theorem
origin: cited
lean: ZLattice.prod_successiveMin_mul_measure_le_two_pow_mul_covolume, Convex.prod_mul_volume_real_le_two_pow, ZLattice.prod_mul_measure_le_two_pow_mul_covolume, ZLattice.prod_successiveMin_mul_measureReal_le_two_pow_mul_covolume, ZLattice.two_pow_div_factorial_mul_covolume_le_prod_mul_measure, ZLattice.two_pow_div_factorial_mul_covolume_le_prod_successiveMin_mul_measure, ZLattice.two_pow_div_factorial_mul_covolume_le_prod_successiveMin_mul_measureReal, ZLattice.prod_successiveMin_le_covolume_of_two_pow_finrank_le
statement: formalized
proof: formalized
---

# Minkowski's second theorem, upper bound, in terms of the successive minima

For a full
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

## Other forms

**Minkowski's second theorem.** Formalized in Tau Ceti as [`Convex.prod_mul_volume_real_le_two_pow`](https://taucetiproject.org/docs/TauCeti/NumberTheory/GeometryOfNumbers/MinkowskiSecond.html#Convex.prod_mul_volume_real_le_two_pow).

```lean
Convex.prod_mul_volume_real_le_two_pow {n : ℕ} {K : Set (Fin n → ℝ)} (hK : Convex ℝ K)
  (hKs : ∀ x ∈ K, -x ∈ K) {a : Fin n → ℝ} (ha : ∀ (i : Fin n), 0 ≤ a i)
  (hgap :
    ∀ (i : Fin n) (z : Fin n → ℤ),
      (gauge K fun j => ↑(z j)) < a i → ∀ (j : Fin n), i ≤ j → z j = 0) :
  (∏ i, a i) * MeasureTheory.volume.real K ≤ 2 ^ n
```

**Minkowski's second theorem, upper bound.** Formalized in Tau Ceti as [`ZLattice.prod_mul_measure_le_two_pow_mul_covolume`](https://taucetiproject.org/docs/TauCeti/NumberTheory/GeometryOfNumbers/MinkowskiSecond.html#ZLattice.prod_mul_measure_le_two_pow_mul_covolume).

```lean
ZLattice.prod_mul_measure_le_two_pow_mul_covolume.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] (L : Submodule ℤ E)
  [DiscreteTopology ↥L] (μ : MeasureTheory.Measure E := by volume_tac) [μ.IsAddHaarMeasure]
  {K : Set E} (hK : Convex ℝ K) (hKs : ∀ x ∈ K, -x ∈ K) {n : ℕ} (hn : n = Module.finrank ℝ E)
  {a : Fin n → E} (haL : ∀ (i : Fin n), a i ∈ L) (ha : LinearIndependent ℝ a) {g : Fin n → ℝ}
  (hg0 : ∀ (i : Fin n), 0 ≤ g i)
  (hgap : ∀ (j : Fin n), ∀ v ∈ L, gauge K v < g j → v ∈ Submodule.span ℝ (a '' Set.Iio j)) :
  ENNReal.ofReal (∏ i, g i) * μ K ≤ 2 ^ n * ENNReal.ofReal (ZLattice.covolume L μ)
```

**Minkowski's second theorem.** Formalized in Tau Ceti as [`ZLattice.prod_successiveMin_mul_measureReal_le_two_pow_mul_covolume`](https://taucetiproject.org/docs/TauCeti/NumberTheory/GeometryOfNumbers/MinkowskiSecond.html#ZLattice.prod_successiveMin_mul_measureReal_le_two_pow_mul_covolume).

```lean
ZLattice.prod_successiveMin_mul_measureReal_le_two_pow_mul_covolume.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] (L : Submodule ℤ E) [DiscreteTopology ↥L] [IsZLattice ℝ L]
  (μ : MeasureTheory.Measure E := by volume_tac) [μ.IsAddHaarMeasure] {K : ConvexBody E}
  (hKs : ∀ x ∈ K, -x ∈ K) :
  (∏ i, ZLattice.successiveMin L K i) * μ.real ↑K ≤ 2 ^ Module.finrank ℝ E * ZLattice.covolume L μ
```

**Minkowski's second theorem, lower bound, general form.** Formalized in Tau Ceti as [`ZLattice.two_pow_div_factorial_mul_covolume_le_prod_mul_measure`](https://taucetiproject.org/docs/TauCeti/NumberTheory/GeometryOfNumbers/MinkowskiSecond.html#ZLattice.two_pow_div_factorial_mul_covolume_le_prod_mul_measure).

```lean
ZLattice.two_pow_div_factorial_mul_covolume_le_prod_mul_measure.{u_1, u_2} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [MeasurableSpace E] [BorelSpace E] (L : Submodule ℤ E)
  [DiscreteTopology ↥L] (μ : MeasureTheory.Measure E := by volume_tac) [μ.IsAddHaarMeasure]
  {K : Set E} (hK : Convex ℝ K) (h0 : 0 ∈ K) (hKs : ∀ x ∈ K, -x ∈ K) {ι : Type u_2} [Fintype ι]
  (b : Module.Basis ι ℝ E) (hbL : ∀ (i : ι), b i ∈ L) {a : ι → ℝ} (ha : ∀ (i : ι), 0 ≤ a i)
  (hbK : ∀ (i : ι), b i ∈ a i • K) :
  ENNReal.ofReal
      (2 ^ Module.finrank ℝ E / ↑(Module.finrank ℝ E).factorial * ZLattice.covolume L μ) ≤
    ENNReal.ofReal (∏ i, a i) * μ K
```

**Minkowski's second theorem, lower bound, in terms of the successive minima.** Formalized in Tau Ceti as [`ZLattice.two_pow_div_factorial_mul_covolume_le_prod_successiveMin_mul_measure`](https://taucetiproject.org/docs/TauCeti/NumberTheory/GeometryOfNumbers/MinkowskiSecond.html#ZLattice.two_pow_div_factorial_mul_covolume_le_prod_successiveMin_mul_measure).

```lean
ZLattice.two_pow_div_factorial_mul_covolume_le_prod_successiveMin_mul_measure.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] (L : Submodule ℤ E) [DiscreteTopology ↥L] [IsZLattice ℝ L]
  (μ : MeasureTheory.Measure E := by volume_tac) [μ.IsAddHaarMeasure] {K : ConvexBody E}
  (hK : 0 ∈ interior ↑K) (hKs : ∀ x ∈ K, -x ∈ K) :
  ENNReal.ofReal
      (2 ^ Module.finrank ℝ E / ↑(Module.finrank ℝ E).factorial * ZLattice.covolume L μ) ≤
    ENNReal.ofReal (∏ i, ZLattice.successiveMin L K i) * μ ↑K
```

**Minkowski's second theorem.** Formalized in Tau Ceti as [`ZLattice.two_pow_div_factorial_mul_covolume_le_prod_successiveMin_mul_measureReal`](https://taucetiproject.org/docs/TauCeti/NumberTheory/GeometryOfNumbers/MinkowskiSecond.html#ZLattice.two_pow_div_factorial_mul_covolume_le_prod_successiveMin_mul_measureReal).

```lean
ZLattice.two_pow_div_factorial_mul_covolume_le_prod_successiveMin_mul_measureReal.{u_1}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] (L : Submodule ℤ E) [DiscreteTopology ↥L] [IsZLattice ℝ L]
  (μ : MeasureTheory.Measure E := by volume_tac) [μ.IsAddHaarMeasure] {K : ConvexBody E}
  (hK : 0 ∈ interior ↑K) (hKs : ∀ x ∈ K, -x ∈ K) :
  2 ^ Module.finrank ℝ E / ↑(Module.finrank ℝ E).factorial * ZLattice.covolume L μ ≤
    (∏ i, ZLattice.successiveMin L K i) * μ.real ↑K
```

**Minkowski's second theorem for bodies of measure at least `2ⁿ`.** Formalized in Tau Ceti as [`ZLattice.prod_successiveMin_le_covolume_of_two_pow_finrank_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/GeometryOfNumbers/MinkowskiSecond.html#ZLattice.prod_successiveMin_le_covolume_of_two_pow_finrank_le).

```lean
ZLattice.prod_successiveMin_le_covolume_of_two_pow_finrank_le.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] (L : Submodule ℤ E) [DiscreteTopology ↥L] [IsZLattice ℝ L]
  (μ : MeasureTheory.Measure E := by volume_tac) [μ.IsAddHaarMeasure] {K : ConvexBody E}
  (hKs : ∀ x ∈ K, -x ∈ K) (hμK : 2 ^ Module.finrank ℝ E ≤ μ ↑K) :
  ∏ i, ZLattice.successiveMin L K i ≤ ZLattice.covolume L μ
```

## Sources

- [Tau Ceti documentation: `ZLattice.prod_successiveMin_mul_measure_le_two_pow_mul_covolume`](https://taucetiproject.org/docs/TauCeti/NumberTheory/GeometryOfNumbers/MinkowskiSecond.html#ZLattice.prod_successiveMin_mul_measure_le_two_pow_mul_covolume)
- [Source of `ZLattice.prod_successiveMin_mul_measure_le_two_pow_mul_covolume` in TauCeti/NumberTheory/GeometryOfNumbers/MinkowskiSecond.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/GeometryOfNumbers/MinkowskiSecond.lean#L606)
- [Tau Ceti roadmap status: Heights, units and S-units of number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/HeightsAndUnits/STATUS.md)
