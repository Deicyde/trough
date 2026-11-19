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
- [Source of `TauCeti.zHat.unitsEquivPiPadicInt` in TauCeti/Topology/Algebra/Group/Profinite/ZHat/Units.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Algebra/Group/Profinite/ZHat/Units.lean#L79)
- [Tau Ceti roadmap status: Profinite integers, profinite powers, and continuous automorphisms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/ProfiniteArithmetic/STATUS.md)
