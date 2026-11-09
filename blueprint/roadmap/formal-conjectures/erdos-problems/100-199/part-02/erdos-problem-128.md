---
declaration: theorem
origin: cited
lean: Erdos128.erdos_128
statement: formalized
---

# Erdős Problem 128

> *Reference:* [erdosproblems.com/128](https://www.erdosproblems.com/128)

*Quoted from [FormalConjectures/ErdosProblems/128.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/128.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/128](https://www.erdosproblems.com/128).

The file states 1 research or textbook statement: 1 open.

## `Erdos128.erdos_128`

Open: stated without proof.

> Let G be a graph with n vertices such that every induced subgraph on ≥ $n/2$
> vertices has more than $n^2/50$ edges. Must G contain a triangle?

```lean
theorem erdos_128 :
    ∀ (V : Type) [Fintype V] (G : SimpleGraph V),
      (∀ V' : Set V, 2 * V'.ncard + 1 ≥ Fintype.card V →
        50 * (G.induce V').edgeSet.ncard > Fintype.card V ^ 2) → ¬ G.CliqueFree 3
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/128.lean, line 37](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/128.lean#L37).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/128.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/128.lean)
- [erdosproblems.com/128](https://www.erdosproblems.com/128)
