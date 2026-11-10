---
declaration: section
origin: cited
lean: AlgebraicGeometry.SmallEtale.isFiniteTypeOnSite_associatedModule, AlgebraicGeometry.SmallEtale.isFiniteTypeOnSite_of_associatedModule, AlgebraicGeometry.SmallEtale.associatedModuleToPseudoCoherent, AlgebraicGeometry.SmallEtale.pseudoCoherentIffAssociatedModule, AlgebraicGeometry.SmallEtale.pseudoCoherentToAssociatedModule_of_slice_exact, AlgebraicGeometry.SmallEtale.hasTorAmplitude_derivedPullback_of_hasTorAmplitude, AlgebraicGeometry.SmallEtale.hasFiniteTorDimension_derivedPullback_of_hasFiniteTorDimension, AlgebraicGeometry.SmallEtale.locallyHasFiniteTorDimension_relativeDerivedAssociatedModule
statement: formalized
proof: formalized
---

# 75.13 Pseudo-coherent and perfect complexes

Section 75.13 of the Stacks Project, [Tag 08HC](https://stacks.math.columbia.edu/tag/08HC). 11 tags here are carried by 34 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08HD, a lemma

[Tag 08HD](https://stacks.math.columbia.edu/tag/08HD) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.isFiniteTypeOnSite_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleFiniteType.lean, line 458](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleFiniteType.lean#L458). The attribute's comment: “the implication (1) ⇒ (2), with finite type in the categorical form of 03DL (5). The converse is `AlgebraicGeometry.SmallEtale.isFiniteTypeOnSite_of_associatedModule`.”.

> **Stacks 08HD, the implication (1) ⇒ (2).**  The pullback `ε^*𝓕` along the morphism of
> ringed sites `ε : (X_étale, 𝒪) ⟶ (X_Zar, 𝒪_X)` of an `𝒪_X`-module of finite type is of finite
> type on the small étale site of `X`.
>
> This is Stacks 03DO at `ε`: the image open of Stacks 03WT factors every object of the small
> étale site through an open of `X`, uniquely, so sections generating `𝓕` over an open have
> unit images generating `ε^*𝓕` over it.

```lean
theorem isFiniteTypeOnSite_associatedModule (F : X.Modules)
    (hF : SheafOfModules.IsFiniteTypeOnSite F) :
    SheafOfModules.IsFiniteTypeOnSite ((associatedModule B X hX).obj F)
```

**`AlgebraicGeometry.SmallEtale.isFiniteTypeOnSite_of_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleFiniteType.lean, line 896](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleFiniteType.lean#L896). The attribute's comment: “the implication (2) ⇒ (1), with finite type in the categorical form of 03DL (5). The source deduces it from the stalk description of `ε^*`; here it is deduced from the zero-detection assertion of 08H8 for an arbitrary `𝒪_X`-module, `AlgebraicGeometry.SmallEtale.isZero_of_isZero_associatedModule_general`.”.

> **Stacks 08HD, the implication (2) ⇒ (1).**  An `𝒪_X`-module whose pullback `ε^*𝓕` along
> the morphism of ringed sites `ε : (X_étale, 𝒪) ⟶ (X_Zar, 𝒪_X)` is of finite type on the small
> étale site of `X` is itself of finite type, the finite-type condition being in the categorical
> form `SheafOfModules.IsFiniteTypeOnSite` of Stacks 03DL (5).
>
> The covering family of opens is the family of *all* opens of `X` carrying finitely many
> generating sections, so no choice of covering is recorded: what has to be shown is that those
> opens cover, and that is the content of
> `AlgebraicGeometry.SmallEtale.exists_imageOpen_generates`.  Given a point `x` of an open `W`,
> the finite-type hypothesis at the object of `W` gives an object of the small étale site whose
> image contains `x` and on which `ε^*𝓕` has finitely many generating sections; shrinking it
> replaces those by unit images of sections of `𝓕` over its image open, which is contained in
> `W` and contains `x`.

```lean
theorem isFiniteTypeOnSite_of_associatedModule (F : X.Modules)
    (h : SheafOfModules.IsFiniteTypeOnSite ((associatedModule B X hX).obj F)) :
    SheafOfModules.IsFiniteTypeOnSite F
```

## Tag 08HE, a lemma

[Tag 08HE](https://stacks.math.columbia.edu/tag/08HE) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.associatedModuleToPseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtalePseudoCoherentDescent.lean, line 549](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtalePseudoCoherentDescent.lean#L549). The attribute's comment: “clause (2) ⇒ (1): if `ε^*E` is `m`-pseudo-coherent on the small étale site of `S` then `E` is `m`-pseudo-coherent on the small Zariski site of `S`, `ε` being the comparison of ringed sites of Stacks 08H7.”.

> If `ε^*E` is `m`-pseudo-coherent on the small étale site of `S` then `E` is
> `m`-pseudo-coherent on the small Zariski site of `S`, `ε` being the comparison of ringed sites and
> the derived functor being `CategoryTheory.Functor.mapDerivedCategory` of the associated-module
> functor.

```lean
public theorem associatedModuleToPseudoCoherent
    (E : DerivedCategory (SheafOfModules.{u} S.ringCatSheaf)) (m : ℤ) :
    AssociatedModuleToPseudoCoherent B S hS E m
```

**`AlgebraicGeometry.SmallEtale.pseudoCoherentIffAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtalePseudoCoherentDescent.lean, line 565](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtalePseudoCoherentDescent.lean#L565).

> Let `S` be a scheme, let `E` be an object of `D(𝒪_S)` and let `m` be an integer. Then `E` is
> `m`-pseudo-coherent on the small Zariski site of `S` if and only if `ε^*E` is `m`-pseudo-coherent
> on the small étale site of `S`, where `ε : (S_étale, 𝒪) ⟶ (S_Zar, 𝒪_S)` is the comparison of
> ringed sites.

```lean
public theorem pseudoCoherentIffAssociatedModule
    (E : DerivedCategory (SheafOfModules.{u} S.ringCatSheaf)) (m : ℤ) :
    PseudoCoherentIffAssociatedModule B S hS E m
```

**`AlgebraicGeometry.SmallEtale.pseudoCoherentToAssociatedModule_of_slice_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtalePseudoCoherentForward.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtalePseudoCoherentForward.lean#L126). The attribute's comment: “clause (1) ⇒ (2) only: if `E` is `m`-pseudo-coherent on the small Zariski site of `S` then `ε^*E` is `m`-pseudo-coherent on the small étale site of `S`, `ε` being the comparison of Stacks 08H7. Clause (2) ⇒ (1) is `AlgebraicGeometry.SmallEtale.associatedModuleToPseudoCoherent`.”. References: SGA 6 I (2.13), “special case”.

> If `E` is `m`-pseudo-coherent on the small Zariski site of `S` then `ε^*E` is
> `m`-pseudo-coherent on the small étale site of `S`, where the derived functor is
> `CategoryTheory.Functor.mapDerivedCategory` of the associated-module functor.

```lean
public theorem pseudoCoherentToAssociatedModule_of_slice_exact
    (E : DerivedCategory
      (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf S.zariskiRingedSite.O)))
    (m : ℤ) :
    PseudoCoherentToAssociatedModule B S hS E m
```

## Tag 08HF, a lemma

[Tag 08HF](https://stacks.math.columbia.edu/tag/08HF) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.hasTorAmplitude_derivedPullback_of_hasTorAmplitude`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleTorAmplitudeComparison.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleTorAmplitudeComparison.lean#L130). The attribute's comment: “clause (1): `E` has tor amplitude in `[a, b]` ⟺ `ε^*E` has tor amplitude in `[a, b]`, for `ε` the comparison morphism of Equation 75.4.0.1 (Stacks 08H7) read on the `Type u`-presented model `AlgebraicGeometry.SmallEtale.smallModelRingedTopos` of the small étale ringed topos, and `ε^*` its derived pullback. Stated for an arbitrary derived tensor product datum on either side rather than for the canonical one. Clause (2) is `AlgebraicGeometry.SmallEtale.hasFiniteTorDimension_derivedPullback_of_hasFiniteTorDimension`”.

> **Stacks 08HF, clause (1).**  An object `E` of `D(𝒪_S)` has Tor amplitude in `[a, b]` for a
> derived tensor product datum `T` on the small Zariski ringed site of `S` **if and only if** its
> derived pullback `Lε^*E` along the comparison `ε` of Stacks 08H7, read on the `Type u`-presented
> model of the small étale ringed topos, has Tor amplitude in `[a, b]` for a derived tensor product
> datum `T'` on the model.  Both data are arbitrary.
>
> Forwards this is Stacks 08H5.  Backwards it is
> `Stacks.SheafOfModules.DerivedTensorProduct.hasTorAmplitude_of_hasTorAmplitude_derivedPullback`,
> whose two inputs about `ε_model` — that the degreewise pullback of sheaves of modules is exact
> and that it detects the zero sheaf — are the two assertions of Stacks 08H8, read on the model in
> `AlgebraicGeometry.SmallEtale.preservesFiniteLimits_pullbackTopos_toZariskiSmallModelHom` and
> `AlgebraicGeometry.SmallEtale.isZero_of_isZero_pullbackTopos_toZariskiSmallModelHom`.

```lean
public theorem hasTorAmplitude_derivedPullback_of_hasTorAmplitude
    (T : DerivedTensorProduct S.zariskiRingedTopos.toRingedSite)
    (T' : DerivedTensorProduct (smallModelRingedTopos B S hS).toRingedSite)
    (E : RingedSite.DerivedModules S.zariskiRingedTopos.toRingedSite) (a b : ℤ) :
    HasTorAmplitude T' ((derivedPullback (toZariskiSmallModelHom B S hS)).obj E) a b ↔
      HasTorAmplitude T E a b
```

**`AlgebraicGeometry.SmallEtale.hasFiniteTorDimension_derivedPullback_of_hasFiniteTorDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleTorAmplitudeComparison.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleTorAmplitudeComparison.lean#L154). The attribute's comment: “clause (2): `E` has finite tor dimension ⟺ `ε^*E` has finite tor dimension, for `ε` the comparison morphism of Equation 75.4.0.1 (Stacks 08H7) read on the `Type u`-presented model `AlgebraicGeometry.SmallEtale.smallModelRingedTopos` of the small étale ringed topos, and `ε^*` its derived pullback. Stated for an arbitrary derived tensor product datum on either side rather than for the canonical one. Clause (1) is `AlgebraicGeometry.SmallEtale.hasTorAmplitude_derivedPullback_of_hasTorAmplitude`”.

> **Stacks 08HF, clause (2).**  An object `E` of `D(𝒪_S)` has finite Tor dimension for a
> derived tensor product datum `T` on the small Zariski ringed site of `S` **if and only if** its
> derived pullback `Lε^*E` has finite Tor dimension for a derived tensor product datum `T'` on the
> model.  Both data are arbitrary.
>
> This is clause (1) with the interval existentially quantified: an interval containing the Tor
> amplitude of one of the two objects contains that of the other.

```lean
public theorem hasFiniteTorDimension_derivedPullback_of_hasFiniteTorDimension
    (T : DerivedTensorProduct S.zariskiRingedTopos.toRingedSite)
    (T' : DerivedTensorProduct (smallModelRingedTopos B S hS).toRingedSite)
    (E : RingedSite.DerivedModules S.zariskiRingedTopos.toRingedSite) :
    HasFiniteTorDimension T' ((derivedPullback (toZariskiSmallModelHom B S hS)).obj E) ↔
      HasFiniteTorDimension T E
```

## Tag 0DK7, a lemma

[Tag 0DK7](https://stacks.math.columbia.edu/tag/0DK7) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.locallyHasFiniteTorDimension_relativeDerivedAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleRelativeLocalTorDimension.lean, line 523](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleRelativeLocalTorDimension.lean#L523). The attribute's comment: “part (2), with `ε⁻¹f⁻¹𝒪_Y` for `f_small⁻¹𝒪_{Y_étale}`; see the implementation notes of the module of part (1). The form with `f_small⁻¹𝒪_{Y_étale}` itself is, in `AlgebraicGeometry.Space`, `locallyHasFiniteTorDimension_derivedScalarRestriction_iff_representedZariskiDerivedPullback`”.

> **Stacks 0DK7, part (2).**  Let `f : X ⟶ Y` be a morphism of schemes and let `E` be an object
> of `D(f⁻¹𝒪_Y)`.  Then `E` locally has finite Tor dimension if and only if `ε^*E` locally has
> finite Tor dimension as an object of `D(ε⁻¹f⁻¹𝒪_Y)`, in the sense of Stacks 08FZ (3), for any
> families of derived tensor products on the slices of the two sites.
>
> Both conditions are read at the points of `X`.  An open covering of `X` with an interval on each
> member gives, on any object `W` of the small étale site, the covering by the objects mapping into
> one of the members, which is the pullback to `W` of the image of the open covering, a covering
> because the inclusion of the small Zariski site is cover-preserving.  An étale covering of `X`
> with an interval on each member gives the open covering of `X` by the images of the members,
> open because the members are étale over `X`, every point of an image having its geometric point
> lift to the member.

```lean
theorem locallyHasFiniteTorDimension_relativeDerivedAssociatedModule
    (TU : ∀ U : (Scheme.Hom.inverseImageRingedSite f).C,
      Stacks.SheafOfModules.DerivedTensorProduct.{u, u, u, d}
        ((Scheme.Hom.inverseImageRingedSite f).over U))
    (TW : ∀ W : (relativeRingedTopos B X hX f).toRingedSite.C,
      Stacks.SheafOfModules.DerivedTensorProduct.{u + 1, u, u, e}
        ((relativeRingedTopos B X hX f).toRingedSite.over W))
    (E : RingedSite.DerivedModules.{u, u, u, d} (Scheme.Hom.inverseImageRingedSite f)) :
    LocallyHasFiniteTorDimension TU E ↔
      LocallyHasFiniteTorDimension TW ((relativeDerivedAssociatedModule B X hX f).obj E)
```

**`AlgebraicGeometry.SmallEtale.hasTorAmplitude_relativeDerivedAssociatedModule_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleRelativeTorAmplitude.lean, line 536](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleRelativeTorAmplitude.lean#L536). The attribute's comment: “part (1), with `ε⁻¹f⁻¹𝒪_Y` for `f_small⁻¹𝒪_{Y_étale}`; see the implementation notes. The form with `f_small⁻¹𝒪_{Y_étale}` itself is, in `AlgebraicGeometry.Space`, `hasTorAmplitude_derivedScalarRestriction_iff_representedZariskiDerivedPullback`”.

> **Stacks 0DK7, part (1).**  Let `f : X ⟶ Y` be a morphism of schemes and let `E` be an
> object of `D(f⁻¹𝒪_Y)`.  Then `E` has Tor amplitude in `[a, b]` if and only if `ε^*E` has Tor
> amplitude in `[a, b]` as an object of `D(ε⁻¹f⁻¹𝒪_Y)`.
>
> Both sides are read at the stalks by Stacks 0DJJ: on the small Zariski site of `X` at the points
> of `X`, a conservative family, and on the small étale site at the geometric points of `X` at the
> points of `X`, a conservative family too
> (`AlgebraicGeometry.isConservativeFamilyOfPoints_geometricSitePoints`).  At the point `x` the
> two stalks agree, by Stacks 05V5 for `ε`
> (`hasTorAmplitudeCanonical_derivedModuleFiber_relativeDerivedAssociatedModule_iff`).

```lean
theorem hasTorAmplitude_relativeDerivedAssociatedModule_iff
    (E : RingedSite.DerivedModules.{u, u, u, d} (Scheme.Hom.inverseImageRingedSite f))
    (a b : ℤ) :
    Stacks.SheafOfModules.DerivedTensorProduct.HasTorAmplitude T E a b ↔
      Stacks.SheafOfModules.DerivedTensorProduct.HasTorAmplitude T'
        ((relativeDerivedAssociatedModule B X hX f).obj E) a b
```

**`AlgebraicGeometry.Space.locallyHasFiniteTorDimension_derivedScalarRestriction_iff_representedZariskiDerivedPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RepresentedZariskiLocalTorDimension.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RepresentedZariskiLocalTorDimension.lean#L141). The attribute's comment: “part (2)”.

> **Stacks 0DK7, part (2).**  Let `g₀ : X ⟶ Y` be the morphism of schemes underlying a
> morphism `g` of the big fppf site and `E ∈ D(𝒪_X)`.  Then `E` read in `D(g₀⁻¹𝒪_Y)` locally has
> finite Tor dimension if and only if `ε^*E` read in `D(g_{small}⁻¹𝒪_{Y_étale})` locally has
> finite Tor dimension, for any family of derived tensor products on the slices.
>
> As in part (1), `g_{small}⁻¹𝒪_{Y_étale}` is the inverse image of the structure sheaf of
> `yoneda.obj T'` on the small étale site of `yoneda.obj T`, which is that of `X` by Stacks 04M0.
> Both conditions are read at the points: an open cover of `X` with a Tor-amplitude interval on
> each member gives the étale covers by the charts mapping into the members, and an étale cover of
> the identity chart gives the open cover of `X` by the images of its members.

```lean
theorem locallyHasFiniteTorDimension_derivedScalarRestriction_iff_representedZariskiDerivedPullback
    (Tfam : ∀ U : (inverseImageRingedSite B S hS (representedSpaceMap B S hS g)).C,
      Stacks.SheafOfModules.DerivedTensorProduct
        ((inverseImageRingedSite B S hS (representedSpaceMap B S hS g)).over U))
    (E : DerivedCategory (representedSchemeRepresentedZariskiRingedToposHom B S hS T).Modules) :
    Stacks.Cohomology.TorAmplitude.LocallyHasFiniteTorDimension
        (RingedSpace.inverseImage
          (representedSchemeRepresentedZariskiRingedToposHom B S hS T').toRingedSpace
          ((BigFppfOver.toScheme B S hS).map g).base)
        ((Scheme.Hom.derivedScalarRestriction ((BigFppfOver.toScheme B S hS).map g)).obj E) ↔
      Stacks.SheafOfModules.DerivedTensorProduct.LocallyHasFiniteTorDimension Tfam
        ((derivedScalarRestriction B S hS (representedSpaceMap B S hS g)).obj
          ((representedZariskiDerivedPullback B S hS T).obj E))
```

**`AlgebraicGeometry.Space.hasTorAmplitude_derivedScalarRestriction_iff_representedZariskiDerivedPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RepresentedZariskiTorAmplitude.lean, line 274](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RepresentedZariskiTorAmplitude.lean#L274). The attribute's comment: “part (1)”.

> **Stacks 0DK7, part (1).**  Let `g₀ : X ⟶ Y` be the morphism of schemes underlying a
> morphism `g` of the big fppf site, `E ∈ D(𝒪_X)` and `ε^*E` its pullback to the small étale site.
> Then `E` read in `D(g₀⁻¹𝒪_Y)` has Tor amplitude in `[a, b]` if and only if `ε^*E` read in
> `D(g_{small}⁻¹𝒪_{Y_étale})` has Tor amplitude in `[a, b]`.
>
> The small étale site of `X` is the small étale site of the algebraic space `yoneda.obj T`
> (Stacks 04M0), on which `g_{small}⁻¹𝒪_{Y_étale}` is the inverse image of the structure sheaf of
> `yoneda.obj T'` along `yoneda.map g` — the sheaf the source names.  An earlier form used
> `ε⁻¹g₀⁻¹𝒪_Y` instead; identifying the two needs `g₀ ∘ ε_X = ε_Y ∘ g_{small}` and Stacks 070S, so
> that form was not the statement of the source.  The proof is the source's, at the stalks.

```lean
theorem hasTorAmplitude_derivedScalarRestriction_iff_representedZariskiDerivedPullback
    (Tet : Stacks.SheafOfModules.DerivedTensorProduct
      (inverseImageRingedSite B S hS (representedSpaceMap B S hS g)))
    (E : DerivedCategory (representedSchemeRepresentedZariskiRingedToposHom B S hS T).Modules)
    (a b : ℤ) :
    Stacks.Cohomology.TorAmplitude.HasTorAmplitude
        (RingedSpace.inverseImage
          (representedSchemeRepresentedZariskiRingedToposHom B S hS T').toRingedSpace
          ((BigFppfOver.toScheme B S hS).map g).base)
        ((Scheme.Hom.derivedScalarRestriction ((BigFppfOver.toScheme B S hS).map g)).obj E) a b ↔
      Stacks.SheafOfModules.DerivedTensorProduct.HasTorAmplitude Tet
        ((derivedScalarRestriction B S hS (representedSpaceMap B S hS g)).obj
          ((representedZariskiDerivedPullback B S hS T).obj E)) a b
```

## Tag 08HG, a lemma

[Tag 08HG](https://stacks.math.columbia.edu/tag/08HG) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.isPerfectZariski_iff_isPerfectSmallEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SmallEtalePerfectConverse.lean, line 550](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SmallEtalePerfectConverse.lean#L550).

> **Stacks 08HG.** Let `S` be a scheme and `E` an object of `D(𝒪_S)`. Then `E` is a perfect
> object of `D(𝒪_S)` if and only if `ε^*E` is a perfect object of `D(𝒪_étale)`, where
> `ε : (S_étale, 𝒪) ⟶ (S_Zar, 𝒪_S)` is the morphism of ringed sites of Stacks 08H7 and `ε^*` its
> pullback on the derived category — the termwise associated-module functor, `ε` being flat
> (Stacks 08H8).
>
> Perfectness on either side is Stacks 08G5. The direction `E` perfect ⟹ `ε^*E` perfect is
> `AlgebraicGeometry.SmallEtale.perfectToAssociatedModule_of_slice_exact`; the converse is
> `AlgebraicGeometry.SmallEtale.isPerfectZariski_of_isPerfectSmallEtale`.

```lean
theorem isPerfectZariski_iff_isPerfectSmallEtale
    (E : DerivedCategory (SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf S.zariskiRingedSite.O))) :
    IsPerfectZariski S E ↔ IsPerfectSmallEtale B S hS E
```

**`AlgebraicGeometry.SmallEtale.perfectToAssociatedModule_of_slice_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SmallEtalePerfectForward.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SmallEtalePerfectForward.lean#L169). The attribute's comment: “the direction `E` perfect ⟹ `ε^*E` perfect ONLY. Left exactness of `SheafOfModules.pullback (SmallEtale.sliceStructureMap B S hS V)` -- the exactness assertion of Stacks 08H8 localized at an open `V` of `S` -- is supplied by `AlgebraicGeometry.SmallEtale.preservesFiniteLimits_pullback_sliceStructureMap`, which localizes the whole-site 08H8 (`preservesFiniteLimits_associatedModule`) along the open immersion. The converse direction `ε^*E` perfect ⟹ `E` perfect is NOT proved: the source derives it from Stacks 08G8 together with the converses of Stacks 08HE and Stacks 08HF, and of those the converse of Stacks 08HE does not exist in this tree.”.

> **Stacks 08HG, the direction `E` perfect ⟹ `ε^*E` perfect.**
>
> If `E` is a perfect object of `D(𝒪_S)` then `ε^*E` is a perfect object of `D(𝒪_étale)`, `ε` being
> the morphism of ringed sites of Stacks 08H7 and `ε^*` the termwise associated-module functor on the
> derived category, which is what `ε` being flat means.
>
> Left exactness of the associated-module functor on a slice over an open of `S` is the exactness
> assertion of Stacks 08H8 localized at that open, proved by
> `AlgebraicGeometry.SmallEtale.preservesFiniteLimits_pullback_sliceStructureMap`.  Everything else
> is available: the transfer engine
> `AlgebraicGeometry.RingedSite.isPerfect_mapDerivedCategory_of_hypotheses`, the localization square
> of Stacks 03DV (`associatedModuleOverIso`), the unit comparison, and the covering
> (`coversTop_obj_opensToSmallEtale`).

```lean
public theorem perfectToAssociatedModule_of_slice_exact
    (E : DerivedCategory
      (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf S.zariskiRingedSite.O)))
    (hE : IsPerfectZariski S E) :
    IsPerfectSmallEtale B S hS E
```

## Tag 08JL, a lemma

[Tag 08JL](https://stacks.math.columbia.edu/tag/08JL) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_homology_of_isPseudoCoherentFrom_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PseudoCoherentCohomologyUnconditional.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PseudoCoherentCohomologyUnconditional.lean#L259). The attribute's comment: “cohomology above the approximation degree”.

> **Stacks 08JL, first assertion.**  Let `S` be a scheme, let `F` be an algebraic space over
> `S` and let `E` be an object of `D(𝒪_F)`.  If `E` is `n`-pseudo-coherent, then `Hⁱ(E)` is a
> quasi-coherent `𝒪_F`-module for every `i > n`.
>
> The second assertion of the tag is
> `AlgebraicGeometry.Space.derivedCategoryB_of_isPseudoCoherent_unconditional`.
>
> This is `AlgebraicGeometry.Space.isQuasicoherentOnSite_homology_of_isPseudoCoherentFrom` with
> its two closure hypotheses discharged by
> `AlgebraicGeometry.Space.isClosedUnderKernels_over` and
> `AlgebraicGeometry.Space.isClosedUnderCokernels_over`.

```lean
theorem isQuasicoherentOnSite_homology_of_isPseudoCoherentFrom_unconditional
    (E : DerivedCategory (Modules.{u, u} B S hS F hF)) (n i : ℤ)
    (hE : (smallEtaleRingedSite B S hS F hF).IsPseudoCoherentFrom E n) (hi : n < i) :
    ((DerivedCategory.homologyFunctor
      (Modules.{u, u} B S hS F hF) i).obj E).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Space.derivedCategoryB_of_isPseudoCoherent_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PseudoCoherentCohomologyUnconditional.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PseudoCoherentCohomologyUnconditional.lean#L288). The attribute's comment: “pseudo-coherent objects lie in the quasi-coherent derived category”.

> **Stacks 08JL, second assertion.**  Let `S` be a scheme, let `F` be an algebraic space over
> `S` and let `E` be an object of `D(𝒪_F)`.  If `E` is pseudo-coherent, then `E` lies in
> `D_QCoh(𝒪_F)`, that is, every cohomology sheaf of `E` is quasi-coherent.
>
> The conclusion is the object property whose full subcategory is
> `AlgebraicGeometry.Space.QuasicoherentDerivedCategory`, the `D_QCoh(𝒪_F)` of Stacks 071X.  The
> first assertion of the tag is
> `AlgebraicGeometry.Space.isQuasicoherentOnSite_homology_of_isPseudoCoherentFrom_unconditional`.
>
> Apply the first assertion in degree `i` using a strictly perfect approximation from degree
> `i - 1`.

```lean
theorem derivedCategoryB_of_isPseudoCoherent_unconditional
    (E : DerivedCategory (Modules.{u, u} B S hS F hF))
    (hE : (smallEtaleRingedSite B S hS F hF).IsPseudoCoherent E) :
    DerivedCategoryB.derivedCategoryB
      (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS F hF).O))) E
```

## Tag 08IK, a lemma

[Tag 08IK](https://stacks.math.columbia.edu/tag/08IK) in the Stacks Project.

**`AlgebraicGeometry.Space.isCoherentOnSite_homology_of_isPseudoCoherentFrom_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PseudoCoherent/CoherentCohomology.lean, line 383](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PseudoCoherent/CoherentCohomology.lean#L383). The attribute's comment: “(2) gives the coherence clause of (1)”.

> **Stacks 08IK, the coherence clause of (1) derived from (2).**  Let `S` be a scheme, let `F`
> be a Noetherian algebraic space over `S` and let `E` be an object of `D_QCoh(𝒪_F)`.  If `E` is
> `m`-pseudo-coherent then `Hⁱ(E)` is coherent for every `i ≥ m`.
>
> The remaining clause of (1), that `Hⁱ(E)` vanishes for `i ≫ 0`, and the converse implication
> (1) ⇒ (2) are not proved in this development; the module documentation names the missing
> substrate for each.
>
> Only local Noetherianity of `F` is used, which is the third component of Stacks 03EA; the
> quasi-compactness and quasi-separatedness components are not.  The underlying statement with
> that hypothesis alone is
> `AlgebraicGeometry.Space.isCoherentOnSite_homology_of_isPseudoCoherentFrom`.
>
> The quasi-coherence hypothesis is the hypothesis `E ∈ D_QCoh(𝒪_F)` of the source, read in the
> single degree in which it is used, and it is needed only in the degree `i = m`:
> `AlgebraicGeometry.Space.isCoherentOnSite_homology_of_isPseudoCoherentFrom_of_lt` is the same
> conclusion for `i > m` with no hypothesis on `E` beyond pseudo-coherence.

```lean
theorem isCoherentOnSite_homology_of_isPseudoCoherentFrom_of_isNoetherian
    (hZ : B.Contains (⊤_ Scheme.{u})) (hFN : IsNoetherian B S hS hZ F)
    (E : DerivedCategory (Modules.{u, u} B S hS F hF)) (m i : ℤ)
    (hE : (smallEtaleRingedSite B S hS F hF).IsPseudoCoherentFrom E m) (hi : m ≤ i)
    (hqc : ((DerivedCategory.homologyFunctor
      (Modules.{u, u} B S hS F hF) i).obj E).IsQuasicoherentOnSite) :
    SheafOfModules.IsCoherentOnSite
      ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS F hF) i).obj E)
```

**`AlgebraicGeometry.Space.isCoherentOnSite_homology_of_isPseudoCoherent_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PseudoCoherent/CoherentCohomology.lean, line 402](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PseudoCoherent/CoherentCohomology.lean#L402). The attribute's comment: “pseudo-coherent gives coherent cohomology”.

> **Stacks 08IK, the coherence half of the final statement.**  Let `S` be a scheme, let `F` be
> a Noetherian algebraic space over `S` and let `E` be a pseudo-coherent object of `D(𝒪_F)`.  Then
> `Hⁱ(E)` is a coherent `𝒪_F`-module in every degree.
>
> This is the half of "`E` is an object of `D⁻_Coh(𝒪_F)`" that does not mention boundedness; the
> boundedness half is not proved here, and neither is the converse.  No quasi-coherence hypothesis
> is needed: a pseudo-coherent object lies in `D_QCoh(𝒪_F)` by Stacks 08JL,
> `AlgebraicGeometry.Space.derivedCategoryB_of_isPseudoCoherent_unconditional`.

```lean
theorem isCoherentOnSite_homology_of_isPseudoCoherent_of_isNoetherian
    (hZ : B.Contains (⊤_ Scheme.{u})) (hFN : IsNoetherian B S hS hZ F)
    (E : DerivedCategory (Modules.{u, u} B S hS F hF))
    (hE : (smallEtaleRingedSite B S hS F hF).IsPseudoCoherent E) (i : ℤ) :
    SheafOfModules.IsCoherentOnSite
      ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS F hF) i).obj E)
```

**`AlgebraicGeometry.Space.isPseudoCoherentFrom_of_isCoherent_homology_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PseudoCoherent/CoherentCohomologyConverse.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PseudoCoherent/CoherentCohomologyConverse.lean#L161). The attribute's comment: “(1) ⇒ (2)”.

> On a Noetherian algebraic space, an object of `D_QCoh(𝒪_X)` whose cohomology is coherent in
> degrees `≥ m` and zero in degrees `> b` is `m`-pseudo-coherent.

```lean
theorem isPseudoCoherentFrom_of_isCoherent_homology_of_isNoetherian
    (hZ : B.Contains (⊤_ Scheme.{u})) (hXN : IsNoetherian B S hS hZ X.1)
    (E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2)) (m b : ℤ)
    (hqc : ∀ i : ℤ,
      ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS X.1 X.2) i).obj
        E).IsQuasicoherentOnSite)
    (hcoh : ∀ i : ℤ, m ≤ i →
      IsCoherent B S hS X.1 X.2 ((DerivedCategory.homologyFunctor _ i).obj E))
    (hb : ∀ i : ℤ, b < i → IsZero ((DerivedCategory.homologyFunctor _ i).obj E)) :
    (smallEtaleRingedSite B S hS X.1 X.2).IsPseudoCoherentFrom E m
```

**`AlgebraicGeometry.Space.isPseudoCoherent_of_isCoherent_homology_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PseudoCoherent/CoherentCohomologyConverse.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PseudoCoherent/CoherentCohomologyConverse.lean#L176). The attribute's comment: “in particular: an object of D⁻_Coh is pseudo-coherent”.

> On a Noetherian algebraic space an object of `D(𝒪_X)` with coherent cohomology sheaves
> vanishing in large degrees is pseudo-coherent.

```lean
theorem isPseudoCoherent_of_isCoherent_homology_of_isNoetherian
    (hZ : B.Contains (⊤_ Scheme.{u})) (hXN : IsNoetherian B S hS hZ X.1)
    (E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2))
    (hcoh : ∀ i : ℤ, IsCoherent B S hS X.1 X.2 ((DerivedCategory.homologyFunctor _ i).obj E))
    (hb : DerivedCategoryB.IsBoundedAbove E) :
    (smallEtaleRingedSite B S hS X.1 X.2).IsPseudoCoherent E
```

**`AlgebraicGeometry.Space.isPseudoCoherentFrom_iff_and_isPseudoCoherent_iff_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PseudoCoherent/CoherentCohomologyEquivalence.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PseudoCoherent/CoherentCohomologyEquivalence.lean#L174).

> **Stacks 08IK.** Let `S` be a scheme, let `F` be a Noetherian algebraic space over `S` and
> let `E` be an object of `D_QCoh(𝒪_F)`. For every `m ∈ ℤ` the following are equivalent:
>
> 1. `Hⁱ(E)` is coherent for `i ≥ m` and zero for `i ≫ 0`, and
> 2. `E` is `m`-pseudo-coherent.
>
> In particular, `E` is pseudo-coherent if and only if `E` is an object of `D⁻_Coh(𝒪_F)`, that
> is, its cohomology vanishes in all sufficiently large degrees and is coherent in every degree.
>
> The first conjunct is `AlgebraicGeometry.Space.isPseudoCoherentFrom_iff_of_isNoetherian` and the
> second `AlgebraicGeometry.Space.isPseudoCoherent_iff_of_isNoetherian`. Noetherianity of `F` is
> Stacks 03EA: quasi-compact, quasi-separated and locally Noetherian. `D_QCoh(𝒪_F)` is the
> condition whose full subcategory is `AlgebraicGeometry.Space.QuasicoherentDerivedCategory`
> (Stacks 071X).

```lean
theorem isPseudoCoherentFrom_iff_and_isPseudoCoherent_iff_of_isNoetherian
    (hZ : B.Contains (⊤_ Scheme.{u})) (hFN : IsNoetherian B S hS hZ F)
    (E : DerivedCategory (Modules.{u, u} B S hS F hF))
    (hE : DerivedCategoryB.derivedCategoryB
      (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS F hF).O))) E) :
    (∀ m : ℤ,
      ((∀ i : ℤ, m ≤ i → SheafOfModules.IsCoherentOnSite
          ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS F hF) i).obj E)) ∧
        DerivedCategoryB.IsBoundedAbove E) ↔
        (smallEtaleRingedSite B S hS F hF).IsPseudoCoherentFrom E m) ∧
      ((smallEtaleRingedSite B S hS F hF).IsPseudoCoherent E ↔
        (DerivedCategoryB.IsBoundedAbove E ∧
          ∀ i : ℤ, SheafOfModules.IsCoherentOnSite
            ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS F hF) i).obj E)))
```

**`AlgebraicGeometry.Space.isCoherentOnSite_homology_and_isBoundedAbove_of_isPseudoCoherentFrom_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PseudoCoherent/CoherentCohomologyVanishing.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PseudoCoherent/CoherentCohomologyVanishing.lean#L106). The attribute's comment: “(2) gives (1)”.

> Let `S` be a scheme, let `F` be a Noetherian algebraic space over `S` and let `E` be an
> object of `D_QCoh(𝒪_F)`.  If `E` is `m`-pseudo-coherent then `Hⁱ(E)` is coherent for every
> `i ≥ m` and `Hⁱ(E)` vanishes for `i ≫ 0`.

```lean
theorem isCoherentOnSite_homology_and_isBoundedAbove_of_isPseudoCoherentFrom_of_isNoetherian
    (hZ : B.Contains (⊤_ Scheme.{u})) (hFN : IsNoetherian B S hS hZ F)
    (E : DerivedCategory (Modules.{u, u} B S hS F hF)) (m : ℤ)
    (hE : (smallEtaleRingedSite B S hS F hF).IsPseudoCoherentFrom E m)
    (hqc : ∀ i : ℤ, ((DerivedCategory.homologyFunctor
      (Modules.{u, u} B S hS F hF) i).obj E).IsQuasicoherentOnSite) :
    (∀ i : ℤ, m ≤ i → SheafOfModules.IsCoherentOnSite
        ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS F hF) i).obj E)) ∧
      DerivedCategoryB.IsBoundedAbove E
```

**`AlgebraicGeometry.Space.isCoherentOnSite_homology_and_isBoundedAbove_of_isPseudoCoherent_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PseudoCoherent/CoherentCohomologyVanishing.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PseudoCoherent/CoherentCohomologyVanishing.lean#L123). The attribute's comment: “pseudo-coherent gives D⁻_Coh”.

> Let `S` be a scheme, let `F` be a Noetherian algebraic space over `S` and let `E` be a
> pseudo-coherent object of `D(𝒪_F)`.  Then `E` is an object of `D⁻_Coh(𝒪_F)`: its cohomology
> vanishes in all sufficiently large degrees and is coherent in every degree.

```lean
theorem isCoherentOnSite_homology_and_isBoundedAbove_of_isPseudoCoherent_of_isNoetherian
    (hZ : B.Contains (⊤_ Scheme.{u})) (hFN : IsNoetherian B S hS hZ F)
    (E : DerivedCategory (Modules.{u, u} B S hS F hF))
    (hE : (smallEtaleRingedSite B S hS F hF).IsPseudoCoherent E) :
    DerivedCategoryB.IsBoundedAbove E ∧
      ∀ i : ℤ, SheafOfModules.IsCoherentOnSite
        ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS F hF) i).obj E)
```

**`AlgebraicGeometry.Space.isCoherent_homology_iff_isPseudoCoherentFrom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PseudoCoherent/PseudoCoherentIffCoherentHomology.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PseudoCoherent/PseudoCoherentIffCoherentHomology.lean#L264).

> **Stacks 08IK.** Let `S` be a scheme, `X` a Noetherian algebraic space over `S` and `E` an
> object of `D_QCoh(𝒪_X)`. For `m ∈ ℤ` the following are equivalent:
> 1. `Hⁱ(E)` is coherent for `i ≥ m` and zero for `i ≫ 0`, and
> 2. `E` is `m`-pseudo-coherent.

```lean
theorem isCoherent_homology_iff_isPseudoCoherentFrom (hZ : B.Contains (⊤_ Scheme.{u}))
    (X : AlgebraicSpaces B S hS) (hX : IsNoetherian B S hS hZ X.1)
    (E : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2) (m : ℤ) :
    ((∀ i : ℤ, m ≤ i → IsCoherent B S hS X.1 X.2
        ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS X.1 X.2) i).obj E.obj)) ∧
      ∃ b : ℤ, ∀ i : ℤ, b < i →
        IsZero ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS X.1 X.2) i).obj E.obj)) ↔
      (smallEtaleRingedSite B S hS X.1 X.2).IsPseudoCoherentFrom E.obj m
```

**`AlgebraicGeometry.Space.isPseudoCoherent_iff_isCoherent_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PseudoCoherent/PseudoCoherentIffCoherentHomology.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PseudoCoherent/PseudoCoherentIffCoherentHomology.lean#L284). The attribute's comment: “pseudo-coherent objects of D_QCoh are those of D⁻_Coh”.

> **Stacks 08IK, the final statement.** Let `X` be a Noetherian algebraic space over `S`. An
> object `E` of `D_QCoh(𝒪_X)` is pseudo-coherent if and only if it lies in `D⁻_Coh(𝒪_X)`: its
> cohomology sheaves are coherent and vanish in all sufficiently large degrees.

```lean
theorem isPseudoCoherent_iff_isCoherent_homology (hZ : B.Contains (⊤_ Scheme.{u}))
    (X : AlgebraicSpaces B S hS) (hX : IsNoetherian B S hS hZ X.1)
    (E : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2) :
    (smallEtaleRingedSite B S hS X.1 X.2).IsPseudoCoherent E.obj ↔
      (∃ b : ℤ, ∀ i : ℤ, b < i →
          IsZero ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS X.1 X.2) i).obj E.obj)) ∧
        ∀ i : ℤ, IsCoherent B S hS X.1 X.2
          ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS X.1 X.2) i).obj E.obj)
```

## Tag 08IL, a lemma

[Tag 08IL](https://stacks.math.columbia.edu/tag/08IL) in the Stacks Project.

**`AlgebraicGeometry.Space.hasTorAmplitude_iff_hasTorAmplitudeOnQuasicoherent_standardModel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TorAmplitudeQuasiCoherentDetection.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TorAmplitudeQuasiCoherentDetection.lean#L84).

> **Stacks 08IL.**  Let `X` be a quasi-separated algebraic space and `E` an object of
> `D_QCoh(𝒪_X)`.  Then `E` has Tor amplitude in `[a, b]` if and only if
> `Hⁱ(E ⊗^L_{𝒪_X} ℱ) = 0` for `i ∉ [a, b]` and every quasi-coherent `𝒪_X`-module `ℱ`.
>
> This is the form at the standard model of `D(𝒪_X)`, with no hypothesis on the tensor product of
> sheaves.  The derived tensor product is any `T`; Tor amplitude and condition (2) do not depend on
> it.  The hypothesis `a ≤ b` of the source is not needed.  For (2) ⟹ (1), Tor amplitude is checked
> on the affine étale charts `j : U ⟶ X`; condition (2) passes to `Lj^*E` because `X` is
> quasi-separated (`AlgebraicGeometry.Space.hasTorAmplitudeOnQuasicoherent_chart`), `Lj^*E` lies in
> `D_QCoh`, and the affine case is
> `AlgebraicGeometry.Space.hasTorAmplitude_of_hasTorAmplitudeOnQuasicoherent_representedAffine`.

```lean
theorem hasTorAmplitude_iff_hasTorAmplitudeOnQuasicoherent_standardModel
    (hZ : B.Contains (⊤_ Scheme.{u}))
    (X : AlgebraicSpaces B S hS) (hXqs : IsAbsolutelyQuasiSeparated B S hS hZ X.1)
    (T : DerivedTensorProduct (smallEtaleRingedSite B S hS X.1 X.2))
    (E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2)) (hE : QcohDerived B S hS X E)
    (a b : ℤ) :
    DerivedTensorProduct.HasTorAmplitude T E a b ↔
      HasTorAmplitudeOnQuasicoherent B S hS X.2 T E a b
```

**`AlgebraicGeometry.Space.hasTorAmplitudeOnQuasicoherent_of_hasTorAmplitude`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TorAmplitudeQuasiCoherentTests.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TorAmplitudeQuasiCoherentTests.lean#L97). The attribute's comment: “(1) implies (2)”.

> If an object of `D(𝒪_X)` on an algebraic space `X` has Tor amplitude in `[a, b]`, then its
> derived tensor product with every quasi-coherent `𝒪_X`-module has vanishing cohomology outside
> `[a, b]`.

```lean
theorem hasTorAmplitudeOnQuasicoherent_of_hasTorAmplitude
    (T : DerivedTensorProduct.{u + 1, u, u, d} (smallEtaleRingedSite B S hS F hF))
    (E : RingedSite.DerivedModules.{u + 1, u, u, d} (smallEtaleRingedSite B S hS F hF))
    (a b : ℤ)
    (hE : Stacks.SheafOfModules.DerivedTensorProduct.HasTorAmplitude T E a b) :
    HasTorAmplitudeOnQuasicoherent B S hS hF T E a b
```

**`AlgebraicGeometry.Space.hasTorAmplitude_iff_hasTorAmplitudeOnQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TorAmplitudeQuasiCoherentTestsConverse.lean, line 410](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TorAmplitudeQuasiCoherentTestsConverse.lean#L410).

> **Stacks 08IL.**  Let `X` be a quasi-separated algebraic space over `S`, let `E` be an object
> of `D_QCoh(𝒪_X)`, and let `T` be a derived tensor product on `D(𝒪_X)`.  The following are
> equivalent:
>
> 1. `E` has Tor amplitude in `[a, b]`;
> 2. `Hⁱ(E ⊗^L_{𝒪_X} ℱ) = 0` for `i ∉ [a, b]` and every quasi-coherent `𝒪_X`-module `ℱ`.
>
> The source assumes `a ≤ b`; neither direction uses it, as in the scheme case Stacks 08EA, so it is
> not assumed.  (1) ⟹ (2) is
> `AlgebraicGeometry.Space.hasTorAmplitudeOnQuasicoherent_of_hasTorAmplitude`.  For (2) ⟹ (1) the
> converse `AlgebraicGeometry.Space.hasTorAmplitude_of_hasTorAmplitudeOnQuasicoherent_ofSlices` is
> applied at the standard derived categories of `X` and of its slices, and carried to the given
> derived category of `X` and the given datum `T` along the identity of `Mod(𝒪_X)`, which carries
> Tor tests to Tor tests
> (`Stacks.SheafOfModules.DerivedTensorProduct.isZero_homology_tensor_single_iff_of_equivalence`).

```lean
theorem hasTorAmplitude_iff_hasTorAmplitudeOnQuasicoherent
    (hZ : B.Contains (⊤_ Scheme.{u})) (hqs : IsAbsolutelyQuasiSeparated B S hS hZ F)
    (T : DerivedTensorProduct.{u + 1, u, u, d} (smallEtaleRingedSite B S hS F hF))
    (E : RingedSite.DerivedModules.{u + 1, u, u, d} (smallEtaleRingedSite B S hS F hF))
    (hE : DerivedCategoryB.derivedCategoryB
      (_root_.SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        (Tensor.ringSheaf (smallEtaleRingedSite B S hS F hF).O)) E)
    (a b : ℤ) :
    HasTorAmplitude T E a b ↔ HasTorAmplitudeOnQuasicoherent B S hS hF T E a b
```

## Tag 08JP, a lemma

[Tag 08JP](https://stacks.math.columbia.edu/tag/08JP) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.isIso_derivedAssociatedModuleDerivedSheafHomComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleDerivedSheafHomComparisonIso.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleDerivedSheafHomComparisonIso.lean#L227). The attribute's comment: “case (2), E in the thick closure of 𝒪_S, over the data T₂, e₂, m”.

> **Stacks 08JP, case (2), over the mixed-universe data `T₂`, `e₂`, `m`.**
>
> The canonical map
>
> `ε^* R𝓗om_{𝒪_S}(E, F) ⟶ R𝓗om_𝒪(ε^* E, ε^* F)`
>
> of `AlgebraicGeometry.SmallEtale.derivedAssociatedModuleDerivedSheafHomComparison`, between the
> two sides `AlgebraicGeometry.SmallEtale.raisedDerivedAssociatedModuleDerivedSheafHom` and
> `AlgebraicGeometry.SmallEtale.derivedSheafHomOfAssociatedModule`, is an **isomorphism** whenever
> `E` lies in the strictly full saturated triangulated subcategory of `D(𝒪_S)` generated by the
> structure sheaf, and `F` is arbitrary — which is the shape of case (2) of Stacks 08JP, whose
> hypothesis on `E` is perfection and whose `F` is unrestricted.
>
> The condition on `E` is what takes the statement off `E = 𝒪_S`; the conditions on the data are
> listed in the module docstring. The two model identifications are isomorphisms, so the conclusion
> for the canonical map is the conclusion for the comparison at the standard model.

```lean
theorem isIso_derivedAssociatedModuleDerivedSheafHomComparison
    (hn₁ : MixedTranspose.TensorHomEquivNatural (Stacks.SheafOfModules.derivedSheafHom S.sheaf)
      (internalHomTensorUncurried S.toRingedSpace) (tensorHomEquiv S.toRingedSpace))
    (hr₁ : MixedTranspose.RightUnitorNatural (internalHomTensorUncurried S.toRingedSpace)
      (zariskiUnitObj S) r₁)
    (hn₂ : MixedTranspose.MixedTensorHomEquivNatural (derivedModuleULift B S hS)
      (derivedSheafHomBifunctor B S hS) T₂ e₂)
    (hr₂ : MixedTranspose.MixedRightUnitorNatural
      (derivedAssociatedModuleFunctorStandardModel B S hS) T₂ (zariskiUnitObj S) r₂)
    (hm : MixedTranspose.MonoidalityUnital
      (derivedAssociatedModuleFunctorStandardModel B S hS) (derivedModuleULift B S hS)
      (internalHomTensorUncurried S.toRingedSpace) T₂ m (zariskiUnitObj S) r₁ r₂)
    (F : DerivedCategory (SheafOfModules.{u} S.ringCatSheaf))
    [(MixedTranspose.comparisonSourceFunctor
      (derivedAssociatedModuleFunctorStandardModel B S hS) (derivedModuleULift B S hS)
      (Stacks.SheafOfModules.derivedSheafHom S.sheaf) F).CommShift ℤ]
    [(MixedTranspose.comparisonTargetFunctor
      (derivedAssociatedModuleFunctorStandardModel B S hS)
      (derivedSheafHomBifunctor B S hS) F).CommShift ℤ]
    [(MixedTranspose.comparisonSourceFunctor
      (derivedAssociatedModuleFunctorStandardModel B S hS) (derivedModuleULift B S hS)
      (Stacks.SheafOfModules.derivedSheafHom S.sheaf) F).IsTriangulated]
    [(MixedTranspose.comparisonTargetFunctor
      (derivedAssociatedModuleFunctorStandardModel B S hS)
      (derivedSheafHomBifunctor B S hS) F).IsTriangulated]
    (η : MixedTranspose.comparisonSourceFunctor
        (derivedAssociatedModuleFunctorStandardModel B S hS) (derivedModuleULift B S hS)
        (Stacks.SheafOfModules.derivedSheafHom S.sheaf) F ⟶
      MixedTranspose.comparisonTargetFunctor
        (derivedAssociatedModuleFunctorStandardModel B S hS)
        (derivedSheafHomBifunctor B S hS) F)
    [NatTrans.CommShift η ℤ]
    (hη : ∀ Z : DerivedCategory (SheafOfModules.{u} S.ringCatSheaf),
      η.app (op Z) = derivedSheafHomPullbackComparisonAtStandardModel B S hS T₂ e₂ m Z F)
    (E : DerivedCategory (SheafOfModules.{u} S.ringCatSheaf))
    (hE : MixedTranspose.GeneratedByOp (zariskiUnitObj S) E) :
    IsIso (derivedAssociatedModuleDerivedSheafHomComparison B S hS T₂ e₂ m E F)
```

**`AlgebraicGeometry.SmallEtale.isIso_derivedPullbackSheafHomMap_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleDerivedSheafHomPerfect.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleDerivedSheafHomPerfect.lean#L118). The attribute's comment: “case (2): E perfect, F arbitrary”.

> **Stacks 08JP, case (2): `ε^*` commutes with `RSheafHom` out of a perfect object.** Let `S`
> be a scheme and `ε : (S_étale, 𝒪) ⟶ (S_Zar, 𝒪_S)` the morphism of ringed sites of Stacks 08H7,
> read on the model of the small étale site. For `E` perfect and `F` arbitrary in `D(𝒪_S)`, the
> canonical map `ε^* RSheafHom(E, F) ⟶ RSheafHom(ε^* E, ε^* F)` of Stacks 08JF,
> `AlgebraicGeometry.RingedToposSiteHom.derivedPullbackSheafHomMap`, is an isomorphism.
>
> By `isIso_derivedPullbackSheafHomMap_iff_isIso_homComparisonMonoidal` it is enough that the
> comparison of the monoidal functor `ε^*` is invertible at `E`, and it is, `E` being one half of
> the exact pairing `exactPairingDerivedDualZariski` with its derived dual.

```lean
theorem isIso_derivedPullbackSheafHomMap_of_isPerfect
    (E F : DerivedCategory (SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf S.zariskiRingedTopos.O)))
    (hE : S.zariskiRingedSite.IsPerfect E) :
    IsIso (RingedToposSiteHom.derivedPullbackSheafHomMap (toZariskiSmallModelHom B S hS)
      (isMorphismOfSites_toZariskiSmallModelHom_u B S hS) E F)
```

**`AlgebraicGeometry.SmallEtale.isIso_derivedPullbackSheafHomMap_of_isPseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleDerivedSheafHomPseudoCoherent.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleDerivedSheafHomPseudoCoherent.lean#L194). The attribute's comment: “case (1): E pseudo-coherent, F bounded below”.

> **Stacks 08JP, case (1): `ε^*` commutes with `RSheafHom` out of a pseudo-coherent object into
> a bounded below one.** Let `S` be a scheme and `ε : (S_étale, 𝒪) ⟶ (S_Zar, 𝒪_S)` the morphism of
> ringed sites of Stacks 08H7, read on the model of the small étale site. For `E` pseudo-coherent
> and `F` in `D^+(𝒪_S)`, the canonical map `ε^* RSheafHom(E, F) ⟶ RSheafHom(ε^* E, ε^* F)` of
> Stacks 08JF, `AlgebraicGeometry.RingedToposSiteHom.derivedPullbackSheafHomMap`, is an
> isomorphism.
>
> The only hypotheses are the two of the source: pseudo-coherence of `E` and boundedness below of
> `F`. By `isIso_derivedPullbackSheafHomMap_iff_isIso_homComparisonMonoidal` it is enough that the
> comparison of the monoidal functor `ε^*` is invertible at `E` and `F`, which is
> `isIso_homComparisonMonoidal_derivedPullbackSmallModel_of_isPseudoCoherent`.

```lean
theorem isIso_derivedPullbackSheafHomMap_of_isPseudoCoherent
    (E F : DerivedCategory (SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf S.zariskiRingedTopos.O)))
    (hE : S.zariskiRingedSite.IsPseudoCoherent E) (hF : ∃ a : ℤ, F.IsGE a) :
    IsIso (RingedToposSiteHom.derivedPullbackSheafHomMap (toZariskiSmallModelHom B S hS)
      (isMorphismOfSites_toZariskiSmallModelHom_u B S hS) E F)
```

## Tag 0A8A, a lemma

[Tag 0A8A](https://stacks.math.columbia.edu/tag/0A8A) in the Stacks Project.

**`AlgebraicGeometry.Space.qcohDerived_smallEtaleDerivedSheafHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedSheafHomQuasicoherent.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedSheafHomQuasicoherent.lean#L235).

> **Stacks 0A8A.** Let `X` be an algebraic space and `K`, `L` objects of `D(𝒪_X)`. If either
> `L` lies in `D^+_QCoh(𝒪_X)` and `K` is pseudo-coherent, or `L` lies in `D_QCoh(𝒪_X)` and `K` is
> perfect, then `R𝓗om(K, L)` lies in `D_QCoh(𝒪_X)`.

```lean
theorem qcohDerived_smallEtaleDerivedSheafHom (X : AlgebraicSpaces B S hS)
    (K L : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)))
    (h : (RingedSite.IsPseudoCoherent (smallEtaleRingedSite B S hS X.1 X.2) K ∧
        DerivedCategoryB.derivedCategoryBPlus
          (A := SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X))
          (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
            ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O))) L) ∨
      (RingedSite.IsPerfect (smallEtaleRingedSite B S hS X.1 X.2) K ∧ QcohDerived B S hS X L)) :
    QcohDerived B S hS X (((smallEtaleDerivedSheafHom B S hS X).obj (op K)).obj L)
```

## Tag 0E4Q, a lemma

[Tag 0E4Q](https://stacks.math.columbia.edu/tag/0E4Q) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_derivedTensorHomDiagonal_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedTensorHomDiagonal.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedTensorHomDiagonal.lean#L164). The attribute's comment: “case (1): M perfect”.

> **Stacks 0E4Q case (1).** For objects `K`, `L`, `M` of `D(𝒪_X)` on an algebraic space `X`
> with `M` perfect, the canonical morphism of Stacks 0BYU
>
> `K ⊗^L_{𝒪_X} RSheafHom(M, L) ⟶ RSheafHom(M, K ⊗^L_{𝒪_X} L)`
>
> is an isomorphism. Nothing is assumed of `K` or `L`; in particular quasi-coherence of the
> cohomology sheaves is not used.

```lean
theorem isIso_derivedTensorHomDiagonal_of_isPerfect
    (K L M : DerivedCategory
      (SheafOfModules.{u}
        (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleModelRingedSite B S hS F hF).O)))
    (hM : (smallEtaleModelRingedSite B S hS F hF).IsPerfect M) :
    IsIso (RingedSite.derivedTensorHomDiagonal
      (smallEtaleModelRingedSite B S hS F hF) K L M)
```

**`AlgebraicGeometry.Space.isIso_derivedTensorHomDiagonal_of_isPerfect_tensorFactor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedTensorHomDiagonal.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedTensorHomDiagonal.lean#L185). The attribute's comment: “case (2): K perfect”.

> **Stacks 0E4Q case (2).** For objects `K`, `L`, `M` of `D(𝒪_X)` on an algebraic space `X`
> with the tensor factor `K` perfect, the canonical morphism of Stacks 0BYU
>
> `K ⊗^L_{𝒪_X} RSheafHom(M, L) ⟶ RSheafHom(M, K ⊗^L_{𝒪_X} L)`
>
> is an isomorphism. Nothing is assumed of `L` or `M`; neither side need have quasi-coherent
> cohomology.

```lean
theorem isIso_derivedTensorHomDiagonal_of_isPerfect_tensorFactor
    (K L M : DerivedCategory
      (SheafOfModules.{u}
        (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleModelRingedSite B S hS F hF).O)))
    (hK : (smallEtaleModelRingedSite B S hS F hF).IsPerfect K) :
    IsIso (RingedSite.derivedTensorHomDiagonal
      (smallEtaleModelRingedSite B S hS F hF) K L M)
```

**`AlgebraicGeometry.Space.isIso_derivedTensorHomDiagonal_of_isPseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedTensorHomDiagonal.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedTensorHomDiagonal.lean#L212). The attribute's comment: “case (3): M pseudo-coherent, L bounded below, K of finite Tor dimension”.

> **Stacks 0E4Q case (3).** For objects `K`, `L`, `M` of `D(𝒪_X)` on an algebraic space `X`
> with `M` pseudo-coherent, `L` cohomologically bounded below and `K` of finite Tor dimension,
> the canonical morphism of Stacks 0BYU
>
> `K ⊗^L_{𝒪_X} RSheafHom(M, L) ⟶ RSheafHom(M, K ⊗^L_{𝒪_X} L)`
>
> is an isomorphism.
>
> Nothing is assumed beyond the three conditions the source states; in particular
> quasi-coherence of the cohomology sheaves is not used. Like the two cases above, this
> specialises the corresponding part of Stacks 0ATN for an arbitrary ringed site —
> `AlgebraicGeometry.RingedSite.isIso_derivedTensorHomDiagonal_of_isPseudoCoherent` — to the
> model of the small étale ringed site of `X`.

```lean
theorem isIso_derivedTensorHomDiagonal_of_isPseudoCoherent
    (K L M : DerivedCategory
      (SheafOfModules.{u}
        (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleModelRingedSite B S hS F hF).O)))
    (hM : (smallEtaleModelRingedSite B S hS F hF).IsPseudoCoherent M)
    (hL : DerivedCategoryB.IsBoundedBelow L)
    (hK : Stacks.SheafOfModules.DerivedTensorProduct.HasFiniteTorDimension
      (Stacks.SheafOfModules.canonicalDerivedTensorProduct
        (smallEtaleModelRingedSite B S hS F hF)) K) :
    IsIso (RingedSite.derivedTensorHomDiagonal
      (smallEtaleModelRingedSite B S hS F hF) K L M)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 75.13, Tag 08HC](https://stacks.math.columbia.edu/tag/08HC)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
