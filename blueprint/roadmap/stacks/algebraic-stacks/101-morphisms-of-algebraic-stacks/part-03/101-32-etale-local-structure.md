---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isAlgebraicSpace_quotientSheaf_of_isOpenImmersion, AlgebraicGeometry.Space.isEtale_quotientSheafToBase_of_isOpenImmersion, AlgebraicGeometry.Stack.quotientStackToQuotientSheaf, AlgebraicGeometry.Stack.quotientStackProjection_comp_quotientStackToQuotientSheaf, AlgebraicGeometry.Stack.quotientStackToQuotientSheaf_comp_toBase, AlgebraicGeometry.Stack.isAlgebraicSpace_and_equivalenceOver_and_isEtale_of_isOpenImmersion, AlgebraicGeometry.Stack.isAlgebraicStack_representable_surjective_etale_quotientStackMap, Stacks.Groupoids.GroupoidScheme.exists_quasiSplitting_isAffine_isFinite_flat
statement: formalized
proof: formalized
---

# 101.32 Étale local structure

Section 101.32 of the Stacks Project, [Tag 0DU0](https://stacks.math.columbia.edu/tag/0DU0). 5 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DU1, a lemma

[Tag 0DU1](https://stacks.math.columbia.edu/tag/0DU1) in the Stacks Project.

**`AlgebraicGeometry.Space.isAlgebraicSpace_quotientSheaf_of_isOpenImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/OpenRelationEtaleQuotient.lean, line 429](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/OpenRelationEtaleQuotient.lean#L429). The attribute's comment: “algebraicity of the quotient U/R”.

> **Stacks 0DU1, algebraicity of the quotient.** Let `(U, R, s, t, c)` be a groupoid in
> algebraic spaces over an algebraic space `Y` whose object space is flat and locally of finite
> presentation over `Y` and whose pre-relation `(t, s) : R ⟶ U ×_Y U` is an open immersion.  Then
> the quotient sheaf `U/R` of Stacks 044J is an algebraic space over `S`.
>
> The pre-relation is an equivalence relation and `s` and `t` are flat and locally of finite
> presentation, so Stacks 04S6, condition (1), applies.

```lean
theorem isAlgebraicSpace_quotientSheaf_of_isOpenImmersion
    (hflat : IsFlat C S hS G.objectsToBase.hom)
    (hlfp : IsLocallyOfFinitePresentation C S hS G.objectsToBase.hom)
    (hopen : IsOpenImmersion C S hS (groupoidPreRelation G).left) :
    IsAlgebraicSpace C S hS (quotientSheaf (groupoidPreRelation G)).obj
```

**`AlgebraicGeometry.Space.isEtale_quotientSheafToBase_of_isOpenImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/OpenRelationEtaleQuotient.lean, line 574](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/OpenRelationEtaleQuotient.lean#L574). The attribute's comment: “étaleness of the structural morphism U/R → Y”.

> **Stacks 0DU1, étaleness of the quotient over the base.** Let `(U, R, s, t, c)` be a
> groupoid in algebraic spaces over an algebraic space `Y` whose object space is flat and locally
> of finite presentation over `Y` and whose pre-relation `(t, s) : R ⟶ U ×_Y U` is an open
> immersion.  Then the canonical morphism `U/R ⟶ Y` of Stacks 044J is étale.
>
> Algebraicity of the quotient,
> `AlgebraicGeometry.Space.isAlgebraicSpace_quotientSheaf_of_isOpenImmersion`, is what Stacks 06PG
> needs in order to give the three properties of the covering map `U ⟶ U/R`.

```lean
theorem isEtale_quotientSheafToBase_of_isOpenImmersion
    (hflat : IsFlat C S hS G.objectsToBase.hom)
    (hlfp : IsLocallyOfFinitePresentation C S hS G.objectsToBase.hom)
    (hopen : IsOpenImmersion C S hS (groupoidPreRelation G).left) :
    IsEtale C S hS (quotientSheafToBase Y.property.isSheaf (groupoidPreRelation G)).hom
```

**`AlgebraicGeometry.Stack.quotientStackToQuotientSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/OpenRelationEtaleQuotient.lean, line 638](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/OpenRelationEtaleQuotient.lean#L638). The attribute's comment: “the canonical comparison [U/R] → U/R”.

> **Stacks 0DU1, the canonical comparison `[U/R] ⟶ U/R`.** Under the hypotheses of Stacks 0DU1
> the quotient sheaf is an algebraic space
> (`AlgebraicGeometry.Space.isAlgebraicSpace_quotientSheaf_of_isOpenImmersion`), so the quotient
> projection `U ⟶ U/R` is an invariant morphism to an algebraic space, and it descends to a
> 1-morphism from the quotient stack to the category fibred in sets of `U/R`.
>
> This is the comparison asserted by the equality `X = [U/R] = U/R` of the source.  It is a real
> construction — the descent of Stacks 044R applied to the quotient projection — and not a choice
> out of an existence statement; `AlgebraicGeometry.Stack.quotientStackToQuotientSheaf_unique`
> shows it is the only 1-morphism restricting along the projection to the quotient map.

```lean
noncomputable def quotientStackToQuotientSheaf :
    quotientStack G ⥤ᵇ
      (fibredCategory C S hS (quotientSheafSpace G hflat hlfp hopen).obj).val
```

**`AlgebraicGeometry.Stack.quotientStackProjection_comp_quotientStackToQuotientSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/OpenRelationEtaleQuotient.lean, line 648](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/OpenRelationEtaleQuotient.lean#L648). The attribute's comment: “the comparison composed with the quotient projection is the map attached to U → U/R”.

> **Stacks 0DU1.** The canonical comparison composed with the projection `U ⟶ [U/R]` of
> Stacks 044R is the 1-morphism that Stacks 0458 attaches to the quotient map `U ⟶ U/R`.

```lean
theorem quotientStackProjection_comp_quotientStackToQuotientSheaf :
    BasedFunctor.comp (quotientStackProjection G)
        (quotientStackToQuotientSheaf G hflat hlfp hopen) =
      (associatedMap C S hS (Space.toQuotientSheaf (Space.groupoidPreRelation G))).1.hom
```

**`AlgebraicGeometry.Stack.quotientStackToQuotientSheaf_comp_toBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/OpenRelationEtaleQuotient.lean, line 678](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/OpenRelationEtaleQuotient.lean#L678). The attribute's comment: “the comparison is compatible with the structural morphisms to the base”.

> **Stacks 0DU1.** The canonical comparison is a morphism over the base: composed with the
> 1-morphism attached to the structural morphism `U/R ⟶ Y` it is the structure arrow
> `[U/R] ⟶ Y` of Stacks 044R.
>
> Both sides restrict along the projection to the structure morphism `U ⟶ Y` of the object space,
> and by Stacks 0DUH a 1-morphism from the quotient stack to an algebraic space is determined by
> that restriction.

```lean
theorem quotientStackToQuotientSheaf_comp_toBase :
    BasedFunctor.comp (quotientStackToQuotientSheaf G hflat hlfp hopen)
        (associatedMap C S hS (quotientSheafToBaseSpace G hflat hlfp hopen).hom).1.hom =
      quotientStackToBase G
```

**`AlgebraicGeometry.Stack.isAlgebraicSpace_and_equivalenceOver_and_isEtale_of_isOpenImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/OpenRelationEtaleQuotientEquivalence.lean, line 413](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/OpenRelationEtaleQuotientEquivalence.lean#L413).

> **Stacks 0DU1.** Let `(U, R, s, t, c)` be a groupoid in algebraic spaces over an algebraic
> space `Y` whose object space `U` is flat and locally of finite presentation over `Y` and whose
> pre-relation `(t, s) : R ⟶ U ×_Y U` is an open immersion.  Then `X = [U/R] = U/R` is an algebraic
> space and `X ⟶ Y` is étale: the quotient sheaf `U/R` of Stacks 044J is an algebraic space, the
> canonical comparison `AlgebraicGeometry.Stack.quotientStackToQuotientSheaf` from the quotient
> stack `[U/R]` to it is an equivalence over the big fppf site, and the structural morphism
> `U/R ⟶ Y` is étale.
>
> The three clauses are `AlgebraicGeometry.Space.isAlgebraicSpace_quotientSheaf_of_isOpenImmersion`,
> `AlgebraicGeometry.Stack.nonempty_equivalenceOver_quotientStackToQuotientSheaf` and
> `AlgebraicGeometry.Space.isEtale_quotientSheafToBase_of_isOpenImmersion`.

```lean
theorem isAlgebraicSpace_and_equivalenceOver_and_isEtale_of_isOpenImmersion :
    IsAlgebraicSpace C S hS (Space.quotientSheaf (Space.groupoidPreRelation G)).obj ∧
      Nonempty { e : StacksRepresentableCFG.EquivalenceOver (quotientStack G).p
          (fibredCategory C S hS (quotientSheafSpace G hflat hlfp hopen).obj).val.p //
        e.hom.functor = (quotientStackToQuotientSheaf G hflat hlfp hopen).toFunctor } ∧
      Space.IsEtale C S hS
        (Space.quotientSheafToBase Y.property.isSheaf (Space.groupoidPreRelation G)).hom
```

## Tag 0DU2, a lemma

[Tag 0DU2](https://stacks.math.columbia.edu/tag/0DU2) in the Stacks Project.

**`AlgebraicGeometry.Stack.isAlgebraicStack_representable_surjective_etale_quotientStackMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/OpenSubgroupoidQuotientStackFull.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/OpenSubgroupoidQuotientStackFull.lean#L84).

> **Stacks 0DU2.** Let `(U, R, s, t, c)` be a groupoid in algebraic spaces (here over an
> algebraic space `A` over `S`, which contains the case of a groupoid over `S`) with `s`, `t` flat
> and locally of finite presentation, and let `P ⊆ R` be an open subspace such that
> `(U, P, s|_P, t|_P, c|_P)` is a groupoid in algebraic spaces; that is, let `φ : G ⟶ H` be a
> morphism of groupoids in algebraic spaces whose map on objects is an isomorphism and whose map on
> arrows is an open immersion. Then `[U/P]` and `[U/R]` are algebraic stacks, and
> `[φ] : [U/P] ⟶ [U/R]` is representable by algebraic spaces, surjective and étale, the last two in
> the sense of Stacks 03YK.

```lean
theorem isAlgebraicStack_representable_surjective_etale_quotientStackMap
    {G H : GroupoidInAlgebraicSpaces C S hS A} (φ : GroupoidInAlgebraicSpaces.Hom G H)
    (hopen : Space.IsOpenImmersion C S hS φ.toGroupoidHom.mapArrows)
    (hobj : IsIso φ.toGroupoidHom.mapObjects)
    (hsflat : Space.IsFlat C S hS H.source.hom) (htflat : Space.IsFlat C S hS H.target.hom)
    (hslfp : Space.IsLocallyOfFinitePresentation C S hS H.source.hom)
    (htlfp : Space.IsLocallyOfFinitePresentation C S hS H.target.hom) :
    IsAlgebraicStack.{u, w} C S hS (quotientStack G) ∧
      IsAlgebraicStack.{u, w} C S hS (quotientStack H) ∧
      ∃ hrep : IsRepresentableByAlgebraicSpaces C S hS (quotientStackMap φ),
        HasRelativeProperty.{u, u + 1, u + 1, u} C S hS
          (Space.surjectiveMorphismProperty C S hS) (quotientStackMapCFGHom φ) hrep ∧
        HasRelativeProperty.{u, u + 1, u + 1, u} C S hS
          (Space.etaleMorphisms C S hS) (quotientStackMapCFGHom φ) hrep
```

## Tag 0DU3, a lemma

[Tag 0DU3](https://stacks.math.columbia.edu/tag/0DU3) in the Stacks Project.

**`Stacks.Groupoids.GroupoidScheme.exists_quasiSplitting_isAffine_isFinite_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/EtaleLocalStructureQuasiSplitting.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/EtaleLocalStructureQuasiSplitting.lean#L165). The attribute's comment: “the groupoid scheme of clause (3), with U and its arrow scheme affine and source and target finite, flat and locally of finite presentation, built from a quasi-splitting of Stacks 04RK. Clause (1), clause (2) and the identification of the stack with [U/R] in clause (3) are NOT covered: see the implementation notes for the three named obstructions”.

> **Stacks 0DU3, the groupoid of clause (3).**
>
> Let `(U, R, s, t, c)` be a groupoid scheme over `S` with `U` affine and with `s` and `t` flat and
> locally of finite presentation, and let `u` be a point of `U` over which the groupoid is
> quasi-split in the sense of **Stacks 04RK**, part (3).  Then there is a groupoid scheme
> `(U, P, s|_P, t|_P, c|_P)` together with a morphism into `(U, R, s, t, c)` which is an open
> immersion on arrow schemes and the identity on object schemes, carrying the identity arrow at
> `u`, whose *both* structure schemes are affine and whose source and target are finite, flat and
> locally of finite presentation.
>
> This is the groupoid scheme of clause (3) of **Stacks 0DU3**, with every property that clause
> asserts of it: the source's proof takes `𝒰 = [U/P]` for exactly this `P`.  The properties are
> asserted of one single groupoid scheme, as the tag asserts them.
>
> The three conjuncts that are not re-derivations are the equality of object schemes, the open
> immersion and the identity arrow: these are the three pieces of data a quasi-splitting *is*
> (conditions (a) and (c) of Stacks 04RK), and they are listed so that the groupoid produced is
> pinned to be the quasi-splitting at `u` rather than an unrelated groupoid.  Everything else is
> derived: affineness of the object scheme from the equality, flatness and local finite
> presentation of `s|_P` and `t|_P` from the open immersion composed with `s` and `t`, and
> affineness of the arrow scheme from finiteness of `s|_P` over the affine object scheme — the
> last being the step where an *open* subscheme of `R` is shown affine without `R` being used at
> all.

```lean
theorem exists_quasiSplitting_isAffine_isFinite_flat [IsAffine G.objects.left]
    [Flat G.source.left] [LocallyOfFinitePresentation G.source.left]
    [Flat G.target.left] [LocallyOfFinitePresentation G.target.left]
    {u : G.objects.left} (h : IsQuasiSplitAt G u) :
    ∃ (G' : GroupoidScheme S) (φ : Hom G' G),
      G'.objects = G.objects ∧
      IsOpenImmersion φ.mapArrows.left ∧
      (∃ p : G'.arrows.left, φ.mapArrows.left.base p = G.identity.left.base u) ∧
      IsAffine G'.objects.left ∧ IsAffine G'.arrows.left ∧
      IsFinite G'.source.left ∧
      Flat G'.source.left ∧ LocallyOfFinitePresentation G'.source.left ∧
      IsFinite G'.target.left ∧
      Flat G'.target.left ∧ LocallyOfFinitePresentation G'.target.left
```

**`AlgebraicGeometry.Stack.exists_etale_quotientStack_of_isQuasiDM`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/EtaleLocalStructureStack.lean, line 341](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/EtaleLocalStructureStack.lean#L341).

> **Stacks 0DU3.** Let `𝒳` be an algebraic stack over `S` which is quasi-DM (Stacks 050D) with
> separated diagonal `Δ_{𝒳/S}` (Stacks 04XB), and let `x ∈ |𝒳|`. Then there is a 1-morphism of
> algebraic stacks `g : 𝒰 ⟶ 𝒳` such that
>
> 1. some point of `|𝒰|` maps to `x`,
> 2. `g` is representable by algebraic spaces and étale,
> 3. `𝒰` is the quotient stack `[U/R]` of (the realization of) a groupoid scheme `(U, R, s, t, c)`
>    with `U` and `R` affine and `s`, `t` finite, flat and locally of finite presentation: there is
>    an equivalence over the site between that quotient stack and `𝒰`.
>
> The parenthetical equivalent hypothesis of the source (`I_𝒳 ⟶ 𝒳` locally quasi-finite and
> separated) is Stacks 0CL0, parts (1) and (5).

```lean
theorem exists_etale_quotientStack_of_isQuasiDM (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (hQ : AlgebraicStacks.IsAbsolutelyQuasiDM B S hS B.contains_terminal 𝒳)
    (hΔ : Stack.IsSeparated.{u, u, u + 1} B S hS
      (relativeDiagonal.{u, u, u + 1} B S hS 𝒳.val
        (schemeStack.{u, w} B S hS (Over.mk (𝟙 (B.obj hS)))).val
        (structureMorphism B S hS 𝒳).hom))
    (x : AlgebraicStacks.points B S hS 𝒳) :
    ∃ (𝒰 : AlgebraicStacks.{u, w} B S hS) (g : 𝒰 ⟶ 𝒳),
      (∃ v, AlgebraicStacks.pointsMap B S hS g v = x) ∧
      (IsRepresentableByAlgebraicSpaces B S hS g.hom.hom ∧ IsEtale B S hS g) ∧
      ∃ (G : GroupoidScheme S) (hU : B.Contains G.objects.left) (hR : B.Contains G.arrows.left)
        (hP : B.Contains (pullback G.source G.target).left),
        IsAffine G.objects.left ∧ IsAffine G.arrows.left ∧
        IsFinite G.source.left ∧ Flat G.source.left ∧ LocallyOfFinitePresentation G.source.left ∧
        IsFinite G.target.left ∧ Flat G.target.left ∧ LocallyOfFinitePresentation G.target.left ∧
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (quotientStack (G.realization B hS hU hR hP)).p 𝒰.val.val.p)
```

## Tag 0DU4, a lemma

[Tag 0DU4](https://stacks.math.columbia.edu/tag/0DU4) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_etale_quotientStack_inducesIsomorphismAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/EtaleLocalStructureAutomorphism.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/EtaleLocalStructureAutomorphism.lean#L86).

> **Stacks 0DU4.** Let `𝒳` be an algebraic stack over `S` which is quasi-DM (Stacks 050D) with
> separated diagonal `Δ_{𝒳/S}` (Stacks 04XB), and let `x ∈ |𝒳|` be a point at which the automorphism
> group of `𝒳` is finite (Remark 0DTU). Then there is a 1-morphism of algebraic stacks
> `g : 𝒰 ⟶ 𝒳` such that
>
> 1. some point `v ∈ |𝒰|` maps to `x` and `g` induces an isomorphism between the automorphism
>    groups at `v` and `x` (Stacks 0DTW),
> 2. `g` is representable by algebraic spaces and étale,
> 3. `𝒰` is the quotient stack `[U/R]` of (the realization of) a groupoid scheme `(U, R, s, t, c)`
>    with `U` and `R` affine and `s`, `t` finite, flat and locally of finite presentation: there is
>    an equivalence over the site between that quotient stack and `𝒰`.
>
> The parenthetical equivalent hypothesis of the source (`I_𝒳 ⟶ 𝒳` locally quasi-finite and
> separated) is Stacks 0CL0, parts (1) and (5).

```lean
theorem exists_etale_quotientStack_inducesIsomorphismAt (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (hQ : AlgebraicStacks.IsAbsolutelyQuasiDM B S hS B.contains_terminal 𝒳)
    (hΔ : Stack.IsSeparated.{u, u, u + 1} B S hS
      (relativeDiagonal.{u, u, u + 1} B S hS 𝒳.val
        (schemeStack.{u, w} B S hS (Over.mk (𝟙 (B.obj hS)))).val
        (structureMorphism B S hS 𝒳).hom))
    (x : AlgebraicStacks.points B S hS 𝒳)
    (hAut : AutomorphismGroupHasProperty B S hS (IsFiniteOverBase B S hS) x) :
    ∃ (𝒰 : AlgebraicStacks.{u, w} B S hS) (g : 𝒰 ⟶ 𝒳),
      (∃ v, AlgebraicStacks.pointsMap B S hS g v = x ∧ InducesIsomorphismAt B S hS g v) ∧
      (IsRepresentableByAlgebraicSpaces B S hS g.hom.hom ∧ IsEtale B S hS g) ∧
      ∃ (G : GroupoidScheme S) (hU : B.Contains G.objects.left) (hR : B.Contains G.arrows.left)
        (hP : B.Contains (pullback G.source G.target).left),
        IsAffine G.objects.left ∧ IsAffine G.arrows.left ∧
        IsFinite G.source.left ∧ Flat G.source.left ∧ LocallyOfFinitePresentation G.source.left ∧
        IsFinite G.target.left ∧ Flat G.target.left ∧ LocallyOfFinitePresentation G.target.left ∧
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (quotientStack (G.realization B hS hU hR hP)).p 𝒰.val.val.p)
```

## Tag 0DU5, a lemma

[Tag 0DU5](https://stacks.math.columbia.edu/tag/0DU5) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_etale_quotientStack_residualGerbeMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/EtaleLocalStructureResidualGerbeExistence.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/EtaleLocalStructureResidualGerbeExistence.lean#L98).

> **Stacks 0DU5.** Let `𝒳` be an algebraic stack over `S` which is quasi-DM (Stacks 050D) with
> separated diagonal `Δ_{𝒳/S}` (Stacks 04XB), and let `x ∈ |𝒳|` be a point which can be represented
> by a quasi-compact morphism from the spectrum of a field. Then there is a 1-morphism of algebraic
> stacks `g : 𝒰 ⟶ 𝒳` such that
>
> 1. some point `v ∈ |𝒰|` maps to `x`, the residual gerbes of `𝒰` at `v` and of `𝒳` at `x` exist,
>    and the 1-morphism between them induced by `g` (Stacks 0DTH) is an isomorphism for every
>    choice of them;
> 2. `g` is representable by algebraic spaces and étale;
> 3. `𝒰` is the quotient stack `[U/R]` of (the realization of) a groupoid scheme `(U, R, s, t, c)`
>    with `U` and `R` affine and `s`, `t` finite, flat and locally of finite presentation: there is
>    an equivalence over the site between that quotient stack and `𝒰`.
>
> The parenthetical equivalent hypothesis of the source (`I_𝒳 ⟶ 𝒳` locally quasi-finite and
> separated) is Stacks 0CL0, parts (1) and (5). See the module documentation for the proof.

```lean
theorem exists_etale_quotientStack_residualGerbeMap (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (hQ : AlgebraicStacks.IsAbsolutelyQuasiDM B S hS B.contains_terminal 𝒳)
    (hΔ : Stack.IsSeparated.{u, u, u + 1} B S hS
      (relativeDiagonal.{u, u, u + 1} B S hS 𝒳.val
        (schemeStack.{u, w} B S hS (Over.mk (𝟙 (B.obj hS)))).val
        (structureMorphism B S hS 𝒳).hom))
    (x : AlgebraicStacks.points B S hS 𝒳)
    (hqc : ∃ p : FieldValuedPoint B S hS 𝒳.val.val,
      pointClass B S hS 𝒳.val.val 𝒳.val.isFiberedInGroupoids p = x ∧
        IsQuasiCompactFieldValuedPoint B S hS 𝒳.val p) :
    ∃ (𝒰 : AlgebraicStacks.{u, w} B S hS) (g : 𝒰 ⟶ 𝒳)
      (v : AlgebraicStacks.points B S hS 𝒰),
      (AlgebraicStacks.pointsMap B S hS g v = x ∧
        (∃ P : ObjectProperty 𝒰.val.val.obj, IsResidualGerbeAt B S hS 𝒰 v P) ∧
        (∃ Q : ObjectProperty 𝒳.val.val.obj, IsResidualGerbeAt B S hS 𝒳 x Q) ∧
        ∀ (P : ObjectProperty 𝒰.val.val.obj) (Q : ObjectProperty 𝒳.val.val.obj)
          (hv : IsResidualGerbeAt B S hS 𝒰 v P)
          (hx : IsResidualGerbeAt B S hS 𝒳 (AlgebraicStacks.pointsMap B S hS g v) Q),
          Nonempty (Functor.IsEquivalenceOver
            (fullSubcategoryAlgebraicStack 𝒰 P hv.2.choose).val.val.p
            (fullSubcategoryAlgebraicStack 𝒳 Q hx.2.choose).val.val.p
            (CatFiberedInGroupoids.homFunctor
              (residualGerbeMap B S hS g hv.2.choose hx.2.choose
                (map_mem_of_isResidualGerbeAt B S hS g v _ rfl hv hx)).hom))) ∧
      (IsRepresentableByAlgebraicSpaces B S hS g.hom.hom ∧ IsEtale B S hS g) ∧
      ∃ (G : GroupoidScheme S) (hU : B.Contains G.objects.left) (hR : B.Contains G.arrows.left)
        (hP : B.Contains (pullback G.source G.target).left),
        IsAffine G.objects.left ∧ IsAffine G.arrows.left ∧
        IsFinite G.source.left ∧ Flat G.source.left ∧ LocallyOfFinitePresentation G.source.left ∧
        IsFinite G.target.left ∧ Flat G.target.left ∧ LocallyOfFinitePresentation G.target.left ∧
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (quotientStack (G.realization B hS hU hR hP)).p 𝒰.val.val.p)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.32, Tag 0DU0](https://stacks.math.columbia.edu/tag/0DU0)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
