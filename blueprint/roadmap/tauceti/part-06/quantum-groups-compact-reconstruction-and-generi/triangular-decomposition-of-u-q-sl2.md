---
declaration: def
origin: cited
lean: TauCeti.UqSl2.triangularEquiv
statement: formalized
---

# Triangular decomposition of `U_q(sl₂)`

Multiplication
`p ⊗ r ⊗ s ↦ p(F) * r(K) * s(E)` is a linear isomorphism
`ℂ[X] ⊗ ℂ[T, T⁻¹] ⊗ ℂ[X] ≃ UqSl2 q`, that is, `U⁻ ⊗ U⁰ ⊗ U⁺ ≃ U_q(sl₂)`.  It sends the
tensor product of monomial bases to the PBW basis.

```lean
TauCeti.UqSl2.triangularEquiv (q : ℂ) [Fact (q ≠ 0)] :
  TensorProduct ℂ (Polynomial ℂ) (TensorProduct ℂ (LaurentPolynomial ℂ) (Polynomial ℂ)) ≃ₗ[ℂ]
    TauCeti.UqSl2 q
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.OreExtension](tauceti-oreextension.md)
- [TauCeti.UqSl2.pbwBasis](tauceti-uqsl2-pbwbasis.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.UqSl2.triangularEquiv`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/Triangular.html#TauCeti.UqSl2.triangularEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.UqSl2.triangularEquiv`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/Triangular.html#TauCeti.UqSl2.triangularEquiv)
- [Source of `TauCeti.UqSl2.triangularEquiv` in TauCeti/QuantumGroups/UqSl2/Triangular.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/QuantumGroups/UqSl2/Triangular.lean#L119)
- [Tau Ceti roadmap status: Quantum groups: compact reconstruction and generic rank-one representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/QuantumGroups/STATUS.md)
