---
declaration: def
origin: cited
lean: TauCeti.zHat.unitsEquivPiPadicInt
statement: formalized
---

# The unit-group decomposition of the profinite integers

The product decomposition
`Additive zHat ≃+* ∀ ℓ, ℤ_[ℓ]` restricts to an isomorphism of topological groups on units.

```lean
TauCeti.zHat.unitsEquivPiPadicInt.{u} :
  (Additive ↑TauCeti.zHat.toProfinite.toTop)ˣ ≃ₜ* ((ℓ : Nat.Primes) → ℤ_[↑ℓ]ˣ)
```

## Depends on

- [The product decomposition of the profinite integers](the-product-decomposition-of-the-profinite-integ.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.zHat.unitsEquivPiPadicInt`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ZHat/Units.html#TauCeti.zHat.unitsEquivPiPadicInt).

## Sources

- [Tau Ceti documentation: `TauCeti.zHat.unitsEquivPiPadicInt`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ZHat/Units.html#TauCeti.zHat.unitsEquivPiPadicInt)
- [Source of `TauCeti.zHat.unitsEquivPiPadicInt` in TauCeti/Topology/Algebra/Group/Profinite/ZHat/Units.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/ZHat/Units.lean#L77)
- [Tau Ceti roadmap status: Profinite integers, profinite powers, and continuous automorphisms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ProfiniteArithmetic/STATUS.md)
