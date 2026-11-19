---
declaration: theorem
origin: cited
lean: TauCeti.quantumFactorial_ne_zero_iff_lt
statement: formalized
proof: formalized
---

# Quantum factorials at a root of unity

if `q²` is a primitive `ℓ`-th root of unity with
`ℓ > 0`, then `[n]_q! ≠ 0` exactly when `n < ℓ`.

```lean
TauCeti.quantumFactorial_ne_zero_iff_lt.{u_1} {K : Type u_1} [Field K] {q : K} {ℓ : ℕ}
  (h : IsPrimitiveRoot (q ^ 2) ℓ) (hℓ : 0 < ℓ) {n : ℕ} : TauCeti.quantumFactorial q n ≠ 0 ↔ n < ℓ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.quantumFactorial_ne_zero_iff_lt`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/QuantumInteger/Factorial.html#TauCeti.quantumFactorial_ne_zero_iff_lt).

## Sources

- [Tau Ceti documentation: `TauCeti.quantumFactorial_ne_zero_iff_lt`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/QuantumInteger/Factorial.html#TauCeti.quantumFactorial_ne_zero_iff_lt)
- [Source of `TauCeti.quantumFactorial_ne_zero_iff_lt` in TauCeti/QuantumGroups/QuantumInteger/Factorial.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/QuantumGroups/QuantumInteger/Factorial.lean#L154)
- [Tau Ceti roadmap status: Quantum enveloping algebras of full root data, integral forms and quantum Frobenius](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/QuantumEnvelopingAlgebras/STATUS.md)
