---
declaration: theorem
origin: cited
lean: Erdos1139.erdos_1139
statement: formalized
---

# Erdős Problem 1139

> *Reference:* [erdosproblems.com/1139](https://www.erdosproblems.com/1139)

*Quoted from [FormalConjectures/ErdosProblems/1139.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1139.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1139](https://www.erdosproblems.com/1139).

The file states 1 research or textbook statement: 1 open.

## `Erdos1139.erdos_1139`

Open: stated without proof.

> Let $1\leq u_1 < u_2 < \cdots$ be the sequence of integers with at most $2$ prime factors.
> Is it true that
>
> $$\limsup_{k \to \infty} \frac{u_{k+1}-u_k}{\log k}=\infty?$$

```lean
theorem erdos_1139 :
    letI u := Nat.nth (fun n ↦ 0 < n ∧ Ω n ≤ 2)
    atTop.limsup (fun k : ℕ ↦ (((u (k + 1) : ℝ) - (u k : ℝ)) / Real.log (↑k + 1) : EReal)) = ⊤
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1139.lean, line 38](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1139.lean#L38).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1139.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1139.lean)
- [erdosproblems.com/1139](https://www.erdosproblems.com/1139)
