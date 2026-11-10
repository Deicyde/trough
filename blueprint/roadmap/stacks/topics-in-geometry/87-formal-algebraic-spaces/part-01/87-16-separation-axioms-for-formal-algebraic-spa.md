---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.isAbsolutelyQuasiSeparated_reduction_tfae, AlgebraicGeometry.FormalSpace.isAbsolutelyQuasiSeparated_reduction_tfae_representable, AlgebraicGeometry.FormalSpace.isAbsolutelySeparated_reduction_of_hasAffineIntersectionsULift, AlgebraicGeometry.FormalSpace.isAbsolutelySeparated_reduction_iff_hasAffineIntersectionsULift, AlgebraicGeometry.FormalSpace.exists_isReduction_and_isAbsolutelySeparated_iff_hasAffineIntersectionsULift, AlgebraicGeometry.FormalSpace.isAbsolutelySeparated_reduction_iff_hasRepresentableAffineIntersectionsULift, AlgebraicGeometry.FormalSpace.exists_isReduction_and_isAbsolutelySeparated_iff_hasRepresentableAffineIntersectionsULift, AlgebraicGeometry.FormalSpace.IsSeparated
statement: formalized
proof: formalized
---

# 87.16 Separation axioms for formal algebraic spaces

Section 87.16 of the Stacks Project, [Tag 0AJ4](https://stacks.math.columbia.edu/tag/0AJ4). 5 tags here are carried by 26 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AJ5, a lemma

[Tag 0AJ5](https://stacks.math.columbia.edu/tag/0AJ5) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isAbsolutelyQuasiSeparated_reduction_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionQuasiSeparated.lean, line 281](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionQuasiSeparated.lean#L281). The attribute's comment: “the reduction of X is a given, in the sense of AlgebraicGeometry.FormalSpace.IsReduction and supplied by Stacks 0AIN, and is presented by a presheaf of Type u together with an isomorphism from its universe lift, since an algebraic space over S is a presheaf of Type u while a formal algebraic space is a sheaf of Type (u + 1); clauses (2) and (3) quantify over the objects of the site representing the fibre product, as the carriers of Stacks 0AHR do for the identical clauses, rather than asserting that it is representable, which is Stacks 0AIP”.

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

**`AlgebraicGeometry.FormalSpace.isAbsolutelyQuasiSeparated_reduction_tfae_representable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxiomsRepresentable.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxiomsRepresentable.lean#L255). The attribute's comment: “with clauses (2) and (3) in the source's own form, asserting that the fibre product U ×_X V is representable by an object of the site with quasi-compact underlying scheme; read against a reduction of X, in the sense of AlgebraicGeometry.FormalSpace.IsReduction and supplied by Stacks 0AIN, presented by a presheaf of Type u together with an isomorphism from its universe lift”.

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

**`AlgebraicGeometry.FormalSpace.isAbsolutelySeparated_reduction_of_hasAffineIntersectionsULift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionSeparated.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionSeparated.lean#L255). The attribute's comment: “(2) implies (1): the affine-intersection and surjectivity condition for X gives that the reduction of X is a separated algebraic space. The reduction is a given, in the sense of AlgebraicGeometry.FormalSpace.IsReduction and supplied by Stacks 0AIN, and is presented by a presheaf of Type u together with an isomorphism from its universe lift, since an algebraic space over S is a presheaf of Type u while a formal algebraic space is a sheaf of Type (u + 1). Clause (2) quantifies over the objects of the site representing the fibre product, as the carrier of Stacks 0AHS does for the identical clause, rather than asserting that it is representable, which is Stacks 0AIP. The converse implication (1) implies (2), the equivalence read against an arbitrary reduction, and the tag itself, whose reduction is produced from Stacks 0AIN, are AlgebraicGeometry.FormalSpace.hasAffineIntersectionsULift_of_isReduction, AlgebraicGeometry.FormalSpace.isAbsolutelySeparated_reduction_iff_hasAffineIntersectionsULift and AlgebraicGeometry.FormalSpace.exists_isReduction_and_isAbsolutelySeparated_iff_hasAffineIntersectionsULift in StacksFrontier.AlgebraicGeometry.FormalSpace.ReductionSeparatedConverse”. References: EGA I (10.15.7), “partial”.

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

**`AlgebraicGeometry.FormalSpace.isAbsolutelySeparated_reduction_iff_hasAffineIntersectionsULift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionSeparatedConverse.lean, line 416](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionSeparatedConverse.lean#L416). The attribute's comment: “both implications, read against a reduction of X, in the sense of AlgebraicGeometry.FormalSpace.IsReduction, and a presentation of it by a presheaf of Type u together with an isomorphism from its universe lift -- an algebraic space over S being a presheaf of Type u while a formal algebraic space is a sheaf of Type (u + 1). Clause (2) quantifies over the objects of the site representing the fibre product, as the carrier of Stacks 0AHS does for the identical clause, rather than asserting that it is representable, which is Stacks 0AIP. The tag itself, which produces the reduction and its presentation, is AlgebraicGeometry.FormalSpace.exists_isReduction_and_isAbsolutelySeparated_iff_hasAffineIntersectionsULift”. References: EGA I (10.15.7), “more general”.

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

**`AlgebraicGeometry.FormalSpace.exists_isReduction_and_isAbsolutelySeparated_iff_hasAffineIntersectionsULift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionSeparatedConverse.lean, line 455](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionSeparatedConverse.lean#L455). References: EGA I (10.15.7), “more general”.

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

**`AlgebraicGeometry.FormalSpace.isAbsolutelySeparated_reduction_iff_hasRepresentableAffineIntersectionsULift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionSeparatedRepresentable.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionSeparatedRepresentable.lean#L177). The attribute's comment: “both implications, with clause (2) in the source's own form, which asserts that the fibre product U ×_X V is representable by an object of the site and that its underlying scheme is affine, rather than quantifying over the objects of the site representing it. The two readings agree on a formal algebraic space, by AlgebraicGeometry.FormalSpace.hasRepresentableAffineIntersectionsULift_iff, whose nontrivial direction is the representability assertion of Stacks 0AIP for an arbitrary formal algebraic space. Read against a reduction of X, in the sense of AlgebraicGeometry.FormalSpace.IsReduction, and a presentation of it by a presheaf of Type u together with an isomorphism from its universe lift -- an algebraic space over S being a presheaf of Type u while a formal algebraic space is a sheaf of Type (u + 1). The tag with the reduction and its presentation produced is AlgebraicGeometry.FormalSpace.exists_isReduction_and_isAbsolutelySeparated_iff_hasRepresentableAffineIntersectionsULift”. References: EGA I (10.15.7), “more general”.

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

**`AlgebraicGeometry.FormalSpace.exists_isReduction_and_isAbsolutelySeparated_iff_hasRepresentableAffineIntersectionsULift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionSeparatedRepresentable.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionSeparatedRepresentable.lean#L213). The attribute's comment: “the reduction and its presentation by a presheaf of Type u produced, from Stacks 0AIN for an arbitrary formal algebraic space and from the pointwise u-smallness of an algebraic space, with clause (2) in the source's own form, which asserts that the fibre product U ×_X V is representable by an object of the site and that its underlying scheme is affine. The variant whose clause (2) quantifies over the objects of the site representing the fibre product instead is AlgebraicGeometry.FormalSpace.exists_isReduction_and_isAbsolutelySeparated_iff_hasAffineIntersectionsULift in StacksFrontier.AlgebraicGeometry.FormalSpace.ReductionSeparatedConverse”. References: EGA I (10.15.7), “more general”.

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

**`AlgebraicGeometry.FormalSpace.IsSeparated`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffineFibreProduct.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AffineFibreProduct.lean#L138). The attribute's comment: “clause (2): separated, in the form of clause (2) of Stacks 0AJ6”.

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

**`AlgebraicGeometry.FormalSpace.IsQuasiSeparated`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxioms.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxioms.lean#L88). The attribute's comment: “clause (1): quasi-separated, in the form of clause (3) of Stacks 0AJ5, whose equivalence with clause (2) of Stacks 0AJ5 and with quasi-separatedness of the reduction is not proved in this library”.

> An fppf sheaf `X` on the big fppf site of `S` is *quasi-separated* when, for every pair of
> morphisms to `X` from sheaves represented by affine schemes over `S`, every object of the site
> representing their fibre product has quasi-compact underlying scheme.

```lean
abbrev IsQuasiSeparated (X : FppfSheaf B S hS) : Prop
```

**`AlgebraicGeometry.FormalSpace.IsAffineFormalAlgebraicSpace.isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxioms.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxioms.lean#L109). The attribute's comment: “clause (2): an affine formal algebraic space is separated, in the form of clause (2) of Stacks 0AJ6, whose equivalence with clause (1) is not proved in this library”.

> Every affine formal algebraic space over `S` is separated, in the form of clause (2) of
> Stacks 0AJ6.

```lean
theorem IsAffineFormalAlgebraicSpace.isSeparated {X : FppfSheaf B S hS}
    (hX : IsAffineFormalAlgebraicSpace B S hS X) : IsSeparated B S hS X
```

**`AlgebraicGeometry.FormalSpace.isQuasiSeparated_of_isAffineFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxioms.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxioms.lean#L210). The attribute's comment: “clause (1): an affine formal algebraic space is quasi-separated, in the form of clause (3) of Stacks 0AJ5”.

> Every affine formal algebraic space over `S` is quasi-separated, in the form of clause (3)
> of Stacks 0AJ5.

```lean
theorem isQuasiSeparated_of_isAffineFormalAlgebraicSpace {X : FppfSheaf B S hS}
    (hX : IsAffineFormalAlgebraicSpace B S hS X) :
    IsQuasiSeparated B S hS X
```

**`AlgebraicGeometry.FormalSpace.IsQuasiSeparatedFormalAlgebraicSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxiomsRepresentable.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxiomsRepresentable.lean#L290). The attribute's comment: “clause (1): a formal algebraic space is quasi-separated when the conditions of Stacks 0AJ5 hold, recorded as clause (3) of Stacks 0AJ5 with the fibre product asserted to be a scheme; equivalent to every condition of Stacks 0AJ5 by isQuasiSeparatedFormalAlgebraicSpace_tfae”.

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

**`AlgebraicGeometry.FormalSpace.IsSeparatedFormalAlgebraicSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxiomsRepresentable.lean, line 311](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxiomsRepresentable.lean#L311). The attribute's comment: “clause (2): a formal algebraic space is separated when the conditions of Stacks 0AJ6 hold, recorded as clause (2) of Stacks 0AJ6 with the fibre product asserted to be a scheme; equivalent to clause (1) of Stacks 0AJ6 by isSeparatedFormalAlgebraicSpace_tfae”.

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

**`AlgebraicGeometry.FormalSpace.isQuasiSeparatedFormalAlgebraicSpace_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxiomsRepresentable.lean, line 356](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxiomsRepresentable.lean#L356). The attribute's comment: “clause (1): the definition is equivalent to each of the conditions of Stacks 0AJ5, read against a reduction of X presented by a presheaf of Type u, which exists by Stacks 0AIN”.

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

**`AlgebraicGeometry.FormalSpace.isSeparatedFormalAlgebraicSpace_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxiomsRepresentable.lean, line 381](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxiomsRepresentable.lean#L381). The attribute's comment: “clause (2): the definition is equivalent to clause (1) of Stacks 0AJ6, read against a reduction of X presented by a presheaf of Type u, which exists by Stacks 0AIN”.

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

**`AlgebraicGeometry.FormalSpace.isAffineFormalAlgebraicSpace_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffineFibreProduct.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AffineFibreProduct.lean#L254). The attribute's comment: “the fibre product of affine formal algebraic spaces over a separated base”.

> The fibre product of two affine formal algebraic spaces over a separated fppf sheaf with
> representable relative products is an affine formal algebraic space.

```lean
theorem isAffineFormalAlgebraicSpace_pullback
    {X Y Z : FppfSheaf B S hS} (p : X ⟶ Z) (q : Y ⟶ Z)
    (hZrep : HasRepresentableRelativeProducts B S hS Z)
    (hZsep : IsSeparated B S hS Z)
    (hX : IsAffineFormalAlgebraicSpace B S hS X)
    (hY : IsAffineFormalAlgebraicSpace B S hS Y) :
    IsAffineFormalAlgebraicSpace B S hS (pullback p q)
```

**`AlgebraicGeometry.FormalSpace.isAffineFormalAlgebraicSpace_pullback_of_isFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffineFibreProductFormalBase.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AffineFibreProductFormalBase.lean#L59). The attribute's comment: “clause (1): the fibre product of two affine formal algebraic spaces over a separated formal algebraic space, at the hypotheses of the source”.

> **Stacks 0AN3, clause (1).** The fibre product of two affine formal algebraic spaces over a
> separated formal algebraic space is an affine formal algebraic space.

```lean
theorem isAffineFormalAlgebraicSpace_pullback_of_isFormalAlgebraicSpace
    {X Y Z : FppfSheaf B S hS} (p : X ⟶ Z) (q : Y ⟶ Z)
    (hZ : IsFormalAlgebraicSpace B S hS Z)
    (hZsep : IsSeparated B S hS Z)
    (hX : IsAffineFormalAlgebraicSpace B S hS X)
    (hY : IsAffineFormalAlgebraicSpace B S hS Y) :
    IsAffineFormalAlgebraicSpace B S hS (pullback p q)
```

**`AlgebraicGeometry.FormalSpace.exists_quotientSystem_iso_pullback_completedTensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletedTensorFibreProduct.lean, line 651](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletedTensorFibreProduct.lean#L651). The attribute's comment: “clause (3), that the fibre product of two McQuillan affine formal algebraic spaces over a third is the formal spectrum of the completed tensor product of their weakly admissible topological rings, compatibly with both projections. The quotient system on the completed tensor product and the comparison with the fibre product are proved. The one input this library does not carry is the hypothesis epres: that the fibre product is itself a formal spectrum, which is clause (2) of the same tag together with the McQuillan criterion of Stacks 0AIC. Stacks 0AN0 is full faithfulness of Spf against formal spectra only (existsUnique_continuousHom_formalSpectrumMap_eq), not a universal property against arbitrary fppf sheaves, so representability of the fibre product is not a consequence of it; separatedness of the base, which the source uses only to obtain clauses (1) and (2), is therefore not needed here and is not assumed”.

> **Stacks 0AN3, clause (3).** Let `A₀`, `A₁` and `A` be weakly admissible topological rings
> over `S` with chart systems `D₀`, `D₁`, `D`, and let `A₀ → A₁` and `A₀ → A` be continuous
> homomorphisms over `S`. If the fibre product `Spf A₁ ×_{Spf A₀} Spf A` is itself the formal
> spectrum of a weakly admissible topological ring over `S`, then it is the formal spectrum of the
> completed tensor product `A₁ ⊗̂_{A₀} A`: that ring carries a chart system over `S` and an
> isomorphism onto the fibre product compatible with both projections, through which the two
> projections are the formal spectra of the two canonical maps into the completed tensor
> product.

```lean
theorem exists_quotientSystem_iso_pullback_completedTensorProduct
    (h₀ : TopologicalRing.IsWeaklyAdmissible A₀)
    (h₁ : TopologicalRing.IsWeaklyAdmissible A₁) (hA : TopologicalRing.IsWeaklyAdmissible A)
    (D₀ : QuotientSystem B S hS A₀) (D₁ : QuotientSystem B S hS A₁)
    (D : QuotientSystem B S hS A)
    (c₁ : ContinuousHom D₀ D₁) (c : ContinuousHom D₀ D)
    (hc₁ : c₁.toRingHom = algebraMap A₀ A₁) (hc : c.toRingHom = algebraMap A₀ A)
    {R : Type u} [CommRing R] [TopologicalSpace R] [IsTopologicalRing R] [IsLinearTopology R R]
    (hR : TopologicalRing.IsWeaklyAdmissible R) (E : QuotientSystem B S hS R)
    (epres : pullback (formalSpectrumMap h₀ c₁) (formalSpectrumMap h₀ c) ≅ formalSpectrum E) :
    ∃ (DT : QuotientSystem B S hS (TopologicalRing.CompletedTensorProduct
        (R := A₀) (M := A₁) (N := A)))
        (t₁ : ContinuousHom D₁ DT) (t : ContinuousHom D DT)
        (eT : pullback (formalSpectrumMap h₀ c₁) (formalSpectrumMap h₀ c) ≅ formalSpectrum DT),
      t₁.toRingHom = algebraMap A₁ (TopologicalRing.CompletedTensorProduct
          (R := A₀) (M := A₁) (N := A)) ∧
        t.toRingHom = algebraMap A (TopologicalRing.CompletedTensorProduct
            (R := A₀) (M := A₁) (N := A)) ∧
        eT.hom ≫ formalSpectrumMap h₁ t₁ =
          pullback.fst (formalSpectrumMap h₀ c₁) (formalSpectrumMap h₀ c) ∧
        eT.hom ≫ formalSpectrumMap hA t =
          pullback.snd (formalSpectrumMap h₀ c₁) (formalSpectrumMap h₀ c)
```

**`AlgebraicGeometry.FormalSpace.exists_continuous_ringEquiv_completedTensorProduct_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletedTensorFibreProduct.lean, line 779](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletedTensorFibreProduct.lean#L779). The attribute's comment: “clause (3) read on chart rings: the chart ring of the fibre product of two McQuillan affine formal algebraic spaces over a third is the completed tensor product of their weakly admissible topological rings, by an isomorphism of topological rings compatible with both projections. The one input this library does not carry is the hypothesis epres, that the fibre product is itself a formal spectrum, which is clause (2) of the same tag together with the McQuillan criterion of Stacks 0AIC; Stacks 0AN0 is full faithfulness of Spf against formal spectra only, so representability of the fibre product does not follow from it. Separatedness of the base, which the source uses only for clauses (1) and (2), is not needed here and is not assumed”.

> **Stacks 0AN3, clause (3), in the form of an isomorphism of chart rings.** If the fibre
> product `Spf A₁ ×_{Spf A₀} Spf A` is the formal spectrum of a weakly admissible topological
> ring `R` over `S`, then `R` is isomorphic, as a topological ring, to the completed tensor
> product `A₁ ⊗̂_{A₀} A`, compatibly with the two projections: the isomorphism carries each of the
> two canonical maps into the completed tensor product to the continuous homomorphism that
> Stacks 0AN0 attaches to the corresponding projection.

```lean
theorem exists_continuous_ringEquiv_completedTensorProduct_pullback
    (h₀ : TopologicalRing.IsWeaklyAdmissible A₀)
    (h₁ : TopologicalRing.IsWeaklyAdmissible A₁) (hA : TopologicalRing.IsWeaklyAdmissible A)
    (D₀ : QuotientSystem B S hS A₀) (D₁ : QuotientSystem B S hS A₁)
    (D : QuotientSystem B S hS A)
    (c₁ : ContinuousHom D₀ D₁) (c : ContinuousHom D₀ D)
    (hc₁ : c₁.toRingHom = algebraMap A₀ A₁) (hc : c.toRingHom = algebraMap A₀ A)
    {R : Type u} [CommRing R] [TopologicalSpace R] [IsTopologicalRing R] [IsLinearTopology R R]
    (hR : TopologicalRing.IsWeaklyAdmissible R) (E : QuotientSystem B S hS R)
    (epres : pullback (formalSpectrumMap h₀ c₁) (formalSpectrumMap h₀ c) ≅ formalSpectrum E) :
    ∃ ε : (TopologicalRing.CompletedTensorProduct (R := A₀) (M := A₁) (N := A)) ≃+* R,
      Continuous ε ∧ Continuous ε.symm ∧
        ∀ (a₁ : ContinuousHom D₁ E) (a : ContinuousHom D E),
          formalSpectrumMap h₁ a₁ = epres.inv ≫
              pullback.fst (formalSpectrumMap h₀ c₁) (formalSpectrumMap h₀ c) →
            formalSpectrumMap hA a = epres.inv ≫
              pullback.snd (formalSpectrumMap h₀ c₁) (formalSpectrumMap h₀ c) →
            ε.toRingHom.comp (algebraMap A₁ (TopologicalRing.CompletedTensorProduct
                (R := A₀) (M := A₁) (N := A))) = a₁.toRingHom ∧
              ε.toRingHom.comp (algebraMap A (TopologicalRing.CompletedTensorProduct
                  (R := A₀) (M := A₁) (N := A))) = a.toRingHom
```

**`AlgebraicGeometry.FormalSpace.exists_quotientSystem_iso_pullback_completedTensorProduct_of_isWeaklyAdmissible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletedTensorFibreProduct.lean, line 1241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletedTensorFibreProduct.lean#L1241). The attribute's comment: “clause (3), that the fibre product of two McQuillan affine formal algebraic spaces over a third is the formal spectrum of the completed tensor product of their weakly admissible topological rings, compatibly with both projections, with no hypothesis beyond the weak admissibility of the three rings: the fibre product is proved to be a formal spectrum, as the colimit of the stagewise fibre products”.

> **Stacks 0AN3, clause (3), with no presentation of the fibre product assumed.** Let `A₀`,
> `A₁` and `A` be weakly admissible topological rings over `S` with quotient systems `D₀`, `D₁`,
> `D`, and let `A₀ → A₁` and `A₀ → A` be continuous homomorphisms over `S`. Then the fibre product
> `Spf A₁ ×_{Spf A₀} Spf A` is the formal spectrum of the completed tensor product
> `A₁ ⊗̂_{A₀} A`: that ring carries a quotient system over `S` and an isomorphism of its formal
> spectrum onto the fibre product, through which the two projections are the formal spectra of
> the two canonical maps into the completed tensor product.
>
> This is `exists_quotientSystem_iso_pullback_completedTensorProduct` with its hypothesis `epres`
> discharged: the fibre product of the two formal spectra is the colimit of the stagewise fibre
> products, which are the stages of `Spf (A₁ ⊗̂_{A₀} A)` at the projection kernels, and those are
> cofinal among all its stages.

```lean
theorem exists_quotientSystem_iso_pullback_completedTensorProduct_of_isWeaklyAdmissible
    (h₀ : TopologicalRing.IsWeaklyAdmissible A₀)
    (h₁ : TopologicalRing.IsWeaklyAdmissible A₁) (hA : TopologicalRing.IsWeaklyAdmissible A)
    (D₀ : QuotientSystem B S hS A₀) (D₁ : QuotientSystem B S hS A₁)
    (D : QuotientSystem B S hS A)
    (c₁ : ContinuousHom D₀ D₁) (c : ContinuousHom D₀ D)
    (hc₁ : c₁.toRingHom = algebraMap A₀ A₁) (hc : c.toRingHom = algebraMap A₀ A) :
    ∃ (DT : QuotientSystem B S hS (TopologicalRing.CompletedTensorProduct
        (R := A₀) (M := A₁) (N := A)))
        (t₁ : ContinuousHom D₁ DT) (t : ContinuousHom D DT)
        (eT : pullback (formalSpectrumMap h₀ c₁) (formalSpectrumMap h₀ c) ≅ formalSpectrum DT),
      t₁.toRingHom = algebraMap A₁ (TopologicalRing.CompletedTensorProduct
          (R := A₀) (M := A₁) (N := A)) ∧
        t.toRingHom = algebraMap A (TopologicalRing.CompletedTensorProduct
            (R := A₀) (M := A₁) (N := A)) ∧
        eT.hom ≫ formalSpectrumMap h₁ t₁ =
          pullback.fst (formalSpectrumMap h₀ c₁) (formalSpectrumMap h₀ c) ∧
        eT.hom ≫ formalSpectrumMap hA t =
          pullback.snd (formalSpectrumMap h₀ c₁) (formalSpectrumMap h₀ c)
```

**`AlgebraicGeometry.FormalSpace.exists_formalSpectrum_completedTensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletedTensorProductFibreProduct.lean, line 1017](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletedTensorProductFibreProduct.lean#L1017). The attribute's comment: “clause (3): the fibre product of two McQuillan affine formal algebraic spaces over a McQuillan affine separated one is the formal spectrum of the completed tensor product of their weakly admissible topological rings, at the hypotheses of the source”.

> **Stacks 0AN3, clause (3).** Let `S` be a scheme contained in a big fppf site `B`, let
> `X ⟶ Z` and `Y ⟶ Z` be morphisms of fppf sheaves over `S` with `Z` separated, and suppose that
> `X`, `Y` and `Z` are the formal spectra of weakly admissible topological rings `A`, `B` and `C`
> over `S`, the two morphisms being the ones induced by continuous homomorphisms `C ⟶ A` and
> `C ⟶ B` over `S`. Then the fibre product `X ×_Z Y` is the formal spectrum of the completed
> tensor product `A ⊗̂_C B`, which is again weakly admissible.

```lean
theorem exists_formalSpectrum_completedTensorProduct (𝔅 : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : 𝔅.Contains S) {A B C : Type u} [CommRing A] [TopologicalSpace A]
    [IsTopologicalRing A] [IsLinearTopology A A] [CommRing B] [TopologicalSpace B]
    [IsTopologicalRing B] [IsLinearTopology B B] [CommRing C] [TopologicalSpace C]
    [IsTopologicalRing C] [IsLinearTopology C C]
    (hA : TopologicalRing.IsWeaklyAdmissible A) (hB : TopologicalRing.IsWeaklyAdmissible B)
    (hC : TopologicalRing.IsWeaklyAdmissible C) (DA : QuotientSystem 𝔅 S hS A)
    (DB : QuotientSystem 𝔅 S hS B) (DC : QuotientSystem 𝔅 S hS C)
    {X Y Z : FppfSheaf 𝔅 S hS} (f : X ⟶ Z) (g : Y ⟶ Z) (eX : X ≅ formalSpectrum DA)
    (eY : Y ≅ formalSpectrum DB) (eZ : Z ≅ formalSpectrum DC)
    (_hZsep : IsSeparated 𝔅 S hS Z) (cToA : ContinuousHom DC DA) (cToB : ContinuousHom DC DB)
    (hf : formalSpectrumMap hC cToA = eX.inv ≫ f ≫ eZ.hom)
    (hg : formalSpectrumMap hC cToB = eY.inv ≫ g ≫ eZ.hom) :
    letI : Algebra C A := cToA.toRingHom.toAlgebra
    letI : Algebra C B := cToB.toRingHom.toAlgebra
    ∃ DT : QuotientSystem 𝔅 S hS
        (TopologicalRing.CompletedTensorProduct (R := C) (M := A) (N := B)),
      TopologicalRing.IsWeaklyAdmissible
          (TopologicalRing.CompletedTensorProduct (R := C) (M := A) (N := B)) ∧
        Nonempty (pullback f g ≅ formalSpectrum DT)
```

**`AlgebraicGeometry.FormalSpace.exists_formalSpectrum_completedTensorProduct_compatible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletedTensorProductFibreProductSupplement.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletedTensorProductFibreProductSupplement.lean#L373). The attribute's comment: “clause (3): the fibre product of two McQuillan affine formal algebraic spaces over a separated McQuillan affine formal algebraic space is the formal spectrum of the completed tensor product of the three weakly admissible topological rings, compatibly with both projections; McQuillanness of the two factors is in the form of condition (2) of Stacks 0AIC, the form the library's clause (2) consumes”.

> Let `X ⟶ Z` and `Y ⟶ Z` be morphisms of fppf sheaves on the big fppf site of `S` with `Z` a
> separated affine formal algebraic space, let `X` and `Y` be McQuillan affine formal algebraic
> spaces, and let `X = Spf A`, `Y = Spf B`, `Z = Spf C` for weakly admissible topological rings
> `A`, `B`, `C` over `S` with the two morphisms induced by continuous ring maps `C → A` and `C → B`
> over `S`. Then
>
> `X ×_Z Y = Spf (A ⊗̂_C B)`,
>
> compatibly with the two projections and with the canonical maps of `A` and of `B` into the
> completed tensor product.
>
> The conclusion produces the ring over `S`, that is the
> `AlgebraicGeometry.FormalSpace.QuotientSystem` of `A ⊗̂_C B`, together with the two continuous
> homomorphisms over `S` out of `A` and `B`, says that those are the canonical maps into the
> completion of the algebraic tensor product, and characterises the isomorphism by its
> compatibility with both projections of the fibre product.

```lean
theorem exists_formalSpectrum_completedTensorProduct_compatible {X Y Z : FppfSheaf 𝔅 S hS}
    (hX : HasAffineClosedImmersionCriterionMapToSpec 𝔅 S hS X)
    (hY : HasAffineClosedImmersionCriterionMapToSpec 𝔅 S hS Y)
    (hZ : IsAffineFormalAlgebraicSpace 𝔅 S hS Z)
    (hZsep : IsSeparated 𝔅 S hS Z)
    {A B C : Type u}
    [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
    [CommRing C] [TopologicalSpace C] [IsTopologicalRing C] [IsLinearTopology C C]
    (hA : TopologicalRing.IsWeaklyAdmissible A)
    (hB : TopologicalRing.IsWeaklyAdmissible B)
    (hC : TopologicalRing.IsWeaklyAdmissible C)
    (DA : QuotientSystem 𝔅 S hS A) (DB : QuotientSystem 𝔅 S hS B)
    (DC : QuotientSystem 𝔅 S hS C)
    (eX : X ≅ formalSpectrum DA) (eY : Y ≅ formalSpectrum DB) (eZ : Z ≅ formalSpectrum DC)
    (f : X ⟶ Z) (g : Y ⟶ Z)
    (cToA : ContinuousHom DC DA) (cToB : ContinuousHom DC DB)
    (hf : formalSpectrumMap hC cToA = eX.inv ≫ f ≫ eZ.hom)
    (hg : formalSpectrumMap hC cToB = eY.inv ≫ g ≫ eZ.hom) :
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
        e.hom ≫ formalSpectrumMap hB bToT = pullback.snd f g ≫ eY.hom
```

**`AlgebraicGeometry.FormalSpace.isPullback_formalSpectrumMap_completedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSpectrumCompletedTensorProduct.lean, line 1341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSpectrumCompletedTensorProduct.lean#L1341). The attribute's comment: “clause (3): Spf A ×_{Spf C} Spf B corresponds to the completed tensor product”.

> Let `A₀ → A₁` and `A₀ → A₂` be continuous homomorphisms of
> weakly admissible topological rings over `S`. Then the completed tensor product
> `T = A₁ ⊗̂_{A₀} A₂` is weakly admissible and `Spf T`, with the maps induced by the canonical
> continuous homomorphisms `A₁ → T` and `A₂ → T`, is the fibre product
> `Spf A₁ ×_{Spf A₀} Spf A₂`.

```lean
theorem isPullback_formalSpectrumMap_completedTensor :
    TopologicalRing.IsWeaklyAdmissible
        (TopologicalRing.CompletedTensorProduct (R := A₀) (M := A₁) (N := A₂)) ∧
      IsPullback (formalSpectrumMap hA₁ (completedTensorLeftHom A₀ hA₁ hA₂ D₁ D₂))
        (formalSpectrumMap hA₂ (completedTensorRightHom A₀ hA₁ hA₂ D₁ D₂ hA₀ φ₁ φ₂ hφ₁ hφ₂))
        (formalSpectrumMap hA₀ φ₁) (formalSpectrumMap hA₀ φ₂)
```

**`AlgebraicGeometry.FormalSpace.hasAffineClosedImmersionCriterion_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedFibreProduct.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedFibreProduct.lean#L247). The attribute's comment: “clause (2): the fibre product of two McQuillan affine formal algebraic spaces over a separated formal algebraic space is McQuillan affine, with McQuillanness in the form of condition (2) of Stacks 0AIC”.

> **Stacks 0AN3, clause (2).** Let `X ⟶ Z` and `Y ⟶ Z` be morphisms of fppf sheaves on the
> big fppf site of `S` with `Z` a separated formal algebraic space. If `X` and `Y` are McQuillan
> affine formal algebraic spaces, then so is the fibre product `X ×_Z Y`.
>
> McQuillanness is here condition (2) of **Stacks 0AIC**: an affine formal algebraic space
> together with a morphism to the spectrum of a ring through which every closed
> immersion of an affine scheme of the site composes to a closed immersion of schemes. The ring
> witnessing the conclusion is the tensor product over `ℤ` of the two rings witnessing the
> hypotheses, which is the ring the source's proof uses.

```lean
theorem hasAffineClosedImmersionCriterion_pullback
    {X Y Z : FppfSheaf B S hS} (p : X ⟶ Z) (q : Y ⟶ Z)
    (hZ : IsFormalAlgebraicSpace B S hS Z)
    (hZsep : IsSeparated B S hS Z)
    (hX : HasAffineClosedImmersionCriterionMapToSpec B S hS X)
    (hY : HasAffineClosedImmersionCriterionMapToSpec B S hS Y) :
    HasAffineClosedImmersionCriterionMapToSpec B S hS (pullback p q)
```

**`AlgebraicGeometry.FormalSpace.hasSomeSurjectivePresentation_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedFibreProduct.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedFibreProduct.lean#L292). The attribute's comment: “clause (2): the fibre product of two McQuillan affine formal algebraic spaces over a separated formal algebraic space is McQuillan affine, with the conclusion in the form of condition (4) of Stacks 0AIC, the predicate Stacks 0AID names McQuillan in this library”.

> **Stacks 0AN3, clause (2), in the form of condition (4) of Stacks 0AIC.** The fibre product
> of two McQuillan affine formal algebraic spaces over a separated formal algebraic space is an
> affine formal algebraic space some presentation of which by affine thickenings has surjective
> section-ring projections.
>
> This is the predicate `AlgebraicGeometry.FormalSpace.HasSomeSurjectivePresentation` that
> **Stacks 0AID** names "McQuillan" in this library, and it is the hypothesis as well as the
> conclusion: condition (4) gives condition (2) by
> `AlgebraicGeometry.FormalSpace.hasAffineClosedImmersionCriterion_of_hasSomeSurjectivePresentation`,
> and condition (2) gives condition (4) back by the implications (2) ⟹ (5) ⟹ (4) of
> **Stacks 0AIC**.

```lean
theorem hasSomeSurjectivePresentation_pullback
    {X Y Z : FppfSheaf B S hS} (p : X ⟶ Z) (q : Y ⟶ Z)
    (hZ : IsFormalAlgebraicSpace B S hS Z)
    (hZsep : IsSeparated B S hS Z)
    (hX : HasSomeSurjectivePresentation B S hS X)
    (hY : HasSomeSurjectivePresentation B S hS Y) :
    HasSomeSurjectivePresentation B S hS (pullback p q)
```

## Tag 0APX, a lemma

[Tag 0APX](https://stacks.math.columbia.edu/tag/0APX) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isSeparatedMorphism_of_isClosedImmersion_diag`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxioms.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparationAxioms.lean#L228).

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
