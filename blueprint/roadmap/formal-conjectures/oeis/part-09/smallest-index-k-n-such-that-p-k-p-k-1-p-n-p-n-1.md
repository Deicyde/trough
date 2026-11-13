---
declaration: theorem
origin: cited
lean: OeisA167918.conjecture_infinite, OeisA167918.conjecture1, OeisA167918.conjecture2
statement: formalized
---

# Smallest index $k > n$ such that $(p_k+p_{k+1})/(p_n+p_{n+1})$ is an integer $\ge 2$

> *References:*
> - [A167918](https://oeis.org/A167918)

*Quoted from [FormalConjectures/OEIS/167918.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/167918.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 open. It also has 5 test statements and 15 API statements, counted here but not shown.

## `OeisA167918.conjecture_infinite`

Open: stated without proof.

> Conjecture: the sequence is infinite, that is, for every $n \geq 1$ there is some $k > n$
> with $S(n) \mid S(k)$, so that $a(n)$ is defined.

```lean
theorem conjecture_infinite (n : ℕ) (hn : n > 0) : ∃ k > n, S n ∣ S k
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/167918.lean, line 203](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/167918.lean#L203).

## `OeisA167918.conjecture1`

Open: stated without proof.

> Conjecture: $f(n, k) = 2$ for infinitely many cases, where $k = a(n)$.
>
> No hypothesis on the existence of $a(n)$ is needed: if no suitable $k > n$ exists then
> $a(n) = 0$ and $S(0) = 4 < 2 S(n)$, so such $n$ cannot be witnesses.

```lean
theorem conjecture1 (M : ℕ) :
    ∃ n : ℕ, n ≥ M ∧ n > 0 ∧ S (a n) = 2 * S n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/167918.lean, line 213](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/167918.lean#L213).

## `OeisA167918.conjecture2`

Open: stated without proof.

> Open problem: is the ratio $f(n, k)$ bounded, where $k = a(n)$?
>
> No hypothesis on the existence of $a(n)$ is needed: if no suitable $k > n$ exists then
> $a(n) = 0$ and $S(0) / S(n) = 4 / S(n) = 0$ for $n > 0$, so such $n$ do not affect boundedness.
> When $a(n) \neq 0$ we have $S(n) \mid S(a(n))$ by definition, so the division is exact.

```lean
theorem conjecture2 : ∃ C : ℕ, ∀ n : ℕ, n > 0 → S (a n) / S n ≤ C
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/167918.lean, line 225](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/167918.lean#L225).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/167918.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/167918.lean)
- [A167918](https://oeis.org/A167918)
