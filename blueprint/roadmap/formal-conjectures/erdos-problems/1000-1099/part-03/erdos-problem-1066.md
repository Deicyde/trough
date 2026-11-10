---
declaration: theorem
origin: cited
lean: Erdos1066.erdos_1066, Erdos1066.erdos_1066.variants.pollack, Erdos1066.erdos_1066.variants.swanepoel, Erdos1066.erdos_1066.variants.pach_toth, Erdos1066.erdos_1066.variants.higher_dim
statement: formalized
---

# Erdős Problem 1066

> *References:*
> - [erdosproblems.com/1066](https://www.erdosproblems.com/1066)
> - [Cs98] Csizmadia, G., *On the independence number of minimum distance graphs*.
>   Discrete Comput. Geom. 20 (1998), 179-187.
> - [Er87b] Erdős, P., *Some combinatorial and metric problems in geometry*.
>   Intuitive geometry (Siófok, 1985) (1987), 167-177.
> - [PaTo96] Pach, J. and Tóth, G., *On the independence number of coin graphs*.
>   Geombinatorics 6 (1996), 30-33.
> - [Po85] Pollack, R., *Increasing the minimum distance of a set of points*.
>   J. Combin. Theory Ser. A 40 (1985), 450.
> - [Sw02] Swanepoel, K. J., *Independence numbers of planar contact graphs*.
>   Discrete Comput. Geom. 28 (2002), 649-670.

*Quoted from [FormalConjectures/ErdosProblems/1066.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1066.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1066](https://www.erdosproblems.com/1066).

The file states 5 research or textbook statements: 2 open and 3 solved. It also has 1 API statement, counted here but not shown.

## `Erdos1066.erdos_1066`

Open: stated without proof.

> Let $G$ be a graph given by $n$ points in $\mathbb{R}^2$, where any two distinct points are at
> least distance $1$ apart, and we draw an edge between two points if they are distance $1$ apart.
>
> Let $g(n)$ be maximal such that any such graph always has an independent set on at least $g(n)$
> vertices. Estimate $g(n)$, or perhaps $\lim \frac{g(n)}{n}$.
>
> We ask for $\lim g(n)/n$. The limit exists by Fekete's lemma, since placing two configurations far
> apart shows $g(a+b) \leq g(a)+g(b)$.

```lean
theorem erdos_1066 :
    Tendsto (fun n : ℕ ↦ (g n : ℝ) / n) atTop (𝓝 erdos_1066.answer)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1066.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1066.lean#L84).

## `Erdos1066.erdos_1066.variants.pollack`

Solved: stated here without proof.

> Such graphs are always planar. Pollack [Po85] noted that the Four colour theorem implies
> $g(n)\geq n/4$, since the graph is planar.

```lean
theorem erdos_1066.variants.pollack (n : ℕ) : (n : ℝ) / 4 ≤ (g n : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1066.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1066.lean#L93).

## `Erdos1066.erdos_1066.variants.swanepoel`

Solved: stated here without proof.

> This lower bound has been improved to $\frac{9}{35}n$ by Csizmadia [Cs98] and then
> $\frac{8}{31}n$ by Swanepoel [Sw02].

```lean
theorem erdos_1066.variants.swanepoel (n : ℕ) : (8 / 31 : ℝ) * n ≤ (g n : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1066.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1066.lean#L101).

## `Erdos1066.erdos_1066.variants.pach_toth`

Solved: stated here without proof.

> Erdős initially thought that $g(n)=n/3$, but Chung and Graham, and independently Pach, gave a
> construction that shows $g(n)\leq \frac{6}{19}n$. Pach and Tóth [PaTo96] improved this to
> $g(n)\leq \frac{5}{16}n$.
>
> Since $g(1) = 1$, the bound cannot hold for all $n$, so it is stated for infinitely many $n$,
> with $5/16$ replaced by $5/16+\varepsilon$ for every $\varepsilon > 0$.

```lean
theorem erdos_1066.variants.pach_toth :
    ∀ ε > (0 : ℝ), ∃ᶠ n : ℕ in atTop, (g n : ℝ) ≤ (5 / 16 + ε) * n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1066.lean, line 113](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1066.lean#L113).

## `Erdos1066.erdos_1066.variants.higher_dim`

Open: stated without proof.

> Pollack [Po85] also reports a letter from Erdős which poses the more general problem of, given
> $n$ points in $\mathbb{R}^d$ with minimum distance $1$, let $g_d(n)$ be maximal such that there
> always exist at least $g_d(n)$ many points which have minimum distance $>1$. Is it true that
> $g_d(n) \gg n/d$ in general?
>
> We read this with a constant independent of $d$ and $n$.

```lean
theorem erdos_1066.variants.higher_dim :
    ∃ c > (0 : ℝ), ∀ d n : ℕ, 1 ≤ d → c * n / d ≤ (gDim d n : ℝ)
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1066.lean, line 126](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1066.lean#L126).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1066.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1066.lean)
- [erdosproblems.com/1066](https://www.erdosproblems.com/1066)
