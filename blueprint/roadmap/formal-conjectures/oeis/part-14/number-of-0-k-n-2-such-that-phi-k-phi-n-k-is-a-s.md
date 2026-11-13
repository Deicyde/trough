---
declaration: theorem
origin: cited
lean: OeisA236998.conjecture_1, OeisA236998.conjecture_2, OeisA236998.conjecture_3
statement: formalized
---

# Number of $0 < k < n/2$ such that $\phi(k)\phi(n-k)$ is a square

> Let $\phi$ denote Euler's totient function. The sequence $a(n)$ counts the number of integers
> $0 < k < n/2$ such that $\phi(k)\phi(n-k)$ is a square.
>
> *References:*
> - [A236998](https://oeis.org/A236998)

*Quoted from [FormalConjectures/OEIS/236998.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/236998.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 open. It also has 7 test statements, counted here but not shown.

## `OeisA236998.conjecture_1`

Open: stated without proof.

> Conjecture: (i) $a(n) > 0$ for all $n > 8$.

```lean
theorem conjecture_1 (n : ℕ) (hn : 8 < n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/236998.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/236998.lean#L64).

## `OeisA236998.conjecture_2`

Open: stated without proof.

> Conjecture: (ii) If $n > 20$, then $\phi(k)\phi(n-k) + 1$ is a square for some $0 < k < n/2$.

```lean
theorem conjecture_2 (n : ℕ) (hn : 20 < n) :
    ∃ k : ℕ, 0 < k ∧ 2 * k < n ∧ IsSquare (k.totient * (n - k).totient + 1)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/236998.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/236998.lean#L71).

## `OeisA236998.conjecture_3`

Open: stated without proof.

> Conjecture: (iii) If $n > 1$ is not among $4, 7, 60, 199, 267$, then $k\phi(n-k)$ is a square for
> some $0 < k < n$.

```lean
theorem conjecture_3 (n : ℕ) (hn : 1 < n) (h4 : n ≠ 4) (h7 : n ≠ 7) (h60 : n ≠ 60)
    (h199 : n ≠ 199) (h267 : n ≠ 267) :
    ∃ k : ℕ, 0 < k ∧ k < n ∧ IsSquare (k * (n - k).totient)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/236998.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/236998.lean#L80).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/236998.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/236998.lean)
- [A236998](https://oeis.org/A236998)
