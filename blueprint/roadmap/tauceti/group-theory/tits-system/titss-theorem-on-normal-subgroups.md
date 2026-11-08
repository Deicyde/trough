---
declaration: theorem
origin: cited
lean: TauCeti.TitsSystem.exists_standardParabolic_eq_sup_of_normal, TauCeti.TitsSystem.le_normalCore_subgroupOf_or_eq_top_of_normal
statement: formalized
proof: formalized
---

# Tits's theorem on normal subgroups

For a normal subgroup `H`, the subgroup `H ⊔ B` is a
standard parabolic `P_J` for a set `J` of simple reflections that commutes elementwise with its
complement.

```lean
TauCeti.TitsSystem.exists_standardParabolic_eq_sup_of_normal.{u} {G : Type u} [Group G]
  (T : TauCeti.TitsSystem G) (H : Subgroup G) [H.Normal] :
  ∃ J, T.standardParabolic J = H ⊔ T.subgroupB ∧ ∀ s ∈ J, ∀ t ∉ J, ↑s * ↑t = ↑t * ↑s
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Bruhat decomposition of a standard parabolic](the-bruhat-decomposition-of-a-standard-parabolic.md)
- [The key step of Tits's theorem on normal subgroups](the-key-step-of-titss-theorem-on-normal-subgroup.md)
- [Tits's simplicity theorem](titss-simplicity-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.TitsSystem.exists_standardParabolic_eq_sup_of_normal`](https://taucetiproject.org/docs/TauCeti/GroupTheory/TitsSystem/NormalSubgroup.html#TauCeti.TitsSystem.exists_standardParabolic_eq_sup_of_normal).

## Other forms

**Tits's theorem on normal subgroups of the normal closure of `U`.** Formalized in Tau Ceti as [`TauCeti.TitsSystem.le_normalCore_subgroupOf_or_eq_top_of_normal`](https://taucetiproject.org/docs/TauCeti/GroupTheory/TitsSystem/NormalClosure.html#TauCeti.TitsSystem.le_normalCore_subgroupOf_or_eq_top_of_normal).

```lean
TauCeti.TitsSystem.le_normalCore_subgroupOf_or_eq_top_of_normal.{u} {G : Type u} [Group G]
  (T : TauCeti.TitsSystem G) {U : Subgroup G} (hirr : T.IsIrreducible) [Group.IsSolvable ↥U]
  (hBU : T.subgroupB ≤ Subgroup.normalizer ↑U)
  (hsplit : T.subgroupB ≤ U ⊔ T.subgroupB ⊓ T.subgroupN)
  [Group.IsPerfect ↥(Subgroup.normalClosure ↑U)] (K : Subgroup ↥(Subgroup.normalClosure ↑U))
  [K.Normal] : K ≤ T.subgroupB.normalCore.subgroupOf (Subgroup.normalClosure ↑U) ∨ K = ⊤
```

## Sources

- [Tau Ceti documentation: `TauCeti.TitsSystem.exists_standardParabolic_eq_sup_of_normal`](https://taucetiproject.org/docs/TauCeti/GroupTheory/TitsSystem/NormalSubgroup.html#TauCeti.TitsSystem.exists_standardParabolic_eq_sup_of_normal)
- [Source of `TauCeti.TitsSystem.exists_standardParabolic_eq_sup_of_normal` in TauCeti/GroupTheory/TitsSystem/NormalSubgroup.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/TitsSystem/NormalSubgroup.lean#L98)
