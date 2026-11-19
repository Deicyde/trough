---
declaration: theorem
origin: cited
lean: TauCeti.qInt_two_mul_cos_floor_add_one_neg
statement: formalized
proof: formalized
---

# TauCeti.qInt_two_mul_cos_floor_add_one_neg

The index immediately after `⌊π / θ⌋` has negative weight for `0 < θ < π`.
Together with `qInt_two_mul_cos_pos_of_le_floor`, this identifies the first negative index
when `π / θ` is not an integer.

```lean
TauCeti.qInt_two_mul_cos_floor_add_one_neg {θ : ℝ} (hθ : 0 < θ) (hθπ : θ < Real.pi) :
  TauCeti.qInt ℝ (2 * Real.cos θ) (⌊Real.pi / θ⌋₊ + 1) < 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.qInt_two_mul_cos_floor_add_one_neg`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/QuantumInteger/Real.html#TauCeti.qInt_two_mul_cos_floor_add_one_neg).

## Sources

- [Tau Ceti documentation: `TauCeti.qInt_two_mul_cos_floor_add_one_neg`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/QuantumInteger/Real.html#TauCeti.qInt_two_mul_cos_floor_add_one_neg)
- [Source of `TauCeti.qInt_two_mul_cos_floor_add_one_neg` in TauCeti/QuantumGroups/QuantumInteger/Real.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/QuantumGroups/QuantumInteger/Real.lean#L84)
- [Tau Ceti roadmap status: Subfactors, Jones index and planar standard invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Subfactors/STATUS.md)
