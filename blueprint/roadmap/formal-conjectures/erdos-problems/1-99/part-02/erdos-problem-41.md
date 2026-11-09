---
declaration: theorem
origin: cited
lean: Erdos41.erdos_41, Erdos41.erdos_41.variants.pairwise
statement: formalized
---

# Erdős Problem 41

> *Reference:* [erdosproblems.com/41](https://www.erdosproblems.com/41)

*Quoted from [FormalConjectures/ErdosProblems/41.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/41.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/41](https://www.erdosproblems.com/41).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos41.erdos_41`

Open: stated without proof.

> Let $A \subset \mathbb{N}$ be an infinite set such that the triple sums $a+b+c$ are all distinct
> for $a,b,c \in A$ (aside from the trivial coincidences). Is it true that
> $$\liminf_{N \to \infty} \frac{\lvert A \cap \{1,\ldots,N\}\rvert}{N^{1/3}}=0?$$

```lean
theorem erdos_41 (A : Set ℕ) (h_triple : NtupleCondition A 3) (h_infinite : A.Infinite) :
    Filter.atTop.liminf (fun N => (A ∩ Icc 1 N).ncard / (N : ℝ)^(1/3 : ℝ)) = 0
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/41.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/41.lean#L55).

## `Erdos41.erdos_41.variants.pairwise`

Solved: stated here without proof.

> Erdős proved that if the pairwise sums $a+b$ are all distinct aside from the trivial
> coincidences, then
> $$\liminf_{N \to \infty} \frac{\lvert A \cap \{1,\ldots,N\}\rvert}{N^{1/2}}=0.$$

```lean
theorem erdos_41.variants.pairwise (A : Set ℕ) (hA₂ : NtupleCondition A 2) (hA : A.Infinite) :
    Filter.atTop.liminf (fun N => (A ∩ Icc 1 N).ncard / (N : ℝ).sqrt) = 0
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/41.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/41.lean#L65).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/41.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/41.lean)
- [erdosproblems.com/41](https://www.erdosproblems.com/41)
