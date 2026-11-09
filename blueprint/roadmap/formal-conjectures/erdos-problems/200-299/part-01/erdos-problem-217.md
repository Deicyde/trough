---
declaration: theorem
origin: cited
lean: Erdos217.erdos_217
statement: formalized
---

# Erdős Problem 217

> *Reference:* [Erdős Problem 217](https://www.erdosproblems.com/217)

*Quoted from [FormalConjectures/ErdosProblems/217.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/217.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/217](https://www.erdosproblems.com/217).

The file states 1 research or textbook statement: 1 open.

## `Erdos217.erdos_217`

Open: stated without proof.

> For which $n$ do there exist $n$ points in $\mathbb{R}^2$, no three on a line and no four on
> a circle, that determine $n-1$ distinct distances whose multiplicities are
> $1,2,\ldots,n-1$? The condition $n>0$ excludes the empty configuration, since the
> requested number $n-1$ of distances is nonnegative.

```lean
theorem erdos_217 : erdos_217.answer = {n : ℕ | 0 < n ∧ ∃ P : Finset ℝ²,
    P.card = n ∧ InGeneralPosition (P : Set ℝ²) ∧
      (distanceSet P).card = n - 1 ∧
      (distanceSet P).image (distanceMultiplicity P) = Finset.Icc 1 (n - 1)}
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/217.lean, line 40](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/217.lean#L40).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/217.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/217.lean)
- [erdosproblems.com/217](https://www.erdosproblems.com/217)
