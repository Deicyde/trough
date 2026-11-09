---
declaration: theorem
origin: cited
lean: Erdos1008.erdos_1008, Erdos1008.erdos_1008.variants.three_quarters, Erdos1008.erdos_1008.variants.folkman, Erdos1008.erdos_1008.variants.lower_bound
statement: formalized
---

# Erdős Problem 1008

> *References:*
> - [erdosproblems.com/1008](https://www.erdosproblems.com/1008)
> - [CFS14b] Conlon, D. and Fox, J. and Sudakov, B., *Large subgraphs without complete bipartite
>   graphs*. arXiv:1401.6711 (2014).
> - [Er71] Erdős, P., *Some unsolved problems in graph theory and combinatorial analysis*.
>   Combinatorial Mathematics and its Applications (Proc. Conf., Oxford, 1969) (1971), 97-109.

*Quoted from [FormalConjectures/ErdosProblems/1008.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1008.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1008](https://www.erdosproblems.com/1008).

The file states 4 research or textbook statements: 4 solved.

## `Erdos1008.erdos_1008`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1008.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1008.lean).

> Does every graph with $m$ edges contain a subgraph with $\gg m^{2/3}$ edges which contains
> no $C_4$?
>
> This problem was first solved in the affirmative by Conlon, Fox, and Sudakov [CFS14b]. A simple
> proof is given by Hunter in the comments.

```lean
theorem erdos_1008 :
    ∃ c > (0 : ℝ), ∀ (V : Type) [Fintype V] (G : SimpleGraph V),
      ∃ H ≤ G, (cycleGraph 4).Free H ∧
        c * (G.edgeSet.ncard : ℝ) ^ (2 / 3 : ℝ) ≤ (H.edgeSet.ncard : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1008.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1008.lean#L46).

## `Erdos1008.erdos_1008.variants.three_quarters`

Solved: stated here without proof.

> Originally asked by Bollobás and Erdős in 'a colloquium on graph theory at Tihany' with $m^{2/3}$
> replaced by $m^{3/4}$. Folkman showed this is false with the counterexample $K_{n,n^2}$, which has
> $n^3$ edges, and yet every subgraph with $>n^2+\binom{n}{2}$ edges contains a $C_4$.

```lean
theorem erdos_1008.variants.three_quarters :
    ¬ ∃ c > (0 : ℝ), ∀ (V : Type) [Fintype V] (G : SimpleGraph V),
      ∃ H ≤ G, (cycleGraph 4).Free H ∧
        c * (G.edgeSet.ncard : ℝ) ^ (3 / 4 : ℝ) ≤ (H.edgeSet.ncard : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1008.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1008.lean#L58).

## `Erdos1008.erdos_1008.variants.folkman`

Solved: stated here without proof.

> Folkman's counterexample $K_{n,n^2}$, which has $n^3$ edges, and yet every subgraph with
> $>n^2+\binom{n}{2}$ edges contains a $C_4$.

```lean
theorem erdos_1008.variants.folkman (n : ℕ) :
    ((completeBipartiteGraph (Fin n) (Fin (n ^ 2))).edgeSet.ncard = n ^ 3) ∧
      ∀ H ≤ completeBipartiteGraph (Fin n) (Fin (n ^ 2)),
        n ^ 2 + n.choose 2 < H.edgeSet.ncard → cycleGraph 4 ⊑ H
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1008.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1008.lean#L69).

## `Erdos1008.erdos_1008.variants.lower_bound`

Solved: stated here without proof.

> In [Er71] Erdős revises the conjecture to $m^{2/3}$, and notes $\gg m^{1/2}$ is trivial.

```lean
theorem erdos_1008.variants.lower_bound :
    ∃ c > (0 : ℝ), ∀ (V : Type) [Fintype V] (G : SimpleGraph V),
      ∃ H ≤ G, (cycleGraph 4).Free H ∧
        c * (G.edgeSet.ncard : ℝ) ^ (1 / 2 : ℝ) ≤ (H.edgeSet.ncard : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1008.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1008.lean#L79).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1008.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1008.lean)
- [erdosproblems.com/1008](https://www.erdosproblems.com/1008)
