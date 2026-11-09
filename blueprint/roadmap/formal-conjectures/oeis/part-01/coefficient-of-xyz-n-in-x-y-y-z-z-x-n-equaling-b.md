---
declaration: theorem
origin: cited
lean: OeisA2897.a_eq_coeff
statement: formalized
---

# Coefficient of $(xyz)^n$ in $((x+y)(y+z)(z+x))^n$ equaling $\binom{2n}{n}^3$

> The sequence $a(n)$ is defined by $a(n) = \binom{2n}{n}^3$.
>
> *References:*
> - [A002897](https://oeis.org/A002897)
> - [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research with AI-Driven Formal Proof Search* by George Tsoukalas et al.

*Quoted from [FormalConjectures/OEIS/2897.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/2897.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA2897.a_eq_coeff`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/2897.wip.lean#L408](https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/2897.wip.lean#L408).

> Conjecture: $a(n) = [x^n y^n z^n] (1+x+y+z)^{2n} (1+x+y-z)^n (1+x-y+z)^n$. - _Peter Bala_, Apr 10 2022
>
> A formal proof has been found with the methods described in
> [arxiv/2605.22763](https://arxiv.org/abs/2605.22763).

```lean
theorem a_eq_coeff (n : ℕ) : (a n : ℤ) = MvPolynomial.coeff (xyzPowN n) (pPoly n)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/2897.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/2897.lean#L95).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/2897.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/2897.lean)
- [A002897](https://oeis.org/A002897)
