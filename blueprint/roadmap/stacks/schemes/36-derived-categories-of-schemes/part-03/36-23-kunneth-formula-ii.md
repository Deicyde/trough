---
declaration: section
origin: cited
lean: Stacks.Cohomology.DerivedKunneth.kunnethMap, Stacks.Cohomology.DerivedKunneth.kunnethMap_natural_left, Stacks.Cohomology.DerivedKunneth.kunnethMap_natural_right, Stacks.Cohomology.GlobalKunneth.kunnethGlobalMapCanonical, Stacks.Cohomology.GlobalKunneth.kunnethGlobalMapCanonical_naturality, Stacks.Cohomology.GlobalKunneth.kunnethGlobalMapSchemeCanonical, Stacks.Cohomology.GlobalKunneth.kunnethGlobalMapSchemeCanonical_naturality, Stacks.Cohomology.DerivedKunneth.isIso_kunnethMapScheme
statement: formalized
proof: formalized
---

# 36.23 Künneth formula, II

Section 36.23 of the Stacks Project, [Tag 0FLN](https://stacks.math.columbia.edu/tag/0FLN). 8 tags here are carried by 26 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FLP, an equation

[Tag 0FLP](https://stacks.math.columbia.edu/tag/0FLP) in the Stacks Project.

**`Stacks.Cohomology.DerivedKunneth.kunnethMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/KunnethMap.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/KunnethMap.lean#L199).

> **The relative Künneth morphism**
> `Ra_*K ⊗^L_{𝒪_S} Rb_*M ⟶ Rf_*(Lp^*K ⊗^L_{𝒪_W} Lq^*M)`, Equation 36.23.0.1: the adjoint
> transpose of the monoidality isomorphism of Stacks 079U for `Lf^*` followed by the tensor
> product of the two counit legs.  It is defined for arbitrary `K ∈ D(𝒪_X)` and `M ∈ D(𝒪_Y)`.

```lean
def kunnethMap
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (M : DerivedCategory (SheafOfModules.{u} (structureSheafRing Y))) :
    ((Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor S.sheaf).obj
          ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward a).obj K)).obj
        ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward b).obj M) ⟶
      (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f).obj
        (((Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor W.sheaf).obj
            ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback p).obj K)).obj
          ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback q).obj M))
```

**`Stacks.Cohomology.DerivedKunneth.kunnethMap_natural_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/KunnethMap.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/KunnethMap.lean#L237). The attribute's comment: “naturality in the complex on the first factor”.

> The relative Künneth morphism is natural in the derived module on `X`.

```lean
theorem kunnethMap_natural_left
    {K K' : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))}
    (k : K ⟶ K')
    (M : DerivedCategory (SheafOfModules.{u} (structureSheafRing Y))) :
    ((Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor S.sheaf).map
          ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward a).map k)).app
        ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward b).obj M) ≫
        kunnethMap a b p q f hp hq K' M =
      kunnethMap a b p q f hp hq K M ≫
        (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f).map
          (((Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor W.sheaf).map
              ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback p).map k)).app
            ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback q).obj M))
```

**`Stacks.Cohomology.DerivedKunneth.kunnethMap_natural_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/KunnethMap.lean, line 259](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/KunnethMap.lean#L259). The attribute's comment: “naturality in the complex on the second factor”.

> The relative Künneth morphism is natural in the derived module on `Y`.

```lean
theorem kunnethMap_natural_right
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    {M M' : DerivedCategory (SheafOfModules.{u} (structureSheafRing Y))}
    (m : M ⟶ M') :
    ((Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor S.sheaf).obj
          ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward a).obj K)).map
        ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward b).map m) ≫
        kunnethMap a b p q f hp hq K M' =
      kunnethMap a b p q f hp hq K M ≫
        (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f).map
          (((Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor W.sheaf).obj
              ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback p).obj K)).map
            ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback q).map m))
```

## Tag 0G7V, an equation

[Tag 0G7V](https://stacks.math.columbia.edu/tag/0G7V) in the Stacks Project.

**`Stacks.Cohomology.GlobalKunneth.kunnethGlobalMapCanonical`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalKunnethMapCanonical.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalKunnethMapCanonical.lean#L154). The attribute's comment: “the map, for arbitrary K ∈ D(𝒪\_X) and M ∈ D(𝒪\_Y) over an arbitrary base”.

> **The global Künneth map of Tag 0G7V, with no parameter.**
>
> `RΓ(X, K) ⊗^𝐋_A RΓ(Y, M) ⟶ RΓ(W, Lp^*K ⊗^𝐋_{𝒪_W} Lq^*M)`
>
> in `D(A)` for `A = Γ(S, 𝒪_S)`, where `p ≫ a = f = q ≫ b`; the source takes `W = X ×_S Y` with its
> two projections.  It is defined for arbitrary `K ∈ D(𝒪_X)` and `M ∈ D(𝒪_Y)`, over an arbitrary
> base, and it is built from the canonical global cup product of Section 0FKU on the base together
> with the relative Künneth map of Tag 0FLP and the Leray isomorphism of Tag 0D5W.

```lean
def kunnethGlobalMapCanonical (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (M : DerivedCategory (SheafOfModules.{u} (structureSheafRing Y))) :
    ((tensorBase S).obj ((sectionsOverBase a).obj K)).obj ((sectionsOverBase b).obj M) ⟶
      (sectionsOverBase f).obj
        (((derivedTensorProductFunctor W.sheaf).obj ((derivedPullback p).obj K)).obj
          ((derivedPullback q).obj M))
```

**`Stacks.Cohomology.GlobalKunneth.kunnethGlobalMapCanonical_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalKunnethMapCanonical.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalKunnethMapCanonical.lean#L173). The attribute's comment: “naturality in both complexes, with no parameter”.

> **The global Künneth map with no parameter is natural in both complexes jointly.**

```lean
theorem kunnethGlobalMapCanonical_naturality
    {K K' : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))}
    {M M' : DerivedCategory (SheafOfModules.{u} (structureSheafRing Y))} (k : K ⟶ K') (m : M ⟶ M') :
    (Functor.uncurry.obj (tensorBase S)).map
          ((sectionsOverBase a).map k ×ₘ (sectionsOverBase b).map m) ≫
        kunnethGlobalMapCanonical a b p q f hp hq K' M' =
      kunnethGlobalMapCanonical a b p q f hp hq K M ≫
        (sectionsOverBase f).map
          ((Functor.uncurry.obj (derivedTensorProductFunctor W.sheaf)).map
            ((derivedPullback p).map k ×ₘ (derivedPullback q).map m))
```

**`Stacks.Cohomology.GlobalKunneth.kunnethGlobalMapSchemeCanonical`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalKunnethMapCanonical.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalKunnethMapCanonical.lean#L205). The attribute's comment: “the map at X ×\_S Y, for arbitrary K and M over an arbitrary base scheme”.

> **The global Künneth map of Tag 0G7V at the fibre product of two schemes, with no
> parameter.**  For schemes `a : X ⟶ S` and `b : Y ⟶ S` over a base and `A = Γ(S, 𝒪_S)`, the
> canonical map
>
> `RΓ(X, K) ⊗^𝐋_A RΓ(Y, M) ⟶ RΓ(X ×_S Y, Lp^*K ⊗^𝐋_{𝒪_{X ×_S Y}} Lq^*M)`
>
> in `D(A)`, where `p` and `q` are the two projections of `X ×_S Y`.  The base scheme is arbitrary
> and `K`, `M` are arbitrary; quasi-compactness, quasi-separatedness, quasi-coherence and
> Tor-independence enter only in Tag 0FLQ, which asserts that this map is an isomorphism.

```lean
def kunnethGlobalMapSchemeCanonical (K : DerivedCategory X.Modules)
    (M : DerivedCategory Y.Modules) :
    ((tensorBase S.toRingedSpace).obj ((sectionsOverBase a.toLRSHom.toShHom).obj K)).obj
        ((sectionsOverBase b.toLRSHom.toShHom).obj M) ⟶
      (sectionsOverBase (pullback.fst a b ≫ a).toLRSHom.toShHom).obj
        (((derivedTensorProductFunctor (pullback a b).toRingedSpace.sheaf).obj
            ((derivedPullback (pullback.fst a b).toLRSHom.toShHom).obj K)).obj
          ((derivedPullback (pullback.snd a b).toLRSHom.toShHom).obj M))
```

**`Stacks.Cohomology.GlobalKunneth.kunnethGlobalMapSchemeCanonical_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalKunnethMapCanonical.lean, line 226](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalKunnethMapCanonical.lean#L226). The attribute's comment: “naturality at the fibre product of two schemes, with no parameter”.

> **The global Künneth map at the fibre product of two schemes, with no parameter, is natural in
> both complexes.**

```lean
theorem kunnethGlobalMapSchemeCanonical_naturality {K K' : DerivedCategory X.Modules}
    {M M' : DerivedCategory Y.Modules} (k : K ⟶ K') (m : M ⟶ M') :
    (Functor.uncurry.obj (tensorBase S.toRingedSpace)).map
          ((sectionsOverBase a.toLRSHom.toShHom).map k ×ₘ
            (sectionsOverBase b.toLRSHom.toShHom).map m) ≫
        kunnethGlobalMapSchemeCanonical a b K' M' =
      kunnethGlobalMapSchemeCanonical a b K M ≫
        (sectionsOverBase (pullback.fst a b ≫ a).toLRSHom.toShHom).map
          ((Functor.uncurry.obj
              (derivedTensorProductFunctor (pullback a b).toRingedSpace.sheaf)).map
            ((derivedPullback (pullback.fst a b).toLRSHom.toShHom).map k ×ₘ
              (derivedPullback (pullback.snd a b).toLRSHom.toShHom).map m))
```

## Tag 0FLQ, a lemma

[Tag 0FLQ](https://stacks.math.columbia.edu/tag/0FLQ) in the Stacks Project.

**`Stacks.Cohomology.DerivedKunneth.isIso_kunnethMapScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/KunnethDischarged.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/KunnethDischarged.lean#L88). The attribute's comment: “first statement: for qcqs a and b with X and Y Tor independent over S, the relative Künneth map (0FLP) at X ×\_S Y is an isomorphism for K ∈ D\_QCoh(𝒪\_X) and M ∈ D\_QCoh(𝒪\_Y)”.

> **[Stacks, Tag 0FLQ], the relative conclusion, with no hypothesis beyond the tag's own.**
> Let `a : X ⟶ S` and `b : Y ⟶ S` be quasi-compact and quasi-separated morphisms of schemes with
> `X` and `Y` Tor independent over `S`, let `W = X ×_S Y` with projections `p` and `q`, and let
> `K ∈ D_QCoh(𝒪_X)` and `M ∈ D_QCoh(𝒪_Y)`.  Then the relative Künneth morphism of
> [Stacks, Tag 0FLP]
>
> `Ra_*K ⊗^𝐋_{𝒪_S} Rb_*M ⟶ R(p ≫ a)_*(Lp^*K ⊗^𝐋_{𝒪_W} Lq^*M)`
>
> is an isomorphism.
>
> This is `isIso_kunnethMap_pullback_of_torIndependent_of_baseChange` with its one remaining
> carried proposition discharged against the proved [Stacks, Tag 08IB].  All three comparisons the
> source's proof chains together are now proved in this library: `hproj₁` and `hproj₂` from
> [Stacks, Tag 08EU], with the interchanged-order conjugation supplied by the proved braiding
> compatibility of [Stacks, Tag 079U], and `hbase` from [Stacks, Tag 08IB].

```lean
theorem isIso_kunnethMapScheme
    [QuasiCompact a] [QuasiSeparated a] [QuasiCompact b] [QuasiSeparated b]
    (hTor : TorIndependent a b)
    (K : DerivedCategory X.Modules) (M : DerivedCategory Y.Modules)
    (hK : IsQCohAll K) (hM : IsQCohAll M) :
    IsIso (kunnethMap a.toLRSHom.toShHom b.toLRSHom.toShHom
      (pullback.fst a b).toLRSHom.toShHom (pullback.snd a b).toLRSHom.toShHom
      (pullback.fst a b ≫ a).toLRSHom.toShHom rfl
      (Stacks.Cohomology.GlobalKunneth.toShHom_pullback_condition a b) K M)
```

**`Stacks.Cohomology.DerivedKunneth.isIso_kunnethMapScheme_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/KunnethDischarged.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/KunnethDischarged.lean#L126). The attribute's comment: “the relative conclusion, at an arbitrary cartesian square of schemes”.

> **[Stacks, Tag 0FLQ], the relative conclusion, at an arbitrary cartesian square of
> schemes.**  Let `a : X ⟶ S` and `b : Y ⟶ S` be quasi-compact and quasi-separated morphisms of
> schemes with `X` and `Y` Tor independent over `S`, let `p : W ⟶ X` and `q : W ⟶ Y` make `W` a
> fibre product of `a` and `b`, and let `K ∈ D_QCoh(𝒪_X)` and `M ∈ D_QCoh(𝒪_Y)`.  Then the
> relative Künneth morphism of [Stacks, Tag 0FLP]
>
> `Ra_*K ⊗^𝐋_{𝒪_S} Rb_*M ⟶ R(p ≫ a)_*(Lp^*K ⊗^𝐋_{𝒪_W} Lq^*M)`
>
> is an isomorphism.
>
> The three comparisons of
> `Stacks.Cohomology.DerivedKunneth.isIso_kunnethMap_of_projectionFormulas_of_baseChange` are
> proved at the given square: the projection formula at `a` by [Stacks, Tag 08EU], the base change
> leg by [Stacks, Tag 08IB] at the flipped square, and the interchanged-order projection formula at
> `p` by [Stacks, Tag 08EU] at `p` (quasi-compact and quasi-separated as a base change of `b`)
> conjugated by the symmetries of the derived tensor product.

```lean
theorem isIso_kunnethMapScheme_of_isPullback {W : Scheme.{u}} (p : W ⟶ X) (q : W ⟶ Y)
    (hW : IsPullback p q a b)
    [QuasiCompact a] [QuasiSeparated a] [QuasiCompact b] [QuasiSeparated b]
    (hTor : TorIndependent a b)
    (K : DerivedCategory X.Modules) (M : DerivedCategory Y.Modules)
    (hK : IsQCohAll K) (hM : IsQCohAll M) :
    IsIso (kunnethMap a.toLRSHom.toShHom b.toLRSHom.toShHom
      p.toLRSHom.toShHom q.toLRSHom.toShHom (p ≫ a).toLRSHom.toShHom rfl
      (congrArg (fun g : W ⟶ S => g.toLRSHom.toShHom) hW.w.symm) K M)
```

**`Stacks.Cohomology.DerivedKunneth.isIso_kunnethGlobalMapScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/KunnethGlobalCupProduct.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/TorIndependence/KunnethGlobalCupProduct.lean#L130). The attribute's comment: “second statement: under the same hypotheses with S affine, the global Künneth map (0G7V) RΓ(X, K) ⊗^L\_A RΓ(Y, M) → RΓ(X ×\_S Y, Lp^*K ⊗^L Lq^*M), built from the cup product of Section 0FKU, is an isomorphism”.

> **[Stacks, Tag 0FLQ], the global conclusion over an affine base, with no hypothesis beyond
> the tag's own.**
>
> Let `a : X ⟶ S` and `b : Y ⟶ S` be quasi-compact and quasi-separated morphisms of schemes with
> `S` affine and `X` and `Y` Tor independent over `S`, let `W = X ×_S Y` with projections `p` and
> `q`, and let `K ∈ D_QCoh(𝒪_X)` and `M ∈ D_QCoh(𝒪_Y)`.  Then the global Künneth morphism of
> [Stacks, Tag 0G7V]
>
> `RΓ(X, K) ⊗^𝐋_A RΓ(Y, M) ⟶ RΓ(W, Lp^*K ⊗^𝐋_{𝒪_W} Lq^*M)`
>
> for the global cup product of Cohomology, Section 0FKU is an isomorphism.
>
> The cup product is the canonical one, not a parameter: it is
> `Stacks.Cohomology.DerivedGlobalCupProduct.globalCupProduct` of the one-point comparison
> `Stacks.Cohomology.DerivedSectionsLeftAdjoint.onePointComparisonOnARingedSpace`, which is the
> relative cup product of [Stacks, Tag 0B68] for the structure morphism `π : S ⟶ ({*}, A)` of
> [Stacks, Tag 01BH] read through the identification of modules on the point with `A`-modules,
> exactly as the source defines `μ`.
>
> The three inputs of `isIso_kunnethGlobalMapScheme_of_onePointComparison` are discharged: the
> tensor comparison of that one-point comparison is invertible because it is the `hom` of an
> isomorphism of bifunctors, and affineness of the base supplies the invertibility of the unit and
> of the counit on the quasi-coherent part, which is the Spec–Γ equivalence of
> [Stacks, Tag 06Z0].

```lean
theorem isIso_kunnethGlobalMapScheme
    [IsAffine S] [QuasiCompact a] [QuasiSeparated a] [QuasiCompact b] [QuasiSeparated b]
    (hTor : TorIndependent a b)
    (K : DerivedCategory X.Modules) (M : DerivedCategory Y.Modules)
    (hK : IsQCohAll K) (hM : IsQCohAll M) :
    IsIso (Stacks.Cohomology.GlobalKunneth.kunnethGlobalMapScheme a b
      (globalCupProduct
        (Stacks.Cohomology.DerivedSectionsLeftAdjoint.onePointComparisonOnARingedSpace
          S.toRingedSpace)) K M)
```

## Tag 0FML, a lemma

[Tag 0FML](https://stacks.math.columbia.edu/tag/0FML) in the Stacks Project.

**`Stacks.RelativeComplexPushforward.isIso_projectionFormulaMap_relativeComplex_of_isLocallyBounded_of_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativeComplexProjectionFormula.lean, line 880](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/RelativeComplexProjectionFormula.lean#L880). The attribute's comment: “conclusion (5), with no hypothesis beyond the tag's own: for a quasi-compact quasi-separated morphism of schemes a : X ⟶ S, a LOCALLY BOUNDED complex F^• of a^\{-1}O\_S-modules each of whose terms carries a compatible quasi-coherent O\_X-module structure, and K in D\_QCoh(O\_S), the Tag 0B53 map Ra\_*F^• ⊗ᴸ\_\{O\_S} K ⟶ Ra\_*(F^• ⊗ᴸ\_\{a^\{-1}O\_S} L(a')^*K) is invertible. One difference from the source's phrasing, not a weakening: flatness of the terms, which the source assumes, is not needed for this conclusion and is not assumed. The two tensor factors are in the order the Tag 0B53 map produces them, which is the opposite of the source's”.

> **Stacks Project, Tag 0FML, conclusion (5)**, with no hypothesis beyond the tag's own.  For
> `f : X ⟶ S` quasi-compact and quasi-separated, `K` an object of `D_QCoh(𝒪_S)` and `F` a *locally
> bounded* complex of `f^{-1}𝒪_S`-modules, the term in degree `i` being the restriction of scalars
> of a quasi-coherent `𝒪_X`-module `M i`, the projection-formula morphism of [Stacks, Tag 0B53] at
> `(X, f^{-1}𝒪_S) ⟶ (S, 𝒪_S)` is an isomorphism.
>
> `isIso_projectionFormulaMap_relativeComplex_of_isLocallyBounded` above with its hypothesis
> discharged by `isIso_projectionFormulaMap_single_relativeBase`.

```lean
theorem isIso_projectionFormulaMap_relativeComplex_of_isLocallyBounded_of_isQuasicoherent
    [QuasiCompact f] [QuasiSeparated f] (K : DerivedCategory (Modules S.toRingedSpace))
    (hK : DerivedCategoryB.derivedCategoryB
      (_root_.SheafOfModules.isQuasicoherent S.ringCatSheaf) K)
    (F : CochainComplex (Modules (inverseImageBase f)) ℤ)
    (hF : Stacks.SheafOfModules.OnSpace.IsLocallyBounded (inverseImageBase f) F)
    (M : ℤ → X.Modules) (hM : ∀ i, (M i).IsQuasicoherent)
    (hFM : ∀ i, F.X i ≅ (pushforward (toInverseImageBase f)).obj (M i)) :
    IsIso (projectionFormulaMap (inverseImageBaseProjection f)
      (DerivedCategory.Q.obj F) K)
```

**`Stacks.RelativeComplexPushforward.relativeComplexProjectionFormulaIsoOfIsLocallyBoundedOfIsQuasicoherent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativeComplexProjectionFormula.lean, line 904](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/RelativeComplexProjectionFormula.lean#L904). The attribute's comment: “conclusion (5) read as an isomorphism, with no hypothesis beyond the tag's own: Ra\_*F^• ⊗ᴸ\_\{O\_S} K is Ra\_*(F^• ⊗ᴸ\_\{a^\{-1}O\_S} a^\{-1}K) for K in D\_QCoh(O\_S) and F^• LOCALLY BOUNDED. The same single difference from the source's phrasing as in the invertibility form, not a weakening: flatness of the terms is not needed for this conclusion and is not assumed”.

> **Stacks Project, Tag 0FML, conclusion (5)** read as an isomorphism and with no hypothesis
> beyond the tag's own,
>
> `Rf_*F^• ⊗^𝐋_{𝒪_S} K ≅ Rf_*(F^• ⊗^𝐋_{f^{-1}𝒪_S} f^{-1}K)`
>
> for `K` in `D_QCoh(𝒪_S)` and `F` locally bounded, the two tensor products being written in the
> order the morphism of [Stacks, Tag 0B53] produces them.

```lean
def relativeComplexProjectionFormulaIsoOfIsLocallyBoundedOfIsQuasicoherent [QuasiCompact f]
    [QuasiSeparated f] (K : DerivedCategory (Modules S.toRingedSpace))
    (hK : DerivedCategoryB.derivedCategoryB
      (_root_.SheafOfModules.isQuasicoherent S.ringCatSheaf) K)
    (F : CochainComplex (Modules (inverseImageBase f)) ℤ)
    (hF : Stacks.SheafOfModules.OnSpace.IsLocallyBounded (inverseImageBase f) F)
    (M : ℤ → X.Modules) (hM : ∀ i, (M i).IsQuasicoherent)
    (hFM : ∀ i, F.X i ≅ (pushforward (toInverseImageBase f)).obj (M i)) :
    ((derivedTensorProductFunctor S.toRingedSpace.sheaf).obj
        ((derivedPushforward (inverseImageBaseProjection f)).obj
          (DerivedCategory.Q.obj F))).obj K ≅
      (derivedPushforward (inverseImageBaseProjection f)).obj
        (((derivedTensorProductFunctor (inverseImageBase f).sheaf).obj
            (DerivedCategory.Q.obj F)).obj
          ((derivedPullback (inverseImageBaseProjection f)).obj K))
```

**`Stacks.RelativeComplexPushforward.relativeComplexOrdinaryProjectionFormulaIsoOfIsLocallyBoundedOfIsQuasicoherent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativeComplexProjectionFormula.lean, line 1108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/RelativeComplexProjectionFormula.lean#L1108). The attribute's comment: “conclusion (4), with no hypothesis beyond the tag's own: for a quasi-compact quasi-separated morphism of schemes a : X ⟶ S, a LOCALLY BOUNDED complex F^• of a^\{-1}O\_S-modules each of whose terms is flat over a^\{-1}O\_S and carries a compatible quasi-coherent O\_X-module structure, and an ORDINARY quasi-coherent O\_S-module G, Ra\_*F^• ⊗ᴸ\_\{O\_S} G is Ra\_*(F^• ⊗\_\{a^\{-1}O\_S} a^\{-1}G) with the ORDINARY tensor product on the right. The two tensor factors are in the order the Tag 0B53 map produces them, which is the opposite of the source's”.

> **Stacks Project, Tag 0FML, conclusion (4)**, with no hypothesis beyond the tag's own.  For
> `f : X ⟶ S` quasi-compact and quasi-separated, `G` a *quasi-coherent* `𝒪_S`-module and `F` a
> *locally bounded* complex of `f^{-1}𝒪_S`-modules, each term flat over `f^{-1}𝒪_S` and the
> restriction of scalars of a quasi-coherent `𝒪_X`-module,
>
> `Rf_*F^• ⊗^𝐋_{𝒪_S} G ≅ Rf_*(F^• ⊗_{f^{-1}𝒪_S} f^{-1}G)`,
>
> the tensor product on the right being the *ordinary* one.
>
> `relativeComplexOrdinaryProjectionFormulaIsoOfIsLocallyBounded` above with its hypothesis
> discharged by `isIso_projectionFormulaMap_single_relativeBase` at `K = G[0]`, which lies in
> `D_QCoh(𝒪_S)` by `derivedCategoryB_isQuasicoherent_single`.

```lean
def relativeComplexOrdinaryProjectionFormulaIsoOfIsLocallyBoundedOfIsQuasicoherent
    [QuasiCompact f] [QuasiSeparated f] (G : Modules S.toRingedSpace) (hG : G.IsQuasicoherent)
    (F : CochainComplex (Modules (inverseImageBase f)) ℤ)
    (hF : Stacks.SheafOfModules.OnSpace.IsLocallyBounded (inverseImageBase f) F)
    (hflat : ∀ i : ℤ, AlgebraicGeometry.SheafOfModules.IsFlat.{u, u, u, u}
      (O := (inverseImageBase f).sheaf) (F.X i))
    (M : ℤ → X.Modules) (hM : ∀ i, (M i).IsQuasicoherent)
    (hFM : ∀ i, F.X i ≅ (pushforward (toInverseImageBase f)).obj (M i)) :
    ((derivedTensorProductFunctor S.toRingedSpace.sheaf).obj
        ((derivedPushforward (inverseImageBaseProjection f)).obj
          (DerivedCategory.Q.obj F))).obj
      ((DerivedCategory.singleFunctor (Modules S.toRingedSpace) 0).obj G) ≅
      (derivedPushforward (inverseImageBaseProjection f)).obj
        (DerivedCategory.Q.obj
          (((Stacks.SheafOfModules.Tensor.tensorComplex (inverseImageBase f).sheaf).obj F).obj
            ((CochainComplex.singleFunctor (Modules (inverseImageBase f)) 0).obj
              ((RingedSpaceModuleAdjunction.modulePullback
                (inverseImageBaseProjection f)).obj G))))
```

**`Stacks.RelativeComplexPushforward.relativeDerivedPushforward_locallyBounded_qcoh_torDimension_projectionFormula`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativeComplexPushforwardLocal.lean, line 595](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/RelativeComplexPushforwardLocal.lean#L595). The attribute's comment: “all five conclusions, under exactly the source's hypotheses: a : X ⟶ S quasi-compact and quasi-separated, F^• a LOCALLY BOUNDED complex of a^\{-1}O\_S-modules with flat terms each carrying a compatible quasi-coherent O\_X-module structure (differentials not O\_X-linear); Ra\_* is the unbounded derived pushforward along (X, a^\{-1}O\_S) ⟶ (S, O\_S). (1) every point of S has an open neighbourhood U with (Ra\_*F^•)|\_U cohomologically bounded; (2) Ra\_*F^• in D\_QCoh(O\_S); (3) LocallyHasFiniteTorDimension at the derived tensor product of Tag 06YU; (4) an isomorphism Ra\_*F^• ⊗ᴸ G ≅ Ra\_*(F^• ⊗ a^\{-1}G) for G quasi-coherent; (5) invertibility of the Tag 0B53 map for K in D\_QCoh(O\_S). Tensor factors in (4), (5) are in the order the Tag 0B53 map produces them, the opposite of the source's”.

> **Stacks Project, Tag 0FML.** Let `a : X ⟶ S` be a quasi-compact and quasi-separated
> morphism of schemes and `F^•` a locally bounded complex of `a⁻¹𝒪_S`-modules, each term `F^n` a
> flat `a⁻¹𝒪_S`-module carrying the structure of a quasi-coherent `𝒪_X`-module `M n` compatible
> with its `a⁻¹𝒪_S`-module structure (`F^n ≅ b_*(M n)` for `b : (X, 𝒪_X) ⟶ (X, a⁻¹𝒪_S)`; the
> differentials of `F^•` need not be `𝒪_X`-linear). Write `Ra_*F^•` for the derived pushforward
> along the morphism of ringed spaces `(X, a⁻¹𝒪_S) ⟶ (S, 𝒪_S)`. Then
>
> 1. `Ra_*F^•` is locally bounded: every point of `S` has an open neighbourhood `U` on which
>    `(Ra_*F^•)|_U` has only finitely many nonzero cohomology sheaves;
> 2. `Ra_*F^•` lies in `D_QCoh(𝒪_S)`;
> 3. `Ra_*F^•` locally has finite Tor dimension;
> 4. `Ra_*F^• ⊗^𝐋_{𝒪_S} 𝒢 ≅ Ra_*(F^• ⊗_{a⁻¹𝒪_S} a⁻¹𝒢)` for every quasi-coherent `𝒢`;
> 5. the map of [Stacks, Tag 0B53] `Ra_*F^• ⊗^𝐋_{𝒪_S} K ⟶ Ra_*(F^• ⊗^𝐋_{a⁻¹𝒪_S} a⁻¹K)` is an
>    isomorphism for every `K` in `D_QCoh(𝒪_S)`.
>
> The tensor products in (4) and (5) are written in the order the map of [Stacks, Tag 0B53]
> produces them, the opposite of the source's; the two orders agree by symmetry. Conclusions (4)
> and (5) are `relativeComplexOrdinaryProjectionFormulaIsoOfIsLocallyBoundedOfIsQuasicoherent` and
> `isIso_projectionFormulaMap_relativeComplex_of_isLocallyBounded_of_isQuasicoherent`.
> Conclusions (1)–(3) are local on `S`; over an affine open `V` the complex is bounded on the
> quasi-compact `a⁻¹V`, and `prop_restrict_derivedPushforward_relativeComplex` reduces each of
> them to a single quasi-coherent `M n`, where (1) is [Stacks, Tag 01XJ], (2) is the
> quasi-coherence of the higher direct images and (3) is the Mayer–Vietoris bound on Tor amplitude
> of a derived direct image of a module flat over the base.

```lean
theorem relativeDerivedPushforward_locallyBounded_qcoh_torDimension_projectionFormula
    [QuasiCompact f] [QuasiSeparated f]
    (F : CochainComplex (Modules (inverseImageBase f)) ℤ)
    (hF : Stacks.SheafOfModules.OnSpace.IsLocallyBounded (inverseImageBase f) F)
    (hflat : ∀ i : ℤ, AlgebraicGeometry.SheafOfModules.IsFlat.{u, u, u, u}
      (O := (inverseImageBase f).sheaf) (F.X i))
    (M : ℤ → X.Modules) (hM : ∀ i, (M i).IsQuasicoherent)
    (hFM : ∀ i, F.X i ≅ (pushforward (toInverseImageBase f)).obj (M i)) :
    (∀ s : S, ∃ U : S.Opens, s ∈ U ∧ DerivedCategoryB.IsBounded
      ((Scheme.Modules.restrictFunctor U.ι).mapDerivedCategory.obj
        ((derivedPushforward (inverseImageBaseProjection f)).obj
          (DerivedCategory.Q.obj F)))) ∧
    (DerivedCategoryB.derivedCategoryB (_root_.SheafOfModules.isQuasicoherent S.ringCatSheaf) :
      ObjectProperty (DerivedCategory (Modules S.toRingedSpace)))
      ((derivedPushforward (inverseImageBaseProjection f)).obj (DerivedCategory.Q.obj F)) ∧
    LocallyHasFiniteTorDimension S.toRingedSpace
      ((derivedPushforward (inverseImageBaseProjection f)).obj (DerivedCategory.Q.obj F)) ∧
    (∀ G : Modules S.toRingedSpace, G.IsQuasicoherent →
      Nonempty (((derivedTensorProductFunctor S.toRingedSpace.sheaf).obj
          ((derivedPushforward (inverseImageBaseProjection f)).obj
            (DerivedCategory.Q.obj F))).obj
        ((DerivedCategory.singleFunctor (Modules S.toRingedSpace) 0).obj G) ≅
        (derivedPushforward (inverseImageBaseProjection f)).obj
          (DerivedCategory.Q.obj
            (((Stacks.SheafOfModules.Tensor.tensorComplex (inverseImageBase f).sheaf).obj F).obj
              ((CochainComplex.singleFunctor (Modules (inverseImageBase f)) 0).obj
                ((RingedSpaceModuleAdjunction.modulePullback
                  (inverseImageBaseProjection f)).obj G)))))) ∧
    (∀ K : DerivedCategory (Modules S.toRingedSpace),
      DerivedCategoryB.derivedCategoryB
        (_root_.SheafOfModules.isQuasicoherent S.ringCatSheaf) K →
      IsIso (Stacks.Cohomology.DerivedProjectionFormula.projectionFormulaMap
        (inverseImageBaseProjection f) (DerivedCategory.Q.obj F) K))
```

**`Stacks.RelativeComplexPushforward.isQuasicoherent_homology_relativeDerivedPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativeComplexPushforwardQcoh.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/RelativeComplexPushforwardQcoh.lean#L89). The attribute's comment: “conclusion (2), that Ra\_* of the complex lies in D\_QCoh, degreewise, for a complex bounded below with an explicit bound rather than merely locally bounded”.

> **Stacks Project, Tag 0FML, conclusion (2).** Let `f : X ⟶ S` be quasi-compact and
> quasi-separated and let `K` be a complex of `f^{-1}𝒪_S`-modules, strictly bounded below, whose
> term in degree `i` is the restriction of scalars of a quasi-coherent `𝒪_X`-module `M i`. Then
> every cohomology sheaf of `Rf_*K` is quasi-coherent.

```lean
theorem isQuasicoherent_homology_relativeDerivedPushforward [QuasiCompact f] [QuasiSeparated f]
    (n : ℤ) (K : CochainComplex (Modules (inverseImageBase f)) ℤ)
    [CochainComplex.IsStrictlyGE K n] (M : ℤ → X.Modules) (hM : ∀ i, (M i).IsQuasicoherent)
    (hK : ∀ i, K.X i ≅ (pushforward (toInverseImageBase f)).obj (M i)) (i : ℤ) :
    ((DerivedCategory.Plus.homologyFunctor S.Modules i).obj
      (relativeDerivedPushforward f n K)).IsQuasicoherent
```

**`Stacks.RelativeComplexPushforward.derivedCategoryB_relativeDerivedPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativeComplexPushforwardQcoh.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/RelativeComplexPushforwardQcoh.lean#L127). The attribute's comment: “conclusion (2), that Ra\_* of the complex lies in D\_QCoh, as a membership, for a complex bounded below with an explicit bound rather than merely locally bounded”.

> **Stacks Project, Tag 0FML, conclusion (2)**, in the membership form: the object property on
> `D(𝒪_S)` cutting out the complexes with quasi-coherent cohomology holds of `Rf_*K`. The complex
> being bounded below, `Rf_*K` is read in `D⁺(𝒪_S)` and compared with `D(𝒪_S)` along the
> inclusion, under which the cohomology functors agree.

```lean
theorem derivedCategoryB_relativeDerivedPushforward [QuasiCompact f] [QuasiSeparated f]
    (n : ℤ) (K : CochainComplex (Modules (inverseImageBase f)) ℤ)
    [CochainComplex.IsStrictlyGE K n] (M : ℤ → X.Modules) (hM : ∀ i, (M i).IsQuasicoherent)
    (hK : ∀ i, K.X i ≅ (pushforward (toInverseImageBase f)).obj (M i)) :
    DerivedCategoryB.derivedCategoryB (_root_.SheafOfModules.isQuasicoherent S.ringCatSheaf)
      (DerivedCategory.Plus.ι.obj (relativeDerivedPushforward f n K))
```

## Tag 0FMQ, a lemma

[Tag 0FMQ](https://stacks.math.columbia.edu/tag/0FMQ) in the Stacks Project.

**`AlgebraicGeometry.kFlat_totalCechComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/Coherator/KunnethTotalCech.lean, line 1082](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/Coherator/KunnethTotalCech.lean#L1082).

> **Stacks 0FMQ.** Let `f : X ⟶ S` be a morphism of schemes with `S` affine and
> `A = Γ(S, 𝒪_S)`, and let `U : I → X.Opens` be a finite family of opens all of whose
> finite intersections are affine. Let `K` be a bounded complex of presheaves of `A`-modules
> on `X` whose degree-`n` term is the presheaf of sections of a quasi-coherent `𝒪_X`-module
> `F n` that is flat over `S`. Then `Tot(Č^•(𝒰, K))` is K-flat as a complex of `A`-modules.

```lean
public theorem kFlat_totalCechComplex {X S : Scheme.{u}} [IsAffine S] (f : X ⟶ S)
    {I : Type u} [Finite I] (U : I → X.Opens)
    (haffine : ∀ (p : ℕ) (s : Fin (p + 1) → I), IsAffineOpen (⨅ k, U (s k)))
    (K : CochainComplex ((X.Opens)ᵒᵖ ⥤ ModuleCat.{u} ↑Γ(S, ⊤)) ℤ) (a b : ℤ)
    [CochainComplex.IsStrictlyGE K a] [CochainComplex.IsStrictlyLE K b]
    (F : ℤ → X.Modules) (hqc : ∀ n, (F n).IsQuasicoherent)
    (hflat : ∀ n, IsFlatOver f.toLRSHom.toShHom (F n))
    (hterm : ∀ n, K.X n ≅ sectionsPresheaf f (F n)) :
    CochainComplex.KFlat.{u, u} ((totalCechComplex U).obj K)
```

## Tag 0G49, an equation

[Tag 0G49](https://stacks.math.columbia.edu/tag/0G49) in the Stacks Project.

**`Stacks.Cohomology.GlobalKunneth.kunnethMapOfSheavesCanonical`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalCupProductCanonicalInstances.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalCupProductCanonicalInstances.lean#L192). The attribute's comment: “the map, at the A-linear global cup product `globalCupProductCanonical` of Section 0FKU on the base”.

> **The global Künneth map for two module sheaves at the canonical global cup product.**
>
> `RΓ(X, ℱ) ⊗^𝐋_A RΓ(Y, 𝒢) ⟶ RΓ(W, p^*ℱ ⊗_{𝒪_W} q^*𝒢)`
>
> in `D(A)` for `A = Γ(S, 𝒪_S)`, where `p ≫ a = f = q ≫ b`; the source takes `W = X ×_S Y` with
> its two projections.  It is `Stacks.Cohomology.GlobalKunneth.kunnethMapOfSheaves` at the
> canonical global cup product of Section 0FKU.

```lean
def kunnethMapOfSheavesCanonical (F : Modules X.sheaf) (G : Modules Y.sheaf) :
    ((tensorBase S).obj ((sectionsOverBase a).obj (singleD F))).obj
        ((sectionsOverBase b).obj (singleD G)) ⟶
      (sectionsOverBase f).obj
        (singleD (sheafTensorObj ((modulePullback p).obj F) ((modulePullback q).obj G)))
```

**`Stacks.Cohomology.GlobalKunneth.kunnethMapOfSheavesCanonical_eq_kunnethGlobalMapCanonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalCupProductCanonicalInstances.lean, line 220](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalCupProductCanonicalInstances.lean#L220). The attribute's comment: “the map is the derived map at the sheaves in degree zero: both sides are at the canonical global cup product, the right-hand side being `kunnethGlobalMapCanonical` of Tag 0G7V”.

> The Künneth map for two module sheaves at the canonical global cup product is the derived
> Künneth map `kunnethGlobalMapCanonical` at the two sheaves placed in degree zero, followed by
> derived global sections of the canonical comparison from the derived tensor product of the derived
> pullbacks to the ordinary tensor product of the ordinary pullbacks.

```lean
theorem kunnethMapOfSheavesCanonical_eq_kunnethGlobalMapCanonical (F : Modules X.sheaf)
    (G : Modules Y.sheaf) :
    kunnethMapOfSheavesCanonical a b p q f hp hq F G =
      kunnethGlobalMapCanonical a b p q f hp hq (singleD F) (singleD G) ≫
        (sectionsOverBase f).map (externalTensorComparison p q F G)
```

**`Stacks.Cohomology.GlobalKunneth.kunnethMapOfSheavesCanonical_naturality_derived`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalCupProductCanonicalInstances.lean, line 230](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalCupProductCanonicalInstances.lean#L230). The attribute's comment: “naturality inherited from the derived map, at the canonical global cup product”.

> The derived Künneth map `kunnethGlobalMapCanonical` at sheaves placed in degree zero, the
> first factor of `kunnethMapOfSheavesCanonical`, is natural in the two sheaves `ℱ` and `𝒢`.

```lean
theorem kunnethMapOfSheavesCanonical_naturality_derived
    {F F' : Modules X.sheaf} {G G' : Modules Y.sheaf} (φ : F ⟶ F') (ψ : G ⟶ G') :
    (Functor.uncurry.obj (tensorBase S)).map
          ((sectionsOverBase a).map (DerivedCategory.Q.map
              ((CochainComplex.singleFunctor (Modules X.sheaf) 0).map φ)) ×ₘ
            (sectionsOverBase b).map (DerivedCategory.Q.map
              ((CochainComplex.singleFunctor (Modules Y.sheaf) 0).map ψ))) ≫
        kunnethGlobalMapCanonical a b p q f hp hq (singleD F') (singleD G') =
      kunnethGlobalMapCanonical a b p q f hp hq (singleD F) (singleD G) ≫
        (sectionsOverBase f).map
          ((Functor.uncurry.obj (derivedTensorProductFunctor W.sheaf)).map
            ((derivedPullback p).map (DerivedCategory.Q.map
                ((CochainComplex.singleFunctor (Modules X.sheaf) 0).map φ)) ×ₘ
              (derivedPullback q).map (DerivedCategory.Q.map
                ((CochainComplex.singleFunctor (Modules Y.sheaf) 0).map ψ))))
```

**`Stacks.Cohomology.GlobalKunneth.kunnethMapOfSheavesSchemeCanonical`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalCupProductCanonicalInstances.lean, line 265](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalCupProductCanonicalInstances.lean#L265). The attribute's comment: “the map at X ×\_S Y, at the global cup product `globalCupProductCanonical` on the base”.

> **The global Künneth map at the fibre product of two schemes, at the canonical global cup
> product.** For schemes `a : X ⟶ S` and `b : Y ⟶ S` over a base, `A = Γ(S, 𝒪_S)`, an
> `𝒪_X`-module `ℱ` and an `𝒪_Y`-module `𝒢`, the canonical map
>
> `RΓ(X, ℱ) ⊗^𝐋_A RΓ(Y, 𝒢) ⟶ RΓ(X ×_S Y, p^*ℱ ⊗_{𝒪_{X ×_S Y}} q^*𝒢)`
>
> in `D(A)`, where `p` and `q` are the two projections of `X ×_S Y` and the target is the external
> tensor product of Tag 0G46 placed in degree zero.

```lean
def kunnethMapOfSheavesSchemeCanonical (F : X.Modules) (G : Y.Modules) :
    ((tensorBase S.toRingedSpace).obj
          ((sectionsOverBase a.toLRSHom.toShHom).obj (singleD F))).obj
        ((sectionsOverBase b.toLRSHom.toShHom).obj (singleD G)) ⟶
      (sectionsOverBase (pullback.fst a b ≫ a).toLRSHom.toShHom).obj
        (singleD (externalTensorProduct a b F G))
```

**`Stacks.Cohomology.GlobalKunneth.kunnethMapOfSheavesSchemeCanonical_eq_kunnethGlobalMapSchemeCanonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalCupProductCanonicalInstances.lean, line 286](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalCupProductCanonicalInstances.lean#L286). The attribute's comment: “the map at the fibre product is the derived map at the sheaves in degree zero: both sides are at the canonical global cup product, the right-hand side being `kunnethGlobalMapSchemeCanonical` of Tag 0G7V”.

> At the fibre product of two schemes, the Künneth map for two module sheaves at the canonical
> global cup product is the derived Künneth map `kunnethGlobalMapSchemeCanonical` at the two sheaves
> placed in degree zero, followed by derived global sections of `externalTensorComparison`.

```lean
theorem kunnethMapOfSheavesSchemeCanonical_eq_kunnethGlobalMapSchemeCanonical
    (F : X.Modules) (G : Y.Modules) :
    kunnethMapOfSheavesSchemeCanonical a b F G =
      kunnethGlobalMapSchemeCanonical a b (singleD F) (singleD G) ≫
        (sectionsOverBase (pullback.fst a b ≫ a).toLRSHom.toShHom).map
          (externalTensorComparison (pullback.fst a b).toLRSHom.toShHom
            (pullback.snd a b).toLRSHom.toShHom F G)
```

## Tag 0FU4, a lemma

[Tag 0FU4](https://stacks.math.columbia.edu/tag/0FU4) in the Stacks Project.

**`AlgebraicGeometry.FlatKunneth.isIso_kunnethMapOfSheavesSchemeCanonical_of_affineDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/FlatKunneth/KunnethFlatSheaves.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/BaseChange/FlatKunneth/KunnethFlatSheaves.lean#L257).

> **[Stacks, Tag 0FU4].**  Let `a : X ⟶ S` and `b : Y ⟶ S` be morphisms of schemes with `S`
> affine, let `A = Γ(S, 𝒪_S)`, and let `p`, `q` be the projections of `X ×_S Y`.  If `ℱ` on `X` and
> `𝒢` on `Y` are `S`-flat and quasi-coherent and `X` and `Y` are quasi-compact with affine
> diagonal, then the Künneth map of [Stacks, Tag 0G49]
>
> `RΓ(X, ℱ) ⊗^𝐋_A RΓ(Y, 𝒢) ⟶ RΓ(X ×_S Y, p^*ℱ ⊗_{𝒪_{X ×_S Y}} q^*𝒢)`
>
> is an isomorphism in `D(A)`.  The map is
> `Stacks.Cohomology.GlobalKunneth.kunnethMapOfSheavesSchemeCanonical`, built from the global cup
> product of Cohomology, Section 0FKU with no parameter.
>
> Nothing is carried.  Quasi-compactness and affineness of the diagonals give the
> quasi-compactness and quasi-separatedness of `a` and `b`; affineness of `S`, flatness of `𝒢` and
> quasi-coherence of `ℱ` and `𝒢` are consumed by
> `isIso_kunnethMapOfSheavesSchemeCanonical_of_isFlatOver`, which this specializes.  Flatness of
> `ℱ` is the tag's hypothesis but the proof does not need it: one flat factor suffices, by the
> Tor vanishing of [Stacks, Tag 0GMU].

```lean
theorem isIso_kunnethMapOfSheavesSchemeCanonical_of_affineDiagonal [IsAffine S] [CompactSpace X]
    [CompactSpace Y] [IsAffineHom (pullback.diagonal (terminal.from X))]
    [IsAffineHom (pullback.diagonal (terminal.from Y))]
    (F : X.Modules) (G : Y.Modules) [F.IsQuasicoherent] [G.IsQuasicoherent]
    (_hF : IsFlatOver a.toLRSHom.toShHom F) (hG : IsFlatOver b.toLRSHom.toShHom G) :
    IsIso (kunnethMapOfSheavesSchemeCanonical a b F G)
```

**`Stacks.Cohomology.GlobalKunneth.isIso_kunnethMapOfSheavesScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/KunnethIsomorphismOfSheaves.lean, line 239](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/KunnethIsomorphismOfSheaves.lean#L239). The attribute's comment: “the isomorphism at X ×\_S Y; three inputs are carried, so the geometric hypotheses are not consumed: hκ, invertibility of the global cup product on the affine base, which no bare GlobalCupProduct has; hrel, Tag 0FLQ at the sheaves in degree zero; hext, the 06YU comparison, which the tag's relative S-flatness cannot discharge in this library”.

> **[Stacks, Tag 0FU4].**  Let `a : X ⟶ S` and `b : Y ⟶ S` be morphisms of schemes with `S`
> affine, let `A = Γ(S, 𝒪_S)` and let `p`, `q` be the projections of `W = X ×_S Y`.  If `X` and `Y`
> are quasi-compact with affine diagonal and `ℱ` on `X`, `𝒢` on `Y` are quasi-coherent and flat
> over `S`, then the Künneth map of [Stacks, Tag 0G49]
>
> `RΓ(X, ℱ) ⊗^𝐋_A RΓ(Y, 𝒢) ⟶ RΓ(X ×_S Y, ℱ ⊠ 𝒢)`
>
> is an isomorphism in `D(A)`.
>
> The three inputs of the proof are carried as the hypotheses `hκ`, `hrel` and `hext`, and the
> geometric hypotheses are therefore not consumed; the implementation notes of this file say what
> each of the three is and why none is available in the library.  `hκ` is the invertibility of the
> `A`-linear global cup product on the affine base, `hrel` is [Stacks, Tag 0FLQ] at the two sheaves
> placed in degree zero, and `hext` is the invertibility of the derived-to-ordinary comparison in
> which the source consumes the flatness of `ℱ` and `𝒢`.  What is proved here is that the three
> suffice.

```lean
theorem isIso_kunnethMapOfSheavesScheme [IsAffine S] [CompactSpace X] [CompactSpace Y]
    [IsAffineHom (pullback.diagonal (terminal.from X))]
    [IsAffineHom (pullback.diagonal (terminal.from Y))]
    (κ : GlobalCupProduct S.toRingedSpace) (F : X.Modules) (G : Y.Modules)
    [F.IsQuasicoherent] [G.IsQuasicoherent]
    (_hF : IsFlatOver a.toLRSHom.toShHom F) (_hG : IsFlatOver b.toLRSHom.toShHom G)
    (hκ : IsIso (κ.app ((derivedPushforward a.toLRSHom.toShHom).obj (singleD F),
      (derivedPushforward b.toLRSHom.toShHom).obj (singleD G))))
    (hrel : IsIso (Stacks.Cohomology.DerivedKunneth.kunnethMap a.toLRSHom.toShHom
      b.toLRSHom.toShHom (pullback.fst a b).toLRSHom.toShHom
      (pullback.snd a b).toLRSHom.toShHom (pullback.fst a b ≫ a).toLRSHom.toShHom rfl
      (toShHom_pullback_condition a b) (singleD F) (singleD G)))
    (hext : IsIso (externalTensorComparison (pullback.fst a b).toLRSHom.toShHom
      (pullback.snd a b).toLRSHom.toShHom F G)) :
    IsIso (kunnethMapOfSheavesScheme a b κ F G)
```

## Tag 0G7W, a remark

[Tag 0G7W](https://stacks.math.columbia.edu/tag/0G7W) in the Stacks Project.

**`Stacks.Cohomology.KunnethCupWithClass.kunnethGlobalMapSchemeCanonical_cupWithClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalKunnethCupWithClassCanonical.lean, line 481](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalKunnethCupWithClassCanonical.lean#L481).

> **Remark 0G7W.**  Let `a : X ⟶ S` and `b : Y ⟶ S` be morphisms of schemes, let
> `p : X ×_S Y ⟶ X` and `q : X ×_S Y ⟶ Y` be the projections, and set `A = Γ(S, 𝒪_S)`.  Let
> `𝒢, ℱ ∈ D(𝒪_X)` and `ℰ ∈ D(𝒪_Y)` — for instance quasi-coherent modules placed in degree
> zero — and let `ξ ∈ Hⁱ(X, 𝒢)`, with pullback `p^*ξ ∈ Hⁱ(X ×_S Y, Lp^*𝒢)`, represented by the
> morphism `A[-i] ⟶ RΓ(X, 𝒢)` representing `ξ` followed by the pullback map
> `p^* : RΓ(X, 𝒢) ⟶ RΓ(X ×_S Y, Lp^*𝒢)` (that this represents the class `Hⁱ(p^*)(ξ)` is
> `Stacks.Cohomology.KunnethCupWithClass.classOverBase_comp_homology`).  Then the square
>
> ```
> RΓ(X, ℱ)[-i] ⊗^𝐋_A RΓ(Y, ℰ) --ξ ⊗ 1--> RΓ(X, 𝒢 ⊗ ℱ) ⊗^𝐋_A RΓ(Y, ℰ)
>            |                                            |
>            v                                            v
> RΓ(X ×_S Y, Lp^*ℱ ⊗ Lq^*ℰ)[-i] --p^*ξ--> RΓ(X ×_S Y, Lp^*(𝒢 ⊗ ℱ) ⊗ Lq^*ℰ)
> ```
>
> commutes in `D(A)`.  The horizontal arrows are cup product with a class, Remark 0G6W, for the
> `A`-linear global cup products of Section 0FKU on `X` and on `X ×_S Y`; the vertical arrows are
> the global Künneth map of Equation 36.23.0.2, `kunnethGlobalMapSchemeCanonical` (Tag 0G7V),
> shifted by `[-i]` through the source's identification `M[-i] = A[-i] ⊗^𝐋_A M`.  Nothing is a
> parameter: the cup products, the pullback map, the associativity constraint `baseAssociator`
> of `⊗^𝐋_A` (that of `D({*}, A)` read through `D(A) = D({*}, A)`, as in Section 0FKU) and that
> of `⊗^𝐋_{𝒪}` (Tag 0FPB) are all canonical.  The two identifications the source makes silently in
> the bottom-right corner, `Lp^*(𝒢 ⊗ ℱ) = Lp^*𝒢 ⊗ Lp^*ℱ` (Tag 079U) and the rebracketing, are
> the last two arrows of the right-hand route.  No quasi-coherence, affineness or finiteness
> hypothesis is needed.

```lean
theorem kunnethGlobalMapSchemeCanonical_cupWithClass
    (𝒢 ℱ : DerivedCategory X.Modules) (ℰ : DerivedCategory Y.Modules) (i : ℤ)
    (ξ : ModuleCat.of (baseRing S.toRingedSpace) (baseRing S.toRingedSpace) ⟶
      cohomologyModuleOverBase a.toLRSHom.toShHom 𝒢 i) :
    ((tensorBase S.toRingedSpace).map
          (cupWithClassOverBase (sectionsOverBaseComparison a.toLRSHom.toShHom) 𝒢 ℱ i
            (classOverBase a.toLRSHom.toShHom 𝒢 i ξ))).app
          ((sectionsOverBase b.toLRSHom.toShHom).obj ℰ) ≫
        kunnethGlobalMapSchemeCanonical a b
            (((derivedTensorProductFunctor X.toRingedSpace.sheaf).obj 𝒢).obj ℱ) ℰ ≫
          (sectionsOverBase (pullback.fst a b ≫ a).toLRSHom.toShHom).map
              ((Functor.uncurry.obj
                  (derivedTensorProductFunctor (pullback a b).toRingedSpace.sheaf)).map
                (pullbackTensorComparisonApp (pullback.fst a b).toLRSHom.toShHom 𝒢 ℱ ×ₘ
                  𝟙 ((derivedPullback (pullback.snd a b).toLRSHom.toShHom).obj ℰ))) ≫
            (sectionsOverBase (pullback.fst a b ≫ a).toLRSHom.toShHom).map
              (derivedAssociator (pullback a b).toRingedSpace
                ((derivedPullback (pullback.fst a b).toLRSHom.toShHom).obj 𝒢)
                ((derivedPullback (pullback.fst a b).toLRSHom.toShHom).obj ℱ)
                ((derivedPullback (pullback.snd a b).toLRSHom.toShHom).obj ℰ)) =
      (Functor.uncurry.obj (tensorBase S.toRingedSpace)).map
          ((baseShiftTensorIso S.toRingedSpace i
              ((sectionsOverBase a.toLRSHom.toShHom).obj ℱ)).inv ×ₘ
            𝟙 ((sectionsOverBase b.toLRSHom.toShHom).obj ℰ)) ≫
        baseAssociator S.toRingedSpace (baseShift S.toRingedSpace i)
            ((sectionsOverBase a.toLRSHom.toShHom).obj ℱ)
            ((sectionsOverBase b.toLRSHom.toShHom).obj ℰ) ≫
          ((tensorBase S.toRingedSpace).obj (baseShift S.toRingedSpace i)).map
              (kunnethGlobalMapSchemeCanonical a b ℱ ℰ) ≫
            (baseShiftTensorIso S.toRingedSpace i
              ((sectionsOverBase (pullback.fst a b ≫ a).toLRSHom.toShHom).obj
                (((derivedTensorProductFunctor (pullback a b).toRingedSpace.sheaf).obj
                  ((derivedPullback (pullback.fst a b).toLRSHom.toShHom).obj ℱ)).obj
                    ((derivedPullback (pullback.snd a b).toLRSHom.toShHom).obj ℰ)))).hom ≫
              cupWithClassOverBase
                (sectionsOverBaseComparison (pullback.fst a b ≫ a).toLRSHom.toShHom)
                ((derivedPullback (pullback.fst a b).toLRSHom.toShHom).obj 𝒢)
                (((derivedTensorProductFunctor (pullback a b).toRingedSpace.sheaf).obj
                    ((derivedPullback (pullback.fst a b).toLRSHom.toShHom).obj ℱ)).obj
                  ((derivedPullback (pullback.snd a b).toLRSHom.toShHom).obj ℰ)) i
                (classOverBase a.toLRSHom.toShHom 𝒢 i ξ ≫
                  pullbackSections a.toLRSHom.toShHom (pullback.fst a b).toLRSHom.toShHom
                    (pullback.fst a b ≫ a).toLRSHom.toShHom rfl 𝒢)
```

**`Stacks.Cohomology.DerivedGlobalCupProduct.kunnethOverBase_cupWithClassOverBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalKunnethMapAndCupProduct.lean, line 561](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/GlobalKunnethMapAndCupProduct.lean#L561). The attribute's comment: “the commutativity of the square, for A-linear cup products built from a one-point comparison on X and on W (the parameters `κX`, `κW`, as for Section 0FKU in this development), for the pullback map `π` on derived global sections with its compatibility `hπ` with the two cup products (Cohomology, Lemma 0FP6, which this development cannot transport onto them), and for associativity constraints `aA`, `aB` with their naturality `haA`, `haB` and the compatibility `hα` of the comparison with them, all universally quantified; the source's suppressed identifications p^*(G ⊗ F) = p^*G ⊗ p^*F of Tag 079U and the rebracketing are the last two arrows of the right-hand route”.

> **Remark 0G7W.**  Let `a : X ⟶ S` and `b : Y ⟶ S` be spaces over a base, let `p : W ⟶ X`,
> `q : W ⟶ Y` and `f : W ⟶ S` with `p ≫ a = f = q ≫ b`, and set `A = Γ(S, 𝒪_S)`.  For
> `𝒢, ℱ ∈ D(𝒪_X)`, `ℰ ∈ D(𝒪_Y)` and a class `ξ ∈ Hⁱ(X, 𝒢)` represented by a morphism
> `A[-i] ⟶ RΓ(X, 𝒢)`, the square
>
> ```
> RΓ(X, ℱ)[-i] ⊗^𝐋_A RΓ(Y, ℰ) --ξ ⊗ 1--> RΓ(X, 𝒢 ⊗^𝐋 ℱ) ⊗^𝐋_A RΓ(Y, ℰ)
>            |                                            |
>            v                                            v
> RΓ(W, Lp^*ℱ ⊗^𝐋 Lq^*ℰ)[-i] --p^*ξ--> RΓ(W, Lp^*(𝒢 ⊗^𝐋 ℱ) ⊗^𝐋 Lq^*ℰ)
> ```
>
> commutes in `D(A)`, the horizontals being cup product with a class as in Remark 0G6W and the
> verticals the global Künneth map of Equation 36.23.0.2.  The right-hand route is continued by
> the pullback–tensor comparison of Tag 079U and the associativity constraint, the two
> identifications the source makes silently in its bottom-right corner.

```lean
theorem kunnethOverBase_cupWithClassOverBase
    (aA : ∀ P Q Z : DerivedCategory (ModuleCat.{u} (baseRing S)),
      ((tensorBase S).obj (((tensorBase S).obj P).obj Q)).obj Z ⟶
        ((tensorBase S).obj P).obj (((tensorBase S).obj Q).obj Z))
    (aB : ∀ U V Z : DerivedCategory (SheafOfModules.{u} (structureSheafRing W)),
      ((derivedTensorProductFunctor W.sheaf).obj
          (((derivedTensorProductFunctor W.sheaf).obj U).obj V)).obj Z ⟶
        ((derivedTensorProductFunctor W.sheaf).obj U).obj
          (((derivedTensorProductFunctor W.sheaf).obj V).obj Z))
    (haA : ∀ {P P' Q Q' Z Z' : DerivedCategory (ModuleCat.{u} (baseRing S))} (k : P ⟶ P')
        (l : Q ⟶ Q') (m : Z ⟶ Z'),
      (Functor.uncurry.obj (tensorBase S)).map
            ((Functor.uncurry.obj (tensorBase S)).map (k ×ₘ l) ×ₘ m) ≫ aA P' Q' Z' =
        aA P Q Z ≫
          (Functor.uncurry.obj (tensorBase S)).map
            (k ×ₘ (Functor.uncurry.obj (tensorBase S)).map (l ×ₘ m)))
    (haB : ∀ {U U' V V' Z Z' : DerivedCategory (SheafOfModules.{u} (structureSheafRing W))}
        (k : U ⟶ U') (l : V ⟶ V') (m : Z ⟶ Z'),
      (Functor.uncurry.obj (derivedTensorProductFunctor W.sheaf)).map
            ((Functor.uncurry.obj (derivedTensorProductFunctor W.sheaf)).map (k ×ₘ l) ×ₘ m) ≫
          aB U' V' Z' =
        aB U V Z ≫
          (Functor.uncurry.obj (derivedTensorProductFunctor W.sheaf)).map
            (k ×ₘ (Functor.uncurry.obj (derivedTensorProductFunctor W.sheaf)).map (l ×ₘ m)))
    (hα : ∀ P Q Z : DerivedCategory (ModuleCat.{u} (baseRing S)),
      κW.tensorComparison.app ((Functor.uncurry.obj (tensorBase S)).obj (P, Q), Z) ≫
          (Functor.uncurry.obj (derivedTensorProductFunctor W.sheaf)).map
              (κW.tensorComparison.app (P, Q) ×ₘ 𝟙 (κW.pullback.obj Z)) ≫
            aB (κW.pullback.obj P) (κW.pullback.obj Q) (κW.pullback.obj Z) =
        κW.pullback.map (aA P Q Z) ≫
          κW.tensorComparison.app (P, (Functor.uncurry.obj (tensorBase S)).obj (Q, Z)) ≫
            (Functor.uncurry.obj (derivedTensorProductFunctor W.sheaf)).map
              (𝟙 (κW.pullback.obj P) ×ₘ κW.tensorComparison.app (Q, Z)))
    (hπ : CupProductPullbackCompatible κX κW π)
    (ξ : baseShift S i ⟶ (sectionsOverBase a).obj 𝒢) :
    ((tensorBase S).map (cupWithClassOverBase κX 𝒢 ℱ i ξ)).app
            ((sectionsOverBase b).obj ℰ) ≫
        kunnethOverBase κW π ρ (((derivedTensorProductFunctor X.sheaf).obj 𝒢).obj ℱ) ℰ ≫
          (sectionsOverBase f).map
              ((Functor.uncurry.obj (derivedTensorProductFunctor W.sheaf)).map
                (pullbackTensorComparisonApp p 𝒢 ℱ ×ₘ 𝟙 ((derivedPullback q).obj ℰ))) ≫
            (sectionsOverBase f).map
              (aB ((derivedPullback p).obj 𝒢) ((derivedPullback p).obj ℱ)
                ((derivedPullback q).obj ℰ)) =
      (Functor.uncurry.obj (tensorBase S)).map
          ((baseShiftTensorIso S i ((sectionsOverBase a).obj ℱ)).inv ×ₘ
            𝟙 ((sectionsOverBase b).obj ℰ)) ≫
        aA (baseShift S i) ((sectionsOverBase a).obj ℱ) ((sectionsOverBase b).obj ℰ) ≫
          ((tensorBase S).obj (baseShift S i)).map (kunnethOverBase κW π ρ ℱ ℰ) ≫
            (baseShiftTensorIso S i
              ((sectionsOverBase f).obj
                (((derivedTensorProductFunctor W.sheaf).obj
                  ((derivedPullback p).obj ℱ)).obj ((derivedPullback q).obj ℰ)))).hom ≫
              cupWithClassOverBase κW ((derivedPullback p).obj 𝒢)
                (((derivedTensorProductFunctor W.sheaf).obj ((derivedPullback p).obj ℱ)).obj
                  ((derivedPullback q).obj ℰ)) i (ξ ≫ π 𝒢)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.23, Tag 0FLN](https://stacks.math.columbia.edu/tag/0FLN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
