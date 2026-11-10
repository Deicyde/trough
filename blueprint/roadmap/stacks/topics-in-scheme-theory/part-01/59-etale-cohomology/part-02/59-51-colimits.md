---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.inverseImageSystem, Stacks.EtaleCohomology.EtaleSheafSystem, Stacks.EtaleCohomology.affineEtaleSiteColimit, Stacks.EtaleCohomology.affineEtaleSiteColimit_level_cover, Stacks.EtaleCohomology.affineEtaleSiteColimit_levelEquiv_isDenseSubsite, Stacks.EtaleCohomology.affineEtaleSiteColimit_levelToSmallEtale_isContinuous, Stacks.EtaleCohomology.affineEtaleSiteColimit_levelToSmallEtale_sheafEquiv, Stacks.EtaleCohomology.affineEtaleSiteColimit_obj_descends
statement: formalized
proof: formalized
---

# 59.51 Colimits

Section 59.51 of the Stacks Project, [Tag 03Q4](https://stacks.math.columbia.edu/tag/03Q4). 10 tags here are carried by 40 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EZL, a definition

[Tag 0EZL](https://stacks.math.columbia.edu/tag/0EZL) in the Stacks Project.

**`Stacks.EtaleCohomology.inverseImageSystem`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/InverseImageSystem.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/InverseImageSystem.lean#L111). The attribute's comment: “the system of INVERSE IMAGES of a single sheaf: for a cocone on the inverse system with vertex `S` and an abelian sheaf on the small etale site of `S`, the system `𝒢_i = (D_i ⟶ S)^{-1} ℱ` together with its cocycle condition, constructed and not assumed. Coefficients are `Ab.{u + 1}` on Mathlib's `Scheme.smallEtaleTopology`, which is where the inverse image of abelian sheaves exists unconditionally”.

> **The system of inverse images of a single sheaf, constructed.** Let `D` be an inverse system
> of schemes, let `d` be a cocone on it with vertex `S` — so every `D_i` carries a morphism
> `D_i ⟶ S` compatible with the transitions — and let `ℱ` be an abelian sheaf on the small étale
> site of `S`. The inverse images `(D_i ⟶ S)^{-1} ℱ`, with the transition maps supplied by
> `coconeInverseImageComp`, form a system of sheaves on `D` in the sense of Stacks 0EZL.
>
> The cocycle condition is the associativity pentagon
> `smallEtalePullbackAbCompIso'_assoc` of the inverse-image comparison, at the three morphisms
> `D_i ⟶ D_j ⟶ D_k ⟶ S`.

```lean
def inverseImageSystem : EtaleSheafSystem D Ab.{u + 1}
```

**`Stacks.EtaleCohomology.EtaleSheafSystem`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/SheafSystems.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/SheafSystems.lean#L110).

> A *system of sheaves* on an inverse system of schemes `D`: a sheaf on the small étale site of
> each member, together with a map from the inverse image of the sheaf at an index to the sheaf at
> any larger index, compatible with composition of the transition morphisms through the canonical
> comparison `Stacks.EtaleCohomology.systemPullbackComp`.

```lean
public structure EtaleSheafSystem
```

## Tag 0EYL, a lemma

[Tag 0EYL](https://stacks.math.columbia.edu/tag/0EYL) in the Stacks Project.

**`Stacks.EtaleCohomology.affineEtaleSiteColimit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/AffineEtaleSites/ColimitSite.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/AffineEtaleSites/ColimitSite.lean#L40). The attribute's comment: “canonical site system”.

> **Stacks 0EYL.** Let `I` be a directed set, let `(X_i, f_{i'i})` be an inverse system of
> schemes over `I` with affine transition morphisms and let `X = lim X_i`.  Then
> `X_{affine, étale} = colim (X_i)_{affine, étale}` as sites in the sense of Stacks 09YL.

```lean
public noncomputable def affineEtaleSiteColimit (hc : IsLimit c)
    [∀ {i j : Iᵒᵖ} (a : i ⟶ j), IsAffineHom (D.map a)] :
    AffineEtaleSiteColimit D c B hD hX
```

**`Stacks.EtaleCohomology.affineEtaleSiteColimit_level_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/AffineEtaleSites/ColimitSite.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/AffineEtaleSites/ColimitSite.lean#L88). The attribute's comment: “level coverings”.

> The level equivalences identify the Grothendieck topologies: a presieve is covering at a
> stage exactly when its image generates a covering sieve of the corresponding affine étale site.
> Finiteness is not imposed here, since an equivalence can identify distinct isomorphic source
> objects and need not reflect finiteness of a particular presieve.

```lean
public theorem affineEtaleSiteColimit_level_cover
    (i : (affineEtaleSiteColimit D c B hD hX hc).system.I)
    (Y : (affineEtaleSiteColimit D c B hD hX hc).system.C i) (R : Presieve Y) :
    R ∈ ((affineEtaleSiteColimit D c B hD hX hc).system.J i).toPrecoverage Y ↔
      R.map ((affineEtaleSiteColimit D c B hD hX hc).levelEquiv i).functor ∈
        (AlgebraicGeometry.SmallAffineEtale.topology B
          (D.obj ((affineEtaleSiteColimit D c B hD hX hc).indexEquiv.functor.obj i))
          (hD ((affineEtaleSiteColimit D c B hD hX hc).indexEquiv.functor.obj
            i))).toPrecoverage
          (((affineEtaleSiteColimit D c B hD hX hc).levelEquiv i).functor.obj Y)
```

**`Stacks.EtaleCohomology.affineEtaleSiteColimit_levelEquiv_isDenseSubsite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/AffineEtaleSites/ColimitSite.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/AffineEtaleSites/ColimitSite.lean#L112). The attribute's comment: “level coverings, as a dense subsite”.

> **The level equivalences identify the Grothendieck topologies, in the form of a dense
> subsite.** The topology of a level is the topology induced on the category of representatives by
> the level equivalence, so that equivalence's functor is a dense subsite of the small affine étale
> site of the corresponding `X_i`.
>
> This is `affineEtaleSiteColimit_level_cover` in the form typeclass inference consumes.  The
> covering correspondence is a statement about presieves; transporting sheaves across a level needs
> continuity of the functor as an *instance*, and `CategoryTheory.Functor.IsDenseSubsite` carries
> both that and the cover-lifting direction.  Nothing is asserted beyond the covering
> correspondence: the content is that it holds for sieves at every object, which is what makes the
> induced topology the topology of the level.

```lean
public theorem affineEtaleSiteColimit_levelEquiv_isDenseSubsite
    (i : (affineEtaleSiteColimit D c B hD hX hc).system.I) :
    ((affineEtaleSiteColimit D c B hD hX hc).levelEquiv i).functor.IsDenseSubsite
      ((affineEtaleSiteColimit D c B hD hX hc).system.J i)
      (AlgebraicGeometry.SmallAffineEtale.topology B
        (D.obj ((affineEtaleSiteColimit D c B hD hX hc).indexEquiv.functor.obj i))
        (hD ((affineEtaleSiteColimit D c B hD hX hc).indexEquiv.functor.obj i)))
```

**`Stacks.EtaleCohomology.affineEtaleSiteColimit_levelToSmallEtale_isContinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/AffineEtaleSites/ColimitSite.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/AffineEtaleSites/ColimitSite.lean#L133). The attribute's comment: “levels as morphisms of sites to the small étale sites”.

> **A level of the system, carried into the small étale site of its scheme, is a morphism of
> sites.** The composite of the level equivalence with the inclusion of Stacks 04HR is continuous
> from the topology of the level to the small étale topology of `X_i`.
>
> This is the level-side counterpart of
> `Stacks.EtaleCohomology.AffineLimitCohomology.isContinuous_limitToSmallEtale`, and unlike that one
> it is not a universe raising followed by 04HR: a level of this system is a category of
> representatives, equivalent to the small affine étale site of `X_i` but not equal to it, so the
> first factor is the level equivalence and its continuity is
> `affineEtaleSiteColimit_levelEquiv_isDenseSubsite`.  Without this a sheaf on the small étale site
> of `X_i` cannot be read on the level at all.

```lean
public theorem affineEtaleSiteColimit_levelToSmallEtale_isContinuous
    (i : (affineEtaleSiteColimit D c B hD hX hc).system.I) :
    (((affineEtaleSiteColimit D c B hD hX hc).levelEquiv i).functor ⋙
        AlgebraicGeometry.SmallAffineEtale.inclusion B
          (D.obj ((affineEtaleSiteColimit D c B hD hX hc).indexEquiv.functor.obj i))
          (hD ((affineEtaleSiteColimit D c B hD hX hc).indexEquiv.functor.obj
            i))).IsContinuous
      ((affineEtaleSiteColimit D c B hD hX hc).system.J i)
      (AlgebraicGeometry.SmallEtale.topology B
        (D.obj ((affineEtaleSiteColimit D c B hD hX hc).indexEquiv.functor.obj i))
        (hD ((affineEtaleSiteColimit D c B hD hX hc).indexEquiv.functor.obj i)))
```

**`Stacks.EtaleCohomology.affineEtaleSiteColimit_levelToSmallEtale_sheafEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/AffineEtaleSites/ColimitSite.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/AffineEtaleSites/ColimitSite.lean#L155). The attribute's comment: “sheaves of a level are sheaves of the small étale site of its scheme”.

> **Restriction of sheaves of sets from the small étale site of `X_i` to a level is an
> equivalence.** Both factors of the crossing are: the level equivalence by
> `affineEtaleSiteColimit_levelEquiv_isDenseSubsite`, and the inclusion of the small affine étale
> site by Stacks 04HR.
>
> This says that reading a sheaf of a level as the restriction of a sheaf on the small étale site of
> `X_i` is no restriction on the level sheaf: every one of them is isomorphic to such a restriction,
> and every map of them to a map of those.

```lean
public theorem affineEtaleSiteColimit_levelToSmallEtale_sheafEquiv
    (i : (affineEtaleSiteColimit D c B hD hX hc).system.I) :
    letI := affineEtaleSiteColimit_levelToSmallEtale_isContinuous D c B hD hX hc i
    ((((affineEtaleSiteColimit D c B hD hX hc).levelEquiv i).functor ⋙
      AlgebraicGeometry.SmallAffineEtale.inclusion B
        (D.obj ((affineEtaleSiteColimit D c B hD hX hc).indexEquiv.functor.obj i))
        (hD ((affineEtaleSiteColimit D c B hD hX hc).indexEquiv.functor.obj
          i))).sheafPushforwardContinuous (Type (max u v + 1))
      ((affineEtaleSiteColimit D c B hD hX hc).system.J i)
      (AlgebraicGeometry.SmallEtale.topology B
        (D.obj ((affineEtaleSiteColimit D c B hD hX hc).indexEquiv.functor.obj i))
        (hD ((affineEtaleSiteColimit D c B hD hX hc).indexEquiv.functor.obj
          i)))).IsEquivalence
```

**`Stacks.EtaleCohomology.affineEtaleSiteColimit_obj_descends`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/AffineEtaleSites/ColimitSite.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/AffineEtaleSites/ColimitSite.lean#L180). The attribute's comment: “objects”.

> Every affine étale object over the limit descends to a finite stage.

```lean
public theorem affineEtaleSiteColimit_obj_descends
    (Z : AlgebraicGeometry.SmallAffineEtale B c.pt hX) :
    ∃ (i : (affineEtaleSiteColimit D c B hD hX hc).system.I)
      (Y : (affineEtaleSiteColimit D c B hD hX hc).system.C i),
      ((affineEtaleSiteColimit D c B hD hX hc).toLimit i).obj Y = Z
```

**`Stacks.EtaleCohomology.affineEtaleSiteColimit_hom_descends`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/AffineEtaleSites/ColimitSite.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/AffineEtaleSites/ColimitSite.lean#L190). The attribute's comment: “morphisms”.

> Every morphism between objects descended from one stage descends after increasing the
> stage.

```lean
public theorem affineEtaleSiteColimit_hom_descends
    (i : (affineEtaleSiteColimit D c B hD hX hc).system.I)
    (X Y : (affineEtaleSiteColimit D c B hD hX hc).system.C i)
    (f : ((affineEtaleSiteColimit D c B hD hX hc).toLimit i).obj X ⟶
      ((affineEtaleSiteColimit D c B hD hX hc).toLimit i).obj Y) :
    ∃ (j : (affineEtaleSiteColimit D c B hD hX hc).system.I) (a : j ⟶ i)
      (g : ((affineEtaleSiteColimit D c B hD hX hc).system.u a).obj X ⟶
        ((affineEtaleSiteColimit D c B hD hX hc).system.u a).obj Y),
      ((affineEtaleSiteColimit D c B hD hX hc).toLimit j).map g =
        eqToHom (Functor.congr_obj
          ((affineEtaleSiteColimit D c B hD hX hc).toLimit_transition a) X) ≫ f ≫
          eqToHom (Functor.congr_obj
            ((affineEtaleSiteColimit D c B hD hX hc).toLimit_transition a) Y).symm
```

**`Stacks.EtaleCohomology.affineEtaleSiteColimit_hom_eventually_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/AffineEtaleSites/ColimitSite.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/AffineEtaleSites/ColimitSite.lean#L334). The attribute's comment: “faithfulness”.

> Two morphisms that agree over the limit agree after increasing the stage.

```lean
public theorem affineEtaleSiteColimit_hom_eventually_eq
    (i : (affineEtaleSiteColimit D c B hD hX hc).system.I)
    (X Y : (affineEtaleSiteColimit D c B hD hX hc).system.C i)
    (f g : X ⟶ Y)
    (hfg : ((affineEtaleSiteColimit D c B hD hX hc).toLimit i).map f =
      ((affineEtaleSiteColimit D c B hD hX hc).toLimit i).map g) :
    ∃ (j : (affineEtaleSiteColimit D c B hD hX hc).system.I) (a : j ⟶ i),
      ((affineEtaleSiteColimit D c B hD hX hc).system.u a).map f =
        ((affineEtaleSiteColimit D c B hD hX hc).system.u a).map g
```

**`Stacks.EtaleCohomology.affineEtaleSiteColimit_mem_precoverage_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/AffineEtaleSites/ColimitSite.lean, line 569](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/AffineEtaleSites/ColimitSite.lean#L569). The attribute's comment: “coverings”.

> Coverings of the small affine étale site of the limit are exactly the images of finite
> coverings from a stage.

```lean
public theorem affineEtaleSiteColimit_mem_precoverage_iff
    (Z : AlgebraicGeometry.SmallAffineEtale B c.pt hX) (R : Presieve Z) :
    R ∈ AlgebraicGeometry.SmallAffineEtale.precoverage B c.pt hX Z ↔
      ∃ (i : (affineEtaleSiteColimit D c B hD hX hc).system.I)
        (Y : (affineEtaleSiteColimit D c B hD hX hc).system.C i)
        (h : ((affineEtaleSiteColimit D c B hD hX hc).toLimit i).obj Y = Z)
        (S : Presieve Y),
        S ∈ ((affineEtaleSiteColimit D c B hD hX hc).system.J i).toPrecoverage Y ∧
          S ∈ Precoverage.finite ((affineEtaleSiteColimit D c B hD hX hc).system.C i) Y ∧
          R = h ▸ S.map ((affineEtaleSiteColimit D c B hD hX hc).toLimit i)
```

**`Stacks.EtaleCohomology.affineEtaleSiteColimit_isColimitPrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/AffineEtaleSites/ColimitSite.lean, line 626](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/AffineEtaleSites/ColimitSite.lean#L626). The attribute's comment: “colimit site”.

> **Stacks 0EYL**, the clause "as sites in the sense of Stacks 09YL". The standard étale
> precoverage of the small affine étale site of the limit `X = lim X_i` *is* the colimit
> precoverage that Stacks 09YL produces from the canonical system: its coverings are exactly the
> images of the finite coverings of the stages, and it therefore satisfies the three axioms of a
> site in the sense of Stacks 00VH — a one-element family given by an isomorphism is a covering,
> coverings are stable under refinement by coverings, and the fibre products of a covering along
> any morphism exist and again form a covering.

```lean
public theorem affineEtaleSiteColimit_isColimitPrecoverage :
    (∀ (Z : AlgebraicGeometry.SmallAffineEtale B c.pt hX) (R : Presieve Z),
        R ∈ AlgebraicGeometry.SmallAffineEtale.precoverage B c.pt hX Z ↔
          ∃ (i : (affineEtaleSiteColimit D c B hD hX hc).system.I)
            (Y : (affineEtaleSiteColimit D c B hD hX hc).system.C i)
            (h : ((affineEtaleSiteColimit D c B hD hX hc).toLimit i).obj Y = Z)
            (S : Presieve Y),
            S ∈ ((affineEtaleSiteColimit D c B hD hX hc).system.J i).toPrecoverage Y ∧
              S ∈ Precoverage.finite
                  ((affineEtaleSiteColimit D c B hD hX hc).system.C i) Y ∧
                R = h ▸ S.map ((affineEtaleSiteColimit D c B hD hX hc).toLimit i)) ∧
      (AlgebraicGeometry.SmallAffineEtale.precoverage B c.pt hX).HasIsos ∧
      (∀ (Z : AlgebraicGeometry.SmallAffineEtale B c.pt hX) (R : Presieve Z)
          (T : ∀ ⦃Y : AlgebraicGeometry.SmallAffineEtale B c.pt hX⦄ (f : Y ⟶ Z),
            R f → Presieve Y),
          R ∈ AlgebraicGeometry.SmallAffineEtale.precoverage B c.pt hX Z →
            (∀ ⦃Y : AlgebraicGeometry.SmallAffineEtale B c.pt hX⦄ (f : Y ⟶ Z) (hf : R f),
                T f hf ∈ AlgebraicGeometry.SmallAffineEtale.precoverage B c.pt hX Y) →
              R.bind T ∈ AlgebraicGeometry.SmallAffineEtale.precoverage B c.pt hX Z) ∧
        ∃ _ : (AlgebraicGeometry.SmallAffineEtale.precoverage B c.pt hX).HasPullbacks,
          ∀ (Z W : AlgebraicGeometry.SmallAffineEtale B c.pt hX) (f : W ⟶ Z)
              (R : Presieve Z) [R.HasPullbacks f],
            R ∈ AlgebraicGeometry.SmallAffineEtale.precoverage B c.pt hX Z →
              R.pullbackArrows f ∈
                AlgebraicGeometry.SmallAffineEtale.precoverage B c.pt hX W
```

**`AlgebraicGeometry.smallEtaleStagesCoveringsRefine_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/SmallEtaleCoveringsRefine.lean, line 382](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/SmallEtaleCoveringsRefine.lean#L382). The attribute's comment: “coverings of the final object, for the small étale site”.

> **Stacks 0EYL for the small étale site.** Let `X = lim X_i` be the limit of a directed
> inverse system of quasi-compact, quasi-separated schemes with affine transition morphisms inside
> a big étale site. Every covering of the final object of the small étale site of `X` is refined
> by the inverse image of a finite covering of the final object at some stage beyond a prescribed
> one.
>
> The hypotheses are the three geometric conditions the assertion needs and which
> `AlgebraicGeometry.SmallEtaleStagesCoveringsRefine`, a predicate on an arbitrary cone, does not
> itself carry: the cone is limiting, the transition morphisms are affine, and the stages are
> quasi-compact and quasi-separated. Quasi-compactness is not cosmetic: the conclusion demands a
> finite refining family, and over a vertex which is an infinite disjoint union the covering by
> the components admits none.

```lean
public theorem smallEtaleStagesCoveringsRefine_of_isLimit (hc : IsLimit c)
    (haff : ∀ {p q : Iᵒᵖ} (e : p ⟶ q), IsAffineHom (B.inclusion.map (Dg.map e)))
    (hqc : ∀ p : I, CompactSpace (Dg.obj (op p)).obj)
    (hqs : ∀ p : I, QuasiSeparatedSpace (Dg.obj (op p)).obj) :
    SmallEtaleStagesCoveringsRefine B Dg c hX
```

## Tag 09YQ, a theorem

[Tag 09YQ](https://stacks.math.columbia.edu/tag/09YQ) in the Stacks Project.

**`Stacks.EtaleCohomology.AffineLimitCohomology.transitionImage_isoLevelTerminal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/AffineEtaleCohomologyColimit.lean, line 444](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/AffineEtaleCohomologyColimit.lean#L444). The attribute's comment: “the affine case: the transition image of the terminal object `X_i` is the terminal object `X_j`, so the value of the cohomology diagram at `a : j ⟶ i` is the cohomology over `X_j`”.

> **Stacks 09YQ, the diagram values.** The transition image of `X_i` at a level `j` below `i`
> is `X_j`: the value of the cohomology diagram at `a : j ⟶ i` is the cohomology of `F_j` over the
> terminal object of the site of `X_j`, that is over `X_j` itself.

```lean
def transitionImage_isoLevelTerminal {i j : (sys D c B hD hX hc).I} (a : j ⟶ i) :
    ((sys D c B hD hX hc).u a).obj (levelTerminal D c B hD hX hc i) ≅
      levelTerminal D c B hD hX hc j
```

**`Stacks.EtaleCohomology.AffineLimitCohomology.toLimitImage_isoLimitTerminal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/AffineEtaleCohomologyColimit.lean, line 457](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/AffineEtaleCohomologyColimit.lean#L457). The attribute's comment: “the affine case: the image of the terminal object `X_i` in the site of the limit is the terminal object `X`, so the vertex of the cohomology cocone is the cohomology over `X`”.

> **Stacks 09YQ, the cocone vertex.** The image of `X_i` in the site of the limit is `X`: the
> vertex of the cohomology cocone is the cohomology of `𝒢` over the terminal object of the site of
> `X`, that is over `X` itself.

```lean
def toLimitImage_isoLimitTerminal (i : (sys D c B hD hX hc).I) :
    (toLimitSmall D c B hD hX hc i).obj (levelTerminal D c B hD hX hc i) ≅
      limitTerminal D c B hX hc
```

**`Stacks.EtaleCohomology.AffineLimitCohomology.etaleCohomologyColimit_isColimit_of_affine`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/AffineEtaleCohomologyColimit.lean, line 487](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/AffineEtaleCohomologyColimit.lean#L487). The attribute's comment: “the affine case: the schemes `X_i` of the system are affine, so that `X_i` is itself an object of its own small affine etale site and is the terminal one; the sites are the small AFFINE etale sites and the cohomology of THIS statement is the right-derived `sheafSections` of Stacks 09YP on them. The comparison across Stacks 04HR that turns those groups into the library's mainstream etale cohomology of a scheme is `Stacks.EtaleCohomology.AffineLimitCohomology.limitCohomologyFunctorIsoEtaleCohomology` at the limit and `...levelTerminalCohomologyIsoEtaleCohomology` at a level”.

> **Stacks 09YQ, the affine case.** Let `I` be a directed set, let `(X_i)` be an inverse system
> of *affine* schemes over `I` with affine transition morphisms, and let `X = lim X_i`. Let `F` be a
> system of abelian sheaves on the small affine etale sites of the `X_i`, let `𝒢` on the small
> affine etale site of `X` present the colimit `colim f_i^{-1} F_i`, and let `p` be a degree. Then
> `H^p(X, 𝒢)` is the filtered colimit, over the arrows `a : j ⟶ i`, of the groups `H^p(X_j, F_j)`:
> the canonical cocone is a colimit cocone.
>
> The base object is `levelTerminal i`, which is `X_i` (`levelTerminal_isTerminal`); its image in
> the site of the limit is `X` (`toLimitImage_isoLimitTerminal`) and its transition image at a
> level `j` is `X_j` (`transitionImage_isoLevelTerminal`), so the vertex and the values of the
> diagram are the cohomology groups of the schemes of the system.
>
> This is Stacks 09YP, applied to the colimit of sites of Stacks 0EYL through
> `mem_limitSitePrecoverage_iff` and the three descent clauses above.

```lean
def etaleCohomologyColimit_isColimit_of_affine
    (F : InverseSystemOfFiniteSites.AbelianSheafSystem.{v, v, max u v + 1, max u v + 1}
      (sys D c B hD hX hc))
    (𝒢 : Sheaf (limitSitePrecoverage D c B hX).toGrothendieck Ab.{max u v + 1})
    (ι : ∀ j, (F.obj j).obj ⟶ (toLimitSmall D c B hD hX hc j).op ⋙ 𝒢.obj)
    (hcolim : IsColimitPresentation.{v, v, max u v + 1, max u v + 1}
      (sys D c B hD hX hc) (toLimitSmall D c B hD hX hc)
      (toLimitSmall_transition D c B hD hX hc) (limitSitePrecoverage D c B hX) F 𝒢 ι)
    (i : (sys D c B hD hX hc).I) (p : ℕ)
    (E : CohomologyCocone.{v, v, max u v + 1, max u v + 1}
      (sys D c B hD hX hc) (toLimitSmall D c B hD hX hc)
      (toLimitSmall_transition D c B hD hX hc) (limitSitePrecoverage D c B hX) F 𝒢 ι i
      (levelTerminal D c B hD hX hc i) p) :
    IsColimit E.cocone
```

**`Stacks.EtaleCohomology.AffineLimitCohomology.etaleCohomologyColimit_isColimit_of_affine_colimitSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/AffineEtaleCohomologyColimit.lean, line 550](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/AffineEtaleCohomologyColimit.lean#L550). The attribute's comment: “the affine case with the colimit sheaf CONSTRUCTED: the sheaf `𝒢` presenting `colim f_i^{-1} F_i` on the site of the limit, its legs and its universal property are the left Kan extension of the system and are no longer hypotheses. The system `F` itself is still given, and the cohomology of THIS statement is the right-derived `sheafSections` of Stacks 09YP on the small AFFINE etale sites; `AffineLimitCohomology.etaleCohomologyColimit_isColimit_of_affine_etaleVertex` is the same colimit with its vertex the library's mainstream etale cohomology of the limit.”.

> **Stacks 09YQ in the affine case, with the colimit sheaf constructed.** Let `(X_i)` be an
> inverse system of affine schemes with affine transitions, `X = lim X_i`, and let `F` be a system
> of abelian sheaves on their small affine etale sites. Then
>
> `H^p(X, colim_i f_i^{-1} F_i) = colim_i H^p(X_i, F_i)`.
>
> This is `etaleCohomologyColimit_isColimit_of_affine` with the sheaf presenting the colimit, its
> legs and its universal property no longer hypotheses but the constructions `colimitSheaf`,
> `colimitSheafLegs` and `isColimitPresentation_colimitSheaf`.

```lean
def etaleCohomologyColimit_isColimit_of_affine_colimitSheaf
    (E : CohomologyCocone.{v, v, max u v + 1, max u v + 1} (sys D c B hD hX hc)
      (toLimitSmall D c B hD hX hc) (toLimitSmall_transition D c B hD hX hc)
      (limitSitePrecoverage D c B hX) F (colimitSheaf D c B hD hX hc F)
      (colimitSheafLegs D c B hD hX hc F) i (levelTerminal D c B hD hX hc i) p :=
      cohomologyCoconeOfColimitSheaf D c B hD hX hc F i p) :
    IsColimit E.cocone
```

**`Stacks.EtaleCohomology.QcqsLimitCohomology.etaleCohomologyColimit_isColimit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/QcqsEtaleCohomologyColimit.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/QcqsEtaleCohomologyColimit.lean#L233). The attribute's comment: “the general case of the levels: the schemes `X_i` are arbitrary — only the transition morphisms are affine — and the cohomology is taken over an arbitrary object `Z` of the small affine etale site of `X_i`, whose transition images and whose image in the site of the limit carry the groups of the diagram and the vertex. For an affine `X_i` the terminal object of that site is `X_i` itself and this specializes to the affine case already recorded in `Stacks.EtaleCohomology.AffineLimitCohomology`; for a merely quasi-compact and quasi-separated `X_i`, which is NOT an object of its own small affine etale site, the identification of this cohomology with `H^p(X_i, F_i)` is the Cech / Mayer-Vietoris descent along a finite affine cover and is NOT performed here — only the covering input is, in `exists_finite_jointlySurjective_smallAffineEtale`. The sites are the small AFFINE etale sites and the cohomology is the right-derived `sheafSections` of the weak-system Stacks 09YP on them, not the library's mainstream etale cohomology of a scheme, the comparison across Stacks 04HR not being performed here. No hypothesis of this statement is an instance of its own conclusion.”.

> **Stacks 09YQ for arbitrary levels, over an arbitrary object of a level.** Let `I` be a
> directed set, let `(X_i)` be an inverse system of schemes over `I` whose transition morphisms are
> affine, and let `X = lim X_i`. Let `F` be a system of abelian sheaves on the small affine etale
> sites of the `X_i`, let `𝒢` on the small affine etale site of `X` present the colimit
> `colim f_i^{-1} F_i`, let `Z` be an object of the small affine etale site of `X_i` and let `p` be
> a degree. Then `H^p(Z_X, 𝒢)`, the cohomology over the image of `Z` in the site of the limit, is
> the filtered colimit, over the arrows `a : j ⟶ i`, of the groups `H^p(Z_j, F_j)` over the
> transition images of `Z`: the canonical cocone is a colimit cocone.
>
> The schemes `X_i` are arbitrary here; only the transition morphisms are affine. This is Stacks
> 09YP, in its weak-system form, applied to the colimit of sites of Stacks 0EYL through
> `mem_limitSitePrecoverage_iff` and the three descent clauses of that file, none of which uses any
> affineness of the levels.
>
> Specialized to affine `X_i` and `Z` the terminal object of the site of `X_i`, the objects carrying
> the cohomology are `X_j` and `X`, which is the affine case
> `Stacks.EtaleCohomology.AffineLimitCohomology.etaleCohomologyColimit_isColimit_of_affine`. For a
> merely quasi-compact and quasi-separated `X_i` there is no such terminal object, and the passage
> from the charts `Z` to `X_i` is the Cech / Mayer-Vietoris step along a finite affine cover; this
> file supplies only its covering input,
> `exists_finite_jointlySurjective_smallAffineEtale`.

```lean
def etaleCohomologyColimit_isColimit
    (F : InverseSystemOfFiniteSites.AbelianSheafSystem.{v, v, max u v + 1, max u v + 1}
      (sys D c B hD hX hc))
    (𝒢 : Sheaf (limitSitePrecoverage D c B hX).toGrothendieck Ab.{max u v + 1})
    (ι : ∀ j, (F.obj j).obj ⟶ (toLimitSmall D c B hD hX hc j).op ⋙ 𝒢.obj)
    (hcolim : IsColimitPresentation.{v, v, max u v + 1, max u v + 1}
      (sys D c B hD hX hc) (toLimitSmall D c B hD hX hc)
      (toLimitSmall_transition D c B hD hX hc) (limitSitePrecoverage D c B hX) F 𝒢 ι)
    (i : (sys D c B hD hX hc).I) (Z : (sys D c B hD hX hc).C i) (p : ℕ)
    (E : CohomologyCocone.{v, v, max u v + 1, max u v + 1}
      (sys D c B hD hX hc) (toLimitSmall D c B hD hX hc)
      (toLimitSmall_transition D c B hD hX hc) (limitSitePrecoverage D c B hX) F 𝒢 ι i Z p) :
    IsColimit E.cocone
```

**`Stacks.EtaleCohomology.EtaleSheafSystem.isSystemColimit_etaleCohomologyPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/SheafSystemCohomologyColimit.lean, line 453](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/SheafSystemCohomologyColimit.lean#L453).

> **Étale cohomology commutes with limits of quasi-compact quasi-separated schemes with affine
> transition morphisms** ([Stacks, Tag 09YQ]). Let `X = lim X_i` be the limit of a directed
> inverse system of quasi-compact and quasi-separated schemes with affine transition morphisms,
> `(F_i, φ_{i'i})` a system of abelian sheaves on the small étale sites of the `X_i`, and
> `ι_i : f_i⁻¹F_i ⟶ 𝓕` a colimit of the system of the inverse images on the small étale site of
> `X`. Then for every `p` the pull back maps `H^p(X_i, F_i) ⟶ H^p(X, 𝓕)` exhibit `H^p(X, 𝓕)` as
> the colimit of the system of the `H^p(X_i, F_i)`.

```lean
theorem EtaleSheafSystem.isSystemColimit_etaleCohomologyPullback (p : ℕ)
    (F : EtaleSheafSystem D Ab.{u + 1}) (𝓕 : Sheaf (smallEtaleTopology c.pt) Ab.{u + 1})
    (ι : ∀ i : Iᵒᵖ, (smallEtalePullbackAb (c.π.app i)).obj (F.obj i) ⟶ 𝓕)
    (hι : LimitHigherDirectImage.IsPullbackCocone c F ι)
    (hpres : LimitHigherDirectImage.IsPullbackColimitPresentation c 𝓕 F ι) :
    IsSystemColimit (fun i => AddCommGrpCat.of (Sheaf.H.{u + 1} (F.obj i) p))
      (fun a => AddCommGrpCat.ofHom (etaleCohomologyPullback (D.map a) (F.map a) p))
      (AddCommGrpCat.of (Sheaf.H.{u + 1} 𝓕 p))
      (fun i => AddCommGrpCat.ofHom (etaleCohomologyPullback (c.π.app i) (ι i) p))
```

**`Stacks.EtaleCohomology.SmallEtaleLimitCohomology.isCohomologyColimit_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/SmallEtaleColimitUnconditional.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/SmallEtaleColimitUnconditional.lean#L132). The attribute's comment: “the whole tag, for ALL degrees `p ≥ 0` and every system of abelian sheaves in the sense of Tag 0EZL, with no hypothesis beyond the source's. The source assumes a directed set, affine transition morphisms, `X = lim X_i` and that every `X_i` is quasi-compact and quasi-separated; those are `IsDirected`, `IsAffineHom (D.map a)`, `hc : IsLimit c`, and the per-level `CompactSpace`/`QuasiSeparatedSpace` instances. The big etale site `B` with `hD`/`hX` is a SIZE device and not a source hypothesis: it fixes which small sites are meant, and `AlgebraicGeometry.BigEtaleSite.exists_contains_of_small` produces one for any small family. The corresponding instances on the VERTEX are derived, not assumed. The conclusion is the tag's equality of groups in elementwise form -- joint surjectivity of the legs together with eventual vanishing, which for a filtered index and abelian coefficients is exactly the assertion that the cocone is colimiting -- and `Stacks.EtaleCohomology.SmallEtaleLimitCohomology.isColimit_stableCohomologyCocone` transports it, in both directions, to a genuine `CategoryTheory.Limits.IsColimit` whose vertex is the full `H^p(X, 𝒢)`. No identity law is used: Definition 59.51.1 imposes only the cocycle condition, so the naive diagram `i ↦ H^p(X_i, F_i)` is not a functor in general, and `hasCohomologyIdentityLaw_iff_forall_stableCohomologySubgroup_eq_top` says precisely when the two spellings coincide. No hypothesis of this statement is an instance of its own conclusion.”.

> **[Stacks, Tag 09YQ] on Mathlib's small étale sites, in every degree, unconditionally.** Let
> `I` be a nonempty directed index, let `(X_i)` be an inverse system of schemes over `Iᵒᵖ` with
> **affine** transition morphisms and every `X_i` **quasi-compact and quasi-separated**, let `c` be a
> **limit** cone with vertex `X`, and let all the `X_i` and `X` be objects of a big étale site `B`.
> Then for every presented system `E` — a system `(F_i)` of abelian sheaves on Mathlib's small étale
> sites of the `X_i` in the sense of [Stacks, Tag 0EZL], together with an abelian sheaf `𝒢` on the
> small étale site of `X` and legs `ι_i : f_i^{-1}F_i ⟶ 𝒢` exhibiting `𝒢 = colim_i f_i^{-1}F_i` —
> and every degree `p`, the cohomology `H^p(X, 𝒢)` is the filtered colimit of the `H^p(X_i, F_i)`
> along the legs.
>
> This is `isCohomologyColimit_of_degreeZero_of_affineOpensAcyclic` with all four of its hypotheses
> supplied; the module docstring says which theorem supplies each, and how the two instances
> on the vertex are derived rather than assumed.
>
> **No identity law** on the system of [Stacks, Tag 0EZL] is used or available: Definition 59.51.1 of
> that tag imposes only the cocycle condition, and none of the four suppliers asks for more.

```lean
theorem isCohomologyColimit_of_isLimit (p : ℕ)
    (E : PresentedSystem (c := c) IsColimitPresentation) : IsCohomologyColimit E p
```

## Tag 03Q5, a lemma

[Tag 03Q5](https://stacks.math.columbia.edu/tag/03Q5) in the Stacks Project.

**`Stacks.EtaleCohomology.isIso_colimit_post_rightDerived_Γ_smallEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FilteredColimitsOfEtaleCohomology.lean, line 305](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FilteredColimitsOfEtaleCohomology.lean#L305).

> **Stacks 03Q5.** Let `X` be a quasi-compact and quasi-separated scheme. For every degree `p`
> and every filtered system `F` of abelian sheaves on the small étale site of `X`, the canonical map
>
> > `colim_i H^p_étale(X, F_i) ⟶ H^p_étale(X, colim_i F_i)`
>
> is an isomorphism: taking cohomology of the étale site of `X` commutes with filtered colimits.
>
> Étale cohomology is the right derived functor of global sections, which is sections over the final
> object `X ⟶ X` of the small étale site; that object is quasi-compact and separated over `X`, so
> this is the case `U = X` of
> `Stacks.EtaleCohomology.isIso_colimit_post_rightDerived_sheafSections_smallEtale`.

```lean
theorem isIso_colimit_post_rightDerived_Γ_smallEtale (X : Scheme.{u})
    [CompactSpace X] [QuasiSeparatedSpace X] (p : ℕ)
    {I : Type (max (u + 1) v)} [SmallCategory I] [IsFiltered I]
    (F : I ⥤ Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}) :
    IsIso (colimit.post F
      ((Sheaf.Γ X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}).rightDerived p))
```

**`AlgebraicGeometry.isIso_vanishingCyclesFibreMap_app_constantComplex_of_isColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/LocallyConstantCoefficientsUnconditional.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/LocallyConstantCoefficientsUnconditional.lean#L337). The attribute's comment: “for the canonical map of Tag 0GJN at a variety of vanishing cycles, in the unbounded derived category: the locus where the map is invertible on constant coefficients is closed under filtered colimits of the coefficient group”.

> **Stacks 03Q5 for the canonical map of Tag 0GJN on constant coefficients.** The locus where
> the canonical map `α_{K,x,t}` is an isomorphism on constant coefficients is closed under filtered
> colimits of the coefficient group: if `M` is the colimit of a filtered system `N` of abelian
> groups and `α` is invertible on the constant complex with value `N i` for every `i`, then it is
> invertible on the constant complex with value `M`.
>
> A map of `D(Ab)` is invertible as soon as it is so on cohomology in every degree, and in each
> degree both sides are functors of the coefficient group commuting with filtered colimits: below
> degree zero both vanish, and in degree `p ≥ 0` the stalk side is `M ↦ (constant sheaf M)_x` placed
> in degree zero while the sections side is `H^p_étale(F_{x,t}, -)` of the inverse image of the
> constant sheaf. The variety of vanishing cycles is affine, hence quasi-compact and
> quasi-separated, so [Stacks, Tag 03Q5] on its small étale site applies.
>
> See the module docstring for why this is not phrased as preservation of filtered colimits by
> `α`.

```lean
theorem isIso_vanishingCyclesFibreMap_app_constantComplex_of_isColimit
    (B : BigEtaleSite.{u}) {X S : Scheme.{u}} (hX : B.Contains X) (hS : B.Contains S)
    (f : X ⟶ S) (x : GeometricPoint X)
    (t : GeometricPoint (strictHenselization B S hS (x.map f)))
    {I : Type (u + 1)} [SmallCategory I] [IsFiltered I] (N : I ⥤ Ab.{u + 1})
    (c : Cocone N) (hc : IsColimit c)
    (hi : ∀ i, IsIso ((vanishingCyclesFibreMap B hX hS f x t).app
      (smallEtaleConstantComplexAb X (N.obj i)))) :
    IsIso ((vanishingCyclesFibreMap B hX hS f x t).app
      (smallEtaleConstantComplexAb X c.pt))
```

## Tag 03Q6, a lemma

[Tag 03Q6](https://stacks.math.columbia.edu/tag/03Q6) in the Stacks Project.

**`Stacks.EtaleCohomology.ColimitBaseChange.isIso_colimitDesc_algebraCohomologyCocone`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/AlgebraColimitCohomology.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/AlgebraColimitCohomology.lean#L159).

> Let `A` be a ring, `(B_i)` a directed system of `A`-algebras with colimit `B`, `f : X ⟶ Spec A`
> quasi-compact and quasi-separated, and `F` an abelian sheaf on `X_étale`. With
> `Y_i = Spec B_i ×_{Spec A} X`, `Y = Spec B ×_{Spec A} X` and `G_i`, `G` the inverse images of `F`,
> the restriction maps exhibit `H^p(Y, G)` as `colim_i H^p(Y_i, G_i)`, for every `p`.

```lean
theorem isIso_colimitDesc_algebraCohomologyCocone [Nonempty I] [IsDirected I (· ≤ ·)]
    (hcB : IsColimit cB) [QuasiCompact f] [QuasiSeparated f] (n : ℕ) :
    IsIso (colimit.desc (algebraCohomologyDiagram A B f F n)
      (algebraCohomologyCocone A B cB f F n))
```

**`Stacks.EtaleCohomology.BaseChangeAlgebraSystem.etaleCohomologyColimit_baseChange_systemLimit_isColimit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/BaseChangeAlgebraSystemCohomology.lean, line 622](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/BaseChangeAlgebraSystemCohomology.lean#L622). The attribute's comment: “the case of an AFFINE `X`: the source allows `X ⟶ Spec(A)` quasi-compact and quasi-separated, and the passage from an affine `X` to a general qcqs one is the Cech descent along a finite affine cover, which this library does not carry. The system is geometric rather than ring-level: `T`, the `Z_i` and `X` are affine schemes over `T`, and `A`, `B_i`, `B = colim B_i` are reached through `Spec(colim B_i) = lim Spec B_i` of Stacks 01YW, no `CommRingCat`-level wrapper taking a ring and a functor `I ⟶ CommRingCat` being stated. The base change is written `Z_i ×_T X`. The cohomology is the right-derived `sheafSections` of Stacks 09YP on the small AFFINE etale sites, inherited from `etaleCohomologyColimit_isColimit_of_affine`, and is NOT yet identified with the mainstream `Stacks.EtaleCohomology.etaleCohomologyFunctor`: the 04HR half of that identification is supplied here by `affineEtaleCohomologyFunctorIso`, but transporting cohomology across `AsSmall.equiv` onto the universe-raised site Stacks 09YP is stated on does not exist in this library”.

> **Stacks 03Q6 for an affine `X`, at the canonical limit.** This is
> `etaleCohomologyColimit_baseChange_isColimit`
> instantiated at `cY = systemLimitCone T X Z`, so that the scheme the cohomology on the left is
> taken over is the honest `Y = (lim_i Z_i) ×_T X`: with `T = Spec A`, `Z_i = Spec B_i` and
> `B = colim_i B_i` this is `Spec B ×_{Spec A} X`, by Stacks 01YW
> (`AlgebraicGeometry.Scheme.affineLimitCone`, through `overLimitCone_pt_iso`).

```lean
def etaleCohomologyColimit_baseChange_systemLimit_isColimit
    (T : Scheme.{u}) (X : Over T) (Z : Iᵒᵖ ⥤ Over T)
    [IsAffine T] [IsAffine X.left] [∀ i, IsAffine (Z.obj i).left]
    (B : AlgebraicGeometry.BigEtaleSite.{u})
    (hD : ∀ i, B.Contains ((baseChange T X Z).obj i))
    (hY : B.Contains (systemLimitCone T X Z).pt)
    (F : InverseSystemOfFiniteSites.AbelianSheafSystem.{u, u, u + 1, u + 1}
      (bcSys T X Z (systemLimitCone T X Z) (isLimitSystemLimitCone T X Z) B hD hY))
    (𝒢 : Sheaf (bcPrecoverage T X Z (systemLimitCone T X Z)
      (isLimitSystemLimitCone T X Z) B hD hY).toGrothendieck Ab.{u + 1})
    (ι : ∀ j, (F.obj j).obj ⟶ (bcToLimitSmall T X Z (systemLimitCone T X Z)
      (isLimitSystemLimitCone T X Z) B hD hY j).op ⋙ 𝒢.obj)
    (hcolim : IsColimitPresentation.{u, u, u + 1, u + 1}
      (bcSys T X Z (systemLimitCone T X Z) (isLimitSystemLimitCone T X Z) B hD hY)
      (bcToLimitSmall T X Z (systemLimitCone T X Z) (isLimitSystemLimitCone T X Z) B hD hY)
      (bcToLimitSmall_transition T X Z (systemLimitCone T X Z)
        (isLimitSystemLimitCone T X Z) B hD hY)
      (bcPrecoverage T X Z (systemLimitCone T X Z) (isLimitSystemLimitCone T X Z) B hD hY) F 𝒢 ι)
    (i : (bcSys T X Z (systemLimitCone T X Z) (isLimitSystemLimitCone T X Z) B hD hY).I) (p : ℕ)
    (E : CohomologyCocone.{u, u, u + 1, u + 1}
      (bcSys T X Z (systemLimitCone T X Z) (isLimitSystemLimitCone T X Z) B hD hY)
      (bcToLimitSmall T X Z (systemLimitCone T X Z) (isLimitSystemLimitCone T X Z) B hD hY)
      (bcToLimitSmall_transition T X Z (systemLimitCone T X Z)
        (isLimitSystemLimitCone T X Z) B hD hY)
      (bcPrecoverage T X Z (systemLimitCone T X Z) (isLimitSystemLimitCone T X Z) B hD hY) F 𝒢 ι i
      (bcLevelTerminal T X Z (systemLimitCone T X Z)
        (isLimitSystemLimitCone T X Z) B hD hY i) p) :
    IsColimit E.cocone
```

**`Stacks.EtaleCohomology.etaleCohomology_specBaseChange_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/BaseChangeAlgebraSystemQcqs.lean, line 431](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/BaseChangeAlgebraSystemQcqs.lean#L431). The attribute's comment: “the whole lemma, at the source's hypotheses: a ring `A`, a directed set `I` (nonempty, as directed sets are in the source), a system of `A`-algebras `B : I ⥤ Under A` with a colimit cocone `cB` (so `B = colim B_i` is `cB.pt`), a quasi-compact and quasi-separated `g : X ⟶ Spec A`, an abelian sheaf `F` on Mathlib's small etale site of `X` and every degree `p`. `Y_i` and `Y` are the fibre products `Spec B_i ×_{Spec A} X` and `Spec B ×_{Spec A} X` (the factors in Mathlib's `pullback` order), `G_i`, `G` the inverse images of `F` along their projections to `X`, and the cohomology is the library's etale cohomology `Sheaf.H` on the small etale sites, with coefficients in `AddCommGrpCat.{u + 1}`, the first universe in which these sites have sheafification. The equality of the source is stated as the elementwise form of a filtered colimit of abelian groups along the restriction maps: joint surjectivity of the maps `H^p(Y_i, G_i) to H^p(Y, G)` and eventual vanishing of a class killed on `Y`, which over a directed index is exactly the assertion that the cohomology cocone is colimiting. The proof is the source's, Tag 09YQ at the inverse system of base changes.”.

> **[Stacks, Tag 03Q6].** Let `A` be a ring, `I` a nonempty directed set, `(B_i)` a system of
> `A`-algebras over `I` (a functor `B : I ⥤ Under A`) and `cB` a colimit cocone of it, with vertex
> `B = colim_i B_i`. Let `g : X ⟶ Spec(A)` be quasi-compact and quasi-separated and `F` an abelian
> sheaf on `X_étale`. Write `Y_i = Spec(B_i) ×_{Spec A} X`, `Y = Spec(B) ×_{Spec A} X` and `G_i`,
> `G` for the inverse images of `F` along the projections to `X`. Then for every `p`,
>
> `H^p_étale(Y, G) = colim_i H^p_étale(Y_i, G_i)`,
>
> the colimit taken along the restriction maps of the morphisms `Y_j ⟶ Y_i` (for `i ≤ j`) and
> `Y ⟶ Y_i`. The colimit is stated elementwise, which over a directed index and with abelian
> groups is the assertion that the cocone is a colimit: every class on `Y` comes from some `Y_i` (the
> inverse image of `G_i` on `Y` identified with `G` by the composition isomorphism of inverse
> images), and a class on `Y_i` which dies on `Y` already dies on some `Y_j`, `j ≥ i`.
>
> The proof is the source's: this is [Stacks, Tag 09YQ] at the inverse system of the `Y_i`
> (`Stacks.EtaleCohomology.etaleCohomologyBaseChangeColimit`), the limit `Spec(B) = lim Spec(B_i)`
> being the image of the colimit `B` under `Spec`.

```lean
theorem etaleCohomology_specBaseChange_colimit (A : CommRingCat.{u}) (I : Type u) [Preorder I]
    [Nonempty I] [IsDirected I (· ≤ ·)] (B : I ⥤ Under A) (cB : Cocone B) (hcB : IsColimit cB)
    (X : Scheme.{u}) (g : X ⟶ Spec A) [QuasiCompact g] [QuasiSeparated g]
    (F : Sheaf X.smallEtaleTopology AddCommGrpCat.{u + 1}) (p : ℕ) :
    (∀ η : Sheaf.H.{u + 1}
        ((etaleAbelianInverseImage.{u, 0} (pullback.snd (Spec.map cB.pt.hom) g)).obj F) p,
      ∃ (i : I)
        (ξ : Sheaf.H.{u + 1}
          ((etaleAbelianInverseImage.{u, 0} (pullback.snd (Spec.map (B.obj i).hom) g)).obj F) p),
        (etaleCohomologyRestrictionMap.{u, 0, u + 1}
          (pullback.map (Spec.map cB.pt.hom) g (Spec.map (B.obj i).hom) g
            (Spec.map (cB.ι.app i).right) (𝟙 X) (𝟙 (Spec A))
            (by rw [Category.comp_id, ← Spec.map_comp, Under.w]; rfl) (by simp)) _ p ξ).comp
          (Ext.mk₀ ((etaleAbelianInverseImageCompIso'.{u, 0}
            (pullback.map (Spec.map cB.pt.hom) g (Spec.map (B.obj i).hom) g
              (Spec.map (cB.ι.app i).right) (𝟙 X) (𝟙 (Spec A))
              (by rw [Category.comp_id, ← Spec.map_comp, Under.w]; rfl) (by simp))
            (pullback.snd (Spec.map (B.obj i).hom) g) (pullback.snd (Spec.map cB.pt.hom) g)
            (by simp only [pullback.map, pullback.lift_snd, Category.comp_id])).app F).inv)
          (add_zero p) = η) ∧
    (∀ (i : I)
        (ξ : Sheaf.H.{u + 1}
          ((etaleAbelianInverseImage.{u, 0} (pullback.snd (Spec.map (B.obj i).hom) g)).obj F) p),
        etaleCohomologyRestrictionMap.{u, 0, u + 1}
          (pullback.map (Spec.map cB.pt.hom) g (Spec.map (B.obj i).hom) g
            (Spec.map (cB.ι.app i).right) (𝟙 X) (𝟙 (Spec A))
            (by rw [Category.comp_id, ← Spec.map_comp, Under.w]; rfl) (by simp)) _ p ξ = 0 →
        ∃ (j : I) (a : i ⟶ j),
          etaleCohomologyRestrictionMap.{u, 0, u + 1}
            (pullback.map (Spec.map (B.obj j).hom) g (Spec.map (B.obj i).hom) g
              (Spec.map (B.map a).right) (𝟙 X) (𝟙 (Spec A))
              (by rw [Category.comp_id, ← Spec.map_comp, Under.w]) (by simp)) _ p ξ = 0)
```

## Tag 03Q8, a lemma

[Tag 03Q8](https://stacks.math.columbia.edu/tag/03Q8) in the Stacks Project.

**`Stacks.HigherDirectImage.higherDirectImageComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Comparison/HigherDirectImage.lean, line 460](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Comparison/HigherDirectImage.lean#L460). The attribute's comment: “abelian sheaves”.

> **Stacks 03Q8 for abelian sheaves.** The higher direct image `R^p f_*` is the sheafification
> of the presheaf `V ↦ H^p_ét(X ×_Y V, F)`, by a natural isomorphism whose components are the
> counit-normalized objectwise comparison `higherDirectImageSheafificationIso`, and whose
> cohomology presheaf has the derived restriction maps of sections.

```lean
public def higherDirectImageComparison (p : ℕ) :
    HigherDirectImageComparison.{u, w} B f p
```

**`Stacks.HigherDirectImage.derivedPushforwardComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Comparison/HigherDirectImageDerived.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Comparison/HigherDirectImageDerived.lean#L273). The attribute's comment: “unbounded complexes”.

> **Stacks 03Q8, unbounded complexes.** The canonical comparison of `Rf_*` with the sheafified
> derived presheaf of sections over the étale base changes is invertible, evaluating the derived
> presheaf of sections at `V` is the total right derived functor of sections over `X ×_Y V`, and
> the restriction maps of the hypercohomology presheaf are the derived restriction maps of
> sections.

```lean
public theorem derivedPushforwardComparison : DerivedPushforwardComparison.{u, w} B f
```

**`Stacks.HigherDirectImage.higherDirectImageStalkCohomologyPresheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/HigherDirectImageStalkColimit.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/HigherDirectImageStalkColimit.lean#L103). The attribute's comment: “the stalk form: the stalk at a geometric point `s` of `R^p f_* F` is the stalk at `s` of the cohomology presheaf `V ↦ H^p(X ×_Y V, F)`, hence the colimit of that presheaf over the étale neighbourhoods of `s`. This is the first display in the source's proof of Stacks 03Q9, which the source attributes to this tag. The base, the morphism `f` and the geometric point are arbitrary. It is NOT Stacks 03Q9: that tag identifies the colimit with the cohomology of the base change of `X` to `Spec(O^{sh}_{Y,s})`, which is Stacks 03Q6 and is not available in a consumable shape”. References: SGA 4 VIII (5.1), “partial”; SGA 4½ Arcata (2.3.3).

> **Stacks 03Q8 at a geometric point.** The stalk at `s` of the `p`-th higher direct image of
> `F` along `f` is the stalk at `s` of the cohomology presheaf `V ↦ H^p_ét(X ×_Y V, F)`, which by
> definition of the stalk is the colimit of that presheaf over the étale neighbourhoods of `s`.
>
> This is the objectwise comparison of Stacks 03Q8, `higherDirectImageSheafificationIso`, followed
> by the invariance of a stalk under sheafification,
> `AlgebraicGeometry.etaleStalkSheafificationIso`.

```lean
public def higherDirectImageStalkCohomologyPresheafIso
    (F : Sheaf (JX B (X := X)) AddCommGrpCat.{w}) (p : ℕ) :
    etaleStalk B Y.obj Y.property s (((pushforward.{u, w} B f).rightDerived p).obj F).obj ≅
      etaleStalk B Y.obj Y.property s (preimageCohomologyPresheaf.{u, w} B f F p)
```

## Tag 09Z1, a lemma

[Tag 09Z1](https://stacks.math.columbia.edu/tag/09Z1) in the Stacks Project.

**`Stacks.EtaleCohomology.FixedBaseHigherDirectImage.transitionMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitHigherDirectImageFixedBase.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitHigherDirectImageFixedBase.lean#L128). The attribute's comment: “the transition maps `ψ_{i'i} : R^p g_{i, *} ℱ_i ⟶ R^p g_{i', *} ℱ_{i'}` of the diagram whose colimit the lemma computes, constructed from the base change map on higher direct images of Stacks 0F02 for the square over the fixed base and the transition map of the system of sheaves. The cocycle condition `ψ_{i''i} = ψ_{i''i'} ∘ ψ_{i'i}` is NOT proved here: the pasting law it reduces to, `Stacks.EtaleCohomology.higherBaseChangeMapAb_paste_app`, is unconditional, and the cocycle condition for the transition maps of a system of bases is `Stacks.EtaleCohomology.LimitHigherDirectImage.transitionMap_comp`, but neither is transported to the fixed base, where the comparisons of the inverse image along `𝟙_S` have to be moved past them. The colimit assertion `R^p g_* ℱ = colim_i R^p g_{i, *} ℱ_i` is NOT proved either; it additionally needs Theorem 09YQ at quasi-compact quasi-separated levels and the comparison of Stacks 04HR at the level of cohomology, the carriers of 09YQ in this repository being stated for the right-derived `CategoryTheory.sheafSections` of the small AFFINE étale sites.”.

> The transition map `ψ_{i'i} : R^p g_{i, *} ℱ_i ⟶ R^p g_{i', *} ℱ_{i'}`: the base change map
> `higherBaseChangeMapAb` for the square `g_{i'} ≫ 𝟙_S = f_{i'i} ≫ g_i`, read through the
> identification of the inverse image along `𝟙_S` with the identity functor, followed by
> `R^p g_{i', *}` of the transition map `φ_{i'i} : f_{i'i}^{-1}ℱ_i ⟶ ℱ_{i'}` of the system of
> sheaves.

```lean
def transitionMap (F : EtaleSheafSystem D Ab.{u + 1}) {i j : Iᵒᵖ} (a : i ⟶ j)
    (w : g i = D.map a ≫ g j) :
    stage g p F j ⟶ stage g p F i
```

**`Stacks.EtaleCohomology.FixedBaseHigherDirectImage.projectionMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitHigherDirectImageFixedBase.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitHigherDirectImageFixedBase.lean#L171). The attribute's comment: “the cocone maps `ψ_i : R^p g_{i, *} ℱ_i ⟶ R^p g_* ℱ` whose universality the lemma asserts, constructed from the base change map on higher direct images of Stacks 0F02 for the square over the fixed base and the map `ι_i : f_i^{-1}ℱ_i ⟶ ℱ` presenting the colimit. The compatibility `ψ_{i'} ∘ ψ_{i'i} = ψ_i`, which would exhibit these maps as a cocone, is NOT proved, for the reason recorded on `Stacks.EtaleCohomology.FixedBaseHigherDirectImage.transitionMap`. The colimit assertion `R^p g_* ℱ = colim_i R^p g_{i, *} ℱ_i` is NOT proved.”.

> The map `ψ_i : R^p g_{i, *} ℱ_i ⟶ R^p g_* ℱ`: the base change map `higherBaseChangeMapAb`
> for the square `g ≫ 𝟙_S = f_i ≫ g_i`, read through the identification of the inverse image along
> `𝟙_S` with the identity functor, followed by `R^p g_*` of the map `ι_i : f_i^{-1}ℱ_i ⟶ ℱ`
> presenting `ℱ` as `colim f_i^{-1}ℱ_i`.

```lean
def projectionMap (F : EtaleSheafSystem D Ab.{u + 1})
    (ι : ∀ i : Iᵒᵖ, (smallEtalePullbackAb (c.π.app i)).obj (F.obj i) ⟶ 𝓕) (i : Iᵒᵖ)
    (w : gX = c.π.app i ≫ g i) :
    stage g p F i ⟶ ((smallEtalePushforwardAb gX).rightDerived p).obj 𝓕
```

**`Stacks.EtaleCohomology.FixedBaseHigherDirectImage.isSystemColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitHigherDirectImageFixedBaseColimit.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitHigherDirectImageFixedBaseColimit.lean#L169). References: SGA 4 VII (5.11), “special case”.

> Let `X = lim X_i` be the limit of a directed inverse system of schemes over `S` with affine
> transition morphisms and quasi-compact and quasi-separated structure morphisms `g_i : X_i ⟶ S`,
> let `g : X ⟶ S` be the structure morphism of the limit, and let `ι_i : f_i⁻¹ℱ_i ⟶ ℱ` present
> `ℱ = colim f_i⁻¹ℱ_i` for a system `(ℱ_i, φ_{i'i})` of abelian sheaves. Then for every `p` the
> maps `ψ_i : R^p g_{i, *}ℱ_i ⟶ R^p g_*ℱ` present `R^p g_*ℱ = colim_i R^p g_{i, *}ℱ_i`, the
> transition maps being the `ψ_{i'i}`.

```lean
theorem isSystemColimit (p : ℕ) (F : EtaleSheafSystem D Ab.{u + 1})
    (𝓕 : Sheaf (smallEtaleTopology c.pt) Ab.{u + 1})
    (ι : ∀ i : Iᵒᵖ, (smallEtalePullbackAb (c.π.app i)).obj (F.obj i) ⟶ 𝓕)
    (hι : ∀ {i j : Iᵒᵖ} (a : i ⟶ j),
      (conePullbackComp c a).inv.app (F.obj j) ≫
        (smallEtalePullbackAb (c.π.app i)).map (F.map a) ≫ ι i = ι j)
    (hpres : LimitHigherDirectImage.IsPullbackColimitPresentation c 𝓕 F ι) :
    IsSystemColimit (stage g p F) (fun {_i _j} a => transitionMap g p F a (hg a))
      (((smallEtalePushforwardAb gX).rightDerived p).obj 𝓕)
      (fun i => projectionMap g p c gX 𝓕 F ι i (w i))
```

## Tag 0EYM, a lemma

[Tag 0EYM](https://stacks.math.columbia.edu/tag/0EYM) in the Stacks Project.

**`Stacks.EtaleCohomology.LimitHigherDirectImage.transitionMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitHigherDirectImage.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitHigherDirectImage.lean#L143). The attribute's comment: “the transition maps `ψ_{i'i} : h_{i'i}^{-1} R^p g_{i, *} ℱ_i ⟶ R^p g_{i', *} ℱ_{i'}` of the first paragraph of the proof, constructed from the base change map on higher direct images of Stacks 0F02 and the transition map of the system of sheaves. The cocycle condition `ψ_{i''i} = ψ_{i''i'} ∘ h_{i''i'}^{-1}ψ_{i'i}`, which the source gets from Stacks 0E47, is NOT proved: pasting of base change maps is carried for ringed topoi on sheaves of modules and for the unbounded derived étale base change map, but not for the bounded below `Stacks.EtaleCohomology.smallEtaleDerivedBaseChangeAb` that `Stacks.EtaleCohomology.higherBaseChangeMapAb` descends from. The colimit assertion `R^p g_* ℱ = colim_i h_i^{-1} R^p g_{i, *} ℱ_i` is NOT proved either; it additionally needs the comparison of Stacks 04HR at the level of cohomology, the carried Stacks 09YQ being stated for the right-derived `sheafSections` of the small AFFINE étale sites.”.

> **The transition maps of Stacks 0EYM**, `ψ_{i'i} : h_{i'i}^{-1} R^p g_{i, *} ℱ_i ⟶
> R^p g_{i', *} ℱ_{i'}`: the base change map of the transition square
> `g_{i'} ≫ h_{i'i} = f_{i'i} ≫ g_i` on higher direct images, followed by `R^p g_{i', *}` of the
> transition map `φ_{i'i} : f_{i'i}^{-1}ℱ_i ⟶ ℱ_{i'}` of the system of sheaves.

```lean
def transitionMap (F : EtaleSheafSystem DX Ab.{u + 1}) {i j : Iᵒᵖ} (a : i ⟶ j) :
    (smallEtalePullbackAb (DS.map a)).obj
        (((smallEtalePushforwardAb (γ.app j)).rightDerived p).obj (F.obj j)) ⟶
      ((smallEtalePushforwardAb (γ.app i)).rightDerived p).obj (F.obj i)
```

**`Stacks.EtaleCohomology.LimitHigherDirectImage.projectionMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitHigherDirectImage.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitHigherDirectImage.lean#L179). The attribute's comment: “the cocone maps `ψ_i : h_i^{-1} R^p g_{i, *} ℱ_i ⟶ R^p g_* ℱ` of the first paragraph of the proof, constructed from the base change map on higher direct images of Stacks 0F02 and the map `ι_i : f_i^{-1}ℱ_i ⟶ ℱ` presenting the colimit. The compatibility `ψ_{i'} ∘ h_{i'}^{-1}ψ_{i'i} = ψ_i`, which the source gets from Stacks 0E47, is NOT proved, for the reason recorded on `transitionMap`; so these maps are not exhibited as a cocone. The colimit assertion `R^p g_* ℱ = colim_i h_i^{-1} R^p g_{i, *} ℱ_i` is NOT proved.”.

> **The cocone maps of Stacks 0EYM**, `ψ_i : h_i^{-1} R^p g_{i, *} ℱ_i ⟶ R^p g_* ℱ`: the base
> change map of the projection square `g ≫ h_i = f_i ≫ g_i` on higher direct images, followed by
> `R^p g_*` of the map `ι_i : f_i^{-1}ℱ_i ⟶ ℱ` presenting `ℱ` as `colim f_i^{-1}ℱ_i`.

```lean
def projectionMap (F : EtaleSheafSystem DX Ab.{u + 1})
    (ι : ∀ i : Iᵒᵖ, (smallEtalePullbackAb (cX.π.app i)).obj (F.obj i) ⟶ 𝓕) (i : Iᵒᵖ) :
    (smallEtalePullbackAb (cS.π.app i)).obj
        (((smallEtalePushforwardAb (γ.app i)).rightDerived p).obj (F.obj i)) ⟶
      ((smallEtalePushforwardAb (limitMorphism γ cX cS hcS)).rightDerived p).obj 𝓕
```

**`Stacks.EtaleCohomology.LimitHigherDirectImage.isHigherDirectImageColimit_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitHigherDirectImageColimitAssertion.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitHigherDirectImageColimitAssertion.lean#L280). References: SGA 4 VII (5.11), “more general”.

> Let `I` be a directed set, let `(X_i, f_{i'i})` and `(S_i, h_{i'i})` be inverse systems of
> schemes over `I` with affine transition morphisms, let `g_i : X_i ⟶ S_i` be a morphism of inverse
> systems with every `g_i` quasi-compact and quasi-separated, let `X = lim X_i`, `S = lim S_i` and
> `g : X ⟶ S` the limit morphism. Let `(F_i, φ_{i'i})` be a system of abelian
> sheaves on `(X_i, f_{i'i})` and `ι_i : f_i^{-1}F_i ⟶ 𝓕` maps, compatible with the transition maps,
> presenting `𝓕 = colim f_i^{-1}F_i`. Then for every `p ≥ 0`
>
> `R^p g_* 𝓕 = colim_{i ∈ I} h_i^{-1} R^p g_{i, *}F_i`:
>
> every family of maps out of the `h_i^{-1} R^p g_{i, *}F_i` compatible with the maps
> `h_{i'}^{-1}ψ_{i'i}` induced by the transition maps
> `ψ_{i'i} : h_{i'i}^{-1} R^p g_{i, *}F_i ⟶ R^p g_{i', *}F_{i'}` factors uniquely through the cocone
> maps `ψ_i : h_i^{-1} R^p g_{i, *}F_i ⟶ R^p g_* 𝓕`, both families being built from the base change
> maps on higher direct images as in the source
> (`Stacks.EtaleCohomology.LimitHigherDirectImage.transitionMap`,
> `Stacks.EtaleCohomology.LimitHigherDirectImage.projectionMap`).

```lean
theorem isHigherDirectImageColimit_of_isLimit (p : ℕ)
    (𝓕 : Sheaf (smallEtaleTopology cX.pt) Ab.{max u v + 1})
    (F : EtaleSheafSystem DX Ab.{max u v + 1})
    (ι : ∀ i : Iᵒᵖ, (smallEtalePullbackAb (cX.π.app i)).obj (F.obj i) ⟶ 𝓕)
    (hι : ∀ {i j : Iᵒᵖ} (a : i ⟶ j),
      (conePullbackComp cX a).inv.app (F.obj j) ≫
        (smallEtalePullbackAb (cX.π.app i)).map (F.map a) ≫ ι i = ι j)
    (hpres : IsPullbackColimitPresentation cX 𝓕 F ι) :
    IsHigherDirectImageColimit γ p cX cS hcS 𝓕 F ι
```

**`Stacks.EtaleCohomology.LimitHigherDirectImage.higherDirectImageColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitHigherDirectImageColimitTheorem.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitHigherDirectImageColimitTheorem.lean#L92). References: SGA 4 VII (5.11), “more general”.

> Let `I` be a directed set, `g_i : X_i ⟶ S_i` an inverse system of quasi-compact and
> quasi-separated morphisms of schemes with affine transition morphisms `f_{i'i}`, `h_{i'i}`,
> `g : X ⟶ S` its limit with projections `f_i`, `h_i`, `(ℱ_i, φ_{i'i})` a system of abelian sheaves
> on `(X_i, f_{i'i})` and `ℱ = colim f_i⁻¹ℱ_i`. Then for every `p`
>
> * the maps `ψ_{i'i} : h_{i'i}⁻¹R^p g_{i, *}ℱ_i ⟶ R^p g_{i', *}ℱ_{i'}` satisfy the cocycle condition
>   `ψ_{i''i} = ψ_{i''i'} ∘ h_{i''i'}⁻¹ψ_{i'i}`;
> * the maps `ψ_i : h_i⁻¹R^p g_{i, *}ℱ_i ⟶ R^p g_*ℱ` satisfy `ψ_{i'} ∘ h_{i'}⁻¹ψ_{i'i} = ψ_i`;
> * they present `R^p g_*ℱ = colim_{i ∈ I} h_i⁻¹R^p g_{i, *}ℱ_i`.

```lean
theorem higherDirectImageColimit (p : ℕ) (F : EtaleSheafSystem DX Ab.{u + 1})
    (𝓕 : Sheaf (smallEtaleTopology cX.pt) Ab.{u + 1})
    (ι : ∀ i : Iᵒᵖ, (smallEtalePullbackAb (cX.π.app i)).obj (F.obj i) ⟶ 𝓕)
    (hι : ∀ {i j : Iᵒᵖ} (a : i ⟶ j),
      (conePullbackComp cX a).inv.app (F.obj j) ≫
        (smallEtalePullbackAb (cX.π.app i)).map (F.map a) ≫ ι i = ι j)
    (hpres : IsPullbackColimitPresentation cX 𝓕 F ι) :
    (∀ {i j k : Iᵒᵖ} (a : i ⟶ j) (b : j ⟶ k),
        (systemPullbackComp DS Ab.{u + 1} a b).inv.app
              (((smallEtalePushforwardAb (γ.app k)).rightDerived p).obj (F.obj k)) ≫
            (systemPullback DS Ab.{u + 1} a).map (transitionMap γ p F b) ≫
              transitionMap γ p F a =
          transitionMap γ p F (a ≫ b)) ∧
      (∀ {i j : Iᵒᵖ} (a : i ⟶ j),
          (conePullbackComp cS a).inv.app
                (((smallEtalePushforwardAb (γ.app j)).rightDerived p).obj (F.obj j)) ≫
              (smallEtalePullbackAb (cS.π.app i)).map (transitionMap γ p F a) ≫
                projectionMap γ cX cS hcS p 𝓕 F ι i =
            projectionMap γ cX cS hcS p 𝓕 F ι j) ∧
        IsHigherDirectImageColimit γ p cX cS hcS 𝓕 F ι
```

## Tag 0EYN, a lemma

[Tag 0EYN](https://stacks.math.columbia.edu/tag/0EYN) in the Stacks Project.

**`Stacks.EtaleCohomology.directImageSystem`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/DirectImageSystem.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/DirectImageSystem.lean#L342). The attribute's comment: “the system of sheaves”.

> Let `(X_i, f_{i'i})` be an inverse system of schemes, let `f_i : X ⟶ X_i` be the projections
> of a cone over it, and let `𝓕` be a sheaf on the small étale site of `X`. The direct images
> `f_{i,*}𝓕`, with the canonical maps `φ_{i'i} : f_{i'i}^{-1} f_{i,*}𝓕 ⟶ f_{i',*}𝓕` adjoint to the
> identification `f_{i,*}𝓕 ≅ f_{i'i,*} f_{i',*}𝓕` given by `f_i = f_{i'} ≫ f_{i'i}`, form a system
> of sheaves on `(X_i, f_{i'i})` in the sense of Stacks 0EZL.

```lean
public def directImageSystem : EtaleSheafSystem D A
```

**`Stacks.EtaleCohomology.isPullbackColimitPresentation_directImageSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/DirectImageSystemColimitPresentation.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/DirectImageSystemColimitPresentation.lean#L94). The attribute's comment: “the colimit `𝓕 = colim f_i⁻¹f_{i,*}𝓕`”.

> **[Stacks, Tag 0EYN], the colimit.** Let `X = lim X_i` be a directed limit of schemes with
> affine transition morphisms and projections `f_i : X ⟶ X_i`, and let `𝓕` be an abelian sheaf on
> `X_étale`. Then the counits `f_i⁻¹f_{i,*}𝓕 ⟶ 𝓕` present `𝓕 = colim f_i⁻¹f_{i,*}𝓕` over the
> system of sheaves `(f_{i,*}𝓕, φ_{i'i})` of `Stacks.EtaleCohomology.directImageSystem`.

```lean
theorem isPullbackColimitPresentation_directImageSystem (hc : IsLimit c) :
    LimitHigherDirectImage.IsPullbackColimitPresentation c 𝓕
      (directImageSystem D Ab.{u + 1} c 𝓕) (coneDirectImageCounit c 𝓕)
```

**`Stacks.EtaleCohomology.isColimitPullbackDirectImageCocone`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/DirectImageSystemIsColimit.lean, line 377](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/DirectImageSystemIsColimit.lean#L377). The attribute's comment: “part (2): `𝓕 = colim_i f_i^{-1}f_{i,*}𝓕` for the system of part (1), on Mathlib's small étale site, for sheaves of sets”.

> **[Stacks, Tag 0EYN] (2), for sheaves of sets.** Let `X = lim X_i` be a directed limit of
> schemes with affine transition morphisms `f_{i'i}` and projection morphisms `f_i : X ⟶ X_i`, and
> let `𝓕` be a sheaf of sets on the small étale site of `X`. Then `𝓕 = colim_i f_i^{-1}f_{i,*}𝓕`:
> the cocone of counits `f_i^{-1}f_{i,*}𝓕 ⟶ 𝓕` over the diagram
> `Stacks.EtaleCohomology.pullbackDirectImageDiagram`, whose transition maps are built from the maps
> `φ_{i'i} : f_{i'i}^{-1}f_{i,*}𝓕 ⟶ f_{i',*}𝓕` of the system of sheaves of part (1),
> `Stacks.EtaleCohomology.directImageSystem`, is a colimit cocone. Equivalently, the canonical map
> `colim_i f_i^{-1}f_{i,*}𝓕 ⟶ 𝓕` is an isomorphism.

```lean
def isColimitPullbackDirectImageCocone
    (F : Sheaf (AlgebraicGeometry.Scheme.smallEtaleTopology c.pt) (Type (max u v + 1))) :
    IsColimit (pullbackDirectImageCocone D (Type (max u v + 1)) c F)
```

**`Stacks.EtaleCohomology.AffineLimitCohomology.restrictionIsColimit_limitToSmallEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/SmallEtaleLimitColimitSheaf.lean, line 721](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/SmallEtaleLimitColimitSheaf.lean#L721). The attribute's comment: “part (2): `F = colim_i p_i^{-1}p_{i,*}F`, on the site of Stacks 021B”.

> **Stacks 0EYN, second half, on the small étale site of a limit of schemes.** Let `(X_i)` be
> an inverse system of schemes with affine transition morphisms over a nonempty directed index, all
> of them objects of a big étale site `B`, let `X = lim X_i`, and let `F` be a sheaf of sets on the
> small étale site of `X`. Then
>
> `F = colim_i p_i^{-1} p_{i,*} F`,
>
> in the form the inverse-system machinery proves it: every family of maps out of the restrictions
> of `F` to the levels of the system of sites of [Stacks, Tag 0EYL], compatible with the canonical
> transition maps, is the restriction of a **unique** map of sheaves out of `F`. Those restrictions
> are the `p_{i,*}F` read on the levels — they are `levelRestrict`, whose sections over a level
> object are the sections of `F` over its image in the site of the limit (`levelRestrict_obj`, an
> `rfl`), and that image is the base change of the level object along `p_i`.
>
> This is the geometric instantiation of
> `CategoryTheory.Sites.InverseSystem.InverseSystemOfFiniteSites.descent_along_restriction` at
> `Λ = limitToSmallEtale`: the five site inputs of [Stacks, Tag 09YP] for the raised site are
> `toLimitSmall_transition`, `toLimitSmall_obj_descends`, `toLimitSmall_hom_descends`,
> `toLimitSmall_hom_eventually_eq` and `mem_limitSitePrecoverage_iff`, and the two instances making
> restriction along the composite crossing fully faithful are `full_limitRestriction` and
> `faithful_limitRestriction`.
>
> **Why the conclusion is the named predicate.** Written out, the telescope mentions
> `(sys D c B hD hX hc).I`, `.C i` and `.u a` some thirty times and exceeds the heartbeat budget in
> the signature; the failure is a `(deterministic) timeout at isDefEq`
> inside the compatibility hypothesis of the family `g`, before any proof runs. The docstring of
> `CategoryTheory.Sites.InverseSystem.InverseSystemOfFiniteSites.RestrictionIsColimit` records the
> rule and the three other places in this development where it was needed.
>
> **Why `hK` is supplied by `rw` and not as a term.** `mem_limitSitePrecoverage_iff` states exactly
> the required equivalence, but its last clause is a transport `R = h ▸ S.map (toLimitSmall …)`
> whose motive was elaborated against the concrete functor, while the motive the machinery's
> hypothesis carries is the one elaborated against its variable `u`. The two are definitionally
> equal and deciding them is another heartbeat timeout; rewriting the goal with the equivalence
> closes it outright instead.
>
> Part (1) of the tag, that the `p_{i,*}F` carry canonical maps making them a system of sheaves in
> the sense of [Stacks, Tag 0EZL], is `Stacks.EtaleCohomology.directImageSystem`, which states it on
> Mathlib's small étale site; that declaration and this one are the covering set of Tag 0EYN.

```lean
theorem restrictionIsColimit_limitToSmallEtale
    (F : Sheaf (AlgebraicGeometry.SmallEtale.topology B c.pt hX) (Type (max u v + 1))) :
    InverseSystemOfFiniteSites.RestrictionIsColimit
      (AlgebraicGeometry.SmallEtale.topology B c.pt hX) (sys D c B hD hX hc)
      (fun i => toLimitSmall D c B hD hX hc i ⋙ limitToSmallEtale D c B hX)
      (InverseSystemOfFiniteSites.compTransitionIso (limitToSmallEtale D c B hX)
        (sys D c B hD hX hc) (toLimitSmall D c B hD hX hc)
        (toLimitSmall_transition D c B hD hX hc)) F
```

## Tag 0DV2, a lemma

[Tag 0DV2](https://stacks.math.columbia.edu/tag/0DV2) in the Stacks Project.

**`Stacks.EtaleCohomology.LimitHigherDirectImage.isColimit_pushforwardStage_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/PushforwardStageColimit.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/PushforwardStageColimit.lean#L76). The attribute's comment: “the colimit assertion for the canonical diagram and the canonical cocone, with the cocycle condition of the diagram and the cocone identity of its legs”.

> **Stacks 0DV2.** Let `I` be a directed set, let `(X_i, f_{i'i})` and `(S_i, h_{i'i})` be
> inverse systems of schemes with affine transition morphisms, let `g_i : X_i ⟶ S_i` be a morphism
> of the first system into the second with every `g_i` quasi-compact and quasi-separated, let
> `f_i : X ⟶ X_i` and `h_i : S ⟶ S_i` be the projections of limit cones over the two systems, let
> `g : X ⟶ S` be the limit morphism, and let `𝓕` be an abelian sheaf on the small étale site of
> `X`. Then
>
> `R^p g_* 𝓕 = colim_{i ∈ I} h_i^{-1} R^p g_{i, *}(f_{i, *}𝓕)`:
>
> the objects `h_i^{-1} R^p g_{i, *}(f_{i, *}𝓕)` with the maps induced by the transition maps
> `ψ_{i'i}` of [Stacks, Tag 0EYM] satisfy the cocycle condition, the maps `ψ_i` of the same source
> form a cocone on them, and that cocone is a colimit.
>
> The counits present `𝓕 = colim_i f_i^{-1}f_{i, *}𝓕` by the colimit half of [Stacks, Tag 0EYN],
> `Stacks.EtaleCohomology.isPullbackColimitPresentation_directImageSystem`; they are compatible with
> the transition maps of `Stacks.EtaleCohomology.directImageSystem` by
> `Stacks.EtaleCohomology.coneDirectImageCounit_cocone`, and [Stacks, Tag 0EYM],
> `Stacks.EtaleCohomology.LimitHigherDirectImage.isHigherDirectImageColimit`, applies.

```lean
theorem isColimit_pushforwardStage_of_isLimit [Nonempty I] [IsDirected I (· ≤ ·)]
    [∀ {i j : Iᵒᵖ} (a : i ⟶ j), IsAffineHom (DX.map a)]
    [∀ {i j : Iᵒᵖ} (a : i ⟶ j), IsAffineHom (DS.map a)]
    [∀ i : Iᵒᵖ, QuasiCompact (γ.app i)] [∀ i : Iᵒᵖ, QuasiSeparated (γ.app i)]
    (hcX : IsLimit cX) :
    (∀ {i j k : Iᵒᵖ} (a : i ⟶ j) (b : j ⟶ k),
        (systemPullbackComp DS Ab.{u + 1} a b).inv.app
              (((smallEtalePushforwardAb (γ.app k)).rightDerived p).obj
                ((directImageSystem DX Ab.{u + 1} cX 𝓕).obj k)) ≫
            (systemPullback DS Ab.{u + 1} a).map (pushforwardStageTransition cX 𝓕 γ p b) ≫
              pushforwardStageTransition cX 𝓕 γ p a =
          pushforwardStageTransition cX 𝓕 γ p (a ≫ b)) ∧
      (∀ {i j : Iᵒᵖ} (a : i ⟶ j),
          (conePullbackComp cS a).inv.app
                (((smallEtalePushforwardAb (γ.app j)).rightDerived p).obj
                  ((directImageSystem DX Ab.{u + 1} cX 𝓕).obj j)) ≫
              (smallEtalePullbackAb (cS.π.app i)).map (pushforwardStageTransition cX 𝓕 γ p a) ≫
                pushforwardStageLeg cX 𝓕 γ cS hcS p i =
            pushforwardStageLeg cX 𝓕 γ cS hcS p j) ∧
        IsHigherDirectImageColimit γ p cX cS hcS 𝓕 (directImageSystem DX Ab.{u + 1} cX 𝓕)
          (coneDirectImageCounit cX 𝓕)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.51, Tag 03Q4](https://stacks.math.columbia.edu/tag/03Q4)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
