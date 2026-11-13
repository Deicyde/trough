---
declaration: theorem
origin: cited
lean: OeisA87207.conjecture
statement: formalized
---

# Binary representation of primes that divide a number, in decimal

> The value $a(n)$ is given by
>
> $$ a(n) = \sum_{p \mid n, p \text{ prime}} 2^{\pi(p) - 1} $$
>
> where $\pi(p) = \mathrm{primeCounting}(p)$ gives the 1-based index of the prime $p$.
>
> *References:*
> - [A087207](https://oeis.org/A087207)

*Quoted from [FormalConjectures/OEIS/87207.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/87207.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA87207.conjecture`

Open: stated without proof.

> Starting at any $n$ and iterating the map $n \mapsto a(n)$, we will always reach $0$.
> - _Antti Karttunen_, Jun 18,20 2017

```lean
theorem conjecture (n : ℕ) : ∃ k : ℕ, (a^[k]) n = 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/87207.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/87207.lean#L65).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/87207.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/87207.lean)
- [A087207](https://oeis.org/A087207)
