---
declaration: theorem
origin: cited
lean: Erdos1137.erdos_1137
statement: formalized
---

# Erdős Problem 1137

> *Reference:* [erdosproblems.com/1137](https://www.erdosproblems.com/1137)

*Quoted from [FormalConjectures/ErdosProblems/1137.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1137.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1137](https://www.erdosproblems.com/1137).

The file states 1 research or textbook statement: 1 open.

## `Erdos1137.erdos_1137`

Open: stated without proof.

> Let $d_n=p_{n+1}-p_n$, where $p_n$ denotes the $n$th prime. Is it true that
>
> $$\frac{\max_{n < x}d_{n}d_{n-1}}{(\max_{n < x}d_n)^2}\to 0$$
>
> as $x\to \infty$?

```lean
theorem erdos_1137 :
    Tendsto (fun x ↦
       (((range x).sup (fun n ↦ (primeGap n) * (primeGap (n - 1))) : ℕ) : ℝ) /
       (((range x).sup primeGap : ℕ) : ℝ) ^ 2) atTop (𝓝 0)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1137.lean, line 38](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1137.lean#L38).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1137.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1137.lean)
- [erdosproblems.com/1137](https://www.erdosproblems.com/1137)
