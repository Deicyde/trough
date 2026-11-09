---
declaration: theorem
origin: cited
lean: Erdos740.erdos_740
statement: formalized
---

# Erdős Problem 740: Infinitary version of chromatic number and odd cycles

> *Reference:* [erdosproblems.com/740](https://erdosproblems.com/740)

*Quoted from [FormalConjectures/ErdosProblems/740.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/740.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/740](https://www.erdosproblems.com/740).

The file states 1 research or textbook statement: 1 open.

## `Erdos740.erdos_740`

Open: stated without proof.

> Let $\mathfrak{m}$ be an infinite cardinal and $G$ be a graph with chromatic number $\mathfrak{m}$.
> Let $r\geq 1$. Must $G$ contain a subgraph of chromatic number $\mathfrak{m}$ which does not contain
> any odd cycle of length $\leq r$?

```lean
theorem erdos_740 :
    ∀ (V : Type*) (G : SimpleGraph V),
      ℵ₀ ≤ G.chromaticCardinal →
        ∀ (r : ℕ),
          ∃ (H : G.Subgraph), H.coe.chromaticCardinal = G.chromaticCardinal ∧
            NoShortOddCycle H.coe r
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/740.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/740.lean#L42).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/740.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/740.lean)
- [erdosproblems.com/740](https://www.erdosproblems.com/740)
