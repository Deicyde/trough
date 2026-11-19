---
declaration: def
origin: cited
lean: Subgroup.presentationEquiv
statement: formalized
---

# Subgroup.presentationEquiv

A presentation of the exact subgroup `K` of a presented group, using a free basis of its
preimage and the rewritten transversal-conjugated relators. No assumption that the subgroup
is normal, finite, or of index two is imposed.

```lean
Subgroup.presentationEquiv.{u_1, u_2} {α : Type u_1} {β : Type u_2} {R : Set (FreeGroup α)}
  (K : Subgroup (PresentedGroup R)) (e : FreeGroup β ≃* ↥(Subgroup.comap (PresentedGroup.mk R) K))
  (T : Set (FreeGroup α)) (hT : ∀ (g : FreeGroup α), ∃ h, ∃ t ∈ T, ↑h * t = g) :
  PresentedGroup (PresentedGroup.subgroupRelators R (Subgroup.comap (PresentedGroup.mk R) K) e T) ≃*
    ↥K
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Subgroup.presentationEquiv`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Presentation/Subgroup.html#Subgroup.presentationEquiv).

## Sources

- [Tau Ceti documentation: `Subgroup.presentationEquiv`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Presentation/Subgroup.html#Subgroup.presentationEquiv)
- [Source of `Subgroup.presentationEquiv` in TauCeti/GroupTheory/Presentation/Subgroup.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/Presentation/Subgroup.lean#L117)
- [Tau Ceti roadmap status: Finiteness and simplicity of the groups on the CFSG list](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CFSGBasicProperties/STATUS.md)
