---
declaration: theorem
origin: cited
lean: Erdos150.erdos_150, Erdos150.erdos_150.variants.erdos_nesetril, Erdos150.erdos_150.variants.seymour, Erdos150.erdos_150.variants.lower_bound, Erdos150.erdos_150.variants.upper_bound
statement: formalized
---

# Erdős Problem 150

> *References:*
> - [erdosproblems.com/150](https://www.erdosproblems.com/150)
> - [Br24] Bradač, D., *On a question of Erdős and Nešetřil about minimal cuts in a graph*.
>   arXiv:2409.02974 (2024).
> - [Er88] Erdős, P., *Problems and results in combinatorial analysis and graph theory*.
>   Discrete Math. (1988), 81-92.
> - [FKTV08] Fomin, Fedor V. and Kratsch, Dieter and Todinca, Ioan and Villanger, Yngve, *Exact
>   algorithms for treewidth and minimum fill-in*. SIAM J. Comput. (2008), 1058-1079.
> - [FoVi12] Fomin, Fedor V. and Villanger, Yngve, *Treewidth computation and extremal
>   combinatorics*. Combinatorica (2012), 289-308.
> - [GaMa18] Gaspers, Serge and Mackenzie, Simon, *On the number of minimal separators in graphs*.
>   J. Graph Theory (2018), 653-659.

*Quoted from [FormalConjectures/ErdosProblems/150.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/150.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/150](https://www.erdosproblems.com/150).

The file states 5 research or textbook statements: 5 solved.

## `Erdos150.erdos_150`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos150.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos150.lean).

> A minimal cut of a graph is a minimal set of vertices whose removal disconnects the graph. Let
> $c(n)$ be the maximum number of minimal cuts a graph on $n$ vertices can have.
>
> Does $c(n)^{1/n}\to \alpha$ for some $\alpha <2$?
>
> It is unclear in [Er88] whether Erdős knew that the limit existed, which follows from a simple
> argument first given in the literature (to the best of my knowledge) by Bradač [Br24].
>
> That $\alpha<2$ was proved by Fomin, Kratsch, Todinca, and Villanger [FKTV08], who proved
> $\alpha \leq 1.7087$. This was independently studied by Bradač [Br24] (unaware of this earlier
> work), who proved that $\alpha \leq 2^{H(1/3)}\approx 1.8899$, where $H(\cdot)$ is the binary
> entropy function.
>
> This was formalized in Lean by Monticone using Aristotle.

```lean
theorem erdos_150 :
    ∃ α : ℝ, α < 2 ∧
      Tendsto (fun n : ℕ ↦ (maxMinimalCuts n : ℝ) ^ (1 / n : ℝ)) atTop (𝓝 α)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/150.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/150.lean#L73).

## `Erdos150.erdos_150.variants.erdos_nesetril`

Solved: stated here without proof.

> Asked by Erdős and Nešetřil, who also ask whether $c(3m+2)=3^m$.
>
> Note that the lower bound $1.4457\leq \alpha$ of Gaspers and Mackenzie [GaMa18] provides a
> negative answer to the above question of Erdős and Nešetřil.

```lean
theorem erdos_150.variants.erdos_nesetril :
    ¬ ∀ m : ℕ, maxMinimalCuts (3 * m + 2) = 3 ^ m
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/150.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/150.lean#L85).

## `Erdos150.erdos_150.variants.seymour`

Solved: stated here without proof.

> Seymour observed that $c(3m+2)\geq 3^m$, as seen by the graph of $m$ independent paths of length
> $4$ joining two vertices.

```lean
theorem erdos_150.variants.seymour (m : ℕ) : 3 ^ m ≤ maxMinimalCuts (3 * m + 2)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/150.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/150.lean#L94).

## `Erdos150.erdos_150.variants.lower_bound`

Solved: stated here without proof.

> The current best-known bounds on $\alpha$ are
>
> $$1.4457\leq \alpha \leq \frac{1+\sqrt{5}}{2}\approx 1.618.$$
>
> The lower bound is due to Gaspers and Mackenzie [GaMa18].

```lean
theorem erdos_150.variants.lower_bound (α : ℝ)
    (hα : Tendsto (fun n : ℕ ↦ (maxMinimalCuts n : ℝ) ^ (1 / n : ℝ)) atTop (𝓝 α)) :
    1.4457 ≤ α
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/150.lean, line 103](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/150.lean#L103).

## `Erdos150.erdos_150.variants.upper_bound`

Solved: stated here without proof.

> The current best-known bounds on $\alpha$ are
>
> $$1.4457\leq \alpha \leq \frac{1+\sqrt{5}}{2}\approx 1.618.$$
>
> The upper bound is due to Fomin and Villanger [FoVi12] (with a simpler proof in [GaMa18]).

```lean
theorem erdos_150.variants.upper_bound (α : ℝ)
    (hα : Tendsto (fun n : ℕ ↦ (maxMinimalCuts n : ℝ) ^ (1 / n : ℝ)) atTop (𝓝 α)) :
    α ≤ (1 + Real.sqrt 5) / 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/150.lean, line 114](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/150.lean#L114).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/150.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/150.lean)
- [erdosproblems.com/150](https://www.erdosproblems.com/150)
