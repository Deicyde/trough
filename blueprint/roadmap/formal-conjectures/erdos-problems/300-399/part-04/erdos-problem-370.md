---
declaration: theorem
origin: cited
lean: Erdos370.erdos_370
statement: formalized
---

# Erdős Problem 370

> *Reference:* [erdosproblems.com/370](https://www.erdosproblems.com/370)

*Quoted from [FormalConjectures/ErdosProblems/370.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/370.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/370](https://www.erdosproblems.com/370).

The file states 1 research or textbook statement: 1 solved.

## `Erdos370.erdos_370`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos370.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos370.lean); a Lean proof is at [https://github.com/XC0R/formal-conjectures/blob/f58dea7d2cc5c9da2e050ec80a73e838b54a6dd2/FormalConjectures/ErdosProblems/370.lean#L73](https://github.com/XC0R/formal-conjectures/blob/f58dea7d2cc5c9da2e050ec80a73e838b54a6dd2/FormalConjectures/ErdosProblems/370.lean#L73).

> Are there infinitely many $n$ such that the largest prime factor of $n$ is $< n^{\frac{1}{2}}$ and
> the largest prime factor of $n + 1$ is $< (n + 1)^{\frac{1}{2}}$.
>
> Steinerberger has pointed out this problem has a trivial solution.
>
> This was formalized in Lean by Alexeev using Aristotle.

```lean
theorem erdos_370 :
    { n | Nat.maxPrimeFac n < √n ∧ Nat.maxPrimeFac (n + 1) < √(n + 1) }.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/370.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/370.lean#L42).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/370.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/370.lean)
- [erdosproblems.com/370](https://www.erdosproblems.com/370)
