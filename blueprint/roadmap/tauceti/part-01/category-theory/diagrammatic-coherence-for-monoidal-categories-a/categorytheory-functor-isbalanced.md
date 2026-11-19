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

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Functor.IsBalanced`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Braided/Balanced/Functor.html#CategoryTheory.Functor.IsBalanced).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Functor.IsBalanced`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Braided/Balanced/Functor.html#CategoryTheory.Functor.IsBalanced)
- [Source of `CategoryTheory.Functor.IsBalanced` in TauCeti/CategoryTheory/Monoidal/Braided/Balanced/Functor.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/Monoidal/Braided/Balanced/Functor.lean#L41)
- [Tau Ceti roadmap status: Diagrammatic coherence for monoidal categories and duality](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DiagrammaticCoherence/STATUS.md)
