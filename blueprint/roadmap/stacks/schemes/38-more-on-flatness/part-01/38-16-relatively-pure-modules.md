---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsPureAlong, AlgebraicGeometry.IsUniversallyPureAlong, AlgebraicGeometry.IsSchemePureAlong, AlgebraicGeometry.IsUniversallyPureRelative, AlgebraicGeometry.IsPureRelative, AlgebraicGeometry.IsSchemePureRelative, AlgebraicGeometry.noElementaryEtaleImpurity_of_noQuasiFiniteImpurity, AlgebraicGeometry.noHenselianImpurity_iff_relativeAssassinSpecializesIntoClosedFibre
statement: formalized
proof: formalized
---

# 38.16 Relatively pure modules

Section 38.16 of the Stacks Project, [Tag 05BB](https://stacks.math.columbia.edu/tag/05BB). 7 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05J4, a definition

[Tag 05J4](https://stacks.math.columbia.edu/tag/05J4) in the Stacks Project.

**`AlgebraicGeometry.IsPureAlong`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/Purity.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/Purity.lean#L111). The attribute's comment: “part (1)”.

> A finite type quasi-coherent module is pure along the fibre over the chosen point if no
> impurity occurs over an elementary étale neighbourhood of that point.

```lean
abbrev IsPureAlong (P : PrePureSituation.{u}) : Prop
```

**`AlgebraicGeometry.IsUniversallyPureAlong`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/Purity.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/Purity.lean#L124). The attribute's comment: “part (2)”.

> A finite type quasi-coherent module is universally pure along the fibre over the chosen
> point if no impurity occurs after any base change.

```lean
abbrev IsUniversallyPureAlong (P : PrePureSituation.{u}) : Prop
```

**`AlgebraicGeometry.IsSchemePureAlong`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/Purity.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/Purity.lean#L129). The attribute's comment: “part (3)”.

> The scheme `X` is pure along the fibre over `s` when its structure sheaf is pure there.

```lean
abbrev IsSchemePureAlong {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [QuasiCompact f] (s : S) : Prop
```

**`AlgebraicGeometry.IsUniversallyPureRelative`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/Purity.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/Purity.lean#L143). The attribute's comment: “part (4)”.

> A finite type quasi-coherent module is universally pure relative to the base if it is
> universally pure along every fibre.

```lean
abbrev IsUniversallyPureRelative {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [QuasiCompact f] (F : X.Modules)
    [F.IsFiniteType] [F.IsQuasicoherent] : Prop
```

**`AlgebraicGeometry.IsPureRelative`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/Purity.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/Purity.lean#L156). The attribute's comment: “part (5)”.

> A finite type quasi-coherent module is pure relative to the base if it is pure along every
> fibre.

```lean
abbrev IsPureRelative {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [QuasiCompact f] (F : X.Modules)
    [F.IsFiniteType] [F.IsQuasicoherent] : Prop
```

**`AlgebraicGeometry.IsSchemePureRelative`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/Purity.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/Purity.lean#L169). The attribute's comment: “part (6)”.

> The scheme `X` is pure relative to `S` when its structure sheaf is pure relative to the
> base.

```lean
abbrev IsSchemePureRelative {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [QuasiCompact f] : Prop
```

## Tag 05J5, a remark

[Tag 05J5](https://stacks.math.columbia.edu/tag/05J5) in the Stacks Project.

**`AlgebraicGeometry.noElementaryEtaleImpurity_of_noQuasiFiniteImpurity`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/RelativelyPure/LocallyOfFiniteTypePurity.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/RelativelyPure/LocallyOfFiniteTypePurity.lean#L219). The attribute's comment: “condition (2) implies condition (1)”.

> Condition (2) implies condition (1): an elementary étale neighbourhood is étale, hence
> quasi-finite at its distinguished point.
>
> This is one direction of the equivalence of conditions (1) and (2), and is unconditional. The
> converse is Tag 05J0, whose proof does not use quasi-compactness but which is not available in
> this library, so the equivalence itself is not claimed here.

```lean
theorem noElementaryEtaleImpurity_of_noQuasiFiniteImpurity {f : X ⟶ S} {F : X.Modules} {s : S}
    (h : NoQuasiFiniteImpurity f F s) : NoElementaryEtaleImpurity f F s
```

**`AlgebraicGeometry.noHenselianImpurity_iff_relativeAssassinSpecializesIntoClosedFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/RelativelyPure/LocallyOfFiniteTypePurity.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/RelativelyPure/LocallyOfFiniteTypePurity.lean#L269). The attribute's comment: “conditions (3) and (4) are equivalent”.

> **Stacks Project, Tag 05J5.** For a morphism which is only locally of finite type,
> conditions (3) and (4) are still equivalent: the impurities above `s` whose test family is a
> model of `S^h → S` are exactly the points of `Ass_{X^h/S^h}(ℱ^h)` which fail to specialize into
> the fibre of `X^h` over the closed point of `S^h`.
>
> What makes this work is that the auxiliary data of such an impurity carry no information: its
> distinguished point is forced to be the closed point of the model, because every point of
> `S^h` over `s` is the closed point, and the specialization to it is automatic, because every
> point of the spectrum of a local ring specializes to its closed point.

```lean
theorem noHenselianImpurity_iff_relativeAssassinSpecializesIntoClosedFibre
    [LocallyOfFiniteType f] [F.IsFiniteType] [F.IsQuasicoherent] :
    NoHenselianImpurity f F s Rh ↔ RelativeAssassinSpecializesIntoClosedFibre f F s Rh
```

**`AlgebraicGeometry.noElementaryEtaleImpurity_iff_noQuasiFiniteImpurity`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/RelativelyPure/QuasiFiniteImpurityData.lean, line 285](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/RelativelyPure/QuasiFiniteImpurityData.lean#L285). The attribute's comment: “conditions (1) and (2) are equivalent”.

> **Stacks Project, Tag 05J5.** For a morphism which is only locally of finite type,
> conditions (1) and (2) are still equivalent: an impurity above `s` whose test family is merely
> quasi-finite at its distinguished point can be replaced by one whose test family is an
> elementary étale neighbourhood of `s`.
>
> This is the half of the remark which asserts that the proof of Tag 05J0 does not use
> quasi-compactness of the morphism: that proof is run here for impurity data, which carry no
> such hypothesis.

```lean
theorem noElementaryEtaleImpurity_iff_noQuasiFiniteImpurity {f : X ⟶ S} [LocallyOfFiniteType f]
    {F : X.Modules} [F.IsQuasicoherent] {s : S} :
    NoElementaryEtaleImpurity f F s ↔ NoQuasiFiniteImpurity f F s
```

## Tag 05J6, a lemma

[Tag 05J6](https://stacks.math.columbia.edu/tag/05J6) in the Stacks Project.

**`AlgebraicGeometry.isUniversallyPureAlong_iff_forall_baseChange_isPureAlong`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/RelativelyPure/BaseChange.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/RelativelyPure/BaseChange.lean#L70). The attribute's comment: “the pointed-fibre equivalence”.

> **Stacks Project, Tag 05J6.** Universal purity along the chosen fibre can be tested by
> purity after every pointed base change.

```lean
public theorem isUniversallyPureAlong_iff_forall_baseChange_isPureAlong
    (P : PrePureSituation.{u}) :
    IsUniversallyPureAlong P ↔
      ∀ (Q : PrePureSituation.{u}) (g : Q.S ⟶ P.S)
        (_hg : g.base Q.s = P.s) (toX : Q.X ⟶ P.X)
        (_hpb : IsPullback toX Q.f P.f g)
        (_hF : Q.F ≅ (Scheme.Modules.pullback toX).obj P.F),
          IsPureAlong Q
```

**`AlgebraicGeometry.isUniversallyPureRelative_iff_forall_baseChange_isPureRelative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/RelativelyPure/BaseChange.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/RelativelyPure/BaseChange.lean#L117). The attribute's comment: “the relative equivalence”.

> **Stacks Project, Tag 05J6, in particular.** Universal purity over the base can be tested
> by purity relative to every base change.

```lean
public theorem isUniversallyPureRelative_iff_forall_baseChange_isPureRelative
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f] [QuasiCompact f]
    (F : X.Modules) [F.IsFiniteType] [F.IsQuasicoherent] :
    IsUniversallyPureRelative f F ↔
      ∀ {X' S' : Scheme.{u}} (f' : X' ⟶ S')
        [LocallyOfFiniteType f'] [QuasiCompact f']
        (F' : X'.Modules) [F'.IsFiniteType] [F'.IsQuasicoherent]
        (g : S' ⟶ S) (toX : X' ⟶ X)
        (_hpb : IsPullback toX f' f g)
        (_hF : F' ≅ (Scheme.Modules.pullback toX).obj F),
          IsPureRelative f' F'
```

## Tag 05J7, a lemma

[Tag 05J7](https://stacks.math.columbia.edu/tag/05J7) in the Stacks Project.

**`AlgebraicGeometry.isPureAlong_of_quasiFiniteAt_of_isPureAlong`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/RelativelyPure/QuasiFinitePointedBaseChange.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/RelativelyPure/QuasiFinitePointedBaseChange.lean#L54).

> **Stacks Project, Tag 05J7.** If a morphism of pointed schemes `(S', s') → (S, s)` is
> quasi-finite at `s'` and a finite type quasi-coherent module is pure along the fibre over `s`,
> then its pullback to the base change is pure along the fibre over `s'`.

```lean
public theorem isPureAlong_of_quasiFiniteAt_of_isPureAlong {P Q : PrePureSituation.{u}}
    (g : Q.S ⟶ P.S) (hg : g.base Q.s = P.s) (toX : Q.X ⟶ P.X)
    (hpb : IsPullback toX Q.f P.f g)
    (hF : Q.F ≅ (Scheme.Modules.pullback toX).obj P.F)
    (hqf : quasiFiniteAt g Q.s) (hP : IsPureAlong P) :
    IsPureAlong Q
```

## Tag 05J8, a lemma

[Tag 05J8](https://stacks.math.columbia.edu/tag/05J8) in the Stacks Project.

**`AlgebraicGeometry.isPureAlong_iff_isUniversallyPureAlong_of_isNoetherianRing_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/RelativelyPure/NoetherianStalk.lean, line 218](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/RelativelyPure/NoetherianStalk.lean#L218).

> **Stacks Project, Tag 05J8.** Let `f : X ⟶ S` be of finite type, let `ℱ` be a finite type
> quasi-coherent `𝒪_X`-module and let `s` be a point of `S` whose local ring `𝒪_{S, s}` is
> Noetherian. Then `ℱ` is pure along the fibre `X_s` if and only if it is universally pure
> along `X_s`.

```lean
theorem isPureAlong_iff_isUniversallyPureAlong_of_isNoetherianRing_stalk
    (P : PrePureSituation.{u}) [IsNoetherianRing (P.S.presheaf.stalk P.s)] :
    IsPureAlong P ↔ IsUniversallyPureAlong P
```

## Tag 05J9, a lemma

[Tag 05J9](https://stacks.math.columbia.edu/tag/05J9) in the Stacks Project.

**`AlgebraicGeometry.isPureAlong_of_flatPointedBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningStratification/PurityDescent.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningStratification/PurityDescent.lean#L102). The attribute's comment: “flat\_descend\_pure”.

> **Stacks Project, Tag 05J9.** Purity along the original fibre follows from purity along the
> fibre of a pointed base change which is flat at its distinguished point.

```lean
public theorem isPureAlong_of_flatPointedBaseChange (H : FlatPointedBaseChangeSituation.{u})
    (P' : PrePureSituation.{u}) (eS : P'.S = H.S') (eX : P'.X = pullback H.f H.g)
    (hf : eqToHom eX.symm ≫ P'.f ≫ eqToHom eS = pullback.snd H.f H.g)
    (hF : HEq P'.F ((Scheme.Modules.pullback (pullback.fst H.f H.g)).obj H.F))
    (hs : eS ▸ P'.s = H.s') (hpure : IsPureAlong P') :
    IsPureAlong ({ S := H.S, X := H.X, f := H.f, F := H.F, s := H.s } :
      PrePureSituation.{u})
```

**`AlgebraicGeometry.universallyPureAlong_of_flatPointedBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningStratification/PurityDescent.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningStratification/PurityDescent.lean#L180). The attribute's comment: “flat\_descend\_universally\_pure”.

> **Stacks Project, Tag 05J9.** Universal purity along a fibre descends through a pointed base
> change which is flat at the new distinguished point.

```lean
public theorem universallyPureAlong_of_flatPointedBaseChange
    (H : FlatPointedBaseChangeSituation.{u})
    (h : IsUniversallyPureAlong H.baseChangedSituation) :
    IsUniversallyPureAlong ({ S := H.S, X := H.X, f := H.f, F := H.F, s := H.s } :
      PrePureSituation.{u})
```

## Tag 05K1, a lemma

[Tag 05K1](https://stacks.math.columbia.edu/tag/05K1) in the Stacks Project.

**`AlgebraicGeometry.isPureAlong_iff_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/RelativelyPure/FinitePushforward.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/RelativelyPure/FinitePushforward.lean#L201). The attribute's comment: “purity along the fibre”.

> **Stacks Project, Tag 05K1.** Purity along a fibre is unchanged by pushing a finite type
> quasi-coherent module forward along a closed immersion.

```lean
theorem isPureAlong_iff_pushforward :
    IsPureAlong (prePureSituationComp i f F s) ↔
      IsPureAlong (prePureSituationPushforward i f F s)
```

**`AlgebraicGeometry.isUniversallyPureAlong_iff_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/RelativelyPure/FinitePushforward.lean, line 225](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/RelativelyPure/FinitePushforward.lean#L225). The attribute's comment: “universal purity along the fibre”.

> **Stacks Project, Tag 05K1.** Universal purity along a fibre is unchanged by pushing a finite
> type quasi-coherent module forward along a closed immersion.

```lean
theorem isUniversallyPureAlong_iff_pushforward :
    IsUniversallyPureAlong (prePureSituationComp i f F s) ↔
      IsUniversallyPureAlong (prePureSituationPushforward i f F s)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.16, Tag 05BB](https://stacks.math.columbia.edu/tag/05BB)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
