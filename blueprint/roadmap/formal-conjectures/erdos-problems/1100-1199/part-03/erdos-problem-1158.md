---
declaration: theorem
origin: cited
lean: Erdos1158.erdos_1158
statement: formalized
---

# Erdős Problem 1158

> *References:*
> - [erdosproblems.com/1158](https://www.erdosproblems.com/1158)
> - [Er64f] Erdős, P., On extremal problems of graphs and generalized graphs. Israel J. Math. (1964),
>   183--190.

*Quoted from [FormalConjectures/ErdosProblems/1158.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1158.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1158](https://www.erdosproblems.com/1158).

The file states 1 research or textbook statement: 1 open.

## `Erdos1158.erdos_1158`

Open: stated without proof.

> Let $K_{t}(r)$ be the complete $t$-partite $t$-uniform hypergraph with $r$ vertices in each class.
> Is it true that
>
> $$\mathrm{ex}_t(n,K_t(r)) \geq n^{t-r^{1-t}-o(1)}$$
>
> for all $t,r\geq 2$? The restriction $r\geq 2$ excludes forbidding a single edge.

```lean
theorem erdos_1158 :
    ∀ t r : ℕ, 2 ≤ t → 2 ≤ r →
    ∀ ε : ℝ, 0 < ε → ∀ᶠ n : ℕ in atTop,
      (n : ℝ) ^ ((t : ℝ) - (r : ℝ) ^ (1 - (t : ℝ)) - ε) ≤
        (Hypergraph.partiteExtremalNumber n t r : ℝ)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1158.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1158.lean#L42).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1158.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1158.lean)
- [erdosproblems.com/1158](https://www.erdosproblems.com/1158)
