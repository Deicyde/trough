---
declaration: theorem
origin: cited
lean: TauCeti.exists_qInt_eq_zero_iff
statement: formalized
proof: formalized
---

# The root-of-unity dictionary

Over an algebraically closed field of characteristic zero,
some quantum integer `[n]` with `n ≥ 1` vanishes at `δ` iff `δ = ζ + ζ⁻¹` for a root of unity
`ζ ≠ ±1`. The exclusions are needed: `[n] = n` at `δ = 2` and `[n] = (-1)^(n+1) n` at `δ = -2`
(`qInt_two_left`, `qInt_neg_two_left`) never vanish in characteristic zero.

```lean
TauCeti.exists_qInt_eq_zero_iff.{u_1} (K : Type u_1) [Field K] [IsAlgClosed K] [CharZero K]
  (δ : K) :
  (∃ n, 1 ≤ n ∧ TauCeti.qInt K δ n = 0) ↔
    ∃ ζ, (∃ m, 0 < m ∧ ζ ^ m = 1) ∧ ζ ≠ 1 ∧ ζ ≠ -1 ∧ δ = ↑ζ + ↑ζ⁻¹
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_qInt_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/QuantumInteger/RootOfUnity.html#TauCeti.exists_qInt_eq_zero_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_qInt_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/QuantumInteger/RootOfUnity.html#TauCeti.exists_qInt_eq_zero_iff)
- [Source of `TauCeti.exists_qInt_eq_zero_iff` in TauCeti/QuantumGroups/QuantumInteger/RootOfUnity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/QuantumGroups/QuantumInteger/RootOfUnity.lean#L85)
- [Tau Ceti roadmap status: Temperley–Lieb diagrams, categories, and algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TemperleyLieb/STATUS.md)
