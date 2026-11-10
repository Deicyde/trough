---
declaration: theorem
origin: cited
lean: Arxiv.«1207.5099».conjecture
statement: formalized
---

# Conway's subprime Fibonacci sequences

> A subprime Fibonacci sequence starts from two positive integers. Each new term is the sum of the
> previous two terms if that sum is prime; if the sum is composite, it is divided once by its least
> prime factor. This file formalizes the no-infinite-chains component of the conjecture: every such
> sequence eventually enters a cycle. It does not assert that the seven known loops are complete or
> unique.
>
> *References:*
> - R. K. Guy, T. Khovanova, and J. Salazar,
>   ["Conway's subprime Fibonacci sequences"](https://arxiv.org/abs/1207.5099),
>   *Mathematics Magazine* **87** (2014), no. 5, 323–337.
> - [A214897](https://oeis.org/A214897), Conway's subprime Fibonacci sequence: cycle lengths.

*Quoted from [FormalConjectures/Arxiv/1207.5099/SubprimeFibonacci.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/1207.5099/SubprimeFibonacci.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 10 test statements and 1 API statement, counted here but not shown.

## `Arxiv.«1207.5099».conjecture`

Open: stated without proof.

> Every subprime Fibonacci sequence starting from two positive integers eventually enters a cycle.
> This is the "no infinite chains" conjecture recorded in [A214897](https://oeis.org/A214897),
> associated with [Guy–Khovanova–Salazar](https://arxiv.org/abs/1207.5099).

```lean
theorem conjecture (x y : ℕ) (hx : 0 < x) (hy : 0 < y) : EventuallyPeriodic (x, y)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Arxiv/1207.5099/SubprimeFibonacci.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/1207.5099/SubprimeFibonacci.lean#L110).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/1207.5099/SubprimeFibonacci.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/1207.5099/SubprimeFibonacci.lean)
- ["Conway's subprime Fibonacci sequences"](https://arxiv.org/abs/1207.5099)
