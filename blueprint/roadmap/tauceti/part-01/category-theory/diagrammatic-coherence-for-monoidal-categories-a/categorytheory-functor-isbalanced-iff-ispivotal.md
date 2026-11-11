---
declaration: theorem
origin: cited
lean: CategoryTheory.Functor.isBalanced_iff_isPivotal
statement: formalized
proof: formalized
---

# CategoryTheory.Functor.isBalanced_iff_isPivotal

For the twists corresponding to the chosen pivotal structures, a strong braided functor
is balanced if and only if it is pivotal. The balanced structures are explicit local choices.

```lean
CategoryTheory.Functor.isBalanced_iff_isPivotal.{v₁, v₂, u₁, u₂} {C : Type u₁}
  [CategoryTheory.Category.{v₁, u₁} C] [CategoryTheory.MonoidalCategory C]
  [CategoryTheory.BraidedCategory C] [CategoryTheory.RigidCategory C] {D : Type u₂}
  [CategoryTheory.Category.{v₂, u₂} D] [CategoryTheory.MonoidalCategory D]
  [CategoryTheory.BraidedCategory D] [CategoryTheory.RigidCategory D] [TauCeti.PivotalCategory C]
  [TauCeti.PivotalCategory D] (F : CategoryTheory.Functor C D) [F.Braided] :
  F.IsBalanced ↔ F.IsPivotal
```

## Depends on

- [CategoryTheory.Functor.IsBalanced](categorytheory-functor-isbalanced.md)
- [TauCeti.BalancedCategory](../pivotal-and-spherical-categories/tauceti-balancedcategory.md)

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Functor.isBalanced_iff_isPivotal`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Pivotal/Functor/Balanced.html#CategoryTheory.Functor.isBalanced_iff_isPivotal).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Functor.isBalanced_iff_isPivotal`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Pivotal/Functor/Balanced.html#CategoryTheory.Functor.isBalanced_iff_isPivotal)
- [Source of `CategoryTheory.Functor.isBalanced_iff_isPivotal` in TauCeti/CategoryTheory/Monoidal/Pivotal/Functor/Balanced.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Monoidal/Pivotal/Functor/Balanced.lean#L68)
- [Tau Ceti roadmap status: Diagrammatic coherence for monoidal categories and duality](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DiagrammaticCoherence/STATUS.md)
