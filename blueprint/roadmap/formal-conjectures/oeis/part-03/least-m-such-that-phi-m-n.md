---
declaration: theorem
origin: cited
lean: OeisA55487.conjecture
statement: formalized
---

# Least $m$ such that $\phi(m) = n!$

> The smallest positive integer $m$ whose Euler totient equals $n!$.
>
> *References:*
> - [A055487](https://oeis.org/A055487)

*Quoted from [FormalConjectures/OEIS/55487.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/55487.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 4 test statements, counted here but not shown.

## `OeisA55487.conjecture`

Open: stated without proof.

> Conjecture: unless $n! + 1$ is prime (i.e., $n \in \text{A002981}$), $a(n) = p q$ where $p$ is the
> least prime $> \sqrt{n!}$ such that $(p - 1) \mid n!$ and $q = \frac{n!}{p - 1} + 1$ is prime.
> - M. F. Hasler, Oct 04 2009
>
> The conclusion $(p(n)).\text{Prime}$ asserts that such a prime $p$ exists: if no prime satisfies
> the search conditions then `p n` is `sInf ∅ = 0`, which is not prime.

```lean
theorem conjecture (n : ℕ) (hn : 1 ≤ n) (h_not_prime : ¬ isFactorialPrime n) :
    (p n).Prime ∧ a n = p n * q n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/55487.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/55487.lean#L72).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/55487.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/55487.lean)
- [A055487](https://oeis.org/A055487)
