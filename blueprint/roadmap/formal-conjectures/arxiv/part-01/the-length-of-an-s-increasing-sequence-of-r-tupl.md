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

*Quoted from [FormalConjectures/Arxiv/1609.08688/sIncreasingrTuples.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/Arxiv/1609.08688/sIncreasingrTuples.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

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

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/1609.08688/sIncreasingrTuples.lean, line 190](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/Arxiv/1609.08688/sIncreasingrTuples.lean#L190).

## `Arxiv.«1609.08688».maximalLength_ge_of_isSquare`

Solved: stated here; a Lean proof is at [https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-13-000015](https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-13-000015).

> Whenever $n$ is a perfect square we have $F(n) \geq n^{3/2}$.
>
> This is the lower bound in [GoLo21, Proposition 1.4]. The linked Lean proof by Wentao Li
> formalizes that construction. An earlier Lean proof is in `weiyangzen/awesome_theorems`.

```lean
theorem maximalLength_ge_of_isSquare {n : ℕ} (h : IsSquare n) :
    n.sqrt ^ 3 ≤ F n
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/1609.08688/sIncreasingrTuples.lean, line 223](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/Arxiv/1609.08688/sIncreasingrTuples.lean#L223).

## `Arxiv.«1609.08688».maximalLength_le_isBigO`

Solved: stated here without proof.

> $F(n) \leq n^2 / \exp(\Omega(\log^*(n)))$, i.e. there is a constant $c > 0$ such that
> $F(n) \leq n^2 / \exp(c \log^*(n))$ for all sufficiently large $n$.

```lean
theorem maximalLength_le_isBigO : ∃ c > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
    (F n : ℝ) ≤ (n : ℝ) ^ 2 / Real.exp (c * (Real.iteratedLog n : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/1609.08688/sIncreasingrTuples.lean, line 240](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/Arxiv/1609.08688/sIncreasingrTuples.lean#L240).

## `Arxiv.«1609.08688».maximalLength_pow`

Solved: stated here without proof.

> Suppose that for some $n$ we have $F(n) = n ^ {\alpha}$. Then there are arbitrarily
> large $m$ such that $F(m) \geq m^{\alpha}$.

```lean
theorem maximalLength_pow {n : ℕ} {e : ℝ} (hn : 1 < n) (h : F n = (n : ℝ) ^ e) :
    ∃ᶠ m : ℕ in Filter.atTop, (m : ℝ) ^ e ≤ F m
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/1609.08688/sIncreasingrTuples.lean, line 285](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/Arxiv/1609.08688/sIncreasingrTuples.lean#L285).

## `Arxiv.«1609.08688».maximalLength_pow_eventually`

Solved: stated here without proof.

> Moreover, for every $\beta < \alpha$ and all sufficiently large $m$ we have
> $F(m) \geq m^{\beta}$.

```lean
theorem maximalLength_pow_eventually {n : ℕ} {e : ℝ} (hn : 1 < n) (h : F n = (n : ℝ) ^ e)
    {b : ℝ} (hb : b < e) :
    ∀ᶠ m : ℕ in Filter.atTop, (m : ℝ) ^ b ≤ F m
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/1609.08688/sIncreasingrTuples.lean, line 292](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/Arxiv/1609.08688/sIncreasingrTuples.lean#L292).

## `Arxiv.«1609.08688».maximalLength_le_strong`

Open: stated without proof.

> $F(n) \leq n^{3/2}$.

```lean
theorem maximalLength_le_strong (n : ℕ) : F n ≤ Real.sqrt n ^ 3
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/1609.08688/sIncreasingrTuples.lean, line 299](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/Arxiv/1609.08688/sIncreasingrTuples.lean#L299).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/1609.08688/sIncreasingrTuples.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/Arxiv/1609.08688/sIncreasingrTuples.lean)
- [arxiv/1609.08688](https://arxiv.org/abs/1609.08688)
