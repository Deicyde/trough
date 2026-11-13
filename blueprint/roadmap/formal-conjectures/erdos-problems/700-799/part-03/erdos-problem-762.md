---
declaration: theorem
origin: cited
lean: Erdos762.erdos_762, Erdos762.erdos_762.variants.bounded_clique_number, Erdos762.erdos_762.variants.steiner
statement: formalized
---

# Erdős Problem 762

> *References:*
> - [erdosproblems.com/762](https://www.erdosproblems.com/762)
> - [EGS90] Erdős, Paul and Gimbel, John and Straight, H. Joseph, *Chromatic number versus
>   cochromatic number in graphs with bounded clique number*. European J. Combin. (1990), 235-240.
> - [St24b] R. Steiner, *On the difference between the chromatic and cochromatic number*.
>   arXiv:2408.02400 (2024).

*Quoted from [FormalConjectures/ErdosProblems/762.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/762.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/762](https://www.erdosproblems.com/762).

The file states 3 research or textbook statements: 3 solved.

## `Erdos762.erdos_762`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos762.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos762.lean).

> The cochromatic number of $G$, denoted by $\zeta(G)$, is the minimum number of colours needed to
> colour the vertices of $G$ such that each colour class induces either a complete graph or empty
> graph.
>
> Is it true that if $G$ has no $K_5$ and $\zeta(G)\geq 4$ then $\chi(G) \leq \zeta(G)+2$?
>
> This has been disproved by Steiner [St24b], who constructed a graph $G$ with $\omega(G)=4$,
> $\zeta(G)=4$, and $\chi(G)=7$.

```lean
theorem erdos_762 :
    ¬ ∀ (V : Type*) [Fintype V] (G : SimpleGraph V),
      G.CliqueFree 5 → 4 ≤ G.cochromaticNumber →
        G.chromaticNumber ≤ G.cochromaticNumber + 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/762.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/762.lean#L47).

## `Erdos762.erdos_762.variants.bounded_clique_number`

Solved: stated here without proof.

> A conjecture of Erdős, Gimbel, and Straight [EGS90], who proved that for every $n>2$ there exists
> some $f(n)$ such that if $G$ contains no clique on $n$ vertices then $\chi(G)\leq \zeta(G)+f(n)$.

```lean
theorem erdos_762.variants.bounded_clique_number (n : ℕ) (hn : 2 < n) :
    ∃ f : ℕ, ∀ (V : Type*) [Fintype V] (G : SimpleGraph V),
      G.CliqueFree n → G.chromaticNumber ≤ G.cochromaticNumber + f
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/762.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/762.lean#L58).

## `Erdos762.erdos_762.variants.steiner`

Solved: stated here without proof.

> This has been disproved by Steiner [St24b], who constructed a graph $G$ with $\omega(G)=4$,
> $\zeta(G)=4$, and $\chi(G)=7$.

```lean
theorem erdos_762.variants.steiner :
    ∃ (n : ℕ) (G : SimpleGraph (Fin n)),
      G.cliqueNum = 4 ∧ G.cochromaticNumber = 4 ∧ G.chromaticNumber = 7
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/762.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/762.lean#L68).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/762.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/762.lean)
- [erdosproblems.com/762](https://www.erdosproblems.com/762)
