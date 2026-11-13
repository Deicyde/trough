---
declaration: section
origin: cited
lean: Dualizing.AnyModel.restrictScalarsDerived_adj_derivedHom, Dualizing.derivedHomCompIso, Dualizing.restrictDerivedHomIsoDerivedHomAlong, Dualizing.derivedHomHomologyLinearEquivExt, Dualizing.derivedCoextendScalarsCompDerivedRestrictScalarsIso, Dualizing.derivedCoextendScalarsHomologyLinearEquivExt, Dualizing.isBoundedBelowCoherent_obj_rightDerivedCoextendScalars, Dualizing.DGAResolution
statement: formalized
proof: formalized
---

# 47.13 Trivial duality for a ring map

Section 47.13 of the Stacks Project, [Tag 0A6Z](https://stacks.math.columbia.edu/tag/0A6Z). 9 tags here are carried by 23 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0A70, a lemma

[Tag 0A70](https://stacks.math.columbia.edu/tag/0A70) in the Stacks Project.

**`Dualizing.AnyModel.restrictScalarsDerived_adj_derivedHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DerivedHomAnyModel.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/DerivedHomAnyModel.lean#L141).

> **Stacks 0A70.** Derived coextension of scalars `RHom_A(B, -)` is right adjoint to restriction
> of scalars from `D(B)` to `D(A)`, for arbitrary chosen models of the two derived categories.
>
> This is the model-generic form of `Dualizing.restrictScalarsDerived_adj_derivedHom`, which is
> silently specialised to `HasDerivedCategory.standard`; it is recovered from this by supplying that
> instance.

```lean
theorem restrictScalarsDerived_adj_derivedHom (f : A →+* B) :
    Nonempty ((ModuleCat.restrictScalars.{max v u u'} f).mapDerivedCategory ⊣
      derivedHom.{u, v, u', w, w'} f)
```

## Tag 0C0F, a lemma

[Tag 0C0F](https://stacks.math.columbia.edu/tag/0C0F) in the Stacks Project.

**`Dualizing.derivedHomCompIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TrivialDuality.lean, line 356](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/TrivialDuality.lean#L356).

> For ring maps `A → B → C`, the composite `RHom_B(C, -) ∘ RHom_A(B, -)` is naturally
> isomorphic to `RHom_A(C, -)`.

```lean
theorem derivedHomCompIso (f : A →+* B) (g : B →+* C) :
    Nonempty
      (derivedHom.{u, v} f ⋙ derivedHom.{u, v} g ≅
        derivedHom.{u, v} (g.comp f))
```

## Tag 0A71, a lemma

[Tag 0A71](https://stacks.math.columbia.edu/tag/0A71) in the Stacks Project.

**`Dualizing.restrictDerivedHomIsoDerivedHomAlong`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/CoextendRestrictComparison/Constructed.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/CoextendRestrictComparison/Constructed.lean#L107). The attribute's comment: “derived Hom after restriction, with both derived functors constructed: RHom(B, -) is AnyModel.derivedHom, the total right derived functor of coextension of scalars, and RHom\_A(B, -) is derivedHomAlong, that of Hom\_A(B, -). Both rings in one universe, modules in max v u, arbitrary models of the two derived categories”.

> **Stacks 0A71**, the displayed formula, with both derived functors constructed:
> `φ_* RHom(B, K) = RHom_A(B, K)`, where `φ_* : D(B) ⥤ D(A)` is restriction of scalars.
>
> Restricting the constructed derived coextension functor `Dualizing.AnyModel.derivedHom f` to
> `D(A)` is the constructed `A`-valued derived Hom functor `Dualizing.derivedHomAlong f`, by the
> unique isomorphism compatible with the two derived units. This is
> `Dualizing.derivedCoextendScalarsCompDerivedRestrictScalarsIso` with all four of its parameters
> discharged: `RH`, `β` by `Dualizing.derivedHomAlong`, `Dualizing.derivedHomAlongUnit`, and
> `RF`, `α` by `Dualizing.AnyModel.derivedHom`, `Dualizing.AnyModel.derivedHomUnit`.

```lean
def restrictDerivedHomIsoDerivedHomAlong (f : A →+* B) :
    { e : AnyModel.derivedHom.{u, v, u, wA, wB} f ⋙
          (ModuleCat.restrictScalars.{max v u} f).mapDerivedCategory ≅
        derivedHomAlong.{u, v, wA} f //
      restrictedDerivedUnit f (AnyModel.derivedHom.{u, v, u, wA, wB} f)
            (AnyModel.derivedHomUnit.{u, v, wA, wB} f) ≫
          Functor.whiskerLeft DerivedCategory.Qh e.hom =
        derivedHomAlongUnit.{u, v, wA} f }
```

**`Dualizing.derivedHomHomologyLinearEquivExt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/CoextendRestrictComparison/Constructed.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/CoextendRestrictComparison/Constructed.lean#L129). The attribute's comment: “cohomology as Ext, with the derived functor constructed: RHom(B, -) is AnyModel.derivedHom, the total right derived functor of coextension of scalars. Both rings in one universe, modules in max v u, arbitrary models of the two derived categories”.

> **Stacks 0A71**, the "in particular" clause, with the derived functor constructed:
> `R^q Hom(B, K) = Ext^q_A(B, K)`.
>
> The cohomology of the constructed derived coextension functor `Dualizing.AnyModel.derivedHom f`,
> restricted to `A`-modules, is `Ext^q_A(B, K)`, `A`-linearly, naturally in `K` and normalized by
> the derived unit. This is `Dualizing.derivedCoextendScalarsHomologyLinearEquivExt` with its
> parameters `RF`, `α` discharged by `Dualizing.AnyModel.derivedHom` and
> `Dualizing.AnyModel.derivedHomUnit`.

```lean
def derivedHomHomologyLinearEquivExt (f : A →+* B) :
    HomologyExtComparison f (AnyModel.derivedHom.{u, v, u, wA, wB} f)
      (AnyModel.derivedHomUnit.{u, v, wA, wB} f)
```

**`Dualizing.derivedCoextendScalarsCompDerivedRestrictScalarsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TrivialDualityRing/Basic.lean, line 247](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/TrivialDualityRing/Basic.lean#L247). The attribute's comment: “derived Hom after restriction, for arbitrary right derived functors RF of coextension of scalars and RH of Hom\_A(B, -); the data RF, alpha, RH, beta is discharged by AnyModel.derivedHom with AnyModel.derivedHomUnit and derivedHomAlong with derivedHomAlongUnit, giving the unconditional restrictDerivedHomIsoDerivedHomAlong”.

> Restricting derived coextension gives `RHom_A(B, -)`, with the comparison uniquely
> specified by its compatibility with the derived units.
>
> Both derived functors enter as arbitrary right derived functors presented by their universal
> properties, so the statement is independent of the models chosen for them. That data is
> discharged by `Dualizing.AnyModel.derivedHom` with `Dualizing.AnyModel.derivedHomUnit` on the
> left and by `Dualizing.derivedHomAlong` with `Dualizing.derivedHomAlongUnit` on the right,
> giving the unconditional `Dualizing.restrictDerivedHomIsoDerivedHomAlong`.

```lean
def derivedCoextendScalarsCompDerivedRestrictScalarsIso
    [RF.IsRightDerivedFunctor α (HomotopyCategory.quasiIso (ModuleCat.{max v u} A) (.up ℤ))]
    (RH : DerivedCategory (ModuleCat.{max v u} A) ⥤
      DerivedCategory (ModuleCat.{max v u} A))
    (β : homAlongToDerivedCategory f ⟶ DerivedCategory.Qh ⋙ RH)
    [RH.IsRightDerivedFunctor β (HomotopyCategory.quasiIso (ModuleCat.{max v u} A) (.up ℤ))] :
    { e : RF ⋙ (ModuleCat.restrictScalars.{max v u} f).mapDerivedCategory ≅ RH //
      restrictedDerivedUnit f RF α ≫ Functor.whiskerLeft DerivedCategory.Qh e.hom = β }
```

**`Dualizing.derivedCoextendScalarsHomologyLinearEquivExt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TrivialDualityRing/Ext.lean, line 1024](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/TrivialDualityRing/Ext.lean#L1024). The attribute's comment: “cohomology as Ext, for an arbitrary right derived functor RF of coextension of scalars; the data RF, alpha is discharged by AnyModel.derivedHom with AnyModel.derivedHomUnit, giving the unconditional derivedHomHomologyLinearEquivExt”.

> The cohomology of derived coextension is Ext, naturally and compatibly with the derived
> unit (and hence with the restriction comparison).
>
> Derived coextension enters as an arbitrary right derived functor presented by its universal
> property, so the statement is independent of the model chosen for it. That data is discharged by
> `Dualizing.AnyModel.derivedHom` with `Dualizing.AnyModel.derivedHomUnit`, giving the
> unconditional `Dualizing.derivedHomHomologyLinearEquivExt`.

```lean
def derivedCoextendScalarsHomologyLinearEquivExt
    [RF.IsRightDerivedFunctor α
      (HomotopyCategory.quasiIso (ModuleCat.{max v u} A) (.up ℤ))] :
    HomologyExtComparison f RF α
```

## Tag 0A72, a lemma

[Tag 0A72](https://stacks.math.columbia.edu/tag/0A72) in the Stacks Project.

**`Dualizing.isBoundedBelowCoherent_obj_rightDerivedCoextendScalars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/CoextendRestrictComparison/A72.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/CoextendRestrictComparison/A72.lean#L61).

> Derived coextension of scalars along a finite homomorphism of Noetherian rings sends
> bounded-below complexes with coherent cohomology to bounded-below complexes with coherent
> cohomology.

```lean
theorem isBoundedBelowCoherent_obj_rightDerivedCoextendScalars
    {A B : Type u} [CommRing A] [CommRing B] [IsNoetherianRing A] [IsNoetherianRing B]
    [HasDerivedCategory (ModuleCat.{max v u} A)] [HasDerivedCategory (ModuleCat.{max v u} B)]
    (f : A →+* B) (hf : f.Finite)
    (RF : DerivedCategory (ModuleCat.{max v u} A) ⥤ DerivedCategory (ModuleCat.{max v u} B))
    (alpha : (ModuleCat.coextendScalars f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RF)
    [RF.IsRightDerivedFunctor alpha
      (HomotopyCategory.quasiIso (ModuleCat.{max v u} A) (ComplexShape.up ℤ))]
    {K : DerivedCategory (ModuleCat.{max v u} A)}
    (hK : DerivedCategoryB.derivedCategoryBPlus
      (fun M : ModuleCat.{max v u} A ↦ Module.Finite A M) K) :
    DerivedCategoryB.derivedCategoryBPlus
      (fun M : ModuleCat.{max v u} B ↦ Module.Finite B M) (RF.obj K)
```

## Tag 0BZB, a situation

[Tag 0BZB](https://stacks.math.columbia.edu/tag/0BZB) in the Stacks Project.

**`Dualizing.DGAResolution`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DifferentialGradedResolution.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/DifferentialGradedResolution.lean#L109). The attribute's comment: “resolution data”.

> **Situation 0BZB.** A differential graded resolution of a commutative `R`-algebra `A`: a
> differential graded `R`-algebra `E` together with a homomorphism to `A`, viewed as a
> differential graded algebra with zero differential in degree zero, which is a quasi-isomorphism,
> that is, an isomorphism on cohomology.

```lean
structure DGAResolution (R : Type u) [CommRing R] (A : Type u) [CommRing A] [Algebra R A]
```

**`Dualizing.DGAResolution.derivedEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DifferentialGradedResolution.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/DifferentialGradedResolution.lean#L125). The attribute's comment: “ordinary derived equivalence”.

> **The horizontal equivalence of Situation 0BZB.** Extension of scalars along the resolution,
> followed by the identification of differential graded modules over `A` in degree zero with
> complexes of `A`-modules, is an equivalence `D(E, d) ≌ D(A)`.

```lean
noncomputable def derivedEquivalence :
    derivedCategory' S.E ≌ DerivedCategory (ModuleCat.{u} A)
```

**`Dualizing.DGAResolution.restrictionTriangle`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DifferentialGradedResolution.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/DifferentialGradedResolution.lean#L133). The attribute's comment: “restriction triangle”.

> **The first diagram of Situation 0BZB commutes.** Passing from `D(A)` to `D(E, d)` through
> the equivalence and then forgetting the `E`-action is restriction of scalars along `R → A`.

```lean
noncomputable def restrictionTriangle :
    S.derivedEquivalence.inverse ⋙ derivedForget S.E ≅
      (ModuleCat.restrictScalars.{u} (algebraMap R A)).mapDerivedCategory
```

**`Dualizing.DGAResolution.derivedExtension_comp_iso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DifferentialGradedResolution.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/DifferentialGradedResolution.lean#L269). The attribute's comment: “extension triangle, for an arbitrary left adjoint F of the forgetful functor; its data F, adjF is discharged by derivedExtensionToDGA and derivedExtensionToDGA\_adj, giving the unconditional DGAResolution.derivedExtensionToDGA\_comp\_iso”.

> **The second diagram of Situation 0BZB commutes.** Derived extension of scalars from `D(R)`
> to `D(E, d)` followed by the equivalence `- ⊗_E^𝐋 A` is derived extension of scalars
> `- ⊗_R^𝐋 A : D(R) ⥤ D(A)`.
>
> Derived extension of scalars to the resolution enters as an arbitrary left adjoint `F` of the
> forgetful functor, so the statement is independent of the model chosen for it. That data is
> discharged by `Dualizing.derivedExtensionToDGA` together with
> `Dualizing.derivedExtensionToDGA_adj`, giving the unconditional
> `Dualizing.DGAResolution.derivedExtensionToDGA_comp_iso`.

```lean
noncomputable def derivedExtension_comp_iso
    (F : DerivedCategory (ModuleCat.{u} R) ⥤ derivedCategory' S.E)
    (adjF : F ⊣ derivedForget S.E) :
    F ⋙ S.derivedEquivalence.functor ≅ ordinaryExtension (R := R) (A := A)
```

**`Dualizing.DGAResolution.derivedExtensionToDGA_comp_iso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DifferentialGradedResolutionExtension.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/DifferentialGradedResolutionExtension.lean#L105). The attribute's comment: “extension triangle, with the functor constructed”.

> **The second diagram of Situation 0BZB commutes, with no assumed functor.** Derived
> extension of scalars `- ⊗_R^𝐋 E : D(R) ⥤ D(E, d)` followed by the horizontal equivalence
> `- ⊗_E^𝐋 A : D(E, d) ⥤ D(A)` is derived extension of scalars `- ⊗_R^𝐋 A : D(R) ⥤ D(A)`.
>
> This is `Dualizing.DGAResolution.derivedExtension_comp_iso` with its parameters `F` and `adjF`
> discharged by `Dualizing.derivedExtensionToDGA` and `Dualizing.derivedExtensionToDGA_adj`.

```lean
def derivedExtensionToDGA_comp_iso (S : Dualizing.DGAResolution R A) :
    derivedExtensionToDGA S.E ⋙ S.derivedEquivalence.functor ≅
      Dualizing.DGAResolution.ordinaryExtension (R := R) (A := A)
```

Declarations registered for the tag:

- [`DifferentialGraded.Bimodule.derivedExtensionEquivalence`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedEquivalenceQuasiIso.lean#L329), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/Dualizing/DifferentialGradedResolution.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/DifferentialGradedResolution.lean#L99) (StacksFrontier): “horizontal equivalence”.

## Tag 0BZC, a lemma

[Tag 0BZC](https://stacks.math.columbia.edu/tag/0BZC) in the Stacks Project.

**`Dualizing.DGAResolution.derivedHom_comp_derivedEquivalence_iso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DifferentialGradedResolution.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/DifferentialGradedResolution.lean#L210).

> **Stacks 0BZC.** In Situation 0BZB the functor `R Hom(A, -) : D(R) ⥤ D(A)` is the
> composition of `R Hom(E, -) : D(R) ⥤ D(E, d)` with the equivalence `- ⊗_E^𝐋 A : D(E, d) ⥤ D(A)`.
>
> The functor `R Hom(E, -)` enters as an arbitrary right adjoint `G` of the forgetful functor
> `D(E, d) ⥤ D(R)`, which is what Tag 09LT says derived Hom out of `E` is; so the statement is
> independent of the model chosen for it.

```lean
noncomputable def derivedHom_comp_derivedEquivalence_iso
    (G : DerivedCategory (ModuleCat.{u} R) ⥤ derivedCategory' S.E)
    (adjG : derivedForget S.E ⊣ G) :
    Dualizing.derivedHom.{u, u, u} (algebraMap R A) ≅ G ⋙ S.derivedEquivalence.functor
```

## Tag 0BZD, a lemma

[Tag 0BZD](https://stacks.math.columbia.edu/tag/0BZD) in the Stacks Project.

**`Dualizing.derivedHomIsoGradedDualTensor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DifferentialGradedResolution.lean, line 366](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/DifferentialGradedResolution.lean#L366).

> **Stacks 0BZD.** Let `(E, d)` be a differential graded algebra over a commutative ring `R` —
> in Situation 0BZB, the algebra resolving the `R`-algebra `A` — and let
> `N = Hom^•_R(E^•, R)` be the graded dual of `E^•` over `R`, a differential graded
> `(R, E)`-bimodule. Assume that `E^•` is a compact object of `D(R)` and that `N` computes
> `R Hom(E, R)`. Then `R Hom(E, -) : D(R) ⥤ D(E, d)` is isomorphic to `K ↦ K ⊗_R^𝐋 N`.
>
> Here `D(R)` is the derived category of `R` viewed as a differential graded algebra concentrated
> in degree zero, which is the derived category of `R`-modules by
> `DifferentialGradedModule.degreeZeroDerivedEquivalence`; `R Hom(E, -)` is the right derived
> functor of Tag 09LI for the bimodule `E`, and `- ⊗_R^𝐋 N` the left derived functor of Tag 09LS.
>
> The source deduces this as the case `T = E` of the second assertion of Tag 0BZ0, which is
> `DifferentialGraded.Bimodule.derivedTensorHomDualFunctorIso`; the two hypotheses above are
> exactly its two hypotheses for `T = E`.

```lean
noncomputable def derivedHomIsoGradedDualTensor
    (hcompact : IsCompactBimodule (resolvingBimodule E))
    (hdual : ComputesDerivedHom (resolvingBimodule E)) :
    (derivedHomData E (baseAlgebra R) (resolvingBimodule E).rightModule
        (resolvingBimodule E).leftAction).functor ≅
      Bimodule.derivedTensorFunctor (gradedDualBimodule E)
```

## Tag 0BZE, a lemma

[Tag 0BZE](https://stacks.math.columbia.edu/tag/0BZE) in the Stacks Project.

**`Dualizing.exists_derivedHom_iso_derivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DerivedHomPerfectTensor.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/DerivedHomPerfectTensor.lean#L216). The attribute's comment: “the functor R Hom(A, -) is derived tensoring over R with a differential graded (R, A)-bimodule whose class in D(A) is R Hom(A, R), read through the degree-zero equivalences”.

> **Stacks 0BZE.** Let `R → A` be a map of commutative rings making `A` a
> perfect `R`-module. Then `R Hom(A, -) : D(R) ⥤ D(A)` is a derived tensor product:
> there is a differential graded `(R, A)`-bimodule `M` with `R Hom(A, -) ≅ - ⊗_R^𝐋 M`, whose
> class in `D(A)` is the value `R Hom(A, R)` of that functor at `R`. The two derived categories of
> the degree-zero world are the derived categories of `R`-modules and of `A`-modules through
> `DifferentialGradedModule.degreeZeroDerivedEquivalence`.
>
> A Tate resolution of `A` over `R` exists for every `R`-algebra, along the tautological
> polynomial presentation; it puts us in Situation 0BZB. Perfectness of `A` makes the resolving
> bimodule compact in `D(R)`, and the homogeneous pieces of a Tate resolution are free over `R`,
> which makes its graded dual compute `R Hom(E^•, R)`. Both hypotheses of Stacks 0BZD hold, so
> `Dualizing.DGAResolution.derivedHomIsoDerivedTensor` applies.

```lean
theorem exists_derivedHom_iso_derivedTensor
    (hperf : StacksDraft.Perfect.IsPerfectModule.{u, u, u + 1} (R := R) A) :
    ∃ M : Bimodule (baseAlgebra R) (DifferentialGradedAlgebra.degreeZero R A),
      Nonempty (Dualizing.derivedHom.{u, u, u} (algebraMap R A) ≅
        derivedTensorBimoduleFunctor M) ∧
      Nonempty ((Dualizing.derivedHom.{u, u, u} (algebraMap R A)).obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj (ModuleCat.of R R)) ≅
        (degreeZeroDerivedEquivalence (R := R) (A := A)).functor.obj
          ((toHomotopyCategory (DifferentialGradedAlgebra.degreeZero R A) ⋙
            (quasiIsomorphisms' (DifferentialGradedAlgebra.degreeZero R A)).Q).obj
              M.rightModule))
```

**`Dualizing.nonempty_derivedHom_iso_canonicalDerivedTensor_of_perfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TrivialDualityBundlePerfect.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/TrivialDualityBundlePerfect.lean#L76). The attribute's comment: “in the derived change-of-rings shape of Tag 06Y6, at module universe equal to the ring universe, with no carried hypothesis”.

> **Stacks 0BZE in the derived change-of-rings shape of Tag 06Y6.** Let `f : R → A` make `A` a
> perfect `R`-module and let `L` be a complex of `A`-modules whose class in `D(A)` is the value
> `RHom_R(A, R)` of derived coextension of scalars at the free module of rank one. Then
> `RHom_R(A, -) : D(R) ⥤ D(A)` is the canonical derived change-of-rings tensor product of
> Stacks 06Y6 with `L`.
>
> This is `Dualizing.exists_derivedHom_iso_derivedTensor` — Stacks 0BZE through a Tate resolution —
> carried across `Dualizing.nonempty_derivedTensorBimoduleFunctor_iso_canonical` and then across
> Stacks 0BYK to the chosen representative `L`. No hypothesis beyond the perfectness that
> Stacks 0BZE itself assumes.

```lean
theorem nonempty_derivedHom_iso_canonicalDerivedTensor_of_perfect (f : R →+* A)
    (hperf : letI := f.toAlgebra
      StacksDraft.Perfect.IsPerfectModule.{u, u, u + 1} (R := R) A)
    (L : CochainComplex (ModuleCat.{u} A) ℤ)
    (hL : Nonempty (DerivedCategory.Q.obj L ≅
      (Dualizing.derivedHom.{u, u} f).obj
        ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj (ModuleCat.of R R)))) :
    letI := f.toAlgebra
    Nonempty (Dualizing.derivedHom.{u, u} f ≅
      (canonicalDerivedTensorChangeOfRings.{u, u, u} f L).F)
```

**`Dualizing.derivedHomIsoCanonicalDerivedTensorOfPerfect`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TrivialDualityBundlePerfect.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/TrivialDualityBundlePerfect.lean#L137). The attribute's comment: “in the derived change-of-rings shape of Tag 06Y6, at module universe equal to the ring universe, with no carried hypothesis; the isomorphism is built, at the canonical tensor factor, rather than shown to exist at an arbitrary representative”.

> **Stacks 0BZE in the derived change-of-rings shape of Tag 06Y6, as data.** For `f : R → A`
> making `A` a perfect `R`-module, `RHom_R(A, -) : D(R) ⥤ D(A)` *is* the canonical derived
> change-of-rings tensor product of Stacks 06Y6 with the canonical tensor factor
> `Dualizing.canonicalDerivedHomTensorComplex f`. No existential witness is chosen along the way:
> the Tate resolution is the named one, `Dualizing.DGAResolution.derivedHomIsoDerivedTensor` is a
> construction, and so is `Dualizing.derivedTensorBimoduleFunctorIsoCanonical`, so the isomorphism
> is a function of `f` and `hperf`.
>
> `Dualizing.nonempty_derivedHom_iso_canonicalDerivedTensor_of_perfect` is the form stated at an
> arbitrary complex representing `RHom_R(A, R)`; that form is a proposition because passing from
> this factor to another representative of the same object of `D(A)` goes through a fraction, in
> `Dualizing.InvertibleKernel.derivedTensorIsoOfDerivedIso`.

```lean
def derivedHomIsoCanonicalDerivedTensorOfPerfect (f : R →+* A)
    (hperf : letI := f.toAlgebra
      StacksDraft.Perfect.IsPerfectModule.{u, u, u + 1} (R := R) A) :
    letI := f.toAlgebra
    Dualizing.derivedHom.{u, u} f ≅
      (canonicalDerivedTensorChangeOfRings.{u, u, u} f
        (canonicalDerivedHomTensorComplex f)).F
```

**`Dualizing.nonempty_derivedHom_iso_canonicalDerivedTensor_of_perfect_anyModuleUniverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TrivialDualityBundlePerfectAnyModuleUniverse.lean, line 324](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/TrivialDualityBundlePerfectAnyModuleUniverse.lean#L324). The attribute's comment: “in the derived change-of-rings shape of Tag 06Y6, at an arbitrary module universe above the ring universe, with no carried hypothesis”.

> **Stacks 0BZE in the derived change-of-rings shape of Tag 06Y6, at an arbitrary module
> universe.** Let `f : R → A` make `A` a perfect `R`-module and let `L` be a complex of `A`-modules,
> in a universe `max v u` above the ring universe `u`, whose class in `D(A)` is the value
> `RHom_R(A, R)` of derived coextension of scalars at the free module of rank one on the lifted
> carrier. Then `RHom_R(A, -) : D(R) ⥤ D(A)` is the canonical derived change-of-rings tensor product
> of Stacks 06Y6 with `L`.
>
> This is `Dualizing.nonempty_derivedHom_iso_canonicalDerivedTensor_of_perfect` — which holds at
> module universe equal to the ring universe, the generality of the differential graded chapter —
> renamed along `ULift.ringEquiv`, where the module universe `max v u` *is* the ring universe. All
> three functors involved are carried across that renaming: derived coextension of scalars by
> `StacksDraft.DerivedRingEquivIso.derivedHomRingEquivIso`, and derived extension of scalars together
> with the derived change-of-rings tensor product by
> `StacksDraft.DerivedRingEquivIso.derivedTensorBundleRingEquivIsoOfFactorIso`. The perfectness
> hypothesis is the one Stacks 0BZE itself assumes, read for the lifted rings by
> `Dualizing.isPerfectModule_ulift_ringEquiv`.

```lean
theorem nonempty_derivedHom_iso_canonicalDerivedTensor_of_perfect_anyModuleUniverse (f : R →+* A)
    (hperf : letI := f.toAlgebra
      StacksDraft.Perfect.IsPerfectModule.{u, u, u + 1} (R := R) A)
    (L : CochainComplex (ModuleCat.{max v u} A) ℤ)
    (hL : Nonempty (DerivedCategory.Q.obj L ≅
      (Dualizing.derivedHom.{u, v} f).obj
        ((DerivedCategory.singleFunctor (ModuleCat.{max v u} R) 0).obj
          (ModuleCat.of R (ULift.{max v u} R))))) :
    Nonempty (Dualizing.derivedHom.{u, v} f ≅
      (canonicalDerivedTensorChangeOfRings.{u, u, max v u} f L).F)
```

**`Dualizing.nonempty_restrictScalars_derivedHom_iso_derivedTensor_unitDual`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TrivialDualityPerfectObjectwise.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/TrivialDualityPerfectObjectwise.lean#L107). The attribute's comment: “objectwise and after restriction of scalars to the base”.

> **Stacks 0BZE, objectwise and after restriction of scalars.** Let `f : R → A` be a
> homomorphism of commutative rings with `A` perfect as an `R`-module. For every object `K` of
> `D(R)`, derived coextension of scalars `R Hom(A, K)` of Stacks 0A70, read in `D(R)` by
> restriction of scalars along `f`, is the derived tensor product of `K` with `R Hom(A, R)` read in
> the same way.
>
> Perfectness is consumed, not recorded: it is the first case of the derived tensor--Hom diagonal
> of Stacks 0ATK, applied with the diagonal's internal-Hom source the module `A` placed in degree
> zero and read over `R`. The two vocabularies are reconciled by
> `Dualizing.nonempty_modelHomIsoRestrictScalarsDerivedHom`, which identifies the internal derived
> Hom of Stacks 0A63 out of that object with restricted derived coextension, and the tensor factor
> `K ⊗ᴸ_R R` is cut down by the right unitor of the derived tensor product.
>
> Stacks 0BZE asserts more: an isomorphism of functors `D(R) ⥤ D(A)`. Both of the missing steps —
> naturality of the comparison in `K`, and the identification of `Stacks0BZE.comparison` with the
> diagonal that would carry an isomorphism in `D(R)` up to `D(A)` — are discussed in this module's
> documentation. For the form of Stacks 0BZE that asserts the isomorphism of functors and carries
> those steps as hypotheses, see `Stacks0BZE.cardIso` of
> `StacksFrontier.RingTheory.Dualizing.TrivialDualityKFlat`; for the unconditional form, see
> `Dualizing.exists_derivedHom_iso_derivedTensor` of
> `StacksFrontier.RingTheory.Dualizing.DerivedHomPerfectTensor`.

```lean
theorem nonempty_restrictScalars_derivedHom_iso_derivedTensor_unitDual (f : R →+* A)
    (hperfect : letI := f.toAlgebra
      StacksDraft.Perfect.IsPerfectModule (R := R) A)
    (K : DerivedCategory (ModuleCat.{u} R)) :
    Nonempty
      ((ModuleCat.restrictScalars.{u} f).mapDerivedCategory.obj
          ((derivedHom.{u, u, u} f).obj K) ≅
        (Model.tensor R).obj
          (K, (ModuleCat.restrictScalars.{u} f).mapDerivedCategory.obj
            ((derivedHom.{u, u, u} f).obj
              (DerivedCategory.Q.obj
                ((CochainComplex.singleFunctor (ModuleCat.{u} R) 0).obj
                  (ModuleCat.of R R))))))
```

## Tag 0BZH, a lemma

[Tag 0BZH](https://stacks.math.columbia.edu/tag/0BZH) in the Stacks Project.

**`Dualizing.InvertibleKernel.conormal_invertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TrivialDualityInvertibleKernel.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/TrivialDualityInvertibleKernel.lean#L137). The attribute's comment: “the conormal module `I ⊗_R A` is an invertible `A`-module”.

> **The conormal module of a surjection with invertible kernel is invertible.** Invertibility
> is stable under base change, here along `R → A` itself.
>
> This is the clause of [Stacks, Tag 0BZH] that calls `I ⊗_R A` an invertible `A`-module. Unlike
> the functor identification it needs nothing beyond the two hypotheses of the tag, and it holds at
> every module universe.

```lean
theorem conormal_invertible (hI : Module.Invertible R (RingHom.ker (algebraMap R A))) :
    Module.Invertible A (conormal.{u, v} R A)
```

**`Dualizing.InvertibleKernel.conormalInverse_tensor_conormal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TrivialDualityInvertibleKernel.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/TrivialDualityInvertibleKernel.lean#L148). The attribute's comment: “`N` is the inverse of the invertible `A`-module `I ⊗_R A`”.

> **`N` is a tensor inverse of the conormal module**: `N ⊗_A (I ⊗_R A) ≅ A`.
>
> This is the clause of [Stacks, Tag 0BZH] that names `N` as the inverse of the invertible
> `A`-module `I ⊗_R A`; like `Dualizing.InvertibleKernel.conormal_invertible` it is unconditional
> and holds at every module universe.

```lean
def conormalInverse_tensor_conormal
    (hI : Module.Invertible R (RingHom.ker (algebraMap R A))) :
    conormalInverse.{u, v} R A ⊗[A] conormal.{u, v} R A ≃ₗ[A] A
```

**`Dualizing.InvertibleKernel.nonempty_derivedHom_iso_derivedTensor_conormalInverseShift_anyModuleUniverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TrivialDualityInvertibleKernelAnyModuleUniverse.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/TrivialDualityInvertibleKernelAnyModuleUniverse.lean#L52). The attribute's comment: “at an arbitrary module universe above the ring universe, with no carried hypothesis”.

> For a surjection `f : R → A` whose kernel is an invertible `R`-module, derived coextension of
> scalars `RHom_R(A, -) : D(R) ⥤ D(A)` is derived tensoring over `R` with the conormal inverse shift
> `N[-1]`, for any model of the derived change-of-rings tensor product with that factor and at any
> module universe above the ring universe.

```lean
theorem nonempty_derivedHom_iso_derivedTensor_conormalInverseShift_anyModuleUniverse
    (f : R →+* A) (hf : Function.Surjective f)
    (hI : Module.Invertible R (RingHom.ker f)) :
    letI := f.toAlgebra
    ∀ T : DerivedTensorChangeOfRings f (conormalInverseShift.{u, v} R A),
      Nonempty (Dualizing.derivedHom.{u, v} f ≅ T.F)
```

**`Dualizing.InvertibleKernel.nonempty_derivedHom_iso_derivedTensor_conormalInverseShift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/PolynomialEvalDualityProof.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/UpperShriek/PolynomialEvalDualityProof.lean#L103). The attribute's comment: “at module universe equal to the ring universe, with no carried hypothesis”.

> **Stacks 0BZH.** For a surjection `f : R → A` whose kernel is an invertible `R`-module,
> derived coextension of scalars `RHom_R(A, -) : D(R) ⥤ D(A)` is derived tensoring over `R` with
> the conormal inverse shift `N[-1]`, at any model of the derived change-of-rings tensor product
> with that factor.
>
> This is
> `Dualizing.InvertibleKernel.nonempty_derivedHom_iso_canonicalDerivedTensor_conormalInverseShift`
> transported to an arbitrary model along `Dualizing.InvertibleKernel.derivedTensorIsoOfDerivedIso`
> at the identity of the tensor factor.

```lean
theorem nonempty_derivedHom_iso_derivedTensor_conormalInverseShift (f : R →+* A)
    (hf : Function.Surjective f) (hI : Module.Invertible R (RingHom.ker f)) :
    letI := f.toAlgebra
    ∀ T : DerivedTensorChangeOfRings f (conormalInverseShift.{u, u} R A),
      Nonempty (Dualizing.derivedHom.{u, u} f ≅ T.F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 47.13, Tag 0A6Z](https://stacks.math.columbia.edu/tag/0A6Z)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
