---
declaration: theorem
origin: cited
lean: OeisA232616.conjecture_1, OeisA232616.conjecture_2, OeisA232616.conjecture_3
statement: formalized
---

# Least $m > 0$ such that $\{2^k - k : k = 1, \dots, m\}$ covers all residues modulo $n$

> For $n \ge 1$, $a(n)$ is the least positive integer $m$ such that $\{2^k - k : k = 1, \dots, m\}$
> contains a complete system of residues modulo $n$.
>
> *References:*
> - [A232616](https://oeis.org/A232616)
> - T. Adamczewski, "OEIS Open: How many conjectures can language models turn into theorems?",
>   [arXiv:2608.11941](https://arxiv.org/abs/2608.11941) [cs.AI], 2026.

*Quoted from [FormalConjectures/OEIS/232616.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/232616.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 2 open and 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA232616.conjecture_1`

Solved: stated here without proof.

> Conjecture (i): $a(n) < 2 \cdot (\text{prime}(n) - 1)$ for all $n > 0$,
> where $\text{prime}(n)$ is the $n$-th prime number (1-indexed).
>
> Disproved for $n = 550172$ in the OEIS Open project, see T. Adamczewski, OEIS Open: How many
> conjectures can language models turn into theorems?,
> [arXiv:2608.11941](https://arxiv.org/abs/2608.11941).

```lean
theorem conjecture_1 : ¬ ∀ n > 0, a n < 2 * (Nat.nth Nat.Prime (n - 1) - 1)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/232616.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/232616.lean#L91).

## `OeisA232616.conjecture_2`

Open: stated without proof.

> Conjecture (ii), first equation: The Diophantine equation $x^n - n = y^m$ with $m, n, x, y > 1$
> only has two integral solutions: $2^5 - 5 = 3^3$ and $2^7 - 7 = 11^2$.

```lean
theorem conjecture_2 (x y n m : ℕ) (hx : 1 < x) (hy : 1 < y) (hn : 1 < n) (hm : 1 < m) :
    x ^ n - n = y ^ m ↔ (x = 2 ∧ n = 5 ∧ y = 3 ∧ m = 3) ∨ (x = 2 ∧ n = 7 ∧ y = 11 ∧ m = 2)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/232616.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/232616.lean#L99).

## `OeisA232616.conjecture_3`

Open: stated without proof.

> Conjecture (ii), second equation: The Diophantine equation $x^n + n = y^m$ with $m, n, x, y > 1$
> only has two integral solutions: $5^2 + 2 = 3^3$ and $5^3 + 3 = 2^7$.

```lean
theorem conjecture_3 (x y n m : ℕ) (hx : 1 < x) (hy : 1 < y) (hn : 1 < n) (hm : 1 < m) :
    x ^ n + n = y ^ m ↔ (x = 5 ∧ n = 2 ∧ y = 3 ∧ m = 3) ∨ (x = 5 ∧ n = 3 ∧ y = 2 ∧ m = 7)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/232616.lean, line 108](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/232616.lean#L108).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/232616.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/232616.lean)
- [A232616](https://oeis.org/A232616)
