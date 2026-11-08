---
declaration: theorem
origin: cited
lean: TauCeti.Semigroups.hilleYosida_generation_iff, TauCeti.Semigroups.StronglyContinuousSemigroup.norm_resolvent_complexGenerator_le, TauCeti.Semigroups.exists_generator_eq_and_hasGrowthBound_one_iff_forall_norm_resolvent_le, TauCeti.Semigroups.hilleYosida_generation, TauCeti.Semigroups.StronglyContinuousSemigroup.norm_resolvent_complexGenerator_pow_le, TauCeti.Semigroups.StronglyContinuousSemigroup.norm_generator_resolvent_le, TauCeti.Semigroups.StronglyContinuousSemigroup.resolvent_norm_le
statement: formalized
proof: formalized
---

# Hille--Yosida characterization

An unbounded operator is the generator of a strongly
continuous semigroup with growth bound `(omega, M)` if and only if `1 ≤ M`, its domain is dense,
the half-line `(omega, ∞)` lies in its resolvent set, and its resolvent powers satisfy the sharp
Hille--Yosida estimates.

```lean
TauCeti.Semigroups.hilleYosida_generation_iff.{u_1} {X : Type u_1} [NormedAddCommGroup X]
  [NormedSpace ℝ X] [CompleteSpace X] (A : X →ₗ.[ℝ] X) (M omega : ℝ) :
  (∃ S, S.generator = A ∧ S.HasGrowthBound omega M) ↔
    1 ≤ M ∧
      Dense ↑A.domain ∧
        (∀ (lambda : ℝ), omega < lambda → lambda ∈ A.resolventSet) ∧
          ∀ (n : ℕ),
            1 ≤ n →
              ∀ (lambda : ℝ), omega < lambda → ‖A.resolvent lambda ^ n‖ ≤ M / (lambda - omega) ^ n
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Duhamel identity for the exponential of a bounded operator](../../part-02/normed/part-01/the-duhamel-identity-for-the-exponential-of-a-bo.md)
- [Sharp Hille--Yosida power bound for the generator resolvent](../../part-02/semigroups/sharp-hille-yosida-power-bound-for-the-generator.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Semigroups.hilleYosida_generation_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Generation/HilleYosida/Generation.html#TauCeti.Semigroups.hilleYosida_generation_iff).

## Other forms

**The Hille--Yosida bound at a complex spectral parameter.** Formalized in Tau Ceti as [`TauCeti.Semigroups.StronglyContinuousSemigroup.norm_resolvent_complexGenerator_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Resolvent/Complex.html#TauCeti.Semigroups.StronglyContinuousSemigroup.norm_resolvent_complexGenerator_le).

```lean
TauCeti.Semigroups.StronglyContinuousSemigroup.norm_resolvent_complexGenerator_le.{u_1}
  {X : Type u_1} [NormedAddCommGroup X] [NormedSpace ℂ X] [CompleteSpace X] {omega M : ℝ}
  {lambda : ℂ} (S : TauCeti.Semigroups.StronglyContinuousSemigroup X) (hS : S.IsComplexLinear)
  (hb : S.HasGrowthBound omega M) (hlambda : omega < lambda.re) :
  ‖(S.complexGenerator hS).resolvent lambda‖ ≤ M / (lambda.re - omega)
```

**Hille--Yosida for quasi-contraction semigroups.** Formalized in Tau Ceti as [`TauCeti.Semigroups.exists_generator_eq_and_hasGrowthBound_one_iff_forall_norm_resolvent_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Generation/HilleYosida/Contraction.html#TauCeti.Semigroups.exists_generator_eq_and_hasGrowthBound_one_iff_forall_norm_resolvent_le).

```lean
TauCeti.Semigroups.exists_generator_eq_and_hasGrowthBound_one_iff_forall_norm_resolvent_le.{u_1}
  {X : Type u_1} [NormedAddCommGroup X] [NormedSpace ℝ X] [CompleteSpace X] (A : X →ₗ.[ℝ] X)
  (omega : ℝ) :
  (∃ S, S.generator = A ∧ S.HasGrowthBound omega 1) ↔
    Dense ↑A.domain ∧
      (∀ (lambda : ℝ), omega < lambda → lambda ∈ A.resolventSet) ∧
        ∀ (lambda : ℝ), omega < lambda → ‖A.resolvent lambda‖ ≤ (lambda - omega)⁻¹
```

**Hille--Yosida generation theorem.** Formalized in Tau Ceti as [`TauCeti.Semigroups.hilleYosida_generation`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Generation/HilleYosida/Generation.html#TauCeti.Semigroups.hilleYosida_generation).

```lean
TauCeti.Semigroups.hilleYosida_generation.{u_1} {X : Type u_1} [NormedAddCommGroup X]
  [NormedSpace ℝ X] [CompleteSpace X] {A : X →ₗ.[ℝ] X} {M omega : ℝ} (hM : 1 ≤ M)
  (hres : ∀ (lambda : ℝ), omega < lambda → lambda ∈ A.resolventSet)
  (hpow :
    ∀ (n : ℕ),
      1 ≤ n → ∀ (lambda : ℝ), omega < lambda → ‖A.resolvent lambda ^ n‖ ≤ M / (lambda - omega) ^ n)
  (hdense : Dense ↑A.domain) : ∃ S, S.generator = A ∧ S.HasGrowthBound omega M
```

**The Hille--Yosida power bounds at a complex spectral parameter.** Formalized in Tau Ceti as [`TauCeti.Semigroups.StronglyContinuousSemigroup.norm_resolvent_complexGenerator_pow_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Resolvent/Complex.html#TauCeti.Semigroups.StronglyContinuousSemigroup.norm_resolvent_complexGenerator_pow_le).

```lean
TauCeti.Semigroups.StronglyContinuousSemigroup.norm_resolvent_complexGenerator_pow_le.{u_1}
  {X : Type u_1} [NormedAddCommGroup X] [NormedSpace ℂ X] [CompleteSpace X] {omega M : ℝ}
  {lambda : ℂ} (S : TauCeti.Semigroups.StronglyContinuousSemigroup X) (hS : S.IsComplexLinear)
  (hb : S.HasGrowthBound omega M) (hlambda : omega < lambda.re) (n : ℕ) :
  ‖(S.complexGenerator hS).resolvent lambda ^ n‖ ≤ M / (lambda.re - omega) ^ n
```

**Hille--Yosida resolvent bound for the resolvent of the generator.** Formalized in Tau Ceti as [`TauCeti.Semigroups.StronglyContinuousSemigroup.norm_generator_resolvent_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Resolvent/Identity.html#TauCeti.Semigroups.StronglyContinuousSemigroup.norm_generator_resolvent_le).

```lean
TauCeti.Semigroups.StronglyContinuousSemigroup.norm_generator_resolvent_le.{u_1} {X : Type u_1}
  [NormedAddCommGroup X] [NormedSpace ℝ X] (S : TauCeti.Semigroups.StronglyContinuousSemigroup X)
  [CompleteSpace X] {omega M : ℝ} (hb : S.HasGrowthBound omega M) {lambda : ℝ}
  (hlambda : omega < lambda) : ‖S.generator.resolvent lambda‖ ≤ M / (lambda - omega)
```

**Hille–Yosida resolvent bound.** Formalized in Tau Ceti as [`TauCeti.Semigroups.StronglyContinuousSemigroup.resolvent_norm_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Resolvent/Basic.html#TauCeti.Semigroups.StronglyContinuousSemigroup.resolvent_norm_le).

```lean
TauCeti.Semigroups.StronglyContinuousSemigroup.resolvent_norm_le.{u_1} {X : Type u_1}
  [NormedAddCommGroup X] [NormedSpace ℝ X] [CompleteSpace X]
  (S : TauCeti.Semigroups.StronglyContinuousSemigroup X) {ω M : ℝ} (hb : S.HasGrowthBound ω M)
  (lambda : ℝ) (hlam : ω < lambda) : ‖S.resolvent hb lambda hlam‖ ≤ M / (lambda - ω)
```

## Sources

- [Tau Ceti documentation: `TauCeti.Semigroups.hilleYosida_generation_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Generation/HilleYosida/Generation.html#TauCeti.Semigroups.hilleYosida_generation_iff)
- [Source of `TauCeti.Semigroups.hilleYosida_generation_iff` in TauCeti/Analysis/Semigroups/Generation/HilleYosida/Generation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Semigroups/Generation/HilleYosida/Generation.lean#L215)
- [Tau Ceti roadmap status: One-parameter semigroups, completely monotone and positive-definite functions, and Bochner-type representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/OneParameterSemigroups/STATUS.md)
