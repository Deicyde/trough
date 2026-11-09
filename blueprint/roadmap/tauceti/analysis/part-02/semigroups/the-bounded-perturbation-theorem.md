---
declaration: theorem
origin: cited
lean: TauCeti.Semigroups.StronglyContinuousSemigroup.exists_generator_eq_vadd, TauCeti.Semigroups.StronglyContinuousSemigroup.exists_generator_eq_vadd_of_hasGrowthBound_one, TauCeti.Semigroups.ContractionSemigroup.exists_generator_eq_vadd, TauCeti.Semigroups.IsMDissipative.exists_stronglyContinuousSemigroup_generator_eq_vadd
statement: formalized
proof: formalized
---

# The bounded perturbation theorem

If a strongly continuous semigroup `S` has growth
bound `(omega, M)` and `B` is bounded, then `B +ᵥ S.generator` generates a strongly continuous
semigroup with growth bound `(omega + M * ‖B‖, M)`.

```lean
TauCeti.Semigroups.StronglyContinuousSemigroup.exists_generator_eq_vadd.{u_1} {X : Type u_1}
  [NormedAddCommGroup X] [NormedSpace ℝ X] [CompleteSpace X]
  (S : TauCeti.Semigroups.StronglyContinuousSemigroup X) {omega M : ℝ}
  (hb : S.HasGrowthBound omega M) (B : X →L[ℝ] X) :
  ∃ T, T.generator = ↑B +ᵥ S.generator ∧ T.HasGrowthBound (omega + M * ‖B‖) M
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Converse of the Lumer--Phillips theorem](converse-of-the-lumer-phillips-theorem.md)
- [Lumer--Phillips in duality-map form](lumer-phillips-in-duality-map-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Semigroups.StronglyContinuousSemigroup.exists_generator_eq_vadd`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Generation/BoundedPerturbation.html#TauCeti.Semigroups.StronglyContinuousSemigroup.exists_generator_eq_vadd).

## Other forms

**The bounded perturbation theorem.** Formalized in Tau Ceti as [`TauCeti.Semigroups.StronglyContinuousSemigroup.exists_generator_eq_vadd_of_hasGrowthBound_one`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Generation/BoundedPerturbation.html#TauCeti.Semigroups.StronglyContinuousSemigroup.exists_generator_eq_vadd_of_hasGrowthBound_one).

```lean
TauCeti.Semigroups.StronglyContinuousSemigroup.exists_generator_eq_vadd_of_hasGrowthBound_one.{u_1}
  {X : Type u_1} [NormedAddCommGroup X] [NormedSpace ℝ X] [CompleteSpace X]
  (S : TauCeti.Semigroups.StronglyContinuousSemigroup X) {omega : ℝ} (hb : S.HasGrowthBound omega 1)
  (B : X →L[ℝ] X) : ∃ T, T.generator = ↑B +ᵥ S.generator ∧ T.HasGrowthBound (omega + ‖B‖) 1
```

**The bounded perturbation theorem for contraction semigroups.** Formalized in Tau Ceti as [`TauCeti.Semigroups.ContractionSemigroup.exists_generator_eq_vadd`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Generation/BoundedPerturbation.html#TauCeti.Semigroups.ContractionSemigroup.exists_generator_eq_vadd).

```lean
TauCeti.Semigroups.ContractionSemigroup.exists_generator_eq_vadd.{u_1} {X : Type u_1}
  [NormedAddCommGroup X] [NormedSpace ℝ X] [CompleteSpace X]
  (S : TauCeti.Semigroups.ContractionSemigroup X) (B : X →L[ℝ] X) :
  ∃ T, T.generator = ↑B +ᵥ S.generator ∧ T.HasGrowthBound ‖B‖ 1
```

**The bounded perturbation theorem, operator form.** Formalized in Tau Ceti as [`TauCeti.Semigroups.IsMDissipative.exists_stronglyContinuousSemigroup_generator_eq_vadd`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Generation/BoundedPerturbation.html#TauCeti.Semigroups.IsMDissipative.exists_stronglyContinuousSemigroup_generator_eq_vadd).

```lean
TauCeti.Semigroups.IsMDissipative.exists_stronglyContinuousSemigroup_generator_eq_vadd.{u_1}
  {X : Type u_1} [NormedAddCommGroup X] [NormedSpace ℝ X] {A : X →ₗ.[ℝ] X} [CompleteSpace X]
  (hA : TauCeti.Semigroups.IsMDissipative A) (hdense : Dense ↑A.domain) (B : X →L[ℝ] X) :
  ∃ S, S.generator = ↑B +ᵥ A ∧ S.HasGrowthBound ‖B‖ 1
```

## Sources

- [Tau Ceti documentation: `TauCeti.Semigroups.StronglyContinuousSemigroup.exists_generator_eq_vadd`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Generation/BoundedPerturbation.html#TauCeti.Semigroups.StronglyContinuousSemigroup.exists_generator_eq_vadd)
- [Source of `TauCeti.Semigroups.StronglyContinuousSemigroup.exists_generator_eq_vadd` in TauCeti/Analysis/Semigroups/Generation/BoundedPerturbation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Semigroups/Generation/BoundedPerturbation.lean#L442)
