---
declaration: theorem
origin: cited
lean: Erdos64.erdos_64
statement: formalized
---

# Erdős Problem 64

> *Reference:* [erdosproblems.com/64](https://www.erdosproblems.com/64)

*Quoted from [FormalConjectures/ErdosProblems/64.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/64.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/64](https://www.erdosproblems.com/64).

The file states 1 research or textbook statement: 1 open.

## `Erdos64.erdos_64`

Open: stated without proof.

> Does every finite graph with minimum degree at least $3$
> contain a cycle of length $2^k$ for some $k \geq 2$?

```lean
theorem erdos_64 :
    ∀ (V : Type*) (G : SimpleGraph V) [Fintype V] [DecidableRel G.Adj],
        G.minDegree ≥ 3 → ∃ (k : ℕ) (v : V) (c : G.Walk v v),
            k ≥ 2 ∧ c.IsCycle ∧ c.length = 2^k
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/64.lean, line 35](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/64.lean#L35).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/64.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/64.lean)
- [erdosproblems.com/64](https://www.erdosproblems.com/64)
