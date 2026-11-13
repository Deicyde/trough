---
declaration: section
origin: cited
lean: CommAlgCat.polynomialSite, CommAlgCat.polynomialTopology_eq_bot, CommAlgCat.polynomialStructureSheaf, CommAlgCat.polynomialConstantSheaf, CommAlgCat.polynomialConstantSheafIso, CommAlgCat.polynomialAugmentation, CommAlgCat.polynomialAugmentation_app, CommAlgCat.polynomialInclusion
statement: formalized
proof: formalized
---

# 92.4 Simplicial resolutions and derived lower shriek

Section 92.4 of the Stacks Project, [Tag 08PQ](https://stacks.math.columbia.edu/tag/08PQ). 8 tags here are carried by 45 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08PR, an equation

[Tag 08PR](https://stacks.math.columbia.edu/tag/08PR) in the Stacks Project.

**`CommAlgCat.polynomialSite`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSite.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSite.lean#L117). The attribute's comment: “the site C\_\{B/A}”.

> **Stacks 08PR.** The site `C_{B/A}`: the opposite of the category of polynomial `A`-algebras
> augmented to `B`. Its topology is the chaotic one, recorded through the ringed point below.

```lean
abbrev polynomialSite
```

**`CommAlgCat.polynomialTopology_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSite.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSite.lean#L133). The attribute's comment: “the chaotic topology on C\_\{B/A}”.

> **Stacks 08PR.** The topology of `C_{B/A}` is the chaotic topology: its only coverings are
> the maximal sieves, so every presheaf on `C_{B/A}` is a sheaf.

```lean
theorem polynomialTopology_eq_bot : polynomialTopology A B = ⊥
```

**`CommAlgCat.polynomialStructureSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSite.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSite.lean#L155). The attribute's comment: “the structure sheaf 𝒪”.

> **Stacks 08PR.** The tautological sheaf of rings `𝒪` on `C_{B/A}`, which sends the object
> `(P, α)` to `P`. It is a sheaf because the topology of `C_{B/A}` is chaotic.

```lean
def polynomialStructureSheaf : Sheaf (polynomialTopology A B) CommRingCat.{u + 1}
```

**`CommAlgCat.polynomialConstantSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSite.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSite.lean#L163). The attribute's comment: “the constant sheaf B”.

> **Stacks 08PR.** The constant sheaf of rings `B` on `C_{B/A}`, written with an underline in
> the source. By Tag 08PF it is the inverse image along `π` of the ring on the point.

```lean
def polynomialConstantSheaf : Sheaf (polynomialTopology A B) CommRingCat.{u + 1}
```

**`CommAlgCat.polynomialConstantSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSite.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSite.lean#L188). The attribute's comment: “the constant sheaf B is constant”.

> **Stacks 08PR.** The constant sheaf of rings `B` of Tag 08PF is the constant presheaf with
> value `B`.

```lean
def polynomialConstantSheafIso :
    (polynomialConstantSheaf A B).obj ≅ polynomialConstantPresheaf A B
```

**`CommAlgCat.polynomialAugmentation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSite.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSite.lean#L219). The attribute's comment: “the augmentation 𝒪 ⟶ B”.

> **Stacks 08PR.** The map of sheaves of rings `𝒪 → B` given by the augmentations.

```lean
def polynomialAugmentation :
    polynomialStructureSheaf A B ⟶ polynomialConstantSheaf A B
```

**`CommAlgCat.polynomialAugmentation_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSite.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSite.lean#L228). The attribute's comment: “the augmentation is given by α”.

> **Stacks 08PR.** On sections over the object `(P, α)` of `C_{B/A}`, the augmentation of
> sheaves of rings is `α`, read through the identification of the constant sheaf with the constant
> presheaf.

```lean
theorem polynomialAugmentation_app (X : polynomialSite A B) :
    (polynomialAugmentation A B).hom.app (Opposite.op X) ≫
        (polynomialConstantSheafIso A B).hom.app (Opposite.op X) =
      (polynomialAugmentationPresheaf A B).app (Opposite.op X)
```

**`CommAlgCat.polynomialInclusion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSite.lean, line 295](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSite.lean#L295). The attribute's comment: “the morphism i of ringed topoi”.

> **Stacks 08PR.** The morphism of ringed topoi `i : (Sh(C_{B/A}), B) ⟶ (Sh(C_{B/A}), 𝒪)`:
> the identity on underlying topoi, with `i♯ : 𝒪 ⟶ i_*B` the augmentation.

```lean
def polynomialInclusion :
    AlgebraicGeometry.RingedToposHom (polynomialConstantRingedTopos A B)
      (polynomialStructureRingedTopos A B)
```

**`CommAlgCat.polynomialInclusion_toToposHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSite.lean, line 303](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSite.lean#L303). The attribute's comment: “i is the identity on topoi”.

> **Stacks 08PR.** The geometric morphism underlying `i` is the identity.

```lean
theorem polynomialInclusion_toToposHom :
    (polynomialInclusion A B).toToposHom = polynomialIdentityTopos A B
```

**`CommAlgCat.polynomialProjection`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSite.lean, line 319](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSite.lean#L319). The attribute's comment: “the morphism π of ringed topoi”.

> **Stacks 08PR.** The morphism of ringed topoi `π : (Sh(C_{B/A}), B) ⟶ (Sh(*), B)`, the
> projection of the chaotic site to its ringed point.

```lean
abbrev polynomialProjection
```

**`CommAlgCat.boundedPolynomialSite`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteSmall.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSiteSmall.lean#L137). The attribute's comment: “the site C\_\{B/A} with the section's footnote in force, restricting the sets of variables to cardinality at most κ. The unrestricted version is `CommAlgCat.polynomialSite`; only this one is essentially small”.

> The site `C_{B/A}` cut down to the polynomial algebras on at most `κ` variables: the opposite
> of `CommAlgCat.BoundedPolynomialAugmentation`. For `κ = #B` this is the site of the source,
> footnote included; `CommAlgCat.polynomialSite` is the same construction with the footnote
> omitted.

```lean
abbrev boundedPolynomialSite
```

## Tag 08PS, a lemma

[Tag 08PS](https://stacks.math.columbia.edu/tag/08PS) in the Stacks Project.

**`CommAlgCat.exists_homotopyEquivalences_resolutionMor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ResolutionPointCriterion.lean, line 379](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/ResolutionPointCriterion.lean#L379). The attribute's comment: “the hypothesis of the criterion of Tag 08Q9 for the cosimplicial object of a resolution: each `Mor_C((P_•, ε), W)` is homotopy equivalent to a singleton. The conclusion `Lπ_!(ℱ) = ℱ(P_•, ε)` in `D(Ab)`, resp. `D(B)`, functorially in `ℱ`, is not asserted: the criterion as formalized asks for a small site, and `CommAlgCat.polynomialSite` is large — see the first implementation note”.

> **Stacks 08PS**. Let `P_•` be a simplicial `A`-algebra endowed with an augmentation
> `ε : P_• ⟶ B`, assume every `P_n` is a polynomial algebra over `A` and that `ε` is a trivial Kan
> fibration on underlying simplicial sets. Then for every object `W = (Q, β)` of the site `C_{B/A}`
> the simplicial set `Mor_{C_{B/A}}((P_•, ε), W)` is homotopy equivalent to the constant simplicial
> set on a singleton, which is the hypothesis the criterion of Tag 08Q9 asks of the cosimplicial
> object `CommAlgCat.resolutionCosimplicialObject` of the resolution.

```lean
theorem exists_homotopyEquivalences_resolutionMor
    (hε : SSet.trivialKanFibrations (Functor.whiskerRight ε (forget (CommAlgCat.{u} A))))
    (W : polynomialSite A B) :
    ∃ f : (resolutionCosimplicialObject ε hP).op ⋙ yoneda.obj W ⟶
        (Functor.const SimplexCategoryᵒᵖ).obj PUnit.{u + 1},
      SimplicialObject.homotopyEquivalences (Type u) f
```

**`CommAlgCat.polynomialSiteResolutionDerivedColimitNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ResolutionPointCriterionPolynomialSite.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/ResolutionPointCriterionPolynomialSite.lean#L166). The attribute's comment: “the conclusion `Lπ_!(ℱ) = ℱ(P_•, ε)` in `D(Ab)` functorially in `ℱ` in `Ab(C_{B/A})`, at `CommAlgCat.polynomialSite` -- the site of Tag 08PR itself, not a restriction of it -- as an isomorphism in the derived category, with `π_!` in its colimit presentation of Tag 08PF and the coefficients at the universe `u + 1` of the site's objects”.

> **`Lπ_!(ℱ) = ℱ(P_•, ε)` in `D(Ab)`, functorially in `ℱ`, at the site `C_{B/A}`.**
> Let `ε : P_• ⟶ B` be a simplicial `A`-algebra endowed with an augmentation to `B`, assume every
> `P_n` is a polynomial algebra over `A` and that `ε` is a trivial Kan fibration on underlying
> simplicial sets. Then the extended Moore complex of the simplicial abelian group `ℱ(P_•, ε)` is
> `Lπ_!(ℱ)` in `D(Ab)`, as an **isomorphism of functors** of the abelian sheaf `ℱ` on the site
> `C_{B/A}` of Tag 08PR -- the abelian presheaves being its abelian sheaves, the topology being
> chaotic.
>
> This is the abelian half of the conclusion of Tag 08PS. The hypothesis of the criterion of
> Tag 08Q9 is `CommAlgCat.isPointResolution_resolutionCosimplicialObject`, and
> `Stacks.ChaoticSite.AbelianValued.mooreCochainNatIsoDerivedColimitOfLarge` is that criterion in
> its derived form, natural in the coefficient presheaf and with no smallness hypothesis on the
> site.

```lean
def polynomialSiteResolutionDerivedColimitNatIso
    (hε : SSet.trivialKanFibrations (Functor.whiskerRight ε (forget (CommAlgCat.{u} A)))) :
    Stacks.ChaoticSite.GeneralValued.mooreCochainComplex'
          (resolutionCosimplicialObject ε hP) AddCommGrpCat.{u + 1} ⋙ DerivedCategory.Q ≅
      HomologicalComplex.single ((polynomialSite A B)ᵒᵖ ⥤ AddCommGrpCat.{u + 1})
          (ComplexShape.up ℤ) 0 ⋙
        DerivedCategory.Q ⋙
          totalDerivedColimit' (polynomialSite A B) AddCommGrpCat.{u + 1}
```

**`CommAlgCat.polynomialSiteResolutionModuleDerivedColimitNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ResolutionPointCriterionPolynomialSite.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/ResolutionPointCriterionPolynomialSite.lean#L194). The attribute's comment: “the conclusion `Lπ_!(ℱ) = ℱ(P_•, ε)` in `D(B)` functorially in `ℱ` in `Mod(B̲)`, at `CommAlgCat.polynomialSite` -- the site of Tag 08PR itself, not a restriction of it -- as an isomorphism in the derived category, with the coefficient ring read as `ULift.{u+1} B` exactly as the site's own ringed point `CommAlgCat.polynomialRingedPoint` reads it”.

> **`Lπ_!(ℱ) = ℱ(P_•, ε)` in `D(B)`, functorially in `ℱ`, at the site `C_{B/A}`.**
> Under the hypotheses of Tag 08PS, the extended Moore complex of the simplicial `B`-module
> `ℱ(P_•, ε)` is `Lπ_!(ℱ)` in `D(B)`, as an **isomorphism of functors** of the sheaf of `B`-modules
> `ℱ` on the site `C_{B/A}` of Tag 08PR -- the diagrams of `B`-modules on the site being its
> `B̲`-modules, the topology being chaotic.
>
> This is the module half of the conclusion of Tag 08PS, beside the abelian half
> `CommAlgCat.polynomialSiteResolutionDerivedColimitNatIso`: the same hypothesis
> `CommAlgCat.isPointResolution_resolutionCosimplicialObject` -- which does not mention the
> coefficients -- is fed to
> `Stacks.ChaoticSite.ModuleValued.mooreCochainNatIsoDerivedColimitOfLarge`. The coefficient ring is
> `ULift.{u + 1} B`, the ring of the site's ringed point
> `CommAlgCat.polynomialRingedPoint`.

```lean
def polynomialSiteResolutionModuleDerivedColimitNatIso
    (hε : SSet.trivialKanFibrations (Functor.whiskerRight ε (forget (CommAlgCat.{u} A)))) :
    Stacks.ChaoticSite.GeneralValued.mooreCochainComplex'
          (resolutionCosimplicialObject ε hP)
          (ModuleCat.{u + 1} (ULift.{u + 1} (B : Type u))) ⋙ DerivedCategory.Q ≅
      HomologicalComplex.single
          ((polynomialSite A B)ᵒᵖ ⥤ ModuleCat.{u + 1} (ULift.{u + 1} (B : Type u)))
          (ComplexShape.up ℤ) 0 ⋙
        DerivedCategory.Q ⋙
          totalDerivedColimit' (polynomialSite A B)
            (ModuleCat.{u + 1} (ULift.{u + 1} (B : Type u)))
```

**`CommAlgCat.smallResolutionModuleLeftDerivedLowerShriekNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ResolutionPointCriterionSmallOfModules.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/ResolutionPointCriterionSmallOfModules.lean#L58). The attribute's comment: “the conclusion `Lπ_!(ℱ) = ℱ(P_•, ε)` in `D(B)` functorially in `ℱ` in `Mod(B̲)`, read at the small model of the footnote-restricted site, for the same reason as recorded for the abelian half in `StacksFrontier/Cotangent/ResolutionPointCriterionSmall.lean`”.

> Let `ε : P_• ⟶ B` be a resolution of `B` over `A` whose terms are polynomial algebras on at
> most `κ` variables. For every sheaf of `B`-modules `ℱ` on the small model of the restricted site
> `C_{B/A}`, the sections at the point of `L_nπ_!(ℱ)` are the degree `n` homology of the Moore
> complex of the simplicial `B`-module `ℱ(P_•, ε)`, naturally in `ℱ`; here `π` is the point
> morphism of the small model.

```lean
def smallResolutionModuleLeftDerivedLowerShriekNatIso
    (hε : SSet.trivialKanFibrations (Functor.whiskerRight ε (forget (CommAlgCat.{u} A))))
    (n : ℕ) :
    (modulePointLowerShriek (smallBoundedPolynomialSite A B κ)
          (B : Type u)).leftDerived n ⋙
        Stacks.ChaoticSite.pointSections.{u, u + 1, u} (ModuleCat.{u} (B : Type u)) ≅
      sheafToPresheaf (GrothendieckTopology.trivial (smallBoundedPolynomialSite A B κ))
          (ModuleCat.{u} (B : Type u)) ⋙
        moduleCosimplicialMooreComplex (smallResolutionCosimplicialObject ε κ hPκ) ⋙
          HomologicalComplex.homologyFunctor (ModuleCat.{u} (B : Type u))
            (ComplexShape.down ℕ) n
```

## Tag 08PT, a lemma

[Tag 08PT](https://stacks.math.columbia.edu/tag/08PT) in the Stacks Project.

**`Stacks.ChaoticSite.ModuleValued.mooreCochainQIsoDerivedColimit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedColimitByPointResolution.lean, line 391](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedColimitByPointResolution.lean#L391). The attribute's comment: “derived form at module coefficients, for one module over the constant sheaf of rings: the extended Moore complex of the evaluation on a point resolution is derived lower shriek in D(B), derived lower shriek being the total left derived functor of the colimit over the index category. Not asserted natural in the coefficient module”.

> **The derived form of [Stacks, Tag 08PT] at module coefficients.** Let `C` be a small
> category with the chaotic topology, `B` a ring, and `U_•` a cosimplicial object of `C` such that
> every simplicial set `Mor_C(U_•, W)` is homotopy equivalent to a singleton. Then for every
> diagram `ℱ` of `B`-modules on `Cᵒᵖ` — that is, every `B̲`-module on the chaotic site — the
> extended Moore complex of the simplicial `B`-module `ℱ(U_•)` computes derived lower shriek:
>
> `Q(ℱ(U_•)) ≅ Lπ_!(ℱ)` in `D(B)`.
>
> Here `Lπ_!` is `Stacks.CategoryHomology.totalDerivedColimit`, the total left derived functor of
> the colimit over `Cᵒᵖ`, which is `π_!` on the chaotic site by [Stacks, Tag 08PF]. The proof
> compares the two filtrations of the double complex obtained by evaluating a projective resolution
> of `ℱ` on `U_•`.
>
> The isomorphism depends on the chosen projective resolution and is not asserted to be natural in
> `ℱ`; see the implementation notes of this module.

```lean
def mooreCochainQIsoDerivedColimit (hU : IsPointResolution U) :
    DerivedCategory.Q.obj ((mooreCochainComplex U).obj F) ≅
      (totalDerivedColimit C (ModuleCat.{u} B)).obj
        (DerivedCategory.Q.obj
          ((HomologicalComplex.single (Cᵒᵖ ⥤ ModuleCat.{u} B) (ComplexShape.up ℤ) 0).obj F))
```

**`Stacks.ChaoticSite.ModuleValued.mooreCochainQIsoDerivedColimit_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedColimitByPointResolutionNaturality.lean, line 398](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedColimitByPointResolutionNaturality.lean#L398). The attribute's comment: “the derived form at module coefficients is natural in the point resolution: a morphism of cosimplicial objects between two point resolutions carries the comparison at one to the comparison at the other. Still not asserted natural in the coefficient module”.

> **The derived form of [Stacks, Tag 08PT] at module coefficients is independent of the point
> resolution**, compatibly with morphisms of point resolutions. For a morphism `v : U_• ⟶ V_•` of
> cosimplicial objects of `C`, both point resolutions, and a diagram `ℱ` of `B`-modules on `Cᵒᵖ`,
> the triangle
>
> `Q(ℱ(V_•)) ⟶ Q(ℱ(U_•)) ⟶ Lπ_!(ℱ)`
>
> commutes, the second arrow being
> `Stacks.ChaoticSite.ModuleValued.mooreCochainQIsoDerivedColimit` at `U_•` and the composite being
> the same isomorphism at `V_•`. This is the totalized form of the canonical map of
> [Stacks, Tag 08Q6]: the comparison of the extended Moore complex of a point resolution with
> derived lower shriek does not depend on the point resolution.
>
> The projective resolution of `ℱ` chosen by
> `Stacks.ChaoticSite.ModuleValued.mooreCochainQIsoDerivedColimit` is built from `ℱ` alone, so one
> and the same resolution serves both point resolutions and the statement is
> `Stacks.ChaoticSite.ModuleValued.mooreCochainQIsoDerivedColimitOfResolution_naturality`.

```lean
theorem mooreCochainQIsoDerivedColimit_naturality (v : U ⟶ V) (hU : IsPointResolution U)
    (hV : IsPointResolution V) (F : Cᵒᵖ ⥤ ModuleCat.{u} B) :
    DerivedCategory.Q.map ((mooreCochainMap v).app F) ≫
        (mooreCochainQIsoDerivedColimit U F hU).hom =
      (mooreCochainQIsoDerivedColimit V F hV).hom
```

**`CommAlgCat.standardResolutionAbelianDerivedLowerShriekIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ResolutionDerivedLowerShriek.lean, line 343](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/ResolutionDerivedLowerShriek.lean#L343). The attribute's comment: “`Lπ_!(ℱ) = ℱ(P_•, ε)` in `D(Ab)` functorially in `ℱ` in `Ab(C)`, on the site `C_{B/A}` of 08PR, with coefficients in the universe above that of `A` and `B`”.

> **Stacks 08PT, in `D(Ab)`.** Let `A → B` be a ring map and let `ε : P_• → B` be the standard
> resolution of `B` over `A`. Let `π` be as in Tag 08PR. Then
>
> `Lπ_!(ℱ) = ℱ(P_•, ε)` in `D(Ab)`, functorially in `ℱ` in `Ab(C)`.
>
> Here `C = C_{B/A}` is the site of Tag 08PR (`CommAlgCat.polynomialSite`), whose topology is chaotic
> so that `Ab(C)` is the category of abelian presheaves on it, with coefficients in
> `Type (u + 1)`, the universe in which colimits over `C` exist; `Lπ_!` is
> `CommAlgCat.polynomialDerivedLowerShriek`; and `ℱ(P_•, ε)` is the extended Moore complex of
> the simplicial abelian group obtained by evaluating `ℱ` on the cosimplicial object of `C` given
> by the standard resolution. The standard resolution satisfies the hypotheses of Tag 08PS by
> Tag 08QI: its terms are polynomial algebras, and its augmentation is a homotopy equivalence of
> underlying simplicial sets (Tag 08ND), hence a quasi-isomorphism of associated complexes
> (Tag 08P2), hence a trivial Kan fibration (Tag 08P1).

```lean
def standardResolutionAbelianDerivedLowerShriekIso :
    polynomialMooreCochain A B
        (resolutionCosimplicialObject (standardResolution.{u, u} A B).hom
          (standardResolution_isResolution.{u, u} A B).isPolynomialAlgebra)
        AddCommGrpCat.{u + 1} ⋙ DerivedCategory.Q ≅
      HomologicalComplex.single ((polynomialSite A B)ᵒᵖ ⥤ AddCommGrpCat.{u + 1})
          (ComplexShape.up ℤ) 0 ⋙ DerivedCategory.Q ⋙
        polynomialDerivedLowerShriek A B AddCommGrpCat.{u + 1}
```

**`CommAlgCat.standardResolutionModuleDerivedLowerShriekIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ResolutionDerivedLowerShriek.lean, line 369](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/ResolutionDerivedLowerShriek.lean#L369). The attribute's comment: “`Lπ_!(ℱ) = ℱ(P_•, ε)` in `D(B)` functorially in `ℱ` in `Mod(B̲)`, on the site `C_{B/A}` of 08PR, with module sections in the universe above that of `A` and `B`”.

> **Stacks 08PT, in `D(B)`.** Let `A → B` be a ring map and let `ε : P_• → B` be the standard
> resolution of `B` over `A`. Let `π` be as in Tag 08PR. Then
>
> `Lπ_!(ℱ) = ℱ(P_•, ε)` in `D(B)`, functorially in `ℱ` in `Mod(B̲)`.
>
> Here `C = C_{B/A}` is the site of Tag 08PR (`CommAlgCat.polynomialSite`), whose topology is chaotic
> so that a `B̲`-module is a diagram of `B`-modules on it, with sections in `Type (u + 1)`, the
> universe in which colimits over `C` exist, `B` being lifted to that universe as the ring on the
> point of `π` is; `Lπ_!` is `CommAlgCat.polynomialDerivedLowerShriek`; and `ℱ(P_•, ε)` is the
> extended Moore complex of the simplicial `B`-module obtained by evaluating `ℱ` on the
> cosimplicial object of `C` given by the standard resolution. The standard resolution satisfies
> the hypotheses of Tag 08PS by Tag 08QI, as recorded at
> `CommAlgCat.standardResolutionAbelianDerivedLowerShriekIso`.

```lean
def standardResolutionModuleDerivedLowerShriekIso :
    polynomialMooreCochain A B
        (resolutionCosimplicialObject (standardResolution.{u, u} A B).hom
          (standardResolution_isResolution.{u, u} A B).isPolynomialAlgebra)
        (ModuleCat.{u + 1} (ULift.{u + 1} (B : Type u))) ⋙ DerivedCategory.Q ≅
      HomologicalComplex.single
          ((polynomialSite A B)ᵒᵖ ⥤ ModuleCat.{u + 1} (ULift.{u + 1} (B : Type u)))
          (ComplexShape.up ℤ) 0 ⋙ DerivedCategory.Q ⋙
        polynomialDerivedLowerShriek A B (ModuleCat.{u + 1} (ULift.{u + 1} (B : Type u)))
```

**`CommAlgCat.exists_homotopyEquivalences_standardResolutionMor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ResolutionPointCriterion.lean, line 414](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/ResolutionPointCriterion.lean#L414). The attribute's comment: “the hypothesis of the criterion of Tag 08Q9 for the cosimplicial object of the standard resolution: each `Mor_C((P_•, ε), W)` is homotopy equivalent to a singleton. The conclusion `Lπ_!(ℱ) = ℱ(P_•, ε)` in `D(Ab)`, resp. `D(B)`, functorially in `ℱ`, is not asserted, for the reason recorded at Tag 08PS in this file”.

> **Stacks 08PT**. Let `A → B` be a ring map and let `ε : P_• ⟶ B` be the standard resolution of
> `B` over `A`. Then for every object `W` of the site `C_{B/A}` the simplicial set
> `Mor_{C_{B/A}}((P_•, ε), W)` is homotopy equivalent to the constant simplicial set on a singleton,
> which is the hypothesis the criterion of Tag 08Q9 asks of the cosimplicial object of the standard
> resolution. The two hypotheses of Tag 08PS hold for it by Tag 08QI: its terms are polynomial
> algebras, and its augmentation is a trivial Kan fibration because it is a homotopy equivalence of
> underlying simplicial sets (Tag 08ND), hence a quasi-isomorphism of associated complexes
> (Tag 08P2), hence — being degreewise surjective — a trivial Kan fibration (Tag 08P1).

```lean
theorem exists_homotopyEquivalences_standardResolutionMor (A : Type u) [CommRing A]
    (B : CommAlgCat.{u} A) (W : polynomialSite A B) :
    ∃ f : (resolutionCosimplicialObject (standardResolution.{u, u} A B).hom
          (standardResolution_isResolution.{u, u} A B).isPolynomialAlgebra).op ⋙
        yoneda.obj W ⟶ (Functor.const SimplexCategoryᵒᵖ).obj PUnit.{u + 1},
      SimplicialObject.homotopyEquivalences (Type u) f
```

**`CommAlgCat.standardResolutionDerivedColimitNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ResolutionPointCriterionSmallDerived.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/ResolutionPointCriterionSmallDerived.lean#L202). The attribute's comment: “the conclusion `Lπ_!(ℱ) = ℱ(P_•, ε)` in `D(Ab)` functorially in `ℱ` in `Ab(C_{B/A})`, for the standard resolution, as an isomorphism in the derived category rather than degreewise, read at the small model of the footnote-restricted site — for the reason recorded at Tag 08PS in this file”.

> **`Lπ_!(ℱ) = ℱ(P_•, ε)` in `D(Ab)` for the standard resolution**, functorially in the abelian
> sheaf `ℱ` on the small model of the site restricted to polynomial algebras on at most
> `CommAlgCat.standardResolutionVarCardinal A B` variables.
>
> This is the abelian half of the conclusion of Tag 08PT in the derived category. The two
> hypotheses of Tag 08PS hold for the standard resolution by Tag 08QI — its terms are polynomial
> algebras and its augmentation is a trivial Kan fibration — and its terms are boundedly many
> variables wide by `CommAlgCat.standardResolution_isPolynomialAlgebraBelow`, so nothing is
> assumed.

```lean
def standardResolutionDerivedColimitNatIso :
    Stacks.ChaoticSite.AbelianValued.mooreCochainComplex
          (smallResolutionCosimplicialObject (standardResolution.{u, u} A B).hom
            (standardResolutionVarCardinal A B)
            (standardResolution_isPolynomialAlgebraBelow A B)) ⋙ DerivedCategory.Q ≅
      HomologicalComplex.single
          ((smallBoundedPolynomialSite A B (standardResolutionVarCardinal A B))ᵒᵖ ⥤
            AddCommGrpCat.{u})
          (ComplexShape.up ℤ) 0 ⋙
        DerivedCategory.Q ⋙
          totalDerivedColimit (smallBoundedPolynomialSite A B
            (standardResolutionVarCardinal A B)) AddCommGrpCat.{u}
```

**`CommAlgCat.standardResolutionModuleDerivedColimitNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ResolutionPointCriterionSmallDerived.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/ResolutionPointCriterionSmallDerived.lean#L229). The attribute's comment: “the conclusion `Lπ_!(ℱ) = ℱ(P_•, ε)` in `D(B)` functorially in `ℱ` in `Mod(B̲)`, for the standard resolution, as an isomorphism in the derived category rather than degreewise, read at the small model of the footnote-restricted site — for the reason recorded at Tag 08PS in this file”.

> **`Lπ_!(ℱ) = ℱ(P_•, ε)` in `D(B)` for the standard resolution**, functorially in the sheaf of
> `B`-modules `ℱ` on the small model of the site restricted to polynomial algebras on at most
> `CommAlgCat.standardResolutionVarCardinal A B` variables.
>
> This is the module half of the conclusion of Tag 08PT in the derived category, beside the abelian
> half `CommAlgCat.standardResolutionDerivedColimitNatIso`; as there, the hypotheses of Tag 08PS are
> discharged for the standard resolution by Tag 08QI.

```lean
def standardResolutionModuleDerivedColimitNatIso :
    Stacks.ChaoticSite.ModuleValued.mooreCochainComplex (B := (B : Type u))
          (smallResolutionCosimplicialObject (standardResolution.{u, u} A B).hom
            (standardResolutionVarCardinal A B)
            (standardResolution_isPolynomialAlgebraBelow A B)) ⋙ DerivedCategory.Q ≅
      HomologicalComplex.single
          ((smallBoundedPolynomialSite A B (standardResolutionVarCardinal A B))ᵒᵖ ⥤
            ModuleCat.{u} (B : Type u))
          (ComplexShape.up ℤ) 0 ⋙
        DerivedCategory.Q ⋙
          totalDerivedColimit (smallBoundedPolynomialSite A B
            (standardResolutionVarCardinal A B)) (ModuleCat.{u} (B : Type u))
```

**`CommAlgCat.standardResolutionModuleLeftDerivedLowerShriekNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ResolutionPointCriterionSmallOfModules.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/ResolutionPointCriterionSmallOfModules.lean#L84). The attribute's comment: “the conclusion `Lπ_!(ℱ) = ℱ(P_•, ε)` in `D(B)` functorially in `ℱ` in `Mod(B̲)`, for the standard resolution, read at the small model of the footnote-restricted site, for the reason recorded at Tag 08PS in this file”.

> For every sheaf of `B`-modules `ℱ` on the small model of the site `C_{B/A}` restricted to
> polynomial algebras on at most `CommAlgCat.standardResolutionVarCardinal A B` variables, the
> sections at the point of `L_nπ_!(ℱ)` are the degree `n` homology of the Moore complex of the
> simplicial `B`-module `ℱ(P_•, ε)` for `P_•` the standard resolution of `B` over `A`, naturally
> in `ℱ`.

```lean
def standardResolutionModuleLeftDerivedLowerShriekNatIso (n : ℕ) :
    (modulePointLowerShriek
          (smallBoundedPolynomialSite A B (standardResolutionVarCardinal A B))
          (B : Type u)).leftDerived n ⋙
        Stacks.ChaoticSite.pointSections.{u, u + 1, u} (ModuleCat.{u} (B : Type u)) ≅
      sheafToPresheaf (GrothendieckTopology.trivial
            (smallBoundedPolynomialSite A B (standardResolutionVarCardinal A B)))
          (ModuleCat.{u} (B : Type u)) ⋙
        moduleCosimplicialMooreComplex
            (smallResolutionCosimplicialObject (standardResolution.{u, u} A B).hom
              (standardResolutionVarCardinal A B)
              (standardResolution_isPolynomialAlgebraBelow A B)) ⋙
          HomologicalComplex.homologyFunctor (ModuleCat.{u} (B : Type u))
            (ComplexShape.down ℕ) n
```

## Tag 08PU, a lemma

[Tag 08PU](https://stacks.math.columbia.edu/tag/08PU) in the Stacks Project.

**`CommAlgCat.free_kaehlerDifferential_polynomialSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteCotangentComplex.lean, line 387](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSiteCotangentComplex.lean#L387). The attribute's comment: “the first sentence of the proof: for each object P → B of C\_\{B/A} the module Ω\_\{P/A} is a free P-module; this is the input to the step Li^*Ω\_\{𝒪/A} = i^*Ω\_\{𝒪/A}, which is CommAlgCat.smallPolynomialDerivedPullbackDifferentialsIso”.

> **The differentials of each object of `C_{B/A}` are free over it.** Every object `(P, α)` of
> the site has `P` a polynomial algebra over `A`, so `Ω[P⁄A]` is free on the variables. This is the
> first sentence of the proof of Tag 08PU, the objectwise input to its step `Li^* = i^*`; the
> sheaf-level flatness is `CommAlgCat.polynomialRelativeDifferentials_isFlat`, and the step itself,
> `Li^*Ω_{𝒪/A} ≅ i^*Ω_{𝒪/A}` in `D(B̲)`, is `CommAlgCat.smallPolynomialDerivedPullbackDifferentialsIso`
> of `StacksFrontier/Cotangent/PolynomialAlgebraSiteDerivedPullbackDifferentials.lean`.

```lean
theorem free_kaehlerDifferential_polynomialSite (X : polynomialSite A B) :
    Module.Free (X.unop.obj.left : Type u) Ω[(X.unop.obj.left : Type u)⁄A]
```

**`CommAlgCat.standardResolutionCotangentMooreComplexIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteCotangentComplex.lean, line 486](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSiteCotangentComplex.lean#L486). The attribute's comment: “the step Lπ\_!(Ω\_\{𝒪/A} ⊗\_𝒪 B̲) = (Ω\_\{𝒪/A} ⊗\_𝒪 B̲)(P\_•, ε): the evaluation of i^*Ω\_\{𝒪/A} on the standard resolution is the simplicial module whose complex is L\_\{B/A}, as an isomorphism of complexes”.

> **The Moore complex of `(i^*Ω_{𝒪/A})(P_•, ε)` is the complex of `L_{B/A}`.** For the
> standard resolution of `B` over `A`, the Moore complex of the simplicial abelian group obtained
> by evaluating `i^*Ω_{𝒪/A}` on the cosimplicial object of the small model is the complex
> underlying the cotangent complex of Tag 08PN, namely the alternating face map complex of
> `CommAlgCat.cotangentSimplicialModule` with its `B`-module structures forgotten.
>
> This is the heart of Tag 08PU: an isomorphism of complexes, not merely of their homology.

```lean
def standardResolutionCotangentMooreComplexIso :
    (Stacks.ChaoticSite.cosimplicialMooreComplex
          (standardResolutionSmallCosimplicialObject A B)).obj
        (smallPolynomialCotangentSheaf A B (standardResolutionVarCardinal A B)).obj ≅
      ((forget₂ (ModuleCat.{u} B) AddCommGrpCat.{u}).mapHomologicalComplex
          (ComplexShape.down ℕ)).obj
        ((alternatingFaceMapComplex (ModuleCat.{u} B)).obj
          (cotangentSimplicialModule.{u, u} A B).object)
```

**`CommAlgCat.standardResolutionLeftDerivedCotangentComplexIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteCotangentComplex.lean, line 524](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSiteCotangentComplex.lean#L524). The attribute's comment: “the identification L\_\{B/A} = Lπ\_!(Ω\_\{𝒪/A} ⊗\_𝒪 B̲), for the point morphism of the small model of the footnote-restricted site C\_\{B/A} and with Lπ\_! read degreewise, as the left derived functors of the π\_! of Tag 08PF at abelian coefficients: the sections at the point of L\_nπ\_! are the degree -n cohomology of the cotangent complex of Tag 08PN. The source's isomorphism in D(B) needs the module-level Lπ\_!, which is absent from this library”.

> **Tag 08PU at the small model of the restricted site `C_{B/A}`.** The sections at the point
> of `L_nπ_!(Ω_{𝒪/A} ⊗_𝒪 B̲)` are the degree `-n` cohomology of the cotangent complex `L_{B/A}` of
> Tag 08PN, with its `B`-module structure forgotten; here `π` is the point morphism of the small
> model of the footnote-restricted site and `Lπ_!` is read degreewise, as the left derived functors
> of the `π_!` of Tag 08PF.
>
> The proof is the source's: Tag 08PT computes `L_nπ_!` on the standard resolution
> (`CommAlgCat.standardResolutionLeftDerivedLowerShriekNatIso`), the evaluation of
> `Ω_{𝒪/A} ⊗_𝒪 B̲` there is the simplicial module defining `L_{B/A}`
> (`CommAlgCat.standardResolutionCotangentMooreComplexIso`), and the cotangent complex is the
> reindexing of that simplicial module's alternating face map complex. The step
> `Li^*Ω_{𝒪/A} = i^*Ω_{𝒪/A}` of the source is the flatness of `Ω_{𝒪/A}` over `𝒪`,
> `CommAlgCat.polynomialRelativeDifferentials_isFlat`; see the implementation notes for what
> separates this statement from the source's isomorphism in `D(B)`.

```lean
def standardResolutionLeftDerivedCotangentComplexIso (n : ℕ) :
    (Stacks.ChaoticSite.pointSections.{u, u + 1, u} AddCommGrpCat.{u}).obj
        (((Stacks.ChaoticSite.abelianPointLowerShriek
              (smallBoundedPolynomialSite A B
                (standardResolutionVarCardinal A B))).leftDerived n).obj
          (smallPolynomialCotangentSheaf A B (standardResolutionVarCardinal A B))) ≅
      (forget₂ (ModuleCat.{u} B) AddCommGrpCat.{u}).obj
        ((cotangentComplex.{u, u} A B).homology (-(n : ℤ)))
```

**`CommAlgCat.smallPolynomialDerivedPullbackDifferentialsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteDerivedPullbackDifferentials.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSiteDerivedPullbackDifferentials.lean#L159). The attribute's comment: “the step Li^*Ω\_\{𝒪/A} = i^*Ω\_\{𝒪/A} in D(B̲), on the small model of the footnote-restricted site C\_\{B/A}, where i^* is extension of scalars along the augmentation 𝒪 ⟶ B̲ and Li^* its total left derived functor”.

> **`Li^*Ω_{𝒪/A} = i^*Ω_{𝒪/A}`** in `D(B̲)`, on the small model of the footnote-restricted site
> `C_{B/A}`: the total left derived functor of the module pullback along `i`, evaluated at
> `Ω_{𝒪/A}` in degree zero, is the underived pullback in degree zero. This is the comparison
> `Li^* ⟶ i^*` at `Ω_{𝒪/A}[0]`, invertible by
> `CommAlgCat.isIso_derivedExtendScalarsCounit_singleDifferentials`, read between the two
> single-degree embeddings.

```lean
def smallPolynomialDerivedPullbackDifferentialsIso :
    (smallPolynomialDerivedModulePullback A B κ).obj
        ((DerivedCategory.singleFunctor _ 0).obj (smallPolynomialDifferentials A B κ)) ≅
      (DerivedCategory.singleFunctor _ 0).obj
        ((smallPolynomialModulePullback A B κ).obj (smallPolynomialDifferentials A B κ))
```

**`CommAlgCat.cotangentComplexIsoDerivedLowerShriekDerivedPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteDerivedPullbackDifferentials.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSiteDerivedPullbackDifferentials.lean#L192). The attribute's comment: “the chain L\_\{B/A} = Lπ\_!(Li^*Ω\_\{𝒪/A}) = Lπ\_!(i^*Ω\_\{𝒪/A}) = Lπ\_!(Ω\_\{𝒪/A} ⊗\_𝒪 B̲), read in D(Ab), on the small model of the footnote-restricted site C\_\{B/A}”.

> **[Stacks, Tag 08PU] as the full chain, in `D(Ab)`**: on the small model of the
> footnote-restricted site `C_{B/A}`, at the cardinal bounding the standard resolution,
>
> `L_{B/A} ≅ Lπ_!(Li^*Ω_{𝒪/A})`,
>
> with `Lπ_!` the derived colimit of the underlying abelian presheaves
> (`Stacks.ChaoticSite.abelianDerivedColimitOfModules`). The isomorphism is the composite of the
> source's three steps: `Li^*Ω_{𝒪/A} = i^*Ω_{𝒪/A}`
> (`CommAlgCat.smallPolynomialDerivedPullbackDifferentialsIso`); `i^*Ω_{𝒪/A} = Ω_{𝒪/A} ⊗_𝒪 B̲`, the
> sheaf `(P, α) ↦ B ⊗_{P,α} Ω_{P/A}` (`CommAlgCat.extendScalarsDifferentialsIso`); and
> `Lπ_!(Ω_{𝒪/A} ⊗_𝒪 B̲) = L_{B/A}`, computed on the standard resolution
> (`CommAlgCat.derivedLowerShriekCotangentIso`).

```lean
def cotangentComplexIsoDerivedLowerShriekDerivedPullback :
    DerivedCategory.Q.obj
        (((forget₂ (ModuleCat.{u} (B : Type u)) AddCommGrpCat.{u}).mapHomologicalComplex
          (ComplexShape.up ℤ)).obj (cotangentComplex.{u, u} A B)) ≅
      (Stacks.ChaoticSite.abelianDerivedColimitOfModules
          (smallPolynomialConstantPresheaf A B (standardResolutionVarCardinal A B))).obj
        ((smallPolynomialDerivedModulePullback A B (standardResolutionVarCardinal A B)).obj
          ((DerivedCategory.singleFunctor _ 0).obj
            (smallPolynomialDifferentials A B (standardResolutionVarCardinal A B))))
```

**`CommAlgCat.standardResolutionModuleLeftDerivedCotangentComplexIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteModuleShriek.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSiteModuleShriek.lean#L162). The attribute's comment: “L\_\{B/A} = Lπ\_!(Ω\_\{𝒪/A} ⊗\_𝒪 B̲) at linear coefficients, for the point morphism of the small model of the footnote-restricted site C\_\{B/A} and with Lπ\_! read degreewise, as the left derived functors of the π\_! of Tag 08PF on sheaves of B-modules: the sections at the point of L\_nπ\_! are the degree -n cohomology of the cotangent complex of Tag 08PN, as B-modules. The source's isomorphism in D(B) needs the derived form of Tag 08PT”.

> **Tag 08PU at the small model of the restricted site `C_{B/A}`, with `B`-linear
> coefficients.** The sections at the point of `L_nπ_!(Ω_{𝒪/A} ⊗_𝒪 B̲)` are the degree `-n`
> cohomology of the cotangent complex `L_{B/A}` of Tag 08PN, as `B`-modules; here `π` is the point
> morphism of the small model of the footnote-restricted site and `Lπ_!` is read degreewise, as
> the left derived functors of the `π_!` of Tag 08PF on sheaves of `B`-modules.
>
> The proof is the source's: Tag 08PT at linear coefficients computes `L_nπ_!` on the standard
> resolution (`CommAlgCat.standardResolutionModuleLeftDerivedLowerShriekNatIso`), the evaluation of
> `Ω_{𝒪/A} ⊗_𝒪 B̲` there is the simplicial `B`-module defining `L_{B/A}`
> (`CommAlgCat.standardResolutionCotangentModuleMooreComplexIso`), and the cotangent complex is the
> reindexing of that simplicial module's alternating face map complex.

```lean
def standardResolutionModuleLeftDerivedCotangentComplexIso (n : ℕ) :
    (Stacks.ChaoticSite.pointSections.{u, u + 1, u} (ModuleCat.{u} (B : Type u))).obj
        (((Stacks.ChaoticSite.ModuleValued.modulePointLowerShriek
              (smallBoundedPolynomialSite A B (standardResolutionVarCardinal A B))
              (B : Type u)).leftDerived n).obj
          (smallPolynomialCotangentModuleSheaf A B (standardResolutionVarCardinal A B))) ≅
      (cotangentComplex.{u, u} A B).homology (-(n : ℤ))
```

**`CommAlgCat.standardResolutionCotangentDerivedLowerShriekIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteModuleShriekDerived.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSiteModuleShriekDerived.lean#L101). The attribute's comment: “in D(B), at module coefficients: Q(L\_\{B/A}) = L pi\_!(Omega ⊗ B) for the point morphism of the small model of the footnote-restricted site C\_\{B/A}, with L pi\_! the total left derived functor of the colimit on D(B-underline)”.

> **[Stacks, Tag 08PU] in `D(B)`, at module coefficients and on the small model of the
> footnote-restricted site `C_{B/A}`.** The cotangent complex `L_{B/A}` of [Stacks, Tag 08PN] is
> derived lower shriek of the sheaf of `B̲`-modules `i^*Ω_{𝒪/A} = Ω_{𝒪/A} ⊗_𝒪 B̲`, as an object of
> `D(B)`:
>
> `Q(L_{B/A}) ≅ Lπ_!(Ω_{𝒪/A} ⊗_𝒪 B̲)`.
>
> Here `Lπ_!` is `CommAlgCat.smallPolynomialModuleDerivedLowerShriek`, the total left derived
> functor of the colimit over the index category of `B̲`-modules, which is the `π_!` of
> [Stacks, Tag 08PF].
>
> The proof is the source's. The standard resolution is a point resolution of the small model
> (`CommAlgCat.isPointResolution_standardResolutionSmallCosimplicialObject`), so the derived form
> of [Stacks, Tag 08PT] at module coefficients
> (`Stacks.ChaoticSite.ModuleValued.mooreCochainQIsoDerivedColimit`) computes `Lπ_!` of
> `i^*Ω_{𝒪/A}` as the extended Moore complex of its evaluation on that resolution, and that
> complex is the cotangent complex. The step `Li^*Ω_{𝒪/A} = i^*Ω_{𝒪/A}` of the source is the
> flatness of `Ω_{𝒪/A}` over `𝒪`, which is why `i^*Ω_{𝒪/A}` may be used underived.

```lean
def standardResolutionCotangentDerivedLowerShriekIso :
    DerivedCategory.Q.obj (cotangentComplex.{u, u} A B) ≅
      smallPolynomialCotangentDerivedLowerShriek A B (standardResolutionVarCardinal A B)
```

**`CommAlgCat.smallResolutionCotangentDerivedLowerShriekIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ResolutionCotangentDerived.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/ResolutionCotangentDerived.lean#L118). The attribute's comment: “in D(B), at module coefficients, for an arbitrary resolution whose terms have at most κ variables: Q of the complex of that resolution is L pi\_!(Omega ⊗ B-underline) for the point morphism of the small model of the footnote-restricted site C\_\{B/A}. Combined with the same statement at the standard resolution this is Remark 08QI, that any resolution computes L\_\{B/A}”.

> **[Stacks, Tag 08PU] in `D(B)` for an arbitrary bounded resolution.** Let `ε : P_• ⟶ B` be a
> resolution of `B` over `A` in the sense of [Stacks, Tag 08QI] whose terms are polynomial algebras
> on at most `κ` variables. Then the complex `Ω[P_•⁄A] ⊗_{P_•} B` of that resolution, read in
> cohomological degrees `≤ 0`, is derived lower shriek of the sheaf of `B̲`-modules
> `i^*Ω_{𝒪/A} = Ω_{𝒪/A} ⊗_𝒪 B̲`, as an object of `D(B)`:
>
> `Q(Ω[P_•⁄A] ⊗_{P_•} B) ≅ Lπ_!(Ω_{𝒪/A} ⊗_𝒪 B̲)`.
>
> Here `Lπ_!` is `CommAlgCat.smallPolynomialModuleDerivedLowerShriek`, the total left derived
> functor of the colimit over the index category of `B̲`-modules, which is the `π_!` of
> [Stacks, Tag 08PF].
>
> The proof is the source's, with the standard resolution replaced by `P_•`: the resolution is a
> point resolution of the small model of the footnote-restricted site
> (`CommAlgCat.isPointResolution_smallResolutionCosimplicialObject`), so the derived form of
> [Stacks, Tag 08PT] at module coefficients
> (`Stacks.ChaoticSite.ModuleValued.mooreCochainQIsoDerivedColimit`) computes `Lπ_!` of
> `i^*Ω_{𝒪/A}` as the extended Moore complex of its evaluation on `P_•`, and that evaluation is
> `Ω[P_•⁄A] ⊗_{P_•} B`. Since the right-hand side does not mention the resolution, this is also
> the assertion of [Stacks, Remark 08QI] that any resolution computes `L_{B/A}`.

```lean
def smallResolutionCotangentDerivedLowerShriekIso
    (hε : SSet.trivialKanFibrations (Functor.whiskerRight ε (forget (CommAlgCat.{u} A)))) :
    DerivedCategory.Q.obj
        (((alternatingFaceMapComplex (ModuleCat.{u} (B : Type u))).obj
            (resolutionOver ε ⋙ overDifferentialsFunctor)).extend
          (ComplexShape.embeddingUpIntLE (0 : ℤ))) ≅
      smallPolynomialCotangentDerivedLowerShriek A B κ
```

**`CommAlgCat.standardResolutionCotangentDerivedLowerShriekIsoOfLE`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ResolutionCotangentDerived.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/ResolutionCotangentDerived.lean#L162). The attribute's comment: “in D(B), at module coefficients, at an arbitrary cardinal bound κ containing the standard resolution: Q(L\_\{B/A}) = L pi\_!(Omega ⊗ B-underline) for the point morphism of the small model of the site restricted to at most κ variables”.

> **[Stacks, Tag 08PU] in `D(B)` at an arbitrary cardinal bound.** The cotangent complex
> `L_{B/A}` of [Stacks, Tag 08PN] is derived lower shriek of the sheaf of `B̲`-modules
> `i^*Ω_{𝒪/A} = Ω_{𝒪/A} ⊗_𝒪 B̲` on the small model of the site restricted to polynomial algebras
> on at most `κ` variables, for any bound `κ` containing the standard resolution:
>
> `Q(L_{B/A}) ≅ Lπ_!(Ω_{𝒪/A} ⊗_𝒪 B̲)`.
>
> This is `CommAlgCat.smallResolutionCotangentDerivedLowerShriekIso` at the standard resolution,
> whose complex `Ω[P_•⁄A] ⊗_{P_•} B` is the cotangent complex by
> `CommAlgCat.standardResolutionOverDifferentialsIso`. At
> `κ = CommAlgCat.standardResolutionVarCardinal A B` it is
> `CommAlgCat.standardResolutionCotangentDerivedLowerShriekIso`; the point of the free bound is
> that a second resolution may need a larger one.

```lean
def standardResolutionCotangentDerivedLowerShriekIsoOfLE
    (hκ : standardResolutionVarCardinal A B ≤ κ) :
    DerivedCategory.Q.obj (cotangentComplex.{u, u} A B) ≅
      smallPolynomialCotangentDerivedLowerShriek A B κ
```

**`CommAlgCat.smallResolutionCotangentDerivedLowerShriekIso_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ResolutionCotangentDerivedNaturality.lean, line 312](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/ResolutionCotangentDerivedNaturality.lean#L312). The attribute's comment: “in D(B), at module coefficients: the identification of the complex of a resolution with L pi\_!(Omega ⊗ B-underline) is functorial in the resolution, so the isomorphism it gives between the complexes of two resolutions is the map induced by a morphism between them. This is the arrow-level form of Remark 08QI”.

> **[Stacks, Tag 08PU] in `D(B)` is functorial in the resolution.** Let `ε : P_• ⟶ B` and
> `ε' : P'_• ⟶ B` be resolutions of `B` over `A` in the sense of [Stacks, Tag 08QI] whose terms are
> polynomial algebras on at most `κ` variables, and let `w : P_• ⟶ P'_•` be a morphism of simplicial
> `A`-algebras over `B`. Then the triangle
>
> `Q(Ω[P_•⁄A] ⊗_{P_•} B) ⟶ Q(Ω[P'_•⁄A] ⊗_{P'_•} B) ⟶ Lπ_!(Ω_{𝒪/A} ⊗_𝒪 B̲)`
>
> commutes: the comparison of `CommAlgCat.smallResolutionCotangentDerivedLowerShriekIso` at `ε'`,
> precomposed with the map `CommAlgCat.resolutionCotangentComplexMap` induced by `w`, is the
> comparison at `ε`.
>
> In particular the isomorphism between the complexes of two resolutions that the two instances of
> [Stacks, Tag 08PU] produce is the map induced by any morphism between the resolutions — which is
> the content of [Stacks, Remark 08QI] beyond the object-level statement, and what a comparison of
> two presentations consumes.
>
> The proof is the naturality of the derived form of [Stacks, Tag 08PT] in the point resolution
> (`Stacks.ChaoticSite.ModuleValued.mooreCochainQIsoDerivedColimit_naturality`), applied at
> `CommAlgCat.smallResolutionCosimplicialObjectMap`, together with
> `CommAlgCat.smallResolutionCotangentMooreCochainIso_naturality`.

```lean
theorem smallResolutionCotangentDerivedLowerShriekIso_naturality (w : P ⟶ P') (hw : w ≫ ε' = ε)
    (hε : SSet.trivialKanFibrations (Functor.whiskerRight ε (forget (CommAlgCat.{u} A))))
    (hε' : SSet.trivialKanFibrations (Functor.whiskerRight ε' (forget (CommAlgCat.{u} A)))) :
    DerivedCategory.Q.map (resolutionCotangentComplexMap ε ε' w hw) ≫
        (smallResolutionCotangentDerivedLowerShriekIso ε' κ hP'κ hε').hom =
      (smallResolutionCotangentDerivedLowerShriekIso ε κ hPκ hε).hom
```

**`CommAlgCat.leftDerivedColimPolynomialCotangentIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SurjectionSymmetricPowerVanishing.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SurjectionSymmetricPowerVanishing.lean#L119). The attribute's comment: “the identification L\_\{B/A} = Lπ\_!(Ω\_\{𝒪/A} ⊗\_𝒪 B̲) read degreewise at LINEAR coefficients: for every n, the nth left derived functor of the colimit over the opposite of the small model of the footnote-restricted site, applied to Ω, is the degree -n cohomology of the cotangent complex of Tag 08PN, as an isomorphism of B-modules. L\_n colim is Tag 08PF's definition of H\_n(C\_\{B/A}, -); the identification with the sections at the point of L\_nπ\_! is Stacks.ChaoticSite.ModuleValued.moduleLeftDerivedPointLowerShriekNatIso. Proved for every ring map A → B”.

> **Tag 08PU at the small model of the restricted site `C_{B/A}`, at linear coefficients.**
> The `n`th homology of `C_{B/A}` with coefficients in `Ω = Ω_{𝒪/A} ⊗_𝒪 B̲` — the `n`th left
> derived functor of the colimit over the opposite of the small model, which is Tag 08PF's
> definition — is the degree `-n` cohomology of the cotangent complex `L_{B/A}` of Tag 08PN, as
> `B`-modules.
>
> This is the linear-coefficient refinement of
> `CommAlgCat.standardResolutionLeftDerivedCotangentComplexIso`, which is its image under the
> forgetful functor to abelian groups. The proof is the same: the module half of Tag 08Q9
> computes `L_n colim` on the standard resolution, and the evaluation of `Ω` there is the
> simplicial module defining `L_{B/A}`.

```lean
def leftDerivedColimPolynomialCotangentIso (n : ℕ) :
    ((colim :
          ((smallBoundedPolynomialSite A B (standardResolutionVarCardinal A B))ᵒᵖ ⥤
            ModuleCat.{u} B) ⥤ ModuleCat.{u} B).leftDerived n).obj
        (smallPolynomialCotangentModulePresheaf A B (standardResolutionVarCardinal A B)) ≅
      (cotangentComplex.{u, u} A B).homology (-(n : ℤ))
```

## Tag 08QE, a lemma

[Tag 08QE](https://stacks.math.columbia.edu/tag/08QE) in the Stacks Project.

**`CommAlgCat.atiyahModuleDerivedInverseImageCompLowerShriekIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/AtiyahClassBigSiteResolution.lean, line 170](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/AtiyahClassBigSiteResolution.lean#L170). The attribute's comment: “in D(B), at module coefficients: Lπ\_!(π^\{-1}M) = M at `CommAlgCat.polynomialSite` -- the site of Tag 08PR itself, not a restriction of it, read on its `AsSmall` model -- with Lπ\_! the total left derived functor of the colimit on D(B̲), π^\{-1} the constant diagram, and the coefficient ring read as `ULift.{u+1} B` exactly as the site's own ringed point `CommAlgCat.polynomialRingedPoint` reads it”.

> **[Stacks, Tag 08QE] at the site `C_{B/A}` itself.** Derived lower shriek of the inverse
> image of a `B`-module is that module: `Lπ_!(π^{-1}M) = M` in `D(B)`, naturally in `M`. Here
> `π^{-1}` is the constant diagram and `Lπ_!` the total left derived functor of the colimit over
> the index category, which is the `π_!` of [Stacks, Tag 08PF]; the coefficient ring is
> `ULift B`, the ring of the site's own ringed point `CommAlgCat.polynomialRingedPoint`.
>
> The proof is the source's: the augmentation `A → B` is a terminal object of the site
> (`CommAlgCat.isTerminal_atiyahBaseObj`), so `π^{-1}` has the exact right adjoint "sections over
> `A → B`" and `Stacks.ChaoticSite.derivedConstCompColimitIso` applies with no hypothesis on the
> existence of the derived functor. The statement at the footnote-restricted site is
> `CommAlgCat.smallPolynomialModuleDerivedInverseImageCompLowerShriekIso`; that is a statement
> about different coefficients, the restriction to a full subcategory changing both `Mod(B̲)` and
> `Lπ_!`.

```lean
def atiyahModuleDerivedInverseImageCompLowerShriekIso :
    (Functor.const (atiyahSite A B)ᵒᵖ :
          ModuleCat.{u + 1} (ULift.{u + 1} (B : Type u)) ⥤ _).mapDerivedCategory ⋙
        totalDerivedColimit (atiyahSite A B)
          (ModuleCat.{u + 1} (ULift.{u + 1} (B : Type u))) ≅ 𝟭 _
```

**`CommAlgCat.polynomialLeftDerivedZeroLowerShriekInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteCotangentComplex.lean, line 552](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSiteCotangentComplex.lean#L552). The attribute's comment: “Lπ\_!(π^\{-1}M) = M in degree zero, for the point morphism of the small model of the footnote-restricted site C\_\{B/A} at abelian coefficients”.

> **Tag 08QE at the small model of the restricted site `C_{B/A}`, in degree zero.** The
> sections at the point of `L_0π_!(π^{-1}M)` are the sections of `M`, for every abelian sheaf `M`
> on the point; here `π` is the point morphism of the small model of the footnote-restricted site.
>
> This is the source's proof: Tag 08PT computes `Lπ_!(π^{-1}M)` by `(π^{-1}M)(P_•, ε)` for the
> standard resolution, and that is the constant simplicial object on `M`.

```lean
def polynomialLeftDerivedZeroLowerShriekInverseImageIso
    (M : Sheaf (GrothendieckTopology.trivial (Discrete PUnit.{u + 1})) AddCommGrpCat.{u}) :
    (Stacks.ChaoticSite.pointSections.{u, u + 1, u} AddCommGrpCat.{u}).obj
        (((Stacks.ChaoticSite.abelianPointLowerShriek
              (smallBoundedPolynomialSite A B
                (standardResolutionVarCardinal A B))).leftDerived 0).obj
          ((Stacks.ChaoticSite.abelianPointInverseImage
            (smallBoundedPolynomialSite A B
              (standardResolutionVarCardinal A B))).obj M)) ≅
      (Stacks.ChaoticSite.pointSections.{u, u + 1, u} AddCommGrpCat.{u}).obj M
```

**`CommAlgCat.isZero_polynomialLeftDerivedSuccLowerShriekInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteCotangentComplex.lean, line 570](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSiteCotangentComplex.lean#L570). The attribute's comment: “Lπ\_!(π^\{-1}M) = M in positive degrees: L\_nπ\_!(π^\{-1}M) = 0 for n > 0”.

> **Tag 08QE at the small model of the restricted site `C_{B/A}`, in positive degrees.** The
> sections at the point of `L_nπ_!(π^{-1}M)` vanish for `n > 0`, so together with
> `CommAlgCat.polynomialLeftDerivedZeroLowerShriekInverseImageIso` this is the source's
> `Lπ_!(π^{-1}M) = M`, read degreewise.

```lean
theorem isZero_polynomialLeftDerivedSuccLowerShriekInverseImage
    (M : Sheaf (GrothendieckTopology.trivial (Discrete PUnit.{u + 1})) AddCommGrpCat.{u})
    (n : ℕ) :
    IsZero ((Stacks.ChaoticSite.pointSections.{u, u + 1, u} AddCommGrpCat.{u}).obj
      (((Stacks.ChaoticSite.abelianPointLowerShriek
            (smallBoundedPolynomialSite A B
              (standardResolutionVarCardinal A B))).leftDerived (n + 1)).obj
        ((Stacks.ChaoticSite.abelianPointInverseImage
          (smallBoundedPolynomialSite A B
            (standardResolutionVarCardinal A B))).obj M)))
```

**`CommAlgCat.smallPolynomialModuleDerivedInverseImageCompLowerShriekIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteModuleShriek.lean, line 271](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSiteModuleShriek.lean#L271). The attribute's comment: “in D(B), at module coefficients: Lπ\_!(π^\{-1}M) = M for the point morphism of the small model of the footnote-restricted site C\_\{B/A}, with Lπ\_! the total left derived functor of the colimit on D(B̲) and π^\{-1} the constant diagram”.

> **Tag 08QE in `D(B)` at the small model of the restricted site `C_{B/A}`.** Derived lower
> shriek of the inverse image of a `B`-module is that module: `Lπ_!(π^{-1}M) = M` in `D(B)`,
> naturally in `M`. Here `π^{-1}` is the constant diagram and `Lπ_!` the total left derived
> functor of the colimit, and the proof is that the augmentation `A → B` is a terminal object of
> the site, so that `π^{-1}` has the exact right adjoint "sections over `A → B`".

```lean
def smallPolynomialModuleDerivedInverseImageCompLowerShriekIso :
    (Functor.const (smallBoundedPolynomialSite A B κ)ᵒᵖ :
          ModuleCat.{u} (B : Type u) ⥤ _).mapDerivedCategory ⋙
        Stacks.CategoryHomology.totalDerivedColimit (smallBoundedPolynomialSite A B κ)
          (ModuleCat.{u} (B : Type u)) ≅ 𝟭 _
```

## Tag 08QF, a lemma

[Tag 08QF](https://stacks.math.columbia.edu/tag/08QF) in the Stacks Project.

**`CommAlgCat.cotangentComplex_homologyZeroIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/HomologyZero.lean, line 345](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/HomologyZero.lean#L345).

> **Stacks Project, Tag 08QF.** The degree-zero homology of the cotangent complex `L_{B/A}` is
> the module of Kähler differentials `Ω[B⁄A]`.

```lean
public noncomputable def cotangentComplex_homologyZeroIso :
    (cotangentComplex A B).homology 0 ≅ ModuleCat.of B (KaehlerDifferential A B)
```

## Tag 08QG, a lemma

[Tag 08QG](https://stacks.math.columbia.edu/tag/08QG) in the Stacks Project.

**`CommAlgCat.polynomialEvaluationLowerShriekAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteShriek.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSiteShriek.lean#L137). The attribute's comment: “evaluation at B → B is a lower shriek”.

> **Stacks 08QG.** For `B` a polynomial algebra over `A`, evaluation at the identity
> augmentation `B → B` is left adjoint to `π^{-1}`: it *is* a lower shriek.

```lean
def polynomialEvaluationLowerShriekAdjunction (hB : IsPolynomialAlgebra A B) :
    Stacks.ChaoticSite.evaluationLowerShriek AddCommGrpCat.{max (u + 1) m}
        (polynomialIdentityObj A B hB) (polynomialTopology A B) ⊣
      polynomialAbelianInverseImage.{m} A B
```

**`CommAlgCat.polynomialAbelianLowerShriekEvaluationIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteShriek.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSiteShriek.lean#L147). The attribute's comment: “π\_! is evaluation at B → B”.

> **Stacks 08QG.** For `B` a polynomial algebra over `A`, the lower shriek `π_!` of Stacks 08PR
> is canonically evaluation at the identity augmentation `B → B`.

```lean
def polynomialAbelianLowerShriekEvaluationIso (hB : IsPolynomialAlgebra A B) :
    polynomialAbelianLowerShriek.{m} A B ≅
      Stacks.ChaoticSite.evaluationLowerShriek AddCommGrpCat.{max (u + 1) m}
        (polynomialIdentityObj A B hB) (polynomialTopology A B)
```

**`CommAlgCat.polynomialAbelianLowerShriek_pointSectionsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteShriek.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSiteShriek.lean#L157). The attribute's comment: “π\_!F = F(B → B)”.

> **Stacks 08QG.** `π_!ℱ = ℱ(B → B)`: the sections of `π_!ℱ` at the point are the sections of
> `ℱ` over the identity augmentation, naturally in `ℱ`.

```lean
def polynomialAbelianLowerShriek_pointSectionsIso (hB : IsPolynomialAlgebra A B) :
    polynomialAbelianLowerShriek.{m} A B ⋙
        Stacks.ChaoticSite.pointSections AddCommGrpCat.{max (u + 1) m} ≅
      sheafToPresheaf (polynomialTopology A B) AddCommGrpCat.{max (u + 1) m} ⋙
        (evaluation (polynomialSite A B)ᵒᵖ AddCommGrpCat.{max (u + 1) m}).obj
          (polynomialIdentityObj A B hB)
```

**`CommAlgCat.polynomialAbelianLowerShriek_preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteShriek.lean, line 170](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSiteShriek.lean#L170). The attribute's comment: “π\_! is exact: finite limits”.

> **Stacks 08QG.** For `B` a polynomial algebra over `A`, `π_!` preserves finite limits. With
> `CommAlgCat.polynomialAbelianLowerShriek_preservesColimitsOfShape` this is the exactness of `π_!`
> asserted by the source.

```lean
theorem polynomialAbelianLowerShriek_preservesFiniteLimits (hB : IsPolynomialAlgebra A B) :
    PreservesFiniteLimits (polynomialAbelianLowerShriek.{m} A B)
```

**`CommAlgCat.polynomialAbelianLowerShriek_preservesColimitsOfShape`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteShriek.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSiteShriek.lean#L178). The attribute's comment: “π\_! is exact: colimits”.

> **Stacks 08QG.** `π_!` preserves all colimits, being a left adjoint; no hypothesis on `B` is
> needed for this half of exactness.

```lean
instance polynomialAbelianLowerShriek_preservesColimitsOfShape {K : Type*} [Category* K] :
    PreservesColimitsOfShape K (polynomialAbelianLowerShriek.{m} A B)
```

## Tag 08QH, a lemma

[Tag 08QH](https://stacks.math.columbia.edu/tag/08QH) in the Stacks Project.

**`CommAlgCat.cotangentComplex_iso_kaehlerDifferential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebra.lean, line 285](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebra.lean#L285).

> **Stacks Project, Tag 08QH.** If `B` is a polynomial algebra over the ring `A`, then the
> cotangent complex `L_{B/A}` is quasi-isomorphic to `Ω[B⁄A][0]`.

```lean
public theorem cotangentComplex_iso_kaehlerDifferential (hB : Algebra.IsPolynomialAlgebra A B) :
    Nonempty
      (DerivedCategory.Q.obj (cotangentComplex A B) ≅
        (DerivedCategory.singleFunctor (ModuleCat.{max u v} B) 0).obj
          (ModuleCat.of B (KaehlerDifferential A B)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 92.4, Tag 08PQ](https://stacks.math.columbia.edu/tag/08PQ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
