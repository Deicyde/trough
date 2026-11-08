---
declaration: theorem
origin: cited
lean: TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff_forall_norm_resolvent_le
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

- [Lumer--Phillips in duality-map form](../../part-02/semigroups/lumer-phillips-in-duality-map-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff_forall_norm_resolvent_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Generation/HilleYosida/Contraction.html#TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff_forall_norm_resolvent_le).

## Sources

- [Tau Ceti documentation: `TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff_forall_norm_resolvent_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Generation/HilleYosida/Contraction.html#TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff_forall_norm_resolvent_le)
- [Source of `TauCeti.Semigroups.exists_contractionSemigroup_generator_eq_iff_forall_norm_resolvent_le` in TauCeti/Analysis/Semigroups/Generation/HilleYosida/Contraction.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Semigroups/Generation/HilleYosida/Contraction.lean#L70)
- [Tau Ceti roadmap status: One-parameter semigroups, completely monotone and positive-definite functions, and Bochner-type representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/OneParameterSemigroups/STATUS.md)
