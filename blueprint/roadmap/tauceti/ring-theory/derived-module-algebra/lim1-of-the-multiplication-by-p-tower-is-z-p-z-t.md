---
declaration: def
origin: cited
lean: TauCeti.ModuleTower.limOneMultiplicationTowerEquiv
statement: formalized
---

# `lim¹` of the multiplication-by-`p` tower is `ℤ_[p] ⧸ ℤ`, the isomorphism being induced by the `p`-adic summation map `(aₙ) ↦ ∑ₙ pⁿ aₙ` (`limOneMultiplicationTowerEquiv_mk`)

```lean
TauCeti.ModuleTower.limOneMultiplicationTowerEquiv (p : ℕ) [Fact (Nat.Prime p)] :
  (TauCeti.ModuleTower.multiplicationTower ↑p).limOne ≃+ ℤ_[p] ⧸ (Int.castAddHom ℤ_[p]).range
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ModuleTower.limOneMultiplicationTowerEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/Tower/Padic.html#TauCeti.ModuleTower.limOneMultiplicationTowerEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.ModuleTower.limOneMultiplicationTowerEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/Tower/Padic.html#TauCeti.ModuleTower.limOneMultiplicationTowerEquiv)
- [Source of `TauCeti.ModuleTower.limOneMultiplicationTowerEquiv` in TauCeti/Algebra/Category/ModuleCat/Tower/Padic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Category/ModuleCat/Tower/Padic.lean#L139)
- [Tau Ceti roadmap status: Derived module algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DerivedModuleAlgebra/STATUS.md)
