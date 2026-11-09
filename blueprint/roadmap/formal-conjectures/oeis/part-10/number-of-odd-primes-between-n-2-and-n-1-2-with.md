---
declaration: theorem
origin: cited
lean: OeisA185150.conjecture
statement: formalized
---

# Number of odd primes between $n^2$ and $(n+1)^2$ with $(n/p) = 1$

> $a(n)$ is the number of odd primes $p$ between $n^2$ and $(n+1)^2$ such that the Legendre symbol
> $\left(\frac{n}{p}\right) = 1$.
>
> *References:*
> - [A185150](https://oeis.org/A185150)
> - Z.-W. Sun, "Conjectures involving primes and quadratic forms", arXiv preprint
>   [arXiv:1211.1588](https://arxiv.org/abs/1211.1588) [math.NT], 2012.

*Quoted from [FormalConjectures/OEIS/185150.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/185150.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA185150.conjecture`

Open: stated without proof.

> Conjecture: $a(n) > 0$ for all $n > 0$.
> - _Zhi-Wei Sun_, Dec 29 2012

```lean
theorem conjecture (n : ℕ) (hn : 0 < n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/185150.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/185150.lean#L74).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/185150.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/185150.lean)
- [A185150](https://oeis.org/A185150)
