---
declaration: section
origin: cited
lean: AlgebraicGeometry.isoSpec_hom_base_apply_of_isAffine, RingedSpace.basicOpen, RingedSpace.mem_top_basicOpen, RingedSpace.isUnit_res_basicOpen, basicOpen_eq_of_affine, Scheme.toSpecΓ_preimage_basicOpen, AlgebraicGeometry.bijective_Γ_map_op_of_isAffine, AffineScheme.equivCommRingCat
statement: formalized
proof: formalized
---

# 26.6 The category of affine schemes

Section 26.6 of the Stacks Project, [Tag 01HX](https://stacks.math.columbia.edu/tag/01HX). 8 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 9 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01HY, a lemma

[Tag 01HY](https://stacks.math.columbia.edu/tag/01HY) in the Stacks Project.

**`AlgebraicGeometry.isoSpec_hom_base_apply_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Schemes/MorphismsToAffine.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Schemes/MorphismsToAffine.lean#L215).

> Let `X` be a locally ringed space, let `Y` be an affine scheme and let
> `f : X ⟶ Y` be a morphism of locally ringed spaces. Given `x : X`, consider the ring maps
>
>     Γ(Y, 𝒪_Y) --f^♯--> Γ(X, 𝒪_X) ⟶ 𝒪_{X,x}
>
> and let `p ⊆ Γ(Y, 𝒪_Y)` be the inverse image of the maximal ideal `m_x`. Let `y ∈ Y` be the
> corresponding point. Then `f x = y`.
>
> The point `y` of the affine scheme `Y` corresponding to a prime of `Γ(Y, 𝒪_Y)` is named by
> transporting along `AlgebraicGeometry.Scheme.isoSpec`, the identification of `Y` with
> `Spec Γ(Y, 𝒪_Y)`: the statement here is that `Y.isoSpec.hom` sends `f x` to `p`, and
> `AlgebraicGeometry.base_eq_isoSpec_inv_base_of_isAffine` is the same thing written as `f x = y`.
> The prime `p` is spelled as the inverse image along `f^♯` of the inverse image along
> `Γ(X, 𝒪_X) ⟶ 𝒪_{X,x}` of the maximal ideal, which is the inverse image along the composite.

```lean
theorem isoSpec_hom_base_apply_of_isAffine (X : LocallyRingedSpace.{u}) (Y : Scheme.{u})
    [IsAffine Y] (f : X ⟶ Y.toLocallyRingedSpace) (x : X) :
    Y.isoSpec.hom.base (f.base x) =
      PrimeSpectrum.comap (LocallyRingedSpace.Γ.map f.op).hom
        (PrimeSpectrum.comap (X.presheaf.Γgerm x).hom
          (IsLocalRing.closedPoint (X.presheaf.stalk x)))
```

## Tag 01HZ, a lemma

[Tag 01HZ](https://stacks.math.columbia.edu/tag/01HZ) in the Stacks Project.

Declarations registered for the tag:

- [`RingedSpace.basicOpen`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingedSpace.basicOpen#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L94) (StacksFrontier): “D(f), the locus where the germ of f is a unit, is open”.
- [`RingedSpace.mem_top_basicOpen`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingedSpace.mem_top_basicOpen#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L95) (StacksFrontier): “membership in D(f) for a global section”.
- [`RingedSpace.isUnit_res_basicOpen`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingedSpace.isUnit_res_basicOpen#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L96) (StacksFrontier): “f is invertible on D(f)”.

## Tag 01I0, a lemma

[Tag 01I0](https://stacks.math.columbia.edu/tag/01I0) in the Stacks Project.

Declarations registered for the tag:

- [`basicOpen_eq_of_affine`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=basicOpen_eq_of_affine#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L98) (StacksFrontier): “for X = Spec R”.
- [`Scheme.toSpecΓ_preimage_basicOpen`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Scheme.toSpecΓ_preimage_basicOpen#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L99) (StacksFrontier): “for X affine, through X ≅ Spec Γ(X)”.

## Tag 01I1, a lemma

[Tag 01I1](https://stacks.math.columbia.edu/tag/01I1) in the Stacks Project.

**`AlgebraicGeometry.bijective_Γ_map_op_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Schemes/MorphismsToAffine.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Schemes/MorphismsToAffine.lean#L146). References: EGA I (1.7.3), “more general”.

> Let `X` be a locally ringed space and let `Y` be an affine scheme. The map
>
>     Mor(X, Y) ⟶ Hom(Γ(Y, 𝒪_Y), Γ(X, 𝒪_X))
>
> sending a morphism to the ring map it induces on global sections is bijective.
>
> The target is read as a locally ringed space, which is where the morphisms of the source live.

```lean
theorem bijective_Γ_map_op_of_isAffine (X : LocallyRingedSpace.{u}) (Y : Scheme.{u}) [IsAffine Y] :
    Function.Bijective (fun f : X ⟶ Y.toLocallyRingedSpace =>
      LocallyRingedSpace.Γ.map f.op)
```

## Tag 01I2, a lemma

[Tag 01I2](https://stacks.math.columbia.edu/tag/01I2) in the Stacks Project.

Declarations registered for the tag:

- [`AffineScheme.equivCommRingCat`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AffineScheme.equivCommRingCat#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L101) (StacksFrontier): “the equivalence with the opposite of rings”.
- [`AffineScheme.ΓIsEquiv`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AffineScheme.ΓIsEquiv#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L102) (StacksFrontier): “it is given by global sections”.

## Tag 01I3, a lemma

[Tag 01I3](https://stacks.math.columbia.edu/tag/01I3) in the Stacks Project.

Declarations registered for the tag:

- [`IsAffineOpen.basicOpen`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsAffineOpen.basicOpen#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L104) (StacksFrontier).

## Tag 01I4, a lemma

[Tag 01I4](https://stacks.math.columbia.edu/tag/01I4) in the Stacks Project.

**`AlgebraicGeometry.AffineScheme.preservesLimits_forgetToLocallyRingedSpace`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Affine/FibreProductsLocallyRingedSpaces.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Affine/FibreProductsLocallyRingedSpaces.lean#L55). The attribute's comment: “limits agree with those of locally ringed spaces”.

> The forgetful functor from affine schemes to locally ringed spaces preserves all limits:
> limits of affine schemes, in particular products and fibre products, are the same as those
> computed in locally ringed spaces.

```lean
instance preservesLimits_forgetToLocallyRingedSpace :
    PreservesLimits (forgetToScheme.{u} ⋙ Scheme.forgetToLocallyRingedSpace)
```

**`AlgebraicGeometry.LocallyRingedSpace.prodSpecIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Affine/FibreProductsLocallyRingedSpaces.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Affine/FibreProductsLocallyRingedSpaces.lean#L96). The attribute's comment: “products in locally ringed spaces”.

> In the category of locally ringed spaces, `Spec R × Spec S ≅ Spec (R ⊗[ℤ] S)`.

```lean
noncomputable def prodSpecIso :
    Spec.locallyRingedSpaceObj (.of R) ⨯ Spec.locallyRingedSpaceObj (.of S) ≅
      Spec.locallyRingedSpaceObj (.of (R ⊗[ℤ] S))
```

**`AlgebraicGeometry.LocallyRingedSpace.pullbackSpecIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Affine/FibreProductsLocallyRingedSpaces.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Affine/FibreProductsLocallyRingedSpaces.lean#L142). The attribute's comment: “fibre products in locally ringed spaces”.

> In the category of locally ringed spaces, `Spec A ×_{Spec R} Spec B ≅ Spec (A ⊗[R] B)`.

```lean
noncomputable def pullbackSpecIso :
    pullback (Spec.locallyRingedSpaceMap (ofHom (algebraMap R A)))
      (Spec.locallyRingedSpaceMap (ofHom (algebraMap R B))) ≅
      Spec.locallyRingedSpaceObj (.of (A ⊗[R] B))
```

Declarations registered for the tag:

- [`AlgebraicGeometry.AffineScheme.hasLimits`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.AffineScheme.hasLimits#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/Affine/FibreProductsLocallyRingedSpaces.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Affine/FibreProductsLocallyRingedSpaces.lean#L44) (StacksFrontier): “finite products and fibre products exist”.

## Tag 01I5, a lemma

[Tag 01I5](https://stacks.math.columbia.edu/tag/01I5) in the Stacks Project.

**`Stacks.ZariskiAndSeparation.AffineDisjointUnion.isAffine_of_sup_eq_top_of_disjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/AffineDisjointUnion.lean, line 39](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/AffineDisjointUnion.lean#L39). The attribute's comment: “for a scheme; a locally ringed space with an affine open cover is one”.

> **A scheme covered by two disjoint affine opens is affine.**

```lean
theorem isAffine_of_sup_eq_top_of_disjoint {X : Scheme.{u}} (U V : X.Opens)
    (hUV : U ⊔ V = ⊤) (hd : Disjoint U V) (hU : IsAffineOpen U) (hV : IsAffineOpen V) :
    IsAffine X
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 26.6, Tag 01HX](https://stacks.math.columbia.edu/tag/01HX)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
