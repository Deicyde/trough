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
- [Source of `TauCeti.zHat.unitsEquivPiPadicInt` in TauCeti/Topology/Algebra/Group/Profinite/ZHat/Units.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/Profinite/ZHat/Units.lean#L77)
- [Tau Ceti roadmap status: Profinite integers, profinite powers, and continuous automorphisms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/ProfiniteArithmetic/STATUS.md)
