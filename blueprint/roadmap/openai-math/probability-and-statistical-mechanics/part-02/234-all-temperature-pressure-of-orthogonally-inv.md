---
declaration: section
origin: cited
lean: OAI.InvariantIsing.limiting_pressure_of_extreme_limits_unconditional, OAI.InvariantIsing.limiting_wasserstein_field_pressure_of_extreme_limits_unconditional, OAI.InvariantIsing.positive_temperature_pressure_unconditional, OAI.InvariantIsing.ground_state_limit_unconditional, OAI.InvariantIsing.random_pressure_tendsto_in_measure_unconditional, OAI.InvariantIsing.random_pressure_limit_unconditional, OAI.InvariantIsing.random_pressure_tendsto_ae_unconditional, OAI.InvariantIsing.random_field_pressure_tendsto_ae_unconditional
statement: formalized
proof: formalized
---

# 234. All-temperature pressure of orthogonally invariant Ising spin glasses

1 manuscript and 11 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Gives an exact variational formula for the limiting pressure of orthogonally invariant Ising spin glasses at every fixed temperature, both almost surely and in expectation. The coupling matrix is a Haar-random rotation of a deterministic spectrum converging to a compactly supported law, with extreme eigenvalues converging to its support edges. The zero-field ground-state energy follows as temperature tends to zero.

## All-temperature pressure for orthogonally invariant Ising spin glasses

We determine the limiting pressure of an Ising spin glass with Haar orthogonal eigenvectors, a compact limiting spectral law, and no asymptotic outliers, at every fixed temperature. The pressure converges in expectation and almost surely to a variational formula. We also give the limiting pressure with deterministic external fields whose empirical laws converge in first-moment transport distance, and derive a formula for the zero-field ground-state energy by taking temperature to zero.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/All-temperature-pressure-for-orthogonally-invariant-Ising-spin-glasses-September-25-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization gives variational limits for orthogonally invariant Ising spin glasses whose eigenvectors have Haar law and whose empirical eigenvalue distributions converge to a compactly supported law with the stated control of extreme eigenvalues. The pressure converges both in expectation and almost surely to an explicit functional of the limiting spectral law. A version with external fields assumes convergence of their empirical laws in Wasserstein distance and gives the corresponding magnetic-field functional.

The formalization also covers every positive temperature, a ground-state limit, random spectral data with the stated conditional Haar law, and Gaussian-pattern specializations. These hypotheses identify the invariant models to which the limits apply.

## Lean: Pressure and ground-state limits for invariant Ising models

```lean
theorem limiting_pressure_of_extreme_limits_unconditional :
  ∀ {Ω : Type*} [MeasurableSpace Ω] (P : Measure Ω) [IsProbabilityMeasure P]
    (U : (N : ℕ) → Ω → Orthogonal N) (_hU : ∀ N, Measurable (U N))
    (_hHaar : ∀ N, (P.map (U N)).IsMulRightInvariant)
    (eig : (N : ℕ) → Fin N → ℝ) (ν : ProbabilityMeasure ℝ) (a b : ℝ)
    (_hcompact : IsCompact (ν : Measure ℝ).support)
    (_hbound : (ν : Measure ℝ).support ⊆ Icc a b)
    (_ha : a∈(ν : Measure ℝ).support) (_hb : b∈(ν : Measure ℝ).support)
    (_hmin : Tendsto (fun k => spectralMinimum (eig (k+1))) atTop (𝓝 a))
    (_hmax : Tendsto (fun k => spectralMaximum (eig (k+1))) atTop (𝓝 b))
    (_hweak : Tendsto (fun k => empiricalSpectralLaw (Nat.succ_pos k) (eig (k+1)))
      atTop (𝓝 ν)),
    Tendsto (fun N => ∫ ω, rotatedPressure (eig N) (matrixRotation (U N ω)⁻¹) (fun _ => 0) ∂P)
      atTop (𝓝 (variationalFunctional (measureR (ν : Measure ℝ) b)).toReal) ∧
    ∀ᵐ ω ∂P, Tendsto (fun N => rotatedPressure (eig N) (matrixRotation (U N ω)⁻¹) (fun _ => 0))
      atTop (𝓝 (variationalFunctional (measureR (ν : Measure ℝ) b)).toReal)
```

Stated in [InvariantIsing.lean, line 282](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/InvariantIsing.lean#L282). Proved in [lean/OAI/Probability/InvariantIsing/Unconditional.lean, line 27](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/InvariantIsing/Unconditional.lean#L27).

```lean
theorem limiting_wasserstein_field_pressure_of_extreme_limits_unconditional :
  ∀ {Ω : Type*} [MeasurableSpace Ω] (P : Measure Ω) [IsProbabilityMeasure P]
    (U : (N : ℕ) → Ω → Orthogonal N) (_hU : ∀ N, Measurable (U N))
    (_hHaar : ∀ N, (P.map (U N)).IsMulRightInvariant)
    (eig : (N : ℕ) → Fin N → ℝ) (ν : ProbabilityMeasure ℝ) (a b : ℝ)
    (_hcompact : IsCompact (ν : Measure ℝ).support)
    (_hbound : (ν : Measure ℝ).support ⊆ Icc a b)
    (_ha : a∈(ν : Measure ℝ).support) (_hb : b∈(ν : Measure ℝ).support)
    (_hmin : Tendsto (fun k => spectralMinimum (eig (k+1))) atTop (𝓝 a))
    (_hmax : Tendsto (fun k => spectralMaximum (eig (k+1))) atTop (𝓝 b))
    (_hweak : Tendsto (fun k => empiricalSpectralLaw (Nat.succ_pos k) (eig (k+1)))
      atTop (𝓝 ν))
    (field : (N : ℕ) → Fin N → ℝ) (ξ : ProbabilityMeasure ℝ)
    (_hξ : Integrable (fun x : ℝ => x) (ξ : Measure ℝ))
    (_hw : Tendsto (fun k => fieldWassersteinOne (empiricalSpectralLaw (Nat.succ_pos k) (field (k+1))) ξ)
      atTop (𝓝 0)),
    Tendsto (fun N => ∫ ω, rotatedPressure (eig N) (matrixRotation (U N ω)⁻¹) (field N) ∂P)
      atTop (𝓝 (magneticFieldFunctional (ν : Measure ℝ) b ξ)) ∧
    ∀ᵐ ω ∂P, Tendsto (fun N => rotatedPressure (eig N) (matrixRotation (U N ω)⁻¹) (field N))
      atTop (𝓝 (magneticFieldFunctional (ν : Measure ℝ) b ξ))
```

Stated in [InvariantIsing.lean, line 300](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/InvariantIsing.lean#L300). Proved in [lean/OAI/Probability/InvariantIsing/Unconditional.lean, line 45](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/InvariantIsing/Unconditional.lean#L45).

```lean
theorem positive_temperature_pressure_unconditional :
  ∀ {Ω : Type*} [MeasurableSpace Ω] (P : Measure Ω) [IsProbabilityMeasure P]
    (U : (N : ℕ) → Ω → Orthogonal N) (_hU : ∀ N, Measurable (U N))
    (_hHaar : ∀ N, (P.map (U N)).IsMulRightInvariant)
    (eig : (N : ℕ) → Fin N → ℝ) (ν : ProbabilityMeasure ℝ) (a b : ℝ)
    (_hbound : (ν : Measure ℝ).support ⊆ Icc a b)
    (_ha : a∈(ν : Measure ℝ).support) (_hb : b∈(ν : Measure ℝ).support)
    (_hno : ∀ ε : ℝ, 0 < ε → ∀ᶠ N in atTop, ∀ i, a-ε ≤ eig N i ∧ eig N i ≤ b+ε)
    (β : ℝ) (_hβ : 0 < β)
    (_hweak : Tendsto (fun k => empiricalSpectralLaw (Nat.succ_pos k) (eig (k+1)))
      atTop (𝓝 ν)),
    Tendsto (fun N => ∫ ω, rotatedPressure (fun i => β*eig N i) (matrixRotation (U N ω)⁻¹) (fun _ => 0) ∂P)
      atTop (𝓝 (variationalFunctional (measureR (scaledSpectralLaw ν β : Measure ℝ) (β*b))).toReal) ∧
    ∀ᵐ ω ∂P, Tendsto (fun N => rotatedPressure (fun i => β*eig N i) (matrixRotation (U N ω)⁻¹) (fun _ => 0))
      atTop (𝓝 (variationalFunctional (measureR (scaledSpectralLaw ν β : Measure ℝ) (β*b))).toReal)
```

Stated in [InvariantIsing.lean, line 322](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/InvariantIsing.lean#L322). Proved in [lean/OAI/Probability/InvariantIsing/Unconditional.lean, line 67](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/InvariantIsing/Unconditional.lean#L67).

```lean
theorem ground_state_limit_unconditional :
  ∀ {Ω : Type*} [MeasurableSpace Ω] (P : Measure Ω) [IsProbabilityMeasure P]
    (U : (N : ℕ) → Ω → Orthogonal N) (_hU : ∀ N, Measurable (U N))
    (_hHaar : ∀ N, (P.map (U N)).IsMulRightInvariant)
    (eig : (N : ℕ) → Fin N → ℝ) (ν : ProbabilityMeasure ℝ) (a b : ℝ)
    (_hbound : (ν : Measure ℝ).support ⊆ Icc a b)
    (_ha : a∈(ν : Measure ℝ).support) (_hb : b∈(ν : Measure ℝ).support)
    (_hno : ∀ ε : ℝ, 0 < ε → ∀ᶠ N in atTop, ∀ i, a-ε ≤ eig N i ∧ eig N i ≤ b+ε)
    (_hweak : Tendsto (fun k => empiricalSpectralLaw (Nat.succ_pos k) (eig (k+1)))
      atTop (𝓝 ν)),
    ∃ M : ℝ,
      Tendsto (fun N => ∫ ω, groundStateEnergy (eig N) (matrixRotation (U N ω)⁻¹) ∂P)
        atTop (𝓝 M) ∧
      (∀ᵐ ω ∂P, Tendsto (fun N => groundStateEnergy (eig N) (matrixRotation (U N ω)⁻¹))
        atTop (𝓝 M)) ∧
      Tendsto (thermalVariationalValue ν b) atTop (𝓝 M)
```

Stated in [InvariantIsing.lean, line 339](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/InvariantIsing.lean#L339). Proved in [lean/OAI/Probability/InvariantIsing/Unconditional.lean, line 84](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/InvariantIsing/Unconditional.lean#L84).

```lean
theorem random_pressure_tendsto_in_measure_unconditional
    {Ω : Type*} [MeasurableSpace Ω] (P : Measure Ω) [IsProbabilityMeasure P]
    (eig : (N : ℕ) → Ω → Fin N → ℝ) (Y : ℕ → Ω → ℝ)
    (heig : ∀ N, Measurable (eig N)) (hY : ∀ N, Measurable (Y N))
    (H : (N : ℕ) → Measure (Orthogonal N)) [∀ N, IsProbabilityMeasure (H N)]
    [∀ N, (H N).IsMulRightInvariant]
    (hlaw : ∀ N, ConditionalFieldOrbitLaw P (fun ω => (eig N ω,fun _ => 0)) (Y N) (H N))
    (ν : ProbabilityMeasure ℝ) (a b : ℝ)
    (hcompact : IsCompact (ν : Measure ℝ).support)
    (hbound : (ν : Measure ℝ).support ⊆ Icc a b)
    (ha : a∈(ν : Measure ℝ).support) (hb : b∈(ν : Measure ℝ).support)
    (hweak : TendstoInMeasure P (fun k ω => LevyProkhorov.ofMeasure
      (empiricalSpectralLaw (Nat.succ_pos k) (eig (k+1) ω))) atTop
      (fun _ => LevyProkhorov.ofMeasure ν))
    (hexcess : TendstoInMeasure P (fun k ω => spectralExcess (eig (k+1) ω) a b)
      atTop (fun _ => 0)) :
    TendstoInMeasure P (fun k => Y (k+1)) atTop
      (fun _ => (variationalFunctional (measureR (ν : Measure ℝ) b)).toReal)
```

Stated in [InvariantIsing.lean, line 357](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/InvariantIsing.lean#L357). Proved in [lean/OAI/Probability/InvariantIsing/Unconditional.lean, line 102](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/InvariantIsing/Unconditional.lean#L102).

```lean
theorem random_pressure_limit_unconditional :
  ∀ {Ω : Type*} [MeasurableSpace Ω] (P : Measure Ω) [IsProbabilityMeasure P]
    (eig : (N : ℕ) → Ω → Fin N → ℝ) (Y : ℕ → Ω → ℝ)
    (_heig : ∀ N, Measurable (eig N)) (_hY : ∀ N, Measurable (Y N))
    (H : (N : ℕ) → Measure (Orthogonal N)) [∀ N, IsProbabilityMeasure (H N)]
    [∀ N, (H N).IsMulRightInvariant]
    (_hlaw : ∀ N, ConditionalFieldOrbitLaw P (fun ω => (eig N ω,fun _ => 0)) (Y N) (H N))
    (ν : ProbabilityMeasure ℝ) (a b : ℝ)
    (_hcompact : IsCompact (ν : Measure ℝ).support)
    (_hbound : (ν : Measure ℝ).support ⊆ Icc a b)
    (_ha : a∈(ν : Measure ℝ).support) (_hb : b∈(ν : Measure ℝ).support)
    (_hweak : TendstoInMeasure P (fun k ω => LevyProkhorov.ofMeasure
      (empiricalSpectralLaw (Nat.succ_pos k) (eig (k+1) ω))) atTop
      (fun _ => LevyProkhorov.ofMeasure ν))
    (_hexcess : TendstoInMeasure P (fun k ω => spectralExcess (eig (k+1) ω) a b)
      atTop (fun _ => 0))
    (_hUI : UniformIntegrable (fun k => Y (k+1)) 1 P),
    TendstoInMeasure P (fun k => Y (k+1)) atTop
      (fun _ => (variationalFunctional (measureR (ν : Measure ℝ) b)).toReal) ∧
    Tendsto (fun k => eLpNorm (fun ω => Y (k+1) ω-
      (variationalFunctional (measureR (ν : Measure ℝ) b)).toReal) 1 P) atTop (𝓝 0) ∧
    Tendsto (fun k => ∫ ω, Y (k+1) ω ∂P) atTop
      (𝓝 (variationalFunctional (measureR (ν : Measure ℝ) b)).toReal)
```

Stated in [InvariantIsing.lean, line 377](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/InvariantIsing.lean#L377). Proved in [lean/OAI/Probability/InvariantIsing/Unconditional.lean, line 124](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/InvariantIsing/Unconditional.lean#L124).

```lean
theorem random_pressure_tendsto_ae_unconditional :
  ∀ {Ω : Type*} [MeasurableSpace Ω] (P : Measure Ω) [IsProbabilityMeasure P]
    (eig : (N : ℕ) → Ω → Fin N → ℝ) (Y : ℕ → Ω → ℝ)
    (_heig : ∀ N, Measurable (eig N)) (_hY : ∀ N, Measurable (Y N))
    (H : (N : ℕ) → Measure (Orthogonal N)) [∀ N, IsProbabilityMeasure (H N)]
    [∀ N, (H N).IsMulRightInvariant]
    (_hlaw : ∀ N, ConditionalFieldOrbitLaw P (fun ω => (eig N ω,fun _ => 0)) (Y N) (H N))
    (ν : ProbabilityMeasure ℝ) (a b : ℝ)
    (_hcompact : IsCompact (ν : Measure ℝ).support)
    (_hbound : (ν : Measure ℝ).support ⊆ Icc a b)
    (_ha : a∈(ν : Measure ℝ).support) (_hb : b∈(ν : Measure ℝ).support)
    (_hno : ∀ᵐ ω ∂P, ∀ ε : ℝ, 0 < ε → ∀ᶠ N in atTop,
      ∀ i, a-ε ≤ eig N ω i ∧ eig N ω i ≤ b+ε)
    (_hweak : ∀ᵐ ω ∂P, Tendsto (fun k =>
      empiricalSpectralLaw (Nat.succ_pos k) (eig (k+1) ω)) atTop (𝓝 ν)),
    ∀ᵐ ω ∂P, Tendsto (fun N => Y N ω) atTop
      (𝓝 (variationalFunctional (measureR (ν : Measure ℝ) b)).toReal)
```

Stated in [InvariantIsing.lean, line 402](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/InvariantIsing.lean#L402). Proved in [lean/OAI/Probability/InvariantIsing/Unconditional.lean, line 149](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/InvariantIsing/Unconditional.lean#L149).

```lean
theorem random_field_pressure_tendsto_ae_unconditional :
  ∀ {Ω : Type*} [MeasurableSpace Ω] (P : Measure Ω) [IsProbabilityMeasure P]
    (d : (N : ℕ) → Ω → FieldSpectralData N) (Y : ℕ → Ω → ℝ)
    (_hd : ∀ N, Measurable (d N)) (_hY : ∀ N, Measurable (Y N))
    (H : (N : ℕ) → Measure (Orthogonal N)) [∀ N, IsProbabilityMeasure (H N)]
    [∀ N, (H N).IsMulRightInvariant]
    (_hlaw : ∀ N, ConditionalFieldOrbitLaw P (d N) (Y N) (H N))
    (ν : ProbabilityMeasure ℝ) (a b : ℝ)
    (_hcompact : IsCompact (ν : Measure ℝ).support)
    (_hbound : (ν : Measure ℝ).support ⊆ Icc a b)
    (_ha : a∈(ν : Measure ℝ).support) (_hb : b∈(ν : Measure ℝ).support)
    (_hno : ∀ᵐ ω ∂P, ∀ ε : ℝ, 0 < ε → ∀ᶠ N in atTop,
      ∀ i, a-ε ≤ (d N ω).1 i ∧ (d N ω).1 i ≤ b+ε)
    (_hweak : ∀ᵐ ω ∂P, Tendsto (fun k =>
      empiricalSpectralLaw (Nat.succ_pos k) (d (k+1) ω).1) atTop (𝓝 ν))
    (ξ : ProbabilityMeasure ℝ) (_hξ : Integrable (fun x : ℝ => x) (ξ : Measure ℝ))
    (_hw : ∀ᵐ ω ∂P, Tendsto (fun k => fieldWassersteinOne
      (empiricalSpectralLaw (Nat.succ_pos k) (d (k+1) ω).2) ξ) atTop (𝓝 0)),
    ∀ᵐ ω ∂P, Tendsto (fun N => Y N ω) atTop
      (𝓝 (magneticFieldFunctional (ν : Measure ℝ) b ξ))
```

Stated in [InvariantIsing.lean, line 421](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/InvariantIsing.lean#L421). Proved in [lean/OAI/Probability/InvariantIsing/Unconditional.lean, line 168](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/InvariantIsing/Unconditional.lean#L168).

```lean
theorem gaussianPattern_pressure_limit_unconditional :
  ∀ (α : ℝ) (_hα : 0 < α)
    {Ω : Type u} [MeasurableSpace Ω] (P : Measure Ω) [IsProbabilityMeasure P]
    (Z : (N : ℕ) → Ω → EuclideanSpace ℝ (Fin N × Fin (gaussianPatternCount α N)))
    (_hZ : ∀ N, Measurable (Z N)) (_hlaw : ∀ N, HasLaw (Z N) (stdGaussian _) P)
    (c : ℝ),
    TendstoInMeasure P (fun k ω => gaussianPatternPressure (N := k+1) (m := gaussianPatternCount α (k+1)) c (Z (k+1) ω)) atTop
      (fun _ => gaussianPatternLimit α c) ∧
    Tendsto (fun k => eLpNorm (fun ω => gaussianPatternPressure (N := k+1) (m := gaussianPatternCount α (k+1)) c (Z (k+1) ω)-
      gaussianPatternLimit α c) 1 P) atTop (𝓝 0) ∧
    Tendsto (fun k => ∫ ω, gaussianPatternPressure (N := k+1) (m := gaussianPatternCount α (k+1)) c (Z (k+1) ω) ∂P) atTop
      (𝓝 (gaussianPatternLimit α c))
```

Stated in [InvariantIsing.lean, line 443](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/InvariantIsing.lean#L443). Proved in [lean/OAI/Probability/InvariantIsing/Unconditional.lean, line 190](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/InvariantIsing/Unconditional.lean#L190).

```lean
theorem gaussianPattern_ground_limit_unconditional :
  ∀ (α : ℝ) (_hα : 0 < α)
    {Ω : Type u} [MeasurableSpace Ω] (P : Measure Ω) [IsProbabilityMeasure P]
    (Z : (N : ℕ) → Ω → EuclideanSpace ℝ (Fin N × Fin (gaussianPatternCount α N)))
    (_hZ : ∀ N, Measurable (Z N)) (_hlaw : ∀ N, HasLaw (Z N) (stdGaussian _) P)
    (ε : ℝ),
    ∃ e : ℝ,
      TendstoInMeasure P (fun k ω => gaussianPatternGroundEnergy ε (Z (k+1) ω)) atTop (fun _ => e) ∧
      Tendsto (fun k => eLpNorm (fun ω => gaussianPatternGroundEnergy ε (Z (k+1) ω)-e) 1 P)
        atTop (𝓝 0) ∧
      Tendsto (fun k => ∫ ω, gaussianPatternGroundEnergy ε (Z (k+1) ω) ∂P) atTop (𝓝 e) ∧
      Tendsto (fun β => gaussianPatternLimit α (ε*β)/β) atTop (𝓝 e)
```

Stated in [InvariantIsing.lean, line 457](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/InvariantIsing.lean#L457). Proved in [lean/OAI/Probability/InvariantIsing/Unconditional.lean, line 204](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/InvariantIsing/Unconditional.lean#L204).

```lean
theorem gaussianPattern_norm_limits_unconditional :
  ∀ (α : ℝ) (_hα : 0 < α)
    {Ω : Type u} [MeasurableSpace Ω] (P : Measure Ω) [IsProbabilityMeasure P]
    (Z : (N : ℕ) → Ω → EuclideanSpace ℝ (Fin N × Fin (gaussianPatternCount α N)))
    (_hZ : ∀ N, Measurable (Z N)) (_hlaw : ∀ N, HasLaw (Z N) (stdGaussian _) P),
    ∃ eplus eminus : ℝ, 0 ≤ eplus ∧ eminus ≤ 0 ∧
      Tendsto (fun β => gaussianPatternLimit α β/β) atTop (𝓝 eplus) ∧
      Tendsto (fun β => gaussianPatternLimit α (-β)/β) atTop (𝓝 eminus) ∧
      (TendstoInMeasure P (fun k ω => ‖gaussianPatternOperator (Z (k+1) ω)‖/(k+1)) atTop
        (fun _ => Real.sqrt (2*eplus)) ∧
       Tendsto (fun k => eLpNorm (fun ω => ‖gaussianPatternOperator (Z (k+1) ω)‖/(k+1)-
        Real.sqrt (2*eplus)) 1 P) atTop (𝓝 0)) ∧
      (TendstoInMeasure P (fun k ω =>
        (Finset.univ.inf' Finset.univ_nonempty (fun σ : Spin (k+1) => ‖gaussianPatternSum (Z (k+1) ω) σ‖))/(k+1))
        atTop (fun _ => Real.sqrt (-2*eminus)) ∧
       Tendsto (fun k => eLpNorm (fun ω =>
        (Finset.univ.inf' Finset.univ_nonempty (fun σ : Spin (k+1) => ‖gaussianPatternSum (Z (k+1) ω) σ‖))/(k+1)-
          Real.sqrt (-2*eminus)) 1 P) atTop (𝓝 0))
```

Stated in [InvariantIsing.lean, line 471](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/InvariantIsing.lean#L471). Proved in [lean/OAI/Probability/InvariantIsing/Unconditional.lean, line 218](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/InvariantIsing/Unconditional.lean#L218).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/234.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/234.md)
