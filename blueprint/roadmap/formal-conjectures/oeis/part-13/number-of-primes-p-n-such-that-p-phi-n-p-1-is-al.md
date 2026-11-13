---
declaration: theorem
origin: cited
lean: OeisA233566.conjecture_1, OeisA233566.conjecture_2
statement: formalized
---

# Number of primes $p < n$ such that $p \phi(n - p) - 1$ is also prime

> Let $\phi$ denote Euler's totient function. The sequence $a(n)$ counts the primes $p < n$ such
> that $p \phi(n - p) - 1$ is also prime.
>
> *References:*
> - [A233566](https://oeis.org/A233566)

*Quoted from [FormalConjectures/OEIS/233566.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/233566.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 5 test statements, counted here but not shown.

## `OeisA233566.conjecture_1`

Open: stated without proof.

> Conjecture: $a(n) > 0$ for all $n > 3$.

```lean
theorem conjecture_1 (n : ℕ) (hn : 3 < n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/233566.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/233566.lean#L62).

## `OeisA233566.conjecture_2`

Open: stated without proof.

> Conjecture: For any $n > 2$ there is a prime $p < n$ with $p^2 \phi(n - p) - 1$ prime.

```lean
theorem conjecture_2 (n : ℕ) (hn : 2 < n) :
    ∃ p < n, p.Prime ∧ Nat.Prime (p ^ 2 * (n - p).totient - 1)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/233566.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/233566.lean#L69).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/233566.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/233566.lean)
- [A233566](https://oeis.org/A233566)
