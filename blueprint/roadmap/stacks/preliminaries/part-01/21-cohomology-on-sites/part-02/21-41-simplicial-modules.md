---
declaration: section
origin: cited
lean: Stacks.SimplicialModules.derivedProjectionLowerShriekIsoMooreComplex, Stacks.SimplicialModules.derivedProjectionLowerShriekIsoMooreComplexModules, Stacks.SimplicialModules.simplicialSheafEquivalence, Stacks.SimplicialModules.SimplicialModule, Stacks.SimplicialModules.ringSheaf, Stacks.SimplicialModules.isIso_derivedBaseChangeComparison, Stacks.SimplicialModules.isIso_derivedLowerShriekHomology_map_of_fibrewise, Stacks.SimplicialModules.isIso_derivedLowerShriekHomology_map_of_fibrewise_unconditional
statement: formalized
proof: formalized
---

# 21.41 Simplicial modules

Section 21.41 of the Stacks Project, [Tag 09D0](https://stacks.math.columbia.edu/tag/09D0). 4 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09D0, the section

[Tag 09D0](https://stacks.math.columbia.edu/tag/09D0) in the Stacks Project.

**`Stacks.SimplicialModules.derivedProjectionLowerShriekIsoMooreComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/DerivedProjectionMooreComplex.lean, line 496](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/DerivedProjectionMooreComplex.lean#L496). The attribute's comment: “Lπ_!(ℱ_•) is represented by the alternating-face-map complex s(ℱ_•) of the simplicial abelian sheaf ℱ_•, for every abelian sheaf on Δ × C — in particular for the underlying abelian sheaf of a simplicial A_•-module over any simplicial sheaf of rings A_•, the Lπ_! of the section being the abelian one of Remark 09CY. Proved from Stacks 08PJ's two inputs as the source directs: the acyclicity of π_! and the Moore computation over Δ”.

> **Stacks 09D0.** Let `(C, J)` be a small site and let `Δ × C` carry the topology inherited
> from `(C, J)` along the projection `π : Δ × C ⥤ C`. For every sheaf of abelian groups `ℱ` on
> `Δ × C`, the abelian derived lower shriek of Remark 09CY carries `ℱ` to the associated chain
> complex of the simplicial abelian sheaf `ℱ_•` that `ℱ` is:
>
> `Lπ_!(ℱ[0]) ≅ s(ℱ_•)` in `D(Ab(C))`,
>
> where `s(ℱ_•)` is the alternating-face-map complex of `ℱ_• = fibrewise ℱ`, read as a cochain
> complex over `ℤ` in non-positive degrees.
>
> This is the source's own argument: a resolution of `ℱ` by direct sums of the free abelian
> sheaves `j_{W!}ℤ_W` (Stacks 06XX) computes `Lπ_!` because `π_!` is acyclic on those
> (`Stacks.SimplicialModules.abelianLowerShriekAcyclic_projection`, which is Lemma 21.40.2), and
> the degreewise colimit over `Δᵒᵖ` of such a resolution is the Moore complex
> (`Stacks.ChaoticSite.GeneralValued.mooreCochainQIsoColimOfResolution`, which is Lemma
> 21.39.7).

```lean
def derivedProjectionLowerShriekIsoMooreComplex
    (F : Sheaf (projectionTopology C J) AddCommGrpCat.{w}) :
    (derivedAbelianLowerShriek.{w} (projectionTopology C J) J (projection C)).obj
        (DerivedCategory.Q.obj
          ((HomologicalComplex.single (Sheaf (projectionTopology C J) AddCommGrpCat.{w})
            (ComplexShape.up ℤ) 0).obj F)) ≅
      DerivedCategory.Q.obj
        ((Stacks.ChaoticSite.GeneralValued.mooreCochainComplex (𝟭 SimplexCategory)
          (Sheaf J AddCommGrpCat.{w})).obj ((fibrewise J AddCommGrpCat.{w}).obj F))
```

**`Stacks.SimplicialModules.derivedProjectionLowerShriekIsoMooreComplexModules`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/DerivedProjectionMooreComplexModules.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/DerivedProjectionMooreComplexModules.lean#L236). The attribute's comment: “the MODULE-coefficient representation: for a simplicial sheaf of O-modules ℱ_•, equivalently a sheaf of π^{-1}O-modules on Δ × C, Lπ_!(ℱ_•) is represented by the associated chain complex s(ℱ_•) in D(O). This is the form in which the untagged paragraph of Section 09D0 is used by Tag 09DH, whose triangle lives in D(ℬ); the abelian registration beside it, derivedProjectionLowerShriekIsoMooreComplex, cannot reach it because derived lower shriek does not commute with forgetting the module structure”.

> **Stacks 09D0 at module coefficients.** Let `(C, J)` be a small site, let `O` be a sheaf of
> rings on it and let `Δ × C` carry the topology inherited from `(C, J)` along the projection
> `π : Δ × C ⥤ C`. For every sheaf of `π^{-1}O`-modules `ℱ` on `Δ × C`, the derived lower shriek of
> Remark 09CY carries `ℱ` to the associated chain complex of the simplicial sheaf of `O`-modules
> `ℱ_•` that `ℱ` is:
>
> `Lπ_!(ℱ[0]) ≅ s(ℱ_•)` in `D(O)`,
>
> where `s(ℱ_•)` is the alternating-face-map complex of `ℱ_• = fibrewiseMod ℱ`, read as a cochain
> complex over `ℤ` in non-positive degrees.
>
> This is the source's own argument, run at module coefficients: a resolution of `ℱ` by direct sums
> of the `j_{W!}(π^{-1}O)_W` (Stacks 06XX) computes `Lπ_!` because `π_!` is acyclic on those
> (`Stacks.Cohomology.DerivedLowerShriek.lowerShriekAcyclic_of_preservesCoveringPullbacks`, which
> is Lemma 21.40.2), and the degreewise colimit over `Δᵒᵖ` of such a resolution is the Moore
> complex (`Stacks.ChaoticSite.GeneralValued.mooreCochainQIsoColimOfResolution`, which is Lemma
> 21.39.7).

```lean
def derivedProjectionLowerShriekIsoMooreComplexModules
    (F : SheafOfModules.{w} (projectionRing C J O)) :
    (derivedProjectionLowerShriek C J O).obj
        (DerivedCategory.Q.obj
          ((HomologicalComplex.single (SheafOfModules.{w} (projectionRing C J O))
            (ComplexShape.up ℤ) 0).obj F)) ≅
      DerivedCategory.Q.obj
        ((Stacks.ChaoticSite.GeneralValued.mooreCochainComplex (𝟭 SimplexCategory)
          (SheafOfModules.{w} O)).obj ((fibrewiseMod C J O).obj F))
```

**`Stacks.SimplicialModules.simplicialSheafEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/SimplicialSheafEquivalence.lean, line 362](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/SimplicialSheafEquivalence.lean#L362). The attribute's comment: “a simplicial sheaf on C is the same thing as a sheaf on Δ × C for the topology inherited along π”.

> **Stacks 09D0.** A sheaf on `Δ × C` *is* a simplicial sheaf on `C`: levelwise restriction to
> the fibres and uncurrying are an equivalence of categories.

```lean
def simplicialSheafEquivalence (A : Type u₁) [Category.{v₁} A] :
    Sheaf ((CategoryTheory.Prod.snd SimplexCategory C).inheritedTopology J) A ≌
      CategoryTheory.SimplicialObject (Sheaf J A)
```

## Tag 09D1, a definition

[Tag 09D1](https://stacks.math.columbia.edu/tag/09D1) in the Stacks Project.

**`Stacks.SimplicialModules.SimplicialModule`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/SimplicialModules.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/SimplicialModules.lean#L50).

> A simplicial module over a simplicial sheaf of rings `A` is a presheaf of modules over the
> associated ring presheaf on `Δ × C` whose underlying abelian-group presheaf is a sheaf for the
> topology inherited from `C`.

```lean
abbrev SimplicialModule (A : SimplicialObject (Sheaf J RingCat.{r}))
```

**`Stacks.SimplicialModules.ringSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/SimplicialModulesAbelian.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/SimplicialModulesAbelian.lean#L275). The attribute's comment: “the sheaf of rings on Δ × C associated to A_•”.

> **Stacks 09D1.** The sheaf of rings on `Δ × C` associated to a simplicial sheaf of rings.
> The sheaf condition is `isSheaf_associatedRingPresheaf`.

```lean
def ringSheaf :
    Sheaf ((CategoryTheory.Prod.snd SimplexCategory C).inheritedTopology J) RingCat.{r}
```

## Tag 09D2, a lemma

[Tag 09D2](https://stacks.math.columbia.edu/tag/09D2) in the Stacks Project.

**`Stacks.SimplicialModules.isIso_derivedBaseChangeComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/LowerShriekBaseChange.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/LowerShriekBaseChange.lean#L330).

> Let `C` be a site and `A_• ⟶ B_•` a homomorphism of simplicial sheaves of (commutative) rings
> on `C`. If `Lπ_!A_• ⟶ Lπ_!B_•` is an isomorphism in `D(C)`, then the canonical map
> `Lπ_!(K) ⟶ Lπ_!(K ⊗^L_{A_•} B_•)` is an isomorphism for every `K` in `D(A_•)`.

```lean
theorem isIso_derivedBaseChangeComparison : IsIso (derivedBaseChangeComparison J φ)
```

**`Stacks.SimplicialModules.isIso_derivedLowerShriekHomology_map_of_fibrewise`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/SimplicialSiteLowerShriek.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/SimplicialSiteLowerShriek.lean#L146). The attribute's comment: “the reduction to the fibre categories Δ × U”.

> **The reduction of Stacks 09D2 to the fibre categories.** Let `C` be a site and let
> `π : Δ × C ⥤ C` be the projection. A morphism `a` of abelian sheaves on `Δ × C` which induces an
> isomorphism on the degree `n` homology of the fibre over every object of `C` is inverted by
> `L_nπ_!`.
>
> This is the step of the proof of Stacks 09D2 which, both sides of the asserted identity being
> sheaves, computes their cohomology sheaves by the procedure of Stacks 08PI and so reduces the
> lemma to the restriction of the coefficients to the fibre categories `Δ × U`, where the source
> appeals to Stacks 08RX. It is not the lemma: the derived tensor product, the flat resolution and
> Stacks 08RX itself do not appear. See the scope paragraph of the module docstring.
>
> The two acyclicity statements of Stacks 08PJ are taken as arguments here;
> `isIso_derivedLowerShriekHomology_map_of_fibrewise_unconditional` is the same reduction with
> both discharged.

```lean
theorem isIso_derivedLowerShriekHomology_map_of_fibrewise
    (h : (simplicialSituation B).AbelianLowerShriekAcyclic)
    (hcov : (simplicialSituation B).UliftFreeCoverLowerShriekAcyclic) (n : ℕ)
    {F G : Sheaf (simplicialSituation B).topology AddCommGrpCat.{max w u}} (a : F ⟶ G)
    (ha : ∀ U : B.Cᵒᵖ, IsIso (((fiberHomologyPresheafFunctor (simplicialSituation B) n).map
      ((sheafToPresheaf (simplicialSituation B).topology
        AddCommGrpCat.{max w u}).map a)).app U)) :
    IsIso (((simplicialSituation B).derivedAbelianLowerShriekHomology n).map a)
```

**`Stacks.SimplicialModules.isIso_derivedLowerShriekHomology_map_of_fibrewise_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/SimplicialSiteLowerShriek.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/SimplicialSiteLowerShriek.lean#L172). The attribute's comment: “the reduction to the fibre categories Δ × U”.

> **The reduction of Stacks 09D2 to the fibre categories**, with no hypothesis. Let `C` be a
> site and let `π : Δ × C ⥤ C` be the projection. A morphism `a` of abelian sheaves on `Δ × C`
> which induces an isomorphism on the degree `n` homology of the fibre over every object of `C` is
> inverted by `L_nπ_!`.
>
> Both acyclicity statements of Stacks 08PJ are discharged rather than carried:
> `StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/ProjectionLowerShriekAcyclic.lean` proves Stacks 0D6X along the projection of a fibred category,
> hence `FibredCategorySituation.abelianLowerShriekAcyclic` and the instance giving `Lπ_!`, and
> `StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/UliftFreeCoverGenerators.lean` proves
> `FibredCategorySituation.abelianLowerShriekGeneratorsAcyclic`, from which the acyclicity of the
> sheafified canonical presentation follows by
> `uliftFreeCoverLowerShriekAcyclic_of_generatorsAcyclic`.
>
> It is still not the lemma, for the reasons in the scope paragraph of the module docstring.

```lean
theorem isIso_derivedLowerShriekHomology_map_of_fibrewise_unconditional (n : ℕ)
    {F G : Sheaf (simplicialSituation B).topology AddCommGrpCat.{max w u}} (a : F ⟶ G)
    (ha : ∀ U : B.Cᵒᵖ, IsIso (((fiberHomologyPresheafFunctor (simplicialSituation B) n).map
      ((sheafToPresheaf (simplicialSituation B).topology
        AddCommGrpCat.{max w u}).map a)).app U)) :
    IsIso (((simplicialSituation B).derivedAbelianLowerShriekHomology n).map a)
```

## Tag 09D3, a remark

[Tag 09D3](https://stacks.math.columbia.edu/tag/09D3) in the Stacks Project.

**`Stacks.SimplicialModules.augmentedDerivedLowerShriek`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/AugmentedDerivedLowerShriek.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/AugmentedDerivedLowerShriek.lean#L149). The attribute's comment: “the functor `Lπ_! : D(A_•) ⟶ D(O)`, the composition of `- ⊗^L_{A_•} O` with the functor `Lπ_! : D(Δ × C, π^{-1}O) ⟶ D(O)` of Remark 09CY”.

> **Remark 09D3, the functor.** For an augmentation `ε : A_• ⟶ O` of a simplicial sheaf of rings
> by a sheaf of rings, `Lπ_! : D(A_•) ⥤ D(O)` is the composite of derived base change
> `- ⊗^L_{A_•} O : D(A_•) ⥤ D(Δ × C, π^{-1}O)` with the functor
> `Lπ_! : D(Δ × C, π^{-1}O) ⥤ D(O)` of Remark 09CY.

```lean
def augmentedDerivedLowerShriek (ε : CommAugmentation J A O) :
    DerivedCategory (Modules J A) ⥤
      DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf O))
```

**`Stacks.SimplicialModules.augmentedDerivedLowerShriek_commShift`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/AugmentedDerivedLowerShriek.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/AugmentedDerivedLowerShriek.lean#L157). The attribute's comment: “`Lπ_! : D(A_•) ⟶ D(O)` is a functor of triangulated categories: it commutes with the shift”.

> **Remark 09D3, exactness: the functor commutes with the shift.**

```lean
instance augmentedDerivedLowerShriek_commShift (ε : CommAugmentation J A O) :
    (augmentedDerivedLowerShriek J ε).CommShift ℤ
```

**`Stacks.SimplicialModules.augmentedDerivedLowerShriek_isTriangulated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/AugmentedDerivedLowerShriek.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/AugmentedDerivedLowerShriek.lean#L164). The attribute's comment: “`Lπ_! : D(A_•) ⟶ D(O)` is an exact functor of triangulated categories”.

> **Remark 09D3, exactness: `Lπ_! : D(A_•) ⥤ D(O)` is an exact functor of triangulated
> categories**, as a composite of two exact functors.

```lean
instance augmentedDerivedLowerShriek_isTriangulated (ε : CommAugmentation J A O) :
    (augmentedDerivedLowerShriek J ε).IsTriangulated
```

**`Stacks.SimplicialModules.augmentedDerivedLowerShriekForgetIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/AugmentedDerivedLowerShriek.lean, line 398](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/AugmentedDerivedLowerShriek.lean#L398). The attribute's comment: “the `O`-module structure on `Lπ_!(K)`: under the hypothesis that `ε` induces a quasi-isomorphism `s(A_•) ⟶ O`, the canonical, functorial identification of `Lπ_!(K)` with `Lπ_!(K ⊗^L_{A_•} O)` of Lemma 09D2, read as the underlying complex of abelian sheaves of the object `Lπ_!(K)` of `D(O)`”.

> **Remark 09D3, the `O`-module structure on `Lπ_!(K)`.** Let `ε : A_• ⟶ O` be an augmentation
> inducing a quasi-isomorphism `s(A_•) ⟶ O`. For `K` in `D(A_•)`, `Lπ_!(K)` is canonically and
> functorially identified with `Lπ_!(K ⊗^L_{A_•} O)` by Lemma 09D2, and the latter is, by
> Remark 09CY, the underlying complex of abelian sheaves of the object `Lπ_!(K)` of `D(O)` of
> `augmentedDerivedLowerShriek`. So, naturally in `K`, forgetting the `O`-module structure of the
> functor of the source gives back `Lπ_!(K)`.

```lean
def augmentedDerivedLowerShriekForgetIso (ε : CommAugmentation J A O)
    (hε : InducesQuasiIso J ε) :
    augmentedDerivedLowerShriek J ε ⋙
        (SheafOfModules.toSheaf (Stacks.SheafOfModules.Tensor.ringSheaf O)).mapDerivedCategory ≅
      moduleDerivedLowerShriek J A
```

**`Stacks.SimplicialModules.augmentedLowerShriek`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/AugmentedLowerShriek.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/AugmentedLowerShriek.lean#L155). The attribute's comment: “the functor Lπ_! : D(A_•) ⟶ D(O). Two inputs of the source are carried as explicit parameters, the library not yet having them: `base` is derived extension of scalars `- ⊗^L_{A_•} O`, introduced in the untagged prose before Lemma 09D2, and `proj` is the functor Lπ_! : D(π^{-1}O) ⟶ D(O) of Tag 09CY, which is Tag 08PC part (3) for modules and is reduced in this library to the acyclicity statement of Tag 0794 at the class of direct sums of the j_{U!} O_U; see the implementation notes for what that still owes”.

> **Stacks 09D3.** Derived lower shriek along an augmented simplicial sheaf of rings:
> `Lπ_! : D(A_•) ⟶ D(O)`, the composite of derived extension of scalars along the augmentation
> with derived lower shriek on modules over `π^{-1}O`.

```lean
def augmentedLowerShriek (_ε : Augmentation J A O)
    (base : DerivedCategory (SimplicialModule.{w, v, u, r} J A) ⥤
      DerivedCategory (SimplicialModule.{w, v, u, r} J (constantRing J O)))
    (proj : DerivedCategory (SimplicialModule.{w, v, u, r} J (constantRing J O)) ⥤
      DerivedCategory D) :
    DerivedCategory (SimplicialModule.{w, v, u, r} J A) ⥤ DerivedCategory D
```

**`Stacks.SimplicialModules.augmentedLowerShriek_commShift`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/AugmentedLowerShriek.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/AugmentedLowerShriek.lean#L166). The attribute's comment: “the functor commutes with the shift”.

> **Stacks 09D3.** Derived lower shriek along an augmented simplicial sheaf of rings commutes
> with the shift.

```lean
instance augmentedLowerShriek_commShift (ε : Augmentation J A O)
    (base : DerivedCategory (SimplicialModule.{w, v, u, r} J A) ⥤
      DerivedCategory (SimplicialModule.{w, v, u, r} J (constantRing J O)))
    (proj : DerivedCategory (SimplicialModule.{w, v, u, r} J (constantRing J O)) ⥤
      DerivedCategory D) [base.CommShift ℤ] [proj.CommShift ℤ] :
    (augmentedLowerShriek J ε base proj).CommShift ℤ
```

**`Stacks.SimplicialModules.augmentedLowerShriek_isTriangulated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/AugmentedLowerShriek.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/AugmentedLowerShriek.lean#L177). The attribute's comment: “the functor is exact”.

> **Stacks 09D3.** Derived lower shriek along an augmented simplicial sheaf of rings is an
> exact functor of triangulated categories.

```lean
instance augmentedLowerShriek_isTriangulated (ε : Augmentation J A O)
    (base : DerivedCategory (SimplicialModule.{w, v, u, r} J A) ⥤
      DerivedCategory (SimplicialModule.{w, v, u, r} J (constantRing J O)))
    (proj : DerivedCategory (SimplicialModule.{w, v, u, r} J (constantRing J O)) ⥤
      DerivedCategory D) [base.CommShift ℤ] [proj.CommShift ℤ]
    [base.IsTriangulated] [proj.IsTriangulated] :
    (augmentedLowerShriek J ε base proj).IsTriangulated
```

**`Stacks.SimplicialModules.augmentedLowerShriek_derivedTarget`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/AugmentedLowerShriek.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/AugmentedLowerShriek.lean#L210). The attribute's comment: “the functor Lπ_! : D(A_•) ⟶ D(O), at the target D(O) the source names and with the abelian structure and the derived category of both categories of simplicial modules discharged rather than assumed. Two inputs of the source are carried as explicit parameters, the library not yet having them: `base` is derived extension of scalars `- ⊗^L_{A_•} O`, introduced in the untagged prose before Lemma 09D2, and `proj` is the functor Lπ_! : D(π^{-1}O) ⟶ D(O) of Tag 09CY, whose underived half is `Stacks.SimplicialModules.moduleLowerShriek` and whose total left derived functor is part (3) of Tag 08PC, open here”.

> **Stacks 09D3.** Derived lower shriek along an augmented simplicial sheaf of rings,
> `Lπ_! : D(A_•) ⟶ D(O)` with `D(O)` the derived category of the sheaves of `O`-modules on `C`,
> which is the `D(O)` of the source.
>
> Nothing is assumed about either category of simplicial modules: the abelian structure is
> `Stacks.SimplicialModules.abelian` and the derived category is `HasDerivedCategory.standard`,
> both seated as local instances. That abelian structure is supplied at sections universe
> `max u v r w`, which is why the module sections are taken there.

```lean
def augmentedLowerShriek_derivedTarget (_ε : Augmentation J A O)
    (base : DerivedCategory (SimplicialModule.{max u v r w, v, u, r} J A) ⥤
      DerivedCategory (SimplicialModule.{max u v r w, v, u, r} J (constantRing J O)))
    (proj : DerivedCategory (SimplicialModule.{max u v r w, v, u, r} J (constantRing J O)) ⥤
      DerivedCategory (SheafOfModules.{max u v r w} O)) :
    DerivedCategory (SimplicialModule.{max u v r w, v, u, r} J A) ⥤
      DerivedCategory (SheafOfModules.{max u v r w} O)
```

**`Stacks.SimplicialModules.augmentedLowerShriek_derivedTarget_commShift`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/AugmentedLowerShriek.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/AugmentedLowerShriek.lean#L222). The attribute's comment: “the functor commutes with the shift, at the target D(O) the source names”.

> **Stacks 09D3.** Derived lower shriek along an augmented simplicial sheaf of rings commutes
> with the shift, at the target `D(O)`.

```lean
instance augmentedLowerShriek_derivedTarget_commShift (ε : Augmentation J A O)
    (base : DerivedCategory (SimplicialModule.{max u v r w, v, u, r} J A) ⥤
      DerivedCategory (SimplicialModule.{max u v r w, v, u, r} J (constantRing J O)))
    (proj : DerivedCategory (SimplicialModule.{max u v r w, v, u, r} J (constantRing J O)) ⥤
      DerivedCategory (SheafOfModules.{max u v r w} O))
    [base.CommShift ℤ] [proj.CommShift ℤ] :
    (augmentedLowerShriek_derivedTarget.{w} J ε base proj).CommShift ℤ
```

**`Stacks.SimplicialModules.augmentedLowerShriek_derivedTarget_isTriangulated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/AugmentedLowerShriek.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/AugmentedLowerShriek.lean#L234). The attribute's comment: “the functor is exact, at the target D(O) the source names”.

> **Stacks 09D3.** Derived lower shriek along an augmented simplicial sheaf of rings is an
> exact functor of triangulated categories, at the target `D(O)`.

```lean
instance augmentedLowerShriek_derivedTarget_isTriangulated (ε : Augmentation J A O)
    (base : DerivedCategory (SimplicialModule.{max u v r w, v, u, r} J A) ⥤
      DerivedCategory (SimplicialModule.{max u v r w, v, u, r} J (constantRing J O)))
    (proj : DerivedCategory (SimplicialModule.{max u v r w, v, u, r} J (constantRing J O)) ⥤
      DerivedCategory (SheafOfModules.{max u v r w} O))
    [base.CommShift ℤ] [proj.CommShift ℤ]
    [base.IsTriangulated] [proj.IsTriangulated] :
    (augmentedLowerShriek_derivedTarget.{w} J ε base proj).IsTriangulated
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.41, Tag 09D0](https://stacks.math.columbia.edu/tag/09D0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
