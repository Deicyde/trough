---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.supp_restrictToChart_eq_preimage_supportOfSheaf_of_isQuasicoherent, AlgebraicGeometry.Space.nontrivial_geometricModuleStalk_iff_nontrivial_residueFibre, AlgebraicGeometry.Space.supportOfSheaf_modulePullback_eq, AlgebraicGeometry.Space.isClosed_supportOfSheaf_of_isFiniteTypeOnSite, AlgebraicGeometry.Space.supportOfSheaf_of_isQuasicoherentOnSite_isFiniteTypeOnSite, AlgebraicGeometry.Space.mem_supportOfSheaf_iff_nontrivial_geometricModuleStalk_of_liesOver, AlgebraicGeometry.Space.supportOfSheaf_eq_range_pointsMap_schemeTheoreticSupport, AlgebraicGeometry.Space.exists_module_on_schemeTheoreticSupport
statement: formalized
proof: formalized
---

# 67.15 Supports of modules

Section 67.15 of the Stacks Project, [Tag 07TX](https://stacks.math.columbia.edu/tag/07TX). 4 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07TY, a lemma

[Tag 07TY](https://stacks.math.columbia.edu/tag/07TY) in the Stacks Project.

**`AlgebraicGeometry.Space.supp_restrictToChart_eq_preimage_supportOfSheaf_of_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SupportGeometricStalkCriterion.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SupportGeometricStalkCriterion.lean#L91). The attribute's comment: “the support of a quasi-coherent module pulled back along an étale chart”.

> **Stacks 07TY.** Let `X` be an algebraic space over `S`, let `F` be a quasi-coherent
> `𝒪_X`-module and let `φ : U ⟶ X` be an étale morphism from a scheme, that is, an object of the
> small étale site of `X`.  Then the support of `φ^* F` as a module on the *scheme* `U` is the
> inverse image under `|φ|` of the support of `F`:
> `Supp(φ^* F) = |φ|^{-1}(Supp(F))`.
>
> The proof is `AlgebraicGeometry.Space.supp_restrictToChart_eq_preimage_supportOfSheaf` with its
> comparison `(φ^* F)_u ⊗_{𝒪_{U, u}} 𝒪_{X, x̄} ≅ F_{x̄}` supplied by Stacks 05VP,
> `AlgebraicGeometry.Space.isIso_chartStalkTensorComparison`, which holds because `F` is
> quasi-coherent.

```lean
theorem supp_restrictToChart_eq_preimage_supportOfSheaf_of_isQuasicoherent
    (X : AlgebraicSpaces B S hS) (U : SmallEtale B S hS X.1)
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite] :
    SheafOfModules.supp (restrictToChart B S hS X.2 F U) =
      (fun u => pointsMap B S hS (yoneda.obj ((SmallEtale.toOver B S hS X.1).obj U))
          U.obj.hom
          ((pointsEquivScheme B S hS ((SmallEtale.toOver B S hS X.1).obj U)).symm u)) ⁻¹'
        supportOfSheaf B S hS X.1 ((SheafOfModules.toSheaf _).obj F)
```

## Tag 07TZ, a lemma

[Tag 07TZ](https://stacks.math.columbia.edu/tag/07TZ) in the Stacks Project.

**`AlgebraicGeometry.Space.nontrivial_geometricModuleStalk_iff_nontrivial_residueFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricStalkResidueFibre.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GeometricStalkResidueFibre.lean#L105). The attribute's comment: “part (2), second equivalence: the stalk at a geometric point is nonzero iff the fibre over the residue field is nonzero”.

> **Stacks 07TZ, part (2), second equivalence.** Let `F` be a quasi-coherent `𝒪_X`-module of
> finite type on an algebraic space `X` over `S` and let `x̄` be a geometric point of `X`.  Then
>
> `F_{x̄} ≠ 0 ↔ F_{x̄} ⊗_{𝒪_{X, x̄}} κ(x̄) ≠ 0`.
>
> This is Nakayama's lemma.  The stalk is a finite module over the étale local ring by
> `AlgebraicGeometry.Space.module_finite_geometricModuleStalk`, and the residue map is a local
> homomorphism of local rings, so base change along it keeps a nonzero finite module nonzero
> (`AlgebraicGeometry.Space.nontrivial_extendScalars_of_isLocalHom`); the converse direction
> needs no hypotheses at all
> (`AlgebraicGeometry.Space.nontrivial_of_nontrivial_extendScalars`).

```lean
theorem nontrivial_geometricModuleStalk_iff_nontrivial_residueFibre (X : AlgebraicSpaces B S hS)
    (F : Modules.{u, u} B S hS X.1 X.2) (hqc : F.IsQuasicoherentOnSite)
    (hft : SheafOfModules.IsFiniteTypeOnSite F) (x : GeometricPoint B S hS X.1) :
    Nontrivial ↥(geometricModuleStalk B S hS X x F) ↔
      letI := isLocalRing_etaleLocalRing B S hS X.1 X.2 x
      Nontrivial ↥(geometricModuleResidueFibre B S hS X x F)
```

**`AlgebraicGeometry.Space.supportOfSheaf_modulePullback_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModulePullbackSupportEquality.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ModulePullbackSupportEquality.lean#L228). The attribute's comment: “part (3): the stalk of a pullback at a geometric point, and the equality of supports”.

> **Stacks 07TZ, part (3).** Let `g : X' ⟶ X` be a morphism of algebraic spaces over `S` and
> let `F` be a quasi-coherent `𝒪_X`-module of finite type.  Then the support of the pullback
> `g^* F` of Stacks 03LU is the inverse image of the support of `F`:
>
> `Supp(g^* F) = |g|^{-1}(Supp(F))`.
>
> The pullback is again of finite type by Stacks 03DO,
> `AlgebraicGeometry.Space.isFiniteTypeOnSite_modulePullback`, which is the other clause of this
> part of the tag.
>
> At a geometric point `ȳ` of `X'` the stalk of the pullback is the base change
> `(g^* F)_{ȳ} ≅ 𝒪_{X', ȳ} ⊗_{𝒪_{X, g ∘ ȳ}} F_{g ∘ ȳ}` of the stalk of `F` at the image
> geometric point, by `AlgebraicGeometry.Space.geometricModuleStalkPullbackIso`.  One inclusion
> is `AlgebraicGeometry.Space.nontrivial_of_nontrivial_extendScalars`, which needs no
> hypotheses.  The other is `AlgebraicGeometry.Space.nontrivial_extendScalars_of_isLocalHom`: the
> stalk of `F` is a finite module over the étale local ring, the homomorphism of étale local
> rings of Stacks 04NG is local, and the image geometric point detects the support because `F` is
> quasi-coherent (the first equivalence of part (2)).

```lean
theorem supportOfSheaf_modulePullback_eq (g : X' ⟶ X) (F : Modules.{u, u} B S hS X.1 X.2)
    (hqc : F.IsQuasicoherentOnSite) (hft : SheafOfModules.IsFiniteTypeOnSite F) :
    supportOfSheaf B S hS X'.1
        ((SheafOfModules.toSheaf _).obj ((modulePullback B S hS g).obj F)) =
      pointsMap B S hS X'.1 g.hom ⁻¹'
        supportOfSheaf B S hS X.1 ((SheafOfModules.toSheaf _).obj F)
```

**`AlgebraicGeometry.Space.isClosed_supportOfSheaf_of_isFiniteTypeOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SupportClosedFiniteType.lean, line 335](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SupportClosedFiniteType.lean#L335). The attribute's comment: “support\_closed”.

> **Stacks 07TZ, part (1).** The support of an `𝒪_X`-module of finite type on an algebraic
> space `X` is closed in the point set of `X`.
>
> Outside the support pick a geometric point over the given point; its stalk vanishes, so there
> is an étale chart carrying only the zero section of the module.  The image of the point set of
> that chart is open, because an étale chart is open on points by clause (3) of Stacks 03BX, it
> contains the given point, and it misses the support: a geometric point of `X` over a point of
> the image lifts to the chart by Stacks 05VN, so the chart is a neighbourhood of it and its
> stalk vanishes too.

```lean
theorem isClosed_supportOfSheaf_of_isFiniteTypeOnSite (hX : IsAlgebraicSpace B S hS X)
    (F : Modules.{u, m} B S hS X hX) [SheafOfModules.IsFiniteTypeOnSite F] :
    IsClosed (supportOfSheaf B S hS X ((SheafOfModules.toSheaf _).obj F))
```

**`AlgebraicGeometry.Space.supportOfSheaf_of_isQuasicoherentOnSite_isFiniteTypeOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SupportFiniteTypeModule.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SupportFiniteTypeModule.lean#L92).

> **Stacks 07TZ.** Let `X` be an algebraic space over a scheme `S` and let `F` be a
> quasi-coherent `𝒪_X`-module of finite type.  Then
>
> 1. the support of `F` is closed;
> 2. for a geometric point `x̄` of `X` lying over a point `x`,
>    `x ∈ Supp(F) ↔ F_{x̄} ≠ 0` and `F_{x̄} ≠ 0 ↔ F_{x̄} ⊗_{𝒪_{X, x̄}} κ(x̄) ≠ 0`;
> 3. for every morphism `g : X' ⟶ X` of algebraic spaces over `S` the pullback `g^* F` of
>    Stacks 03LU is again of finite type and `Supp(g^* F) = |g|^{-1}(Supp(F))`.
>
> Clause (1) is `AlgebraicGeometry.Space.isClosed_supportOfSheaf_of_isFiniteTypeOnSite`, which
> does not use quasi-coherence.  The two equivalences of clause (2) are
> `AlgebraicGeometry.Space.mem_supportOfSheaf_iff_nontrivial_geometricModuleStalk_of_liesOver`
> and `AlgebraicGeometry.Space.nontrivial_geometricModuleStalk_iff_nontrivial_residueFibre`.  The
> two conclusions of clause (3) are
> `AlgebraicGeometry.Space.isFiniteTypeOnSite_modulePullback` and
> `AlgebraicGeometry.Space.supportOfSheaf_modulePullback_eq`.

```lean
theorem supportOfSheaf_of_isQuasicoherentOnSite_isFiniteTypeOnSite
    (X : AlgebraicSpaces B S hS) (F : Modules.{u, u} B S hS X.1 X.2)
    (hqc : F.IsQuasicoherentOnSite) (hft : SheafOfModules.IsFiniteTypeOnSite F) :
    IsClosed (supportOfSheaf B S hS X.1 ((SheafOfModules.toSheaf _).obj F)) ∧
      (∀ (x : GeometricPoint B S hS X.1) (pt : points B S hS X.1), x.LiesOver pt →
        (pt ∈ supportOfSheaf B S hS X.1 ((SheafOfModules.toSheaf _).obj F) ↔
            Nontrivial (geometricModuleStalk B S hS X x F)) ∧
          (Nontrivial (geometricModuleStalk B S hS X x F) ↔
            letI := isLocalRing_etaleLocalRing B S hS X.1 X.2 x
            Nontrivial (geometricModuleResidueFibre B S hS X x F))) ∧
      ∀ (X' : AlgebraicSpaces B S hS) (g : X' ⟶ X),
        SheafOfModules.IsFiniteTypeOnSite ((modulePullback B S hS g).obj F) ∧
          supportOfSheaf B S hS X'.1
              ((SheafOfModules.toSheaf _).obj ((modulePullback B S hS g).obj F)) =
            pointsMap B S hS X'.1 g.hom ⁻¹'
              supportOfSheaf B S hS X.1 ((SheafOfModules.toSheaf _).obj F)
```

**`AlgebraicGeometry.Space.mem_supportOfSheaf_iff_nontrivial_geometricModuleStalk_of_liesOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SupportGeometricStalkCriterion.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SupportGeometricStalkCriterion.lean#L136). The attribute's comment: “part (2), first equivalence: the support against the stalk at a geometric point”.

> **Stacks 07TZ, part (2), first equivalence.** Let `F` be a quasi-coherent `𝒪_X`-module on an
> algebraic space `X` and let `x̄` be a geometric point lying over a point `x` of `X`.  Then
>
> `x ∈ Supp(F) ↔ F_{x̄} ≠ 0`.
>
> The support of Stacks 04KA is defined by nonvanishing of the stalk at some geometric point over
> `x`; the content here is that for a quasi-coherent module every geometric point over `x`
> detects the support, so the equivalence holds at the given `x̄`.
>
> Pick a small étale neighbourhood of `x̄`.  Nonvanishing of `F_{x̄}` is membership of the chart
> point in the support of the chart restriction, and that support is the inverse image of the
> support of `F` by Stacks 07TY; the chart point maps to the image of `x̄`, which is `x`.

```lean
theorem mem_supportOfSheaf_iff_nontrivial_geometricModuleStalk_of_liesOver
    (X : AlgebraicSpaces B S hS) (F : Modules.{u, u} B S hS X.1 X.2)
    [F.IsQuasicoherentOnSite] (x : GeometricPoint B S hS X.1)
    (pt : points B S hS X.1) (hx : x.LiesOver pt) :
    pt ∈ supportOfSheaf B S hS X.1 ((SheafOfModules.toSheaf _).obj F) ↔
      Nontrivial (geometricModuleStalk B S hS X x F)
```

## Tag 07U0, a lemma

[Tag 07U0](https://stacks.math.columbia.edu/tag/07U0) in the Stacks Project.

**`AlgebraicGeometry.Space.supportOfSheaf_eq_range_pointsMap_schemeTheoreticSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperModuleSupport.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperModuleSupport.lean#L178). The attribute's comment: “part (4): the support of F is the point set of its scheme-theoretic support”.

> **The support of a finite type `𝒪_X`-module is the set of points of its scheme-theoretic
> support.**
>
> The point set of a closed subspace is the zero locus of its defining ideal sheaf, and the ideal
> sheaf cutting out the scheme-theoretic support is the annihilator ideal of `F`; so the claim is
> that the support of `F` is the zero locus of its annihilator ideal sheaf.  One inclusion needs
> only that the unit function lies in the annihilator ideal wherever that ideal is the whole of
> `𝒪_X`, so `F` vanishes on every chart over such a chart and its support misses the image.  The
> other is where finite type enters: off the support every geometric stalk of `F` vanishes, and
> for a module of finite type that produces a small étale neighbourhood over which `F` has no
> nonzero sections at all, hence a chart whose image contains the point and on which the
> annihilator ideal is everything.
>
> That the scheme-theoretic support is a closed subspace cut out by the annihilator ideal sheaf
> is `AlgebraicGeometry.Space.exists_isClosedSubspace_schemeTheoreticSupport`, which quasi-
> coherence and finite type supply.
>
> This is part (4) of [Stacks, Tag 07U0] for the module on the ambient space.

```lean
theorem supportOfSheaf_eq_range_pointsMap_schemeTheoreticSupport
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : F.IsQuasicoherentOnSite)
    (hFft : SheafOfModules.IsFiniteTypeOnSite F) :
    supportOfSheaf B S hS X.1 ((SheafOfModules.toSheaf _).obj F) =
      Set.range (pointsMap B S hS (schemeTheoreticSupport B S hS X F).toFunctor
        (schemeTheoreticSupport B S hS X F).ι)
```

**`AlgebraicGeometry.Space.exists_module_on_schemeTheoreticSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SchemeTheoreticSupport.lean, line 505](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SchemeTheoreticSupport.lean#L505). The attribute's comment: “existence of the quasi-coherent module on the scheme-theoretic support”.

> **Stacks 07U0, existence.**  A finite type quasi-coherent `𝒪_X`-module `F` is the direct
> image of a quasi-coherent module on its scheme-theoretic support, which is a closed subspace
> of `X`.
>
> That the scheme-theoretic support is a closed subspace, and that the ideal cutting it out is
> the annihilator ideal of `F`, are
> `AlgebraicGeometry.Space.exists_isClosedSubspace_schemeTheoreticSupport`; so that ideal
> annihilates `F`, and
> `AlgebraicGeometry.Space.isQuasicoherentEssImagePushforward_of_isClosedImmersion` turns that
> into the module.

```lean
theorem exists_module_on_schemeTheoreticSupport (F : Modules.{u, u} B S hS X.1 X.2)
    (hF : F.IsQuasicoherentOnSite)
    (hft : PresheafOfModules.IsFiniteType (smallEtaleRingedSite B S hS X.1 X.2).J F.val) :
    ∃ (hZ : IsClosedSubspace B S hS (schemeTheoreticSupport B S hS X F))
      (G : Modules.{u, u} B S hS
        (closedSubspaceToSpace B S hS X ⟨schemeTheoreticSupport B S hS X F, hZ⟩).1
        (closedSubspaceToSpace B S hS X ⟨schemeTheoreticSupport B S hS X F, hZ⟩).2),
      G.IsQuasicoherentOnSite ∧ Nonempty ((modulePushforward B S hS
        (closedSubspaceInclusion B S hS X
          ⟨schemeTheoreticSupport B S hS X F, hZ⟩)).obj G ≅ F)
```

**`AlgebraicGeometry.Space.schemeTheoreticSupport_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SchemeTheoreticSupport.lean, line 527](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SchemeTheoreticSupport.lean#L527). The attribute's comment: “minimality: the scheme-theoretic support is contained in every closed subspace from which F is a direct image”.

> **Stacks 07U0, minimality.**  The scheme-theoretic support of `F` is contained in every
> closed subspace of `X` from which `F` is a direct image.
>
> The ideal cutting out such a closed subspace annihilates `F` by the first half of Stacks 04CJ
> part (3), so that subspace is a member of the family being intersected.

```lean
theorem schemeTheoreticSupport_le (F : Modules.{u, u} B S hS X.1 X.2)
    (Z : ClosedSubspaces B S hS X.1)
    (G : Modules.{u, u} B S hS (closedSubspaceToSpace B S hS X Z).1
      (closedSubspaceToSpace B S hS X Z).2)
    (e : (modulePushforward B S hS (closedSubspaceInclusion B S hS X Z)).obj G ≅ F) :
    schemeTheoreticSupport B S hS X F ≤ Z.1
```

**`AlgebraicGeometry.Space.module_on_closedSubspace_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SchemeTheoreticSupport.lean, line 543](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SchemeTheoreticSupport.lean#L543). The attribute's comment: “part (2): uniqueness up to unique isomorphism”.

> **Stacks 07U0, part (2).**  A module on a closed subspace of `X` whose direct image is `F`
> is unique up to a unique isomorphism compatible with the chosen identifications of the direct
> images with `F`.
>
> This is full faithfulness of the direct image along a closed immersion, Stacks 04CJ part (2).

```lean
theorem module_on_closedSubspace_unique (F : Modules.{u, u} B S hS X.1 X.2)
    (Z : ClosedSubspaces B S hS X.1)
    (G H : Modules.{u, u} B S hS (closedSubspaceToSpace B S hS X Z).1
      (closedSubspaceToSpace B S hS X Z).2)
    (eG : (modulePushforward B S hS (closedSubspaceInclusion B S hS X Z)).obj G ≅ F)
    (eH : (modulePushforward B S hS (closedSubspaceInclusion B S hS X Z)).obj H ≅ F) :
    ∃! φ : G ≅ H,
      (modulePushforward B S hS (closedSubspaceInclusion B S hS X Z)).map φ.hom ≫ eH.hom =
        eG.hom
```

**`AlgebraicGeometry.Space.isFiniteTypeOnSite_module_on_closedSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SchemeTheoreticSupport.lean, line 572](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SchemeTheoreticSupport.lean#L572). The attribute's comment: “part (3): the module on the closed subspace is of finite type”.

> **Stacks 07U0, part (3).**  A module on a closed subspace of `X` whose direct image is a
> module of finite type is itself of finite type.
>
> By Stacks 04CJ part (2) it is isomorphic to the inverse image of `F`, which is of finite type by
> Stacks 03DO, and finite type passes along an epimorphism.

```lean
theorem isFiniteTypeOnSite_module_on_closedSubspace (F : Modules.{u, u} B S hS X.1 X.2)
    (hFft : SheafOfModules.IsFiniteTypeOnSite F) (Z : ClosedSubspaces B S hS X.1)
    (G : Modules.{u, u} B S hS (closedSubspaceToSpace B S hS X Z).1
      (closedSubspaceToSpace B S hS X Z).2)
    (e : (modulePushforward B S hS (closedSubspaceInclusion B S hS X Z)).obj G ≅ F) :
    SheafOfModules.IsFiniteTypeOnSite G
```

**`AlgebraicGeometry.Space.schemeTheoreticSupport_isSmallest_and_properties`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SchemeTheoreticSupportCharacterization.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SchemeTheoreticSupportCharacterization.lean#L72).

> **Stacks 07U0.** Let `F` be a finite type quasi-coherent `𝒪_X`-module on an algebraic
> space `X`. Its scheme-theoretic support `Z` is a closed subspace of `X` carrying a
> quasi-coherent `𝒪_Z`-module `G` with `i_*G ≅ F`, and it is the smallest closed subspace from
> which `F` is a direct image. Moreover:
>
> 1. on every étale scheme chart `U` of `X`, the scheme-theoretic support of the restriction of
>    `F` to `U` is `Z ×_X U`;
> 2. a module `G` on `Z` with `i_*G ≅ F` is unique up to unique isomorphism;
> 3. such a `G` is of finite type;
> 4. the support of `F` is `|Z|`, and the support of such a `G` is all of `|Z|`.

```lean
theorem schemeTheoreticSupport_isSmallest_and_properties (F : Modules.{u, u} B S hS X.1 X.2)
    (hF : F.IsQuasicoherentOnSite) (hFft : SheafOfModules.IsFiniteTypeOnSite F) :
    ∃ hZ : IsClosedSubspace B S hS (schemeTheoreticSupport B S hS X F),
      -- existence of a quasi-coherent module on `Z` whose direct image is `F`
      (∃ G : Modules.{u, u} B S hS
          (closedSubspaceToSpace B S hS X ⟨schemeTheoreticSupport B S hS X F, hZ⟩).1
          (closedSubspaceToSpace B S hS X ⟨schemeTheoreticSupport B S hS X F, hZ⟩).2,
        G.IsQuasicoherentOnSite ∧ Nonempty ((modulePushforward B S hS
          (closedSubspaceInclusion B S hS X
            ⟨schemeTheoreticSupport B S hS X F, hZ⟩)).obj G ≅ F)) ∧
      -- minimality
      (∀ (Z' : ClosedSubspaces B S hS X.1)
        (G' : Modules.{u, u} B S hS (closedSubspaceToSpace B S hS X Z').1
          (closedSubspaceToSpace B S hS X Z').2),
        ((modulePushforward B S hS (closedSubspaceInclusion B S hS X Z')).obj G' ≅ F) →
          schemeTheoreticSupport B S hS X F ≤ Z'.1) ∧
      -- part (1)
      (∀ A : SmallEtale B S hS X.1,
        letI : (chartRestrictionSheaf B S hS X F A).IsQuasicoherent :=
          isQuasicoherent_chartRestrictionSheaf B S hS X F hF A
        letI : (chartRestrictionSheaf B S hS X F A).IsFiniteType :=
          Stacks.AlgebraicGeometry.TopDegreeFiniteType.isFiniteType_of_forall_moduleFinite_sections
            (chartRestrictionSheaf B S hS X F A)
            (moduleFinite_sections_chartRestrictionSheaf B S hS X F hF hFft A)
        Scheme.Modules.schemeTheoreticSupport (chartRestrictionSheaf B S hS X F A) =
          idealSheafDataOfChart B S hS X
            (definingIdealSheaf B S hS X ⟨schemeTheoreticSupport B S hS X F, hZ⟩)
            (definingIdealSheaf_isCartesianOnAffineCharts B S hS X
              ⟨schemeTheoreticSupport B S hS X F, hZ⟩) A) ∧
      -- part (2)
      (∀ (G H : Modules.{u, u} B S hS
          (closedSubspaceToSpace B S hS X ⟨schemeTheoreticSupport B S hS X F, hZ⟩).1
          (closedSubspaceToSpace B S hS X ⟨schemeTheoreticSupport B S hS X F, hZ⟩).2)
        (eG : (modulePushforward B S hS (closedSubspaceInclusion B S hS X
          ⟨schemeTheoreticSupport B S hS X F, hZ⟩)).obj G ≅ F)
        (eH : (modulePushforward B S hS (closedSubspaceInclusion B S hS X
          ⟨schemeTheoreticSupport B S hS X F, hZ⟩)).obj H ≅ F),
        ∃! φ : G ≅ H, (modulePushforward B S hS (closedSubspaceInclusion B S hS X
          ⟨schemeTheoreticSupport B S hS X F, hZ⟩)).map φ.hom ≫ eH.hom = eG.hom) ∧
      -- part (3)
      (∀ (G : Modules.{u, u} B S hS
          (closedSubspaceToSpace B S hS X ⟨schemeTheoreticSupport B S hS X F, hZ⟩).1
          (closedSubspaceToSpace B S hS X ⟨schemeTheoreticSupport B S hS X F, hZ⟩).2),
        ((modulePushforward B S hS (closedSubspaceInclusion B S hS X
          ⟨schemeTheoreticSupport B S hS X F, hZ⟩)).obj G ≅ F) →
          SheafOfModules.IsFiniteTypeOnSite G) ∧
      -- part (4)
      supportOfSheaf B S hS X.1 ((SheafOfModules.toSheaf _).obj F) =
          Set.range (pointsMap B S hS (schemeTheoreticSupport B S hS X F).toFunctor
            (schemeTheoreticSupport B S hS X F).ι) ∧
      (∀ (G : Modules.{u, u} B S hS
          (closedSubspaceToSpace B S hS X ⟨schemeTheoreticSupport B S hS X F, hZ⟩).1
          (closedSubspaceToSpace B S hS X ⟨schemeTheoreticSupport B S hS X F, hZ⟩).2),
        ((modulePushforward B S hS (closedSubspaceInclusion B S hS X
          ⟨schemeTheoreticSupport B S hS X F, hZ⟩)).obj G ≅ F) →
          supportOfSheaf B S hS
            (closedSubspaceToSpace B S hS X ⟨schemeTheoreticSupport B S hS X F, hZ⟩).1
            ((SheafOfModules.toSheaf _).obj G) = Set.univ)
```

**`AlgebraicGeometry.Space.schemeTheoreticSupport_chartRestrictionSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SchemeTheoreticSupportChartComparison.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SchemeTheoreticSupportChartComparison.lean#L207). The attribute's comment: “part (1): on a scheme U étale over X the scheme-theoretic support of the restriction of F, in the sense of schemes, is the sheaf of ideals that the scheme-theoretic support of F cuts out on U”.

> **Stacks 07U0, part (1), with the support of the restriction taken in the sense of
> schemes.**  Let `F` be a finite type quasi-coherent `𝒪_X`-module, let `Z ⊆ X` be its
> scheme-theoretic support and let `A` be an étale scheme chart of `X` — a scheme `U` with an
> étale morphism to `X`.  Then the scheme-theoretic support of Stacks 05JV of the restriction of
> `F` to `U` is the sheaf of ideals that `Z` cuts out on `U`, that is, `Z ×_X U`.
>
> Over an affine open `V` of `U` both sides are the annihilator of the sections of `F` over the
> étale chart `V` cuts out: the left-hand side by
> `AlgebraicGeometry.Space.annihilator_sections_chartRestrictionSheaf` and the right-hand side
> because the ideal cutting out the scheme-theoretic support is the annihilator ideal sheaf of
> `F`.

```lean
theorem schemeTheoreticSupport_chartRestrictionSheaf (F : Modules.{u, u} B S hS X.1 X.2)
    (hF : F.IsQuasicoherentOnSite) (hFft : SheafOfModules.IsFiniteTypeOnSite F)
    (Z : ClosedSubspaces B S hS X.1) (hZ : Z.1 = schemeTheoreticSupport B S hS X F)
    (A : SmallEtale B S hS X.1) :
    letI : (chartRestrictionSheaf B S hS X F A).IsQuasicoherent :=
      isQuasicoherent_chartRestrictionSheaf B S hS X F hF A
    letI : (chartRestrictionSheaf B S hS X F A).IsFiniteType :=
      Stacks.AlgebraicGeometry.TopDegreeFiniteType.isFiniteType_of_forall_moduleFinite_sections
        (chartRestrictionSheaf B S hS X F A)
        (moduleFinite_sections_chartRestrictionSheaf B S hS X F hF hFft A)
    Scheme.Modules.schemeTheoreticSupport (chartRestrictionSheaf B S hS X F A) =
      idealSheafDataOfChart B S hS X (definingIdealSheaf B S hS X Z)
        (definingIdealSheaf_isCartesianOnAffineCharts B S hS X Z) A
```

**`AlgebraicGeometry.Space.schemeTheoreticSupport_modulePullback_schemeSpace_of_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SchemeTheoreticSupportEtaleChart.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SchemeTheoreticSupportEtaleChart.lean#L90). The attribute's comment: “part (1): on a scheme étale over X the scheme-theoretic support of the inverse image of F is the inverse image of the scheme-theoretic support of F”.

> **Stacks 07U0, part (1).**  Let `F` be a finite type quasi-coherent `𝒪_X`-module with
> scheme-theoretic support `Z ⊆ X`, let `U` be a scheme over `S` and let `φ : U → X` be an étale
> morphism.  Then the fibre product `Z ×_X U` is the scheme-theoretic support of `φ^*F`.
>
> An étale morphism of algebraic spaces is flat (Stacks 0467,
> `AlgebraicGeometry.Space.isFlat_of_isEtale`), so this is Stacks 089C,
> `AlgebraicGeometry.Space.schemeTheoreticSupport_modulePullback`, at `φ`.

```lean
theorem schemeTheoreticSupport_modulePullback_schemeSpace_of_isEtale
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : F.IsQuasicoherentOnSite)
    (hft : PresheafOfModules.IsFiniteType (smallEtaleRingedSite B S hS X.1 X.2).J F.val)
    (U : BigFppfOver B S hS) (φ : schemeSpace U ⟶ X) (hφ : IsEtale B S hS φ.hom) :
    schemeTheoreticSupport B S hS (schemeSpace U) ((modulePullback B S hS φ).obj F) =
      (schemeTheoreticSupport B S hS X F).preimage φ.hom
```

**`AlgebraicGeometry.Space.supportOfSheaf_module_on_schemeTheoreticSupport_eq_univ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SchemeTheoreticSupportEtaleChart.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SchemeTheoreticSupportEtaleChart.lean#L110). The attribute's comment: “part (4): the module on the scheme-theoretic support has support all of it”.

> **Stacks 07U0, part (4), for the module on the scheme-theoretic support.**  Let `F` be a
> finite type quasi-coherent `𝒪_X`-module, let `Z ⊆ X` be its scheme-theoretic support and let
> `G` be an `𝒪_Z`-module whose direct image along the inclusion is `F`.  Then the support of `G`
> is all of `|Z|`.
>
> `G` is of finite type by part (3), so the support of its direct image is the image of its
> support under the injective map on points of a closed immersion; that direct image is `F`,
> whose support is `|Z|` by the other half of part (4),
> `AlgebraicGeometry.Space.supportOfSheaf_eq_range_pointsMap_schemeTheoreticSupport`.

```lean
theorem supportOfSheaf_module_on_schemeTheoreticSupport_eq_univ
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : F.IsQuasicoherentOnSite)
    (hFft : SheafOfModules.IsFiniteTypeOnSite F) (Z : ClosedSubspaces B S hS X.1)
    (hZeq : Z.1 = schemeTheoreticSupport B S hS X F)
    (G : Modules.{u, u} B S hS (closedSubspaceToSpace B S hS X Z).1
      (closedSubspaceToSpace B S hS X Z).2)
    (e : (modulePushforward B S hS (closedSubspaceInclusion B S hS X Z)).obj G ≅ F) :
    supportOfSheaf B S hS (closedSubspaceToSpace B S hS X Z).1
      ((SheafOfModules.toSheaf _).obj G) = Set.univ
```

## Tag 07U1, a definition

[Tag 07U1](https://stacks.math.columbia.edu/tag/07U1) in the Stacks Project.

**`AlgebraicGeometry.Space.schemeTheoreticSupport`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SchemeTheoreticSupport.lean, line 398](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SchemeTheoreticSupport.lean#L398).

> **Stacks 07U1.** The *scheme theoretic support* of a finite type quasi-coherent
> `𝒪_X`-module `F`: the intersection of the closed subspaces of `X` whose defining ideal
> annihilates `F`.
>
> By `AlgebraicGeometry.Space.schemeTheoreticSupport_eq_of_definingIdealSheaf_eq` this is the
> closed subspace cut out by the annihilator ideal sheaf of `F`, which for a quasi-coherent `F` of
> finite type is a quasi-coherent sheaf of ideals; so the intersection is itself a closed subspace
> and it is the smallest member of the family, which is the content of Stacks 07U0.

```lean
def schemeTheoreticSupport (F : Modules.{u, u} B S hS X.1 X.2) : Subfunctor X.1
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.15, Tag 07TX](https://stacks.math.columbia.edu/tag/07TX)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
