---
declaration: section
origin: cited
lean: AlgebraicGeometry.pseudoCoherent_tfae, AlgebraicGeometry.locallyOfFinitePresentation_of_pseudoCoherent, AlgebraicGeometry.pseudoCoherent_tfae_three, AlgebraicGeometry.PseudoCoherent, AlgebraicGeometry.pseudoCoherent_of_isPullback_of_flat, AlgebraicGeometry.pseudoCoherent_comp, AlgebraicGeometry.pseudoCoherent_of_flat_of_locallyOfFinitePresentation, AlgebraicGeometry.pseudoCoherent_of_comp
statement: formalized
proof: formalized
---

# 37.60 Pseudo-coherent morphisms

Section 37.60 of the Stacks Project, [Tag 067X](https://stacks.math.columbia.edu/tag/067X). 13 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 067Y, a lemma

[Tag 067Y](https://stacks.math.columbia.edu/tag/067Y) in the Stacks Project.

**`AlgebraicGeometry.pseudoCoherent_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/PseudoCoherent.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/PseudoCoherent.lean#L114). The attribute's comment: “the equivalence of (1) and (2)”.

> For a morphism of schemes the following are equivalent: there is an affine open cover of the
> base and, over each of its members, an affine open cover of its inverse image on which the maps on
> sections are pseudo-coherent ring maps; and every compatible pair of affine opens has
> pseudo-coherent map on sections.

```lean
public theorem pseudoCoherent_tfae {X S : Scheme.{u}} (f : X ⟶ S) :
    let pseudoCoherentOn := fun (V : S.Opens) (U : X.Opens)
        (h : U ≤ f ⁻¹ᵁ V) ↦
      letI : Algebra Γ(S, V) Γ(X, U) := (f.appLE V U h).hom.toAlgebra
      Algebra.PseudoCoherent Γ(S, V) Γ(X, U)
    List.TFAE [
      ∃ (J : Type u) (V : J → S.Opens),
        IsOpenCover V ∧
          (∀ j, IsAffineOpen (V j)) ∧
          ∀ j, ∃ (I : Type u) (U : I → X.Opens)
            (hU : (⨆ i, U i) = f ⁻¹ᵁ (V j)),
            (∀ i, IsAffineOpen (U i)) ∧
              ∀ i, pseudoCoherentOn (V j) (U i)
                ((le_iSup U i).trans hU.le),
      ∀ (U : X.Opens), IsAffineOpen U →
        ∀ (V : S.Opens), IsAffineOpen V →
          ∀ (h : U ≤ f ⁻¹ᵁ V), pseudoCoherentOn V U h]
```

**`AlgebraicGeometry.locallyOfFinitePresentation_of_pseudoCoherent`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/PseudoCoherent.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/PseudoCoherent.lean#L162). The attribute's comment: “condition (2) implies the finite-type half of condition (3)”.

> **Stacks 0682.** A pseudo-coherent morphism of schemes is locally of finite presentation.
>
> On every compatible pair of affine opens the map on sections is a pseudo-coherent ring map,
> hence of finite presentation by `RingHom.PseudoCoherent.finitePresentation`.
>
> Followed by Mathlib's instance from `AlgebraicGeometry.LocallyOfFinitePresentation` to
> `AlgebraicGeometry.LocallyOfFiniteType`, this is how type class search finds that a
> pseudo-coherent morphism is locally of finite type, the clause of Stacks 067Y recorded by the
> second tag.

```lean
public instance (priority := 100) locallyOfFinitePresentation_of_pseudoCoherent {X S : Scheme.{u}}
    (f : X ⟶ S) [hf : PseudoCoherent f] : LocallyOfFinitePresentation f
```

**`AlgebraicGeometry.pseudoCoherent_tfae_three`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/StructureSheafComparison.lean, line 442](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PseudoCoherent/StructureSheafComparison.lean#L442). The attribute's comment: “the full three-condition equivalence”.

> **Stacks 067Y.** For a morphism of schemes `f : X ⟶ S` the following are equivalent: there
> are an affine open covering of `S` and, over each of its members, an affine open covering of its
> inverse image on which the maps on sections are pseudo-coherent ring maps; the map on sections is
> pseudo-coherent at every compatible pair of affine opens; and `f` is locally of finite type with
> `𝒪_X` pseudo-coherent relative to `S`.
>
> The equivalence of the first two conditions is `AlgebraicGeometry.pseudoCoherent_tfae`, and the
> third enters through `AlgebraicGeometry.relativeStructureSheafComparison`. This declaration states
> the whole of the source's lemma, so it subsumes the two clauses of it tagged in
> `StacksFrontier/AlgebraicGeometry/Morphisms/PseudoCoherent.lean`.

```lean
public theorem pseudoCoherent_tfae_three :
    let pseudoCoherentOn := fun (V : S.Opens) (U : X.Opens)
        (h : U ≤ f ⁻¹ᵁ V) ↦
      letI : Algebra Γ(S, V) Γ(X, U) := (f.appLE V U h).hom.toAlgebra
      Algebra.PseudoCoherent Γ(S, V) Γ(X, U)
    List.TFAE [
      ∃ (J : Type u) (V : J → S.Opens),
        IsOpenCover V ∧
          (∀ j, IsAffineOpen (V j)) ∧
          ∀ j, ∃ (I : Type u) (U : I → X.Opens)
            (hU : (⨆ i, U i) = f ⁻¹ᵁ (V j)),
            (∀ i, IsAffineOpen (U i)) ∧
              ∀ i, pseudoCoherentOn (V j) (U i)
                ((le_iSup U i).trans hU.le),
      ∀ (U : X.Opens), IsAffineOpen U →
        ∀ (V : S.Opens), IsAffineOpen V →
          ∀ (h : U ≤ f ⁻¹ᵁ V), pseudoCoherentOn V U h,
      ∃ hft : LocallyOfFiniteType f,
        letI := hft
        Scheme.Hom.IsModulePseudoCoherent f (SheafOfModules.unit X.ringCatSheaf)]
```

## Tag 067Z, a definition

[Tag 067Z](https://stacks.math.columbia.edu/tag/067Z) in the Stacks Project.

**`AlgebraicGeometry.PseudoCoherent`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/PseudoCoherent.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/PseudoCoherent.lean#L71).

> A morphism of schemes `f : X ⟶ S` is pseudo-coherent if for every affine open `V ⊆ S` and every
> affine open `U ⊆ X` with `U ⊆ f ⁻¹ᵁ V` the induced map on sections `Γ(S, V) ⟶ Γ(X, U)` is a
> pseudo-coherent ring map.

```lean
public class PseudoCoherent {X S : Scheme.{u}} (f : X ⟶ S) : Prop
```

## Tag 0680, a lemma

[Tag 0680](https://stacks.math.columbia.edu/tag/0680) in the Stacks Project.

**`AlgebraicGeometry.pseudoCoherent_of_isPullback_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentMorphism/FlatBaseChange.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentMorphism/FlatBaseChange.lean#L160).

> **Stacks 0680.** A flat base change of a pseudo-coherent morphism of schemes is
> pseudo-coherent: if `f : X ⟶ S` is pseudo-coherent, `g : S' ⟶ S` is flat and the square with
> sides `g' : X' ⟶ X` and `f' : X' ⟶ S'` is cartesian, then `f'` is pseudo-coherent.

```lean
theorem pseudoCoherent_of_isPullback_of_flat {X X' S S' : Scheme.{u}} {f : X ⟶ S} {g : S' ⟶ S}
    {g' : X' ⟶ X} {f' : X' ⟶ S'} (sq : IsPullback g' f' f g) [Flat g] [PseudoCoherent f] :
    PseudoCoherent f'
```

## Tag 0681, a lemma

[Tag 0681](https://stacks.math.columbia.edu/tag/0681) in the Stacks Project.

**`AlgebraicGeometry.pseudoCoherent_comp`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentMorphism/Composition.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentMorphism/Composition.lean#L82).

> **Stacks 0681.** A composition of pseudo-coherent morphisms of schemes is pseudo-coherent.

```lean
instance pseudoCoherent_comp {X Y Z : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ Z)
    [hf : PseudoCoherent f] [hg : PseudoCoherent g] : PseudoCoherent (f ≫ g)
```

## Tag 0682, a lemma

[Tag 0682](https://stacks.math.columbia.edu/tag/0682) in the Stacks Project.

**`AlgebraicGeometry.locallyOfFinitePresentation_of_pseudoCoherent`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/PseudoCoherent.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/PseudoCoherent.lean#L162).

> **Stacks 0682.** A pseudo-coherent morphism of schemes is locally of finite presentation.
>
> On every compatible pair of affine opens the map on sections is a pseudo-coherent ring map,
> hence of finite presentation by `RingHom.PseudoCoherent.finitePresentation`.
>
> Followed by Mathlib's instance from `AlgebraicGeometry.LocallyOfFinitePresentation` to
> `AlgebraicGeometry.LocallyOfFiniteType`, this is how type class search finds that a
> pseudo-coherent morphism is locally of finite type, the clause of Stacks 067Y recorded by the
> second tag.

```lean
public instance (priority := 100) locallyOfFinitePresentation_of_pseudoCoherent {X S : Scheme.{u}}
    (f : X ⟶ S) [hf : PseudoCoherent f] : LocallyOfFinitePresentation f
```

## Tag 0695, a lemma

[Tag 0695](https://stacks.math.columbia.edu/tag/0695) in the Stacks Project.

**`AlgebraicGeometry.pseudoCoherent_of_flat_of_locallyOfFinitePresentation`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentMorphism/FinitePresentation.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentMorphism/FinitePresentation.lean#L57).

> **Stacks 0695.** A flat morphism of schemes which is locally of finite presentation is
> pseudo-coherent.
>
> On every compatible pair of affine opens the map on sections is flat and of finite presentation,
> hence pseudo-coherent by `RingHom.PseudoCoherent.of_flat_of_finitePresentation`, the
> pseudo-coherence half of Stacks 067J.

```lean
instance pseudoCoherent_of_flat_of_locallyOfFinitePresentation {X S : Scheme.{u}} (f : X ⟶ S)
    [Flat f] [LocallyOfFinitePresentation f] : PseudoCoherent f
```

## Tag 0683, a lemma

[Tag 0683](https://stacks.math.columbia.edu/tag/0683) in the Stacks Project.

**`AlgebraicGeometry.pseudoCoherent_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentMorphism/Composition.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentMorphism/Composition.lean#L95). References: SGA 6 III (1.14), “special case”.

> **Stacks 0683.** If `X` and `Y` are pseudo-coherent over a base scheme `S`, then any morphism
> `f : X ⟶ Y` over `S` is pseudo-coherent.
>
> Pseudo-coherence of `f` is checked around a point `x` of `X` on an affine open `U ∋ x` of `X`
> contained in the preimage of an affine open `V` of `Y`, itself contained in the preimage of an
> affine open `W` of `S`. The map `Γ(S, W) ⟶ Γ(X, U)` is the composite of `Γ(S, W) ⟶ Γ(Y, V)` with
> `Γ(Y, V) ⟶ Γ(X, U)`, and the outer two are pseudo-coherent by hypothesis, so the algebra
> cancellation lemma applies.

```lean
theorem pseudoCoherent_of_comp {X Y S : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ S)
    [PseudoCoherent (f ≫ g)] [PseudoCoherent g] : PseudoCoherent f
```

## Tag 0AVX, a lemma

[Tag 0AVX](https://stacks.math.columbia.edu/tag/0AVX) in the Stacks Project.

**`AlgebraicGeometry.Scheme.isPseudoCoherentSite_pushforward_derivedStructureSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportSitePseudoCoherent.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportSitePseudoCoherent.lean#L55). The attribute's comment: “for a closed immersion, at the site notion of pseudo-coherence”.

> If a closed immersion of schemes `i : Z ⟶ X` is pseudo-coherent, then `Ri_* 𝒪_Z` is a
> pseudo-coherent object of `D(𝒪_X)` at the ringed site of opens of `X`, in the sense of
> [Stacks, Tag 08FT].

```lean
theorem isPseudoCoherentSite_pushforward_derivedStructureSheaf (hi : PseudoCoherent i) :
    (Stacks.SheafOfModules.ringedSite X.sheaf).IsPseudoCoherent
      ((modulePushforward
        (Stacks.ClosedImmersion.closedQuotientOfClosedImmersion i).i).mapDerivedCategory.obj
          (RingedSite.derivedStructureSheaf (Stacks.SheafOfModules.ringedSite Z.sheaf)))
```

**`AlgebraicGeometry.pseudoCoherent_iff_isPseudoCoherent_pushforward_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentMorphism/FiniteMorphism.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentMorphism/FiniteMorphism.lean#L144).

> **Stacks 0AVX.** A finite morphism of schemes `f : X ⟶ S` is pseudo-coherent if and only if
> the direct image `f_*𝒪_X` of its structure sheaf is a pseudo-coherent `𝒪_S`-module, that is, if
> and only if the object of `D(𝒪_S)` it determines in degree zero is pseudo-coherent.

```lean
public theorem pseudoCoherent_iff_isPseudoCoherent_pushforward_unit {X S : Scheme.{u}} (f : X ⟶ S)
    [IsFinite f] :
    PseudoCoherent f ↔
      RingedSpace.IsPseudoCoherent (X := S.toRingedSpace)
        ((DerivedCategory.singleFunctor S.Modules 0).obj
          ((Scheme.Modules.pushforward f).obj (SheafOfModules.unit X.ringCatSheaf)))
```

## Tag 0684, a lemma

[Tag 0684](https://stacks.math.columbia.edu/tag/0684) in the Stacks Project.

**`AlgebraicGeometry.pseudoCoherent_iff_locallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentMorphism/Noetherian.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentMorphism/Noetherian.lean#L76). References: SGA 6 III (1.3), “loc. noetherian case”.

> **Stacks 0684.** A morphism of schemes whose target is locally Noetherian is pseudo-coherent
> if and only if it is locally of finite type.
>
> A pseudo-coherent morphism is always locally of finite type. Conversely, over a locally
> Noetherian base the sections over an affine open form a Noetherian ring, so every map on sections
> over a compatible pair of affine opens is a finite-type ring map out of a Noetherian ring, hence
> pseudo-coherent by Stacks 067I.

```lean
theorem pseudoCoherent_iff_locallyOfFiniteType {X S : Scheme.{u}} [IsLocallyNoetherian S]
    (f : X ⟶ S) : PseudoCoherent f ↔ LocallyOfFiniteType f
```

## Tag 0696, a lemma

[Tag 0696](https://stacks.math.columbia.edu/tag/0696) in the Stacks Project.

**`AlgebraicGeometry.pseudoCoherent_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentMorphism/FpqcLocalAtTarget.lean, line 347](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentMorphism/FpqcLocalAtTarget.lean#L347).

> **Stacks 0696.** Pseudo-coherence of a morphism of schemes is fpqc local on the base: a
> morphism is pseudo-coherent if and only if its base change along every member of an fpqc
> covering of its target is pseudo-coherent.
>
> Both implications are part of `CategoryTheory.MorphismProperty.IsLocalAtTarget`; they are spelled
> out as a single `Iff` by `AlgebraicGeometry.pseudoCoherent_iff_of_fpqcCover`.

```lean
instance pseudoCoherent_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget (@PseudoCoherent : MorphismProperty Scheme.{u})
      Scheme.fpqcPrecoverage
```

## Tag 0697, a lemma

[Tag 0697](https://stacks.math.columbia.edu/tag/0697) in the Stacks Project.

**`Algebra.pseudoCoherent_quotient_iff_isModulePseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/PseudoCoherentMap/Quotient.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/PseudoCoherentMap/Quotient.lean#L123).

> **Stacks 0697.** Let `A → B` be a flat ring map of finite presentation and let `I` be an
> ideal of `B`. Then `A → B ⧸ I` is pseudo-coherent if and only if `I` is pseudo-coherent as a
> `B`-module.
>
> Pseudo-coherence of `A → B ⧸ I` is pseudo-coherence of `B ⧸ I` relative to `A`; Stacks 0673
> restricts that along the finite map `B → B ⧸ I`, Stacks 0DHQ makes it absolute over `B` because
> `A → B` is itself pseudo-coherent by Stacks 067J, and Stacks 064V exchanges `B ⧸ I` for `I`.

```lean
theorem pseudoCoherent_quotient_iff_isModulePseudoCoherent
    {A B : Type u} [CommRing A] [CommRing B] [Algebra A B] [Module.Flat A B]
    [Algebra.FinitePresentation A B] (I : Ideal B) :
    Algebra.PseudoCoherent A (B ⧸ I) ↔ IsModulePseudoCoherent (R := B) I
```

## Tag 0698, a lemma

[Tag 0698](https://stacks.math.columbia.edu/tag/0698) in the Stacks Project.

**`AlgebraicGeometry.PseudoCoherent.isLocalAtSource_syntomicPrecoverage`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentMorphism/SyntomicDescent.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentMorphism/SyntomicDescent.lean#L79).

> **Stacks 0698.** Pseudo-coherence of morphisms of schemes is local on the source for the
> syntomic topology.
>
> This is `AlgebraicGeometry.pseudoCoherent_isLocalAtSource_of_affine_descent`, the reduction of
> the source's statement to the case of a surjective syntomic morphism of affine schemes, with
> that case discharged by
> `AlgebraicGeometry.pseudoCoherent_of_comp_surjective_syntomic_of_isAffine`.

```lean
instance PseudoCoherent.isLocalAtSource_syntomicPrecoverage :
    MorphismProperty.IsLocalAtSource (@PseudoCoherent.{u} : MorphismProperty Scheme.{u})
      (Scheme.precoverage (@Syntomic.{u}))
```

## Tag 0699, a lemma

[Tag 0699](https://stacks.math.columbia.edu/tag/0699) in the Stacks Project.

**`AlgebraicGeometry.PseudoCoherent.isLocalAtSource_fppfPrecoverage`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentMorphism/FppfDescent.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentMorphism/FppfDescent.lean#L56).

> **Stacks 0699.** Pseudo-coherence of morphisms of schemes is local on the source for the
> fppf topology: a morphism is pseudo-coherent exactly when its composites with the members of an
> fppf covering of its source are.
>
> This is `AlgebraicGeometry.pseudoCoherent_isLocalAtSource_fppf_of_finiteLocallyFree_descent`,
> the reduction of the source's statement to descent along a surjective finite locally free
> morphism, with that descent discharged by
> `AlgebraicGeometry.pseudoCoherent_of_comp_surjective_finiteLocallyFree`.

```lean
instance PseudoCoherent.isLocalAtSource_fppfPrecoverage :
    MorphismProperty.IsLocalAtSource (@PseudoCoherent.{u} : MorphismProperty Scheme.{u})
      Scheme.fppfPrecoverage
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.60, Tag 067X](https://stacks.math.columbia.edu/tag/067X)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
