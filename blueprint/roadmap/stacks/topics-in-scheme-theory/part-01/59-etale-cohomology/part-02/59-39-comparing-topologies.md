---
declaration: section
origin: cited
lean: AlgebraicGeometry.openEqLocus, AlgebraicGeometry.factorsThrough_openEqLocus_iff, AlgebraicGeometry.zariskiInverseImageSectionsComparison, AlgebraicGeometry.zariskiInverseImageSectionsIso, AlgebraicGeometry.etaleInverseImageSectionsComparison, AlgebraicGeometry.etaleInverseImageSectionsIso, AlgebraicGeometry.smallSiteInverseImage_sections_and_isSheaf_fpqc, Stacks.EtaleCohomology.isIso_globalSectionsSmallEtaleInverseImage_of_flat_quasiCompact
statement: formalized
proof: formalized
---

# 59.39 Comparing topologies

Section 59.39 of the Stacks Project, [Tag 09XL](https://stacks.math.columbia.edu/tag/09XL). 5 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09XM, a lemma

[Tag 09XM](https://stacks.math.columbia.edu/tag/09XM) in the Stacks Project.

**`AlgebraicGeometry.openEqLocus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/OpenEqualityLocus.lean, line 405](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/OpenEqualityLocus.lean#L405). The attribute's comment: “open locus”.

> **Stacks 09XM, the open locus.** The largest open subscheme of `S` on which two global
> sections of a sheaf on the small étale site of `S` agree: the supremum of the opens through
> which only agreeing morphisms factor.

```lean
public def openEqLocus : (B.inclusion.obj S).Opens
```

**`AlgebraicGeometry.factorsThrough_openEqLocus_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/OpenEqualityLocus.lean, line 435](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/OpenEqualityLocus.lean#L435). The attribute's comment: “universal property”.

> **Stacks 09XM, the universal property.** A morphism of the big étale site factors through
> the open equality locus exactly when the two sections agree after inverse image along the
> induced morphism of small étale topoi.

```lean
public theorem factorsThrough_openEqLocus_iff (f : T ⟶ S) :
    (∃ g : B.inclusion.obj T ⟶ (openEqLocus B S F s t).toScheme,
      g ≫ (openEqLocus B S F s t).ι = B.inclusion.map f) ↔
      (smallEtalePullback B S T f).map s =
        (smallEtalePullback B S T f).map t
```

## Tag 09XN, a lemma

[Tag 09XN](https://stacks.math.columbia.edu/tag/09XN) in the Stacks Project.

**`AlgebraicGeometry.zariskiInverseImageSectionsComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiPullbackSections.lean, line 288](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiPullbackSections.lean#L288). The attribute's comment: “pullback\_formula”.

> The section comparisons for all schemes over `S`, compatible with the canonical
> small-pullback restriction maps. The family and the compatibility are chosen together.

```lean
public noncomputable def zariskiInverseImageSectionsComparison
    (B : BigZariskiSite.{u}) (S : B.Schemes) :
    { e : ∀ X : BigZariskiOver B S.1 S.property,
        (smallZariskiProjection B S).inverseImage ⋙
          (sheafSections (BigZariskiOver.topology B S.1 S.property)
            (Type (u + 1))).obj (Opposite.op X) ≅
        (smallZariskiBaseChange B X.hom).sheafPullback
            (Type (u + 1))
            (SmallZariski.topology B S.1 S.property)
            (SmallZariski.topology B X.left.1 X.left.property) ⋙
          Sheaf.Γ (SmallZariski.topology B X.left.1 X.left.property)
            (Type (u + 1)) //
      ∀ {X Y : BigZariskiOver B S.1 S.property} (g : Y ⟶ X)
        (F : Sheaf (SmallZariski.topology B S.1 S.property) (Type (u + 1))),
        (e X).hom.app F ≫ zariskiPullbackSectionsRestriction B S g F =
          ((smallZariskiProjection B S).inverseImage.obj F).obj.map g.op ≫
            (e Y).hom.app F }
```

**`AlgebraicGeometry.zariskiInverseImageSectionsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiPullbackSections.lean, line 366](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiPullbackSections.lean#L366). The attribute's comment: “pullback\_formula”.

> **Stacks 09XN, pullback formula (Zariski case).** For a sheaf `F` on the small Zariski site
> of `S` and a scheme `f : X ⟶ S` over `S`, the sections of `π_S⁻¹F` at `X` are the global
> sections of the small Zariski pullback `f⁻¹F`, naturally in `F`. Restriction in `X` is recorded
> by `AlgebraicGeometry.zariskiInverseImageSectionsIso_naturality`.

```lean
public noncomputable def zariskiInverseImageSectionsIso
    (B : BigZariskiSite.{u}) (S : B.Schemes) (X : BigZariskiOver B S.1 S.property) :
    (smallZariskiProjection B S).inverseImage ⋙
      (sheafSections (BigZariskiOver.topology B S.1 S.property)
        (Type (u + 1))).obj (Opposite.op X) ≅
    (smallZariskiBaseChange B X.hom).sheafPullback
        (Type (u + 1))
        (SmallZariski.topology B S.1 S.property)
        (SmallZariski.topology B X.left.1 X.left.property) ⋙
      Sheaf.Γ (SmallZariski.topology B X.left.1 X.left.property)
        (Type (u + 1))
```

**`AlgebraicGeometry.etaleInverseImageSectionsComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtalePullbackSections.lean, line 245](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtalePullbackSections.lean#L245). The attribute's comment: “pullback\_formula”.

> The section comparisons for all schemes over `S`, compatible with the canonical
> small-pullback restriction maps. The family and the compatibility are chosen together.

```lean
public noncomputable def etaleInverseImageSectionsComparison
    (B : BigEtaleSite.{u}) (S : B.Scheme) :
    { e : ∀ X : BigEtaleOver B S.obj S.property,
        (bigEtaleToSmallEtaleMorphism B S.obj S.property).inverseImage ⋙
          (sheafSections (BigEtaleOver.topology B S.obj S.property)
            (Type (u + 1))).obj (Opposite.op X) ≅
        (smallEtaleBaseChange B X.hom).sheafPullback
            (Type (u + 1))
            (SmallEtale.topology B S.obj S.property)
            (SmallEtale.topology B X.left.obj X.left.property) ⋙
          Sheaf.Γ (SmallEtale.topology B X.left.obj X.left.property)
            (Type (u + 1)) //
      ∀ {X Y : BigEtaleOver B S.obj S.property} (g : Y ⟶ X)
        (F : Sheaf (SmallEtale.topology B S.obj S.property) (Type (u + 1))),
        (e X).hom.app F ≫ etalePullbackSectionsRestriction B S g F =
          ((bigEtaleToSmallEtaleMorphism B S.obj S.property).inverseImage.obj F).obj.map g.op ≫
            (e Y).hom.app F }
```

**`AlgebraicGeometry.etaleInverseImageSectionsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtalePullbackSections.lean, line 327](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtalePullbackSections.lean#L327). The attribute's comment: “pullback\_formula”.

> **Stacks 09XN, pullback formula (étale case).** For a sheaf `F` on the small étale site of
> `S` and a scheme `f : X ⟶ S` over `S`, the sections of `π_S⁻¹F` at `X` are the global sections
> of the small étale pullback `f⁻¹F`, naturally in `F`. Restriction in `X` is recorded by
> `AlgebraicGeometry.etaleInverseImageSectionsIso_naturality`.

```lean
public noncomputable def etaleInverseImageSectionsIso
    (B : BigEtaleSite.{u}) (S : B.Scheme) (X : BigEtaleOver B S.obj S.property) :
    (bigEtaleToSmallEtaleMorphism B S.obj S.property).inverseImage ⋙
      (sheafSections (BigEtaleOver.topology B S.obj S.property)
        (Type (u + 1))).obj (Opposite.op X) ≅
    (smallEtaleBaseChange B X.hom).sheafPullback
        (Type (u + 1))
        (SmallEtale.topology B S.obj S.property)
        (SmallEtale.topology B X.left.obj X.left.property) ⋙
      Sheaf.Γ (SmallEtale.topology B X.left.obj X.left.property)
        (Type (u + 1))
```

**`AlgebraicGeometry.smallSiteInverseImage_sections_and_isSheaf_fpqc`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/SmallSitePullbackSectionsAndFpqcSheaf.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/SmallSitePullbackSectionsAndFpqcSheaf.lean#L63).

> **Stacks 09XN.** Let `S` be a scheme, let `τ` be the Zariski or the étale topology and let
> `π_S : (Sch/S)_τ ⟶ S_τ` be the projection from the big `τ`-topos over `S` to the small
> `τ`-topos of `S`. For a sheaf `F` on the small `τ`-site of `S`:
>
> 1. the sections of `π_S⁻¹F` over a scheme `f : X ⟶ S` over `S` are the global sections on the
>    small `τ`-site of `X` of the small-site pullback `f⁻¹F`, naturally in `F` and compatibly
>    with restriction along any morphism of schemes over `S`;
> 2. the presheaf underlying `π_S⁻¹F` is a sheaf for the fpqc topology on the big `τ`-site
>    over `S`.
>
> The first component of the conjunction is the Zariski case, the second the étale case; the two
> are the source's two values of `τ`, which are unrelated site structures here. Within each case
> the sections formula is `AlgebraicGeometry.zariskiInverseImageSectionsComparison` resp.
> `AlgebraicGeometry.etaleInverseImageSectionsComparison` — the family of comparison isomorphisms
> together with its compatibility with restriction — and the fpqc sheaf condition is
> `AlgebraicGeometry.smallZariskiProjection_inverseImage_isSheaf_fpqc` resp.
> `AlgebraicGeometry.bigEtaleToSmallEtale_inverseImage_isSheaf_fpqc`.

```lean
public noncomputable def smallSiteInverseImage_sections_and_isSheaf_fpqc :
    (∀ (B : BigZariskiSite.{u}) (S : B.Schemes),
        { e : ∀ X : BigZariskiOver B S.obj S.property,
            (smallZariskiProjection B S).inverseImage ⋙
              (sheafSections (BigZariskiOver.topology B S.obj S.property)
                (Type (u + 1))).obj (Opposite.op X) ≅
            (smallZariskiBaseChange B X.hom).sheafPullback
                (Type (u + 1))
                (SmallZariski.topology B S.obj S.property)
                (SmallZariski.topology B X.left.obj X.left.property) ⋙
              Sheaf.Γ (SmallZariski.topology B X.left.obj X.left.property)
                (Type (u + 1)) //
          (∀ {X Y : BigZariskiOver B S.obj S.property} (g : Y ⟶ X)
              (F : Sheaf (SmallZariski.topology B S.obj S.property) (Type (u + 1))),
              (e X).hom.app F ≫ zariskiPullbackSectionsRestriction B S g F =
                ((smallZariskiProjection B S).inverseImage.obj F).obj.map g.op ≫
                  (e Y).hom.app F) ∧
            ∀ F : Sheaf (SmallZariski.topology B S.obj S.property) (Type (u + 1)),
              Presheaf.IsSheaf
                ((Scheme.fpqcPrecoverage.comap
                  (BigZariskiOver.toScheme B S.obj S.property)).toGrothendieck)
                ((smallZariskiProjection B S).inverseImage.obj F).obj }) ×'
    ∀ (B : BigEtaleSite.{u}) (S : B.Scheme),
      { e : ∀ X : BigEtaleOver B S.obj S.property,
          (bigEtaleToSmallEtaleMorphism B S.obj S.property).inverseImage ⋙
            (sheafSections (BigEtaleOver.topology B S.obj S.property)
              (Type (u + 1))).obj (Opposite.op X) ≅
          (smallEtaleBaseChange B X.hom).sheafPullback
              (Type (u + 1))
              (SmallEtale.topology B S.obj S.property)
              (SmallEtale.topology B X.left.obj X.left.property) ⋙
            Sheaf.Γ (SmallEtale.topology B X.left.obj X.left.property)
              (Type (u + 1)) //
        (∀ {X Y : BigEtaleOver B S.obj S.property} (g : Y ⟶ X)
            (F : Sheaf (SmallEtale.topology B S.obj S.property) (Type (u + 1))),
            (e X).hom.app F ≫ etalePullbackSectionsRestriction B S g F =
              ((bigEtaleToSmallEtaleMorphism B S.obj S.property).inverseImage.obj F).obj.map
                  g.op ≫
                (e Y).hom.app F) ∧
          ∀ F : Sheaf (SmallEtale.topology B S.obj S.property) (Type (u + 1)),
            Presheaf.IsSheaf
              ((Scheme.fpqcPrecoverage.comap
                (BigEtaleOver.toScheme B S.obj S.property)).toGrothendieck)
              ((bigEtaleToSmallEtaleMorphism B S.obj S.property).inverseImage.obj F).obj }
```

## Tag 0A3H, a lemma

[Tag 0A3H](https://stacks.math.columbia.edu/tag/0A3H) in the Stacks Project.

**`Stacks.EtaleCohomology.isIso_globalSectionsSmallEtaleInverseImage_of_flat_quasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FlatSectionsCanonical.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FlatSectionsCanonical.lean#L60). The attribute's comment: “the form the source asserts: the canonical comparison on global sections, rather than a bare isomorphism of global-sections functors”.

> **Stacks Project, Tag 0A3H.** For `f : T ⟶ S` flat and quasi-compact with geometrically
> connected fibres, the *canonical* comparison `Γ(S, F) ⟶ Γ(T, f⁻¹F)` is an isomorphism for every
> sheaf of sets `F` on the small étale site of `S`, naturally in `F`. This is the form in which
> the source asserts the tag — it writes `Γ(S, F) = Γ(T, f⁻¹F)` for the canonical map, and proves
> that map injective and surjective — and it is stronger than the bare existence of an isomorphism
> of global-sections functors, which would not say that the isomorphism is restriction of
> sections.

```lean
public theorem isIso_globalSectionsSmallEtaleInverseImage_of_flat_quasiCompact
    {T S : Scheme.{u}} (f : T ⟶ S) [Flat f] [QuasiCompact f] [GeometricallyConnected f] :
    IsIso (globalSectionsSmallEtaleInverseImage.{u, v} f)
```

**`Stacks.EtaleCohomology.globalSectionsSmallEtaleInverseImageIso_of_flat_of_quasiCompact`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FlatSectionsCanonical.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FlatSectionsCanonical.lean#L73). The attribute's comment: “the natural isomorphism of global-sections functors, with no hypothesis beyond the source's”.

> **Stacks Project, Tag 0A3H.** Pullback along a flat quasi-compact morphism with
> geometrically connected fibres preserves global sections of every sheaf of sets on the small
> étale site, naturally in the sheaf. The isomorphism is the canonical comparison, which
> `Stacks.EtaleCohomology.isIso_globalSectionsSmallEtaleInverseImage_of_flat_quasiCompact`
> inverts.

```lean
public def globalSectionsSmallEtaleInverseImageIso_of_flat_of_quasiCompact
    {T S : Scheme.{u}} (f : T ⟶ S) [Flat f] [QuasiCompact f] [GeometricallyConnected f] :
    Sheaf.Γ (smallEtaleTopology S) (Type (max (u + 1) v)) ≅
      smallEtaleInverseImage.{u, v} f ⋙
        Sheaf.Γ (smallEtaleTopology T) (Type (max (u + 1) v))
```

## Tag 0EZK, a lemma

[Tag 0EZK](https://stacks.math.columbia.edu/tag/0EZK) in the Stacks Project.

**`Stacks.EtaleCohomology.isIso_globalSectionsSmallEtaleInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SubmersiveSections.lean, line 2480](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SubmersiveSections.lean#L2480). The attribute's comment: “corrected: Stacks erratum. The tag in the form the source asserts it, about the canonical comparison rather than a bare isomorphism of global-sections functors. The tag is false with only `f` submersive; see the counterexample in the docstring of globalSectionsSmallEtaleInverseImageIso”.

> **Stacks Project, Tag 0EZK.** For `f` universally submersive with geometrically connected
> fibres, the *canonical* comparison `Γ(S, F) ⟶ Γ(X, f⁻¹F)` is an isomorphism, naturally in the
> sheaf `F`. This is the form in which the source asserts the tag — it says "there is a canonical
> map `Γ(S, F) → Γ(X, f⁻¹F)`" and then that it is injective and surjective — and it is strictly
> stronger than the bare existence of an isomorphism of global-sections functors, which would not
> say that the isomorphism is restriction of sections.
>
> **Stacks erratum.** The hypothesis stated here is the corrected one;
> `Stacks.EtaleCohomology.globalSectionsSmallEtaleInverseImageIso` carries the characteristic-`2`
> counterexample to the tag as the source writes it.

```lean
public theorem isIso_globalSectionsSmallEtaleInverseImage
    {X S : Scheme.{u}} (f : X ⟶ S)
    (hsub : (topologically @Topology.IsQuotientMap :
      MorphismProperty Scheme.{u}).universally f)
    [GeometricallyConnected f] :
    IsIso (globalSectionsSmallEtaleInverseImage.{u, v} f)
```

**`Stacks.EtaleCohomology.globalSectionsSmallEtaleInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SubmersiveSections.lean, line 2524](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SubmersiveSections.lean#L2524). The attribute's comment: “corrected: Stacks erratum. The tag is false with only `f` submersive, since the proof's reduction is an etale base change and submersivity does not survive one; universal submersivity is assumed instead. Counterexample in characteristic 2: the homeomorphism Spec k[t,1/t] -> Spec \{g : g(0) = g(1)} and the double cover T = Spec A[z]/(z^2 + z + a) with a = t^2 + t, for which the sections downstairs are empty while there are two upstairs; see this declaration's docstring”.

> **Stacks Project, Tag 0EZK.** Pullback along a universally submersive morphism with
> geometrically connected fibres preserves global sections of every sheaf of sets on the small
> étale site, naturally in the sheaf. The isomorphism is the canonical comparison, which
> `Stacks.EtaleCohomology.isIso_globalSectionsSmallEtaleInverseImage` inverts.
>
> **Stacks erratum.** The hypothesis stated here is the corrected
> one. As the source writes the tag it asks only that `f` be submersive, and in that form the
> statement is false: the proof reduces along an étale base change, and submersivity does not
> survive one. The counterexample lives in characteristic `2`. Let `k` be a field of
> characteristic `2`, let `A = {g ∈ k[t] ∣ g(0) = g(1)}` be the node — the affine line with the
> two points `t = 0` and `t = 1` glued — let `B = k[t, 1/t]` be the affine line with `t = 0`
> removed, and let `f : Spec B ⟶ Spec A` be the homeomorphism described in the Stacks proof: it
> is bijective because the node has already glued the removed point `t = 0` to the surviving
> point `t = 1`. Take `F = h_T`, the functor of points of `T = Spec A[z]/(z² + z + a)` with
> `a = t² + t`, which is the connected étale double cover of `Spec A` — étale because the
> derivative of `z² + z + a` in `z` is the unit `1` in characteristic `2`. Then `Γ(S, F)` is
> EMPTY: a root of `z² + z + a` in `k[t]` is `t` or `t + 1`, and neither takes the same value at
> `0` and at `1`, so neither lies in `A`. But `Γ(X, f⁻¹F)` has TWO elements, `t` and `t + 1`,
> both of which lie in `B`. So the claimed bijection `Γ(S, F) = Γ(X, f⁻¹F)` cannot hold, and the
> submersive hypothesis alone does not suffice. Universal submersivity — equivalently,
> submersivity after every étale base change — is what the argument uses and what is assumed
> here; it is part of the corrected statement, not a strengthening of it.

```lean
public def globalSectionsSmallEtaleInverseImageIso
    {X S : Scheme.{u}} (f : X ⟶ S)
    (hsub : (topologically @Topology.IsQuotientMap :
      MorphismProperty Scheme.{u}).universally f)
    [GeometricallyConnected f] :
    Sheaf.Γ (smallEtaleTopology S) (Type (max (u + 1) v)) ≅
      smallEtaleInverseImage f ⋙
        Sheaf.Γ (smallEtaleTopology X) (Type (max (u + 1) v))
```

**`Stacks.EtaleCohomology.isIso_globalSectionsSmallEtaleInverseImage_of_etaleBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SubmersiveSectionsEtaleBaseChange.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SubmersiveSectionsEtaleBaseChange.lean#L51). The attribute's comment: “corrected: Stacks erratum: f submersive after every etale base change, the exact corrected hypothesis; the source's plain submersivity of f is not enough, see the counterexample in the docstring of globalSectionsSmallEtaleInverseImageIso. The universally submersive special case is isIso\_globalSectionsSmallEtaleInverseImage”.

> **Stacks Project, Tag 0EZK.** Let `f : X ⟶ S` have geometrically connected fibres and be
> submersive after every étale base change: for every étale `g : V ⟶ S` the projection
> `V ×_S X ⟶ V` is a quotient map. Then the canonical comparison `Γ(S, F) ⟶ Γ(X, f⁻¹F)` is an
> isomorphism, naturally in the sheaf `F` on the small étale site of `S`.

```lean
public theorem isIso_globalSectionsSmallEtaleInverseImage_of_etaleBaseChange
    {X S : Scheme.{u}} (f : X ⟶ S)
    (hsub : ∀ ⦃V : Scheme.{u}⦄ (g : V ⟶ S) [Etale g],
      Topology.IsQuotientMap (pullback.fst g f))
    [GeometricallyConnected f] :
    IsIso (globalSectionsSmallEtaleInverseImage.{u, v} f)
```

**`Stacks.EtaleCohomology.globalSectionsSmallEtaleInverseImageIsoOfEtaleBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SubmersiveSectionsEtaleBaseChange.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SubmersiveSectionsEtaleBaseChange.lean#L77). The attribute's comment: “corrected: Stacks erratum: f submersive after every etale base change, the exact corrected hypothesis; the source's plain submersivity of f is not enough, see the counterexample in the docstring of globalSectionsSmallEtaleInverseImageIso. The universally submersive special case is globalSectionsSmallEtaleInverseImageIso”.

> **Stacks Project, Tag 0EZK.** Pullback along a morphism with geometrically connected fibres
> that is submersive after every étale base change preserves global sections of every sheaf of
> sets on the small étale site, naturally in the sheaf; the isomorphism is the canonical
> comparison `Γ(S, F) ⟶ Γ(X, f⁻¹F)`.

```lean
public noncomputable def globalSectionsSmallEtaleInverseImageIsoOfEtaleBaseChange
    {X S : Scheme.{u}} (f : X ⟶ S)
    (hsub : ∀ ⦃V : Scheme.{u}⦄ (g : V ⟶ S) [Etale g],
      Topology.IsQuotientMap (pullback.fst g f))
    [GeometricallyConnected f] :
    Sheaf.Γ (smallEtaleTopology S) (Type (max (u + 1) v)) ≅
      smallEtaleInverseImage f ⋙
        Sheaf.Γ (smallEtaleTopology X) (Type (max (u + 1) v))
```

## Tag 0A3I, a lemma

[Tag 0A3I](https://stacks.math.columbia.edu/tag/0A3I) in the Stacks Project.

**`Stacks.EtaleCohomology.globalSectionsSmallEtaleInverseImageIso_of_isSepClosed`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SeparablyClosedBaseFieldSections.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SeparablyClosedBaseFieldSections.lean#L41). References: SGA 4 XVI (1.5), “partial”.

> For a scheme `S` over a separably closed field `k` and any field extension `K/k`, pullback
> along the projection `S ×_{Spec k} Spec K ⟶ S` preserves global sections of every sheaf of sets on
> the small étale site, naturally in the sheaf.

```lean
public def globalSectionsSmallEtaleInverseImageIso_of_isSepClosed
    (k K : Type u) [Field k] [IsSepClosed k] [Field K] [Algebra k K]
    {S : Scheme.{u}} (f : S ⟶ Spec (.of k)) :
    Sheaf.Γ (smallEtaleTopology S) (Type (max (u + 1) v)) ≅
      smallEtaleInverseImage.{u, v}
          (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))) ⋙
        Sheaf.Γ
          (smallEtaleTopology (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K)))))
          (Type (max (u + 1) v))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.39, Tag 09XL](https://stacks.math.columbia.edu/tag/09XL)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
