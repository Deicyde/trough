---
declaration: theorem
origin: cited
lean: OeisA232194.conjecture_1, OeisA232194.conjecture_2, OeisA232194.conjecture_3, OeisA232194.conjecture_4, OeisA232194.conjecture_5, OeisA232194.conjecture_6
statement: formalized
---

# Ways to write $n = x + y$ with $nx + y$ and $ny - x$ both prime

> Number of ways to write $n = x + y$ ($x, y > 0$) with $nx + y$ and $ny - x$ both prime.
>
> *References:*
> - [A232194](https://oeis.org/A232194)

*Quoted from [FormalConjectures/OEIS/232194.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/232194.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 6 research or textbook statements: 6 open. It also has 5 test statements, counted here but not shown.

## `OeisA232194.conjecture_1`

Open: stated without proof.

> Conjecture (i), part 1: $a(n) > 0$ for all $n > 2$.

```lean
theorem conjecture_1 (n : ℕ) (hn : n > 2) : a n > 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/232194.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/232194.lean#L58).

## `OeisA232194.conjecture_2`

Open: stated without proof.

> Conjecture (i), part 2: $a(n) = 1$ only for $n = 3, 4, 6, 20, 24$.

```lean
theorem conjecture_2 (n : ℕ) :
    a n = 1 ↔ n ∈ ({3, 4, 6, 20, 24} : Finset ℕ)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/232194.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/232194.lean#L65).

## `OeisA232194.conjecture_3`

Open: stated without proof.

> Conjecture (ii): Any positive integer $n$ not among $1, 30, 54$ can be written as $x + y$
> ($x, y > 0$) with $nx + y$ and $ny + x$ both prime.

```lean
theorem conjecture_3 (n : ℕ) (hn : n > 0) (hne : n ∉ ({1, 30, 54} : Finset ℕ)) :
    ∃ x y : ℕ, 0 < x ∧ 0 < y ∧ x + y = n ∧
      (n * x + y).Prime ∧ (n * y + x).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/232194.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/232194.lean#L74).

## `OeisA232194.conjecture_4`

Open: stated without proof.

> Conjecture (iii): Each integer $n > 1$ not equal to $8$ can be expressed as $x + y$ ($x, y > 0$)
> with $nx^2 + y$ prime.

```lean
theorem conjecture_4 (n : ℕ) (hn : n > 1) (hne : n ≠ 8) :
    ∃ x y : ℕ, 0 < x ∧ 0 < y ∧ x + y = n ∧ (n * x ^ 2 + y).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/232194.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/232194.lean#L84).

## `OeisA232194.conjecture_5`

Open: stated without proof.

> Conjecture (iii), variant: Each integer $n > 1$ not equal to $8$ can be expressed as $x + y$
> ($x, y > 0$) with $x^4 + ny$ prime.

```lean
theorem conjecture_5 (n : ℕ) (hn : n > 1) (hne : n ≠ 8) :
    ∃ x y : ℕ, 0 < x ∧ 0 < y ∧ x + y = n ∧ (x ^ 4 + n * y).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/232194.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/232194.lean#L93).

## `OeisA232194.conjecture_6`

Open: stated without proof.

> Conjecture (iv): Any integer $n > 5$ can be written as $p + q$ ($q > 0$) with $p$ and $nq^2 + 1$
> both prime.

```lean
theorem conjecture_6 (n : ℕ) (hn : n > 5) :
    ∃ p q : ℕ, 0 < q ∧ p + q = n ∧ p.Prime ∧ (n * q ^ 2 + 1).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/232194.lean, line 102](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/232194.lean#L102).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/232194.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/232194.lean)
- [A232194](https://oeis.org/A232194)
