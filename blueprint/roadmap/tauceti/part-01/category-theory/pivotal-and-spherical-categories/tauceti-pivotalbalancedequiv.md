---
declaration: def
origin: cited
lean: TauCeti.pivotalBalancedEquiv
statement: formalized
---

# TauCeti.pivotalBalancedEquiv

Pivotal structures on a braided rigid category correspond to balanced structures via
`θ_X = φ_X ≫ u_X⁻¹`, with inverse `φ_X = θ_X ≫ u_X`.

```lean
TauCeti.pivotalBalancedEquiv.{v, u} (C : Type u) [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C]
  [CategoryTheory.RigidCategory C] : TauCeti.PivotalCategory C ≃ TauCeti.BalancedCategory C
```

## Depends on

- [TauCeti.BalancedCategory](tauceti-balancedcategory.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.pivotalBalancedEquiv`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Pivotal/OfBalanced.html#TauCeti.pivotalBalancedEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.pivotalBalancedEquiv`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Pivotal/OfBalanced.html#TauCeti.pivotalBalancedEquiv)
- [Source of `TauCeti.pivotalBalancedEquiv` in TauCeti/CategoryTheory/Monoidal/Pivotal/OfBalanced.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Monoidal/Pivotal/OfBalanced.lean#L112)
- [Tau Ceti roadmap status: Pivotal and spherical categories](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PivotalSpherical/STATUS.md)
