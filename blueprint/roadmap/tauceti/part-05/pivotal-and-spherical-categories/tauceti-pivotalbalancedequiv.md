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
- [Source of `TauCeti.pivotalBalancedEquiv` in TauCeti/CategoryTheory/Monoidal/Pivotal/OfBalanced.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/CategoryTheory/Monoidal/Pivotal/OfBalanced.lean#L112)
- [Tau Ceti roadmap status: Pivotal and spherical categories](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PivotalSpherical/STATUS.md)
