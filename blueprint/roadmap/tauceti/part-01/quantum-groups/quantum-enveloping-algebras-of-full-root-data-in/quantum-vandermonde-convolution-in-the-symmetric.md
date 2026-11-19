---
declaration: theorem
origin: cited
lean: TauCeti.quantumBinomial_add_left_eq
statement: formalized
proof: formalized
---

# Quantum Vandermonde convolution, in the symmetric normalization

The exponent is
`n*a-m*b`, and the formula remains valid at roots of unity because it involves no division
by quantum integers.

```lean
TauCeti.quantumBinomial_add_left_eq.{u_1} {K : Type u_1} [Semifield K] {q : K} (hq : q ≠ 0)
  (m n r : ℕ) :
  TauCeti.quantumBinomial q (m + n) r =
    ∑ p ∈ Finset.HasAntidiagonal.antidiagonal r,
      q ^ (↑n * ↑p.1 - ↑m * ↑p.2) * TauCeti.quantumBinomial q m p.1 *
        TauCeti.quantumBinomial q n p.2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.quantumBinomial_add_left_eq`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/QuantumInteger/Vandermonde.html#TauCeti.quantumBinomial_add_left_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.quantumBinomial_add_left_eq`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/QuantumInteger/Vandermonde.html#TauCeti.quantumBinomial_add_left_eq)
- [Source of `TauCeti.quantumBinomial_add_left_eq` in TauCeti/QuantumGroups/QuantumInteger/Vandermonde.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/QuantumGroups/QuantumInteger/Vandermonde.lean#L53)
- [Tau Ceti roadmap status: Quantum enveloping algebras of full root data, integral forms and quantum Frobenius](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/QuantumEnvelopingAlgebras/STATUS.md)
