---
declaration: section
origin: cited
lean: SheafOfModules.IsQuasicoherent, SheafOfModules.isQuasicoherent, directSum_isQuasicoherent, AlgebraicGeometry.SheafOfModules.modulePullback_isQuasicoherent, Stacks.AssociatedSheaf.associatedSheafAdjunction, Stacks.AssociatedSheaf.pullbackAssociatedSheafIso, Stacks.AssociatedSheaf.pullbackAssociatedSheafIso_hom_app_apply, Stacks.AssociatedSheaf.presentationSheafIso
statement: formalized
proof: formalized
---

# 17.10 Quasi-coherent modules

Section 17.10 of the Stacks Project, [Tag 01BD](https://stacks.math.columbia.edu/tag/01BD). 8 tags here are carried by 17 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01BE, a definition

[Tag 01BE](https://stacks.math.columbia.edu/tag/01BE) in the Stacks Project.

Declarations registered for the tag:

- [`SheafOfModules.IsQuasicoherent`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.IsQuasicoherent#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch17.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch17.lean#L53) (StacksFrontier): “quasi-coherent sheaf of modules”. References: EGA 0 (5.1.3); SGA 4 XVII (5.5.29), “partial”; SGA 6 0 (2.5); SGA 6 II (2.2.1).
- [`SheafOfModules.isQuasicoherent`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.isQuasicoherent#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch17.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch17.lean#L54) (StacksFrontier): “the category QCoh(O\_X)”. References: EGA 0 (5.1.3); SGA 4 Vbis (4.2.0), “Fiber G\_X”; SGA 4 XVII (5.5.29), “partial”; SGA 6 0 (2.5); SGA 6 II (2.2.1).

## Tag 01BF, a lemma

[Tag 01BF](https://stacks.math.columbia.edu/tag/01BF) in the Stacks Project.

**`directSum_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/QuasicoherentDirectSum.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/QuasicoherentDirectSum.lean#L78). References: EGA 0 (5.1.3), “direct sum remark”; EGA I (4.1.1), “direct sums (binary)”.

> Stacks Tag 01BF (Lemma 17.10.2): the direct sum of two quasi-coherent
> `O_X`-modules on a ringed space is quasi-coherent.

```lean
theorem directSum_isQuasicoherent
    (X : AlgebraicGeometry.RingedSpace)
    (M N : SheafOfModules (ringCatSheaf X))
    (hM : M.IsQuasicoherent) (hN : N.IsQuasicoherent) :
    (M ⊞ N).IsQuasicoherent
```

## Tag 01BG, a lemma

[Tag 01BG](https://stacks.math.columbia.edu/tag/01BG) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.modulePullback_isQuasicoherent`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/Quasicoherent.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/Quasicoherent.lean#L58).

> **Stacks 01BG.** The pullback of a quasi-coherent sheaf of modules along a
> morphism of ringed spaces is quasi-coherent.

```lean
lemma modulePullback_isQuasicoherent {X Y : RingedSpace.{u, u}} (f : X ⟶ Y)
    (G : _root_.SheafOfModules.{u} (structureSheafRing Y)) [G.IsQuasicoherent] :
    ((modulePullback f).obj G).IsQuasicoherent
```

## Tag 01BH, a lemma

[Tag 01BH](https://stacks.math.columbia.edu/tag/01BH) in the Stacks Project.

**`Stacks.AssociatedSheaf.associatedSheafAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/AssociatedSheafComparison.lean, line 392](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/AssociatedSheafComparison.lean#L392). The attribute's comment: “Mor(ℱ\_M, 𝒢) = Hom\_R(M, Γ(X,𝒢))”.

> The tensor-sheafification adjunction: `associatedSheafFunctor` is left adjoint to global
> sections with scalars restricted along `α`, so that `Mor_{𝒪_X}(ℱ_M, 𝒢) = Hom_R(M, Γ(X, 𝒢))`.

```lean
def associatedSheafAdjunction :
    associatedSheafFunctor.{u, max u v} X α ⊣ globalSectionsFunctor.{u, v} X α
```

**`Stacks.AssociatedSheaf.pullbackAssociatedSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/AssociatedSheafIsos.lean, line 515](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/AssociatedSheafIsos.lean#L515). The attribute's comment: “comparison\_of\_three\_constructions”.

> Pullback along `π : X ⟶ ({*}, R)` of `M` regarded as a sheaf of modules on the coefficient
> point is construction (3), naturally in `M`, with the module universe independent of the
> universe of `X` and `R`.

```lean
def pullbackAssociatedSheafIso :
    coefficientPointModuleFunctor.{u, v} (R := R) ⋙ coefficientPointPullback.{u, v} X α ≅
      associatedSheafFunctor.{u, v} X α
```

**`Stacks.AssociatedSheaf.pullbackAssociatedSheafIso_hom_app_apply`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/AssociatedSheafIsos.lean, line 528](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/AssociatedSheafIsos.lean#L528). The attribute's comment: “comparison\_of\_three\_constructions”.

> The comparison `pullbackAssociatedSheafIso` carries the image of `1 ⊗ m` under the unit of
> `π^* ⊣ π_*` to `1 ⊗ m`.

```lean
lemma pullbackAssociatedSheafIso_hom_app_apply (M : ModuleCat.{v} R) (m : M) :
    PresheafOfModules.Hom.app ((pullbackAssociatedSheafIso.{u, v} X α).hom.app M).val (op ⊤)
        (PresheafOfModules.Hom.app ((coefficientPointAdjunction.{u, v} X α).unit.app
          ((coefficientPointModuleFunctor.{u, v} (R := R)).obj M)).val (op ⊤)
          (tensorUnitSection (coefficientPoint (CommRingCat.of R)) (pointRing (R := R))
            M (op ⊤) m)) =
      tensorUnitSection X α M (op ⊤) m
```

**`Stacks.AssociatedSheaf.presentationSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PresentationSheafIso.lean, line 735](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PresentationSheafIso.lean#L735). The attribute's comment: “comparison\_of\_three\_constructions”.

> **Stacks 01BH, (2) = (3).** The cokernel of the relation matrix of a presentation of `M`
> over the structure sheaf of `X` is the sheafification of `U ↦ 𝒪_X(U) ⊗_R M`, with the sections
> lifted to the common universe of the module, the generators and the relations.

```lean
def presentationSheafIso :
    presentationSheaf X α P ≅
      SheafOfModules.uliftObj.{_, _, _, _, max w z} (associatedSheaf X α M)
```

**`Stacks.AssociatedSheaf.presentationSheafIso_hom_app_apply`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PresentationSheafIso.lean, line 763](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PresentationSheafIso.lean#L763). The attribute's comment: “comparison\_of\_three\_constructions”.

> **Stacks 01BH, the comparison of (2) and (3) is pinned down.** On every open it carries the
> image of the `i`-th generator to the image of `1 ⊗ (generator i)`.

```lean
lemma presentationSheafIso_hom_app_apply (i : P.G) (U : Opens X.carrier) :
    PresheafOfModules.Hom.app (presentationSheafIso X α M P).hom.val (op U)
        (PresheafOfModules.Hom.app (presentationGenerator X α P i).val (op U)
          (ULift.up (1 : X.presheaf.obj (op U)))) =
      ULift.up (tensorUnitSection X α M (op U)
        (P.toSolution.π (Finsupp.single i 1)))
```

**`Stacks.AssociatedSheaf.preservesColimitsOfSize_associatedSheafFunctor`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/AssociatedSheaf/Free.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/AssociatedSheaf/Free.lean#L209). The attribute's comment: “the functor M ↦ ℱ\_M commutes with arbitrary colimits”.

> The functor `M ↦ ℱ_M`, sending an `R`-module to the associated sheaf of `𝒪_X`-modules,
> commutes with arbitrary colimits.

```lean
instance preservesColimitsOfSize_associatedSheafFunctor :
    PreservesColimitsOfSize.{w, w} (associatedSheafFunctor.{u, max u v} X α)
```

**`Stacks.AssociatedSheaf.isQuasicoherent_associatedSheafFunctor_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/AssociatedSheaf/Quasicoherent.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/AssociatedSheaf/Quasicoherent.lean#L53). The attribute's comment: “ℱ\_M is quasi-coherent”.

> **Stacks 01BH and 01BE.** The sheaf of `𝒪_X`-modules associated to an `R`-module along a
> ring homomorphism `R ⟶ Γ(X, 𝒪_X)` is quasi-coherent, with no hypothesis on the module: the
> tautological presentation of the module gives a presentation of the associated sheaf.

```lean
theorem isQuasicoherent_associatedSheafFunctor_obj (X : RingedSpace.{u, u}) {R : Type u}
    [CommRing R] (α : R →+* X.presheaf.obj (op ⊤)) (M : ModuleCat.{u} R) :
    ((associatedSheafFunctor.{u, u} X α).obj M).IsQuasicoherent
```

**`Stacks.AssociatedSheaf.quasicoherentAssociatedSheafFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/AssociatedSheaf/Quasicoherent.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/AssociatedSheaf/Quasicoherent.lean#L66). The attribute's comment: “a functor from R-modules to quasi-coherent sheaves on X”.

> **Stacks 01BH, clause (2): the construction is a functor into quasi-coherent sheaves.**
> Construction (3) lifts through the full subcategory of quasi-coherent sheaves of `𝒪_X`-modules,
> by `Stacks.AssociatedSheaf.isQuasicoherent_associatedSheafFunctor_obj`. The colimit-preservation
> half of the clause is
> `Stacks.AssociatedSheaf.preservesColimitsOfSize_associatedSheafFunctor`.

```lean
noncomputable def quasicoherentAssociatedSheafFunctor : ModuleCat.{u} R ⥤
    (SheafOfModules.isQuasicoherent
      (structureSheafRing X)).FullSubcategory
```

**`Stacks.AssociatedSheaf.associatedSheafStalkLinearEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/AssociatedSheaf/StalkLinear.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/AssociatedSheaf/StalkLinear.lean#L163). The attribute's comment: “the stalk of ℱ\_M is 𝒪\_\{X,x} ⊗\_R M”.

> **`(ℱ_M)_x = 𝒪_{X,x} ⊗_A M` as `𝒪_{X,x}`-modules.**  The stalk at a point `x` of the sheaf of
> `𝒪_X`-modules associated to an `A`-module `M` and a ring map `α : A → Γ(X, 𝒪_X)` is the base
> change of `M` to the stalk of the structure sheaf, linearly over that stalk.

```lean
def associatedSheafStalkLinearEquiv :
    letI := stalkAlgebra X α x
    ToType (TopCat.Presheaf.stalk (C := AddCommGrpCat.{u})
        ((associatedSheafValFunctor X α).obj M).presheaf x) ≃ₗ[X.presheaf.stalk x]
      (X.presheaf.stalk x ⊗[A] M)
```

**`Stacks.AssociatedSheaf.associatedSheafStalkFunctorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/AssociatedSheaf/StalkLinear.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/AssociatedSheaf/StalkLinear.lean#L266). The attribute's comment: “the stalk of ℱ\_M is 𝒪\_\{X,x} ⊗\_R M, functorially in M”.

> **`(ℱ_M)_x = 𝒪_{X,x} ⊗_A M`, naturally in `M`.**  The identification
> `(ℱ_M)_x = 𝒪_{X,x} ⊗_A M` is a natural isomorphism of functors `ModuleCat A ⥤ ModuleCat 𝒪_{X,x}`;
> its components are `Stacks.AssociatedSheaf.associatedSheafStalkLinearEquiv`.

```lean
def associatedSheafStalkFunctorIso :
    stalkBaseChangeFunctor X α x ≅ associatedSheafStalkFunctor X α x
```

**`Stacks.AssociatedSheaf.associatedSheafUnitIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/AssociatedSheaf/Tensor.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/AssociatedSheaf/Tensor.lean#L160). The attribute's comment: “construction (3) at the base ring is the structure sheaf”.

> **Construction (3) carries the base ring to the structure sheaf:** `ℱ_R ≅ 𝒪_X`.
>
> Both legs are already in the repository: `Stacks.AssociatedSheaf.freeIsoAssociatedSheaf`
> identifies `ℱ` of a free module with the free sheaf of modules on the same index type, and
> `Stacks.SheafOfModules.Site.freePUnitIso` identifies the free sheaf of modules on a one-element
> index type with the structure sheaf. What is interposed is only the `R`-module isomorphism
> `(PUnit →₀ R) ≃ₗ[R] R`.

```lean
def associatedSheafUnitIso :
    associatedSheaf X α (ModuleCat.of R R) ≅
      SheafOfModules.unit (structureSheafRing X)
```

Declarations registered for the tag:

- [`Stacks.AssociatedSheaf.associatedSheaf`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/AssociatedSheafComparison.lean#L307), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/AssociatedSheafTerminology.lean, line 28](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/AssociatedSheafTerminology.lean#L28) (StacksFrontier): “associated\_sheaf\_construction”.

## Tag 01BI, a definition

[Tag 01BI](https://stacks.math.columbia.edu/tag/01BI) in the Stacks Project.

Declarations registered for the tag:

- [`Stacks.AssociatedSheaf.associatedSheaf`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/AssociatedSheafComparison.lean#L307), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/AssociatedSheafTerminology.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/AssociatedSheafTerminology.lean#L56) (StacksFrontier).

## Tag 01BJ, a lemma

[Tag 01BJ](https://stacks.math.columbia.edu/tag/01BJ) in the Stacks Project.

**`Stacks.AssociatedSheaf.ringedSpacePullbackAssociatedSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/AssociatedSheaf/Pullback.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/AssociatedSheaf/Pullback.lean#L124).

> **Stacks 01BJ.** The pullback of the sheaf associated to a module is the sheaf associated to
> the module obtained by extension of scalars along the map on global sections.
>
> The name says `ringedSpace` because `Stacks.AssociatedSheaf.pullbackAssociatedSheafIso` of
> `StacksFrontier.Algebra.Category.ModuleCat.Sheaf.AssociatedSheafIsos` is a different
> comparison, between the coefficient-point pullback and the associated-sheaf functor.

```lean
def ringedSpacePullbackAssociatedSheafIso {X Y : RingedSpace.{u, u}} (g : Y ⟶ X) :
    associatedSheafFunctor.{u, u} X (RingHom.id (X.presheaf.obj (op ⊤))) ⋙
        RingedSpaceModuleAdjunction.modulePullback g ≅
      ModuleCat.extendScalars (SheafedSpace.Γ.map g.op).hom ⋙
        associatedSheafFunctor.{u, u} Y (RingHom.id (Y.presheaf.obj (op ⊤)))
```

## Tag 01BK, a lemma

[Tag 01BK](https://stacks.math.columbia.edu/tag/01BK) in the Stacks Project.

**`Stacks.AssociatedSheaf.exists_open_associatedSheaf_iso`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/AssociatedSheaf/QuasicoherentNearPoint.lean, line 451](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/AssociatedSheaf/QuasicoherentNearPoint.lean#L451).

> **Stacks 01BK.** A quasi-coherent sheaf of modules is locally associated to a
> module over the ring of sections near a point with a basis of quasi-compact
> neighborhoods.

```lean
public lemma exists_open_associatedSheaf_iso (X : RingedSpace.{u, u}) (x : X)
    (hx : ∀ V : Set X, V ∈ 𝓝 x →
      ∃ K : Set X, IsCompact K ∧ K ∈ 𝓝 x ∧ K ⊆ V)
    (F : SheafOfModules.{u} (structureSheafRing X)) [F.IsQuasicoherent] :
    ∃ U : Opens X, x ∈ U ∧
      ∃ M : ModuleCat.{u} ((X.restrict U.isOpenEmbedding).presheaf.obj (op ⊤)),
        Nonempty (((modulePullback (X.ofRestrict U.isOpenEmbedding)).obj F) ≅
          associatedSheaf (X.restrict U.isOpenEmbedding)
            (RingHom.id ((X.restrict U.isOpenEmbedding).presheaf.obj (op ⊤))) M)
```

## Tag 01BL, an example

[Tag 01BL](https://stacks.math.columbia.edu/tag/01BL) in the Stacks Project.

**`Stacks.AssociatedSheaf.exists_free_iso_associatedSheaf_freeModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FreeAssociatedSheafBasis.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FreeAssociatedSheafBasis.lean#L62). The attribute's comment: “associated free-module sheaves”.

> **Stacks 01BL, first half.** The free sheaf of `𝒪_X`-modules on `I` is isomorphic to the sheaf
> associated to the free `Γ(X, 𝒪_X)`-module on `I`, by an isomorphism carrying the `i`-th basis
> section to the image of `Finsupp.single i 1` under the unit of the tensor-sheafification
> adjunction.

```lean
theorem exists_free_iso_associatedSheaf_freeModule (X : RingedSpace.{u, u}) (I : Type u) :
    ∃ s : SheafOfModules.free (R := structureSheafRing X) I ≅
        associatedSheaf X (RingHom.id (X.presheaf.obj (op ⊤)))
          (ModuleCat.of (X.presheaf.obj (op ⊤))
            (I →₀ X.presheaf.obj (op ⊤))),
      ∀ i : I, s.hom.val.app (op ⊤) (basisSection X ⊤ i) =
        ((associatedSheafAdjunction.{u, u} X
          (RingHom.id (X.presheaf.obj (op ⊤)))).unit.app
          (ModuleCat.of (X.presheaf.obj (op ⊤))
            (I →₀ X.presheaf.obj (op ⊤)))) (Finsupp.single i 1)
```

**`Stacks.Bouquet.exists_freeSheafMorphism_not_locally_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/FreeMorphismNotMatrix.lean, line 454](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/FreeMorphismNotMatrix.lean#L454). The attribute's comment: “non-module-induced morphism”.

> The countable bouquet carries a morphism of sheaves associated to free
> modules that does not locally come from a homomorphism of the free modules:
> its value on a basis section is never a finite target-basis combination on
> any neighborhood of the common origin.

```lean
public theorem exists_freeSheafMorphism_not_locally_finite :
    ∃ (X : RingedSpace.{0, 0}) (e : X ≃ₜ Point)
      (σ : X.presheaf ≅
        TopCat.presheafToTopCommRing (X := X.carrier) (TopCommRingCat.of ℝ))
      (s : SheafOfModules.free (R := structureSheafRing X) ℕ ≅
        associatedSheaf X (RingHom.id (X.presheaf.obj (op ⊤)))
          (ModuleCat.of (X.presheaf.obj (op ⊤))
            (ℕ →₀ X.presheaf.obj (op ⊤))))
      (t : SheafOfModules.free (R := structureSheafRing X) (ℕ × ℕ) ≅
        associatedSheaf X (RingHom.id (X.presheaf.obj (op ⊤)))
          (ModuleCat.of (X.presheaf.obj (op ⊤))
            ((ℕ × ℕ) →₀ X.presheaf.obj (op ⊤))))
      (φ : associatedSheaf X (RingHom.id (X.presheaf.obj (op ⊤)))
          (ModuleCat.of (X.presheaf.obj (op ⊤))
            (ℕ →₀ X.presheaf.obj (op ⊤))) ⟶
        associatedSheaf X (RingHom.id (X.presheaf.obj (op ⊤)))
          (ModuleCat.of (X.presheaf.obj (op ⊤))
            ((ℕ × ℕ) →₀ X.presheaf.obj (op ⊤)))),
      (∀ j : ℕ, s.hom.val.app (op ⊤) (basisSection X ⊤ j) =
        ((associatedSheafAdjunction X
          (RingHom.id (X.presheaf.obj (op ⊤)))).unit.app
          (ModuleCat.of (X.presheaf.obj (op ⊤))
            (ℕ →₀ X.presheaf.obj (op ⊤)))) (Finsupp.single j 1)) ∧
      (∀ k : ℕ × ℕ, t.hom.val.app (op ⊤) (basisSection X ⊤ k) =
        ((associatedSheafAdjunction X
          (RingHom.id (X.presheaf.obj (op ⊤)))).unit.app
          (ModuleCat.of (X.presheaf.obj (op ⊤))
            ((ℕ × ℕ) →₀ X.presheaf.obj (op ⊤)))) (Finsupp.single k 1)) ∧
      (∃ (f : ℝ → ℝ) (_ : Continuous f),
        (∀ x : ℝ, |x| < 1 → f x = 0) ∧
        (∀ x : ℝ, 2 < |x| → f x = 1) ∧
        (∃ π : (ℕ × ℕ) →
            (SheafOfModules.free (R := structureSheafRing X) (ℕ × ℕ) ⟶
              SheafOfModules.unit (structureSheafRing X)),
          (∀ k l : ℕ × ℕ,
            SheafOfModules.ιFree (R := structureSheafRing X) l ≫ π k = if k = l then 𝟙 _ else 0) ∧
          (∀ (U : Opens X) (j i : ℕ) (x : {x : ℝ // x ≠ 0})
            (hx : e.symm (branch i x) ∈ U) (k : ℕ × ℕ),
            ((σ.hom.app (op U)
              ((π k).val.app (op U)
                (t.inv.val.app (op U)
                  (φ.val.app (op U)
                    (s.hom.val.app (op U) (basisSection X U j))))))).hom
                ⟨e.symm (branch i x), hx⟩ =
              if k = (j, i) then f ((j + 1) * (x : ℝ)) else 0))) ∧
      (∀ U : Opens X, e.symm origin ∈ U →
        ∃ j : ℕ, ∀ g : (ℕ × ℕ) →₀ (structureSheafRing X).obj.obj (op U),
          φ.val.app (op U) (s.hom.val.app (op U) (basisSection X U j)) ≠
            t.hom.val.app (op U)
              (g.sum (fun k r => r • basisSection X U k)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 17.10, Tag 01BD](https://stacks.math.columbia.edu/tag/01BD)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
