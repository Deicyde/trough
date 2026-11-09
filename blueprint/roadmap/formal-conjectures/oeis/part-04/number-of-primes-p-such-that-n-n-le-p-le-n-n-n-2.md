---
declaration: theorem
origin: cited
lean: OeisA69922.conjecture
statement: formalized
---

# Number of primes $p$ such that $n^n \le p \le n^n + n^2$

> The sequence $a(n)$ counts the number of prime numbers in the interval $[n^n, n^n + n^2]$:
>
> $$a(n) = |\{p \text{ prime} \mid n^n \le p \le n^n + n^2\}|$$
>
> *References:*
> - [A069922](https://oeis.org/A069922)

*Quoted from [FormalConjectures/OEIS/69922.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/69922.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA69922.conjecture`

Open: stated without proof.

> Question: for any $n > 0$, is there at least one prime $p$ such that $n^n \le p \le n^n + n^2$?
> In this case, that would be stronger than the Schinzel conjecture: "for $m > 1$ there's at least
> one prime $p$ such that $m \le p \le m + \log(m)^2$" since $n^2 < \log(n^n)^2 = n^2 \log(n)^2$.

```lean
theorem conjecture (n : ℕ) (hn : 0 < n) : 1 ≤ a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/69922.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/69922.lean#L69).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/69922.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/69922.lean)
- [A069922](https://oeis.org/A069922)
