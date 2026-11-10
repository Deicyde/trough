---
declaration: section
origin: cited
lean: AlgebraicGeometry.PushoutAlongClosedImmersionAndIntegralSituation, Stacks.Pushout.exists_affineOpens_preimage_eq, AlgebraicGeometry.pushoutAlongClosedImmersionAndIntegral, AlgebraicGeometry.pushoutSquare_isPullback, AlgebraicGeometry.pushoutInl_isIntegralHom, AlgebraicGeometry.pushoutInr_isClosedImmersion, AlgebraicGeometry.pushoutStructureSheaf_isPullback, AlgebraicGeometry.pushoutScheme_isSeparated
statement: formalized
proof: formalized
---

# 37.67 Pushouts in the category of schemes, II

Section 37.67 of the Stacks Project, [Tag 0ECH](https://stacks.math.columbia.edu/tag/0ECH). 9 tags here are carried by 32 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0ECI, a situation

[Tag 0ECI](https://stacks.math.columbia.edu/tag/0ECI) in the Stacks Project.

**`AlgebraicGeometry.PushoutAlongClosedImmersionAndIntegralSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/PushoutSituation.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/PushoutSituation.lean#L40).

> **Stacks Project, Tag 0ECI.** The standing situation for a pushout along a
> closed immersion and an integral morphism.

```lean
structure PushoutAlongClosedImmersionAndIntegralSituation
```

## Tag 0ECJ, a lemma

[Tag 0ECJ](https://stacks.math.columbia.edu/tag/0ECJ) in the Stacks Project.

**`Stacks.Pushout.exists_affineOpens_preimage_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Pushout/CompatibleAffines.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Pushout/CompatibleAffines.lean#L164).

> **Stacks Project, Tag 0ECJ.**  Let `i : Z ⟶ X` be a closed immersion and `j : Z ⟶ Y` an
> integral morphism such that every fibre of `j` maps under `i` into an affine open of `X`.  Then
> every `y : Y` has an affine open neighbourhood `V` whose preimage under `j` is the preimage under
> `i` of an affine open `U` of `X`.
>
> The argument of the source, run twice.  Shrinking `Y` around `y` makes `j ⁻¹ᵁ V₀` land inside
> `i ⁻¹ᵁ U₀`; separating the fibre by a basic open of `U₀` inside the open `W` with
> `i ⁻¹ᵁ W ≤ j ⁻¹ᵁ V₀` reverses that inclusion.  Shrinking a second time and pulling the resulting
> function on `V₀` back along the closed immersion makes the two preimages equal, because the basic
> open of the pullback of `g` is cut out of `i ⁻¹ᵁ U₁` by `j ⁻¹ᵁ (Y.basicOpen g)`.

```lean
theorem exists_affineOpens_preimage_eq (i : Z ⟶ X) (j : Z ⟶ Y) [IsClosedImmersion i]
    [IsIntegralHom j]
    (hfib : ∀ y : Y, ∃ U : X.Opens, IsAffineOpen U ∧ ∀ z : Z, j z = y → i z ∈ U) (y : Y) :
    ∃ (U : X.Opens) (V : Y.Opens), IsAffineOpen U ∧ IsAffineOpen V ∧ y ∈ V ∧
      i ⁻¹ᵁ U = j ⁻¹ᵁ V
```

## Tag 0E25, a proposition

[Tag 0E25](https://stacks.math.columbia.edu/tag/0E25) in the Stacks Project.

**`AlgebraicGeometry.pushoutAlongClosedImmersionAndIntegral`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Pushout/Gluing.lean, line 302](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Pushout/Gluing.lean#L302). The attribute's comment: “the pushout”.

> **Stacks Project, Tag 0E25.** The pushout along a closed immersion and an integral morphism
> exists as a scheme.

```lean
noncomputable def pushoutAlongClosedImmersionAndIntegral
    (s : PushoutAlongClosedImmersionAndIntegralSituation.{u}) :
    PushoutAlongClosedImmersionAndIntegral s
```

**`AlgebraicGeometry.pushoutSquare_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Pushout/Gluing.lean, line 333](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Pushout/Gluing.lean#L333). The attribute's comment: “the diagram is a fibre square”.

> **Stacks Project, Tag 0E25.** The pushout square is also a pullback square.

```lean
theorem pushoutSquare_isPullback
    (s : PushoutAlongClosedImmersionAndIntegralSituation.{u}) :
    IsPullback s.i s.j (pushoutInl s) (pushoutInr s)
```

**`AlgebraicGeometry.pushoutInl_isIntegralHom`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Pushout/Gluing.lean, line 340](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Pushout/Gluing.lean#L340). The attribute's comment: “the morphism a is integral”.

> **Stacks Project, Tag 0E25.** The canonical map from `X` to the pushout is integral.

```lean
instance pushoutInl_isIntegralHom
    (s : PushoutAlongClosedImmersionAndIntegralSituation.{u}) :
    IsIntegralHom (pushoutInl s)
```

**`AlgebraicGeometry.pushoutInr_isClosedImmersion`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Pushout/Gluing.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Pushout/Gluing.lean#L351). The attribute's comment: “the morphism b is a closed immersion”.

> **Stacks Project, Tag 0E25.** The canonical map from `Y` to the pushout is a closed
> immersion.

```lean
instance pushoutInr_isClosedImmersion
    (s : PushoutAlongClosedImmersionAndIntegralSituation.{u}) :
    IsClosedImmersion (pushoutInr s)
```

**`AlgebraicGeometry.pushoutStructureSheaf_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Pushout/Gluing.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Pushout/Gluing.lean#L366). The attribute's comment: “the structure sheaf”.

> **Stacks Project, Tag 0E25.** On every open of the pushout, its ring of sections is the fibre
> product of the rings of sections on `Y` and `X` over the corresponding ring on `Z`.
>
> These are the component squares, after applying `CategoryTheory.sheafToPresheaf`, of the source's
> square of sheaves of rings: its natural transformations have components `b.app U`, `a.app U`,
> `j.app (b ⁻¹ᵁ U)`, and the transported map `i.app (a ⁻¹ᵁ U)` occurring below.  The equivalence
> with the sheaf-level pullback is `CategoryTheory.IsPullback.iff_app` together with reflection of
> limits along the fully faithful `CategoryTheory.sheafToPresheaf`.

```lean
theorem pushoutStructureSheaf_isPullback
    (s : PushoutAlongClosedImmersionAndIntegralSituation.{u})
    (U : (pushoutScheme s).Opens) :
    let e : s.i ⁻¹ᵁ (pushoutInl s ⁻¹ᵁ U) =
        s.j ⁻¹ᵁ (pushoutInr s ⁻¹ᵁ U) :=
      congrArg (fun f : s.Z ⟶ pushoutScheme s ↦ f ⁻¹ᵁ U)
        (pushoutAlongClosedImmersionAndIntegral s).isPushout.w
    IsPullback (pushoutInr s |>.app U) (pushoutInl s |>.app U)
      (s.j.app (pushoutInr s ⁻¹ᵁ U))
      (s.i.app (pushoutInl s ⁻¹ᵁ U) ≫
        eqToHom (congrArg (fun V ↦ Γ(s.Z, V)) e))
```

## Tag 0E26, a lemma

[Tag 0E26](https://stacks.math.columbia.edu/tag/0E26) in the Stacks Project.

**`AlgebraicGeometry.pushoutScheme_isSeparated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Pushout/Separation.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Pushout/Separation.lean#L61). The attribute's comment: “separated”.

> **Stacks Project, Tag 0E26.** If both schemes being glued are separated, then the pushout
> along a closed immersion and an integral morphism is separated.

```lean
instance pushoutScheme_isSeparated
    (s : PushoutAlongClosedImmersionAndIntegralSituation.{u})
    [s.X.IsSeparated] [s.Y.IsSeparated] :
    (pushoutScheme s).IsSeparated
```

**`AlgebraicGeometry.pushoutToBase_isSeparated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Pushout/Separation.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Pushout/Separation.lean#L81). The attribute's comment: “separated_over_s”.

> **Stacks Project, Tag 0E26.** If both schemes being glued are separated over the base, then
> the pushout along a closed immersion and an integral morphism is separated over the base.

```lean
instance pushoutToBase_isSeparated
    (s : PushoutAlongClosedImmersionAndIntegralSituation.{u})
    [IsSeparated s.pX] [IsSeparated s.pY] :
    IsSeparated (pushoutToBase s)
```

**`AlgebraicGeometry.pushoutScheme_quasiSeparatedSpace`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Pushout/Separation.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Pushout/Separation.lean#L118). The attribute's comment: “quasi_separated”.

> **Stacks Project, Tag 0E26.** If both schemes being glued are quasi-separated, then the
> pushout along a closed immersion and an integral morphism is quasi-separated.

```lean
instance pushoutScheme_quasiSeparatedSpace
    (s : PushoutAlongClosedImmersionAndIntegralSituation.{u})
    [QuasiSeparatedSpace s.X] [QuasiSeparatedSpace s.Y] :
    QuasiSeparatedSpace (pushoutScheme s)
```

**`AlgebraicGeometry.pushoutToBase_quasiSeparated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Pushout/Separation.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Pushout/Separation.lean#L131). The attribute's comment: “quasi_separated_over_s”.

> **Stacks Project, Tag 0E26.** If both schemes being glued are quasi-separated over the
> base, then the pushout along a closed immersion and an integral morphism is quasi-separated
> over the base.

```lean
instance pushoutToBase_quasiSeparated
    (s : PushoutAlongClosedImmersionAndIntegralSituation.{u})
    [QuasiSeparated s.pX] [QuasiSeparated s.pY] :
    QuasiSeparated (pushoutToBase s)
```

## Tag 0E27, a lemma

[Tag 0E27](https://stacks.math.columbia.edu/tag/0E27) in the Stacks Project.

**`AlgebraicGeometry.pushoutToBase_locallyOfFiniteType`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Pushout/FiniteType.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Pushout/FiniteType.lean#L152).

> **Stacks Project, Tag 0E27.** In the standing situation of [Stacks Project, Tag 0ECI], if
> the base is locally Noetherian and `X`, `Y` and `Z` are locally of finite type over it, then the
> pushout `Y ⨿_Z X` of [Stacks Project, Tag 0E25] is locally of finite type over the base.

```lean
instance pushoutToBase_locallyOfFiniteType
    (s : PushoutAlongClosedImmersionAndIntegralSituation.{u})
    [IsLocallyNoetherian s.S]
    [LocallyOfFiniteType s.pX]
    [LocallyOfFiniteType s.pY]
    [LocallyOfFiniteType s.pZ] :
    LocallyOfFiniteType (pushoutToBase s)
```

## Tag 0ECK, a lemma

[Tag 0ECK](https://stacks.math.columbia.edu/tag/0ECK) in the Stacks Project.

**`AlgebraicGeometry.primedFiber_preimage_subset_affine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Pushout/CartesianDiagram.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Pushout/CartesianDiagram.lean#L142). The attribute's comment: “part (1)”.

> The primed span of a cartesian diagram satisfies the fibrewise affineness condition of a
> pushout situation: every fibre of `j'` maps under `i'` into a single affine open of `X'`.

```lean
theorem primedFiber_preimage_subset_affine
    (s : PushoutAlongClosedImmersionAndIntegralSituation.{u}) (d : CartesianDiagram s) :
    ∀ y : d.Y', ∃ U : d.X'.Opens, IsAffineOpen U ∧
      ∀ z : d.Z', d.j' z = y → d.i' z ∈ U
```

**`AlgebraicGeometry.pushoutMap_left_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Pushout/QuasiFiniteFunctoriality.lean, line 491](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Pushout/QuasiFiniteFunctoriality.lean#L491). The attribute's comment: “part (3), the X square”.

> **Stacks Project, Tag 0ECK, part (3).** The square relating the two canonical maps from `X`
> and `X'` to the two pushouts is cartesian.

```lean
theorem pushoutMap_left_isPullback
    (s : PushoutAlongClosedImmersionAndIntegralSituation.{u}) (d : CartesianDiagram s) :
    IsPullback (pushoutInl (inducedSituation s d)) d.f (pushoutMap s d) (pushoutInl s)
```

**`AlgebraicGeometry.pushoutMap_right_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Pushout/QuasiFiniteFunctoriality.lean, line 502](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Pushout/QuasiFiniteFunctoriality.lean#L502). The attribute's comment: “part (3), the Y square”.

> **Stacks Project, Tag 0ECK, part (3).** The square relating the two canonical maps from `Y`
> and `Y'` to the two pushouts is cartesian.

```lean
theorem pushoutMap_right_isPullback
    (s : PushoutAlongClosedImmersionAndIntegralSituation.{u}) (d : CartesianDiagram s) :
    IsPullback (pushoutInr (inducedSituation s d)) d.g (pushoutMap s d) (pushoutInr s)
```

**`AlgebraicGeometry.pushoutMap_isSeparated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Pushout/QuasiFiniteFunctoriality.lean, line 512](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Pushout/QuasiFiniteFunctoriality.lean#L512). The attribute's comment: “part (2), separated”.

> **Stacks Project, Tag 0ECK, part (2).** The induced morphism of pushouts is separated.

```lean
instance pushoutMap_isSeparated
    (s : PushoutAlongClosedImmersionAndIntegralSituation.{u}) (d : CartesianDiagram s) :
    IsSeparated (pushoutMap s d)
```

**`AlgebraicGeometry.pushoutMap_locallyOfFiniteType`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Pushout/QuasiFiniteFunctoriality.lean, line 537](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Pushout/QuasiFiniteFunctoriality.lean#L537). The attribute's comment: “part (2), locally of finite type”.

> **Stacks Project, Tag 0ECK, part (2).** The induced morphism of pushouts is locally of finite
> type.

```lean
instance pushoutMap_locallyOfFiniteType
    (s : PushoutAlongClosedImmersionAndIntegralSituation.{u}) (d : CartesianDiagram s) :
    LocallyOfFiniteType (pushoutMap s d)
```

**`AlgebraicGeometry.pushoutMap_locallyQuasiFinite`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Pushout/QuasiFiniteFunctoriality.lean, line 556](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Pushout/QuasiFiniteFunctoriality.lean#L556). The attribute's comment: “part (2), locally quasi-finite fibres”.

> **Stacks Project, Tag 0ECK, part (2).** The induced morphism of pushouts has locally
> quasi-finite fibres.

```lean
instance pushoutMap_locallyQuasiFinite
    (s : PushoutAlongClosedImmersionAndIntegralSituation.{u}) (d : CartesianDiagram s) :
    LocallyQuasiFinite (pushoutMap s d)
```

## Tag 0ECL, a lemma

[Tag 0ECL](https://stacks.math.columbia.edu/tag/0ECL) in the Stacks Project.

**`AlgebraicGeometry.flat_pushoutMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Pushout/FlatQuasiFiniteDescent.lean, line 302](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Pushout/FlatQuasiFiniteDescent.lean#L302). The attribute's comment: “flatness of the pushout map”.

> **Stacks Project, Tag 0ECL.** The morphism of pushouts induced by a cartesian triple whose
> three vertical morphisms are flat is flat.

```lean
theorem flat_pushoutMap (s : PushoutAlongClosedImmersionAndIntegralSituation.{u})
    (d : CartesianDiagram s) [Flat d.f] [Flat d.g] [Flat d.h] :
    Flat (pushoutMap s d)
```

**`AlgebraicGeometry.etale_pushoutMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Pushout/FlatQuasiFiniteDescent.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Pushout/FlatQuasiFiniteDescent.lean#L319). The attribute's comment: “étaleness of the pushout map”.

> **Stacks Project, Tag 0ECL.** The morphism of pushouts induced by a cartesian triple whose
> three vertical morphisms are étale is étale.

```lean
theorem etale_pushoutMap (s : PushoutAlongClosedImmersionAndIntegralSituation.{u})
    (d : CartesianDiagram s) [Etale d.f] [Etale d.g] [Etale d.h] :
    Etale (pushoutMap s d)
```

**`AlgebraicGeometry.flatTriple_pushout_equivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Pushout/FlatQuasiFiniteDescent.lean, line 815](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Pushout/FlatQuasiFiniteDescent.lean#L815). The attribute's comment: “flat equivalence”.

> **Stacks Project, Tag 0ECL.** The pushout construction is an equivalence from the cartesian
> triples with flat vertical morphisms to the flat, separated, locally quasi-finite schemes over
> the pushout.  On objects it is the pushout of the triple together with its canonical morphism to
> `Y ⨿_Z X`, and on morphisms it is the morphism of pushouts induced by the three components.

```lean
theorem flatTriple_pushout_equivalence
    (s : PushoutAlongClosedImmersionAndIntegralSituation.{u}) :
    ∃ F : FlatCartesianTriple s ⥤ flatSchemesOver s,
      F.IsEquivalence ∧
      (∀ d, (F.obj d).1 = Over.mk (pushoutMap s d.1)) ∧
      (∀ (d e : FlatCartesianTriple s) (m : CartesianTripleHom d.1 e.1),
        ∃ k : pushoutScheme (inducedSituation s d.1) ⟶
            pushoutScheme (inducedSituation s e.1),
          HEq (((F.map m).1).left) k ∧
          (pushoutInl (inducedSituation s d.1) ≫ k =
            m.x ≫ pushoutInl (inducedSituation s e.1)) ∧
          (pushoutInr (inducedSituation s d.1) ≫ k =
            m.y ≫ pushoutInr (inducedSituation s e.1)))
```

**`AlgebraicGeometry.etaleTriple_pushout_equivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Pushout/FlatQuasiFiniteDescent.lean, line 846](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Pushout/FlatQuasiFiniteDescent.lean#L846). The attribute's comment: “étale equivalence”.

> **Stacks Project, Tag 0ECL.** The pushout construction is an equivalence from the cartesian
> triples with étale vertical morphisms to the étale, separated, locally quasi-finite schemes over
> the pushout.  On objects it is the pushout of the triple together with its canonical morphism to
> `Y ⨿_Z X`, and on morphisms it is the morphism of pushouts induced by the three components.

```lean
theorem etaleTriple_pushout_equivalence
    (s : PushoutAlongClosedImmersionAndIntegralSituation.{u}) :
    ∃ F : EtaleCartesianTriple s ⥤ etaleSchemesOver s,
      F.IsEquivalence ∧
      (∀ d, (F.obj d).1 = Over.mk (pushoutMap s d.1)) ∧
      (∀ (d e : EtaleCartesianTriple s) (m : CartesianTripleHom d.1 e.1),
        ∃ k : pushoutScheme (inducedSituation s d.1) ⟶
            pushoutScheme (inducedSituation s e.1),
          HEq (((F.map m).1).left) k ∧
          (pushoutInl (inducedSituation s d.1) ≫ k =
            m.x ≫ pushoutInl (inducedSituation s e.1)) ∧
          (pushoutInr (inducedSituation s d.1) ≫ k =
            m.y ≫ pushoutInr (inducedSituation s e.1)))
```

## Tag 0B7M, a lemma

[Tag 0B7M](https://stacks.math.columbia.edu/tag/0B7M) in the Stacks Project.

**`AlgebraicGeometry.hasPushout_of_isClosedImmersion`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Pushout/ClosedImmersions.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Pushout/ClosedImmersions.lean#L111). The attribute's comment: “the pushout exists”.

> **[Stacks, Tag 0B7M].** The pushout of two closed immersions of schemes exists in the
> category of schemes.

```lean
instance hasPushout_of_isClosedImmersion {Z X Y : Scheme.{u}} (i : Z ⟶ X) (j : Z ⟶ Y)
    [IsClosedImmersion i] [IsClosedImmersion j] : HasPushout i j
```

**`AlgebraicGeometry.isPullback_pushout_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Pushout/ClosedImmersions.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Pushout/ClosedImmersions.lean#L119). The attribute's comment: “the diagram is a fibre square”.

> **[Stacks, Tag 0B7M].** The defining pushout square of two closed immersions of schemes is
> also a fibre square.

```lean
theorem isPullback_pushout_of_isClosedImmersion {Z X Y : Scheme.{u}} (i : Z ⟶ X) (j : Z ⟶ Y)
    [IsClosedImmersion i] [IsClosedImmersion j] :
    IsPullback i j (pushout.inl i j) (pushout.inr i j)
```

**`AlgebraicGeometry.pushout_inl_isClosedImmersion`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Pushout/ClosedImmersions.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Pushout/ClosedImmersions.lean#L142). The attribute's comment: “the morphism a is a closed immersion”.

> **[Stacks, Tag 0B7M].** The canonical map `a : X ⟶ Y ⨿_Z X` out of the first scheme is a
> closed immersion.

```lean
instance pushout_inl_isClosedImmersion {Z X Y : Scheme.{u}} (i : Z ⟶ X) (j : Z ⟶ Y)
    [IsClosedImmersion i] [IsClosedImmersion j] : IsClosedImmersion (pushout.inl i j)
```

**`AlgebraicGeometry.pushout_inr_isClosedImmersion`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Pushout/ClosedImmersions.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Pushout/ClosedImmersions.lean#L157). The attribute's comment: “the morphism b is a closed immersion”.

> **[Stacks, Tag 0B7M].** The canonical map `b : Y ⟶ Y ⨿_Z X` out of the second scheme is a
> closed immersion.

```lean
instance pushout_inr_isClosedImmersion {Z X Y : Scheme.{u}} (i : Z ⟶ X) (j : Z ⟶ Y)
    [IsClosedImmersion i] [IsClosedImmersion j] : IsClosedImmersion (pushout.inr i j)
```

**`AlgebraicGeometry.pushout_structureSheafModule_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Pushout/ClosedImmersions.lean, line 321](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Pushout/ClosedImmersions.lean#L321). The attribute's comment: “the short exact sequence”.

> **[Stacks, Tag 0B7M].** For two closed immersions `i : Z ⟶ X` and `j : Z ⟶ Y`, the
> canonical sequence
>
> `0 ⟶ 𝒪_(Y ⨿_Z X) ⟶ a_* 𝒪_X ⊕ b_* 𝒪_Y ⟶ c_* 𝒪_Z ⟶ 0`
>
> of modules over the structure sheaf of the pushout is short exact, where `a` and `b` are the
> two canonical maps into the pushout and `c = a ∘ i = b ∘ j`.

```lean
theorem pushout_structureSheafModule_shortExact {Z X Y : Scheme.{u}} (i : Z ⟶ X) (j : Z ⟶ Y)
    [IsClosedImmersion i] [IsClosedImmersion j] :
    ∃ zero : pushoutStructureSheafModuleToBiprod i j ≫ pushoutBiprodToIntersection i j = 0,
      (ShortComplex.mk (pushoutStructureSheafModuleToBiprod i j)
        (pushoutBiprodToIntersection i j) zero).ShortExact
```

## Tag 0CYY, a lemma

[Tag 0CYY](https://stacks.math.columbia.edu/tag/0CYY) in the Stacks Project.

**`AlgebraicGeometry.induced_locallyOfFiniteType_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Pushout/InducedFiniteType.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Pushout/InducedFiniteType.lean#L287). The attribute's comment: “locally_of_finite_type”.

> In the situation of two closed immersions `i : Z ⟶ X` and `j : Z ⟶ Y`, morphisms
> `f : X' ⟶ X` and `g : Y' ⟶ Y`, and an isomorphism over `Z` between the two inverse images of `Z`,
> the induced morphism from the glued scheme `X' ⨿_{X' ×_X Z} Y'` to the pushout `Y ⨿_Z X` is
> locally of finite type if and only if `f` and `g` are locally of finite type.

```lean
theorem induced_locallyOfFiniteType_iff (S : CompatiblePushoutMorphismSituation.{u}) :
    LocallyOfFiniteType S.induced ↔
      LocallyOfFiniteType S.f ∧ LocallyOfFiniteType S.g
```

**`AlgebraicGeometry.flat_induced_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Pushout/InducedFlat.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Pushout/InducedFlat.lean#L261). The attribute's comment: “flat”.

> In the situation of `AlgebraicGeometry.CompatiblePushoutMorphismSituation`, the induced
> morphism between the two pushouts is flat if and only if both morphisms on the pieces are flat.

```lean
theorem flat_induced_iff (S : CompatiblePushoutMorphismSituation.{u}) :
    Flat S.induced ↔ Flat S.f ∧ Flat S.g
```

**`AlgebraicGeometry.flat_locallyOfFinitePresentation_induced_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Pushout/InducedFlat.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Pushout/InducedFlat.lean#L280). The attribute's comment: “flat_locally_of_finite_presentation”.

> In the situation of `AlgebraicGeometry.CompatiblePushoutMorphismSituation`, the induced
> morphism between the two pushouts is flat and locally of finite presentation if and only if both
> morphisms on the pieces are flat and locally of finite presentation.

```lean
theorem flat_locallyOfFinitePresentation_induced_iff
    (S : CompatiblePushoutMorphismSituation.{u}) :
    (Flat S.induced ∧ LocallyOfFinitePresentation S.induced) ↔
      ((Flat S.f ∧ LocallyOfFinitePresentation S.f) ∧
        (Flat S.g ∧ LocallyOfFinitePresentation S.g))
```

**`AlgebraicGeometry.etale_induced_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Pushout/InducedSmooth.lean, line 329](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Pushout/InducedSmooth.lean#L329). The attribute's comment: “etale”.

> In a compatible morphism of pushouts along closed immersions, the induced morphism is étale if
> and only if the morphisms on both pieces are étale.

```lean
theorem etale_induced_iff (S : CompatiblePushoutMorphismSituation.{u}) :
    Etale S.induced ↔ (Etale S.f ∧ Etale S.g)
```

**`AlgebraicGeometry.smooth_induced_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Pushout/InducedSmooth.lean, line 340](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Pushout/InducedSmooth.lean#L340). The attribute's comment: “smooth”.

> In a compatible morphism of pushouts along closed immersions, the induced morphism is smooth
> if and only if the morphisms on both pieces are smooth.

```lean
theorem smooth_induced_iff (S : CompatiblePushoutMorphismSituation.{u}) :
    Smooth S.induced ↔ (Smooth S.f ∧ Smooth S.g)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.67, Tag 0ECH](https://stacks.math.columbia.edu/tag/0ECH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
