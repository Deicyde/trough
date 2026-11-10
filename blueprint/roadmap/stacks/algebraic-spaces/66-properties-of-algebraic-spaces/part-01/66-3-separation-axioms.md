---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isAbsolutelyQuasiSeparated_of_presentation, AlgebraicGeometry.Space.IsAbsolutelySeparated, AlgebraicGeometry.Space.IsAbsolutelyLocallySeparated, AlgebraicGeometry.Space.IsAbsolutelyQuasiSeparated, AlgebraicGeometry.Space.IsAbsolutelyZariskiLocallyQuasiSeparated, AlgebraicGeometry.Space.isAbsolutelyZariskiLocallyQuasiSeparated_of_isAbsolutelyQuasiSeparated, AlgebraicGeometry.Space.isAbsolutelyLocallySeparated_of_isAbsolutelySeparated, AlgebraicGeometry.Space.isAbsolutelyQuasiSeparated_of_isAbsolutelySeparated
statement: formalized
proof: formalized
---

# 66.3 Separation axioms

Section 66.3 of the Stacks Project, [Tag 03BR](https://stacks.math.columbia.edu/tag/03BR). 4 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03BS, a definition

[Tag 03BS](https://stacks.math.columbia.edu/tag/03BS) in the Stacks Project.

**`AlgebraicGeometry.Space.isAbsolutelyQuasiSeparated_of_presentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PresentationQuasiCompact.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PresentationQuasiCompact.lean#L125). The attribute's comment: “part (3): quasi-separated”.

> **Stacks 07S4 for a presentation.** An algebraic space presented by a chart whose
> underlying space is quasi-separated, with quasi-compact source projection, is
> quasi-separated.
>
> The relation of the presentation is the kernel pair of the chart, so
> `presheaf_quasiCompact_pullback_snd_of_presentation` supplies the hypothesis of Stacks
> 07S4.

```lean
theorem isAbsolutelyQuasiSeparated_of_presentation (hZ : B.Contains (⊤_ Scheme.{u}))
    (hseparated : QuasiSeparatedSpace ((BigFppfOver.toScheme B S hS).obj P.U))
    (hsource : QuasiCompact ((BigFppfOver.toScheme B S hS).map P.source)) :
    IsAbsolutelyQuasiSeparated B S hS hZ F
```

**`AlgebraicGeometry.Space.IsAbsolutelySeparated`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Separated.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Separated.lean#L95). The attribute's comment: “part (1): separated”.

> An algebraic space is *separated* when it is separated over the terminal scheme, that is,
> when its absolute diagonal is a closed immersion.

```lean
abbrev IsAbsolutelySeparated (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) : Prop
```

**`AlgebraicGeometry.Space.IsAbsolutelyLocallySeparated`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Separated.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Separated.lean#L101). The attribute's comment: “part (2): locally separated”.

> An algebraic space is *locally separated* when it is locally separated over the terminal
> scheme, that is, when its absolute diagonal is an immersion.

```lean
abbrev IsAbsolutelyLocallySeparated (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) : Prop
```

**`AlgebraicGeometry.Space.IsAbsolutelyQuasiSeparated`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Separated.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Separated.lean#L107). The attribute's comment: “part (3): quasi-separated”.

> An algebraic space is *quasi-separated* when it is quasi-separated over the terminal
> scheme, that is, when its absolute diagonal is quasi-compact.

```lean
abbrev IsAbsolutelyQuasiSeparated (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) : Prop
```

**`AlgebraicGeometry.Space.IsAbsolutelyZariskiLocallyQuasiSeparated`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Separated.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Separated.lean#L113). The attribute's comment: “part (4): Zariski locally quasi-separated”.

> An algebraic space is *Zariski locally quasi-separated* when its absolute form admits a
> Zariski covering by quasi-separated open subspaces.

```lean
abbrev IsAbsolutelyZariskiLocallyQuasiSeparated
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) : Prop
```

## Tag 03DY, a lemma

[Tag 03DY](https://stacks.math.columbia.edu/tag/03DY) in the Stacks Project.

**`AlgebraicGeometry.Space.isAbsolutelyZariskiLocallyQuasiSeparated_of_isAbsolutelyQuasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ConditionComparisons.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ConditionComparisons.lean#L101). The attribute's comment: “part (2): Zariski locally quasi-separated”.

> Condition `(η)` implies condition `(ζ)`: a quasi-separated algebraic space is Zariski
> locally quasi-separated.

```lean
theorem isAbsolutelyZariskiLocallyQuasiSeparated_of_isAbsolutelyQuasiSeparated
    (hX : IsAlgebraicSpace B S hS X) (h : IsAbsolutelyQuasiSeparated B S hS hZ X) :
    IsAbsolutelyZariskiLocallyQuasiSeparated B S hS hZ X
```

**`AlgebraicGeometry.Space.isAbsolutelyLocallySeparated_of_isAbsolutelySeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SeparatedVariants.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SeparatedVariants.lean#L89). The attribute's comment: “part (1): locally separated”.

> A separated algebraic space is locally separated.

```lean
theorem isAbsolutelyLocallySeparated_of_isAbsolutelySeparated
    (hZ : B.Contains (⊤_ Scheme.{u})) (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : IsAbsolutelySeparated B S hS hZ F) :
    IsAbsolutelyLocallySeparated B S hS hZ F
```

**`AlgebraicGeometry.Space.isAbsolutelyQuasiSeparated_of_isAbsolutelySeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SeparatedVariants.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SeparatedVariants.lean#L97). The attribute's comment: “part (1): quasi-separated”.

> A separated algebraic space is quasi-separated.

```lean
theorem isAbsolutelyQuasiSeparated_of_isAbsolutelySeparated
    (hZ : B.Contains (⊤_ Scheme.{u})) (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : IsAbsolutelySeparated B S hS hZ F) :
    IsAbsolutelyQuasiSeparated B S hS hZ F
```

## Tag 0AHR, a lemma

[Tag 0AHR](https://stacks.math.columbia.edu/tag/0AHR) in the Stacks Project.

**`AlgebraicGeometry.Space.isAbsolutelyQuasiSeparated_iff_compactSpace_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiSeparatedFibreProducts.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiSeparatedFibreProducts.lean#L249). The attribute's comment: “equivalence of (1) and (2)”.

> **Stacks 0AHR, equivalence of (1) and (2).** An algebraic space over `S` is quasi-separated
> exactly when the fibre product of any two quasi-compact schemes over it is a quasi-compact
> scheme.

```lean
theorem isAbsolutelyQuasiSeparated_iff_compactSpace_pullback
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X) :
    IsAbsolutelyQuasiSeparated B S hS hZ X ↔
      ∀ (U V : BigFppfOver B S hS)
        (f : yoneda.obj U ⟶ X) (g : yoneda.obj V ⟶ X),
        CompactSpace ((BigFppfOver.toScheme B S hS).obj U) →
        CompactSpace ((BigFppfOver.toScheme B S hS).obj V) →
        ∃ W : BigFppfOver B S hS,
          CompactSpace ((BigFppfOver.toScheme B S hS).obj W) ∧
          Nonempty (yoneda.obj W ≅ pullback f g)
```

**`AlgebraicGeometry.Space.isAbsolutelyQuasiSeparated_iff_compactSpace_pullback_affine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiSeparatedFibreProducts.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiSeparatedFibreProducts.lean#L270). The attribute's comment: “equivalence of (1) and (3)”.

> **Stacks 0AHR, equivalence of (1) and (3).** It is enough to test quasi-compactness of the
> fibre products of Stacks 0AHR on pairs of *affine* schemes over the algebraic space.

```lean
theorem isAbsolutelyQuasiSeparated_iff_compactSpace_pullback_affine
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X) :
    IsAbsolutelyQuasiSeparated B S hS hZ X ↔
      ∀ (U V : BigFppfOver B S hS)
        (f : yoneda.obj U ⟶ X) (g : yoneda.obj V ⟶ X),
        IsAffine ((BigFppfOver.toScheme B S hS).obj U) →
        IsAffine ((BigFppfOver.toScheme B S hS).obj V) →
        ∃ W : BigFppfOver B S hS,
          CompactSpace ((BigFppfOver.toScheme B S hS).obj W) ∧
          Nonempty (yoneda.obj W ≅ pullback f g)
```

**`AlgebraicGeometry.Space.isAbsolutelyQuasiSeparated_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SeparatedAffineIntersections.lean, line 570](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SeparatedAffineIntersections.lean#L570).

> **Stacks 0AHR.** For an algebraic space `X` over `S` the following are equivalent: `X` is a
> quasi-separated algebraic space; for every pair of morphisms into `X` from objects of the big
> fppf site with quasi-compact underlying scheme the fibre product has quasi-compact underlying
> scheme; and the same for every pair of morphisms from objects with affine underlying scheme.
>
> Condition (1) implies condition (2) because the fibre product maps to the product of the two
> factors by a base change of the absolute diagonal, so that morphism is quasi-compact, and the
> product of two quasi-compact objects over the terminal scheme is quasi-compact. Condition (2)
> implies condition (3) because an affine scheme is quasi-compact. Condition (3) implies
> condition (1) because quasi-compactness is Zariski local at the target, so the diagonal need
> only be tested on objects of the site with affine underlying scheme, and over such an object
> the criterion applies to the two morphisms the test factors through.

```lean
theorem isAbsolutelyQuasiSeparated_tfae (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B S hS X) :
    List.TFAE
      [ IsAbsolutelyQuasiSeparated B S hS hZ X,
        HasQuasiCompactIntersections B S hS
          (fun Z : Scheme.{u} ↦ CompactSpace (Z : Type u)) X,
        HasQuasiCompactIntersections B S hS (fun Z : Scheme.{u} ↦ IsAffine Z) X ]
```

## Tag 0AHS, a lemma

[Tag 0AHS](https://stacks.math.columbia.edu/tag/0AHS) in the Stacks Project.

**`AlgebraicGeometry.Space.isAbsolutelySeparated_iff_hasAffineIntersections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SeparatedAffineIntersections.lean, line 384](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SeparatedAffineIntersections.lean#L384).

> **Stacks 0AHS.** An algebraic space over `S` is separated if and only if for every pair of
> objects of the big fppf site with affine underlying scheme mapping to it the fibre product has
> affine underlying scheme and the canonical map from the tensor product over `ℤ` of the two
> rings of global sections to the ring of global sections of the fibre product is surjective.
>
> Necessity: the morphism from the fibre product to the product `U ×_{Spec ℤ} V` is a base change
> of the absolute diagonal, hence a closed immersion; and a closed immersion into a product of
> two affine schemes is exactly an affine source together with a surjective map on global
> sections.
>
> Sufficiency: being a closed immersion is Zariski local at the target, so the diagonal need only
> be tested on objects of the site with affine underlying scheme, and over such an object the
> criterion applies to the two morphisms the test factors through.

```lean
theorem isAbsolutelySeparated_iff_hasAffineIntersections
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X) :
    IsAbsolutelySeparated B S hS hZ X ↔ HasAffineIntersections B S hS X
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 66.3, Tag 03BR](https://stacks.math.columbia.edu/tag/03BR)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
