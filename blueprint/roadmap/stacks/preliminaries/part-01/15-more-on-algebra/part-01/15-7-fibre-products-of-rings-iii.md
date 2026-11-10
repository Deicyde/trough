---
declaration: section
origin: cited
lean: MilnorPatching.RelativeModuleFibreProductSituation, MilnorPatching.extensionOfScalarsToTensorProductPullback, MilnorPatching.relativeCompatiblePairsRightAdjoint_counit_isIso, MilnorPatching.image_extendedKernel_eq_extendedIdeal, MilnorPatching.finite_relativeRightAdjoint_obj_of_finite_components, MilnorPatching.relativelyFlatModulesEquivalenceOverFibreProduct, MilnorPatching.finitePresentation_rightAdjoint_obj_of_factorization, MilnorPatching.ringHom_properties_pullback_iff_and_flatAlgebra_equivalence
statement: formalized
proof: formalized
---

# 15.7 Fibre products of rings, III

Section 15.7 of the Stacks Project, [Tag 0D2K](https://stacks.math.columbia.edu/tag/0D2K). 9 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08KK, a situation

[Tag 08KK](https://stacks.math.columbia.edu/tag/08KK) in the Stacks Project.

**`MilnorPatching.RelativeModuleFibreProductSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/MilnorPatching/Relative.lean, line 355](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/MilnorPatching/Relative.lean#L355).

> **Stacks Project, Tag 08KK.** The relative fibre-product situation consists of a
> fibre-product square `B' = B ×_A A'` as in Tag 08KH and an additional ring map
> `B' → D'`.

```lean
public structure RelativeModuleFibreProductSituation
    (base : RingFibreProduct.Situation toBase surjection I)
```

## Tag 08KL, an equation

[Tag 08KL](https://stacks.math.columbia.edu/tag/08KL) in the Stacks Project.

**`MilnorPatching.extensionOfScalarsToTensorProductPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/MilnorPatching/Relative.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/MilnorPatching/Relative.lean#L82).

> **Stacks Project, Tag 08KL.** After base change along a `B'`-algebra `D'`, extension
> of scalars gives the functor
> `Mod D' \longrightarrow Mod (D' \otimes_{B'} B) \times_{Mod (D' \otimes_{B'} A)}
> Mod (D' \otimes_{B'} A')`.
>
> It sends a module `L'` to its scalar extensions to `D' \otimes_{B'} B` and
> `D' \otimes_{B'} A'`, equipped with the canonical identification after extending both
> once more to `D' \otimes_{B'} A`.

```lean
noncomputable def extensionOfScalarsToTensorProductPullback
    {B' : Type uB'} {B : Type uB} {A' : Type uA'} {A : Type uA} {D' : Type uD'}
    [CommRing B'] [CommRing B] [CommRing A'] [CommRing A]
    [CommRing D'] [Algebra B' B] [Algebra B' A'] [Algebra B' A] [Algebra B' D']
    (BtoA : B →ₐ[B'] A) (A'toA : A' →ₐ[B'] A) :
    ModuleCat.{max v uD' uB uA' uA} D' ⥤
      CategoricalPullback
        (ModuleCat.extendScalars.{_, _, max v uD' uB uA' uA}
          (Algebra.TensorProduct.map (AlgHom.id B' D') BtoA).toRingHom)
        (ModuleCat.extendScalars.{_, _, max v uD' uB uA' uA}
          (Algebra.TensorProduct.map (AlgHom.id B' D') A'toA).toRingHom)
```

## Tag 08KM, a lemma

[Tag 08KM](https://stacks.math.columbia.edu/tag/08KM) in the Stacks Project.

**`MilnorPatching.relativeCompatiblePairsRightAdjoint_counit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/MilnorPatching/Relative.lean, line 1062](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/MilnorPatching/Relative.lean#L1062).

> **Stacks Project, Tag 08KM.** In the relative fibre-product situation, extension of
> scalars from `D'` to compatible `D`- and `C'`-modules has a right adjoint.  Its value on
> `(N, M', φ)` is naturally the fibre product `N ×_{M' / I M'} M'`.  The counit is an
> isomorphism, so extending this fibre-product module back to `D` and to `C'` canonically
> and naturally recovers `N` and `M'`.

```lean
public theorem relativeCompatiblePairsRightAdjoint_counit_isIso
    (s : RelativeModuleFibreProductSituation (D' := D') base) :
    ∃ (F : RelativeModuleFibreProductSituation.CompatibleModules s ⥤
          ModuleCat.{u} D')
      (e : ∀ X, F.obj X ≃ RelativeCompatiblePairs s X)
      (adj : (letI : Algebra base.fibreProduct D' := s.toD'.toAlgebra
         letI : Algebra base.fibreProduct B := (toBase.pullbackFst surjection).toAlgebra
         letI : Algebra base.fibreProduct A' := (toBase.pullbackSnd surjection).toAlgebra
         letI : Algebra base.fibreProduct A := (toBase.comp (toBase.pullbackFst
           surjection)).toAlgebra
         extensionOfScalarsToTensorProductPullback (D' := D')
           ({ toBase with commutes' := fun _ => rfl } : B →ₐ[base.fibreProduct] A)
           ({ surjection with commutes' := fun r => r.property.symm } : A' →ₐ[base.fibreProduct] A))
             ⊣ F),
      (∀ (L : ModuleCat.{u} D') (X) (h : L ⟶ F.obj X) (l : L),
          (e X (h l)).1.1 =
              ((adj.homEquiv L X).symm h).fst
                ((1 : s.D) ⊗ₜ[D',s.toD] l) ∧
            (e X (h l)).1.2 =
              ((adj.homEquiv L X).symm h).snd
                ((1 : s.C') ⊗ₜ[D',s.toC'] l)) ∧
        IsIso adj.counit
```

## Tag 08KN, a lemma

[Tag 08KN](https://stacks.math.columbia.edu/tag/08KN) in the Stacks Project.

**`MilnorPatching.image_extendedKernel_eq_extendedIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/MilnorPatching/Relative.lean, line 919](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/MilnorPatching/Relative.lean#L919).

> **Stacks Project, Tag 08KN.** If `J` is the kernel of `B' → B`, then the
> canonical map from `J D'` to `I C'` is surjective.

```lean
public theorem image_extendedKernel_eq_extendedIdeal
    (s : RelativeModuleFibreProductSituation (D' := D') base) :
    s.toC' ''
        (↑((RingHom.ker (toB (base := base))).map s.toD') : Set D') =
      (↑(I.map s.A'toC') : Set s.C')
```

## Tag 08IH, a lemma

[Tag 08IH](https://stacks.math.columbia.edu/tag/08IH) in the Stacks Project.

**`MilnorPatching.finite_relativeRightAdjoint_obj_of_finite_components`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/MilnorPatching/RelativeProperties.lean, line 369](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/MilnorPatching/RelativeProperties.lean#L369).

> **Stacks Project, Tag 08IH.** In a relative module fibre-product situation, the
> compatible-pairs module associated to a finite `D`-module and a finite `C'`-module is
> finite over `D'`.

```lean
public theorem finite_relativeRightAdjoint_obj_of_finite_components
    {A A' B D' : Type u} [CommRing A] [CommRing A'] [CommRing B] [CommRing D']
    {toBase : B →+* A} {surjection : A' →+* A} {I : Ideal A'}
    {base : RingFibreProduct.Situation toBase surjection I}
    (s : RelativeModuleFibreProductSituation (D' := D') base)
    (F : RelativeModuleFibreProductSituation.CompatibleModules s ⥤
      ModuleCat.{u} D')
    (adj : (letI : Algebra base.fibreProduct D' := s.toD'.toAlgebra
       letI : Algebra base.fibreProduct B := (toBase.pullbackFst surjection).toAlgebra
       letI : Algebra base.fibreProduct A' := (toBase.pullbackSnd surjection).toAlgebra
       letI : Algebra base.fibreProduct A := (toBase.comp (toBase.pullbackFst surjection)).toAlgebra
       extensionOfScalarsToTensorProductPullback (D' := D')
         ({ toBase with commutes' := fun _ => rfl } : B →ₐ[base.fibreProduct] A)
         ({ surjection with commutes' := fun r => r.property.symm } : A' →ₐ[base.fibreProduct] A)) ⊣
           F)
    (hCounit : IsIso adj.counit)
    (X : RelativeModuleFibreProductSituation.CompatibleModules s) :
    Module.Finite s.D X.fst → Module.Finite s.C' X.snd →
      Module.Finite D' (F.obj X)
```

## Tag 07RW, a lemma

[Tag 07RW](https://stacks.math.columbia.edu/tag/07RW) in the Stacks Project.

**`MilnorPatching.relativelyFlatModulesEquivalenceOverFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/MilnorPatching/RelativeProperties.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/MilnorPatching/RelativeProperties.lean#L134).

> **Stacks Project, Tag 07RW.** In a relative fibre-product situation, compatible pairs
> whose components are flat over the original rings glue to a module flat over the original
> fibre-product ring. Every relatively flat module is canonically reconstructed from its scalar
> extensions, and these operations induce an equivalence of the corresponding full
> subcategories.
>
> Relative flatness, canonical reconstruction, and gluing of relatively flat modules.

```lean
public theorem relativelyFlatModulesEquivalenceOverFibreProduct
    {A A' B D' : Type u} [CommRing A] [CommRing A'] [CommRing B] [CommRing D']
    {toBase : B →+* A} {surjection : A' →+* A} {I : Ideal A'}
    {base : RingFibreProduct.Situation toBase surjection I}
    (s : RelativeModuleFibreProductSituation (D' := D') base) :
    let E := (letI : Algebra base.fibreProduct D' := s.toD'.toAlgebra
       letI : Algebra base.fibreProduct B := (toBase.pullbackFst surjection).toAlgebra
       letI : Algebra base.fibreProduct A' := (toBase.pullbackSnd surjection).toAlgebra
       letI : Algebra base.fibreProduct A := (toBase.comp (toBase.pullbackFst surjection)).toAlgebra
       extensionOfScalarsToTensorProductPullback (D' := D')
         ({ toBase with commutes' := fun _ => rfl } : B →ₐ[base.fibreProduct] A)
         ({ surjection with commutes' := fun r => r.property.symm } : A' →ₐ[base.fibreProduct] A))
    let flatSource : ObjectProperty (ModuleCat.{u} D') :=
      fun L ↦ Module.Flat base.fibreProduct
        ((ModuleCat.restrictScalars.{u, u, u} s.toD').obj L)
    let flatTarget : ObjectProperty
        (RelativeModuleFibreProductSituation.CompatibleModules s) :=
      fun X ↦
        Module.Flat B ((ModuleCat.restrictScalars.{u, u, u} s.BtoD).obj X.fst) ∧
          Module.Flat A'
            ((ModuleCat.restrictScalars.{u, u, u} s.A'toC').obj X.snd)
    ∃ (F : RelativeModuleFibreProductSituation.CompatibleModules s ⥤
          ModuleCat.{u} D')
      (e : ∀ X, F.obj X ≃ₗ[D']
          compatiblePairsModule.{u} s.toD s.toC' s.DtoC s.C'toC s.relativeSquare_comm X)
      (adj : E ⊣ F),
      (∀ (L : ModuleCat.{u} D') (X) (h : L ⟶ F.obj X) (l : L),
          (e X (h l)).1.1 =
              ((adj.homEquiv L X).symm h).fst
                ((1 : s.D) ⊗ₜ[D',s.toD] l) ∧
            (e X (h l)).1.2 =
              ((adj.homEquiv L X).symm h).snd
                ((1 : s.C') ⊗ₜ[D',s.toC'] l)) ∧
        (∀ {X Y} (f : X ⟶ Y) (p : F.obj X),
          (e Y (F.map f p)).1.1 = f.fst (e X p).1.1 ∧
            (e Y (F.map f p)).1.2 = f.snd (e X p).1.2) ∧
        IsIso adj.counit ∧
        (∀ X, flatTarget X → flatSource (F.obj X)) ∧
        (∀ L, flatSource L → IsIso (adj.unit.app L)) ∧
        ∃ q : flatSource.FullSubcategory ≌ flatTarget.FullSubcategory,
          Nonempty (flatSource.ι ⋙ E ≅ q.functor ⋙ flatTarget.ι) ∧
            Nonempty (flatTarget.ι ⋙ F ≅ q.inverse ⋙ flatSource.ι)
```

## Tag 08KP, a lemma

[Tag 08KP](https://stacks.math.columbia.edu/tag/08KP) in the Stacks Project.

**`MilnorPatching.finitePresentation_rightAdjoint_obj_of_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/MilnorPatching/RelativeProperties.lean, line 1310](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/MilnorPatching/RelativeProperties.lean#L1310).

> **Stacks Project, Tag 08KP.** In a relative module fibre-product situation, the
> compatible-pairs module is finitely presented over `D'` if its `D`-component and
> `C'`-component are finitely presented and flat over `B` and `A'`, respectively, and
> the map `B' → D'` factors as a flat map followed by a finitely presented map.

```lean
public theorem finitePresentation_rightAdjoint_obj_of_factorization
    {A A' B D' : Type u} {D'' : Type v}
    [CommRing A] [CommRing A'] [CommRing B] [CommRing D'] [CommRing D'']
    {toBase : B →+* A} {surjection : A' →+* A} {I : Ideal A'}
    {base : RingFibreProduct.Situation toBase surjection I}
    (s : RelativeModuleFibreProductSituation (D' := D') base)
    (F : RelativeModuleFibreProductSituation.CompatibleModules s ⥤
      ModuleCat.{u} D')
    (adj : (letI : Algebra base.fibreProduct D' := s.toD'.toAlgebra
       letI : Algebra base.fibreProduct B := (toBase.pullbackFst surjection).toAlgebra
       letI : Algebra base.fibreProduct A' := (toBase.pullbackSnd surjection).toAlgebra
       letI : Algebra base.fibreProduct A := (toBase.comp (toBase.pullbackFst surjection)).toAlgebra
       extensionOfScalarsToTensorProductPullback (D' := D')
         ({ toBase with commutes' := fun _ => rfl } : B →ₐ[base.fibreProduct] A)
         ({ surjection with commutes' := fun r => r.property.symm } : A' →ₐ[base.fibreProduct] A)) ⊣
           F)
    (_ : IsIso adj.counit)
    (X : RelativeModuleFibreProductSituation.CompatibleModules s)
    (_ : Module.FinitePresentation s.D X.fst)
    (_ : Module.Flat B ((ModuleCat.restrictScalars s.BtoD).obj X.fst))
    (_ : Module.FinitePresentation s.C' X.snd)
    (_ : Module.Flat A' ((ModuleCat.restrictScalars s.A'toC').obj X.snd))
    (toD'' : base.fibreProduct →+* D'') (fromD'' : D'' →+* D')
    (_ : fromD''.comp toD'' = s.toD')
    (_ : @Module.Flat base.fibreProduct D'' _ _ (Module.compHom D'' toD''))
    (_ : fromD''.FinitePresentation) :
    Module.FinitePresentation D' (F.obj X)
```

## Tag 08KQ, a lemma

[Tag 08KQ](https://stacks.math.columbia.edu/tag/08KQ) in the Stacks Project.

**`MilnorPatching.ringHom_properties_pullback_iff_and_flatAlgebra_equivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/MilnorPatching/Algebras.lean, line 1456](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/MilnorPatching/Algebras.lean#L1456).

> **Stacks Project, Tag 08KQ.** Properties of an algebra obtained by gluing algebras over a
> fibre product are detected on its two base changes. Every flat algebra over the fibre product
> is canonically reconstructed from those base changes, and base change induces an equivalence
> with the category of compatible systems of flat algebras.

```lean
public theorem ringHom_properties_pullback_iff_and_flatAlgebra_equivalence
    {A A' B : Type u} {D : Type v} {C' : Type w} {C : Type x}
    [CommRing A] [CommRing A'] [CommRing B] [CommRing D] [CommRing C'] [CommRing C]
    (toBase : B →+* A) (surjection : A' →+* A) (I : Ideal A')
    (base : RingFibreProduct.Situation toBase surjection I)
    (BtoD : B →+* D) (A'toC' : A' →+* C') (AtoC : A →+* C)
    (DtoC : D →+* C) (C'toC : C' →+* C)
    (hD : ringPushout BtoD toBase DtoC AtoC)
    (hC' : ringPushout A'toC' surjection C'toC AtoC) :
    let toB : base.fibreProduct →+* B := base.pullbackCone.fst.hom
    let toA' : base.fibreProduct →+* A' := base.pullbackCone.snd.hom
    let toD' : base.fibreProduct →+* RingHom.pullback DtoC C'toC :=
      RingHom.codRestrict ((BtoD.comp toB).prod (A'toC'.comp toA'))
        (RingHom.pullback DtoC C'toC) (fun x ↦ by
          change DtoC (BtoD (toB x)) = C'toC (A'toC' (toA' x))
          have hd : DtoC.comp BtoD = AtoC.comp toBase := ringPushout_comm hD
          have hc : C'toC.comp A'toC' = AtoC.comp surjection := ringPushout_comm hC'
          calc
            _ = AtoC (toBase (toB x)) := DFunLike.congr_fun hd (toB x)
            _ = AtoC (surjection (toA' x)) := congrArg AtoC
              (DFunLike.congr_fun
                (congrArg CommRingCat.Hom.hom base.pullbackCone.condition) x)
            _ = _ := (DFunLike.congr_fun hc (toA' x)).symm)
    let flat := CommRingCat.flat
    let BtoA := MorphismProperty.Under.pushout flat ⊤ (CommRingCat.ofHom toBase)
    let A'toA := MorphismProperty.Under.pushout flat ⊤ (CommRingCat.ofHom surjection)
    let B'toB := MorphismProperty.Under.pushout flat ⊤ (CommRingCat.ofHom toB)
    let B'toA' := MorphismProperty.Under.pushout flat ⊤ (CommRingCat.ofHom toA')
    (toD'.FiniteType ↔ BtoD.FiniteType ∧ A'toC'.FiniteType) ∧
      (toD'.Flat ↔ BtoD.Flat ∧ A'toC'.Flat) ∧
      (toD'.Flat ∧ toD'.FinitePresentation ↔
        (BtoD.Flat ∧ BtoD.FinitePresentation) ∧
          (A'toC'.Flat ∧ A'toC'.FinitePresentation)) ∧
      (toD'.Smooth ↔ BtoD.Smooth ∧ A'toC'.Smooth) ∧
      (toD'.Etale ↔ BtoD.Etale ∧ A'toC'.Etale) ∧
      (∀ (E : Type u) [CommRing E] (f : base.fibreProduct →+* E), f.Flat →
        let s : RelativeModuleFibreProductSituation (D' := E) base := ⟨f⟩
        Function.Bijective s.toRelativePullback) ∧
      ∃ q : (flat.Under ⊤ (CommRingCat.of base.fibreProduct)) ≌
          CategoricalPullback BtoA A'toA,
        Nonempty (q.functor ⋙ CategoricalPullback.π₁ BtoA A'toA ≅ B'toB) ∧
          Nonempty (q.functor ⋙ CategoricalPullback.π₂ BtoA A'toA ≅ B'toA')
```

## Tag 08KR, a remark

[Tag 08KR](https://stacks.math.columbia.edu/tag/08KR) in the Stacks Project.

**`MilnorPatching.relativeFlatFinitelyPresentedQuotientsEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/MilnorPatching/Quotients.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/MilnorPatching/Quotients.lean#L332).

> **Stacks Project, Tag 08KR.** If `B' → D'` is of finite presentation, the
> finitely presented quotients of a `D'`-module which are flat over `B'` correspond to
> pairs of finitely presented quotients after base change to `D` and `C'`, flat over `B`
> and `A'`, and agreeing as quotients after base change to `C`.
>
> The forward correspondence is extension of scalars.  The inverse target module is the
> fibre product of the two quotient modules over their common quotient over `C`; the final
> formula records the prescribed quotient map from `L`.
>
> Scalar extension and the compatible-pairs construction give the canonical equivalence of
> finitely presented relatively flat quotient categories.

```lean
public theorem relativeFlatFinitelyPresentedQuotientsEquivalence
    (s : RelativeModuleFibreProductSituation (D' := D') base)
    (hfp : s.toD'.FinitePresentation) (L : ModuleCat.{u} D') :
    let E := (letI : Algebra base.fibreProduct D' := s.toD'.toAlgebra
       letI : Algebra base.fibreProduct B := (toBase.pullbackFst surjection).toAlgebra
       letI : Algebra base.fibreProduct A' := (toBase.pullbackSnd surjection).toAlgebra
       letI : Algebra base.fibreProduct A := (toBase.comp (toBase.pullbackFst surjection)).toAlgebra
       extensionOfScalarsToTensorProductPullback (D' := D')
         ({ toBase with commutes' := fun _ => rfl } : B →ₐ[base.fibreProduct] A)
         ({ surjection with commutes' := fun r => r.property.symm } : A' →ₐ[base.fibreProduct] A))
    let source := (RelativeFlatFinitelyPresentedQuotient s L).FullSubcategory
    let target := (CompatibleRelativeFlatFinitelyPresentedQuotient s L).FullSubcategory
    ∃ e : source ≌ target,
      Nonempty
          ((RelativeFlatFinitelyPresentedQuotient s L).ι ⋙ Under.post E ≅
            e.functor ⋙ (CompatibleRelativeFlatFinitelyPresentedQuotient s L).ι) ∧
        ∀ q : target,
          ∃ glueEquiv : (e.inverse.obj q).obj.right ≃
              RelativeCompatiblePairs s q.obj.right,
            ∀ l : L,
              (glueEquiv ((e.inverse.obj q).obj.hom l)).1.1 =
                  q.obj.hom.fst
                    ((ModuleCat.extendRestrictScalarsAdj s.toD).unit.app L l) ∧
                (glueEquiv ((e.inverse.obj q).obj.hom l)).1.2 =
                  q.obj.hom.snd
                    ((ModuleCat.extendRestrictScalarsAdj s.toC').unit.app L l)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.7, Tag 0D2K](https://stacks.math.columbia.edu/tag/0D2K)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
