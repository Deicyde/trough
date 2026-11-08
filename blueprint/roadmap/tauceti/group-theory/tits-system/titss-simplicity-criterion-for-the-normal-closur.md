---
declaration: theorem
origin: cited
lean: TauCeti.TitsSystem.isSimpleGroup_quotient_normalCore_subgroupOf
statement: formalized
proof: formalized
---

# Tits's simplicity criterion for the normal closure of `U`

Under the hypotheses of
`TauCeti.TitsSystem.le_normalCore_subgroupOf_or_eq_top_of_normal`, the quotient `H⁺ / (Z ∩ H⁺)`
of the normal closure `H⁺` of `U` by its intersection with `Z = ⋂ g B g⁻¹` is simple whenever it is
nontrivial.

```lean
TauCeti.TitsSystem.isSimpleGroup_quotient_normalCore_subgroupOf.{u} {G : Type u} [Group G]
  (T : TauCeti.TitsSystem G) {U : Subgroup G} (hirr : T.IsIrreducible) [Group.IsSolvable ↥U]
  (hBU : T.subgroupB ≤ Subgroup.normalizer ↑U)
  (hsplit : T.subgroupB ≤ U ⊔ T.subgroupB ⊓ T.subgroupN)
  [Group.IsPerfect ↥(Subgroup.normalClosure ↑U)]
  [Nontrivial
      (↥(Subgroup.normalClosure ↑U) ⧸
        T.subgroupB.normalCore.subgroupOf (Subgroup.normalClosure ↑U))] :
  IsSimpleGroup
    (↥(Subgroup.normalClosure ↑U) ⧸ T.subgroupB.normalCore.subgroupOf (Subgroup.normalClosure ↑U))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Tits's theorem on normal subgroups](titss-theorem-on-normal-subgroups.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.TitsSystem.isSimpleGroup_quotient_normalCore_subgroupOf`](https://taucetiproject.org/docs/TauCeti/GroupTheory/TitsSystem/NormalClosure.html#TauCeti.TitsSystem.isSimpleGroup_quotient_normalCore_subgroupOf).

## Sources

- [Tau Ceti documentation: `TauCeti.TitsSystem.isSimpleGroup_quotient_normalCore_subgroupOf`](https://taucetiproject.org/docs/TauCeti/GroupTheory/TitsSystem/NormalClosure.html#TauCeti.TitsSystem.isSimpleGroup_quotient_normalCore_subgroupOf)
- [Source of `TauCeti.TitsSystem.isSimpleGroup_quotient_normalCore_subgroupOf` in TauCeti/GroupTheory/TitsSystem/NormalClosure.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/TitsSystem/NormalClosure.lean#L160)
