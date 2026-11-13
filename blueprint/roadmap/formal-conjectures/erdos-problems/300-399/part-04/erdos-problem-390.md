---
declaration: theorem
origin: cited
lean: Erdos390.erdos_390.variants.theta, Erdos390.erdos_390
statement: formalized
---

# Erdős Problem 390

> *References:*
>  - [erdosproblems.com/390](https://www.erdosproblems.com/390)
>  - [EGS82] Erdős, P., R. K. Guy, and J. L. Selfridge. "Another Property of 239 and some related
>     questions." Congr. Numer. 34 (1982): 243-257.
>  -

*Quoted from [FormalConjectures/ErdosProblems/390.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/390.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/390](https://www.erdosproblems.com/390).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos390.erdos_390.variants.theta`

Solved: stated here without proof.

> `f n - 2 * n = θ (n / log n)`. This is proved in [EGS82].

```lean
theorem erdos_390.variants.theta :
    (fun n => f n - 2 * n : ℕ → ℝ) =Θ[atTop] (fun n => n / log (n : ℝ))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/390.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/390.lean#L44).

## `Erdos390.erdos_390`

Open: stated without proof.

> Does there exists a constant `c` such that `f n - 2 * n ~ c * (n / log n)`?

```lean
theorem erdos_390 :
    ∃ c,
      (fun n => f n - 2 * n : ℕ → ℝ) ~[atTop] (fun n => c * n / log (n : ℝ))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/390.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/390.lean#L50).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/390.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/390.lean)
- [erdosproblems.com/390](https://www.erdosproblems.com/390)
