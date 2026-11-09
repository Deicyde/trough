---
declaration: theorem
origin: cited
lean: OeisA228143.exists_power_series_eighth_pow_eq
statement: formalized
---

# Eighth root of the generating function of an Apéry-like sequence

> The auxiliary sequence used for the Hankel matrix, defined as
>
> $$\sum_{k=0}^n \binom{n}{k}^2 \binom{n+k}{k}^2$$
>
> Determinant of the $(n+1) \times (n+1)$ Hankel-type matrix with
> $(i,j)$-entry equal to A005259$(i+j)$ for all $i,j = 0,\dots,n$.
> The entry function A005259 is taken to be $\sum_{k=0}^n \binom{n}{k}^2 \binom{n+k}{k}^2$.
>
> *References:*
> - [A228143](https://oeis.org/A228143)
> - [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research with AI-Driven Formal Proof Search* by George Tsoukalas et al.
> - [A005259](https://oeis.org/A005259)

*Quoted from [FormalConjectures/OEIS/228143.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/228143.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA228143.exists_power_series_eighth_pow_eq`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/228143.wip.lean#L698](https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/228143.wip.lean#L698).

> Conjecture: if $A(x) = 1 + 48x + 161856 x^2 + \cdots$ denotes the o.g.f. then $A(x/3)^{1/8}$ has integer coefficients. - _Peter Bala_, Apr 22 2018
>
> A formal proof has been found with the methods described in
> [arxiv/2605.22763](https://arxiv.org/abs/2605.22763).

```lean
theorem exists_power_series_eighth_pow_eq : ∃ C : PowerSeries ℤ,
    (PowerSeries.map (Int.castRingHom ℚ)) (C ^ 8) = ogfAScaled
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/228143.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/228143.lean#L99).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/228143.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/228143.lean)
- [A228143](https://oeis.org/A228143)
