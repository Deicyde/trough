---
declaration: theorem
origin: cited
lean: EuclideanRamseyCircle.at_most_five_circle_points_ramsey
statement: formalized
---

# Euclidean Ramsey configurations on a circle

> *Reference:* OpenAI, *A classification of finite Euclidean Ramsey configurations* (2026).
> https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-classification-of-finite-Euclidean-Ramsey-configurations-September-23-2026/paper.pdf

*Quoted from [FormalConjectures/Paper/EuclideanRamseyCircle.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/EuclideanRamseyCircle.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `EuclideanRamseyCircle.at_most_five_circle_points_ramsey`

Solved: stated here without proof.

> Every nonempty configuration of at most five distinct points on a circle is Euclidean
> Ramsey: every finite colouring of a suitable Euclidean space has a monochromatic
> copy with the same pairwise distances. Singletons and radius-zero circles are included.

```lean
theorem at_most_five_circle_points_ramsey {s : ℕ} (a : Fin s → E (Fin 2))
    (hs : 0 < s) (hs5 : s ≤ 5) (ha : Function.Injective a)
    (hsphere : ∃ c : E (Fin 2), ∃ r : ℝ, ∀ i, dist (a i) c = r) :
    ∀ colors : ℕ, 2 ≤ colors → ∃ D : ℕ, 1 ≤ D ∧
      ∀ c : E (Fin D) → Fin colors, ∃ b : Fin s → E (Fin D),
        (∀ i j, dist (b i) (b j) = dist (a i) (a j)) ∧
          ∃ k : Fin colors, ∀ i, c (b i) = k
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Paper/EuclideanRamseyCircle.lean, line 37](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/EuclideanRamseyCircle.lean#L37).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/EuclideanRamseyCircle.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/EuclideanRamseyCircle.lean)
- [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-classification-of-finite-Euclidean-Ramsey-configurations-September-23-2026/paper.pdf](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-classification-of-finite-Euclidean-Ramsey-configurations-September-23-2026/paper.pdf)
