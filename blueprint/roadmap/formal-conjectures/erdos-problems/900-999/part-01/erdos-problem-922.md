---
declaration: theorem
origin: cited
lean: Erdos922.erdos_922
statement: formalized
---

# Erdős Problem 922

> *References:*
> - [erdosproblems.com/922](https://www.erdosproblems.com/922)
> - [ErHa67b] Erdős, P. and Hajnal, András, *On chromatic graphs*. Mat. Lapok (1967), 1-4.
> - [Er69b] Erdős, P., *Problems and results in chromatic graph theory*. Proof Techniques in Graph
>   Theory (Proc. Second Ann Arbor Graph Theory Conf., Ann Arbor, Mich., 1968) (1969), 27-35.
> - [Fo70b] Folkman, J. H., *An upper bound on the chromatic number of a graph*. (1970), 437-457.

*Quoted from [FormalConjectures/ErdosProblems/922.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/922.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/922](https://www.erdosproblems.com/922).

The file states 1 research or textbook statement: 1 solved.

## `Erdos922.erdos_922`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos922.lean#L5595](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos922.lean#L5595).

> Let $k\geq 0$. Let $G$ be a graph such that every subgraph $H$ contains an independent set of size
> $\geq (n-k)/2$, where $n$ is the number of vertices of $H$. Must $G$ have chromatic number at most
> $k+2$?
>
> A question of Erdős and Hajnal [ErHa67b]. The case $k=0$ is trivial, but they could not prove
> this even for $k=1$.
>
> This is true, and was proved by Folkman [Fo70b].
>
> See also [73](https://www.erdosproblems.com/73).

```lean
theorem erdos_922 : ∀ (k : ℕ) (V : Type) [Fintype V] (G : SimpleGraph V),
    (∀ S : Finset V, ∃ I : Finset V, I ⊆ S ∧ (G.induce (I : Set V)).edgeSet = ∅ ∧
      (I.card : ℝ) ≥ (S.card - k : ℝ) / 2) →
    G.chromaticNumber ≤ k + 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/922.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/922.lean#L52).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/922.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/922.lean)
- [erdosproblems.com/922](https://www.erdosproblems.com/922)
