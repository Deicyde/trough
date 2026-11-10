---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isQuasiSeparatedOver_of_isSeparatedOver, AlgebraicGeometry.Space.presheaf_isSeparated_inf_quasiFinite_diag_of_isQuasiSeparatedOver, AlgebraicGeometry.Space.presheaf_isQuasiAffineHom_diag_of_isQuasiSeparatedOver, AlgebraicGeometry.presheaf_locallyOfFiniteType_diag, AlgebraicGeometry.presheaf_monomorphisms_diag, AlgebraicGeometry.presheaf_isSeparated_diag, AlgebraicGeometry.presheaf_locallyQuasiFinite_diag, AlgebraicGeometry.Space.IsSeparatedOver
statement: formalized
proof: formalized
---

# 65.13 Separation conditions on algebraic spaces

Section 65.13 of the Stacks Project, [Tag 02X3](https://stacks.math.columbia.edu/tag/02X3). 3 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02X3, the section

[Tag 02X3](https://stacks.math.columbia.edu/tag/02X3) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasiSeparatedOver_of_isSeparatedOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactDiagonalQuasiAffine.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactDiagonalQuasiAffine.lean#L82). The attribute's comment: “separated gives a quasi-compact diagonal”.

> **Stacks 02X3.** An algebraic space separated over `S` is quasi-separated over `S`: a
> diagonal which is a closed immersion is in particular quasi-compact. Together with the
> definition of quasi-separatedness this is the parenthetical remark of Section 65.13, that the
> diagonal is quasi-compact as soon as `F` is separated or quasi-separated over `S`.

```lean
theorem isQuasiSeparatedOver_of_isSeparatedOver (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : IsSeparatedOver B S hS F) : IsQuasiSeparatedOver B S hS F
```

**`AlgebraicGeometry.Space.presheaf_isSeparated_inf_quasiFinite_diag_of_isQuasiSeparatedOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactDiagonalQuasiAffine.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactDiagonalQuasiAffine.lean#L98). The attribute's comment: “a quasi-compact diagonal is quasi-finite and separated”.

> **Stacks 02X3.** Let `F` be an algebraic space over `S` whose diagonal is quasi-compact,
> that is, which is quasi-separated over `S`. Then the diagonal is separated and quasi-finite:
> every represented base change of it is a separated, locally quasi-finite, locally of finite
> type and quasi-compact morphism of schemes.
>
> Separatedness is Stacks 02X4, part (3); locally quasi-finite and locally of finite type are
> Stacks 02X4, part (4); quasi-compactness is the hypothesis.

```lean
theorem presheaf_isSeparated_inf_quasiFinite_diag_of_isQuasiSeparatedOver
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    (hΔ : IsQuasiSeparatedOver B S hS F) :
    (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@AlgebraicGeometry.IsSeparated.{u} ⊓ @AlgebraicGeometry.LocallyQuasiFinite.{u} ⊓
          @AlgebraicGeometry.LocallyOfFiniteType.{u} ⊓ @AlgebraicGeometry.QuasiCompact.{u} :
        MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS))) (diag F)
```

**`AlgebraicGeometry.Space.presheaf_isQuasiAffineHom_diag_of_isQuasiSeparatedOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactDiagonalQuasiAffine.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactDiagonalQuasiAffine.lean#L120). The attribute's comment: “a quasi-compact diagonal is quasi-affine”.

> **Stacks 02X3.** Let `F` be an algebraic space over `S` whose diagonal is quasi-compact,
> that is, which is quasi-separated over `S`. Then the diagonal is quasi-affine: every
> represented base change of it is a quasi-affine morphism of schemes.
>
> The diagonal is separated and quasi-finite, and a separated quasi-finite morphism of schemes
> is quasi-affine by Stacks 02LR.

```lean
theorem presheaf_isQuasiAffineHom_diag_of_isQuasiSeparatedOver
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    (hΔ : IsQuasiSeparatedOver B S hS F) :
    (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@AlgebraicGeometry.IsQuasiAffineHom.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS))) (diag F)
```

## Tag 02X4, a lemma

[Tag 02X4](https://stacks.math.columbia.edu/tag/02X4) in the Stacks Project.

**`AlgebraicGeometry.presheaf_locallyOfFiniteType_diag`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DiagonalProperties.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DiagonalProperties.lean#L332). The attribute's comment: “part (1)”.

> **Stacks 02X4, part (1).** The diagonal of an algebraic space over `S` is locally of
> finite type: every represented base change of it is a morphism of schemes locally of finite
> type.

```lean
theorem presheaf_locallyOfFiniteType_diag (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : IsAlgebraicSpace B S hS F) :
    (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@LocallyOfFiniteType.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS))) (diag F)
```

**`AlgebraicGeometry.presheaf_monomorphisms_diag`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DiagonalProperties.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DiagonalProperties.lean#L346). The attribute's comment: “part (2)”.

> **Stacks 02X4, part (2).** The diagonal of an algebraic space over `S` is a monomorphism:
> every represented base change of it is a monomorphism of schemes.

```lean
theorem presheaf_monomorphisms_diag (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : IsAlgebraicSpace B S hS F) :
    (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (MorphismProperty.monomorphisms Scheme.{u})
      (BigFppfOver.toScheme B S hS))) (diag F)
```

**`AlgebraicGeometry.presheaf_isSeparated_diag`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DiagonalProperties.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DiagonalProperties.lean#L360). The attribute's comment: “part (3)”.

> **Stacks 02X4, part (3).** The diagonal of an algebraic space over `S` is separated: every
> represented base change of it is a separated morphism of schemes. This follows from part (2),
> a monomorphism of schemes being separated.

```lean
theorem presheaf_isSeparated_diag (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : IsAlgebraicSpace B S hS F) :
    (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@IsSeparated.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS))) (diag F)
```

**`AlgebraicGeometry.presheaf_locallyQuasiFinite_diag`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DiagonalProperties.lean, line 374](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DiagonalProperties.lean#L374). The attribute's comment: “part (4)”.

> **Stacks 02X4, part (4).** The diagonal of an algebraic space over `S` is locally
> quasi-finite: every represented base change of it is a morphism of schemes which is locally of
> finite type and has discrete fibres.

```lean
theorem presheaf_locallyQuasiFinite_diag (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : IsAlgebraicSpace B S hS F) :
    (MorphismProperty.presheaf (MorphismProperty.inverseImage
      ((@LocallyOfFiniteType.{u} : MorphismProperty Scheme.{u}) ⊓
        (@LocallyQuasiFinite.{u} : MorphismProperty Scheme.{u}))
      (BigFppfOver.toScheme B S hS))) (diag F)
```

## Tag 02X5, a definition

[Tag 02X5](https://stacks.math.columbia.edu/tag/02X5) in the Stacks Project.

**`AlgebraicGeometry.Space.IsSeparatedOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Separated.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Separated.lean#L57). The attribute's comment: “separated”.

> An algebraic space over `S` is *separated over `S`* when its diagonal is a closed immersion
> of algebraic spaces.

```lean
abbrev IsSeparatedOver (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) : Prop
```

**`AlgebraicGeometry.Space.IsLocallySeparatedOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Separated.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Separated.lean#L63). The attribute's comment: “locally\_separated”.

> An algebraic space over `S` is *locally separated over `S`* when its diagonal is an
> immersion of algebraic spaces.

```lean
abbrev IsLocallySeparatedOver (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) : Prop
```

**`AlgebraicGeometry.Space.IsQuasiSeparatedOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Separated.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Separated.lean#L69). The attribute's comment: “quasi\_separated”.

> An algebraic space over `S` is *quasi-separated over `S`* when its diagonal is
> quasi-compact after every representable base change.

```lean
abbrev IsQuasiSeparatedOver (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) : Prop
```

**`AlgebraicGeometry.Space.IsZariskiLocallyQuasiSeparatedOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Separated.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Separated.lean#L77). The attribute's comment: “zariski\_locally\_quasi\_separated”.

> An algebraic space over `S` is *Zariski locally quasi-separated over `S`* when it admits a
> Zariski covering by open subspaces which are quasi-separated over `S`.

```lean
abbrev IsZariskiLocallyQuasiSeparatedOver (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 65.13, Tag 02X3](https://stacks.math.columbia.edu/tag/02X3)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
