---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.RestrictionPair, AlgebraicGeometry.Space.restrictionOfScalars, AlgebraicGeometry.Space.restrictionOfScalarsHomEquiv, AlgebraicGeometry.Space.isSheaf_restrictionOfScalars, AlgebraicGeometry.Space.baseChangeFiberProductMap, AlgebraicGeometry.Space.isPullback_baseChangeFiberProductMap, AlgebraicGeometry.Space.restrictionOfScalars_baseChange, AlgebraicGeometry.Space.restrictionOfScalars_baseChange_fiberProduct
statement: formalized
proof: formalized
---

# 97.11 Restriction of scalars

Section 97.11 of the Stacks Project, [Tag 05Y8](https://stacks.math.columbia.edu/tag/05Y8). 7 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05Y9, an equation

[Tag 05Y9](https://stacks.math.columbia.edu/tag/05Y9) in the Stacks Project.

**`AlgebraicGeometry.Space.RestrictionPair`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/RestrictionOfScalars.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/RestrictionOfScalars.lean#L77). The attribute's comment: “the pair (a, b) displayed by the diagram”.

> A pair `(a, b)` for the restriction of scalars of `x : X ⟶ Z` along
> `z : Z ⟶ Q` at a test presheaf `T`: a morphism `a : T ⟶ Q` together with a morphism
> `b : T ×_{a, Q} Z ⟶ X` lying over `Z`.
>
> This is a pair of `AlgebraicGeometry.Space.RelativeMorphism` for `z` and `x ≫ z` subject to the
> stronger requirement that `b` lie over `Z` and not merely over `Q`; see
> `AlgebraicGeometry.Space.restrictionPairEquivSubtype`.

```lean
structure RestrictionPair {X Z Q : AlgebraicSpaces B S hS} (x : X ⟶ Z) (z : Z ⟶ Q)
    (T : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
```

## Tag 05YA, an equation

[Tag 05YA](https://stacks.math.columbia.edu/tag/05YA) in the Stacks Project.

**`AlgebraicGeometry.Space.restrictionOfScalars`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/RestrictionOfScalars.lean, line 304](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/RestrictionOfScalars.lean#L304).

> The restriction of scalars `Res_{Z/Q}(X)` of `x : X ⟶ Z` along `z : Z ⟶ Q`: the functor of
> points on the big fppf site of `S` whose sections over a scheme `T` are the pairs `(a, b)` of
> Stacks 05Y9, with its projection to `Q` and with restriction given by base change.

```lean
noncomputable def restrictionOfScalars {X Z Q : AlgebraicSpaces B S hS} (x : X ⟶ Z)
    (z : Z ⟶ Q) : RestrictionOfScalarsConstruction B S hS x z
```

## Tag 05YB, a lemma

[Tag 05YB](https://stacks.math.columbia.edu/tag/05YB) in the Stacks Project.

**`AlgebraicGeometry.Space.restrictionOfScalarsHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/RestrictionOfScalarsHom.lean, line 340](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/RestrictionOfScalarsHom.lean#L340). The attribute's comment: “the functor of points”.

> **Stacks 05YB.** Morphisms from an algebraic space `T` into the restriction of scalars
> `Res_{Z/Q}(X)` of `x : X ⟶ Z` along `z : Z ⟶ Q` are the pairs `(a, b)` of Stacks 05Y9 at `T`:
> a morphism `a : T ⟶ Q` together with a morphism `b : T ×_{a, Q} Z ⟶ X` over `Z`.
>
> The bijection is characterized by the two properties recorded with it: its value at `v` base
> changes, along every scheme-valued point `i` of `T`, to the pair that Stacks 05YA attaches to
> `i ≫ v`; and it is natural in `T`.

```lean
noncomputable def restrictionOfScalarsHomEquiv (x : X ⟶ Z) (z : Z ⟶ Q) :
    {e : ∀ T : AlgebraicSpaces B S hS,
        (T.obj ⟶ (restrictionOfScalars B S hS x z).presheaf) ≃
          RestrictionPair B S hS x z T.obj //
      (∀ (T : AlgebraicSpaces B S hS) (U : BigFppfOver B S hS) (i : yoneda.obj U ⟶ T.obj)
          (v : T.obj ⟶ (restrictionOfScalars B S hS x z).presheaf),
        RestrictionPair.IsPullbackAlong i (e T v)
          ((restrictionOfScalars B S hS x z).pairEquiv U (yonedaEquiv (i ≫ v)))) ∧
      (∀ (T T' : AlgebraicSpaces B S hS) (f : T' ⟶ T)
          (v : T.obj ⟶ (restrictionOfScalars B S hS x z).presheaf),
        RestrictionPair.IsPullbackAlong f.hom (e T v) (e T' (f.hom ≫ v)))}
```

**`AlgebraicGeometry.Space.isSheaf_restrictionOfScalars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/RestrictionOfScalarsSheaf.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/RestrictionOfScalarsSheaf.lean#L64). The attribute's comment: “part (1): `Res_{Z/B}(X)` is a sheaf on the big fppf site of `S`”.

> **Stacks 05YB**, part (1). For morphisms `x : X ⟶ Z` and `z : Z ⟶ Q` of algebraic spaces
> over `S`, the restriction of scalars `Res_{Z/Q}(X)` of Stacks 05YA is a sheaf on the big fppf
> site of `S`.
>
> A pair `(a, b)` of Stacks 05Y9 is a pair of Stacks 05Y1 whose second component lies over `Z`,
> and the cartesian square of Stacks 05YE presents `Res_{Z/Q}(X)` as the fibre product of
> `Mor_Q(Z, X)` and `Q` over `Mor_Q(Z, Z)`. The descent of pairs the source carries out is
> therefore already done: it is part (1) of Stacks 05Y3 for the two relative morphism functors,
> and the fibre product of sheaves of types is a sheaf.

```lean
theorem isSheaf_restrictionOfScalars {X Z Q : AlgebraicSpaces B S hS} (x : X ⟶ Z) (z : Z ⟶ Q) :
    Presheaf.IsSheaf (BigFppfOver.topology B S hS)
      (restrictionOfScalars B S hS x z).presheaf
```

## Tag 05YC, a lemma

[Tag 05YC](https://stacks.math.columbia.edu/tag/05YC) in the Stacks Project.

**`AlgebraicGeometry.Space.baseChangeFiberProductMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/RestrictionOfScalarsBaseChange.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/RestrictionOfScalarsBaseChange.lean#L126). The attribute's comment: “the base-changed morphism”.

> **Stacks 05YC.** The base change `Q' ×_Q X ⟶ Q' ×_Q Z` of a morphism `x : X ⟶ Z` of
> algebraic spaces over `z : Z ⟶ Q` along a morphism `b : Q' ⟶ Q`, for the chosen fibre products
> of Stacks 02X2. It is the identity on the first factor and `x` on the second.

```lean
noncomputable def baseChangeFiberProductMap {X Z Q Q' : AlgebraicSpaces B S hS} (x : X ⟶ Z)
    (z : Z ⟶ Q) (b : Q' ⟶ Q) :
    AlgebraicSpaces.fiberProduct B S hS b (x ≫ z) ⟶ AlgebraicSpaces.fiberProduct B S hS b z
```

**`AlgebraicGeometry.Space.isPullback_baseChangeFiberProductMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/RestrictionOfScalarsBaseChange.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/RestrictionOfScalarsBaseChange.lean#L168). The attribute's comment: “the base-changed morphism as a fibre product”.

> **Stacks 05YC.** The base-changed morphism exhibits `Q' ×_Q X` as `(Q' ×_Q Z) ×_Z X`. This
> is the form in which `AlgebraicGeometry.Space.restrictionOfScalars_baseChange` asks for the
> base change of `x`.

```lean
theorem isPullback_baseChangeFiberProductMap :
    IsPullback (baseChangeFiberProductMap B S hS x z b).hom
      (pullback.snd b.hom (x ≫ z).hom) (pullback.snd b.hom z.hom) x.hom
```

**`AlgebraicGeometry.Space.restrictionOfScalars_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/RestrictionOfScalarsBaseChange.lean, line 472](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/RestrictionOfScalarsBaseChange.lean#L472). The attribute's comment: “the base-change identification”.

> **Stacks 05YC.** Let `x : X ⟶ Z` and `z : Z ⟶ Q` be morphisms of algebraic spaces over `S`
> and let `b : Q' ⟶ Q` be a morphism of algebraic spaces over `S`. Let `z' : Z' ⟶ Q'`, `c : Z' ⟶ Z`
> exhibit `Z'` as the base change `Q' ×_Q Z`, and let `x' : X' ⟶ Z'`, `e : X' ⟶ X` exhibit `X'` as
> the base change `Z' ×_Z X`, so that `X' = Q' ×_Q X`. Then
>
> ```text
> Res_{Z'/Q'}(X')  =  Q' ×_Q Res_{Z/Q}(X)
> ```
>
> as presheaves on the big fppf site of `S`: there is an isomorphism compatible with the
> projections to `Q'`, which on sections carries the pair of Stacks 05Y9 of a section of
> `Res_{Z'/Q'}(X')` to its base change
> `AlgebraicGeometry.Space.RestrictionPair.baseChange`.
>
> For the chosen fibre products of Stacks 02X2 the two hypotheses are
> `AlgebraicGeometry.Space.isPullback_hom_fiberProduct` and
> `AlgebraicGeometry.Space.isPullback_baseChangeFiberProductMap`; that instance is
> `AlgebraicGeometry.Space.restrictionOfScalars_baseChange_fiberProduct`.

```lean
theorem restrictionOfScalars_baseChange :
    ∃ i : r'.presheaf ≅ pullback b.hom r.projection,
      i.hom ≫ pullback.fst b.hom r.projection = r'.projection ∧
        ∀ (T : BigFppfOver B S hS) (v : r'.presheaf.obj (op T)),
          r.pairEquiv T ((i.hom ≫ pullback.snd b.hom r.projection).app (op T) v) =
            (r'.pairEquiv T v).baseChange hZ hX
```

**`AlgebraicGeometry.Space.restrictionOfScalars_baseChange_fiberProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/RestrictionOfScalarsBaseChange.lean, line 506](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/RestrictionOfScalarsBaseChange.lean#L506). The attribute's comment: “the base-change identification for the chosen fibre products”.

> **Stacks 05YC.** The form of `AlgebraicGeometry.Space.restrictionOfScalars_baseChange` for
> the chosen fibre products of Stacks 02X2: with `Z' = Q' ×_Q Z` and `X' = Q' ×_Q X` those fibre
> products and `x' : X' ⟶ Z'` the base-changed morphism
> `AlgebraicGeometry.Space.baseChangeFiberProductMap`,
>
> ```text
> Res_{Z'/Q'}(X')  =  Q' ×_Q Res_{Z/Q}(X)
> ```
>
> as presheaves on the big fppf site of `S`, compatibly with the projections to `Q'`.

```lean
theorem restrictionOfScalars_baseChange_fiberProduct {X Z Q Q' : AlgebraicSpaces B S hS}
    (x : X ⟶ Z) (z : Z ⟶ Q) (b : Q' ⟶ Q)
    (r : RestrictionOfScalarsConstruction B S hS x z)
    (r' : RestrictionOfScalarsConstruction B S hS (baseChangeFiberProductMap B S hS x z b)
      (ObjectProperty.homMk (pullback.fst b.hom z.hom) :
        AlgebraicSpaces.fiberProduct B S hS b z ⟶ Q')) :
    ∃ i : r'.presheaf ≅ pullback b.hom r.projection,
      i.hom ≫ pullback.fst b.hom r.projection = r'.projection ∧
        ∀ (T : BigFppfOver B S hS) (v : r'.presheaf.obj (op T)),
          r.pairEquiv T ((i.hom ≫ pullback.snd b.hom r.projection).app (op T) v) =
            (r'.pairEquiv T v).baseChange (isPullback_hom_fiberProduct B S hS b z)
              (isPullback_baseChangeFiberProductMap B S hS x z b)
```

## Tag 05YD, a lemma

[Tag 05YD](https://stacks.math.columbia.edu/tag/05YD) in the Stacks Project.

**`AlgebraicGeometry.Space.isSurjective_restrictionOfScalarsMap_of_isFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ChartComparisonAssembly.lean, line 426](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ChartComparisonAssembly.lean#L426). The attribute's comment: “surjective, given `X' ⟶ X` surjective: at the hypotheses of the source, with nothing carried”.

> **Stacks 05YD, third conclusion, at the hypotheses of the source.**  Let
> `X' → X → Z → Q` be morphisms of algebraic spaces over `S` with `X' → X` étale and surjective
> and `Z → Q` finite locally free.  Then `Res_{Z/Q}(X') → Res_{Z/Q}(X)` is surjective.
>
> This is `AlgebraicGeometry.Space.isSurjective_restrictionOfScalarsMap` with its hypothesis
> `h05XQ` discharged by `AlgebraicGeometry.Space.isFibreSectionsSurjective`.  It is stated here
> rather than beside that theorem because
> `StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartLocalizationBaseChange.lean`, which the
> chart comparison of Stacks 03ZU is built on, already imports the file where it lives.

```lean
theorem isSurjective_restrictionOfScalarsMap_of_isFiniteLocallyFree
    {X' X Z Q : AlgebraicSpaces B S hS} {x' : X' ⟶ Z} {x : X ⟶ Z} (g : X' ⟶ X)
    (hg : g ≫ x = x') (z : Z ⟶ Q)
    (hg_etale : IsEtale B S hS g.hom) (hg_surjective : IsSurjective B S hS g.hom)
    (hz : IsFiniteLocallyFree B S hS z) :
    IsSurjective B S hS (restrictionOfScalarsMap g hg z).1
```

**`AlgebraicGeometry.Space.isRepresentableByAlgebraicSpaces_restrictionOfScalarsMap_of_isFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FibreSectionsAlgebraicEtale.lean, line 358](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FibreSectionsAlgebraicEtale.lean#L358). The attribute's comment: “representable by algebraic spaces: at the hypotheses of the source, with nothing carried”.

> **Stacks 05YD, first conclusion, at the hypotheses of the source.** Let `X' → X → Z → Q` be
> morphisms of algebraic spaces over `S` with `X' → X` étale and `Z → Q` finite locally free. Then
> `Res_{Z/Q}(X') → Res_{Z/Q}(X)` is representable by algebraic spaces.

```lean
theorem isRepresentableByAlgebraicSpaces_restrictionOfScalarsMap_of_isFiniteLocallyFree
    {X' X Z Q : AlgebraicSpaces B S hS} {x' : X' ⟶ Z} {x : X ⟶ Z} (g : X' ⟶ X)
    (hg : g ≫ x = x') (z : Z ⟶ Q) (hg_etale : IsEtale B S hS g.hom)
    (hz : IsFiniteLocallyFree B S hS z) :
    IsRepresentableByAlgebraicSpaces B S hS (restrictionOfScalarsMap g hg z).1
```

**`AlgebraicGeometry.Space.hasProperty_isEtale_restrictionOfScalarsMap_of_isFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FibreSectionsAlgebraicEtale.lean, line 370](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FibreSectionsAlgebraicEtale.lean#L370). The attribute's comment: “étale: at the hypotheses of the source, with nothing carried”.

> **Stacks 05YD, second conclusion, at the hypotheses of the source.** In the situation of
> `isRepresentableByAlgebraicSpaces_restrictionOfScalarsMap_of_isFiniteLocallyFree`,
> the morphism `Res_{Z/Q}(X') → Res_{Z/Q}(X)` is étale.

```lean
theorem hasProperty_isEtale_restrictionOfScalarsMap_of_isFiniteLocallyFree
    {X' X Z Q : AlgebraicSpaces B S hS} {x' : X' ⟶ Z} {x : X ⟶ Z} (g : X' ⟶ X)
    (hg : g ≫ x = x') (z : Z ⟶ Q) (hg_etale : IsEtale B S hS g.hom)
    (hz : IsFiniteLocallyFree B S hS z) :
    HasProperty B S hS (fun _ _ f => IsEtale B S hS f.hom) (restrictionOfScalarsMap g hg z).1
      (isRepresentableByAlgebraicSpaces_restrictionOfScalarsMap_of_isFiniteLocallyFree B S hS g hg
        z hg_etale hz)
```

## Tag 05YE, a lemma

[Tag 05YE](https://stacks.math.columbia.edu/tag/05YE) in the Stacks Project.

**`AlgebraicGeometry.Space.isPullback_restrictionOfScalars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/RestrictionOfScalarsCartesian.lean, line 407](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/RestrictionOfScalarsCartesian.lean#L407). The attribute's comment: “the cartesian square of presheaves on the big fppf site”.

> The square
>
> ```text
> Mor_Q(Z, X) ⟶ Mor_Q(Z, Z)
>      ↑              ↑ id_Z
> Res_{Z/Q}(X) ⟶     Q
> ```
>
> of presheaves on the big fppf site of `S` is cartesian: the restriction of scalars of `x : X ⟶ Z`
> along `z : Z ⟶ Q` is the fibre product of `Mor_Q(Z, X)` and `Q` over `Mor_Q(Z, Z)`, where the
> morphism from `Q` picks out the identity endomorphism of `Z`.

```lean
theorem isPullback_restrictionOfScalars {X Z Q : AlgebraicSpaces B S hS} {x : X ⟶ Z} {z : Z ⟶ Q}
    (R : RestrictionOfScalarsConstruction B S hS x z)
    (HX : RelativeHomConstruction B S hS Z.obj X.obj Q.obj z.hom (x.hom ≫ z.hom))
    (HZ : RelativeHomConstruction B S hS Z.obj Z.obj Q.obj z.hom z.hom) :
    IsPullback (restrictionOfScalarsToRelativeHom R HX) R.projection
      (relativeHomPostcompose HX HZ x.hom rfl) (relativeHomIdentity HZ)
```

**`AlgebraicGeometry.Space.isPullback_restrictionOfScalars_relativeHomData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/RestrictionOfScalarsCartesian.lean, line 489](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/RestrictionOfScalarsCartesian.lean#L489). The attribute's comment: “the cartesian square, for the functors of Stacks 05Y2 and 05YA”.

> The square of `AlgebraicGeometry.Space.isPullback_restrictionOfScalars` is cartesian for the
> relative morphism functor of Stacks 05Y2 and the restriction of scalars of Stacks 05YA.

```lean
theorem isPullback_restrictionOfScalars_relativeHomData {X Z Q : AlgebraicSpaces B S hS}
    (x : X ⟶ Z) (z : Z ⟶ Q) :
    IsPullback
      (restrictionOfScalarsToRelativeHom (restrictionOfScalars B S hS x z)
        (relativeHomData B S hS Z.obj X.obj Q.obj z.hom (x.hom ≫ z.hom) Z.property X.property
          Q.property))
      (restrictionOfScalars B S hS x z).projection
      (relativeHomPostcompose
        (relativeHomData B S hS Z.obj X.obj Q.obj z.hom (x.hom ≫ z.hom) Z.property X.property
          Q.property)
        (relativeHomData B S hS Z.obj Z.obj Q.obj z.hom z.hom Z.property Z.property Q.property)
        x.hom rfl)
      (relativeHomIdentity
        (relativeHomData B S hS Z.obj Z.obj Q.obj z.hom z.hom Z.property Z.property Q.property))
```

## Tag 05YF, a proposition

[Tag 05YF](https://stacks.math.columbia.edu/tag/05YF) in the Stacks Project.

**`AlgebraicGeometry.Space.isAlgebraicSpace_restrictionOfScalars_of_isFiniteLocallyFree_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FibreSectionsAlgebraicEtale.lean, line 487](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FibreSectionsAlgebraicEtale.lean#L487). The attribute's comment: “at the hypotheses of the source, with nothing carried”.

> **Stacks 05YF, at the hypotheses of the source.** Let `x : X ⟶ Z` and `z : Z ⟶ Q` be
> morphisms of algebraic spaces over `S` with `z` finite locally free. Then the restriction of
> scalars `Res_{Z/Q}(X)` of Stacks 05YA is an algebraic space over `S`.

```lean
theorem isAlgebraicSpace_restrictionOfScalars_of_isFiniteLocallyFree_source
    {X Z Q : AlgebraicSpaces B S hS} (x : X ⟶ Z) (z : Z ⟶ Q)
    (hz : IsFiniteLocallyFree B S hS z) :
    IsAlgebraicSpace B S hS (restrictionOfScalars B S hS x z).presheaf
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 97.11, Tag 05Y8](https://stacks.math.columbia.edu/tag/05Y8)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
