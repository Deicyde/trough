---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.isAbsolutelyQuasiSeparated_reduction_tfae, AlgebraicGeometry.FormalSpace.isAbsolutelyQuasiSeparated_reduction_tfae_representable, AlgebraicGeometry.FormalSpace.isAbsolutelySeparated_reduction_of_hasAffineIntersectionsULift, AlgebraicGeometry.FormalSpace.isAbsolutelySeparated_reduction_iff_hasAffineIntersectionsULift, AlgebraicGeometry.FormalSpace.exists_isReduction_and_isAbsolutelySeparated_iff_hasAffineIntersectionsULift, AlgebraicGeometry.FormalSpace.isAbsolutelySeparated_reduction_iff_hasRepresentableAffineIntersectionsULift, AlgebraicGeometry.FormalSpace.exists_isReduction_and_isAbsolutelySeparated_iff_hasRepresentableAffineIntersectionsULift, AlgebraicGeometry.FormalSpace.IsSeparated
statement: formalized
proof: formalized
---

# 87.16 Separation axioms for formal algebraic spaces

Section 87.16 of the Stacks Project, [Tag 0AJ4](https://stacks.math.columbia.edu/tag/0AJ4). 5 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AJ5, a lemma

[Tag 0AJ5](https://stacks.math.columbia.edu/tag/0AJ5) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isAbsolutelyQuasiSeparated_reduction_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionQuasiSeparated.lean, line 281](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionQuasiSeparated.lean#L281). The attribute's comment: “the reduction of X is a given, in the sense of AlgebraicGeometry.FormalSpace.IsReduction and supplied by Stacks 0AIN, and is presented by a presheaf of Type u together with an isomorphism from its universe lift, since an algebraic space over S is a presheaf of Type u while a formal algebraic space is a sheaf of Type (u + 1); clauses (2) and (3) quantify over the objects of the site representing the fibre product, as the carriers of Stacks 0AHR do for the identical clauses, rather than asserting that it is representable, which is Stacks 0AIP”.

> **Stacks 0AJ5.** Let `X` be a formal algebraic space over `S` and let `i : X_red ⟶ X` be a
> reduction of `X`, presented by a presheaf `Xred` of `Type u` together with an isomorphism from
> its universe lift. The following are equivalent: `Xred` is a quasi-separated algebraic space;
> for every pair of objects of the big fppf site of `S` with quasi-compact underlying scheme and
> every pair of morphisms from their universe-lifted Yoneda presheaves into `X`, every object of
> the site representing the fibre product has quasi-compact underlying scheme; and the same for
> every pair of objects with affine underlying scheme.
>
> Condition (1) is equivalent to the intersection condition for `Xred`, with quasi-compact or
> with affine test objects, by Stacks 0AHR. The intersection condition for `X` implies the one
> for `Xred` because the inclusion of a reduction is a monomorphism, and conversely it follows
> from the one for `Xred` by the thickening comparison of
> `AlgebraicGeometry.FormalSpace.hasQuasiCompactIntersectionsULift_of_isReduction`.

```lean
theorem isAbsolutelyQuasiSeparated_reduction_tfae
    {X Xr : FppfSheaf B S hS} (_hX : IsFormalAlgebraicSpace B S hS X)
    {i : Xr ⟶ X} (hi : IsReduction B S hS X Xr i)
    {Xred : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (e : Xred ⋙ uliftFunctor.{u + 1} ≅ Xr.obj) :
    List.TFAE
      [ Space.IsAbsolutelyQuasiSeparated B S hS hZ Xred,
        HasQuasiCompactIntersectionsULift B S hS
          (fun Z : Scheme.{u} ↦ CompactSpace (Z : Type u)) X.obj,
        HasQuasiCompactIntersectionsULift B S hS (fun Z : Scheme.{u} ↦ IsAffine Z) X.obj ]
```

**`AlgebraicGeometry.FormalSpace.isAbsolutelyQuasiSeparated_reduction_tfae_representable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxiomsRepresentable.lean, line 255](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxiomsRepresentable.lean#L255). The attribute's comment: “with clauses (2) and (3) in the source's own form, asserting that the fibre product U ×\_X V is representable by an object of the site with quasi-compact underlying scheme; read against a reduction of X, in the sense of AlgebraicGeometry.FormalSpace.IsReduction and supplied by Stacks 0AIN, presented by a presheaf of Type u together with an isomorphism from its universe lift”.

> **Stacks 0AJ5, with clauses (2) and (3) asserting representability.** Let `X` be a formal
> algebraic space over `S` and let `i : X_red ⟶ X` be a reduction of `X`, presented by a presheaf
> `Xred` of `Type u` together with an isomorphism from its universe lift. The following are
> equivalent: `Xred` is a quasi-separated algebraic space; for every pair of objects of the big
> fppf site of `S` with quasi-compact underlying scheme and every pair of morphisms from their
> universe-lifted Yoneda presheaves into `X`, the fibre product is represented by an object of
> the site with quasi-compact underlying scheme; and the same for every pair of objects with
> affine underlying scheme.
>
> This is `AlgebraicGeometry.FormalSpace.isAbsolutelyQuasiSeparated_reduction_tfae` together with
> `AlgebraicGeometry.FormalSpace.hasRepresentableQuasiCompactIntersectionsULift_iff`.

```lean
theorem isAbsolutelyQuasiSeparated_reduction_tfae_representable
    {X Xr : FppfSheaf B S hS} (hX : IsFormalAlgebraicSpace B S hS X)
    {i : Xr ⟶ X} (hi : IsReduction B S hS X Xr i)
    {Xred : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (e : Xred ⋙ uliftFunctor.{u + 1} ≅ Xr.obj) :
    List.TFAE
      [ Space.IsAbsolutelyQuasiSeparated B S hS hZ Xred,
        HasRepresentableQuasiCompactIntersectionsULift B S hS
          (fun Z : Scheme.{u} ↦ CompactSpace (Z : Type u)) X.obj,
        HasRepresentableQuasiCompactIntersectionsULift B S hS
          (fun Z : Scheme.{u} ↦ IsAffine Z) X.obj ]
```

## Tag 0AJ6, a lemma

[Tag 0AJ6](https://stacks.math.columbia.edu/tag/0AJ6) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isAbsolutelySeparated_reduction_of_hasAffineIntersectionsULift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionSeparated.lean, line 255](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionSeparated.lean#L255). The attribute's comment: “(2) implies (1): the affine-intersection and surjectivity condition for X gives that the reduction of X is a separated algebraic space. The reduction is a given, in the sense of AlgebraicGeometry.FormalSpace.IsReduction and supplied by Stacks 0AIN, and is presented by a presheaf of Type u together with an isomorphism from its universe lift, since an algebraic space over S is a presheaf of Type u while a formal algebraic space is a sheaf of Type (u + 1). Clause (2) quantifies over the objects of the site representing the fibre product, as the carrier of Stacks 0AHS does for the identical clause, rather than asserting that it is representable, which is Stacks 0AIP. The converse implication (1) implies (2), the equivalence read against an arbitrary reduction, and the tag itself, whose reduction is produced from Stacks 0AIN, are AlgebraicGeometry.FormalSpace.hasAffineIntersectionsULift\_of\_isReduction, AlgebraicGeometry.FormalSpace.isAbsolutelySeparated\_reduction\_iff\_hasAffineIntersectionsULift and AlgebraicGeometry.FormalSpace.exists\_isReduction\_and\_isAbsolutelySeparated\_iff\_hasAffineIntersectionsULift in StacksFrontier.AlgebraicGeometry.FormalSpace.ReductionSeparatedConverse”. References: EGA I (10.15.7), “partial”.

> **Stacks 0AJ6, the implication (2) ⟹ (1).** Let `X` be a formal algebraic space over `S`
> and let `i : X_red ⟶ X` be a reduction of `X`, presented by a presheaf `Xred` of `Type u`
> together with an isomorphism from its universe lift. If for every pair of objects of the big
> fppf site of `S` with affine underlying scheme and every pair of morphisms from their
> universe-lifted Yoneda presheaves into `X` every object of the site representing the fibre
> product has affine underlying scheme and the canonical map from the tensor product over `ℤ` of
> the two rings of global sections to its ring of global sections is surjective, then `Xred` is a
> separated algebraic space.
>
> The inclusion of a reduction is a monomorphism, so a cartesian square exhibiting a fibre
> product over `Xred` also exhibits it over `X`; the condition therefore restricts from `X` to
> `Xred`, where it is separatedness by Stacks 0AHS.

```lean
theorem isAbsolutelySeparated_reduction_of_hasAffineIntersectionsULift
    {X Xr : FppfSheaf B S hS} (_hX : IsFormalAlgebraicSpace B S hS X)
    {i : Xr ⟶ X} (hi : IsReduction B S hS X Xr i)
    {Xred : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (e : Xred ⋙ uliftFunctor.{u + 1} ≅ Xr.obj)
    (h : HasAffineIntersectionsULift B S hS X.obj) :
    Space.IsAbsolutelySeparated B S hS hZ Xred
```

**`AlgebraicGeometry.FormalSpace.isAbsolutelySeparated_reduction_iff_hasAffineIntersectionsULift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionSeparatedConverse.lean, line 415](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionSeparatedConverse.lean#L415). The attribute's comment: “both implications, read against a reduction of X, in the sense of AlgebraicGeometry.FormalSpace.IsReduction, and a presentation of it by a presheaf of Type u together with an isomorphism from its universe lift -- an algebraic space over S being a presheaf of Type u while a formal algebraic space is a sheaf of Type (u + 1). Clause (2) quantifies over the objects of the site representing the fibre product, as the carrier of Stacks 0AHS does for the identical clause, rather than asserting that it is representable, which is Stacks 0AIP. The tag itself, which produces the reduction and its presentation, is AlgebraicGeometry.FormalSpace.exists\_isReduction\_and\_isAbsolutelySeparated\_iff\_hasAffineIntersectionsULift”. References: EGA I (10.15.7), “more general”.

> **Stacks 0AJ6.** Let `X` be a formal algebraic space over `S` and let `i : X_red ⟶ X` be a
> reduction of `X`, presented by a presheaf `Xred` of `Type u` together with an isomorphism from
> its universe lift. Then `Xred` is a separated algebraic space if and only if for every pair of
> objects of the big fppf site of `S` with affine underlying scheme and every pair of morphisms
> from their universe-lifted Yoneda presheaves into `X` every object of the site representing the
> fibre product has affine underlying scheme and the canonical map from the tensor product over
> `ℤ` of the two rings of global sections to its ring of global sections is surjective.
>
> The implication from the condition to separatedness is
> `AlgebraicGeometry.FormalSpace.isAbsolutelySeparated_reduction_of_hasAffineIntersectionsULift`:
> the inclusion of a reduction is a monomorphism, so the condition restricts from `X` to the
> reduction, where it is separatedness by Stacks 0AHS. The converse is
> `AlgebraicGeometry.FormalSpace.hasAffineIntersectionsULift_of_isReduction`, the argument of the
> source through the thickening comparison of the two fibre products.

```lean
theorem isAbsolutelySeparated_reduction_iff_hasAffineIntersectionsULift
    {X Xr : FppfSheaf B S hS} (hX : IsFormalAlgebraicSpace B S hS X)
    {i : Xr ⟶ X} (hi : IsReduction B S hS X Xr i)
    {Xred : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (e : Xred ⋙ uliftFunctor.{u + 1} ≅ Xr.obj) :
    Space.IsAbsolutelySeparated B S hS hZ Xred ↔
      HasAffineIntersectionsULift B S hS X.obj
```

**`AlgebraicGeometry.FormalSpace.exists_isReduction_and_isAbsolutelySeparated_iff_hasAffineIntersectionsULift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionSeparatedConverse.lean, line 454](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionSeparatedConverse.lean#L454). References: EGA I (10.15.7), “more general”.

> **Stacks 0AJ6.** Let `S` be a scheme contained in a big fppf site `B` and let `X` be a
> formal algebraic space over `S`. The reduction of `X` exists — a reduced algebraic space
> `X_red` and a representable thickening `i : X_red ⟶ X` through which every morphism to `X`
> from a reduced algebraic space factors uniquely — it is presented by a presheaf `Xred` of
> `Type u` together with an isomorphism from its universe lift, and the following are
> equivalent:
>
> 1. `Xred` is a separated algebraic space;
> 2. for every pair of objects of the big fppf site of `S` with affine underlying scheme and
>    every pair of morphisms from their universe-lifted Yoneda presheaves into `X`, every
>    object of the site representing the fibre product has affine underlying scheme and the
>    canonical map from the tensor product over `ℤ` of the two rings of global sections to its
>    ring of global sections is surjective.
>
> The reduction comes from Stacks 0AIN,
> `AlgebraicGeometry.FormalSpace.exists_isReduction_of_isFormalAlgebraicSpace`; its presentation
> by a presheaf of `Type u` from the pointwise `u`-smallness of an algebraic space,
> `AlgebraicGeometry.Space.exists_comp_uliftFunctor_iso_of_isAlgebraicSpaceULift`; and the
> equivalence from
> `AlgebraicGeometry.FormalSpace.isAbsolutelySeparated_reduction_iff_hasAffineIntersectionsULift`,
> which reads it against any reduction and any presentation of it.

```lean
theorem exists_isReduction_and_isAbsolutelySeparated_iff_hasAffineIntersectionsULift
    (X : FppfSheaf B S hS) (hX : IsFormalAlgebraicSpace B S hS X) :
    ∃ (Xr : FppfSheaf B S hS) (i : Xr ⟶ X) (Xred : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
      (_ : Xred ⋙ uliftFunctor.{u + 1} ≅ Xr.obj),
      IsReduction B S hS X Xr i ∧
        (Space.IsAbsolutelySeparated B S hS hZ Xred ↔
          HasAffineIntersectionsULift B S hS X.obj)
```

**`AlgebraicGeometry.FormalSpace.isAbsolutelySeparated_reduction_iff_hasRepresentableAffineIntersectionsULift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionSeparatedRepresentable.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionSeparatedRepresentable.lean#L177). The attribute's comment: “both implications, with clause (2) in the source's own form, which asserts that the fibre product U ×\_X V is representable by an object of the site and that its underlying scheme is affine, rather than quantifying over the objects of the site representing it. The two readings agree on a formal algebraic space, by AlgebraicGeometry.FormalSpace.hasRepresentableAffineIntersectionsULift\_iff, whose nontrivial direction is the representability assertion of Stacks 0AIP for an arbitrary formal algebraic space. Read against a reduction of X, in the sense of AlgebraicGeometry.FormalSpace.IsReduction, and a presentation of it by a presheaf of Type u together with an isomorphism from its universe lift -- an algebraic space over S being a presheaf of Type u while a formal algebraic space is a sheaf of Type (u + 1). The tag with the reduction and its presentation produced is AlgebraicGeometry.FormalSpace.exists\_isReduction\_and\_isAbsolutelySeparated\_iff\_hasRepresentableAffineIntersectionsULift”. References: EGA I (10.15.7), “more general”.

> **Stacks 0AJ6, with clause (2) asserting representability.** Let `X` be a formal algebraic
> space over `S` and let `i : X_red ⟶ X` be a reduction of `X`, presented by a presheaf `Xred` of
> `Type u` together with an isomorphism from its universe lift. Then `Xred` is a separated
> algebraic space if and only if for every pair of objects of the big fppf site of `S` with affine
> underlying scheme and every pair of morphisms from their universe-lifted Yoneda presheaves into
> `X` the fibre product is represented by an object of the site with affine underlying scheme and
> the canonical map from the tensor product over `ℤ` of the two rings of global sections to its
> ring of global sections is surjective.
>
> This is `…isAbsolutelySeparated_reduction_iff_hasAffineIntersectionsULift` composed with
> `…hasRepresentableAffineIntersectionsULift_iff`, which identifies clause (2) in the source's
> form with the form that quantifies over the representing objects.

```lean
theorem isAbsolutelySeparated_reduction_iff_hasRepresentableAffineIntersectionsULift
    {X Xr : FppfSheaf B S hS} (hX : IsFormalAlgebraicSpace B S hS X)
    {i : Xr ⟶ X} (hi : IsReduction B S hS X Xr i)
    {Xred : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (e : Xred ⋙ uliftFunctor.{u + 1} ≅ Xr.obj) :
    Space.IsAbsolutelySeparated B S hS hZ Xred ↔
      HasRepresentableAffineIntersectionsULift B S hS X.obj
```

**`AlgebraicGeometry.FormalSpace.exists_isReduction_and_isAbsolutelySeparated_iff_hasRepresentableAffineIntersectionsULift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionSeparatedRepresentable.lean, line 213](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionSeparatedRepresentable.lean#L213). The attribute's comment: “the reduction and its presentation by a presheaf of Type u produced, from Stacks 0AIN for an arbitrary formal algebraic space and from the pointwise u-smallness of an algebraic space, with clause (2) in the source's own form, which asserts that the fibre product U ×\_X V is representable by an object of the site and that its underlying scheme is affine. The variant whose clause (2) quantifies over the objects of the site representing the fibre product instead is AlgebraicGeometry.FormalSpace.exists\_isReduction\_and\_isAbsolutelySeparated\_iff\_hasAffineIntersectionsULift in StacksFrontier.AlgebraicGeometry.FormalSpace.ReductionSeparatedConverse”. References: EGA I (10.15.7), “more general”.

> **Stacks 0AJ6, with clause (2) asserting representability.** Let `S` be a scheme contained
> in a big fppf site `B` and let `X` be a formal algebraic space over `S`. The reduction of `X`
> exists — a reduced algebraic space `X_red` and a representable thickening `i : X_red ⟶ X`
> through which every morphism to `X` from a reduced algebraic space factors uniquely — it is
> presented by a presheaf `Xred` of `Type u` together with an isomorphism from its universe lift,
> and the following are equivalent:
>
> 1. `Xred` is a separated algebraic space;
> 2. for every pair of objects of the big fppf site of `S` with affine underlying scheme and
>    every pair of morphisms from their universe-lifted Yoneda presheaves into `X`, the fibre
>    product is represented by an object of the site with affine underlying scheme and the
>    canonical map from the tensor product over `ℤ` of the two rings of global sections to its
>    ring of global sections is surjective.
>
> Clause (2) is here the source's own, asserting that `U ×_X V` is a scheme. The reduction comes
> from Stacks 0AIN for an arbitrary formal algebraic space,
> `AlgebraicGeometry.FormalSpace.exists_isReduction_of_isFormalAlgebraicSpace`.

```lean
theorem exists_isReduction_and_isAbsolutelySeparated_iff_hasRepresentableAffineIntersectionsULift
    (X : FppfSheaf B S hS) (hX : IsFormalAlgebraicSpace B S hS X) :
    ∃ (Xr : FppfSheaf B S hS) (i : Xr ⟶ X) (Xred : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
      (_ : Xred ⋙ uliftFunctor.{u + 1} ≅ Xr.obj),
      IsReduction B S hS X Xr i ∧
        (Space.IsAbsolutelySeparated B S hS hZ Xred ↔
          HasRepresentableAffineIntersectionsULift B S hS X.obj)
```

## Tag 0AJ7, a definition

[Tag 0AJ7](https://stacks.math.columbia.edu/tag/0AJ7) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsSeparated`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffineFibreProduct.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/AffineFibreProduct.lean#L138). The attribute's comment: “clause (2): separated, in the form of clause (2) of Stacks 0AJ6”.

> An fppf sheaf `X` on the big fppf site of `S` is *separated* when, for every pair of morphisms
> to `X` from sheaves represented by affine schemes over `S`, every object of the site representing
> their fibre product is affine and the canonical map from the tensor product over `ℤ` of the two
> coordinate rings to its coordinate ring is surjective.
>
> The condition quantifies over the objects of the site representing the fibre product, so on an
> fppf sheaf whose fibre products are not representable it holds vacuously. On a formal algebraic
> space it agrees with `AlgebraicGeometry.FormalSpace.IsSeparatedFormalAlgebraicSpace`, by
> `AlgebraicGeometry.FormalSpace.isSeparatedFormalAlgebraicSpace_iff_isSeparated`.

```lean
abbrev IsSeparated (X : FppfSheaf B S hS) : Prop
```

**`AlgebraicGeometry.FormalSpace.IsQuasiSeparated`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxioms.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxioms.lean#L88). The attribute's comment: “clause (1): quasi-separated, in the form of clause (3) of Stacks 0AJ5, whose equivalence with clause (2) of Stacks 0AJ5 and with quasi-separatedness of the reduction is not proved in this library”.

> An fppf sheaf `X` on the big fppf site of `S` is *quasi-separated* when, for every pair of
> morphisms to `X` from sheaves represented by affine schemes over `S`, every object of the site
> representing their fibre product has quasi-compact underlying scheme.

```lean
abbrev IsQuasiSeparated (X : FppfSheaf B S hS) : Prop
```

**`AlgebraicGeometry.FormalSpace.IsAffineFormalAlgebraicSpace.isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxioms.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxioms.lean#L109). The attribute's comment: “clause (2): an affine formal algebraic space is separated, in the form of clause (2) of Stacks 0AJ6, whose equivalence with clause (1) is not proved in this library”.

> Every affine formal algebraic space over `S` is separated, in the form of clause (2) of
> Stacks 0AJ6.

```lean
theorem IsAffineFormalAlgebraicSpace.isSeparated {X : FppfSheaf B S hS}
    (hX : IsAffineFormalAlgebraicSpace B S hS X) : IsSeparated B S hS X
```

**`AlgebraicGeometry.FormalSpace.isQuasiSeparated_of_isAffineFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxioms.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxioms.lean#L210). The attribute's comment: “clause (1): an affine formal algebraic space is quasi-separated, in the form of clause (3) of Stacks 0AJ5”.

> Every affine formal algebraic space over `S` is quasi-separated, in the form of clause (3)
> of Stacks 0AJ5.

```lean
theorem isQuasiSeparated_of_isAffineFormalAlgebraicSpace {X : FppfSheaf B S hS}
    (hX : IsAffineFormalAlgebraicSpace B S hS X) :
    IsQuasiSeparated B S hS X
```

**`AlgebraicGeometry.FormalSpace.IsQuasiSeparatedFormalAlgebraicSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxiomsRepresentable.lean, line 290](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxiomsRepresentable.lean#L290). The attribute's comment: “clause (1): a formal algebraic space is quasi-separated when the conditions of Stacks 0AJ5 hold, recorded as clause (3) of Stacks 0AJ5 with the fibre product asserted to be a scheme; equivalent to every condition of Stacks 0AJ5 by isQuasiSeparatedFormalAlgebraicSpace\_tfae”.

> **Stacks 0AJ7, clause (1): quasi-separated formal algebraic spaces.** A formal algebraic
> space `X` over `S` is *quasi-separated* when the equivalent conditions of Stacks 0AJ5 hold.
> The condition recorded is clause (3) of Stacks 0AJ5: for every pair of objects `U`, `V` of the
> big fppf site of `S` with affine underlying scheme and every pair of morphisms `U ⟶ X`,
> `V ⟶ X` (morphisms `h_U ⟶ X`, `h_V ⟶ X` of presheaves out of the universe-lifted Yoneda
> presheaves), the fibre product `U ×_X V` is a scheme — represented by an object of the site
> with a cartesian square over the two morphisms — and that scheme is quasi-compact.
>
> The fibre product is the genuine one, and it is always representable, by Stacks 0AIP; so the
> condition is never vacuous. Its equivalence with the other conditions of Stacks 0AJ5 —
> quasi-separatedness of the reduction of `X`, and clause (2) with quasi-compact test objects —
> is `AlgebraicGeometry.FormalSpace.isQuasiSeparatedFormalAlgebraicSpace_tfae`. On a formal
> algebraic space it agrees with `AlgebraicGeometry.FormalSpace.IsQuasiSeparated`, by
> `AlgebraicGeometry.FormalSpace.isQuasiSeparatedFormalAlgebraicSpace_iff_isQuasiSeparated`.

```lean
def IsQuasiSeparatedFormalAlgebraicSpace (X : FppfSheaf B S hS) : Prop
```

**`AlgebraicGeometry.FormalSpace.IsSeparatedFormalAlgebraicSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxiomsRepresentable.lean, line 311](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxiomsRepresentable.lean#L311). The attribute's comment: “clause (2): a formal algebraic space is separated when the conditions of Stacks 0AJ6 hold, recorded as clause (2) of Stacks 0AJ6 with the fibre product asserted to be a scheme; equivalent to clause (1) of Stacks 0AJ6 by isSeparatedFormalAlgebraicSpace\_tfae”.

> **Stacks 0AJ7, clause (2): separated formal algebraic spaces.** A formal algebraic space
> `X` over `S` is *separated* when the equivalent conditions of Stacks 0AJ6 hold. The condition
> recorded is clause (2) of Stacks 0AJ6: for every pair of objects `U`, `V` of the big fppf site
> of `S` with affine underlying scheme and every pair of morphisms `U ⟶ X`, `V ⟶ X` (morphisms
> `h_U ⟶ X`, `h_V ⟶ X` of presheaves out of the universe-lifted Yoneda presheaves), the fibre
> product `U ×_X V` is a scheme — represented by an object of the site with a cartesian square
> over the two morphisms — that scheme is affine, and the canonical map
> `𝒪(U) ⊗_ℤ 𝒪(V) ⟶ 𝒪(U ×_X V)` is surjective.
>
> The fibre product is the genuine one, and it is always representable, by Stacks 0AIP; so the
> condition is never vacuous. Its equivalence with clause (1) of Stacks 0AJ6, separatedness of
> the reduction of `X`, is `AlgebraicGeometry.FormalSpace.isSeparatedFormalAlgebraicSpace_tfae`.
> On a formal algebraic space it agrees with `AlgebraicGeometry.FormalSpace.IsSeparated`, by
> `AlgebraicGeometry.FormalSpace.isSeparatedFormalAlgebraicSpace_iff_isSeparated`.

```lean
def IsSeparatedFormalAlgebraicSpace (X : FppfSheaf B S hS) : Prop
```

**`AlgebraicGeometry.FormalSpace.isQuasiSeparatedFormalAlgebraicSpace_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxiomsRepresentable.lean, line 356](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxiomsRepresentable.lean#L356). The attribute's comment: “clause (1): the definition is equivalent to each of the conditions of Stacks 0AJ5, read against a reduction of X presented by a presheaf of Type u, which exists by Stacks 0AIN”.

> **Stacks 0AJ7, clause (1), is the class of the conditions of Stacks 0AJ5.** Let `X` be a
> formal algebraic space over `S` and let `i : X_red ⟶ X` be a reduction of `X`, presented by a
> presheaf `Xred` of `Type u` together with an isomorphism from its universe lift. The following
> are equivalent: `X` is quasi-separated in the sense of Stacks 0AJ7; `Xred` is a quasi-separated
> algebraic space (clause (1) of Stacks 0AJ5); for every pair of quasi-compact test objects over
> `X` the fibre product is a quasi-compact scheme (clause (2)); and the same for every pair of
> affine test objects (clause (3)).

```lean
theorem isQuasiSeparatedFormalAlgebraicSpace_tfae
    {X Xr : FppfSheaf B S hS} (hX : IsFormalAlgebraicSpace B S hS X)
    {i : Xr ⟶ X} (hi : IsReduction B S hS X Xr i)
    {Xred : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (e : Xred ⋙ uliftFunctor.{u + 1} ≅ Xr.obj) :
    List.TFAE
      [ IsQuasiSeparatedFormalAlgebraicSpace B S hS X,
        Space.IsAbsolutelyQuasiSeparated B S hS hZ Xred,
        HasRepresentableQuasiCompactIntersectionsULift B S hS
          (fun Z : Scheme.{u} ↦ CompactSpace (Z : Type u)) X.obj,
        HasRepresentableQuasiCompactIntersectionsULift B S hS
          (fun Z : Scheme.{u} ↦ IsAffine Z) X.obj ]
```

**`AlgebraicGeometry.FormalSpace.isSeparatedFormalAlgebraicSpace_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxiomsRepresentable.lean, line 381](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxiomsRepresentable.lean#L381). The attribute's comment: “clause (2): the definition is equivalent to clause (1) of Stacks 0AJ6, read against a reduction of X presented by a presheaf of Type u, which exists by Stacks 0AIN”.

> **Stacks 0AJ7, clause (2), is the class of the conditions of Stacks 0AJ6.** Let `X` be a
> formal algebraic space over `S` and let `i : X_red ⟶ X` be a reduction of `X`, presented by a
> presheaf `Xred` of `Type u` together with an isomorphism from its universe lift. Then `X` is
> separated in the sense of Stacks 0AJ7 if and only if `Xred` is a separated algebraic space
> (clause (1) of Stacks 0AJ6).

```lean
theorem isSeparatedFormalAlgebraicSpace_tfae
    {X Xr : FppfSheaf B S hS} (hX : IsFormalAlgebraicSpace B S hS X)
    {i : Xr ⟶ X} (hi : IsReduction B S hS X Xr i)
    {Xred : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (e : Xred ⋙ uliftFunctor.{u + 1} ≅ Xr.obj) :
    IsSeparatedFormalAlgebraicSpace B S hS X ↔ Space.IsAbsolutelySeparated B S hS hZ Xred
```

## Tag 0AN3, a lemma

[Tag 0AN3](https://stacks.math.columbia.edu/tag/0AN3) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.pullback_isAffine_hasSomeSurjectivePresentation_completedTensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletedTensorProductFibreProductSupplement.lean, line 824](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletedTensorProductFibreProductSupplement.lean#L824). The attribute's comment: “all three clauses: over a separated formal algebraic space, the fibre product of affine formal algebraic spaces is affine, that of McQuillan ones is McQuillan, and over a McQuillan base it corresponds to the completed tensor product of the three weakly admissible topological rings, compatibly with both projections”.

> **Stacks 0AN3.** Let `X ⟶ Z` and `Y ⟶ Z` be morphisms of fppf sheaves on the big fppf site
> of `S` with `Z` a separated formal algebraic space.
>
> 1. If `X` and `Y` are affine formal algebraic spaces, then so is `X ×_Z Y`.
> 2. If `X` and `Y` are McQuillan affine formal algebraic spaces, then so is `X ×_Z Y`.
> 3. If `X`, `Y` and `Z` are McQuillan affine formal algebraic spaces corresponding to the weakly
>   admissible topological rings `A`, `B` and `C` over `S`, then the two morphisms are induced by
>   continuous ring maps `C → A` and `C → B` over `S`, and `X ×_Z Y` corresponds to the completed
>   tensor product `A ⊗̂_C B`, compatibly with both projections and with the canonical maps of `A`
>   and `B` into the completed tensor product.
>
> McQuillanness is `AlgebraicGeometry.FormalSpace.HasSomeSurjectivePresentation`, the predicate
> **Stacks 0AID** names McQuillan in this library. The source's hypothesis that `X` and `Y` are
> formal algebraic spaces is not needed: in each clause they are affine formal algebraic spaces.

```lean
theorem pullback_isAffine_hasSomeSurjectivePresentation_completedTensorProduct
    {X Y Z : FppfSheaf 𝔅 S hS} (f : X ⟶ Z) (g : Y ⟶ Z)
    (hZ : IsFormalAlgebraicSpace 𝔅 S hS Z) (hZsep : IsSeparated 𝔅 S hS Z) :
    (IsAffineFormalAlgebraicSpace 𝔅 S hS X → IsAffineFormalAlgebraicSpace 𝔅 S hS Y →
        IsAffineFormalAlgebraicSpace 𝔅 S hS (pullback f g)) ∧
      (HasSomeSurjectivePresentation 𝔅 S hS X → HasSomeSurjectivePresentation 𝔅 S hS Y →
        HasSomeSurjectivePresentation 𝔅 S hS (pullback f g)) ∧
      (HasSomeSurjectivePresentation 𝔅 S hS X → HasSomeSurjectivePresentation 𝔅 S hS Y →
        HasSomeSurjectivePresentation 𝔅 S hS Z →
        ∀ {A B C : Type u}
          [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
          [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
          [CommRing C] [TopologicalSpace C] [IsTopologicalRing C] [IsLinearTopology C C]
          (hA : TopologicalRing.IsWeaklyAdmissible A)
          (hB : TopologicalRing.IsWeaklyAdmissible B)
          (hC : TopologicalRing.IsWeaklyAdmissible C)
          (DA : QuotientSystem 𝔅 S hS A) (DB : QuotientSystem 𝔅 S hS B)
          (DC : QuotientSystem 𝔅 S hS C)
          (eX : X ≅ formalSpectrum DA) (eY : Y ≅ formalSpectrum DB)
          (eZ : Z ≅ formalSpectrum DC),
          ∃ (cToA : ContinuousHom DC DA) (cToB : ContinuousHom DC DB),
            formalSpectrumMap hC cToA = eX.inv ≫ f ≫ eZ.hom ∧
            formalSpectrumMap hC cToB = eY.inv ≫ g ≫ eZ.hom ∧
            letI : Algebra C A := cToA.toRingHom.toAlgebra
            letI : Algebra C B := cToB.toRingHom.toAlgebra
            letI : TopologicalSpace (A ⊗[C] B) :=
              TopologicalRing.tensorProductTopology (R := C) (M := A) (N := B)
            letI : UniformSpace (A ⊗[C] B) :=
              TopologicalRing.tensorProductUniformSpace (R := C) (M := A) (N := B)
            ∃ (DT : QuotientSystem 𝔅 S hS
                (TopologicalRing.CompletedTensorProduct (R := C) (M := A) (N := B)))
              (aToT : ContinuousHom DA DT) (bToT : ContinuousHom DB DT)
              (e : pullback f g ≅ formalSpectrum DT),
              TopologicalRing.IsWeaklyAdmissible
                  (TopologicalRing.CompletedTensorProduct (R := C) (M := A) (N := B)) ∧
                aToT.toRingHom = (UniformSpace.Completion.coeRingHom).comp
                    (Algebra.TensorProduct.includeLeftRingHom : A →+* A ⊗[C] B) ∧
                bToT.toRingHom = (UniformSpace.Completion.coeRingHom).comp
                    ((Algebra.TensorProduct.includeRight : B →ₐ[C] A ⊗[C] B).toRingHom) ∧
                e.hom ≫ formalSpectrumMap hA aToT = pullback.fst f g ≫ eX.hom ∧
                e.hom ≫ formalSpectrumMap hB bToT = pullback.snd f g ≫ eY.hom)
```

## Tag 0APX, a lemma

[Tag 0APX](https://stacks.math.columbia.edu/tag/0APX) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isSeparatedMorphism_of_isClosedImmersion_diag`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxioms.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxioms.lean#L228).

> A morphism `f : U ⟶ X` of fppf sheaves over `S` whose source is separated over `S`, that is
> whose diagonal `U ⟶ U ⨯ U` is a closed immersion, is separated.

```lean
theorem isSeparatedMorphism_of_isClosedImmersion_diag {U X : FppfSheaf B S hS}
    (hU : IsClosedImmersion B S hS (diag U)) (f : U ⟶ X) :
    IsSeparatedMorphism B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.16, Tag 0AJ4](https://stacks.math.columbia.edu/tag/0AJ4)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
