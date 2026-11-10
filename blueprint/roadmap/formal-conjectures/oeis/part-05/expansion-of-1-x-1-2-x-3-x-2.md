---
declaration: theorem
origin: cited
lean: OeisA87455.conjecture
statement: formalized
---

# Expansion of $(1 - x)/(1 - 2 x + 3 x^2)$

> This sequence is the expansion of $(1 - x)/(1 - 2 x + 3 x^2)$ in powers of $x$.
> It satisfies the linear recurrence relation $a(n) = 2 a(n-1) - 3 a(n-2)$ for $n \ge 2$,
> with initial values $a(0)=1$ and $a(1)=1$.
>
> *References:*
> - [A087455](https://oeis.org/A087455)

*Quoted from [FormalConjectures/OEIS/87455.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/87455.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA87455.conjecture`

Open: stated without proof.

> It is an open question whether or not this sequence satisfies Benford's law
> [Berger-Hill, 2017; Arno Berger, email, Jan 06 2017]. - N. J. A. Sloane, Feb 08 2017

```lean
theorem conjecture : SatisfiesBenford a
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [60 Probability theory and stochastic processes](../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/OEIS/87455.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/87455.lean#L81).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/87455.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/87455.lean)
- [A087455](https://oeis.org/A087455)
