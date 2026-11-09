---
declaration: theorem
origin: cited
lean: Erdos180.erdos_180, Erdos180.erdos_180.variants.counterexample
statement: formalized
---

# Erdős Problem 180

> *References:*
> - [erdosproblems.com/180](https://www.erdosproblems.com/180)
> - [ErSi82] Erdős, P. and Simonovits, M., *Compactness results in extremal graph theory*.
>   Combinatorica (1982), 275-288.
> - [OpenAI26] OpenAI, *Ten advances in mathematics and theoretical computer science*. (2026).

*Quoted from [FormalConjectures/ErdosProblems/180.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/180.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/180](https://www.erdosproblems.com/180).

The file states 2 research or textbook statements: 2 solved.

## `Erdos180.erdos_180`

Solved: stated here without proof.

> If $\mathcal{F}$ is a finite set of finite graphs then $\mathrm{ex}(n;\mathcal{F})$ is the maximum
> number of edges a graph on $n$ vertices can have without containing any subgraphs from
> $\mathcal{F}$. Note that it is trivial that $\mathrm{ex}(n;\mathcal{F})\leq \mathrm{ex}(n;G)$ for
> every $G\in\mathcal{F}$. Is it true that, for every $\mathcal{F}$, there exists $G\in\mathcal{F}$
> such that
> $$\mathrm{ex}(n;G)\ll_{\mathcal{F}}\mathrm{ex}(n;\mathcal{F})?$$
>
> This is the Erdős–Simonovits compactness conjecture. The answer is no: OpenAI [OpenAI26] give a
> family of connected bipartite graphs, none of them acyclic, for which no single member controls
> the family extremal number. See `erdos_180.variants.counterexample`.

```lean
theorem erdos_180 :
    ¬ ∀ family : Finset FiniteGraph,
      family.Nonempty → IsCyclicFamily family → IsCompactFamily family
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/180.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/180.lean#L75).

## `Erdos180.erdos_180.variants.counterexample`

Solved: stated here; a Lean proof is at [https://github.com/openai/ten-proofs/blob/94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6/CompactnessAndDegeneracy.lean](https://github.com/openai/ten-proofs/blob/94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6/CompactnessAndDegeneracy.lean).

> The counterexample: a nonempty family of connected bipartite graphs, none acyclic, that is not
> compact.

```lean
theorem erdos_180.variants.counterexample :
    ∃ family : Finset FiniteGraph,
      family.Nonempty ∧
      (∀ forbidden ∈ family,
        forbidden.graph.Connected ∧ forbidden.graph.IsBipartite ∧
          ¬ forbidden.graph.IsAcyclic) ∧
      ¬ IsCompactFamily family
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/180.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/180.lean#L87).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/180.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/180.lean)
- [erdosproblems.com/180](https://www.erdosproblems.com/180)
