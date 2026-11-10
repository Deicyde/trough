---
declaration: section
origin: cited
lean: CategoryTheory.Mono, AlgebraicGeometry.Space.mono_hom_iff_mono, AlgebraicGeometry.Space.mono_iff_isIso_diagonal, AlgebraicGeometry.Space.isSeparated_of_mono, CategoryTheory.mono_comp, CategoryTheory.MorphismProperty.IsStableUnderBaseChange.monomorphisms, AlgebraicGeometry.Space.mono_tfae, AlgebraicGeometry.Space.mono_of_isImmersion
statement: formalized
proof: formalized
---

# 67.10 Monomorphisms

Section 67.10 of the Stacks Project, [Tag 042K](https://stacks.math.columbia.edu/tag/042K). 9 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 042L, a definition

[Tag 042L](https://stacks.math.columbia.edu/tag/042L) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Mono`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Mono#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fold5/Monomorphisms.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fold5/Monomorphisms.lean#L63) (StacksFrontier). References: EGA IV (8.11.5.1); SGA 1 V (3.6); SGA 3 VIIB (2.4.1); SGA 3 VIII (3.4); SGA 4 I (10.4); SGA 4 II (3.2).

## Tag 042M, a lemma

[Tag 042M](https://stacks.math.columbia.edu/tag/042M) in the Stacks Project.

**`AlgebraicGeometry.Space.mono_hom_iff_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Monomorphisms.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Monomorphisms.lean#L213). The attribute's comment: “parts (1) and (2)”.

> **Stacks 042M, parts (1) and (2).** A morphism of algebraic spaces over `S` is a
> monomorphism of the underlying presheaves exactly when it is a monomorphism of the category
> of algebraic spaces over `S`.

```lean
theorem mono_hom_iff_mono {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) :
    Mono f.hom ↔ Mono f
```

**`AlgebraicGeometry.Space.mono_iff_isIso_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Monomorphisms.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Monomorphisms.lean#L227). The attribute's comment: “parts (2) and (3)”. References: EGA I (5.3.8).

> **Stacks 042M, parts (2) and (3).** A morphism of algebraic spaces over `S` is a
> monomorphism of the category of algebraic spaces over `S` exactly when its relative diagonal
> is an isomorphism.

```lean
theorem mono_iff_isIso_diagonal {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) :
    Mono f ↔ IsIso (pullback.diagonal f)
```

## Tag 042N, a lemma

[Tag 042N](https://stacks.math.columbia.edu/tag/042N) in the Stacks Project.

**`AlgebraicGeometry.Space.isSeparated_of_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SeparatedQuasiFiniteEtaleDescent.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SeparatedQuasiFiniteEtaleDescent.lean#L218).

> **Stacks 042N.** A monomorphism of presheaves on the big fppf site of `S` is a separated
> morphism of algebraic spaces over `S`: its relative diagonal is an isomorphism, and an
> isomorphism is a closed immersion. The statement is made for an arbitrary morphism of presheaves
> on the big fppf site of `S`; no algebraic-space hypothesis is used.
>
> This strictly generalises `AlgebraicGeometry.Space.isSeparated_of_isIso`, which is the same
> statement for an isomorphism.

```lean
theorem isSeparated_of_mono {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (m : F ⟶ G) (hm : Mono m) :
    IsSeparated B S hS m
```

**`AlgebraicGeometry.Space.isSeparated_of_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeDiagonalMonomorphism.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeDiagonalMonomorphism.lean#L148).

> **Stacks 042N.** A monomorphism of algebraic spaces over `S` is separated: its relative
> diagonal is an isomorphism, and an isomorphism is a closed immersion.
>
> The statement is made for an arbitrary morphism of presheaves on the big fppf site of `S`; no
> algebraic-space hypothesis is used.

```lean
theorem isSeparated_of_mono {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (g : F ⟶ G) (hg : Mono g) :
    IsSeparated B S hS g
```

## Tag 042O, a lemma

[Tag 042O](https://stacks.math.columbia.edu/tag/042O) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.mono_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.mono_comp#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fold5/Monomorphisms.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fold5/Monomorphisms.lean#L64) (StacksFrontier).

## Tag 042P, a lemma

[Tag 042P](https://stacks.math.columbia.edu/tag/042P) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.MorphismProperty.IsStableUnderBaseChange.monomorphisms`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.MorphismProperty.IsStableUnderBaseChange.monomorphisms#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fold5/Monomorphisms.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fold5/Monomorphisms.lean#L65) (StacksFrontier). References: EGA I (3.3.12), “more general”; EGA IV (2.7.1), “(ix)”; SGA 3 IV (4.5.7), “more general”; SGA 3 VIB (10.1), “monomorphisms”.

## Tag 042Q, a lemma

[Tag 042Q](https://stacks.math.columbia.edu/tag/042Q) in the Stacks Project.

**`AlgebraicGeometry.Space.mono_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Monomorphisms.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Monomorphisms.lean#L239).

> **Stacks 042Q.** For a morphism `f : X ⟶ Y` of algebraic spaces over `S` the following are
> equivalent: `f` is a monomorphism; every base change of `f` to a scheme of the site is a
> monomorphism; every base change of `f` to an affine scheme of the site is a monomorphism; the
> base change of `f` along some surjective étale chart of `Y` is a monomorphism; and the base
> changes of `f` along the members of some Zariski covering of `Y` are monomorphisms.

```lean
theorem mono_tfae {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    List.TFAE [
      Mono f,
      (∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ Y), Mono (pullback.snd f g)),
      (∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ Y),
        IsAffine ((BigFppfOver.toScheme B S hS).obj Z) → Mono (pullback.snd f g)),
      (∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y),
        IsSurjective B S hS g ∧ IsEtale B S hS g ∧ Mono (pullback.snd f g)),
      (∃ (I : Type u) (U : I → Subfunctor Y),
        IsZariskiCover B S hS I U ∧ ∀ i, Mono (pullback.snd f (U i).ι))]
```

## Tag 042R, a lemma

[Tag 042R](https://stacks.math.columbia.edu/tag/042R) in the Stacks Project.

**`AlgebraicGeometry.Space.mono_of_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Monomorphisms.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Monomorphisms.lean#L306). The attribute's comment: “monomorphism”.

> **Stacks 042R.** An immersion of algebraic spaces over `S` is a monomorphism: an immersion
> of schemes is a monomorphism, and a morphism of presheaves all of whose represented base
> changes are monomorphisms is a monomorphism.

```lean
theorem mono_of_isImmersion {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : F ⟶ G}
    (hf : IsImmersion B S hS f) : Mono f
```

**`AlgebraicGeometry.Space.isSeparated_of_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Monomorphisms.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Monomorphisms.lean#L322). The attribute's comment: “separatedness”. References: EGA I (5.5.1), “(i) immersions”.

> **Stacks 042R.** An immersion of algebraic spaces over `S` is separated: it is a
> monomorphism, so its relative diagonal is an isomorphism, and an isomorphism of presheaves is
> a closed immersion.

```lean
theorem isSeparated_of_isImmersion {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : F ⟶ G}
    (hf : IsImmersion B S hS f) : IsSeparated B S hS f
```

## Tag 06MG, a lemma

[Tag 06MG](https://stacks.math.columbia.edu/tag/06MG) in the Stacks Project.

**`AlgebraicGeometry.Space.isEmpty_points_or_isIso_of_mono_to_spec_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MonoToZeroDimensionalLocalSpectra.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/MonoToZeroDimensionalLocalSpectra.lean#L235).

> **Stacks 06MG.** A monomorphism of algebraic spaces over `S` whose target is the spectrum
> of a field `k` is either a morphism out of an algebraic space with no points, or an
> isomorphism.
>
> A field is a zero-dimensional local ring, so the source is a scheme by Stacks 06RZ, and the
> dichotomy is then the scheme-level one.

```lean
theorem isEmpty_points_or_isIso_of_mono_to_spec_field
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hF : IsAlgebraicSpace B S hS F) (f : F ⟶ G)
    [Mono f] (Y : BigFppfOver B S hS) (eG : G ≅ yoneda.obj Y) (k : Type u) [Field k]
    (eY : (BigFppfOver.toScheme B S hS).obj Y ≅ Spec (.of k)) :
    IsEmpty (points B S hS F) ∨ IsIso f
```

## Tag 06RV, a lemma

[Tag 06RV](https://stacks.math.columbia.edu/tag/06RV) in the Stacks Project.

**`AlgebraicGeometry.Space.pointsMap_injective_of_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsMono.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsMono.lean#L67).

> **Stacks 06RV.** A monomorphism induces an injective map on equivalence classes of
> field-valued points.

```lean
theorem pointsMap_injective_of_mono
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (f : F ⟶ G) [Mono f] :
    Function.Injective (pointsMap B S hS F f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.10, Tag 042K](https://stacks.math.columbia.edu/tag/042K)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
