---
declaration: theorem
origin: cited
lean: MulAction.IwasawaStructure.isSimpleGroup_quotient, MulAction.IwasawaStructure.isSimpleGroup_quotient_center, MulAction.IwasawaStructure.isSimpleGroup_derivedCentralQuotient
statement: formalized
proof: formalized
---

# Iwasawa's criterion for a quotient

Let a perfect group `G` have an Iwasawa structure on a
quasiprimitive action. If a proper normal subgroup `N` contains every element acting trivially,
then `G ⧸ N` is simple.

```lean
MulAction.IwasawaStructure.isSimpleGroup_quotient.{u_1, u_2} {G : Type u_1} {α : Type u_2} [Group G]
  [MulAction G α] [MulAction.IsQuasiPreprimitive G α] (IwaS : MulAction.IwasawaStructure G α)
  [Group.IsPerfect G] {N : Subgroup G} [N.Normal] (hN : N ≠ ⊤)
  (hker : ∀ (g : G), (∀ (x : α), g • x = x) → g ∈ N) : IsSimpleGroup (G ⧸ N)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Iwasawa's normal-subgroup theorem for a perfect group](iwasawas-normal-subgroup-theorem-for-a-perfect-g.md)

## Lean

Formalized in Tau Ceti as [`MulAction.IwasawaStructure.isSimpleGroup_quotient`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupAction/Iwasawa.html#MulAction.IwasawaStructure.isSimpleGroup_quotient).

## Other forms

**Iwasawa's criterion for the central quotient.** Formalized in Tau Ceti as [`MulAction.IwasawaStructure.isSimpleGroup_quotient_center`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupAction/Iwasawa.html#MulAction.IwasawaStructure.isSimpleGroup_quotient_center).

```lean
MulAction.IwasawaStructure.isSimpleGroup_quotient_center.{u_1, u_2} {G : Type u_1} {α : Type u_2}
  [Group G] [MulAction G α] [MulAction.IsQuasiPreprimitive G α]
  (IwaS : MulAction.IwasawaStructure G α) [Group.IsPerfect G] [Nontrivial G]
  (hker : ∀ (g : G), (∀ (x : α), g • x = x) → g ∈ Subgroup.center G) :
  IsSimpleGroup (G ⧸ Subgroup.center G)
```

**Iwasawa's criterion for the derived central quotient.** Formalized in Tau Ceti as [`MulAction.IwasawaStructure.isSimpleGroup_derivedCentralQuotient`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupAction/Iwasawa.html#MulAction.IwasawaStructure.isSimpleGroup_derivedCentralQuotient).

```lean
MulAction.IwasawaStructure.isSimpleGroup_derivedCentralQuotient.{u_1, u_2} {G : Type u_1}
  {α : Type u_2} [Group G] [MulAction G α] [MulAction.IsQuasiPreprimitive G α]
  (IwaS : MulAction.IwasawaStructure G α) [Group.IsPerfect G] [Nontrivial G]
  (hker : ∀ (g : G), (∀ (x : α), g • x = x) → g ∈ Subgroup.center G) :
  IsSimpleGroup (TauCeti.DerivedCentralQuotient G)
```

## Sources

- [Tau Ceti documentation: `MulAction.IwasawaStructure.isSimpleGroup_quotient`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupAction/Iwasawa.html#MulAction.IwasawaStructure.isSimpleGroup_quotient)
- [Source of `MulAction.IwasawaStructure.isSimpleGroup_quotient` in TauCeti/GroupTheory/GroupAction/Iwasawa.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/GroupAction/Iwasawa.lean#L136)
