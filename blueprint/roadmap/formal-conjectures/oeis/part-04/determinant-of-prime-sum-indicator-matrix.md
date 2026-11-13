---
declaration: theorem
origin: cited
lean: OeisA69191.conjecture_1, OeisA69191.conjecture_2
statement: formalized
---

# Determinant of prime sum indicator matrix

> Determinant of the $n \times n$ matrix with $(i,j)$-entry ($1 \le i, j \le n$) equal to $1$
> if $i + j$ is prime, and $0$ otherwise.
>
> *References:*
> - [A069191](https://oeis.org/A069191)

*Quoted from [FormalConjectures/OEIS/69191.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/69191.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 7 test statements, counted here but not shown.

## `OeisA69191.conjecture_1`

Open: stated without proof.

> Conjecture: Let $M(n)$ be the $n \times n$ matrix with $(i,j)$-entry equal to $1$ or $0$ according as
> $i + j$ is prime or not. For each $n = 24, 25, \dots$, the characteristic polynomial of $M(n)$ is
> irreducible over the field of rational numbers.
> - _Zhi-Wei Sun_, Aug 25 2013

```lean
theorem conjecture_1 (n : ℕ) (hn : 24 ≤ n) :
    Irreducible (primeMatrix ℚ n).charpoly
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/69191.lean, line 107](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/69191.lean#L107).

## `OeisA69191.conjecture_2`

Open: stated without proof.

> Conjecture: Let $M(n)$ be the $n \times n$ matrix with $(i,j)$-entry equal to $1$ or $0$ according as
> $i + j$ is prime or not. For each $n = 24, 25, \dots$, the $n$ eigenvalues of $M(n)$ can be listed as
> $\lambda(1), \dots, \lambda(n)$ such that
> $\lambda(1) > -\lambda(2) > \lambda(3) > -\lambda(4) > \dots > (-1)^{n-1} \lambda(n) > 0$.
> - _Zhi-Wei Sun_, Aug 25 2013

```lean
theorem conjecture_2 (n : ℕ) (hn : 24 ≤ n) :
    ∃ ev : Fin n → ℝ,
      (primeMatrix ℝ n).charpoly = ∏ i : Fin n, (Polynomial.X - Polynomial.C (ev i)) ∧
      StrictAnti (fun i : Fin n => (-1 : ℝ) ^ (i : ℕ) * ev i) ∧
      ∀ i : Fin n, 0 < (-1 : ℝ) ^ (i : ℕ) * ev i
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/69191.lean, line 119](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/69191.lean#L119).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/69191.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/69191.lean)
- [A069191](https://oeis.org/A069191)
