---
declaration: section
origin: cited
lean: AlgebraicGeometry.geometricGenusOfCurve, AlgebraicGeometry.geometricGenusOfCurve_eq_genus
statement: formalized
proof: formalized
---

# 53.11 Geometric genus

Section 53.11 of the Stacks Project, [Tag 0BYE](https://stacks.math.columbia.edu/tag/0BYE). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BYF, a definition

[Tag 0BYF](https://stacks.math.columbia.edu/tag/0BYF) in the Stacks Project.

**`AlgebraicGeometry.geometricGenusOfCurve`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GeometricGenusSmoothModel.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GeometricGenusSmoothModel.lean#L307).

> **Stacks Project, Tag 0BYF.** The *geometric genus* of a geometrically irreducible curve `X`
> over a field `k`: the genus of a smooth projective model of `X` possibly defined over an
> extension field of `k`, as in Tag 0BY4 — for an extension `K/k` such that the nonsingular
> projective model `Y_K` of `(X_K)_red` is smooth over `K`, the genus `dim_K H¹(Y_K, 𝒪_{Y_K})`.
>
> It does not depend on the choice of `K` or of the model, by
> `AlgebraicGeometry.geometricGenusOfCurve_eq_genus`. Such a model exists by Tag 0BY4 (2)
> (`AlgebraicGeometry.nonempty_smoothModelOverExtension_of_isProper` for proper `X`); the value
> `0` is a junk value for the case where none is supplied.

```lean
def geometricGenusOfCurve : ℕ
```

**`AlgebraicGeometry.geometricGenusOfCurve_eq_genus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GeometricGenusSmoothModel.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GeometricGenusSmoothModel.lean#L313). The attribute's comment: “the definition is independent of the extension field and of the smooth model”.

> **Stacks Project, Tag 0BYF, well-definedness.** The geometric genus of `X` is the genus of
> every smooth projective model of `X` over every extension field of `k`.

```lean
theorem geometricGenusOfCurve_eq_genus (N : SmoothModelOverExtension k sX) :
    geometricGenusOfCurve k sX = genus N.model.structureMap
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 53.11, Tag 0BYE](https://stacks.math.columbia.edu/tag/0BYE)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
