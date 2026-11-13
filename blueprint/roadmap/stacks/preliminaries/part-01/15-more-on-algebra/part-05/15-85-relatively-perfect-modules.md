---
declaration: section
origin: cited
lean: PseudoCoherence.IsRelativelyPerfect, PseudoCoherence.isClosedUnderIsomorphisms_relativelyPerfect, PseudoCoherence.isTriangulated_relativelyPerfect, PseudoCoherence.isSaturated_relativelyPerfect, PseudoCoherence.isRelativelyPerfect_of_isPerfect, PseudoCoherence.isRelativelyPerfect_derivedTensor, PseudoCoherence.isRelativelyPerfect_iff_exists_bounded_flat_finitePresentation, PseudoCoherence.derivedExtensionScalars_isRelativelyPerfect
statement: formalized
proof: formalized
---

# 15.85 Relatively perfect modules

Section 15.85 of the Stacks Project, [Tag 0DHR](https://stacks.math.columbia.edu/tag/0DHR). 10 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DHS, a definition

[Tag 0DHS](https://stacks.math.columbia.edu/tag/0DHS) in the Stacks Project.

**`PseudoCoherence.IsRelativelyPerfect`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/RelativelyPerfect.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/PseudoCoherent/RelativelyPerfect.lean#L59). References: SGA 6 III (4.1), “affine, flat f.p. case”.

> **Stacks 0DHS.** For a flat, finitely presented ring map `R → A`, an object `K` of `D(A)` is
> perfect relative to `R` if it is pseudo-coherent over `A` and its restriction of scalars has
> finite Tor dimension over `R`.

```lean
public def IsRelativelyPerfect
    {R : Type u} {A : Type v} [CommRing R] [CommRing A] [Algebra R A]
    [Module.Flat R A] [Algebra.FinitePresentation R A]
    (derivedTensor :
      DerivedCategory (ModuleCat.{max u v w} R) ⥤
        DerivedCategory (ModuleCat.{max u v w} R) ⥤ DerivedCategory (ModuleCat.{max u v w} R))
    (comparison : ∀ M : ModuleCat.{max u v w} R,
      DerivedCategory.Q ⋙
          derivedTensor.flip.obj
            ((DerivedCategory.singleFunctor (ModuleCat.{max u v w} R) 0).obj M) ⟶
        (StacksDraft.TorAmplitude.tensorModuleRight M).mapHomologicalComplex
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (isLeftDerived : ∀ M : ModuleCat.{max u v w} R,
      (derivedTensor.flip.obj
          ((DerivedCategory.singleFunctor
            (ModuleCat.{max u v w} R) 0).obj M)).IsLeftDerivedFunctor
        (comparison M)
        (HomologicalComplex.quasiIso (ModuleCat.{max u v w} R) (ComplexShape.up ℤ)))
    (K : DerivedCategory (ModuleCat.{max u v w} A)) : Prop
```

## Tag 0DHT, a lemma

[Tag 0DHT](https://stacks.math.columbia.edu/tag/0DHT) in the Stacks Project.

**`PseudoCoherence.isClosedUnderIsomorphisms_relativelyPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/RelativelyPerfect/Triangulated.lean, line 267](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/RelativelyPerfect/Triangulated.lean#L267).

> For a flat, finitely presented ring map `R → A`, the objects of `D(A)` perfect relative to
> `R` form a *strictly full* subcategory: relative perfectness is invariant under isomorphism in
> `D(A)`.

```lean
theorem isClosedUnderIsomorphisms_relativelyPerfect :
    (relativelyPerfect.{u, v, w} (A := A) derivedTensor comparison
      isLeftDerived).IsClosedUnderIsomorphisms
```

**`PseudoCoherence.isTriangulated_relativelyPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/RelativelyPerfect/Triangulated.lean, line 299](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/RelativelyPerfect/Triangulated.lean#L299). References: SGA 6 III (4.2), “affine case, flat f.p.”.

> For a flat, finitely presented ring map `R → A`, the objects of `D(A)` perfect relative to
> `R` form a *triangulated* subcategory: the property contains the zero object, is stable under all
> shifts, and is closed under extensions.

```lean
theorem isTriangulated_relativelyPerfect :
    (relativelyPerfect.{u, v, w} (A := A) derivedTensor comparison
      isLeftDerived).IsTriangulated
```

**`PseudoCoherence.isSaturated_relativelyPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/RelativelyPerfect/Triangulated.lean, line 325](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/RelativelyPerfect/Triangulated.lean#L325).

> For a flat, finitely presented ring map `R → A`, the objects of `D(A)` perfect relative to
> `R` form a *saturated* (thick) subcategory: a direct summand of a relatively perfect object is
> relatively perfect.

```lean
theorem isSaturated_relativelyPerfect :
    (relativelyPerfect.{u, v, w} (A := A) derivedTensor comparison
      isLeftDerived).IsSaturated
```

## Tag 0DHU, a lemma

[Tag 0DHU](https://stacks.math.columbia.edu/tag/0DHU) in the Stacks Project.

**`PseudoCoherence.isRelativelyPerfect_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/RelativelyPerfect/Tensor.lean, line 630](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/RelativelyPerfect/Tensor.lean#L630).

> **Stacks 0DHU.** For a flat, finitely presented ring map `R → A`, a perfect object of `D(A)`
> is perfect relative to `R`: a bounded complex of finite projective `A`-modules representing it is
> pseudo-coherent by Stacks 064U, and its terms are flat over `R` by transitivity of flatness, so
> its restriction to `R` has finite Tor dimension.

```lean
theorem isRelativelyPerfect_of_isPerfect (K : DerivedCategory (ModuleCat.{max u v w} A))
    (hK : StacksDraft.Perfect.IsPerfect K) :
    IsRelativelyPerfect.{u, v, w} derivedTensor comparison isLeftDerived K
```

**`PseudoCoherence.isRelativelyPerfect_derivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/RelativelyPerfect/Tensor.lean, line 695](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/RelativelyPerfect/Tensor.lean#L695).

> **Stacks 0DHU.** For a flat, finitely presented ring map `R → A`, the derived tensor product
> over `A` of a perfect object of `D(A)` with an `R`-perfect object is `R`-perfect.
>
> Pseudo-coherence: a bounded-above finite free representative of the perfect object is K-flat, so
> the derived tensor product is computed by the total tensor product with a bounded-above finite
> free representative of the `R`-perfect object, and that has bounded-above finite free terms.
>
> Finite Tor dimension: a *bounded* finite projective representative of the perfect object is also
> K-flat, and the `R`-perfect object has a bounded representative whose terms are flat over `R`
> (Stacks 0653); the total tensor product of the two is bounded with terms flat over `R`.

```lean
theorem isRelativelyPerfect_derivedTensor
    (K M : DerivedCategory (ModuleCat.{max u v w} A))
    (hK : StacksDraft.Perfect.IsPerfect K)
    (hM : IsRelativelyPerfect.{u, v, w} derivedTensor comparison isLeftDerived M) :
    IsRelativelyPerfect.{u, v, w} derivedTensor comparison isLeftDerived
      ((derivedTensorA.obj K).obj M)
```

## Tag 0DHV, a lemma

[Tag 0DHV](https://stacks.math.columbia.edu/tag/0DHV) in the Stacks Project.

**`PseudoCoherence.isRelativelyPerfect_iff_exists_bounded_flat_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/RelativelyPerfect/FlatComplex.lean, line 356](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/RelativelyPerfect/FlatComplex.lean#L356).

> **Stacks 0DHV.** For a flat, finitely presented ring map `R → A`, an object of `D(A)` is
> perfect relative to `R` if and only if it is isomorphic to a finite complex of `A`-modules that
> are flat over `R` and finitely presented over `A`.

```lean
theorem isRelativelyPerfect_iff_exists_bounded_flat_finitePresentation
    (K : DerivedCategory (ModuleCat.{max u v w} A)) :
    IsRelativelyPerfect.{u, v, w} derivedTensor comparison isLeftDerived K ↔
      ∃ (P : CochainComplex (ModuleCat.{max u v w} A) ℤ) (a b : ℤ),
        P.IsStrictlyGE a ∧ P.IsStrictlyLE b ∧
        (∀ i : ℤ, Module.Flat R
          ((ModuleCat.restrictScalars (algebraMap R A)).obj (P.X i))) ∧
        (∀ i : ℤ, Module.FinitePresentation A (P.X i)) ∧
        Nonempty (K ≅ DerivedCategory.Q.obj P)
```

## Tag 0DHW, a lemma

[Tag 0DHW](https://stacks.math.columbia.edu/tag/0DHW) in the Stacks Project.

**`PseudoCoherence.derivedExtensionScalars_isRelativelyPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/RelativelyPerfect/BaseChange.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/RelativelyPerfect/BaseChange.lean#L121).

> **Stacks 0DHW.** If `A` is flat and finitely presented over `R`, then arbitrary base change
> `R → R'` sends an `R`-perfect object of `D(A)` to an `R'`-perfect object of `D(A ⊗[R] R')`.

```lean
theorem derivedExtensionScalars_isRelativelyPerfect
    {R A R' : Type u} [CommRing R] [CommRing A] [CommRing R']
    [Algebra R A] [Algebra R R'] [Module.Flat R A] [Algebra.FinitePresentation R A]
    (derivedTensorR :
      DerivedCategory (ModuleCat.{u} R) ⥤
        DerivedCategory (ModuleCat.{u} R) ⥤ DerivedCategory (ModuleCat.{u} R))
    (comparisonR : ∀ M : ModuleCat.{u} R,
      DerivedCategory.Q ⋙
          derivedTensorR.flip.obj ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj M) ⟶
        (tensorModuleRight M).mapHomologicalComplex (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (isLeftDerivedR : ∀ M : ModuleCat.{u} R,
      (derivedTensorR.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj M)).IsLeftDerivedFunctor
        (comparisonR M)
        (HomologicalComplex.quasiIso (ModuleCat.{u} R) (ComplexShape.up ℤ)))
    (derivedTensorR' :
      DerivedCategory (ModuleCat.{u} R') ⥤
        DerivedCategory (ModuleCat.{u} R') ⥤ DerivedCategory (ModuleCat.{u} R'))
    (comparisonR' : ∀ M : ModuleCat.{u} R',
      DerivedCategory.Q ⋙
          derivedTensorR'.flip.obj ((DerivedCategory.singleFunctor (ModuleCat.{u} R') 0).obj M) ⟶
        (tensorModuleRight M).mapHomologicalComplex (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (isLeftDerivedR' : ∀ M : ModuleCat.{u} R',
      (derivedTensorR'.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R') 0).obj M)).IsLeftDerivedFunctor
        (comparisonR' M)
        (HomologicalComplex.quasiIso (ModuleCat.{u} R') (ComplexShape.up ℤ)))
    (K : DerivedCategory (ModuleCat.{u} A))
    (hK : IsRelativelyPerfect.{u, u, u} derivedTensorR comparisonR isLeftDerivedR K) :
    let A' := A ⊗[R] R'
    letI : Algebra R' A' := Algebra.TensorProduct.rightAlgebra
    let e : (R' ⊗[R] A) ≃ₐ[R'] A' :=
      AlgEquiv.ofRingEquiv (f := (Algebra.TensorProduct.comm R R' A).toRingEquiv)
        (fun r' => by
          change (Algebra.TensorProduct.comm R R' A)
            (algebraMap R' (R' ⊗[R] A) r') = _
          rw [Algebra.TensorProduct.algebraMap_apply, Algebra.algebraMap_self_apply,
            Algebra.TensorProduct.comm_tmul]
          rfl)
    letI : Module.Flat R' A' := Module.Flat.of_linearEquiv e.symm.toLinearEquiv
    letI : Algebra.FinitePresentation R' A' := Algebra.FinitePresentation.equiv e
    let f : A →+* A' := Algebra.TensorProduct.includeLeftRingHom
    IsRelativelyPerfect.{u, u, u} derivedTensorR' comparisonR' isLeftDerivedR'
      ((totalDerivedExtensionScalars.{u, u, u} f).functor.obj K)
```

## Tag 0E1U, a lemma

[Tag 0E1U](https://stacks.math.columbia.edu/tag/0E1U) in the Stacks Project.

**`StacksDraft.RelativelyPerfect.relativeHomComplex_represents_RHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/RelativelyPerfect/RepresentativeBaseChange.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/RelativelyPerfect/RepresentativeBaseChange.lean#L207).

> **Stacks 0E1U.** Let `R → A` be a flat ring map, and let `K, L ∈ D(A)` with `K`
> pseudo-coherent and `L` of finite Tor dimension over `R`. Then:
>
> (1)–(2) there are a bounded above complex `P` of finite free `A`-modules representing `K` and a
> bounded complex `F` of `R`-flat `A`-modules representing `L`;
>
> given any such choices,
>
> (a) `E = Hom^•(P, F)` is a bounded below complex of `R`-flat `A`-modules representing
> `RHom_A(K, L)`;
>
> (b) for every ring map `R → R'`, with `A' = A ⊗_R R'`, the complex `E ⊗_A A'` represents
> `RHom_{A'}(K ⊗ᴸ_A A', L ⊗ᴸ_A A')`: `P ⊗_A A'` and `F ⊗_A A'` represent the derived base changes
> of `K` and `L`, their Hom complex computes the morphisms between these, and `E ⊗_A A'` is
> canonically that Hom complex (see
> `StacksDraft.RelativelyPerfect.IsRelativeHomRepresentativePair.represents_RHom_baseChange`).
>
> If moreover `R → A` is of finite presentation and `L` is `R`-perfect (pseudo-coherent, its finite
> Tor dimension over `R` being already assumed), the choices can be made with every `F^p`, and
> consequently every `E^n`, a finitely presented `A`-module.
>
> Objects of `D(A)` are presented by cochain complexes `K` and `L`; finite Tor dimension over `R`
> is Tor amplitude in some `[a, b]` of `L` viewed as a complex of `R`-modules.

```lean
theorem relativeHomComplex_represents_RHom [Module.Flat R A]
    (K L : CochainComplex (ModuleCat.{u} A) ℤ)
    (hK : ∀ m : ℤ, IsPseudoCoherentFrom (DerivedCategory.Q.obj K) m)
    (hL : ∃ a b : ℤ, StacksDraft.TorAmplitude.FaithfullyFlat.HasTorAmplitude
      (((ModuleCat.restrictScalars (algebraMap R A)).mapHomologicalComplex (.up ℤ)).obj L) a b) :
    (∃ (P F : CochainComplex (ModuleCat.{u} A) ℤ)
        (_ : DerivedCategory.Q.obj P ≅ DerivedCategory.Q.obj K)
        (_ : DerivedCategory.Q.obj F ≅ DerivedCategory.Q.obj L),
        IsRelativeHomRepresentativePair R P F) ∧
      (∀ (P F : CochainComplex (ModuleCat.{u} A) ℤ)
        (eP : DerivedCategory.Q.obj P ≅ DerivedCategory.Q.obj K)
        (eF : DerivedCategory.Q.obj F ≅ DerivedCategory.Q.obj L),
        IsRelativeHomRepresentativePair R P F →
        (∃ c : ℤ, (CochainComplex.HomComplexR A P F).IsStrictlyGE c) ∧
          (∀ i : ℤ, Module.Flat R
            ((ModuleCat.restrictScalars (algebraMap R A)).obj
              ((CochainComplex.HomComplexR A P F).X i))) ∧
          (∀ n : ℤ, Function.Bijective (cohomologyClassToDerivedHom P F eP eF n)) ∧
          ∀ (R' : Type u) [CommRing R'] [Algebra R R'],
            let f : A →+* A ⊗[R] R' := Algebra.TensorProduct.includeLeftRingHom
            let Ext := (ModuleCat.extendScalars.{u, u, u} f).mapHomologicalComplex
              (ComplexShape.up ℤ)
            let D := (totalDerivedExtensionScalars.{u, u, u} f).functor
            ∃ (eP' : DerivedCategory.Q.obj (Ext.obj P) ≅ D.obj (DerivedCategory.Q.obj K))
              (eF' : DerivedCategory.Q.obj (Ext.obj F) ≅ D.obj (DerivedCategory.Q.obj L)),
              (∀ n : ℤ, Function.Bijective
                (cohomologyClassToDerivedHom (Ext.obj P) (Ext.obj F) eP' eF' n)) ∧
              ∃! e : Ext.obj (CochainComplex.HomComplexR A P F) ≅
                  CochainComplex.HomComplexR (A ⊗[R] R') (Ext.obj P) (Ext.obj F),
                IsCanonicalHomComplexBaseChangeIso f P F e) ∧
      (Algebra.FinitePresentation R A →
        (∀ m : ℤ, IsPseudoCoherentFrom (DerivedCategory.Q.obj L) m) →
        ∃ (P F : CochainComplex (ModuleCat.{u} A) ℤ)
          (_ : DerivedCategory.Q.obj P ≅ DerivedCategory.Q.obj K)
          (_ : DerivedCategory.Q.obj F ≅ DerivedCategory.Q.obj L),
          IsRelativeHomRepresentativePair R P F ∧
            (∀ i : ℤ, Module.FinitePresentation A (F.X i)) ∧
            ∀ n : ℤ, Module.FinitePresentation A ((CochainComplex.HomComplexR A P F).X n))
```

## Tag 0DHX, a lemma

[Tag 0DHX](https://stacks.math.columbia.edu/tag/0DHX) in the Stacks Project.

**`PseudoCoherence.relativelyPerfectComplexes_filteredColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/RelativelyPerfect/Colimit/FilteredColimit.lean, line 439](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/RelativelyPerfect/Colimit/FilteredColimit.lean#L439).

> Relatively perfect complexes descend through filtered colimits, derived Hom from a
> pseudo-coherent complex to a complex of finite Tor-dimension commutes with such a colimit, and
> the category of relatively perfect complexes over the limit is the categorical colimit of the
> categories at the stages.

```lean
public theorem relativelyPerfectComplexes_filteredColimit
    {R₀ : Type uR} [CommRing R₀]
    {I : Type uI} [Category.{uJ} I] [IsFiltered I]
    (F : I ⥤ CommAlgCat.{uR} R₀) (c : Cocone F)
    (hc : IsColimit ((CommAlgCat.uliftFunctor.{max uI uJ, uR, uR} R₀).mapCocone c))
    (A₀ : Type uA) [CommRing A₀] [Algebra R₀ A₀]
    [Module.Flat R₀ A₀] [Algebra.FinitePresentation R₀ A₀]
    (D₀ : DerivedTensoringDatum.{uR, max uR uA uM} R₀)
    (D : ∀ i : I, DerivedTensoringDatum.{uR, max uR uA uM} (F.obj i))
    (Dlim : DerivedTensoringDatum.{uR, max uR uA uM} c.pt) :
    let E := fun {A B : Type (max uR uA)} [CommRing A] [CommRing B] (f : A →+* B) ↦
      totalDerivedExtensionScalars.{max uR uA, max uR uA, uM} f
    let liftBase : ULift.{uR} A₀ →+* A₀ := ULift.ringEquiv.toRingHom
    let W := (ModuleCat.restrictScalars.{max uR uA uM} liftBase).mapDerivedCategory
    let b := fun i : I ↦ (baseToStageMap F A₀ i).comp liftBase
    let blim := (baseToLimitMap c A₀).comp liftBase
    let B := fun i : I ↦ W ⋙ (E (b i)).functor
    let Blim := W ⋙ (E blim).functor
    let S := fun (i : I) ↦ E (stageToLimitMap c A₀ i)
    let P : ∀ i : I, ObjectProperty
        (DerivedCategory (ModuleCat.{max uR uA uM} (stageAlgebra F A₀ i))) := fun i K ↦
      IsRelativelyPerfect.{uR, max uR uA, uM}
        (D i).tensor (D i).comparison (D i).isLeftDerived K
    let Plim : ObjectProperty
        (DerivedCategory (ModuleCat.{max uR uA uM} (c.pt ⊗[R₀] A₀))) := fun K ↦
      IsRelativelyPerfect.{uR, max uR uA, uM}
        Dlim.tensor Dlim.comparison Dlim.isLeftDerived K
    ∃ (comp : ∀ {A B C : Type (max uR uA)} [CommRing A] [CommRing B] [CommRing C]
          (f : A →+* B) (g : B →+* C),
          (E f).functor ⋙ (E g).functor ≅ (E (g.comp f)).functor)
      (unit : ∀ (A : Type (max uR uA)) [CommRing A],
        𝟭 (DerivedCategory (ModuleCat.{max uR uA uM} A)) ≅ (E (RingHom.id A)).functor),
      (∀ {A B C : Type (max uR uA)} [CommRing A] [CommRing B] [CommRing C]
          (f : A →+* B) (g : B →+* C)
          (Q : CochainComplex (ModuleCat.{max uR uA uM} A) ℤ),
        letI : (ModuleCat.extendScalars.{max uR uA, max uR uA, max uR uA uM} f).IsLeftAdjoint :=
          (ModuleCat.extendRestrictScalarsAdj.{max uR uA uM, max uR uA, max uR uA}
            f).isLeftAdjoint
        (E g).functor.map ((E f).comparison.app Q) ≫
            (E g).comparison.app
              (((ModuleCat.extendScalars.{max uR uA, max uR uA, max uR uA uM}
                f).mapHomologicalComplex
                (ComplexShape.up ℤ)).obj Q) ≫
            (extensionOfScalarsComplexComp.{max uR uA, uM} f g).inv.app Q =
          (comp f g).hom.app (DerivedCategory.Q.obj Q) ≫
            (E (g.comp f)).comparison.app Q) ∧
      (∀ {A B C D' : Type (max uR uA)} [CommRing A] [CommRing B] [CommRing C] [CommRing D']
          (f : A →+* B) (g : B →+* C) (h : C →+* D')
          (X : DerivedCategory (ModuleCat.{max uR uA uM} A)),
        (E h).functor.map ((comp f g).hom.app X) ≫ (comp (g.comp f) h).hom.app X =
          (comp g h).hom.app ((E f).functor.obj X) ≫
            (comp f (h.comp g)).hom.app X) ∧
      (∀ {A B : Type (max uR uA)} [CommRing A] [CommRing B] (f : A →+* B)
          (X : DerivedCategory (ModuleCat.{max uR uA uM} A)),
        (E f).functor.map ((unit A).hom.app X) ≫
            (comp (RingHom.id A) f).hom.app X = 𝟙 _) ∧
      (∀ {A B : Type (max uR uA)} [CommRing A] [CommRing B] (f : A →+* B)
          (X : DerivedCategory (ModuleCat.{max uR uA uM} A)),
        (unit B).hom.app ((E f).functor.obj X) ≫
            (comp f (RingHom.id B)).hom.app X = 𝟙 _) ∧
      (∀ (K : DerivedCategory (ModuleCat.{max uR uA uM} (c.pt ⊗[R₀] A₀))), Plim K →
        ∃ (i : I) (Kᵢ : DerivedCategory (ModuleCat.{max uR uA uM} (stageAlgebra F A₀ i))),
          P i Kᵢ ∧ Nonempty ((S i).functor.obj Kᵢ ≅ K)) ∧
      (∀ (K₀ L₀ : DerivedCategory (ModuleCat.{max uR uA uM} A₀)),
        StacksDraft.PseudoCoherence.IsPseudoCoherent K₀ →
        HasFiniteTorDimension D₀.tensor D₀.comparison D₀.isLeftDerived
            ((ModuleCat.restrictScalars (algebraMap R₀ A₀)).mapDerivedCategory.obj L₀) →
        ∃ (H : I ⥤ Type (max uI uJ (max uR uA uM + 1)))
          (eH : ∀ i : I, H.obj i ≃ ((B i).obj K₀ ⟶ (B i).obj L₀))
          (s : Cocone H)
          (eTarget : s.pt ≃ (Blim.obj K₀ ⟶ Blim.obj L₀))
          (_hs : IsColimit s),
          (∀ {i j : I} (f : i ⟶ j) (x : H.obj i),
            let h : (stageMap F A₀ f).comp (b i) =
                b j := by
              ext a
              simp [b, liftBase, stageMap, baseToStageMap, Algebra.TensorProduct.includeRight_apply,
                Algebra.TensorProduct.map_tmul]
            let stageComp := comp (b i) (stageMap F A₀ f) ≪≫
              derivedExtensionScalarsCongr.{max uR uA, uM} h
            eH j (H.map f x) =
              stageComp.inv.app (W.obj K₀) ≫ (E (stageMap F A₀ f)).functor.map (eH i x) ≫
                stageComp.hom.app (W.obj L₀)) ∧
          (∀ (i : I) (g : (B i).obj K₀ ⟶ (B i).obj L₀),
            let h : (stageToLimitMap c A₀ i).comp (b i) =
                blim := by
              ext a
              simp [b, blim, liftBase, stageToLimitMap, baseToStageMap, baseToLimitMap,
                Algebra.TensorProduct.includeRight_apply, Algebra.TensorProduct.map_tmul]
            let limitComp := comp (b i) (stageToLimitMap c A₀ i) ≪≫
              derivedExtensionScalarsCongr.{max uR uA, uM} h
            eTarget (s.ι.app i ((eH i).symm g)) =
              limitComp.inv.app (W.obj K₀) ≫ (S i).functor.map g ≫ limitComp.hom.app (W.obj L₀))) ∧
      (∀ i : I, (P i).IsTriangulated) ∧ Plim.IsTriangulated ∧
      ∃ (G : I ⥤ Cat.{max uI uJ (max uR uA uM + 1), max uI uJ (max uR uA uM + 1)})
        (eG : ∀ i : I, G.obj i ≌ (P i).FullSubcategory)
        (transition : ∀ {i j : I} (f : i ⟶ j),
          (eG i).inverse ⋙ (G.map f).toFunctor ⋙ (eG j).functor ⋙
              ObjectProperty.ι (P j) ≅
            ObjectProperty.ι (P i) ⋙ (E (stageMap F A₀ f)).functor)
        (_transition_id : ∀ (i : I) (X : (P i).FullSubcategory),
          let mapIdIso : (G.map (𝟙 i)).toFunctor ≅ 𝟭 (G.obj i) :=
            eqToIso (congrArg Cat.Hom.toFunctor (G.map_id i))
          let h : RingHom.id (stageAlgebra F A₀ i) = stageMap F A₀ (𝟙 i) := by
            ext <;> simp [stageMap]
          ((eG i).functor ⋙ ObjectProperty.ι (P i)).map
                (mapIdIso.hom.app ((eG i).inverse.obj X)) ≫
              (ObjectProperty.ι (P i)).map ((eG i).counitIso.hom.app X) ≫
              (unit (stageAlgebra F A₀ i)).hom.app ((ObjectProperty.ι (P i)).obj X) ≫
              (derivedExtensionScalarsCongr.{max uR uA, uM} h).hom.app
                ((ObjectProperty.ι (P i)).obj X) =
            (transition (𝟙 i)).hom.app X)
        (_transition_comp : ∀ {i j k : I} (f : i ⟶ j) (g : j ⟶ k)
            (X : (P i).FullSubcategory),
          let mapCompIso : (G.map (f ≫ g)).toFunctor ≅
              (G.map f).toFunctor ⋙ (G.map g).toFunctor :=
            eqToIso (congrArg Cat.Hom.toFunctor (G.map_comp f g))
          let h : (stageMap F A₀ g).comp (stageMap F A₀ f) =
              stageMap F A₀ (f ≫ g) := by
            ext <;> simp [stageMap, Algebra.TensorProduct.map_tmul]
          let Z := (eG i).inverse.obj X
          let Y := (eG j).functor.obj ((G.map f).toFunctor.obj Z)
          ((eG k).functor ⋙ ObjectProperty.ι (P k)).map (mapCompIso.hom.app Z) ≫
              ((eG k).functor ⋙ ObjectProperty.ι (P k)).map
                ((G.map g).toFunctor.map
                  ((eG j).unitIso.hom.app ((G.map f).toFunctor.obj Z))) ≫
              (transition g).hom.app Y ≫
              (E (stageMap F A₀ g)).functor.map ((transition f).hom.app X) ≫
              (comp (stageMap F A₀ f) (stageMap F A₀ g)).hom.app
                ((ObjectProperty.ι (P i)).obj X) ≫
              (derivedExtensionScalarsCongr.{max uR uA, uM} h).hom.app
                ((ObjectProperty.ι (P i)).obj X) =
            (transition (f ≫ g)).hom.app X)
        (sG : Cocone G) (_hsG : IsColimit sG)
        (eLimit : sG.pt ≌ Plim.FullSubcategory)
        (leg : ∀ i : I,
          (eG i).inverse ⋙ (sG.ι.app i).toFunctor ⋙ eLimit.functor ⋙
                ObjectProperty.ι Plim ≅
            ObjectProperty.ι (P i) ⋙ (S i).functor),
        ∀ {i j : I} (f : i ⟶ j) (X : (P i).FullSubcategory),
          let mapCoconeIso : (G.map f).toFunctor ⋙ (sG.ι.app j).toFunctor ≅
              (sG.ι.app i).toFunctor :=
            eqToIso (congrArg Cat.Hom.toFunctor (sG.w f))
          let h : (stageToLimitMap c A₀ j).comp (stageMap F A₀ f) =
              stageToLimitMap c A₀ i := by
            ext x
            · simp [stageToLimitMap, stageMap]
            · simp [stageToLimitMap, stageMap]
          let limitComp := comp (stageMap F A₀ f) (stageToLimitMap c A₀ j) ≪≫
            derivedExtensionScalarsCongr.{max uR uA, uM} h
          let Z := (eG i).inverse.obj X
          let Y := (eG j).functor.obj ((G.map f).toFunctor.obj Z)
          ((eLimit.functor ⋙ ObjectProperty.ι Plim).map (mapCoconeIso.hom.app Z)) ≫
                (leg i).hom.app X =
            (((sG.ι.app j).toFunctor ⋙ eLimit.functor ⋙ ObjectProperty.ι Plim).map
                ((eG j).unitIso.hom.app ((G.map f).toFunctor.obj Z))) ≫
              (leg j).hom.app Y ≫
              (S j).functor.map ((transition f).hom.app X) ≫
              limitComp.hom.app ((ObjectProperty.ι (P i)).obj X)
```

## Tag 0DJG, a lemma

[Tag 0DJG](https://stacks.math.columbia.edu/tag/0DJG) in the Stacks Project.

**`PseudoCoherence.isRelativelyPerfect_of_derivedExtensionScalars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/RelativelyPerfect/Nilpotent.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/RelativelyPerfect/Nilpotent.lean#L206).

> **Stacks 0DJG.** Let `R' → A'` be a flat ring map of finite presentation, let `R' → R` be a
> surjective ring map whose kernel is a nilpotent ideal and set `A = A' ⊗[R'] R`. If the derived
> extension of scalars of `K' ∈ D(A')` to `A` is perfect relative to `R`, then `K'` is perfect
> relative to `R'`.

```lean
theorem isRelativelyPerfect_of_derivedExtensionScalars
    {R' A' R : Type u} [CommRing R'] [CommRing A'] [CommRing R]
    [Algebra R' A'] [Algebra R' R] [Module.Flat R' A']
    [Algebra.FinitePresentation R' A']
    (hsurj : Function.Surjective (algebraMap R' R))
    (hnil : IsNilpotent (RingHom.ker (algebraMap R' R)))
    (derivedTensorR' :
      DerivedCategory (ModuleCat.{u} R') ⥤
        DerivedCategory (ModuleCat.{u} R') ⥤ DerivedCategory (ModuleCat.{u} R'))
    (comparisonR' : ∀ M : ModuleCat.{u} R',
      DerivedCategory.Q ⋙
          derivedTensorR'.flip.obj ((DerivedCategory.singleFunctor (ModuleCat.{u} R') 0).obj M) ⟶
        (tensorModuleRight M).mapHomologicalComplex (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (isLeftDerivedR' : ∀ M : ModuleCat.{u} R',
      (derivedTensorR'.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R') 0).obj M)).IsLeftDerivedFunctor
        (comparisonR' M)
        (HomologicalComplex.quasiIso (ModuleCat.{u} R') (ComplexShape.up ℤ)))
    (derivedTensorR :
      DerivedCategory (ModuleCat.{u} R) ⥤
        DerivedCategory (ModuleCat.{u} R) ⥤ DerivedCategory (ModuleCat.{u} R))
    (comparisonR : ∀ M : ModuleCat.{u} R,
      DerivedCategory.Q ⋙
          derivedTensorR.flip.obj ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj M) ⟶
        (tensorModuleRight M).mapHomologicalComplex (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (isLeftDerivedR : ∀ M : ModuleCat.{u} R,
      (derivedTensorR.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj M)).IsLeftDerivedFunctor
        (comparisonR M)
        (HomologicalComplex.quasiIso (ModuleCat.{u} R) (ComplexShape.up ℤ)))
    (K' : DerivedCategory (ModuleCat.{u} A')) :
    let A := A' ⊗[R'] R
    let e : (R ⊗[R'] A') ≃ₐ[R] A :=
      AlgEquiv.ofRingEquiv (f := (Algebra.TensorProduct.comm R' R A').toRingEquiv)
        (fun r => by
          change (Algebra.TensorProduct.comm R' R A')
            (algebraMap R (R ⊗[R'] A') r) = _
          rw [Algebra.TensorProduct.algebraMap_apply, Algebra.algebraMap_self_apply,
            Algebra.TensorProduct.comm_tmul]
          rfl)
    letI : Module.Flat R A := Module.Flat.of_linearEquiv e.symm.toLinearEquiv
    letI : Algebra.FinitePresentation R A := Algebra.FinitePresentation.equiv e
    let f : A' →+* A := Algebra.TensorProduct.includeLeftRingHom
    IsRelativelyPerfect.{u, u, u} derivedTensorR comparisonR isLeftDerivedR
        ((totalDerivedExtensionScalars.{u, u, u} f).functor.obj K') →
      IsRelativelyPerfect.{u, u, u} derivedTensorR' comparisonR' isLeftDerivedR' K'
```

## Tag 0DJH, a lemma

[Tag 0DJH](https://stacks.math.columbia.edu/tag/0DJH) in the Stacks Project.

**`PseudoCoherence.hasTorAmplitude_localization_of_isZero_homology_fibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/RelativelyPerfect/Fibrewise.lean, line 334](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/RelativelyPerfect/Fibrewise.lean#L334).

> **Stacks 0DJH.** Let `A` be flat and of finite presentation over `R`, presented by `d`
> variables, let `q ⊂ A` be a prime lying over `p ⊂ R` and let `K ∈ D(A)` be pseudo-coherent. If the
> cohomology of `K_q ⊗ᴸ_{R_p} κ(p)` vanishes outside `[a, b]`, then `K_q` has Tor amplitude in
> `[a - d, b]` over `R`.

```lean
theorem hasTorAmplitude_localization_of_isZero_homology_fibre
    {R A : Type u} [CommRing R] [CommRing A] [Algebra R A]
    [Module.Flat R A] [Algebra.FinitePresentation R A]
    (d : ℕ) (presentation : MvPolynomial (Fin d) R →ₐ[R] A)
    (hpresentation : Function.Surjective presentation)
    (q : Ideal A) [q.IsPrime]
    (derivedTensor :
      DerivedCategory (ModuleCat.{u} R) ⥤
        DerivedCategory (ModuleCat.{u} R) ⥤ DerivedCategory (ModuleCat.{u} R))
    (comparison : ∀ N : ModuleCat.{u} R,
      DerivedCategory.Q ⋙
          derivedTensor.flip.obj ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj N) ⟶
        (tensorModuleRight N).mapHomologicalComplex (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (isLeftDerived : ∀ N : ModuleCat.{u} R,
      (derivedTensor.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj N)).IsLeftDerivedFunctor
        (comparison N) (HomologicalComplex.quasiIso (ModuleCat.{u} R) (ComplexShape.up ℤ)))
    (fibreTensor :
      DerivedCategory (ModuleCat.{u} (Localization.AtPrime (q.under R))) ⥤
        DerivedCategory (ModuleCat.{u} (Localization.AtPrime (q.under R))) ⥤
          DerivedCategory (ModuleCat.{u} (Localization.AtPrime (q.under R))))
    (fibreComparison : ∀ N : ModuleCat.{u} (Localization.AtPrime (q.under R)),
      DerivedCategory.Q ⋙
          fibreTensor.flip.obj
            ((DerivedCategory.singleFunctor
              (ModuleCat.{u} (Localization.AtPrime (q.under R))) 0).obj N) ⟶
        (tensorModuleRight N).mapHomologicalComplex (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (fibreIsLeftDerived : ∀ N : ModuleCat.{u} (Localization.AtPrime (q.under R)),
      (fibreTensor.flip.obj
          ((DerivedCategory.singleFunctor
            (ModuleCat.{u} (Localization.AtPrime (q.under R))) 0).obj N)).IsLeftDerivedFunctor
        (fibreComparison N)
        (HomologicalComplex.quasiIso
          (ModuleCat.{u} (Localization.AtPrime (q.under R))) (ComplexShape.up ℤ)))
    (K : DerivedCategory (ModuleCat.{u} A))
    (hK : StacksDraft.PseudoCoherence.IsPseudoCoherent K) (a b : ℤ)
    (hfibre : ∀ i : ℤ, i < a ∨ b < i →
      IsZero ((DerivedCategory.homologyFunctor
        (ModuleCat.{u} (Localization.AtPrime (q.under R))) i).obj
        ((fibreTensor.obj
          ((ModuleCat.restrictScalars
            (algebraMap (Localization.AtPrime (q.under R))
              (Localization.AtPrime q))).mapDerivedCategory.obj
            ((totalDerivedExtensionScalars
              (algebraMap A (Localization.AtPrime q))).functor.obj K))).obj
          ((DerivedCategory.singleFunctor
            (ModuleCat.{u} (Localization.AtPrime (q.under R))) 0).obj
              (ModuleCat.of (Localization.AtPrime (q.under R))
                (q.under R).ResidueField))))) :
    HasTorAmplitude derivedTensor comparison isLeftDerived
      ((ModuleCat.restrictScalars
        ((algebraMap A (Localization.AtPrime q)).comp
          (algebraMap R A))).mapDerivedCategory.obj
        ((totalDerivedExtensionScalars
          (algebraMap A (Localization.AtPrime q))).functor.obj K))
      (a - (d : ℤ)) b
```

## Tag 0GHJ, a lemma

[Tag 0GHJ](https://stacks.math.columbia.edu/tag/0GHJ) in the Stacks Project.

**`PseudoCoherence.isRelativelyPerfect_iff_isBoundedBelow_and_fibres_isBoundedBelow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/RelativelyPerfect/Criterion.lean, line 605](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/RelativelyPerfect/Criterion.lean#L605).

> **Stacks 0GHJ.** Let `R → A` be a flat ring map of finite presentation and let `K` be a
> pseudo-coherent object of `D(A)`. Then `K` is perfect relative to `R` if and only if `K` is
> bounded below and, for every prime `p` of `R`, the derived fibre `K ⊗_R^L κ(p)` is bounded
> below.

```lean
theorem isRelativelyPerfect_iff_isBoundedBelow_and_fibres_isBoundedBelow
    {R : Type u} {A : Type u} [CommRing R] [CommRing A] [Algebra R A]
    [Module.Flat R A] [Algebra.FinitePresentation R A]
    (derivedTensor :
      DerivedCategory (ModuleCat.{u} R) ⥤
        DerivedCategory (ModuleCat.{u} R) ⥤ DerivedCategory (ModuleCat.{u} R))
    (comparison : ∀ M : ModuleCat.{u} R,
      DerivedCategory.Q ⋙
          derivedTensor.flip.obj
            ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj M) ⟶
        (StacksDraft.TorAmplitude.tensorModuleRight M).mapHomologicalComplex
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (isLeftDerived : ∀ M : ModuleCat.{u} R,
      (derivedTensor.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj M)).IsLeftDerivedFunctor
        (comparison M)
        (HomologicalComplex.quasiIso (ModuleCat.{u} R) (ComplexShape.up ℤ)))
    (K : DerivedCategory (ModuleCat.{u} A))
    (hK : StacksDraft.PseudoCoherence.IsPseudoCoherent K) :
    IsRelativelyPerfect.{u, u, u} derivedTensor comparison isLeftDerived K ↔
      (∃ a : ℤ, K.IsGE a) ∧
        ∀ p : PrimeSpectrum R, ∃ a : ℤ,
          ((CochainComplex.DerivedExtensionScalars.totalDerivedExtensionScalars.{u, u, u}
              (algebraMap R p.asIdeal.ResidueField)).functor.obj
            ((ModuleCat.restrictScalars (algebraMap R A)).mapDerivedCategory.obj K)).IsGE a
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.85, Tag 0DHR](https://stacks.math.columbia.edu/tag/0DHR)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
