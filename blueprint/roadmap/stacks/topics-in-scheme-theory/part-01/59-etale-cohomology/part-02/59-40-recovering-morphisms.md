---
declaration: section
origin: cited
lean: AlgebraicGeometry.smallEtaleRingedSiteHom_isLocallyRinged, AlgebraicGeometry.Space.schemeSmallEtaleRingedToposHom_twoMorphism_eq_id, AlgebraicGeometry.Space.schemeSmallEtaleRingedToposHom_twoMorphismOfRingedTopoi_eq_id, AlgebraicGeometry.eq_of_smallEtale_twoIso, AlgebraicGeometry.eq_of_smallEtale_twoIso_comm, AlgebraicGeometry.eq_of_smallEtaleRingedToposHom_twoIso, AlgebraicGeometry.eq_of_twoIso_smallEtaleRingedToposHom, AlgebraicGeometry.exists_schemeHom_twoIso_of_isLocallyRinged
statement: formalized
proof: formalized
---

# 59.40 Recovering morphisms

Section 59.40 of the Stacks Project, [Tag 04JH](https://stacks.math.columbia.edu/tag/04JH). 5 tags here are carried by 10 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04I5, a lemma

[Tag 04I5](https://stacks.math.columbia.edu/tag/04I5) in the Stacks Project.

**`AlgebraicGeometry.smallEtaleRingedSiteHom_isLocallyRinged`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/LocallyRinged.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/LocallyRinged.lean#L130).

> **Stacks 04I5.** The morphism of ringed sites `(a_small, a_small^♯)` associated to a
> morphism of schemes `a : X ⟶ Y` is a morphism of locally ringed sites: its square of units
> subsheaves is cartesian.
>
> The geometric points of `X` are a conservative family of points of its small étale site, and at
> each of them the stalk of `a⁻¹𝒪_Y ⟶ 𝒪_X` is the map of étale local rings
> `(𝒪_Y)_ȳ ⟶ (𝒪_X)_x̄`, which is a local ring map.

```lean
public theorem smallEtaleRingedSiteHom_isLocallyRinged :
    (smallEtaleRingedSiteHom B a).IsLocallyRinged
```

## Tag 04IJ, a lemma

[Tag 04IJ](https://stacks.math.columbia.edu/tag/04IJ) in the Stacks Project.

**`AlgebraicGeometry.Space.schemeSmallEtaleRingedToposHom_twoMorphism_eq_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SchemeSmallEtaleTwoMorphismRigidity.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SchemeSmallEtaleTwoMorphismRigidity.lean#L66).

> **Stacks 04IJ.** A 2-morphism from the morphism of small étale ringed topoi induced by a
> morphism of schemes to itself is the identity.

```lean
theorem schemeSmallEtaleRingedToposHom_twoMorphism_eq_id
    (t : AlgebraicGeometry.RingedToposHom.TwoMorphism.{u, u + 1, u, u, u + 1, u}
      (smallEtaleRingedToposHom B S hS (schemeSpaceMap g))
      (smallEtaleRingedToposHom B S hS (schemeSpaceMap g))) :
    t = AlgebraicGeometry.RingedToposHom.TwoMorphism.id
      (smallEtaleRingedToposHom B S hS (schemeSpaceMap g))
```

**`AlgebraicGeometry.Space.schemeSmallEtaleRingedToposHom_twoMorphismOfRingedTopoi_eq_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SchemeSmallEtaleTwoMorphismRigidity.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SchemeSmallEtaleTwoMorphismRigidity.lean#L78).

> **Stacks 04IJ** for a 2-morphism over the four-field morphism of ringed topoi: a 2-morphism
> from the morphism of small étale ringed topoi induced by a morphism of schemes to itself is the
> identity.

```lean
theorem schemeSmallEtaleRingedToposHom_twoMorphismOfRingedTopoi_eq_id
    (t : Stacks.Sheaves.RingedToposModules.TwoMorphismOfRingedTopoi.{u, u + 1, u, u, u + 1, u}
      (smallEtaleRingedToposHom B S hS (schemeSpaceMap g)).toRingedToposModulesHom
      (smallEtaleRingedToposHom B S hS (schemeSpaceMap g)).toRingedToposModulesHom) :
    t = Stacks.Sheaves.RingedToposModules.TwoMorphismOfRingedTopoi.id.{u, u + 1, u, u, u + 1, u}
      (smallEtaleRingedToposHom B S hS (schemeSpaceMap g)).toRingedToposModulesHom
```

## Tag 04LW, a lemma

[Tag 04LW](https://stacks.math.columbia.edu/tag/04LW) in the Stacks Project.

**`AlgebraicGeometry.eq_of_smallEtale_twoIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/Faithful.lean, line 441](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/Faithful.lean#L441).

> **Stacks 04LW.** Let `X` and `Y` be schemes. Two morphisms `a, b : X ⟶ Y` for which there
> is a 2-isomorphism `(a_small, a_small^♯) ≅ (b_small, b_small^♯)` in the 2-category of ringed
> topoi are equal.
>
> The hypotheses are the data of such a 2-isomorphism: an isomorphism `t` of the direct images,
> and the commutation of `t` with the two structure maps.

```lean
public theorem eq_of_smallEtale_twoIso {X Y : B.Scheme} (a b : X ⟶ Y)
    (t : (smallEtaleBaseChange B a).sheafPushforwardContinuous (Type u)
        (SmallEtale.topology B Y.obj Y.property)
        (SmallEtale.topology B X.obj X.property) ≅
      (smallEtaleBaseChange B b).sheafPushforwardContinuous (Type u)
        (SmallEtale.topology B Y.obj Y.property)
        (SmallEtale.topology B X.obj X.property))
    (hsharp : ∀ (V : SmallEtale B Y.obj Y.property)
        (s : (SmallEtale.commRingStructureSheaf B Y.obj Y.property).obj.obj (op V)),
      (t.hom.app (setStructureSheaf B X.obj X.property)).hom.app (op V)
          ((structureSharp B a).hom.app (op V) s) =
        (structureSharp B b).hom.app (op V) s) :
    a = b
```

**`AlgebraicGeometry.eq_of_smallEtale_twoIso_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/Faithful.lean, line 473](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/Faithful.lean#L473).

> **Stacks 04LW**, with the compatibility with the structure maps written as the commuting
> triangle of a 2-morphism of ringed topoi: the composite of `a_small^♯` with `t`, evaluated at
> the structure sheaf of `X`, is `b_small^♯`, after forgetting the ring structure of the two
> structure sheaves, which is what a 2-morphism of topoi acts on.

```lean
public theorem eq_of_smallEtale_twoIso_comm {X Y : B.Scheme} (a b : X ⟶ Y)
    (t : (smallEtaleBaseChange B a).sheafPushforwardContinuous (Type u)
        (SmallEtale.topology B Y.obj Y.property)
        (SmallEtale.topology B X.obj X.property) ≅
      (smallEtaleBaseChange B b).sheafPushforwardContinuous (Type u)
        (SmallEtale.topology B Y.obj Y.property)
        (SmallEtale.topology B X.obj X.property))
    (hsharp : (sheafCompose (SmallEtale.topology B Y.obj Y.property)
            (forget CommRingCat.{u})).map (structureSharp B a) ≫
          t.hom.app ((sheafCompose (SmallEtale.topology B X.obj X.property)
            (forget CommRingCat.{u})).obj
            (SmallEtale.commRingStructureSheaf B X.obj X.property)) =
        (sheafCompose (SmallEtale.topology B Y.obj Y.property)
          (forget CommRingCat.{u})).map (structureSharp B b)) :
    a = b
```

**`AlgebraicGeometry.eq_of_smallEtaleRingedToposHom_twoIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/RingedToposTwoIso.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/RingedToposTwoIso.lean#L86).

> **Stacks 04LW**, in the 2-category of ringed topoi.  Two morphisms of schemes `a, b : X ⟶ Y`
> for which `(a_small, a_small^♯)` and `(b_small, b_small^♯)` are 2-isomorphic are equal.

```lean
theorem eq_of_smallEtaleRingedToposHom_twoIso (a b : X ⟶ Y)
    (t : RingedToposHom.TwoIso.{u, u + 1, u, u, u + 1, u} (smallEtaleRingedToposHom B a)
      (smallEtaleRingedToposHom B b)) :
    a = b
```

**`AlgebraicGeometry.eq_of_twoIso_smallEtaleRingedToposHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/RingedToposTwoIso.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/RingedToposTwoIso.lean#L99). The attribute's comment: “the uniqueness clause of 04I6”.

> **The uniqueness half of Stacks 04I6.**  A morphism of ringed topoi between the small étale
> ringed topoi of two schemes is 2-isomorphic to `(f_small, f_small^♯)` for at most one morphism
> of schemes `f : X ⟶ Y`.

```lean
theorem eq_of_twoIso_smallEtaleRingedToposHom
    (g : RingedToposHom
      (RingedSite.toRingedTopos (smallEtaleRingedSite B X.obj X.property))
      (RingedSite.toRingedTopos (smallEtaleRingedSite B Y.obj Y.property)))
    (a b : X ⟶ Y)
    (ta : RingedToposHom.TwoIso.{u, u + 1, u, u, u + 1, u} g (smallEtaleRingedToposHom B a))
    (tb : RingedToposHom.TwoIso.{u, u + 1, u, u, u + 1, u} g (smallEtaleRingedToposHom B b)) :
    a = b
```

## Tag 04I6, a lemma

[Tag 04I6](https://stacks.math.columbia.edu/tag/04I6) in the Stacks Project.

**`AlgebraicGeometry.exists_schemeHom_twoIso_of_isLocallyRinged`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/AffineExistence.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/AffineExistence.lean#L212). The attribute's comment: “the existence clause: 2-isomorphic to some (f_small, f_small^sharp)”.

> **The existence half of [Stacks Project, Tag 04I6].**  Let `X` and `Y` be schemes of a big
> étale site with `Y` affine, and let
>
> `(g, g^♯) : (Sh(X_étale), 𝒪_X) ⟶ (Sh(Y_étale), 𝒪_Y)`
>
> be a morphism of *locally* ringed topoi.  Then there is a morphism of schemes `f : X ⟶ Y` such
> that `(g, g^♯)` is 2-isomorphic to `(f_{small}, f_{small}^♯)` in the sense of
> [Stacks Project, Tag 04IC].
>
> This is the half of the tag that has content; uniqueness is
> `AlgebraicGeometry.eq_of_twoIso_smallEtaleRingedToposHom`, i.e. [Stacks Project, Tag 04LW], and
> needs no hypothesis, so it upgrades this to the `∃!` of
> `AlgebraicGeometry.existsUnique_schemeHom_twoIso_of_isLocallyRinged` for free.  The affineness of
> `X`, which the tag assumes, is not needed; see the module documentation.

```lean
theorem exists_schemeHom_twoIso_of_isLocallyRinged (hg : g.IsLocallyRinged) :
    ∃ a : X ⟶ Y,
      Nonempty (RingedToposHom.TwoIso.{u, u + 1, u, u, u + 1, u} g
        (smallEtaleRingedToposHom B a))
```

**`AlgebraicGeometry.existsUnique_schemeHom_twoIso_of_isLocallyRinged`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/AffineExistence.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/AffineExistence.lean#L237).

> **[Stacks Project, Tag 04I6].**  Let `X` and `Y` be schemes of a big étale site with `Y`
> affine, and let
>
> `(g, g^♯) : (Sh(X_étale), 𝒪_X) ⟶ (Sh(Y_étale), 𝒪_Y)`
>
> be a morphism of *locally* ringed topoi.  Then there is a **unique** morphism of schemes
> `f : X ⟶ Y` such that `(g, g^♯)` is 2-isomorphic to `(f_{small}, f_{small}^♯)` in the sense of
> [Stacks Project, Tag 04IC].
>
> Existence is `AlgebraicGeometry.exists_schemeHom_twoIso_of_isLocallyRinged`, whose content is the
> whole of the source's proof: the ring map on global functions and the morphism `f = Spec φ` it
> names, the comparison `g⁻¹h_V ≅ h_{X ×_Y V}` at the affine étale charts of `Y` with its stalk
> computation through [Stacks Project, Tag 04GX], the transport to all charts along
> [Stacks Project, Tag 04HR], and the agreement of the two structure maps.  Uniqueness is
> [Stacks Project, Tag 04LW], `AlgebraicGeometry.eq_of_twoIso_smallEtaleRingedToposHom`.
>
> The tag assumes `X` affine as well; that hypothesis is not needed here.

```lean
theorem existsUnique_schemeHom_twoIso_of_isLocallyRinged (hg : g.IsLocallyRinged) :
    ∃! a : X ⟶ Y,
      Nonempty (RingedToposHom.TwoIso.{u, u + 1, u, u, u + 1, u} g
        (smallEtaleRingedToposHom B a))
```

Declarations registered for the tag:

- [`AlgebraicGeometry.eq_of_twoIso_smallEtaleRingedToposHom`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/RingedToposTwoIso.lean#L99), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/RingedToposTwoIso.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/RingedToposTwoIso.lean#L109) (StacksFrontier): “the uniqueness clause: for two affine schemes and a morphism of locally ringed topoi, which this statement covers since it assumes neither”.

## Tag 04I7, a theorem

[Tag 04I7](https://stacks.math.columbia.edu/tag/04I7) in the Stacks Project.

**`AlgebraicGeometry.existsUnique_schemeHom_twoIso_smallEtaleRingedToposHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/Existence/Assembly.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/Existence/Assembly.lean#L345).

> Let `X` and `Y` be schemes (of a big étale site) and let
> `(g, g^♯) : (Sh(X_étale), 𝒪_X) ⟶ (Sh(Y_étale), 𝒪_Y)` be a morphism of locally ringed topoi.  Then
> there is a unique morphism of schemes `f : X ⟶ Y` such that `(g, g^♯)` is 2-isomorphic to
> `(f_small, f_small^♯)`.
>
> Existence: `f` is glued from the morphisms `f_V : W_V ⟶ V` over the affine opens `V` of `Y`
> determined by `g` on global sections (`AlgebraicGeometry.glueHom`), and the 2-isomorphism is
> `AlgebraicGeometry.twoIsoGlueHom`.  Uniqueness is Stacks 04LW
> (`AlgebraicGeometry.eq_of_twoIso_smallEtaleRingedToposHom`).

```lean
theorem existsUnique_schemeHom_twoIso_smallEtaleRingedToposHom (B : BigEtaleSite.{u})
    {X Y : B.Scheme}
    (g : RingedToposHom (RingedSite.toRingedTopos (smallEtaleRingedSite B X.obj X.property))
      (RingedSite.toRingedTopos (smallEtaleRingedSite B Y.obj Y.property)))
    (hg : g.IsLocallyRinged) :
    ∃! f : X ⟶ Y, Nonempty (RingedToposHom.TwoIso.{u, u + 1, u, u, u + 1, u} g
      (smallEtaleRingedToposHom B f))
```

Declarations registered for the tag:

- [`AlgebraicGeometry.eq_of_twoIso_smallEtaleRingedToposHom`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/RingedToposTwoIso.lean#L99), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/RingedToposTwoIso.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/RingedToposTwoIso.lean#L113) (StacksFrontier): “the uniqueness clause, i.e. the faithfulness half of the full faithfulness asserted by the theorem”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.40, Tag 04JH](https://stacks.math.columbia.edu/tag/04JH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
