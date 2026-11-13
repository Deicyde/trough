---
declaration: theorem
origin: cited
lean: OeisA4290.a_ten_pow, OeisA4290.conjecture
statement: formalized
---

# Least positive multiple of $n$ in base 10 with digits 0 and 1

> Least positive multiple of $n$ that when written in base 10 uses only 0's and 1's.
>
> *References:*
> - [A004290](https://oeis.org/A004290)

*Quoted from [FormalConjectures/OEIS/4290.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/4290.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 textbook result. It also has 3 test statements, counted here but not shown.

## `OeisA4290.a_ten_pow`

Textbook result, proved here.

> $a(10^k) = 10^k$ for all $k$.

```lean
theorem a_ten_pow (k : ℕ) : a (10 ^ k) = 10 ^ k
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/4290.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/4290.lean#L109).

## `OeisA4290.conjecture`

Open: stated without proof.

> It is known that $a(10^k - 1) = (10^{9k} - 1) / 9$ for all $k$.
> Is $a(n) < a(10^k - 1)$ for all $n < 10^k - 1$?
> - David Radcliffe, Aug 01 2025

```lean
theorem conjecture (k : ℕ) :
    ∀ n < 10 ^ k - 1, a n < a (10 ^ k - 1)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/4290.lean, line 129](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/4290.lean#L129).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/4290.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/4290.lean)
- [A004290](https://oeis.org/A004290)
