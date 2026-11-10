---
declaration: section
origin: cited
lean: Stacks.Duality.serreEquivalenceOfIsGorenstein
statement: formalized
proof: formalized
---

# 57.4 Examples of Serre functors

Section 57.4 of the Stacks Project, [Tag 0FY7](https://stacks.math.columbia.edu/tag/0FY7). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FY8, a lemma

[Tag 0FY8](https://stacks.math.columbia.edu/tag/0FY8) in the Stacks Project.

**`Stacks.Duality.serreEquivalenceOfIsGorenstein`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/SerreFunctor.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/SerreFunctor.lean#L366).

> **Stacks Project, Tag 0FY8.** Let `X` be a proper Gorenstein scheme over a field `k`, and let
> `ω_X^•` be its dualizing complex ([Stacks, Tag 0FVV]). Then `S(K) = K ⊗^𝐋 ω_X^•` is a Serre functor
> on `D_perf(𝒪_X)`: there is a Serre equivalence of `D_perf(𝒪_X)` (`CategoryTheory.SerreEquivalence`)
> whose functor is derived tensoring with `ω_X^•`.

```lean
def serreEquivalenceOfIsGorenstein [AlgebraicGeometry.IsGorenstein Y.left] :
    letI : Linear k Y.left.Modules := modulesLinear k Y
    { E : SerreEquivalence k (C := perfectDerived Y.left) //
      Nonempty (E.equivalence.functor ⋙ ObjectProperty.ι _ ≅ ObjectProperty.ι _ ⋙
        (Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor
          Y.left.toRingedSpace.sheaf).flip.obj (dualizingComplexOverField Y.hom).obj) }
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 57.4, Tag 0FY7](https://stacks.math.columbia.edu/tag/0FY7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
