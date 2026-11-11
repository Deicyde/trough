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
- [Source of `TauCeti.qInt_two_mul_cos_pos_of_le_floor` in TauCeti/QuantumGroups/QuantumInteger/Real.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/QuantumGroups/QuantumInteger/Real.lean#L76)
- [Tau Ceti roadmap status: Subfactors, Jones index and planar standard invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Subfactors/STATUS.md)
