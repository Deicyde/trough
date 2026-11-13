---
declaration: theorem
origin: cited
lean: Erdos827.erdos_827, Erdos827.erdos_827.variants.martinez_roldan_pensado, Erdos827.erdos_827.variants.n_four_le, Erdos827.erdos_827.variants.n_five_le
statement: formalized
---

# Erdős Problem 827

> *References:*
> - [erdosproblems.com/827](https://www.erdosproblems.com/827)
> - [Er75h] Erdős, P., *Some problems on elementary geometry*. Austral. Math. Soc. Gaz. 2 (1975),
>   2-3.
> - [Er78c] Erdős, P., *Some more problems on elementary geometry*. Austral. Math. Soc. Gaz. 5
>   (1978), 52-54.
> - [MaRo15] Martínez, L. and Roldán-Pensado, E., *Points defining triangles with distinct
>   circumradii*. Acta Math. Hungar. 145 (2015), 136-141.
>   [arXiv:1402.6276](https://arxiv.org/abs/1402.6276)

*Quoted from [FormalConjectures/ErdosProblems/827.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/827.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/827](https://www.erdosproblems.com/827).

The file states 4 research or textbook statements: 1 open and 3 solved. It also has 1 API statement, counted here but not shown.

## `Erdos827.erdos_827`

Open: stated without proof.

> Let $n_k$ be minimal such that if $n_k$ points in $\mathbb{R}^2$ are in general position then
> there exists a subset of $k$ points such that all $\binom{k}{3}$ triples determine circles of
> different radii.
>
> Determine $n_k$.
>
> General position means that no three points are collinear and no four are concyclic, as in
> [Er75h] (quoted in [MaRo15]).

```lean
theorem erdos_827 : n = erdos_827.answer
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/827.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/827.lean#L81).

## `Erdos827.erdos_827.variants.martinez_roldan_pensado`

Solved: stated here without proof.

> In [Er78c] Erdős gave an argument for $n_k \leq k+2\binom{k-1}{2}\binom{k-1}{3}$, but this
> argument is incorrect, as explained by Martínez and Roldán-Pensado [MaRo15], who give a corrected
> argument that proves $n_k\ll k^9$.
>
> [MaRo15, Theorem 1.1] assumes only that no four points lie on a line or a circle. That class
> contains the sets in general position, so the bound holds for $n_k$ as defined here.

```lean
theorem erdos_827.variants.martinez_roldan_pensado :
    (fun k : ℕ ↦ (n k : ℝ)) =O[atTop] fun k : ℕ ↦ (k : ℝ) ^ 9
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/827.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/827.lean#L93).

## `Erdos827.erdos_827.variants.n_four_le`

Solved: stated here without proof.

> Martínez and Roldán-Pensado [MaRo15, Theorem 1.2] show that $n_4 \leq 9$.

```lean
theorem erdos_827.variants.n_four_le : n 4 ≤ 9
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/827.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/827.lean#L101).

## `Erdos827.erdos_827.variants.n_five_le`

Solved: stated here without proof.

> Martínez and Roldán-Pensado [MaRo15, Theorem 1.2] show that $n_5 \leq 37$.

```lean
theorem erdos_827.variants.n_five_le : n 5 ≤ 37
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/827.lean, line 108](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/827.lean#L108).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/827.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/827.lean)
- [erdosproblems.com/827](https://www.erdosproblems.com/827)
