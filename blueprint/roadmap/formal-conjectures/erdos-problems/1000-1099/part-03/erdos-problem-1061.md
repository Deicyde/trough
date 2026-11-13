---
declaration: theorem
origin: cited
lean: Erdos1061.erdos_1061
statement: formalized
---

# Erdős Problem 1061

> *References:*
>  - [erdosproblems.com/1061](https://www.erdosproblems.com/1061)
>  - [Gu04] Guy, Richard K., _Unsolved problems in number theory_. (2004), Problem B15.

*Quoted from [FormalConjectures/ErdosProblems/1061.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1061.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1061](https://www.erdosproblems.com/1061).

The file states 1 research or textbook statement: 1 open.

## `Erdos1061.erdos_1061`

Open: stated without proof.

> How many (ordered) solutions are there to `σ(a) + σ(b) = σ(a + b)` with `a + b ≤ x`?
> Is it true that this number is asymptotic to `c * x` for some constant `c > 0`?

```lean
theorem erdos_1061 : ∃ c : ℝ, 0 < c ∧ S ~[atTop] (fun x : ℝ ↦ c * x)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1061.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1061.lean#L49).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1061.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1061.lean)
- [erdosproblems.com/1061](https://www.erdosproblems.com/1061)
