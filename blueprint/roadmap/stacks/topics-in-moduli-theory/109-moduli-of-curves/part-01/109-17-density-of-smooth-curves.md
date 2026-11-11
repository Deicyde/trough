---
declaration: section
origin: cited
lean: AlgebraicGeometry.curvesPointSet_smooth_isOpen_dense_in_lciPlus
statement: formalized
proof: formalized
---

# 109.17 Density of smooth curves

Section 109.17 of the Stacks Project, [Tag 0E85](https://stacks.math.columbia.edu/tag/0E85). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0E86, a lemma

[Tag 0E86](https://stacks.math.columbia.edu/tag/0E86) in the Stacks Project.

**`AlgebraicGeometry.curvesPointSet_smooth_isOpen_dense_in_lciPlus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesSmoothDensePoints.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesSmoothDensePoints.lean#L140).

> **Stacks 0E86.** The inclusion `|Curves^{smooth}| ⊂ |Curves^{lci+}|` is that of an open dense
> subset.
>
> `Curves^{smooth}` is the substack of the stack of curves of smooth families of curves, and
> `Curves^{lci+}` that of families `X ⟶ S` which are local complete intersection morphisms whose
> singular locus is finite over `S` (Stacks 0DZX); `|Curves^{smooth}|` and `|Curves^{lci+}|` are
> their images in `|Curves|`, with the topology of Stacks 04Y8, and `|Curves^{lci+}|` carries the
> subspace topology.

```lean
theorem curvesPointSet_smooth_isOpen_dense_in_lciPlus :
    curvesPointSet B hZ (IsSmoothFamily B hZ) ⊆ curvesPointSet B hZ (IsLciPlusFamily B hZ) ∧
      IsOpen (Subtype.val ⁻¹' curvesPointSet B hZ (IsSmoothFamily B hZ) :
        Set (curvesPointSet B hZ (IsLciPlusFamily B hZ))) ∧
      Dense (Subtype.val ⁻¹' curvesPointSet B hZ (IsSmoothFamily B hZ) :
        Set (curvesPointSet B hZ (IsLciPlusFamily B hZ)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 109.17, Tag 0E85](https://stacks.math.columbia.edu/tag/0E85)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
