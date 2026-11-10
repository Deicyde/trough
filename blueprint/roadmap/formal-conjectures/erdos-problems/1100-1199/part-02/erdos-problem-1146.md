---
declaration: theorem
origin: cited
lean: Erdos1146.erdos_1146
statement: formalized
---

# Erdős Problem 1146

> *References:*
> - [erdosproblems.com/1146](https://www.erdosproblems.com/1146)
> - [Ru99] Ruzsa, I., Erdős and the Integers. Journal of Number Theory (1999), 115-163.

*Quoted from [FormalConjectures/ErdosProblems/1146.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1146.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1146](https://www.erdosproblems.com/1146).

The file states 1 research or textbook statement: 1 open.

## `Erdos1146.erdos_1146`

Open: stated without proof.

> Is $B=\{2^m3^n : m,n\geq 0\}$ an essential component?
>
> In [Ru99] Ruzsa states "The simplest set with a chance to be an essential component is the
> collection of numbers in the form $2^m3^n$ and Erdős often asked whether it is an essential
> component or not; I do not even have a plausible guess."

```lean
theorem erdos_1146 :
    IsEssentialComponent { k | ∃ m n : ℕ, k = 2 ^ m * 3 ^ n }
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1146.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1146.lean#L54).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1146.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1146.lean)
- [erdosproblems.com/1146](https://www.erdosproblems.com/1146)
