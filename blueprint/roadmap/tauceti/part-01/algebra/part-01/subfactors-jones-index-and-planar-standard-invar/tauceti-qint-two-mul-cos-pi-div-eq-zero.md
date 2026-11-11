---
declaration: theorem
origin: cited
lean: TauCeti.qInt_two_mul_cos_pi_div_eq_zero
statement: formalized
proof: formalized
---

# TauCeti.qInt_two_mul_cos_pi_div_eq_zero

At the discrete cosine parameter `2 * cos (π / m)`, the quantum integer `[m]` vanishes.

```lean
TauCeti.qInt_two_mul_cos_pi_div_eq_zero {m : ℕ} (hm : 2 ≤ m) :
  TauCeti.qInt ℝ (2 * Real.cos (Real.pi / ↑m)) m = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.qInt_two_mul_cos_pi_div_eq_zero`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/QuantumInteger/Real.html#TauCeti.qInt_two_mul_cos_pi_div_eq_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.qInt_two_mul_cos_pi_div_eq_zero`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/QuantumInteger/Real.html#TauCeti.qInt_two_mul_cos_pi_div_eq_zero)
- [Source of `TauCeti.qInt_two_mul_cos_pi_div_eq_zero` in TauCeti/QuantumGroups/QuantumInteger/Real.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/QuantumGroups/QuantumInteger/Real.lean#L58)
- [Tau Ceti roadmap status: Subfactors, Jones index and planar standard invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Subfactors/STATUS.md)
