---
declaration: theorem
origin: cited
lean: Erdos591.erdos_591
statement: formalized
---

# Erdős Problem 591

> *References:*
> - [erdosproblems.com/591](https://www.erdosproblems.com/591)
> - [Sc10] Schipperus, Rene, Countable partition ordinals. Ann. Pure Appl. Logic (2010), 1195-1215.

*Quoted from [FormalConjectures/ErdosProblems/591.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/591.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/591](https://www.erdosproblems.com/591).

The file states 1 research or textbook statement: 1 solved.

## `Erdos591.erdos_591`

Solved: stated here without proof.

> Let $α$ be the infinite ordinal $\omega^{\omega^2}$. Is it true that any red/blue colouring of the
> edges of $K_α$ there is either a red $K_α$ or a blue $K_3$?
>
> This is true and was proved independently by Schipperus [Sc10] and Darby.

```lean
theorem erdos_591 : OrdinalCardinalRamsey (ω ^ ω ^ 2) (ω ^ ω ^ 2) 3
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md). Declared in [FormalConjectures/ErdosProblems/591.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/591.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/591.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/591.lean)
- [erdosproblems.com/591](https://www.erdosproblems.com/591)
