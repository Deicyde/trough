---
declaration: theorem
origin: cited
lean: Erdos162.erdos_162, Erdos162.erdos_162.variants.bounds, Erdos162.erdos_162.variants.half
statement: formalized
---

# Erdős Problem 162

> *References:*
> - [erdosproblems.com/162](https://www.erdosproblems.com/162)
> - [Er90b] Erdős, Paul, *Problems and results on graphs and hypergraphs: similarities and
>   differences*. Mathematics of Ramsey theory (1990), 12-28.

*Quoted from [FormalConjectures/ErdosProblems/162.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/162.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/162](https://www.erdosproblems.com/162).

The file states 3 research or textbook statements: 1 open, 1 solved and 1 textbook result. It also has 2 API statements, counted here but not shown.

## `Erdos162.erdos_162`

Open: stated without proof.

> Let $\alpha > 0$ and $n \geq 1$. Let $F(n,\alpha)$ be the largest $k$ such that there exists some
> 2-colouring of the edges of $K_n$ in which any induced subgraph $H$ on at least $k$ vertices
> contains more than $\alpha\binom{|H|}{2}$ many edges of each colour.
>
> Prove that for every fixed $0 \leq \alpha \leq 1/2$, as $n \to \infty$,
> $F(n,\alpha) \sim c_\alpha \log n$ for some constant $c_\alpha$.
>
> We require $\alpha < 1/2$: at $\alpha = 1/2$ no colouring works for any `k ≤ n`
> (see `erdos_162.variants.half`).

```lean
theorem erdos_162 (α : ℝ) (h0 : 0 ≤ α) (h1 : α < 1 / 2) :
    ∃ c : ℝ, (fun n : ℕ ↦ (F n α : ℝ)) ~[atTop] (fun n : ℕ ↦ c * Real.log n)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/162.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/162.lean#L65).

## `Erdos162.erdos_162.variants.bounds`

Solved: stated here without proof.

> It is easy to show with the probabilistic method that there exist $c_1(\alpha), c_2(\alpha)$ such
> that $c_1(\alpha)\log n < F(n,\alpha) < c_2(\alpha)\log n$.

```lean
theorem erdos_162.variants.bounds (α : ℝ) (h0 : 0 ≤ α) (h1 : α < 1 / 2) :
    ∃ c₁ c₂ : ℝ, 0 < c₁ ∧ c₁ < c₂ ∧ ∀ᶠ n : ℕ in atTop,
      c₁ * Real.log n < F n α ∧ (F n α : ℝ) < c₂ * Real.log n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/162.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/162.lean#L74).

## `Erdos162.erdos_162.variants.half`

Textbook result, proved here.

> At $\alpha = 1/2$ the two colour counts in $H$ add up to $\binom{|H|}{2}$, so both cannot exceed
> half of it. Hence $F(n, 1/2) = n + 1$, and the claim fails at $\alpha = 1/2$.

```lean
theorem erdos_162.variants.half (n : ℕ) : F n (1 / 2) = n + 1
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/162.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/162.lean#L84).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/162.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/162.lean)
- [erdosproblems.com/162](https://www.erdosproblems.com/162)
