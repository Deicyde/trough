---
declaration: theorem
origin: cited
lean: Erdos712.erdos_712, Erdos712.erdos_712.variants.limit_exists, Erdos712.erdos_712.variants.graph_case, Erdos712.erdos_712.variants.graph_case_div_sq
statement: formalized
---

# Erdős Problem 712

> *References:*
> - [erdosproblems.com/712](https://www.erdosproblems.com/712)
> - [Er81] Erdős, P., On the combinatorial problems which I would most like to see solved.
>   Combinatorica (1981), 25-42.

*Quoted from [FormalConjectures/ErdosProblems/712.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/712.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/712](https://www.erdosproblems.com/712).

The file states 4 research or textbook statements: 1 open, 2 solved and 1 textbook result.

## `Erdos712.erdos_712`

Open: stated without proof.

> Determine, for any $k>r>2$, the limiting value as $n\to\infty$ of
>
> $$\frac{\mathrm{ex}_r(n,K_k^r)}{\binom{n}{r}},$$
>
> where $\mathrm{ex}_r(n,K_k^r)$ is the largest number of $r$-edges which can placed on $n$ vertices
> so that there exists no set of $k$ vertices which is covered by all $\binom{k}{r}$ possible
> $r$-edges.

```lean
theorem erdos_712 :
    ∀ k r : ℕ, 2 < r → r < k →
      Tendsto (fun n ↦ (Hypergraph.cliqueExtremalNumber n r k : ℝ) / n.choose r)
        atTop (𝓝 (erdos_712.answer k r))
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/712.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/712.lean#L46).

## `Erdos712.erdos_712.variants.limit_exists`

Textbook result, stated without proof.

> The normalized extremal numbers have a limit in $[0,1]$. This existence result does
> not determine the value asked for in Erdős Problem 712.

```lean
theorem erdos_712.variants.limit_exists (r k : ℕ) :
    ∃ π ∈ Set.Icc (0 : ℝ) 1,
      Tendsto (fun n : ℕ ↦ (Hypergraph.cliqueExtremalNumber n r k : ℝ) / n.choose r)
        atTop (𝓝 π)
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/712.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/712.lean#L56).

## `Erdos712.erdos_712.variants.graph_case`

Solved: stated here without proof.

> Turán's theorem gives the graph case:
> $\mathrm{ex}_2(n,K_k)/\binom{n}{2}\to 1-1/(k-1)$.

```lean
theorem erdos_712.variants.graph_case (k : ℕ) (hk : 2 ≤ k) :
    Tendsto (fun n : ℕ ↦ (Hypergraph.cliqueExtremalNumber n 2 k : ℝ) / n.choose 2)
      atTop (𝓝 (1 - 1 / ((k : ℝ) - 1)))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/712.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/712.lean#L65).

## `Erdos712.erdos_712.variants.graph_case_div_sq`

Solved: stated here without proof.

> With denominator $n^2$, Turán's graph limit is
> $\frac12(1-1/(k-1))$. The factor $\frac12$ comes from the normalization.

```lean
theorem erdos_712.variants.graph_case_div_sq (k : ℕ) (hk : 2 ≤ k) :
    Tendsto (fun n : ℕ ↦ (Hypergraph.cliqueExtremalNumber n 2 k : ℝ) / (n : ℝ) ^ 2)
      atTop (𝓝 ((1 / 2) * (1 - 1 / ((k : ℝ) - 1))))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/712.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/712.lean#L73).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/712.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/712.lean)
- [erdosproblems.com/712](https://www.erdosproblems.com/712)
