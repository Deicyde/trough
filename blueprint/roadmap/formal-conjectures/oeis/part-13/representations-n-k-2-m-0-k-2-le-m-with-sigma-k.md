---
declaration: theorem
origin: cited
lean: OeisA233544.conjecture_1, OeisA233544.conjecture_2, OeisA233544.conjecture_3
statement: formalized
---

# Representations $n = k^2 + m$ ($0 < k^2 \le m$) with $\sigma(k^2) + \phi(m)$ prime

> Let $\sigma$ denote the sum-of-divisors function and $\phi$ denote Euler's totient function.
> The sequence $a(n)$ counts the representations $n = k^2 + m$ ($0 < k^2 \le m$) such that
> $\sigma(k^2) + \phi(m)$ is prime.
>
> *References:*
> - [A233544](https://oeis.org/A233544)

*Quoted from [FormalConjectures/OEIS/233544.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/233544.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 open. It also has 5 test statements, counted here but not shown.

## `OeisA233544.conjecture_1`

Open: stated without proof.

> Conjecture (i): $a(n) > 0$ for all $n > 1$.
> - _Zhi-Wei Sun_

```lean
theorem conjecture_1 (n : ℕ) (hn : 1 < n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/233544.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/233544.lean#L73).

## `OeisA233544.conjecture_2`

Open: stated without proof.

> Conjecture (ii): Any integer $n > 1$ can be written as $k + m$ with $k > 0$ and $m > 0$
> such that $\sigma(k)^2 + \phi(m)$ is prime.
> - _Zhi-Wei Sun_

```lean
theorem conjecture_2 (n : ℕ) (hn : 1 < n) :
    ∃ k m : ℕ, 0 < k ∧ 0 < m ∧ n = k + m ∧ Nat.Prime (σ 1 k ^ 2 + m.totient)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/233544.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/233544.lean#L82).

## `OeisA233544.conjecture_3`

Open: stated without proof.

> Conjecture (ii): Any integer $n > 1$ can be written as $k + m$ with $k > 0$ and $m > 0$
> such that $\sigma(k) + \phi(m)^2$ is prime.
> - _Zhi-Wei Sun_

```lean
theorem conjecture_3 (n : ℕ) (hn : 1 < n) :
    ∃ k m : ℕ, 0 < k ∧ 0 < m ∧ n = k + m ∧ Nat.Prime (σ 1 k + m.totient ^ 2)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/233544.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/233544.lean#L92).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/233544.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/233544.lean)
- [A233544](https://oeis.org/A233544)
