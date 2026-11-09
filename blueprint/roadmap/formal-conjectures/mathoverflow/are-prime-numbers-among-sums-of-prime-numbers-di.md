---
declaration: theorem
origin: cited
lean: MathOverflow434111.restricted_prime_number_theorem, MathOverflow434111.restricted_prime_number_theorem.variants.even_subsequence
statement: formalized
---

# Are prime numbers among sums of prime numbers distributed as $\frac n{2\ln(n)}$?

> *Reference:*
>
> [mathoverflow.net/questions/434111](https://mathoverflow.net/questions/434111/are-prime-numbers-among-sums-of-prime-numbers-distributed-as-frac-n2-lnn)
>
> [Me18] Meštrović, R., *Curious Conjectures on the Distribution of Primes
> Among the Sums of the First `2n` Primes*, [arXiv:1804.04198](https://arxiv.org/abs/1804.04198)
> (2018), Conjecture 3.3.

*Quoted from [FormalConjectures/Mathoverflow/434111.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Mathoverflow/434111.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open.

## `MathOverflow434111.restricted_prime_number_theorem`

Open: stated without proof.

> The conjecture claims that $\pi_n\sim\frac n{2\ln(n)}$.
>
> In other words, primes are distributed among the much sparser sequence $(S_n)_n$
> with essentially the same density as in the positive integers, up to a factor of $2$.
>
> [MathOverflow 434111](https://mathoverflow.net/questions/434111/are-prime-numbers-among-sums-of-prime-numbers-distributed-as-frac-n2-lnn).
>
> [Me18] Meštrović, R., *Curious Conjectures on the Distribution of Primes
> Among the Sums of the First `2n` Primes*, [arXiv:1804.04198](https://arxiv.org/abs/1804.04198)
> (2018).

```lean
theorem restricted_prime_number_theorem :
    ((fun n : ℕ => (piRestricted n : ℝ)) ~[atTop] (fun n : ℕ => (n : ℝ) / (2 * Real.log n)))
```

Category `research open`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Mathoverflow/434111.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Mathoverflow/434111.lean#L60).

## `MathOverflow434111.restricted_prime_number_theorem.variants.even_subsequence`

Open: stated without proof.

> Meštrović's original formulation [Me18, Conjecture 3.3]: the sequence of sums of the
> first $2m$ primes satisfies the Restricted Prime Number Theorem, $\pi(m, (S_{2m})) \sim \frac{m}{\ln m}$.

```lean
theorem restricted_prime_number_theorem.variants.even_subsequence :
    ((fun m : ℕ => (((Finset.Icc 1 m).filter (fun k => Nat.Prime (S (2 * k)))).card : ℝ)) ~[atTop]
      (fun m : ℕ => (m : ℝ) / Real.log m))
```

Category `research open`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Mathoverflow/434111.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Mathoverflow/434111.lean#L69).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Mathoverflow/434111.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Mathoverflow/434111.lean)
- [mathoverflow.net/questions/434111](https://mathoverflow.net/questions/434111/are-prime-numbers-among-sums-of-prime-numbers-distributed-as-frac-n2-lnn)
