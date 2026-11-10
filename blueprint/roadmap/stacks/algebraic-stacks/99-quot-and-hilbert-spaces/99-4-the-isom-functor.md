---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.HomSituation.isomSubfunctor, AlgebraicGeometry.Space.HomSituation.isomFunctor, AlgebraicGeometry.Space.HomSituation.isSheafFor_isomFunctor, AlgebraicGeometry.Space.HomSituation.isSheafFor_isomFunctor_of_isFpqcCovering, AlgebraicGeometry.Space.HomSituation.baseOfIsomMor_isomMorOfSpaceIsom, AlgebraicGeometry.Space.HomSituation.bijective_isomMorOver, AlgebraicGeometry.Space.HomSituation.bijective_isomMorOfSpaceIsom, AlgebraicGeometry.Space.HomSituation.isAffineFinitePresentationAlgebraicSpaceOver_isomFunctor_of_hasProperSupport
statement: formalized
proof: formalized
---

# 99.4 The Isom functor

Section 99.4 of the Stacks Project, [Tag 08K7](https://stacks.math.columbia.edu/tag/08K7). 4 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08K7, the section

[Tag 08K7](https://stacks.math.columbia.edu/tag/08K7) in the Stacks Project.

**`AlgebraicGeometry.Space.HomSituation.isomSubfunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeIsom.lean, line 349](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/RelativeIsom.lean#L349). The attribute's comment: “the Isom functor as a subfunctor of the Hom functor”.

> **Stacks 08K7.**  The relative Isom functor `Isom(F, G) ⊆ Hom(F, G)` as a subfunctor of the
> relative Hom functor of Stacks 08JT: its sections at a test scheme `T` over the base are the
> invertible `𝒪_{X_T}`-homomorphisms `F_T ⟶ G_T`.
>
> It is a subfunctor because invertibility is stable under pullback,
> `AlgebraicGeometry.Space.HomSituation.isIsomAt_homMap`.  The ambient relative Hom functor is
> taken at the pseudofunctoriality of the direct images of Stacks 03LU,
> `AlgebraicGeometry.Space.modulePushforwardCoherence`.

```lean
def isomSubfunctor : Subfunctor (s.homFunctor (modulePushforwardCoherence B S hS))
```

**`AlgebraicGeometry.Space.HomSituation.isomFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeIsom.lean, line 367](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/RelativeIsom.lean#L367). The attribute's comment: “the Isom functor”.

> **Stacks 08K7.**  The relative Isom functor `Isom(F, G) : (Sch/base)ᵒᵖ ⥤ Sets`, whose value
> at a test scheme `T` over the base is the set of invertible `𝒪_{X_T}`-homomorphisms
> `F_T ⟶ G_T` and whose action on a morphism of test schemes is pullback of homomorphisms.  Its
> inclusion into the relative Hom functor is `CategoryTheory.Subfunctor.ι`.

```lean
def isomFunctor : (s.SchemesOver)ᵒᵖ ⥤ Type (u + 1)
```

## Tag 08K8, a lemma

[Tag 08K8](https://stacks.math.columbia.edu/tag/08K8) in the Stacks Project.

**`AlgebraicGeometry.Space.HomSituation.isSheafFor_isomFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeIsom.lean, line 416](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/RelativeIsom.lean#L416). The attribute's comment: “conditional on the sheaf property of the relative Hom functor (Stacks 08JV), on the full-faithfulness clause of the fpqc descent of quasi-coherent modules (Stacks 04W8), and on the quasi-coherence of the two base-changed modules (Stacks 03GA)”.

> **Stacks 08K8.**  In the standing data of Stacks 08JT the relative Isom functor
> `Isom(F, G)` satisfies the sheaf property for the fpqc topology: for every fpqc covering
> `{U i ⟶ T}` of test schemes over the base, every compatible family of invertible
> `𝒪_{X_{U i}}`-homomorphisms `F_{U i} ⟶ G_{U i}` has a unique amalgamation, again invertible.
>
> This is the proof of the source.  The relative Hom functor already satisfies the sheaf property,
> so the family glues to a unique homomorphism `F_T ⟶ G_T`; what remains is that it is invertible,
> and that is `AlgebraicGeometry.Space.HomSituation.isIsomAt_of_isFpqcCovering`, which produces
> the fpqc covering `{X_{U i} ⟶ X_T}` of `X_T` by Stacks 03MR, part (3), and descends
> invertibility along it.  The passage from the sheaf property of `Hom(F, G)` to that of its
> subfunctor is `CategoryTheory.Subfunctor.isSheafFor_of_local`.

```lean
theorem isSheafFor_isomFunctor
    (hdesc : ReflectsIsoAlongFpqcCovering.{u, v} B S hS)
    {I : Type v} {T : s.SchemesOver} {U : I → s.SchemesOver} (g : ∀ i, U i ⟶ T)
    (hg : IsFpqcCovering B S hS
      fun i ↦ ((schemeSpaceFunctor B S hS).map (g i).left).hom)
    (hF : (s.baseChangedModule T s.F).IsQuasicoherentOnSite)
    (hG : (s.baseChangedModule T s.G).IsQuasicoherentOnSite)
    (hHom : Presieve.IsSheafFor (s.homFunctor (modulePushforwardCoherence B S hS))
      (Presieve.ofArrows U g)) :
    Presieve.IsSheafFor s.isomFunctor (Presieve.ofArrows U g)
```

**`AlgebraicGeometry.Space.HomSituation.isSheafFor_isomFunctor_of_isFpqcCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeIsomFpqcSheaf.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/RelativeIsomFpqcSheaf.lean#L141).

> **Stacks 08K8.**  In Situation 08JT the relative Isom functor `Isom(F, G)` satisfies the
> sheaf property for the fpqc topology: for every fpqc covering `{U i ⟶ T}` of schemes over the
> base, every compatible family of invertible homomorphisms `F_{U i} ⟶ G_{U i}` has a unique
> amalgamation, an invertible homomorphism `F_T ⟶ G_T`.
>
> This is the proof of the source.  `Hom(F, G)` satisfies the sheaf property, Stacks 08JV in the
> form of `AlgebraicGeometry.Space.HomSituation.isSheafFor_homFunctor_of_isFpqcCovering`, so it
> remains that a homomorphism `F_T ⟶ G_T` whose base changes to the `U i` are isomorphisms is an
> isomorphism; the base changes `{X_{U i} ⟶ X_T}` form an fpqc covering of `X_T` by Stacks 03MR,
> and invertibility descends along it by Stacks 04W8,
> `AlgebraicGeometry.Space.reflectsIsoAlongFpqcCovering`, the base-changed modules being
> quasi-coherent by Stacks 03GA.

```lean
theorem isSheafFor_isomFunctor_of_isFpqcCovering {I : Type v} {T : s.SchemesOver}
    {U : I → s.SchemesOver} (g : ∀ i, U i ⟶ T)
    (hg : IsFpqcCovering B S hS fun i ↦ ((schemeSpaceFunctor B S hS).map (g i).left).hom) :
    Presieve.IsSheafFor s.isomFunctor (Presieve.ofArrows U g)
```

## Tag 0D3T, a lemma

[Tag 0D3T](https://stacks.math.columbia.edu/tag/0D3T) in the Stacks Project.

**`AlgebraicGeometry.Space.HomSituation.baseOfIsomMor_isomMorOfSpaceIsom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Hom/IsomFunctorMorphisms.lean, line 586](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Hom/IsomFunctorMorphisms.lean#L586). The attribute's comment: “the first component of the pair is recovered from the morphism of sheaves into the Isom functor, conditional on the pseudofunctoriality of the direct images of Stacks 03LU”.

> **The morphism to the base is recovered from the morphism of presheaves into the Isom
> presheaf**: for a pair `(h, u)` with `u` invertible the morphism underlying
> `isomMorOfSpaceIsom (h, u)` is `h`.  This is the half of Stacks 0D3T that needs no descent,
> and it is inherited from the corresponding half of Stacks 0D3S,
> `AlgebraicGeometry.Space.HomSituation.baseOfMor_morOfSpaceHom`, the two left-hand sides being
> compared through the inclusion of the subfunctor.

```lean
theorem baseOfIsomMor_isomMorOfSpaceIsom (hc : ModulePushforwardCoherence B S hS)
    {T : AlgebraicSpaces B S hS} (h : T ⟶ s.base) (u : s.spaceHomAt (Over.mk h))
    (hu : s.IsIsomOverAt u) :
    s.baseOfIsomMor hc (s.isomMorOfSpaceIsom hc h u hu) = h
```

**`AlgebraicGeometry.Space.HomSituation.bijective_isomMorOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Hom/IsomFunctorMorphisms.lean, line 678](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Hom/IsomFunctorMorphisms.lean#L678). The attribute's comment: “the identification is a bijection on the fibres over a fixed morphism to the base; carries three hypotheses: `hc`, the pseudofunctoriality of the direct images of Stacks 03LU, and `hd`, `hd'`, the fullness clause of Stacks 04W8 for a one-member etale covering, for the two modules of the situation and for them exchanged (the faithfulness clause of Stacks 04W8 is proved here and not assumed)”.

> **Stacks 0D3T, the fibres of the identification.**  For a fixed morphism `h : T ⟶ base` of
> algebraic spaces over `S`, the assignment `u ↦ isomMorOfSpaceIsom (h, u)` is a *bijection* from
> the isomorphisms `u : F_T ⟶ G_T` of the two modules pulled back to `X ×_{base, h} T` onto the
> morphisms of presheaves `T ⟶ Isom(F, G)` lying over `h`.
>
> Together with `AlgebraicGeometry.Space.HomSituation.baseOfIsomMor_isomMorOfSpaceIsom`, which
> recovers the first component, this is the identification
> `Mor(T, Isom(F, G)) = {(h, u) | h : T ⟶ base, u : F_T ⟶ G_T an isomorphism}` of Stacks 0D3T.
>
> This is the argument of the source: both sides are cut out of the two sides of Stacks 0D3S, and
> what is checked is that the subsets correspond.  Injectivity is inherited from Stacks 0D3S and
> is unconditional beyond the coherence `hc`.  Surjectivity needs, beyond the hypothesis `hd` of
> Stacks 0D3S, that invertibility descends along the covering of base changes cut out by a scheme
> atlas of `T`, which is the same fullness clause of Stacks 04W8 for the reversed pair of
> modules, carried as `hd'`.

```lean
theorem bijective_isomMorOver (hc : ModulePushforwardCoherence B S hS)
    (hd : s.EtaleHomDescent) (hd' : s.EtaleReverseHomDescent)
    {T : AlgebraicSpaces B S hS} (h : T ⟶ s.base) :
    Function.Bijective (s.isomMorOver hc h)
```

**`AlgebraicGeometry.Space.HomSituation.bijective_isomMorOfSpaceIsom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Hom/IsomFunctorMorphismsEquiv.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Hom/IsomFunctorMorphismsEquiv.lean#L65). The attribute's comment: “the whole identification: the map (h, u) |-> the morphism T -> Isom(F, G) is a bijection from all pairs of h : T -> base and an isomorphism u : F_T -> G_T onto all morphisms from T into Isom(F, G), for any algebraic space T over S, with no hypothesis”.

> Let `T` be an algebraic space over `S`. The assignment `(h, u) ↦ isomMorOfSpaceIsom (h, u)`
> is a bijection from the pairs of a morphism `h : T ⟶ base` and an isomorphism `u : F_T ⟶ G_T` of
> the modules pulled back to `X ×_{base, h} T` onto the morphisms of presheaves `T ⟶ Isom(F, G)` on
> the big fppf site of `S`:
>
> `Mor(T, Isom(F, G)) = {(h, u) | h : T ⟶ base, u : F_T ⟶ G_T an isomorphism}`.
>
> Here `Isom(F, G)` is the presheaf built from the pseudofunctoriality of direct images
> `AlgebraicGeometry.Space.modulePushforwardCoherence`.

```lean
theorem bijective_isomMorOfSpaceIsom (T : AlgebraicSpaces B S hS) :
    Function.Bijective (fun p : (Σ h : T ⟶ s.base,
        {u : s.spaceHomAt (Over.mk h) // s.IsIsomOverAt u}) =>
      s.isomMorOfSpaceIsom (modulePushforwardCoherence B S hS) p.1 p.2.1 p.2.2)
```

## Tag 08K9, a proposition

[Tag 08K9](https://stacks.math.columbia.edu/tag/08K9) in the Stacks Project.

**`AlgebraicGeometry.Space.HomSituation.isAffineFinitePresentationAlgebraicSpaceOver_isomFunctor_of_hasProperSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeIsomAffineFinitePresentation.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/RelativeIsomAffineFinitePresentation.lean#L56). The attribute's comment: “Isom(F, G) is an algebraic space affine of finite presentation over B, for f of finite presentation and F, G of finite presentation, flat over B, with support proper over B”.

> In Situation 08JT assume that `f : X ⟶ B` is of finite presentation and that `𝓕` and `𝒢`
> are finitely presented `𝒪_X`-modules, flat over `B`, with support proper over `B`. Then the
> functor `Isom(𝓕, 𝒢)` is an algebraic space affine of finite presentation over `B`.

```lean
theorem isAffineFinitePresentationAlgebraicSpaceOver_isomFunctor_of_hasProperSupport
    (s : HomSituation B S hS) (hfp : IsFinitePresentation B S hS s.f.hom)
    (hF : s.F.IsFinitePresentationOnSite) (hG : s.G.IsFinitePresentationOnSite)
    (hFflat : IsFlatOver B S hS s.X.2 s.f.hom s.F)
    (hGflat : IsFlatOver B S hS s.X.2 s.f.hom s.G)
    (hFsupp : HasProperSupport B S hS s.X.2 s.base.2 s.f.hom
      (isLocallyOfFiniteType_of_isLocallyOfFinitePresentation B S hS hfp.1)
      ((SheafOfModules.toSheaf _).obj s.F))
    (hGsupp : HasProperSupport B S hS s.X.2 s.base.2 s.f.hom
      (isLocallyOfFiniteType_of_isLocallyOfFinitePresentation B S hS hfp.1)
      ((SheafOfModules.toSheaf _).obj s.G)) :
    IsAffineFinitePresentationAlgebraicSpaceOver s.base s.isomFunctor
```

**`AlgebraicGeometry.Space.HomSituation.mutualInverseFunctorIsoIsom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeIsomMutualInverse.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/RelativeIsomMutualInverse.lean#L272). The attribute's comment: “ONLY the identification Isom(F,G) = (H' x_B H) x_{c, I x_B I', sigma} B that the proof rests on, with no hypothesis on f, F or G. The conclusion of Stacks 08K9 — that Isom(F,G) is an algebraic space affine of finite presentation over B — is NOT covered. It needs, first, the conclusion of Stacks 08K6 for the four Hom functors, which this development does not have (Stacks 08K6 in turn needs Stacks 08JY, 08JV, 07V7 and 08K2, of which only Stacks 08K2 is proved in this library, as AlgebraicGeometry.Space.MorphismDescentSituation.exists_isProperOver_supportOfSheaf_moduleAt); and second, stability of AlgebraicGeometry.Space.IsAffineHom and of AlgebraicGeometry.Space.IsFinitePresentation under base change along a morphism of algebraic spaces, which this library does not prove — only isAffineHom_comp and isLocallyOfFinitePresentation_of_comp exist — and which the fibre-product step needs. The remaining inputs of the source's proof, Stacks 03KP parts (1)-(4) and Stacks 05WT, ARE available, in StacksFrontier/AlgebraicGeometry/Spaces/SeparatedCriteria.lean and StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FinitePresentation.lean”. References: SGA 6 XII (2.4), “partial”.

> The functor of mutually inverse pairs `(H' ×_B H) ×_{c, I ×_B I', σ} B` is isomorphic to
> the relative Isom functor `Isom(F, G)` of Stacks 08K7.

```lean
def mutualInverseFunctorIsoIsom : s.mutualInverseFunctor ≅ s.isomFunctor
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 99.4, Tag 08K7](https://stacks.math.columbia.edu/tag/08K7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
