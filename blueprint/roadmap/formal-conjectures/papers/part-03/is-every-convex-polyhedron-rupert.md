---
declaration: theorem
origin: cited
lean: Rupert.is_every_convex_polyhedron_rupert
statement: formalized
---

# Is Every Convex Polyhedron Rupert?

> A polyhedron is Rupert if one can cut a hole in it and pass another
> copy of the same polyhedron through that hole.
>
> More formally: a convex body in ℝ³ is a compact, convex set with
> nonempty interior. A convex body X is said to be Rupert if there are
> two affine transforms T₁, T₂ ∈ SE(3) such that π(T₁(X)) ⊆
> int(π(T₂(X))), where π : ℝ³ → ℝ² is the evident projection, and int
> denotes topological interior.
>
> Not all convex bodies are Rupert. For example,
> - the unit ball is not Rupert
> - the circular cylinder of unit diameter and height
>   closed on each end by disks is not Rupert
>
> However, many convex polyhedra are Rupert. All Platonic solids, and
> most Archimedean and Catalan solids are known to be Rupert.
>
> Question: are all convex polyhedra with nonempty interior Rupert?
>
> *References:*
>
> * [Platonic Passages](https://www.researchgate.net/publication/314715434_Platonic_Passages),
>   R. P. Jerrard, J. E. Wetzel, and L. Yuan., Math. Mag., 90(2):87–98,
>   2017. conjectures ("with a certain hesitancy") that perhaps all
>   convex polyhedra are Rupert.
>
> * However, [An Algorithmic Approach to Rupert's Problem](https://arxiv.org/pdf/2112.13754#cite.JeWeYu17)
>   describes experimental evidence to suggest that three Archimedean
>   solids may not be Rupert.
>
> * [Optimizing for the Rupert property](https://arxiv.org/abs/2210.00601)
>   is the source of some of the Catalan solid results, and has more
>   results for Johnson polyhedra as well.
>
> * [This video by David Renshaw](https://www.youtube.com/watch?v=evKFok65t_E) visualizes
>   known results for Platonic, Archimedean, and Catalan solids.
>
> * This problem's name comes from the fact that it is a generalization
>   of [Prince Rupert's Cube](https://en.wikipedia.org/wiki/Prince_Rupert%27s_cube).
>
> * [A convex polyhedron without Rupert's property](https://arxiv.org/abs/2508.18475),
>   Jakob Steininger and Sergey Yurkevich, 2025. Constructs a convex polyhedron and
>   a proof that it is not Rupert, resolving the open question.

*Quoted from [FormalConjectures/Paper/Rupert.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/Rupert.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `Rupert.is_every_convex_polyhedron_rupert`

Solved: stated here; a Lean proof is at [https://github.com/jcreedcmu/Noperthedron/blob/1ee88118097acc9db768b44b3c6ea9f60a4e4b67/KernelCaseAnalysis/ProofOfMainTheorem.lean#L21](https://github.com/jcreedcmu/Noperthedron/blob/1ee88118097acc9db768b44b3c6ea9f60a4e4b67/KernelCaseAnalysis/ProofOfMainTheorem.lean#L21).

> There exists a convex polyhedron with nonempty interior for which the Rupert property does
> not hold.

```lean
theorem is_every_convex_polyhedron_rupert :
    ¬ ∀ (vertices : Finset ℝ³),
       (interior (convexHull ℝ vertices : Set ℝ³)).Nonempty → IsRupert vertices
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Paper/Rupert.lean, line 115](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/Rupert.lean#L115).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/Rupert.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/Rupert.lean)
- [Platonic Passages](https://www.researchgate.net/publication/314715434_Platonic_Passages)
