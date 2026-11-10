---
declaration: section
origin: cited
lean: Stacks.SheafOfModules.coherentDerivedComparison_mem, Stacks.SheafOfModules.coherentDerivedComparison, Stacks.SheafOfModules.coherentDerivedComparison_comp_inclusion, AlgebraicGeometry.coherentToQuasicoherentDerivedMinus, AlgebraicGeometry.coherentToQuasicoherentDerivedMinus_isEquivalence, AlgebraicGeometry.coherentToModulesDerivedMinus_isEquivalence, AlgebraicGeometry.coherentToModulesDerivedBounded_isEquivalence, Stacks.AlgebraicGeometry.ProperSupportCoherent.derivedCategoryBBounded_derivedPushforward_of_isProperOver_supp_unconditional
statement: formalized
proof: formalized
---

# 36.11 Derived category of coherent modules

Section 36.11 of the Stacks Project, [Tag 08E0](https://stacks.math.columbia.edu/tag/08E0). 9 tags here are carried by 23 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08E1, an equation

[Tag 08E1](https://stacks.math.columbia.edu/tag/08E1) in the Stacks Project.

**`Stacks.SheafOfModules.coherentDerivedComparison_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/CoherentDerivedCategory.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/CoherentDerivedCategory.lean#L78). The attribute's comment: “well-definedness”.

> **Stacks Project, Tag 08E1.** The derived inclusion of coherent modules has coherent
> cohomology in every degree.

```lean
theorem coherentDerivedComparison_mem
    {X : Type u} [TopologicalSpace X]
    (R : Sheaf (Opens.grothendieckTopology X) RingCat.{u}) :
    let P : ObjectProperty (_root_.SheafOfModules.{u} R) := fun M => IsCoherent M
    letI : Preadditive P.FullSubcategory := Abelian.toPreadditive
    letI : Preadditive (_root_.SheafOfModules.{u} R) := Abelian.toPreadditive
    let I : P.FullSubcategory ⥤ _root_.SheafOfModules.{u} R := P.ι
    letI : PreservesFiniteLimits I :=
      ObjectProperty.preservesFiniteLimits_ι_of_isWeakSerreClass P
    letI : PreservesFiniteColimits I :=
      ObjectProperty.preservesFiniteColimits_ι_of_isWeakSerreClass P
    letI : I.Additive := I.additive_of_preserves_binary_products
    ∀ K : DerivedCategory (CoherentModules R),
      (DerivedCategoryB.derivedCategoryB P) (I.mapDerivedCategory.obj K)
```

**`Stacks.SheafOfModules.coherentDerivedComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/CoherentDerivedCategory.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/CoherentDerivedCategory.lean#L111). The attribute's comment: “comparison functor”.

> **Stacks Project, Tag 08E1.** The canonical functor from the derived category of coherent
> modules to the subcategory of the derived category with coherent cohomology.

```lean
noncomputable def coherentDerivedComparison
    {X : Type u} [TopologicalSpace X]
    (R : Sheaf (Opens.grothendieckTopology X) RingCat.{u}) :
    DerivedCategory (CoherentModules R) ⥤
      (DerivedCategoryB.derivedCategoryB
        (fun M : _root_.SheafOfModules.{u} R => IsCoherent M)).FullSubcategory
```

**`Stacks.SheafOfModules.coherentDerivedComparison_comp_inclusion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/CoherentDerivedCategory.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/CoherentDerivedCategory.lean#L132). The attribute's comment: “canonical comparison”.

> **Stacks Project, Tag 08E1.** Forgetting the coherence condition after comparison gives the
> derived functor of the inclusion of coherent modules.

```lean
noncomputable def coherentDerivedComparison_comp_inclusion
    {X : Type u} [TopologicalSpace X]
    (R : Sheaf (Opens.grothendieckTopology X) RingCat.{u}) :
    let P : ObjectProperty (_root_.SheafOfModules.{u} R) := fun M => IsCoherent M
    letI : Preadditive P.FullSubcategory := Abelian.toPreadditive
    letI : Preadditive (_root_.SheafOfModules.{u} R) := Abelian.toPreadditive
    let I : P.FullSubcategory ⥤ _root_.SheafOfModules.{u} R := P.ι
    letI : PreservesFiniteLimits I :=
      ObjectProperty.preservesFiniteLimits_ι_of_isWeakSerreClass P
    letI : PreservesFiniteColimits I :=
      ObjectProperty.preservesFiniteColimits_ι_of_isWeakSerreClass P
    letI : I.Additive := I.additive_of_preserves_binary_products
    coherentDerivedComparison R ⋙ (DerivedCategoryB.derivedCategoryB P).ι ≅
      I.mapDerivedCategory
```

## Tag 0FDA, a lemma

[Tag 0FDA](https://stacks.math.columbia.edu/tag/0FDA) in the Stacks Project.

**`AlgebraicGeometry.coherentToQuasicoherentDerivedMinus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedCoherent/Basic.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedCoherent/Basic.lean#L249).

> **Stacks Project, Tag 0FDA.** The canonical functor
> `D⁻(Coh(𝒪_X)) ⥤ D⁻_Coh(QCoh(𝒪_X))` on a Noetherian scheme: the derived functor of the
> inclusion `Coh(𝒪_X) ⥤ QCoh(𝒪_X)`, restricted to the bounded above complexes and corestricted
> to the bounded above complexes with coherent cohomology, where it lands.

```lean
def coherentToQuasicoherentDerivedMinus [IsNoetherian X] :
    DerivedCategory.Minus (SheafOfModules.CoherentModules X.ringCatSheaf) ⥤
      (DerivedCategoryB.derivedCategoryBMinus (coherentInQuasicoherent X)).FullSubcategory
```

**`AlgebraicGeometry.coherentToQuasicoherentDerivedMinus_isEquivalence`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedCoherent/Basic.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedCoherent/Basic.lean#L293). References: SGA 6 II (2.2.2).

> **Stacks Project, Tag 0FDA.** On a Noetherian scheme the canonical functor
> `D⁻(Coh(𝒪_X)) ⥤ D⁻_Coh(QCoh(𝒪_X))` is an equivalence: the bounded above derived category of
> coherent modules is the full subcategory of the bounded above derived category of
> quasi-coherent modules whose objects have coherent cohomology.

```lean
instance coherentToQuasicoherentDerivedMinus_isEquivalence [IsNoetherian X] :
    (coherentToQuasicoherentDerivedMinus X).IsEquivalence
```

## Tag 0FDB, a proposition

[Tag 0FDB](https://stacks.math.columbia.edu/tag/0FDB) in the Stacks Project.

**`AlgebraicGeometry.coherentToModulesDerivedMinus_isEquivalence`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedCoherent/Modules.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedCoherent/Modules.lean#L306). The attribute's comment: “bounded above”. References: SGA 6 II (2.2.2.1), “more general”.

> **Stacks Project, Tag 0FDB.** On a Noetherian scheme the canonical functor
> `D⁻(Coh(𝒪_X)) ⥤ D⁻_Coh(𝒪_X)` is an equivalence: the bounded above derived category of the
> coherent `𝒪_X`-modules is the full subcategory of `D(𝒪_X)` of the complexes which are
> cohomologically bounded above with coherent cohomology sheaves.

```lean
instance coherentToModulesDerivedMinus_isEquivalence [IsNoetherian X] :
    (coherentToModulesDerivedMinus X).IsEquivalence
```

**`AlgebraicGeometry.coherentToModulesDerivedBounded_isEquivalence`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedCoherent/Modules.lean, line 418](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedCoherent/Modules.lean#L418). The attribute's comment: “bounded”. References: SGA 6 II (2.2.2.1).

> **Stacks Project, Tag 0FDB.** On a Noetherian scheme the canonical functor
> `D^b(Coh(𝒪_X)) ⥤ D^b_Coh(𝒪_X)` is an equivalence: the bounded derived category of the coherent
> `𝒪_X`-modules is the full subcategory of `D(𝒪_X)` of the complexes which are cohomologically
> bounded with coherent cohomology sheaves.

```lean
instance coherentToModulesDerivedBounded_isEquivalence [IsNoetherian X] :
    (coherentToModulesDerivedBounded X).IsEquivalence
```

## Tag 08E2, a lemma

[Tag 08E2](https://stacks.math.columbia.edu/tag/08E2) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProperSupportCoherent.derivedCategoryBBounded_derivedPushforward_of_isProperOver_supp_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProperSupportCoherent/DerivedDirectImageSupplement.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProperSupportCoherent/DerivedDirectImageSupplement.lean#L80). References: EGA II (7.3.12), “special case”; EGA III (6.2.5), “special case”; SGA 6 III (2.2.1), “special case”; SGA 6 XIV (2.3), “special case”.

> **[Stacks, Tag 08E2].** Let `S` be a Noetherian scheme, `f : X ⟶ S` locally of finite type
> and `E` a bounded object of `D(𝒪_X)` whose cohomology sheaves are coherent with support proper
> over `S`. Then `Rf_*E` is an object of `D^b_Coh(𝒪_S)`.
>
> The dévissage is applied to the window `[a, b]` of `E`; at each cohomology sheaf of `E` its
> hypothesis is `hasCoherentBoundedDirectImages_of_isProperOver_supp_unconditional`, this library's
> form of [Stacks, Tag 08DS] together with the uniform vanishing of [Stacks, Tag 01XJ].

```lean
theorem derivedCategoryBBounded_derivedPushforward_of_isProperOver_supp_unconditional
    [IsNoetherian S] [LocallyOfFiniteType f] (E : DerivedCategory X.Modules)
    (hcoh : ∀ j : ℤ, ((DerivedCategory.homologyFunctor X.Modules j).obj E).IsCoherent)
    (hsupp : ∀ j : ℤ, IsProperOver f
      ⟨SheafOfModules.supp ((DerivedCategory.homologyFunctor X.Modules j).obj E),
        @SheafOfModules.isClosed_supp _ _ _ (hcoh j).isFiniteType⟩)
    (a b : ℤ) (hGE : E.IsGE a) (hLE : E.IsLE b) :
    DerivedCategoryB.derivedCategoryBBounded (fun N : S.Modules => N.IsCoherent)
      ((derivedPushforwardModules f).obj E)
```

**`Stacks.AlgebraicGeometry.ProperSupportCoherent.derivedCategoryBBounded_derivedPushforward_of_properSupp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProperSupportCoherent/DerivedDirectImageUnconditional.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProperSupportCoherent/DerivedDirectImageUnconditional.lean#L76). References: EGA III (3.2.1), “Noetherian target”; EGA III (3.2.4), “special case”; EGA III (4.1.10), “more general”; SGA 6 0 (3.1), “partial”; SGA 6 III (2.2.1), “special case”.

> **[Stacks, Tag 08E2].** Let `S` be a Noetherian scheme, let `f : X ⟶ S` be locally of finite
> type and let `E` be a bounded object of `D(𝒪_X)` whose cohomology sheaves are coherent with
> support proper over `S`. Then `Rf_*E` is an object of `D^b_Coh(𝒪_S)`.
>
> The dévissage `derivedCategoryBBounded_derivedPushforward_of_isProperOver_supp` asks for
> [Stacks, Tag 02O5] in the affine-base form
> `AlgebraicGeometry.ProperCoherentImage.HigherDirectImageIsCoherentOverAffineBase`, which
> `AlgebraicGeometry.ProperCoherenceWitness.higherDirectImageIsCoherentOverAffineBase` supplies.

```lean
theorem derivedCategoryBBounded_derivedPushforward_of_properSupp {X S : Scheme.{u}} (f : X ⟶ S)
    [IsNoetherian S] [LocallyOfFiniteType f] (E : DerivedCategory X.Modules)
    (hcoh : ∀ j : ℤ, ((DerivedCategory.homologyFunctor X.Modules j).obj E).IsCoherent)
    (hsupp : ∀ j : ℤ, IsProperOver f
      ⟨SheafOfModules.supp ((DerivedCategory.homologyFunctor X.Modules j).obj E),
        @SheafOfModules.isClosed_supp _ _ _ (hcoh j).isFiniteType⟩)
    (a b : ℤ) (hGE : E.IsGE a) (hLE : E.IsLE b) :
    DerivedCategoryB.derivedCategoryBBounded (fun N : S.Modules => N.IsCoherent)
      ((derivedPushforwardModules f).obj E)
```

**`Stacks.AlgebraicGeometry.ProperSupportCoherent.derivedCategoryBBounded_derivedPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProperSupportCoherent/UnconditionalBounded.lean, line 39](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProperSupportCoherent/UnconditionalBounded.lean#L39).

> **[Stacks, Tag 08E2].** Let `S` be a Noetherian scheme, `f : X ⟶ S` locally of finite type
> and `E` an object of `D^b_Coh(𝒪_X)` such that the support of `H^i(E)` is proper over `S` for all
> `i`. Then `Rf_*E` is an object of `D^b_Coh(𝒪_S)`.

```lean
theorem derivedCategoryBBounded_derivedPushforward [IsNoetherian S]
    (E : DerivedCategory X.Modules)
    (hcoh : ∀ j : ℤ, ((DerivedCategory.homologyFunctor X.Modules j).obj E).IsCoherent)
    (hsupp : ∀ j : ℤ, IsProperOver f
      ⟨SheafOfModules.supp ((DerivedCategory.homologyFunctor X.Modules j).obj E),
        @SheafOfModules.isClosed_supp _ _ _ (hcoh j).isFiniteType⟩)
    (a b : ℤ) (hGE : E.IsGE a) (hLE : E.IsLE b) :
    DerivedCategoryB.derivedCategoryBBounded (fun N : S.Modules => N.IsCoherent)
      ((derivedPushforwardModules f).obj E)
```

## Tag 0D0B, a lemma

[Tag 0D0B](https://stacks.math.columbia.edu/tag/0D0B) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProperSupportCoherent.derivedCategoryBPlus_derivedPushforward_of_properSupp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProperSupportCoherent/BoundedBelowUnconditional.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProperSupportCoherent/BoundedBelowUnconditional.lean#L96). References: EGA III (3.2.1), “Noetherian target”; EGA III (3.2.4), “special case”; EGA III (4.1.10), “more general”.

> **[Stacks, Tag 0D0B].** Let `S` be a Noetherian scheme, let `f : X ⟶ S` be a morphism of
> schemes which is locally of finite type and let `E` be an object of `D^+_Coh(𝒪_X)` such that the
> support of `H^i(E)` is proper over `S` for all `i`. Then `Rf_*E` is an object of `D^+_Coh(𝒪_S)`.
>
> This is `derivedCategoryBPlus_derivedPushforward_of_isProperOver_supp` with its appeal to
> [Stacks, Tag 02O5] supplied by
> `AlgebraicGeometry.ProperCoherenceWitness.higherDirectImageIsCoherentOverAffineBase`, a
> theorem.

```lean
theorem derivedCategoryBPlus_derivedPushforward_of_properSupp [IsNoetherian S]
    [LocallyOfFiniteType f] (E : DerivedCategory X.Modules)
    (hE : DerivedCategoryB.derivedCategoryBPlus (fun M : X.Modules => M.IsCoherent) E)
    (hsupp : ∀ j : ℤ, IsProperOver f
      ⟨SheafOfModules.supp ((DerivedCategory.homologyFunctor X.Modules j).obj E),
        @SheafOfModules.isClosed_supp _ _ _ (hE.2 j).isFiniteType⟩) :
    DerivedCategoryB.derivedCategoryBPlus (fun N : S.Modules => N.IsCoherent)
      ((derivedPushforwardModules f).obj E)
```

## Tag 0D0C, a lemma

[Tag 0D0C](https://stacks.math.columbia.edu/tag/0D0C) in the Stacks Project.

**`AlgebraicGeometry.derivedCategoryBPlus_coherent_affineDerivedSheafHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffineCoherentDerivedHom.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffineCoherentDerivedHom.lean#L240). The attribute's comment: “the coherence clause on Spec R, for sheafified D⁻_Coh and D⁺_Coh arguments”.

> **The coherence clause of [Stacks, Tag 0D0C] on an affine scheme.** Let `R` be a Noetherian
> ring, let `K` be an object of `D⁻_Coh(R)` and `L` an object of `D⁺_Coh(R)`. Then
> `R𝓗om_{𝒪_{Spec R}}(K̃, L̃)` lies in `D⁺_Coh(𝒪_{Spec R})`: it is cohomologically bounded below and
> all of its cohomology sheaves are coherent.
>
> Boundedness below is `Stacks.SheafOfModules.isBoundedBelow_derivedSheafHom`, the clause of the
> tag the library already carries, applied after transporting the bounds of `K` and `L` to their
> sheafifications. Coherence is `isCoherent_homology_affineDerivedSheafHom`.
>
> The hypotheses are on the module-level objects `K` and `L`; the source states the tag for objects
> of `D⁻_Coh(𝒪_X)` and `D⁺_Coh(𝒪_X)` on an arbitrary locally Noetherian `X`, and neither the
> reduction to an affine open nor the identification of a sheaf-level coherent complex with a
> sheafification ([Stacks, Tag 06Z0]) is carried out here; see the module documentation.

```lean
theorem derivedCategoryBPlus_coherent_affineDerivedSheafHom [IsNoetherianRing R]
    (K L : DerivedCategory (ModuleCat.{u} R))
    (hK : DerivedCategoryB.derivedCategoryBMinus
      (fun M : ModuleCat.{u} R => Module.Finite R M) K)
    (hL : DerivedCategoryB.derivedCategoryBPlus
      (fun M : ModuleCat.{u} R => Module.Finite R M) L) :
    DerivedCategoryB.derivedCategoryBPlus (A := (Spec R).Modules)
      (Stacks.SheafOfModules.coherentModules (Spec R).ringCatSheaf)
      (((Stacks.SheafOfModules.derivedSheafHom (Spec R).sheaf).obj
          (op ((tilde.functor R).mapDerivedCategory.obj K))).obj
            ((tilde.functor R).mapDerivedCategory.obj L))
```

**`AlgebraicGeometry.derivedCategoryBPlus_isCoherent_derivedSheafHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/SchemeCoherentDerivedHom.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/SchemeCoherentDerivedHom.lean#L336).

> **Stacks Project, Tag 0D0C.** Let `X` be a locally Noetherian scheme, `K` an object of
> `D⁻_Coh(𝒪_X)` and `L` an object of `D⁺_Coh(𝒪_X)`. Then `R𝓗om_{𝒪_X}(K, L)` lies in
> `D⁺_Coh(𝒪_X)`.
>
> Boundedness below is `Stacks.SheafOfModules.isBoundedBelow_derivedSheafHom`, which needs only the
> two cohomological bounds; coherence of the cohomology sheaves is
> `isCoherent_homology_derivedSheafHom`.

```lean
theorem derivedCategoryBPlus_isCoherent_derivedSheafHom (Y : Scheme.{u})
    [IsLocallyNoetherian Y] (E F : DerivedCategory Y.Modules)
    (hE : DerivedCategoryB.derivedCategoryBMinus
      (Stacks.SheafOfModules.coherentModules Y.ringCatSheaf) E)
    (hF : DerivedCategoryB.derivedCategoryBPlus
      (Stacks.SheafOfModules.coherentModules Y.ringCatSheaf) F) :
    DerivedCategoryB.derivedCategoryBPlus
      (Stacks.SheafOfModules.coherentModules Y.ringCatSheaf)
      (((Stacks.SheafOfModules.derivedSheafHom Y.sheaf).obj (op E)).obj F)
```

**`Stacks.SheafOfModules.isBoundedBelow_derivedSheafHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedBoundedBelow.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedBoundedBelow.lean#L120). The attribute's comment: “the boundedness clause, on an arbitrary ringed space and with no coherence or Noetherian hypothesis; the coherence clause is not carried”.

> **The derived internal Hom of a bounded-above complex into a bounded-below complex is
> cohomologically bounded below.** If `K` is bounded above and `L` is bounded below, then
> `RSheafHom(K, L)` is bounded below, on an arbitrary ringed space.

```lean
public theorem isBoundedBelow_derivedSheafHom
    (K L : DerivedCategory (StructureSheafModules Rc))
    (hK : DerivedCategoryB.IsBoundedAbove K) (hL : DerivedCategoryB.IsBoundedBelow L) :
    DerivedCategoryB.IsBoundedBelow (((derivedSheafHom Rc).obj (op K)).obj L)
```

## Tag 0FXU, a lemma

[Tag 0FXU](https://stacks.math.columbia.edu/tag/0FXU) in the Stacks Project.

**`Stacks.AlgebraicGeometry.PerfectCohomology.isBoundedCoherent_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PseudoCoherentComplex/PerfectBoundedCoherent.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/PseudoCoherentComplex/PerfectBoundedCoherent.lean#L47). The attribute's comment: “perfect_bounded_coherent”.

> **A perfect derived object on a Noetherian scheme has bounded coherent cohomology.**

```lean
theorem isBoundedCoherent_of_isPerfect
    (X : Scheme.{u}) [IsNoetherian X]
    [HasDerivedCategory.{d} (StrictlyPerfect.OXMod.{u, u} X.toRingedSpace)]
    (K : DerivedCategory (StrictlyPerfect.OXMod.{u, u} X.toRingedSpace))
    (hK : RingedSpace.IsPerfect (X := X.toRingedSpace) K) :
    DerivedCategoryB.derivedCategoryBBounded
      (fun M : StrictlyPerfect.OXMod.{u, u} X.toRingedSpace => M.IsCoherent) K
```

**`Stacks.AlgebraicGeometry.PerfectCohomology.derivedCategoryB_coherent_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PseudoCoherentComplex/PerfectTensorInternalHom.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/PseudoCoherentComplex/PerfectTensorInternalHom.lean#L337). The attribute's comment: “part (2): for L in D_Coh(𝒪_X) both E ⊗^𝐋 L and R𝓗om(E, L) are in D_Coh(𝒪_X)”.

> **[Stacks, Tag 0FXU], part (2).** Let `X` be a Noetherian scheme and let `E` in `D(𝒪_X)` be
> perfect. If `L` is in `D_Coh(𝒪_X)` then `E ⊗^𝐋_{𝒪_X} L` and `R𝓗om_{𝒪_X}(E, L)` are in
> `D_Coh(𝒪_X)`.

```lean
theorem derivedCategoryB_coherent_of_isPerfect [IsNoetherian X]
    (E L : DerivedCategory (StrictlyPerfect.OXMod.{u, u} X.toRingedSpace))
    (hE : RingedSpace.IsPerfect (X := X.toRingedSpace) E)
    (hL : DerivedCategoryB.derivedCategoryB
      (fun M : StrictlyPerfect.OXMod.{u, u} X.toRingedSpace => M.IsCoherent) L) :
    DerivedCategoryB.derivedCategoryB
        (fun M : StrictlyPerfect.OXMod.{u, u} X.toRingedSpace => M.IsCoherent)
        (derivedTensorObj X E L) ∧
      DerivedCategoryB.derivedCategoryB
        (fun M : StrictlyPerfect.OXMod.{u, u} X.toRingedSpace => M.IsCoherent)
        (derivedSheafHomObj X E L)
```

**`Stacks.AlgebraicGeometry.PerfectCohomology.derivedCategoryBBounded_coherent_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PseudoCoherentComplex/PerfectTensorInternalHom.lean, line 356](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/PseudoCoherentComplex/PerfectTensorInternalHom.lean#L356). The attribute's comment: “part (3): for L in D^b_Coh(𝒪_X) both E ⊗^𝐋 L and R𝓗om(E, L) are in D^b_Coh(𝒪_X)”.

> **[Stacks, Tag 0FXU], part (3).** Let `X` be a Noetherian scheme and let `E` in `D(𝒪_X)` be
> perfect. If `L` is in `D^b_Coh(𝒪_X)` then `E ⊗^𝐋_{𝒪_X} L` and `R𝓗om_{𝒪_X}(E, L)` are in
> `D^b_Coh(𝒪_X)`.

```lean
theorem derivedCategoryBBounded_coherent_of_isPerfect [IsNoetherian X]
    (E L : DerivedCategory (StrictlyPerfect.OXMod.{u, u} X.toRingedSpace))
    (hE : RingedSpace.IsPerfect (X := X.toRingedSpace) E)
    (hL : DerivedCategoryB.derivedCategoryBBounded
      (fun M : StrictlyPerfect.OXMod.{u, u} X.toRingedSpace => M.IsCoherent) L) :
    DerivedCategoryB.derivedCategoryBBounded
        (fun M : StrictlyPerfect.OXMod.{u, u} X.toRingedSpace => M.IsCoherent)
        (derivedTensorObj X E L) ∧
      DerivedCategoryB.derivedCategoryBBounded
        (fun M : StrictlyPerfect.OXMod.{u, u} X.toRingedSpace => M.IsCoherent)
        (derivedSheafHomObj X E L)
```

**`Stacks.AlgebraicGeometry.PerfectCohomology.derivedCategoryBPlus_coherent_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PseudoCoherentComplex/PerfectTensorInternalHom.lean, line 379](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/PseudoCoherentComplex/PerfectTensorInternalHom.lean#L379). The attribute's comment: “part (4): for L in D^+_Coh(𝒪_X) both E ⊗^𝐋 L and R𝓗om(E, L) are in D^+_Coh(𝒪_X)”.

> **[Stacks, Tag 0FXU], part (4).** Let `X` be a Noetherian scheme and let `E` in `D(𝒪_X)` be
> perfect. If `L` is in `D^+_Coh(𝒪_X)` then `E ⊗^𝐋_{𝒪_X} L` and `R𝓗om_{𝒪_X}(E, L)` are in
> `D^+_Coh(𝒪_X)`.

```lean
theorem derivedCategoryBPlus_coherent_of_isPerfect [IsNoetherian X]
    (E L : DerivedCategory (StrictlyPerfect.OXMod.{u, u} X.toRingedSpace))
    (hE : RingedSpace.IsPerfect (X := X.toRingedSpace) E)
    (hL : DerivedCategoryB.derivedCategoryBPlus
      (fun M : StrictlyPerfect.OXMod.{u, u} X.toRingedSpace => M.IsCoherent) L) :
    DerivedCategoryB.derivedCategoryBPlus
        (fun M : StrictlyPerfect.OXMod.{u, u} X.toRingedSpace => M.IsCoherent)
        (derivedTensorObj X E L) ∧
      DerivedCategoryB.derivedCategoryBPlus
        (fun M : StrictlyPerfect.OXMod.{u, u} X.toRingedSpace => M.IsCoherent)
        (derivedSheafHomObj X E L)
```

**`Stacks.AlgebraicGeometry.PerfectCohomology.derivedCategoryBMinus_coherent_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PseudoCoherentComplex/PerfectTensorInternalHom.lean, line 400](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/PseudoCoherentComplex/PerfectTensorInternalHom.lean#L400). The attribute's comment: “part (5): for L in D^-_Coh(𝒪_X) both E ⊗^𝐋 L and R𝓗om(E, L) are in D^-_Coh(𝒪_X)”.

> **[Stacks, Tag 0FXU], part (5).** Let `X` be a Noetherian scheme and let `E` in `D(𝒪_X)` be
> perfect. If `L` is in `D^-_Coh(𝒪_X)` then `E ⊗^𝐋_{𝒪_X} L` and `R𝓗om_{𝒪_X}(E, L)` are in
> `D^-_Coh(𝒪_X)`.

```lean
theorem derivedCategoryBMinus_coherent_of_isPerfect [IsNoetherian X]
    (E L : DerivedCategory (StrictlyPerfect.OXMod.{u, u} X.toRingedSpace))
    (hE : RingedSpace.IsPerfect (X := X.toRingedSpace) E)
    (hL : DerivedCategoryB.derivedCategoryBMinus
      (fun M : StrictlyPerfect.OXMod.{u, u} X.toRingedSpace => M.IsCoherent) L) :
    DerivedCategoryB.derivedCategoryBMinus
        (fun M : StrictlyPerfect.OXMod.{u, u} X.toRingedSpace => M.IsCoherent)
        (derivedTensorObj X E L) ∧
      DerivedCategoryB.derivedCategoryBMinus
        (fun M : StrictlyPerfect.OXMod.{u, u} X.toRingedSpace => M.IsCoherent)
        (derivedSheafHomObj X E L)
```

## Tag 0D0D, a lemma

[Tag 0D0D](https://stacks.math.columbia.edu/tag/0D0D) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProperSupportCoherent.moduleFinite_ext_of_proper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProperSupportCoherent/ExtFinitenessUnconditional.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProperSupportCoherent/ExtFinitenessUnconditional.lean#L259).

> **Stacks Project, Tag 0D0D.** Let `A` be a Noetherian ring, let `X` be a scheme proper over
> `A`, let `K` be an object of `D^-_Coh(𝒪_X)` and let `L` be an object of `D^+_Coh(𝒪_X)`. Then the
> `A`-module `Ext^n_{𝒪_X}(K, L)` is finite, for every `n`, the `A`-action being the canonical one
> induced by the structure morphism `X ⟶ Spec A`.
>
> `Ext^n_{𝒪_X}(K, L)` is `Hom_{D(𝒪_X)}(K, L⟦n⟧)`, which is the degree-zero cohomology of
> `RΓ(X, R𝓗om(K, L⟦n⟧))` as an `A`-module by `extLinearEquiv`, that is by [Stacks, Tag 08DK];
> `R𝓗om(K, L⟦n⟧)` is an object of `D^+_Coh(𝒪_X)` by [Stacks, Tag 0D0C], the shift of `L` being one
> by `derivedCategoryBPlus_isCoherent_shift`; and
> `moduleFinite_homologyZero_derivedGlobalSections_of_proper` makes the degree-zero
> hypercohomology of such an object a finite `A`-module.

```lean
theorem moduleFinite_ext_of_proper {A : Type u} [CommRing A] [IsNoetherianRing A]
    (X : Over (Spec (CommRingCat.of A))) [IsProper X.hom]
    (K L : DerivedCategory X.left.Modules)
    (hK : DerivedCategoryB.derivedCategoryBMinus
      (fun M : X.left.Modules => M.IsCoherent) K)
    (hL : DerivedCategoryB.derivedCategoryBPlus
      (fun M : X.left.Modules => M.IsCoherent) L)
    (n : ℤ) :
    letI : Linear A X.left.Modules := modulesLinear A X
    Module.Finite A (DerivedCategory.Ext K L n)
```

## Tag 0FDC, a lemma

[Tag 0FDC](https://stacks.math.columbia.edu/tag/0FDC) in the Stacks Project.

**`Stacks.AlgebraicGeometry.PerfectCohomology.isBoundedCoherent_of_isPerfect_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PseudoCoherentComplex/RegularPerfect.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/PseudoCoherentComplex/RegularPerfect.lean#L79). The attribute's comment: “converse direction only: a perfect object on a quasi-compact regular scheme is bounded with coherent cohomology”.

> **The converse half of [Stacks, Tag 0FDC].** Let `X` be a regular scheme which is
> quasi-compact — equivalently, Noetherian and regular. Then every perfect object of the derived
> category of `𝒪_X`-modules lies in `D^b_{Coh}(𝒪_X)`: it is bounded and all of its cohomology
> sheaves are coherent.
>
> Regularity enters only through local Noetherianity, so this is
> `Stacks.AlgebraicGeometry.PerfectCohomology.isBoundedCoherent_of_isPerfect`
> ([Stacks, Tag 0FXU]) read at the hypotheses of [Stacks, Tag 0FDC].

```lean
theorem isBoundedCoherent_of_isPerfect_of_isRegular
    (X : Scheme.{u}) (hX : IsRegular X) [CompactSpace X]
    [HasDerivedCategory.{d} (StrictlyPerfect.OXMod.{u, u} X.toRingedSpace)]
    (K : DerivedCategory (StrictlyPerfect.OXMod.{u, u} X.toRingedSpace))
    (hK : RingedSpace.IsPerfect (X := X.toRingedSpace) K) :
    DerivedCategoryB.derivedCategoryBBounded
      (fun M : StrictlyPerfect.OXMod.{u, u} X.toRingedSpace => M.IsCoherent) K
```

**`Stacks.AlgebraicGeometry.PerfectCohomology.isPerfect_of_isBoundedCoherent_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RegularBoundedCoherentPerfect.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RegularBoundedCoherentPerfect.lean#L241). The attribute's comment: “forward direction: a bounded object with coherent cohomology on a regular scheme is perfect”.

> **The forward half of [Stacks, Tag 0FDC].** Let `X` be a regular scheme. Then every object of
> `D^b_{Coh}(𝒪_X)` — every object of the derived category of `𝒪_X`-modules which is bounded and all
> of whose cohomology sheaves are coherent — is perfect.
>
> Quasi-compactness of `X` is not assumed. The proof is an induction on the length of the interval
> carrying the cohomology of the object, with
> `AlgebraicGeometry.isPerfect_single_of_isCoherent_of_isRegular` as its base case; that statement
> needs no quasi-compactness either.

```lean
theorem isPerfect_of_isBoundedCoherent_of_isRegular {X : Scheme.{u}} (hX : IsRegular X)
    [HasDerivedCategory.{d} (StrictlyPerfect.OXMod.{u, u} X.toRingedSpace)]
    (K : DerivedCategory (StrictlyPerfect.OXMod.{u, u} X.toRingedSpace))
    (hK : DerivedCategoryB.derivedCategoryBBounded
      (fun M : StrictlyPerfect.OXMod.{u, u} X.toRingedSpace => M.IsCoherent) K) :
    RingedSpace.IsPerfect (X := X.toRingedSpace) K
```

**`Stacks.AlgebraicGeometry.PerfectCohomology.isPerfect_iff_isBoundedCoherent_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RegularBoundedCoherentPerfect.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/RegularBoundedCoherentPerfect.lean#L262). The attribute's comment: “the equivalence, on a quasi-compact regular scheme”.

> **[Stacks, Tag 0FDC].** Let `X` be a quasi-compact regular scheme — equivalently, a
> Noetherian regular scheme. Then the perfect objects of the derived category of `𝒪_X`-modules are
> exactly the objects of `D^b_{Coh}(𝒪_X)`.
>
> The forward implication is
> `Stacks.AlgebraicGeometry.PerfectCohomology.isPerfect_of_isBoundedCoherent_of_isRegular`, which
> does not use quasi-compactness; the converse is
> `Stacks.AlgebraicGeometry.PerfectCohomology.isBoundedCoherent_of_isPerfect_of_isRegular`, which
> does.

```lean
theorem isPerfect_iff_isBoundedCoherent_of_isRegular {X : Scheme.{u}} (hX : IsRegular X)
    [CompactSpace X]
    [HasDerivedCategory.{d} (StrictlyPerfect.OXMod.{u, u} X.toRingedSpace)]
    (K : DerivedCategory (StrictlyPerfect.OXMod.{u, u} X.toRingedSpace)) :
    RingedSpace.IsPerfect (X := X.toRingedSpace) K ↔
      DerivedCategoryB.derivedCategoryBBounded
        (fun M : StrictlyPerfect.OXMod.{u, u} X.toRingedSpace => M.IsCoherent) K
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.11, Tag 08E0](https://stacks.math.columbia.edu/tag/08E0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
