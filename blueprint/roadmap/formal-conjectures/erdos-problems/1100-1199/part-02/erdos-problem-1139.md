---
declaration: theorem
origin: cited
lean: Erdos1139.erdos_1139
statement: formalized
---

# Erdős Problem 1139

> *Reference:* [erdosproblems.com/1139](https://www.erdosproblems.com/1139)

*Quoted from [FormalConjectures/ErdosProblems/1139.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/1139.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1139](https://www.erdosproblems.com/1139).

The file states 1 research or textbook statement: 1 solved.

## `Erdos1139.erdos_1139`

Solved: stated here; a Lean proof is at [https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-24-000011](https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-24-000011).

> Let $1\leq u_1 < u_2 < \cdots$ be the sequence of integers with at most $2$ prime factors.
> Is it true that
>
> $$\limsup_{k \to \infty} \frac{u_{k+1}-u_k}{\log k}=\infty?$$

```lean
theorem erdos_1139 :
    letI u := Nat.nth (fun n ↦ 0 < n ∧ Ω n ≤ 2)
    atTop.limsup (fun k : ℕ ↦ (((u (k + 1) : ℝ) - (u k : ℝ)) / Real.log (↑k + 1) : EReal)) = ⊤
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1139.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/1139.lean#L39).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1139.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/1139.lean)
- [erdosproblems.com/1139](https://www.erdosproblems.com/1139)
