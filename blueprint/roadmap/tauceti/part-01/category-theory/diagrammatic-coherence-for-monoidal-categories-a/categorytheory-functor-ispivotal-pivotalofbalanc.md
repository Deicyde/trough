---
declaration: theorem
origin: cited
lean: CategoryTheory.Functor.isPivotal_pivotalOfBalanced_iff
statement: formalized
proof: formalized
---

# CategoryTheory.Functor.isPivotal_pivotalOfBalanced_iff

For the pivotal structures induced by chosen twists, pivotal preservation is equivalent
to twist preservation. No compatibility of either twist with duals is required.

```lean
CategoryTheory.Functor.isPivotal_pivotalOfBalanced_iff.{v₁, v₂, u₁, u₂} {C : Type u₁}
  [CategoryTheory.Category.{v₁, u₁} C] [CategoryTheory.MonoidalCategory C]
  [CategoryTheory.BraidedCategory C] [CategoryTheory.RigidCategory C] {D : Type u₂}
  [CategoryTheory.Category.{v₂, u₂} D] [CategoryTheory.MonoidalCategory D]
  [CategoryTheory.BraidedCategory D] [CategoryTheory.RigidCategory D] [TauCeti.BalancedCategory C]
  [TauCeti.BalancedCategory D] (F : CategoryTheory.Functor C D) [F.Braided] :
  F.IsPivotal ↔ F.IsBalanced
```

## Depends on

- [CategoryTheory.Functor.IsBalanced](categorytheory-functor-isbalanced.md)

## Proof depends on

- [CategoryTheory.Functor.isBalanced_iff_isPivotal](categorytheory-functor-isbalanced-iff-ispivotal.md)

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Functor.isPivotal_pivotalOfBalanced_iff`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Pivotal/Functor/Balanced.html#CategoryTheory.Functor.isPivotal_pivotalOfBalanced_iff).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Functor.isPivotal_pivotalOfBalanced_iff`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Pivotal/Functor/Balanced.html#CategoryTheory.Functor.isPivotal_pivotalOfBalanced_iff)
- [Source of `CategoryTheory.Functor.isPivotal_pivotalOfBalanced_iff` in TauCeti/CategoryTheory/Monoidal/Pivotal/Functor/Balanced.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/Monoidal/Pivotal/Functor/Balanced.lean#L97)
- [Tau Ceti roadmap status: Diagrammatic coherence for monoidal categories and duality](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DiagrammaticCoherence/STATUS.md)
