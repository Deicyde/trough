---
declaration: theorem
origin: cited
lean: OeisA46969.conjecture1, OeisA46969.conjecture2
statement: formalized
---

# Denominators of coefficients in Stirling's expansion for $\log(\Gamma(z))$

> The $n$-th term is the denominator of $\frac{B_{2n}}{2n(2n-1)}$ where $B_{2n}$ is the $2n$-th
> Bernoulli number.
>
> *References:*
> - [A046969](https://oeis.org/A046969)

*Quoted from [FormalConjectures/OEIS/46969.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/46969.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 6 test statements and 3 API statements, counted here but not shown.

## `OeisA46969.conjecture1`

Open: stated without proof.

> Conjecture I: if $n > 2$, then $\frac{a(\text{A005382}(n))}{12}$ is prime,
> where A005382 is the sequence of primes $p$ such that $2p-1$ is also prime.
> Since $\text{A005382}(1) = 2$, $\text{A005382}(2) = 3$ and $\text{A005382}(3) = 7$, this says
> that $\frac{a(p)}{12}$ is prime for every prime $p > 3$ such that $2p-1$ is also prime.
> - Lorenzo Sauras Altuzarra, Oct 13 2020

```lean
theorem conjecture1 (p : ℕ) (hp : p.Prime) (hp' : (2 * p - 1).Prime) (h3 : 3 < p) :
    (a p / 12).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/46969.lean, line 125](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/46969.lean#L125).

## `OeisA46969.conjecture2`

Solved: stated here; a Lean proof is at [https://github.com/epoch-research/LeanOpenProblems-results/blob/f02efd9a8c5fc6a735d2a90c33e24f7278ce0ffc/runs/oeis-full-50usd-ant-j0j0g4uzligm1k41/oeis_a046969_conjecture_2/Submission/Spec.lean#L845](https://github.com/epoch-research/LeanOpenProblems-results/blob/f02efd9a8c5fc6a735d2a90c33e24f7278ce0ffc/runs/oeis-full-50usd-ant-j0j0g4uzligm1k41/oeis_a046969_conjecture_2/Submission/Spec.lean#L845).

> Conjecture II: if $\frac{a(n)}{12}$ is prime, then $\frac{a(n-1)}{12} - (n-1)$,
> $\frac{a(n)}{12} - n$ and $\frac{a(n+2)}{12} - (n+2)$ are multiples of 6.
> - Lorenzo Sauras Altuzarra, Oct 13 2020
>
> This is false for $n = 236791$.

```lean
theorem conjecture2 :
    ¬ ∀ (n : ℕ), 2 ≤ n → 12 ∣ a n → Nat.Prime (a n / 12) →
      12 ∣ a (n - 1) → 12 ∣ a (n + 2) →
      6 ∣ ((a (n - 1) / 12 : ℤ) - (n - 1 : ℤ)) ∧
      6 ∣ ((a n / 12 : ℤ) - (n : ℤ)) ∧
      6 ∣ ((a (n + 2) / 12 : ℤ) - (n + 2 : ℤ))
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/46969.lean, line 139](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/46969.lean#L139).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/46969.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/46969.lean)
- [A046969](https://oeis.org/A046969)
