---
declaration: theorem
origin: cited
lean: ErdosUlamProblem.erdos_ulam_problem, ErdosUlamProblem.erdos_ulam_problem.variants.anning_erdos, ErdosUlamProblem.erdos_ulam_problem.variants.solymosi_de_zeeuw
statement: formalized
---

# The Erdős–Ulam problem

> *References:*
> * [Wikipedia](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Ulam_problem)
> * [Ul60] Ulam, S. M. (1960). *A Collection of Mathematical Problems.* Interscience, p. 40.
> * [SdZ10] Solymosi, J. and de Zeeuw, F. (2010). "On a question of Erdős and Ulam."
>   *Discrete Comput. Geom.* 43, pp. 393--401. [arXiv:0806.3095](https://arxiv.org/abs/0806.3095)
> * [Ta14] Tao, T. (2014). "The Erdős–Ulam problem, varieties of general type, and the
>   Bombieri–Lang conjecture." Blog post,
>   [terrytao.wordpress.com](https://terrytao.wordpress.com/2014/12/20/the-erdos-ulam-problem-varieties-of-general-type-and-the-bombieri-lang-conjecture/)
> * [AE45] Anning, N. H. and Erdős, P. (1945). "Integral distances." *Bull. Amer. Math. Soc.* 51,
>   pp. 598--600.

*Quoted from [FormalConjectures/Wikipedia/ErdosUlamProblem.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ErdosUlamProblem.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 1 test statement, counted here but not shown.

## `ErdosUlamProblem.erdos_ulam_problem`

Open: stated without proof.

> **The Erdős–Ulam problem (Ulam 1945).**
>
> Is there a dense subset of the plane whose points are at pairwise rational distances?
> Conjecturally, no such set exists. Solymosi and de Zeeuw [SdZ10] proved that if a
> rational-distance set has infinitely many points on a line or circle, all but finitely many
> points lie on that line or circle.

```lean
theorem erdos_ulam_problem :
    ∃ S : Set (EuclideanSpace ℝ (Fin 2)), Dense S ∧ PairwiseRationalDistances S
```

Category `research open`; AMS [51 Geometry](../../by-subject/part-02/51-geometry/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Wikipedia/ErdosUlamProblem.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ErdosUlamProblem.lean#L56).

## `ErdosUlamProblem.erdos_ulam_problem.variants.anning_erdos`

Solved: stated here without proof.

> **Infinite integer-distance sets are collinear (Anning–Erdős 1945).**
>
> Anning and Erdős proved that an infinite set of points in the plane with pairwise *integer*
> distances must be contained in a line.
>
> *Reference:* [AE45].

```lean
theorem erdos_ulam_problem.variants.anning_erdos
    (S : Set (EuclideanSpace ℝ (Fin 2))) (hinf : S.Infinite)
    (hd : ∀ p ∈ S, ∀ q ∈ S, ∃ n : ℤ, dist p q = (n : ℝ)) :
    ∃ a b : EuclideanSpace ℝ (Fin 2), a ≠ b ∧
      S ⊆ {x | ∃ t : ℝ, x = a + t • (b - a)}
```

Category `research solved`; AMS [51 Geometry](../../by-subject/part-02/51-geometry/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Wikipedia/ErdosUlamProblem.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ErdosUlamProblem.lean#L82).

## `ErdosUlamProblem.erdos_ulam_problem.variants.solymosi_de_zeeuw`

Solved: stated here without proof.

> If a plane set with pairwise rational distances has infinitely many points on a line or
> circle, all but finitely many of its points are contained in a line or circle.
> This is the finite-exception corollary of [SdZ10, Theorem 2.2], whose sharper bounds are
> four exceptions for a line and three for a circle.

```lean
theorem erdos_ulam_problem.variants.solymosi_de_zeeuw
    (S : Set (EuclideanSpace ℝ (Fin 2))) (hd : PairwiseRationalDistances S)
    (hstructure :
      (∃ a b : EuclideanSpace ℝ (Fin 2), a ≠ b ∧
        {x ∈ S | ∃ t : ℝ, x = a + t • (b - a)}.Infinite) ∨
      (∃ (c : EuclideanSpace ℝ (Fin 2)) (ρ : ℝ), 0 < ρ ∧
        {x ∈ S | dist x c = ρ}.Infinite)) :
    (∃ a b : EuclideanSpace ℝ (Fin 2), a ≠ b ∧
        {x ∈ S | ¬ ∃ t : ℝ, x = a + t • (b - a)}.Finite) ∨
    (∃ (c : EuclideanSpace ℝ (Fin 2)) (ρ : ℝ), 0 < ρ ∧
        {x ∈ S | dist x c ≠ ρ}.Finite)
```

Category `research solved`; AMS [51 Geometry](../../by-subject/part-02/51-geometry/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Wikipedia/ErdosUlamProblem.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ErdosUlamProblem.lean#L96).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/ErdosUlamProblem.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/ErdosUlamProblem.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Ulam_problem)
