---
declaration: section
origin: cited
lean: AlgebraicGeometry.relativeHomObjEquivOverBase, AlgebraicGeometry.relativeHom, AlgebraicGeometry.relativeHom_representableBy_affine, Stacks.Morphisms.relativeHom_representableBy_affineHom, Stacks.Morphisms.homFromFiniteLocallyFree_isRepresentable, Stacks.Morphisms.relativeHom_isRepresentable_of_locallyQuasiFinite
statement: formalized
proof: formalized
---

# 37.68 Relative morphisms

Section 37.68 of the Stacks Project, [Tag 0BL0](https://stacks.math.columbia.edu/tag/0BL0). 6 tags here are carried by 5 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BL1, an equation

[Tag 0BL1](https://stacks.math.columbia.edu/tag/0BL1) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.relativeHomObjEquivOverBase`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/RelativeMorphismFunctor.lean#L74), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/RelativeMorphismDiagram.lean, line 26](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/RelativeMorphismDiagram.lean#L26) (StacksFrontier): “the datum pictured by diagram (37.68.0.1), a morphism `b : T ×_S Z ⟶ T ×_S X` over `T`, identified with its description as a morphism `T ×_S Z ⟶ X` over `S`”.

## Tag 0BL2, an equation

[Tag 0BL2](https://stacks.math.columbia.edu/tag/0BL2) in the Stacks Project.

**`AlgebraicGeometry.relativeHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/RelativeMorphismFunctor.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/RelativeMorphismFunctor.lean#L50).

> The relative morphism functor `Mor_S(Z, X)` of two schemes `Z` and `X` over `S`: it sends a
> scheme `T` over `S` to the set of morphisms `T ×_S Z ⟶ X` over `S`, and a morphism `T' ⟶ T` over
> `S` to the operation of base change along it.

```lean
noncomputable def relativeHom (Z X : Over S) : (Over S)ᵒᵖ ⥤ Type u
```

## Tag 05Y6, a lemma

[Tag 05Y6](https://stacks.math.columbia.edu/tag/05Y6) in the Stacks Project.

**`AlgebraicGeometry.relativeHom_representableBy_affine`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/RelativeMorphisms.lean, line 416](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/RelativeMorphisms.lean#L416).

> **Stacks Project, Tag 05Y6.** If `Z` and `X` are affine schemes over an affine scheme `S`
> and `Γ(Z, 𝒪_Z)` is finite free over `Γ(S, 𝒪_S)`, then the relative morphism
> functor `Mor_S(Z, X)` is represented by an affine scheme over `S`.

```lean
lemma relativeHom_representableBy_affine
    (S Z X : Scheme.{u}) (f : Z ⟶ S) (g : X ⟶ S)
    [IsAffine S] [IsAffine Z] [IsAffine X]
    (hfinite : letI := f.appTop.hom.toAlgebra
      Module.Finite Γ(S, ⊤) Γ(Z, ⊤))
    (hfree : letI := f.appTop.hom.toAlgebra
      Module.Free Γ(S, ⊤) Γ(Z, ⊤)) :
    ∃ W : Over S, IsAffine W.left ∧
      Nonempty
        (((Limits.prod.functor.obj (Over.mk f)).op ⋙
          yoneda.obj (Over.mk g)).RepresentableBy W)
```

## Tag 0BL3, a lemma

[Tag 0BL3](https://stacks.math.columbia.edu/tag/0BL3) in the Stacks Project.

**`Stacks.Morphisms.relativeHom_representableBy_affineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteLocallyFree/AffineRepresentability.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteLocallyFree/AffineRepresentability.lean#L136).

> If `Z ⟶ S` is finite locally free and `X ⟶ S` is affine, then the relative morphism functor
> `Mor_S(Z, X)` is represented by a scheme affine over `S`.

```lean
theorem relativeHom_representableBy_affineHom {S Z X : Scheme.{u}} (f : Z ⟶ S) (g : X ⟶ S)
    [IsFiniteLocallyFree f] [IsAffineHom g] :
    ∃ W : Over S, IsAffineHom W.hom ∧
      Nonempty
        (((prod.functor.obj (Over.mk f)).op ⋙ yoneda.obj (Over.mk g)).RepresentableBy W)
```

## Tag 0BL4, a lemma

[Tag 0BL4](https://stacks.math.columbia.edu/tag/0BL4) in the Stacks Project.

**`Stacks.Morphisms.homFromFiniteLocallyFree_isRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteLocallyFree/Representability.lean, line 904](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteLocallyFree/Representability.lean#L904).

> **Stacks Project, Tag 0BL4.** If `Z` is finite locally free over `S` and every finite set of
> points in a fibre of `X` lies in an affine open of `X`, then the functor of `S`-morphisms from
> `Z` to `X` is representable.

```lean
theorem homFromFiniteLocallyFree_isRepresentable
    {S Z X : Scheme.{u}} (f : Z ⟶ S) (g : X ⟶ S)
    [IsFiniteLocallyFree f]
    (hX : ∀ (s : S) (t : Set X), t.Finite →
      (∀ x ∈ t, g.base x = s) →
      ∃ U : X.Opens, IsAffineOpen U ∧ t ⊆ U) :
    ((prod.functor.obj (Over.mk f)).op ⋙ yoneda.obj (Over.mk g)).IsRepresentable
```

## Tag 0BL5, a lemma

[Tag 0BL5](https://stacks.math.columbia.edu/tag/0BL5) in the Stacks Project.

**`Stacks.Morphisms.relativeHom_isRepresentable_of_locallyQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteLocallyFree/Representability.lean, line 921](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteLocallyFree/Representability.lean#L921).

> **Stacks Project, Tag 0BL5.** If `Z` is finite locally free over `S` and `X` is separated
> and quasi-finite over `S`, then the functor of `S`-morphisms from `Z` to `X` is representable.
>
> The hypothesis of Stacks Tag 0BL4 is supplied by Stacks Tag 07S0: a finite set of points of `X`
> in one fibre over `s : S` lies above an affine open `U ∋ s`, so it is a finite set of points of
> `g ⁻¹ᵁ U`, which is separated and quasi-finite over the affine scheme `U`.

```lean
theorem relativeHom_isRepresentable_of_locallyQuasiFinite
    {S Z X : Scheme.{u}} (f : Z ⟶ S) (g : X ⟶ S)
    [IsFiniteLocallyFree f] [IsSeparated g] [LocallyOfFiniteType g] [LocallyQuasiFinite g] :
    ((prod.functor.obj (Over.mk f)).op ⋙ yoneda.obj (Over.mk g)).IsRepresentable
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.68, Tag 0BL0](https://stacks.math.columbia.edu/tag/0BL0)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
