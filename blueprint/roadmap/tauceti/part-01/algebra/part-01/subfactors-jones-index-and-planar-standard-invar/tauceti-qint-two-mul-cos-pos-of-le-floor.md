---
declaration: theorem
origin: cited
lean: TauCeti.qInt_two_mul_cos_pos_of_le_floor
statement: formalized
proof: formalized
---

# TauCeti.qInt_two_mul_cos_pos_of_le_floor

For a nonintegral `π / θ`, every positive index at most its floor has positive weight.

```lean
TauCeti.qInt_two_mul_cos_pos_of_le_floor {θ : ℝ} (hθ : 0 < θ)
  (hfloor : ↑⌊Real.pi / θ⌋₊ < Real.pi / θ) {n : ℕ} (hn : 0 < n) (hnfloor : n ≤ ⌊Real.pi / θ⌋₊) :
  0 < TauCeti.qInt ℝ (2 * Real.cos θ) n
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.qInt_two_mul_cos_pos_of_le_floor`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/QuantumInteger/Real.html#TauCeti.qInt_two_mul_cos_pos_of_le_floor).

## Sources

- [Tau Ceti documentation: `TauCeti.qInt_two_mul_cos_pos_of_le_floor`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/QuantumInteger/Real.html#TauCeti.qInt_two_mul_cos_pos_of_le_floor)
- [Source of `TauCeti.qInt_two_mul_cos_pos_of_le_floor` in TauCeti/QuantumGroups/QuantumInteger/Real.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/QuantumGroups/QuantumInteger/Real.lean#L76)
- [Tau Ceti roadmap status: Subfactors, Jones index and planar standard invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Subfactors/STATUS.md)
