---
declaration: theorem
origin: cited
lean: OeisA78729.conjecture
statement: formalized
---

# Least $k > 0$ such that $(k+1)(k+2)\cdots(k+n) + 1$ is prime

> The sequence $a(n)$ is the least positive integer $k$ such that $(k+1)(k+2)\cdots(k+n) + 1$ is
> prime,
> if such $k$ exists; otherwise $a(n) = 0$.
>
> *References:*
> - [A078729](https://oeis.org/A078729)

*Quoted from [FormalConjectures/OEIS/78729.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/78729.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA78729.conjecture`

Open: stated without proof.

> $(k+1)(k+2)(k+3)(k+4) + 1 = (k^2 + 5k + 5)^2$, which is never prime. Hence $a(4) = 0$.
> Conjecture: $a(n) = 0$ if and only if $n = 4$.

```lean
theorem conjecture (n : ℕ) (hn : 0 < n) : a n = 0 ↔ n = 4
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/78729.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/78729.lean#L101).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/78729.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/78729.lean)
- [A078729](https://oeis.org/A078729)
