---
declaration: theorem
origin: cited
lean: Erdos581.erdos_581
statement: formalized
---

# Erdős Problem 581

> *References:*
> - [erdosproblems.com/581](https://www.erdosproblems.com/581)
> - [CEG79] Chung, F. R. K. and Erdős, P. and Graham, R. L., _On the product of the point and line
>   covering numbers of a graph_. Second International Conference on Combinatorial Mathematics
>   (New York, 1978) (1979), 597-602.
> - [Al96] Alon, Noga, _Bipartite subgraphs_. Combinatorica (1996), 301-311.

*Quoted from [FormalConjectures/ErdosProblems/581.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/581.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/581](https://www.erdosproblems.com/581).

The file states 1 research or textbook statement: 1 solved.

## `Erdos581.erdos_581`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos581.lean#L31](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos581.lean#L31).

> Let $f(m)$ be the maximal $k$ such that a triangle-free graph on $m$ edges must contain a
> bipartite graph with $k$ edges. Determine $f(m)$.
>
> Resolved by Alon [Al96], who showed that there exist constants $c_1,c_2>0$ such that
>
> $$\frac{m}{2}+c_1m^{4/5}\leq f(m)\leq \frac{m}{2}+c_2m^{4/5}.$$

```lean
theorem erdos_581 : ∃ c₁ c₂ : ℝ, 0 < c₁ ∧ 0 < c₂ ∧ ∀ m : ℕ,
    (m : ℝ) / 2 + c₁ * (m : ℝ) ^ (4 / 5 : ℝ) ≤ f m ∧
      (f m : ℝ) ≤ (m : ℝ) / 2 + c₂ * (m : ℝ) ^ (4 / 5 : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/581.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/581.lean#L53).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/581.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/581.lean)
- [erdosproblems.com/581](https://www.erdosproblems.com/581)
