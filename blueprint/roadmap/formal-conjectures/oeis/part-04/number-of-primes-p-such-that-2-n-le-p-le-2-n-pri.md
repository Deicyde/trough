---
declaration: theorem
origin: cited
lean: OeisA69923.conjecture
statement: formalized
---

# Number of primes $p$ such that $2^n \le p \le 2^n + \mathrm{prime}(n)$

> The sequence $a(n)$ counts the number of primes $p$ in the interval $[2^n, 2^n + p_n]$,
> where $p_n$ is the $n$-th prime ($p_1 = 2, p_2 = 3, \dots$):
>
> $$a(n) = |\{p \text{ prime} \mid 2^n \le p \le 2^n + p_n\}|$$
>
> for $n \ge 1$, and $a(0) = 0$.
>
> *References:*
> - [A069923](https://oeis.org/A069923)

*Quoted from [FormalConjectures/OEIS/69923.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/69923.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 4 test statements, counted here but not shown.

## `OeisA69923.conjecture`

Open: stated without proof.

> For any $n > 0$, is there always at least one prime $p$ such that
> $2^n \le p \le 2^n + \mathrm{prime}(n)$?
> (checked up to $n = 250$). In this case, that would be stronger than the Schinzel conjecture:
> "for $m > 1$ there's at least one prime $p$ such that $m \le p \le m + \log(m)^2$" since,
> for $n > 2$, $\mathrm{prime}(n) < \log(2^n)^2 = n^2 \log(2)$.

```lean
theorem conjecture (n : ℕ) (hn : 0 < n) : 1 ≤ a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/69923.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/69923.lean#L79).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/69923.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/69923.lean)
- [A069923](https://oeis.org/A069923)
