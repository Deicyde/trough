---
declaration: section
origin: cited
lean: AlgebraicGeometry.SmallEtale.fShriekDerivedAdjunction, AlgebraicGeometry.SmallEtale.fShriekRUpperShriekAdjunction, AlgebraicGeometry.SmallEtale.moduleFShriekDerivedAdjunction, AlgebraicGeometry.SmallEtale.moduleFShriekRUpperShriekAdjunction, AlgebraicGeometry.SmallEtale.moduleTorsionSheafProperty_fShriekMod, AlgebraicGeometry.SmallEtale.moduleTorsionCohomologyProperty_moduleFShriekDerivedFunctor, AlgebraicGeometry.SmallEtale.moduleTorsionSheafProperty_fShriekMod_obj, AlgebraicGeometry.SmallEtale.moduleTorsionCohomologyProperty_moduleFShriekDerivedFunctor_fShriekMod
statement: formalized
proof: formalized
---

# 63.7 Derived upper shriek for locally quasi-finite morphisms

Section 63.7 of the Stacks Project, [Tag 0F5M](https://stacks.math.columbia.edu/tag/0F5M). 4 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0F5N, a lemma

[Tag 0F5N](https://stacks.math.columbia.edu/tag/0F5N) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.fShriekDerivedAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/DerivedUpperShriekAdjunction.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/DerivedUpperShriekAdjunction.lean#L178). The attribute's comment: “abelian coefficients, the case Λ = ℤ”. References: SGA 4 XVIII (3.1.5), “special case”.

> **Stacks 0F5N.** Let `f : X ⟶ Y` be a locally quasi-finite morphism. The direct image with
> compact support `f_!` of Stacks 0F6R, which is exact and therefore induces a functor
> `D(X_étale) ⥤ D(Y_étale)` on unbounded derived categories of abelian étale sheaves, is left
> adjoint to any total right derived functor `Rf^! : D(Y_étale) ⥤ D(X_étale)` of the upper shriek
> `f^!` of Stacks 0F59.

```lean
public def fShriekDerivedAdjunction
    (RfUpperShriek : DerivedCategory (AbelianSheaf.{u, v} B Y) ⥤
      DerivedCategory (AbelianSheaf.{u, v} B X))
    (β : (fUpperShriekFunctor.{u, v} B f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
        DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RfUpperShriek)
    [RfUpperShriek.IsRightDerivedFunctor β
      (HomotopyCategory.quasiIso (AbelianSheaf.{u, v} B Y) (ComplexShape.up ℤ))] :
    (fShriekFunctor.{u, v} B f).mapDerivedCategory ⊣ RfUpperShriek
```

**`AlgebraicGeometry.SmallEtale.fShriekRUpperShriekAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/DerivedUpperShriekAdjunction.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/DerivedUpperShriekAdjunction.lean#L192). The attribute's comment: “abelian coefficients, for the chosen total right derived functor of f^!”.

> **Stacks 0F5N** for the chosen total right derived functor: `f_!` on unbounded derived
> categories of abelian étale sheaves is left adjoint to `rUpperShriekFunctor`.

```lean
public def fShriekRUpperShriekAdjunction :
    (fShriekFunctor.{u, v} B f).mapDerivedCategory ⊣ rUpperShriekFunctor.{u, v, w} B f
```

**`AlgebraicGeometry.SmallEtale.moduleFShriekDerivedAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/DerivedUpperShriekAdjunction.lean, line 400](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/DerivedUpperShriekAdjunction.lean#L400). The attribute's comment: “general coefficient ring Λ, from a Λ-linear lift of f_!”.

> **Stacks 0F5N** for a general coefficient ring. Let `f : X ⟶ Y` be a locally quasi-finite
> morphism and let `fShriekMod` be a `Λ`-linear lift of the direct image with compact support
> `f_!` of Stacks 0F6R. The lift is then exact, so it induces a functor
> `D(X_étale, Λ) ⥤ D(Y_étale, Λ)`, it has a right adjoint `f^!`, and that functor is left adjoint
> to any total right derived functor `Rf^! : D(Y_étale, Λ) ⥤ D(X_étale, Λ)` of `f^!`.

```lean
public def moduleFShriekDerivedAdjunction (f : X ⟶ Y)
    [LocallyOfFiniteType (B.inclusion.map f)] [LocallyQuasiFinite (B.inclusion.map f)]
    (fShriekMod : ModuleSheaf.{u, v, r} B X Λ ⥤ ModuleSheaf.{u, v, r} B Y Λ)
    (hlift : fShriekMod ⋙ forgetModuleSheaf.{u, v, r} B Y Λ ≅
      forgetModuleSheaf.{u, v, r} B X Λ ⋙ fShriekFunctor.{u, max v r} B f)
    (RfUpperShriek : DerivedCategory (ModuleSheaf.{u, v, r} B Y Λ) ⥤
      DerivedCategory (ModuleSheaf.{u, v, r} B X Λ))
    (β : moduleUpperShriekQh.{u, v, w, r} B Λ f fShriekMod hlift ⟶
      DerivedCategory.Qh ⋙ RfUpperShriek)
    [RfUpperShriek.IsRightDerivedFunctor β
      (HomotopyCategory.quasiIso (ModuleSheaf.{u, v, r} B Y Λ) (ComplexShape.up ℤ))] :
    moduleFShriekDerivedFunctor.{u, v, w, r} B Λ f fShriekMod hlift ⊣ RfUpperShriek
```

**`AlgebraicGeometry.SmallEtale.moduleFShriekRUpperShriekAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekModuleAdjunction.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekModuleAdjunction.lean#L116). The attribute's comment: “general coefficient ring Λ, for f_! and f^! themselves”. References: SGA 4 XVIII (3.1.5), “special case”.

> **Stacks 0F5N.** Let `f : X ⟶ Y` be a locally quasi-finite morphism of schemes and let `Λ` be
> a ring. The direct image with compact support `f_!` of Stacks 0F6R and the upper shriek `f^!` of
> Stacks 0F59 induce adjoint functors `f_! : D(X_étale, Λ) ⟶ D(Y_étale, Λ)` and
> `Rf^! : D(Y_étale, Λ) ⟶ D(X_étale, Λ)` on unbounded derived categories of étale sheaves of
> `Λ`-modules.
>
> The functor `f_!` with coefficients in `Λ` is `AlgebraicGeometry.SmallEtale.fShriekMod`; it is
> exact and therefore needs no deriving, and `Rf^!` is the total right derived functor of the `f^!`
> of Stacks 0F59 part (3).

```lean
public def moduleFShriekRUpperShriekAdjunction :
    moduleFShriekDerivedFunctor.{u, v, w, r} B Λ f (fShriekMod.{u, v, r} B Λ f)
        (fShriekModForgetIso.{u, v, r} B Λ f) ⊣
      moduleRUpperShriekFunctor.{u, v, w, r} B Λ f
```

## Tag 0GJX, a remark

[Tag 0GJX](https://stacks.math.columbia.edu/tag/0GJX) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.moduleTorsionSheafProperty_fShriekMod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekDerivedTorsion.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekDerivedTorsion.lean#L111). The attribute's comment: “the sheaf-level reduction: a `Λ`-linear lift of `f_!` preserves torsion”.

> A `Λ`-linear lift of the direct image with compact support sends torsion étale sheaves of
> `Λ`-modules to torsion étale sheaves of `Λ`-modules: the lift is identified with `f_!` on
> underlying abelian sheaves, and `f_!` preserves torsion there.

```lean
public theorem moduleTorsionSheafProperty_fShriekMod
    (fShriekMod : ModuleSheaf.{u, v, r} B X Λ ⥤ ModuleSheaf.{u, v, r} B Y Λ)
    (hlift : fShriekMod ⋙ forgetModuleSheaf.{u, v, r} B Y Λ ≅
      forgetModuleSheaf.{u, v, r} B X Λ ⋙ fShriekFunctor.{u, max v r} B f)
    (F : ModuleSheaf.{u, v, r} B X Λ)
    (hF : moduleTorsionSheafProperty.{u, v, r} B X Λ F) :
    moduleTorsionSheafProperty.{u, v, r} B Y Λ (fShriekMod.obj F)
```

**`AlgebraicGeometry.SmallEtale.moduleTorsionCohomologyProperty_moduleFShriekDerivedFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekDerivedTorsion.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekDerivedTorsion.lean#L152). The attribute's comment: “general coefficient ring `Λ`: for a `Λ`-linear lift of `f_!`, the functor `f_! : D(X_étale, Λ) ⥤ D(Y_étale, Λ)` of Tag 0F5N sends complexes with torsion cohomology sheaves to complexes with torsion cohomology sheaves”.

> **Stacks 0GJX.** Let `f : X ⟶ Y` be a locally quasi-finite morphism of schemes and let `Λ` be
> a ring. The functor `f_! : D(X_étale, Λ) ⥤ D(Y_étale, Λ)` of Stacks 0F5N sends a complex with
> torsion cohomology sheaves to a complex with torsion cohomology sheaves.
>
> The `Λ`-linear lift of `f_!` is exact, so the cohomology of `f_! K` is `f_!` of the cohomology of
> `K`; torsion of a sheaf of `Λ`-modules is torsion of its underlying abelian sheaf, which `hlift`
> identifies with the image under `f_!` of the underlying abelian sheaf; and `f_!` preserves torsion
> abelian sheaves, which Stacks 0GJX reads off the stalk description of `f_!` in Stacks 0F5F.

```lean
public theorem moduleTorsionCohomologyProperty_moduleFShriekDerivedFunctor
    (fShriekMod : ModuleSheaf.{u, v, r} B X Λ ⥤ ModuleSheaf.{u, v, r} B Y Λ)
    (hlift : fShriekMod ⋙ forgetModuleSheaf.{u, v, r} B Y Λ ≅
      forgetModuleSheaf.{u, v, r} B X Λ ⋙ fShriekFunctor.{u, max v r} B f)
    (K : DerivedCategory (ModuleSheaf.{u, v, r} B X Λ))
    (hK : moduleTorsionCohomologyProperty.{u, v, w, r} B X Λ K) :
    moduleTorsionCohomologyProperty.{u, v, w, r} B Y Λ
      ((moduleFShriekDerivedFunctor.{u, v, w, r} B Λ f fShriekMod hlift).obj K)
```

**`AlgebraicGeometry.SmallEtale.moduleTorsionSheafProperty_fShriekMod_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekDerivedTorsionModule.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekDerivedTorsionModule.lean#L70). The attribute's comment: “the sheaf-level input, for f_! with coefficients in Λ itself”.

> The direct image with compact support with coefficients in a ring `Λ` sends torsion étale
> sheaves of `Λ`-modules to torsion étale sheaves of `Λ`-modules: on underlying abelian sheaves it
> is `f_!`, which preserves torsion by the stalk description of Stacks 0F5F.

```lean
public theorem moduleTorsionSheafProperty_fShriekMod_obj (F : ModuleSheaf.{u, v, r} B X Λ)
    (hF : moduleTorsionSheafProperty.{u, v, r} B X Λ F) :
    moduleTorsionSheafProperty.{u, v, r} B Y Λ ((fShriekMod.{u, v, r} B Λ f).obj F)
```

**`AlgebraicGeometry.SmallEtale.moduleTorsionCohomologyProperty_moduleFShriekDerivedFunctor_fShriekMod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekDerivedTorsionModule.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekDerivedTorsionModule.lean#L90). The attribute's comment: “f_! on D(X_étale, Λ) ⟶ D(Y_étale, Λ) sends complexes with torsion cohomology sheaves to complexes with torsion cohomology sheaves”.

> **Stacks 0GJX.** Let `f : X ⟶ Y` be a locally quasi-finite morphism of schemes and let `Λ` be
> a ring. The functor `f_! : D(X_étale, Λ) ⟶ D(Y_étale, Λ)` of Stacks 0F5N sends complexes with
> torsion cohomology sheaves to complexes with torsion cohomology sheaves.
>
> The functor `f_!` with coefficients in `Λ` is exact, so the cohomology of `f_! K` is `f_!` of the
> cohomology of `K`; torsion of a sheaf of `Λ`-modules is torsion of its underlying abelian sheaf,
> which is the image under `f_!` of the underlying abelian sheaf of the cohomology; and `f_!`
> preserves torsion abelian sheaves, which the source reads off the stalk description of `f_!` in
> Stacks 0F5F.

```lean
public theorem moduleTorsionCohomologyProperty_moduleFShriekDerivedFunctor_fShriekMod
    (K : DerivedCategory (ModuleSheaf.{u, v, r} B X Λ))
    (hK : moduleTorsionCohomologyProperty.{u, v, w, r} B X Λ K) :
    moduleTorsionCohomologyProperty.{u, v, w, r} B Y Λ
      ((moduleFShriekDerivedFunctor.{u, v, w, r} B Λ f (fShriekMod.{u, v, r} B Λ f)
        (fShriekModForgetIso.{u, v, r} B Λ f)).obj K)
```

**`AlgebraicGeometry.SmallEtale.exists_nsmul_eq_zero_etaleStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekTorsion.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekTorsion.lean#L82). The attribute's comment: “an input to the proof: the stalk of a torsion abelian étale sheaf at a geometric point is a torsion abelian group”.

> The stalk of a torsion abelian étale sheaf at a geometric point is a torsion abelian group.

```lean
public theorem exists_nsmul_eq_zero_etaleStalk (t : GeometricPoint S)
    (F : Sheaf (SmallEtale.topology B S hS) AddCommGrpCat.{max (u + 1) v})
    (hF : torsionSheafProperty (SmallEtale.topology B S hS) F)
    (g : ↑(etaleStalk B S hS t F.obj)) :
    ∃ n : ℕ, 0 < n ∧ n • g = 0
```

**`AlgebraicGeometry.SmallEtale.torsionSheafProperty_of_forall_etaleStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekTorsion.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekTorsion.lean#L100). The attribute's comment: “the stalk criterion used by the proof: an abelian étale sheaf whose stalks at all geometric points are torsion is a torsion abelian sheaf”.

> An abelian étale sheaf whose stalks at all geometric points are torsion abelian groups is a
> torsion abelian sheaf.

```lean
public theorem torsionSheafProperty_of_forall_etaleStalk
    (F : Sheaf (SmallEtale.topology B S hS) AddCommGrpCat.{max (u + 1) v})
    (hF : ∀ (t : GeometricPoint S) (g : ↑(etaleStalk B S hS t F.obj)),
      ∃ n : ℕ, 0 < n ∧ n • g = 0) :
    torsionSheafProperty (SmallEtale.topology B S hS) F
```

**`AlgebraicGeometry.SmallEtale.torsionSheafProperty_fShriekFunctor_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekTorsion.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekTorsion.lean#L134). The attribute's comment: “the abelian-sheaf case: `f_!` of a locally quasi-finite morphism sends a torsion abelian sheaf to a torsion abelian sheaf. The statement for a general coefficient ring is `AlgebraicGeometry.SmallEtale.moduleTorsionCohomologyProperty_moduleFShriekDerivedFunctor`”.

> The direct image with compact support `f_!` of a locally quasi-finite morphism sends a torsion
> abelian sheaf on the small étale site of `X` to a torsion abelian sheaf on the small étale site of
> `Y`.

```lean
public theorem torsionSheafProperty_fShriekFunctor_obj (F : AbelianSheaf.{u, v} B X)
    (hF : torsionSheafProperty (SmallEtale.topology B X.obj X.property) F) :
    torsionSheafProperty (SmallEtale.topology B Y.obj Y.property)
      ((fShriekFunctor.{u, v} B f).obj F)
```

## Tag 0GKK, a lemma

[Tag 0GKK](https://stacks.math.columbia.edu/tag/0GKK) in the Stacks Project.

**`Stacks.EtaleCohomology.exists_distTriang_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/CoverTriangle.lean, line 447](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/CoverTriangle.lean#L447). The attribute's comment: “abelian coefficients; first map carries the Mayer-Vietoris sign”.

> **Stacks Project, Tag 0GKK, for abelian coefficients.**  Let `X` be a scheme with
> `X = U ∪ V` for open subschemes `U` and `V`.  For every object `K` of the derived category of
> abelian sheaves on the small étale site of `X` there is a distinguished triangle
> `j_{U ∩ V!} K|_{U ∩ V} ⟶ j_{U!} K|_U ⊕ j_{V!} K|_V ⟶ K ⟶ (j_{U ∩ V!} K|_{U ∩ V})[1]`,
> the first arrow being `(ι, -ι)` and the second the pair of counits of `j_! ⊣ j^{-1}`, both
> induced on the derived category by exactness of the functors involved.
>
> Correction to the source: the displayed sequence is exact only with the Mayer--Vietoris sign on
> one of the two components of the first arrow, which is carried here.  The source states the
> triangle for sheaves of `Λ`-modules over an arbitrary ring `Λ`; this is the case `Λ = ℤ`, and
> the general case is `Stacks.EtaleCohomology.exists_distTriang_etaleModuleCover`.

```lean
theorem exists_distTriang_cover
    [HasDerivedCategory.{w} (Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v})]
    (K : DerivedCategory (Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v})) :
    ∃ δ : K ⟶
        ((extensionByZeroOfRestriction.{u, v} (U ⊓ V).ι).mapDerivedCategory.obj K)⟦(1 : ℤ)⟧,
      Triangle.mk
        ((derivedNatTrans (extensionByZeroOfRestriction.{u, v} (U ⊓ V).ι)
          (coverBiprod.{u, v} U V) (coverToBiprod.{u, v} U V)).app K)
        (((coverBiprod.{u, v} U V).mapDerivedCategoryTransToId
          (coverFromBiprod.{u, v} U V)).app K) δ ∈
        distTriang (DerivedCategory
          (Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}))
```

**`Stacks.EtaleCohomology.exists_distTriang_etaleModuleCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/CoverTriangleModules.lean, line 517](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/CoverTriangleModules.lean#L517). The attribute's comment: “first map carries the Mayer-Vietoris sign”.

> **Stacks Project, Tag 0GKK.**  Let `Λ` be a ring and let `X` be a scheme with `X = U ∪ V`
> for open subschemes `U` and `V`.  For every object `K` of the derived category of sheaves of
> `Λ`-modules on the small étale site of `X` there is a distinguished triangle
> `j_{U ∩ V!} K|_{U ∩ V} ⟶ j_{U!} K|_U ⊕ j_{V!} K|_V ⟶ K ⟶ (j_{U ∩ V!} K|_{U ∩ V})[1]`,
> the first arrow being `(ι, -ι)` and the second the pair of counits of `j_! ⊣ j^{-1}`, both
> induced on the derived category by exactness of the functors involved.
>
> Correction to the source: the displayed sequence is exact only with the Mayer--Vietoris sign on
> one of the two components of the first arrow, which is carried here.

```lean
theorem exists_distTriang_etaleModuleCover
    [HasDerivedCategory.{w} (EtaleModules.{u, r} Λ X)]
    (K : DerivedCategory (EtaleModules.{u, r} Λ X)) :
    ∃ δ : K ⟶ ((etaleModuleExtensionByZeroOfRestriction.{u, r} Λ
        (U ⊓ V).ι).mapDerivedCategory.obj K)⟦(1 : ℤ)⟧,
      Triangle.mk
        ((derivedNatTrans
          (etaleModuleExtensionByZeroOfRestriction.{u, r} Λ (U ⊓ V).ι)
          (etaleModuleCoverBiprod.{u, r} Λ U V)
          (etaleModuleCoverToBiprod.{u, r} Λ U V)).app K)
        (((etaleModuleCoverBiprod.{u, r} Λ U V).mapDerivedCategoryTransToId
          (etaleModuleCoverFromBiprod.{u, r} Λ U V)).app K) δ ∈
        distTriang (DerivedCategory (EtaleModules.{u, r} Λ X))
```

## Tag 0GKL, a lemma

[Tag 0GKL](https://stacks.math.columbia.edu/tag/0GKL) in the Stacks Project.

**`Stacks.EtaleCohomology.exists_distTriang_extensionByZero_etaleAbelianDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/DerivedOpenClosedTriangle.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/DerivedOpenClosedTriangle.lean#L191). The attribute's comment: “abelian coefficients”.

> **Stacks Project, Tag 0GKL, for abelian coefficients.**  Let `X` be a scheme, let
> `i : Z ⟶ X` be a closed immersion and let `j : U ⟶ X` be an open immersion whose image is the
> complement of the image of `i`.  For every object `K` of the derived category of abelian sheaves
> on the small étale site of `X` there is a distinguished triangle
> `j_! j^{-1} K ⟶ K ⟶ i_* i^{-1} K ⟶ (j_! j^{-1} K)[1]`,
> whose first arrow is the counit of `j_! ⊣ j^{-1}` and whose second arrow is the unit of
> `i^{-1} ⊣ i_*`, both induced on the derived category by exactness of the four functors
> involved.
>
> The source states the triangle for sheaves of `Λ`-modules over an arbitrary ring `Λ`; this is the
> case `Λ = ℤ`, the general case being
> `Stacks.EtaleCohomology.exists_distTriang_etaleModuleExtensionByZero_directImage`.

```lean
theorem exists_distTriang_extensionByZero_etaleAbelianDirectImage {Z U X : Scheme.{u}}
    (i : Z ⟶ X) [IsClosedImmersion i] (j : U ⟶ X) [IsOpenImmersion j]
    (hij : Set.range j.base = (Set.range i.base)ᶜ)
    [HasDerivedCategory.{w} (Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v})]
    (K : DerivedCategory (Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v})) :
    ∃ δ : (etaleAbelianDirectImageOfInverseImage.{u, v} i).mapDerivedCategory.obj K ⟶
        ((extensionByZeroOfRestriction.{u, v} j).mapDerivedCategory.obj K)⟦(1 : ℤ)⟧,
      Triangle.mk
        (((extensionByZeroOfRestriction.{u, v} j).mapDerivedCategoryTransToId
          (extensionByZeroAdj.{u, v} j).counit).app K)
        (((etaleAbelianDirectImageOfInverseImage.{u, v} i).mapDerivedCategoryTransFromId
          (etaleAbelianInverseImageDirectImageAdj.{u, v} i).unit).app K) δ ∈
        distTriang (DerivedCategory
          (Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}))
```

**`Stacks.EtaleCohomology.exists_distTriang_etaleModuleExtensionByZero_directImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/ModuleOpenClosedTriangle.lean, line 386](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ExtensionByZero/ModuleOpenClosedTriangle.lean#L386).

> **Stacks Project, Tag 0GKL.**  Let `X` be a scheme, let `i : Z ⟶ X` be a closed immersion and
> let `j : U ⟶ X` be an open immersion whose image is the complement of the image of `i`, and let
> `Λ` be a ring.  For every object `K` of the derived category `D(X_étale, Λ)` of sheaves of
> `Λ`-modules on the small étale site of `X` there is a distinguished triangle
> `j_! j^{-1} K ⟶ K ⟶ i_* i^{-1} K ⟶ (j_! j^{-1} K)[1]`,
> whose first arrow is the counit of `j_! ⊣ j^{-1}` and whose second arrow is the unit of
> `i^{-1} ⊣ i_*`, both induced on the derived category by exactness of the four functors
> involved.

```lean
theorem exists_distTriang_etaleModuleExtensionByZero_directImage (Λ : Type r) [Ring Λ]
    {Z U X : Scheme.{u}} (i : Z ⟶ X) [IsClosedImmersion i] (j : U ⟶ X) [IsOpenImmersion j]
    (hij : Set.range j.base = (Set.range i.base)ᶜ)
    [HasDerivedCategory.{w} (EtaleModules.{u, r} Λ X)]
    (K : DerivedCategory (EtaleModules.{u, r} Λ X)) :
    ∃ δ : (etaleModuleDirectImageOfInverseImage.{u, r} Λ i).mapDerivedCategory.obj K ⟶
        ((etaleModuleExtensionByZeroOfRestriction.{u, r} Λ j).mapDerivedCategory.obj K)⟦(1 : ℤ)⟧,
      Triangle.mk
        (((etaleModuleExtensionByZeroOfRestriction.{u, r} Λ j).mapDerivedCategoryTransToId
          (etaleModuleExtensionByZeroAdj.{u, r} Λ j).counit).app K)
        (((etaleModuleDirectImageOfInverseImage.{u, r} Λ i).mapDerivedCategoryTransFromId
          (etaleModuleInverseImageAdj.{u, r} Λ i).unit).app K) δ ∈
        distTriang (DerivedCategory (EtaleModules.{u, r} Λ X))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 63.7, Tag 0F5M](https://stacks.math.columbia.edu/tag/0F5M)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
