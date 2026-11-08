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
- [Source of `Int.IsFundamentalDiscr.existsUnique_finset_primeDiscriminant` in TauCeti/NumberTheory/Multiquadratic/FundamentalDiscriminant/Factorization.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Multiquadratic/FundamentalDiscriminant/Factorization.lean#L253)
- [Tau Ceti roadmap status: Multiquadratic fields and genus theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/Multiquadratic/STATUS.md)
