---
declaration: theorem
origin: cited
lean: Erdos105.erdos_105, Erdos105.erdos_105.variants.hickerson, Erdos105.erdos_105.variants.beck_szemeredi_trotter, Erdos105.erdos_105.variants.sub_four
statement: formalized
---

# Erdős Problem 105

> *References:*
> - [erdosproblems.com/105](https://www.erdosproblems.com/105)
> - [Be83] Beck, József, *On the lattice property of the plane and some problems of Dirac, Motzkin
>   and Erdős in combinatorial geometry*. Combinatorica (1983), 281-297.
> - [ErPu95] Erdős, P. and Purdy, G., *Two combinatorial problems in the plane*. Discrete Comput.
>   Geom. (1995), 441-443.
> - [SzTr83] Szemerédi, Endre and Trotter, Jr., William T., *Extremal problems in discrete
>   geometry*. Combinatorica (1983), 381-392.

*Quoted from [FormalConjectures/ErdosProblems/105.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/105.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/105](https://www.erdosproblems.com/105).

The file states 4 research or textbook statements: 4 solved.

## `Erdos105.erdos_105`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos105.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos105.lean).

> Let $A,B\subset \mathbb{R}^2$ be disjoint sets of size $n$ and $n-3$ respectively, with not all
> of $A$ contained on a single line. Is there a line which contains at least two points from $A$
> and no points from $B$?
>
> This has been disproved by Xichuan in the comments, who has found three explicit
> counterexamples.

```lean
theorem erdos_105 :
    ¬ ∀ A B : Finset ℝ², Disjoint A B → A.card = B.card + 3 →
      ¬ Collinear ℝ (A : Set ℝ²) →
      ∃ p ∈ A, ∃ q ∈ A, p ≠ q ∧ ∀ b ∈ B, b ∉ line[ℝ, p, q]
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/105.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/105.lean#L49).

## `Erdos105.erdos_105.variants.hickerson`

Solved: stated here without proof.

> A construction of Hickerson shows that this fails with $n-2$.

```lean
theorem erdos_105.variants.hickerson : ¬ ∀ A B : Finset ℝ², Disjoint A B →
    A.card = B.card + 2 → ¬ Collinear ℝ (A : Set ℝ²) →
    ∃ p ∈ A, ∃ q ∈ A, p ≠ q ∧ ∀ b ∈ B, b ∉ line[ℝ, p, q]
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/105.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/105.lean#L59).

## `Erdos105.erdos_105.variants.beck_szemeredi_trotter`

Solved: stated here without proof.

> A result independently proved by Beck [Be83] and Szemerédi and Trotter [SzTr83] (see [211])
> implies it is true with $n-3$ replaced by $cn$ for some constant $c>0$.

```lean
theorem erdos_105.variants.beck_szemeredi_trotter : ∃ c > (0 : ℝ),
    ∀ A B : Finset ℝ², Disjoint A B → (B.card : ℝ) ≤ c * A.card →
      ¬ Collinear ℝ (A : Set ℝ²) →
      ∃ p ∈ A, ∃ q ∈ A, p ≠ q ∧ ∀ b ∈ B, b ∉ line[ℝ, p, q]
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/105.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/105.lean#L69).

## `Erdos105.erdos_105.variants.sub_four`

Solved: stated here; a Lean proof is at [https://github.com/kusasyu36/erdos105-sub-four/blob/a2d073034d2d15af216d8bd71771f1eda13b3de3/Erdos105SubFour.lean#L93](https://github.com/kusasyu36/erdos105-sub-four/blob/a2d073034d2d15af216d8bd71771f1eda13b3de3/Erdos105SubFour.lean#L93).

> It remains possible that this holds with $n-4$ (or in general with $n-O(1)$ or $(1-o(1))n$).
>
> This fails with $n-4$ as well: Core_65536 gives an explicit counterexample in the
> [forum](https://www.erdosproblems.com/forum/thread/105#post-8033) (24 July 2026), with $|A| = 10$
> and $|B| = 6$ and integer coordinates, in which every line through two points of $A$ contains a
> point of $B$. The incidences have been verified in Lean.

```lean
theorem erdos_105.variants.sub_four :
    ¬ ∀ A B : Finset ℝ², Disjoint A B → A.card = B.card + 4 →
      ¬ Collinear ℝ (A : Set ℝ²) →
      ∃ p ∈ A, ∃ q ∈ A, p ≠ q ∧ ∀ b ∈ B, b ∉ line[ℝ, p, q]
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/105.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/105.lean#L86).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/105.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/105.lean)
- [erdosproblems.com/105](https://www.erdosproblems.com/105)
