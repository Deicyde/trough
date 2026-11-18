---
declaration: theorem
origin: cited
lean: TauCeti.ordinaryHypergeometric_neg_nat_one
statement: formalized
proof: formalized
---

# Chu–Vandermonde (DLMF 15.4.24)

`₂F₁(−n, b; c; 1) = (c − b)ₙ / (c)ₙ` when `(c)ₙ ≠ 0`.

```lean
TauCeti.ordinaryHypergeometric_neg_nat_one.{u_1} {K : Type u_1} [Field K] [CharZero K]
  [TopologicalSpace K] [IsTopologicalRing K] (n : ℕ) (b : K) {c : K}
  (hc : Polynomial.eval c (ascPochhammer K n) ≠ 0) :
  ₂F₁ (-↑n) b c 1 =
    Polynomial.eval (c - b) (ascPochhammer K n) / Polynomial.eval c (ascPochhammer K n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Chu–Vandermonde identity in Pochhammer form](../../../ring-theory/part-02/polynomial/the-chu-vandermonde-identity-in-pochhammer-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ordinaryHypergeometric_neg_nat_one`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Hypergeometric/ChuVandermonde.html#TauCeti.ordinaryHypergeometric_neg_nat_one).

## Sources

- [Tau Ceti documentation: `TauCeti.ordinaryHypergeometric_neg_nat_one`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Hypergeometric/ChuVandermonde.html#TauCeti.ordinaryHypergeometric_neg_nat_one)
- [Source of `TauCeti.ordinaryHypergeometric_neg_nat_one` in TauCeti/Analysis/SpecialFunctions/Hypergeometric/ChuVandermonde.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Hypergeometric/ChuVandermonde.lean#L49)
