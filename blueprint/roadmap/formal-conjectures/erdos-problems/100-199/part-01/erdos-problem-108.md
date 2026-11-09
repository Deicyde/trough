---
declaration: theorem
origin: cited
lean: Erdos108.erdos_108
statement: formalized
---

# Erdős Problem 108

> *Reference:* [erdosproblems.com/108](https://www.erdosproblems.com/108)

*Quoted from [FormalConjectures/ErdosProblems/108.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/108.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/108](https://www.erdosproblems.com/108).

The file states 1 research or textbook statement: 1 open.

## `Erdos108.erdos_108`

Open: stated without proof.

> For every r ≥ 4 and k ≥ 2 is there some finite f(k,r) such that every graph of chromatic number ≥ f(k,r)
> contains a subgraph of girth ≥ r and chromatic number ≥ k?

```lean
theorem erdos_108 :
    ∀ r ≥ 4, ∀ k ≥ (2 : ℕ), ∃ (f : ℕ),
    ∀ (V : Type u) (G : SimpleGraph V) (_ : Nonempty V)
      (hchro : f ≤ SimpleGraph.chromaticNumber G),
    ∃ (H : G.Subgraph), (SimpleGraph.girth H.coe ≥ r) ∧
    (SimpleGraph.chromaticNumber H.coe ≥ k)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/108.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/108.lean#L39).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/108.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/108.lean)
- [erdosproblems.com/108](https://www.erdosproblems.com/108)
