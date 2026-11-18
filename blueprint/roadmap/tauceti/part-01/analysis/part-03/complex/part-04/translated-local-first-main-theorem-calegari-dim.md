---
declaration: theorem
origin: cited
lean: MeromorphicOn.abs_discCharacteristic_sub_discCharacteristic_one_div_sub_sub_log_le
statement: formalized
proof: formalized
---

# Translated local First Main Theorem (Calegari–Dimitrov–Tang, §6.1, eq. (6.1.3))

for
`f : ℂ → ℂ` meromorphic on `ball 0 R`, `a : ℂ`, and `0 < r < R` (in particular `R = 1` on the unit
disc `ball 0 1`),
`|discCharacteristic f r - discCharacteristic (fun z ↦ 1 / (f z - a)) r - log ‖c(f - a, 0)‖| ≤
  log⁺ ‖a‖ + log 2`,
where `c(f - a, 0) = meromorphicTrailingCoeffAt (fun z ↦ f z - a) 0` is the leading Laurent
coefficient of `f - a` at `0` (nonzero whenever `meromorphicOrderAt (fun z ↦ f z - a) 0 ≠ ⊤`, while
when `meromorphicOrderAt (fun z ↦ f z - a) 0 = ⊤` the bound also holds via `Real.log 0 = 0`).

```lean
MeromorphicOn.abs_discCharacteristic_sub_discCharacteristic_one_div_sub_sub_log_le {f : ℂ → ℂ}
  {r R : ℝ} (hf : MeromorphicOn f (Metric.ball 0 R)) (a : ℂ) (hr : 0 < r) (hrR : r < R) :
  |TauCeti.discCharacteristic f r - TauCeti.discCharacteristic (fun z => 1 / (f z - a)) r -
        Real.log ‖meromorphicTrailingCoeffAt (fun z => f z - a) 0‖| ≤
    ‖a‖.posLog + Real.log 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Local First Main Inversion Identity (Calegari–Dimitrov–Tang, §6.1, eq. (6.1.4))](../part-03/local-first-main-inversion-identity-calegari-dim.md)

## Lean

Formalized in Tau Ceti as [`MeromorphicOn.abs_discCharacteristic_sub_discCharacteristic_one_div_sub_sub_log_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/ValueDistribution/Disc/Characteristic.html#MeromorphicOn.abs_discCharacteristic_sub_discCharacteristic_one_div_sub_sub_log_le).

## Sources

- [Tau Ceti documentation: `MeromorphicOn.abs_discCharacteristic_sub_discCharacteristic_one_div_sub_sub_log_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/ValueDistribution/Disc/Characteristic.html#MeromorphicOn.abs_discCharacteristic_sub_discCharacteristic_one_div_sub_sub_log_le)
- [Source of `MeromorphicOn.abs_discCharacteristic_sub_discCharacteristic_one_div_sub_sub_log_le` in TauCeti/Analysis/Complex/ValueDistribution/Disc/Characteristic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/ValueDistribution/Disc/Characteristic.lean#L441)
