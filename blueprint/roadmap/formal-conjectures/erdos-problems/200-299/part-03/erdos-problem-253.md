---
declaration: theorem
origin: cited
lean: Erdos253.erdos_253
statement: formalized
---

# Erdős Problem 253

> *Reference:* [erdosproblems.com/253](https://www.erdosproblems.com/253)

*Quoted from [FormalConjectures/ErdosProblems/253.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/253.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/253](https://www.erdosproblems.com/253).

The file states 1 research or textbook statement: 1 solved.

## `Erdos253.erdos_253`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/1268917deaaaa0d674f651287027baa26cea9920/src/latest/ErdosProblems/Erdos253.lean#L699](https://github.com/plby/lean-proofs/blob/1268917deaaaa0d674f651287027baa26cea9920/src/latest/ErdosProblems/Erdos253.lean#L699).

> Let $a_1 < a_2 < \dotsc$ be an infinite sequence of positive integers such that
> $\frac{a_{i+1}}{a_i} \to 1$. If every arithmetic progression contains infinitely many
> integers which are the sum of distinct $a_i$ then every sufficiently large integer is
> the sum of distinct $a_i$.

```lean
theorem erdos_253 : ¬ ∀ a : ℕ → ℕ, 0 < a 0 →
    RepresentsAPs a → (Filter.atTop.Tendsto (fun n ↦ (a <| n + 1 : ℝ) / a n) (𝓝 1)) →
      subsetSums (Set.range a) ∈ Filter.cofinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/253.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/253.lean#L46).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/253.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/253.lean)
- [erdosproblems.com/253](https://www.erdosproblems.com/253)
