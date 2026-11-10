---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.derivedPushoutEssentialImage
statement: formalized
proof: formalized
---

# 81.8 Pushouts and derived categories

Section 81.8 of the Stacks Project, [Tag 0DL6](https://stacks.math.columbia.edu/tag/0DL6). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DL7, a lemma

[Tag 0DL7](https://stacks.math.columbia.edu/tag/0DL7) in the Stacks Project.

**`AlgebraicGeometry.Space.derivedPushoutEssentialImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/DerivedPushoutGlueingRepresentedAffine.lean, line 567](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/DerivedPushoutGlueingRepresentedAffine.lean#L567).

> **Stacks 0DL7.** Let `S` be a scheme and let
> ```
> X  --i-->  X'
> |          |
> f          f'
> v          v
> Y  --j-->  Y'
> ```
> be a pushout in the category of algebraic spaces over `S` as in Stacks 07VX, with `i` a
> thickening and `f` affine. Then the essential image of the functor
> `D(𝒪_{Y'}) ⥤ D(𝒪_Y) ×_{D(𝒪_X)} D(𝒪_{X'})`, `M' ↦ (Lj^* M', L(f')^* M', can)`, given by derived
> pullback, contains every triple `(M, K', α)` with `M ∈ D(𝒪_Y)` and `K' ∈ D(𝒪_{X'})`
> pseudo-coherent: for every isomorphism `α : Lf^* M ≅ Li^* K'` there are `M' ∈ D(𝒪_{Y'})` and
> isomorphisms `a : Lj^* M' ≅ M` and `b : L(f')^* M' ≅ K'` with `Li^* b` equal to `α ∘ Lf^* a`
> through the 2-cell `Lf^* Lj^* ≅ Li^* L(f')^*` (Stacks 0D6D). This holds at any models of the four
> derived categories; the statement is `AlgebraicGeometry.Space.DerivedPushoutEssentialImage`.
>
> The proof is the source's: the fibre `M'` of the glueing map
> `Rj_* M ⊕ Rf'_* K' ⟶ Rj_* Rf_* Li^* K'`
> (`AlgebraicGeometry.Space.derivedPushoutEssentialImage_of_derivedPushoutGlueingIsIso`), the
> isomorphism step checked on the affine étale charts of `Y'`
> (`AlgebraicGeometry.Space.derivedPushoutGlueingIsIso_of_onAffineChart`), where the base change
> of the square is a represented affine square whose rings form a fibre product along a surjection
> with nil kernel (`AlgebraicGeometry.Space.derivedPushoutEssentialImage_of_representedAffine`), and
> on which the step is the ring-level statement
> (`MilnorPatching.isIso_homEquiv_symm_of_isPullback_of_distinguished_glueingMap_derivedExtension`)
> carried to the algebraic spaces along the derived associated-module functors
> (`AlgebraicGeometry.Space.pushoutGlueingIsIsoStepOnRepresentedAffine`).

```lean
theorem derivedPushoutEssentialImage :
    DerivedPushoutEssentialImage.{w₁, w₂, w₃, w₄, u} B S hS
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 81.8, Tag 0DL6](https://stacks.math.columbia.edu/tag/0DL6)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
