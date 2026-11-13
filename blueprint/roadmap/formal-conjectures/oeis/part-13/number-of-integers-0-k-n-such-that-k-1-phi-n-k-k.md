---
declaration: theorem
origin: cited
lean: OeisA234360.conjecture_1, OeisA234360.conjecture_2, OeisA234360.conjecture_3, OeisA234360.conjecture_4
statement: formalized
---

# Number of integers $0 < k < n$ such that $(k + 1)^{\phi(n - k)} + k$ is prime

> For $n \ge 1$, $a(n)$ counts the integers $0 < k < n$ for which $(k + 1)^{\phi(n - k)} + k$ is
> prime, where $\phi$ is Euler's totient function.
>
> *References:*
> - [A234360](https://oeis.org/A234360)
> - T. Adamczewski, "OEIS Open: How many conjectures can language models turn into theorems?",
>   [arXiv:2608.11941](https://arxiv.org/abs/2608.11941) [cs.AI], 2026.

*Quoted from [FormalConjectures/OEIS/234360.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/234360.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 3 open and 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA234360.conjecture_1`

Open: stated without proof.

> Conjecture (i): $a(n) > 0$ for all $n > 1$.

```lean
theorem conjecture_1 (n : ℕ) (hn : 1 < n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/234360.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/234360.lean#L64).

## `OeisA234360.conjecture_2`

Solved: stated here without proof.

> Conjecture (i): For any $n > 5$ there is a positive integer $k < n$ with
> $(k + 1)^{\phi(n - k) / 2} - k$ prime.
>
> Disproved for $n = 1408$ in the OEIS Open project, see T. Adamczewski, OEIS Open: How many
> conjectures can language models turn into theorems?,
> [arXiv:2608.11941](https://arxiv.org/abs/2608.11941).

```lean
theorem conjecture_2 :
    ¬ ∀ n : ℕ, 5 < n →
      ∃ k, 0 < k ∧ k < n ∧
        ∃ p : ℕ, p.Prime ∧ (p + k) ^ 2 = (k + 1) ^ (n - k).totient
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/234360.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/234360.lean#L76).

## `OeisA234360.conjecture_3`

Open: stated without proof.

> Conjecture (ii): If $n > 1$, then $k(k + 1)^{\phi(n - k)} + 1$ is prime for some $0 < k < n$.

```lean
theorem conjecture_3 (n : ℕ) (hn : 1 < n) :
    ∃ k, 0 < k ∧ k < n ∧ Nat.Prime (k * (k + 1) ^ (n - k).totient + 1)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/234360.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/234360.lean#L86).

## `OeisA234360.conjecture_4`

Open: stated without proof.

> Conjecture (ii): If $n > 3$, then $k(k + 1)^{\phi(n - k) / 2} - 1$ is prime for some $0 < k < n$.

```lean
theorem conjecture_4 (n : ℕ) (hn : 3 < n) :
    ∃ k, 0 < k ∧ k < n ∧
      ∃ p : ℕ, p.Prime ∧ (p + 1) ^ 2 = k ^ 2 * (k + 1) ^ (n - k).totient
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/234360.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/234360.lean#L94).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/234360.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/234360.lean)
- [A234360](https://oeis.org/A234360)
