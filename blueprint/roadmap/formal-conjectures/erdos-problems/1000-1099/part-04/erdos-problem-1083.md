---
declaration: theorem
origin: cited
lean: Erdos1083.erdos_1083
statement: formalized
---

# Erdős Problem 1083

> *References:*
> - [erdosproblems.com/1083](https://www.erdosproblems.com/1083)
> - [APST04] Aronov, Boris and Pach, János and Sharir, Micha and Tardos, Gábor, *Distinct distances in
>   three and higher dimensions*. Combin. Probab. Comput. (2004), 283--293.
> - [CEGSW90] Clarkson, Kenneth L. and Edelsbrunner, Herbert and Guibas, Leonidas J. and Sharir, Micha
>   and Welzl, Emo, *Combinatorial complexity bounds for arrangements of curves and spheres*. Discrete
>   Comput. Geom. (1990), 99--160.
> - [Er46b] Erdős, P., *On sets of distances of {$n$} points*. Amer. Math. Monthly (1946), 248--250.
> - [SoVu08] Solymosi, József and Vu, Van H., *Near optimal bounds for the {E}rdős distinct distances
>   problem in high dimensions*. Combinatorica (2008), 113--125.

*Quoted from [FormalConjectures/ErdosProblems/1083.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1083.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1083](https://www.erdosproblems.com/1083).

The file states 1 research or textbook statement: 1 open.

## `Erdos1083.erdos_1083`

Open: stated without proof.

> Let $d\geq 3$, and let $f_d(n)$ be the minimal $m$ such that every set of $n$ points in $\mathbb{R}^d$ determines at least $m$ distinct distances. Estimate $f_d(n)$ - in particular, is it true that
>
> $$f_d(n)=n^{\frac{2}{d}-o(1)}?$$

```lean
theorem erdos_1083 :
    ∀ d : ℕ, 3 ≤ d → ∃ o : ℕ → ℝ, o =o[atTop] (1 : ℕ → ℝ) ∧
      ∀ᶠ n : ℕ in atTop,
        (minimalDistinctDistances (ℝ^d) n : ℝ) = (n : ℝ) ^ ((2 : ℝ) / (d : ℝ) - o n)
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1083.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1083.lean#L46).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1083.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1083.lean)
- [erdosproblems.com/1083](https://www.erdosproblems.com/1083)
