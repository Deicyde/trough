---
declaration: theorem
origin: cited
lean: Erdos766.erdos_766.parts.i, Erdos766.erdos_766.parts.ii, Erdos766.erdos_766.variants.dirac_erdos, Erdos766.erdos_766.variants.minExtremalNumber_estimate, Erdos766.erdos_766.variants.minExtremalNumber_strictMonoOn
statement: formalized
---

# Erdős Problem 766

> *References:*
> - [erdosproblems.com/766](https://www.erdosproblems.com/766)
> - [Er64c] Erdős, P., *Extremal problems in graph theory*. Theory of Graphs and its Applications
>   (Proc. Sympos. Smolenice, 1963) (1964), 29-36.
>   [PDF](https://www.renyi.hu/~p_erdos/1964-06.pdf)

*Quoted from [FormalConjectures/ErdosProblems/766.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/766.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/766](https://www.erdosproblems.com/766).

The file states 5 research or textbook statements: 4 open and 1 solved. It also has 3 test statements and 2 API statements, counted here but not shown.

## `Erdos766.erdos_766.parts.i`

Open: stated without proof.

> Let $f(n;k,l)=\min \mathrm{ex}(n;G)$, where $G$ ranges over all graphs with $k$ vertices and $l$
> edges.
>
> Give good estimates for $f(n;k,l)$ in the range $k\lt l\leq k^2/4$.
>
> In [Er64c, p. 33] this question is asked for $f_1(n;k,l)$ (`Erdos766.forcingNumber`), which
> forces at least one graph with $k$ vertices and $l$ edges rather than one fixed graph; we follow
> the source. The question for the function of erdosproblems.com is
> `Erdos766.erdos_766.variants.minExtremalNumber_estimate`.

```lean
theorem erdos_766.parts.i :
    ∀ k l : ℕ, k < l → l ≤ k ^ 2 / 4 →
      (fun n ↦ (forcingNumber n k l : ℝ)) =Θ[atTop] erdos_766.parts.i.answer k l
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/766.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/766.lean#L105).

## `Erdos766.erdos_766.parts.ii`

Open: stated without proof.

> For fixed $k$ and large $n$ is $f(n;k,l)$ a strictly monotone function of $l$?
>
> As in `Erdos766.erdos_766.parts.i`, $f$ is $f_1$ of [Er64c], and we use the range
> $k\lt l\leq k^2/4$ in which the question is asked there; here `k ^ 2 / 4` is $\lfloor k^2/4\rfloor$.
> The question for the function of erdosproblems.com is
> `Erdos766.erdos_766.variants.minExtremalNumber_strictMonoOn`.

```lean
theorem erdos_766.parts.ii :
    ∀ k : ℕ, ∀ᶠ n : ℕ in atTop,
      StrictMonoOn (forcingNumber n k) (Set.Ioc k (k ^ 2 / 4))
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/766.lean, line 119](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/766.lean#L119).

## `Erdos766.erdos_766.variants.dirac_erdos`

Solved: stated here without proof.

> Dirac and Erdős proved independently that when $l=\lfloor k^2/4\rfloor+1$
>
> $$f(n;k,l)\leq \lfloor n^2/4\rfloor+1.$$
>
> [Er64c, p. 34] states this for every $k \leq n$. We assume $k \geq 3$, since for $k \leq 2$ there
> is no graph with $k$ vertices and $\lfloor k^2/4\rfloor+1$ edges.

```lean
theorem erdos_766.variants.dirac_erdos (n k : ℕ) (hk : 3 ≤ k) (hkn : k ≤ n) :
    forcingNumber n k (k ^ 2 / 4 + 1) ≤ n ^ 2 / 4 + 1
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/766.lean, line 132](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/766.lean#L132).

## `Erdos766.erdos_766.variants.minExtremalNumber_estimate`

Open: stated without proof.

> The estimate question of `Erdos766.erdos_766.parts.i` for the function
> $\min \mathrm{ex}(n;G)$ of erdosproblems.com (`Erdos766.minExtremalNumber`).

```lean
theorem erdos_766.variants.minExtremalNumber_estimate :
    ∀ k l : ℕ, k < l → l ≤ k ^ 2 / 4 →
      (fun n ↦ ((minExtremalNumber n k l).toNat : ℝ)) =Θ[atTop]
        erdos_766.variants.minExtremalNumber_estimate.answer k l
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/766.lean, line 143](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/766.lean#L143).

## `Erdos766.erdos_766.variants.minExtremalNumber_strictMonoOn`

Open: stated without proof.

> The monotonicity question of `Erdos766.erdos_766.parts.ii` for the function
> $\min \mathrm{ex}(n;G)$ of erdosproblems.com (`Erdos766.minExtremalNumber`).

```lean
theorem erdos_766.variants.minExtremalNumber_strictMonoOn :
    ∀ k : ℕ, ∀ᶠ n : ℕ in atTop,
      StrictMonoOn (minExtremalNumber n k) (Set.Ioc k (k ^ 2 / 4))
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/766.lean, line 154](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/766.lean#L154).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/766.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/766.lean)
- [erdosproblems.com/766](https://www.erdosproblems.com/766)
