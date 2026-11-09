---
declaration: theorem
origin: cited
lean: Erdos502.erdos_502
statement: formalized
---

# Erdős Problem 502

> *References:*
> - [erdosproblems.com/502](https://www.erdosproblems.com/502)
> - [Er61] Erdős, Paul, *Some unsolved problems*. Magyar Tud. Akad. Mat. Kutató Int. Közl. (1961),
>   221-254.
> - [BBS83] Bannai, Eiichi and Bannai, Etsuko and Stanton, Dennis, *An upper bound for the
>   cardinality of an $s$-distance subset in real Euclidean space. II*. Combinatorica (1983),
>   147-152.
> - [PePo21] Petrov, Fedor and Pohoata, Cosmin, *A remark on sets with few distances in
>   $\mathbb{R}^d$*. Proc. Amer. Math. Soc. (2021), 569-571.

*Quoted from [FormalConjectures/ErdosProblems/502.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/502.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/502](https://www.erdosproblems.com/502).

The file states 1 research or textbook statement: 1 solved.

## `Erdos502.erdos_502`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos502.lean](https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos502.lean).

> What is the size of the largest $A\subseteq \mathbb{R}^n$ such that there are only two distinct
> distances between elements of $A$? That is,
>
> $$\# \{ \lvert x-y\rvert : x\neq y\in A\} = 2.$$
>
> Asked to Erdős by Coxeter. Bannai, Bannai, and Stanton [BBS83] have proved that
>
> $$\lvert A\rvert \leq \binom{n+2}{2}.$$
>
> A simple proof of this upper bound was given by Petrov and Pohoata [PePo21].
>
> The exact maximum is not known in general: a lower bound of $\binom{n+1}{2}$ follows from the
> construction of Alweiss (see [503]).

```lean
theorem erdos_502 (n : ℕ) (A : Set (ℝ^n)) (hA : A.Finite)
    (hA2 : {d : ℝ | ∃ x ∈ A, ∃ y ∈ A, x ≠ y ∧ dist x y = d}.ncard = 2) :
    A.ncard ≤ (n + 2).choose 2
```

Category `research solved`; AMS [51 Geometry](../../../by-subject/part-02/51-geometry/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/502.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/502.lean#L53).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/502.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/502.lean)
- [erdosproblems.com/502](https://www.erdosproblems.com/502)
