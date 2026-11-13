---
declaration: section
origin: cited
lean: Deformation.GroupoidInFunctors.IsNormalized, Deformation.GroupoidInFunctors.IsMinimal, Deformation.GroupoidInFunctors.exists_isMinimalVersal_of_isMinimal, Deformation.GroupoidInFunctors.exists_quotientMorphism_iso_associatedMorphism_of_isMinimal, Deformation.GroupoidInFunctors.isNormalized_iff_bijective_quotientDifferential, Deformation.GroupoidInFunctors.isMinimal_iff_quotientDifferential_ker_le_derivationRange, Deformation.isIso_of_tangentSpace_bijective, Deformation.GroupoidInFunctors.isIso_quotientMap_of_isEquivalence
statement: formalized
proof: formalized
---

# 90.27 Remarks regarding minimality

Section 90.27 of the Stacks Project, [Tag 06TD](https://stacks.math.columbia.edu/tag/06TD). 8 tags here are carried by 16 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06KM, a definition

[Tag 06KM](https://stacks.math.columbia.edu/tag/06KM) in the Stacks Project.

**`Deformation.GroupoidInFunctors.IsNormalized`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Minimality.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Minimality.lean#L65). The attribute's comment: “normalized”. References: SGA 7 VI (2.11), “normalized”.

> **Stacks Project, Tag 06KM, part (1).** A smooth prorepresentable groupoid in functors
> `(U, R, s, t, c)` is *normalized* when the groupoid `(U(k[ε]), R(k[ε]), s, t, c)` obtained by
> evaluating at the dual numbers `k[ε]` is totally disconnected: there are no arrows between
> distinct objects.
>
> Total disconnection is stated here in the equivalent pointwise form: every element of
> `R(k[ε])`, i.e. every arrow of the evaluated groupoid, has equal source and target.

```lean
public abbrev IsNormalized (G : GroupoidInFunctors
  (ArtinianLocalAlgCat.{u, max v w, w} Λ k)) : Prop
```

**`Deformation.GroupoidInFunctors.IsMinimal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Minimality.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Minimality.lean#L92). The attribute's comment: “minimal”.

> **Stacks Project, Tag 06KM, part (2).** A smooth prorepresentable groupoid in functors
> `(U, R, s, t, c)` is *minimal* when the quotient morphism `U → [U/R]` is given by a minimal
> versal formal object of `[U/R]`.
>
> Here `p : [U/R] ⥤ 𝒞_Λ` is the structure morphism of the quotient category, realized as
> `Grothendieck.forget (evaluationFunctor G)`, and the data asserted to exist are:
>
> * `ξ`, a formal object of `[U/R]`, required by the first conjunct to be minimal versal
>   (`IsMinimalVersal`, Tag 06T4): this is the source's "minimal versal formal object
>   of `[U/R]`";
> * `pushforwards`, a choice of cocartesian pushforwards in `[U/R]`. This is the auxiliary
>   data needed to build the morphism `ξ^#` associated to `ξ` (`associatedMorphism`, Tag
>   06HC), which goes from the category of elements of `restrictedCoyoneda ξ.base` to
>   `[U/R]`; "the morphism given by `ξ`" means `ξ^#`;
> * `e`, an equivalence from the category of elements of the object functor `U` to that of
>   `restrictedCoyoneda ξ.base`. The second conjunct, `e.functor ⋙ π = π`, says that `e`
>   commutes with the projections to `𝒞_Λ`, i.e. that it is an equivalence *over* `𝒞_Λ`;
>   it is this that lets `ξ^#` be read as a morphism `e.functor ⋙ ξ^#` out of `U`;
> * the third conjunct: a natural isomorphism `α` from `quotientMorphism G`, which is the
>   quotient morphism `U → [U/R]`, to `e.functor ⋙ ξ^#`, every component of which lies over
>   an identity arrow of `𝒞_Λ` (`Functor.IsHomLift p (𝟙 X.1)`). Being isomorphic by such a
>   vertical natural isomorphism is the sense in which `U → [U/R]` *is* given by `ξ`.

```lean
public def IsMinimal
    (G : GroupoidInFunctors.{_, max v w, max (max v w) z}
      (ArtinianLocalAlgCat.{u, max v w, w} Λ k)) : Prop
```

**`Deformation.GroupoidInFunctors.exists_isMinimalVersal_of_isMinimal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Minimality.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Minimality.lean#L114). The attribute's comment: “minimal: the quotient has a minimal versal formal object”.

> **Stacks Project, Tag 06KM, part (2).** A minimal groupoid in functors has a minimal versal
> formal object of its quotient: the object `ξ` whose associated morphism the quotient morphism
> `U → [U/R]` is given by. This states the first conjunct of `IsMinimal` on its own, so that the
> content of part (2) is available as a theorem and not only inside the definition.

```lean
public theorem exists_isMinimalVersal_of_isMinimal
    {G : GroupoidInFunctors.{_, max v w, max (max v w) z}
      (ArtinianLocalAlgCat.{u, max v w, w} Λ k)}
    (hG : IsMinimal.{u, v, w, z} G) :
    ∃ ξ : FormalObject (Grothendieck.forget (evaluationFunctor G)),
      IsMinimalVersal (quotientProjection_cofibered G) ξ
```

**`Deformation.GroupoidInFunctors.exists_quotientMorphism_iso_associatedMorphism_of_isMinimal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Minimality.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Minimality.lean#L128). The attribute's comment: “minimal: the quotient morphism is the one associated to that object”.

> **Stacks Project, Tag 06KM, part (2).** For a minimal groupoid in functors, the quotient
> morphism `U → [U/R]` is, up to a vertical natural isomorphism and the equivalence
> prorepresenting `U`, the morphism associated to a minimal versal formal object of `[U/R]`. This
> is part (2) in full, stated as a theorem.

```lean
public theorem exists_quotientMorphism_iso_associatedMorphism_of_isMinimal
    {G : GroupoidInFunctors.{_, max v w, max (max v w) z}
      (ArtinianLocalAlgCat.{u, max v w, w} Λ k)}
    (hG : IsMinimal.{u, v, w, z} G) :
    ∃ (ξ : FormalObject (Grothendieck.forget (evaluationFunctor G)))
      (pushforwards : ChosenPushforwards (Grothendieck.forget (evaluationFunctor G)))
      (e : G.objects.Elements ≌ (restrictedCoyoneda ξ.base).Elements),
      IsMinimalVersal (quotientProjection_cofibered G) ξ ∧
      (e.functor ⋙ Functor.Elements.π (restrictedCoyoneda ξ.base) =
        Functor.Elements.π G.objects) ∧
      Nonempty
        { α : quotientMorphism G ≅
            e.functor ⋙ (associatedMorphism (quotientProjection_cofibered G) ξ
              pushforwards).toBasedFunctor.toFunctor //
          ∀ X : G.objects.Elements,
            CategoryTheory.Functor.IsHomLift
              (Grothendieck.forget (evaluationFunctor G)) (𝟙 X.1) (α.hom.app X) }
```

## Tag 06KN, a lemma

[Tag 06KN](https://stacks.math.columbia.edu/tag/06KN) in the Stacks Project.

**`Deformation.GroupoidInFunctors.isNormalized_iff_bijective_quotientDifferential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/GroupoidQuotient/Minimality.lean, line 716](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/GroupoidQuotient/Minimality.lean#L716). The attribute's comment: “part (1): normalized iff isomorphism on tangent spaces”.

> A groupoid in functors is normalized precisely when the quotient morphism `U → [U/R]` induces
> an isomorphism on tangent spaces.

```lean
public theorem isNormalized_iff_bijective_quotientDifferential
    (G : GroupoidInFunctors (ArtinianLocalAlgCat.{u, max v w, w} Λ k)) :
    IsNormalized.{u, v, w} G ↔ Function.Bijective (quotientDifferential.{u, v, w} G)
```

**`Deformation.GroupoidInFunctors.isMinimal_iff_quotientDifferential_ker_le_derivationRange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/GroupoidQuotient/Minimality.lean, line 852](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/GroupoidQuotient/Minimality.lean#L852). The attribute's comment: “part (2): minimal iff the kernel of the differential lies in the image of Der”.

> A smooth prorepresentable groupoid in functors is minimal precisely when the kernel of the
> differential of `U → [U/R]` is contained in the image of the canonical map `Der_Λ(k, k) → TU`.

```lean
public theorem isMinimal_iff_quotientDifferential_ker_le_derivationRange
    [IsNoetherianRing Λ] [Module.Finite Λ k]
    (hpro : IsProrepresentable G) (hsmooth : IsSmooth G) :
    IsMinimal.{u, v, w, v} G ↔
      ∀ x : tangentSpaceArtinian.{u, w, v} Λ k
          (isomorphismClasses (BasedCategory.ofFunctor (Functor.Elements.π G.objects))
            (categoryOfElements_projection_isCofibered G.objects)),
        quotientDifferential.{u, v, w} G x =
            quotientDifferential.{u, v, w} G
              (derivationToTangentSpace (Functor.Elements.π G.objects)
                (objects_isPredeformationCategory_of_isProrepresentable G hpro) 0) →
          x ∈ Set.range (derivationToTangentSpace (Functor.Elements.π G.objects)
            (objects_isPredeformationCategory_of_isProrepresentable G hpro))
```

## Tag 06KP, a lemma

[Tag 06KP](https://stacks.math.columbia.edu/tag/06KP) in the Stacks Project.

**`Deformation.isIso_of_tangentSpace_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Predeformation/ProrepresentableEndomorphism.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Predeformation/ProrepresentableEndomorphism.lean#L60).

> **Stacks Project, Tag 06KP.** An endomorphism of a prorepresentable functor on Artinian
> local `Λ`-algebras whose differential — its component at the dual numbers — is bijective is an
> isomorphism.

```lean
theorem isIso_of_tangentSpace_bijective
    (U : ArtinianLocalAlgCat.{u, max v w, w} Λ k ⥤ Type (max v w))
    (hU : IsProrepresentable U) (φ : U ⟶ U)
    (hφ : Function.Bijective (φ.app (artinianDualNumbers Λ k))) :
    IsIso φ
```

## Tag 06KQ, a lemma

[Tag 06KQ](https://stacks.math.columbia.edu/tag/06KQ) in the Stacks Project.

**`Deformation.GroupoidInFunctors.isIso_quotientMap_of_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/GroupoidQuotient/MinimalAutoequivalence.lean, line 485](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/GroupoidQuotient/MinimalAutoequivalence.lean#L485). The attribute's comment: “equivalence taken as induced by an endomorphism of the groupoid, and the conclusion read as strict isomorphism of categories. Neither is the source's reading, so this is an auxiliary and not the tag's covering declaration: the tag is carried outright by `Deformation.GroupoidInFunctors.exists_isIso_hom_of_isEquivalence_endo`, which takes an arbitrary 1-morphism of the quotients over 𝒞\_Λ whose functor is an equivalence of categories and concludes that it is isomorphic to the one induced by an isomorphism of groupoids in functors. What this auxiliary adds is that the induced functor is then an isomorphism of categories on the nose, which is stronger than the source's conclusion and not invariant under isomorphism of functors”.

> **Stacks Project, Tag 06KQ.** Let `(U, R, s, t, c)` be a minimal smooth prorepresentable
> groupoid in functors on `𝒞_Λ`. An equivalence `[U/R] → [U/R]` of categories cofibered in
> groupoids induced by an endomorphism of the groupoid is an isomorphism of categories.

```lean
public theorem isIso_quotientMap_of_isEquivalence [IsNoetherianRing Λ] [Module.Finite Λ k]
    (hpro : IsProrepresentable G) (hsmooth : IsSmooth G) (hmin : IsMinimal.{u, v, w, v} G)
    (f : G ⟶ G) [(quotientMap f).IsEquivalence] :
    IsIso (quotientMap f).toCatHom
```

**`Deformation.GroupoidInFunctors.exists_isIso_hom_of_isEquivalence_endo`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/GroupoidQuotient/MinimalEquivalence.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/GroupoidQuotient/MinimalEquivalence.lean#L257).

> **Stacks Project, Tag 06KQ.** Let `(U, R, s, t, c)` be a minimal smooth prorepresentable
> groupoid in functors on `𝒞_Λ`. A `1`-morphism `[U/R] → [U/R]` over `𝒞_Λ` whose functor is an
> equivalence of categories is an isomorphism: it is isomorphic to the functor induced by an
> **isomorphism** of groupoids in functors, and therefore has a two-sided inverse `1`-morphism
> over `𝒞_Λ` up to `2`-isomorphism, by
> `Deformation.GroupoidInFunctors.exists_inverse_morphismOver_of_isIso`.
>
> The `1`-morphism is realised by a morphism `F` of groupoids in functors, which is the assertion
> opening the source proof and is
> `Deformation.GroupoidInFunctors.exists_hom_of_morphismOver`; the functor induced by `F` is then
> an equivalence, so `F` is an isomorphism by
> `Deformation.GroupoidInFunctors.isIso_of_quotientMap_isEquivalence`, which is the differential
> argument of the source proof.

```lean
theorem exists_isIso_hom_of_isEquivalence_endo [IsNoetherianRing Λ] [Module.Finite Λ k]
    (hpro : IsProrepresentable G) (hsmooth : IsSmooth G) (hmin : IsMinimal.{u, v, w, v} G)
    (Φ : StacksRepresentableCFG.MorphismOver
      (Grothendieck.forget (evaluationFunctor G))
      (Grothendieck.forget (evaluationFunctor G))) [Φ.functor.IsEquivalence] :
    ∃ F : G ⟶ G, IsIso F ∧ Nonempty (quotientMap F ≅ Φ.functor)
```

## Tag 06KR, a lemma

[Tag 06KR](https://stacks.math.columbia.edu/tag/06KR) in the Stacks Project.

**`Deformation.GroupoidInFunctors.isIso_quotientMap_of_quotientMaps_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/GroupoidQuotient/MinimalEquivalence.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/GroupoidQuotient/MinimalEquivalence.lean#L142). The attribute's comment: “equivalence and quasi-inverse taken as induced by morphisms of groupoids, and the conclusion read as strict isomorphism of categories. Neither is the source's reading, so this is an auxiliary and not the tag's covering declaration: the tag is carried outright by `Deformation.GroupoidInFunctors.exists_isIso_hom_of_isEquivalence` below, which takes an arbitrary 1-morphism of the quotients over 𝒞\_Λ whose functor is an equivalence of categories. What this auxiliary adds is that the induced functor is then an isomorphism of categories on the nose, which is stronger than the source's conclusion and not invariant under isomorphism of functors”.

> An equivalence `[U/R] → [U'/R']` of minimal smooth prorepresentable quotients induced by a
> morphism of groupoids in functors, and admitting a quasi-inverse induced by one in the opposite
> direction, induces an isomorphism of categories on the nose.

```lean
public theorem isIso_quotientMap_of_quotientMaps_isEquivalence
    [IsNoetherianRing Λ] [Module.Finite Λ k]
    (hproG : IsProrepresentable G) (hsmoothG : IsSmooth G) (hminG : IsMinimal.{u, v, w, v} G)
    (hproH : IsProrepresentable H) (hsmoothH : IsSmooth H) (hminH : IsMinimal.{u, v, w, v} H)
    (F : G ⟶ H) (F' : H ⟶ G)
    [(quotientMap F).IsEquivalence] [(quotientMap F').IsEquivalence] :
    IsIso (quotientMap F).toCatHom
```

**`Deformation.GroupoidInFunctors.exists_isIso_hom_of_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/GroupoidQuotient/MinimalEquivalence.lean, line 279](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/GroupoidQuotient/MinimalEquivalence.lean#L279).

> **Stacks Project, Tag 06KR.** Let `(U, R, s, t, c)` and `(U', R', s', t', c')` be minimal
> smooth prorepresentable groupoids in functors on `𝒞_Λ`. A `1`-morphism `[U/R] → [U'/R']` over
> `𝒞_Λ` whose functor is an equivalence of categories is an isomorphism: it is isomorphic to the
> functor induced by an **isomorphism** of groupoids in functors, and therefore has a two-sided
> inverse `1`-morphism over `𝒞_Λ` up to `2`-isomorphism, by
> `Deformation.GroupoidInFunctors.exists_inverse_morphismOver_of_isIso`.
>
> This is the source's proof: a quasi-inverse of the given `1`-morphism, corrected to lie over
> `𝒞_Λ` by `Deformation.GroupoidInFunctors.inverseMorphismOver`, is realised by a morphism of
> groupoids in functors in the opposite direction, and the two composites are autoequivalences of
> the two quotients, hence isomorphisms by Tag 06KQ.

```lean
theorem exists_isIso_hom_of_isEquivalence [IsNoetherianRing Λ] [Module.Finite Λ k]
    (hproG : IsProrepresentable G) (hsmoothG : IsSmooth G) (hminG : IsMinimal.{u, v, w, v} G)
    (hproH : IsProrepresentable H) (hsmoothH : IsSmooth H) (hminH : IsMinimal.{u, v, w, v} H)
    (Φ : StacksRepresentableCFG.MorphismOver
      (Grothendieck.forget (evaluationFunctor G))
      (Grothendieck.forget (evaluationFunctor H))) [Φ.functor.IsEquivalence] :
    ∃ F : G ⟶ H, IsIso F ∧ Nonempty (quotientMap F ≅ Φ.functor)
```

## Tag 06L2, a lemma

[Tag 06L2](https://stacks.math.columbia.edu/tag/06L2) in the Stacks Project.

**`Deformation.exists_minimalPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/CofiberedPresentation/MinimalPresentation.lean, line 567](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/CofiberedPresentation/MinimalPresentation.lean#L567).

> **Stacks Project, Tag 06L2.** Let `ℱ` be a deformation category over `𝒞_Λ` with
> `dim_k Tℱ < ∞` and `dim_k Inf(ℱ) < ∞`. Then there is a minimal versal formal object `ξ` of
> `ℱ`, say over `R`, and, with `U = R̲|_{𝒞_Λ}` and `f = ξ : U → ℱ` the associated morphism, the
> groupoid in functors `(U, R, s, t, c)` constructed from `f` in Tag 06KY is a minimal smooth
> prorepresentable groupoid in functors on `𝒞_Λ` with `[U/R] → ℱ` an equivalence.
>
> The two `Fact` instances carry no content beyond `hp`; they make Tag 06IH's canonical
> `k`-vector space structure on the tangent space available, so that the finite dimensionality
> of `Tℱ` can be stated.

```lean
public theorem exists_minimalPresentation [IsNoetherianRing Λ] [Module.Finite Λ k]
    (p : F ⥤ ArtinianLocalAlgCat.{u, max v v₃ w, w} Λ k)
    (hp : IsDeformationCategory.{u, max v v₃, w} p)
    [h𝓕 : Fact (IsPredeformationCategory.{u, max v v₃, w} (BasedCategory.ofFunctor p).p)]
    [Fact (SchlessingerConditionS2 (Functor.Elements.π
      (isomorphismClasses (BasedCategory.ofFunctor p) h𝓕.out.cofibered)))]
    [FiniteDimensional k (tangentSpaceArtinian.{u, w, max v v₃} Λ k
      (isomorphismClasses (BasedCategory.ofFunctor p) h𝓕.out.cofibered))]
    (hInf : ∀ (x : F) (_hbase : p.obj x = residueFieldObject.{u, max v v₃, w} Λ k)
      (PF : ChosenPushforwardsAt p x), FiniteDimensional k
        ↥((infinitesimalAutomorphismLinearLift.{u, max v v₃, w} PF hp.satisfiesRS).functor.obj
          (FGModuleCat.of k (ULift.{max v v₃} k)))) :
    Nonempty (MinimalPresentation.{u, v, w, u₃, v₃} p hp.predeformation.cofibered)
```

## Tag 06L3, a lemma

[Tag 06L3](https://stacks.math.columbia.edu/tag/06L3) in the Stacks Project.

**`Deformation.GroupoidInFunctors.nonempty_iso_of_presentations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/CofiberedPresentation/MinimalUniqueness.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/CofiberedPresentation/MinimalUniqueness.lean#L104). The attribute's comment: “the statement is specialised to third universe `max v w`, that is `IsMinimal.{u, v, w, v}`, which is where Stacks 06KR and the Stacks 06KQ under it are fixed; `IsNoetherianRing Λ` and `Module.Finite Λ k` are the chapter's standing assumptions on Λ, which Stacks 06KQ consumes”.

> **Stacks Project, Tag 06L3.** Let `ℱ` be a category cofibered in groupoids over `𝒞_Λ`.
> If `ℱ` admits presentations by minimal smooth prorepresentable groupoids in functors
> `(U, R, s, t, c)` and `(U', R', s', t', c')`, then the two are isomorphic.
>
> The two presentations compose to an equivalence `[U/R] → [U'/R']` over `𝒞_Λ`. Both its
> forward and its backward 1-morphism of quotients is induced, up to isomorphism of functors, by
> a morphism of groupoids in functors, so the forward morphism induces an equivalence of the
> quotients whose quasi-inverse is induced as well, and it is therefore an isomorphism by
> Tag 06KR.

```lean
public theorem nonempty_iso_of_presentations [IsNoetherianRing Λ] [Module.Finite Λ k]
    {ℱ : Type u₁} [Category.{v₁} ℱ] (p : ℱ ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k)
    (hp : Deformation.IsCofiberedInGroupoids p)
    (G H : GroupoidInFunctors.{_, max v w, max v w}
      (ArtinianLocalAlgCat.{u, max v w, w} Λ k))
    (hGpro : IsProrepresentable G) (hGsmooth : IsSmooth G) (hGmin : IsMinimal.{u, v, w, v} G)
    (hGpres : Deformation.Presentation G p)
    (hHpro : IsProrepresentable H) (hHsmooth : IsSmooth H) (hHmin : IsMinimal.{u, v, w, v} H)
    (hHpres : Deformation.Presentation H p) :
    Nonempty (G ≅ H)
```

## Tag 06TE, a theorem

[Tag 06TE](https://stacks.math.columbia.edu/tag/06TE) in the Stacks Project.

**`Deformation.hasNormalizedPresentation_iff_hasMinimalPresentation_of_isSeparable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/CofiberedPresentation/Criteria.lean, line 560](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/CofiberedPresentation/Criteria.lean#L560). The attribute's comment: “the separability clause of the tag: when k' ⊂ k is separable, condition (1), a normalized smooth prorepresentable presentation, is equivalent to the other three. Proved outright. Separability is read as Algebra.IsSeparable (residueImageField Λ k) k, and the equivalence of (1) with conditions (2), (3), (4) is this equivalence with (3) together with the equivalence of (2), (3), (4) in Deformation.hasSmoothPresentation\_tfae; the four-way equivalence is assembled as Deformation.tfae\_of\_isSeparable”.

> **Stacks Project, Tag 06TE**, the separable case. When `k` is separable over the image
> field of `Λ` the residue field carries no nonzero `Λ`-derivation, so a minimal smooth
> prorepresentable presentation is normalized and conditions (1) and (3) agree.

```lean
theorem hasNormalizedPresentation_iff_hasMinimalPresentation_of_isSeparable
    [IsNoetherianRing Λ] [Module.Finite Λ k]
    [Algebra.IsSeparable (residueImageField Λ k) k] :
    HasNormalizedPresentation.{u, v, w} p ↔ HasMinimalPresentation.{u, v, w} p
```

**`Deformation.hasSmoothPresentation_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/CofiberedPresentation/Criteria.lean, line 595](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/CofiberedPresentation/Criteria.lean#L595). The attribute's comment: “the tag: for ℱ cofibered in groupoids over 𝒞\_Λ, conditions (2) a smooth prorepresentable presentation, (3) a minimal one, and (4) ℱ a deformation category with dim\_k Tℱ and dim\_k Inf(ℱ) finite, are equivalent and implied by (1) a normalized one, and all four are equivalent when k' ⊂ k is separable. Delivered outright and with no carried hypothesis: (1) ⟹ (3), (3) ⟹ (2), (4) ⟹ (3), (2) ⟹ (4) — the last from Deformation.hasSmoothPresentation\_iff\_isFiniteDimensionalDeformationCategory, Stacks 06L8 — and (3) ⟺ (1) whenever Der\_Λ(k, k) vanishes. Nothing is assumed: this theorem takes no hypothesis beyond the chapter's standing IsNoetherianRing Λ and Module.Finite Λ k, and the vanishing of Der\_Λ(k, k) is the antecedent of the fourth conjunct, which is proved outright as an implication. Separability of k' ⊂ k supplies that vanishing, by Deformation.derivation\_eq\_zero\_of\_residueImageField\_separable, so the fourth conjunct is at least as strong as the source's separable clause; that clause itself, as the four-way equivalence, is Deformation.tfae\_of\_isSeparable, also carrying this tag. The final uniqueness clause of the tag is not here: it is Stacks 06L3, carried by this tag's add\_to\_stacks on Deformation.GroupoidInFunctors.nonempty\_iso\_of\_presentations, and it too is delivered outright — the realisation of a 1-morphism of quotients by a morphism of groupoids in functors, which that proof attributes to Definition 06KB, is proved as Deformation.GroupoidInFunctors.exists\_hom\_of\_morphismOver. No part of this tag is conditional. The statement is specialised to a hom-set universe of ℱ equal to the value universe v of the groupoids in functors, which is where Stacks 06L2 and Stacks 06L3 meet”.

> **Stacks Project, Tag 06TE.** Conditions (2), (3) and (4) are equivalent, and (1) implies
> them; when the residue field carries no nonzero `Λ`-derivation all four are equivalent.
>
> The implications are (1) implies (3) and (3) implies (2), from Tag 06KN and the definitions,
> (4) implies (3), from Tag 06L2, and (2) implies (4), from Tag 06L8; the equivalence of (1)
> and (3) under `hzero` is the other half of Tag 06KN.

```lean
theorem hasSmoothPresentation_tfae [IsNoetherianRing Λ] [Module.Finite Λ k] :
    (HasNormalizedPresentation.{u, v, w} p → HasMinimalPresentation.{u, v, w} p) ∧
      (HasSmoothPresentation.{u, v, w} p ↔ HasMinimalPresentation.{u, v, w} p) ∧
      (HasSmoothPresentation.{u, v, w} p ↔
        IsFiniteDimensionalDeformationCategory.{u, v, w} p) ∧
      ((∀ δ : Derivation Λ k k, δ = 0) →
        (HasNormalizedPresentation.{u, v, w} p ↔ HasMinimalPresentation.{u, v, w} p))
```

**`Deformation.tfae_of_isSeparable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/CofiberedPresentation/Criteria.lean, line 629](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/CofiberedPresentation/Criteria.lean#L629). The attribute's comment: “the tag's final equivalence, assembled: under separability of k' ⊂ k the four conditions (1) a normalized smooth prorepresentable presentation, (2) a smooth prorepresentable one, (3) a minimal one, and (4) ℱ a deformation category with dim\_k Tℱ and dim\_k Inf(ℱ) finite are all equivalent. Proved outright, with no carried hypothesis. Separability is read as Algebra.IsSeparable (residueImageField Λ k) k. The statement is specialised to a hom-set universe of ℱ equal to the value universe v of the groupoids in functors, which is where Stacks 06L2 and Stacks 06L3 meet. The uniqueness clause of the tag is separate and is also delivered outright: see this tag's add\_to\_stacks on Deformation.GroupoidInFunctors.nonempty\_iso\_of\_presentations”.

> **Stacks Project, Tag 06TE**, the four-way equivalence under separability. When `k` is
> separable over the image field of `Λ`, a category cofibered in groupoids over `𝒞_Λ` admits a
> presentation by a normalized smooth prorepresentable groupoid in functors if and only if it
> admits one by a smooth prorepresentable groupoid in functors, if and only if it admits one by
> a minimal smooth prorepresentable groupoid in functors, if and only if it is a deformation
> category whose tangent space and whose space of infinitesimal automorphisms are
> finite dimensional over `k`.
>
> The cycle is (1) implies (3) by Tag 06KN, (3) implies (2) by the definitions, (2) implies (4)
> by Tag 06L8, and (4) implies (1) by Tag 06L2 followed by the separable half of Tag 06KN.

```lean
theorem tfae_of_isSeparable [IsNoetherianRing Λ] [Module.Finite Λ k]
    [Algebra.IsSeparable (residueImageField Λ k) k] :
    List.TFAE [HasNormalizedPresentation.{u, v, w} p, HasSmoothPresentation.{u, v, w} p,
      HasMinimalPresentation.{u, v, w} p,
      IsFiniteDimensionalDeformationCategory.{u, v, w} p]
```

Declarations registered for the tag:

- [`Deformation.GroupoidInFunctors.nonempty_iso_of_presentations`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/CofiberedPresentation/MinimalUniqueness.lean#L104), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Deformation/CofiberedPresentation/Criteria.lean, line 646](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/CofiberedPresentation/Criteria.lean#L646) (StacksFrontier): “the final uniqueness clause of the tag: the minimal smooth prorepresentable groupoids in functors which present a given category cofibered in groupoids over 𝒞\_Λ are unique up to isomorphism. This is Stacks 06L3, delivered outright: the realisation it rests on — that a 1-morphism of quotients over 𝒞\_Λ is, up to isomorphism of functors, the one induced by a morphism of groupoids in functors, the step the source proof attributes to Definition 06KB — is proved as Deformation.GroupoidInFunctors.exists\_hom\_of\_morphismOver, for a prorepresentable source and a smooth target, which both presentations here supply. No part of Stacks 06TE is conditional; for the equivalence of the four conditions see Deformation.hasSmoothPresentation\_tfae and Deformation.tfae\_of\_isSeparable”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 90.27, Tag 06TD](https://stacks.math.columbia.edu/tag/06TD)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
