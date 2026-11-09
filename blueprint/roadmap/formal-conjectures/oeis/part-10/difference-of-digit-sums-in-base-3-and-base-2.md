---
declaration: theorem
origin: cited
lean: OeisA180017.conjecture
statement: formalized
---

# Difference of digit sums in base 3 and base 2

> Difference of sums of digits of $n$ in ternary and in binary:
>
> $$a(n) = \sum \mathrm{digits}_3(n) - \sum \mathrm{digits}_2(n).$$
>
> *References:*
> - [A180017](https://oeis.org/A180017)

*Quoted from [FormalConjectures/OEIS/180017.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/180017.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA180017.conjecture`

Open: stated without proof.

> "This sequence is positive on average, since 1/log(3) > 1/log(4). Do all integers appear
> infinitely often?" - Charles R Greathouse IV, Feb 07 2013

```lean
theorem conjecture (z : ℤ) : Set.Infinite {n : ℕ | a n = z}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/180017.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/180017.lean#L56).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/180017.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/180017.lean)
- [A180017](https://oeis.org/A180017)
