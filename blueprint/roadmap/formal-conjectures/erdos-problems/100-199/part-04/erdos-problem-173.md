---
declaration: theorem
origin: cited
lean: Erdos173.erdos_173, Erdos173.erdos_173.variants.right_triangle, Erdos173.erdos_173.variants.equilateral_exception
statement: formalized
---

# Erdős Problem 173

> *References:*
> - [erdosproblems.com/173](https://www.erdosproblems.com/173)
> - [Sh76] Shader, L. E., *All right triangles are Ramsey in $E^2$!*. J. Combin. Theory Ser. A
>   (1976), 385-389.

*Quoted from [FormalConjectures/ErdosProblems/173.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/173.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/173](https://www.erdosproblems.com/173).

The file states 3 research or textbook statements: 1 open and 2 solved.

## `Erdos173.erdos_173`

Open: stated without proof.

> In any $2$-colouring of $\mathbb{R}^2$, for all but at most one triangle $T$ (up to
> congruence), there is a monochromatic congruent copy of $T$.
>
> The colouring is arbitrary. No measurability is assumed. `≅` compares vertices with the same
> label, so the conclusion allows a relabelling `σ`.

```lean
theorem erdos_173 : ∀ (c : ℝ² → Fin 2) (T₁ T₂ : Triangle ℝ ℝ²),
    ¬ HasMonochromaticCopy c T₁ → ¬ HasMonochromaticCopy c T₂ →
      ∃ σ : Equiv.Perm (Fin 3), T₁.points ∘ σ ≅ T₂.points
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/173.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/173.lean#L52).

## `Erdos173.erdos_173.variants.right_triangle`

Solved: stated here without proof.

> Shader [Sh76] proved that in any $2$-colouring of $\mathbb{R}^2$, every right-angled triangle
> has a monochromatic congruent copy.

```lean
theorem erdos_173.variants.right_triangle (c : ℝ² → Fin 2) (T : Triangle ℝ ℝ²)
    (hT : ∠ (T.points 0) (T.points 1) (T.points 2) = Real.pi / 2) :
    HasMonochromaticCopy c T
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/173.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/173.lean#L62).

## `Erdos173.erdos_173.variants.equilateral_exception`

Solved: stated here without proof.

> The exceptional triangle can exist: colouring the plane in alternating half-open strips of
> suitable width gives no monochromatic copy of some equilateral triangle.

```lean
theorem erdos_173.variants.equilateral_exception : ∃ (c : ℝ² → Fin 2) (T : Triangle ℝ ℝ²),
    dist (T.points 0) (T.points 1) = dist (T.points 1) (T.points 2) ∧
    dist (T.points 1) (T.points 2) = dist (T.points 2) (T.points 0) ∧
    ¬ HasMonochromaticCopy c T
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/173.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/173.lean#L72).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/173.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/173.lean)
- [erdosproblems.com/173](https://www.erdosproblems.com/173)
