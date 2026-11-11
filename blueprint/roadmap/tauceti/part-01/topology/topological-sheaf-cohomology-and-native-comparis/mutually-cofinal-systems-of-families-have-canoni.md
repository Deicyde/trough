---
declaration: def
origin: cited
lean: TauCeti.CategoryTheory.cechCohomologyIso
statement: formalized
---

# Mutually cofinal systems of families have canonically isomorphic Čech cohomology

If every
member of each of two directed systems of families is refined by a member of the other, their
Čech cohomologies are isomorphic, naturally in the presheaf and compatibly with
`toCechCohomology` (`toCechCohomology_comp_cechCohomologyComparison`).

```lean
TauCeti.CategoryTheory.cechCohomologyIso.{w, t, t', v, v', u, u'} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Limits.HasFiniteProducts C] (A : Type u')
  [CategoryTheory.Category.{v', u'} A] [CategoryTheory.Preadditive A]
  [CategoryTheory.Limits.HasProducts A] [CategoryTheory.CategoryWithHomology A] {J : Type t}
  [Preorder J] (E : J → CategoryTheory.Limits.FormalCoproduct C)
  (hE : ∀ ⦃i j : J⦄, i ≤ j → Nonempty (E j ⟶ E i)) {K : Type t'} [Preorder K]
  (F : K → CategoryTheory.Limits.FormalCoproduct C) (hF : ∀ ⦃i j : K⦄, i ≤ j → Nonempty (F j ⟶ F i))
  (n : ℕ) [CategoryTheory.Limits.HasColimitsOfShape J A] [IsDirectedOrder J] [IsDirectedOrder K]
  [CategoryTheory.Limits.HasColimitsOfShape K A] (h : ∀ (j : J), ∃ k, Nonempty (F k ⟶ E j))
  (h' : ∀ (k : K), ∃ j, Nonempty (E j ⟶ F k)) :
  TauCeti.CategoryTheory.cechCohomology A E hE n ≅ TauCeti.CategoryTheory.cechCohomology A F hF n
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CategoryTheory.cechCohomologyIso`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Sites/SheafCohomology/Cech/Cofinal.html#TauCeti.CategoryTheory.cechCohomologyIso).

## Sources

- [Tau Ceti documentation: `TauCeti.CategoryTheory.cechCohomologyIso`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Sites/SheafCohomology/Cech/Cofinal.html#TauCeti.CategoryTheory.cechCohomologyIso)
- [Source of `TauCeti.CategoryTheory.cechCohomologyIso` in TauCeti/CategoryTheory/Sites/SheafCohomology/Cech/Cofinal.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Sites/SheafCohomology/Cech/Cofinal.lean#L165)
- [Tau Ceti roadmap status: Topological sheaf cohomology and native comparison maps](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TopologicalSheafCohomology/STATUS.md)
