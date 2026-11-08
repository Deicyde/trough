---
declaration: theorem
origin: cited
lean: PowerSeries.aeval_multiset_esymm_add_multiplicativeSequence
statement: formalized
proof: formalized
---

# The Whitney formula for roots

on the union of a family `s` of `n` roots and a family `t`
of `m` roots, `Kₖ` is the convolution of the values of the multiplicative sequence on `s` and
on `t`.

```lean
PowerSeries.aeval_multiset_esymm_add_multiplicativeSequence.{u_1, u_2} {R : Type u_1} [CommRing R]
  (Q : PowerSeries R) (n k : ℕ) {S : Type u_2} [CommSemiring S] [Algebra R S] {m : ℕ}
  (s t : Multiset S) (hs : s.card = n) (ht : t.card = m) :
  (MvPolynomial.aeval fun j => (s + t).esymm (↑j + 1)) (Q.multiplicativeSequence (n + m) k) =
    ∑ p ∈ Finset.HasAntidiagonal.antidiagonal k,
      (MvPolynomial.aeval fun j => s.esymm (↑j + 1)) (Q.multiplicativeSequence n p.1) *
        (MvPolynomial.aeval fun j => t.esymm (↑j + 1)) (Q.multiplicativeSequence m p.2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`PowerSeries.aeval_multiset_esymm_add_multiplicativeSequence`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/MultiplicativeSequence.html#PowerSeries.aeval_multiset_esymm_add_multiplicativeSequence).

## Sources

- [Tau Ceti documentation: `PowerSeries.aeval_multiset_esymm_add_multiplicativeSequence`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/MultiplicativeSequence.html#PowerSeries.aeval_multiset_esymm_add_multiplicativeSequence)
- [Source of `PowerSeries.aeval_multiset_esymm_add_multiplicativeSequence` in TauCeti/RingTheory/PowerSeries/MultiplicativeSequence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/PowerSeries/MultiplicativeSequence.lean#L179)
