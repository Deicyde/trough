---
declaration: theorem
origin: cited
lean: Erdos831.erdos_831, Erdos831.erdos_831.variants.szekeres
statement: formalized
---

# Erdős Problem 831

> *References:*
> - [erdosproblems.com/831](https://www.erdosproblems.com/831)
> - [Er75h] Erdős, P., *Some problems on elementary geometry*. Austral. Math. Soc. Gaz. (1975), 2-3.
>   [PDF](https://www.renyi.hu/~p_erdos/1975-41.pdf)
> - [Er92e] Erdős, Pál, *Some Unsolved problems in Geometry, Number Theory and Combinatorics*. Eureka
>   (1992), 44-48.

*Quoted from [FormalConjectures/ErdosProblems/831.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/831.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/831](https://www.erdosproblems.com/831).

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 1 API statement, counted here but not shown.

## `Erdos831.erdos_831`

Open: stated without proof.

> Let $h(n)$ be maximal such that in any $n$ points in $\mathbb{R}^2$ (with no three on a line and
> no four on a circle) there are at least $h(n)$ many circles of different radii passing through
> three points. Estimate $h(n)$.
>
> Erdős asks this in [Er75h, pp. 2-3] (see also [Er92e]); see also Problems 104 and 506. We read
> "estimate" as the order of magnitude `=Θ`. [Er75h] also asks how $h(n)$ changes if one only
> assumes that the points are not all on a circle; this is not formalised.

```lean
theorem erdos_831 :
    (fun n : ℕ ↦ (h n : ℝ)) =Θ[atTop] erdos_831.answer
```

Category `research open`; AMS [51 Geometry](../../../by-subject/part-02/51-geometry/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/831.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/831.lean#L80).

## `Erdos831.erdos_831.variants.szekeres`

Solved: stated here without proof.

> Erdős [Er75h, p. 2] attributes to E. Szekeres the observation that for three points
> $x_1,x_2,x_3$ of the plane, not on a line, there is a unique point $x_4$ such that
> $x_1,x_2,x_3,x_4$ are not on a circle and the four circles determined by the four triples of these
> points have the same radius; one can take $x_4$ to be the orthocentre of the triangle
> $x_1x_2x_3$.
>
> Read literally this fails for a right-angled triangle, whose orthocentre is a vertex, so we assume
> that the triangle has no right angle. We also require the four points to be in general position,
> so that the four circles exist.

```lean
theorem erdos_831.variants.szekeres (x₁ x₂ x₃ : ℝ²)
    (hcol : ¬ Collinear ℝ ({x₁, x₂, x₃} : Set ℝ²)) (hright : ¬ IsRightAngled x₁ x₂ x₃) :
    ∃! x₄ : ℝ², x₄ ∉ ({x₁, x₂, x₃} : Set ℝ²) ∧
      InGeneralPosition ({x₁, x₂, x₃, x₄} : Set ℝ²) ∧
      (circleRadii ({x₁, x₂, x₃, x₄} : Set ℝ²)).ncard = 1
```

Category `research solved`; AMS [51 Geometry](../../../by-subject/part-02/51-geometry/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/831.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/831.lean#L96).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/831.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/831.lean)
- [erdosproblems.com/831](https://www.erdosproblems.com/831)
