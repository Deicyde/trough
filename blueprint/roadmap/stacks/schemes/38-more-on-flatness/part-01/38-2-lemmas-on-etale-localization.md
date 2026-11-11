---
declaration: section
origin: cited
lean: Stacks.Etale.exists_etale_lift_of_isClosedImmersion, AlgebraicGeometry.etale_stalkBaseChangeMap, AlgebraicGeometry.isFlatOverAt_comp_iff_of_etale, AlgebraicGeometry.isFlatOver_comp_iff_of_etale, AlgebraicGeometry.flat_stalk_iff_of_etale, flat_tfae_henselization, flat_tfae_baseChange_henselization, flat_tfae_iteratedBaseChange_henselization
statement: formalized
proof: formalized
---

# 38.2 Lemmas on étale localization

Section 38.2 of the Stacks Project, [Tag 05FM](https://stacks.math.columbia.edu/tag/05FM). 9 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 057R, a lemma

[Tag 057R](https://stacks.math.columbia.edu/tag/057R) in the Stacks Project.

**`Stacks.Etale.exists_etale_lift_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/LiftAcrossClosedImmersion.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/LiftAcrossClosedImmersion.lean#L138).

> Let `Z → X` be a closed immersion of affine schemes and let `Z' → Z` be an
> étale morphism with affine source. Then it is the pullback of an étale morphism
> `X' → X` with affine source.

```lean
theorem exists_etale_lift_of_isClosedImmersion
    {Z X Z' : AlgebraicGeometry.Scheme.{u}} (i : Z ⟶ X) (p : Z' ⟶ Z)
    [AlgebraicGeometry.IsAffine Z] [AlgebraicGeometry.IsAffine X]
    [AlgebraicGeometry.IsAffine Z'] [AlgebraicGeometry.IsClosedImmersion i]
    [AlgebraicGeometry.Etale p] :
    ∃ (X' : AlgebraicGeometry.Scheme.{u}) (f : X' ⟶ X),
      AlgebraicGeometry.IsAffine X' ∧ AlgebraicGeometry.Etale f ∧
        ∃ e : Z' ≅ pullback i f, e.hom ≫ pullback.fst i f = p
```

## Tag 05H2, a lemma

[Tag 05H2](https://stacks.math.columbia.edu/tag/05H2) in the Stacks Project.

**`AlgebraicGeometry.etale_stalkBaseChangeMap`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/EtaleBaseChange.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/EtaleBaseChange.lean#L94).

> **Stacks Project, Tag 05H2.** The morphism between the base changes to the spectrum of a
> local ring, induced by a commutative square with étale horizontal morphisms, is étale.

```lean
lemma etale_stalkBaseChangeMap (f' : X' ⟶ S') (g' : X' ⟶ X)
    (g : S' ⟶ S) (f : X ⟶ S) (h : g' ≫ f = f' ≫ g) (s' : S')
    [Etale g'] [Etale g] : Etale (stalkBaseChangeMap f' g' g f h s')
```

## Tag 05B9, a lemma

[Tag 05B9](https://stacks.math.columbia.edu/tag/05B9) in the Stacks Project.

**`AlgebraicGeometry.isFlatOverAt_comp_iff_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/EtaleBase.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/EtaleBase.lean#L101). The attribute's comment: “pointwise statement”.

> Flatness of a quasi-coherent module at a point is unchanged when the base
> is replaced by an étale intermediate scheme.

```lean
public theorem isFlatOverAt_comp_iff_of_etale [Etale g] (x : X) :
    AlgebraicGeometry.IsFlatOverAt (f ≫ g).toLRSHom.toShHom F x ↔
      AlgebraicGeometry.IsFlatOverAt f.toLRSHom.toShHom F x
```

**`AlgebraicGeometry.isFlatOver_comp_iff_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/EtaleBase.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/EtaleBase.lean#L149). The attribute's comment: “global statement”.

> A quasi-coherent module is flat over the base if and only if it is flat
> over an étale intermediate scheme.

```lean
public theorem isFlatOver_comp_iff_of_etale [Etale g] :
    AlgebraicGeometry.IsFlatOver (f ≫ g).toLRSHom.toShHom F ↔
      AlgebraicGeometry.IsFlatOver f.toLRSHom.toShHom F
```

## Tag 05BA, a lemma

[Tag 05BA](https://stacks.math.columbia.edu/tag/05BA) in the Stacks Project.

**`AlgebraicGeometry.flat_stalk_iff_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/EtaleStalk.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/EtaleStalk.lean#L73).

> Let `f : T ⟶ S` be étale, let `t : T` and let `M` be a module over `𝒪_{T,t}`. Then `M` is
> flat over `𝒪_{S,f(t)}`, acting through the map of local rings, if and only if it is flat over
> `𝒪_{T,t}`.

```lean
theorem flat_stalk_iff_of_etale [Etale f] (t : T) (M : Type*) [AddCommGroup M]
    [Module (T.presheaf.stalk t) M] :
    letI : Module (S.presheaf.stalk (f t)) M := Module.compHom M (f.stalkMap t).hom
    Module.Flat (S.presheaf.stalk (f t)) M ↔ Module.Flat (T.presheaf.stalk t) M
```

## Tag 05VL, a lemma

[Tag 05VL](https://stacks.math.columbia.edu/tag/05VL) in the Stacks Project.

**`flat_tfae_henselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/EtaleLocalization/FlatHenselization.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/EtaleLocalization/FlatHenselization.lean#L133). The attribute's comment: “conditions (1)--(3)”. References: SGA 4 VIII (4.1), “more general”; SGA 4 VIII (4.4), “more general”; SGA 4 XVII (5.5.29), “Flatness clause”.

> **Stacks Project, Tag 05VL, conditions (1)--(3).** A module over a henselization with
> extended residue field is flat over the original local ring if and only if it is flat over the
> henselization with unchanged residue field, if and only if it is flat over the
> extended-residue-field henselization. A strict henselization is the case where `K` is a separable
> closure of the residue field.

```lean
theorem flat_tfae_henselization {Msh : Type y} [AddCommGroup Msh] [Module Rsh Msh] :
    letI : Module Rh Msh := Module.compHom Msh (algebraMap Rh Rsh)
    letI : Module R Msh := Module.compHom Msh (algebraMap R Rsh)
    List.TFAE [Module.Flat R Msh, Module.Flat Rh Msh, Module.Flat Rsh Msh]
```

**`flat_tfae_baseChange_henselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/EtaleLocalization/FlatHenselization.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/EtaleLocalization/FlatHenselization.lean#L152). The attribute's comment: “conditions (1)--(5)”.

> **Stacks Project, Tag 05VL, conditions (1)--(5).** If the module over the
> extended-residue-field henselization is obtained from an `Rh`-module by extension of scalars, its
> three flatness conditions are also equivalent to flatness of the original module over `R` and
> over `Rh`.

```lean
theorem flat_tfae_baseChange_henselization {Mh : Type y} [AddCommGroup Mh] [Module Rh Mh] :
    letI : Module R Mh := Module.compHom Mh (algebraMap R Rh)
    letI : Module Rsh (Rsh ⊗[Rh] Mh) := TensorProduct.leftModule
    letI : Module Rh (Rsh ⊗[Rh] Mh) := Module.compHom (Rsh ⊗[Rh] Mh) (algebraMap Rh Rsh)
    letI : Module R (Rsh ⊗[Rh] Mh) := Module.compHom (Rsh ⊗[Rh] Mh) (algebraMap R Rsh)
    List.TFAE [Module.Flat R (Rsh ⊗[Rh] Mh), Module.Flat Rh (Rsh ⊗[Rh] Mh),
      Module.Flat Rsh (Rsh ⊗[Rh] Mh), Module.Flat R Mh, Module.Flat Rh Mh]
```

**`flat_tfae_iteratedBaseChange_henselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/EtaleLocalization/FlatHenselization.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/EtaleLocalization/FlatHenselization.lean#L187). The attribute's comment: “conditions (1)--(6)”.

> **Stacks Project, Tag 05VL, conditions (1)--(6).** If the `Rh`-module is in turn obtained from
> an `R`-module by extension of scalars, all five flatness conditions after base change are
> equivalent to flatness of the original module over `R`.

```lean
theorem flat_tfae_iteratedBaseChange_henselization {M : Type y} [AddCommGroup M] [Module R M] :
    letI : Module Rh (Rh ⊗[R] M) := TensorProduct.leftModule
    letI : Module R (Rh ⊗[R] M) := Module.compHom (Rh ⊗[R] M) (algebraMap R Rh)
    letI : Module Rsh (Rsh ⊗[Rh] (Rh ⊗[R] M)) := TensorProduct.leftModule
    letI : Module Rh (Rsh ⊗[Rh] (Rh ⊗[R] M)) :=
      Module.compHom (Rsh ⊗[Rh] (Rh ⊗[R] M)) (algebraMap Rh Rsh)
    letI : Module R (Rsh ⊗[Rh] (Rh ⊗[R] M)) :=
      Module.compHom (Rsh ⊗[Rh] (Rh ⊗[R] M)) (algebraMap R Rsh)
    List.TFAE [Module.Flat R (Rsh ⊗[Rh] (Rh ⊗[R] M)), Module.Flat Rh (Rsh ⊗[Rh] (Rh ⊗[R] M)),
      Module.Flat Rsh (Rsh ⊗[Rh] (Rh ⊗[R] M)), Module.Flat R (Rh ⊗[R] M),
      Module.Flat Rh (Rh ⊗[R] M), Module.Flat R M]
```

## Tag 0DK0, a lemma

[Tag 0DK0](https://stacks.math.columbia.edu/tag/0DK0) in the Stacks Project.

**`torAmplitude_tfae_henselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/EtaleLocalization/TorAmplitudeHenselization.lean, line 983](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/EtaleLocalization/TorAmplitudeHenselization.lean#L983). The attribute's comment: “conditions (1)--(3)”.

> **Stacks Project, Tag 0DK0, conditions (1)--(3).** The tor amplitude of a
> complex over a henselization with extended residue field is the same whether
> it is measured over the original local ring, the henselization with unchanged
> residue field, or the extended-residue-field henselization.

```lean
public theorem torAmplitude_tfae_henselization
    (Msh : CochainComplex (ModuleCat.{max u uh ush w} Rsh) ℤ) (a b : ℤ) :
    List.TFAE
      [StacksDraft.TorAmplitude.HasTorAmplitudeCanonicalLift
        (DerivedCategory.Q.obj
          (((ModuleCat.restrictScalars (algebraMap R Rsh)).mapHomologicalComplex
            (ComplexShape.up ℤ)).obj Msh)) a b,
       StacksDraft.TorAmplitude.HasTorAmplitudeCanonicalLift
        (DerivedCategory.Q.obj
          (((ModuleCat.restrictScalars (algebraMap Rh Rsh)).mapHomologicalComplex
            (ComplexShape.up ℤ)).obj Msh)) a b,
       StacksDraft.TorAmplitude.HasTorAmplitudeCanonicalLift
         (DerivedCategory.Q.obj Msh) a b]
```

**`torAmplitude_tfae_baseChange_henselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/EtaleLocalization/TorAmplitudeHenselization.lean, line 1029](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/EtaleLocalization/TorAmplitudeHenselization.lean#L1029). The attribute's comment: “conditions (1)--(5)”.

> **Stacks Project, Tag 0DK0, conditions (1)--(5).** If the complex over the
> extended-residue-field henselization is obtained from a complex over `Rh` by
> base change, the preceding three conditions are also equivalent to tor
> amplitude of the original complex over `R` and over `Rh`.

```lean
public theorem torAmplitude_tfae_baseChange_henselization
    (Mh : CochainComplex (ModuleCat.{max u uh ush w} Rh) ℤ) (a b : ℤ) :
    let Msh := (CochainComplex.extendScalarsLarge.{max u w, uh, ush}
      (algebraMap Rh Rsh)).obj Mh
    List.TFAE
      [StacksDraft.TorAmplitude.HasTorAmplitudeCanonicalLift
        (DerivedCategory.Q.obj
          (((ModuleCat.restrictScalars (algebraMap R Rsh)).mapHomologicalComplex
            (ComplexShape.up ℤ)).obj Msh)) a b,
       StacksDraft.TorAmplitude.HasTorAmplitudeCanonicalLift
        (DerivedCategory.Q.obj
          (((ModuleCat.restrictScalars (algebraMap Rh Rsh)).mapHomologicalComplex
            (ComplexShape.up ℤ)).obj Msh)) a b,
       StacksDraft.TorAmplitude.HasTorAmplitudeCanonicalLift
         (DerivedCategory.Q.obj Msh) a b,
       StacksDraft.TorAmplitude.HasTorAmplitudeCanonicalLift
        (DerivedCategory.Q.obj
          (((ModuleCat.restrictScalars (algebraMap R Rh)).mapHomologicalComplex
            (ComplexShape.up ℤ)).obj Mh)) a b,
       StacksDraft.TorAmplitude.HasTorAmplitudeCanonicalLift
         (DerivedCategory.Q.obj Mh) a b]
```

**`torAmplitude_tfae_iteratedBaseChange_henselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/EtaleLocalization/TorAmplitudeHenselization.lean, line 1095](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/EtaleLocalization/TorAmplitudeHenselization.lean#L1095). The attribute's comment: “conditions (1)--(6)”.

> **Stacks Project, Tag 0DK0, conditions (1)--(6).** If the complex over `Rh`
> is itself obtained by base change from `R`, all five conditions after base
> change are equivalent to tor amplitude of the original complex over `R`.

```lean
public theorem torAmplitude_tfae_iteratedBaseChange_henselization
    (M : CochainComplex (ModuleCat.{max u uh ush w} R) ℤ) (a b : ℤ) :
    let Mh := (CochainComplex.extendScalarsLarge.{max ush w, u, uh}
      (algebraMap R Rh)).obj M
    let Msh := (CochainComplex.extendScalarsLarge.{max u w, uh, ush}
      (algebraMap Rh Rsh)).obj Mh
    List.TFAE
      [StacksDraft.TorAmplitude.HasTorAmplitudeCanonicalLift
        (DerivedCategory.Q.obj
          (((ModuleCat.restrictScalars (algebraMap R Rsh)).mapHomologicalComplex
            (ComplexShape.up ℤ)).obj Msh)) a b,
       StacksDraft.TorAmplitude.HasTorAmplitudeCanonicalLift
        (DerivedCategory.Q.obj
          (((ModuleCat.restrictScalars (algebraMap Rh Rsh)).mapHomologicalComplex
            (ComplexShape.up ℤ)).obj Msh)) a b,
       StacksDraft.TorAmplitude.HasTorAmplitudeCanonicalLift
         (DerivedCategory.Q.obj Msh) a b,
       StacksDraft.TorAmplitude.HasTorAmplitudeCanonicalLift
        (DerivedCategory.Q.obj
          (((ModuleCat.restrictScalars (algebraMap R Rh)).mapHomologicalComplex
            (ComplexShape.up ℤ)).obj Mh)) a b,
       StacksDraft.TorAmplitude.HasTorAmplitudeCanonicalLift
         (DerivedCategory.Q.obj Mh) a b,
       StacksDraft.TorAmplitude.HasTorAmplitudeCanonicalLift
         (DerivedCategory.Q.obj M) a b]
```

## Tag 05FN, a lemma

[Tag 05FN](https://stacks.math.columbia.edu/tag/05FN) in the Stacks Project.

**`AlgebraicGeometry.isWeaklyAssociatedPoint_pullback_iff_of_finite_flat`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/EtaleLocalization/FiniteFlatPullback.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/EtaleLocalization/FiniteFlatPullback.lean#L276).

> **Stacks Project, Tag 05FN.** A point is weakly associated to the pullback of a
> quasi-coherent module along a finite flat morphism if and only if its image is weakly
> associated to the original module.

```lean
lemma isWeaklyAssociatedPoint_pullback_iff_of_finite_flat
    {T S : Scheme.{u}} (g : T ⟶ S) [IsFinite g] [Flat g]
    (G : S.Modules) [G.IsQuasicoherent] (t : T) :
    Stacks.Divisors.IsWeaklyAssociatedPoint ((Scheme.Modules.pullback g).obj G) t ↔
      Stacks.Divisors.IsWeaklyAssociatedPoint G (g.base t)
```

## Tag 05FP, a lemma

[Tag 05FP](https://stacks.math.columbia.edu/tag/05FP) in the Stacks Project.

**`AlgebraicGeometry.isWeaklyAssociatedPoint_pullback_iff_of_etale`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/EtaleLocalization/EtalePullback.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/EtaleLocalization/EtalePullback.lean#L239).

> **Stacks Project, Tag 05FP.** A point is weakly associated to the pullback of a
> quasi-coherent module along an étale morphism if and only if its image is weakly associated to
> the original module.

```lean
lemma isWeaklyAssociatedPoint_pullback_iff_of_etale
    {U S : Scheme.{u}} (h : U ⟶ S) [Etale h]
    (G : S.Modules) [G.IsQuasicoherent] (x : U) :
    Stacks.Divisors.IsWeaklyAssociatedPoint ((Scheme.Modules.pullback h).obj G) x ↔
      Stacks.Divisors.IsWeaklyAssociatedPoint G (h.base x)
```

**`AlgebraicGeometry.schemeWeaklyAssociatedPoints_eq_preimage_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedLocallyFiniteCharts.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedLocallyFiniteCharts.lean#L77). The attribute's comment: “the weakly associated points of a scheme etale over another, at the structure sheaf”.

> For an étale morphism of schemes `f : X ⟶ Y`, the weakly associated points of `X` are the
> preimage under `f` of the weakly associated points of `Y`.

```lean
theorem schemeWeaklyAssociatedPoints_eq_preimage_of_etale {X Y : Scheme.{u}} (f : X ⟶ Y)
    [Etale f] :
    Stacks.Divisors.schemeWeaklyAssociatedPoints X =
      f.base ⁻¹' Stacks.Divisors.schemeWeaklyAssociatedPoints Y
```

## Tag 0CTU, a lemma

[Tag 0CTU](https://stacks.math.columbia.edu/tag/0CTU) in the Stacks Project.

**`AlgebraicGeometry.weaklyAssociated_tfae_henselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/EtaleLocalization/Henselization.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/EtaleLocalization/Henselization.lean#L164).

> **Stacks Project, Tag 0CTU.** A point is weakly associated to a quasi-coherent sheaf if and
> only if the maximal ideal of its stalk is weakly associated to the stalk module; equivalently,
> the corresponding maximal ideal remains weakly associated after extension to a henselization or
> a strict henselization.

```lean
theorem weaklyAssociated_tfae_henselization
    {X : Scheme.{u}} (F : X.Modules) [F.IsQuasicoherent] (x : X)
    {Rh Rsh : Type u}
    [CommRing Rh] [IsLocalRing Rh] [Algebra (X.presheaf.stalk x) Rh]
    [IsHenselization (X.presheaf.stalk x) (ResidueField (X.presheaf.stalk x)) Rh]
    [CommRing Rsh] [IsLocalRing Rsh] [Algebra (X.presheaf.stalk x) Rsh]
    [Algebra (ResidueField (X.presheaf.stalk x)) (ResidueField Rsh)]
    [IsSepClosure (ResidueField (X.presheaf.stalk x)) (ResidueField Rsh)]
    [IsHenselization (X.presheaf.stalk x) (ResidueField Rsh) Rsh] :
    let F' : PresheafOfModules (X.presheaf ⋙ forget₂ CommRingCat RingCat) := F.val
    let M := ↑(TopCat.Presheaf.stalk F'.presheaf x)
    letI : Module (X.presheaf.stalk x) M := inferInstance
    List.TFAE
      [Stacks.Divisors.IsWeaklyAssociatedPoint F x,
       IsWeaklyAssociatedPrime (X.presheaf.stalk x) M
         (maximalIdeal (X.presheaf.stalk x)),
       IsWeaklyAssociatedPrime Rh (TensorProduct (X.presheaf.stalk x) Rh M)
         (maximalIdeal Rh),
       IsWeaklyAssociatedPrime Rsh (TensorProduct (X.presheaf.stalk x) Rsh M)
         (maximalIdeal Rsh)]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.2, Tag 05FM](https://stacks.math.columbia.edu/tag/05FM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
