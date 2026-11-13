---
declaration: theorem
origin: cited
lean: OeisA196697.conjecture_1, OeisA196697.conjecture_2
statement: formalized
---

# Number of primes of the form $2^n \pm 2^k \pm 1$ with $0 \le k < n$

> The sequence $a(n)$ counts the number of distinct primes of the form $2^n \pm 2^k \pm 1$ for
> $0 \le k < n$.
>
> *References:*
> - [A196697](https://oeis.org/A196697)

*Quoted from [FormalConjectures/OEIS/196697.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/196697.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 5 test statements, counted here but not shown.

## `OeisA196697.conjecture_1`

Open: stated without proof.

> Conjecture: all terms of this sequence are greater than $0$.
> - _Lei Zhou_, Oct 05 2011

```lean
theorem conjecture_1 (n : ℕ) (hn : 1 ≤ n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/196697.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/196697.lean#L63).

## `OeisA196697.conjecture_2`

Open: stated without proof.

> Conjecture: infinitely many elements of this sequence are equal to $0$.
> - _Charles R Greathouse IV_, Nov 21 2011

```lean
theorem conjecture_2 : Set.Infinite {n : ℕ | a n = 0}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/196697.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/196697.lean#L71).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/196697.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/196697.lean)
- [A196697](https://oeis.org/A196697)
