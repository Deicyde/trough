---
declaration: theorem
origin: cited
lean: Int.IsFundamentalDiscr.existsUnique_finset_primeDiscriminant
statement: formalized
proof: formalized
---

# Unique prime-discriminant factorization of a fundamental discriminant

Every fundamental
discriminant is the product of a unique finite set of prime discriminants.

```lean
Int.IsFundamentalDiscr.existsUnique_finset_primeDiscriminant {D : ℤ} (hD : D.IsFundamentalDiscr) :
  ∃! s, (∀ P ∈ s, TauCeti.Multiquadratic.IsPrimeDiscriminant P) ∧ ∏ P ∈ s, P = D
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Int.IsFundamentalDiscr.existsUnique_finset_primeDiscriminant`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Multiquadratic/FundamentalDiscriminant/Factorization.html#Int.IsFundamentalDiscr.existsUnique_finset_primeDiscriminant).

## Sources

- [Tau Ceti documentation: `Int.IsFundamentalDiscr.existsUnique_finset_primeDiscriminant`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Multiquadratic/FundamentalDiscriminant/Factorization.html#Int.IsFundamentalDiscr.existsUnique_finset_primeDiscriminant)
- [Source of `Int.IsFundamentalDiscr.existsUnique_finset_primeDiscriminant` in TauCeti/NumberTheory/Multiquadratic/FundamentalDiscriminant/Factorization.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Multiquadratic/FundamentalDiscriminant/Factorization.lean#L255)
- [Tau Ceti roadmap status: Multiquadratic fields and genus theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/Multiquadratic/STATUS.md)
