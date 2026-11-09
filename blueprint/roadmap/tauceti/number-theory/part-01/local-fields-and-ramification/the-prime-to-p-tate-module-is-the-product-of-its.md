---
declaration: def
origin: cited
lean: TauCeti.PrimeToPTateModule.continuousMulEquivPiPadicTateTwist
statement: formalized
---

# The prime-to-`p` Tate module is the product of its `ℓ`-adic components

the
`ℓ`-adic components `toPadicTateTwist`, over all primes `ℓ` prime to `p`, form an isomorphism of
topological groups `ℤ̂^{(p')}(1) ≃ₜ* ∏_{ℓ ∤ p} ℤ_ℓ(1)`. It holds for every commutative monoid `E`,
by the Chinese remainder theorem at each level `μ_m(E)`.

```lean
TauCeti.PrimeToPTateModule.continuousMulEquivPiPadicTateTwist.{u_1} (p : ℕ) (E : Type u_1)
  [CommMonoid E] :
  TauCeti.PrimeToPTateModule p E ≃ₜ*
    ((ℓ : { ℓ // Nat.Prime ℓ ∧ ℓ.Coprime p }) → Multiplicative (TauCeti.PadicTateTwist (↑ℓ) E))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PrimeToPTateModule.continuousMulEquivPiPadicTateTwist`](https://taucetiproject.org/docs/TauCeti/RingTheory/RootsOfUnity/PadicTateTwist.html#TauCeti.PrimeToPTateModule.continuousMulEquivPiPadicTateTwist).

## Sources

- [Tau Ceti documentation: `TauCeti.PrimeToPTateModule.continuousMulEquivPiPadicTateTwist`](https://taucetiproject.org/docs/TauCeti/RingTheory/RootsOfUnity/PadicTateTwist.html#TauCeti.PrimeToPTateModule.continuousMulEquivPiPadicTateTwist)
- [Source of `TauCeti.PrimeToPTateModule.continuousMulEquivPiPadicTateTwist` in TauCeti/RingTheory/RootsOfUnity/PadicTateTwist.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/RootsOfUnity/PadicTateTwist.lean#L501)
- [Tau Ceti roadmap status: Local fields and ramification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/LocalFieldsRamification/STATUS.md)
