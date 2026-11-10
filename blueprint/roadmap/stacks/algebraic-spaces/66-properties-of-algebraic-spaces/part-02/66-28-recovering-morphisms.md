---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.smallEtaleRingedToposHom_isLocallyRinged, AlgebraicGeometry.Space.smallEtaleRingedToposHom_twoMorphism_eq_id, AlgebraicGeometry.Space.smallEtaleRingedToposHom_twoMorphismOfRingedTopoi_eq_id, AlgebraicGeometry.Space.eq_of_smallEtaleRingedToposHom_twoIso, AlgebraicGeometry.Space.exists_smallBaseChange_iso_of_twoIso, AlgebraicGeometry.Space.existsUnique_spaceHom_twoIso_of_isLocallyRinged, AlgebraicGeometry.Space.bijective_smallEtaleLocallyRingedClass, AlgebraicGeometry.Space.eq_of_twoIso_smallEtaleRingedToposHom
statement: formalized
proof: formalized
---

# 66.28 Recovering morphisms

Section 66.28 of the Stacks Project, [Tag 04KI](https://stacks.math.columbia.edu/tag/04KI). 5 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04KJ, a lemma

[Tag 04KJ](https://stacks.math.columbia.edu/tag/04KJ) in the Stacks Project.

**`AlgebraicGeometry.Space.smallEtaleRingedToposHom_isLocallyRinged`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRingedToposHomLocallyRinged.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRingedToposHomLocallyRinged.lean#L131).

> For a morphism `f : X ⟶ Y` of algebraic spaces over a scheme `S`, the morphism of small
> étale ringed topoi `(f_small, f♯)` attached to `f` is a morphism of locally ringed topoi: its
> square of units subsheaves is cartesian.
>
> The geometric points of `X` are a conservative family of points of its small étale site, and at
> each of them the fibre of `f⁻¹𝒪_Y ⟶ 𝒪_X` is the map of étale local rings
> `𝒪_{Y, f(x̄)} ⟶ 𝒪_{X, x̄}`, which is a local ring map.

```lean
theorem smallEtaleRingedToposHom_isLocallyRinged :
    (smallEtaleRingedToposHom B S hS f).IsLocallyRinged
```

## Tag 04KK, a lemma

[Tag 04KK](https://stacks.math.columbia.edu/tag/04KK) in the Stacks Project.

**`AlgebraicGeometry.Space.smallEtaleRingedToposHom_twoMorphism_eq_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRingedToposHomRigidity.lean, line 529](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRingedToposHomRigidity.lean#L529).

> **Stacks 04KK.** A 2-endomorphism of the morphism of small étale ringed topoi induced by a
> morphism of algebraic spaces is the identity.

```lean
theorem smallEtaleRingedToposHom_twoMorphism_eq_id
    (t : AlgebraicGeometry.RingedToposHom.TwoMorphism.{u, u + 1, u, u, u + 1, u}
      (smallEtaleRingedToposHom B S hS f)
      (smallEtaleRingedToposHom B S hS f)) :
    t = AlgebraicGeometry.RingedToposHom.TwoMorphism.id
      (smallEtaleRingedToposHom B S hS f)
```

**`AlgebraicGeometry.Space.smallEtaleRingedToposHom_twoMorphismOfRingedTopoi_eq_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleTwoMorphismRigidity.lean, line 720](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleTwoMorphismRigidity.lean#L720).

> **Stacks 04KK.**  A 2-morphism from the morphism of small étale ringed topoi induced by a
> morphism of algebraic spaces to itself is the identity.
>
> The 2-morphism is taken over `(smallEtaleRingedToposHom B S hS f).toRingedToposModulesHom`,
> since `Stacks.Sheaves.RingedToposModules.TwoMorphismOfRingedTopoi` (Stacks 04IC) is defined for
> the four-field `Stacks.Sheaves.RingedToposModules.RingedToposHom`; the two structures are
> equivalent.

```lean
theorem smallEtaleRingedToposHom_twoMorphismOfRingedTopoi_eq_id (f : X ⟶ Y)
    (t : Stacks.Sheaves.RingedToposModules.TwoMorphismOfRingedTopoi.{u, u + 1, u, u, u + 1, u}
      (smallEtaleRingedToposHom B S hS f).toRingedToposModulesHom
      (smallEtaleRingedToposHom B S hS f).toRingedToposModulesHom) :
    t = Stacks.Sheaves.RingedToposModules.TwoMorphismOfRingedTopoi.id.{u, u + 1, u, u, u + 1, u}
      (smallEtaleRingedToposHom B S hS f).toRingedToposModulesHom
```

## Tag 04M6, a lemma

[Tag 04M6](https://stacks.math.columbia.edu/tag/04M6) in the Stacks Project.

**`AlgebraicGeometry.Space.eq_of_smallEtaleRingedToposHom_twoIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleTwoIsoAffineCover.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleTwoIsoAffineCover.lean#L171).

> **Stacks 04M6.** Let `S` be a scheme and let `X, Y` be algebraic spaces over `S`. Two
> morphisms `a, b : X ⟶ Y` of algebraic spaces over `S` for which there exists a 2-isomorphism
> `(a_small, a^♯) ≅ (b_small, b^♯)` in the 2-category of ringed topoi are equal.
>
> No representability is assumed: the general case is reduced to a scheme source by
> `AlgebraicGeometry.Space.eq_of_twoIso_of_schemeSource`, where the two morphisms are
> automatically representable because the diagonal of an algebraic space is.

```lean
theorem eq_of_smallEtaleRingedToposHom_twoIso (a b : X ⟶ Y)
    (t : RingedToposHom.TwoIso.{u, u + 1, u, u, u + 1, u}
      (smallEtaleRingedToposHom B S hS a) (smallEtaleRingedToposHom B S hS b)) :
    a = b
```

**`AlgebraicGeometry.Space.exists_smallBaseChange_iso_of_twoIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleTwoIsoChartComparison.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleTwoIsoChartComparison.lean#L289). The attribute's comment: “the étale-chart comparison of the proof: for two representable morphisms the 2-isomorphism of the morphisms of small étale ringed topoi is, through the 03G8 identification of the direct images with étale-chart base change, restriction along an isomorphism of the chart base-change functors”.

> **The étale-chart comparison of Stacks 04M6.** Let `a, b : X ⟶ Y` be two representable
> morphisms of algebraic spaces whose morphisms of small étale ringed topoi are 2-isomorphic.
> Through the Stacks 03G8 identification of the two direct images with base change of étale scheme
> charts, the 2-isomorphism is restriction along an isomorphism `V ×_{Y,b} X ≅ V ×_{Y,a} X` of the
> chart base-change functors, natural in the étale chart `V` of `Y`.

```lean
theorem exists_smallBaseChange_iso_of_twoIso {X Y : AlgebraicSpaces B S hS} (a b : X ⟶ Y)
    (ha : yoneda.relativelyRepresentable a.hom) (hb : yoneda.relativelyRepresentable b.hom)
    (t : RingedToposHom.TwoIso.{u, u + 1, u, u, u + 1, u}
      (smallEtaleRingedToposHom B S hS a) (smallEtaleRingedToposHom B S hS b)) :
    letI := (smallBaseChange_isMorphismOfSites B S hS a ha).toIsContinuous
    letI := (smallBaseChange_isMorphismOfSites B S hS b hb).toIsContinuous
    ∃ e : smallBaseChange B S hS b hb ≅ smallBaseChange B S hS a ha,
      ∀ (H : Sheaf (SmallEtale.topology B S hS X.obj) (Type u))
        (V : SmallEtale B S hS Y.obj)
        (x : (((smallBaseChange B S hS a ha).sheafPushforwardContinuous (Type u)
          (SmallEtale.topology B S hS Y.obj)
          (SmallEtale.topology B S hS X.obj)).obj H).obj.obj (op V)),
        ((((smallEtaleRingedToposHom_representable B S hS a ha).symm ≪≫ t.e ≪≫
            smallEtaleRingedToposHom_representable B S hS b hb).hom.app H).hom.app (op V)) x =
          H.obj.map (op (e.hom.app V)) x
```

## Tag 04KL, a theorem

[Tag 04KL](https://stacks.math.columbia.edu/tag/04KL) in the Stacks Project.

**`AlgebraicGeometry.Space.existsUnique_spaceHom_twoIso_of_isLocallyRinged`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RecoveringMorphisms/Main.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RecoveringMorphisms/Main.lean#L172).

> **Stacks 04KL.** Let `X` and `Y` be algebraic spaces over `Spec ℤ` (here `Spec (ULift ℤ)`, the
> terminal scheme at the universe of the site) and let
> `(g, g♯) : (Sh(X_étale), 𝒪_X) ⟶ (Sh(Y_étale), 𝒪_Y)` be a morphism of locally ringed topoi.
> Then there is a unique morphism of algebraic spaces `f : X ⟶ Y` such that `(g, g♯)` is
> 2-isomorphic to `(f_small, f♯)` (Stacks 04IC, 03G8).

```lean
theorem existsUnique_spaceHom_twoIso_of_isLocallyRinged (B : BigFppfSite.{u})
    (hZ : B.Contains (Spec (CommRingCat.of (ULift.{u} ℤ))))
    {X Y : AlgebraicSpaces B (Spec (CommRingCat.of (ULift.{u} ℤ))) hZ}
    (g : RingedToposHom (smallEtaleRingedTopos B _ hZ X) (smallEtaleRingedTopos B _ hZ Y))
    (hg : g.IsLocallyRinged) :
    ∃! f : X ⟶ Y, Nonempty (RingedToposHom.TwoIso.{u, u + 1, u, u, u + 1, u} g
      (smallEtaleRingedToposHom B _ hZ f))
```

**`AlgebraicGeometry.Space.bijective_smallEtaleLocallyRingedClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RecoveringMorphisms/Main.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RecoveringMorphisms/Main.lean#L216). The attribute's comment: “the reformulation: X ↦ (X\_étale, 𝒪\_X) is fully faithful, morphisms of locally ringed topoi being taken up to 2-isomorphism”.

> **Stacks 04KL, in the form of full faithfulness.** Over `Spec ℤ`, the construction
> `X ↦ (X_étale, 𝒪_X)` is fully faithful from algebraic spaces to locally ringed topoi, morphisms of
> the latter being taken up to 2-isomorphism: `f ↦ [(f_small, f♯)]` is a bijection from the
> morphisms `X ⟶ Y` of algebraic spaces onto the 2-isomorphism classes of morphisms of locally ringed
> topoi `(Sh(X_étale), 𝒪_X) ⟶ (Sh(Y_étale), 𝒪_Y)`.

```lean
theorem bijective_smallEtaleLocallyRingedClass (B : BigFppfSite.{u})
    (hZ : B.Contains (Spec (CommRingCat.of (ULift.{u} ℤ))))
    (X Y : AlgebraicSpaces B (Spec (CommRingCat.of (ULift.{u} ℤ))) hZ) :
    Function.Bijective (smallEtaleLocallyRingedClass B _ hZ X Y)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.eq_of_twoIso_smallEtaleRingedToposHom`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleTwoIsoAffineCover.lean#L193), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleTwoIsoAffineCover.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleTwoIsoAffineCover.lean#L201) (StacksFrontier): “the uniqueness clause over a base: at most one morphism of algebraic spaces over S induces a given morphism of the small étale ringed topoi. This is the faithfulness half of the asserted full faithfulness, and it needs neither of the theorem's hypotheses — not local ringedness of the morphism of topoi, and not 2-compatibility with structure morphisms to a further base”.

## Tag 05YZ, a lemma

[Tag 05YZ](https://stacks.math.columbia.edu/tag/05YZ) in the Stacks Project.

**`AlgebraicGeometry.Space.existsUnique_spaceHom_twoIso_of_smallEtaleRingedToposIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRingedToposIsoLocallyRinged.lean, line 644](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRingedToposIsoLocallyRinged.lean#L644).

> **Stacks 05YZ.** Let `X` and `Y` be algebraic spaces over `ℤ`, and let
> `(g, g♯) : (Sh(X_étale), 𝒪_X) ⟶ (Sh(Y_étale), 𝒪_Y)` be an isomorphism of ringed topoi: its
> direct image is an equivalence and `g♯ : 𝒪_Y ⟶ g_*𝒪_X` is an isomorphism.  Then there is a
> unique morphism `f : X ⟶ Y` of algebraic spaces such that `(g, g♯)` is 2-isomorphic to
> `(f_small, f♯)` — the morphism of small étale ringed topoi
> `AlgebraicGeometry.Space.smallEtaleRingedToposHom` of Stacks 03G8, a 2-isomorphism being one of
> Stacks 04IC — and that morphism is an isomorphism of algebraic spaces.
>
> As in the source, the existence and uniqueness is Stacks 04KL
> (`AlgebraicGeometry.Space.existsUnique_spaceHom_twoIso_of_isLocallyRinged`), applicable because
> `(g, g♯)` is a morphism of locally ringed topoi
> (`AlgebraicGeometry.Space.isLocallyRinged_of_smallEtaleRingedToposIso`).  For the last clause,
> Stacks 04KL applied to the inverse of `(g, g♯)` and to the inverse of that gives `f'` and `f''`,
> and `AlgebraicGeometry.Space.isIso_of_twoIso_of_inverse` shows that `f` is invertible.

```lean
theorem existsUnique_spaceHom_twoIso_of_smallEtaleRingedToposIso (B : BigFppfSite.{u})
    (hZ : B.Contains (Spec (CommRingCat.of (ULift.{u} ℤ))))
    {X Y : AlgebraicSpaces B (Spec (CommRingCat.of (ULift.{u} ℤ))) hZ}
    (g : RingedToposHom (smallEtaleRingedTopos B (Spec (CommRingCat.of (ULift.{u} ℤ))) hZ X)
      (smallEtaleRingedTopos B (Spec (CommRingCat.of (ULift.{u} ℤ))) hZ Y))
    [g.toToposHom.pushforward.IsEquivalence] [IsIso g.fSharp] :
    (∃! f : X ⟶ Y, Nonempty (RingedToposHom.TwoIso.{u, u + 1, u, u, u + 1, u} g
      (smallEtaleRingedToposHom B (Spec (CommRingCat.of (ULift.{u} ℤ))) hZ f))) ∧
    ∀ f : X ⟶ Y, Nonempty (RingedToposHom.TwoIso.{u, u + 1, u, u, u + 1, u} g
      (smallEtaleRingedToposHom B (Spec (CommRingCat.of (ULift.{u} ℤ))) hZ f)) → IsIso f
```

**`AlgebraicGeometry.Space.existsUnique_spaceHom_twoIso_of_smallEtaleRingedToposIso'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpaceRecoveredFromSmallEtale.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SpaceRecoveredFromSmallEtale.lean#L188). The attribute's comment: “the clause about f ALONE: its existence and uniqueness, together with the 2-isomorphism of (g, g sharp) with (f\_small, f sharp) (Stacks 04IC). Stacks 04KL over a base, which the existence needs, is isRecoveredFromSmallEtale\_holds. The source's further clause that f is an ISOMORPHISM of algebraic spaces lies outside this registration. NARROWER than the source in one further respect: the source states 05YZ for spaces over Spec(Z), where f is an absolute morphism and no compatibility is asked of (g, g sharp), while f here is a morphism over S, so the 2-compatibility hbase is assumed in addition -- it is what Stacks 04SG supplies, and without it the conclusion is FALSE”.

> **[Stacks Project, Tag 05YZ], the clause about `f`.**  If `g` is a morphism of the small
> étale ringed topoi of `X` and `Y` whose direct image is an equivalence and whose structure map
> is an isomorphism, and `g` is 2-compatible with a pair of structure morphisms `pX : X ⟶ A`,
> `pY : Y ⟶ A`, then there is exactly one morphism of algebraic spaces `f : X ⟶ Y` with `g`
> 2-isomorphic to the morphism of small étale ringed topoi of `f`.
>
> This is `AlgebraicGeometry.Space.IsRecoveredFromSmallEtaleOver` at `A`, supplied by
> `AlgebraicGeometry.Space.isRecoveredFromSmallEtale_holds`, applied to `g`: the hypothesis that
> `g` is locally ringed is `AlgebraicGeometry.Space.isLocallyRinged_of_smallEtaleRingedToposIso`,
> and the two 2-isomorphisms are read in the opposite direction from
> `AlgebraicGeometry.Space.InducesSmallEtaleRingedToposHom`.
>
> Only the source's clause about `f` is registered here; its further clause that `f` is an
> isomorphism of algebraic spaces lies outside this statement.
>
> The 2-compatibility `hbase` is not optional: the source states Stacks 05YZ for algebraic spaces
> over `Spec(ℤ)`, where `f` is an absolute morphism, whereas `f : X ⟶ Y` here is a morphism over
> `S`.  Without it the conclusion is false — see the σ-twist counterexample recorded with
> `AlgebraicGeometry.Space.IsRecoveredFromSmallEtale`.  Since
> `AlgebraicGeometry.Space.baseSpace` is terminal, `hbase` can always be asked of the structure
> morphisms to the base itself.

```lean
theorem existsUnique_spaceHom_twoIso_of_smallEtaleRingedToposIso' {A : AlgebraicSpaces B S hS}
    (pX : X ⟶ A) (pY : Y ⟶ A)
    (g : RingedToposHom (smallEtaleRingedTopos B S hS X) (smallEtaleRingedTopos B S hS Y))
    [g.toToposHom.pushforward.IsEquivalence] [IsIso g.fSharp]
    (hbase : Nonempty (SmallEtaleTwoIso B S hS
      (smallEtaleComp B S hS (smallEtaleRingedToposHom B S hS pY) g)
      (smallEtaleRingedToposHom B S hS pX))) :
    ∃! f : X ⟶ Y, Nonempty (RingedToposHom.TwoIso.{u, u + 1, u, u, u + 1, u} g
      (smallEtaleRingedToposHom B S hS f))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 66.28, Tag 04KI](https://stacks.math.columbia.edu/tag/04KI)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
