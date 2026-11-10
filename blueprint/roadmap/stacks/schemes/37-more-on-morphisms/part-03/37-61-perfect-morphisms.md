---
declaration: section
origin: cited
lean: AlgebraicGeometry.locallyOfFinitePresentation_of_perfect, AlgebraicGeometry.exists_affine_openCover_perfect_iff_forall, AlgebraicGeometry.Perfect, AlgebraicGeometry.perfect_of_isPullback_of_flat, AlgebraicGeometry.perfect_comp, AlgebraicGeometry.flat_and_perfect_iff_flat_and_locallyOfFinitePresentation, AlgebraicGeometry.perfect_of_isRegular, AlgebraicGeometry.perfect_of_isKoszulRegularImmersion
statement: formalized
proof: formalized
---

# 37.61 Perfect morphisms

Section 37.61 of the Stacks Project, [Tag 0685](https://stacks.math.columbia.edu/tag/0685). 15 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0685, the section

[Tag 0685](https://stacks.math.columbia.edu/tag/0685) in the Stacks Project.

**`AlgebraicGeometry.locallyOfFinitePresentation_of_perfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PerfectMorphism/Flat.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PerfectMorphism/Flat.lean#L73). The attribute's comment: “the section's unnumbered assertion that a perfect morphism is pseudo-coherent, hence locally of finite presentation; the fifteen numbered items of the section carry their own tags”.

> **Stacks 0685.** A perfect morphism of schemes is locally of finite presentation: it is
> pseudo-coherent, and a pseudo-coherent morphism is locally of finite presentation by Stacks
> 0682.

```lean
public theorem locallyOfFinitePresentation_of_perfect {X S : Scheme.{u}} (f : X ⟶ S)
    [Perfect f] : LocallyOfFinitePresentation f
```

## Tag 0686, a lemma

[Tag 0686](https://stacks.math.columbia.edu/tag/0686) in the Stacks Project.

**`AlgebraicGeometry.exists_affine_openCover_perfect_iff_forall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PerfectMorphism/AffineLocal.lean, line 554](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PerfectMorphism/AffineLocal.lean#L554).

> For a locally finite type morphism of schemes, perfectness on some affine open covering
> of the target and affine open coverings of its preimages is equivalent to perfectness on every
> pair of affine opens for which the source open maps into the target open.

```lean
theorem exists_affine_openCover_perfect_iff_forall
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f] :
    (∃ (J : Type u) (V : J → S.Opens),
      IsOpenCover V ∧
        (∀ j, IsAffineOpen (V j)) ∧
        ∀ j, ∃ (I : Type u) (U : I → X.Opens)
          (hU : (⨆ i, U i) = f ⁻¹ᵁ (V j)),
          (∀ i, IsAffineOpen (U i)) ∧
            ∀ i,
              let g := (f.appLE (V j) (U i) ((le_iSup U i).trans hU.le)).hom
              letI := g.toAlgebra
              ∀ D : CertifiedDerivedTensoring Γ(S, V j),
                RingHom.IsPerfectRingMap Γ(S, V j) Γ(X, U i)
                  D.tensor D.comparison D.isLeftDerived) ↔
      ∀ (U : X.Opens) (_ : IsAffineOpen U) (V : S.Opens) (_ : IsAffineOpen V)
        (hUV : U ≤ f ⁻¹ᵁ V),
          let g := (f.appLE V U hUV).hom
          letI := g.toAlgebra
          ∀ D : CertifiedDerivedTensoring Γ(S, V),
            RingHom.IsPerfectRingMap Γ(S, V) Γ(X, U)
              D.tensor D.comparison D.isLeftDerived
```

## Tag 0687, a definition

[Tag 0687](https://stacks.math.columbia.edu/tag/0687) in the Stacks Project.

**`AlgebraicGeometry.Perfect`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/Morphism.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/Morphism.lean#L70).

> **Stacks 0687.** A morphism of schemes `f : X ⟶ S` is perfect if it is locally of finite
> type and, for every affine open `U ⊆ X` and every affine open `V ⊆ S` with `U ⊆ f ⁻¹ᵁ V`, the
> induced map on sections `Γ(S, V) ⟶ Γ(X, U)` is a perfect ring map, with respect to every
> certified derived tensor product on `Γ(S, V)`.
>
> This is condition (2) of Stacks 0686, which is the condition Stacks 0687 defines perfectness by.

```lean
public class Perfect {X S : Scheme.{u}} (f : X ⟶ S) : Prop extends LocallyOfFiniteType f
```

## Tag 0688, a lemma

[Tag 0688](https://stacks.math.columbia.edu/tag/0688) in the Stacks Project.

**`AlgebraicGeometry.perfect_of_isPullback_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PerfectMorphism/FlatBaseChange.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PerfectMorphism/FlatBaseChange.lean#L164).

> **Stacks 0688.** A flat base change of a perfect morphism of schemes is perfect: if
> `f : X ⟶ S` is perfect, `g : S' ⟶ S` is flat and the square with sides `g' : X' ⟶ X` and
> `f' : X' ⟶ S'` is cartesian, then `f'` is perfect.

```lean
theorem perfect_of_isPullback_of_flat {X X' S S' : Scheme.{u}} {f : X ⟶ S} {g : S' ⟶ S}
    {g' : X' ⟶ X} {f' : X' ⟶ S'} (sq : IsPullback g' f' f g) [Flat g] [Perfect f] :
    Perfect f'
```

## Tag 0689, a lemma

[Tag 0689](https://stacks.math.columbia.edu/tag/0689) in the Stacks Project.

**`AlgebraicGeometry.perfect_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PerfectMorphism/Composition.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PerfectMorphism/Composition.lean#L146).

> **Stacks Project, Tag 0689.** A composition of perfect morphisms of schemes is perfect.

```lean
public theorem perfect_comp {X Y Z : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ Z)
    [Perfect f] [Perfect g] : Perfect (f ≫ g)
```

## Tag 068A, a lemma

[Tag 068A](https://stacks.math.columbia.edu/tag/068A) in the Stacks Project.

**`AlgebraicGeometry.flat_and_perfect_iff_flat_and_locallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PerfectMorphism/Flat.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PerfectMorphism/Flat.lean#L99).

> **Stacks 068A.** A morphism of schemes is flat and perfect if and only if it is flat and
> locally of finite presentation.
>
> Neither implication uses flatness on the side it starts from: a perfect morphism is always
> locally of finite presentation, through `AlgebraicGeometry.pseudoCoherent_of_perfect` and Stacks
> 0682, and a flat morphism locally of finite presentation is always perfect, through
> `AlgebraicGeometry.perfect_of_flat_of_locallyOfFinitePresentation`.

```lean
public theorem flat_and_perfect_iff_flat_and_locallyOfFinitePresentation {X S : Scheme.{u}}
    (f : X ⟶ S) : (Flat f ∧ Perfect f) ↔ (Flat f ∧ LocallyOfFinitePresentation f)
```

## Tag 068B, a lemma

[Tag 068B](https://stacks.math.columbia.edu/tag/068B) in the Stacks Project.

**`AlgebraicGeometry.perfect_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PerfectMorphism/RegularTarget.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PerfectMorphism/RegularTarget.lean#L54).

> **Stacks 068B.** A morphism of schemes locally of finite type over a regular scheme is
> perfect.

```lean
public theorem perfect_of_isRegular {X S : Scheme.{u}} (f : X ⟶ S) (hS : IsRegular S)
    [LocallyOfFiniteType f] : Perfect f
```

## Tag 068C, a lemma

[Tag 068C](https://stacks.math.columbia.edu/tag/068C) in the Stacks Project.

**`AlgebraicGeometry.perfect_of_isKoszulRegularImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PerfectMorphism/RegularImmersion.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PerfectMorphism/RegularImmersion.lean#L200). The attribute's comment: “Koszul-regular immersion”. References: SGA 6 III (4.1.1), “reg. immersion perfect”; SGA 6 III (1.1.2); SGA 6 VII (1.9), “more general”; SGA 6 VIII (1.7), “special case”; SGA 6 X (7.1), “partial”.

> **Stacks 068C.** A Koszul-regular immersion of schemes is a perfect morphism.
>
> The immersion factors as its closed factor into the canonical open, whose defining ideal sheaf is
> Koszul-regular by definition, followed by an open immersion, which is flat and locally of finite
> presentation and hence perfect by Stacks 068A; perfectness composes by Stacks 0689.

```lean
theorem perfect_of_isKoszulRegularImmersion {X S : Scheme.{u}} (i : X ⟶ S) [IsImmersion i]
    (hi : IsKoszulRegularImmersion i) : Perfect i
```

**`AlgebraicGeometry.perfect_of_isRegularImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PerfectMorphism/RegularImmersion.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PerfectMorphism/RegularImmersion.lean#L213). The attribute's comment: “regular immersion”. References: SGA 6 III (4.1.1), “reg. immersion perfect”; SGA 6 III (1.1.2); SGA 6 VIII (1.7), “special case”; SGA 6 X (7.1), “partial”.

> **Stacks 068C.** A regular immersion of schemes is a perfect morphism, because a regular
> immersion is Koszul-regular by Stacks 063K.

```lean
theorem perfect_of_isRegularImmersion {X S : Scheme.{u}} (i : X ⟶ S) [IsImmersion i]
    (hi : IsRegularImmersion i) : Perfect i
```

## Tag 068D, a lemma

[Tag 068D](https://stacks.math.columbia.edu/tag/068D) in the Stacks Project.

**`AlgebraicGeometry.perfect_of_comp_eq_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PerfectMorphism/SmoothTarget.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PerfectMorphism/SmoothTarget.lean#L68).

> **Stacks 068D.** In a commutative triangle of morphisms of schemes with `f ≫ q = p`, `q`
> smooth and `p` perfect, the morphism `f` is perfect.

```lean
public theorem perfect_of_comp_eq_of_smooth {X Y S : Scheme.{u}} (f : X ⟶ Y) (q : Y ⟶ S)
    {p : X ⟶ S} (hfq : f ≫ q = p) [Smooth q] [Perfect p] : Perfect f
```

## Tag 069B, a lemma

[Tag 069B](https://stacks.math.columbia.edu/tag/069B) in the Stacks Project.

**`AlgebraicGeometry.perfect_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PerfectMorphism/FpqcLocalAtTarget.lean, line 457](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PerfectMorphism/FpqcLocalAtTarget.lean#L457). References: SGA 6 IV (3.1.1), “special case”.

> **Stacks 069B.** Perfectness of a morphism of schemes is fpqc local on the base: a morphism is
> perfect if and only if its base change along every member of an fpqc covering of its target is
> perfect.
>
> Both implications are part of `CategoryTheory.MorphismProperty.IsLocalAtTarget`; they are spelled
> out as a single `Iff` by `AlgebraicGeometry.perfect_iff_of_fpqcCover`.

```lean
public instance perfect_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget (@Perfect.{u}) Scheme.fpqcPrecoverage
```

## Tag 069C, a lemma

[Tag 069C](https://stacks.math.columbia.edu/tag/069C) in the Stacks Project.

**`AlgebraicGeometry.perfect_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PerfectMorphism/RelativeTorDimensionClause.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PerfectMorphism/RelativeTorDimensionClause.lean#L231).

> Let `f : X ⟶ S` be a pseudo-coherent morphism of schemes. The following are equivalent:
> 1. `f` is perfect;
> 2. `𝒪_X` locally has finite Tor dimension as a sheaf of `f^{-1}𝒪_S`-modules, that is, the
>    restriction of scalars of `𝒪_X[0]` along `f^{-1}𝒪_S ⟶ 𝒪_X` locally has finite Tor dimension
>    on the inverse-image ringed space `(X, f^{-1}𝒪_S)`, at the derived tensor product;
> 3. for every `x ∈ X` the local ring `𝒪_{X, x}` has finite Tor dimension as an
>    `𝒪_{S, f x}`-module through the stalk map of `f`.

```lean
theorem perfect_tfae {X S : Scheme.{u}} (f : X ⟶ S) [PseudoCoherent f] :
    List.TFAE
      [Perfect f,
        Stacks.Cohomology.TorAmplitude.LocallyHasFiniteTorDimension
          (RingedSpace.inverseImage S.toRingedSpace f.base)
          ((derivedScalarRestriction f).obj
            ((DerivedCategory.singleFunctor (OXMod.{u, u} X.toRingedSpace) 0).obj
              (structureModule X.toRingedSpace))),
        ∀ x : X,
          let _ : Algebra (S.presheaf.stalk (f.base x)) (X.presheaf.stalk x) :=
            (f.stalkMap x).hom.toAlgebra
          HasFiniteTorDimensionCanonical (S.presheaf.stalk (f.base x))
            ((DerivedCategory.singleFunctor (ModuleCat.{u} (S.presheaf.stalk (f.base x))) 0).obj
              (ModuleCat.of (S.presheaf.stalk (f.base x)) (X.presheaf.stalk x)))]
```

## Tag 0G2E, a lemma

[Tag 0G2E](https://stacks.math.columbia.edu/tag/0G2E) in the Stacks Project.

**`AlgebraicGeometry.isPerfect_pushforward_structureSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PerfectClosedImmersion.lean, line 359](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/PerfectClosedImmersion.lean#L359).

> **Stacks 0G2E.** If `i : Z ⟶ X` is a perfect closed immersion of schemes then `i_*𝒪_Z` is a
> perfect `𝒪_X`-module, that is, a perfect object of the derived category of `𝒪_X`-modules.

```lean
theorem isPerfect_pushforward_structureSheaf {Z X : Scheme.{u}} (i : Z ⟶ X)
    [IsClosedImmersion i] [Perfect i]
    [HasDerivedCategory.{d} (OXMod.{u, u} X.toRingedSpace)] :
    RingedSpace.IsPerfect
      ((DerivedCategory.singleFunctor (OXMod.{u, u} X.toRingedSpace) 0).obj
        ((Scheme.Modules.pushforward i).obj (SheafOfModules.unit Z.ringCatSheaf)))
```

## Tag 0B6G, a lemma

[Tag 0B6G](https://stacks.math.columbia.edu/tag/0B6G) in the Stacks Project.

**`Stacks.AlgebraicGeometry.PerfectProperDirectImage.isPerfect_derivedPushforward_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PerfectMorphism/MayerVietorisTorDimension.lean, line 393](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PerfectMorphism/MayerVietorisTorDimension.lean#L393). References: SGA 6 0 (3.1), “special case”; SGA 6 0 (4.1); SGA 6 III (4.8.1), “special case”; SGA 6 IV (2.12), “special case”; SGA 6 IV (3.3.2), “3.3.2.3, special case”; SGA 6 XIV (2.2), “special case”.

> **[Stacks, Tag 0B6G].** Let `S` be a Noetherian scheme, let `f : X ⟶ S` be a perfect proper
> morphism of schemes and let `E` be a perfect object of `D(𝒪_X)`. Then `Rf_*E` is a perfect object
> of `D(𝒪_S)`.
>
> By [Stacks, Tag 08CQ] perfectness is pseudo-coherence together with locally finite Tor dimension.
> Pseudo-coherence is `isPseudoCoherent_derivedPushforward_of_isPerfect`, and the Tor-dimension half
> is `hasFiniteTorDimension_derivedPushforward_affineOpen` fed into
> `isPerfect_derivedPushforward_of_isPerfect_of_forall_affineOpen`. Nothing is assumed beyond the
> source's own hypotheses.

```lean
theorem isPerfect_derivedPushforward_of_isPerfect {X S : Scheme.{u}} (f : X ⟶ S)
    [IsNoetherian S] [Perfect f] [IsProper f] (E : DerivedCategory X.Modules)
    (hE : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace) E) :
    Stacks.Cohomology.PerfectComplexes.IsPerfect (X := S.toRingedSpace)
      ((derivedPushforwardModules f).obj E)
```

**`Stacks.AlgebraicGeometry.PerfectProperDirectImage.isPseudoCoherent_derivedPushforward_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PerfectMorphism/ProperDirectImage.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PerfectMorphism/ProperDirectImage.lean#L218). The attribute's comment: “the pseudo-coherence half of the conclusion: Rf\_*E is a pseudo-coherent object of D(𝒪\_S), proved under the source's own hypotheses and no others”. References: SGA 6 0 (3.1), “partial”; SGA 6 XIV (2.2), “special case”.

> **[Stacks, Tag 0B6G], the pseudo-coherence half of the conclusion, with no hypothesis.** Let
> `S` be a Noetherian scheme, let `f : X ⟶ S` be a perfect proper morphism of schemes and let `E`
> be a perfect object of `D(𝒪_X)`. Then `Rf_*E` is a pseudo-coherent object of `D(𝒪_S)`.
>
> By [Stacks, Tag 08CQ] perfectness is pseudo-coherence together with locally finite Tor
> dimension; this is the first of the two. The hypotheses the pseudo-coherence half of
> [Stacks, Tag 08EV] makes of `E` are supplied by `isCoherent_homology_and_bounds_of_isPerfect`,
> and its support hypothesis by the fact that every closed subset of the source of a proper
> morphism is proper over the target. The hypothesis that half carries for [Stacks, Tag 02O5] is
> supplied by the proof of [Stacks, Tag 02O5] in this tree,
> `AlgebraicGeometry.ProperCoherenceWitness.higherDirectImageIsCoherentOverAffineBase`, so it is
> not assumed here.

```lean
theorem isPseudoCoherent_derivedPushforward_of_isPerfect [IsNoetherian S]
    [AlgebraicGeometry.Perfect f] [IsProper f] (E : DerivedCategory X.Modules)
    (hE : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace) E) :
    AlgebraicGeometry.RingedSpace.IsPseudoCoherent (X := S.toRingedSpace)
      ((derivedPushforwardModules f).obj E)
```

## Tag 069D, a lemma

[Tag 069D](https://stacks.math.columbia.edu/tag/069D) in the Stacks Project.

**`AlgebraicGeometry.Perfect.isLocalAtSource_fppfPrecoverage`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PerfectMorphism/FppfDescent.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PerfectMorphism/FppfDescent.lean#L84).

> Perfectness of morphisms of schemes is local on the source for the fppf topology: a morphism
> is perfect exactly when its composites with the members of an fppf covering of its source are.

```lean
instance Perfect.isLocalAtSource_fppfPrecoverage :
    MorphismProperty.IsLocalAtSource (@Perfect.{u} : MorphismProperty Scheme.{u})
      Scheme.fppfPrecoverage
```

## Tag 09RK, a lemma

[Tag 09RK](https://stacks.math.columbia.edu/tag/09RK) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.isRegularImmersion_of_perfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/PerfectFactor.lean, line 485](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/PerfectFactor.lean#L485). The attribute's comment: “i is a regular immersion”.

> **Stacks tag 09RK for the inner factor.**  Let `i : Z ⟶ Y` and `j : Y ⟶ X` be immersions of
> schemes with `X` locally Noetherian and `i` perfect.  If the composite `i ≫ j` is a regular
> immersion, then `i` is a regular immersion.

```lean
theorem isRegularImmersion_of_perfect (hji : IsRegularImmersion (i ≫ j)) :
    IsRegularImmersion i
```

**`Stacks.AlgebraicGeometry.RegularIdealSheaf.exists_opens_isRegularImmersion_comp_of_perfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/PerfectFactor.lean, line 510](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularImmersion/PerfectFactor.lean#L510). The attribute's comment: “j is a regular immersion near the image of i”.

> **Stacks tag 09RK for the outer factor, in its neighbourhood form — the corrected statement
> of a Stacks erratum.**  Under the same hypotheses there is an open
> `V ⊆ Y` containing the image of `i` such that the immersion `V.ι ≫ j` of that open subscheme
> into `X` is regular.
>
> The source concludes instead that `j` itself is a regular immersion, and that is false.  Over a
> field `k`, take `Z = Spec k`, `Y = Spec k ⊔ Spec k`, `X = Spec k ⊔ Spec k[ε]/(ε²)`, let `i` be
> the inclusion of the first component of `Y`, and let `j` be the identity on the first component
> and the reduced point `Spec k ↪ Spec k[ε]/(ε²)` on the second.  All three hypotheses hold: `X` is
> the spectrum of the Noetherian ring `k × k[ε]/(ε²)`, and `i` and `i ≫ j` are inclusions of a
> component, hence open immersions, hence regular immersions, so `i` is perfect.  Yet `j` is not a
> regular immersion: on the second component its ideal is `(ε) ⊆ k[ε]/(ε²)`, and no weakly regular
> sequence generates it, since every element of `(ε)` kills `ε ≠ 0`.  This is
> `Stacks.Examples.not_forall_isRegularImmersion_of_perfect_of_isRegularImmersion_comp`.
>
> The hypotheses control `j` only at the points of `i(Z)` — in the example the first component,
> where `j` is an isomorphism — and the neighbourhood form below is exactly what the source's own
> local-ring argument supplies.  See also the implementation notes of this file.

```lean
theorem exists_opens_isRegularImmersion_comp_of_perfect (hji : IsRegularImmersion (i ≫ j)) :
    ∃ V : Y.Opens, (∀ z : Z, i.base z ∈ V) ∧ IsRegularImmersion (V.ι ≫ j)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.61, Tag 0685](https://stacks.math.columbia.edu/tag/0685)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
