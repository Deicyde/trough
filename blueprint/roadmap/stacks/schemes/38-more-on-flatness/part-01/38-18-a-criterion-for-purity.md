---
declaration: section
origin: cited
lean: Stacks.RelativeAssassin.exists_specializes_mem_associatedPoints_fibre, AlgebraicGeometry.isPureAlong_iff_relativeAssassin_specializing_mem_range_of_associatedPoints, AlgebraicGeometry.isUniversallyPureAlong_of_isPureAlong, AlgebraicGeometry.isPureRelative_of_isUniversallyPureRelative, AlgebraicGeometry.isUniversallyPureRelative_of_isPureRelative, AlgebraicGeometry.isPureRelative_iff_isUniversallyPureRelative, AlgebraicGeometry.isPureRelative_iff_isUniversallyPureRelative_of_isLocallyNoetherian, AlgebraicGeometry.exists_stage_isPureAlong_of_isLimit
statement: formalized
proof: formalized
---

# 38.18 A criterion for purity

Section 38.18 of the Stacks Project, [Tag 05L2](https://stacks.math.columbia.edu/tag/05L2). 6 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05L3, a lemma

[Tag 05L3](https://stacks.math.columbia.edu/tag/05L3) in the Stacks Project.

**`Stacks.RelativeAssassin.exists_specializes_mem_associatedPoints_fibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeAssassin/FlatFibreSpecialization.lean, line 273](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeAssassin/FlatFibreSpecialization.lean#L273).

> **Stacks Project, Tag 05L3: a criterion for purity.** Let `f : X ⟶ S` be locally of finite
> type and `F` a quasi-coherent `𝒪_X`-module of finite type which is flat over `S` at every point
> of the fibre `X_s`. A point of `Ass_{X/S}(F)` which specializes to some point of `X_s`
> specializes to a point of `X_s` associated to the restriction of `F` to `X_s`.

```lean
theorem exists_specializes_mem_associatedPoints_fibre
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType] (s : S)
    (hflat : ∀ t : f.fiber s, IsFlatOverAt f.toLRSHom.toShHom F (f.fiberι s t))
    {x' : X} (hx' : x' ∈ Stacks.Divisors.relativeAssassin f F)
    (hmeets : ∃ t : f.fiber s, x' ⤳ f.fiberι s t) :
    ∃ x : f.fiber s, x' ⤳ f.fiberι s x ∧
      x ∈ Stacks.Divisors.associatedPoints
        ((Scheme.Modules.pullback (f.fiberι s)).obj F)
```

## Tag 05L4, a lemma

[Tag 05L4](https://stacks.math.columbia.edu/tag/05L4) in the Stacks Project.

**`AlgebraicGeometry.isPureAlong_iff_relativeAssassin_specializing_mem_range_of_associatedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/PurityCriterion.lean, line 603](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/PurityCriterion.lean#L603).

> **Stacks Project, Tag 05L4.** Let `f : X ⟶ S` be of finite type, let `ℱ` be a finite type
> quasi-coherent `𝒪_X`-module and let `s ∈ S`. Let `(S', s') ⟶ (S, s)` be an elementary étale
> neighbourhood and let `g : X' ⟶ X` and `p : X' ⟶ S'` form a commutative square over `S' ⟶ S`.
> Assume
>
> 1. `ℱ` is flat over `S` at all points of `X_s`,
> 2. `p : X' ⟶ S'` is of finite type,
> 3. `g^*ℱ` is pure along `X'_{s'}`,
> 4. `g : X' ⟶ X` is étale, and
> 5. `g(X'_{s'})` contains `Ass_{X_s}(ℱ_s)`.
>
> Then `ℱ` is pure along `X_s` if and only if the image of `X' ⟶ X ×_S S'` contains the points of
> `Ass_{X ×_S S'/S'}(ℱ ×_S S')` lying over points of `S'` which specialize to `s'`.
>
> The source states (5) as `g(X') ⊇ Ass_{X_s}(ℱ_s)`. With that reading the statement is false, by
> `Stacks.Examples.not_forall_isPureAlong_iff_of_associatedPoints_subset_range`: take
> `X = S`, `ℱ = 𝒪_S`, `S' = S ⨿ S` with `s'` in the first copy and `X' = S` mapping onto the second
> copy. The proof of the source, which first replaces `S` by `S'`, uses (5) for the fibre over `s'`,
> as stated here.
>
> Hypothesis (5) is moved to the fibre of `X ×_S S'` over `s'` by Tag 05DC
> (`AlgebraicGeometry.mem_relativeAssassin_pullback_iff`), and a point of that fibre is pinned down
> by its image in `X` (`AlgebraicGeometry.pullbackLift_eq_fiberι_of_fst_eq`).

```lean
public theorem isPureAlong_iff_relativeAssassin_specializing_mem_range_of_associatedPoints
    {X S X' : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f] [QuasiCompact f]
    (F : X.Modules) [F.IsFiniteType] [F.IsQuasicoherent]
    (s : S) (U : EtaleNeighborhood S s) (hU : U.IsElementary)
    (p : X' ⟶ U.scheme) [LocallyOfFiniteType p] [QuasiCompact p]
    (g : X' ⟶ X) [Etale g] (hcomm : g ≫ f = p ≫ U.toBase)
    (hflat : ∀ x : f.fiber s, IsFlatOverAt f.toLRSHom.toShHom F (f.fiberι s x))
    (hpure' : IsPureAlong
      ({ S := U.scheme
         X := X'
         f := p
         F := (Scheme.Modules.pullback g).obj F
         isFiniteType := SheafOfModules.pullback_isFiniteType g.toLRSHom.toShHom F
         isQuasicoherent := by
           have hF : F.IsQuasicoherent := inferInstance
           exact @SheafOfModules.modulePullback_isQuasicoherent X'.toRingedSpace
             X.toRingedSpace g.toLRSHom.toShHom F hF
         s := U.point } : PrePureSituation.{u}))
    (hass : ∀ z : f.fiber s,
      z ∈ Stacks.Divisors.associatedPoints ((Scheme.Modules.pullback (f.fiberι s)).obj F) →
        f.fiberι s z ∈ g '' (p ⁻¹' {U.point})) :
    IsPureAlong ({ S := S, X := X, f := f, F := F, s := s } : PrePureSituation.{u}) ↔
      ∀ x : pullback (C := Scheme.{u}) f U.toBase,
        x ∈ Stacks.Divisors.relativeAssassin (pullback.snd f U.toBase)
            ((Scheme.Modules.pullback (pullback.fst f U.toBase)).obj F) →
          pullback.snd f U.toBase x ⤳ U.point →
            x ∈ Set.range (pullback.lift g p hcomm)
```

## Tag 05L5, a lemma

[Tag 05L5](https://stacks.math.columbia.edu/tag/05L5) in the Stacks Project.

**`AlgebraicGeometry.isUniversallyPureAlong_of_isPureAlong`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/UniversalPurityCriterion.lean, line 403](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/UniversalPurityCriterion.lean#L403).

> **Stacks Project, Tag 05L5.** Let `f : X ⟶ S` be of finite type, let `ℱ` be a finite type
> quasi-coherent `𝒪_X`-module, and let `s : S`. If `ℱ` is flat over `S` at every point of the fibre
> `X_s` and pure along `X_s`, then `ℱ` is universally pure along `X_s`.
>
> The inputs are Tag 05L1, which produces an affine étale chart of the whole fibre with free
> sections after an elementary étale localization of the base, Tag 05K6, which makes that chart
> universally pure over the local base, Tag 05L4, which converts the resulting containment of the
> relative assassin into purity after an arbitrary base change, the unconditional half of Tag 05KL,
> which propagates that containment along a base change, and Tags 05J7 and 05J9, which transport
> purity and universal purity along the elementary étale neighbourhood and the localization.

```lean
public theorem isUniversallyPureAlong_of_isPureAlong
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f] [QuasiCompact f]
    (F : X.Modules) [F.IsFiniteType] [F.IsQuasicoherent] (s : S)
    (hflat : ∀ x : f.fiber s, IsFlatOverAt f.toLRSHom.toShHom F (f.fiberι s x))
    (hpure : IsPureAlong ({ S := S, X := X, f := f, F := F, s := s } : PrePureSituation.{u})) :
    IsUniversallyPureAlong ({ S := S, X := X, f := f, F := F, s := s } :
      PrePureSituation.{u})
```

## Tag 05L6, a lemma

[Tag 05L6](https://stacks.math.columbia.edu/tag/05L6) in the Stacks Project.

**`AlgebraicGeometry.isPureRelative_of_isUniversallyPureRelative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/PurityIffUniversalPurity.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/PurityIffUniversalPurity.lean#L58). The attribute's comment: “the implication universally pure relative to S implies pure relative to S, with no flatness and no Noetherian hypothesis”.

> **Stacks Project, Tag 05L6**, the implication which needs no hypothesis on the base: a
> finite type quasi-coherent module which is universally pure relative to the base is pure
> relative to the base, there being fewer impurity diagrams to exclude.

```lean
theorem isPureRelative_of_isUniversallyPureRelative {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [QuasiCompact f] (F : X.Modules)
    [F.IsFiniteType] [F.IsQuasicoherent] (h : IsUniversallyPureRelative f F) :
    IsPureRelative f F
```

**`AlgebraicGeometry.isUniversallyPureRelative_of_isPureRelative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/PurityIffUniversalPurity.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/PurityIffUniversalPurity.lean#L69). The attribute's comment: “the implication pure relative to S implies universally pure relative to S, for a module flat over S, with no hypothesis on S”.

> **Stacks Project, Tag 05L6**, the harder implication. Let `f : X ⟶ S` be of finite type and
> let `ℱ` be a finite type quasi-coherent `𝒪_X`-module which is flat over `S`. If `ℱ` is pure
> relative to `S` then it is universally pure relative to `S`.

```lean
theorem isUniversallyPureRelative_of_isPureRelative {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [QuasiCompact f] (F : X.Modules)
    [F.IsFiniteType] [F.IsQuasicoherent] (hflat : IsFlatOver f.toLRSHom.toShHom F)
    (h : IsPureRelative f F) :
    IsUniversallyPureRelative f F
```

**`AlgebraicGeometry.isPureRelative_iff_isUniversallyPureRelative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/PurityIffUniversalPurity.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/PurityIffUniversalPurity.lean#L81).

> **Stacks Project, Tag 05L6.** Let `f : X ⟶ S` be of finite type and let `ℱ` be a finite type
> quasi-coherent `𝒪_X`-module which is flat over `S`. Then `ℱ` is pure relative to `S` if and only
> if it is universally pure relative to `S`.

```lean
theorem isPureRelative_iff_isUniversallyPureRelative {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [QuasiCompact f] (F : X.Modules)
    [F.IsFiniteType] [F.IsQuasicoherent] (hflat : IsFlatOver f.toLRSHom.toShHom F) :
    IsPureRelative f F ↔ IsUniversallyPureRelative f F
```

**`AlgebraicGeometry.isPureRelative_iff_isUniversallyPureRelative_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/PurityIffUniversalPurity.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/PurityIffUniversalPurity.lean#L94). The attribute's comment: “a strengthening over a locally Noetherian base: Tag 05J8 replaces Tag 05L5 and needs no flatness, so the flatness hypothesis of the source is dropped here”.

> **Stacks Project, Tag 05L6** over a locally Noetherian base, where the flatness hypothesis
> is unnecessary. Let `f : X ⟶ S` be of finite type and let `ℱ` be a finite type quasi-coherent
> `𝒪_X`-module. If `S` is locally Noetherian then `ℱ` is pure relative to `S` if and only if it is
> universally pure relative to `S`.

```lean
theorem isPureRelative_iff_isUniversallyPureRelative_of_isLocallyNoetherian
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f] [QuasiCompact f]
    [IsLocallyNoetherian S] (F : X.Modules) [F.IsFiniteType] [F.IsQuasicoherent] :
    IsPureRelative f F ↔ IsUniversallyPureRelative f F
```

## Tag 05MA, a lemma

[Tag 05MA](https://stacks.math.columbia.edu/tag/05MA) in the Stacks Project.

**`AlgebraicGeometry.exists_stage_isPureAlong_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/PurityCriterionLimits.lean, line 340](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/PurityCriterionLimits.lean#L340). The attribute's comment: “assuming the limit descent as hdescend and the purity step as hstage”.

> **Stacks Project, Tag 05MA.** Let `(S_i)` be an inverse system of affine schemes over a
> directed index with limit `S`, let `s ∈ S` with images `s_i`, let `f : X ⟶ S` be of finite
> presentation and let `ℱ` be a quasi-coherent `𝒪_X`-module of finite presentation which is pure
> along `X_s` and flat over `S` at every point of `X_s`. Then the whole situation descends to a
> finite stage: some `i` carries a finite-presentation morphism `X_i ⟶ S_i` and a finitely
> presented quasi-coherent module `ℱ_i` which is pure along `(X_i)_{s_i}` and flat over `S_i` at
> every point of that fibre, with `X = X_i ×_{S_i} S` and `ℱ` the pullback of `ℱ_i`.
>
> The descent of the morphism, the module, the open flat locus and the flatness, which is Stacks
> Limits 01ZM, 01ZR, 01ZS and 05LY, is the hypothesis `hdescend`; the passage of purity to a
> finite stage, which is the second half of the proof of the source and uses Stacks 05KW, 05K6,
> 05L4, 05KR and Limits 05F4, is the hypothesis `hstage`.

```lean
public theorem exists_stage_isPureAlong_of_isLimit
    {I : Type u} [Category.{u} I] [IsCofiltered I]
    (D : I ⥤ Scheme.{u}) [∀ i : I, IsAffine (D.obj i)] (c : Cone D) (_hc : IsLimit c)
    {X : Scheme.{u}} (f : X ⟶ c.pt)
    [LocallyOfFinitePresentation f] [QuasiCompact f] [QuasiSeparated f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFinitePresentation] [F.IsFiniteType] (s : c.pt)
    (_hpure : IsPureAlong ({ S := c.pt, X := X, f := f, F := F,
                             s := s } : PrePureSituation.{u}))
    (_hflat : ∀ x : f.fiber s, IsFlatOverAt f.toLRSHom.toShHom F (f.fiberι s x))
    (hdescend : ∃ (i : I) (Xi : Scheme.{u}) (fi : Xi ⟶ D.obj i)
      (_ : LocallyOfFinitePresentation fi) (_ : QuasiCompact fi) (_ : QuasiSeparated fi)
      (Fi : Xi.Modules) (_ : Fi.IsFiniteType) (_ : Fi.IsQuasicoherent)
      (_ : Fi.IsFinitePresentation) (a : X ⟶ Xi),
      IsPullback a f fi (c.π.app i) ∧ Nonempty (F ≅ (Scheme.Modules.pullback a).obj Fi) ∧
        ∀ x : fi.fiber (c.π.app i s),
          IsFlatOverAt fi.toLRSHom.toShHom Fi (fi.fiberι (c.π.app i s) x))
    (hstage : ∀ (i : I) (Xi : Scheme.{u}) (fi : Xi ⟶ D.obj i)
      (_ : LocallyOfFinitePresentation fi) (_ : QuasiCompact fi) (_ : QuasiSeparated fi)
      (Fi : Xi.Modules) (_ : Fi.IsFiniteType) (_ : Fi.IsQuasicoherent)
      (_ : Fi.IsFinitePresentation) (a : X ⟶ Xi), IsPullback a f fi (c.π.app i) →
      Nonempty (F ≅ (Scheme.Modules.pullback a).obj Fi) →
      (∀ x : fi.fiber (c.π.app i s),
        IsFlatOverAt fi.toLRSHom.toShHom Fi (fi.fiberι (c.π.app i s) x)) →
      ∃ (j : I) (e : j ⟶ i) (_ : LocallyOfFiniteType (pullback.snd fi (D.map e)))
        (_ : QuasiCompact (pullback.snd fi (D.map e)))
        (_ : ((Scheme.Modules.pullback (pullback.fst fi (D.map e))).obj Fi).IsFiniteType)
        (_ : ((Scheme.Modules.pullback (pullback.fst fi (D.map e))).obj Fi).IsQuasicoherent),
        IsPureAlong ({ S := D.obj j, X := pullback fi (D.map e),
                       f := pullback.snd fi (D.map e),
                       F := (Scheme.Modules.pullback (pullback.fst fi (D.map e))).obj Fi,
                       s := c.π.app j s } : PrePureSituation.{u})) :
    ∃ (i : I) (Xi : Scheme.{u}) (fi : Xi ⟶ D.obj i) (_ : LocallyOfFinitePresentation fi)
      (_ : QuasiCompact fi) (_ : QuasiSeparated fi) (Fi : Xi.Modules) (_ : Fi.IsFiniteType)
      (_ : Fi.IsQuasicoherent) (_ : Fi.IsFinitePresentation) (a : X ⟶ Xi),
      IsPullback a f fi (c.π.app i) ∧ Nonempty (F ≅ (Scheme.Modules.pullback a).obj Fi) ∧
        (∀ x : fi.fiber (c.π.app i s),
          IsFlatOverAt fi.toLRSHom.toShHom Fi (fi.fiberι (c.π.app i s) x)) ∧
        IsPureAlong ({ S := D.obj i, X := Xi, f := fi, F := Fi,
                       s := c.π.app i s } : PrePureSituation.{u})
```

**`AlgebraicGeometry.exists_stage_isPureAlong_of_isLimit_directed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/PurityLimitStage.lean, line 612](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/PurityLimitStage.lean#L612).

> **Stacks Project, Tag 05MA.** Let `I` be a directed set, let `(S_k)` be an inverse system of
> affine schemes indexed by `I` with limit `S`, let `s` be a point of `S` with images `s_k`, let
> `f : X ⟶ S` be of finite presentation and let `ℱ` be a quasi-coherent `𝒪_X`-module of finite
> presentation which is pure along `X_s` and flat over `S` at every point of `X_s`. Then the whole
> situation descends to a finite stage: some `k` carries a finite-presentation morphism
> `X_k ⟶ S_k` and a finitely presented quasi-coherent module `ℱ_k` which is pure along
> `(X_k)_{s_k}` and flat over `S_k` at every point of that fibre, with `X = X_k ×_{S_k} S` and `ℱ`
> the pullback of `ℱ_k`.
>
> The descent of the morphism, of the module and of the flatness over the open locus where it
> holds — Stacks Limits 01ZM, 01ZR, 01Z4 and 05LY — is
> `AlgebraicGeometry.exists_stage_isFlatOverAt_fiber_of_isLimit`; the passage of purity to a finite
> stage, which is the rest of the proof of the source, is
> `AlgebraicGeometry.exists_stage_isPureAlong`.

```lean
public theorem exists_stage_isPureAlong_of_isLimit_directed {I : Type u} [Preorder I]
    [IsDirected I (· ≤ ·)] [Nonempty I] (D : Iᵒᵖ ⥤ Scheme.{u}) [∀ k : Iᵒᵖ, IsAffine (D.obj k)]
    (c : Cone D) (hc : IsLimit c) {X : Scheme.{u}} (f : X ⟶ c.pt)
    [LocallyOfFinitePresentation f] [QuasiCompact f] [QuasiSeparated f]
    (F : X.Modules) [F.IsFinitePresentation] [F.IsQuasicoherent] (s : c.pt)
    (hpure : IsPureAlong ({ S := c.pt, X := X, f := f, F := F, s := s } : PrePureSituation.{u}))
    (hflat : ∀ x : f.fiber s,
      IsFlatOverAt f.toLRSHom.toShHom F (f.fiberι s x)) :
    ∃ (k : I) (Xk : Scheme.{u}) (fk : Xk ⟶ D.obj (op k))
      (_ : LocallyOfFinitePresentation fk) (_ : QuasiCompact fk) (_ : QuasiSeparated fk)
      (Fk : Xk.Modules) (_ : Fk.IsQuasicoherent) (_ : Fk.IsFinitePresentation)
      (_ : Fk.IsFiniteType) (a : X ⟶ Xk),
      IsPullback a f fk (c.π.app (op k)) ∧ Nonempty (F ≅ (Scheme.Modules.pullback a).obj Fk) ∧
        (∀ x : fk.fiber (c.π.app (op k) s),
          IsFlatOverAt fk.toLRSHom.toShHom Fk (fk.fiberι (c.π.app (op k) s) x)) ∧
        IsPureAlong ({ S := D.obj (op k), X := Xk, f := fk, F := Fk,
                       s := c.π.app (op k) s } : PrePureSituation.{u})
```

## Tag 05MC, a lemma

[Tag 05MC](https://stacks.math.columbia.edu/tag/05MC) in the Stacks Project.

**`AlgebraicGeometry.isOpen_setOf_isPureAlong`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/PurityCriterionLimits.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/PurityCriterionLimits.lean#L162). The attribute's comment: “using Stacks 05KR, proved outright in this library”.

> **Stacks Project, Tag 05MC.** For a morphism `f : X ⟶ S` of finite presentation and a
> quasi-coherent `𝒪_X`-module `ℱ` of finite presentation which is flat over `S`, the set of points
> `s ∈ S` at which `ℱ` is pure along the fibre `X_s` is open in `S`.
>
> The local constructibility of the fibrewise containment locus, Tag 05KR, which the argument
> applies to the base change of `f`, is proved outright in this library.

```lean
public theorem isOpen_setOf_isPureAlong
    {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFinitePresentation f] [QuasiCompact f] [QuasiSeparated f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFinitePresentation] [F.IsFiniteType]
    (hflat : ∀ x : X, IsFlatOverAt f.toLRSHom.toShHom F x) :
    IsOpen {s : S | IsPureAlong ({ S := S, X := X, f := f, F := F,
                                   s := s } : PrePureSituation.{u})}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.18, Tag 05L2](https://stacks.math.columbia.edu/tag/05L2)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
