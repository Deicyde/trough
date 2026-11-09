---
declaration: theorem
origin: cited
lean: OeisA117531.conjecture
statement: formalized
---

# Number of primes in $n$-th row of triangle $k^2 - k + p_n$

> $a(n)$ is the number of primes in the $n$-th row of the triangle $T(n, k) = k^2 - k + p_n$
> for $1 \le k \le n$, where $p_n$ is the $n$-th prime ($p_1=2, p_2=3, \dots$).
>
> *References:*
> - [A117531](https://oeis.org/A117531)

*Quoted from [FormalConjectures/OEIS/117531.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/117531.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA117531.conjecture`

Open: stated without proof.

> Conjecture: $a(n) < n$ for $n > 13$.

```lean
theorem conjecture (n : ℕ) (h : n > 13) : a n < n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/117531.lean, line 127](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/117531.lean#L127).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/117531.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/117531.lean)
- [A117531](https://oeis.org/A117531)
