---
declaration: def
origin: cited
lean: TauCeti.CategoryTheory.strictMonoCechComplexHomotopyEquiv
statement: formalized
---

# The ordered Čech complex is homotopy equivalent to the Čech complex

For a family of
objects of a thin category (for instance open subsets of a topological space) indexed by a
linearly ordered type, restricting Čech cochains to the strictly increasing tuples
(`toStrictMonoCechComplex`) is a homotopy equivalence `Č(U, P) ≃ Čₒ(U, P)`, with homotopy inverse
the alternating extension (`fromStrictMonoCechComplex`). No covering condition, finiteness or
coefficient hypothesis beyond preadditivity is needed, and no division by factorials occurs.

Thinness cannot be dropped: in a category with products, the Čech complex of the family with
the single member `X` has the terms `P(X × ⋯ × X)`, whereas its ordered Čech complex is `P(X)`
in degree `0`.

```lean
TauCeti.CategoryTheory.strictMonoCechComplexHomotopyEquiv.{w, v, v', u, u'} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Limits.HasFiniteProducts C] {A : Type u'}
  [CategoryTheory.Category.{v', u'} A] [CategoryTheory.Preadditive A]
  [CategoryTheory.Limits.HasProducts A] {ι : Type w} [LinearOrder ι] (U : ι → C) [Quiver.IsThin C]
  (P : CategoryTheory.Functor Cᵒᵖ A) :
  HomotopyEquiv ((CategoryTheory.cechComplexFunctor U).obj P)
    ((TauCeti.CategoryTheory.strictMonoCechComplexFunctor U).obj P)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CategoryTheory.strictMonoCechComplexHomotopyEquiv`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Sites/SheafCohomology/Cech/Ordered/HomotopyEquiv.html#TauCeti.CategoryTheory.strictMonoCechComplexHomotopyEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.CategoryTheory.strictMonoCechComplexHomotopyEquiv`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Sites/SheafCohomology/Cech/Ordered/HomotopyEquiv.html#TauCeti.CategoryTheory.strictMonoCechComplexHomotopyEquiv)
- [Source of `TauCeti.CategoryTheory.strictMonoCechComplexHomotopyEquiv` in TauCeti/CategoryTheory/Sites/SheafCohomology/Cech/Ordered/HomotopyEquiv.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/Sites/SheafCohomology/Cech/Ordered/HomotopyEquiv.lean#L738)
- [Tau Ceti roadmap status: Topological sheaf cohomology and native comparison maps](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TopologicalSheafCohomology/STATUS.md)
