---
declaration: theorem
origin: cited
lean: MeromorphicOn.discCharacteristic_sub_discCharacteristic_inv
statement: formalized
proof: formalized
---

# Local First Main Inversion Identity (Calegari–Dimitrov–Tang, §6.1, eq. (6.1.4))

for
`f : ℂ → ℂ` meromorphic on `closedBall 0 r` and `0 < r`,
`discCharacteristic f r - discCharacteristic f⁻¹ r = log ‖meromorphicTrailingCoeffAt f 0‖`.
No global meromorphicity or centre regularity hypothesis is required; when
`meromorphicOrderAt f 0 ≠ ⊤`, `meromorphicTrailingCoeffAt f 0` is the nonzero leading Laurent
coefficient at `0`, while if `meromorphicOrderAt f 0 = ⊤` (`f = 0` away from a discrete set) both
sides vanish by totalization.

```lean
MeromorphicOn.discCharacteristic_sub_discCharacteristic_inv {f : ℂ → ℂ} {r : ℝ}
  (hf : MeromorphicOn f (Metric.closedBall 0 r)) (hr : 0 < r) :
  TauCeti.discCharacteristic f r - TauCeti.discCharacteristic f⁻¹ r =
    Real.log ‖meromorphicTrailingCoeffAt f 0‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Disc-local Jensen identity (Calegari–Dimitrov–Tang, §6.1, eq. (6.1.4))](../part-01/disc-local-jensen-identity-calegari-dimitrov-tan.md)

## Lean

Formalized in Tau Ceti as [`MeromorphicOn.discCharacteristic_sub_discCharacteristic_inv`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/ValueDistribution/Disc/Characteristic.html#MeromorphicOn.discCharacteristic_sub_discCharacteristic_inv).

## Sources

- [Tau Ceti documentation: `MeromorphicOn.discCharacteristic_sub_discCharacteristic_inv`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/ValueDistribution/Disc/Characteristic.html#MeromorphicOn.discCharacteristic_sub_discCharacteristic_inv)
- [Source of `MeromorphicOn.discCharacteristic_sub_discCharacteristic_inv` in TauCeti/Analysis/Complex/ValueDistribution/Disc/Characteristic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/ValueDistribution/Disc/Characteristic.lean#L285)
