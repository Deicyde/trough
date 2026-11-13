---
declaration: theorem
origin: cited
lean: Erdos1203.erdos_1203, Erdos1203.erdos_1203.variants.lower_bound
statement: formalized
---

# Erdős Problem 1203

> *References:*
> - [erdosproblems.com/1203](https://www.erdosproblems.com/1203)

*Quoted from [FormalConjectures/ErdosProblems/1203.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1203.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1203](https://www.erdosproblems.com/1203).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos1203.erdos_1203`

Open: stated without proof.

> Prove that $F(n)\to \infty$ as $n\to \infty$.

```lean
theorem erdos_1203 :
    Tendsto F atTop atTop
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1203.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1203.lean#L45).

## `Erdos1203.erdos_1203.variants.lower_bound`

Solved: stated here without proof.

> It is easy to prove that $F(n)\geq 1-o(1)$.

```lean
theorem erdos_1203.variants.lower_bound :
    ∀ ε > 0, ∀ᶠ n in atTop, F n ≥ 1 - ε
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1203.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1203.lean#L53).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1203.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1203.lean)
- [erdosproblems.com/1203](https://www.erdosproblems.com/1203)
