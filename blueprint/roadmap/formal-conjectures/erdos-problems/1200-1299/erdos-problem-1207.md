---
declaration: theorem
origin: cited
lean: Erdos1207.erdos_1207
statement: formalized
---

# Erdős Problem 1207

> *References:*
> - [erdosproblems.com/1207](https://www.erdosproblems.com/1207)
> - [BMP05] Brass, Peter and Moser, William and Pach, János, *Research problems in discrete geometry*.
>   (2005), xii+499.
> - [Er80] Erdős, Paul, *A survey of problems in combinatorial number theory*. Ann. Discrete Math.
>   (1980), 89-115.
> - [LPZ26] Lee, S., Pohoata, C., and Zhu, D. G., *The Minkowski grid has robustly many repeated
>   distances*. [arXiv:2607.05374](https://arxiv.org/abs/2607.05374) (2026).
> - [PaTa02] Pach, János and Tardos, Gábor, *Isosceles triangles determined by a planar point set*.
>   Graphs Combin. (2002), 769--779.

*Quoted from [FormalConjectures/ErdosProblems/1207.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1207.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1207](https://www.erdosproblems.com/1207).

The file states 1 research or textbook statement: 1 solved.

## `Erdos1207.erdos_1207`

Solved: stated here without proof.

> Let $P_d(n)$ be such that in any set of $n$ points in $\mathbb{R}^d$ there exist at least $P_d(n)$ many points which do not contain an isosceles triangle. Estimate $P_d(n)$ - in particular, is it true that
>
> $$P_2(n)\lt n^{1-c}$$
>
> for some constant $c>0$?
>
> Lee, Pohoata, and Zhu [LPZ26] proved the stated planar bound. Their isosceles-free subsets
> also exclude degenerate triangles of equally spaced collinear points.

```lean
theorem erdos_1207 :
    ∃ c > (0 : ℝ), ∀ᶠ n : ℕ in atTop, (P 2 n : ℝ) < (n : ℝ) ^ (1 - c)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1207.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1207.lean#L57).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1207.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1207.lean)
- [erdosproblems.com/1207](https://www.erdosproblems.com/1207)
