---
declaration: theorem
origin: cited
lean: Erdos224.erdos_224
statement: formalized
---

# Erdős Problem 224

> *References:*
> - [erdosproblems.com/224](https://www.erdosproblems.com/224)
> - [DaGr62] Danzer, L. and Gr\"{u}nbaum, B., *\"{U}ber zwei Probleme
>   bez\"{u}glich konvexer K\"{o}rper von P. Erd\H{o}s und von V. L. Klee*.
>   Math. Z. (1962), 95-99.

*Quoted from [FormalConjectures/ErdosProblems/224.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/224.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/224](https://www.erdosproblems.com/224).

The file states 1 research or textbook statement: 1 solved.

## `Erdos224.erdos_224`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos224.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos224.lean).

> If $A\subseteq \mathbb{R}^d$ is any set of $2^d+1$ points then some three points in $A$ determine an obtuse angle.
>
> The general case was proved by Danzer and Gr\"{u}nbaum [DaGr62].

```lean
theorem erdos_224 {d : ℕ} (A : Finset (ℝ^d)) (hcard : A.card = 2 ^ d + 1) :
    ∃ x y z : ℝ^d, x ∈ A ∧ y ∈ A ∧ z ∈ A ∧
      x ≠ y ∧ x ≠ z ∧ y ≠ z ∧ ObtuseAt x y z
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/224.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/224.lean#L48).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/224.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/224.lean)
- [erdosproblems.com/224](https://www.erdosproblems.com/224)
