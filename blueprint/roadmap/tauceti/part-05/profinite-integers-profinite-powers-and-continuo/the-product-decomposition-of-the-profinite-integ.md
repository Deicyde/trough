---
declaration: def
origin: cited
lean: TauCeti.zHat.ringEquivPiPadicInt
statement: formalized
---

# The product decomposition of the profinite integers

The ring homomorphism from
`Additive zHat` to `∀ ℓ : Nat.Primes, ℤ_[ℓ]` with components the `ℓ`-adic components
`zHat.component ℓ` is a ring isomorphism: injective by `zHat.ext_of_component` and surjective by
`zHat.exists_forall_component_eq`. It is a homeomorphism (`zHat.continuous_ringEquivPiPadicInt`,
`zHat.continuous_ringEquivPiPadicInt_symm`), so an isomorphism of topological rings.

```lean
TauCeti.zHat.ringEquivPiPadicInt.{u} :
  Additive ↑TauCeti.zHat.toProfinite.toTop ≃+* ((ℓ : Nat.Primes) → ℤ_[↑ℓ])
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.zHat.ringEquivPiPadicInt`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ZHat/Decomposition.html#TauCeti.zHat.ringEquivPiPadicInt).

## Sources

- [Tau Ceti documentation: `TauCeti.zHat.ringEquivPiPadicInt`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ZHat/Decomposition.html#TauCeti.zHat.ringEquivPiPadicInt)
- [Source of `TauCeti.zHat.ringEquivPiPadicInt` in TauCeti/Topology/Algebra/Group/Profinite/ZHat/Decomposition.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/ZHat/Decomposition.lean#L159)
- [Tau Ceti roadmap status: Profinite integers, profinite powers, and continuous automorphisms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ProfiniteArithmetic/STATUS.md)
