---
declaration: theorem
origin: cited
lean: WeakTiling.problem_4_1, WeakTiling.problem_4_2, WeakTiling.problem_4_3
statement: formalized
---

# Weak tiling problems

> Problems 4.1, 4.2, and 4.3 from [arxiv/2506.23631](https://arxiv.org/abs/2506.23631).
>
> *Reference:*
> * [Geometric implications of weak tiling](https://arxiv.org/abs/2506.23631)
>
> See also `FormalConjectures.Wikipedia.Fuglede` for Fuglede's spectral set conjecture, which
> motivates the study of weak tilings.

*Quoted from [FormalConjectures/Paper/WeakTiling.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/WeakTiling.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 1 open and 2 solved.

## `WeakTiling.problem_4_1`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/weak-tiling-bounded-density/blob/5d10499e1932cc017b7aaf8e931926dc969bd8f7/lean/WeakTilingProblem41FC.lean#L11484-L11487](https://github.com/KitaKen1/weak-tiling-bounded-density/blob/5d10499e1932cc017b7aaf8e931926dc969bd8f7/lean/WeakTilingProblem41FC.lean#L11484-L11487).

> **Problem 4.1.** Let $\Omega \subset \mathbb{R}$ be a finite union of intervals and $\nu$
>     a weak tiling measure for $\Omega$. Must $\mathrm{supp}(\nu)$ have bounded density?
>
> The answer is positive: Kenta Kitamura (KitaKen1 on GitHub) has given a Lean proof
> ([weak-tiling-bounded-density](https://github.com/KitaKen1/weak-tiling-bounded-density)).

```lean
theorem problem_4_1 :
    ∀ (Ω : Set ℝ) (_ : IsFiniteUnionOfIntervals Ω)
      (ν : Measure ℝ) (_ : IsWeakTilingMeasure Ω ν), HasBoundedDensity ν.support
```

Category `research solved`; AMS [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md), [46 Functional analysis](../../by-subject/part-02/46-functional-analysis/README.md). Declared in [FormalConjectures/Paper/WeakTiling.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/WeakTiling.lean#L90).

## `WeakTiling.problem_4_2`

Open: stated without proof.

> **Problem 4.2.** Let $\Omega \subset \mathbb{R}$ be a finite union of three or more
> intervals. If $\Omega$ weakly tiles its complement, must it also tile its complement
> properly?

```lean
theorem problem_4_2 :
    ∀ (n : ℕ) (_ : 3 ≤ n) (Ω : Set ℝ)
      (_ : IsUnionOfNIntervals n Ω) (ν : Measure ℝ) (_ : IsWeakTilingMeasure Ω ν),
      ∃ T : Set ℝ, IsProperTiling Ω T
```

Category `research open`; AMS [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md), [46 Functional analysis](../../by-subject/part-02/46-functional-analysis/README.md). Declared in [FormalConjectures/Paper/WeakTiling.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/WeakTiling.lean#L99).

## `WeakTiling.problem_4_3`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/weak-tiling-counterexample/blob/5bf93234cc51f02fd7681407d77dcebde592f3ac/formal-conjectures-v4.27.0/WeakTilingCounterexample.lean](https://github.com/KitaKen1/weak-tiling-counterexample/blob/5bf93234cc51f02fd7681407d77dcebde592f3ac/formal-conjectures-v4.27.0/WeakTilingCounterexample.lean).

> **Problem 4.3.** Let $\Omega \subset \mathbb{R}$ be a finite union of intervals and $\nu$
>     a weak tiling measure for $\Omega$. Must $\nu$ be expressible as a convex combination of
>     proper tiling measures?
>
> The answer is negative.
>
> An AI-assisted investigation by Kenta Kitamura produced a counterexample for
> $\Omega = (0,1) \cup (2,3) \cup (12,13) \cup (30,31)$.
> A finite computation shows that every convex combination of proper tiling measures
> for this $\Omega$ assigns equal mass to $\{7\}$ and $\{15\}$.
> However, the constructed weak tiling measure $\nu$ satisfies
> $\nu(\{7\}) = \frac{1}{2}$ and $\nu(\{15\}) = 0$, so $\nu$ cannot be expressed
> as a convex combination of proper tiling measures.

```lean
theorem problem_4_3 :
    ¬ ∀ (Ω : Set ℝ) (_ : IsFiniteUnionOfIntervals Ω)
      (ν : Measure ℝ) (_ : IsWeakTilingMeasure Ω ν),
      ∃ (T : ℕ → Set ℝ) (c : ℕ → ℝ≥0), (∀ i, IsProperTiling Ω (T i)) ∧ ∑' i : ℕ, c i = 1 ∧
      ν = Measure.sum
        (fun i => (c i : ℝ≥0∞) • Measure.sum (fun t : T i => Measure.dirac (t : ℝ)))
```

Category `research solved`; AMS [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md), [46 Functional analysis](../../by-subject/part-02/46-functional-analysis/README.md). Declared in [FormalConjectures/Paper/WeakTiling.lean, line 123](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/WeakTiling.lean#L123).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/WeakTiling.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/WeakTiling.lean)
- [Geometric implications of weak tiling](https://arxiv.org/abs/2506.23631)
