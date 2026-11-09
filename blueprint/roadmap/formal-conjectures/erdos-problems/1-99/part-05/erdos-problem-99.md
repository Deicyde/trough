---
declaration: theorem
origin: cited
lean: Erdos99.erdos_99
statement: formalized
---

# Erdős Problem 99

> *References:*
> * [erdosproblems.com/99](https://www.erdosproblems.com/99)
> * [BeFo99] Bezdek, Andr\'{a}s and Fodor, Ferenc, Minimal diameter of certain sets in the plane. J. Combin. Theory Ser. A (1999), 105-111.
> * [Er94b] Erd\H{o}s, Paul, Some problems in number theory, combinatorics and combinatorial geometry. Math. Pannon. (1994), 261-269.

*Quoted from [FormalConjectures/ErdosProblems/99.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/99.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/99](https://www.erdosproblems.com/99).

The file states 1 research or textbook statement: 1 open.

## `Erdos99.erdos_99`

Open: stated without proof.

> For sufficiently large n, is it the case that any set of n points with minimum distance $1$
> that minimizes diameter must contain an equilateral triangle of side length 1?

```lean
theorem erdos_99 :
    ∀ᶠ n in Filter.atTop, ∀ A : Finset ℝ²,
      A.card = n → HasMinDist1 A →
      (IsMinOn (fun B: Finset ℝ² => diam (B : Set ℝ²)) {B : Finset ℝ² | B.card = n ∧ HasMinDist1 B} A) →
      ∃ᵉ (p ∈ A) (q ∈ A) (r ∈ A), FormsEquilateralTriangle p q r
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/99.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/99.lean#L48).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/99.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/99.lean)
- [erdosproblems.com/99](https://www.erdosproblems.com/99)
