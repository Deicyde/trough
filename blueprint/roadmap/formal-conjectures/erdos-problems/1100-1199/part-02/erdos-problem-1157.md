---
declaration: theorem
origin: cited
lean: Erdos1157.erdos_1157
statement: formalized
---

# Erdős Problem 1157

> *References:*
> - [erdosproblems.com/1157](https://www.erdosproblems.com/1157)
> - [BES73] Brown, W. G. and Erdős, P. and S\'os, V. T., Some extremal problems on {$r$}-graphs.
>   (1973), 53--63.

*Quoted from [FormalConjectures/ErdosProblems/1157.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1157.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1157](https://www.erdosproblems.com/1157).

The file states 1 research or textbook statement: 1 open.

## `Erdos1157.erdos_1157`

Open: stated without proof.

> Let $s,k,r\geq 2$. Let $\mathcal{F}$ be the family of all $r$-uniform hypergraphs with $k$ vertices
> and $s$ edges. Determine
>
> $$\mathrm{ex}_r(n,\mathcal{F}).$$

```lean
theorem erdos_1157 :
    ∀ r k s : ℕ, 2 ≤ r → 2 ≤ k → 2 ≤ s → ∀ n : ℕ,
      Hypergraph.configurationExtremalNumber n r k s = erdos_1157.answer n r k s
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1157.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1157.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1157.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1157.lean)
- [erdosproblems.com/1157](https://www.erdosproblems.com/1157)
