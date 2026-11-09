---
declaration: theorem
origin: cited
lean: OeisA227582.a_eq_floor_harmonic_expr
statement: formalized
---

# Representation of sequence terms by harmonic numbers $\lfloor \frac{1}{2H(n) - H(n^2+n-1) - \gamma} \rfloor$

> A227582: Expansion of $(2+3x+2x^2+2x^3+3x^4+x^5-x^6)/(1-2x+x^2-x^5+2x^6-x^7)$.
>
> The sequence satisfies the linear recurrence:
> $$a(n) = 2 a(n-1) - a(n-2) + a(n-5) - 2 a(n-6) + a(n-7)$$
> with initial values $a(1) = 2, a(2) = 7, a(3) = 14, a(4) = 23, a(5) = 35, a(6) = 50, a(7) = 67$.
>
> The sequence is 1-indexed in OEIS, so $a(n)$ is the $(n-1)$-th term of the 0-indexed solution.
>
> *References:*
> - [A227582](https://oeis.org/A227582)
> - [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research with AI-Driven Formal Proof Search* by George Tsoukalas et al.

*Quoted from [FormalConjectures/OEIS/227582.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/227582.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements and 1 API statement, counted here but not shown.

## `OeisA227582.a_eq_floor_harmonic_expr`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/227582.wip.lean#L282](https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/227582.wip.lean#L282).

> Conjecture (from A227581): $a(n) = \lfloor 1/(2 H(n) - H(n^2 + n - 1) - \gamma) \rfloor$,
> where $H$ denotes harmonic numbers and $\gamma$ denotes the Euler-Mascheroni constant.
>
> A formal proof has been found with the methods described in
> [arxiv/2605.22763](https://arxiv.org/abs/2605.22763).

```lean
theorem a_eq_floor_harmonic_expr (n : ℕ) (hn : 0 < n) :
    a n = (Int.floor (1 / (2 * (↑(harmonic n) : ℝ) -
    (↑(harmonic (n * n + n - 1)) : ℝ) - Real.eulerMascheroniConstant))).toNat
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/227582.lean, line 123](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/227582.lean#L123).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/227582.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/227582.lean)
- [A227582](https://oeis.org/A227582)
