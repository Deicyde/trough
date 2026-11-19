---
declaration: theorem
origin: cited
lean: TauCeti.TitsSystem.isSimpleGroup_derivedCentralQuotient
statement: formalized
proof: formalized
---

# Simplicity of the derived central quotient from a split Tits system

Suppose the Weyl group
is irreducible, `U` is a solvable subgroup normalized by `B` with `B ≤ U (B ∩ N)` and
`Z ∩ U = 1` for `Z = ⋂ g B g⁻¹`, the normal closure of `U` is the derived subgroup `[G, G]`, and
`[G, G]` is perfect. Then the derived central quotient `[G, G] / Z([G, G])` is simple whenever it
is nontrivial.

```lean
TauCeti.TitsSystem.isSimpleGroup_derivedCentralQuotient.{u} {G : Type u} [Group G]
  (T : TauCeti.TitsSystem G) {U : Subgroup G} (hirr : T.IsIrreducible) [Group.IsSolvable ↥U]
  (hBU : T.subgroupB ≤ Subgroup.normalizer ↑U)
  (hsplit : T.subgroupB ≤ U ⊔ T.subgroupB ⊓ T.subgroupN) (hZU : T.subgroupB.normalCore ⊓ U = ⊥)
  (hU : Subgroup.normalClosure ↑U = commutator G) [Group.IsPerfect ↥(commutator G)]
  [Nontrivial (TauCeti.DerivedCentralQuotient G)] : IsSimpleGroup (TauCeti.DerivedCentralQuotient G)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Tits's simplicity criterion for the normal closure of `U`](titss-simplicity-criterion-for-the-normal-closur.md)
- [Tits's theorem on normal subgroups](../tits-system/titss-theorem-on-normal-subgroups.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.TitsSystem.isSimpleGroup_derivedCentralQuotient`](https://taucetiproject.org/docs/TauCeti/GroupTheory/TitsSystem/NormalClosure.html#TauCeti.TitsSystem.isSimpleGroup_derivedCentralQuotient).

## Sources

- [Tau Ceti documentation: `TauCeti.TitsSystem.isSimpleGroup_derivedCentralQuotient`](https://taucetiproject.org/docs/TauCeti/GroupTheory/TitsSystem/NormalClosure.html#TauCeti.TitsSystem.isSimpleGroup_derivedCentralQuotient)
- [Source of `TauCeti.TitsSystem.isSimpleGroup_derivedCentralQuotient` in TauCeti/GroupTheory/TitsSystem/NormalClosure.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/TitsSystem/NormalClosure.lean#L174)
- [Tau Ceti roadmap status: Finiteness and simplicity of the groups on the CFSG list](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CFSGBasicProperties/STATUS.md)
