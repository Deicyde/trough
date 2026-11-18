---
declaration: def
origin: cited
lean: TauCeti.SchemeInertia.decompositionQuotientInertiaEquiv
statement: formalized
---

# The decomposition group modulo the inertia group is the automorphism group of the residue extension

**The decomposition group modulo the inertia group is the automorphism group of the residue
extension**, when `G` acts by automorphisms over `X` and any two points of `Y` with values in a
field and the same image in `X` differ by the action of an element of `G`.

```lean
TauCeti.SchemeInertia.decompositionQuotientInertiaEquiv.{u, v} {Y : AlgebraicGeometry.Scheme}
  {G : Type v} [Group G] (σ : G →* CategoryTheory.Aut Y) {X : AlgebraicGeometry.Scheme} (π : Y ⟶ X)
  (hπ : ∀ (g : G), CategoryTheory.CategoryStruct.comp (σ g).asIso.hom π = π)
  (horb :
    ∀ {K : Type u} [inst : Field K] {x₁ x₂ : AlgebraicGeometry.Spec ↧K ⟶ Y},
      CategoryTheory.CategoryStruct.comp x₁ π = CategoryTheory.CategoryStruct.comp x₂ π →
        ∃ g, CategoryTheory.CategoryStruct.comp x₁ (σ g).asIso.hom = x₂)
  (y : ↥Y) :
  ↥(TauCeti.SchemeInertia.decomposition σ y) ⧸
      (TauCeti.SchemeInertia.inertia σ y).subgroupOf (TauCeti.SchemeInertia.decomposition σ y) ≃*
    Gal(↑(Y.residueField y)/↑(X.residueField (π y)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SchemeInertia.decompositionQuotientInertiaEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/GroupAction/Inertia.html#TauCeti.SchemeInertia.decompositionQuotientInertiaEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.SchemeInertia.decompositionQuotientInertiaEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/GroupAction/Inertia.html#TauCeti.SchemeInertia.decompositionQuotientInertiaEquiv)
- [Source of `TauCeti.SchemeInertia.decompositionQuotientInertiaEquiv` in TauCeti/AlgebraicGeometry/GroupAction/Inertia.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/GroupAction/Inertia.lean#L352)
- [Tau Ceti roadmap status: Étale cohomology foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EtaleCohomologyFoundations/STATUS.md)
