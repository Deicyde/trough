---
declaration: theorem
origin: cited
lean: OeisA224.conjecture
statement: formalized
---

# Number of squares $\bmod n$

> The number of squares modulo $n$.
> This is the cardinality of the set $\{k^2 \bmod n \mid k \in \{0, 1, \dots, n-1\}\}$.
>
> *References:*
> - [A000224](https://oeis.org/A000224)

*Quoted from [FormalConjectures/OEIS/224.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/224.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA224.conjecture`

Open: stated without proof.

> $n^2 \equiv 1 \pmod{a(n)(a(n)-1)}$ if and only if $n$ is an odd prime.
> - Thomas Ordowski, Jun 08 2017

```lean
theorem conjecture (n : ℕ) (hn : 1 < n) :
    (n.Prime ∧ n ≠ 2) ↔ n ^ 2 ≡ 1 [MOD a n * (a n - 1)]
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/224.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/224.lean#L65).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/224.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/224.lean)
- [A000224](https://oeis.org/A000224)
