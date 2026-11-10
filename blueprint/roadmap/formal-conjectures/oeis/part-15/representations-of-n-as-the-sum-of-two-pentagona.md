---
declaration: theorem
origin: cited
lean: OeisA253187.conjecture_1, OeisA253187.conjecture_2
statement: formalized
---

# Representations of $n$ as the sum of two pentagonal and a generalized decagonal number

> The sequence $a(n)$ counts the number of ordered ways to write $n$ as the sum of a pentagonal
> number $\frac{x(3x-1)}{2}$ ($x \ge 0$), a second pentagonal number $\frac{y(3y+1)}{2}$ ($y \ge 0$),
> and a generalized decagonal number $m(4m-3)$ ($m \in \mathbb{Z}$).
>
> *References:*
> - [A253187](https://oeis.org/A253187)

*Quoted from [FormalConjectures/OEIS/253187.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/253187.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 5 test statements, counted here but not shown.

## `OeisA253187.conjecture_1`

Open: stated without proof.

> Conjecture: $a(n) > 0$ for all $n$.
> - _Zhi-Wei Sun_

```lean
theorem conjecture_1 (n : ℕ) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/253187.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/253187.lean#L76).

## `OeisA253187.conjecture_2`

Open: stated without proof.

> Conjecture: For any ordered pair $(k, m)$ among $(5,7), (5,9), (5,13), (6,5), (6,7), (7,5)$,
> each nonnegative integer $n$ can be written as the sum of a $k$-gonal number, a second $k$-gonal
> number, and a generalized $m$-gonal number.
> - _Zhi-Wei Sun_

```lean
theorem conjecture_2 (k m : ℕ) (hkm : (k, m) ∈ cPairs) (n : ℕ) :
    ∃ x y : ℕ, ∃ z : ℤ,
      Nat.polygonalNumber k x + Nat.generalizedPolygonalNumber k (-(y : ℤ)) +
        Nat.generalizedPolygonalNumber m z = n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/253187.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/253187.lean#L86).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/253187.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/253187.lean)
- [A253187](https://oeis.org/A253187)
