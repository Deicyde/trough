---
declaration: theorem
origin: cited
lean: OeisA242174.conjecture_1, OeisA242174.conjecture_2
statement: formalized
---

# Least primitive prime divisor of the Franel numbers of order $4$

> Let $f_r(n) = \sum_{k=0}^n \binom{n}{k}^r$ be the Franel number of order $r$. The sequence
> $a(n)$ is the least prime divisor of $f_4(n)$ (A005260) that does not divide any previous
> term $f_4(k)$ with $1 \le k < n$, or $1$ if no such prime divisor exists.
>
> *References:*
> - [A242174](https://oeis.org/A242174)

*Quoted from [FormalConjectures/OEIS/242174.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/242174.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 5 test statements, counted here but not shown.

## `OeisA242174.conjecture_1`

Open: stated without proof.

> Conjecture: $a(n)$ is prime for any $n > 0$.

```lean
theorem conjecture_1 (n : ℕ) (hn : 0 < n) : (a n).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/242174.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/242174.lean#L77).

## `OeisA242174.conjecture_2`

Open: stated without proof.

> "In general, for any $r > 2$, if $n$ is large enough then $f_r(n) = \sum_{k=0}^n \binom{n}{k}^r$
> has a prime divisor which does not divide any previous terms $f_r(k)$ with $k < n$."

```lean
theorem conjecture_2 (r : ℕ) (hr : 2 < r) :
    ∃ N : ℕ, ∀ n : ℕ, N ≤ n → primitivePrimeDivisorFranel r n ≠ 1
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/242174.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/242174.lean#L85).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/242174.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/242174.lean)
- [A242174](https://oeis.org/A242174)
