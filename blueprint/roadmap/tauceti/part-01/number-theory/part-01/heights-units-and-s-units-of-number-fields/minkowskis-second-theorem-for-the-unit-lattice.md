---
declaration: theorem
origin: cited
lean: TauCeti.NumberField.Units.exists_isMaxRank_prod_sum_abs_logEmbedding_le, Submodule.two_pow_div_factorial_mul_covolume_le_prod_successiveMinimum_pow_mul_measure, Submodule.two_pow_div_factorial_mul_covolume_le_prod_successiveMinimum_pow_mul_measureReal, Submodule.prod_successiveMinimum_pow_mul_measureReal_le_two_pow_mul_covolume, Submodule.prod_successiveMinimum_pow_mul_measure_le_two_pow_mul_covolume
statement: formalized
proof: formalized
---

# Minkowski's second theorem for the unit lattice

There are units `u 0, …, u (r - 1)`, where
`r = rank K`, with linearly independent logarithmic embeddings and
`∏ i, ‖log u i‖₁ ≤ r! * regulator K`, where `‖log x‖₁` is the `ℓ¹` norm of the logarithmic
embedding of `x`. This is Minkowski's second theorem for the unit lattice and the `ℓ¹` unit ball
`logBall K`, whose volume is `2 ^ r / r!`.

```lean
TauCeti.NumberField.Units.exists_isMaxRank_prod_sum_abs_logEmbedding_le.{u_1} {K : Type u_1}
  [Field K] [NumberField K] :
  ∃ u,
    NumberField.Units.IsMaxRank u ∧
      ∏ i, ∑ w, |(NumberField.Units.logEmbedding K) (Additive.ofMul (u i)) w| ≤
        ↑(NumberField.Units.rank K).factorial * NumberField.Units.regulator K
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A basis from the successive minima (Cassels, Chapter V, Lemma 8)](a-basis-from-the-successive-minima-cassels-chapt.md)
- [Minkowski's second theorem, upper bound, in terms of the successive minima](minkowskis-second-theorem-upper-bound-in-terms-o.md)
- [ZLattice.successiveMin](zlattice-successivemin.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.Units.exists_isMaxRank_prod_sum_abs_logEmbedding_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Units/FundamentalSystem.html#TauCeti.NumberField.Units.exists_isMaxRank_prod_sum_abs_logEmbedding_le).

## Other forms

**Minkowski's second theorem over `K`, lower bound.** Formalized in Tau Ceti as [`Submodule.two_pow_div_factorial_mul_covolume_le_prod_successiveMinimum_pow_mul_measure`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/CanonicalEmbedding/SuccessiveMinima.html#Submodule.two_pow_div_factorial_mul_covolume_le_prod_successiveMinimum_pow_mul_measure).

```lean
Submodule.two_pow_div_factorial_mul_covolume_le_prod_successiveMinimum_pow_mul_measure.{u_3, u_4}
  {K : Type u_3} [Field K] [NumberField K] {ι : Type u_4} [Fintype ι]
  (Λ : Submodule (NumberField.RingOfIntegers K) (ι → K)) [DiscreteTopology ↥Λ.mixedImage]
  [IsZLattice ℝ Λ.mixedImage]
  (μ : MeasureTheory.Measure (ι → NumberField.mixedEmbedding.mixedSpace K) := by volume_tac)
  [μ.IsAddHaarMeasure] {B : Set (ι → NumberField.mixedEmbedding.mixedSpace K)} (hBc : Convex ℝ B)
  (hBk : IsCompact B) (hB0 : B ∈ nhds 0)
  (hBbal :
    ∀ z ∈ B,
      ∀ (a : NumberField.mixedEmbedding.mixedSpace K),
        (∀ (w : NumberField.InfinitePlace K), (NumberField.mixedEmbedding.normAtPlace w) a ≤ 1) →
          (fun i => a * z i) ∈ B) :
  ENNReal.ofReal
      (2 ^ (Module.finrank ℚ K * Fintype.card ι) /
          (↑(Module.finrank ℚ K * Fintype.card ι).factorial *
            TauCeti.NumberField.integralBasisHouse K ^ (Module.finrank ℚ K * Fintype.card ι)) *
        ZLattice.covolume Λ.mixedImage μ) ≤
    ENNReal.ofReal (∏ l, Λ.successiveMinimum B ↑l ^ Module.finrank ℚ K) * μ B
```

**Minkowski's second theorem over `K`, lower bound (`ℝ`-valued measure form).** Formalized in Tau Ceti as [`Submodule.two_pow_div_factorial_mul_covolume_le_prod_successiveMinimum_pow_mul_measureReal`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/CanonicalEmbedding/SuccessiveMinima.html#Submodule.two_pow_div_factorial_mul_covolume_le_prod_successiveMinimum_pow_mul_measureReal).

```lean
Submodule.two_pow_div_factorial_mul_covolume_le_prod_successiveMinimum_pow_mul_measureReal.{u_3,
    u_4}
  {K : Type u_3} [Field K] [NumberField K] {ι : Type u_4} [Fintype ι]
  (Λ : Submodule (NumberField.RingOfIntegers K) (ι → K)) [DiscreteTopology ↥Λ.mixedImage]
  [IsZLattice ℝ Λ.mixedImage]
  (μ : MeasureTheory.Measure (ι → NumberField.mixedEmbedding.mixedSpace K) := by volume_tac)
  [μ.IsAddHaarMeasure] {B : Set (ι → NumberField.mixedEmbedding.mixedSpace K)} (hBc : Convex ℝ B)
  (hBk : IsCompact B) (hB0 : B ∈ nhds 0)
  (hBbal :
    ∀ z ∈ B,
      ∀ (a : NumberField.mixedEmbedding.mixedSpace K),
        (∀ (w : NumberField.InfinitePlace K), (NumberField.mixedEmbedding.normAtPlace w) a ≤ 1) →
          (fun i => a * z i) ∈ B) :
  2 ^ (Module.finrank ℚ K * Fintype.card ι) /
        (↑(Module.finrank ℚ K * Fintype.card ι).factorial *
          TauCeti.NumberField.integralBasisHouse K ^ (Module.finrank ℚ K * Fintype.card ι)) *
      ZLattice.covolume Λ.mixedImage μ ≤
    (∏ l, Λ.successiveMinimum B ↑l ^ Module.finrank ℚ K) * μ.real B
```

**Minkowski's second theorem over `K`, upper bound (`ℝ`-valued measure form).** Formalized in Tau Ceti as [`Submodule.prod_successiveMinimum_pow_mul_measureReal_le_two_pow_mul_covolume`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/CanonicalEmbedding/SuccessiveMinima.html#Submodule.prod_successiveMinimum_pow_mul_measureReal_le_two_pow_mul_covolume).

```lean
Submodule.prod_successiveMinimum_pow_mul_measureReal_le_two_pow_mul_covolume.{u_3, u_4}
  {K : Type u_3} [Field K] [NumberField K] {ι : Type u_4} [Fintype ι]
  (Λ : Submodule (NumberField.RingOfIntegers K) (ι → K)) [DiscreteTopology ↥Λ.mixedImage]
  [IsZLattice ℝ Λ.mixedImage]
  (μ : MeasureTheory.Measure (ι → NumberField.mixedEmbedding.mixedSpace K) := by volume_tac)
  [μ.IsAddHaarMeasure] {B : Set (ι → NumberField.mixedEmbedding.mixedSpace K)} (hBc : Convex ℝ B)
  (hBk : IsCompact B) (hBs : ∀ z ∈ B, -z ∈ B) :
  (∏ l, Λ.successiveMinimum B ↑l ^ Module.finrank ℚ K) * μ.real B ≤
    2 ^ (Module.finrank ℚ K * Fintype.card ι) * ZLattice.covolume Λ.mixedImage μ
```

**Minkowski's second theorem over `K`, upper bound.** Formalized in Tau Ceti as [`Submodule.prod_successiveMinimum_pow_mul_measure_le_two_pow_mul_covolume`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/CanonicalEmbedding/SuccessiveMinima.html#Submodule.prod_successiveMinimum_pow_mul_measure_le_two_pow_mul_covolume).

```lean
Submodule.prod_successiveMinimum_pow_mul_measure_le_two_pow_mul_covolume.{u_3, u_4} {K : Type u_3}
  [Field K] [NumberField K] {ι : Type u_4} [Fintype ι]
  (Λ : Submodule (NumberField.RingOfIntegers K) (ι → K)) [DiscreteTopology ↥Λ.mixedImage]
  [IsZLattice ℝ Λ.mixedImage]
  (μ : MeasureTheory.Measure (ι → NumberField.mixedEmbedding.mixedSpace K) := by volume_tac)
  [μ.IsAddHaarMeasure] {B : Set (ι → NumberField.mixedEmbedding.mixedSpace K)} (hBc : Convex ℝ B)
  (hBk : IsCompact B) (hBs : ∀ z ∈ B, -z ∈ B) :
  ENNReal.ofReal (∏ l, Λ.successiveMinimum B ↑l ^ Module.finrank ℚ K) * μ B ≤
    2 ^ (Module.finrank ℚ K * Fintype.card ι) * ENNReal.ofReal (ZLattice.covolume Λ.mixedImage μ)
```

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.Units.exists_isMaxRank_prod_sum_abs_logEmbedding_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Units/FundamentalSystem.html#TauCeti.NumberField.Units.exists_isMaxRank_prod_sum_abs_logEmbedding_le)
- [Source of `TauCeti.NumberField.Units.exists_isMaxRank_prod_sum_abs_logEmbedding_le` in TauCeti/NumberTheory/NumberField/Units/FundamentalSystem.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/NumberField/Units/FundamentalSystem.lean#L185)
