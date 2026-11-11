---
declaration: def
origin: cited
lean: TauCeti.UqSl2.clebschGordanEquiv
statement: formalized
---

# TauCeti.UqSl2.clebschGordanEquiv

The quantum Clebsch–Gordan decomposition: at a generic parameter,
`L_m^ε ⊗ L_n^δ ≃ ⊕_(j = 0)^(min m n) L_(m + n - 2j)^(εδ)` as `UqSl2 q`-modules, with the `j`-th
summand embedded by `clebschGordanInclusion`.

```lean
TauCeti.UqSl2.clebschGordanEquiv {q : ℂ} [Fact (q ≠ 0)] {m n : ℕ} {ε δ : ℤˣ}
  (hq : TauCeti.IsGenericQuantumParameter q) :
  ((j : Fin (min m n + 1)) →
      TauCeti.UqSl2.LadderModule q (m + n - 2 * ↑j) (ε * δ)) ≃ₗ[TauCeti.UqSl2 q]
    TauCeti.BialgebraModule.Tensor ℂ (TauCeti.UqSl2 q) (TauCeti.UqSl2.LadderModule q m ε)
      (TauCeti.UqSl2.LadderModule q n δ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.UqSl2.clebschGordanEquiv`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/ClebschGordan/Basic.html#TauCeti.UqSl2.clebschGordanEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.UqSl2.clebschGordanEquiv`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/ClebschGordan/Basic.html#TauCeti.UqSl2.clebschGordanEquiv)
- [Source of `TauCeti.UqSl2.clebschGordanEquiv` in TauCeti/QuantumGroups/UqSl2/ClebschGordan/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/QuantumGroups/UqSl2/ClebschGordan/Basic.lean#L393)
- [Tau Ceti roadmap status: Quantum groups: compact reconstruction and generic rank-one representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/QuantumGroups/STATUS.md)
