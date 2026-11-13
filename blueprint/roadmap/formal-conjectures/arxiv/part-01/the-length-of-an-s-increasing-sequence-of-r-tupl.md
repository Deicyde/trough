---
declaration: theorem
origin: cited
lean: Arxiv.«1609.08688».maximalLength_le, Arxiv.«1609.08688».maximalLength_ge_of_isSquare, Arxiv.«1609.08688».maximalLength_le_isBigO, Arxiv.«1609.08688».maximalLength_pow, Arxiv.«1609.08688».maximalLength_pow_eventually, Arxiv.«1609.08688».maximalLength_le_strong
statement: formalized
---

# The length of an $s$-increasing sequence of $r$-tuples

> This file contains the formalisation of [GoLo21] up to and
> including Conjecture 1.8.
>
> *References:*
> - [arxiv/1609.08688](https://arxiv.org/abs/1609.08688)
>   **The length of an $s$-increasing sequence of $r$-tuples** by *W. T. Gowers, J. Long*
> - [GoLo21](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/length-of-an-sincreasing-sequence-of-rtuples/7301418D47DB1ECD6BE71C20E8A98D0A)
>   **The length of an $s$-increasing sequence of $r$-tuples**
>   by *W. T. Gowers, J. Long*, Combinatorics, Probability and Computing (2021), 686-721

*Quoted from [FormalConjectures/Arxiv/1609.08688/sIncreasingrTuples.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/1609.08688/sIncreasingrTuples.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 6 research or textbook statements: 1 open and 5 solved. It also has 9 test statements and 11 API statements, counted here but not shown.

## `Arxiv.«1609.08688».maximalLength_le`

Proved here.

> For all $n$ we have $F(n) \leq n^2$.
>
> This is the upper bound in [GoLo21, Proposition 1.4], proved by applying the
> pigeonhole principle to the first two coordinates.

```lean
theorem maximalLength_le (n : ℕ) : F n ≤ n ^ 2
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/1609.08688/sIncreasingrTuples.lean, line 190](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/1609.08688/sIncreasingrTuples.lean#L190).

## `Arxiv.«1609.08688».maximalLength_ge_of_isSquare`

Solved: stated here without proof.

> Moreover, whenever $n$ is a perfect square we have $F(n) \geq n^{3/2}$.

```lean
theorem maximalLength_ge_of_isSquare {n : ℕ} (h : IsSquare n) :
    n.sqrt ^ 3 ≤ F n
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/1609.08688/sIncreasingrTuples.lean, line 217](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/1609.08688/sIncreasingrTuples.lean#L217).

## `Arxiv.«1609.08688».maximalLength_le_isBigO`

Solved: stated here without proof.

> $F(n) \leq n^2 / \exp(\Omega(\log^*(n)))$, i.e. there is a constant $c > 0$ such that
> $F(n) \leq n^2 / \exp(c \log^*(n))$ for all sufficiently large $n$.

```lean
theorem maximalLength_le_isBigO : ∃ c > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
    (F n : ℝ) ≤ (n : ℝ) ^ 2 / Real.exp (c * (Real.iteratedLog n : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/1609.08688/sIncreasingrTuples.lean, line 234](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/1609.08688/sIncreasingrTuples.lean#L234).

## `Arxiv.«1609.08688».maximalLength_pow`

Solved: stated here without proof.

> Suppose that for some $n$ we have $F(n) = n ^ {\alpha}$. Then there are arbitrarily
> large $m$ such that $F(m) \geq m^{\alpha}$.

```lean
theorem maximalLength_pow {n : ℕ} {e : ℝ} (hn : 1 < n) (h : F n = (n : ℝ) ^ e) :
    ∃ᶠ m : ℕ in Filter.atTop, (m : ℝ) ^ e ≤ F m
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/1609.08688/sIncreasingrTuples.lean, line 279](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/1609.08688/sIncreasingrTuples.lean#L279).

## `Arxiv.«1609.08688».maximalLength_pow_eventually`

Solved: stated here without proof.

> Moreover, for every $\beta < \alpha$ and all sufficiently large $m$ we have
> $F(m) \geq m^{\beta}$.

```lean
theorem maximalLength_pow_eventually {n : ℕ} {e : ℝ} (hn : 1 < n) (h : F n = (n : ℝ) ^ e)
    {b : ℝ} (hb : b < e) :
    ∀ᶠ m : ℕ in Filter.atTop, (m : ℝ) ^ b ≤ F m
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/1609.08688/sIncreasingrTuples.lean, line 286](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/1609.08688/sIncreasingrTuples.lean#L286).

## `Arxiv.«1609.08688».maximalLength_le_strong`

Open: stated without proof.

> $F(n) \leq n^{3/2}$.

```lean
theorem maximalLength_le_strong (n : ℕ) : F n ≤ Real.sqrt n ^ 3
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/1609.08688/sIncreasingrTuples.lean, line 293](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/1609.08688/sIncreasingrTuples.lean#L293).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/1609.08688/sIncreasingrTuples.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/1609.08688/sIncreasingrTuples.lean)
- [arxiv/1609.08688](https://arxiv.org/abs/1609.08688)
