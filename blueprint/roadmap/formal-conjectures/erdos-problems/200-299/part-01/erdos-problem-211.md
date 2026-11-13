---
declaration: theorem
origin: cited
lean: Erdos211.erdos_211.variants.one_sixth, Erdos211.erdos_211.variants.sharpness, Erdos211.erdos_211, Erdos211.erdos_211.variants.quadratic
statement: formalized
---

# Erdős Problem 211

> *References:*
> - [erdosproblems.com/211](https://www.erdosproblems.com/211)
> - [Be83] Beck, József, *On the lattice property of the plane and some problems of Dirac,
>   Motzkin and Erdős in combinatorial geometry*. Combinatorica (1983), 281-297.
> - [SzTr83] Szemerédi, Endre and Trotter, Jr., William T., *Extremal problems in discrete
>   geometry*. Combinatorica (1983), 381-392.
> - [Er84] Erdős, P., *Research problems*. Period. Math. Hungar. (1984), 101-103.
> - [BGS74] Burr, Stefan A. and Grünbaum, Branko and Sloane, N. J. A., *The orchard problem*.
>   Geometriae Dedicata (1974), 397-424.
> - [FuPa84] Füredi, Z. and Palásti, I., *Arrangements of lines with a large number of triangles*.
>   Proc. Amer. Math. Soc. (1984), 561-566.

*Quoted from [FormalConjectures/ErdosProblems/211.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/211.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/211](https://www.erdosproblems.com/211).

The file states 4 research or textbook statements: 1 open and 3 solved. It also has 12 API statements, counted here but not shown.

## `Erdos211.erdos_211.variants.one_sixth`

Open: stated without proof.

> Erdős speculates that there are at least $(1+o(1))kn/6$ determined lines [Er84].
> The asymptotic bound is uniform over $1 \leq k < n$.

```lean
theorem erdos_211.variants.one_sixth :
  ∀ ε : ℝ, 0 < ε → ∃ N : ℕ, ∀ (n k : ℕ), N ≤ n → 1 ≤ k → k < n →
    ∀ s : Finset ℝ², s.card = n →
      (∀ L : AffineSubspace ℝ ℝ², IsLine L → (s.filter fun p => p ∈ L).card ≤ n - k) →
      (1 - ε) / 6 * (k : ℝ) * (n : ℝ) ≤ ((determinedLines s).card : ℝ)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/211.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/211.lean#L67).

## `Erdos211.erdos_211.variants.sharpness`

Solved: stated here without proof.

> There are arbitrarily large configurations with no four collinear points and
> $\sim n^2/6$ three-point lines, constructed by Burr, Grünbaum, and Sloane [BGS74]
> and Füredi and Palásti [FuPa84]. The index need not equal the number of points.

```lean
theorem erdos_211.variants.sharpness :
  ∃ s : ℕ → Finset ℝ²,
    Tendsto (fun i => (s i).card) atTop atTop ∧
    (∀ (i : ℕ) (L : AffineSubspace ℝ ℝ²), IsLine L →
      ((s i).filter fun p => p ∈ L).card ≤ 3) ∧
    Tendsto (fun i =>
      (((determinedLines (s i)).filter fun L => ((s i).filter fun p => p ∈ L).card = 3).card : ℝ) /
        ((s i).card : ℝ) ^ 2) atTop (nhds (1 / 6 : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/211.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/211.lean#L79).

## `Erdos211.erdos_211`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos211.lean#L900](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos211.lean#L900).

> Let $1\leq k\lt n$. Given $n$ points in $\mathbb{R}^2$, at most $n-k$ on any line,
> there are $\gg kn$ many lines which contain at least two points.
> Solved by Beck [Be83] and Szemerédi and Trotter [SzTr83].

```lean
theorem erdos_211 : MainBound
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/211.lean, line 266](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/211.lean#L266).

## `Erdos211.erdos_211.variants.quadratic`

Proved here.

> Given any $2n$ points with at most $n$ on a line there are $\gg n^2$ many lines
> formed by the points. Solved by Beck [Be83] and Szemerédi and Trotter [SzTr83].

```lean
theorem erdos_211.variants.quadratic : QuadraticBound
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/211.lean, line 272](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/211.lean#L272).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/211.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/211.lean)
- [erdosproblems.com/211](https://www.erdosproblems.com/211)
