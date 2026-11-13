---
declaration: theorem
origin: cited
lean: Erdos837.erdos_837
statement: formalized
---

# Erdős Problem 837

> *References:*
> - [erdosproblems.com/837](https://www.erdosproblems.com/837)

*Quoted from [FormalConjectures/ErdosProblems/837.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/837.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/837](https://www.erdosproblems.com/837).

The file states 1 research or textbook statement: 1 open.

## `Erdos837.erdos_837`

Open: stated without proof.

> Let $k\geq 2$ and $A_k\subseteq [0,1]$ be the set of $\alpha$ such that there exists some
> $\beta(\alpha)>\alpha$ with the property that, if $G_1,G_2,\ldots$ is a sequence of $k$-uniform
> hypergraphs with
>
> $$\liminf \frac{e(G_n)}{\binom{\lvert G_n\rvert}{k}} >\alpha$$
>
> then there exist subgraphs $H_n\subseteq G_n$ such that $\lvert H_n\rvert \to \infty$ and
>
> $$\liminf \frac{e(H_n)}{\binom{\lvert H_n\rvert}{k}} >\beta,$$
>
> and further that this property does not necessarily hold if $>\alpha$ is replaced by $\geq \alpha$.
> What is $A_3$?

```lean
theorem erdos_837 :
    {α : ℝ | α ∈ Set.Icc 0 1 ∧ ∃ β : ℝ, α < β ∧
    Hypergraph.HasDensityJump 3 α β true ∧ ¬ Hypergraph.HasDensityJump 3 α β false}
      = erdos_837.answer
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/837.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/837.lean#L46).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/837.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/837.lean)
- [erdosproblems.com/837](https://www.erdosproblems.com/837)
