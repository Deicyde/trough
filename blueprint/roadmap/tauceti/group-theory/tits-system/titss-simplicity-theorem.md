---
declaration: theorem
origin: cited
lean: TauCeti.TitsSystem.isSimpleGroup_quotient_normalCore, TauCeti.TitsSystem.le_normalCore_or_eq_top_of_normal
statement: formalized
proof: formalized
---

# Tits's simplicity theorem

Suppose there is at least one simple reflection, the Weyl group
is irreducible, `G` is perfect, and `U` is a solvable subgroup normalized by `B` whose conjugates
generate `G`. Then the quotient of `G` by the normal core `⋂ g B g⁻¹` of `B` is simple.

```lean
TauCeti.TitsSystem.isSimpleGroup_quotient_normalCore.{u} {G : Type u} [Group G]
  (T : TauCeti.TitsSystem G) (hS : T.simple.Nonempty) (hirr : T.IsIrreducible) [Group.IsPerfect G]
  {U : Subgroup G} [Group.IsSolvable ↥U] (hBU : T.subgroupB ≤ Subgroup.normalizer ↑U)
  (hU : Subgroup.normalClosure ↑U = ⊤) : IsSimpleGroup (G ⧸ T.subgroupB.normalCore)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Bruhat decomposition of a standard parabolic](the-bruhat-decomposition-of-a-standard-parabolic.md)
- [Tits's theorem on normal subgroups](titss-theorem-on-normal-subgroups.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.TitsSystem.isSimpleGroup_quotient_normalCore`](https://taucetiproject.org/docs/TauCeti/GroupTheory/TitsSystem/NormalSubgroup.html#TauCeti.TitsSystem.isSimpleGroup_quotient_normalCore).

## Other forms

**Tits's simplicity theorem, for normal subgroups.** Formalized in Tau Ceti as [`TauCeti.TitsSystem.le_normalCore_or_eq_top_of_normal`](https://taucetiproject.org/docs/TauCeti/GroupTheory/TitsSystem/NormalSubgroup.html#TauCeti.TitsSystem.le_normalCore_or_eq_top_of_normal).

```lean
TauCeti.TitsSystem.le_normalCore_or_eq_top_of_normal.{u} {G : Type u} [Group G]
  (T : TauCeti.TitsSystem G) (hirr : T.IsIrreducible) [Group.IsPerfect G] {U : Subgroup G}
  [Group.IsSolvable ↥U] (hBU : T.subgroupB ≤ Subgroup.normalizer ↑U)
  (hU : Subgroup.normalClosure ↑U = ⊤) (H : Subgroup G) [H.Normal] :
  H ≤ T.subgroupB.normalCore ∨ H = ⊤
```

## Sources

- [Tau Ceti documentation: `TauCeti.TitsSystem.isSimpleGroup_quotient_normalCore`](https://taucetiproject.org/docs/TauCeti/GroupTheory/TitsSystem/NormalSubgroup.html#TauCeti.TitsSystem.isSimpleGroup_quotient_normalCore)
- [Source of `TauCeti.TitsSystem.isSimpleGroup_quotient_normalCore` in TauCeti/GroupTheory/TitsSystem/NormalSubgroup.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/TitsSystem/NormalSubgroup.lean#L129)
