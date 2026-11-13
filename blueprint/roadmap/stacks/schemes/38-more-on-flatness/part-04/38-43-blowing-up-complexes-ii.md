---
declaration: section
origin: cited
lean: AlgebraicGeometry.ComplexAndDivisorSituation, AlgebraicGeometry.ComplexAndDivisorSituation.AffineChart.restrict, AlgebraicGeometry.ComplexAndDivisorSituation.AffineChart.map_determinantalIdeal, AlgebraicGeometry.ComplexAndDivisorSituation.AffineChart.pullback, AlgebraicGeometry.ComplexAndDivisorSituation.isGoodTriple_pullback, AlgebraicGeometry.RingedSpace.KFlatDerivedPullback.isPerfect_uniqFunctor_obj, AlgebraicGeometry.ComplexAndDivisorSituation.AffineChart.pullback_determinantalIdeal, AlgebraicGeometry.ComplexAndDivisorSituation.isPerfect_derivedEtaData_obj
statement: formalized
proof: formalized
---

# 38.43 Blowing up complexes, II

Section 38.43 of the Stacks Project, [Tag 0F8R](https://stacks.math.columbia.edu/tag/0F8R). 14 tags here are carried by 52 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0F8S, a situation

[Tag 0F8S](https://stacks.math.columbia.edu/tag/0F8S) in the Stacks Project.

**`AlgebraicGeometry.ComplexAndDivisorSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/ComplexAndDivisor.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/ComplexAndDivisor.lean#L43).

> **Stacks Project, Tag 0F8S.** The standing situation of a perfect derived object on a
> scheme together with an effective Cartier divisor on that scheme.

```lean
structure ComplexAndDivisorSituation
```

## Tag 0F8T, a lemma

[Tag 0F8T](https://stacks.math.columbia.edu/tag/0F8T) in the Stacks Project.

**`AlgebraicGeometry.ComplexAndDivisorSituation.AffineChart.restrict`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/AffineChartRestrict.lean, line 291](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/AffineChartRestrict.lean#L291). The attribute's comment: “part (1) in the case `h = 𝟙 X`: the restriction of an affine chart to a smaller affine open `V ⊆ U` is an affine chart, with representing complex `M^• ⊗_A Γ(X, V)`. The case of a general `h` is AlgebraicGeometry.ComplexAndDivisorSituation.AffineChart.pullback in StacksFrontier.AlgebraicGeometry.Flatness.BlowUpSquare.ChartPullback, which carries the tag too.”.

> **Stacks tag 0F8T, part (1), for the inclusion of an affine open into a chart.**  An affine
> chart `(U, A, f, M^•)` for a triple `(X, D, M)` as in Situation 0F8S restricts to an affine chart
> over any affine open `V ⊆ U`: its equation is the restriction `f|_V`, and its bounded complex of
> finite free modules is the base change `M^• ⊗_A Γ(X, V)`, i.e. the complex whose differentials
> are the entrywise images of those of `M^•` under `A ⟶ Γ(X, V)`.
>
> That `f|_V` is again a nonzerodivisor is
> `AlgebraicGeometry.IsAffineOpen.isRegular_presheaf_map_of_le`, the restriction between affine
> opens being flat; that it cuts out `D ∩ V` is
> `AlgebraicGeometry.Scheme.IdealSheafData.map_ideal`; and that `M^• ⊗_A Γ(X, V)` represents the
> restriction of `M` is `restrictRepresentsIso`.

```lean
def restrict (C : AffineChart S) (V : S.X.affineOpens)
    (hle : (V : S.X.Opens) ≤ (C.U : S.X.Opens)) : AffineChart S
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.AffineChart.map_determinantalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/ChartBaseChange.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/ChartBaseChange.lean#L59). The attribute's comment: “the determinantal ideals of an affine chart under base change”.

> **Stacks Project, Tag 0F8T, second assertion.** For an affine chart `(U, A, f, M^•)` and a
> ring map `φ : A ⟶ B`, the ideal generated in `B` by the determinantal ideal `I_i(M^•, f)` is the
> determinantal ideal `I_i(M^• ⊗_A B, φ f)` of the base-changed chart data.

```lean
public theorem map_determinantalIdeal (C : AffineChart S) {B : Type u} [CommRing B]
    (φ : Γ(S.X, C.U) →+* B) (i : ℤ) :
    Ideal.map φ (C.determinantalIdeal i) = idealI (C.complex.baseChange φ) (φ C.f) i
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.AffineChart.pullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/ChartPullback.lean, line 337](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/ChartPullback.lean#L337). The attribute's comment: “part (1): an affine chart pulls back, along an arbitrary morphism `h` for which the pullback of the divisor is defined, to an affine chart of the pulled-back triple over any affine open of the source lying over its domain”.

> **Stacks tag 0F8T, part (1).**  Let `(X, D, M)` be a triple as in Situation 0F8S, let
> `h : Y ⟶ X` be a morphism of schemes along which the pullback `E = h⁻¹D` of the divisor is
> defined, let `(U, A, f, M^•)` be an affine chart for `(X, D, M)` and let `V = Spec(B) ⊆ Y` be an
> affine open with `h(V) ⊆ U`.  Then `(V, B, g, M^• ⊗_A B)`, with `g ∈ B` the image of `f`, is an
> affine chart for `(Y, E, Lh^*M)`.
>
> That `g` is a nonzerodivisor is `isRegular_pullbackRingHom_f`; that it cuts out `E ∩ V` is
> `comap_ideal_eq_span`; and that `M^• ⊗_A B` represents the restriction of `Lh^*M` to `V` is
> `pullbackRepresentsIso`.

```lean
def pullback (C : AffineChart S) {Y : Scheme.{u}} (h : Y ⟶ S.X)
    (hD : Stacks.Divisors.IsPullbackDefined h S.D) (V : Y.affineOpens)
    (hV : (V : Y.Opens) ≤ h ⁻¹ᵁ (C.U : S.X.Opens)) : AffineChart (S.pullback h hD)
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.isGoodTriple_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/ChartPullback.lean, line 413](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/ChartPullback.lean#L413). The attribute's comment: “part (3): goodness of a triple is inherited by the pulled-back triple”.

> **Stacks tag 0F8T, part (3).**  If `(X, D, M)` is a good triple and `h : Y ⟶ X` is a
> morphism of schemes along which the pullback `E = h⁻¹D` of the divisor is defined, then
> `(Y, E, Lh^*M)` is a good triple.
>
> A point of `E` maps into `D`, so it has an affine chart `(U, A, f, M^•)` of `(X, D, M)` over it
> with principal determinantal ideals; the preimage of `U` is an open neighbourhood of the point,
> so it contains an affine open `V` containing it; and part (1) turns the chart into a chart of
> `(Y, E, Lh^*M)` over `V`, whose determinantal ideals are principal by part (2).

```lean
theorem isGoodTriple_pullback (S : ComplexAndDivisorSituation.{u, d}) {Y : Scheme.{u}}
    (h : Y ⟶ S.X) (hD : Stacks.Divisors.IsPullbackDefined h S.D) (hS : IsGoodTriple S) :
    IsGoodTriple (S.pullback h hD)
```

**`AlgebraicGeometry.RingedSpace.KFlatDerivedPullback.isPerfect_uniqFunctor_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/PerfectDerivedPullback.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/PerfectDerivedPullback.lean#L194).

> **Perfectness survives a change of model of the derived category.**  The canonical
> equivalence between two localizations of the complexes at the quasi-isomorphisms carries a
> perfect object to a perfect object: the representative does not change, and the isomorphism
> exhibiting it is composed with `CategoryTheory.Localization.compUniqFunctor`.

```lean
theorem isPerfect_uniqFunctor_obj {X : RingedSpace.{u, u}}
    (inst₁ : HasDerivedCategory.{d} (OXMod.{u, u} X))
    (inst₂ : HasDerivedCategory.{d'} (OXMod.{u, u} X))
    (K : @DerivedCategory (OXMod.{u, u} X) _ _ inst₁)
    (hK : @Stacks.Cohomology.PerfectComplexes.IsPerfect.{u, u, d} X inst₁ K) :
    @Stacks.Cohomology.PerfectComplexes.IsPerfect.{u, u, d'} X inst₂
      ((Localization.uniq (@DerivedCategory.Q (OXMod.{u, u} X) _ _ inst₁)
        (@DerivedCategory.Q (OXMod.{u, u} X) _ _ inst₂)
        (HomologicalComplex.quasiIso (OXMod.{u, u} X) (ComplexShape.up ℤ))).functor.obj K)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.ComplexAndDivisorSituation.AffineChart.pullback_determinantalIdeal`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/ChartPullback.lean#L384), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/ChartPullbackRepresents.lean, line 337](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/ChartPullbackRepresents.lean#L337) (StacksFrontier): “part (2) for a general `h`: the determinantal ideals of the chart base-changed along the ring map induced by `h` on the two affine opens”.

## Tag 0GTW, a lemma

[Tag 0GTW](https://stacks.math.columbia.edu/tag/0GTW) in the Stacks Project.

**`AlgebraicGeometry.ComplexAndDivisorSituation.isPerfect_derivedEtaData_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/ChartDecalage.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/ChartDecalage.lean#L192). The attribute's comment: “Lη\_I M is perfect for a good triple (X, D, M); Lη\_I is Stacks.Divisors.Eta.derivedEtaData, and M is carried to its model of D(𝒪\_X) by the canonical equivalence of localizations”.

> **[Stacks, Tag 0GTW].** Let `X, D, I, M` be as in Situation 0F8S. If `(X, D, M)` is a good
> triple, then `Lη_I M` is a perfect object of `D(𝒪_X)`. Here `Lη_I` is the derived décalage of
> tag 0F8Q and `M` is read in the model of `D(𝒪_X)` in which it is constructed.

```lean
theorem isPerfect_derivedEtaData_obj (S : ComplexAndDivisorSituation.{u, d})
    (hS : IsGoodTriple S) :
    RingedSpace.IsPerfect (X := S.X.toRingedSpace)
      ((derivedEtaData S.D).functor.obj S.standardM)
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.IsGoodTriple.isPerfect_derivedEta_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/ChartDecalageExistence.lean, line 415](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/ChartDecalageExistence.lean#L415).

> **Stacks tag 0GTW.**  Let `X`, `D`, `I`, `M` be as in Situation 0F8S.  If `(X, D, M)` is a
> good triple, then `Lη_I M` is a perfect object of `D(𝒪_X)`.
>
> This is `AlgebraicGeometry.ComplexAndDivisorSituation.isPerfect_derivedEta_obj`, whose
> comparison on affine charts is
> `AlgebraicGeometry.ComplexAndDivisorSituation.chartDecalage_of_derivedEta` and whose charts off the
> divisor are
> `ComplexAndDivisorSituation.exists_chart_isPrincipal_determinantalIdeal_of_notMem_supportSet`.
> The derived décalage is any `Stacks.Divisors.Eta.DerivedEta` of the divisor at the model of
> `D(𝒪_X)` the triple carries; for a triple at the standard model it may be taken to be
> `Stacks.Divisors.Eta.derivedEtaData`, the functor of tag 0F8Q, and for that functor applied to
> the object carried to the standard model this is
> `AlgebraicGeometry.ComplexAndDivisorSituation.isPerfect_derivedEtaData_obj`.  The untagged
> `AlgebraicGeometry.ComplexAndDivisorSituation.isPerfect_derivedEta_obj_of_isGoodTriple` is the
> same statement with the affine-chart comparison as a hypothesis.

```lean
theorem IsGoodTriple.isPerfect_derivedEta_obj (S : ComplexAndDivisorSituation.{u, d})
    (E : Stacks.Divisors.Eta.DerivedEta S.D) (hS : IsGoodTriple S) :
    RingedSpace.IsPerfect (X := S.X.toRingedSpace) (E.functor.obj S.M)
```

## Tag 0GTX, a lemma

[Tag 0GTX](https://stacks.math.columbia.edu/tag/0GTX) in the Stacks Project.

**`Stacks.BlowUpComplexes.exists_isLocallyBoundedFiniteLocallyFree_derivedEta`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodTripleLocallyFree.lean, line 535](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodTripleLocallyFree.lean#L535).

> **Stacks Project, Tag 0GTX.**  Let `X` be a scheme, `D ⊆ X` an effective Cartier divisor
> with ideal sheaf `ℐ`, and `M` a perfect object of `D(𝒪_X)`, and assume `(X, D, M)` is a good
> triple.  If `M` is represented by a locally bounded complex of finite locally free
> `𝒪_X`-modules, then so is `Lη_ℐ M`.
>
> The representing complex for `Lη_ℐ M` is the chain-level décalage `η_ℐ ℳ^•` of the given one.

```lean
theorem exists_isLocallyBoundedFiniteLocallyFree_derivedEta (X : Scheme.{u})
    (D : X.IdealSheafData) (hD : Stacks.Divisors.IsEffectiveCartierDivisor D)
    (M : DerivedCategory X.Modules)
    (hM : RingedSpace.IsPerfect (X := X.toRingedSpace) M)
    (hgood : IsGoodTriple
      { X := X, D := D, isEffectiveCartierDivisor := hD, M := M, isPerfect := hM })
    (hrep : ∃ ℳ : CochainComplex X.Modules ℤ,
      Stacks.Chow.IsLocallyBoundedFiniteLocallyFree ℳ ∧
        Nonempty (DerivedCategory.Q.obj ℳ ≅ M)) :
    ∃ 𝒬 : CochainComplex X.Modules ℤ,
      Stacks.Chow.IsLocallyBoundedFiniteLocallyFree 𝒬 ∧
        Nonempty (DerivedCategory.Q.obj 𝒬 ≅
          (@Stacks.Divisors.Eta.derivedEtaData X D hD).functor.obj M)
```

## Tag 0F9X, a lemma

[Tag 0F9X](https://stacks.math.columbia.edu/tag/0F9X) in the Stacks Project.

**`Stacks.Divisors.Eta.isIso_derivedEtaPullbackComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/EtaDerivedPullbackComparison.lean, line 287](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/EtaDerivedPullbackComparison.lean#L287). The attribute's comment: “the case of a flat h, which neither implies nor is implied by the source's statement: flatness replaces goodness of the triple, and no goodness is used. the general case, for an arbitrary h and a good triple, is AlgebraicGeometry.ComplexAndDivisorSituation.nonempty\_derivedPullback\_derivedEta\_iso”.

> **[Stacks, Tag 0F9X] for a flat morphism.**  Let `X` be a scheme, let `D ⊆ X` be an effective
> Cartier divisor with ideal sheaf `I = ℐ_D`, let `h : Y ⟶ X` be a flat morphism of schemes and
> suppose the pullback `E = h^{-1}D` is defined, with ideal sheaf `J = ℐ_E`.  Then for every object
> `M = [G^•]` of `D(𝒪_X)` presented by a complex of `I`-torsion-free modules, the canonical
> comparison `Lh^*(Lη_I M) ⟶ Lη_J(Lh^* M)` is an isomorphism.
>
> Two of the three constituents of `Stacks.Divisors.Eta.derivedEtaPullbackComparison` are
> components of the natural isomorphism identifying `Lh^*` with the functor induced by `h^*`,
> hence isomorphisms; the remaining one is an isomorphism by
> `Stacks.IdealTorsion.Eta.isIso_transportedPullbackDerivedEtaMap`, which is where flatness is
> used.

```lean
theorem isIso_derivedEtaPullbackComparison
    (hflat : AlgebraicGeometry.IsFlat h.toLRSHom.toShHom)
    (K : CochainComplex
      (Stacks.IdealTorsion.Eta.TorsionFreeModule X.toRingedSpace (idealSheafι D)) ℤ) :
    IsIso (derivedEtaPullbackComparison h D hflat K)
```

**`Stacks.Divisors.Eta.nonempty_derivedPullback_derivedEta_iso_of_forall_stalk_good`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/EtaGoodBaseChange/GeneralComparison.lean, line 220](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/EtaGoodBaseChange/GeneralComparison.lean#L220). The attribute's comment: “the general case --- goodness in place of flatness, with goodness of the triple (Situation 0F8S) read at the stalks: at every point z of Y the stalk complex of the chosen representative is represented in the derived category of the local ring O\_\{X,h(z)} by a bounded complex C of finite free modules whose determinantal ideals I\_i(C, a) are all principal, a being a generator of the stalk of the ideal sheaf. The passage from AlgebraicGeometry.ComplexAndDivisorSituation.IsGoodTriple to that stalkwise reading is AlgebraicGeometry.ComplexAndDivisorSituation.exists\_affineOpen\_stalk\_goodModel, and the statement of the tag at a good triple is AlgebraicGeometry.ComplexAndDivisorSituation.nonempty\_derivedPullback\_derivedEta\_iso. The case of a flat h, which neither implies nor is implied by this one, is Stacks.Divisors.Eta.isIso\_derivedEtaPullbackComparison”.

> **[Stacks, Tag 0F9X] with goodness in place of flatness.**  Let `X` be a scheme, let
> `D ⊆ X` be an effective Cartier divisor with ideal sheaf `I = ℐ_D`, let `h : Y ⟶ X` be an
> **arbitrary** morphism of schemes such that the inverse image `E = h^{-1}D` is defined, and let
> `J = ℐ_E`.  Let `M` be an object of `D(𝒪_X)` presented by a K-flat complex `𝒦` of flat
> `𝒪_X`-modules, and suppose that at every point `z` of `Y` the stalk complex of `𝒦` at `h(z)` is
> **good**: there are a generator `a` of `I_{h(z)}` whose germ generates `J_z` and a bounded
> complex `C` of finite free `𝒪_{X,h(z)}`-modules representing `𝒦_{h(z)}` in `D(𝒪_{X,h(z)})` all
> of whose determinantal ideals `I_i(C, a)` are principal.  Then
>
> `Lh^*(Lη_I M) ≅ Lη_J(Lh^* M)`
>
> in `D(𝒪_Y)`.
>
> **No flatness of `h` is used**, which is what separates this from
> `Stacks.Divisors.Eta.isIso_derivedEtaPullbackComparison`.  Presenting `M` by a K-flat complex of
> flat modules is no restriction: `Stacks.Divisors.Eta.exists_kFlat_isFlat_rep'` produces one for
> every object of `D(𝒪_X)`.  The auxiliary K-flat presentation of `η_I 𝒦` that the reduction
> consumes is supplied here by the K-flat resolution of Stacks 06YF, so it is not a hypothesis.

```lean
theorem nonempty_derivedPullback_derivedEta_iso_of_forall_stalk_good
    (h𝒦 : Stacks.Cohomology.KFlatDerivedPullback.KFlatComplex X.toRingedSpace 𝒦)
    (hgood : ∀ z : Y, ∃ (a : ringStalk X.toRingedSpace (h.toLRSHom.toShHom.hom.base z))
        (_ : GeneratesStalkIdeal X.toRingedSpace (idealSheafι D)
          (h.toLRSHom.toShHom.hom.base z) a)
        (_ : GeneratesStalkIdeal Y.toRingedSpace
          (pullbackIdealIncl h.toLRSHom.toShHom (idealSheaf D) (idealSheafι D)) z
          (commStalkGermMap h.toLRSHom.toShHom z a))
        (C : BoundedComplex (ringStalk X.toRingedSpace (h.toLRSHom.toShHom.hom.base z))),
        (∀ i : ℤ, (idealI C a i).IsPrincipal) ∧
          Nonempty (DerivedCategory.Q.obj C.toCochainComplex ≅
            DerivedCategory.Q.obj
              (stalkComplex X.toRingedSpace (h.toLRSHom.toShHom.hom.base z) 𝒦)))
    (M : DerivedCategory X.Modules) (e : DerivedCategory.Q.obj 𝒦 ≅ M) :
    Nonempty ((derivedPullback h.toLRSHom.toShHom).obj ((derivedEtaData D).functor.obj M) ≅
      (derivedEtaData (D.comap h)).functor.obj
        ((derivedPullback h.toLRSHom.toShHom).obj M))
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.derivedEtaPullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodTripleEtaPullback.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodTripleEtaPullback.lean#L139). The attribute's comment: “the case of a flat h, with no goodness hypothesis, which is therefore neither weaker nor stronger than the source's statement. the general case, for an arbitrary h and a good triple, is AlgebraicGeometry.ComplexAndDivisorSituation.nonempty\_derivedPullback\_derivedEta\_iso”.

> **[Stacks, Tag 0F9X] for a flat morphism.**  Let `X`, `D`, `I`, `M` be as in Situation 0F8S,
> let `h : Y ⟶ X` be a flat morphism of schemes such that the pullback `E = h^{-1}D` is defined,
> and let `J = ℐ_E`.  Then
>
> `Lh^*(Lη_I M) ≅ Lη_J(Lh^* M)`
>
> in `D(𝒪_Y)`, where the right-hand side is the object of the pulled-back triple
> `AlgebraicGeometry.ComplexAndDivisorSituation.pullback`.
>
> The isomorphism is `Stacks.Divisors.Eta.derivedEtaPullbackIso`, conjugated by the presentation
> `hKM` of `M` by a complex of `I`-torsion-free modules on each side.
>
> The source's hypothesis that `(X, D, M)` is a good triple is **not** needed by this route and is
> therefore not carried: the statement below is the flat case of tag 0F9X *without* goodness, which
> is strictly stronger than the flat case of the source's statement.  Flatness, which the source
> does not assume, is named in the attribute.

```lean
def derivedEtaPullbackIso (S : ComplexAndDivisorSituation.{u, d}) {Y : Scheme.{u}}
    (h : Y ⟶ S.X) [AlgebraicGeometry.Flat h]
    [hD : Stacks.Divisors.IsPullbackDefined h S.D]
    (K : CochainComplex
      (Stacks.IdealTorsion.Eta.TorsionFreeModule S.X.toRingedSpace (idealSheafι S.D)) ℤ)
    (hKM : DerivedCategory.Q.obj
      ((Stacks.IdealTorsion.Eta.torsionFreeComplex S.X.toRingedSpace
        (idealSheafι S.D)).obj K) ≅ S.standardObject) :
    (derivedPullback h.toLRSHom.toShHom).obj
        ((@Stacks.IdealTorsion.Eta.derivedEta S.X.toRingedSpace (idealSheaf S.D)
          (idealSheafι S.D) (Stacks.Divisors.Eta.mono_idealSheafι S.D)
          (Stacks.Divisors.Eta.isInvertible_idealSheaf S.D)
          (hasTorsionFreeResolutions S.D)).obj S.standardObject) ≅
      (@Stacks.IdealTorsion.Eta.derivedEta Y.toRingedSpace (idealSheaf (S.D.comap h))
          (idealSheafι (S.D.comap h)) (Stacks.Divisors.Eta.mono_idealSheafι (S.D.comap h))
          (Stacks.Divisors.Eta.isInvertible_idealSheaf (S.D.comap h))
          (hasTorsionFreeResolutions (S.D.comap h))).obj
        (S.derivedPullbackObject h)
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.nonempty_derivedPullback_derivedEta_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodTripleEtaPullbackGeneral.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodTripleEtaPullbackGeneral.lean#L222). The attribute's comment: “the whole statement: for a good triple and an arbitrary morphism `h` along which the inverse image of the divisor is defined, `Lh^*(Lη_I M) ≅ Lη_J(Lh^* M)`. Goodness enters through its reading at the stalks, AlgebraicGeometry.ComplexAndDivisorSituation.exists\_affineOpen\_stalk\_goodModel, and the ring-level input is Stacks 0F7X in the form Stacks.Eta.GoodBaseChange.quasiIso\_baseChangeMap\_comp\_etaBaseChangeMap\_of\_kFlat. The case of a flat h without goodness is Stacks.Divisors.Eta.isIso\_derivedEtaPullbackComparison”.

> **[Stacks, Tag 0F9X].**  Let `(X, D, M)` be a triple as in Situation 0F8S, with `ℐ` the ideal
> sheaf of `D`, and let `h : Y ⟶ X` be a morphism of schemes such that the inverse image
> `E = h^{-1}D` is defined, with ideal sheaf `𝒥`.  If `(X, D, M)` is a good triple then
>
> `Lh^*(Lη_ℐ M) ≅ Lη_𝒥(Lh^* M)`
>
> in `D(𝒪_Y)`, the right-hand side being the décalage by the ideal sheaf of `E` of the object of
> the pulled-back triple, i.e.
> `AlgebraicGeometry.ComplexAndDivisorSituation.etaDerivedPullbackObject`.
>
> No flatness of `h` is assumed.  The object is presented by a K-flat complex of flat modules —
> which every object admits — and goodness is read at the stalks by
> `AlgebraicGeometry.ComplexAndDivisorSituation.exists_affineOpen_stalk_goodModel`, which also
> supplies the generator of the stalk ideal whose germ generates the stalk ideal of `h^*ℐ`.

```lean
theorem nonempty_derivedPullback_derivedEta_iso (hgood : S.IsGoodTriple) {Y : Scheme.{u}}
    (h : Y ⟶ S.X) (hD : Stacks.Divisors.IsPullbackDefined h S.D) :
    Nonempty ((derivedPullback h.toLRSHom.toShHom).obj
        ((derivedEtaData S.D).functor.obj S.standardObject) ≅
      (derivedEtaData (S.D.comap h)).functor.obj (S.derivedPullbackObject h))
```

## Tag 0GTY, a lemma

[Tag 0GTY](https://stacks.math.columbia.edu/tag/0GTY) in the Stacks Project.

**`AlgebraicGeometry.ComplexAndDivisorSituation.AffineChart.isAdmissibleBlowup_blowUpToBase_blowupCentreIdealSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/ChartBlowupAdmissible.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/ChartBlowupAdmissible.lean#L210). The attribute's comment: “the admissibility assertion over an affine chart: the blowing up of the chart in the product of its determinantal ideals, which is what `b` restricts to there, is a `(U \ D)`-admissible blowing up”.

> **Stacks tag 0GTY, the admissibility assertion over an affine chart.**  Over an affine chart
> `(U, A, f, M^•)` the morphism `b` of the tag is the blowing up of `U` in the product
> `∏ᵢ I_i(M^•, f)` of the determinantal ideals of the chart, and that blowing up is a
> `(U \ D)`-admissible blowing up: the centre is of finite presentation and its support, being
> contained in that of `D ∩ U`, is disjoint from `U \ D`.

```lean
theorem isAdmissibleBlowup_blowUpToBase_blowupCentreIdealSheaf (C : AffineChart S) :
    Stacks.Blowup.IsAdmissibleBlowup
      ((C.U : S.X.Opens).ι ⁻¹ᵁ S.D.support.compl)
      (AlgebraicGeometry.blowUpToBase C.blowupCentreIdealSheaf)
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.AffineChart.isGoodOver_chartBlowupToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/ChartBlowupAdmissible.lean, line 421](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/ChartBlowupAdmissible.lean#L421). The attribute's comment: “clause (1) over an affine chart: the triple pulled back along the blowing up of the chart in the product of its determinantal ideals --- which is what `b` restricts to over the chart --- is a good triple, and the pullback of `D` along it is defined”.

> **Stacks tag 0GTY, clause (1) over an affine chart.**  Let `(U, A, f, M^•)` be an affine
> chart for the triple `(X, D, M)` and let `b_U : U' ⟶ U` be the blowing up of `U` in the product
> `∏ᵢ I_i(M^•, f)` of its determinantal ideals.  Then the composite `U' ⟶ U ⟶ X` is good for the
> triple: the pullback of `D` along it is defined, and the pulled-back triple
> `(U', b_U⁻¹(D ∩ U), Lb_U^*M)` is a good triple.
>
> Every point of `U'` lies in an affine open `V` on which all the finitely many inverse images
> `I_i(M^•, f)𝒪_{U'}` are principal, these being effective Cartier divisors by
> `AffineChart.isEffectiveCartierDivisor_comap_determinantalIdealSheaf`; the degrees in which `M^•`
> vanishes contribute the unit ideal.  By part (1) of Stacks tag 0F8T such a `V` carries the
> pulled-back chart `(V, Γ(U', V), f|_V, M^• ⊗_A Γ(U', V))`, and by part (2) of that tag its
> determinantal ideals are exactly those inverse images.

```lean
theorem isGoodOver_chartBlowupToBase (C : AffineChart S) :
    S.IsGoodOver C.chartBlowupToBase
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.AffineChart.existsUnique_lift_chartBlowup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/ChartBlowupUniversal.lean, line 248](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/ChartBlowupUniversal.lean#L248). The attribute's comment: “clause (2) over an affine chart: a morphism to the chart whose composite with the inclusion of the chart is good for the triple factors uniquely through the blowing up of the chart in the product of its determinantal ideals, which is what `b` restricts to there”.

> **Stacks tag 0GTY, clause (2) over an affine chart.**  Let `(U, A, f, M^•)` be an affine chart
> for the triple `(X, D, M)` and let `b_U : U' ⟶ U` be the blowing up of `U` in the product
> `∏ᵢ I_i(M^•, f)` of its determinantal ideals.  Every morphism `h : Y ⟶ U` whose composite with
> the inclusion of `U` is good for the triple factors through `b_U` in exactly one way.
>
> The inverse image of the centre along `h` is an effective Cartier divisor by
> `AffineChart.isEffectiveCartierDivisor_comap_blowupCentreIdealSheaf`, so the universal property of
> blowing up, Stacks tag 0806, applies.

```lean
theorem existsUnique_lift_chartBlowup (C : AffineChart S) {Y : Scheme.{u}}
    (b : Y ⟶ (C.U : S.X.Opens).toScheme)
    (hgood : S.IsGoodOver (b ≫ (C.U : S.X.Opens).ι)) :
    ∃! k : Y ⟶ blowUp C.blowupCentreIdealSheaf,
      k ≫ blowUpToBase C.blowupCentreIdealSheaf = b
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.isAdmissibleBlowup_morphismRestrict_goodBlowupToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodBlowupQuasiCompact.lean, line 399](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodBlowupQuasiCompact.lean#L399). The attribute's comment: “the quasi-compact-open admissibility assertion: for a quasi-compact open `W ⊂ X` the restriction `b|_{b^{-1}(W)} : b^{-1}(W) ⟶ W` of the morphism of the tag is a `W \ D`-admissible blowing up. The centre is glued from the normalized determinantal products of the charts of a finite cover of `W`, with the product taken over a finite degree window containing the supports of those finitely many charts' complexes”.

> **Stacks tag 0GTY, the quasi-compact-open admissibility assertion.**  In Situation 0F8S let
> `b : X' ⟶ X` be the morphism of tag 0GTY and let `W ⊂ X` be a quasi-compact open.  Then
> `b|_{b⁻¹(W)} : b⁻¹(W) ⟶ W` is a `W \ D`-admissible blowing up.
>
> The centre is `AlgebraicGeometry.ComplexAndDivisorSituation.gluedNormalizedCentre`, glued from
> the normalized centres of the charts of a finite cover of `W` by chart domains; it is of finite
> presentation and supported on the divisor, and over each chart of the cover the restriction of
> `b` is the blowing up in it, so the identification descends to `W`.

```lean
theorem isAdmissibleBlowup_morphismRestrict_goodBlowupToBase
    (S : ComplexAndDivisorSituation.{u, d}) (W : S.X.Opens) (hW : IsCompact (W : Set S.X)) :
    Stacks.Blowup.IsAdmissibleBlowup (W.ι ⁻¹ᵁ S.D.support.compl)
      (S.goodBlowupToBase ∣_ W)
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.existsUnique_isGoodBlowup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodBlowupTag.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodBlowupTag.lean#L87). The attribute's comment: “the existence and uniqueness assertion: there is a morphism `b : X' ⟶ X` whose pullback of `D` is defined and makes the pulled-back triple good, through which every morphism to `X` with defined pullback of `D` and good pulled-back triple factors uniquely, and any two such morphisms are identified by a unique isomorphism over `X`”.

> **Stacks tag 0GTY: the existence and uniqueness assertion.**  In Situation 0F8S there is a
> morphism `b : X' ⟶ X` such that
>
> 1. the pullback `D' = b⁻¹D` is defined and `(X', D', Lb^*M)` is a good triple, and
> 2. every morphism `h : Y ⟶ X` for which `h⁻¹D` is defined and `(Y, h⁻¹D, Lh^*M)` is a good triple
>    factors uniquely through `b`,
>
> and any morphism with those two properties is identified with it by a unique isomorphism over
> `X`.
>
> The morphism is `AlgebraicGeometry.ComplexAndDivisorSituation.goodBlowupToBase`, obtained by
> blowing up each affine chart in the product of its determinantal ideals and gluing over the basis
> of chart domains; the uniqueness is
> `AlgebraicGeometry.ComplexAndDivisorSituation.IsGoodBlowup.existsUnique_iso`.

```lean
theorem existsUnique_isGoodBlowup :
    ∃ (X' : Scheme.{u}) (b : X' ⟶ S.X), S.IsGoodBlowup b ∧
      ∀ (X'' : Scheme.{u}) (b' : X'' ⟶ S.X), S.IsGoodBlowup b' →
        ∃! e : X'' ≅ X', e.hom ≫ b = b'
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.AffineChart.existsUnique_iso_preimage_blowUp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodBlowupTag.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodBlowupTag.lean#L108). The attribute's comment: “the affine-chart description: over an affine chart `(U, A, f, M^•)` the restriction `b⁻¹(U) ⟶ U` of the morphism of the tag is the blowing up of `U` in the product of the determinantal ideals `I_i(M^•, f)` of the chart, by a unique isomorphism over `U`”.

> **Stacks tag 0GTY: the affine-chart description of `b`.**  Over an affine chart
> `(U, A, f, M^•)` for the triple, the restriction `b⁻¹(U) ⟶ U` of the morphism of the tag is the
> blowing up of `U` in the product `∏ᵢ I_i(M^•, f)` of the determinantal ideals of the chart: there
> is exactly one isomorphism `b⁻¹(U) ≅ U'` over `U` between the two.
>
> Both morphisms have the two conditions of the tag over `U` — the restriction of `b` by
> `AlgebraicGeometry.ComplexAndDivisorSituation.IsGoodBlowupOver.restrict`, the blowing up of the
> chart by `AffineChart.isGoodBlowupOver_chartBlowupToBase` — so they are identified by a unique
> isomorphism over `X`, and over `U` that is the same thing.

```lean
theorem existsUnique_iso_preimage_blowUp (C : AffineChart S) :
    ∃! e : (S.goodBlowupToBase ⁻¹ᵁ (C.U : S.X.Opens)).toScheme ≅
        AlgebraicGeometry.blowUp C.blowupCentreIdealSheaf,
      e.hom ≫ AlgebraicGeometry.blowUpToBase C.blowupCentreIdealSheaf =
        S.goodBlowupToBase ∣_ (C.U : S.X.Opens)
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.AffineChart.blowupCentre_fg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodTriple.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodTriple.lean#L177). The attribute's comment: “the centre `∏ᵢ I_i(M^•, f)` of the blowup over an affine chart is of finite type; for the blowup in it over an affine chart --- its admissibility, the goodness of the pulled-back triple and its universal property --- see `ChartBlowupAdmissible.lean` and `ChartBlowupUniversal.lean`, and for the morphism `b : X' ⟶ X` glued from them see `GoodBlowupTag.lean`”.

> **Stacks tag 0GTY, the centre of the blowup over an affine chart: finite type.**  The
> product of the determinantal ideals is finitely generated, being a finite product of finitely
> generated ideals.  Finite type of the centre is the condition under which the blowup in it is
> proper and, with
> `AlgebraicGeometry.ComplexAndDivisorSituation.AffineChart.pow_mem_blowupCentre`, admissible away
> from the divisor.

```lean
theorem blowupCentre_fg (C : AffineChart S) : C.blowupCentre.FG
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.AffineChart.pow_mem_blowupCentre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodTriple.lean, line 193](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodTriple.lean#L193). The attribute's comment: “the centre `∏ᵢ I_i(M^•, f)` of the blowup over an affine chart contains a power of the equation of the divisor, hence is supported on it; for the blowup in it over an affine chart --- its admissibility, the goodness of the pulled-back triple and its universal property --- see `ChartBlowupAdmissible.lean` and `ChartBlowupUniversal.lean`, and for the morphism `b : X' ⟶ X` glued from them see `GoodBlowupTag.lean`”.

> **Stacks tag 0GTY, the centre of the blowup over an affine chart: supported on the
> divisor.**  The power `f ^ (∑ᵢ rᵢ)` of the equation of `D ∩ U` lies in the product of the
> determinantal ideals, since `f ^ rᵢ` lies in the `i`-th factor.  Hence the closed subscheme cut
> out by the centre is contained in `D ∩ U`, so the centre is disjoint from `U \ D`: this is the
> condition that makes the blowup of the chart in it a `(U \ D)`-admissible blowing up.

```lean
theorem pow_mem_blowupCentre (C : AffineChart S) :
    C.f ^ (∑ i ∈ C.complex.bounded.toFinset, C.complex.rank i) ∈ C.blowupCentre
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.isGoodBlowup_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodTripleBlowup.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodTripleBlowup.lean#L132). The attribute's comment: “the morphism `b`, in the case where `𝟙 X` is good for the triple: the identity of `X` then has both properties of the tag, so `b` may be taken to be `𝟙 X`”.

> **The existence assertion of Stacks tag 0GTY for a triple that is already good.**  If `𝟙 X`
> is good for `(X, D, M)` then it has both properties (1) and (2) of the tag: property (1) is the
> hypothesis, and every morphism `h : Y ⟶ X` factors through `𝟙 X` uniquely, by `h` itself.

```lean
theorem isGoodBlowup_id (h : S.IsGoodOver (𝟙 S.X)) : S.IsGoodBlowup (𝟙 S.X)
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.IsGoodBlowup.existsUnique_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodTripleBlowup.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodTripleBlowup.lean#L155). The attribute's comment: “the uniqueness assertion: any two morphisms to `X` with properties (1) and (2) of the tag are identified by a unique isomorphism over `X`, which is what it means for the morphism the tag describes to be unique”.

> **The uniqueness assertion of Stacks tag 0GTY.**  Two morphisms to `X` with properties (1)
> and (2) are identified by a unique isomorphism over `X`.
>
> Each factors through the other by (2), and the two composites are identities by
> `AlgebraicGeometry.ComplexAndDivisorSituation.IsGoodBlowup.eq_id_of_comp_eq`; an isomorphism
> over `X` is determined by its underlying morphism, which (2) pins down.

```lean
theorem existsUnique_iso {X₁ X₂ : Scheme.{u}} {b₁ : X₁ ⟶ S.X} {b₂ : X₂ ⟶ S.X}
    (h₁ : S.IsGoodBlowup b₁) (h₂ : S.IsGoodBlowup b₂) :
    ∃! e : X₁ ≅ X₂, e.hom ≫ b₂ = b₁
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.IsGoodBlowup.isIso_of_isGoodOver_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodTripleBlowup.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodTripleBlowup.lean#L171). The attribute's comment: “the morphism `b` over a triple for which `𝟙 X` is good: any morphism with the two properties of the tag is then an isomorphism”.

> A morphism with properties (1) and (2) of Stacks tag 0GTY over a triple for which `𝟙 X` is
> already good is an isomorphism.  By
> `AlgebraicGeometry.ComplexAndDivisorSituation.isGoodBlowup_id` the identity also has those
> properties, so the two are identified over `X` by
> `AlgebraicGeometry.ComplexAndDivisorSituation.IsGoodBlowup.existsUnique_iso`.

```lean
theorem isIso_of_isGoodOver_id (hb : S.IsGoodBlowup b) (h : S.IsGoodOver (𝟙 S.X)) : IsIso b
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.exists_isPullback_blowUpToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodTripleBlowupGlue.lean, line 337](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodTripleBlowupGlue.lean#L337). The attribute's comment: “over every affine chart, b is the blowing up in the product of the determinantal ideals”.

> **Stacks tag 0GTY, over an affine chart.**  For every affine chart `(U, A, f, M^•)` of the
> triple, the part `b⁻¹(U) ⟶ U` of `b` over `U` is the blowing up of `U` in the product
> `∏ᵢ I_i(M^•, f)` of the determinantal ideals of the chart: there is a morphism from that blowup
> to `X'` making the square with `b` and the inclusion of `U` Cartesian.
>
> The chart need not be one of those used to glue `X'`: the blowup of any chart has the universal
> property over its domain, and so does the part of `b` over it.

```lean
theorem exists_isPullback_blowUpToBase (S : ComplexAndDivisorSituation.{u, d})
    (C : AffineChart S) :
    ∃ e : blowUp C.blowupCentreIdealSheaf ⟶ S.goodBlowup,
      IsPullback e (blowUpToBase C.blowupCentreIdealSheaf) S.goodBlowupToBase
        (C.U : S.X.Opens).ι
```

## Tag 0F8U, a lemma

[Tag 0F8U](https://stacks.math.columbia.edu/tag/0F8U) in the Stacks Project.

**`AlgebraicGeometry.ComplexAndDivisorSituation.isPerfect_etaDerivedPullbackObject_goodBlowup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodBlowupDecalagePerfect.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodBlowupDecalagePerfect.lean#L58). The attribute's comment: “`Q = Lη_{I'} Lb^* M` is perfect, for `b` the morphism goodBlowupToBase of tag 0GTY (existsUnique\_isGoodBlowup), `Lη_{I'}` the derived décalage Stacks.Divisors.Eta.derivedEtaData of `D' = b⁻¹D` and `Lb^*` the derived pullback of modules”.

> **Stacks tag 0F8U.**  In Situation 0F8S let `b : X' ⟶ X` be the morphism of Stacks tag 0GTY
> and `D' = b⁻¹D`, with ideal sheaf `ℐ'`.  Then `Q = Lη_{ℐ'}Lb^*M` is a perfect object of
> `D(𝒪_{X'})`.

```lean
theorem isPerfect_etaDerivedPullbackObject_goodBlowup :
    RingedSpace.IsPerfect (X := S.goodBlowup.toRingedSpace)
      (S.etaDerivedPullbackObject S.goodBlowupToBase
        S.isGoodOver_goodBlowupToBase.pullbackDefined)
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.isPerfect_etaDerivedPullbackObject_goodBlowupToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodBlowupEtaPerfect.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodBlowupEtaPerfect.lean#L83). The attribute's comment: “perfectness of `Q = Lη_{I'} Lb^* M` for the morphism `b` of tag 0GTY itself, namely AlgebraicGeometry.ComplexAndDivisorSituation.goodBlowupToBase, with the datum `hcomp` of the formalization of tag 0GTW: the second assertion of tag 0GTV read at an affine open of `X'`”.

> **Stacks tag 0F8U for the morphism `b : X' ⟶ X` of Stacks tag 0GTY.**  In Situation 0F8S let
> `b` be the morphism of tag 0GTY and `D' = b⁻¹D` with ideal sheaf `ℐ'`.  Then
> `Q = Lη_{ℐ'}Lb^*M` is a perfect object of `D(𝒪_{X'})`.
>
> The morphism is `AlgebraicGeometry.ComplexAndDivisorSituation.goodBlowupToBase`; it satisfies
> condition (1) of tag 0GTY by
> `AlgebraicGeometry.ComplexAndDivisorSituation.isGoodOver_goodBlowupToBase`, so this is
> `AlgebraicGeometry.ComplexAndDivisorSituation.isPerfect_etaDerivedPullbackObject_of_chartDecalage`
> read at it.  The hypothesis `hcomp` is the affine-chart comparison for `Lη_{ℐ'}` described in
> the module documentation.

```lean
theorem isPerfect_etaDerivedPullbackObject_goodBlowupToBase
    (hcomp : ChartDecalage
      (S.pullback S.goodBlowupToBase S.isGoodOver_goodBlowupToBase.pullbackDefined)
      (@Stacks.Divisors.Eta.derivedEtaData S.goodBlowup (S.D.comap S.goodBlowupToBase)
        S.isGoodOver_goodBlowupToBase.pullbackDefined)) :
    RingedSpace.IsPerfect (X := S.goodBlowup.toRingedSpace)
      (S.etaDerivedPullbackObject S.goodBlowupToBase
        S.isGoodOver_goodBlowupToBase.pullbackDefined)
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.isPerfect_etaDerivedPullbackObject_of_isGoodOver_of_chartDecalage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodOverEtaPerfectOfIsGoodOver.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodOverEtaPerfectOfIsGoodOver.lean#L46). The attribute's comment: “perfectness of `Q = Lη_{I'} Lb^* M` for any `b` satisfying condition (1) of tag 0GTY, with the datum `hcomp` of the formalization of tag 0GTW: the second assertion of tag 0GTV read at an affine open of the pulled-back scheme”.

> **Stacks tag 0F8U, for a morphism good for the triple.**  Let `(X, D, M)` be a triple as in
> Situation 0F8S and let `b : X' ⟶ X` be good for it — condition (1) of tag 0GTY, which the
> morphism of that tag satisfies.  Then `Q = Lη_{ℐ'} Lb^*M` is a perfect object of `D(𝒪_{X'})`,
> for every affine-chart comparison `hcomp` of the shape of the second assertion of tag 0GTV.

```lean
theorem isPerfect_etaDerivedPullbackObject_of_isGoodOver_of_chartDecalage
    (S : ComplexAndDivisorSituation.{u, d}) {X' : Scheme.{u}} (b : X' ⟶ S.X)
    (hb : S.IsGoodOver b)
    (hcomp : ChartDecalage (S.pullback b hb.pullbackDefined)
      (@Stacks.Divisors.Eta.derivedEtaData X' (S.D.comap b) hb.pullbackDefined)) :
    RingedSpace.IsPerfect (X := X'.toRingedSpace)
      (S.etaDerivedPullbackObject b hb.pullbackDefined)
```

## Tag 0F8V, a lemma

[Tag 0F8V](https://stacks.math.columbia.edu/tag/0F8V) in the Stacks Project.

**`AlgebraicGeometry.ComplexAndDivisorSituation.AffineChart.existsUnique_iso_strictTransform`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodBlowupStrictTransform.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodBlowupStrictTransform.lean#L182). The attribute's comment: “the strict-transform assertion: over an affine chart `(U, A, f, M^•)`, the restriction of the morphism `c` of tag 0GTY for the pulled-back triple is identified, by exactly one isomorphism over `h⁻¹(U)`, with the strict transform of `h⁻¹(U)` with respect to the restriction of `b` over `U`, which is the blowing up of `U` in the product of the determinantal ideals of the chart”.

> **Stacks tag 0F8V: the modification of the pulled-back triple is the strict transform.**  Let
> `h : Y ⟶ X` be a morphism along which `E = h⁻¹D` is defined, let `b : X' ⟶ X` and `c : Y' ⟶ Y` be
> the morphisms of Stacks tag 0GTY for `(X, D, M)` and `(Y, E, Lh^*M)`, and let `(U, A, f, M^•)` be
> an affine chart for `(X, D, M)`.  Over `U` the morphism `b` is the blowing up of `U` in
> `I = ∏ᵢ I_i(M^•, f)`, and `c⁻¹(h⁻¹U) ⟶ h⁻¹(U)` is identified, by exactly one isomorphism over
> `h⁻¹(U)`, with the strict transform of `h⁻¹(U)` with respect to that blowing up.
>
> Both are the blowing up of `h⁻¹(U)` in `I𝒪_{h⁻¹(U)}`: the first by
> `AffineChart.isGoodBlowupOver_pullbackChartBlowupToBase` and the uniqueness of a morphism with
> the two conditions of Stacks tag 0GTY over `h⁻¹(U)`, the second by Stacks tag 080E.

```lean
theorem existsUnique_iso_strictTransform (C : AffineChart S) {Y : Scheme.{u}} (h : Y ⟶ S.X)
    (hD : Stacks.Divisors.IsPullbackDefined h S.D) :
    ∃! e : ((S.pullback h hD).goodBlowupToBase ⁻¹ᵁ
        (h ⁻¹ᵁ (C.U : S.X.Opens))).toScheme ≅
      Stacks.StrictTransform.scheme (h ∣_ (C.U : S.X.Opens))
        (AlgebraicGeometry.blowUpToBase C.blowupCentreIdealSheaf)
        (AlgebraicGeometry.exceptionalIdeal C.blowupCentreIdealSheaf),
      e.hom ≫ (Stacks.StrictTransform.ideal (h ∣_ (C.U : S.X.Opens))
            (AlgebraicGeometry.blowUpToBase C.blowupCentreIdealSheaf)
            (AlgebraicGeometry.exceptionalIdeal C.blowupCentreIdealSheaf)).subschemeι ≫
          pullback.fst (h ∣_ (C.U : S.X.Opens))
            (AlgebraicGeometry.blowUpToBase C.blowupCentreIdealSheaf) =
        (S.pullback h hD).goodBlowupToBase ∣_ (h ⁻¹ᵁ (C.U : S.X.Opens))
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.exists_lift_and_nonempty_etaDerivedPullbackObject_iso_of_isGoodBlowup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodOverEtaBaseChangeGeneral.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodOverEtaBaseChangeGeneral.lean#L141). The attribute's comment: “the displayed identification: for `b` with the two properties of tag 0GTY for (X, D, M) and `c` with those properties for (Y, E, Lh^* M), the morphism `h' : Y' -> X'` over `h . c` satisfies `L eta_{J'} L(h . c)^* M ≅ L h'^* Q`. The sentence identifying `Y'` with the strict transform of `Y` with respect to `b` rests on the moreover clause of tag 0GTY --- that over an affine chart the restriction of `b` is the blowing up in the product of the determinantal ideals --- and is proved alongside that clause, as AlgebraicGeometry.ComplexAndDivisorSituation.AffineChart.existsUnique\_iso\_strictTransform in GoodBlowupStrictTransform.lean”.

> **Stacks tag 0F8V, the displayed identification.**  Let `(X, D, M)` be a triple as in
> Situation 0F8S, let `b : X' ⟶ X` have the two properties of tag 0GTY for `(X, D, M)`, and let
> `Q = Lη_{ℐ'} Lb^*M` be the object of tag 0F8U.  Let `h : Y ⟶ X` be a morphism along which
> `E = h^{-1}D` is defined and let `c : Y' ⟶ Y` have the two properties of tag 0GTY for
> `(Y, E, Lh^*M)`.  Then there is a morphism `h' : Y' ⟶ X'` with `h' ∘ b = c ∘ h` — unique, by
> property (2) of tag 0GTY — and for it
>
> `Lη_{𝒥'} L(h ∘ c)^*M ≅ Lh'^* Q`,
>
> where `𝒥'` is the ideal sheaf of `E' = c^{-1}E = (c ∘ h)^{-1}D`.
>
> The morphism `h'` is produced by property (2) of `b` applied to `c ∘ h`, which is good for
> `(X, D, M)` by `AlgebraicGeometry.ComplexAndDivisorSituation.isGoodOver_comp`.  The
> identification is tag 0F9X
> (`AlgebraicGeometry.ComplexAndDivisorSituation.nonempty_derivedPullback_derivedEta_iso`) at the
> triple `(X', b^{-1}D, Lb^*M)`, which is good because `b` has property (1), followed by the
> bookkeeping of
> `AlgebraicGeometry.ComplexAndDivisorSituation.nonempty_etaDerivedPullbackObject_comp`: the
> divisor `h'^{-1}(b^{-1}D)` *is* the divisor `(h' ∘ b)^{-1}D`, and the two routes to the
> pulled-back object agree.

```lean
theorem exists_lift_and_nonempty_etaDerivedPullbackObject_iso_of_isGoodBlowup
    (S : ComplexAndDivisorSituation.{u, d}) {X' Y Y' : Scheme.{u}}
    (b : X' ⟶ S.X) (hb : S.IsGoodBlowup b) (h : Y ⟶ S.X)
    (hD : Stacks.Divisors.IsPullbackDefined h S.D) (c : Y' ⟶ Y)
    (hc : (S.pullback h hD).IsGoodBlowup c) :
    ∃ h' : Y' ⟶ X', h' ≫ b = c ≫ h ∧
      Nonempty ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
          h'.toLRSHom.toShHom).obj
            (S.etaDerivedPullbackObject b hb.isGoodOver.pullbackDefined) ≅
        S.etaDerivedPullbackObject (c ≫ h)
          ((S.isGoodOver_comp h hD c hc.isGoodOver.pullbackDefined).mpr
            hc.isGoodOver.isGoodTriple).pullbackDefined)
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.exists_lift_and_nonempty_etaDerivedPullbackObject_iso_of_isGoodOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodOverEtaBaseChangeGeneral.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodOverEtaBaseChangeGeneral.lean#L190). The attribute's comment: “the final assertion: for `b` with the two properties of tag 0GTY and `h` good for the triple, the unique `k` with `h = b . k` satisfies `L eta_J Lh^* M ≅ Lk^* Q`. It is the displayed identification at c = 1\_Y; the displayed identification itself, for a general `c`, is exists\_lift\_and\_nonempty\_etaDerivedPullbackObject\_iso\_of\_isGoodBlowup”.

> Let `b : X' ⟶ X` satisfy `IsGoodBlowup`. If moreover `(Y, E, Lh^*M)` is a good triple, then
> the unique `k : Y ⟶ X'` with `h = b ∘ k` satisfies
>
> `Lη_𝒥 Lh^*M ≅ Lk^* Q`.
>
> This is `exists_lift_and_nonempty_etaDerivedPullbackObject_iso_of_isGoodBlowup` at `c = 𝟙_Y`,
> which satisfies `IsGoodBlowup` for an already good triple by `isGoodBlowup_id`.

```lean
theorem exists_lift_and_nonempty_etaDerivedPullbackObject_iso_of_isGoodOver
    (S : ComplexAndDivisorSituation.{u, d}) {X' Y : Scheme.{u}}
    (b : X' ⟶ S.X) (hb : S.IsGoodBlowup b) (h : Y ⟶ S.X) (hh : S.IsGoodOver h) :
    ∃ k : Y ⟶ X', k ≫ b = h ∧
      Nonempty ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
          k.toLRSHom.toShHom).obj
            (S.etaDerivedPullbackObject b hb.isGoodOver.pullbackDefined) ≅
        S.etaDerivedPullbackObject h hh.pullbackDefined)
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.exists_lift_isStrictTransform_and_etaDerivedPullbackObject_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/ModificationStrictTransform.lean, line 242](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/ModificationStrictTransform.lean#L242). The attribute's comment: “the strict transform assertion, for every blowing up structure on b over an open W whose centre is supported in D, and the identification Lη\_J' L(h ∘ c)^* M ≅ L(h')^* Q; the last assertion is `exists_lift_and_nonempty_etaDerivedPullbackObject_iso_of_isGoodOver`”.

> **Stacks tag 0F8V.**  Let `(X, D, M)` be a triple as in Situation 0F8S, let `h : Y ⟶ X` be a
> morphism such that `E = h⁻¹D` is defined, and let `b : X' ⟶ X` and `c : Y' ⟶ Y` have
> properties (1) and (2) of Stacks tag 0GTY for `(X, D, M)` and for `(Y, E, Lh^*M)`.  Then:
>
> * there is a unique `h' : Y' ⟶ X'` with `b ∘ h' = h ∘ c`;
> * for every open `W ⊆ X` and every ideal sheaf `ℐ` on `W` with support inside `D` such that
>   `b⁻¹(W) ⟶ W` is the blowing up of `W` in `ℐ`, the morphism `(h', c)` identifies `c⁻¹(h⁻¹W)`
>   with the strict transform of `h⁻¹W` with respect to that blowing up: there is an isomorphism
>   from `c⁻¹(h⁻¹W)` onto the strict transform whose composites with the two projections of
>   `h⁻¹W ×_W Bl_ℐ W` are `c` and `h'`;
> * `(h ∘ c)⁻¹D` is defined and `Lη_{𝒥'}L(h ∘ c)^*M ≅ Lh'^*Q`, where `Q = Lη_{ℐ'}Lb^*M`.
>
> The last assertion of the tag, the case `c = 𝟙_Y`, is
> `exists_lift_and_nonempty_etaDerivedPullbackObject_iso_of_isGoodOver`.

```lean
theorem exists_lift_isStrictTransform_and_etaDerivedPullbackObject_iso {X' Y Y' : Scheme.{u}}
    (b : X' ⟶ S.X) (hb : S.IsGoodBlowup b) (h : Y ⟶ S.X)
    (hE : Stacks.Divisors.IsPullbackDefined h S.D) (c : Y' ⟶ Y)
    (hc : (S.pullback h hE).IsGoodBlowup c) :
    ∃ h' : Y' ⟶ X', h' ≫ b = c ≫ h ∧ (∀ k : Y' ⟶ X', k ≫ b = c ≫ h → k = h') ∧
      (∀ (W : S.X.Opens) (I : W.toScheme.IdealSheafData),
        Disjoint ((W.ι ⁻¹ᵁ S.D.support.compl : W.toScheme.Opens) : Set W.toScheme)
          (I.support : Set W.toScheme) →
        ∀ e : blowUp I ≅ (b ⁻¹ᵁ W).toScheme,
          e.hom ≫ (b ⁻¹ᵁ W).ι ≫ b = blowUpToBase I ≫ W.ι →
          ∃ φ : (c ⁻¹ᵁ (h ⁻¹ᵁ W)).toScheme ≅
              (Stacks.StrictTransform.ideal (h ∣_ W) (blowUpToBase I)
                (exceptionalIdeal I)).subscheme,
            φ.hom ≫ (Stacks.StrictTransform.ideal (h ∣_ W) (blowUpToBase I)
                (exceptionalIdeal I)).subschemeι ≫ pullback.fst (h ∣_ W) (blowUpToBase I) ≫
                (h ⁻¹ᵁ W).ι = (c ⁻¹ᵁ (h ⁻¹ᵁ W)).ι ≫ c ∧
            φ.hom ≫ (Stacks.StrictTransform.ideal (h ∣_ W) (blowUpToBase I)
                (exceptionalIdeal I)).subschemeι ≫ pullback.snd (h ∣_ W) (blowUpToBase I) ≫
                e.hom ≫ (b ⁻¹ᵁ W).ι = (c ⁻¹ᵁ (h ⁻¹ᵁ W)).ι ≫ h') ∧
      ∃ hJ' : Stacks.Divisors.IsPullbackDefined (c ≫ h) S.D,
        Nonempty (S.etaDerivedPullbackObject (c ≫ h) hJ' ≅
          (derivedPullback h'.toLRSHom.toShHom).obj
            (S.etaDerivedPullbackObject b hb.isGoodOver.pullbackDefined))
```

## Tag 0F8W, a lemma

[Tag 0F8W](https://stacks.math.columbia.edu/tag/0F8W) in the Stacks Project.

**`AlgebraicGeometry.ComplexAndDivisorSituation.isIso_pullback_snd_goodBlowupToBase_locallyFreeLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodBlowupLocallyFree.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodBlowupLocallyFree.lean#L89). The attribute's comment: “the morphism `b : X' ⟶ X` of tag 0GTY is an isomorphism over the maximal open `W ⊆ X` on which the cohomology sheaves of `M` are locally free”.

> **Stacks tag 0F8W.**  In Situation 0F8S let `W ⊂ X` be the maximal open subscheme over which
> the cohomology sheaves of `M` are locally free.  The morphism `b : X' ⟶ X` of Stacks tag 0GTY is
> an isomorphism over `W`.
>
> Over an affine chart `(U, A, f, M^•)` the morphism `b` is the blowing up of `U` in the product
> `∏ᵢ I_i(M^•, f)` of the determinantal ideals of the chart, by
> `exists_iso_pullback_blowUp_goodBlowupToBase`; on a chart contained in `W` that centre is locally
> generated by a power of the equation `f` of the divisor, hence an effective Cartier divisor, so
> blowing up in it changes nothing (`AffineChart.isIso_blowUpToBase_of_le_locallyFreeLocus`); and the
> charts contained in `W` cover `W` because the chart domains form a basis of the topology of `X`
> (`exists_chart_mem_le`).  Being an isomorphism is Zariski local on the target, so the chart-local
> statement globalises.

```lean
theorem isIso_pullback_snd_goodBlowupToBase_locallyFreeLocus :
    IsIso (Limits.pullback.snd S.goodBlowupToBase S.locallyFreeLocus.ι)
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.isIso_morphismRestrict_goodBlowupToBase_locallyFreeLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodBlowupLocallyFree.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodBlowupLocallyFree.lean#L99). The attribute's comment: “the restriction `b ∣_ W : b^{-1}W ⟶ W` of the morphism of tag 0GTY over the maximal open `W ⊆ X` on which the cohomology sheaves of `M` are locally free is an isomorphism”.

> **Stacks tag 0F8W, written as the restriction of `b` over `W`.**  The morphism
> `b ∣_ W : b⁻¹W ⟶ W` induced by the morphism of tag 0GTY is an isomorphism.

```lean
theorem isIso_morphismRestrict_goodBlowupToBase_locallyFreeLocus :
    IsIso (S.goodBlowupToBase ∣_ S.locallyFreeLocus)
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.AffineChart.isIso_blowUpToBase_of_le_locallyFreeLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/LocallyFreeLocus.lean, line 313](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/LocallyFreeLocus.lean#L313). The attribute's comment: “the affine-chart case: over an affine chart contained in the locally free locus `W` the centre in which tag 0GTY blows the chart up is locally generated by a power of the equation of the divisor, hence an effective Cartier divisor, so blowing the chart up in that centre is an isomorphism”.

> **The affine-chart case of Stacks tag 0F8W.**  Over an affine chart contained in the
> locally free locus `W` the centre `∏ᵢ I_i(M^•, f)` in which tag 0GTY blows the chart up is an
> effective Cartier divisor, so blowing the chart up in it is an isomorphism; by tag 0GTY that
> blowup is the restriction `b⁻¹(U) → U` of `b`.

```lean
theorem isIso_blowUpToBase_of_le_locallyFreeLocus (C : AffineChart S)
    (hCW : C.U.1 ≤ S.locallyFreeLocus) :
    IsIso (AlgebraicGeometry.blowUpToBase C.blowupCentreIdealSheaf)
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.isIso_pullback_snd_locallyFreeLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/LocallyFreeLocus.lean, line 367](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/LocallyFreeLocus.lean#L367). The attribute's comment: “the general form, over an arbitrary morphism which has the affine-chart description of tag 0GTY: a morphism which over every affine chart is the blowing up of that chart in the product of its determinantal ideals is an isomorphism over `W`, for an open `W` covered by the affine charts contained in it. The tag for the morphism tag 0GTY produces, with both descriptions discharged, is AlgebraicGeometry.ComplexAndDivisorSituation.isIso\_pullback\_snd\_goodBlowupToBase\_locallyFreeLocus”.

> **Stacks tag 0F8W.**  In Situation 0F8S let `W ⊂ X` be the maximal open subscheme over
> which the cohomology sheaves of `M` are locally free.  A morphism `b : X' ⟶ X` which over
> every affine chart `(U, A, f, M^•)` of the triple is the blowing up of `U` in the product
> `∏ᵢ I_i(M^•, f)` of its determinantal ideals — as the morphism of tag 0GTY is — is an
> isomorphism over `W`, provided every point of `W` lies in an affine chart contained in `W`.

```lean
theorem isIso_pullback_snd_locallyFreeLocus {X' : Scheme.{u}} (b : X' ⟶ S.X)
    (hchart : ∀ C : AffineChart S, ∃ e : Limits.pullback b C.U.1.ι ≅
        AlgebraicGeometry.blowUp C.blowupCentreIdealSheaf,
      e.hom ≫ AlgebraicGeometry.blowUpToBase C.blowupCentreIdealSheaf
        = Limits.pullback.snd b C.U.1.ι)
    (hcov : ∀ x ∈ S.locallyFreeLocus, ∃ C : AffineChart S,
      x ∈ C.U.1 ∧ C.U.1 ≤ S.locallyFreeLocus) :
    IsIso (Limits.pullback.snd b S.locallyFreeLocus.ι)
```

## Tag 0GTZ, a lemma

[Tag 0GTZ](https://stacks.math.columbia.edu/tag/0GTZ) in the Stacks Project.

**`AlgebraicGeometry.ComplexAndDivisorSituation.locallyOfFinitePresentation_and_comap_eq_bot_of_ideal_eq_obstructionIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodTripleSubscheme.lean, line 391](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodTripleSubscheme.lean#L391). The attribute's comment: “the finite presentation of the closed immersion `i : T → D` and part (1), at a closed subscheme `T` of `D` cutting out the obstruction ideal of Tag 0F81 on every good affine chart; such a `T` is constructed, and the tag stated existentially, in AlgebraicGeometry.ComplexAndDivisorSituation.exists\_isGoodChartOpen\_ideal\_eq\_obstructionIdeal of GoodTripleSubschemeExistence.lean. Parts (2) and (3), which concern `Li^*Lη_I M`, rest on identifying it over a good chart with the chart-local décalage, for which the affine comparison of Tag 08DW is proved and the remaining ingredient is the chart-level form of Tag 0GTV's second assertion recorded as AlgebraicGeometry.ComplexAndDivisorSituation.ChartDecalage”.

> **More on Flatness, Tag 0GTZ: the finite presentation of the closed immersion and part
> (1).**  Let `(X, D, M)` be a good triple as in Situation 0F8S and let `T ⊆ D` be a closed
> subscheme whose ideal over `D ∩ U` is the total obstruction ideal `J(M^•, f)` of Tag 0F81 for
> every affine chart `(U, A, f, M^•)` with principal determinantal ideals.  Then the closed
> immersion `i : T → D` is locally of finite presentation, and `T` scheme-theoretically contains
> `D ∩ W`, where `W ⊆ X` is the maximal open over which the cohomology sheaves of `M` are locally
> free: the inverse image of the ideal sheaf of `T` on `D ∩ W` is zero.
>
> `T` is a variable of this statement; the subscheme itself is glued from the local closed
> subschemes cut out by `J(M^•, f)` along a cover of `D` by good charts in
> `AlgebraicGeometry.ComplexAndDivisorSituation.exists_isGoodChartOpen_ideal_eq_obstructionIdeal`,
> which combines with this theorem into the existential assertion of the tag.

```lean
theorem locallyOfFinitePresentation_and_comap_eq_bot_of_ideal_eq_obstructionIdeal :
    LocallyOfFinitePresentation T.subschemeι ∧
      T.comap (S.D.subschemeι ⁻¹ᵁ S.locallyFreeLocus).ι = ⊥
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.isFiniteLocallyFree_etaDerivedPullbackRestrictHomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodTripleSubschemeCohomology.lean, line 577](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodTripleSubschemeCohomology.lean#L577). The attribute's comment: “part (2)”.

> **Stacks tag 0GTZ, part (2).**  Let `(X, D, M)` be a triple, let `b : X' ⟶ X` be a
> morphism along which the pullback `D'` of the divisor is defined and the pulled-back triple
> `(X', D', Lb^*M)` is good, and let `T ⊆ D'` be the closed subscheme cut out on every chart with
> principal determinantal ideals by the obstruction ideal of More on Algebra, Tag 0F81.  Then the
> cohomology sheaves of `Lj^*Lη_{ℐ'}Lb^*M` are finite locally free, `j : T ⟶ X'` being the
> inclusion.
>
> On a chart with principal determinantal ideals they are the sheaves of the cohomology modules of
> `η_f M^• ⊗_A C`, `C = (A ⧸ fA) ⧸ J(M^•, f)`, which are finite projective by Tag 0F81; such charts
> cover `T`, the pulled-back triple being good.

```lean
theorem isFiniteLocallyFree_etaDerivedPullbackRestrictHomology
    (hS : (S.pullback b hb).IsGoodTriple)
    (hT : ∀ C : AffineChart (S.pullback b hb), (∀ i : ℤ, (C.determinantalIdeal i).IsPrincipal) →
      T.ideal C.divisorAffineOpen = C.obstructionIdeal) (n : ℤ) :
    AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u}
      (S.etaDerivedPullbackRestrictHomology b hb
        (T.subschemeι ≫ (S.pullback b hb).D.subschemeι) n)
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.finiteLocallyFreeRank_etaDerivedPullbackRestrictHomology_eq_fiberRank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodTripleSubschemeCohomology.lean, line 689](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodTripleSubschemeCohomology.lean#L689). The attribute's comment: “part (3)”.

> **Stacks tag 0GTZ, part (3).**  In the situation of
> `isFiniteLocallyFree_etaDerivedPullbackRestrictHomology`, at a point `t ∈ T` whose image in `X'`
> lies in the locally free locus of `Lb^*M`, the rank of `H^n(Lj^*Lη_{ℐ'}Lb^*M)` at `t` is the
> rank of `H^n(Lb^*M)` at the image of `t`.
>
> Around that image there is a chart with principal determinantal ideals inside the locally free
> locus; its cohomology modules are finite projective, so the décalage has the same cohomology
> (More on Algebra, Tag 0F7P) and its cohomology commutes with base change to `C`.

```lean
theorem finiteLocallyFreeRank_etaDerivedPullbackRestrictHomology_eq_fiberRank
    (hS : (S.pullback b hb).IsGoodTriple)
    (hT : ∀ C : AffineChart (S.pullback b hb), (∀ i : ℤ, (C.determinantalIdeal i).IsPrincipal) →
      T.ideal C.divisorAffineOpen = C.obstructionIdeal) (n : ℤ) (t : T.subscheme)
    (ht : (T.subschemeι ≫ (S.pullback b hb).D.subschemeι) t ∈
      (S.pullback b hb).locallyFreeLocus) :
    @Scheme.Modules.finiteLocallyFreeRank T.subscheme
        (S.etaDerivedPullbackRestrictHomology b hb
          (T.subschemeι ≫ (S.pullback b hb).D.subschemeι) n)
        (S.isFiniteLocallyFree_etaDerivedPullbackRestrictHomology hS hT n) t =
      Scheme.Modules.fiberRank ((S.pullback b hb).cohomologySheaf n)
        ((T.subschemeι ≫ (S.pullback b hb).D.subschemeι) t)
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.exists_isGoodChartOpen_ideal_eq_obstructionIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodTripleSubschemeExistence.lean, line 303](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodTripleSubschemeExistence.lean#L303). The attribute's comment: “the existence of the closed immersion `i : T ⟶ D` of finite presentation, and part (1). `T` is glued from the obstruction ideals of Tag 0F81 on the good affine charts by AlgebraicGeometry.Scheme.IdealSheafData.ofAffineFamily. Parts (2) and (3) concern `Li^*Lη_I M`: over and above the affine comparison of Tag 08DW they need the chart-level comparison AlgebraicGeometry.ComplexAndDivisorSituation.ChartDecalage, and part (3) then reads off Tag 0GTA --- formalized in both halves in StacksFrontier.Algebra.Category.ModuleCat.Sheaf.EtaSheafStalk --- at the points part (1) supplies, `i` being an isomorphism over `D` intersected with the locally free locus”.

> **More on Flatness, Tag 0GTZ: the closed subscheme `T` of `D` exists, the closed immersion
> `i : T ⟶ D` is of finite presentation, and `T` contains `D ∩ W` scheme-theoretically.**  Let
> `(X, D, M)` be a good triple as in Situation 0F8S.  There is a closed subscheme `T ⊆ D` whose
> ideal over `D ∩ U` is the total obstruction ideal `J(M^•, f)` of More on Algebra, Tag 0F81 for
> every affine chart `(U, A, f, M^•)` with principal determinantal ideals; the closed immersion
> `i : T ⟶ D` is locally of finite presentation; and the inverse image on `D ∩ W` of the ideal
> sheaf of `T` is zero, where `W ⊆ X` is the maximal open over which the cohomology sheaves of `M`
> are locally free.
>
> `T` is `goodChartSubscheme`, glued from the chart-local obstruction ideals by
> `AlgebraicGeometry.Scheme.IdealSheafData.ofAffineFamily`; the two properties are
> `locallyOfFinitePresentation_and_comap_eq_bot_of_ideal_eq_obstructionIdeal`.

```lean
theorem exists_isGoodChartOpen_ideal_eq_obstructionIdeal (hS : S.IsGoodTriple) :
    ∃ T : S.D.subscheme.IdealSheafData,
      (∀ C : AffineChart S, (∀ i : ℤ, (C.determinantalIdeal i).IsPrincipal) →
          T.ideal C.divisorAffineOpen = C.obstructionIdeal) ∧
        LocallyOfFinitePresentation T.subschemeι ∧
          T.comap (S.D.subschemeι ⁻¹ᵁ S.locallyFreeLocus).ι = ⊥
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.exists_subscheme_isClosedImmersion_etaPullbackHomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/ObstructionSubschemeCohomology.lean, line 381](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/ObstructionSubschemeCohomology.lean#L381). The attribute's comment: “the existence of the closed immersion i : T → D of finite presentation together with parts (1), (2) and (3); locally free in (2) is proved in the stronger form finite locally free, and part (3) is stated for every degree n”.

> **More on Flatness, Tag 0GTZ.**  Let `X`, `D`, `I`, `M` be as in Situation 0F8S.  If
> `(X, D, M)` is a good triple, then there exists a closed immersion `i : T ⟶ D` of finite
> presentation such that
>
> 1. `T` scheme theoretically contains `D ∩ W`, where `W ⊆ X` is the maximal open over which the
>    cohomology sheaves of `M` are locally free: the ideal sheaf of `T` vanishes on `D ∩ W`;
> 2. the cohomology sheaves of `Li^*(Lη_I M)` are (finite) locally free; and
> 3. for every point `t ∈ T` with image `x = i(t) ∈ W`, the rank of `H^n(M)_x` over `𝒪_{X, x}`
>    and the rank of `H^n(Li^*(Lη_I M))_t` over `𝒪_{T, t}` agree, for every `n`.
>
> The closed subscheme `T ⊆ D` is cut out by the ideal sheaf `obstructionIdealSheaf`, which on a
> good affine chart `(U, A, f, M^•)` is the total obstruction ideal `J(M^•, f)` of More on Algebra,
> Tag 0F81; these ideals glue because they do not depend on the chart (Tag 0GSW, flat base
> change, and `etaTotalDirectSumIdeal_unit_mul`).  A closed immersion is quasi-compact and
> separated, so being of finite presentation is being locally of finite presentation, which holds
> because the obstruction ideals are finitely generated.  Here `Li^*(Lη_I M)` is the derived
> pullback along `T ⟶ D ⟶ X` of the derived décalage of `M`, and its `n`-th cohomology sheaf is
> `etaPullbackHomology`; `W` is `ComplexAndDivisorSituation.locallyFreeLocus`, the open of the
> points at which every cohomology sheaf of `M` has a finite free stalk, which by Stacks 0GT1 is
> the maximal open over which these sheaves are finite locally free.

```lean
theorem exists_subscheme_isClosedImmersion_etaPullbackHomology (hS : S.IsGoodTriple) :
    ∃ T : S.D.subscheme.IdealSheafData,
      IsClosedImmersion T.subschemeι ∧ LocallyOfFinitePresentation T.subschemeι ∧
      T.comap (S.D.subschemeι ⁻¹ᵁ S.locallyFreeLocus).ι = ⊥ ∧
      (∀ n : ℤ, Scheme.Modules.IsFiniteLocallyFree
        (S.etaPullbackHomology (T.subschemeι ≫ S.D.subschemeι) n)) ∧
      ∀ t : T.subscheme, S.D.subschemeι (T.subschemeι t) ∈ S.locallyFreeLocus → ∀ n : ℤ,
        Module.finrank (S.X.presheaf.stalk (S.D.subschemeι (T.subschemeι t)))
            ((S.objectHomology n).presheaf.stalk (S.D.subschemeι (T.subschemeι t))) =
          Module.finrank (T.subscheme.presheaf.stalk t)
            ((S.etaPullbackHomology (T.subschemeι ≫ S.D.subschemeι) n).presheaf.stalk t)
```

## Tag 0F8X, a lemma

[Tag 0F8X](https://stacks.math.columbia.edu/tag/0F8X) in the Stacks Project.

**`AlgebraicGeometry.ComplexAndDivisorSituation.locallyOfFinitePresentation_and_comap_eq_bot_of_isGoodOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/BlowupSubscheme.lean, line 375](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/BlowupSubscheme.lean#L375). The attribute's comment: “the finite presentation of `i : T → b^{-1}D` and part (1), in the general form: over any `b` satisfying condition (1) of tag 0GTY and flat over `W` --- which is what Tag 0F8W supplies for the morphism tag 0GTY produces --- and for a closed subscheme `T` of `b^{-1}D` given to cut out the obstruction ideal of Tag 0F81 on every good chart of the pulled-back triple, as in Tag 0GTZ. Parts (2) and (3) specialize parts (2) and (3) of Tag 0GTZ, which need the chart-level comparison AlgebraicGeometry.ComplexAndDivisorSituation.ChartDecalage over and above Tag 08DW --- that tag being proved in both its parts. The tag over the morphism tag 0GTY produces is AlgebraicGeometry.ComplexAndDivisorSituation.locallyOfFinitePresentation\_and\_comap\_eq\_bot\_goodBlowupToBase”.

> In Situation 0F8S let `b : X' ⟶ X` be good for the triple — condition (1) of tag 0GTY —
> so that `D' = b⁻¹D` is defined and `(X', D', Lb^*M)` is a good triple, let `W ⊆ X` be the
> maximal open over which the cohomology sheaves of `M` are locally free, and suppose that
> `b⁻¹W ↪ X' ⟶ X` is flat. Let `T ⊆ D'` be a closed subscheme whose ideal over `D' ∩ U` is the
> total obstruction ideal `J(N^•, g)` of More on Algebra, tag 0F81 for every affine chart
> `(U, g, N^•)` of the pulled-back triple with principal determinantal ideals. Then
>
> * the closed immersion `i : T ⟶ D'` is locally of finite presentation, and
> * `D' ∩ b⁻¹(W) ⊆ T` scheme theoretically: the inverse image on `D' ∩ b⁻¹(W)` of the ideal sheaf
>   of `T` is zero.

```lean
theorem locallyOfFinitePresentation_and_comap_eq_bot_of_isGoodOver
    {X' : Scheme.{u}} (b : X' ⟶ S.X) (hb : S.IsGoodOver b)
    (hflat : AlgebraicGeometry.Flat ((b ⁻¹ᵁ S.locallyFreeLocus).ι ≫ b))
    (T : (S.pullback b hb.pullbackDefined).D.subscheme.IdealSheafData)
    (hT : ∀ C : AffineChart (S.pullback b hb.pullbackDefined),
      (∀ i : ℤ, (C.determinantalIdeal i).IsPrincipal) →
        T.ideal C.divisorAffineOpen = C.obstructionIdeal) :
    LocallyOfFinitePresentation T.subschemeι ∧
      T.comap ((S.pullback b hb.pullbackDefined).D.subschemeι ⁻¹ᵁ
        (b ⁻¹ᵁ S.locallyFreeLocus)).ι = ⊥
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.locallyOfFinitePresentation_and_comap_eq_bot_goodBlowupToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodBlowupDivisorSubscheme.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodBlowupDivisorSubscheme.lean#L95). The attribute's comment: “the finite presentation of `i : T → b^{-1}D` and part (1), stated for the morphism `b` of tag 0GTY itself --- namely AlgebraicGeometry.ComplexAndDivisorSituation.goodBlowupToBase, whose flatness over `W` is tag 0F8W --- and for a closed subscheme `T` of `b^{-1}D` given to cut out the obstruction ideal of Tag 0F81 on every good chart of the pulled-back triple, as in the formalized Tag 0GTZ. Parts (2) and (3) specialize parts (2) and (3) of Tag 0GTZ, which need the chart-level comparison AlgebraicGeometry.ComplexAndDivisorSituation.ChartDecalage over and above Tag 08DW --- that tag being formalized in both its parts”.

> **Stacks tag 0F8X for the morphism `b : X' ⟶ X` of Stacks tag 0GTY: the finite presentation
> of the closed immersion `i : T ⟶ D'` and part (1).**  Let `b` be the morphism of tag 0GTY, so
> that `D' = b⁻¹D` is defined and `(X', D', Lb^*M)` is a good triple, and let `W ⊆ X` be the
> maximal open over which the cohomology sheaves of `M` are locally free.  Let `T ⊆ D'` be a closed
> subscheme whose ideal over `D' ∩ V` is the total obstruction ideal `J(N^•, g)` of More on
> Algebra, tag 0F81 for every affine chart `(V, g, N^•)` of the pulled-back triple with principal
> determinantal ideals.  Then
>
> * the closed immersion `i : T ⟶ D'` is locally of finite presentation, and
> * `D' ∩ b⁻¹(W) ⊆ T` scheme theoretically.
>
> This is `locallyOfFinitePresentation_and_comap_eq_bot_of_isGoodOver` read at `goodBlowupToBase`:
> condition (1) of tag 0GTY holds for it by `isGoodOver_goodBlowupToBase`, and the flatness of
> `b⁻¹W ↪ X' ⟶ X` is Stacks tag 0F8W, `flat_ι_comp_goodBlowupToBase_locallyFreeLocus`.

```lean
theorem locallyOfFinitePresentation_and_comap_eq_bot_goodBlowupToBase
    (T : (S.pullback S.goodBlowupToBase
      S.isGoodOver_goodBlowupToBase.pullbackDefined).D.subscheme.IdealSheafData)
    (hT : ∀ C : AffineChart (S.pullback S.goodBlowupToBase
        S.isGoodOver_goodBlowupToBase.pullbackDefined),
      (∀ i : ℤ, (C.determinantalIdeal i).IsPrincipal) →
        T.ideal C.divisorAffineOpen = C.obstructionIdeal) :
    LocallyOfFinitePresentation T.subschemeι ∧
      T.comap ((S.pullback S.goodBlowupToBase
        S.isGoodOver_goodBlowupToBase.pullbackDefined).D.subschemeι ⁻¹ᵁ
          (S.goodBlowupToBase ⁻¹ᵁ S.locallyFreeLocus)).ι = ⊥
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.exists_closedSubscheme_goodBlowup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodBlowupSubschemeCohomology.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodBlowupSubschemeCohomology.lean#L111). The attribute's comment: “the closed immersion `i : T → D'` of finite presentation (locally of finite presentation) with parts (1), (2) and (3), for the morphism `b` of tag 0GTY, AlgebraicGeometry.ComplexAndDivisorSituation.goodBlowupToBase; `Li^*Q` is etaDerivedPullbackRestrict of `Q = Lη_{ℐ'}Lb^*M` along `T → D' → X'`, and the rank of a free stalk is Module.finrank”.

> **Stacks Tag 0F8X.**  In Situation 0F8S let `b : X' ⟶ X` be the morphism of tag 0GTY,
> `D' = b⁻¹D`, `Q = Lη_{ℐ'}Lb^*M` as in tag 0F8U, and `W ⊆ X` the maximal open where the
> cohomology sheaves of `M` are locally free.  There is a closed subscheme `T ⊆ D'`, with
> inclusion `i : T ⟶ D'` locally of finite presentation, such that
> 1. `D' ∩ b⁻¹(W) ⊆ T` scheme theoretically,
> 2. the cohomology sheaves of `Li^*Q` are finite locally free, and
> 3. for `t ∈ T` mapping to `x ∈ W`, `H^n(Li^*Q)_t` is free over `𝒪_{T,t}` of the rank of
>    `H^n(M)_x` over `𝒪_{X,x}`.

```lean
theorem exists_closedSubscheme_goodBlowup :
    ∃ T : (S.D.comap S.goodBlowupToBase).subscheme.IdealSheafData,
      LocallyOfFinitePresentation T.subschemeι ∧
      T.comap ((S.D.comap S.goodBlowupToBase).subschemeι ⁻¹ᵁ
          (S.goodBlowupToBase ⁻¹ᵁ S.locallyFreeLocus)).ι = ⊥ ∧
      (∀ n : ℤ, AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u}
        (S.etaDerivedPullbackRestrictHomology S.goodBlowupToBase
          S.isGoodOver_goodBlowupToBase.pullbackDefined
          (T.subschemeι ≫ (S.D.comap S.goodBlowupToBase).subschemeι) n)) ∧
      ∀ (n : ℤ) (t : T.subscheme)
        (_ : ((T.subschemeι ≫ (S.D.comap S.goodBlowupToBase).subschemeι) ≫
          S.goodBlowupToBase).base t ∈ S.locallyFreeLocus),
        letI F := S.etaDerivedPullbackRestrictHomology S.goodBlowupToBase
          S.isGoodOver_goodBlowupToBase.pullbackDefined
          (T.subschemeι ≫ (S.D.comap S.goodBlowupToBase).subschemeι) n
        letI x := ((T.subschemeι ≫ (S.D.comap S.goodBlowupToBase).subschemeι) ≫
          S.goodBlowupToBase).base t
        letI : Module (ToType (TopCat.Presheaf.stalk T.subscheme.presheaf t))
            (ToType (TopCat.Presheaf.stalk F.val.presheaf t)) :=
          RingedSpace.moduleStalk (X := T.subscheme.toRingedSpace) F t
        letI : Module (ToType (S.X.presheaf.stalk x))
            (ToType (TopCat.Presheaf.stalk (S.cohomologySheaf n).val.presheaf x)) :=
          RingedSpace.moduleStalk (X := S.X.toRingedSpace) (S.cohomologySheaf n) x
        Module.Free (ToType (TopCat.Presheaf.stalk T.subscheme.presheaf t))
            (ToType (TopCat.Presheaf.stalk F.val.presheaf t)) ∧
          Module.finrank (ToType (TopCat.Presheaf.stalk T.subscheme.presheaf t))
              (ToType (TopCat.Presheaf.stalk F.val.presheaf t)) =
            Module.finrank (ToType (S.X.presheaf.stalk x))
              (ToType (TopCat.Presheaf.stalk (S.cohomologySheaf n).val.presheaf x))
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.exists_closedSubscheme_etaDerivedPullback_goodBlowupToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodTripleSubschemeCohomology.lean, line 924](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodTripleSubschemeCohomology.lean#L924).

> **Stacks tag 0F8X.**  Let `b : X' ⟶ X` be the morphism of Stacks tag 0GTY, `D' = b⁻¹D` and
> `Q = Lη_{ℐ'}Lb^*M`, and let `W ⊆ X` be the locally free locus of `M`.  There is a closed
> immersion `i : T ⟶ D'` of finite presentation such that
> 1. `D' ∩ b⁻¹(W) ⊆ T` scheme-theoretically,
> 2. the cohomology sheaves of `L(i ≫ D' ⟶ X')^*Q` are finite locally free, and
> 3. at a point `t ∈ T` over `W` the rank of `H^n(L(i ≫ D' ⟶ X')^*Q)` at `t` is the rank of
>    `H^n(M)` at the image of `t`.
>
> `T` is the closed subscheme of Stacks tag 0GTZ for the pulled-back triple.

```lean
theorem exists_closedSubscheme_etaDerivedPullback_goodBlowupToBase :
    ∃ T : (S.pullback S.goodBlowupToBase
        S.isGoodBlowup_goodBlowupToBase.isGoodOver.pullbackDefined).D.subscheme.IdealSheafData,
      LocallyOfFinitePresentation T.subschemeι ∧
      T.comap ((S.pullback S.goodBlowupToBase
          S.isGoodBlowup_goodBlowupToBase.isGoodOver.pullbackDefined).D.subschemeι ⁻¹ᵁ
            (S.goodBlowupToBase ⁻¹ᵁ S.locallyFreeLocus)).ι = ⊥ ∧
      (∀ n : ℤ, AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u}
        (S.etaDerivedPullbackRestrictHomology S.goodBlowupToBase
          S.isGoodBlowup_goodBlowupToBase.isGoodOver.pullbackDefined
          (T.subschemeι ≫ (S.pullback S.goodBlowupToBase
            S.isGoodBlowup_goodBlowupToBase.isGoodOver.pullbackDefined).D.subschemeι) n)) ∧
      ∀ (n : ℤ) (t : T.subscheme),
        ((T.subschemeι ≫ (S.pullback S.goodBlowupToBase
          S.isGoodBlowup_goodBlowupToBase.isGoodOver.pullbackDefined).D.subschemeι) ≫
            S.goodBlowupToBase) t ∈ S.locallyFreeLocus →
        Scheme.Modules.fiberRank (S.etaDerivedPullbackRestrictHomology S.goodBlowupToBase
            S.isGoodBlowup_goodBlowupToBase.isGoodOver.pullbackDefined
            (T.subschemeι ≫ (S.pullback S.goodBlowupToBase
              S.isGoodBlowup_goodBlowupToBase.isGoodOver.pullbackDefined).D.subschemeι) n) t =
          Scheme.Modules.fiberRank (S.cohomologySheaf n)
            (((T.subschemeι ≫ (S.pullback S.goodBlowupToBase
              S.isGoodBlowup_goodBlowupToBase.isGoodOver.pullbackDefined).D.subschemeι) ≫
                S.goodBlowupToBase) t)
```

## Tag 0F8Y, a lemma

[Tag 0F8Y](https://stacks.math.columbia.edu/tag/0F8Y) in the Stacks Project.

**`AlgebraicGeometry.ComplexAndDivisorSituation.exists_isClopen_rankStratum_etaDerivedPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/DivisorRankStrata.lean, line 259](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/DivisorRankStrata.lean#L259). The attribute's comment: “the rank stratum `T(ρ)` is open and closed, contains the inverse image of `W(ρ)` and has `H^n(Li^*Q)` free of rank `ρ_n`. The data are the ones tag 0F8Y is given, over an arbitrary `b` along which the pullback of `D` is defined: the morphism `i : T → D'` of tag 0F8X together with its parts (2) and (3), which are the binders `hQ` and `hrank` and are the instance at the pulled-back triple of parts (2) and (3) of tag 0GTZ, which need the chart-level comparison AlgebraicGeometry.ComplexAndDivisorSituation.ChartDecalage over and above tag 08DW --- that tag being proved in both its parts; plus `hbd`, the local boundedness of `H^n(Li^*Q)`, a consequence of perfectness of `Li^*Q`, and `hM`, the finite local freeness of `H^n(M)` over `W`, which tag 0GT1's second assertion gives over the universe-lifted locus of Stacks.Cohomology.PerfectComplexes.cohomologyFiniteFreeLocus rather than over the open subscheme `W` built from AlgebraicGeometry.RingedSpace.cohomologyFiniteFreeLocus. For the morphism tag 0GTY produces see AlgebraicGeometry.ComplexAndDivisorSituation.exists\_isClopen\_rankStratum\_goodBlowupToBase”.

> **Stacks tag 0F8Y.**  In Situation 0F8S let `b : X' ⟶ X` be a morphism along which the
> pullback `D' = b⁻¹D` of the effective Cartier divisor is defined, let
> `Q = Lη_{ℐ'}Lb^*M` be as in Stacks tag 0F8U, let `i : T ⟶ D'` be as in Stacks tag 0F8X and let
> `ρ = (ρ_n)_{n ∈ ℤ}` be ranks.  Then there is an open and closed `T(ρ) ⊆ T` which contains the
> inverse image in `T` of `W(ρ)`, the rank-`ρ` stratum of the cohomology sheaves of `M` on the
> locally free locus `W`, and on which `H^n(Li^*Q)` is free of rank `ρ_n` near every point.
>
> `T(ρ)` is the rank stratum of the family `H^n(Li^*Q)`, as in the source.  It is open and closed
> by `AlgebraicGeometry.Scheme.Modules.isClopen_rankStratumSet`; the containment is the rank
> agreement `hrank` of tag 0F8X (3) read against the definition of `W(ρ)`, which is the source's
> own one-line proof; and the local freeness is
> `AlgebraicGeometry.Scheme.Modules.exists_free_nbhd_of_mem_rankStratumSet`.

```lean
theorem exists_isClopen_rankStratum_etaDerivedPullback
    (S : ComplexAndDivisorSituation.{u, d}) {X' : Scheme.{u}} (b : X' ⟶ S.X)
    (hb : Stacks.Divisors.IsPullbackDefined b S.D) {T : Scheme.{u}}
    (i : T ⟶ (S.D.comap b).subscheme) (ρ : ℤ → ℕ)
    (hQ : ∀ n : ℤ, AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u}
      (S.etaDerivedPullbackRestrictHomology b hb (i ≫ (S.D.comap b).subschemeι) n))
    (hbd : ∀ t : T, ∃ V : T.Opens, t ∈ V ∧ ∃ s : Finset ℤ, ∀ n ∉ s, ∀ v ∈ V,
      @Scheme.Modules.finiteLocallyFreeRank T
        (S.etaDerivedPullbackRestrictHomology b hb (i ≫ (S.D.comap b).subschemeι) n)
        (hQ n) v = 0)
    (hM : ∀ n : ℤ, AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u}
      (S.locallyFreeLocusCohomologySheaf n))
    (hrank : ∀ (n : ℤ) (t : T)
      (hw : ((i ≫ (S.D.comap b).subschemeι) ≫ b).base t ∈ S.locallyFreeLocus),
      @Scheme.Modules.finiteLocallyFreeRank T
          (S.etaDerivedPullbackRestrictHomology b hb (i ≫ (S.D.comap b).subschemeι) n)
          (hQ n) t =
        @Scheme.Modules.finiteLocallyFreeRank S.locallyFreeLocus.toScheme
          (S.locallyFreeLocusCohomologySheaf n) (hM n)
          ⟨((i ≫ (S.D.comap b).subschemeι) ≫ b).base t, hw⟩) :
    ∃ Tρ : Set T, IsClopen Tρ ∧
      (∀ (t : T) (hw : ((i ≫ (S.D.comap b).subschemeι) ≫ b).base t ∈ S.locallyFreeLocus),
        (⟨((i ≫ (S.D.comap b).subschemeι) ≫ b).base t, hw⟩ : S.locallyFreeLocus.toScheme) ∈
            Scheme.Modules.rankStratumSet S.locallyFreeLocusCohomologySheaf hM ρ →
          t ∈ Tρ) ∧
      ∀ (n : ℤ) (t : T), t ∈ Tρ →
        ∃ (V : T.Opens) (_ : t ∈ V) (I : Type u), Nonempty (I ≃ Fin (ρ n)) ∧
          Nonempty (_root_.SheafOfModules.free.{u} I ≅
            (Scheme.Modules.toRingSheafModule
              (S.etaDerivedPullbackRestrictHomology b hb
                (i ≫ (S.D.comap b).subschemeι) n)).over V)
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.exists_isClopen_rankStratum_goodBlowupToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodBlowupRankStrata.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodBlowupRankStrata.lean#L101). The attribute's comment: “the rank stratum `T(ρ)` is open and closed, contains the inverse image of `W(ρ)` and has `H^n(Li^*Q)` free of rank `ρ_n`, stated for the morphism `b` of tag 0GTY itself, namely AlgebraicGeometry.ComplexAndDivisorSituation.goodBlowupToBase. The data are the ones tag 0F8Y is given: the closed immersion `i : T → D'` of tag 0F8X together with its parts (2) and (3), which are the binders `hQ` and `hrank` and are the instance at the pulled-back triple of parts (2) and (3) of tag 0GTZ, which need the chart-level comparison AlgebraicGeometry.ComplexAndDivisorSituation.ChartDecalage over and above tag 08DW --- that tag being formalized in both its parts; plus `hbd`, the local boundedness of the family `H^n(Li^*Q)`, a consequence of perfectness of `Li^*Q`, and `hM`, the finite local freeness of `H^n(M)` over `W`, which tag 0GT1's second assertion gives over the universe-lifted locus of Stacks.Cohomology.PerfectComplexes.cohomologyFiniteFreeLocus rather than over the open subscheme `W` built from AlgebraicGeometry.RingedSpace.cohomologyFiniteFreeLocus”.

> **Stacks tag 0F8Y for the morphism `b : X' ⟶ X` of Stacks tag 0GTY.**  Let `b` be the
> morphism of tag 0GTY, `D' = b⁻¹D`, `Q = Lη_{ℐ'}Lb^*M` the object of tag 0F8U, `i : T ⟶ D'` the
> closed immersion of tag 0F8X and `ρ = (ρ_n)_{n ∈ ℤ}` ranks.  Then there is an open and closed
> `T(ρ) ⊆ T` which contains the inverse image in `T` of `W(ρ)`, the rank-`ρ` stratum of the
> cohomology sheaves of `M` on the locally free locus `W`, and on which `H^n(Li^*Q)` is free of
> rank `ρ_n` near every point.
>
> This is
> `AlgebraicGeometry.ComplexAndDivisorSituation.exists_isClopen_rankStratum_etaDerivedPullback`
> read at `AlgebraicGeometry.ComplexAndDivisorSituation.goodBlowupToBase`, whose pullback of `D` is
> defined by
> `AlgebraicGeometry.ComplexAndDivisorSituation.isPullbackDefined_goodBlowupToBase`.  `T(ρ)` is the
> rank stratum of the family `H^n(Li^*Q)`, as in the source.

```lean
theorem exists_isClopen_rankStratum_goodBlowupToBase
    {T : Scheme.{u}} (i : T ⟶ (S.D.comap S.goodBlowupToBase).subscheme) (ρ : ℤ → ℕ)
    (hQ : ∀ n : ℤ, AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u}
      (S.etaDerivedPullbackRestrictHomology S.goodBlowupToBase
        S.isPullbackDefined_goodBlowupToBase
        (i ≫ (S.D.comap S.goodBlowupToBase).subschemeι) n))
    (hbd : ∀ t : T, ∃ V : T.Opens, t ∈ V ∧ ∃ s : Finset ℤ, ∀ n ∉ s, ∀ v ∈ V,
      @Scheme.Modules.finiteLocallyFreeRank T
        (S.etaDerivedPullbackRestrictHomology S.goodBlowupToBase
          S.isPullbackDefined_goodBlowupToBase
          (i ≫ (S.D.comap S.goodBlowupToBase).subschemeι) n)
        (hQ n) v = 0)
    (hM : ∀ n : ℤ, AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u}
      (S.locallyFreeLocusCohomologySheaf n))
    (hrank : ∀ (n : ℤ) (t : T)
      (hw : ((i ≫ (S.D.comap S.goodBlowupToBase).subschemeι) ≫ S.goodBlowupToBase).base t ∈
        S.locallyFreeLocus),
      @Scheme.Modules.finiteLocallyFreeRank T
          (S.etaDerivedPullbackRestrictHomology S.goodBlowupToBase
            S.isPullbackDefined_goodBlowupToBase
            (i ≫ (S.D.comap S.goodBlowupToBase).subschemeι) n)
          (hQ n) t =
        @Scheme.Modules.finiteLocallyFreeRank S.locallyFreeLocus.toScheme
          (S.locallyFreeLocusCohomologySheaf n) (hM n)
          ⟨((i ≫ (S.D.comap S.goodBlowupToBase).subschemeι) ≫ S.goodBlowupToBase).base t, hw⟩) :
    ∃ Tρ : Set T, IsClopen Tρ ∧
      (∀ (t : T) (hw : ((i ≫ (S.D.comap S.goodBlowupToBase).subschemeι) ≫
          S.goodBlowupToBase).base t ∈ S.locallyFreeLocus),
        (⟨((i ≫ (S.D.comap S.goodBlowupToBase).subschemeι) ≫ S.goodBlowupToBase).base t, hw⟩ :
              S.locallyFreeLocus.toScheme) ∈
            Scheme.Modules.rankStratumSet S.locallyFreeLocusCohomologySheaf hM ρ →
          t ∈ Tρ) ∧
      ∀ (n : ℤ) (t : T), t ∈ Tρ →
        ∃ (V : T.Opens) (_ : t ∈ V) (I : Type u), Nonempty (I ≃ Fin (ρ n)) ∧
          Nonempty (_root_.SheafOfModules.free.{u} I ≅
            (Scheme.Modules.toRingSheafModule
              (S.etaDerivedPullbackRestrictHomology S.goodBlowupToBase
                S.isPullbackDefined_goodBlowupToBase
                (i ≫ (S.D.comap S.goodBlowupToBase).subschemeι) n)).over V)
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.exists_isClopen_rankStratum_goodBlowup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodBlowupSubschemeRankStrata.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodBlowupSubschemeRankStrata.lean#L209).

> For `b` of tag 0GTY, `Q` of tag 0F8U, `i : T ⟶ D'` of tag 0F8X and integers `ρ_n`, some open
> and closed `T(ρ) ⊆ T` contains `D' ∩ b⁻¹(V)` scheme theoretically for every open `V` on which
> each `H^n(M)` is locally free of rank `ρ_n`, and `H^n(Li^*Q)|_{T(ρ)}` has rank `ρ_n`.

```lean
theorem exists_isClopen_rankStratum_goodBlowup (ρ : ℤ → ℤ) :
    ∃ Tρ : (S.pullbackSubscheme S.goodBlowupToBase S.isGoodOver_goodBlowupToBase).subscheme.Opens,
      IsClopen (Tρ : Set (S.pullbackSubscheme S.goodBlowupToBase
        S.isGoodOver_goodBlowupToBase).subscheme) ∧
      (∀ V : S.X.Opens,
        (∀ (n : ℤ), ∀ x ∈ V, ∃ U : S.X.Opens, x ∈ U ∧ U ≤ V ∧ ∃ ι : Type u, Finite ι ∧
          (Nat.card ι : ℤ) = ρ n ∧ Nonempty ((restrictModules S.X.toRingedSpace U).obj
            (S.cohomologySheaf n) ≅ _root_.SheafOfModules.free.{u} ι)) →
        ∃ g : ((S.D.comap S.goodBlowupToBase).subschemeι ⁻¹ᵁ
            (S.goodBlowupToBase ⁻¹ᵁ V)).toScheme ⟶ Tρ.toScheme,
          g ≫ Tρ.ι ≫
              (S.pullbackSubscheme S.goodBlowupToBase S.isGoodOver_goodBlowupToBase).subschemeι =
            ((S.D.comap S.goodBlowupToBase).subschemeι ⁻¹ᵁ (S.goodBlowupToBase ⁻¹ᵁ V)).ι) ∧
      ∀ (n : ℤ), ∀ t ∈ Tρ, ∃ U : (S.pullbackSubscheme S.goodBlowupToBase
        S.isGoodOver_goodBlowupToBase).subscheme.Opens, t ∈ U ∧ U ≤ Tρ ∧ ∃ I : Type u,
        Finite I ∧ (Nat.card I : ℤ) = ρ n ∧
          Nonempty (_root_.SheafOfModules.free.{u} I ≅
            (Scheme.Modules.toRingSheafModule (S.etaDerivedPullbackRestrictHomology
              S.goodBlowupToBase S.isGoodOver_goodBlowupToBase.pullbackDefined
              ((S.pullbackSubscheme S.goodBlowupToBase
                S.isGoodOver_goodBlowupToBase).subschemeι ≫
                  (S.D.comap S.goodBlowupToBase).subschemeι) n)).over U)
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.exists_isClopen_rankStratum_etaDerivedPullback_of_isGoodOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodTripleSubschemeCohomology.lean, line 887](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodTripleSubschemeCohomology.lean#L887).

> **Stacks tag 0F8Y.**  Let `b : X' ⟶ X` be good for the triple — for instance the morphism of
> Stacks tag 0GTY — let `T ⊆ D'` be the closed subscheme of Stacks tag 0F8X and let
> `ρ = (ρ_n)_{n ∈ ℤ}` be ranks.  There is an open and closed `T(ρ) ⊆ T` containing the inverse
> image of `W(ρ)`, the rank-`ρ` stratum of the cohomology sheaves of `M` on the locally free locus,
> on which `H^n(Lj^*Q)` is free of rank `ρ_n` near every point.
>
> This is `exists_isClopen_rankStratum_etaDerivedPullback`, whose inputs — finite local freeness
> and local boundedness of `H^n(Lj^*Q)`, finite local freeness of `H^n(M)` on `W`, and the rank
> comparison of tag 0F8X, part (3) — are proved in this file.

```lean
theorem exists_isClopen_rankStratum_etaDerivedPullback_of_isGoodOver {X' : Scheme.{u}}
    {b : X' ⟶ S.X} (hb : S.IsGoodOver b)
    {T : (S.pullback b hb.pullbackDefined).D.subscheme.IdealSheafData}
    (hT : ∀ C : AffineChart (S.pullback b hb.pullbackDefined),
      (∀ i : ℤ, (C.determinantalIdeal i).IsPrincipal) →
        T.ideal C.divisorAffineOpen = C.obstructionIdeal) (ρ : ℤ → ℕ) :
    ∃ Tρ : Set T.subscheme, IsClopen Tρ ∧
      (∀ (t : T.subscheme)
        (hw : ((T.subschemeι ≫ (S.pullback b hb.pullbackDefined).D.subschemeι) ≫ b) t ∈
          S.locallyFreeLocus),
        (⟨_, hw⟩ : S.locallyFreeLocus.toScheme) ∈
            Scheme.Modules.rankStratumSet S.locallyFreeLocusCohomologySheaf
              S.isFiniteLocallyFree_locallyFreeLocusCohomologySheaf ρ →
          t ∈ Tρ) ∧
      ∀ (n : ℤ) (t : T.subscheme), t ∈ Tρ →
        ∃ (V : T.subscheme.Opens) (_ : t ∈ V) (I : Type u), Nonempty (I ≃ Fin (ρ n)) ∧
          Nonempty (_root_.SheafOfModules.free.{u} I ≅
            (Scheme.Modules.toRingSheafModule
              (S.etaDerivedPullbackRestrictHomology b hb.pullbackDefined
                (T.subschemeι ≫ (S.pullback b hb.pullbackDefined).D.subschemeι) n)).over V)
```

## Tag 0GU0, a lemma

[Tag 0GU0](https://stacks.math.columbia.edu/tag/0GU0) in the Stacks Project.

**`Stacks.BlowUpComplexes.exists_isLocallyBoundedFiniteLocallyFree_etaDerivedPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodTripleLocallyFree.lean, line 781](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodTripleLocallyFree.lean#L781). The attribute's comment: “for every `b` along which `b⁻¹D` is defined and the pulled-back triple is good, in particular the morphism of Tag 0GTY (`goodBlowupToBase`); `Q` is stated directly as `Lη_{ℐ'}Lb^*M`”.

> **Stacks Project, Tag 0GU0.**  Let `(X, D, M)` be a triple as in Situation 0F8S and let
> `b : X' ⟶ X` be a morphism along which the pullback `D' = b⁻¹D` of the effective Cartier divisor
> is defined and makes the pulled-back triple `(X', D', Lb^*M)` good — the two conditions that
> Stacks tag 0GTY's morphism satisfies.  If `M` is represented by a locally bounded complex of
> finite locally free `𝒪_X`-modules, then `Q = Lη_{ℐ'}Lb^*M` is represented by a locally bounded
> complex of finite locally free `𝒪_{X'}`-modules.
>
> The pullback `b^*ℳ^•` of a representative of `M` is a locally bounded complex of finite locally
> free `𝒪_{X'}`-modules representing `Lb^*M`, so tag 0GTX applies to the pulled-back triple.

```lean
theorem exists_isLocallyBoundedFiniteLocallyFree_etaDerivedPullback
    (S : AlgebraicGeometry.ComplexAndDivisorSituation.{u, d}) {X' : Scheme.{u}} (b : X' ⟶ S.X)
    (hD : Stacks.Divisors.IsPullbackDefined b S.D)
    (hgood : AlgebraicGeometry.ComplexAndDivisorSituation.IsGoodTriple (S.pullback b hD))
    (hrep : ∃ ℳ : CochainComplex (OXMod.{u, u} S.X.toRingedSpace) ℤ,
      Stacks.Chow.IsLocallyBoundedFiniteLocallyFree ℳ ∧
        Nonempty ((@DerivedCategory.Q _ _ _ S.hasDerivedCategory).obj ℳ ≅ S.M)) :
    ∃ 𝒬 : CochainComplex X'.Modules ℤ,
      Stacks.Chow.IsLocallyBoundedFiniteLocallyFree 𝒬 ∧
        Nonempty (DerivedCategory.Q.obj 𝒬 ≅
          (Stacks.Divisors.Eta.derivedEtaData (S.D.comap b)).functor.obj
            (S.derivedPullbackObject b))
```

## Tag 0F9Y, a lemma

[Tag 0F9Y](https://stacks.math.columbia.edu/tag/0F9Y) in the Stacks Project.

**`AlgebraicGeometry.ComplexAndDivisorSituation.goodBlowupToBase_modification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodBlowupModification.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/GoodBlowupModification.lean#L106). The attribute's comment: “the full statement, with the morphism b of tag 0GTY (AlgebraicGeometry.ComplexAndDivisorSituation.goodBlowupToBase) as the witness and Q = Lη\_\{I'} Lb^* M: b proper and clauses (1)--(9), with T the closed subscheme of D' glued from the obstruction ideals J(N^•, g) of tag 0F81. Clause (9) is stated in its corrected form, Q represented by a LOCALLY BOUNDED complex of finite locally free modules (as tag 0GU0 gives): the printed 'bounded' is false for X = ⊔ₙ A¹, D the origins, M = O[n] on the n-th copy; see errata.md, entry 0F9Y (last sentence), 2026-10-27”.

> **Stacks tag 0F9Y.**  Let `(X, D, M)` be as in Situation 0F8S, `W ⊆ X` the maximal open over
> which the cohomology sheaves of `M` are locally free, `b : X' ⟶ X` the morphism of tag 0GTY,
> `D' = b⁻¹D` with ideal sheaf `ℐ'`, and `Q = Lη_{ℐ'}Lb^*M`.  Then `b` is proper and
>
> 1. `b` is an isomorphism over `X ∖ D`,
> 2. `b` is an isomorphism over `W`,
> 3. `D'` is an effective Cartier divisor,
> 4. `Q = Lη_{ℐ'}Lb^*M`,
> 5. `Q` is perfect,
> 6. there is a closed immersion `i : T ⟶ D'` of finite presentation with (a) `D' ∩ b⁻¹(W) ⊆ T`
>    scheme theoretically, (b) `H^n(Li^*Q)` finite locally free, and (c) for `t ∈ T` over
>    `x ∈ W`, `H^n(Li^*Q)_t` free of the rank of `H^n(M)_x`,
> 7. over an affine chart `(U, A, f, M^•)` of `(X, D, M)`, `b⁻¹U ⟶ U` is the blowing up of `U` in
>    `∏ᵢ I_i(M^•, f)`,
> 8. over an affine chart `(V, B, g, N^•)` of `(X', D', Lb^*M)` with every `I_i(N^•, g)`
>    principal, (a) `Q|_V` is the sheaf attached to `η_g N^•`, and (b) `T ∩ V ⊆ D' ∩ V` is cut
>    out by `J(N^•, g)`,
> 9. if `M` is represented by a locally bounded complex of finite locally free modules, so is `Q`.
>
> Clause (9) is printed with "bounded"; see the module docstring for why that is false and
> "locally bounded" is the correct form.

```lean
theorem goodBlowupToBase_modification :
    IsProper S.goodBlowupToBase ∧
    IsIso (S.goodBlowupToBase ∣_ S.divisorComplement) ∧
    IsIso (S.goodBlowupToBase ∣_ S.locallyFreeLocus) ∧
    Stacks.Divisors.IsPullbackDefined S.goodBlowupToBase S.D ∧
    S.etaDerivedPullbackObject S.goodBlowupToBase S.isPullbackDefined_goodBlowupToBase =
      (Stacks.Divisors.Eta.derivedEtaData (S.D.comap S.goodBlowupToBase)).functor.obj
          (S.derivedPullbackObject S.goodBlowupToBase) ∧
    RingedSpace.IsPerfect (X := S.goodBlowup.toRingedSpace)
      (S.etaDerivedPullbackObject S.goodBlowupToBase S.isPullbackDefined_goodBlowupToBase) ∧
    (∃ T : (S.D.comap S.goodBlowupToBase).subscheme.IdealSheafData,
      IsClosedImmersion T.subschemeι ∧ LocallyOfFinitePresentation T.subschemeι ∧
      T.comap ((S.D.comap S.goodBlowupToBase).subschemeι ⁻¹ᵁ
          (S.goodBlowupToBase ⁻¹ᵁ S.locallyFreeLocus)).ι = ⊥ ∧
      (∀ n : ℤ, AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u}
        (S.etaDerivedPullbackRestrictHomology S.goodBlowupToBase
          S.isPullbackDefined_goodBlowupToBase
          (T.subschemeι ≫ (S.D.comap S.goodBlowupToBase).subschemeι) n)) ∧
      (∀ (n : ℤ) (t : T.subscheme)
        (_ : ((T.subschemeι ≫ (S.D.comap S.goodBlowupToBase).subschemeι) ≫
          S.goodBlowupToBase).base t ∈ S.locallyFreeLocus),
        letI F := S.etaDerivedPullbackRestrictHomology S.goodBlowupToBase
          S.isPullbackDefined_goodBlowupToBase
          (T.subschemeι ≫ (S.D.comap S.goodBlowupToBase).subschemeι) n
        letI x := ((T.subschemeι ≫ (S.D.comap S.goodBlowupToBase).subschemeι) ≫
          S.goodBlowupToBase).base t
        letI : Module (ToType (TopCat.Presheaf.stalk T.subscheme.presheaf t))
            (ToType (TopCat.Presheaf.stalk F.val.presheaf t)) :=
          RingedSpace.moduleStalk (X := T.subscheme.toRingedSpace) F t
        letI : Module (ToType (S.X.presheaf.stalk x))
            (ToType (TopCat.Presheaf.stalk (S.cohomologySheaf n).val.presheaf x)) :=
          RingedSpace.moduleStalk (X := S.X.toRingedSpace) (S.cohomologySheaf n) x
        Module.Free (ToType (TopCat.Presheaf.stalk T.subscheme.presheaf t))
            (ToType (TopCat.Presheaf.stalk F.val.presheaf t)) ∧
          Module.finrank (ToType (TopCat.Presheaf.stalk T.subscheme.presheaf t))
              (ToType (TopCat.Presheaf.stalk F.val.presheaf t)) =
            Module.finrank (ToType (S.X.presheaf.stalk x))
              (ToType (TopCat.Presheaf.stalk (S.cohomologySheaf n).val.presheaf x))) ∧
      (∀ C : AffineChart (S.pullback S.goodBlowupToBase S.isPullbackDefined_goodBlowupToBase),
        (∀ i : ℤ, (C.determinantalIdeal i).IsPrincipal) →
          Nonempty ((RingedSpace.PseudoCoherence.restrictModules (S.pullback S.goodBlowupToBase
              S.isPullbackDefined_goodBlowupToBase).X.toRingedSpace C.U.1).mapDerivedCategory.obj
                (S.etaDerivedPullbackObject S.goodBlowupToBase
                  S.isPullbackDefined_goodBlowupToBase) ≅
            DerivedCategory.Q.obj C.specEtaComplex) ∧
          T.ideal C.divisorAffineOpen = C.obstructionIdeal)) ∧
    (∀ C : AffineChart S,
      ∃! e : (S.goodBlowupToBase ⁻¹ᵁ (C.U : S.X.Opens)).toScheme ≅
          AlgebraicGeometry.blowUp C.blowupCentreIdealSheaf,
        e.hom ≫ AlgebraicGeometry.blowUpToBase C.blowupCentreIdealSheaf =
          S.goodBlowupToBase ∣_ (C.U : S.X.Opens)) ∧
    ((∃ ℳ : CochainComplex (StrictlyPerfect.OXMod.{u, u} S.X.toRingedSpace) ℤ,
        Stacks.Chow.IsLocallyBoundedFiniteLocallyFree ℳ ∧
          Nonempty ((@DerivedCategory.Q _ _ _ S.hasDerivedCategory).obj ℳ ≅ S.M)) →
      ∃ 𝒬 : CochainComplex S.goodBlowup.Modules ℤ,
        Stacks.Chow.IsLocallyBoundedFiniteLocallyFree 𝒬 ∧
          Nonempty (DerivedCategory.Q.obj 𝒬 ≅
            S.etaDerivedPullbackObject S.goodBlowupToBase
              S.isPullbackDefined_goodBlowupToBase))
```

**`AlgebraicGeometry.ComplexAndDivisorSituation.exists_isProper_modification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/ModificationCollected.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/ModificationCollected.lean#L137). The attribute's comment: “the full statement in existential form: a proper b : X' ⟶ X and Q with clauses (1)--(9). Clause (9) is stated in its corrected form, Q represented by a LOCALLY BOUNDED complex of finite locally free modules (as tag 0GU0 gives): the printed 'bounded' is false for an infinite disjoint union; see errata.md, entry 0F9Y (last sentence), 2026-10-27”.

> **Stacks tag 0F9Y.**  Let `X` be a scheme, `D ⊆ X` an effective Cartier divisor and `M` a
> perfect object of `D(𝒪_X)`, and let `W ⊆ X` be the maximal open over which the cohomology
> sheaves of `M` are locally free.  There are a proper morphism `b : X' ⟶ X` and an object `Q` of
> `D(𝒪_{X'})` such that
>
> 1. `b` is an isomorphism over `X ∖ D`;
> 2. `b` is an isomorphism over `W`;
> 3. `D' = b⁻¹D` is an effective Cartier divisor;
> 4. `Q = Lη_{ℐ'}Lb^*M`, with `ℐ'` the ideal sheaf of `D'`;
> 5. `Q` is perfect;
> 6. there is a closed immersion `i : T ⟶ D'` of finite presentation with `D' ∩ b⁻¹(W) ⊆ T`
>    scheme-theoretically, such that the cohomology sheaves of `Li^*Q` are finite locally free,
>    and at a point `t ∈ T` over `W` the rank of `H^n(Li^*Q)` is the rank of `H^n(M)` at the image
>    of `t`;
> 7. for every affine chart `(U, A, f, M^•)` of `(X, D, M)`, the part of `b` over `U` is the
>    blowing up of `U` in `∏ᵢ I_i(M^•, f)`;
> 8. for every affine chart `(V, B, g, N^•)` of `(X', D', Lb^*M)` with principal `I_i(N^•, g)`,
>    `Q|_V` is isomorphic to the complex associated with `η_g N^•`, and `T ∩ V` is cut out in
>    `D' ∩ V` by `J(N^•, g) = ∑ᵢ J_i(N^•, g)`;
> 9. if `M` is represented by a locally bounded complex of finite locally free `𝒪_X`-modules, then
>    `Q` is represented by a locally bounded complex of finite locally free `𝒪_{X'}`-modules.
>
> Here `b` is `goodBlowupToBase` (tag 0GTY), properness is `isProper_goodBlowupToBase`, clause (1)
> is `IsGoodBlowup.isIso_resLE_divisorComplement`, clause (2) is tag 0F8W, clause (5) is tag 0F8U,
> clause (6) is tag 0F8X with the subscheme of tag 0GTZ for the pulled-back triple, clause (7) is
> `exists_isPullback_blowUpToBase`, clause (8) is the second assertion of tag 0GTV for the
> pulled-back triple together with the defining property of that subscheme, and clause (9) is tag
> 0GU0.  Clause (9) asks for a locally bounded rather than a bounded complex; see the module
> docstring.

```lean
theorem exists_isProper_modification (S : ComplexAndDivisorSituation.{u, d}) :
    ∃ (X' : Scheme.{u}) (b : X' ⟶ S.X), IsProper b ∧
      IsIso (b.resLE S.divisorComplement (b ⁻¹ᵁ S.divisorComplement) le_rfl) ∧
      IsIso (b.resLE S.locallyFreeLocus (b ⁻¹ᵁ S.locallyFreeLocus) le_rfl) ∧
      ∃ (hD' : Stacks.Divisors.IsEffectiveCartierDivisor (S.D.comap b))
        (Q : DerivedCategory X'.Modules),
        Q = S.etaDerivedPullbackObject b hD' ∧
        RingedSpace.IsPerfect (X := X'.toRingedSpace) Q ∧
        (∃ T : (S.pullback b hD').D.subscheme.IdealSheafData,
          LocallyOfFinitePresentation T.subschemeι ∧
          T.comap ((S.pullback b hD').D.subschemeι ⁻¹ᵁ (b ⁻¹ᵁ S.locallyFreeLocus)).ι = ⊥ ∧
          (∀ n : ℤ, AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u}
            ((DerivedCategory.homologyFunctor T.subscheme.Modules n).obj
              ((derivedPullback
                (T.subschemeι ≫ (S.pullback b hD').D.subschemeι).toLRSHom.toShHom).obj Q))) ∧
          (∀ (n : ℤ) (t : T.subscheme),
            ((T.subschemeι ≫ (S.pullback b hD').D.subschemeι) ≫ b) t ∈ S.locallyFreeLocus →
            Scheme.Modules.fiberRank
                ((DerivedCategory.homologyFunctor T.subscheme.Modules n).obj
                  ((derivedPullback
                    (T.subschemeι ≫ (S.pullback b hD').D.subschemeι).toLRSHom.toShHom).obj Q))
                t =
              Scheme.Modules.fiberRank (S.cohomologySheaf n)
                (((T.subschemeι ≫ (S.pullback b hD').D.subschemeι) ≫ b) t)) ∧
          ∀ C : AffineChart (S.pullback b hD'), (∀ i : ℤ, (C.determinantalIdeal i).IsPrincipal) →
            T.ideal C.divisorAffineOpen = C.obstructionIdeal) ∧
        (∀ C : AffineChart S, ∃ e : blowUp C.blowupCentreIdealSheaf ⟶ X',
          IsPullback e (blowUpToBase C.blowupCentreIdealSheaf) b (C.U : S.X.Opens).ι) ∧
        (∀ C : AffineChart (S.pullback b hD'), (∀ i : ℤ, (C.determinantalIdeal i).IsPrincipal) →
          Nonempty ((RingedSpace.PseudoCoherence.restrictModules (S.pullback b hD').X.toRingedSpace
              C.U.1).mapDerivedCategory.obj Q ≅ DerivedCategory.Q.obj C.specEtaComplex)) ∧
        ((∃ ℳ : CochainComplex (OXMod.{u, u} S.X.toRingedSpace) ℤ,
            Stacks.Chow.IsLocallyBoundedFiniteLocallyFree ℳ ∧
              Nonempty ((@DerivedCategory.Q _ _ _ S.hasDerivedCategory).obj ℳ ≅ S.M)) →
          ∃ 𝒬 : CochainComplex X'.Modules ℤ,
            Stacks.Chow.IsLocallyBoundedFiniteLocallyFree 𝒬 ∧
              Nonempty (DerivedCategory.Q.obj 𝒬 ≅ Q))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.43, Tag 0F8R](https://stacks.math.columbia.edu/tag/0F8R)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
