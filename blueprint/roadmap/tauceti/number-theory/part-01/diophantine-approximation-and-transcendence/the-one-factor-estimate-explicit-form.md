---
declaration: theorem
origin: cited
lean: TauCeti.log_normalizedValuationWithZero_zpow_sub_one_le
statement: formalized
proof: formalized
---

# The one-factor estimate, explicit form

Let `x ∈ Kˣ` have a power `x ^ M ≠ 1` in a
positive-depth step `U(K,i)`, and let `b` be an integer with `(|b| : K) ≠ 0` such that
`v_K(ℓ) < (ℓ - 1) * i` for every prime `ℓ ∣ b`. Then

`v_K(x ^ b - 1) ≤ v_K(x ^ M - 1) + v_K(|b|)`.

```lean
TauCeti.log_normalizedValuationWithZero_zpow_sub_one_le.{u_1} {K : Type u_1} [Field K]
  [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K] {x : Kˣ} {M i : ℕ}
  (hi0 : i ≠ 0) (hM : x ^ M ∈ TauCeti.unitFiltration K i) (hM1 : x ^ M ≠ 1) {b : ℤ}
  (hb : ↑b.natAbs ≠ 0)
  (hi :
    ∀ (ℓ : ℕ),
      Nat.Prime ℓ →
        ∀ (hℓK : ↑ℓ ≠ 0), ℓ ∣ b.natAbs → TauCeti.natCastValuation K ℓ hℓK < (ℓ - 1) * i) :
  ((TauCeti.normalizedValuationWithZero K) (↑x ^ b - 1)).log ≤
    ((TauCeti.normalizedValuationWithZero K) (↑x ^ M - 1)).log +
      ↑(TauCeti.natCastValuation K b.natAbs hb)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.log_normalizedValuationWithZero_zpow_sub_one_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/UnitFiltration/Pow/SubOne.html#TauCeti.log_normalizedValuationWithZero_zpow_sub_one_le).

## Sources

- [Tau Ceti documentation: `TauCeti.log_normalizedValuationWithZero_zpow_sub_one_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/UnitFiltration/Pow/SubOne.html#TauCeti.log_normalizedValuationWithZero_zpow_sub_one_le)
- [Source of `TauCeti.log_normalizedValuationWithZero_zpow_sub_one_le` in TauCeti/NumberTheory/LocalField/UnitFiltration/Pow/SubOne.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/UnitFiltration/Pow/SubOne.lean#L107)
- [Tau Ceti roadmap status: Diophantine approximation and transcendence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DiophantineApproximationAndTranscendence/STATUS.md)
