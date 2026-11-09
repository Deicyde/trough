---
declaration: theorem
origin: cited
lean: Erdos1024.erdos_1024
statement: formalized
---

# Erdős Problem 1024

> *References:*
> - [erdosproblems.com/1024](https://www.erdosproblems.com/1024)
> - [PhRo86] Phelps, K. T. and R\"odl, V., Steiner triple systems with minimum independence number. Ars
>   Combin. (1986), 167--172.

*Quoted from [FormalConjectures/ErdosProblems/1024.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1024.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1024](https://www.erdosproblems.com/1024).

The file states 1 research or textbook statement: 1 solved.

## `Erdos1024.erdos_1024`

Solved: stated here without proof.

> Let $f(n)$ be such that every $3$-uniform linear hypergraph on $n$ vertices contains an independent
> set on $f(n)$ vertices. Estimate $f(n)$.
>
> Phelps and Rödl [PhRo86] proved $f(n) \asymp (n\log n)^{1/2}$.

```lean
theorem erdos_1024 :
    (fun n ↦ (Hypergraph.linearIndependenceNumber n : ℝ)) =Θ[atTop]
    erdos_1024.answer
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1024.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1024.lean#L44).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1024.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1024.lean)
- [erdosproblems.com/1024](https://www.erdosproblems.com/1024)
