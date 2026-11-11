---
declaration: theorem
origin: cited
lean: TauCeti.Multiquadratic.exists_prime_gt_forall_primeDiscriminantCharFun_eq
statement: formalized
proof: formalized
---

# Dirichlet's theorem for prime-discriminant characters

Let `s` be a finite set of prime
discriminants, at most one of them even, let `ε` assign a sign to each, and let `N` be any bound.
Then some odd prime `q > N` has `χ_P(q) = ε P` for every `P ∈ s`. In particular there are
infinitely many such primes.

```lean
TauCeti.Multiquadratic.exists_prime_gt_forall_primeDiscriminantCharFun_eq {s : Finset ℤ}
  (hs : ∀ P ∈ s, TauCeti.Multiquadratic.IsPrimeDiscriminant P)
  (heven :
    ∀ P ∈ s,
      ∀ Q ∈ s,
        TauCeti.Multiquadratic.IsEvenPrimeDiscriminant P →
          TauCeti.Multiquadratic.IsEvenPrimeDiscriminant Q → P = Q)
  (ε : ℤ → ℤˣ) (N : ℕ) :
  ∃ q,
    N < q ∧
      Nat.Prime q ∧ q ≠ 2 ∧ ∀ P ∈ s, TauCeti.Multiquadratic.primeDiscriminantCharFun P ↑q = ↑(ε P)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Multiquadratic.exists_prime_gt_forall_primeDiscriminantCharFun_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Multiquadratic/Legendre/PrimeDiscriminant/Dirichlet/Basic.html#TauCeti.Multiquadratic.exists_prime_gt_forall_primeDiscriminantCharFun_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.Multiquadratic.exists_prime_gt_forall_primeDiscriminantCharFun_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Multiquadratic/Legendre/PrimeDiscriminant/Dirichlet/Basic.html#TauCeti.Multiquadratic.exists_prime_gt_forall_primeDiscriminantCharFun_eq)
- [Source of `TauCeti.Multiquadratic.exists_prime_gt_forall_primeDiscriminantCharFun_eq` in TauCeti/NumberTheory/Multiquadratic/Legendre/PrimeDiscriminant/Dirichlet/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Multiquadratic/Legendre/PrimeDiscriminant/Dirichlet/Basic.lean#L187)
