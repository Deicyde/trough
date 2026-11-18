---
declaration: def
origin: cited
lean: TauCeti.EquivariantGroupoidLift.normalizationPseudofunctor
statement: formalized
---

# TauCeti.EquivariantGroupoidLift.normalizationPseudofunctor

Normalize equivariant lifts, their morphisms and compatible modifications on the
prescribed fibers. The target has only identity `2`-morphisms between equal comparisons.

```lean
TauCeti.EquivariantGroupoidLift.normalizationPseudofunctor.{w, v, u₂, v₁, u₁} {Γ : Type u₁}
  [CategoryTheory.Category.{v₁, u₁} Γ] {H : Type u₂} [Monoid H]
  (actions :
    Γ →
      CategoryTheory.Pseudofunctor (CategoryTheory.LocallyDiscrete (CategoryTheory.SingleObj H))
        CategoryTheory.Cat) :
  CategoryTheory.Pseudofunctor (TauCeti.EquivariantGroupoidLift Γ actions)
    (CategoryTheory.LocallyDiscrete (TauCeti.EquivariantGroupoidLift.NormalizedTransport Γ actions))
```

## Depends on

- [TauCeti.EquivariantGroupoidLift.instBicategory](tauceti-equivariantgroupoidlift-instbicategory.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.EquivariantGroupoidLift.normalizationPseudofunctor`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Bicategory/Functor/EquivariantGroupoidLift/NormalizedTransport/Functor.html#TauCeti.EquivariantGroupoidLift.normalizationPseudofunctor).

## Sources

- [Tau Ceti documentation: `TauCeti.EquivariantGroupoidLift.normalizationPseudofunctor`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Bicategory/Functor/EquivariantGroupoidLift/NormalizedTransport/Functor.html#TauCeti.EquivariantGroupoidLift.normalizationPseudofunctor)
- [Source of `TauCeti.EquivariantGroupoidLift.normalizationPseudofunctor` in TauCeti/CategoryTheory/Bicategory/Functor/EquivariantGroupoidLift/NormalizedTransport/Functor.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/Bicategory/Functor/EquivariantGroupoidLift/NormalizedTransport/Functor.lean#L33)
- [Tau Ceti roadmap status: Geometric representation categories and coherent local transport](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeometricRepresentationCategories/STATUS.md)
