---
declaration: theorem
origin: cited
lean: OeisA196698.conjecture_1, OeisA196698.conjecture_2
statement: formalized
---

# Primes of the form $3^n \pm 3^k \pm 1$

> Number of primes of the form $3^n \pm 3^k \pm 1$ with $0 \le k < n$.
>
> *References:*
> - [A196698](https://oeis.org/A196698)

*Quoted from [FormalConjectures/OEIS/196698.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/196698.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 5 test statements, counted here but not shown.

## `OeisA196698.conjecture_1`

Open: stated without proof.

> "Conjecture: all elements of this sequence are greater than $0$."

```lean
theorem conjecture_1 (n : ℕ) (hn : 1 ≤ n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/196698.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/196698.lean#L66).

## `OeisA196698.conjecture_2`

Open: stated without proof.

> "I conjecture the contrary: infinitely many elements of this sequence are equal to $0$."
> - _Charles R Greathouse IV_, Nov 21 2011

```lean
theorem conjecture_2 : Set.Infinite {n : ℕ | a n = 0}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/196698.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/196698.lean#L74).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/196698.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/196698.lean)
- [A196698](https://oeis.org/A196698)
