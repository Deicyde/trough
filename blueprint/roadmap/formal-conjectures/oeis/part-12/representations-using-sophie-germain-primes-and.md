---
declaration: theorem
origin: cited
lean: OeisA227923.conjecture_1, OeisA227923.conjecture_2, OeisA227923.conjecture_3, OeisA227923.conjecture_4
statement: formalized
---

# Representations using Sophie Germain primes and twin prime pairs

> Number of ways to write $n = x + y$ ($x, y > 0$) such that $6x - 1$ is a Sophie Germain prime
> and $\{6y - 1, 6y + 1\}$ is a twin prime pair.
>
> *References:*
> - [A227923](https://oeis.org/A227923)

*Quoted from [FormalConjectures/OEIS/227923.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/227923.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 4 open. It also has 5 test statements, counted here but not shown.

## `OeisA227923.conjecture_1`

Open: stated without proof.

> Conjecture (i), first part: $a(n) > 0$ for all $n > 1$.

```lean
theorem conjecture_1 (n : ℕ) (hn : n > 1) : a n > 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/227923.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/227923.lean#L61).

## `OeisA227923.conjecture_2`

Open: stated without proof.

> Conjecture (i), second part: Any integer $n > 4$ not equal to $13$ can be written as $x + y$
> with $x$ and $y$ distinct and greater than $1$ such that $6x - 1$ is a Sophie Germain prime
> and $\{6y - 1, 6y + 1\}$ is a twin prime pair.

```lean
theorem conjecture_2 (n : ℕ) (hn : n > 4) (h13 : n ≠ 13) :
    ∃ x y : ℕ, 1 < x ∧ 1 < y ∧ x ≠ y ∧ x + y = n ∧
      (6 * x - 1).Prime ∧ (12 * x - 1).Prime ∧
      (6 * y - 1).Prime ∧ (6 * y + 1).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/227923.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/227923.lean#L70).

## `OeisA227923.conjecture_3`

Open: stated without proof.

> Conjecture (ii), cousin prime variant: Any integer $n > 1$ can be written as $x + y$
> ($x, y > 0$) such that $6x - 1$ is a Sophie Germain prime and $\{6y + 1, 6y + 5\}$ is a
> cousin prime pair.

```lean
theorem conjecture_3 (n : ℕ) (hn : n > 1) :
    ∃ x y : ℕ, 0 < x ∧ 0 < y ∧ x + y = n ∧
      (6 * x - 1).Prime ∧ (12 * x - 1).Prime ∧
      (6 * y + 1).Prime ∧ (6 * y + 5).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/227923.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/227923.lean#L82).

## `OeisA227923.conjecture_4`

Open: stated without proof.

> Conjecture (ii), sexy prime variant: Any integer $n > 1$ can be written as $x + y$
> ($x, y > 0$) such that $6x - 1$ is a Sophie Germain prime and $\{6y - 1, 6y + 5\}$ is a
> sexy prime pair.

```lean
theorem conjecture_4 (n : ℕ) (hn : n > 1) :
    ∃ x y : ℕ, 0 < x ∧ 0 < y ∧ x + y = n ∧
      (6 * x - 1).Prime ∧ (12 * x - 1).Prime ∧
      (6 * y - 1).Prime ∧ (6 * y + 5).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/227923.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/227923.lean#L94).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/227923.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/227923.lean)
- [A227923](https://oeis.org/A227923)
