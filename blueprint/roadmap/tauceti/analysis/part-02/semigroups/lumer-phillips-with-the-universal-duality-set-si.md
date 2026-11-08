---
declaration: theorem
origin: cited
lean: TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff_forall_mem_dualitySet_apply_nonpos
statement: formalized
proof: formalized
---

# Lumer--Phillips with the universal duality-set sign condition

A densely defined
operator generates a contraction semigroup exactly when every member of the duality set of
each `x ∈ D(A)` is nonpositive on `A x`, and the positive resolvent range condition holds.

```lean
TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff_forall_mem_dualitySet_apply_nonpos.{u_1}
  {X : Type u_1} [NormedAddCommGroup X] [NormedSpace ℝ X] [CompleteSpace X] (A : X →ₗ.[ℝ] X) :
  (∃ S, S.generator = A) ↔
    Dense ↑A.domain ∧
      (∀ (x : ↥A.domain), ∀ f ∈ TauCeti.dualitySet ℝ ↑x, f (↑A x) ≤ 0) ∧
        ∃ lambda, 0 < lambda ∧ Function.Surjective fun x => lambda • ↑x - ↑A x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Converse of the Lumer--Phillips theorem](converse-of-the-lumer-phillips-theorem.md)
- [The Lumer--Phillips generation theorem](the-lumer-phillips-generation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff_forall_mem_dualitySet_apply_nonpos`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Generation/LumerPhillips.html#TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff_forall_mem_dualitySet_apply_nonpos).

## Sources

- [Tau Ceti documentation: `TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff_forall_mem_dualitySet_apply_nonpos`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Generation/LumerPhillips.html#TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff_forall_mem_dualitySet_apply_nonpos)
- [Source of `TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff_forall_mem_dualitySet_apply_nonpos` in TauCeti/Analysis/Semigroups/Generation/LumerPhillips.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Semigroups/Generation/LumerPhillips.lean#L129)
