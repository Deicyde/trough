---
declaration: def
origin: cited
lean: TauCeti.EffectiveQuotient.isomorphismClassesHomeomorph
statement: formalized
---

# TauCeti.EffectiveQuotient.isomorphismClassesHomeomorph

Effective reduction does not change the coarse space: the projection to the effective quotient
induces a homeomorphism between the spaces of isomorphism classes.

```lean
TauCeti.EffectiveQuotient.isomorphismClassesHomeomorph.{u_1, u_2} (C : Type u_1)
  [CategoryTheory.Groupoid C] [TopologicalSpace (Quiver.Total C)] [TopologicalSpace C] :
  Quotient (CategoryTheory.isIsomorphicSetoid C) ≃ₜ
    Quotient (CategoryTheory.isIsomorphicSetoid (TauCeti.EffectiveQuotient C))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.EffectiveQuotient.isomorphismClassesHomeomorph`](https://taucetiproject.org/docs/TauCeti/Topology/CategoryTheory/Groupoid/Effective/Basic.html#TauCeti.EffectiveQuotient.isomorphismClassesHomeomorph).

## Sources

- [Tau Ceti documentation: `TauCeti.EffectiveQuotient.isomorphismClassesHomeomorph`](https://taucetiproject.org/docs/TauCeti/Topology/CategoryTheory/Groupoid/Effective/Basic.html#TauCeti.EffectiveQuotient.isomorphismClassesHomeomorph)
- [Source of `TauCeti.EffectiveQuotient.isomorphismClassesHomeomorph` in TauCeti/Topology/CategoryTheory/Groupoid/Effective/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/CategoryTheory/Groupoid/Effective/Basic.lean#L245)
- [Tau Ceti roadmap status: Smooth orbifolds with finite isotropy](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Orbifolds/STATUS.md)
