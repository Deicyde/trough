---
declaration: theorem
origin: cited
lean: OeisA229969.conjecture_1, OeisA229969.conjecture_2, OeisA229969.conjecture_3a, OeisA229969.conjecture_3b, OeisA229969.conjecture_4, OeisA229969.conjecture_5a, OeisA229969.conjecture_5b
statement: formalized
---

# Ways to write $n = x + y + z$ with six linear and quadratic forms prime

> Number of ways to write $n = x + y + z$ with $0 < x \le y \le z$ such that all the six numbers
> $2x-1, 2y-1, 2z-1, 2xy-1, 2xz-1, 2yz-1$ are prime.
>
> *References:*
> - [A229969](https://oeis.org/A229969)

*Quoted from [FormalConjectures/OEIS/229969.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/229969.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 7 research or textbook statements: 7 open. It also has 7 test statements, counted here but not shown.

## `OeisA229969.conjecture_1`

Open: stated without proof.

> Conjecture: $a(n) > 0$ for all $n > 5$.

```lean
theorem conjecture_1 (n : ℕ) (hn : n > 5) : a n > 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/229969.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/229969.lean#L69).

## `OeisA229969.conjecture_2`

Open: stated without proof.

> Moreover, any integer $n > 6$ can be written as $x + y + z$ with $x$ among $3, 4, 6, 10, 15$ such
> that $2y-1, 2z-1, 2xy-1, 2xz-1, 2yz-1$ are prime.

```lean
theorem conjecture_2 (n : ℕ) (hn : n > 6) :
    ∃ x y z : ℕ, 0 < y ∧ 0 < z ∧ x + y + z = n ∧
      x ∈ ({3, 4, 6, 10, 15} : Finset ℕ) ∧
      (2 * y - 1).Prime ∧ (2 * z - 1).Prime ∧
      (2 * x * y - 1).Prime ∧ (2 * x * z - 1).Prime ∧ (2 * y * z - 1).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/229969.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/229969.lean#L77).

## `OeisA229969.conjecture_3a`

Open: stated without proof.

> Conjecture (i), part 1: Any integer $n > 6$ can be written as $x + y + z$ ($x, y, z > 0$) with
> $2x-1, 2y-1, 2z-1$ and $2xyz-1$ all prime and $x$ among $2, 3, 4$.
> - _Zhi-Wei Sun_

```lean
theorem conjecture_3a (n : ℕ) (hn : n > 6) :
    ∃ x y z : ℕ, 0 < x ∧ 0 < y ∧ 0 < z ∧ x + y + z = n ∧
      x ∈ ({2, 3, 4} : Finset ℕ) ∧
      (2 * x - 1).Prime ∧ (2 * y - 1).Prime ∧ (2 * z - 1).Prime ∧
      (2 * x * y * z - 1).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/229969.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/229969.lean#L90).

## `OeisA229969.conjecture_3b`

Open: stated without proof.

> Conjecture (i), part 2: Each integer $n > 2$ can be written as $x + y + z$ ($x, y, z > 0$) with
> $2x+1, 2y+1, 2z+1$ and $2xyz+1$ all prime and $x$ among $1, 2, 3$.
> - _Zhi-Wei Sun_

```lean
theorem conjecture_3b (n : ℕ) (hn : n > 2) :
    ∃ x y z : ℕ, 0 < x ∧ 0 < y ∧ 0 < z ∧ x + y + z = n ∧
      x ∈ ({1, 2, 3} : Finset ℕ) ∧
      (2 * x + 1).Prime ∧ (2 * y + 1).Prime ∧ (2 * z + 1).Prime ∧
      (2 * x * y * z + 1).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/229969.lean, line 103](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/229969.lean#L103).

## `OeisA229969.conjecture_4`

Open: stated without proof.

> Conjecture (ii): Each integer $n > 4$ can be written as $x + y + z$ with $x = 3$ or $6$ such that
> $2y+1, 2xyz-1$ and $2xyz+1$ are prime.
> - _Zhi-Wei Sun_

```lean
theorem conjecture_4 (n : ℕ) (hn : n > 4) :
    ∃ x y z : ℕ, 0 < y ∧ 0 < z ∧ x + y + z = n ∧
      (x = 3 ∨ x = 6) ∧
      (2 * y + 1).Prime ∧ (2 * x * y * z - 1).Prime ∧ (2 * x * y * z + 1).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/229969.lean, line 116](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/229969.lean#L116).

## `OeisA229969.conjecture_5a`

Open: stated without proof.

> Conjecture (iii), part 1: Every integer $n > 5$ can be written as $x + y + z$ ($x, y, z > 0$) with
> $xy-1, xz-1, yz-1$ all prime and $x$ among $2, 6, 10$.
> - _Zhi-Wei Sun_

```lean
theorem conjecture_5a (n : ℕ) (hn : n > 5) :
    ∃ x y z : ℕ, 0 < x ∧ 0 < y ∧ 0 < z ∧ x + y + z = n ∧
      x ∈ ({2, 6, 10} : Finset ℕ) ∧
      (x * y - 1).Prime ∧ (x * z - 1).Prime ∧ (y * z - 1).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/229969.lean, line 128](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/229969.lean#L128).

## `OeisA229969.conjecture_5b`

Open: stated without proof.

> Conjecture (iii), part 2: Any integer $n > 2$ not equal to $16$ can be written as $x + y + z$
> ($x, y, z > 0$) with $xy+1, xz+1, yz+1$ all prime and $x$ among $1, 2, 6$.
> - _Zhi-Wei Sun_

```lean
theorem conjecture_5b (n : ℕ) (hn : n > 2) (hne : n ≠ 16) :
    ∃ x y z : ℕ, 0 < x ∧ 0 < y ∧ 0 < z ∧ x + y + z = n ∧
      x ∈ ({1, 2, 6} : Finset ℕ) ∧
      (x * y + 1).Prime ∧ (x * z + 1).Prime ∧ (y * z + 1).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/229969.lean, line 140](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/229969.lean#L140).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/229969.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/229969.lean)
- [A229969](https://oeis.org/A229969)
