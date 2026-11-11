---
declaration: theorem
origin: cited
lean: MulAction.IwasawaStructure.isSimpleGroup_derivedCentralQuotient, MulAction.IwasawaStructure.isSimpleGroup_quotient, MulAction.IwasawaStructure.isSimpleGroup_quotient_center
statement: formalized
proof: formalized
---

# Iwasawa's criterion for the derived central quotient

Let a nontrivial perfect group `G`
have an Iwasawa structure on a quasiprimitive action whose kernel is central. Then the derived
subgroup of `G` modulo its centre, `TauCeti.DerivedCentralQuotient G`, is simple.

```lean
MulAction.IwasawaStructure.isSimpleGroup_derivedCentralQuotient.{u_1, u_2} {G : Type u_1}
  {α : Type u_2} [Group G] [MulAction G α] [MulAction.IsQuasiPreprimitive G α]
  (IwaS : MulAction.IwasawaStructure G α) [Group.IsPerfect G] [Nontrivial G]
  (hker : ∀ (g : G), (∀ (x : α), g • x = x) → g ∈ Subgroup.center G) :
  IsSimpleGroup (TauCeti.DerivedCentralQuotient G)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Iwasawa's normal-subgroup theorem for a perfect group](iwasawas-normal-subgroup-theorem-for-a-perfect-g.md)

## Lean

Formalized in Tau Ceti as [`MulAction.IwasawaStructure.isSimpleGroup_derivedCentralQuotient`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupAction/Iwasawa.html#MulAction.IwasawaStructure.isSimpleGroup_derivedCentralQuotient).

## Other forms

**Iwasawa's criterion for a quotient.** Formalized in Tau Ceti as [`MulAction.IwasawaStructure.isSimpleGroup_quotient`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupAction/Iwasawa.html#MulAction.IwasawaStructure.isSimpleGroup_quotient).

```lean
MulAction.IwasawaStructure.isSimpleGroup_quotient.{u_1, u_2} {G : Type u_1} {α : Type u_2} [Group G]
  [MulAction G α] [MulAction.IsQuasiPreprimitive G α] (IwaS : MulAction.IwasawaStructure G α)
  [Group.IsPerfect G] {N : Subgroup G} [N.Normal] (hN : N ≠ ⊤)
  (hker : ∀ (g : G), (∀ (x : α), g • x = x) → g ∈ N) : IsSimpleGroup (G ⧸ N)
```

**Iwasawa's criterion for the central quotient.** Formalized in Tau Ceti as [`MulAction.IwasawaStructure.isSimpleGroup_quotient_center`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupAction/Iwasawa.html#MulAction.IwasawaStructure.isSimpleGroup_quotient_center).

```lean
MulAction.IwasawaStructure.isSimpleGroup_quotient_center.{u_1, u_2} {G : Type u_1} {α : Type u_2}
  [Group G] [MulAction G α] [MulAction.IsQuasiPreprimitive G α]
  (IwaS : MulAction.IwasawaStructure G α) [Group.IsPerfect G] [Nontrivial G]
  (hker : ∀ (g : G), (∀ (x : α), g • x = x) → g ∈ Subgroup.center G) :
  IsSimpleGroup (G ⧸ Subgroup.center G)
```

## Sources

- [Tau Ceti documentation: `MulAction.IwasawaStructure.isSimpleGroup_derivedCentralQuotient`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupAction/Iwasawa.html#MulAction.IwasawaStructure.isSimpleGroup_derivedCentralQuotient)
- [Source of `MulAction.IwasawaStructure.isSimpleGroup_derivedCentralQuotient` in TauCeti/GroupTheory/GroupAction/Iwasawa.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/GroupAction/Iwasawa.lean#L166)
- [Tau Ceti roadmap status: Finiteness and simplicity of the groups on the CFSG list](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CFSGBasicProperties/STATUS.md)
