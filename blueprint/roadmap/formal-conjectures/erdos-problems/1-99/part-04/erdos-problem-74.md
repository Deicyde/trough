---
declaration: theorem
origin: cited
lean: Erdos74.erdos_74, Erdos74.erdos_74.variants.sqrt
statement: formalized
---

# Erdős Problem 74

> *Reference:* [erdosproblems.com/74](https://www.erdosproblems.com/74)

*Quoted from [FormalConjectures/ErdosProblems/74.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/74.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/74](https://www.erdosproblems.com/74).

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 2 test statements, counted here but not shown.

## `Erdos74.erdos_74`

Solved: stated here; a Lean proof is at [https://github.com/tadamcz/erdos74/blob/e127ee587c7c91267eecdb3569443d2b0ad64b52/Erdos74/Resolutions/Erdos74_118usd_22h.lean#L2511](https://github.com/tadamcz/erdos74/blob/e127ee587c7c91267eecdb3569443d2b0ad64b52/Erdos74/Resolutions/Erdos74_118usd_22h.lean#L2511).

> Let $f(n)\to \infty$ possibly very slowly.
> Is there a graph of infinite chromatic number such that every finite subgraph on $n$
> vertices can be made bipartite by deleting at most $f(n)$ edges?
>
> The answer is no. A machine-checked disproof constructs a function $f(n) \to \infty$ for which
> every graph satisfying this local deletion bound has finite chromatic number.

```lean
theorem erdos_74 : ¬ ∀ f : ℕ → ℕ, Tendsto f atTop atTop →
    (∃ (V : Type u) (G : SimpleGraph V), G.chromaticNumber = ⊤ ∧
    ∀ n, G.maxSubgraphEdgeDistToBipartite n ≤ f n)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/74.lean, line 132](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/74.lean#L132).

## `Erdos74.erdos_74.variants.sqrt`

Open: stated without proof.

> Is there a graph of infinite chromatic number such that every finite subgraph on $n$
> vertices can be made bipartite by deleting at most $\sqrt{n}$ edges?

```lean
theorem erdos_74.variants.sqrt :
    ∃ (V : Type u) (G : SimpleGraph V), G.chromaticNumber = ⊤ ∧
    ∀ n, G.maxSubgraphEdgeDistToBipartite n ≤ (n : ℝ).sqrt
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/74.lean, line 142](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/74.lean#L142).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/74.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/74.lean)
- [erdosproblems.com/74](https://www.erdosproblems.com/74)
