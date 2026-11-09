---
declaration: theorem
origin: cited
lean: Erdos277.erdos_277
statement: formalized
---

# Erdős Problem 277

> *References:*
> - [erdosproblems.com/277](https://www.erdosproblems.com/277)
> - [Ha79] Haight, J. A., Covering systems of congruences, a negative result. Mathematika (1979),
>   53--61.

*Quoted from [FormalConjectures/ErdosProblems/277.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/277.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/277](https://www.erdosproblems.com/277).

The file states 1 research or textbook statement: 1 solved.

## `Erdos277.erdos_277`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/1268917deaaaa0d674f651287027baa26cea9920/src/latest/ErdosProblems/Erdos277.lean#L1294](https://github.com/plby/lean-proofs/blob/1268917deaaaa0d674f651287027baa26cea9920/src/latest/ErdosProblems/Erdos277.lean#L1294).

> Is it true that, for every $c$, there exists an $n$ such that $\sigma(n)>cn$ but there is no
> covering system whose moduli all divide $n$?
>
> This was answered affirmatively by Haight [Ha79].

```lean
theorem erdos_277 :
   ∀ c : ℝ, ∃ n : ℕ, (σ 1 n : ℝ) > c * n ∧
      ∀ (m : StrictCoveringSystem ℤ), ∃ i, (n : ℤ) ∉ m.moduli i
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/277.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/277.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/277.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/277.lean)
- [erdosproblems.com/277](https://www.erdosproblems.com/277)
