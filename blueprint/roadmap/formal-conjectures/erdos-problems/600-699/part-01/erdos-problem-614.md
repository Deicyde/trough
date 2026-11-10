---
declaration: theorem
origin: cited
lean: Erdos614.erdos_614
statement: formalized
---

# Erdős Problem 614

> *References:*
> - [erdosproblems.com/614](https://www.erdosproblems.com/614)
> - [A problem on sparse induced subgraphs](https://mathweb.ucsd.edu/~erdosproblems/erdos/newproblems/SparseInducedSubgraphs.html)
> - [FRS97] Faudree, R. J., Rousseau, C. C. and Schelp, R. H., *Problems in graph theory from Memphis*.
>   The Mathematics of Paul Erdős, II, 7–26.

*Quoted from [FormalConjectures/ErdosProblems/614.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/614.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/614](https://www.erdosproblems.com/614).

The file states 1 research or textbook statement: 1 open.

## `Erdos614.erdos_614`

Open: stated without proof.

> Let $f(n,k)$ be minimal such that there is a graph with $n$ vertices and $f(n,k)$ edges
> where every set of $k+2$ vertices induces a subgraph with maximum degree at least $k$.
> Determine $f(n,k)$.

```lean
theorem erdos_614 :
    ∀ n k, IsLeast {m : ℕ | ∃ G : SimpleGraph (Fin n), G.edgeFinset.card = m ∧
      ∀ s : Finset (Fin n), s.card = k + 2 →
        ∃ v : s, k ≤ (G.induce (s : Set (Fin n))).degree v} (erdos_614.answer n k)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/614.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/614.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/614.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/614.lean)
- [erdosproblems.com/614](https://www.erdosproblems.com/614)
