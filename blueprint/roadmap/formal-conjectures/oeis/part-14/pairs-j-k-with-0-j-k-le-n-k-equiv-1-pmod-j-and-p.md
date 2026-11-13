---
declaration: theorem
origin: cited
lean: OeisA238224.conjecture
statement: formalized
---

# Pairs $\{j, k\}$ with $0 < j < k \le n$, $k \equiv 1 \pmod j$, and $\pi(jn) \mid \pi(kn)$

> Let $\pi$ denote the prime counting function. The sequence $a(n)$ counts the number of pairs
> $(j, k)$ with $0 < j < k \le n$ and $k \equiv 1 \pmod j$ such that $\pi(jn)$ divides $\pi(kn)$.
>
> *References:*
> - [A238224](https://oeis.org/A238224)

*Quoted from [FormalConjectures/OEIS/238224.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/238224.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA238224.conjecture`

Open: stated without proof.

> Conjecture: $a(n) > 0$ for all $n > 1$.

```lean
theorem conjecture (n : ℕ) (hn : 1 < n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/238224.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/238224.lean#L61).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/238224.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/238224.lean)
- [A238224](https://oeis.org/A238224)
