---
declaration: theorem
origin: cited
lean: OeisA249609.conjecture
statement: formalized
---

# Smallest $m \in [1, n]$ such that $\binom{n}{m}$ is evil

> The sequence $a(n)$ is the smallest $m$ with $1 \le m \le n$ such that $\binom{n}{m}$ is an evil
> number (A001969, having an even number of $1$s in its binary expansion), or $0$ if no such $m$
> exists.
>
> *References:*
> - [A249609](https://oeis.org/A249609)

*Quoted from [FormalConjectures/OEIS/249609.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/249609.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA249609.conjecture`

Open: stated without proof.

> Conjecture: there are only five $n$ ($0, 1, 2, 7, 8$) for which all entries of the $n$-th
> Pascal row (A007318) are odious (A000069), which is equivalent to $a(n) = 0$.

```lean
theorem conjecture (n : ℕ) :
    a n = 0 ↔ n ∈ ({0, 1, 2, 7, 8} : Finset ℕ)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/249609.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/249609.lean#L64).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/249609.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/249609.lean)
- [A249609](https://oeis.org/A249609)
