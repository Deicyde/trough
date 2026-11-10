---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.AlgebraicStacks.IsOpenImmersion, AlgebraicGeometry.Stack.AlgebraicStacks.IsClosedImmersion, AlgebraicGeometry.Stack.AlgebraicStacks.IsImmersion, AlgebraicGeometry.Stack.AlgebraicStacks.isImmersion_snd_of_isTwoFibreProduct, AlgebraicGeometry.Stack.AlgebraicStacks.isClosedImmersion_baseChange_snd, AlgebraicGeometry.Stack.AlgebraicStacks.isOpenImmersion_baseChange_snd, AlgebraicGeometry.Stack.AlgebraicStacks.isOpenImmersion_comp, AlgebraicGeometry.Stack.AlgebraicStacks.isClosedImmersion_comp
statement: formalized
proof: formalized
---

# 100.9 Immersions of algebraic stacks

Section 100.9 of the Stacks Project, [Tag 04YK](https://stacks.math.columbia.edu/tag/04YK). 20 tags here are carried by 83 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04YL, a definition

[Tag 04YL](https://stacks.math.columbia.edu/tag/04YL) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsOpenImmersion`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionAlgebraicStack.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionAlgebraicStack.lean#L209). The attribute's comment: “part (1): open immersions”.

> **Stacks 04YL**, part (1). A 1-morphism of algebraic stacks over `S` is an *open immersion*
> when it is representable by algebraic spaces and is an open immersion in the sense of Stacks
> 04XB.

```lean
abbrev IsOpenImmersion (f : 𝒳 ⟶ 𝒴) : Prop
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsClosedImmersion`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionAlgebraicStack.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionAlgebraicStack.lean#L216). The attribute's comment: “part (2): closed immersions”.

> **Stacks 04YL**, part (2). A 1-morphism of algebraic stacks over `S` is a *closed immersion*
> when it is representable by algebraic spaces and is a closed immersion in the sense of Stacks
> 04XB.

```lean
abbrev IsClosedImmersion (f : 𝒳 ⟶ 𝒴) : Prop
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsImmersion`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionAlgebraicStack.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionAlgebraicStack.lean#L222). The attribute's comment: “part (3): immersions”.

> **Stacks 04YL**, part (3). A 1-morphism of algebraic stacks over `S` is an *immersion* when
> it is representable by algebraic spaces and is an immersion in the sense of Stacks 04XB.

```lean
abbrev IsImmersion (f : 𝒳 ⟶ 𝒴) : Prop
```

## Tag 0501, a lemma

[Tag 0501](https://stacks.math.columbia.edu/tag/0501) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isImmersion_snd_of_isTwoFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionBaseChange.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionBaseChange.lean#L143). The attribute's comment: “immersions”.

> Base change of an immersion of algebraic stacks. If `g : 𝒵 ⟶ 𝒴` is an immersion of
> algebraic stacks over `S` and `P` is a 2-fibre product of the cospan `(g, f)` in the 2-category of
> algebraic stacks, then `P.snd : P.pt ⟶ 𝒳` is an immersion of algebraic stacks.
>
> Both halves are base-change statements: representability by algebraic spaces is Stacks 0302 and
> the immersion property of Stacks 04XB is Stacks 045C. The attribute records the latter, at the
> level of algebraic stacks. It deliberately does **not** record Stacks 04YL: that tag is a
> definition — its three parts define open immersions, closed immersions and immersions in terms
> of Section 04XB — and says nothing about stability under base change, so a theorem must not
> carry it. The definition itself is carried by `AlgebraicStacks.IsImmersion`.

```lean
theorem isImmersion_snd_of_isTwoFibreProduct
    (P : Bicategory.TwoCommSq g f) (hP : Bicategory.IsTwoFibreProduct P)
    (hg : IsImmersion B S hS g) :
    IsImmersion B S hS P.snd
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isClosedImmersion_baseChange_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionsStableUnderBaseChange.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionsStableUnderBaseChange.lean#L166). The attribute's comment: “closed immersions”.

> **Stacks 0501 for closed immersions.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks
> over `S` and let `g : 𝒵 ⟶ 𝒴` be a closed immersion of algebraic stacks. Then the projection
> `𝒵 ×_𝒴 𝒳 ⟶ 𝒳` is a closed immersion of algebraic stacks.
>
> Stated at an arbitrary 2-fibre product square `P` of the cospan `(g, f)` in the 2-category of
> algebraic stacks; the source's `𝒵 ×_𝒴 𝒳` is the canonical such square.

```lean
theorem isClosedImmersion_baseChange_snd
    (P : Bicategory.TwoCommSq g f) (hP : Bicategory.IsTwoFibreProduct P)
    (hg : IsClosedImmersion B S hS g) :
    IsClosedImmersion B S hS P.snd
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isOpenImmersion_baseChange_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionsStableUnderBaseChange.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionsStableUnderBaseChange.lean#L180). The attribute's comment: “open immersions”.

> **Stacks 0501 for open immersions.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks
> over `S` and let `g : 𝒵 ⟶ 𝒴` be an open immersion of algebraic stacks. Then the projection
> `𝒵 ×_𝒴 𝒳 ⟶ 𝒳` is an open immersion of algebraic stacks.
>
> Stated at an arbitrary 2-fibre product square `P` of the cospan `(g, f)` in the 2-category of
> algebraic stacks; the source's `𝒵 ×_𝒴 𝒳` is the canonical such square.

```lean
theorem isOpenImmersion_baseChange_snd
    (P : Bicategory.TwoCommSq g f) (hP : Bicategory.IsTwoFibreProduct P)
    (hg : IsOpenImmersion B S hS g) :
    IsOpenImmersion B S hS P.snd
```

## Tag 0502, a lemma

[Tag 0502](https://stacks.math.columbia.edu/tag/0502) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isOpenImmersion_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionAlgebraicStack.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionAlgebraicStack.lean#L285). The attribute's comment: “open immersions”. References: EGA I (4.2.5), “open immersions”.

> **Stacks 0502** for open immersions: a composite of open immersions of algebraic stacks
> over `S` is an open immersion.

```lean
theorem isOpenImmersion_comp
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : IsOpenImmersion B S hS f) (hg : IsOpenImmersion B S hS g) :
    IsOpenImmersion B S hS (f ≫ g)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isClosedImmersion_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionAlgebraicStack.lean, line 297](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionAlgebraicStack.lean#L297). The attribute's comment: “closed immersions”. References: EGA I (4.2.5), “closed immersions”.

> **Stacks 0502** for closed immersions: a composite of closed immersions of algebraic
> stacks over `S` is a closed immersion.

```lean
theorem isClosedImmersion_comp
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : IsClosedImmersion B S hS f) (hg : IsClosedImmersion B S hS g) :
    IsClosedImmersion B S hS (f ≫ g)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isImmersion_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionAlgebraicStack.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionAlgebraicStack.lean#L312). The attribute's comment: “immersions”. References: EGA I (4.2.5), “immersions”.

> **Stacks 0502**: a composite of immersions of algebraic stacks over `S` is an
> immersion.

```lean
theorem isImmersion_comp
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : IsImmersion B S hS f) (hg : IsImmersion B S hS g) :
    IsImmersion B S hS (f ≫ g)
```

## Tag 0503, a lemma

[Tag 0503](https://stacks.math.columbia.edu/tag/0503) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isImmersion_iff_exists_isImmersion_representingMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionFppfCoverCriterion.lean, line 296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionFppfCoverCriterion.lean#L296). The attribute's comment: “immersions”.

> **Stacks 0503 for immersions.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over
> `S`, let `W` be an algebraic space over `S` and let `g : W ⟶ 𝒴` be surjective, flat and locally
> of finite presentation. Then `f` is an immersion of algebraic stacks (Stacks 04YL, part (3))
> exactly when `V = W ×_𝒴 𝒳` is an algebraic space and `V ⟶ W` is an immersion of algebraic
> spaces.
>
> The forward implication reads representability by algebraic spaces off clause (1); the backward
> one obtains it from Stacks 04ZP. The content of both is Stacks 04XD at the immersion property.

```lean
theorem isImmersion_iff_exists_isImmersion_representingMap :
    IsImmersion B S hS f ↔
      ∃ (V : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (_hV : IsAlgebraicSpace B S hS V)
        (eV : StacksRepresentableCFG.EquivalenceOver
          Q.pt.val.p (presheafOfCategories (V ⋙ typeToCat)).p),
        Space.IsImmersion B S hS (representingMap B S hS Q.pt 𝒲 V W eV eW Q.fst)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isClosedImmersion_iff_exists_isClosedImmersion_representingMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionFppfCoverCriterion.lean, line 311](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionFppfCoverCriterion.lean#L311). The attribute's comment: “closed immersions”.

> **Stacks 0503 for closed immersions.** In the situation of
> `AlgebraicGeometry.Stack.AlgebraicStacks.isImmersion_iff_exists_isImmersion_representingMap`,
> `f` is a closed immersion of algebraic stacks (Stacks 04YL, part (2)) exactly when
> `V = W ×_𝒴 𝒳` is an algebraic space and `V ⟶ W` is a closed immersion of algebraic spaces.

```lean
theorem isClosedImmersion_iff_exists_isClosedImmersion_representingMap :
    IsClosedImmersion B S hS f ↔
      ∃ (V : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (_hV : IsAlgebraicSpace B S hS V)
        (eV : StacksRepresentableCFG.EquivalenceOver
          Q.pt.val.p (presheafOfCategories (V ⋙ typeToCat)).p),
        Space.IsClosedImmersion B S hS (representingMap B S hS Q.pt 𝒲 V W eV eW Q.fst)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isOpenImmersion_iff_exists_isOpenImmersion_representingMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionFppfCoverCriterion.lean, line 326](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionFppfCoverCriterion.lean#L326). The attribute's comment: “open immersions”.

> **Stacks 0503 for open immersions.** In the situation of
> `AlgebraicGeometry.Stack.AlgebraicStacks.isImmersion_iff_exists_isImmersion_representingMap`,
> `f` is an open immersion of algebraic stacks (Stacks 04YL, part (1)) exactly when
> `V = W ×_𝒴 𝒳` is an algebraic space and `V ⟶ W` is an open immersion of algebraic spaces.

```lean
theorem isOpenImmersion_iff_exists_isOpenImmersion_representingMap :
    IsOpenImmersion B S hS f ↔
      ∃ (V : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (_hV : IsAlgebraicSpace B S hS V)
        (eV : StacksRepresentableCFG.EquivalenceOver
          Q.pt.val.p (presheafOfCategories (V ⋙ typeToCat)).p),
        Space.IsOpenImmersion B S hS (representingMap B S hS Q.pt 𝒲 V W eV eW Q.fst)
```

## Tag 0504, a lemma

[Tag 0504](https://stacks.math.columbia.edu/tag/0504) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isMonomorphism_of_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionMonomorphism.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionMonomorphism.lean#L64).

> An immersion of algebraic stacks over `S` is a monomorphism.

```lean
theorem isMonomorphism_of_isImmersion (f : 𝒳 ⟶ 𝒴) (hf : IsImmersion B S hS f) :
    IsMonomorphism B S hS f
```

## Tag 0H20, a lemma

[Tag 0H20](https://stacks.math.columbia.edu/tag/0H20) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isEmbedding_pointsMap_of_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionPointsAlgebraicStack.lean, line 281](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionPointsAlgebraicStack.lean#L281). The attribute's comment: “homeomorphism onto the image”.

> **Stacks 0H20, the homeomorphism onto the image.** An immersion of algebraic stacks over `S`
> is a topological embedding on the spaces of points of Stacks 04XG and 04XL.

```lean
theorem isEmbedding_pointsMap_of_isImmersion (f : 𝒳 ⟶ 𝒴) (hf : IsImmersion B S hS f) :
    @Topology.IsEmbedding _ _ (Stack.pointTopology B S hS 𝒳.val)
      (Stack.pointTopology B S hS 𝒴.val)
      (Stack.pointsMap B S hS 𝒳.val.val 𝒳.val.property 𝒴.val.property f.hom.hom)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyClosed_range_pointsMap_of_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionPointsAlgebraicStack.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionPointsAlgebraicStack.lean#L298). The attribute's comment: “locally closed image”.

> **Stacks 0H20, the locally closed image.** The image on points of an immersion of algebraic
> stacks over `S` is a locally closed subset of the space of points of the target.

```lean
theorem isLocallyClosed_range_pointsMap_of_isImmersion (f : 𝒳 ⟶ 𝒴)
    (hf : IsImmersion B S hS f) :
    @IsLocallyClosed _ (Stack.pointTopology B S hS 𝒴.val)
      (Set.range (Stack.pointsMap B S hS 𝒳.val.val 𝒳.val.property 𝒴.val.property f.hom.hom))
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isClosedMap_pointsMap_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionPointsAlgebraicStack.lean, line 314](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionPointsAlgebraicStack.lean#L314). The attribute's comment: “closed immersions are closed on points”.

> **Stacks 0H20, closed immersions.** A closed immersion of algebraic stacks over `S` is a
> closed map on the spaces of points of Stacks 04XG and 04XL.

```lean
theorem isClosedMap_pointsMap_of_isClosedImmersion (f : 𝒳 ⟶ 𝒴)
    (hf : IsClosedImmersion B S hS f) :
    @IsClosedMap _ _ (Stack.pointTopology B S hS 𝒳.val) (Stack.pointTopology B S hS 𝒴.val)
      (Stack.pointsMap B S hS 𝒳.val.val 𝒳.val.property 𝒴.val.property f.hom.hom)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isOpenMap_pointsMap_of_isOpenImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionPointsAlgebraicStack.lean, line 335](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionPointsAlgebraicStack.lean#L335). The attribute's comment: “open immersions are open on points”.

> **Stacks 0H20, open immersions.** An open immersion of algebraic stacks over `S` is an open
> map on the spaces of points of Stacks 04XG and 04XL.

```lean
theorem isOpenMap_pointsMap_of_isOpenImmersion (f : 𝒳 ⟶ 𝒴)
    (hf : IsOpenImmersion B S hS f) :
    @IsOpenMap _ _ (Stack.pointTopology B S hS 𝒳.val) (Stack.pointTopology B S hS 𝒴.val)
      (Stack.pointsMap B S hS 𝒳.val.val 𝒳.val.property 𝒴.val.property f.hom.hom)
```

## Tag 0505, a lemma

[Tag 0505](https://stacks.math.columbia.edu/tag/0505) in the Stacks Project.

**`AlgebraicGeometry.Stack.isInvariantLocallyClosed_range_of_isImmersion_essImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionIntoQuotientStackSubspace.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionIntoQuotientStackSubspace.lean#L351). The attribute's comment: “the R-invariant locally closed subspace Z = U' of U cut out by an immersion into [U/R]; the 2-fibre product U' = 𝒵 ×_{[U/R]} U of Stacks 04Y6 is carried as the morphism m together with hmem, and the immersion property of m (Stacks 04XD applied to i) as hm; the presentation [Z/R_Z] ⟶ 𝒵 and the 2-commutative triangle are not proved”.

> **Stacks 0505, the invariant locally closed subspace.** Let `G = (U, R, s, t, c)` be a
> groupoid in algebraic spaces, let `i : 𝒵 ⟶ [U/R]` be a 1-morphism over the big fppf site, and
> let `m : U' ⟶ U` be an immersion of algebraic spaces whose range is, pointwise, the inverse
> image along `U ⟶ [U/R]` of the essential image of `i` — which is what it is for `U'` to be the
> 2-fibre product `𝒵 ×_{[U/R]} U` of Stacks 04Y6. Then the range of `m` is an `R`-invariant
> locally closed subspace `Z ⊆ U` in the sense of Stacks 044F, part (2), and `U' ≅ Z`.
>
> Smoothness of `G` is not used.

```lean
theorem isInvariantLocallyClosed_range_of_isImmersion_essImage
    (hm : Space.IsImmersion C S hS m.hom)
    (hmem : ∀ (W : (BigFppfOver C S hS)ᵒᵖ) (u : G.objects.obj.obj W),
      u ∈ (Subfunctor.range m.hom).obj W ↔
        i.toFunctor.essImage ((quotientStackProjection G).obj ⟨W.unop, Discrete.mk u⟩)) :
    IsInvariantLocallyClosed G (Subfunctor.range m.hom)
```

**`AlgebraicGeometry.Stack.isInvariantClosed_range_of_isClosedImmersion_essImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionIntoQuotientStackSubspace.lean, line 367](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionIntoQuotientStackSubspace.lean#L367). The attribute's comment: “the R-invariant closed subspace, for a closed immersion into [U/R]; the 2-fibre product of Stacks 04Y6 is carried as m together with hmem, and the closed immersion property of m (Stacks 04XD applied to i) as hm”.

> **Stacks 0505, the invariant closed subspace.** In the situation of
> `AlgebraicGeometry.Stack.isInvariantLocallyClosed_range_of_isImmersion_essImage`, if `m` is a
> closed immersion — which is what the source gets from `i` being a closed immersion — then the
> range of `m` is an invariant *closed* subspace of `U`.

```lean
theorem isInvariantClosed_range_of_isClosedImmersion_essImage
    (hm : Space.IsClosedImmersion C S hS m.hom)
    (hmem : ∀ (W : (BigFppfOver C S hS)ᵒᵖ) (u : G.objects.obj.obj W),
      u ∈ (Subfunctor.range m.hom).obj W ↔
        i.toFunctor.essImage ((quotientStackProjection G).obj ⟨W.unop, Discrete.mk u⟩)) :
    IsInvariantClosed G (Subfunctor.range m.hom)
```

**`AlgebraicGeometry.Stack.isInvariantOpen_range_of_isOpenImmersion_essImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionIntoQuotientStackSubspace.lean, line 386](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionIntoQuotientStackSubspace.lean#L386). The attribute's comment: “the R-invariant open subspace, for an open immersion into [U/R]; the 2-fibre product of Stacks 04Y6 is carried as m together with hmem, and the open immersion property of m (Stacks 04XD applied to i) as hm”.

> **Stacks 0505, the invariant open subspace.** In the situation of
> `AlgebraicGeometry.Stack.isInvariantLocallyClosed_range_of_isImmersion_essImage`, if `m` is an
> open immersion — which is what the source gets from `i` being an open immersion — then the range
> of `m` is an invariant *open* subspace of `U` in the sense of Stacks 044F, part (1).

```lean
theorem isInvariantOpen_range_of_isOpenImmersion_essImage
    (hm : Space.IsOpenImmersion C S hS m.hom)
    (hmem : ∀ (W : (BigFppfOver C S hS)ᵒᵖ) (u : G.objects.obj.obj W),
      u ∈ (Subfunctor.range m.hom).obj W ↔
        i.toFunctor.essImage ((quotientStackProjection G).obj ⟨W.unop, Discrete.mk u⟩)) :
    IsInvariantOpen G (Subfunctor.range m.hom)
```

**`AlgebraicGeometry.Stack.essImage_quotientStackProjection_iff_exists_twoFibreProductOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionIntoQuotientStackSubspace.lean, line 408](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionIntoQuotientStackSubspace.lean#L408). The attribute's comment: “the points of U covered by the 2-fibre product U' = 𝒵 ×_{[U/R]} U of Stacks 04Y6 are exactly those whose image in [U/R] is in the essential image of i; nothing carried”.

> **Stacks 0505: the locus the 2-fibre product of Stacks 04Y6 covers is the essential-image
> locus.** Let `G = (U, R, s, t, c)` be a groupoid in algebraic spaces and let `i : 𝒵 ⟶ [U/R]` be
> a 1-morphism over the big fppf site whose source is fibred in groupoids. A point `x` of `U`
> over an object `W` of the site is carried by an object of the 2-fibre product
> `U ×_{[U/R]} 𝒵` — the `U'` Stacks 04Y6 forms, for the canonical atlas `U ⟶ [U/R]` of
> Stacks 044R — exactly when the image of `x` in `[U/R]` lies in the essential image of `i`.
>
> Nothing is carried: this is the hypothesis `hmem` of
> `AlgebraicGeometry.Stack.isInvariantLocallyClosed_range_of_isImmersion_essImage`, in the shape
> Stacks 04Y6 states it, proved rather than assumed.

```lean
theorem essImage_quotientStackProjection_iff_exists_twoFibreProductOver
    (h𝒵 : 𝒵.p.IsFiberedInGroupoids) (W : (BigFppfOver C S hS)ᵒᵖ)
    (x : G.objects.obj.obj W) :
    i.toFunctor.essImage ((quotientStackProjection G).obj ⟨W.unop, Discrete.mk x⟩) ↔
      ∃ P : TwoFibreProductOver (fibredCategory C S hS G.objects.obj).val.p 𝒵.p
          (quotientStack G).p (quotientStackProjection G).toFunctor i.toFunctor,
        P.x = ⟨W.unop, Discrete.mk x⟩
```

**`AlgebraicGeometry.Stack.essImage_quotientStackProjection_iff_exists_twoFibreProductSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionIntoQuotientStackSubspace.lean, line 435](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionIntoQuotientStackSubspace.lean#L435). The attribute's comment: “the points of U covered by the apex of the canonical 2-fibre product square of Stacks 04Y6 at the atlas U ⟶ [U/R] are exactly those whose image in [U/R] is in the essential image of the other leg; nothing carried”.

> **Stacks 0505 for the canonical 2-fibre product square of Stacks 04Y6.** The same statement
> as `AlgebraicGeometry.Stack.essImage_quotientStackProjection_iff_exists_twoFibreProductOver`,
> read on the apex of `CategoryTheory.CatFiberedInGroupoids.twoFibreProductSquare` at the
> canonical atlas `AlgebraicGeometry.Stack.quotientStackProjectionHom` of Stacks 044R and at a
> 1-morphism `j : 𝒴 ⟶ [U/R]` of categories fibred in groupoids. That square is the
> `U' = 𝒰 ×_𝒳 𝒳'` of Stacks 04Y6, formed at the universes a quotient stack lives at.
>
> Nothing is carried.

```lean
theorem essImage_quotientStackProjection_iff_exists_twoFibreProductSquare
    (𝒴 : CatFiberedInGroupoids.{u, u + 1, u + 1, u + 1} (BigFppfOver C S hS))
    (j : 𝒴 ⟶ CatFiberedInGroupoids.mk (quotientStack G)
      (isFiberedInGroupoids_quotientStack G))
    (W : (BigFppfOver C S hS)ᵒᵖ) (x : G.objects.obj.obj W) :
    j.hom.toFunctor.essImage
        ((quotientStackProjection G).obj ⟨W.unop, Discrete.mk x⟩) ↔
      ∃ P : (CatFiberedInGroupoids.twoFibreProductSquare.{u, u + 1, u + 1, u + 1}
          (quotientStackProjectionHom G) j).pt.val.obj,
        P.x = ULiftHom.objUp ⟨W.unop, Discrete.mk x⟩
```

**`AlgebraicGeometry.Stack.exists_isInvariantLocallyClosed_groupoidPresentation_of_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionQuotientStackPresentation.lean, line 490](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionQuotientStackPresentation.lean#L490).

> **Stacks 0505.** Let `G = (U, R, s, t, c)` be a smooth groupoid in algebraic spaces over a
> scheme `S` of a big fppf site, and let `i : 𝒵 ⟶ [U/R]` be an immersion — a 1-morphism
> representable by algebraic spaces with the relative immersion property of Stacks 04XB, that is
> part (3) of Stacks 04YL — whose source satisfies descent. Then there are an `R`-invariant locally
> closed subspace `Z ⊆ U` in the sense of Stacks 044F, part (2), a *presentation*
> `[Z/R_Z] ⟶ 𝒵` of `𝒵` in the sense of Stacks 04TI by the restriction `R_Z` of `G` to `Z`
> (Stacks 044B), and a 2-isomorphism making the triangle
>
>     [Z/R_Z] ⟶ 𝒵 ⟶ [U/R]        [Z/R_Z] ⟶ [U/R]
>
> 2-commutative, the second leg being the 1-morphism of Stacks 046Q induced by the canonical
> morphism of groupoids from the restriction. If `i` is a closed, respectively open, immersion then
> `Z` is a closed, respectively open, subspace of `U`.
>
> `Z` is pinned down by the conclusion: it is, pointwise, the locus of `U` whose image in `[U/R]`
> lies in the essential image of `i`, which is the `𝒵 ×_{[U/R]} U` of Stacks 04Y6 read as a
> subspace of `U`.
>
> The subspace and its invariance are
> `AlgebraicGeometry.Stack.exists_isInvariantLocallyClosed_range_of_isImmersion_quotientStack`;
> smoothness of the restricted groupoid, the one place smoothness of `G` is used, is
> `AlgebraicGeometry.GroupoidInAlgebraicSpaces.isSmoothGroupoid_restrict_invariant`; and the
> equivalence together with the 2-commutative triangle is
> `AlgebraicGeometry.Stack.exists_equivalenceOver_quotientStack_restrict`, whose two inputs are
> full faithfulness of `i` (**Stacks 05UK** at the monomorphism **Stacks 042R** supplies, which is
> **Stacks 0504**) and the pointwise description of `Z`.

```lean
theorem exists_isInvariantLocallyClosed_groupoidPresentation_of_isImmersion
    (G : GroupoidInAlgebraicSpaces C S hS (baseSpace C S hS))
    (hG : GroupoidInAlgebraicSpaces.IsSmooth C S hS G)
    (h𝒵 : 𝒵.val.p.IsStack (BigFppfOver.topology C S hS))
    (i : 𝒵 ⟶ CatFiberedInGroupoids.mk (quotientStack G) (isFiberedInGroupoids_quotientStack G))
    (hi : IsRepresentableByAlgebraicSpaces C S hS i.hom)
    (himm : IsImmersion C S hS i) :
    ∃ (Z : Subfunctor G.objects.obj) (hZ : IsInvariantLocallyClosed G Z)
      (hsm : GroupoidInAlgebraicSpaces.IsSmooth C S hS
        (G.restrict (subspaceInclusion G Z hZ.1.1)).groupoid)
      (e : StacksRepresentableCFG.EquivalenceOver
        (quotientStack (G.restrict (subspaceInclusion G Z hZ.1.1)).groupoid).p 𝒵.val.p),
      Nonempty ((GroupoidPresentation.basedFunctor
            (⟨(G.restrict (subspaceInclusion G Z hZ.1.1)).groupoid, hsm, e⟩ :
              GroupoidPresentation C S hS 𝒵.val)).comp i.hom ≅
          quotientStackMap (G.restrict (subspaceInclusion G Z hZ.1.1)).hom) ∧
        (∀ (W : (BigFppfOver C S hS)ᵒᵖ) (u : G.objects.obj.obj W),
          u ∈ Z.obj W ↔ (CatFiberedInGroupoids.homFunctor i).essImage
            ((quotientStackProjection G).obj ⟨W.unop, Discrete.mk u⟩)) ∧
        (IsClosedImmersion C S hS i → Space.IsClosedSubspace C S hS Z) ∧
        (IsOpenImmersion C S hS i → Space.IsOpenSubspace C S hS Z)
```

**`AlgebraicGeometry.Stack.exists_isInvariantLocallyClosed_range_of_isImmersion_quotientStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackImmersionBaseChangeSpace.lean, line 315](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackImmersionBaseChangeSpace.lean#L315). The attribute's comment: “the R-invariant locally closed subspace Z of U cut out by an immersion into [U/R], together with its pointwise description as the locus of U whose image in [U/R] lies in the essential image of i; nothing carried -- the projection m of the 2-fibre product of Stacks 04Y6 and its immersion property are produced here rather than assumed”.

> Let `G = (U, R, s, t, c)` be a groupoid in algebraic spaces over an algebraic space `A` over a
> scheme `S` of a big fppf site, and let `i : 𝒵 ⟶ [U/R]` be an immersion which is representable by
> algebraic spaces. Then the locus of `U` whose image in `[U/R]` lies in the essential image of `i`
> is an `R`-invariant locally closed subspace `Z ⊆ U`; it is the range of an immersion of algebraic
> spaces `m : U' ⟶ U`.

```lean
theorem exists_isInvariantLocallyClosed_range_of_isImmersion_quotientStack
    (G : GroupoidInAlgebraicSpaces C S hS A)
    {𝒵 : CatFiberedInGroupoids.{u, u + 1, u + 1, u + 1} (BigFppfOver C S hS)}
    (i : 𝒵 ⟶ CatFiberedInGroupoids.mk (quotientStack G) (isFiberedInGroupoids_quotientStack G))
    (hi : IsRepresentableByAlgebraicSpaces C S hS i.hom)
    (himm : IsImmersion C S hS i) :
    ∃ (U' : AlgebraicSpaces C S hS) (m : U' ⟶ G.objects),
      Space.IsImmersion C S hS m.hom ∧
        IsInvariantLocallyClosed G (Subfunctor.range m.hom) ∧
        ∀ (W : (BigFppfOver C S hS)ᵒᵖ) (u : G.objects.obj.obj W),
          u ∈ (Subfunctor.range m.hom).obj W ↔
            i.hom.toFunctor.essImage
              ((quotientStackProjection G).obj ⟨W.unop, Discrete.mk u⟩)
```

**`AlgebraicGeometry.Stack.exists_isInvariantOpen_range_of_isOpenImmersion_quotientStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackImmersionBaseChangeSpace.lean, line 338](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackImmersionBaseChangeSpace.lean#L338). The attribute's comment: “the R-invariant open subspace of U, for an open immersion into [U/R]; nothing carried”.

> The open-immersion case of
> `AlgebraicGeometry.Stack.exists_isInvariantLocallyClosed_range_of_isImmersion_quotientStack`: the
> locus is an `R`-invariant open subspace of `U`.

```lean
theorem exists_isInvariantOpen_range_of_isOpenImmersion_quotientStack
    (G : GroupoidInAlgebraicSpaces C S hS A)
    {𝒵 : CatFiberedInGroupoids.{u, u + 1, u + 1, u + 1} (BigFppfOver C S hS)}
    (i : 𝒵 ⟶ CatFiberedInGroupoids.mk (quotientStack G) (isFiberedInGroupoids_quotientStack G))
    (hi : IsRepresentableByAlgebraicSpaces C S hS i.hom)
    (hopen : IsOpenImmersion C S hS i) :
    ∃ (U' : AlgebraicSpaces C S hS) (m : U' ⟶ G.objects),
      Space.IsOpenImmersion C S hS m.hom ∧
        IsInvariantOpen G (Subfunctor.range m.hom) ∧
        ∀ (W : (BigFppfOver C S hS)ᵒᵖ) (u : G.objects.obj.obj W),
          u ∈ (Subfunctor.range m.hom).obj W ↔
            i.hom.toFunctor.essImage
              ((quotientStackProjection G).obj ⟨W.unop, Discrete.mk u⟩)
```

**`AlgebraicGeometry.Stack.exists_isInvariantClosed_range_of_isClosedImmersion_quotientStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackImmersionBaseChangeSpace.lean, line 361](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackImmersionBaseChangeSpace.lean#L361). The attribute's comment: “the R-invariant closed subspace of U, for a closed immersion into [U/R]; nothing carried”.

> The closed-immersion case of
> `AlgebraicGeometry.Stack.exists_isInvariantLocallyClosed_range_of_isImmersion_quotientStack`: the
> locus is an `R`-invariant closed subspace of `U`.

```lean
theorem exists_isInvariantClosed_range_of_isClosedImmersion_quotientStack
    (G : GroupoidInAlgebraicSpaces C S hS A)
    {𝒵 : CatFiberedInGroupoids.{u, u + 1, u + 1, u + 1} (BigFppfOver C S hS)}
    (i : 𝒵 ⟶ CatFiberedInGroupoids.mk (quotientStack G) (isFiberedInGroupoids_quotientStack G))
    (hi : IsRepresentableByAlgebraicSpaces C S hS i.hom)
    (hclosed : IsClosedImmersion C S hS i) :
    ∃ (U' : AlgebraicSpaces C S hS) (m : U' ⟶ G.objects),
      Space.IsClosedImmersion C S hS m.hom ∧
        IsInvariantClosed G (Subfunctor.range m.hom) ∧
        ∀ (W : (BigFppfOver C S hS)ᵒᵖ) (u : G.objects.obj.obj W),
          u ∈ (Subfunctor.range m.hom).obj W ↔
            i.hom.toFunctor.essImage
              ((quotientStackProjection G).obj ⟨W.unop, Discrete.mk u⟩)
```

## Tag 04YN, a lemma

[Tag 04YN](https://stacks.math.columbia.edu/tag/04YN) in the Stacks Project.

**`AlgebraicGeometry.Stack.isImmersion_quotientStackMap_of_invariantRestrictionBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/InvariantSubspaceQuotientImmersion.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/InvariantSubspaceQuotientImmersion.lean#L238). The attribute's comment: “the immersion [Z/R_Z] ⟶ [U/R] for an invariant locally closed subspace”.

> **Stacks 04YN**, the immersion. For a smooth groupoid `G` in algebraic spaces and an invariant
> locally closed subspace `Z` of its object space, the 1-morphism `[Z/R_Z] ⟶ [U/R]` of Stacks 044B
> is an immersion of algebraic stacks: it is representable by algebraic spaces and an immersion in
> the sense of Stacks 04XB.

```lean
theorem isImmersion_quotientStackMap_of_invariantRestrictionBaseChange
    {G : GroupoidInAlgebraicSpaces C S hS B} (hG : IsSmooth C S hS G)
    {Z : Subfunctor G.objects.obj} (hZ : IsInvariantLocallyClosed G Z) :
    IsRepresentableByAlgebraicSpaces C S hS
        (quotientStackMapHom (G.restrict (subspaceInclusion G Z hZ.1.1)).hom).hom ∧
      Stack.IsImmersion C S hS
        (quotientStackMapHom (G.restrict (subspaceInclusion G Z hZ.1.1)).hom)
```

**`AlgebraicGeometry.Stack.isOpenImmersion_quotientStackMap_of_invariantRestrictionBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/InvariantSubspaceQuotientImmersion.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/InvariantSubspaceQuotientImmersion.lean#L255). The attribute's comment: “the open immersion [Z/R_Z] ⟶ [U/R] for an invariant open subspace”.

> **Stacks 04YN**, the open immersion. For a smooth groupoid `G` in algebraic spaces and an
> invariant open subspace `Z` of its object space, the 1-morphism `[Z/R_Z] ⟶ [U/R]` of Stacks 044B
> is an open immersion of algebraic stacks: it is representable by algebraic spaces and an open
> immersion in the sense of Stacks 04XB.

```lean
theorem isOpenImmersion_quotientStackMap_of_invariantRestrictionBaseChange
    {G : GroupoidInAlgebraicSpaces C S hS B} (hG : IsSmooth C S hS G)
    {Z : Subfunctor G.objects.obj} (hZ : IsInvariantOpen G Z) :
    IsRepresentableByAlgebraicSpaces C S hS
        (quotientStackMapHom (G.restrict (subspaceInclusion G Z hZ.1.1)).hom).hom ∧
      Stack.IsOpenImmersion C S hS
        (quotientStackMapHom (G.restrict (subspaceInclusion G Z hZ.1.1)).hom)
```

**`AlgebraicGeometry.Stack.isClosedImmersion_quotientStackMap_of_invariantRestrictionBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/InvariantSubspaceQuotientImmersion.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/InvariantSubspaceQuotientImmersion.lean#L273). The attribute's comment: “the closed immersion [Z/R_Z] ⟶ [U/R] for an invariant closed subspace”.

> **Stacks 04YN**, the closed immersion. For a smooth groupoid `G` in algebraic spaces and an
> invariant closed subspace `Z` of its object space, the 1-morphism `[Z/R_Z] ⟶ [U/R]` of
> Stacks 044B is a closed immersion of algebraic stacks: it is representable by algebraic spaces and
> a closed immersion in the sense of Stacks 04XB.

```lean
theorem isClosedImmersion_quotientStackMap_of_invariantRestrictionBaseChange
    {G : GroupoidInAlgebraicSpaces C S hS B} (hG : IsSmooth C S hS G)
    {Z : Subfunctor G.objects.obj} (hZ : IsInvariantClosed G Z) :
    IsRepresentableByAlgebraicSpaces C S hS
        (quotientStackMapHom (G.restrict (subspaceInclusion G Z hZ.1.1)).hom).hom ∧
      Stack.IsClosedImmersion C S hS
        (quotientStackMapHom (G.restrict (subspaceInclusion G Z hZ.1.1)).hom)
```

## Tag 04YM, a definition

[Tag 04YM](https://stacks.math.columbia.edu/tag/04YM) in the Stacks Project.

**`AlgebraicGeometry.Stack.OpenSubstack`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Substack.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Substack.lean#L107). The attribute's comment: “open_substack”.

> **Stacks 04YM**, part (1). An *open substack* of an algebraic stack `𝒳` over `S` is a
> strictly full subcategory of `𝒳` which is an algebraic stack and whose canonical inclusion into
> `𝒳` is an open immersion.

```lean
structure OpenSubstack (𝒳 : AlgebraicStacks.{u, w} B S hS)
```

**`AlgebraicGeometry.Stack.OpenSubstack.ext`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Substack.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Substack.lean#L120). The attribute's comment: “open_substack”.

> Two open substacks with the same objects are equal.

```lean
theorem OpenSubstack.ext {𝒳 : AlgebraicStacks.{u, w} B S hS} {U V : OpenSubstack 𝒳}
    (h : U.property = V.property) : U = V
```

**`AlgebraicGeometry.Stack.fullSubcategoryInclusion_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Substack.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Substack.lean#L144). The attribute's comment: “open_substack”.

> On objects, the canonical inclusion forgets the membership proof.

```lean
theorem fullSubcategoryInclusion_obj (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (P : ObjectProperty 𝒳.val.val.obj)
    (hP : IsAlgebraicStack.{u, w} B S hS (fullSubcategoryBased 𝒳 P))
    (X : P.FullSubcategory) :
    (fullSubcategoryInclusion 𝒳 P hP).hom.hom.toFunctor.obj X = X.obj
```

**`AlgebraicGeometry.Stack.fullSubcategoryInclusion_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Substack.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Substack.lean#L153). The attribute's comment: “open_substack”.

> On morphisms, the canonical inclusion forgets the membership proof.

```lean
theorem fullSubcategoryInclusion_map (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (P : ObjectProperty 𝒳.val.val.obj)
    (hP : IsAlgebraicStack.{u, w} B S hS (fullSubcategoryBased 𝒳 P))
    {X Y : P.FullSubcategory} (f : X ⟶ Y) :
    (fullSubcategoryInclusion 𝒳 P hP).hom.hom.toFunctor.map f = f.hom
```

**`AlgebraicGeometry.Stack.IsClosedSubstack`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Substack.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Substack.lean#L165). The attribute's comment: “closed_substack”.

> **Stacks 04YM**, part (2). A property of the objects of an algebraic stack `𝒳` over `S`
> selects a *closed substack* when it is closed under isomorphism, its full subcategory is an
> algebraic stack, and the canonical inclusion of that full subcategory into `𝒳` is a closed
> immersion.

```lean
abbrev IsClosedSubstack (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (P : ObjectProperty 𝒳.val.val.obj) : Prop
```

**`AlgebraicGeometry.Stack.IsLocallyClosedSubstack`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Substack.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Substack.lean#L176). The attribute's comment: “locally_closed_substack”.

> **Stacks 04YM**, part (3). A property of the objects of an algebraic stack `𝒳` over `S`
> selects a *locally closed substack* when it is closed under isomorphism, its full subcategory is
> an algebraic stack, and the canonical inclusion of that full subcategory into `𝒳` is an
> immersion.

```lean
abbrev IsLocallyClosedSubstack (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (P : ObjectProperty 𝒳.val.val.obj) : Prop
```

## Tag 0506, a lemma

[Tag 0506](https://stacks.math.columbia.edu/tag/0506) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyClosedSubstack_essImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionSubstack.lean, line 363](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionSubstack.lean#L363). The attribute's comment: “the image is a locally closed substack”.

> **Stacks 0506**, the image is a locally closed substack. The essential image of an immersion
> of algebraic stacks over `S` cuts out a locally closed substack of its target.
>
> It is closed under isomorphism because an essential image always is; its full subcategory is an
> algebraic stack by Stacks 03YQ; and the inclusion of that full subcategory is an immersion because
> the immersion `i` factors through it by an equivalence, so Stacks 0457 transports both
> representability by algebraic spaces and the Stacks 04XB immersion condition.

```lean
theorem isLocallyClosedSubstack_essImage (i : 𝒵 ⟶ 𝒳) (hi : IsImmersion B S hS i) :
    IsLocallyClosedSubstack 𝒳 (CatFiberedInGroupoids.homFunctor i.hom).essImage
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.exists_isEquivalence_to_essImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionSubstack.lean, line 372](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionSubstack.lean#L372). The attribute's comment: “the factorization through the image”.

> **Stacks 0506**, the factorization. An immersion of algebraic stacks over `S` factors as a
> 1-morphism onto the full subcategory cut out by its essential image whose underlying functor is an
> equivalence of categories, followed by the inclusion of that full subcategory.

```lean
theorem exists_isEquivalence_to_essImage (i : 𝒵 ⟶ 𝒳) (hi : IsImmersion B S hS i)
    (hP : IsAlgebraicStack.{u, w} B S hS
      (fullSubcategoryBased 𝒳 (CatFiberedInGroupoids.homFunctor i.hom).essImage)) :
    ∃ f : 𝒵 ⟶ fullSubcategoryAlgebraicStack 𝒳
        (CatFiberedInGroupoids.homFunctor i.hom).essImage hP,
      Functor.IsEquivalence (CatFiberedInGroupoids.homFunctor f.hom) ∧
        Nonempty (f ≫ fullSubcategoryInclusion 𝒳
          (CatFiberedInGroupoids.homFunctor i.hom).essImage hP ≅ i)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.eq_essImage_of_isEquivalence_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionSubstack.lean, line 394](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionSubstack.lean#L394). The attribute's comment: “uniqueness of the substack”.

> **Stacks 0506**, uniqueness. A strictly full subcategory of an algebraic stack which is an
> algebraic stack and through which an immersion factors by a 1-morphism whose underlying functor is
> an equivalence of categories is cut out by the essential image of the immersion.
>
> The essential image of the inclusion of a strictly full subcategory is the property cutting it
> out, and precomposing with an essentially surjective functor does not change an essential image,
> so the essential image of the immersion is that property.

```lean
theorem eq_essImage_of_isEquivalence_factorization (i : 𝒵 ⟶ 𝒳)
    (P : ObjectProperty 𝒳.val.val.obj) (hstrict : P.IsClosedUnderIsomorphisms)
    (hP : IsAlgebraicStack.{u, w} B S hS (fullSubcategoryBased 𝒳 P))
    (f : 𝒵 ⟶ fullSubcategoryAlgebraicStack 𝒳 P hP)
    (hf : Functor.IsEquivalence (CatFiberedInGroupoids.homFunctor f.hom))
    (α : f ≫ fullSubcategoryInclusion 𝒳 P hP ≅ i) :
    P = (CatFiberedInGroupoids.homFunctor i.hom).essImage
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.existsUnique_locallyClosedSubstack_of_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionSubstack.lean, line 427](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionSubstack.lean#L427).

> **Stacks 0506.** For an immersion `i : 𝒵 ⟶ 𝒳` of algebraic stacks over `S` there is a
> *unique* locally closed substack of `𝒳` through which `i` factors as a 1-morphism whose underlying
> functor is an equivalence of categories followed by the inclusion of the substack.
>
> That substack is cut out by the essential image of the functor underlying `i`.

```lean
theorem existsUnique_locallyClosedSubstack_of_isImmersion (i : 𝒵 ⟶ 𝒳)
    (hi : IsImmersion B S hS i) :
    ∃! P : ObjectProperty 𝒳.val.val.obj,
      IsLocallyClosedSubstack 𝒳 P ∧
        ∃ (hP : IsAlgebraicStack.{u, w} B S hS (fullSubcategoryBased 𝒳 P))
          (f : 𝒵 ⟶ fullSubcategoryAlgebraicStack 𝒳 P hP),
          Functor.IsEquivalence (CatFiberedInGroupoids.homFunctor f.hom) ∧
            Nonempty (f ≫ fullSubcategoryInclusion 𝒳 P hP ≅ i)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isClosedSubstack_essImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionSubstack.lean, line 449](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionSubstack.lean#L449). The attribute's comment: “the image of a closed immersion is a closed substack”.

> **Stacks 0506**, the closed case. The essential image of a closed immersion of algebraic
> stacks over `S` cuts out a closed substack of its target.
>
> A closed immersion is an immersion, so the essential image cuts out a locally closed substack; the
> closed-immersion condition on the inclusion is the condition on `i` transported across the
> equivalence by Stacks 0457.

```lean
theorem isClosedSubstack_essImage (i : 𝒵 ⟶ 𝒳) (hi : IsClosedImmersion B S hS i) :
    IsClosedSubstack 𝒳 (CatFiberedInGroupoids.homFunctor i.hom).essImage
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.exists_openSubstack_essImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionSubstack.lean, line 464](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionSubstack.lean#L464). The attribute's comment: “the image of an open immersion is an open substack”.

> **Stacks 0506**, the open case. The essential image of an open immersion of algebraic stacks
> over `S` is the object property of an open substack of its target.
>
> An open immersion is an immersion, so the essential image cuts out a locally closed substack; the
> open-immersion condition on the inclusion is the condition on `i` transported across the
> equivalence by Stacks 0457.

```lean
theorem exists_openSubstack_essImage (i : 𝒵 ⟶ 𝒳) (hi : IsOpenImmersion B S hS i) :
    ∃ U : OpenSubstack 𝒳,
      U.property = (CatFiberedInGroupoids.homFunctor i.hom).essImage
```

## Tag 0507, a lemma

[Tag 0507](https://stacks.math.columbia.edu/tag/0507) in the Stacks Project.

**`AlgebraicGeometry.Stack.factorsThroughSubstack_iff_presentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubstackFactorizationPresentation.lean, line 386](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubstackFactorizationPresentation.lean#L386). The attribute's comment: “factorization_criterion”.

> **Stacks 0507**, the factorization criterion. Let `𝒳` be an algebraic stack over `S`
> presented by a smooth groupoid in algebraic spaces `G` through an equivalence `E` over the big
> fppf site, let `P` cut out an open, closed or locally closed substack of `𝒳`, and let
> `f : 𝒴 ⟶ 𝒳` be a 1-morphism of algebraic stacks. Then `f` factors through the substack, over
> the big fppf site and up to a 2-isomorphism, if and only if the base change of `f` along the
> presentation `S_U ⟶ 𝒳` factors through the base change of the substack.
>
> The proof is pointwise on both sides, and the content is that membership of the substack is
> local on the site; see the module documentation.

```lean
theorem factorsThroughSubstack_iff_presentation
    (𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS)
    (G : GroupoidInAlgebraicSpaces B S hS (baseSpace B S hS))
    (_hG : GroupoidInAlgebraicSpaces.IsSmooth B S hS G)
    (E : (quotientStack G).obj ⥤ 𝒳.val.val.obj)
    [E.IsEquivalence]
    (hE : E ⋙ 𝒳.val.val.p = (quotientStack G).p)
    (P : ObjectProperty 𝒳.val.val.obj)
    (hP : (IsLocallyClosedSubstack 𝒳 P ∨ IsClosedSubstack 𝒳 P) ∨
      ∃ V : OpenSubstack 𝒳, V.property = P)
    (f : 𝒴 ⟶ 𝒳) :
    let U := (fibredCategory B S hS G.objects.obj).val
    let p := (quotientStackProjection G).comp
      (⟨E, hE⟩ : (quotientStack G) ⥤ᵇ 𝒳.val.val)
    let F := TwoFibreProductOver.structureFunctor U.p 𝒴.val.val.p 𝒳.val.val.p
      p.toFunctor f.hom.hom.toFunctor
    let D := BasedCategory.ofFunctor F
    let q : D ⥤ᵇ U :=
      { toFunctor := TwoFibreProductOver.fst U.p 𝒴.val.val.p 𝒳.val.val.p
          p.toFunctor f.hom.hom.toFunctor
        w := TwoFibreProductOver.fst_comp_eq }
    let i := fullSubcategoryBasedInclusion 𝒳 P
    let Z := BasedCategory.ofFunctor
      (TwoFibreProductOver.structureFunctor U.p
        (fullSubcategoryBased 𝒳 P).p
        𝒳.val.val.p p.toFunctor i.toFunctor)
    let z : Z ⥤ᵇ U :=
      { toFunctor := TwoFibreProductOver.fst U.p
          (fullSubcategoryBased 𝒳 P).p
          𝒳.val.val.p p.toFunctor i.toFunctor
        w := TwoFibreProductOver.fst_comp_eq }
    (∃ g : 𝒴.val.val ⥤ᵇ fullSubcategoryBased 𝒳 P,
      Nonempty (g.comp i ≅ f.hom.hom)) ↔
      (∃ g : D ⥤ᵇ Z, Nonempty (g.comp z ≅ q))
```

**`AlgebraicGeometry.Stack.exists_equiv_isInvariantLocallyClosed_presentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubstackPresentationCorrespondence.lean, line 505](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubstackPresentationCorrespondence.lean#L505). The attribute's comment: “locally closed”.

> **Stacks 0507**, locally closed substacks. Let `[U/R] ⟶ 𝒳` be a presentation of an algebraic
> stack. There is a canonical bijection from the locally closed substacks `𝒵` of `𝒳` to the
> `R`-invariant locally closed subspaces of `U`, sending `𝒵` to `U ×_𝒳 𝒵`. Moreover, a 1-morphism
> `f : 𝒴 ⟶ 𝒳` of algebraic stacks factors through `𝒵` if and only if `𝒴 ×_𝒳 U ⟶ U` factors through
> `U ×_𝒳 𝒵`.
>
> Here `[U/R] ⟶ 𝒳` is a presentation of the algebraic stack `𝒳` (Stacks 04TI), and `π : U ⟶ 𝒳`
> is the canonical projection followed by the equivalence. The bijection `e` sends `𝒵` to the
> subspace of `U` that is the image of the projection `U ×_𝒳 𝒵 ⟶ U` from the 2-fibre product
> (first conjunct). For every 1-morphism `f : 𝒴 ⟶ 𝒳` of algebraic stacks, `f` factors through `𝒵`
> over the site and up to a 2-isomorphism exactly when the projection `𝒴 ×_𝒳 U ⟶ U` factors
> through `U ×_𝒳 𝒵` (second conjunct), and exactly when the `U`-component of every object of
> `𝒴 ×_𝒳 U` lies in `e 𝒵` (third conjunct), which is to say that `𝒴 ×_𝒳 U ⟶ U` factors through
> the subspace `e 𝒵`.

```lean
theorem exists_equiv_isInvariantLocallyClosed_presentation :
    ∃ e : {P : ObjectProperty 𝒳.val.val.obj // IsLocallyClosedSubstack 𝒳 P} ≃
        {Z : Subfunctor Pr.groupoid.objects.obj // IsInvariantLocallyClosed Pr.groupoid Z},
      ∀ P : {P : ObjectProperty 𝒳.val.val.obj // IsLocallyClosedSubstack 𝒳 P},
        (∀ (T : BigFppfOver B S hS) (u : Pr.groupoid.objects.obj.obj (op T)),
          u ∈ (e P).1.obj (op T) ↔
            ∃ d : TwoFibreProductOver (fibredCategory B S hS Pr.groupoid.objects.obj).val.p
                (fullSubcategoryBased 𝒳 P.1).p 𝒳.val.val.p
                (presentationProjection Pr.groupoid Pr.basedFunctor.toFunctor
                  Pr.basedFunctor.w).toFunctor
                (fullSubcategoryBasedInclusion 𝒳 P.1).toFunctor,
              d.x = ⟨T, Discrete.mk u⟩) ∧
        ∀ (𝒴 : AlgebraicStacks.{u, w} B S hS) (f : 𝒴 ⟶ 𝒳),
          ((∃ g : 𝒴.val.val ⥤ᵇ fullSubcategoryBased 𝒳 P.1,
              Nonempty (g.comp (fullSubcategoryBasedInclusion 𝒳 P.1) ≅ f.hom.hom)) ↔
            ∃ g : BasedCategory.ofFunctor (TwoFibreProductOver.structureFunctor
                  (fibredCategory B S hS Pr.groupoid.objects.obj).val.p 𝒴.val.val.p 𝒳.val.val.p
                  (presentationProjection Pr.groupoid Pr.basedFunctor.toFunctor
                    Pr.basedFunctor.w).toFunctor f.hom.hom.toFunctor) ⥤ᵇ
                BasedCategory.ofFunctor (TwoFibreProductOver.structureFunctor
                  (fibredCategory B S hS Pr.groupoid.objects.obj).val.p
                  (fullSubcategoryBased 𝒳 P.1).p 𝒳.val.val.p
                  (presentationProjection Pr.groupoid Pr.basedFunctor.toFunctor
                    Pr.basedFunctor.w).toFunctor
                  (fullSubcategoryBasedInclusion 𝒳 P.1).toFunctor),
              Nonempty (g.comp (TwoFibreProductOver.fstBased (fullSubcategoryBased 𝒳 P.1).p
                  𝒳.val.val.p (presentationProjection Pr.groupoid Pr.basedFunctor.toFunctor
                    Pr.basedFunctor.w).toFunctor
                  (fullSubcategoryBasedInclusion 𝒳 P.1).toFunctor) ≅
                TwoFibreProductOver.fstBased 𝒴.val.val.p 𝒳.val.val.p
                  (presentationProjection Pr.groupoid Pr.basedFunctor.toFunctor
                    Pr.basedFunctor.w).toFunctor f.hom.hom.toFunctor)) ∧
          ((∃ g : 𝒴.val.val ⥤ᵇ fullSubcategoryBased 𝒳 P.1,
              Nonempty (g.comp (fullSubcategoryBasedInclusion 𝒳 P.1) ≅ f.hom.hom)) ↔
            ∀ d : TwoFibreProductOver (fibredCategory B S hS Pr.groupoid.objects.obj).val.p
                𝒴.val.val.p 𝒳.val.val.p
                (presentationProjection Pr.groupoid Pr.basedFunctor.toFunctor
                  Pr.basedFunctor.w).toFunctor f.hom.hom.toFunctor,
              d.x.fiber.as ∈ (e P).1.obj (op d.x.base))
```

**`AlgebraicGeometry.Stack.exists_equiv_isInvariantClosed_presentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubstackPresentationCorrespondence.lean, line 563](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubstackPresentationCorrespondence.lean#L563). The attribute's comment: “closed”.

> **Stacks 0507**, closed substacks. Let `[U/R] ⟶ 𝒳` be a presentation of an algebraic stack.
> There is a canonical bijection from the closed substacks `𝒵` of `𝒳` to the `R`-invariant closed
> subspaces of `U`, sending `𝒵` to `U ×_𝒳 𝒵`. Moreover, a 1-morphism `f : 𝒴 ⟶ 𝒳` of algebraic
> stacks factors through `𝒵` if and only if `𝒴 ×_𝒳 U ⟶ U` factors through `U ×_𝒳 𝒵`.
>
> Here `[U/R] ⟶ 𝒳` is a presentation of the algebraic stack `𝒳` (Stacks 04TI), and `π : U ⟶ 𝒳`
> is the canonical projection followed by the equivalence. The bijection `e` sends `𝒵` to the
> subspace of `U` that is the image of the projection `U ×_𝒳 𝒵 ⟶ U` from the 2-fibre product
> (first conjunct). For every 1-morphism `f : 𝒴 ⟶ 𝒳` of algebraic stacks, `f` factors through `𝒵`
> over the site and up to a 2-isomorphism exactly when the projection `𝒴 ×_𝒳 U ⟶ U` factors
> through `U ×_𝒳 𝒵` (second conjunct), and exactly when the `U`-component of every object of
> `𝒴 ×_𝒳 U` lies in `e 𝒵` (third conjunct), which is to say that `𝒴 ×_𝒳 U ⟶ U` factors through
> the subspace `e 𝒵`.

```lean
theorem exists_equiv_isInvariantClosed_presentation :
    ∃ e : {P : ObjectProperty 𝒳.val.val.obj // IsClosedSubstack 𝒳 P} ≃
        {Z : Subfunctor Pr.groupoid.objects.obj // IsInvariantClosed Pr.groupoid Z},
      ∀ P : {P : ObjectProperty 𝒳.val.val.obj // IsClosedSubstack 𝒳 P},
        (∀ (T : BigFppfOver B S hS) (u : Pr.groupoid.objects.obj.obj (op T)),
          u ∈ (e P).1.obj (op T) ↔
            ∃ d : TwoFibreProductOver (fibredCategory B S hS Pr.groupoid.objects.obj).val.p
                (fullSubcategoryBased 𝒳 P.1).p 𝒳.val.val.p
                (presentationProjection Pr.groupoid Pr.basedFunctor.toFunctor
                  Pr.basedFunctor.w).toFunctor
                (fullSubcategoryBasedInclusion 𝒳 P.1).toFunctor,
              d.x = ⟨T, Discrete.mk u⟩) ∧
        ∀ (𝒴 : AlgebraicStacks.{u, w} B S hS) (f : 𝒴 ⟶ 𝒳),
          ((∃ g : 𝒴.val.val ⥤ᵇ fullSubcategoryBased 𝒳 P.1,
              Nonempty (g.comp (fullSubcategoryBasedInclusion 𝒳 P.1) ≅ f.hom.hom)) ↔
            ∃ g : BasedCategory.ofFunctor (TwoFibreProductOver.structureFunctor
                  (fibredCategory B S hS Pr.groupoid.objects.obj).val.p 𝒴.val.val.p 𝒳.val.val.p
                  (presentationProjection Pr.groupoid Pr.basedFunctor.toFunctor
                    Pr.basedFunctor.w).toFunctor f.hom.hom.toFunctor) ⥤ᵇ
                BasedCategory.ofFunctor (TwoFibreProductOver.structureFunctor
                  (fibredCategory B S hS Pr.groupoid.objects.obj).val.p
                  (fullSubcategoryBased 𝒳 P.1).p 𝒳.val.val.p
                  (presentationProjection Pr.groupoid Pr.basedFunctor.toFunctor
                    Pr.basedFunctor.w).toFunctor
                  (fullSubcategoryBasedInclusion 𝒳 P.1).toFunctor),
              Nonempty (g.comp (TwoFibreProductOver.fstBased (fullSubcategoryBased 𝒳 P.1).p
                  𝒳.val.val.p (presentationProjection Pr.groupoid Pr.basedFunctor.toFunctor
                    Pr.basedFunctor.w).toFunctor
                  (fullSubcategoryBasedInclusion 𝒳 P.1).toFunctor) ≅
                TwoFibreProductOver.fstBased 𝒴.val.val.p 𝒳.val.val.p
                  (presentationProjection Pr.groupoid Pr.basedFunctor.toFunctor
                    Pr.basedFunctor.w).toFunctor f.hom.hom.toFunctor)) ∧
          ((∃ g : 𝒴.val.val ⥤ᵇ fullSubcategoryBased 𝒳 P.1,
              Nonempty (g.comp (fullSubcategoryBasedInclusion 𝒳 P.1) ≅ f.hom.hom)) ↔
            ∀ d : TwoFibreProductOver (fibredCategory B S hS Pr.groupoid.objects.obj).val.p
                𝒴.val.val.p 𝒳.val.val.p
                (presentationProjection Pr.groupoid Pr.basedFunctor.toFunctor
                  Pr.basedFunctor.w).toFunctor f.hom.hom.toFunctor,
              d.x.fiber.as ∈ (e P).1.obj (op d.x.base))
```

**`AlgebraicGeometry.Stack.exists_equiv_isInvariantOpen_presentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubstackPresentationCorrespondence.lean, line 630](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubstackPresentationCorrespondence.lean#L630). The attribute's comment: “open”.

> **Stacks 0507**, open substacks. Let `[U/R] ⟶ 𝒳` be a presentation of an algebraic stack.
> There is a canonical bijection from the open substacks `𝒵` of `𝒳` to the `R`-invariant open
> subspaces of `U`, sending `𝒵` to `U ×_𝒳 𝒵`. Moreover, a 1-morphism `f : 𝒴 ⟶ 𝒳` of algebraic
> stacks factors through `𝒵` if and only if `𝒴 ×_𝒳 U ⟶ U` factors through `U ×_𝒳 𝒵`.
>
> Here `[U/R] ⟶ 𝒳` is a presentation of the algebraic stack `𝒳` (Stacks 04TI), and `π : U ⟶ 𝒳`
> is the canonical projection followed by the equivalence. The bijection `e` sends `𝒵` to the
> subspace of `U` that is the image of the projection `U ×_𝒳 𝒵 ⟶ U` from the 2-fibre product
> (first conjunct). For every 1-morphism `f : 𝒴 ⟶ 𝒳` of algebraic stacks, `f` factors through `𝒵`
> over the site and up to a 2-isomorphism exactly when the projection `𝒴 ×_𝒳 U ⟶ U` factors
> through `U ×_𝒳 𝒵` (second conjunct), and exactly when the `U`-component of every object of
> `𝒴 ×_𝒳 U` lies in `e 𝒵` (third conjunct), which is to say that `𝒴 ×_𝒳 U ⟶ U` factors through
> the subspace `e 𝒵`. An `R`-invariant open subspace is one whose inverse image under the source
> map is contained in its inverse image under the target map (Stacks 044F, part (1)).

```lean
theorem exists_equiv_isInvariantOpen_presentation :
    ∃ e : OpenSubstack 𝒳 ≃
        {Z : Subfunctor Pr.groupoid.objects.obj // IsInvariantOpen Pr.groupoid Z},
      ∀ P : OpenSubstack 𝒳,
        (∀ (T : BigFppfOver B S hS) (u : Pr.groupoid.objects.obj.obj (op T)),
          u ∈ (e P).1.obj (op T) ↔
            ∃ d : TwoFibreProductOver (fibredCategory B S hS Pr.groupoid.objects.obj).val.p
                (fullSubcategoryBased 𝒳 P.property).p 𝒳.val.val.p
                (presentationProjection Pr.groupoid Pr.basedFunctor.toFunctor
                  Pr.basedFunctor.w).toFunctor
                (fullSubcategoryBasedInclusion 𝒳 P.property).toFunctor,
              d.x = ⟨T, Discrete.mk u⟩) ∧
        ∀ (𝒴 : AlgebraicStacks.{u, w} B S hS) (f : 𝒴 ⟶ 𝒳),
          ((∃ g : 𝒴.val.val ⥤ᵇ fullSubcategoryBased 𝒳 P.property,
              Nonempty (g.comp (fullSubcategoryBasedInclusion 𝒳 P.property) ≅ f.hom.hom)) ↔
            ∃ g : BasedCategory.ofFunctor (TwoFibreProductOver.structureFunctor
                  (fibredCategory B S hS Pr.groupoid.objects.obj).val.p 𝒴.val.val.p 𝒳.val.val.p
                  (presentationProjection Pr.groupoid Pr.basedFunctor.toFunctor
                    Pr.basedFunctor.w).toFunctor f.hom.hom.toFunctor) ⥤ᵇ
                BasedCategory.ofFunctor (TwoFibreProductOver.structureFunctor
                  (fibredCategory B S hS Pr.groupoid.objects.obj).val.p
                  (fullSubcategoryBased 𝒳 P.property).p 𝒳.val.val.p
                  (presentationProjection Pr.groupoid Pr.basedFunctor.toFunctor
                    Pr.basedFunctor.w).toFunctor
                  (fullSubcategoryBasedInclusion 𝒳 P.property).toFunctor),
              Nonempty (g.comp (TwoFibreProductOver.fstBased (fullSubcategoryBased 𝒳 P.property).p
                  𝒳.val.val.p (presentationProjection Pr.groupoid Pr.basedFunctor.toFunctor
                    Pr.basedFunctor.w).toFunctor
                  (fullSubcategoryBasedInclusion 𝒳 P.property).toFunctor) ≅
                TwoFibreProductOver.fstBased 𝒴.val.val.p 𝒳.val.val.p
                  (presentationProjection Pr.groupoid Pr.basedFunctor.toFunctor
                    Pr.basedFunctor.w).toFunctor f.hom.hom.toFunctor)) ∧
          ((∃ g : 𝒴.val.val ⥤ᵇ fullSubcategoryBased 𝒳 P.property,
              Nonempty (g.comp (fullSubcategoryBasedInclusion 𝒳 P.property) ≅ f.hom.hom)) ↔
            ∀ d : TwoFibreProductOver (fibredCategory B S hS Pr.groupoid.objects.obj).val.p
                𝒴.val.val.p 𝒳.val.val.p
                (presentationProjection Pr.groupoid Pr.basedFunctor.toFunctor
                  Pr.basedFunctor.w).toFunctor f.hom.hom.toFunctor,
              d.x.fiber.as ∈ (e P).1.obj (op d.x.base))
```

## Tag 06FJ, a lemma

[Tag 06FJ](https://stacks.math.columbia.edu/tag/06FJ) in the Stacks Project.

**`AlgebraicGeometry.Stack.OpenSubstack.isOpen_pointSet`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/OpenSubstackPoints.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/OpenSubstackPoints.lean#L131). The attribute's comment: “the point set of an open substack is open, so the rule is defined”.

> The rule of Stacks 06FJ is defined. The set of points of an algebraic stack lying in an
> open substack is open: it is the range of the map on points of the inclusion, which is an open
> map because the inclusion is an open immersion.

```lean
theorem isOpen_pointSet (W : OpenSubstack 𝒳) :
    @IsOpen _ (pointTopology B S hS 𝒳.val) (W.pointSet B S hS)
```

**`AlgebraicGeometry.Stack.OpenSubstack.opens`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/OpenSubstackPoints.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/OpenSubstackPoints.lean#L142). The attribute's comment: “the rule”.

> **The rule `𝒰 ↦ |𝒰|` of Stacks 06FJ**: the point set of an open substack of `𝒳`, as an open
> subset of the topological space of points of `𝒳`.

```lean
noncomputable def opens (W : OpenSubstack 𝒳) :
    letI := pointTopology B S hS 𝒳.val
    TopologicalSpace.Opens (AlgebraicStacks.points B S hS 𝒳)
```

**`AlgebraicGeometry.Stack.OpenSubstack.pointSet_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/OpenSubstackPoints.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/OpenSubstackPoints.lean#L151). The attribute's comment: “inclusion-preservation for the point set of an open substack”.

> The rule of Stacks 06FJ preserves inclusions. An open substack contained in another has a
> smaller point set.

```lean
theorem pointSet_mono {U V : OpenSubstack 𝒳} (h : U.property ≤ V.property) :
    U.pointSet B S hS ⊆ V.pointSet B S hS
```

**`AlgebraicGeometry.Stack.OpenSubstack.opens_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/OpenSubstackPoints.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/OpenSubstackPoints.lean#L161). The attribute's comment: “inclusion-preservation for the rule U goes to |U| as an open subset of the point space”.

> The rule of Stacks 06FJ preserves inclusions, for the rule `𝒰 ↦ |𝒰|` of
> `AlgebraicGeometry.Stack.OpenSubstack.opens`.

```lean
theorem opens_mono {U V : OpenSubstack 𝒳} (h : U.property ≤ V.property) :
    letI := pointTopology B S hS 𝒳.val
    opens B S hS U ≤ opens B S hS V
```

**`AlgebraicGeometry.Stack.OpenSubstack.bijective_opens_and_opens_le_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/OpenSubstackPoints.lean, line 530](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/OpenSubstackPoints.lean#L530).

> **Stacks 06FJ.** Let `𝒳` be an algebraic stack. The rule `𝒰 ↦ |𝒰|` defines an inclusion
> preserving bijection between open substacks of `𝒳` and open subsets of `|𝒳|`: the rule
> `AlgebraicGeometry.Stack.OpenSubstack.opens` is bijective, and `|𝒰| ⊆ |𝒱|` holds exactly when
> `𝒰 ⊆ 𝒱`.
>
> Injectivity, and the reflection of inclusions, is
> `AlgebraicGeometry.Stack.OpenSubstack.property_le_of_pointSet_subset`; surjectivity is
> `AlgebraicGeometry.Stack.OpenSubstack.ofIsOpen` with
> `AlgebraicGeometry.Stack.OpenSubstack.pointSet_ofIsOpen`; preservation of inclusions is
> `AlgebraicGeometry.Stack.OpenSubstack.pointSet_mono`.

```lean
theorem bijective_opens_and_opens_le_iff :
    letI := pointTopology B S hS 𝒳.val
    Function.Bijective (opens B S hS (𝒳 := 𝒳)) ∧
      ∀ U V : OpenSubstack 𝒳, opens B S hS U ≤ opens B S hS V ↔ U ≤ V
```

## Tag 05UP, a lemma

[Tag 05UP](https://stacks.math.columbia.edu/tag/05UP) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_openSubstack_isOpenImmersion_smooth_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/OpenImageSubstack.lean, line 389](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/OpenImageSubstack.lean#L389). The attribute's comment: “the algebraic stack, the open immersion into the given stack and the smooth surjection from the open subspace, all three together with the 2-commutativity of the resulting square. The stack is constructed as the open substack of Stacks 04YM whose point set is the image of the points of the open subspace, by Stacks 06FJ”.

> **Stacks 05UP.** Let `𝒳` be an algebraic stack over `S`, let `U` be an algebraic space over
> `S` with a surjective smooth 1-morphism `f : U ⟶ 𝒳`, and let `i : V ⟶ U` be an open immersion of
> presheaves on the big fppf site of `S`. Then `V` is an algebraic space over `S` and there are an
> algebraic stack `𝒴` over `S`, an open immersion `j : 𝒴 ⟶ 𝒳` and a surjective smooth 1-morphism
> `q : V ⟶ 𝒴` making the square `(i, f, q, j)` 2-commute.
>
> The algebraic stack `𝒴` is the open substack of `𝒳` whose points are the image of `|V|`, and `q`
> is the factorization of `V ⟶ 𝒳` through it, so the three pieces are produced from one
> construction rather than chosen from an existential; the 2-commutativity is an identity.

```lean
theorem exists_openSubstack_isOpenImmersion_smooth_surjective
    {U V : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hU : IsAlgebraicSpace B S hS U) {i : V ⟶ U}
    (hi : Space.IsOpenImmersion B S hS i)
    {𝒳 : AlgebraicStacks.{u, w} B S hS}
    (f : algebraicSpaceStack.{u, w} B S hS U hU ⟶ 𝒳)
    (hfsm : AlgebraicStacks.IsSmooth B S hS f)
    (_hfsurj : IsSurjective B S hS f) :
    ∃ (hV : IsAlgebraicSpace B S hS V) (𝒴 : AlgebraicStacks.{u, w} B S hS)
      (j : 𝒴 ⟶ 𝒳) (q : algebraicSpaceStack.{u, w} B S hS V hV ⟶ 𝒴),
      AlgebraicStacks.IsOpenImmersion B S hS j ∧
        AlgebraicStacks.IsSmooth B S hS q ∧
          IsSurjective B S hS q ∧
            Nonempty (algebraicSpaceStackMap.{u, w} B S hS hV hU i ≫ f ≅ q ≫ j)
```

## Tag 05UQ, a lemma

[Tag 05UQ](https://stacks.math.columbia.edu/tag/05UQ) in the Stacks Project.

**`AlgebraicGeometry.Stack.OpenSubstack.eq_of_isUnion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/OpenSubstackUnion.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/OpenSubstackUnion.lean#L130). The attribute's comment: “uniqueness of the union”.

> The union of a family of open substacks is unique: an open substack of `𝒳` which contains
> every member of the family and is covered by the family is determined by the family. This is what
> makes the notation `⋃_{i ∈ I} 𝒳ᵢ` of the source legitimate.

```lean
theorem eq_of_isUnion {𝒳 : AlgebraicStacks.{u, w} B S hS} {I : Type*} {𝒰 : I → OpenSubstack 𝒳}
    {W W' : OpenSubstack 𝒳} (h : IsUnion 𝒳 𝒰 W.property) (h' : IsUnion 𝒳 𝒰 W'.property) :
    W = W'
```

**`AlgebraicGeometry.Stack.OpenSubstack.exists_openSubstack_of_isUnion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/OpenSubstackUnion.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/OpenSubstackUnion.lean#L177). The attribute's comment: “the members of the family are open substacks of the union”.

> The members of a family of open substacks are open substacks of its union. If an open
> substack `W` of `𝒳` is the union of a family `𝒰 : I → OpenSubstack 𝒳`, then each `𝒰 i` is an
> open substack of `W`: there are open substacks `V i` of `W` whose objects are, under the
> inclusion of `W` into `𝒳`, exactly the objects of `𝒰 i`.

```lean
theorem exists_openSubstack_of_isUnion {𝒳 : AlgebraicStacks.{u, w} B S hS} {I : Type*}
    {𝒰 : I → OpenSubstack 𝒳} {W : OpenSubstack 𝒳} (h : IsUnion 𝒳 𝒰 W.property) :
    ∃ V : I → OpenSubstack (fullSubcategoryAlgebraicStack 𝒳 W.property W.isAlgebraic),
      ∀ (i : I) (x : 𝒳.val.val.obj),
        (𝒰 i).property x ↔ ∃ hx : W.property x, (V i).property ⟨x, hx⟩
```

**`AlgebraicGeometry.Stack.OpenSubstack.exists_isUnion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/OpenSubstackUnion.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/OpenSubstackUnion.lean#L293).

> **Stacks 05UQ.** Let `𝒳` be an algebraic stack and `𝒳ᵢ ⊆ 𝒳`, `i ∈ I`, a collection of open
> substacks. Then there is an open substack `⋃_{i ∈ I} 𝒳ᵢ ⊆ 𝒳` such that the `𝒳ᵢ` are open
> substacks covering it.
>
> The open substack is `AlgebraicGeometry.Stack.OpenSubstack.iUnion 𝒰`. It is the union of the
> family in the sense of `AlgebraicGeometry.Stack.OpenSubstack.IsUnion`: it contains every `𝒳ᵢ`,
> and every object of it lies, over the members of a covering sieve of the fppf topology, in some
> `𝒳ᵢ`. Its points are `⋃_{i ∈ I} |𝒳ᵢ|`, so `∐_{i ∈ I} 𝒳ᵢ ⟶ ⋃_{i ∈ I} 𝒳ᵢ` is surjective. Each `𝒳ᵢ`
> is an open substack `V i` of it. And it is the only open substack of `𝒳` that is the union of the
> family, which is what makes the notation `⋃_{i ∈ I} 𝒳ᵢ` legitimate.

```lean
theorem exists_isUnion {𝒳 : AlgebraicStacks.{u, w} B S hS} {I : Type*}
    (𝒰 : I → OpenSubstack 𝒳) :
    ∃ W : OpenSubstack 𝒳,
      (IsUnion 𝒳 𝒰 W.property ∧ W.pointSet B S hS = ⋃ i, (𝒰 i).pointSet B S hS ∧
        ∃ V : I → OpenSubstack (fullSubcategoryAlgebraicStack 𝒳 W.property W.isAlgebraic),
          ∀ (i : I) (x : 𝒳.val.val.obj),
            (𝒰 i).property x ↔ ∃ hx : W.property x, (V i).property ⟨x, hx⟩) ∧
      ∀ W' : OpenSubstack 𝒳, IsUnion 𝒳 𝒰 W'.property → W' = W
```

**`AlgebraicGeometry.Stack.OpenSubstack.isUnion_pointsWithin`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/OpenSubstackUnionPointsWithin.lean, line 379](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/OpenSubstackUnionPointsWithin.lean#L379). The attribute's comment: “the union of the family is the locus of the set of points lying in a member”.

> Let `Ω` be a set of points of `|𝒳|` consisting exactly of the classes of the field-valued
> points of `𝒳` whose object lies in a member of the family. Then the locus
> `AlgebraicGeometry.Stack.pointsWithin` of `Ω` is the union of the family: it contains every
> member, and every object of it lies, over a covering sieve, in a member.

```lean
theorem OpenSubstack.isUnion_pointsWithin {𝒳 : AlgebraicStacks.{u, w} B S hS} {I : Type*}
    (𝒰 : I → OpenSubstack 𝒳) {Ω : Set (points B S hS 𝒳.val.val 𝒳.val.property)}
    (hΩ : ∀ c, c ∈ Ω ↔ ∃ (i : I) (q : FieldValuedPoint B S hS 𝒳.val.val),
      (𝒰 i).property q.obj ∧ pointClass B S hS 𝒳.val.val 𝒳.val.property q = c) :
    OpenSubstack.IsUnion 𝒳 𝒰 (pointsWithin 𝒳 Ω)
```

## Tag 05UR, a lemma

[Tag 05UR](https://stacks.math.columbia.edu/tag/05UR) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_finset_pointSet_subset_of_isQuasiCompactStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/OpenSubstackFiniteSubcover.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/OpenSubstackFiniteSubcover.lean#L142). The attribute's comment: “the conclusion read on points: finitely many members of the family contain the point set of the quasi-compact open substack”.

> If a quasi-compact open substack `𝒳'` of an algebraic stack `𝒳` is covered by a family of
> open substacks `𝒳ᵢ`, then finitely many of the `𝒳ᵢ` already cover the point set of `𝒳'`.

```lean
theorem exists_finset_pointSet_subset_of_isQuasiCompactStack
    {𝒳 : AlgebraicStacks.{u, w} B S hS} (𝒳' : OpenSubstack 𝒳)
    (hqc : IsQuasiCompactStack.{u, w} B S hS
      (fullSubcategoryAlgebraicStack 𝒳 𝒳'.property 𝒳'.isAlgebraic).val
      (fullSubcategoryAlgebraicStack 𝒳 𝒳'.property 𝒳'.isAlgebraic).property)
    {I : Type*} (𝒰 : I → OpenSubstack 𝒳)
    (hcover : IsOpenSubstackCoverOn B S hS 𝒳 𝒳' 𝒰) :
    ∃ J : Finset I, 𝒳'.pointSet B S hS ⊆ ⋃ i ∈ J, (𝒰 i).pointSet B S hS
```

**`AlgebraicGeometry.Stack.exists_finset_le_of_isQuasiCompactStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/OpenSubstackFiniteSubcover.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/OpenSubstackFiniteSubcover.lean#L167).

> Let `𝒳` be an algebraic stack and `𝒳' ⊆ 𝒳` a quasi-compact open substack. Let `𝒳ᵢ ⊆ 𝒳`,
> `i ∈ I`, be open substacks such that `𝒳' ⊆ ⋃_{i ∈ I} 𝒳ᵢ`, the union being
> `AlgebraicGeometry.Stack.OpenSubstack.iUnion`. Then there is a finite subset `I' ⊆ I` such that
> `𝒳' ⊆ ⋃_{i ∈ I'} 𝒳ᵢ`.

```lean
theorem exists_finset_le_of_isQuasiCompactStack {𝒳 : AlgebraicStacks.{u, w} B S hS}
    (𝒳' : OpenSubstack 𝒳)
    (hqc : IsQuasiCompactStack.{u, w} B S hS
      (fullSubcategoryAlgebraicStack 𝒳 𝒳'.property 𝒳'.isAlgebraic).val
      (fullSubcategoryAlgebraicStack 𝒳 𝒳'.property 𝒳'.isAlgebraic).property)
    {I : Type*} (𝒰 : I → OpenSubstack 𝒳) (hle : 𝒳' ≤ OpenSubstack.iUnion 𝒰) :
    ∃ J : Finset I, 𝒳' ≤ OpenSubstack.iUnion (fun i : J => 𝒰 i)
```

**`AlgebraicGeometry.Stack.exists_finset_le_of_isQuasiCompactStack_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/OpenSubstackPointSetInjective.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/OpenSubstackPointSetInjective.lean#L71).

> Let `𝒳'` be a quasi-compact open substack of an algebraic stack `𝒳` and let `𝒳ᵢ`, `i ∈ I`, be
> open substacks of `𝒳` covering `𝒳'`. Then there is a finite `I' ⊆ I` such that `𝒳'` is contained
> in every open substack containing `𝒳ᵢ` for all `i ∈ I'`, that is, `𝒳' ⊆ ⋃_{i ∈ I'} 𝒳ᵢ`.

```lean
theorem exists_finset_le_of_isQuasiCompactStack_unconditional {𝒳 : AlgebraicStacks.{u, w} B S hS}
    (𝒳' : OpenSubstack 𝒳)
    (hqc : IsQuasiCompactStack.{u, w} B S hS
      (fullSubcategoryAlgebraicStack 𝒳 𝒳'.property 𝒳'.isAlgebraic).val
      (fullSubcategoryAlgebraicStack 𝒳 𝒳'.property 𝒳'.isAlgebraic).property)
    {I : Type*} (𝒰 : I → OpenSubstack 𝒳)
    (hcover : IsOpenSubstackCoverOn B S hS 𝒳 𝒳' 𝒰) :
    ∃ J : Finset I, ∀ W : OpenSubstack 𝒳,
      (∀ i ∈ J, (𝒰 i).property ≤ W.property) → 𝒳'.property ≤ W.property
```

## Tag 05WE, a lemma

[Tag 05WE](https://stacks.math.columbia.edu/tag/05WE) in the Stacks Project.

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpace_of_isOpenSubstackCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/OpenSubstackCover.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/OpenSubstackCover.lean#L227).

> **Stacks 05WE.** Let `𝒳` be an algebraic stack over `S` and let `𝒰 i`, `i ∈ I`, be open
> substacks of `𝒳` which cover `𝒳` and are each representable by an algebraic space over `S`. Then
> `𝒳` is representable by an algebraic space.
>
> The covering hypothesis makes `𝒳` a stack in setoids,
> `AlgebraicGeometry.Stack.isStackInSetoids_of_isOpenSubstackCover`, which is the first step of the
> source's proof; the second step is the implication (1) ⟹ (3) of Stacks 04SZ,
> `AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpace_of_isStackInSetoids`.

```lean
theorem isRepresentableByAlgebraicSpace_of_isOpenSubstackCover
    (𝒳 : AlgebraicStacks.{u, w} B S hS) {I : Type*} (𝒰 : I → OpenSubstack 𝒳)
    (hcover : IsOpenSubstackCover 𝒳 𝒰)
    (hspace : ∀ i, IsRepresentableByAlgebraicSpace B S hS
      (fullSubcategoryAlgebraicStack 𝒳 (𝒰 i).property (𝒰 i).isAlgebraic).val) :
    IsRepresentableByAlgebraicSpace B S hS 𝒳.val
```

## Tag 05WF, a lemma

[Tag 05WF](https://stacks.math.columbia.edu/tag/05WF) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_equivalenceOver_yoneda_of_isOpenSubstackCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/OpenSubstackCoverScheme.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/OpenSubstackCoverScheme.lean#L237).

> **Stacks 05WF.** Let `𝒳` be an algebraic stack over `S` and let `𝒰 i`, `i ∈ I`, be open
> substacks of `𝒳` which cover `𝒳` and are each a scheme, that is, equivalent over the site to the
> category of elements of the representable presheaf of an object of the site. Then `𝒳` is a scheme.
>
> The first step of the source's proof is Stacks 05WE,
> `AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpace_of_isOpenSubstackCover`: it makes `𝒳` an
> algebraic space `F`. The second step is the schematic locus of Stacks 03JH: each substack gives an
> open immersion `h_{T_i} ⟶ F` whose image is therefore contained in the locus, the covering
> hypothesis puts every section of `F` locally in one of those images, and the locus is a sheaf, so
> it is all of `F` and `F` is a scheme. See the implementation notes of this module.

```lean
theorem exists_equivalenceOver_yoneda_of_isOpenSubstackCover
    (𝒳 : AlgebraicStacks.{u, w} B S hS) {I : Type*} (𝒰 : I → OpenSubstack 𝒳)
    (hcover : IsOpenSubstackCover 𝒳 𝒰)
    (hscheme : ∀ i, ∃ T : BigFppfOver B S hS, Nonempty
      (StacksRepresentableCFG.EquivalenceOver
        (fullSubcategoryAlgebraicStack 𝒳 (𝒰 i).property (𝒰 i).isAlgebraic).val.val.p
        (presheafOfCategories (yoneda.obj T ⋙ typeToCat)).p)) :
    ∃ T : BigFppfOver B S hS, Nonempty
      (StacksRepresentableCFG.EquivalenceOver 𝒳.val.val.p
        (presheafOfCategories (yoneda.obj T ⋙ typeToCat)).p)
```

## Tag 06M3, a lemma

[Tag 06M3](https://stacks.math.columbia.edu/tag/06M3) in the Stacks Project.

**`AlgebraicGeometry.Stack.eq_of_isRelativePropertyLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativePropertyLocus.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativePropertyLocus.lean#L166). The attribute's comment: “assertion (A), uniqueness of the maximal open substack on which f has P; unconditional”.

> **Stacks 06M3, assertion (A), uniqueness of the maximal open substack.** Two open substacks
> of `𝒳` on which `f` has `P` and which are maximal with that property coincide: each is contained
> in the other, and an open substack is determined by its object property.
>
> This is what makes the definite article in *the* maximal open substack of the source legitimate,
> and it needs no input beyond those of the ambient site.

```lean
theorem eq_of_isRelativePropertyLocus (P : MorphismProperty (AlgebraicSpaces B S hS))
    [P.IsStableUnderBaseChange]
    [P.IsLocalAtTarget (Space.Topology.fppf.precoverage B S hS)]
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} {f : 𝒳 ⟶ 𝒴}
    {hf : IsRepresentableByAlgebraicSpaces B S hS f.hom.hom} {W W' : OpenSubstack 𝒳}
    (h : IsRelativePropertyLocus B S hS P f hf W)
    (h' : IsRelativePropertyLocus B S hS P f hf W') :
    W = W'
```

**`AlgebraicGeometry.Stack.exists_isRelativePropertyLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativePropertyLocus.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativePropertyLocus.lean#L212). The attribute's comment: “assertion (A), existence of the maximal open substack on which f has P, with the locality of P along a union of open substacks carried as `hLocal`; the property Q of the source is not needed”.

> **Stacks 06M3, assertion (A), the existence of the maximal open substack.** A 1-morphism
> `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` representable by algebraic spaces has an open substack
> of `𝒳` on which it restricts to a 1-morphism with the relative property `P` of **Stacks 03YK**
> and which contains every open substack with that property.
>
> It is the union `AlgebraicGeometry.Stack.OpenSubstack.iUnion` (**Stacks 05UQ**) of the set of
> all open substacks on which `f` has `P`: that `f` has `P` on it is the carried `hLocal`, and
> maximality is the first clause of `AlgebraicGeometry.Stack.OpenSubstack.IsUnion` and does not
> need it.

```lean
theorem exists_isRelativePropertyLocus (P : MorphismProperty (AlgebraicSpaces B S hS))
    [P.IsStableUnderBaseChange]
    [P.IsLocalAtTarget (Space.Topology.fppf.precoverage B S hS)]
    (hLocal : IsRelativePropertyLocalOnOpenSubstackUnions.{u, w} B S hS P)
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom.hom) :
    ∃ W : OpenSubstack 𝒳, IsRelativePropertyLocus B S hS P f hf W
```

**`AlgebraicGeometry.Stack.isRelativePropertyLocus_baseChange_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativePropertyLocus.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativePropertyLocus.lean#L337). The attribute's comment: “assertion (B), the containment 𝒵 ×_𝒴 𝒳' ⊆ W(P, f') of the base change of the maximal open substack in the maximal open substack of the base change, for an arbitrary base change and with neither the property R nor the property Q used; the reverse containment, which is where R enters, is not proved”.

> **Stacks 06M3, assertion (B), the containment `g'^{-1}𝒳' ⊆ 𝒳''`.** Let `Q` be a 2-fibre
> product square over the cospan `(g, f)`, so that `Q.fst` is the base change of
> `f : 𝒳 ⟶ 𝒴` along `g : 𝒵 ⟶ 𝒴` and `Q.snd` is the projection to `𝒳`. Let `W` be the `P`-locus
> of `f` and `W'` the `P`-locus of `Q.fst`. Then every object of the apex carried by `Q.snd` into
> `W` lies in `W'`.
>
> This is one of the two containments assertion (B) asserts, and it holds for an **arbitrary** base
> change: the property `R` of the source is not used, nor is `Q`. The inverse image of `W` along
> `Q.snd` is the 2-fibre product `(𝒵 ×_𝒴 𝒳) ×_𝒳 W`, which by pasting (**Stacks 003Q**) is also
> `W ×_𝒴 𝒵`, so its projection to `𝒵` is a base change of `f|_W` and has `P` by **Stacks 045C**;
> maximality of `W'` finishes.
>
> The reverse containment, which is where the hypotheses on `R` enter, is not proved; see the
> module documentation.

```lean
theorem isRelativePropertyLocus_baseChange_apply
    (P : MorphismProperty (AlgebraicSpaces B S hS))
    [P.IsStableUnderBaseChange]
    [P.IsLocalAtTarget (Space.Topology.fppf.precoverage B S hS)]
    {𝒳 𝒴 𝒵 : AlgebraicStacks.{u, w} B S hS} {f : 𝒳 ⟶ 𝒴} {g : 𝒵 ⟶ 𝒴}
    {hf : IsRepresentableByAlgebraicSpaces B S hS f.hom.hom}
    (Q : Bicategory.TwoCommSq g f) (hQ : Bicategory.IsTwoFibreProduct Q)
    {hfst : IsRepresentableByAlgebraicSpaces B S hS Q.fst.hom.hom}
    {W : OpenSubstack 𝒳} {W' : OpenSubstack Q.pt}
    (hW : IsRelativePropertyLocus B S hS P f hf W)
    (hW' : IsRelativePropertyLocus B S hS P Q.fst hfst W')
    {x : Q.pt.val.val.obj} (hx : W.property (Q.snd.hom.hom.toFunctor.obj x)) :
    W'.property x
```

**`AlgebraicGeometry.Stack.exists_isRelativePropertyLocus_of_hasRelativePropertyLocusOnSpaces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativePropertyLocusOnSpaces.lean, line 643](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativePropertyLocusOnSpaces.lean#L643). The attribute's comment: “assertion (A), the existence of the largest open substack of the source on which a 1-morphism representable by algebraic spaces and having Q has P, from the four hypotheses of the source on P, Q and R, by the chart construction of the source”.

> **The existence of the maximal open substack on which a relative property holds.** Let `P`,
> `Q`, `R` be properties of morphisms of algebraic spaces over `S` which are fppf local on the target
> and stable under arbitrary base change, with smoothness implying `R`, with every morphism of
> algebraic spaces having `Q` carrying a greatest open subspace of its source on which it has `P`,
> and with that greatest open subspace compatible with base change along a morphism with `R`. Then
> a 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` representable by algebraic spaces and
> having `Q` has an open substack of `𝒳` on which it restricts to a 1-morphism with the relative
> property `P` of **Stacks 03YK** and which contains every open substack with that property.

```lean
theorem exists_isRelativePropertyLocus_of_hasRelativePropertyLocusOnSpaces
    (P Q R : MorphismProperty (AlgebraicSpaces B S hS))
    [P.IsStableUnderBaseChange]
    [P.IsLocalAtTarget (Space.Topology.fppf.precoverage.{u, u} B S hS)]
    [Q.IsStableUnderBaseChange]
    [Q.IsLocalAtTarget (Space.Topology.fppf.precoverage.{u, u} B S hS)]
    [R.IsStableUnderBaseChange]
    [R.IsLocalAtTarget (Space.Topology.fppf.precoverage.{u, u} B S hS)]
    (hsmR : SmoothImplies B S hS R)
    (h3 : HasRelativePropertyLocusOnSpaces B S hS P Q)
    (h4 : RelativePropertyLocusBaseChange B S hS P Q R)
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom.hom)
    (hQf : HasRelativeProperty.{u, u, u + 1, u} B S hS Q f.hom hf) :
    ∃ W : OpenSubstack 𝒳, IsRelativePropertyLocus B S hS P f hf W
```

**`AlgebraicGeometry.Stack.isRelativePropertyLocus_baseChange_apply_symm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativePropertyLocusOnSpaces.lean, line 1080](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativePropertyLocusOnSpaces.lean#L1080). The attribute's comment: “assertion (B), the maximality half: the locus of the base change is carried into the locus of the 1-morphism, so that together with the containment proved above the base change of the locus is the locus of the base change. From the four hypotheses of the source on P, Q and R, with Q for the 1-morphism and R for the base change as the source has them, by the source's chart construction run at one more base change”.

> **The locus of a base change is carried into the locus.** Let `P`, `Q`, `R` be properties of
> morphisms of algebraic spaces over `S` satisfying the hypotheses of Stacks 06M3, let
> `f : 𝒳 ⟶ 𝒴` be a 1-morphism representable by algebraic spaces having `Q`, let `g : 𝒵 ⟶ 𝒴` be
> representable by algebraic spaces having `R` and let `D` be a 2-fibre product square over the
> cospan `(g, f)`. If `W` is the `P`-locus of `f` and `W'` the `P`-locus of the base change
> `D.fst`, then every object of the apex lying in `W'` is carried by `D.snd` into `W`: that is,
> `W(P, f') ⊆ 𝒵 ×_𝒴 W(P, f)`.

```lean
theorem isRelativePropertyLocus_baseChange_apply_symm
    (hsmR : SmoothImplies B S hS R)
    (h3 : HasRelativePropertyLocusOnSpaces B S hS P Q)
    (h4 : RelativePropertyLocusBaseChange B S hS P Q R)
    {𝒳 𝒴 𝒵 : AlgebraicStacks.{u, w} B S hS} {f : 𝒳 ⟶ 𝒴} {g : 𝒵 ⟶ 𝒴}
    {hf : IsRepresentableByAlgebraicSpaces B S hS f.hom.hom}
    {hg : IsRepresentableByAlgebraicSpaces B S hS g.hom.hom}
    (hQf : HasRelativeProperty.{u, u, u + 1, u} B S hS Q f.hom hf)
    (hRg : HasRelativeProperty.{u, u, u + 1, u} B S hS R g.hom hg)
    (D : Bicategory.TwoCommSq g f) (hD : Bicategory.IsTwoFibreProduct D)
    {hfst : IsRepresentableByAlgebraicSpaces B S hS D.fst.hom.hom}
    {W : OpenSubstack 𝒳} {W' : OpenSubstack D.pt}
    (hW : IsRelativePropertyLocus B S hS P f hf W)
    (hW' : IsRelativePropertyLocus B S hS P D.fst hfst W')
    {x : D.pt.val.val.obj} (hx : W'.property x) :
    W.property (D.snd.hom.hom.toFunctor.obj x)
```

## Tag 06M4, a remark

[Tag 06M4](https://stacks.math.columbia.edu/tag/06M4) in the Stacks Project.

**`AlgebraicGeometry.Space.le_maximalFlatOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatLocusWarning.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FlatLocusWarning.lean#L286). The attribute's comment: “hypothesis (3) of Stacks 06M3 at P = flat, Q = empty: maximality”.

> **Stacks 06M4, the instantiation: maximality in hypothesis (3) of Stacks 06M3 at
> `P = flat` and `Q = empty`.** Every open subspace of the source on which the morphism is flat
> is contained in the largest flat open: it is a member of the family that open is the supremum
> of. No hypothesis on the morphism is needed, which is what `Q = empty` means.

```lean
theorem le_maximalFlatOpen (f : X ⟶ Y) {U : Subfunctor X}
    (hU : IsOpenSubspace B S hS U) (hUf : IsFlat B S hS (U.ι ≫ f)) :
    U ≤ maximalFlatOpen B S hS f
```

**`AlgebraicGeometry.Space.isOpenSubspace_maximalFlatOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatLocusWarning.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FlatLocusWarning.lean#L331). The attribute's comment: “hypothesis (3) of Stacks 06M3 at P = flat, Q = empty: openness”.

> **Stacks 06M4, the instantiation: openness in hypothesis (3) of Stacks 06M3 at
> `P = flat` and `Q = empty`.** The largest flat open of a morphism of algebraic spaces over `S`
> is an open subspace of the source. No hypothesis on the morphism is needed.

```lean
theorem isOpenSubspace_maximalFlatOpen (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    IsOpenSubspace B S hS (maximalFlatOpen B S hS f)
```

**`AlgebraicGeometry.Space.isFlat_maximalFlatOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatLocusWarning.lean, line 340](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FlatLocusWarning.lean#L340). The attribute's comment: “hypothesis (3) of Stacks 06M3 at P = flat, Q = empty: flatness on the open”.

> **Stacks 06M4, the instantiation: flatness in hypothesis (3) of Stacks 06M3 at
> `P = flat` and `Q = empty`.** A morphism of algebraic spaces over `S` is flat on its largest
> flat open. No hypothesis on the morphism is needed.

```lean
theorem isFlat_maximalFlatOpen (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    IsFlat B S hS ((maximalFlatOpen B S hS f).ι ≫ f)
```

**`AlgebraicGeometry.Space.range_pointsMap_maximalFlatOpen_eq_interior`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatLocusWarning.lean, line 390](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FlatLocusWarning.lean#L390). The attribute's comment: “the warning: the largest flat open is the interior of the flat locus”.

> **Stacks 06M4, the warning.** The point set of the largest open subspace of the source on
> which a morphism of algebraic spaces over `S` is flat is the *interior*, in the point space of
> Stacks 03BU, of the set of points at which the morphism is flat.
>
> This is the structural statement behind the warning of Stacks 06M4: the open subspace that the
> construction of Stacks 06M3 produces at `P = flat` is characterised by a universal property —
> largest open on whose restriction the morphism is flat — and that universal property computes
> the interior of the pointwise flat locus, not the locus. Flatness at a point is the germ
> condition of Stacks 03ML part (2), which does not quantify over neighbourhoods, so no
> hypothesis on the morphism makes the interior superfluous for free.

```lean
theorem range_pointsMap_maximalFlatOpen_eq_interior (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    Set.range (pointsMap B S hS (maximalFlatOpen B S hS f).toFunctor
        (maximalFlatOpen B S hS f).ι) =
      interior {x : points B S hS X | IsFlatAt B S hS f x}
```

**`AlgebraicGeometry.Space.range_pointsMap_maximalFlatOpen_eq_setOf_isFlatAt_iff_isOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatLocusWarning.lean, line 409](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FlatLocusWarning.lean#L409). The attribute's comment: “the warning: equality with the flat locus holds exactly when it is open”.

> **Stacks 06M4, the warning.** The largest open subspace of the source on which a morphism
> of algebraic spaces over `S` is flat has the pointwise flat locus as its point set if and only
> if that locus is open.
>
> This is the warning of Stacks 06M4 in sharp form. The literal reading of the remark — that
> the two are *not* equal — is the statement that the right-hand side fails for some morphism,
> i.e. that the flat locus of some morphism of algebraic spaces is not open; such a morphism
> exists, and
> `AlgebraicGeometry.Space.exists_range_pointsMap_maximalFlatOpen_ne_setOf_isFlatAt` derives the
> literal reading from this equivalence by `Iff.not`.

```lean
theorem range_pointsMap_maximalFlatOpen_eq_setOf_isFlatAt_iff_isOpen
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    Set.range (pointsMap B S hS (maximalFlatOpen B S hS f).toFunctor
        (maximalFlatOpen B S hS f).ι) =
        {x : points B S hS X | IsFlatAt B S hS f x} ↔
      IsOpen {x : points B S hS X | IsFlatAt B S hS f x}
```

**`AlgebraicGeometry.Space.exists_range_pointsMap_maximalFlatOpen_ne_setOf_isFlatAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatLocusWarning.lean, line 474](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FlatLocusWarning.lean#L474). The attribute's comment: “the warning: for some morphism the largest flat open is not the flat locus”.

> **Stacks 06M4, the warning, in its literal form.** There is a morphism of algebraic spaces
> whose largest flat open subspace does *not* have as its point set the set of points at which
> the morphism is flat.
>
> The witness is the morphism of schemes of `AlgebraicGeometry.exists_flat_locus_not_open` —
> the inclusion of `ℤ` into the trivial square-zero extension of `ℤ` by `⨁_p ℤ/p` — read as a
> morphism of representable algebraic spaces over a big fppf site large enough to contain its
> source and target. By
> `AlgebraicGeometry.Space.range_pointsMap_maximalFlatOpen_eq_setOf_isFlatAt_iff_isOpen` it is
> enough that its pointwise flat locus is not open, and for a morphism of representable
> presheaves the flat locus of the morphism of algebraic spaces is cut out by the flat locus of
> the morphism of schemes, through
> `AlgebraicGeometry.Space.isFlatAt_yoneda_iff` and the correspondence
> `AlgebraicGeometry.Space.isOpen_yoneda_iff_isSchemeOpen` of Stacks 03BX.

```lean
theorem exists_range_pointsMap_maximalFlatOpen_ne_setOf_isFlatAt :
    ∃ (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
      (X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (_ : IsAlgebraicSpace B S hS X)
      (_ : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y),
      Set.range (pointsMap B S hS (maximalFlatOpen B S hS f).toFunctor
          (maximalFlatOpen B S hS f).ι) ≠
        {x : points B S hS X | IsFlatAt B S hS f x}
```

## Tag 06M5, a remark

[Tag 06M5](https://stacks.math.columbia.edu/tag/06M5) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isGreatest_isLocallyQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocalSourceLemmaFurtherInstances.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocalSourceLemmaFurtherInstances.lean#L205). The attribute's comment: “entry (2), locally quasi-finite: hypothesis (3) of 06M3”.

> **Stacks 06M5, entry (2), hypothesis (3) of Stacks 06M3.** For `𝒬 = ` locally of finite
> type and `𝒫 = ` locally quasi-finite: every morphism `f : X ⟶ Y` of algebraic spaces over `S`
> which is locally of finite type has a largest open subspace of `X` on which it is locally
> quasi-finite.
>
> It is `AlgebraicGeometry.Space.locallyQuasiFinitePart`, the open subspace of **Stacks 04NW**,
> which is the case `d = 0` of the first entry by **Stacks 04NV**.

```lean
theorem exists_isGreatest_isLocallyQuasiFinite
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f) :
    ∃ W : {W : Subfunctor X // IsOpenSubspace B S hS W},
      IsGreatest {V : {V : Subfunctor X // IsOpenSubspace B S hS V} |
        IsLocallyQuasiFinite B S hS (V.1.ι ≫ f)} W
```

**`AlgebraicGeometry.Space.eq_preimage_of_isGreatest_isLocallyQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocalSourceLemmaFurtherInstances.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocalSourceLemmaFurtherInstances.lean#L225). The attribute's comment: “entry (2), locally quasi-finite: hypothesis (4) of 06M3”.

> **Stacks 06M5, entry (2), hypothesis (4) of Stacks 06M3.** In a cartesian square of
> algebraic spaces over `S` whose right vertical arrow `f` is locally of finite type, any largest
> open subspace of the source of the base change `f'` on which `f'` is locally quasi-finite is the
> inverse image of any largest open subspace of `X` on which `f` is locally quasi-finite.
>
> The source writes `ℛ = ∅` for this entry, and no condition is imposed on the base change. Both
> greatest elements are the canonical open subspaces of **Stacks 04NW**, whose formation commutes
> with arbitrary base change,
> `AlgebraicGeometry.Space.locallyQuasiFinitePart_preimage_of_isPullback`.

```lean
theorem eq_preimage_of_isGreatest_isLocallyQuasiFinite
    {X' X Y' Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {g' : X' ⟶ X} {f' : X' ⟶ Y'} {f : X ⟶ Y} {g : Y' ⟶ Y} (sq : IsPullback g' f' f g)
    (hX' : IsAlgebraicSpace B S hS X') (hX : IsAlgebraicSpace B S hS X)
    (hY' : IsAlgebraicSpace B S hS Y') (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsLocallyOfFiniteType B S hS f)
    (W : {W : Subfunctor X // IsOpenSubspace B S hS W})
    (hW : IsGreatest {V : {V : Subfunctor X // IsOpenSubspace B S hS V} |
      IsLocallyQuasiFinite B S hS (V.1.ι ≫ f)} W)
    (W' : {W' : Subfunctor X' // IsOpenSubspace B S hS W'})
    (hW' : IsGreatest {V : {V : Subfunctor X' // IsOpenSubspace B S hS V} |
      IsLocallyQuasiFinite B S hS (V.1.ι ≫ f')} W') :
    W'.1 = W.1.preimage g'
```

**`AlgebraicGeometry.Space.exists_isGreatest_isUnramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocalSourceLemmaFurtherInstances.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocalSourceLemmaFurtherInstances.lean#L298). The attribute's comment: “entry (3), unramified: hypothesis (3) of 06M3”.

> **Stacks 06M5, entry (3), hypothesis (3) of Stacks 06M3.** For `𝒫 = ` unramified: every
> morphism `f : X ⟶ Y` of algebraic spaces over `S` has a largest open subspace of `X` on which it
> is unramified, and its point set is the set of points at which `f` is unramified.
>
> This is **Stacks 05W2**, part (1): the set of points at which `f` is unramified is open, the
> corresponding open subspace (**Stacks 03BZ**) is `AlgebraicGeometry.Space.unramifiedLocus`, and
> an open subspace on which `f` is unramified is one at all of whose points `f` is unramified. The
> entry's `𝒬`, locally of finite type, is not needed for this hypothesis; it is needed for (4).

```lean
theorem exists_isGreatest_isUnramified
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    ∃ W : {W : Subfunctor X // IsOpenSubspace B S hS W},
      IsGreatest {V : {V : Subfunctor X // IsOpenSubspace B S hS V} |
        IsUnramified B S hS (V.1.ι ≫ f)} W ∧
      Set.range (pointsMap B S hS W.1.toFunctor W.1.ι) =
        {x : points B S hS X | IsUnramifiedAt B S hS f x}
```

**`AlgebraicGeometry.Space.eq_preimage_of_isGreatest_isUnramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocalSourceLemmaFurtherInstances.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocalSourceLemmaFurtherInstances.lean#L319). The attribute's comment: “entry (3), unramified: hypothesis (4) of 06M3”.

> **Stacks 06M5, entry (3), hypothesis (4) of Stacks 06M3.** In a cartesian square of
> algebraic spaces over `S` whose right vertical arrow `f` is locally of finite type, any largest
> open subspace of the source of the base change `f'` on which `f'` is unramified is the inverse
> image of any largest open subspace of `X` on which `f` is unramified.
>
> The source writes `ℛ = ∅` for this entry, and no condition is imposed on the base change. By
> hypothesis (3) both open subspaces are the loci of points at which the morphisms are
> unramified, and those correspond under base change by **Stacks 05W2**, part (2),
> `AlgebraicGeometry.Space.isUnramifiedAt_iff_of_isPullback`.

```lean
theorem eq_preimage_of_isGreatest_isUnramified
    {X' X Y' Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {g' : X' ⟶ X} {f' : X' ⟶ Y'} {f : X ⟶ Y} {g : Y' ⟶ Y} (sq : IsPullback g' f' f g)
    (hX' : IsAlgebraicSpace B S hS X') (hX : IsAlgebraicSpace B S hS X)
    (hY' : IsAlgebraicSpace B S hS Y') (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsLocallyOfFiniteType B S hS f)
    (W : {W : Subfunctor X // IsOpenSubspace B S hS W})
    (hW : IsGreatest {V : {V : Subfunctor X // IsOpenSubspace B S hS V} |
      IsUnramified B S hS (V.1.ι ≫ f)} W)
    (W' : {W' : Subfunctor X' // IsOpenSubspace B S hS W'})
    (hW' : IsGreatest {V : {V : Subfunctor X' // IsOpenSubspace B S hS V} |
      IsUnramified B S hS (V.1.ι ≫ f')} W') :
    W'.1 = W.1.preimage g'
```

**`AlgebraicGeometry.Space.exists_isGreatest_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocalSourceLemmaFurtherInstances.lean, line 371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocalSourceLemmaFurtherInstances.lean#L371). The attribute's comment: “entry (4), flat: hypothesis (3) of 06M3”.

> **Stacks 06M5, entry (4), hypothesis (3) of Stacks 06M3.** For `𝒬 = ` locally of finite
> presentation and `𝒫 = ` flat: every morphism `f : X ⟶ Y` of algebraic spaces over `S` which is
> locally of finite presentation has a largest open subspace of `X` on which it is flat, and its
> point set is exactly the set of points at which `f` is flat.
>
> The set of points at which `f` is flat is open by **Stacks 05WV** for the structure sheaf,
> `AlgebraicGeometry.Space.isOpen_setOf_isFlatAt`, and an open subspace on which `f` is flat is one
> at all of whose points `f` is flat. The second clause is the source's remark that, because `f`
> has `𝒬`, `W(𝒫, f)` is the set of points at which `f` is flat; without `𝒬` it is only the interior
> of that set, which is the warning of **Stacks 06M4**.

```lean
theorem exists_isGreatest_isFlat
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf : IsLocallyOfFinitePresentation B S hS f) :
    ∃ W : {W : Subfunctor X // IsOpenSubspace B S hS W},
      IsGreatest {V : {V : Subfunctor X // IsOpenSubspace B S hS V} |
        IsFlat B S hS (V.1.ι ≫ f)} W ∧
      Set.range (pointsMap B S hS W.1.toFunctor W.1.ι) =
        {x : points B S hS X | IsFlatAt B S hS f x}
```

**`AlgebraicGeometry.Space.eq_preimage_of_isGreatest_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocalSourceLemmaFurtherInstances.lean, line 395](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocalSourceLemmaFurtherInstances.lean#L395). The attribute's comment: “entry (4), flat: hypothesis (4) of 06M3”.

> **Stacks 06M5, entry (4), hypothesis (4) of Stacks 06M3.** In a cartesian square of
> algebraic spaces over `S` whose right vertical arrow `f` is locally of finite presentation and
> whose bottom arrow `g` is flat, any largest open subspace of the source of the base change `f'`
> on which `f'` is flat is the inverse image of any largest open subspace of `X` on which `f` is
> flat.
>
> The entry's `ℛ` is flat and locally of finite presentation; only flatness of `g` is used. By
> hypothesis (3) both open subspaces are the loci of points at which the morphisms are flat, the
> base change being locally of finite presentation as well, and those correspond under a flat
> base change, which is **Stacks 05WW** for the structure sheaf,
> `AlgebraicGeometry.Space.isFlatAt_iff_of_isPullback_of_isFlat`.

```lean
theorem eq_preimage_of_isGreatest_isFlat
    {X' X Y' Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {g' : X' ⟶ X} {f' : X' ⟶ Y'} {f : X ⟶ Y} {g : Y' ⟶ Y} (sq : IsPullback g' f' f g)
    (hX' : IsAlgebraicSpace B S hS X') (hX : IsAlgebraicSpace B S hS X)
    (hY' : IsAlgebraicSpace B S hS Y') (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsLocallyOfFinitePresentation B S hS f) (hg : IsFlat B S hS g)
    (W : {W : Subfunctor X // IsOpenSubspace B S hS W})
    (hW : IsGreatest {V : {V : Subfunctor X // IsOpenSubspace B S hS V} |
      IsFlat B S hS (V.1.ι ≫ f)} W)
    (W' : {W' : Subfunctor X' // IsOpenSubspace B S hS W'})
    (hW' : IsGreatest {V : {V : Subfunctor X' // IsOpenSubspace B S hS V} |
      IsFlat B S hS (V.1.ι ≫ f')} W') :
    W'.1 = W.1.preimage g'
```

**`AlgebraicGeometry.Space.exists_isGreatest_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocalSourceLemmaFurtherInstances.lean, line 459](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocalSourceLemmaFurtherInstances.lean#L459). The attribute's comment: “entry (5), étale: hypothesis (3) of 06M3”.

> **Stacks 06M5, entry (5), hypothesis (3) of Stacks 06M3.** For `𝒬 = ` locally of finite
> presentation and `𝒫 = ` étale: every morphism `f : X ⟶ Y` of algebraic spaces over `S` which is
> locally of finite presentation has a largest open subspace of `X` on which it is étale, and its
> point set is the set of points at which `f` is both unramified and flat.
>
> This combines entries (3) and (4): the two sets of points are open, and on an open subspace `f`
> is étale exactly when it is unramified and flat there, because an unramified morphism which is
> flat and locally of finite presentation is étale (**Stacks 06LU**).

```lean
theorem exists_isGreatest_isEtale
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf : IsLocallyOfFinitePresentation B S hS f) :
    ∃ W : {W : Subfunctor X // IsOpenSubspace B S hS W},
      IsGreatest {V : {V : Subfunctor X // IsOpenSubspace B S hS V} |
        IsEtale B S hS (V.1.ι ≫ f)} W ∧
      Set.range (pointsMap B S hS W.1.toFunctor W.1.ι) =
        {x : points B S hS X | IsUnramifiedAt B S hS f x ∧ IsFlatAt B S hS f x}
```

**`AlgebraicGeometry.Space.eq_preimage_of_isGreatest_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocalSourceLemmaFurtherInstances.lean, line 483](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocalSourceLemmaFurtherInstances.lean#L483). The attribute's comment: “entry (5), étale: hypothesis (4) of 06M3”.

> **Stacks 06M5, entry (5), hypothesis (4) of Stacks 06M3.** In a cartesian square of
> algebraic spaces over `S` whose right vertical arrow `f` is locally of finite presentation and
> whose bottom arrow `g` is flat, any largest open subspace of the source of the base change `f'`
> on which `f'` is étale is the inverse image of any largest open subspace of `X` on which `f` is
> étale.
>
> The entry's `ℛ` is flat and locally of finite presentation; only flatness of `g` is used. By
> hypothesis (3) both open subspaces are the loci of points at which the morphisms are unramified
> and flat, and both conditions correspond under the base change: unramifiedness under any base
> change (**Stacks 05W2**, part (2)) and flatness under a flat one (**Stacks 05WW** for the
> structure sheaf).

```lean
theorem eq_preimage_of_isGreatest_isEtale
    {X' X Y' Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {g' : X' ⟶ X} {f' : X' ⟶ Y'} {f : X ⟶ Y} {g : Y' ⟶ Y} (sq : IsPullback g' f' f g)
    (hX' : IsAlgebraicSpace B S hS X') (hX : IsAlgebraicSpace B S hS X)
    (hY' : IsAlgebraicSpace B S hS Y') (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsLocallyOfFinitePresentation B S hS f) (hg : IsFlat B S hS g)
    (W : {W : Subfunctor X // IsOpenSubspace B S hS W})
    (hW : IsGreatest {V : {V : Subfunctor X // IsOpenSubspace B S hS V} |
      IsEtale B S hS (V.1.ι ≫ f)} W)
    (W' : {W' : Subfunctor X' // IsOpenSubspace B S hS W'})
    (hW' : IsGreatest {V : {V : Subfunctor X' // IsOpenSubspace B S hS V} |
      IsEtale B S hS (V.1.ι ≫ f')} W') :
    W'.1 = W.1.preimage g'
```

**`AlgebraicGeometry.Space.exists_isGreatest_hasRelativeDimensionLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocalSourceLemmaInstances.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocalSourceLemmaInstances.lean#L266). The attribute's comment: “entry (1), hypothesis (3) of Stacks 06M3 at 𝒬 = locally of finite type and 𝒫 = relative dimension ≤ d: the existence of a largest open subspace of the source on which the morphism has relative dimension ≤ d, from Stacks 06LR and Stacks 04NT”.

> **Stacks 06M5, first entry, hypothesis (3) of Stacks 06M3.** For `𝒬 = ` locally of finite
> type and `𝒫 = ` relative dimension `≤ d` (**Stacks 06LR**): every morphism `f : X ⟶ Y` of
> algebraic spaces over `S` which is locally of finite type has a largest open subspace of `X` on
> which it has relative dimension `≤ d`.
>
> The open subspace is `AlgebraicGeometry.Space.boundedRelativeDimensionPart`, built from the
> openness statement **Stacks 04NT** through the correspondence of **Stacks 03BZ**; the two
> clauses of being greatest are
> `AlgebraicGeometry.Space.hasRelativeDimensionLE_boundedRelativeDimensionPart` and
> `AlgebraicGeometry.Space.le_boundedRelativeDimensionPart`.

```lean
theorem exists_isGreatest_hasRelativeDimensionLE (d : ℕ)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f) :
    ∃ W : {W : Subfunctor X // IsOpenSubspace B S hS W},
      IsGreatest {V : {V : Subfunctor X // IsOpenSubspace B S hS V} |
        HasRelativeDimensionLE d B S hS (V.1.ι ≫ f)} W
```

**`AlgebraicGeometry.Space.boundedRelativeDimensionPart_preimage_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocalSourceLemmaInstances.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocalSourceLemmaInstances.lean#L289). The attribute's comment: “entry (1), hypothesis (4) of Stacks 06M3 at 𝒬 = locally of finite type and 𝒫 = relative dimension ≤ d, for the canonical open subspace: the formation of the largest open subspace commutes with base change, for an arbitrary base change since the entry's ℛ is ∅, from Stacks 04NS”.

> **Stacks 06M5, first entry, hypothesis (4) of Stacks 06M3, for the canonical open
> subspace.** In a cartesian square of algebraic spaces over `S` whose right vertical arrow `f`
> is locally of finite type, the base change `f'` is locally of finite type and its open subspace
> of relative dimension `≤ d` is the inverse image of that of `f`.
>
> No condition is imposed on the base change: the source writes `ℛ = ∅` for this entry, and
> **Stacks 04NS** gives the invariance of the relative dimension at a point under an arbitrary
> base change. On points both sides are the locus of relative dimension at most `d`, by
> `AlgebraicGeometry.Space.range_pointsMap_boundedRelativeDimensionPart` and the identification of
> the point set of an inverse image; the two open subspaces then agree because **Stacks 03BZ** is
> injective.

```lean
theorem boundedRelativeDimensionPart_preimage_of_isPullback (d : ℕ)
    {X' X Y' Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {g' : X' ⟶ X} {f' : X' ⟶ Y'} {f : X ⟶ Y} {g : Y' ⟶ Y} (sq : IsPullback g' f' f g)
    (hX' : IsAlgebraicSpace B S hS X') (hX : IsAlgebraicSpace B S hS X)
    (hY' : IsAlgebraicSpace B S hS Y') (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsLocallyOfFiniteType B S hS f) :
    ∃ hf' : IsLocallyOfFiniteType B S hS f',
      (boundedRelativeDimensionPart B S hS d hX' hY' f' hf').1 =
        (boundedRelativeDimensionPart B S hS d hX hY f hf).1.preimage g'
```

**`AlgebraicGeometry.Space.eq_preimage_of_isGreatest_hasRelativeDimensionLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocalSourceLemmaInstances.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocalSourceLemmaInstances.lean#L336). The attribute's comment: “entry (1), hypothesis (4) of Stacks 06M3 at 𝒬 = locally of finite type and 𝒫 = relative dimension ≤ d, quantified over largest open subspaces as the lemma takes it, for an arbitrary base change since the entry's ℛ is ∅”.

> **Stacks 06M5, first entry, hypothesis (4) of Stacks 06M3, in the form the lemma consumes.**
> In a cartesian square of algebraic spaces over `S` whose right vertical arrow `f` is locally of
> finite type, any largest open subspace of the source of the base change on which the base
> change has relative dimension `≤ d` is the inverse image of any largest open subspace of `X` on
> which `f` has relative dimension `≤ d`.
>
> **Stacks 06M3** takes hypothesis (4) in this shape, quantified over largest open subspaces
> rather than over a chosen one. A greatest element of an ordered type is unique, so both are the
> canonical `AlgebraicGeometry.Space.boundedRelativeDimensionPart` and the statement reduces to
> `AlgebraicGeometry.Space.boundedRelativeDimensionPart_preimage_of_isPullback`.

```lean
theorem eq_preimage_of_isGreatest_hasRelativeDimensionLE (d : ℕ)
    {X' X Y' Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {g' : X' ⟶ X} {f' : X' ⟶ Y'} {f : X ⟶ Y} {g : Y' ⟶ Y} (sq : IsPullback g' f' f g)
    (hX' : IsAlgebraicSpace B S hS X') (hX : IsAlgebraicSpace B S hS X)
    (hY' : IsAlgebraicSpace B S hS Y') (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsLocallyOfFiniteType B S hS f)
    (W : {W : Subfunctor X // IsOpenSubspace B S hS W})
    (hW : IsGreatest {V : {V : Subfunctor X // IsOpenSubspace B S hS V} |
      HasRelativeDimensionLE d B S hS (V.1.ι ≫ f)} W)
    (W' : {W' : Subfunctor X' // IsOpenSubspace B S hS W'})
    (hW' : IsGreatest {V : {V : Subfunctor X' // IsOpenSubspace B S hS V} |
      HasRelativeDimensionLE d B S hS (V.1.ι ≫ f')} W') :
    W'.1 = W.1.preimage g'
```

**`AlgebraicGeometry.Space.unramifiedLocus_preimage_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocalSourceLemmaUnramified.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocalSourceLemmaUnramified.lean#L180). The attribute's comment: “entry (3), hypothesis (4) of Stacks 06M3 at 𝒬 = locally of finite type and 𝒫 = unramified, for the canonical open subspace: the formation of the largest open subspace commutes with base change, for an arbitrary base change since the entry's ℛ is ∅, from Stacks 05W2”. References: EGA IV (17.7.2), “more general”.

> **Stacks 06M5, third entry, hypothesis (4) of Stacks 06M3, for the canonical open
> subspace.** In a cartesian square of algebraic spaces over `S` whose right vertical arrow `f`
> is locally of finite type, the open unramified locus of the base change `f'` is the inverse
> image of the open unramified locus of `f`.
>
> No condition is imposed on the base change: the source writes `ℛ = ∅` for this entry, and
> part (2) of **Stacks 05W2**,
> `AlgebraicGeometry.Space.setOf_isUnramifiedAt_eq_preimage_of_isPullback`, gives the invariance
> of the set of points of unramifiedness under an arbitrary base change. On points both sides are
> that set, by `AlgebraicGeometry.Space.range_pointsMap_unramifiedLocus` and the identification
> `AlgebraicGeometry.Space.pointsRange_preimage` of the point set of an inverse image; the two
> open subspaces then agree because part (1) of **Stacks 03BZ** is injective.

```lean
theorem unramifiedLocus_preimage_of_isPullback
    {X' X Y' Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {g' : X' ⟶ X} {f' : X' ⟶ Y'} {f : X ⟶ Y} {g : Y' ⟶ Y} (sq : IsPullback g' f' f g)
    (hX' : IsAlgebraicSpace B S hS X') (hX : IsAlgebraicSpace B S hS X)
    (hY' : IsAlgebraicSpace B S hS Y') (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsLocallyOfFiniteType B S hS f) :
    (unramifiedLocus B S hS hX' f').1 = (unramifiedLocus B S hS hX f).1.preimage g'
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 100.9, Tag 04YK](https://stacks.math.columbia.edu/tag/04YK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
