---
declaration: theorem
origin: cited
lean: Erdos751.erdos_751.parts.i, Erdos751.erdos_751.parts.ii, Erdos751.erdos_751.variants.bondy_vince, Erdos751.erdos_751.variants.finite
statement: formalized
---

# Erdős Problem 751

> *References:*
> - [erdosproblems.com/751](https://www.erdosproblems.com/751)
> - [Er94b] Erdős, Paul, Some problems in number theory, combinatorics and combinatorial geometry.
>   Math. Pannon. (1994), 261--269.
> - [BoVi98] Bondy, J. A. and Vince, A., Cycles in a graph whose lengths differ by one or two.
>   J. Graph Theory (1998), 11--15.

*Quoted from [FormalConjectures/ErdosProblems/751.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/751.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/751](https://www.erdosproblems.com/751).

The file states 4 research or textbook statements: 4 solved.

## `Erdos751.erdos_751.parts.i`

Solved: stated here without proof.

> Let $G$ be a graph with chromatic number $\chi(G)=4$. If $m_1\lt m_2\lt \cdots$ are the lengths of the
> cycles in $G$ then can $\min(m_{i+1}-m_i)$ be arbitrarily large?
>
> The answer is no: Bondy and Vince [BoVi98] proved that every graph with minimum degree at least $3$
> has two cycles whose lengths differ by at most $2$, and hence the same is true for every graph with
> chromatic number $4$.
>
> `erdos_751.variants.finite` below carries the Lean proof. It assumes a finite vertex type,
> where this quantifies over any `V : Type`, and the two are joined by de Bruijn-Erdős: a graph
> that is not $3$-colourable has a finite subgraph that is not $3$-colourable, and cycles of that
> subgraph are cycles of the whole. Mathlib does not have de Bruijn-Erdős, so that step is not
> formalised here.

```lean
theorem erdos_751.parts.i :
    ¬ ∀ k : ℕ, ∃ (V : Type) (G : SimpleGraph V), G.chromaticNumber = 4 ∧
      ∀ m ∈ G.cycleLengths, ∀ m' ∈ G.cycleLengths, m < m' → m + k ≤ m'
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/751.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/751.lean#L50).

## `Erdos751.erdos_751.parts.ii`

Solved: stated here without proof.

> Let $G$ be a graph with chromatic number $\chi(G)=4$. If $m_1\lt m_2\lt \cdots$ are the lengths of the
> cycles in $G$ then can $\min(m_{i+1}-m_i)$ be arbitrarily large? Can this happen if the girth of
> $G$ is large?
>
> The answer is no: Bondy and Vince [BoVi98] proved that every graph with minimum degree at least $3$
> has two cycles whose lengths differ by at most $2$, and hence the same is true for every graph with
> chromatic number $4$.

```lean
theorem erdos_751.parts.ii :
    ¬ ∀ k g : ℕ, ∃ (V : Type) (G : SimpleGraph V), G.chromaticNumber = 4 ∧ g ≤ G.girth ∧
      ∀ m ∈ G.cycleLengths, ∀ m' ∈ G.cycleLengths, m < m' → m + k ≤ m'
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/751.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/751.lean#L65).

## `Erdos751.erdos_751.variants.bondy_vince`

Solved: stated here without proof.

> Bondy and Vince [BoVi98] proved that every graph with minimum degree at least $3$ has two cycles
> whose lengths differ by at most $2$.

```lean
theorem erdos_751.variants.bondy_vince {V : Type*} [Fintype V] (G : SimpleGraph V)
    [DecidableRel G.Adj] (hG : 3 ≤ G.minDegree) :
    ∃ m ∈ G.cycleLengths, ∃ m' ∈ G.cycleLengths, m < m' ∧ m' ≤ m + 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/751.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/751.lean#L75).

## `Erdos751.erdos_751.variants.finite`

Solved: stated here; a Lean proof is at [https://github.com/SpringSense-Innovation-Institute/ai-for-math-lean/blob/ae3ead960a494cf81b28541c477e50997cb03999/erdos-problems/erdos751/Erdos751/Main.lean#L40-L69](https://github.com/SpringSense-Innovation-Institute/ai-for-math-lean/blob/ae3ead960a494cf81b28541c477e50997cb03999/erdos-problems/erdos751/Erdos751/Main.lean#L40-L69).

> The finite case of `erdos_751.parts.i`, which is what the Lean proof establishes: a finite graph
> with chromatic number at least $4$ has two cycles whose lengths differ by $1$ or $2$.
>
> The proof reaches this through a $4$-critical subgraph, which supplies the $2$-connectivity and
> the vertex count its Bondy-Vince step needs on top of minimum degree $3$. Those extra hypotheses
> are why it does not also settle `erdos_751.variants.bondy_vince`, which asks for minimum degree
> $3$ alone.
>
> This was formalized in Lean by SpringSense Innovation Institute using ChatGPT.

```lean
theorem erdos_751.variants.finite {V : Type*} [Fintype V] (G : SimpleGraph V)
    [DecidableRel G.Adj] (hG : (4 : ℕ∞) ≤ G.chromaticNumber) :
    ∃ m ∈ G.cycleLengths, ∃ m' ∈ G.cycleLengths, m < m' ∧ m' ≤ m + 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/751.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/751.lean#L94).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/751.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/751.lean)
- [erdosproblems.com/751](https://www.erdosproblems.com/751)
