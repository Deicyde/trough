---
declaration: theorem
origin: cited
lean: Erdos493.erdos_493
statement: formalized
---

# Erdős Problem 493

> *References:*
> - [erdosproblems.com/493](https://www.erdosproblems.com/493)
> - [Er61] Erdős, Paul, *Some unsolved problems*. Magyar Tud. Akad. Mat. Kutató Int. Közl. (1961), 221-254.

*Quoted from [FormalConjectures/ErdosProblems/493.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/493.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/493](https://www.erdosproblems.com/493).

The file states 1 research or textbook statement: 1 solved.

## `Erdos493.erdos_493`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos493.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos493.lean).

> Does there exist a $k$ such that every sufficiently large integer can be written in the form
>
> $$\prod_{i=1}^k a_i - \sum_{i=1}^k a_i$$
>
> for some integers $a_i\geq 2$?
>
> Erdős attributes this question to Schinzel. Eli Seamans has observed that the answer is yes (with $k=2$) for a very simple reason: $n = 2(n+2)-(2+(n+2))$. There may well have been some additional constraint in the problem as Schinzel posed it, but [Er61] does not record what this is.

```lean
theorem erdos_493 :
    ∃ k : ℕ, ∃ N : ℤ, ∀ n : ℤ, N ≤ n →
      ∃ a : Fin k → ℤ,
        (∀ i : Fin k, (2 : ℤ) ≤ a i) ∧
        (∏ i : Fin k, a i) - (∑ i : Fin k, a i) = n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/493.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/493.lean#L41).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/493.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/493.lean)
- [erdosproblems.com/493](https://www.erdosproblems.com/493)
