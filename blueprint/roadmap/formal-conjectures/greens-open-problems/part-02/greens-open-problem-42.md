---
declaration: theorem
origin: cited
lean: Green42.green_42, Green42.green_42.variants.dimension_one, Green42.green_42.variants.dimension_eight, Green42.green_42.variants.dimension_twenty_four
statement: formalized
---

# Green's Open Problem 42

> *References:*
> - [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.42)
> - [CoEl03] Cohn, Henry, and Noam Elkies. "New upper bounds on sphere packings I."
>   Annals of Mathematics (2003): 689-714.
> - [Vi17] Viazovska, Maryna S. "The sphere packing problem in dimension 8."
>   Annals of mathematics (2017): 991-1015.
> - [CKM17] Cohn, H., Kumar, A., Miller, S., Radchenko, D., & Viazovska, M. (2017).
>   The sphere packing problem in dimension 24. Annals of mathematics, 185(3), 1017-1033.
> - [Sa21] Sardari, Naser Talebizadeh. "Higher Fourier interpolation on the plane."
>   arXiv preprint arXiv:2102.08753 (2021).
> - [OAI26a] OpenAI, *A sharp Fourier certificate for planar circle packing*.
>   OpenAI Math Release preprint (2026).
>   https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-sharp-Fourier-certificate-for-planar-circle-packing-September-23-2026/paper.pdf

*Quoted from [FormalConjectures/GreensOpenProblems/42.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/42.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 4 solved.

## `Green42.green_42`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Analysis/PlanarPacking/Main.lean#L32](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Analysis/PlanarPacking/Main.lean#L32).

> Can the Cohn-Elkies scheme be used to prove the optimal bound for circle-packings in 2 dimensions?
>
> The answer is "yes". This was proved by an internal OpenAI model in September 2026 [OAI26a]; see
> the linked Lean proof, which constructs a radial Schwartz certificate normalised to minimum
> distance $1$.

```lean
theorem green_42 :
    CohnElkiesOptimal 2 (Real.sqrt 3 / 6)
```

Category `research solved`; AMS [51 Geometry](../../by-subject/part-02/51-geometry/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/42.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/42.lean#L99).

## `Green42.green_42.variants.dimension_one`

Solved: stated here without proof.

> [CoEl03] proved this when $d = 1$.

```lean
theorem green_42.variants.dimension_one :
    CohnElkiesOptimal 1 (1 / 2)
```

Category `research solved`; AMS [51 Geometry](../../by-subject/part-02/51-geometry/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/42.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/42.lean#L105).

## `Green42.green_42.variants.dimension_eight`

Solved: stated here; a Lean proof is at [https://github.com/math-inc/Sphere-Packing-Lean/blob/main/SpherePacking/Dim8/MainTheorem.lean](https://github.com/math-inc/Sphere-Packing-Lean/blob/main/SpherePacking/Dim8/MainTheorem.lean).

> [Vi17] established the case $d = 8$.

```lean
theorem green_42.variants.dimension_eight :
    CohnElkiesOptimal 8 (1 / 16)
```

Category `research solved`; AMS [51 Geometry](../../by-subject/part-02/51-geometry/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/42.lean, line 112](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/42.lean#L112).

## `Green42.green_42.variants.dimension_twenty_four`

Solved: stated here; a Lean proof is at [https://github.com/math-inc/Sphere-Packing-Lean/blob/main/SpherePacking/Dim24/MainTheorem.lean](https://github.com/math-inc/Sphere-Packing-Lean/blob/main/SpherePacking/Dim24/MainTheorem.lean).

> In [CKM17], [Vi17] was adapted to $d = 24$.

```lean
theorem green_42.variants.dimension_twenty_four :
    CohnElkiesOptimal 24 1
```

Category `research solved`; AMS [51 Geometry](../../by-subject/part-02/51-geometry/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/42.lean, line 119](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/42.lean#L119).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/42.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/42.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.42)
