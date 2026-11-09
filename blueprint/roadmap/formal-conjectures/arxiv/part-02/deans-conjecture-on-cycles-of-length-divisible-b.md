---
declaration: theorem
origin: cited
lean: Arxiv.«2605.02731».dean_conjecture, Arxiv.«2605.02731».dean_conjecture.variants.five, Arxiv.«2605.02731».dean_conjecture.variants.three, Arxiv.«2605.02731».dean_conjecture.variants.four, Arxiv.«2605.02731».dean_conjecture.variants.six_le
statement: formalized
---

# Dean's conjecture on cycles of length divisible by \`k\`

> *References:*
> - [arxiv/2605.02731](https://arxiv.org/abs/2605.02731)
>   **Existence of cycles of length divisible by 3 or 4**
>   by *Ilkyoo Choi, Hojin Chu, Ringi Kim, Boram Park*, where this is Conjecture 1.1.
> - [De88] Dean, N., Open problem, in Cycles and Rays. (1988).
> - [DeLeSa93] Dean, N. and Lesniak, L. and Saito, A., Cycles of length 0 modulo 4 in graphs.
>   Discrete Math. (1993), 133--139.
> - [ChSa94] Chen, G. and Saito, A., Graphs with a cycle of length divisible by three.
>   J. Combin. Theory Ser. B (1994), 277--292.
> - [LuMaZh26] Luo, Yufan and Ma, Jie and Zhao, Ziyuan, Dean's conjecture and cycles modulo k.
>   [arXiv:2601.13552](https://arxiv.org/abs/2601.13552) (2026).

*Quoted from [FormalConjectures/Arxiv/2605.02731/DeanCycles.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2605.02731/DeanCycles.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 2 open and 3 solved. It also has 2 test statements, counted here but not shown.

## `Arxiv.«2605.02731».dean_conjecture`

Open: stated without proof.

> **Conjecture 1.1 (Dean, 1988).** For every integer $k \geq 3$, every finite simple graph with
> minimum degree at least $k$ contains a cycle whose length is divisible by $k$.
>
> A cycle has length at least `3`, so the divisor is never `0` and the statement is not
> satisfied for a trivial reason. `SimpleGraph.minDegree` is `0` on a graph with no vertices and
> on a graph with no edges, so the hypothesis excludes both.

```lean
theorem dean_conjecture :
    ∀ (k : ℕ), 3 ≤ k → ∀ (V : Type) [Fintype V] [DecidableEq V]
      (G : SimpleGraph V) [DecidableRel G.Adj], k ≤ G.minDegree →
        ∃ m ∈ G.cycleLengths, k ∣ m
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/2605.02731/DeanCycles.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2605.02731/DeanCycles.lean#L51).

## `Arxiv.«2605.02731».dean_conjecture.variants.five`

Open: stated without proof.

> The case $k = 5$. This is the only case of the conjecture that is still open.

```lean
theorem dean_conjecture.variants.five :
    ∀ (V : Type) [Fintype V] [DecidableEq V] (G : SimpleGraph V)
      [DecidableRel G.Adj], 5 ≤ G.minDegree → ∃ m ∈ G.cycleLengths, 5 ∣ m
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/2605.02731/DeanCycles.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2605.02731/DeanCycles.lean#L61).

## `Arxiv.«2605.02731».dean_conjecture.variants.three`

Solved: stated here without proof.

> The case $k = 3$, proved by Chen and Saito [ChSa94].

```lean
theorem dean_conjecture.variants.three {V : Type} [Fintype V] [DecidableEq V]
    (G : SimpleGraph V) [DecidableRel G.Adj] (hG : 3 ≤ G.minDegree) :
    ∃ m ∈ G.cycleLengths, 3 ∣ m
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/2605.02731/DeanCycles.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2605.02731/DeanCycles.lean#L70).

## `Arxiv.«2605.02731».dean_conjecture.variants.four`

Solved: stated here without proof.

> The case $k = 4$, proved by Dean, Lesniak and Saito [DeLeSa93].

```lean
theorem dean_conjecture.variants.four {V : Type} [Fintype V] [DecidableEq V]
    (G : SimpleGraph V) [DecidableRel G.Adj] (hG : 4 ≤ G.minDegree) :
    ∃ m ∈ G.cycleLengths, 4 ∣ m
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/2605.02731/DeanCycles.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2605.02731/DeanCycles.lean#L79).

## `Arxiv.«2605.02731».dean_conjecture.variants.six_le`

Solved: stated here without proof.

> The cases $k \geq 6$, proved by Luo, Ma and Zhao [LuMaZh26]. With [ChSa94] and [DeLeSa93] this
> leaves `dean_conjecture.variants.five` as the only open case.

```lean
theorem dean_conjecture.variants.six_le {V : Type} [Fintype V] [DecidableEq V] {k : ℕ}
    (hk : 6 ≤ k) (G : SimpleGraph V) [DecidableRel G.Adj] (hG : k ≤ G.minDegree) :
    ∃ m ∈ G.cycleLengths, k ∣ m
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/2605.02731/DeanCycles.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2605.02731/DeanCycles.lean#L89).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/2605.02731/DeanCycles.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2605.02731/DeanCycles.lean)
- [arxiv/2605.02731](https://arxiv.org/abs/2605.02731)
