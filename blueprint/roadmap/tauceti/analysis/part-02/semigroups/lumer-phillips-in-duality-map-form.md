---
declaration: theorem
origin: cited
lean: TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff_exists_mem_dualitySet_apply_nonpos, TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff, TauCeti.Semigroups.IsMDissipative.exists_contractionSemigroup_generator_eq, TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff_forall_mem_dualitySet_apply_nonpos
statement: formalized
proof: formalized
---

# Lumer--Phillips in duality-map form

An unbounded operator on a real Banach space
generates a contraction semigroup exactly when it is densely defined, each `x ∈ D(A)` has a
duality-set member `f` with `f (A x) ≤ 0`, and `lambda • I - A` maps `D(A)` onto `X` for some
`lambda > 0`.

```lean
TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff_exists_mem_dualitySet_apply_nonpos.{u_1}
  {X : Type u_1} [NormedAddCommGroup X] [NormedSpace ℝ X] [CompleteSpace X] (A : X →ₗ.[ℝ] X) :
  (∃ S, S.generator = A) ↔
    Dense ↑A.domain ∧
      (∀ (x : ↥A.domain), ∃ f ∈ TauCeti.dualitySet ℝ ↑x, f (↑A x) ≤ 0) ∧
        ∃ lambda, 0 < lambda ∧ Function.Surjective fun x => lambda • ↑x - ↑A x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Converse of the Lumer--Phillips theorem](converse-of-the-lumer-phillips-theorem.md)
- [The Duhamel identity for the exponential of a bounded operator](../normed/part-01/the-duhamel-identity-for-the-exponential-of-a-bo.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff_exists_mem_dualitySet_apply_nonpos`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Generation/LumerPhillips.html#TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff_exists_mem_dualitySet_apply_nonpos).

## Other forms

**Lumer--Phillips as a characterization.** Formalized in Tau Ceti as [`TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Generation/LumerPhillips.html#TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff).

```lean
TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff.{u_1} {X : Type u_1}
  [NormedAddCommGroup X] [NormedSpace ℝ X] [CompleteSpace X] (A : X →ₗ.[ℝ] X) :
  (∃ S, S.generator = A) ↔ Dense ↑A.domain ∧ TauCeti.Semigroups.IsMDissipative A
```

**The Lumer--Phillips generation theorem.** Formalized in Tau Ceti as [`TauCeti.Semigroups.IsMDissipative.exists_contractionSemigroup_generator_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Generation/LumerPhillips.html#TauCeti.Semigroups.IsMDissipative.exists_contractionSemigroup_generator_eq).

```lean
TauCeti.Semigroups.IsMDissipative.exists_contractionSemigroup_generator_eq.{u_1} {X : Type u_1}
  [NormedAddCommGroup X] [NormedSpace ℝ X] [CompleteSpace X] {A : X →ₗ.[ℝ] X}
  (hA : TauCeti.Semigroups.IsMDissipative A) (hdense : Dense ↑A.domain) : ∃ S, S.generator = A
```

**Lumer--Phillips with the universal duality-set sign condition.** Formalized in Tau Ceti as [`TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff_forall_mem_dualitySet_apply_nonpos`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Generation/LumerPhillips.html#TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff_forall_mem_dualitySet_apply_nonpos).

```lean
TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff_forall_mem_dualitySet_apply_nonpos.{u_1}
  {X : Type u_1} [NormedAddCommGroup X] [NormedSpace ℝ X] [CompleteSpace X] (A : X →ₗ.[ℝ] X) :
  (∃ S, S.generator = A) ↔
    Dense ↑A.domain ∧
      (∀ (x : ↥A.domain), ∀ f ∈ TauCeti.dualitySet ℝ ↑x, f (↑A x) ≤ 0) ∧
        ∃ lambda, 0 < lambda ∧ Function.Surjective fun x => lambda • ↑x - ↑A x
```

## Sources

- [Tau Ceti documentation: `TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff_exists_mem_dualitySet_apply_nonpos`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Generation/LumerPhillips.html#TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff_exists_mem_dualitySet_apply_nonpos)
- [Source of `TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff_exists_mem_dualitySet_apply_nonpos` in TauCeti/Analysis/Semigroups/Generation/LumerPhillips.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Semigroups/Generation/LumerPhillips.lean#L115)
