---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.relativelyRepresentable_of_mono_to_coproduct_spec_zeroDimensional
statement: formalized
proof: formalized
---

# 68.19 Monomorphisms

Section 68.19 of the Stacks Project, [Tag 06RY](https://stacks.math.columbia.edu/tag/06RY). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06RZ, a lemma

[Tag 06RZ](https://stacks.math.columbia.edu/tag/06RZ) in the Stacks Project.

**`AlgebraicGeometry.Space.relativelyRepresentable_of_mono_to_coproduct_spec_zeroDimensional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MonoToZeroDimensionalLocalSpectra.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/MonoToZeroDimensionalLocalSpectra.lean#L208).

> **Stacks 06RZ.** A monomorphism of algebraic spaces over `S` whose target is a disjoint
> union of spectra of zero-dimensional local rings is representable; equivalently its source is a
> scheme.

```lean
theorem relativelyRepresentable_of_mono_to_coproduct_spec_zeroDimensional
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hF : IsAlgebraicSpace B S hS F) (f : F ⟶ G)
    [Mono f] (Y : BigFppfOver B S hS) (eG : G ≅ yoneda.obj Y) (I : Type u)
    (A : I → CommRingCat.{u}) (hlocal : ∀ i, IsLocalRing (A i))
    (hdim : ∀ i, ringKrullDim (A i) = 0)
    (eY : (BigFppfOver.toScheme B S hS).obj Y ≅ ∐ fun i : I ↦ Spec (A i)) :
    yoneda.relativelyRepresentable f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 68.19, Tag 06RY](https://stacks.math.columbia.edu/tag/06RY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
