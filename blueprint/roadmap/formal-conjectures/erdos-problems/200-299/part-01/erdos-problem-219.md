---
declaration: theorem
origin: cited
lean: Erdos219.erdos_219
statement: formalized
---

# Erdős Problem 219

> *Reference:* [erdosproblems.com/219](https://www.erdosproblems.com/219)

*Quoted from [FormalConjectures/ErdosProblems/219.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/219.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/219](https://www.erdosproblems.com/219).

The file states 1 research or textbook statement: 1 solved. It also has 2 test statements and 3 API statements, counted here but not shown.

## `Erdos219.erdos_219`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/1268917deaaaa0d674f651287027baa26cea9920/src/latest/ErdosProblems/Erdos219.lean](https://github.com/plby/lean-proofs/blob/1268917deaaaa0d674f651287027baa26cea9920/src/latest/ErdosProblems/Erdos219.lean).

> Are there arbitrarily long arithmetic progressions of primes?
> Solution: yes.
> Ref: Green, Ben and Tao, Terence, _The primes contain arbitrarily long arithmetic progressions_

```lean
theorem erdos_219 : ∀ N : ℕ, ∃ l ∈ primeArithmeticProgressions, N ≤ ENat.card l
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/219.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/219.lean#L81).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/219.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/219.lean)
- [erdosproblems.com/219](https://www.erdosproblems.com/219)
