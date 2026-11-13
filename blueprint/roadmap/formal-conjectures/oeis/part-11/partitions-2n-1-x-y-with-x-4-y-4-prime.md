---
declaration: theorem
origin: cited
lean: OeisA218656.conjecture_1, OeisA218656.conjecture_2, OeisA218656.conjecture_3, OeisA218656.conjecture_4
statement: formalized
---

# Partitions $2n + 1 = x + y$ with $x^4 + y^4$ prime

> For $n \ge 1$, $a(n)$ is the number of ways to write $2n + 1$ as $x + y$ with $0 < x < y$ such that
> $x^4 + y^4$ is prime.
>
> *References:*
> - [A218656](https://oeis.org/A218656)

*Quoted from [FormalConjectures/OEIS/218656.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/218656.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 4 open. It also has 5 test statements, counted here but not shown.

## `OeisA218656.conjecture_1`

Open: stated without proof.

> Conjecture: $a(n) > 0$ for all $n \ge 1$.

```lean
theorem conjecture_1 (n : ℕ) (hn : 1 ≤ n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/218656.lean, line 113](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/218656.lean#L113).

## `OeisA218656.conjecture_2`

Open: stated without proof.

> Conjecture: If $x^4 + y^4$ in the definition of $a(n)$ is
> replaced by $x^2 + y^2$, then the count is positive for all $n \ge 1$.
> - _Thomas Ordowski_, Nov 03 2012

```lean
theorem conjecture_2 (n : ℕ) (hn : 1 ≤ n) :
    ∃ x : ℕ, 1 ≤ x ∧ x ≤ n ∧ Nat.Prime (x ^ 2 + (2 * n + 1 - x) ^ 2)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/218656.lean, line 122](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/218656.lean#L122).

## `OeisA218656.conjecture_3`

Open: stated without proof.

> Conjecture: If $x^4 + y^4$ in the definition of $a(n)$ is replaced by $x^8 + y^8$, then the count
> is positive for all $n \ge 1$ except for $2n + 1 \in \{7, 9, 55, 73, 75, 105\}$
> (i.e., $n \in \{3, 4, 27, 36, 37, 52\}$).
> - _Thomas Ordowski_, Nov 03 2012; exceptions noted by _Mauro Fiorentini_, Sep 22 2023

```lean
theorem conjecture_3 (n : ℕ) (hn : 1 ≤ n) (h_exc : n ∉ ({3, 4, 27, 36, 37, 52} : Set ℕ)) :
    ∃ x : ℕ, 1 ≤ x ∧ x ≤ n ∧ Nat.Prime (x ^ 8 + (2 * n + 1 - x) ^ 8)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/218656.lean, line 133](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/218656.lean#L133).

## `OeisA218656.conjecture_4`

Open: stated without proof.

> Conjecture: If $x^4 + y^4$ in the definition of $a(n)$ is replaced by $x^{16} + y^{16}$, then the
> count is positive for all $n \ge 1$ except for $2n + 1 \in \{5, 9\}$ (i.e., $n \in \{2, 4\}$).
> - _Thomas Ordowski_, Nov 03 2012; exceptions noted by _Mauro Fiorentini_, Sep 22 2023

```lean
theorem conjecture_4 (n : ℕ) (hn : 1 ≤ n) (h_exc : n ∉ ({2, 4} : Set ℕ)) :
    ∃ x : ℕ, 1 ≤ x ∧ x ≤ n ∧ Nat.Prime (x ^ 16 + (2 * n + 1 - x) ^ 16)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/218656.lean, line 143](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/218656.lean#L143).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/218656.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/218656.lean)
- [A218656](https://oeis.org/A218656)
