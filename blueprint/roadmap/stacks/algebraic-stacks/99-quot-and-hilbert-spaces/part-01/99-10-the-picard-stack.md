---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.picardToCoherent, AlgebraicGeometry.Space.range_subset_fibrewiseEtaleRankOneFreeLocus_of_isInvertibleModule, AlgebraicGeometry.Space.hasOpenLocus_picardToCoherent, AlgebraicGeometry.Space.isRepresentableByAlgebraicSpaces_and_isOpenImmersion_picardToCoherent, AlgebraicGeometry.Space.picardObjectToCoherent, AlgebraicGeometry.Space.isOpen_fibrewiseEtaleFreeLocus, AlgebraicGeometry.Space.isOpen_fibrewiseEtaleRankOneFreeLocus, AlgebraicGeometry.Space.range_pointsMap_relativeMap_subset_etaleFreeLocus
statement: formalized
proof: formalized
---

# 99.10 The Picard stack

Section 99.10 of the Stacks Project, [Tag 0D02](https://stacks.math.columbia.edu/tag/0D02). 2 tags here are carried by 13 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0D03, a lemma

[Tag 0D03](https://stacks.math.columbia.edu/tag/0D03) in the Stacks Project.

**`AlgebraicGeometry.Space.picardToCoherent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackOpenImmersion.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackOpenImmersion.lean#L240). The attribute's comment: “the natural map Picardstack\_\{X/B} -> Cohstack\_\{X/B} as a 1-morphism of categories fibred in groupoids, (T, g, L) going to (T, g, L), for f flat and proper, f of finite presentation being part of the standing data D of Situation 08KB”.

> The natural map `Pic_{X/B} ⟶ Coh_{X/B}` as a 1-morphism of categories fibred in groupoids
> over the big fppf site of `S`.

```lean
def picardToCoherent (D : CoherentSituation B S hS) (hflat : IsFlat B S hS D.f.hom)
    (hproper : IsProper B S hS D.f.hom) :
    picardCFG (modulePushforwardCoherence B S hS) D.toPicardSituation ⟶ coherentCFG D
```

**`AlgebraicGeometry.Space.range_subset_fibrewiseEtaleRankOneFreeLocus_of_isInvertibleModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackOpenImmersion.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackOpenImmersion.lean#L328). The attribute's comment: “part two of the proof, the implication (b) => (a) complete, at the source's own U = T \ f\_T(|X\_T| \ W\_1) and the source's own condition (b): if F\_T' is invertible then |T'| maps into U. The hypotheses on F are 0CZT's own three conditions, which an object of Coh\_\{X/Y} has.”.

> If the pullback `F_{T'}` of an object `F` of `Coh_{X/Y}` along `X_g : X_{T'} ⟶ X_T` is
> invertible, then `|T'|` maps into `U = T ∖ f_T(|X_T| ∖ W₁)`.

```lean
theorem range_subset_fibrewiseEtaleRankOneFreeLocus_of_isInvertibleModule
    (D : CoherentSituation B S hS) {T' T : SchemesOver D.Y} (g : T' ⟶ T)
    (F : Modules.{u, u} B S hS (D.space T).1 (D.space T).2)
    (hqc : F.IsQuasicoherentOnSite) (hfp : F.IsFinitePresentationOnSite)
    (hflat : IsFlatOver B S hS (D.space T).2 (D.projection T).hom F)
    (hF : IsInvertibleModule (D.space T') ((modulePullback B S hS (D.relativeMap g)).obj F)) :
    Set.range (pointsMap B S hS ((schemeSpaceFunctor B S hS).obj T'.left).1
        ((schemeSpaceFunctor B S hS).map g.left).hom) ⊆
      fibrewiseEtaleRankOneFreeLocus D T F
```

**`AlgebraicGeometry.Space.hasOpenLocus_picardToCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackOpenImmersion.lean, line 423](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackOpenImmersion.lean#L423). The attribute's comment: “part two of the proof, the open subscheme U of every object (T, g, F) of Cohstack\_\{X/B}, read on scheme-valued points: an object over the base factors through U exactly when its image comes from Picardstack\_\{X/B}”.

> **The open locus of the natural map.**  For every scheme-valued point `y` of `Coh_{X/Y}`
> over an object `U` of the big fppf site of `S`, there is an open subscheme `V ⊆ U` through which
> an object `T` of the big fppf site of `U` factors exactly when `y(T)` comes from `Pic_{X/Y}`.

```lean
theorem hasOpenLocus_picardToCoherent (D : CoherentSituation B S hS)
    (hflat : IsFlat B S hS D.f.hom) (hproper : IsProper B S hS D.f.hom) :
    Stack.HasOpenLocus B S hS (picardToCoherentBased D hflat hproper)
```

**`AlgebraicGeometry.Space.isRepresentableByAlgebraicSpaces_and_isOpenImmersion_picardToCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackOpenImmersion.lean, line 477](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackOpenImmersion.lean#L477). The attribute's comment: “the whole statement: the natural map Picardstack\_\{X/B} -> Cohstack\_\{X/B}, for f flat, of finite presentation (the standing data D of Situation 08KB) and proper, is representable by algebraic spaces and an open immersion in the sense of Tag 04XB, which together are representability by open immersions (Tag 04YL (1))”.

> Let `f : X ⟶ B` be a morphism of algebraic spaces over `S` which is flat, of finite
> presentation and proper, given by the data `D` of Situation 08KB with `hflat` and `hproper`.  The
> natural map `Pic_{X/B} ⟶ Coh_{X/B}` is representable by open immersions: it is representable by
> algebraic spaces (Stacks 02ZW), and every algebraic space representing its base change along a
> scheme-valued point of `Coh_{X/B}` is an open subspace of that scheme (Stacks 04XB at open
> immersions).

```lean
theorem isRepresentableByAlgebraicSpaces_and_isOpenImmersion_picardToCoherent
    (D : CoherentSituation B S hS) (hflat : IsFlat B S hS D.f.hom)
    (hproper : IsProper B S hS D.f.hom) :
    Stack.IsRepresentableByAlgebraicSpaces B S hS (picardToCoherent D hflat hproper).hom ∧
      Stack.IsOpenImmersion B S hS (picardToCoherent D hflat hproper)
```

**`AlgebraicGeometry.Space.picardObjectToCoherent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackOpenInCoherentStack.lean, line 687](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackOpenInCoherentStack.lean#L687). The attribute's comment: “part one of the proof, the well-definedness of the natural map, on objects: the triple (T, g, L) of Section 0372 goes to the same triple in Situation 08KB. All three conditions 08KB imposes are proved, with no hypothesis beyond the tag's own flatness and properness of f. Finite presentation of an invertible module -- and with it quasi-coherence -- is Tag 0B8N(b) on the small etale site. The two citations the source makes are performed: the projection X\_T -> T is flat by Tag 03MO and proper by Tag 04WP (isFlat\_projection, isProper\_projection). Their module-theoretic halves are isFlatOver\_of\_isInvertibleModule (Tag 05VV, through the geometric-stalk criterion and Tag 05VX(1), the geometric stalk of an invertible module being free of rank one) and isProperOver\_supportOfSheaf\_of\_isInvertibleModule (Tag 0CZD, the support being closed by Tag 07TZ and proper over the base by Tag 04XY). What remains of the tag is the second part of its proof, the open locus in T.”.

> **Stacks 0D03, the first part of the proof: the natural map `Pic_{X/B} ⟶ Coh_{X/B}` on
> objects.**  A triple `(T, g, L)` of the Picard stack of Section 0372 is sent to the same triple
> `(T, g, L)` viewed in Situation 08KB.
>
> The three conditions of Situation 08KB hold for an invertible `L` for the reasons the source
> gives, and all three are proved.  Finite presentation is
> `AlgebraicGeometry.Space.isFinitePresentationOnSite_of_isInvertibleModule` and quasi-coherence
> follows from it.  Flatness over `T` is
> `AlgebraicGeometry.Space.isFlatOver_of_isInvertibleModule` applied to the projection `X_T ⟶ T`,
> which is flat by Stacks 03MO.  Properness of the support over `T` is
> `AlgebraicGeometry.Space.isProperOver_supportOfSheaf_of_isInvertibleModule` applied to the same
> projection, which is proper by Stacks 04WP and therefore locally of finite type.

```lean
def picardObjectToCoherent (D : CoherentSituation B S hS) (hflat : IsFlat B S hS D.f.hom)
    (hproper : IsProper B S hS D.f.hom)
    (A : PicardObject D.toPicardSituation) : CoherentObject D
```

**`AlgebraicGeometry.Space.isOpen_fibrewiseEtaleFreeLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackOpenInCoherentStack.lean, line 887](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackOpenInCoherentStack.lean#L887). The attribute's comment: “part two of the proof, the construction of the open T \ f\_T(|X\_T| \ W) and its openness, unconditionally, as an open SUBSET of |T| for the point topology -- realizing it as an open subscheme of T is done in hasOpenLocus\_picardToCoherent of Quot/PicardStackOpenImmersion.lean. W is the etale free locus of Tag 0CZT, open by the mechanism of that tag's openness clause (isOpen\_of\_etale\_witness); the projection X\_T -> T is proper by Tag 04WP, hence closed on points. This is the FIRST of the source's two reductions only; the source's own U is the same construction at the RANK-ONE locus, isOpen\_fibrewiseEtaleRankOneFreeLocus, which performs both reductions at once. The source's parenthetical quasi-compactness assumption on T is not needed for either: it belongs to the decomposition X\_T = X\_0 + X\_1 + ... by rank, which the rank-one locus makes unnecessary.”.

> **Stacks 0D03, the construction of the open `U` of the second part of the proof.**  The locus
> is open in `|T|` when `f` is proper.
>
> The étale free locus is open, so its complement is closed, and the projection `|X_T| ⟶ |T|` is a
> closed map because `X_T ⟶ T` is proper by Stacks 04WP; the image of that complement is therefore
> closed and the locus, its complement, is open.

```lean
theorem isOpen_fibrewiseEtaleFreeLocus (D : CoherentSituation B S hS)
    (hf : IsProper B S hS D.f.hom) (T : SchemesOver D.Y)
    (F : Modules.{u, u} B S hS (D.space T).1 (D.space T).2) :
    IsOpen (fibrewiseEtaleFreeLocus D T F)
```

**`AlgebraicGeometry.Space.isOpen_fibrewiseEtaleRankOneFreeLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackOpenInCoherentStack.lean, line 911](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackOpenInCoherentStack.lean#L911). The attribute's comment: “part two of the proof, the construction of the open U = T \ f\_T(|X\_T| \ W\_1) and its openness, unconditionally, as an open SUBSET of |T| for the point topology -- realizing it as an open subscheme of T is done in hasOpenLocus\_picardToCoherent of Quot/PicardStackOpenImmersion.lean. W\_1 is the locus of Tag 0CZT with the rank pinned to ONE, and this U is the source's own U: it is the composite of the source's two reductions, since |X\_T| \ W\_1 = (|X\_T| \ W) + X\_0 + X\_2 + ..., so the source's decomposition of a finite locally free module by rank is not needed and neither is its parenthetical quasi-compactness assumption on T. Openness of W\_1 is the mechanism of the openness clause of 0CZT (isOpen\_of\_etale\_witness) and the projection X\_T -> T is proper by Tag 04WP, hence closed on points.”.

> **Stacks 0D03, the construction of the open `U` of the second part of the proof, at the
> source's own `U`.**  The rank-one locus is open in `|T|` when `f` is proper.
>
> The rank-one étale free locus `W₁` is open with no hypothesis
> (`AlgebraicGeometry.Space.isOpen_etaleRankOneFreeLocus`, the mechanism of the openness clause of
> Stacks 0CZT), and the projection `|X_T| ⟶ |T|` is a closed map because `X_T ⟶ T` is proper by
> Stacks 04WP; so the image of the closed complement is closed and the locus is open.  No
> decomposition of `X_T` by rank is used, and so no quasi-compactness of `T`.

```lean
theorem isOpen_fibrewiseEtaleRankOneFreeLocus (D : CoherentSituation B S hS)
    (hf : IsProper B S hS D.f.hom) (T : SchemesOver D.Y)
    (F : Modules.{u, u} B S hS (D.space T).1 (D.space T).2) :
    IsOpen (fibrewiseEtaleRankOneFreeLocus D T F)
```

**`AlgebraicGeometry.Space.range_pointsMap_relativeMap_subset_etaleFreeLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackOpenInCoherentStack.lean, line 967](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackOpenInCoherentStack.lean#L967). The attribute's comment: “part two of the proof, the implication (a) => (b) on points, unconditionally: if |T'| maps into U -- which is how condition (a), that T' -> T factors through U, is read here, U being produced as an open subset of |T| -- then |X\_T'| maps into the etale free locus W of F. This is the direction that needs no base-change property of W, as the source's own argument shows; it is the commutation of X\_g with the projections to the test schemes together with the description of U as the points whose whole fibre lies in W. The remaining step needs neither the rank decomposition nor a conditional clause of Tag 0B8Q: the rank decomposition is not needed at all -- pinning the rank to one at the level of the locus replaces it, see range\_pointsMap\_relativeMap\_subset\_etaleRankOneFreeLocus -- and the clause of Tag 0B8Q the step would use is the UNCONDITIONAL one, which holds at this site. What the step does need is recorded on that rank-one statement.”.

> **Stacks 0D03, the implication (a) ⟹ (b) of the second part of the proof, on points.**  If a
> morphism `g : T' ⟶ T` of test schemes over `Y` maps `|T'|` into the locus, then the induced
> morphism `X_g : X_{T'} ⟶ X_T` maps `|X_{T'}|` into the étale free locus of `F`.
>
> A point `x'` of `|X_{T'}|` goes to a point `x` of `|X_T|` lying over the image in `|T|` of the
> point of `|T'|` below `x'`, because `X_g` commutes with the two projections to the test schemes;
> that image lies in the locus, so `x` lies in the étale free locus.  No base-change property of
> the locus is used.

```lean
theorem range_pointsMap_relativeMap_subset_etaleFreeLocus (D : CoherentSituation B S hS)
    {T' T : SchemesOver D.Y} (g : T' ⟶ T)
    (F : Modules.{u, u} B S hS (D.space T).1 (D.space T).2)
    (hg : Set.range (pointsMap B S hS ((schemeSpaceFunctor B S hS).obj T'.left).1
        ((schemeSpaceFunctor B S hS).map g.left).hom) ⊆ fibrewiseEtaleFreeLocus D T F) :
    Set.range (pointsMap B S hS (D.space T').1 (D.relativeMap g).hom) ⊆
      etaleFreeLocus B S hS F
```

**`AlgebraicGeometry.Space.range_pointsMap_relativeMap_subset_etaleRankOneFreeLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackOpenInCoherentStack.lean, line 1002](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackOpenInCoherentStack.lean#L1002). The attribute's comment: “part two of the proof, the implication (a) => (b) on points at the source's own U, unconditionally: if |T'| maps into U = T \ f\_T(|X\_T| \ W\_1) -- which is how condition (a), that T' -> T factors through U, is read here, U being produced as an open subset of |T| -- then |X\_T'| maps into the RANK-ONE etale free locus W\_1 of F. This is the direction that needs no base-change property of the locus, as the source's own argument shows; it is the commutation of X\_g with the projections to the test schemes together with the description of U as the points whose whole fibre lies in W\_1. Pinning the rank to one at the level of the locus is what replaces the source's decomposition X\_T = X\_0 + X\_1 + ... by rank, which is not available for algebraic spaces. The passage from rank-one freeness in an etale neighbourhood of every point of |X\_T'| to invertibility of F\_T' takes two steps -- the easy inclusion of the base-change clause of Tag 0CZT and the local-to-global refinement for the unconditional clause of Tag 0B8Q; both steps are proved (preimage\_etaleRankOneFreeLocus\_subset and isFiniteLocallyFreeOfRank\_one\_of\_forall\_mem\_etaleRankOneFreeLocus), and the complete implication -- |T'| into U gives F\_T' INVERTIBLE, unconditionally -- is isInvertibleModule\_modulePullback\_relativeMap\_of\_subset\_fibrewiseEtaleRankOneFreeLocus below.”.

> **Stacks 0D03, the implication (a) ⟹ (b) of the second part of the proof, on points, at the
> source's own `U`.**  If a morphism `g : T' ⟶ T` of test schemes over `Y` maps `|T'|` into the
> rank-one locus, then `X_g : X_{T'} ⟶ X_T` maps `|X_{T'}|` into the rank-one étale free locus
> of `F`.
>
> This is `AlgebraicGeometry.Space.range_pointsMap_relativeMap_subset_of_subset_fibrewiseLocus` at
> `W₁`, and it is the implication the source proves — its `U` is the rank-one locus, so what (a)
> yields is rank-one freeness at every point of `|X_{T'}|` rather than freeness of some rank.  No
> decomposition by rank and no base-change property of the locus is used.

```lean
theorem range_pointsMap_relativeMap_subset_etaleRankOneFreeLocus (D : CoherentSituation B S hS)
    {T' T : SchemesOver D.Y} (g : T' ⟶ T)
    (F : Modules.{u, u} B S hS (D.space T).1 (D.space T).2)
    (hg : Set.range (pointsMap B S hS ((schemeSpaceFunctor B S hS).obj T'.left).1
        ((schemeSpaceFunctor B S hS).map g.left).hom) ⊆
      fibrewiseEtaleRankOneFreeLocus D T F) :
    Set.range (pointsMap B S hS (D.space T').1 (D.relativeMap g).hom) ⊆
      etaleRankOneFreeLocus B S hS F
```

**`AlgebraicGeometry.Space.range_pointsMap_relativeMap_subset_etaleFreeLocus_of_forall_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackOpenInCoherentStack.lean, line 1090](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackOpenInCoherentStack.lean#L1090). The attribute's comment: “part two of the proof, the implication (b) => (a) on points: if F\_T' is free in an etale neighbourhood of every point then |X\_T'| maps into the etale free locus W of F. UNCONDITIONAL. This is the direction the source derives from the base-change clause of Tag 0CZT, and that clause is proved: etaleFreeLocus\_modulePullback\_eq of Spaces/EtaleFreeLocusBaseChange.lean, registered on 0CZT with a which-part note, states the EQUALITY W(F\_T') = |X\_g|^(-1)(W(F)) at an arbitrary cartesian square. This statement binds no hypothesis standing in for that equality; its binders are D, g, F, 0CZT's own three conditions on F, and the antecedent (b). The source's route is what was assembled: clause (4) of Tag 0CZS (exists\_chartOpen\_over\_iso\_free\_iff\_flat\_geometricFibreModuleStalk) at the image point, the base-change invariance of clause (1) (flat\_geometricFibreModuleStalk\_modulePullback\_iff of Spaces/GeometricFibreStalkBaseChange.lean) for the transport, and the etale-locality of clause (1) (flat\_geometricFibreModuleStalk\_comp\_modulePullback\_iff of Spaces/GeometricFibreStalkEtaleLocal.lean) at the point upstairs. Condition (2) of Tag 05WY is NOT needed and is still neither stated nor proved; that is a gap in the registration of Tag 05WY alone. F carries 0CZT's own three hypotheses, quasi-coherent, of finite presentation and flat over T, which is exactly what an object of Coh\_\{X/Y} is (CoherentObject), so no consumer pays for them.”.

> **Stacks 0D03, the implication (b) ⟹ (a) of the second part of the proof, on points.**  If
> the pullback of `F` along `X_g : X_{T'} ⟶ X_T` is free in an étale neighbourhood of every point
> of `|X_{T'}|` — which is the case when that pullback is invertible — then `X_g` maps `|X_{T'}|`
> into the étale free locus of `F`.
>
> This is the source's "if `T' ⟶ T` satisfies (b) then `|X_{T'}| ⟶ |X_T|` maps into `W`", and it
> is exactly where the base-change clause of Stacks 0CZT enters.  That clause is now proved, as
> `AlgebraicGeometry.Space.etaleFreeLocus_modulePullback_eq` of
> `StacksFrontier/AlgebraicGeometry/Spaces/EtaleFreeLocusBaseChange.lean`, so this statement is
> unconditional.  `F` carries Stacks 0CZT's own hypotheses — quasi-coherent, of finite presentation
> and flat over `T` — which is what an object of `Coh_{X/Y}` is, and local finite presentation of
> the projection `X_T ⟶ T` costs nothing
> (`AlgebraicGeometry.Space.isLocallyOfFinitePresentation_projection`).  The square of the
> morphism of test schemes is cartesian by
> `AlgebraicGeometry.Space.isPullback_baseChangeMap`, which is the form the clause is stated at.

```lean
theorem range_pointsMap_relativeMap_subset_etaleFreeLocus_of_forall_mem
    (D : CoherentSituation B S hS)
    {T' T : SchemesOver D.Y} (g : T' ⟶ T)
    (F : Modules.{u, u} B S hS (D.space T).1 (D.space T).2)
    (hqc : F.IsQuasicoherentOnSite) (hfp : F.IsFinitePresentationOnSite)
    (hflat : IsFlatOver B S hS (D.space T).2 (D.projection T).hom F)
    (hF : ∀ x' : points B S hS (D.space T').1,
      x' ∈ etaleFreeLocus B S hS ((modulePullback B S hS (D.relativeMap g)).obj F)) :
    Set.range (pointsMap B S hS (D.space T').1 (D.relativeMap g).hom) ⊆
      etaleFreeLocus B S hS F
```

**`AlgebraicGeometry.Space.range_pointsMap_relativeMap_subset_etaleFreeLocus_of_isInvertibleModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackOpenInCoherentStack.lean, line 1143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackOpenInCoherentStack.lean#L1143). The attribute's comment: “part two of the proof, the implication (b) => (a) on points, with (b) at the source's own condition that F\_T' be INVERTIBLE rather than at the etale-local freeness of the preceding statement. The step from invertibility to freeness in an etale neighbourhood of every point is unconditional here (mem\_etaleFreeLocus\_of\_isInvertibleModule): the converse clause of Tag 0B8Q applies to the small etale ringed site of an algebraic space, which is locally ringed by Tag 04KH, in its universe-flexible form -- the site has its objects one universe above the sections of its structure sheaf, so the two carriers of 0B8Q stated for a bare ringed site do not instantiate -- and Tag 04M0 identifies a trivialization on a slice of that site with freeness of the pullback to the chart space, which is how the locus W of Tag 0CZT is phrased. UNCONDITIONAL. The base-change clause of Tag 0CZT, which this direction needs, is now proved: etaleFreeLocus\_modulePullback\_eq of Spaces/EtaleFreeLocusBaseChange.lean. This statement binds no hypothesis standing in for that equality; its binders are D, g, F, 0CZT's own three conditions on F, and the antecedent (b). The base-change invariance of clause (1) of Tag 0CZS (flat\_geometricFibreModuleStalk\_modulePullback\_iff) does NOT need condition (2) of Tag 05WY. The converse implication, from |T'| mapping into U to invertibility of F\_T', does not need the source's rank decomposition of X\_T. The decomposition is replaced by pinning the rank to one at the level of the locus (etaleRankOneFreeLocus), and that converse is complete in isInvertibleModule\_modulePullback\_relativeMap\_of\_subset\_fibrewiseEtaleRankOneFreeLocus. F carries 0CZT's own three hypotheses, quasi-coherent, of finite presentation and flat over T, which is exactly what an object of Coh\_\{X/Y} is (CoherentObject).”.

> **Stacks 0D03, the implication (b) ⟹ (a) of the second part of the proof, at the source's
> own condition (b).**  If the pullback `F_{T'}` of `F` along `X_g : X_{T'} ⟶ X_T` is *invertible*
> — which is condition (b) of the source, and not merely the étale-local freeness that
> `Space.range_pointsMap_relativeMap_subset_etaleFreeLocus_of_forall_mem` asks for — then `X_g` maps
> `|X_{T'}|` into the étale free locus of `F`.
>
> The passage from invertibility of `F_{T'}` to its freeness in an étale neighbourhood of every
> point of `|X_{T'}|` is `AlgebraicGeometry.Space.mem_etaleFreeLocus_of_isInvertibleModule` and is
> unconditional: it is the converse clause of Stacks 0B8Q at the small étale ringed site of an
> algebraic space, which is locally ringed by Stacks 04KH, together with the comparison of
> Stacks 04M0 between the slices of that site and the small étale sites of the chart spaces.  The
> base-change clause of Stacks 0CZT is still used, for the same reason as in
> `Space.range_pointsMap_relativeMap_subset_etaleFreeLocus_of_forall_mem`, and it is now proved
> (`AlgebraicGeometry.Space.etaleFreeLocus_modulePullback_eq`), so this statement is
> unconditional as well; `F` carries Stacks 0CZT's own hypotheses here too, which is what an
> object of `Coh_{X/Y}` is.

```lean
theorem range_pointsMap_relativeMap_subset_etaleFreeLocus_of_isInvertibleModule
    (D : CoherentSituation B S hS)
    {T' T : SchemesOver D.Y} (g : T' ⟶ T)
    (F : Modules.{u, u} B S hS (D.space T).1 (D.space T).2)
    (hqc : F.IsQuasicoherentOnSite) (hfp : F.IsFinitePresentationOnSite)
    (hflat : IsFlatOver B S hS (D.space T).2 (D.projection T).hom F)
    (hF : IsInvertibleModule (D.space T')
      ((modulePullback B S hS (D.relativeMap g)).obj F)) :
    Set.range (pointsMap B S hS (D.space T').1 (D.relativeMap g).hom) ⊆
      etaleFreeLocus B S hS F
```

**`AlgebraicGeometry.Space.isInvertibleModule_modulePullback_relativeMap_of_subset_fibrewiseEtaleRankOneFreeLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackOpenInCoherentStack.lean, line 1192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackOpenInCoherentStack.lean#L1192). The attribute's comment: “part two of the proof, the implication (a) => (b) COMPLETE and unconditional, at the source's own U and the source's own condition (b): if |T'| maps into U = T \ f\_T(|X\_T| \ W\_1) -- which is how condition (a), that T' -> T factors through U, is read here, U being produced as an open SUBSET of |T| for the point topology -- then F\_T' is INVERTIBLE. This completes the direction whose last two steps were recorded as missing on range\_pointsMap\_relativeMap\_subset\_etaleRankOneFreeLocus: (i) the easy inclusion of the base-change clause of Tag 0CZT, |X\_g|^\{-1}(W\_1(F)) subset W\_1(F\_T'), which is preimage\_etaleRankOneFreeLocus\_subset and holds for an arbitrary morphism of algebraic spaces; and (ii) the local-to-global refinement from a trivialization through every POINT of |X\_T'| to a trivializing covering family of every OBJECT of the small etale site, which is isFiniteLocallyFreeOfRank\_one\_of\_forall\_mem\_etaleRankOneFreeLocus -- the chosen neighbourhoods form an etale covering, so their charts cover the final object (coversTop\_of\_isEtaleCovering, the slice form of Tag 04M0), and the rank clause of Tag 0409 is local on such a family. The unconditional clause of Tag 0B8Q then gives invertibility. The source's decomposition of X\_T by rank is not used, and neither is the base-change clause of Tag 0CZT: the hard inclusion of that clause is what the CONVERSE implication (b) => (a) needs, and it is proved in etaleFreeLocus\_modulePullback\_eq of Spaces/EtaleFreeLocusBaseChange.lean.”.

> **Stacks 0D03, the implication (a) ⟹ (b) of the second part of the proof, complete.**  If a
> morphism `g : T' ⟶ T` of test schemes over `Y` maps `|T'|` into the source's own locus
> `U = T ∖ f_T(|X_T| ∖ W₁)`, then the pullback `F_{T'}` of `F` along `X_g : X_{T'} ⟶ X_T` is
> *invertible* — which is the source's condition (b).  Unconditionally.
>
> The three steps are each unconditional.  Condition (a) puts every point of `|X_{T'}|` over a
> point of the rank-one étale free locus of `F`
> (`AlgebraicGeometry.Space.range_pointsMap_relativeMap_subset_etaleRankOneFreeLocus`); the easy
> inclusion of the base-change clause of Stacks 0CZT carries that locus forward along `X_g`
> (`AlgebraicGeometry.Space.preimage_etaleRankOneFreeLocus_subset`, a pullback of a rank-one free
> module being rank-one free); and a module whose rank-one étale free locus is all of `|X_{T'}|`
> has rank one on the small étale site
> (`AlgebraicGeometry.Space.isFiniteLocallyFreeOfRank_one_of_forall_mem_etaleRankOneFreeLocus`,
> the local-to-global refinement), hence is invertible by the unconditional clause of Stacks 0B8Q
> (`AlgebraicGeometry.Space.isInvertibleModule_iff_isFiniteLocallyFreeOfRank_one`).
>
> Neither the base-change clause of Stacks 0CZT nor the source's decomposition of `X_T` by rank is
> used: the hard inclusion of that clause is what the *converse* implication needs, and the
> decomposition is replaced by pinning the rank to one at the level of the locus.

```lean
theorem isInvertibleModule_modulePullback_relativeMap_of_subset_fibrewiseEtaleRankOneFreeLocus
    (D : CoherentSituation B S hS) {T' T : SchemesOver D.Y} (g : T' ⟶ T)
    (F : Modules.{u, u} B S hS (D.space T).1 (D.space T).2)
    (hg : Set.range (pointsMap B S hS ((schemeSpaceFunctor B S hS).obj T'.left).1
        ((schemeSpaceFunctor B S hS).map g.left).hom) ⊆
      fibrewiseEtaleRankOneFreeLocus D T F) :
    IsInvertibleModule (D.space T') ((modulePullback B S hS (D.relativeMap g)).obj F)
```

**`AlgebraicGeometry.Space.picardToCoherentHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackToCoherentStack.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackToCoherentStack.lean#L112). The attribute's comment: “the natural map Picardstack\_\{X/B} -> Cohstack\_\{X/B} on hom-sets, together with picardObjectToCoherent on objects: the first part of the source's proof, in which the triple (T, g, L) of Section 0372 is sent to the same triple in Situation 08KB and the morphism (h, a) to the morphism (h, a). The map on hom-sets is a BIJECTION, so the natural map is fully faithful and Picardstack\_\{X/B} is the full subcategory of Cohstack\_\{X/B} on the objects with invertible module. The binders are D and the tag's own flatness and properness of f, which the object map needs. The whole statement of the tag is isRepresentableByAlgebraicSpaces\_and\_isOpenImmersion\_picardToCoherent of Quot/PicardStackOpenImmersion.lean.”.

> **Stacks 0D03, the natural map on hom-sets is a bijection.**  The hom-sets of `Pic_{X/B}`
> and of `Coh_{X/B}` between two objects and their images are the same pair of data — a morphism of
> test schemes over the base and an isomorphism of the inverse image of the module of the target
> with the module of the source — so the natural map identifies them.
>
> So the natural map is fully faithful, and `Pic_{X/B}` is the full subcategory of `Coh_{X/B}` on
> the objects whose module is invertible: the fibre of the map over an object `(T, g, F)` of
> `Coh_{X/B}` is the set of proofs that `F` is invertible, which is a subsingleton.  That is the
> structural reason the tag asserts an *open immersion* rather than a general morphism.

```lean
def picardToCoherentHomEquiv (D : CoherentSituation B S hS) (hflat : IsFlat B S hS D.f.hom)
    (hproper : IsProper B S hS D.f.hom) (A C : PicardObject D.toPicardSituation) :
    PicardHom A C ≃ CoherentHom (picardObjectToCoherent D hflat hproper A)
      (picardObjectToCoherent D hflat hproper C)
```

## Tag 0D04, a proposition

[Tag 0D04](https://stacks.math.columbia.edu/tag/0D04) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.isAlgebraicStack_picardCFG`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackIsAlgebraic.lean#L43), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackAlgebraicRegistration.lean, line 30](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackAlgebraicRegistration.lean#L30) (StacksFrontier): “the full statement. f : X ⟶ B is flat (hflat), of finite presentation (a field of the standing datum D of Situation 08KB) and proper (hproper); then Picardstack\_\{X/B} is an algebraic stack. Nothing is assumed beyond the source's hypotheses.”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 99.10, Tag 0D02](https://stacks.math.columbia.edu/tag/0D02)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
