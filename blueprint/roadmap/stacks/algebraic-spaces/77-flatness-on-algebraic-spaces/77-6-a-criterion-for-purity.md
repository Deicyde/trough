---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_specializes_isRelativeWeaklyAssociatedPoint_fibre_schemeBase, AlgebraicGeometry.Space.relativeWeaklyAssociatedPoints_baseChange_subset_range, AlgebraicGeometry.Space.EtaleOverSource.isPureAbove_of_isPureAbove_situation, AlgebraicGeometry.Space.EtaleOverSource.isUniversallyPureAbove_of_isUniversallyPureAbove_situation, AlgebraicGeometry.Space.EtaleOverSource.relativeWeaklyAssociatedPoints_subset_range_of_isAffineLocalAt, AlgebraicGeometry.Space.EtaleOverSource.relativeWeaklyAssociatedPoints_subset_range_of_isFlatOver_fibre_of_isAffineLocalAt, AlgebraicGeometry.Space.isPureAbove_of_isEtale_of_subset_range, AlgebraicGeometry.Space.relativeWeaklyAssociatedPoints_subset_range_of_isEtale
statement: formalized
proof: formalized
---

# 77.6 A criterion for purity

Section 77.6 of the Stacks Project, [Tag 0CW0](https://stacks.math.columbia.edu/tag/0CW0). 6 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CW1, a lemma

[Tag 0CW1](https://stacks.math.columbia.edu/tag/0CW1) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_specializes_isRelativeWeaklyAssociatedPoint_fibre_schemeBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/PuritySchemeBase.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/PuritySchemeBase.lean#L182). The attribute's comment: “the source's own statement, unconditionally: the base is a scheme of the site (the source's S), flatness is read on the module, Stacks 05VV at a point, exactly as the source reads it, and nothing further is required of the data -- in particular no affineness, the affine etale chart being chosen inside the proof as the source chooses it”.

> **Stacks 0CW1.** Let `X` be a decent algebraic space over a scheme `S` of a big fppf site,
> let `f : X ⟶ h_V` be a morphism locally of finite type into the algebraic space of a scheme `V`
> of the site, let `F` be a finite type quasi-coherent `𝒪_X`-module, and let `s` be a point of
> `|h_V|` such that `F` is flat over `h_V` at every point of the fibre `X_s`. If a point `x'` of
> the relative weak assassin `WeakAss_{X/V}(F)` specializes to a point of `X_s` — that is, if the
> closure of `{x'}` in `|X|` meets `|X_s|` — then it specializes to a point of `WeakAss_{X/V}(F)`
> lying over `s`, so that closure meets `WeakAss_{X/V}(F) ∩ |X_s|`.
>
> The source's `Ass_{X/S}(ℱ)` is the relative weak assassin of Stacks 0CV0, which it writes that
> way because a morphism locally of finite type has locally Noetherian fibres (Stacks 0CUY); its
> flatness hypothesis "`ℱ` is flat over `S` at all points of `X_s`" is flatness of the *module*
> over the target at the points of the fibre, which is
> `AlgebraicGeometry.Space.IsFlatOverAtPoint`, Stacks 05VV at a point.
>
> The two companions in `StacksFrontier/AlgebraicGeometry/Spaces/Flat/PuritySpecialization.lean`
> generalize the base to an arbitrary algebraic space and carry the chart criterion as a
> hypothesis; neither of them is registered against this tag, which is registered here.

```lean
theorem exists_specializes_isRelativeWeaklyAssociatedPoint_fibre_schemeBase
    (V : BigFppfOver B S hS) {X : AlgebraicSpaces B S hS} (f : X ⟶ schemeSpace V)
    (hXdec : IsDecentSpace B S hS X.1) (hf : IsLocallyOfFiniteType B S hS f.hom)
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite]
    [SheafOfModules.IsFiniteTypeOnSite F] (s : points B S hS (schemeSpace V).1)
    (hflat : ∀ t : points B S hS X.1, pointsMap B S hS X.1 f.hom t = s →
      IsFlatOverAtPoint B S hS X.2 f.hom F t)
    {x' : points B S hS X.1} (hx' : IsRelativeWeaklyAssociatedPoint B S hS f F x')
    (hmeets : ∃ t : points B S hS X.1, x' ⤳ t ∧ pointsMap B S hS X.1 f.hom t = s) :
    ∃ x : points B S hS X.1, x' ⤳ x ∧ pointsMap B S hS X.1 f.hom x = s ∧
      IsRelativeWeaklyAssociatedPoint B S hS f F x
```

## Tag 0CW2, a lemma

[Tag 0CW2](https://stacks.math.columbia.edu/tag/0CW2) in the Stacks Project.

**`AlgebraicGeometry.Space.relativeWeaklyAssociatedPoints_baseChange_subset_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceBaseChange.lean, line 289](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceBaseChange.lean#L289). The attribute's comment: “for the relative weak assassin of Stacks 0CV0, stated for an arbitrary module in place of a quasi-coherent one and with no finiteness hypothesis on f, neither of which is used by part (1) of Stacks 0CV2 or by Stacks 03H4. The base changes are presented by cartesian squares, X'\_Z as X\_Z ×\_X X' exactly as the source's proof does, so g is not required to be given as a morphism over Y”.

> Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S`, let `g : X'' ⟶ X` be a
> morphism of algebraic spaces, and let `F` be an `𝒪_X`-module. If `WeakAss_{X/Y}(F)` is
> contained in the image of `|X''| → |X|`, then for every `Z ⟶ Y` the set `WeakAss_{X_Z/Z}(F_Z)`
> is contained in the image of `|X''_Z| → |X_Z|`, where `X_Z = X ×_Y Z` and
> `X''_Z = X_Z ×_X X''`.

```lean
theorem relativeWeaklyAssociatedPoints_baseChange_subset_range
    {X Y Z X'' XZ X'Z : AlgebraicSpaces B S hS} {f : X ⟶ Y} {g : X'' ⟶ X} {h : Z ⟶ Y}
    {pZ : XZ ⟶ X} {qZ : XZ ⟶ Z} {gZ : X'Z ⟶ XZ} {rZ : X'Z ⟶ X''}
    (sq : IsPullback pZ.hom qZ.hom f.hom h.hom)
    (sq' : IsPullback gZ.hom rZ.hom pZ.hom g.hom) (F : Modules.{u, u} B S hS X.1 X.2)
    (hF : relativeWeaklyAssociatedPoints B S hS f F ⊆
      Set.range (pointsMap B S hS X''.1 g.hom)) :
    relativeWeaklyAssociatedPoints B S hS qZ ((modulePullback B S hS pZ).obj F) ⊆
      Set.range (pointsMap B S hS X'Z.1 gZ.hom)
```

## Tag 0CW3, a lemma

[Tag 0CW3](https://stacks.math.columbia.edu/tag/0CW3) in the Stacks Project.

**`AlgebraicGeometry.Space.EtaleOverSource.isPureAbove_of_isPureAbove_situation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityEtaleMorphism.lean, line 464](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityEtaleMorphism.lean#L464). The attribute's comment: “clause (1) for purity above y: the source's own two assumptions on the etale morphism g, that Ass\_\{X/Y}(F) lies in the image of |X'| and that g^*F is pure above y, give purity of F above y. Nothing beyond the source's own assumptions is used”.

> **Stacks 0CW3, clause (1), for purity above `y`.** In the situation of Stacks 0CV6, let
> `g : X' ⟶ X` be étale over `Y` with `X' ⟶ Y` decent and of finite type. If the relative
> assassin `Ass_{X/Y}(ℱ)` lies in the image of `|X'| → |X|` and `g^*ℱ` is pure above `y`, then
> `ℱ` is pure above `y`.
>
> An impurity of `ℱ` above `y` whose structure morphism is quasi-finite at `t` lifts to such an
> impurity of `g^*ℱ` above `y`: the containment passes to the base change by Stacks 0CW2, which
> lifts the distinguished point, and Stacks 0CUZ makes the lift relatively associated.
>
> The containment of the assassin and purity of `g^*ℱ` are the two assumptions the source's own
> clause (1) makes, and nothing further is assumed.  In particular the containment is not obtained
> from clause (2) of the same tag: clause (2) produces it from purity of `ℱ` above `y` — which is
> the conclusion here — over an affine local base whose fibre is met by the image, so none of its
> three inputs is available at clause (1).

```lean
theorem isPureAbove_of_isPureAbove_situation
    (hass : relativeWeaklyAssociatedPoints B S hS P.structureSpaceMorphism P.F ⊆
      Set.range (pointsMap B S hS c.X'.1 c.g.hom))
    (h : IsPureAbove c.situation) : IsPureAbove P
```

**`AlgebraicGeometry.Space.EtaleOverSource.isUniversallyPureAbove_of_isUniversallyPureAbove_situation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityEtaleMorphism.lean, line 486](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityEtaleMorphism.lean#L486). The attribute's comment: “clause (1) for universal purity above y: the source's own two assumptions on the etale morphism g, that Ass\_\{X/Y}(F) lies in the image of |X'| and that g^*F is universally pure above y, give universal purity of F above y. Nothing beyond the source's own assumptions is used”.

> **Stacks 0CW3, clause (1), for universal purity above `y`.** In the situation of
> Stacks 0CV6, let `g : X' ⟶ X` be étale over `Y` with `X' ⟶ Y` decent and of finite type. If
> the relative assassin `Ass_{X/Y}(ℱ)` lies in the image of `|X'| → |X|` and `g^*ℱ` is
> universally pure above `y`, then `ℱ` is universally pure above `y`.
>
> Any impurity of `ℱ` above `y` lifts to an impurity of `g^*ℱ` above `y`.
>
> The containment of the assassin and universal purity of `g^*ℱ` are the two assumptions the
> source's own clause (1) makes, and nothing further is assumed.

```lean
theorem isUniversallyPureAbove_of_isUniversallyPureAbove_situation
    (hass : relativeWeaklyAssociatedPoints B S hS P.structureSpaceMorphism P.F ⊆
      Set.range (pointsMap B S hS c.X'.1 c.g.hom))
    (h : IsUniversallyPureAbove c.situation) : IsUniversallyPureAbove P
```

**`AlgebraicGeometry.Space.EtaleOverSource.relativeWeaklyAssociatedPoints_subset_range_of_isAffineLocalAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityEtaleMorphism.lean, line 789](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityEtaleMorphism.lean#L789). The attribute's comment: “clause (2): purity of F above y, the image of |X'| meeting the whole fibre and an affine local base with closed point y give the containment of Ass\_\{X/Y}(F) in that image. Those are the source's own three assumptions, and nothing beyond them is used”.

> **Stacks 0CW3, clause (2), with nothing granted.** In the situation of Stacks 0CV6, let
> `g : X' ⟶ X` be étale over `Y` with `X' ⟶ Y` decent and of finite type. If `ℱ` is pure above
> `y`, the image of `|X'| → |X|` contains the fibre `F = f^{-1}(\{y\})`, and `Y` is affine local
> with closed point `y`, then that image contains the whole relative assassin `Ass_{X/Y}(ℱ)`.
>
> This is `AlgebraicGeometry.Space.EtaleOverSource.relativeWeaklyAssociatedPoints_subset_range`
> with its specialization step discharged by
> `AlgebraicGeometry.Space.purityFibreSpecialization`, so that only the source's own hypotheses
> remain.

```lean
theorem relativeWeaklyAssociatedPoints_subset_range_of_isAffineLocalAt
    (hlocal : P.IsAffineLocalAt) (hpure : IsPureAbove P)
    (hfibre : pointsMap B S hS P.X P.f ⁻¹' {P.y} ⊆
      Set.range (pointsMap B S hS c.X'.1 c.g.hom)) :
    relativeWeaklyAssociatedPoints B S hS P.structureSpaceMorphism P.F ⊆
      Set.range (pointsMap B S hS c.X'.1 c.g.hom)
```

**`AlgebraicGeometry.Space.EtaleOverSource.relativeWeaklyAssociatedPoints_subset_range_of_isFlatOver_fibre_of_isAffineLocalAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityEtaleMorphism.lean, line 952](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityEtaleMorphism.lean#L952). The attribute's comment: “clause (3): purity of F above y, flatness of the module F over Y at the points of the fibre, the image of |X'| meeting Ass\_\{X/Y}(F) cap F and an affine local base with closed point y give the containment of Ass\_\{X/Y}(F) in that image. Those are the source's own four assumptions, and nothing beyond them is used”.

> **Stacks 0CW3, clause (3), with nothing granted.** In the situation of Stacks 0CV6, let
> `g : X' ⟶ X` be étale over `Y` with `X' ⟶ Y` decent and of finite type. If `ℱ` is pure above
> `y`, `ℱ` is flat over `Y` at every point of the fibre `F = f^{-1}(\{y\})`, the image of
> `|X'| → |X|` contains `Ass_{X/Y}(ℱ) ∩ F`, and `Y` is affine local with closed point `y`, then
> that image contains the whole relative assassin `Ass_{X/Y}(ℱ)`.
>
> The flatness hypothesis is the source's own: flatness of the *module* `ℱ` over `Y` at the
> points of the fibre, `AlgebraicGeometry.Space.IsFlatOverAtPoint`, Stacks 05VV at a point in the
> some-chart form which is condition (1) of Stacks 05VU — and not flatness of the morphism `f`,
> which is the incomparable condition of
> `relativeWeaklyAssociatedPoints_subset_range_of_isFlatAt_fibre_of_isAffineLocalAt` in this
> namespace.
>
> This is `relativeWeaklyAssociatedPoints_subset_range_of_isFlatOver_fibre` in this namespace
> with its specialization step discharged by
> `AlgebraicGeometry.Space.purityFibreSpecialization`, so that nothing beyond the source's own
> hypotheses is assumed.

```lean
theorem relativeWeaklyAssociatedPoints_subset_range_of_isFlatOver_fibre_of_isAffineLocalAt
    (hlocal : P.IsAffineLocalAt) (hpure : IsPureAbove P)
    (hflat : ∀ t : points B S hS P.X, pointsMap B S hS P.X P.f t = P.y →
      IsFlatOverAtPoint B S hS P.hX P.f P.F t)
    (hfibre : relativeWeaklyAssociatedPoints B S hS P.structureSpaceMorphism P.F ∩
        pointsMap B S hS P.X P.f ⁻¹' {P.y} ⊆
      Set.range (pointsMap B S hS c.X'.1 c.g.hom)) :
    relativeWeaklyAssociatedPoints B S hS P.structureSpaceMorphism P.F ⊆
      Set.range (pointsMap B S hS c.X'.1 c.g.hom)
```

**`AlgebraicGeometry.Space.isPureAbove_of_isEtale_of_subset_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityEtaleMorphismClauses.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityEtaleMorphismClauses.lean#L210). The attribute's comment: “clause (1), both the pure and the universally pure reading, under exactly the source's hypotheses”.

> **Stacks 0CW3, clause (1).** Let `Y` be an algebraic space over `S`, let `f : X ⟶ Y` be
> decent and of finite type, `ℱ` a finite type quasi-coherent `𝒪_X`-module and `y ∈ |Y|` (the
> pre-pure situation `P`), and let `g : X' ⟶ X` be étale with `X' ⟶ Y` decent and of finite type.
> If `Ass_{X/Y}(ℱ) ⊆ g(|X'|)` and `g^*ℱ` is pure above `y`, then `ℱ` is pure above `y`; and if
> `Ass_{X/Y}(ℱ) ⊆ g(|X'|)` and `g^*ℱ` is universally pure above `y`, then `ℱ` is universally
> pure above `y`.
>
> The situation on `X'` carrying `g^*ℱ` is
> `(EtaleOverSource.ofIsEtale P X' g hg hft hdec).situation`. The relative assassin `Ass_{X/Y}(ℱ)`
> is the relative weak assassin of Stacks 0CV0, which is the set the source writes `Ass_{X/Y}(ℱ)`
> since `f` is of finite type.

```lean
theorem isPureAbove_of_isEtale_of_subset_range (hg : IsEtale B S hS g.hom)
    (hft : IsFiniteType B S hS (g.hom ≫ P.f)) (hdec : IsDecent B S hS (g.hom ≫ P.f))
    (hass : relativeWeaklyAssociatedPoints B S hS P.structureSpaceMorphism P.F ⊆
      Set.range (pointsMap B S hS X'.1 g.hom)) :
    (IsPureAbove (EtaleOverSource.ofIsEtale P X' g hg hft hdec).situation → IsPureAbove P) ∧
      (IsUniversallyPureAbove (EtaleOverSource.ofIsEtale P X' g hg hft hdec).situation →
        IsUniversallyPureAbove P)
```

**`AlgebraicGeometry.Space.relativeWeaklyAssociatedPoints_subset_range_of_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityEtaleMorphismClauses.lean, line 231](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityEtaleMorphismClauses.lean#L231). The attribute's comment: “clause (2), under exactly the source's hypotheses”.

> **Stacks 0CW3, clause (2).** In the situation of clause (1), if `ℱ` is pure above `y`, the
> image `g(|X'|)` contains the fibre `F = f^{-1}(\{y\})`, and `Y` is affine local with closed point
> `y`, then `Ass_{X/Y}(ℱ) ⊆ g(|X'|)`.
>
> The proof is the source's: the image of an étale morphism is open (Stacks 03IR), and purity
> over the affine local base specializes every point of `Ass_{X/Y}(ℱ)` into `F`
> (`AlgebraicGeometry.Space.purityFibreSpecialization`).  Decency and finiteness of type of
> `X' ⟶ Y`, which the source assumes throughout the lemma, are not used by this clause, so the
> statement omits them and is that much more general.

```lean
theorem relativeWeaklyAssociatedPoints_subset_range_of_isEtale (hg : IsEtale B S hS g.hom)
    (hpure : IsPureAbove P)
    (hfibre : pointsMap B S hS P.X P.f ⁻¹' {P.y} ⊆ Set.range (pointsMap B S hS X'.1 g.hom))
    (hlocal : P.IsAffineLocalAt) :
    relativeWeaklyAssociatedPoints B S hS P.structureSpaceMorphism P.F ⊆
      Set.range (pointsMap B S hS X'.1 g.hom)
```

**`AlgebraicGeometry.Space.relativeWeaklyAssociatedPoints_subset_range_of_isEtale_of_isFlatOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityEtaleMorphismClauses.lean, line 255](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityEtaleMorphismClauses.lean#L255). The attribute's comment: “clause (3), under exactly the source's hypotheses; flatness is flatness of the module over Y at the points of the fibre, as in the source”.

> **Stacks 0CW3, clause (3).** In the situation of clause (1), if `ℱ` is pure above `y`, `ℱ`
> is flat over `Y` at all points of the fibre `F = f^{-1}(\{y\})` (Stacks 05VV at a point), the
> image `g(|X'|)` contains `Ass_{X/Y}(ℱ) ∩ F`, and `Y` is affine local with closed point `y`, then
> `Ass_{X/Y}(ℱ) ⊆ g(|X'|)`.
>
> As in the source: the image of an étale morphism is open (Stacks 03IR), purity over the affine
> local base specializes every point of `Ass_{X/Y}(ℱ)` into `F`
> (`AlgebraicGeometry.Space.purityFibreSpecialization`), and Stacks 0CW1 over the base, which is
> isomorphic to a scheme of the site, improves that to a specialization into
> `Ass_{X/Y}(ℱ) ∩ F`.  As for clause (2), decency and finiteness of type of `X' ⟶ Y` are not used,
> so the statement omits them and is that much more general.

```lean
theorem relativeWeaklyAssociatedPoints_subset_range_of_isEtale_of_isFlatOver
    (hg : IsEtale B S hS g.hom) (hpure : IsPureAbove P)
    (hflat : ∀ t : points B S hS P.X, pointsMap B S hS P.X P.f t = P.y →
      IsFlatOverAtPoint B S hS P.hX P.f P.F t)
    (hfibre : relativeWeaklyAssociatedPoints B S hS P.structureSpaceMorphism P.F ∩
        pointsMap B S hS P.X P.f ⁻¹' {P.y} ⊆ Set.range (pointsMap B S hS X'.1 g.hom))
    (hlocal : P.IsAffineLocalAt) :
    relativeWeaklyAssociatedPoints B S hS P.structureSpaceMorphism P.F ⊆
      Set.range (pointsMap B S hS X'.1 g.hom)
```

## Tag 0CW4, a lemma

[Tag 0CW4](https://stacks.math.columbia.edu/tag/0CW4) in the Stacks Project.

**`AlgebraicGeometry.Space.isUniversallyPureAbove_of_flat_of_isPureAbove`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/UniversalPurityOfFlatPure.lean, line 330](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/UniversalPurityOfFlatPure.lean#L330).

> **Stacks 0CW4.** In the situation of Stacks 0CV6 — a decent, finite type morphism
> `f : X ⟶ Y` of algebraic spaces over `S`, a finite type quasi-coherent `𝒪_X`-module `ℱ` and a
> point `y` of `Y` — if `ℱ` is flat over `Y` at every point of `X` lying over `y` and `ℱ` is pure
> above `y`, then `ℱ` is universally pure above `y`.
>
> See the module docstring for the proof: Stacks 0CVW and 05L1 over an affine elementary étale
> neighbourhood `V` of the base, the descent of Stacks 0CVG part (2) along the flat morphism
> `Spec 𝒪_{V, v} ⟶ Y`, both parts of Stacks 0CW3 over `Spec 𝒪_{V, v}`, and Stacks 05K6 for the
> affine scheme with free global sections that Stacks 05L1 produces.

```lean
theorem isUniversallyPureAbove_of_flat_of_isPureAbove (P : PrePureSituation.{u, u} B S hS)
    (hflat : ∀ x : points B S hS P.X, pointsMap B S hS P.X P.f x = P.y →
      x ∈ flatLocus B S hS P.hX P.f P.F)
    (hpure : IsPureAbove P) :
    IsUniversallyPureAbove P
```

## Tag 0CW5, a lemma

[Tag 0CW5](https://stacks.math.columbia.edu/tag/0CW5) in the Stacks Project.

**`AlgebraicGeometry.Space.isPureRelative_iff_isUniversallyPureRelative_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/UniversalPurityOfFlatPure.lean, line 551](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/UniversalPurityOfFlatPure.lean#L551).

> **Stacks 0CW5.** In the situation of Stacks 0CV6 — a decent, finite type morphism
> `f : X ⟶ Y` of algebraic spaces over `S` and a finite type quasi-coherent `𝒪_X`-module `ℱ` — if
> `ℱ` is flat over `Y`, then `ℱ` is pure relative to `Y` if and only if it is universally pure
> relative to `Y`.
>
> The forward implication is Stacks 0CW4 at each point of `Y`,
> `AlgebraicGeometry.Space.isUniversallyPureRelative_of_flat_of_isPureRelative`; the reverse one is
> formal and holds with no flatness, by
> `AlgebraicGeometry.Space.IsPureRelative.of_isUniversallyPureRelative`.

```lean
theorem isPureRelative_iff_isUniversallyPureRelative_of_flat (P : PrePureSituation.{u, u} B S hS)
    (hflat : ∀ x : points B S hS P.X, x ∈ flatLocus B S hS P.hX P.f P.F) :
    IsPureRelative P ↔ IsUniversallyPureRelative P
```

## Tag 0CW6, a lemma

[Tag 0CW6](https://stacks.math.columbia.edu/tag/0CW6) in the Stacks Project.

**`AlgebraicGeometry.Space.mono_unit_of_relativeWeaklyAssociatedPoints_subset_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityFlatInjection.lean, line 470](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityFlatInjection.lean#L470). The attribute's comment: “the injectivity assertion”.

> **Stacks 0CW6, injectivity.**  Let `Y` be an algebraic space over a scheme `S`, let
> `g : X' ⟶ X` be a flat morphism of algebraic spaces over `Y` with `X` locally of finite type
> over `Y` through `f : X ⟶ Y`, and let `F` be a finite type quasi-coherent `𝒪_X`-module which is
> flat over `Y`.  If the relative assassin `Ass_{X/Y}(F)` is contained in the image of `|X'|`
> then the canonical map `F ⟶ g_*g^*F` — the unit of the adjunction of Stacks 03LU — is a
> monomorphism.
>
> The kernel of the canonical map is zero by
> `AlgebraicGeometry.Space.isZero_of_comp_unit_eq_zero`, which is the source's argument; the
> hypotheses are the tag's own.

```lean
theorem mono_unit_of_relativeWeaklyAssociatedPoints_subset_range
    {X' X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (g : X' ⟶ X)
    (hf : IsLocallyOfFiniteType B S hS f.hom) (hg : IsFlat B S hS g.hom)
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite] [F.IsFiniteType]
    (hF : IsFlatOver B S hS X.2 f.hom F)
    (hass : relativeWeaklyAssociatedPoints B S hS f F ⊆
      Set.range (pointsMap B S hS X'.1 g.hom)) :
    Mono ((modulePullbackAdjunction B S hS g).unit.app F)
```

**`AlgebraicGeometry.Space.mono_unit_baseChange_of_relativeWeaklyAssociatedPoints_subset_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityFlatInjection.lean, line 502](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityFlatInjection.lean#L502). The attribute's comment: “the base-change assertion”.

> **Stacks 0CW6, injectivity after an arbitrary base change.**  In the situation of
> Stacks 0CW6, for every morphism `h : Z ⟶ Y` the canonical map
> `F_Z ⟶ (g_Z)_*g_Z^*F_Z` is a monomorphism as well.
>
> The base changes are presented by cartesian squares, `X_Z` as `X ×_Y Z` and `X'_Z` as
> `X_Z ×_X X'`, exactly as the source's proof does, so `g` is not required to be given as a
> morphism over `Y`.  This is the source's own deduction: every hypothesis of the first half
> survives the base change, and the containment of the relative assassin does so by
> Stacks 0CW2.  Concretely
>
> * `f_Z : X_Z ⟶ Z` is locally of finite type by Stacks 03XH;
> * `g_Z : X'_Z ⟶ X_Z` is flat by Stacks 03MO;
> * `F_Z = p^*F` is quasi-coherent by Stacks 03GA and of finite type by Stacks 03DL(5), both
>   with no hypothesis on `p`;
> * `F_Z` is flat over `Z` by Stacks 05VW;
> * `Ass_{X_Z/Z}(F_Z) ⊆ g_Z(|X'_Z|)` by Stacks 0CW2.
>
> All five are proved, so the hypotheses are the tag's own.

```lean
theorem mono_unit_baseChange_of_relativeWeaklyAssociatedPoints_subset_range
    {X' X Y Z XZ X'Z : AlgebraicSpaces B S hS} (f : X ⟶ Y) (g : X' ⟶ X) (h : Z ⟶ Y)
    (p : XZ ⟶ X) (fZ : XZ ⟶ Z) (q : X'Z ⟶ X') (gZ : X'Z ⟶ XZ)
    (hp : IsPullback p fZ f h) (hq : IsPullback q gZ g p)
    (hf : IsLocallyOfFiniteType B S hS f.hom) (hg : IsFlat B S hS g.hom)
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite] [F.IsFiniteType]
    (hF : IsFlatOver B S hS X.2 f.hom F)
    (hass : relativeWeaklyAssociatedPoints B S hS f F ⊆
      Set.range (pointsMap B S hS X'.1 g.hom)) :
    Mono ((modulePullbackAdjunction B S hS gZ).unit.app
      ((modulePullback B S hS p).obj F))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 77.6, Tag 0CW0](https://stacks.math.columbia.edu/tag/0CW0)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
