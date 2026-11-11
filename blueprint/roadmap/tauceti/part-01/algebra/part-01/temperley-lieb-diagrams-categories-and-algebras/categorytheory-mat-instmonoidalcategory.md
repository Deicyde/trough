---
declaration: instance
origin: cited
lean: CategoryTheory.Mat_.instMonoidalCategory
statement: formalized
---

# CategoryTheory.Mat\_.instMonoidalCategory

The matrix category of a monoidal preadditive category is monoidal, with the Kronecker product
of matrices as tensor product.

```lean
CategoryTheory.Mat_.instMonoidalCategory.{v, u} {C : Type u} [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.Preadditive C] [CategoryTheory.MonoidalCategory C]
  [CategoryTheory.MonoidalPreadditive C] : CategoryTheory.MonoidalCategory (CategoryTheory.Mat_ C)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Mat_.instMonoidalCategory`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Envelope/Mat/Basic.html#CategoryTheory.Mat_.instMonoidalCategory).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Mat_.instMonoidalCategory`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Envelope/Mat/Basic.html#CategoryTheory.Mat_.instMonoidalCategory)
- [Source of `CategoryTheory.Mat_.instMonoidalCategory` in TauCeti/CategoryTheory/Monoidal/Envelope/Mat/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Monoidal/Envelope/Mat/Basic.lean#L193)
- [Tau Ceti roadmap status: Temperley–Lieb diagrams, categories, and algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TemperleyLieb/STATUS.md)
