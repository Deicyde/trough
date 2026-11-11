---
declaration: theorem
origin: cited
lean: TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff_forall_norm_resolvent_le, TauCeti.Semigroups.exists_generator_eq_and_hasGrowthBound_one_iff_forall_norm_resolvent_le, TauCeti.Semigroups.hilleYosida_generation
statement: formalized
proof: formalized
---

# Hille--Yosida for contraction semigroups

An unbounded operator `A` on a real Banach
space generates a strongly continuous contraction semigroup if and only if its domain is dense,
every `lambda > 0` lies in its resolvent set, and `‖R(lambda, A)‖ ≤ 1 / lambda` for every
`lambda > 0`.

```lean
TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff_forall_norm_resolvent_le.{u_1}
  {X : Type u_1} [NormedAddCommGroup X] [NormedSpace ℝ X] [CompleteSpace X] (A : X →ₗ.[ℝ] X) :
  (∃ S, S.generator = A) ↔
    Dense ↑A.domain ∧
      (∀ (lambda : ℝ), 0 < lambda → lambda ∈ A.resolventSet) ∧
        ∀ (lambda : ℝ), 0 < lambda → ‖A.resolvent lambda‖ ≤ lambda⁻¹
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Duhamel identity for the exponential of a bounded operator](../../part-03/normed/part-01/the-duhamel-identity-for-the-exponential-of-a-bo.md)
- [Hille--Yosida characterization](hille-yosida-characterization.md)
- [Lumer--Phillips in duality-map form](../../part-03/semigroups/lumer-phillips-in-duality-map-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff_forall_norm_resolvent_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Generation/HilleYosida/Contraction.html#TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff_forall_norm_resolvent_le).

## Other forms

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

## Sources

- [Tau Ceti documentation: `TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff_forall_norm_resolvent_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Generation/HilleYosida/Contraction.html#TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff_forall_norm_resolvent_le)
- [Source of `TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff_forall_norm_resolvent_le` in TauCeti/Analysis/Semigroups/Generation/HilleYosida/Contraction.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Semigroups/Generation/HilleYosida/Contraction.lean#L70)
- [Tau Ceti roadmap status: One-parameter semigroups, completely monotone and positive-definite functions, and Bochner-type representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/OneParameterSemigroups/STATUS.md)
