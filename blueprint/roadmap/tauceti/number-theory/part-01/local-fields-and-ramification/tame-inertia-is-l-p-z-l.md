---
declaration: theorem
origin: cited
lean: TauCeti.nonempty_continuousMulEquiv_piPadicInt
statement: formalized
proof: formalized
---

# Tame inertia is `∏_{ℓ ≠ p} ℤ_ℓ`

the tame inertia group `I_K/P_K` is isomorphic, as a
topological group, to the product of the additive groups of `ℓ`-adic integers over the primes `ℓ`
different from the residue characteristic `p`. Up to a choice of an isomorphism `ℤ_ℓ(1) ≃ ℤ_ℓ` for
each `ℓ` (`TauCeti.PadicTateTwist.nonempty_continuousAddEquiv`), it is the tame character
`I_K/P_K ≃ ℤ̂^{(p')}(1)` (`TauCeti.quotientWildInertiaSubgroupEquiv`) followed by the
decomposition of `ℤ̂^{(p')}(1)` into its `ℓ`-adic components
(`TauCeti.PrimeToPTateModule.continuousMulEquivPiPadicTateTwist`).

```lean
TauCeti.nonempty_continuousMulEquiv_piPadicInt.{u_1} (K : Type u_1) [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] :
  Nonempty
    (↥(TauCeti.inertiaSubgroup K) ⧸
        (TauCeti.wildInertiaSubgroup K).subgroupOf (TauCeti.inertiaSubgroup K) ≃ₜ*
      Multiplicative
        ((ℓ :
            { ℓ // ↑ℓ ≠ ringChar (IsLocalRing.ResidueField ↥(ValuativeRel.valuation K).integer) }) →
          ℤ_[↑↑ℓ]))
```

## Depends on

- [The wild inertia subgroup `P_K` of the absolute Galois group of a nonarchimedean local field `K`](the-wild-inertia-subgroup-p-k-of-the-absolute-ga.md)

## Proof depends on

- [The prime-to-`p` Tate module is the product of its `ℓ`-adic components](the-prime-to-p-tate-module-is-the-product-of-its.md)
- [Tame inertia is the prime-to-`p` Tate module](tame-inertia-is-the-prime-to-p-tate-module.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.nonempty_continuousMulEquiv_piPadicInt`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Tame/PadicCharacter.html#TauCeti.nonempty_continuousMulEquiv_piPadicInt).

## Sources

- [Tau Ceti documentation: `TauCeti.nonempty_continuousMulEquiv_piPadicInt`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Tame/PadicCharacter.html#TauCeti.nonempty_continuousMulEquiv_piPadicInt)
- [Source of `TauCeti.nonempty_continuousMulEquiv_piPadicInt` in TauCeti/NumberTheory/LocalField/Tame/PadicCharacter.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/Tame/PadicCharacter.lean#L184)
- [Tau Ceti roadmap status: Local fields and ramification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/LocalFieldsRamification/STATUS.md)
