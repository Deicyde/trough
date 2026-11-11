---
declaration: class
origin: cited
lean: CategoryTheory.Functor.IsBalanced
statement: formalized
---

# CategoryTheory.Functor.IsBalanced

A strong braided monoidal functor is balanced when it preserves the chosen twists.

```lean
CategoryTheory.Functor.IsBalanced.{v₁, v₂, u₁, u₂} {C : Type u₁}
  [CategoryTheory.Category.{v₁, u₁} C] [CategoryTheory.MonoidalCategory C]
  [CategoryTheory.BraidedCategory C] [TauCeti.BalancedCategory C] {D : Type u₂}
  [CategoryTheory.Category.{v₂, u₂} D] [CategoryTheory.MonoidalCategory D]
  [CategoryTheory.BraidedCategory D] [TauCeti.BalancedCategory D] (F : CategoryTheory.Functor C D)
  [F.Braided] : Prop
```

## Depends on

- [TauCeti.BalancedCategory](../pivotal-and-spherical-categories/tauceti-balancedcategory.md)

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Functor.IsBalanced`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Braided/Balanced/Functor.html#CategoryTheory.Functor.IsBalanced).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Functor.IsBalanced`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Braided/Balanced/Functor.html#CategoryTheory.Functor.IsBalanced)
- [Source of `CategoryTheory.Functor.IsBalanced` in TauCeti/CategoryTheory/Monoidal/Braided/Balanced/Functor.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Monoidal/Braided/Balanced/Functor.lean#L41)
- [Tau Ceti roadmap status: Diagrammatic coherence for monoidal categories and duality](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DiagrammaticCoherence/STATUS.md)
