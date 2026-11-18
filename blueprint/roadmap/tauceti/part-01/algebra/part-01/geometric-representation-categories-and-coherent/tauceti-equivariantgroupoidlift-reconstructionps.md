---
declaration: def
origin: cited
lean: TauCeti.EquivariantGroupoidLift.reconstructionPseudofunctor
statement: formalized
---

# TauCeti.EquivariantGroupoidLift.reconstructionPseudofunctor

Reconstruct equivariant lifts and their morphisms from normalized transport data.
The unit and compositor are the canonical compatible modifications, and their coherence
follows from uniqueness of compatible modifications.

```lean
TauCeti.EquivariantGroupoidLift.reconstructionPseudofunctor.{w, v, u₂, v₁, u₁} {Γ : Type u₁}
  [CategoryTheory.Category.{v₁, u₁} Γ] {H : Type u₂} [Monoid H]
  (actions :
    Γ →
      CategoryTheory.Pseudofunctor (CategoryTheory.LocallyDiscrete (CategoryTheory.SingleObj H))
        CategoryTheory.Cat) :
  CategoryTheory.Pseudofunctor
    (CategoryTheory.LocallyDiscrete (TauCeti.EquivariantGroupoidLift.NormalizedTransport Γ actions))
    (TauCeti.EquivariantGroupoidLift Γ actions)
```

## Depends on

- [TauCeti.EquivariantGroupoidLift.instBicategory](tauceti-equivariantgroupoidlift-instbicategory.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.EquivariantGroupoidLift.reconstructionPseudofunctor`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Bicategory/Functor/EquivariantGroupoidLift/NormalizedTransport/Reconstruction.html#TauCeti.EquivariantGroupoidLift.reconstructionPseudofunctor).

## Sources

- [Tau Ceti documentation: `TauCeti.EquivariantGroupoidLift.reconstructionPseudofunctor`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Bicategory/Functor/EquivariantGroupoidLift/NormalizedTransport/Reconstruction.html#TauCeti.EquivariantGroupoidLift.reconstructionPseudofunctor)
- [Source of `TauCeti.EquivariantGroupoidLift.reconstructionPseudofunctor` in TauCeti/CategoryTheory/Bicategory/Functor/EquivariantGroupoidLift/NormalizedTransport/Reconstruction.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/Bicategory/Functor/EquivariantGroupoidLift/NormalizedTransport/Reconstruction.lean#L239)
- [Tau Ceti roadmap status: Geometric representation categories and coherent local transport](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeometricRepresentationCategories/STATUS.md)
