---
declaration: theorem
origin: cited
lean: OeisA247824.conjecture_1, OeisA247824.conjecture_2
statement: formalized
---

# Least $m$ such that $m + n$ divides $\mathrm{prime}(m) + \mathrm{prime}(n)$

> The sequence $a(n)$ is the least positive integer $m$ such that $m + n$ divides
> $\mathrm{prime}(m) + \mathrm{prime}(n)$, where $\mathrm{prime}(k)$ denotes the $k$-th prime number
> (with $\mathrm{prime}(1) = 2$).
>
> *References:*
> - [A247824](https://oeis.org/A247824)

*Quoted from [FormalConjectures/OEIS/247824.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/247824.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA247824.conjecture_1`

Open: stated without proof.

> Conjecture: $a(n)$ exists for any $n > 0$.
> The existence of $a(n)$ for $n > 0$ is formalized by requiring that the defining set is nonempty
> (equivalently, $0 < a(n)$).
> - _Zhi-Wei Sun_, Sep 25 2014

```lean
theorem conjecture_1 (n : ℕ) (hn : 0 < n) :
    ({ m : ℕ | 0 < m ∧
      (m + n) ∣ (Nat.nth Nat.Prime (m - 1) + Nat.nth Nat.Prime (n - 1)) }).Nonempty
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/247824.lean, line 112](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/247824.lean#L112).

## `OeisA247824.conjecture_2`

Solved: stated here without proof.

> Conjecture: $a(n) < n(n-1)$ for all $n > 2$.
> - _Zhi-Wei Sun_, Sep 25 2014
>
> Disproved by Khai-Hoan Nguyen-Dang (Oct 30 2026), who found the counterexample
> $n = 1322164$, for which $a(1322164) = 2636932401176 > 1748116320732 = 1322164 \cdot 1322163$.

```lean
theorem conjecture_2 : ¬ ∀ n : ℕ, 2 < n → a n < n * (n - 1)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/247824.lean, line 125](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/247824.lean#L125).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/247824.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/247824.lean)
- [A247824](https://oeis.org/A247824)
