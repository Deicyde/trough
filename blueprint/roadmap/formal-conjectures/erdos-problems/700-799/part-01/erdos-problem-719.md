---
declaration: theorem
origin: cited
lean: Erdos719.erdos_719
statement: formalized
---

# Erdős Problem 719

> *References:*
> - [erdosproblems.com/719](https://www.erdosproblems.com/719)

*Quoted from [FormalConjectures/ErdosProblems/719.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/719.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/719](https://www.erdosproblems.com/719).

The file states 1 research or textbook statement: 1 open.

## `Erdos719.erdos_719`

Open: stated without proof.

> Let $r\geq 2$, and let $\mathrm{ex}_r(n;K_{r+1}^r)$ be the maximum number of $r$-edges that can
> be placed on $n$ vertices without forming a $K_{r+1}^r$ (the $r$-uniform complete graph on
> $r+1$ vertices). Is every
> $r$-hypergraph $G$ on $n$ vertices the union of at most $\mathrm{ex}_{r}(n;K_{r+1}^r)$ many copies
> of $K_r^r$ and $K_{r+1}^r$, no two of which share a $K_r^r$?

```lean
theorem erdos_719 :
    ∀ r : ℕ, 2 ≤ r → ∀ (n : ℕ) (H : Finset (Finset (Fin n))),
    H.IsUniform r → ∃ D : Finset (Finset (Fin n)),
      H.IsCompleteHypergraphDecomposition r D ∧
        D.card ≤ Hypergraph.cliqueExtremalNumber n r (r + 1)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/719.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/719.lean#L41).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/719.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/719.lean)
- [erdosproblems.com/719](https://www.erdosproblems.com/719)
