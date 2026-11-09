---
declaration: theorem
origin: cited
lean: Erdos1071.erdos_1071.parts.i, Erdos1071.erdos_1071.parts.ii
statement: formalized
---

# Erdős Problem 1071

> *References:*
> * [erdosproblems.com/1071](https://www.erdosproblems.com/1071)
> * [Da85] Danzer, L., _Some combinatorial and metric problems in geometry_.
>   Intuitive geometry (Siófok, 1985), 167-177.

*Quoted from [FormalConjectures/ErdosProblems/1071.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1071.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1071](https://www.erdosproblems.com/1071).

The file states 2 research or textbook statements: 2 solved.

## `Erdos1071.erdos_1071.parts.i`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos1071.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos1071.lean).

> Can a finite set of disjoint unit segments in a unit square be maximal?
> Solved affirmatively by [Da85], who gave an explicit construction.
>
> This was formalized in Lean by Alexeev using Aristotle and ChatGPT.

```lean
theorem erdos_1071.parts.i :
    ∃ S : Finset (ℝ² × ℝ²),
      Maximal (fun T : Finset (ℝ² × ℝ²) =>
        (∀ seg ∈ T, dist seg.1 seg.2 = 1 ∧
          seg.1 0 ∈ Icc 0 1 ∧ seg.1 1 ∈ Icc 0 1 ∧
          seg.2 0 ∈ Icc 0 1 ∧ seg.2 1 ∈ Icc 0 1) ∧
          (T : Set (ℝ² × ℝ²)).Pairwise SegmentsDisjoint) S
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1071.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1071.lean#L47).

## `Erdos1071.erdos_1071.parts.ii`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos1071b.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos1071b.lean).

> Is there a region $R$ with a maximal set of disjoint unit line segments that is countably infinite?
> Here a unit line segment is a rotated and translated copy of the open interval $(0,1)$, and it is
> required to be contained in $R$.
> Solved affirmatively by [Fo99], who gave an explicit construction.
>
> This was formalized in Lean by Alexeev using Aristotle and ChatGPT.

```lean
theorem erdos_1071.parts.ii :
    ∃ (R : Set ℝ²) (S : Set (ℝ² × ℝ²)),
      IsOpen R ∧ IsConnected R ∧ S.Countable ∧ S.Infinite ∧
      Maximal (fun T : Set (ℝ² × ℝ²) =>
        (∀ seg ∈ T, dist seg.1 seg.2 = 1 ∧ openSegment ℝ seg.1 seg.2 ⊆ R) ∧
        T.Pairwise SegmentsDisjoint) S
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1071.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1071.lean#L65).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1071.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1071.lean)
- [erdosproblems.com/1071](https://www.erdosproblems.com/1071)
