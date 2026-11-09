---
declaration: theorem
origin: cited
lean: Erdos236.erdos_236
statement: formalized
---

# Erdős Problem 236

> *Reference:* [erdosproblems.com/236](https://www.erdosproblems.com/236)

*Quoted from [FormalConjectures/ErdosProblems/236.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/236.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/236](https://www.erdosproblems.com/236).

The file states 1 research or textbook statement: 1 open.

## `Erdos236.erdos_236`

Open: stated without proof.

> Let $f(n)$ count the number of solutions to $n=p+2^k$ for prime $p$ and $k\geq 0$. Show that $f(n)=o(\log n)$.

```lean
theorem erdos_236: (fun n => (f n : ℝ)) =o[atTop] (fun n => Real.log (n : ℝ))
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/236.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/236.lean#L42).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/236.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/236.lean)
- [erdosproblems.com/236](https://www.erdosproblems.com/236)
