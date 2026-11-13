---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.PicardSituation, AlgebraicGeometry.Space.PicardSituation.picardPresheaf, AlgebraicGeometry.Space.PicardSituation.picardFunctor, AlgebraicGeometry.Space.PicardSituation.fibreIsoClassEquiv, AlgebraicGeometry.Space.PicardSituation.isoClassPresheafIsoPicardPresheaf, AlgebraicGeometry.Space.PicardSituation.isIso_sheafifyLift_toPicardFunctorOfIsoClasses, AlgebraicGeometry.Space.PicardSituation.exact_picardSequence, AlgebraicGeometry.Space.PicardSituation.picardSequence_splitExact
statement: formalized
proof: formalized
---

# 99.11 The Picard functor

Section 99.11 of the Stacks Project, [Tag 0D24](https://stacks.math.columbia.edu/tag/0D24). 9 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0D25, a situation

[Tag 0D25](https://stacks.math.columbia.edu/tag/0D25) in the Stacks Project.

**`AlgebraicGeometry.Space.PicardSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardFunctor.lean, line 311](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PicardFunctor.lean#L311). The attribute's comment: “the standing data”.

> **Stacks 0D25.**  The standing data of the relative Picard functor: a morphism
> `f : X ⟶ base` of algebraic spaces over the scheme `S`.

```lean
structure PicardSituation (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
```

**`AlgebraicGeometry.Space.PicardSituation.picardPresheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardFunctor.lean, line 363](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PicardFunctor.lean#L363). The attribute's comment: “the presheaf of Picard groups of the base changes”.

> **Stacks 0D25.**  The presheaf `T ↦ Pic(X_T)` on the schemes over the base, whose fppf
> sheafification is the relative Picard functor.  Its action on a morphism of test schemes is
> pullback of Picard classes.

```lean
def picardPresheaf : (s.SchemesOver)ᵒᵖ ⥤ Type (u + 1)
```

**`AlgebraicGeometry.Space.PicardSituation.picardFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardFunctor.lean, line 397](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PicardFunctor.lean#L397). The attribute's comment: “the relative Picard functor”. References: SGA 6 X (2.4), “definition of Pic\_\{X/B}”; SGA 6 XIII (3.1).

> **Stacks 0D25.**  The *relative Picard functor* `Pic_{X/base} : (Sch/base)ᵒᵖ ⥤ Sets`: the
> fppf sheafification of the presheaf `T ↦ Pic(X_T)` of isomorphism classes of invertible modules
> on the base changes.

```lean
def picardFunctor : (s.SchemesOver)ᵒᵖ ⥤ Type (u + 1)
```

## Tag 0D26, a lemma

[Tag 0D26](https://stacks.math.columbia.edu/tag/0D26) in the Stacks Project.

**`AlgebraicGeometry.Space.PicardSituation.fibreIsoClassEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardFunctorSheafification.lean, line 227](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PicardFunctorSheafification.lean#L227). The attribute's comment: “ONLY the identification of Ob(Picardstack\_\{X/B,T})/≅ with Pic(X\_T) at one test scheme; the sheafification statement is isIso\_sheafifyLift\_toPicardFunctorOfIsoClasses”.

> **`Ob(Picardstack_{X/B, T})/≅` is `Pic(X_T)`.** The isomorphism class of an object of the
> fibre of the Picard stack over `T` goes to the class in `Pic(X_T)` of its invertible module.

```lean
def fibreIsoClassEquiv (T : s.SchemesOver) :
    _root_.Quotient (isIsomorphicSetoid
        ((picardProjection (modulePushforwardCoherence B S hS) s).Fiber T)) ≃ s.picardAt T
```

**`AlgebraicGeometry.Space.PicardSituation.isoClassPresheafIsoPicardPresheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardFunctorSheafification.lean, line 294](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PicardFunctorSheafification.lean#L294). The attribute's comment: “ONLY the identification of the presheaf T ↦ Ob(Picardstack\_\{X/B,T})/≅ with the presheaf T ↦ Pic(X\_T); the sheafification statement is isIso\_sheafifyLift\_toPicardFunctorOfIsoClasses”.

> **The presheaf `T ↦ Ob(Picardstack_{X/B, T})/≅` is the presheaf `T ↦ Pic(X_T)`.** At each
> test scheme it is `AlgebraicGeometry.Space.PicardSituation.fibreIsoClassEquiv`.

```lean
def isoClassPresheafIsoPicardPresheaf :
    (picardProjection (modulePushforwardCoherence B S hS) s).isoClassPresheaf ≅
      s.picardPresheaf
```

**`AlgebraicGeometry.Space.PicardSituation.isIso_sheafifyLift_toPicardFunctorOfIsoClasses`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardFunctorSheafification.lean, line 318](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PicardFunctorSheafification.lean#L318). The attribute's comment: “the relative Picard functor is the fppf sheafification of the presheaf of isomorphism classes of objects of the fibres of the Picard stack”.

> In Situation 0D25 the relative Picard functor `Pic_{X/B}` is the fppf
> sheafification of the presheaf `T ↦ Ob(Picardstack_{X/B, T})/≅` of isomorphism classes of objects
> of the fibre categories of the Picard stack: `Pic_{X/B}` is an fppf sheaf
> (`AlgebraicGeometry.Space.PicardSituation.isSheaf_picardFunctor`) and the canonical map
> `AlgebraicGeometry.Space.PicardSituation.toPicardFunctorOfIsoClasses` from that presheaf into it
> factors through the sheafification by an isomorphism.

```lean
theorem isIso_sheafifyLift_toPicardFunctorOfIsoClasses :
    IsIso (sheafifyLift s.fppfTopology s.toPicardFunctorOfIsoClasses s.isSheaf_picardFunctor)
```

## Tag 0D27, a lemma

[Tag 0D27](https://stacks.math.columbia.edu/tag/0D27) in the Stacks Project.

**`AlgebraicGeometry.Space.PicardSituation.exact_picardSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardExactSequence.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PicardExactSequence.lean#L98). The attribute's comment: “the exact sequence 0 → Pic(T) → Pic(X\_T) → Pic\_\{X/B}(T)”.

> **Stacks 0D27.**  In Situation 0D25, if `𝒪_T ⟶ f_{T, *}𝒪_{X_T}` is an isomorphism for every
> scheme `T` over the base, then for every such `T` the sequence
> `0 ⟶ Pic(T) ⟶ Pic(X_T) ⟶ Pic_{X/B}(T)` is exact: pullback along `f_T` is injective, and a class
> of `X_T` maps to the trivial element of the relative Picard functor exactly when it is pulled
> back from `T`.

```lean
theorem exact_picardSequence (h : s.StructureSheafMapIso) (T : s.SchemesOver) :
    Function.Injective (s.basePicardPullback T) ∧
      ∀ x : s.picardAt T, s.picardClassMap T x = s.picardClassMap T 0 ↔
        x ∈ Set.range (s.basePicardPullback T)
```

## Tag 0D28, a lemma

[Tag 0D28](https://stacks.math.columbia.edu/tag/0D28) in the Stacks Project.

**`AlgebraicGeometry.Space.PicardSituation.picardSequence_splitExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardSequenceSplitExact.lean, line 268](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PicardSequenceSplitExact.lean#L268).

> In Situation 0D25 let `σ : B ⟶ X` be a section of `f`, and assume that
> `𝒪_T ⟶ f_{T, *}𝒪_{X_T}` is an isomorphism for every scheme `T` over `B`.  Then for every `T`
>
> `0 ⟶ Pic(T) ⟶ Pic(X_T) ⟶ Pic_{X/B}(T) ⟶ 0`
>
> is a split exact sequence with splitting `σ_T^* : Pic(X_T) ⟶ Pic(T)`, the first arrow being
> pullback along `f_T : X_T ⟶ T` and the second the canonical map to the fppf sheafification
> `Pic_{X/B}`.  Spelled out:
>
> * the first arrow is injective;
> * two classes on `X_T` have the same image in `Pic_{X/B}(T)` exactly when they differ by a class
>   pulled back from `T`, and in particular (exactness at `Pic(X_T)`) a class maps to the image of
>   the trivial class exactly when it is pulled back from `T`;
> * the second arrow is surjective;
> * `σ_T^*` is a left inverse of the first arrow;
> * the second arrow restricts to a bijection from the kernel of `σ_T^*` onto `Pic_{X/B}(T)`, the
>   identification `Pic_{X/B}(T) = ker(σ_T^*)` of the proof.

```lean
theorem picardSequence_splitExact (hstr : s.StructureSheafMapIso) (T : s.SchemesOver) :
    Function.Injective (s.basePicardPullback T) ∧
      (∀ x y : s.picardAt T, s.picardClassMap T x = s.picardClassMap T y ↔
        x - y ∈ Set.range (s.basePicardPullback T)) ∧
      (∀ x : s.picardAt T, s.picardClassMap T x = s.picardClassMap T 0 ↔
        x ∈ Set.range (s.basePicardPullback T)) ∧
      Function.Surjective (s.picardClassMap T) ∧
      Function.LeftInverse (sectionPicardPullback σ hσ T) (s.basePicardPullback T) ∧
      Function.Bijective (fun x : (sectionPicardPullbackHom σ hσ T).ker ↦
        s.picardClassMap T (x : s.picardAt T))
```

**`AlgebraicGeometry.Space.PicardSituation.leftInverse_sectionPicardPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardSequenceSplitting.lean, line 255](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PicardSequenceSplitting.lean#L255). The attribute's comment: “auxiliary: the splitting by σ\_T^* for an arbitrary 03LU coherence datum; the full statement, with no hypothesis, is picardSequence\_splitExact”.

> **Stacks 0D28, the splitting.**  Pullback of Picard classes along the section
> `σ_T : T ⟶ X_T` of the base change retracts pullback along the projection `f_T : X_T ⟶ T`:
> `σ_T^* ∘ f_T^*` is the identity of `Pic(T)`.  This is the splitting of the sequence
>
> `0 ⟶ Pic(T) ⟶ Pic(X_T) ⟶ Pic_{X/B}(T) ⟶ 0`
>
> of Stacks 0D28, and it holds with no hypothesis on `𝒪_T ⟶ f_{T, *}𝒪_{X_T}`.

```lean
theorem leftInverse_sectionPicardPullback (hc : ModulePushforwardCoherence B S hS)
    (σ : s.base ⟶ s.X) (hσ : σ ≫ s.f = 𝟙 s.base) (T : s.SchemesOver) :
    Function.LeftInverse (sectionPicardPullback σ hσ T) (s.basePicardPullback T)
```

**`AlgebraicGeometry.Space.PicardSituation.injective_basePicardPullback_of_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardSequenceSplitting.lean, line 270](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PicardSequenceSplitting.lean#L270). The attribute's comment: “auxiliary: exactness at Pic(T) for an arbitrary 03LU coherence datum; the full statement, with no hypothesis, is picardSequence\_splitExact”.

> **Stacks 0D28, exactness at `Pic(T)`.**  In Situation 0D25 with a section `σ : B ⟶ X` of `f`,
> pullback along the projection `f_T : X_T ⟶ T` of the base change is an injection
> `Pic(T) ⟶ Pic(X_T)`: it is retracted by `σ_T^*`.
>
> Stacks 0D27 obtains the same conclusion from `𝒪_T ⟶ f_{T, *}𝒪_{X_T}` being an isomorphism; with a
> section neither that hypothesis nor the unit of the Stacks 03LU adjunction being an isomorphism at
> an invertible module is needed.

```lean
theorem injective_basePicardPullback_of_section (hc : ModulePushforwardCoherence B S hS)
    (σ : s.base ⟶ s.X) (hσ : σ ≫ s.f = 𝟙 s.base) (T : s.SchemesOver) :
    Function.Injective (s.basePicardPullback T)
```

**`AlgebraicGeometry.Space.PicardSituation.existsUnique_add_sectionPicardPullback_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardSequenceSplitting.lean, line 297](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PicardSequenceSplitting.lean#L297). The attribute's comment: “auxiliary: the direct sum decomposition for an arbitrary 03LU coherence datum; the full statement, with no hypothesis, is picardSequence\_splitExact”.

> **Stacks 0D28, the direct sum decomposition.**  The splitting makes `Pic(X_T)` the direct sum
> of the image of `Pic(T)` under `f_T^*` and the kernel of `σ_T^*`: every Picard class on `X_T` is
> the sum of the pullback of a unique Picard class on `T` and a unique class killed by `σ_T^*`.
>
> This is what "the sequence of Stacks 0D28 is split" says internally to `Pic(X_T)`; the
> identification of the kernel of `σ_T^*` with `Pic_{X/B}(T)`, which is the remaining content of
> Stacks 0D28, is not proved here.

```lean
theorem existsUnique_add_sectionPicardPullback_eq_zero (hc : ModulePushforwardCoherence B S hS)
    (σ : s.base ⟶ s.X) (hσ : σ ≫ s.f = 𝟙 s.base) (T : s.SchemesOver) (x : s.picardAt T) :
    ∃! p : s.basePicardAt T × s.picardAt T,
      sectionPicardPullback σ hσ T p.2 = 0 ∧
        x = s.basePicardPullback T p.1 + p.2
```

## Tag 0D29, a lemma

[Tag 0D29](https://stacks.math.columbia.edu/tag/0D29) in the Stacks Project.

**`AlgebraicGeometry.Space.sectionedPicardCFG_isStackInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackSectionedIsStack.lean, line 546](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PicardStackSectionedIsStack.lean#L546). The attribute's comment: “the full statement: Picardstack\_\{X/B,sigma} is a stack in groupoids over (Sch/S)\_fppf, for any section sigma of f”.

> **Stacks 0D29.** In Situation 0D25, given a section `σ` of `f : X ⟶ B`, the rigidified
> Picard stack `Picardstack_{X/B, σ}` is a stack in groupoids over `(Sch/S)_fppf`. The category
> is built from the pseudofunctoriality of Stacks 03LU
> (`AlgebraicGeometry.Space.modulePushforwardCoherence`) and the coherence of the restriction along
> the section (`AlgebraicGeometry.Space.sectionTransportCoherence`), both proved in the library, so
> the statement carries no hypothesis beyond the section.

```lean
theorem sectionedPicardCFG_isStackInGroupoids (s : PicardSituation B S hS) (σ : s.base ⟶ s.X)
    (hσ : σ ≫ s.f = 𝟙 s.base) :
    (sectionedPicardCFG (modulePushforwardCoherence B S hS)
      (sectionTransportCoherence _ σ hσ)).val.p.IsStackInGroupoids.{w}
        (BigFppfOver.topology B S hS)
```

## Tag 0D2A, a lemma

[Tag 0D2A](https://stacks.math.columbia.edu/tag/0D2A) in the Stacks Project.

**`AlgebraicGeometry.Space.forgetTrivialization_representable_surjective_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardForgetTrivializationRepresentable.lean, line 475](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PicardForgetTrivializationRepresentable.lean#L475).

> In Situation 0D25, let `σ : B ⟶ X` be a section.  The 1-morphism
> `Picardstack_{X/B, σ} ⟶ Picardstack_{X/B}` forgetting the trivialisation is representable,
> surjective and smooth: its base change along every 1-morphism from a slice of the site is
> represented by an object of the site (Stacks 02Y7, 04ST), it is representable by algebraic spaces
> (Stacks 02ZW), and every algebraic space representing its base change along a scheme-valued point
> has surjective and smooth structural morphism (Stacks 03YK, 04SX).

```lean
theorem forgetTrivialization_representable_surjective_smooth :
    Stacks.RepresentableMorphism.IsRepresentableMorphism
        (sectionedPicardCFG (modulePushforwardCoherence B S hS)
          (sectionTransportCoherence (modulePushforwardCoherence B S hS) σ hσ)).val.p
        (picardCFG (modulePushforwardCoherence B S hS) s).val.p
        (forgetTrivialization (modulePushforwardCoherence B S hS)
          (sectionTransportCoherence (modulePushforwardCoherence B S hS) σ hσ)).hom.toFunctor ∧
      ∃ hf : Stack.IsRepresentableByAlgebraicSpaces B S hS
          (forgetTrivialization (modulePushforwardCoherence B S hS)
            (sectionTransportCoherence (modulePushforwardCoherence B S hS) σ hσ)).hom,
        Stack.HasRelativeProperty.{u, u + 1, u + 1, u} B S hS
            (Space.surjectiveMorphismProperty B S hS)
            (forgetTrivialization (modulePushforwardCoherence B S hS)
              (sectionTransportCoherence (modulePushforwardCoherence B S hS) σ hσ)) hf ∧
          Stack.HasRelativeProperty.{u, u + 1, u + 1, u} B S hS
            (Space.smoothMorphismProperty B S hS)
            (forgetTrivialization (modulePushforwardCoherence B S hS)
              (sectionTransportCoherence (modulePushforwardCoherence B S hS) σ hσ)) hf
```

**`AlgebraicGeometry.Space.forgetTrivializationFibreEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackCategory.lean, line 523](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PicardStackCategory.lean#L523). The attribute's comment: “ONLY the fibre identification the proof rests on: the fibre of Picardstack\_\{X/B,sigma} -> Picardstack\_\{X/B} over (T,h,L) is the set of trivializations O\_T = sigma\_T^*L, that is Isom\_T(O\_T, sigma\_T^*L). NONE of the three clauses - representable, surjective, smooth - is proved; see the implementation notes of this file for the three obstructions”.

> **The fibre of the 1-morphism of Stacks 0D2A is the set of trivialisations along the
> section.**  The objects of `Picardstack_{X/B, σ}` lying over an object `(T, h, L)` of
> `Picardstack_{X/B}` are the quadruples `(T, h, L, α)`, so they correspond bijectively to the
> trivialisations `α : 𝒪_T ≅ σ_T^*L`; the fibre is `Isom_T(𝒪_T, σ_T^*L)`, which is the
> identification the source's proof of Stacks 0D2A rests on.

```lean
def forgetTrivializationFibreEquiv (A : PicardObject s) :
    (structureModule (s.baseSpaceAt A.T) ≅
        (PicardSituation.sectionPullback σ hσ A.T).obj A.lineBundle) ≃
      {A' : PicardSituation.SectionedPicardObject σ hσ // A'.toPicardObject = A}
```

**`AlgebraicGeometry.Space.exists_sectionedPicardObject_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackCategory.lean, line 544](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PicardStackCategory.lean#L544). The attribute's comment: “ONLY the object-level content of clause (2): an object (T,h,L) of Picardstack\_\{X/B} lifts along the 1-morphism of this tag exactly when sigma\_T^*[L] = 0 in Pic(T). The three clauses themselves - representable, surjective and smooth in the sense of Stacks 02ZW and 03YK - are NOT proved; see the implementation notes of this file”.

> **An object of `Picardstack_{X/B}` lies in the image of the 1-morphism of Stacks 0D2A exactly
> when the class of its invertible module is killed by `σ_T^*`.**  By the fibre identification a
> lift is a trivialisation of `L` along the section, and by Stacks 0D2B such a trivialisation
> exists exactly when `σ_T^*[L] = 0` in `Pic(T)`.

```lean
theorem exists_sectionedPicardObject_iff (A : PicardObject s) :
    (∃ A' : PicardSituation.SectionedPicardObject σ hσ, A'.toPicardObject = A) ↔
      PicardSituation.sectionPicardPullback σ hσ A.T
        (picardClass (s.baseChange A.T) A.lineBundle A.invertible) = 0
```

## Tag 0D2B, a lemma

[Tag 0D2B](https://stacks.math.columbia.edu/tag/0D2B) in the Stacks Project.

**`AlgebraicGeometry.Space.PicardSituation.sectionPicardPullback_eq_zero_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackSection.lean, line 253](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PicardStackSection.lean#L253). The attribute's comment: “the index set of the disjoint union: the kernel of σ\_T^* on Pic(X\_T) is exactly the set of classes of the invertible modules admitting a trivialisation along σ\_T, i.e. of those underlying an object of Picardstack\_\{X/B, σ}. The fibred-in-setoids conclusion and the injectivity of the description are NOT proved: both need the global units of the structure sheaf of an algebraic space, which this development does not carry”.

> **The elements of the kernel of `σ_T^*` are exactly the Picard classes of the invertible
> `𝒪_{X_T}`-modules carrying a trivialisation along `σ_T`.**
>
> This is the identification of the index set of the disjoint union of Stacks 0D2B: for a test
> scheme `(T, h)` over the base, the invertible modules underlying the objects of
> `Picardstack_{X/B, σ}` over `(T, h)` — the modules `L` for which a rigidifying isomorphism
> `α : σ_T^*L ≅ 𝒪_T` exists — are precisely those whose class is killed by
> `σ_T^* : Pic(X_T) ⟶ Pic(T)`.  Stacks 0D2B's description of the isomorphism classes of
> `Picardstack_{X/B, σ}` over `T` as `⨿_h ker(σ_T^*)` is the sum of this statement over the
> objects `(T, h)` of `AlgebraicGeometry.Space.PicardSituation.SchemesOver`.
>
> **The two other halves of Stacks 0D2B are not proved**: that the stack is fibred in setoids, and
> that two objects with the same underlying class are isomorphic.  Both need the global units of
> the structure sheaf of an algebraic space, which this development does not carry; see the
> implementation notes of the file.

```lean
theorem sectionPicardPullback_eq_zero_iff (σ : s.base ⟶ s.X) (hσ : σ ≫ s.f = 𝟙 s.base)
    (T : s.SchemesOver) (x : s.picardAt T) :
    sectionPicardPullback σ hσ T x = 0 ↔
      ∃ (L : Modules.{u, u} B S hS (s.baseChange T).1 (s.baseChange T).2)
        (hL : IsInvertibleModule (s.baseChange T) L), picardClass _ L hL = x ∧
          Nonempty ((modulePullback B S hS (baseChangeSection σ hσ T)).obj L ≅
            structureModule (s.baseSpaceAt T))
```

**`AlgebraicGeometry.Space.sectionedPicardCFG_isFiberedInSetoids_and_isoClassEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackSectionSetoid.lean, line 437](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PicardStackSectionSetoid.lean#L437).

> In Situation 0D25, let `σ` be a section of `f : X ⟶ B` and assume that
> `𝒪_T ⟶ f_{T, *}𝒪_{X_T}` is an isomorphism for every test scheme `T` over `B`.  Then
> `Picardstack_{X/B, σ} ⟶ (Sch/S)_{fppf}` is fibred in setoids, and its set of isomorphism classes
> over a scheme `T` is `∐_{h : T ⟶ B} Ker(σ_T^* : Pic(X ×_{B, h} T) ⟶ Pic(T))`, through the
> bijection `AlgebraicGeometry.Space.sectionedPicardIsoClassEquiv` sending the class of
> `(T, h, L, α)` to `(h, [L])`.
>
> `Picardstack_{X/B, σ}` is `AlgebraicGeometry.Space.sectionedPicardCFG` at the pseudofunctoriality
> `AlgebraicGeometry.Space.modulePushforwardCoherence` of Stacks 03LU and the coherence
> `AlgebraicGeometry.Space.sectionTransportCoherence` of the restriction along the section, both
> unconditional.

```lean
theorem sectionedPicardCFG_isFiberedInSetoids_and_isoClassEquiv {s : PicardSituation B S hS}
    (σ : s.base ⟶ s.X) (hσ : σ ≫ s.f = 𝟙 s.base) (hstr : s.StructureSheafMapIso) :
    (sectionedPicardCFG (modulePushforwardCoherence B S hS)
        (sectionTransportCoherence _ σ hσ)).val.p.IsFiberedInSetoids ∧
      ∀ A : PicardSituation.SectionedPicardObject σ hσ,
        sectionedPicardIsoClassEquiv (modulePushforwardCoherence B S hS)
            (sectionTransportCoherence _ σ hσ) hstr A.testScheme.left
            (Quotient.mk _ ⟨A, rfl⟩) =
          ⟨A.testScheme.hom, ⟨picardClass _ A.toPicardObject.lineBundle
            A.toPicardObject.invertible,
            (PicardSituation.sectionPicardPullback_picardClass_eq_zero_iff σ hσ A.testScheme
              _ _).2 ⟨A.trivialization.symm⟩⟩⟩
```

## Tag 0D2C, a proposition

[Tag 0D2C](https://stacks.math.columbia.edu/tag/0D2C) in the Stacks Project.

**`AlgebraicGeometry.Space.isAlgebraicSpaceOver_picardFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardFunctorIsAlgebraicSpace.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PicardFunctorIsAlgebraicSpace.lean#L93). The attribute's comment: “the full statement: f flat (hflat), of finite presentation (hfp) and proper (hproper), and O\_T -> f\_\{T,*}O\_\{X\_T} an isomorphism for every scheme T over the base (hstr); Pic\_\{X/B} is an algebraic space over B”.

> **The Picard functor is an algebraic space.**  Let `S` be a scheme and
> `f : X ⟶ Y` a morphism of algebraic spaces over `S` such that
>
> 1. `f` is flat, of finite presentation and proper, and
> 2. `𝒪_T ⟶ f_{T, *}𝒪_{X_T}` is an isomorphism for all schemes `T` over `Y`.
>
> Then the relative Picard functor `Pic_{X/Y}` is an algebraic space over `Y`.

```lean
theorem isAlgebraicSpaceOver_picardFunctor {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hflat : IsFlat B S hS f.hom) (hfp : IsFinitePresentation B S hS f.hom)
    (hproper : IsProper B S hS f.hom)
    (hstr : (PicardSituation.mk X Y f).StructureSheafMapIso) :
    IsAlgebraicSpaceOver (PicardSituation.mk X Y f).picardFunctor
```

## Tag 0D2D, a lemma

[Tag 0D2D](https://stacks.math.columbia.edu/tag/0D2D) in the Stacks Project.

**`AlgebraicGeometry.Space.PicardSituation.isImmersion_picardEqualizer_and_isLocallySeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardDiagonalImmersion.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PicardDiagonalImmersion.lean#L244).

> Let `f : X ⟶ B` be a morphism of algebraic spaces over `S` which is flat, of finite
> presentation and proper, such that `𝒪_T ⟶ f_{T,*}𝒪_{X_T}` is an isomorphism for every scheme `T`
> over `B`. Then the diagonal `Pic_{X/B} ⟶ Pic_{X/B} ×_B Pic_{X/B}` is representable by
> immersions: for every scheme `T` over `B` and all `x, y ∈ Pic_{X/B}(T)`, the subfunctor of `h_T`
> of the morphisms `T' ⟶ T` with `x|_{T'} = y|_{T'}` (the base change of the diagonal along
> `(x, y)`) is represented by immersions. In other words, `Pic_{X/B} ⟶ B` is locally separated:
> every morphism of presheaves `q : F ⟶ B` whose fibres are identified with `Pic_{X/B}`, naturally
> in the test scheme, has diagonal an immersion.

```lean
theorem isImmersion_picardEqualizer_and_isLocallySeparated (hflat : IsFlat B S hS s.f.hom)
    (hfp : IsFinitePresentation B S hS s.f.hom) (hp : IsProper B S hS s.f.hom)
    (h : s.StructureSheafMapIso) :
    (∀ (T : s.SchemesOver) (x y : s.picardFunctor.obj (op T)),
      IsImmersion B S hS (s.picardEqualizer T x y).ι) ∧
    ∀ (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (q : F ⟶ s.base.1)
      (e : ∀ T : s.SchemesOver, s.picardFunctor.obj (op T) ≃
        {x : F.obj (op T.left) //
          q.app (op T.left) x =
            yonedaEquiv (show yoneda.obj T.left ⟶ s.base.1 from T.hom.hom)}),
      (∀ (T U : s.SchemesOver) (g : T ⟶ U) (x : s.picardFunctor.obj (op U)),
        (e T (s.picardFunctor.map g.op x)).val = F.map g.left.op (e U x).val) →
      IsLocallySeparated B S hS q
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 99.11, Tag 0D24](https://stacks.math.columbia.edu/tag/0D24)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
