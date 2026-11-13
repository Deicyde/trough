---
declaration: theorem
origin: cited
lean: OeisA159829.conjecture1, OeisA159829.conjecture2
statement: formalized
---

# Smallest $m$ such that $n^3 + m^3 + 1$ is prime

> $a(n)$ is the smallest natural number $m \ge 1$ such that $n^3 + m^3 + 1$ is prime.
>
> *References:*
> - [A159829](https://oeis.org/A159829)

*Quoted from [FormalConjectures/OEIS/159829.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/159829.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 4 test statements, counted here but not shown.

## `OeisA159829.conjecture1`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/oeis-a159829-conjecture1-counterexample/blob/6632e626baa7f28ad14045aa7408a84178ec128d/lean/A159829Conjecture1FC.lean#L52-L61](https://github.com/KitaKen1/oeis-a159829-conjecture1-counterexample/blob/6632e626baa7f28ad14045aa7408a84178ec128d/lean/A159829Conjecture1FC.lean#L52-L61).

> Conjecture 1: For any $k \ge 3$, there are infinitely many primes of the form $n^k + m^k$
> for $n, m \ge 1$.
> - _Ulrich Krug_, 2009
>
> Answer: No.
> - _Kenta Kitamura_, 2026

```lean
theorem conjecture1 :
    ¬ ∀ (k : ℕ), 3 ≤ k →
      Set.Infinite {p : ℕ | ∃ n m : ℕ, 1 ≤ n ∧ 1 ≤ m ∧ p.Prime ∧
        p = n ^ k + m ^ k}
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/159829.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/159829.lean#L99).

## `OeisA159829.conjecture2`

Open: stated without proof.

> Conjecture 2: For any $k \ge 3$, there are infinitely many primes of the form $n^k + m^k + 1$
> for $n, m \ge 1$.
> - _Ulrich Krug_, 2009

```lean
theorem conjecture2 (k : ℕ) (hk : 3 ≤ k) :
    Set.Infinite {p : ℕ | ∃ n m : ℕ, 1 ≤ n ∧ 1 ≤ m ∧ p.Prime ∧ p = n ^ k + m ^ k + 1}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/159829.lean, line 111](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/159829.lean#L111).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/159829.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/159829.lean)
- [A159829](https://oeis.org/A159829)
