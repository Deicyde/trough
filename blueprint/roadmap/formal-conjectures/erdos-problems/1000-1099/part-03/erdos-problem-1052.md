---
declaration: theorem
origin: cited
lean: Erdos1052.erdos_1052, Erdos1052.even_of_isUnitaryPerfect
statement: formalized
---

# Erdős Problem 1052

> *Reference:* [erdosproblems.com/1052](https://www.erdosproblems.com/1052)

*Quoted from [FormalConjectures/ErdosProblems/1052.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1052.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1052](https://www.erdosproblems.com/1052).

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 5 test statements, counted here but not shown.

## `Erdos1052.erdos_1052`

Open: stated without proof.

> Are there only finitely many unitary perfect numbers?

```lean
theorem erdos_1052 :
    {n | IsUnitaryPerfect n}.Finite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1052.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1052.lean#L42).

## `Erdos1052.even_of_isUnitaryPerfect`

Solved: stated here; a Lean proof is at [https://github.com/mzhorvath1/formal-conjectures/blob/b70a2ddf5e55f743aac9d4f4a907786b39bc9807/FormalConjectures/ErdosProblems/1052.lean#L46](https://github.com/mzhorvath1/formal-conjectures/blob/b70a2ddf5e55f743aac9d4f4a907786b39bc9807/FormalConjectures/ErdosProblems/1052.lean#L46).

> All unitary perfect numbers are even.
>
> Formal proof linked here provided by AlphaProof.

```lean
theorem even_of_isUnitaryPerfect (n : ℕ) (hn : IsUnitaryPerfect n) : Even n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1052.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1052.lean#L53).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1052.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1052.lean)
- [erdosproblems.com/1052](https://www.erdosproblems.com/1052)
