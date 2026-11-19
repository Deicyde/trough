---
declaration: theorem
origin: cited
lean: MeromorphicOn.discCharacteristic_eq_circleAverage_add_circleAverage
statement: formalized
proof: formalized
---

# Disc-local Cartan's formula

for `f : ℂ → ℂ` meromorphic on `closedBall 0 r` and `0 < r`,
`discCharacteristic f r` is the sum of the unit-circle average of the `a`-point counting function
`discCounting (fun z ↦ (f z - a)⁻¹) r` and the radius-independent unit-circle average of
`log ‖meromorphicTrailingCoeffAt (f · - a) 0‖`.

```lean
MeromorphicOn.discCharacteristic_eq_circleAverage_add_circleAverage {f : ℂ → ℂ} {r : ℝ}
  (hf : MeromorphicOn f (Metric.closedBall 0 r)) (hr : 0 < r) :
  TauCeti.discCharacteristic f r =
    Real.circleAverage (fun a => TauCeti.discCounting (fun z => (f z - a)⁻¹) r) 0 1 +
      Real.circleAverage (fun a => Real.log ‖meromorphicTrailingCoeffAt (fun z => f z - a) 0‖) 0 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Disc-local Jensen identity (Calegari–Dimitrov–Tang, §6.1, eq. (6.1.4))](disc-local-jensen-identity-calegari-dimitrov-tan.md)

## Lean

Formalized in Tau Ceti as [`MeromorphicOn.discCharacteristic_eq_circleAverage_add_circleAverage`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/ValueDistribution/Disc/Characteristic.html#MeromorphicOn.discCharacteristic_eq_circleAverage_add_circleAverage).

## Sources

- [Tau Ceti documentation: `MeromorphicOn.discCharacteristic_eq_circleAverage_add_circleAverage`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/ValueDistribution/Disc/Characteristic.html#MeromorphicOn.discCharacteristic_eq_circleAverage_add_circleAverage)
- [Source of `MeromorphicOn.discCharacteristic_eq_circleAverage_add_circleAverage` in TauCeti/Analysis/Complex/ValueDistribution/Disc/Characteristic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/ValueDistribution/Disc/Characteristic.lean#L378)
