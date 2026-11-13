---
declaration: theorem
origin: cited
lean: Erdos276.erdos_276
statement: formalized
---

# Erdős Problem 276

> *References:*
> [erdosproblems.com/276](https://www.erdosproblems.com/276)

*Quoted from [FormalConjectures/ErdosProblems/276.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/276.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/276](https://www.erdosproblems.com/276).

The file states 1 research or textbook statement: 1 open.

## `Erdos276.erdos_276`

Open: stated without proof.

> Is there an infinite Lucas sequence $a_0, a_1, \ldots$ where $a_{n+2} = a_{n+1} + a_n$ for
> $n \ge 0$ such that all $a_k$ are composite, and yet no integer has a common factor with every
> term of the sequence?

```lean
theorem erdos_276 :
    ∃ (a : ℕ → ℕ),
    IsLucasSequence a ∧ (∀ k, (a k).Composite) ∧ (∀ n > 1, ∃ k, Nat.gcd n (a k) = 1)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/276.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/276.lean#L49).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/276.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/276.lean)
- [erdosproblems.com/276](https://www.erdosproblems.com/276)
