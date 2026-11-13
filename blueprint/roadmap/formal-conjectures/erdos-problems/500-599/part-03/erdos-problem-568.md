---
declaration: theorem
origin: cited
lean: Erdos568.erdos_568
statement: formalized
---

# Erdős Problem 568

> *References:*
> - [erdosproblems.com/568](https://www.erdosproblems.com/568)
> - [EFRS93] Erdős, P. and Faudree, R. J. and Rousseau, C. C. and Schelp, R. H., Ramsey size linear
>   graphs. Combin. Probab. Comput. (1993), 389-399.

*Quoted from [FormalConjectures/ErdosProblems/568.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/568.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/568](https://www.erdosproblems.com/568).

The file states 1 research or textbook statement: 1 open.

## `Erdos568.erdos_568`

Open: stated without proof.

> Let $G$ be a graph such that $R(G,T_n)\ll n$ for any tree $T_n$ on $n$ vertices and
> $R(G,K_n)\ll n^2$. Is it true that, for any $H$ with $m$ edges and no isolated vertices,
>
> $$R(G,H)\ll m?$$
>
> In other words, is $G$ Ramsey size linear?
>
> This problem is #33 in Ramsey Theory in the graphs problem collection.

```lean
theorem erdos_568 :
    ∀ (V : Type) [Fintype V] (G : SimpleGraph V),
      (∃ c₁ > (0 : ℝ), ∀ (n : ℕ) (T : SimpleGraph (Fin n)),
        T.IsTree → (SimpleGraph.graphRamsey G T : ℝ) ≤ c₁ * n) →
      (∃ c₂ > (0 : ℝ), ∀ (n : ℕ),
        (SimpleGraph.graphRamsey G (SimpleGraph.completeGraph (Fin n)) : ℝ) ≤ c₂ * (n : ℝ) ^ 2) →
      G.IsRamseySizeLinear
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/568.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/568.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/568.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/568.lean)
- [erdosproblems.com/568](https://www.erdosproblems.com/568)
