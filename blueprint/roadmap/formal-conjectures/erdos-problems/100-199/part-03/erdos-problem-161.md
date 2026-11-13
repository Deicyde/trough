---
declaration: theorem
origin: cited
lean: Erdos161.erdos_161.parts.i, Erdos161.erdos_161.parts.ii
statement: formalized
---

# Erdős Problem 161

> *References:*
> - [erdosproblems.com/161](https://www.erdosproblems.com/161)
> - [CFS11] Conlon, David and Fox, Jacob and Sudakov, Benny, Large almost monochromatic subsets in
>   hypergraphs. Israel J. Math. (2011), 423--432.
> - [Er90b] Erdős, Paul, Problems and results on graphs and hypergraphs: similarities and differences
>   . Mathematics of Ramsey theory (1990), 12-28.

*Quoted from [FormalConjectures/ErdosProblems/161.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/161.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/161](https://www.erdosproblems.com/161).

The file states 2 research or textbook statements: 2 open.

## `Erdos161.erdos_161.parts.i`

Open: stated without proof.

> Let $\alpha\in[0,1/2)$ and $n,t\geq 1$. Let $F^{(t)}(n,\alpha)$ be the smallest $m$ such that we can
> $2$-colour the edges of the complete $t$-uniform hypergraph on $n$ vertices such that if $X\subseteq
> [n]$ with $\lvert X\rvert \geq m$ then there are at least $\alpha \binom{\lvert X\rvert}{t}$ many
> $t$-subsets of $X$ of each colour. For fixed $n,t$ as we change $\alpha$ from $0$ to $1/2$ does
> $F^{(t)}(n,\alpha)$ increase continuously or are there jumps? Only one jump?
>
> Here growth is compared up to constant factors as $n\to\infty$. At $\alpha=0$,
> each color must occur, following the source's Ramsey convention.

```lean
theorem erdos_161.parts.i :
    ∀ t : ℕ, 1 ≤ t →
      {p | p.1 ∈ Set.Ico (0 : ℝ) (1 / 2) ∧ p.2 ∈ Set.Ico (0 : ℝ) (1 / 2) ∧
        (fun n ↦ (Hypergraph.balancedColoringThreshold n t p.1 : ℝ)) =Θ[atTop]
          (fun n ↦ (Hypergraph.balancedColoringThreshold n t p.2 : ℝ))} =
        erdos_161.parts.i.answer t
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/161.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/161.lean#L50).

## `Erdos161.erdos_161.parts.ii`

Open: stated without proof.

> For fixed $t\geq 3$, do all positive densities below $1/2$ give the same asymptotic order?

```lean
theorem erdos_161.parts.ii :
    ∀ t : ℕ, 3 ≤ t → ∀ α β : ℝ,
    0 < α → α < 1 / 2 → 0 < β → β < 1 / 2 →
    (fun n ↦ (Hypergraph.balancedColoringThreshold n t α : ℝ)) =Θ[atTop]
      (fun n ↦ (Hypergraph.balancedColoringThreshold n t β : ℝ))
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/161.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/161.lean#L62).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/161.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/161.lean)
- [erdosproblems.com/161](https://www.erdosproblems.com/161)
