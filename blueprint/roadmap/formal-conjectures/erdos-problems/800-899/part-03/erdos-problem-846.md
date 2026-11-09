---
declaration: theorem
origin: cited
lean: Erdos846.erdos_846
statement: formalized
---

# Erdős Problem 846

> *Reference:* [erdosproblems.com/846](https://www.erdosproblems.com/846)

*Quoted from [FormalConjectures/ErdosProblems/846.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/846.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/846](https://www.erdosproblems.com/846).

The file states 1 research or textbook statement: 1 solved.

## `Erdos846.erdos_846`

Solved: stated here; a Lean proof is at [https://github.com/google-deepmind/formal-conjectures/blob/2404258180688283e5141021c75464dc2acfb798/FormalConjectures/ErdosProblems/846.lean](https://github.com/google-deepmind/formal-conjectures/blob/2404258180688283e5141021c75464dc2acfb798/FormalConjectures/ErdosProblems/846.lean).

> **Erdős Problem 846**
> Let `A ⊂ ℝ²` be an infinite set for which there exists some `ϵ>0` such that in any subset of `A`
> of size `n` there are always at least `ϵn` with no three on a line.
> Is it true that `A` is the union of a finite number of sets where no three are on a line?
>
> In other words, prove or disprove the following statement: every infinite `ε`-non-trilinear subset of the
> plane is weakly non-trilinar.

```lean
theorem erdos_846 : ¬ ∀ᵉ (A : Set ℝ²) (ε > 0), A.Infinite → NonTrilinearFor A ε →
    WeaklyNonTrilinear A
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/846.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/846.lean#L58).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/846.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/846.lean)
- [erdosproblems.com/846](https://www.erdosproblems.com/846)
