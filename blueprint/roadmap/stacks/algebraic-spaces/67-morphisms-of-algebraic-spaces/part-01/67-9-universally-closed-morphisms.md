---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.presheaf_universallyClosed_iff, AlgebraicGeometry.Space.IsClosedMorphism, AlgebraicGeometry.Space.UniversallyClosed, AlgebraicGeometry.Space.universallyClosed_pullback, AlgebraicGeometry.Space.isClosedMorphism_comp, AlgebraicGeometry.Space.universallyClosed_comp, AlgebraicGeometry.Space.universallyClosed_tfae, AlgebraicGeometry.AffineLineTranslation.structureMap
statement: formalized
proof: formalized
---

# 67.9 Universally closed morphisms

Section 67.9 of the Stacks Project, [Tag 03HH](https://stacks.math.columbia.edu/tag/03HH). 8 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03XD, a lemma

[Tag 03XD](https://stacks.math.columbia.edu/tag/03XD) in the Stacks Project.

**`AlgebraicGeometry.Space.presheaf_universallyClosed_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversallyClosedRepresentable.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversallyClosedRepresentable.lean#L265).

> **Stacks 03XD.** A representable morphism of algebraic spaces over `S` is universally
> closed in the sense of Stacks 03HI exactly when each of its represented base changes is a
> universally closed morphism of schemes.

```lean
theorem presheaf_universallyClosed_iff
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) {f : X ⟶ Y}
    (hf : yoneda.relativelyRepresentable f) :
    (MorphismProperty.inverseImage
      (@AlgebraicGeometry.UniversallyClosed.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf f ↔ UniversallyClosed B S hS f
```

## Tag 03HI, a definition

[Tag 03HI](https://stacks.math.columbia.edu/tag/03HI) in the Stacks Project.

**`AlgebraicGeometry.Space.IsClosedMorphism`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversallyClosed.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversallyClosed.lean#L117). The attribute's comment: “closed”.

> A morphism of algebraic spaces over `S` is *closed* when the map it induces on points is a
> closed map for the topology detected by scheme-valued points.

```lean
abbrev IsClosedMorphism (f : F ⟶ G) : Prop
```

**`AlgebraicGeometry.Space.UniversallyClosed`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversallyClosed.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversallyClosed.lean#L125). The attribute's comment: “universally closed”.

> A morphism of algebraic spaces over `S` is *universally closed* when its base change along
> every morphism to its target from an algebraic space over `S` is closed.

```lean
abbrev UniversallyClosed (f : F ⟶ G) : Prop
```

## Tag 03IS, a lemma

[Tag 03IS](https://stacks.math.columbia.edu/tag/03IS) in the Stacks Project.

**`AlgebraicGeometry.Space.universallyClosed_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SeparationMorphismProperties.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SeparationMorphismProperties.lean#L143).

> A base change of a universally closed morphism of algebraic spaces over `S` is universally
> closed.

```lean
theorem universallyClosed_pullback {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (f : X ⟶ Y) (g : Z ⟶ Y) (hf : UniversallyClosed B S hS f) :
    UniversallyClosed B S hS (pullback.fst g f)
```

## Tag 03IU, a lemma

[Tag 03IU](https://stacks.math.columbia.edu/tag/03IU) in the Stacks Project.

**`AlgebraicGeometry.Space.isClosedMorphism_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SeparationMorphismProperties.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SeparationMorphismProperties.lean#L129). The attribute's comment: “closed”.

> A composition of closed morphisms of algebraic spaces over `S` is closed.

```lean
theorem isClosedMorphism_comp {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (f : X ⟶ Y) (g : Y ⟶ Z) (hf : IsClosedMorphism B S hS f)
    (hg : IsClosedMorphism B S hS g) :
    IsClosedMorphism B S hS (f ≫ g)
```

**`AlgebraicGeometry.Space.universallyClosed_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SeparationMorphismProperties.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SeparationMorphismProperties.lean#L158). The attribute's comment: “universally closed”.

> A composition of universally closed morphisms of algebraic spaces over `S` is universally
> closed.

```lean
theorem universallyClosed_comp {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hY : IsAlgebraicSpace B S hS Y) (hZ : IsAlgebraicSpace B S hS Z)
    (f : X ⟶ Y) (g : Y ⟶ Z) (hf : UniversallyClosed B S hS f)
    (hg : UniversallyClosed B S hS g) :
    UniversallyClosed B S hS (f ≫ g)
```

## Tag 03IT, a lemma

[Tag 03IT](https://stacks.math.columbia.edu/tag/03IT) in the Stacks Project.

**`AlgebraicGeometry.Space.universallyClosed_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyClosed.lean, line 427](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyClosed.lean#L427).

> **Stacks 03IT.** For a morphism `f : X ⟶ Y` of algebraic spaces over `S` the following are
> equivalent: `f` is universally closed; the base change of `f` along every morphism to `Y` from
> a presheaf represented by an object of the site is closed; the same for the objects with affine
> underlying scheme; the base change of `f` along some surjective étale morphism to `Y` from a
> represented presheaf is universally closed; and there is a Zariski covering of `Y` along each
> member of which the base change of `f` is universally closed.
>
> Algebraicity of the source is retained from the source statement and is not used.

```lean
theorem universallyClosed_tfae (_hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    List.TFAE
      [UniversallyClosed B S hS f,
        ∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ Y),
          IsClosedMorphism B S hS (pullback.fst g f),
        ∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ Y),
          IsAffine ((BigFppfOver.toScheme B S hS).obj Z) →
            IsClosedMorphism B S hS (pullback.fst g f),
        ∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y),
          IsSurjective B S hS g ∧ IsEtale B S hS g ∧
            UniversallyClosed B S hS (pullback.fst g f),
        ∃ (I : Type u) (U : I → Subfunctor Y) (_ : IsZariskiCover B S hS I U),
          ∀ i, UniversallyClosed B S hS (pullback.fst (U i).ι f)]
```

## Tag 03IV, an example

[Tag 03IV](https://stacks.math.columbia.edu/tag/03IV) in the Stacks Project.

**`AlgebraicGeometry.AffineLineTranslation.structureMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyClosed.lean, line 1342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyClosed.lean#L1342). The attribute's comment: “the structure morphism”.

> **Stacks 03IV.** The structure morphism of the quotient `𝔸¹_k/ℤ` of Stacks 02Z7, the unique
> morphism to the terminal object `Spec k` of the big fppf site over `Spec k`.

```lean
noncomputable def structureMap :
    translationQuotient k B hS hU ⟶ yoneda.obj (Over.mk (𝟙 (B.obj hS)))
```

**`AlgebraicGeometry.AffineLineTranslation.universallyClosed_structureMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyClosed.lean, line 1440](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyClosed.lean#L1440). The attribute's comment: “universally closed”.

> **Stacks 03IV.** For a field `k` of characteristic zero the structure morphism of the
> quotient `𝔸¹_k/ℤ` of Stacks 02Z7 to `Spec k` is universally closed.
>
> The source calls this a strange example because the quotient is, by Stacks 02Z7, an algebraic
> space which is not a scheme. The statement needs no hypothesis beyond characteristic zero — in
> particular none of the effective fppf descent of Stacks 0265, which the representability of the
> quotient's chart does need.

```lean
theorem universallyClosed_structureMap [CharZero k] :
    Space.UniversallyClosed B (Spec (.of k)) hS (structureMap k B hS hU)
```

## Tag 04XW, a lemma

[Tag 04XW](https://stacks.math.columbia.edu/tag/04XW) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasiCompact_of_universallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyClosed.lean, line 670](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyClosed.lean#L670).

> **Stacks 04XW.** A universally closed morphism of algebraic spaces over `S` is
> quasi-compact.

```lean
theorem isQuasiCompact_of_universallyClosed
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hF : IsAlgebraicSpace B S hS F)
    (hG : IsAlgebraicSpace B S hS G) (f : F ⟶ G) (hf : UniversallyClosed B S hS f) :
    IsQuasiCompact B S hS f
```

## Tag 05Z2, a lemma

[Tag 05Z2](https://stacks.math.columbia.edu/tag/05Z2) in the Stacks Project.

**`AlgebraicGeometry.Space.isSeparated_of_isSurjective_of_universallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyClosed.lean, line 695](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyClosed.lean#L695). The attribute's comment: “part (4): separated over the base”.

> **Stacks 05Z2, part (4).** Let `X ⟶ Y ⟶ T` be morphisms of algebraic spaces over `S`, with
> `X ⟶ Y` surjective and universally closed. If `X` is separated over `T`, then so is `Y`.

```lean
theorem isSeparated_of_isSurjective_of_universallyClosed
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hT : IsAlgebraicSpace B S hS T) (f : X ⟶ Y) (g : Y ⟶ T)
    (hfsurj : IsSurjective B S hS f) (hfclosed : UniversallyClosed B S hS f)
    (hsep : IsSeparated B S hS (f ≫ g)) :
    IsSeparated B S hS g
```

**`AlgebraicGeometry.Space.isQuasiSeparated_of_isSurjective_of_universallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyClosed.lean, line 753](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyClosed.lean#L753). The attribute's comment: “part (3): quasi-separated over the base”.

> **Stacks 05Z2, part (3).** Let `X ⟶ Y ⟶ T` be morphisms of algebraic spaces over `S`, with
> `X ⟶ Y` surjective and universally closed. If `X` is quasi-separated over `T`, then so is `Y`.

```lean
theorem isQuasiSeparated_of_isSurjective_of_universallyClosed
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hT : IsAlgebraicSpace B S hS T) (f : X ⟶ Y) (g : Y ⟶ T)
    (hfsurj : IsSurjective B S hS f) (hfclosed : UniversallyClosed B S hS f)
    (hqs : IsQuasiSeparated B S hS (f ≫ g)) :
    IsQuasiSeparated B S hS g
```

**`AlgebraicGeometry.Space.isAbsolutelyQuasiSeparated_of_isSurjective_of_universallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyClosed.lean, line 952](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyClosed.lean#L952). The attribute's comment: “part (1): quasi-separated”.

> **Stacks 05Z2, part (1).** Let `X ⟶ Y` be a surjective universally closed morphism of
> algebraic spaces over `S`. If `X` is quasi-separated, then so is `Y`.
>
> This is part (3) over the terminal scheme, as the source says: quasi-separatedness of an
> algebraic space is quasi-separatedness over `Spec ℤ` of its lower-shriek extension along
> `S ⟶ Spec ℤ`, by Stacks 03BS, and that extension of `X ⟶ Y` is again surjective and universally
> closed by `AlgebraicGeometry.Space.isSurjective_relocalize` and
> `AlgebraicGeometry.Space.universallyClosed_relocalize`.

```lean
theorem isAbsolutelyQuasiSeparated_of_isSurjective_of_universallyClosed
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hfsurj : IsSurjective B S hS f) (hfclosed : UniversallyClosed B S hS f)
    (hqs : IsAbsolutelyQuasiSeparated B S hS hZ X) :
    IsAbsolutelyQuasiSeparated B S hS hZ Y
```

**`AlgebraicGeometry.Space.isAbsolutelySeparated_of_isSurjective_of_universallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyClosed.lean, line 974](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyClosed.lean#L974). The attribute's comment: “part (2): separated”.

> **Stacks 05Z2, part (2).** Let `X ⟶ Y` be a surjective universally closed morphism of
> algebraic spaces over `S`. If `X` is separated, then so is `Y`.
>
> This is part (4) over the terminal scheme, as the source says: separatedness of an algebraic
> space is separatedness over `Spec ℤ` of its lower-shriek extension along `S ⟶ Spec ℤ`, by
> Stacks 03BS, and that extension of `X ⟶ Y` is again surjective and universally closed by
> `AlgebraicGeometry.Space.isSurjective_relocalize` and
> `AlgebraicGeometry.Space.universallyClosed_relocalize`.

```lean
theorem isAbsolutelySeparated_of_isSurjective_of_universallyClosed
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hfsurj : IsSurjective B S hS f) (hfclosed : UniversallyClosed B S hS f)
    (hsep : IsAbsolutelySeparated B S hS hZ X) :
    IsAbsolutelySeparated B S hS hZ Y
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.9, Tag 03HH](https://stacks.math.columbia.edu/tag/03HH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
