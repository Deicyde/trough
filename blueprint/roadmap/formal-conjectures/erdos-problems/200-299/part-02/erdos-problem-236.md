---
declaration: theorem
origin: cited
lean: Erdos236.erdos_236
statement: formalized
---

# Erdős Problem 236

> *Reference:* [erdosproblems.com/236](https://www.erdosproblems.com/236)

*Quoted from [FormalConjectures/ErdosProblems/236.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/236.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/236](https://www.erdosproblems.com/236).

The file states 1 research or textbook statement: 1 open.

## `Erdos236.erdos_236`

Open: stated without proof.

> Let $f(n)$ count the number of solutions to $n=p+2^k$ for prime $p$ and $k\geq 0$. Show that $f(n)=o(\log n)$.

```lean
theorem erdos_236: (fun n => (f n : ℝ)) =o[atTop] (fun n => Real.log (n : ℝ))
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/236.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/236.lean#L42).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/236.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/236.lean)
- [erdosproblems.com/236](https://www.erdosproblems.com/236)
