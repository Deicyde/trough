---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.SmallEtale, AlgebraicGeometry.Space.SmallEtale.IsCovering, AlgebraicGeometry.Space.essentiallySmall_spacesEtale, AlgebraicGeometry.Space.SpacesEtale, AlgebraicGeometry.Space.SpacesEtale.IsCovering, AlgebraicGeometry.Space.SpacesEtale.isSite, AlgebraicGeometry.Space.comparisonFunctor, AlgebraicGeometry.Space.comparisonFunctor_obj
statement: formalized
proof: formalized
---

# 66.18 The étale site of an algebraic space

Section 66.18 of the Stacks Project, [Tag 03EB](https://stacks.math.columbia.edu/tag/03EB). 15 tags here are carried by 81 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03ED, a definition

[Tag 03ED](https://stacks.math.columbia.edu/tag/03ED) in the Stacks Project.

**`AlgebraicGeometry.Space.SmallEtale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleSite.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleSite.lean#L119). The attribute's comment: “objects and morphisms”. References: SGA 4½ Arcata (2.1.4), “étale X-schemes”.

> **Stacks 03ED, parts (1) and (2).** The *small étale site* of a presheaf `F` on the big
> fppf site of `S`, as a category: its objects are the étale charts of `F`, and its morphisms
> are the morphisms of the big fppf site of `S` whose triangle over `F` commutes.

```lean
abbrev SmallEtale
```

**`AlgebraicGeometry.Space.SmallEtale.IsCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleSite.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleSite.lean#L139). The attribute's comment: “coverings”. References: SGA 4½ Arcata (2.1.4), “étale topology”.

> **Stacks 03ED, part (3).** A family of étale charts of `F` is a covering family exactly
> when its family of underlying objects of `Sch_κ` is a chosen étale covering family of the
> big étale site carried by `B`.

```lean
abbrev IsCovering (E : Covering (SmallEtale B S hS F)) : Prop
```

## Tag 03G0, a definition

[Tag 03G0](https://stacks.math.columbia.edu/tag/03G0) in the Stacks Project.

**`AlgebraicGeometry.Space.essentiallySmall_spacesEtale`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleEssentiallySmall.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleEssentiallySmall.lean#L243). The attribute's comment: “the set-theoretic condition: the site is essentially small”.

> **Stacks 03G0.** The spaces-étale site of an algebraic space is essentially small at the
> universe of the schemes, even though its objects live in `Type (u + 1)`.
>
> It is the full subcategory of the slice of the algebraic spaces over `X` cut out by étaleness of
> the structure morphism, and that slice is essentially small because the algebraic spaces over `S`
> are.

```lean
instance essentiallySmall_spacesEtale (X : AlgebraicSpaces B S hS) :
    EssentiallySmall.{u} (SpacesEtale B S hS X)
```

**`AlgebraicGeometry.Space.SpacesEtale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleSite.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleSite.lean#L81). The attribute's comment: “objects and morphisms”.

> **Stacks 03G0.** The spaces-étale site of `X`: the category of algebraic spaces étale over
> `X`, with the commutative triangles over `X` as morphisms.

```lean
abbrev SpacesEtale
```

**`AlgebraicGeometry.Space.SpacesEtale.IsCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleSite.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleSite.lean#L118). The attribute's comment: “coverings”.

> **Stacks 03G0.** A family in the spaces-étale site of `X` covers when every point of its
> target lifts to a point of some member of the family.

```lean
abbrev IsCovering (E : Covering (SpacesEtale B S hS X)) : Prop
```

**`AlgebraicGeometry.Space.SpacesEtale.isSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleSite.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleSite.lean#L145). The attribute's comment: “site axioms”.

> **Stacks 03G0.** Joint surjectivity on points of families in the spaces-étale site of `X`
> satisfies the site axioms.

```lean
theorem isSite : IsSite (IsCovering B S hS X)
```

## Tag 03G1, a lemma

[Tag 03G1](https://stacks.math.columbia.edu/tag/03G1) in the Stacks Project.

**`AlgebraicGeometry.Space.comparisonFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleComparison.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleComparison.lean#L154). The attribute's comment: “the functor”.

> **Stacks 03G1.** The canonical inclusion of the small étale site of `X` into its
> spaces-étale site: an étale scheme chart of `X` is an algebraic space étale over `X`.

```lean
def comparisonFunctor : SmallEtale B S hS X.1 ⥤ SpacesEtale B S hS X
```

**`AlgebraicGeometry.Space.comparisonFunctor_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleComparison.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleComparison.lean#L162). The attribute's comment: “canonical action on objects”.

> **Stacks 03G1.** The comparison sends a scheme chart to its Yoneda algebraic space over
> `X`.

```lean
theorem comparisonFunctor_obj (U : SmallEtale B S hS X.1) :
    ((comparisonFunctor B S hS X).obj U).1 = chartOver B S hS X U
```

**`AlgebraicGeometry.Space.comparisonFunctor_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleComparison.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleComparison.lean#L167). The attribute's comment: “canonical action on arrows”.

> **Stacks 03G1.** The comparison sends a chart morphism to its Yoneda morphism.

```lean
theorem comparisonFunctor_map {U V : SmallEtale B S hS X.1} (f : U ⟶ V) :
    HEq ((comparisonFunctor B S hS X).map f).hom.left.hom
      (yoneda.map ((SmallEtale.toOver B S hS X.1).map f))
```

**`AlgebraicGeometry.Space.comparisonFunctor_specialCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleComparison.lean, line 634](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleComparison.lean#L634). The attribute's comment: “special cocontinuity”.

> **Stacks 03G1.** The comparison functor is special cocontinuous in the sense of Stacks
> 03CG.

```lean
theorem comparisonFunctor_specialCocontinuous :
    IsSpecialCocontinuous (SmallEtale.topology B S hS X.1) (SpacesEtale.topology B S hS X)
      (comparisonFunctor B S hS X)
```

**`AlgebraicGeometry.Space.comparisonFunctor_sheafEquivalence`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleComparison.lean, line 654](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleComparison.lean#L654). The attribute's comment: “equivalence of topoi”.

> **Stacks 03G1.** Restriction along the comparison functor is an equivalence of sheaf
> categories, for sheaves valued in any category with the limits needed to define the
> restriction.

```lean
instance comparisonFunctor_sheafEquivalence (A : Type w) [Category.{w'} A]
    [∀ Y, HasLimitsOfShape (StructuredArrow Y (comparisonFunctor B S hS X).op) A] :
    ((comparisonFunctor B S hS X).sheafPushforwardContinuous A
      (SmallEtale.topology B S hS X.1)
      (SpacesEtale.topology B S hS X)).IsEquivalence
```

## Tag 03H7, a remark

[Tag 03H7](https://stacks.math.columbia.edu/tag/03H7) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_etaleChart_singleton_covering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleSheafConditionOneElement.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleSheafConditionOneElement.lean#L96). The attribute's comment: “the one-element covering by a scheme”.

> Let `U` be an algebraic space étale over `X`. There is an étale scheme chart `V` of `X`
> and a morphism `V → U` of the spaces-étale site which is étale and surjective, and the
> one-element family `{V → U}` is a covering family of the spaces-étale site of `X`.

```lean
theorem exists_etaleChart_singleton_covering (U : SpacesEtale B S hS X) :
    ∃ (V : SmallEtale B S hS X.1) (f : (comparisonFunctor B S hS X).obj V ⟶ U),
      IsEtale B S hS ((SpacesEtale.toSpaces B S hS X).map f).hom ∧
      IsSurjective B S hS ((SpacesEtale.toSpaces B S hS X).map f).hom ∧
      SpacesEtale.IsCovering B S hS X ⟨U, PreZeroHypercover.singleton.{u + 1} f⟩
```

**`AlgebraicGeometry.Space.exists_etaleChart_isPullback_self`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleSheafConditionOneElement.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleSheafConditionOneElement.lean#L148). The attribute's comment: “the fibre product is a scheme”.

> Let `U` be an algebraic space étale over `X`, let `V` be an étale scheme chart of `X` and
> let `f : V → U` be a morphism of the spaces-étale site. Then there is an étale scheme chart `W`
> of `X` and a pair of morphisms `p, q : W → V` of the *small* étale site whose images under the
> comparison functor exhibit `W` as the fibre product `V ×_U V` in the spaces-étale site.

```lean
theorem exists_etaleChart_isPullback_self (U : SpacesEtale B S hS X)
    (V : SmallEtale B S hS X.1) (f : (comparisonFunctor B S hS X).obj V ⟶ U) :
    ∃ (W : SmallEtale B S hS X.1) (p q : W ⟶ V),
      IsPullback ((comparisonFunctor B S hS X).map p)
        ((comparisonFunctor B S hS X).map q) f f
```

**`AlgebraicGeometry.Space.exists_isLimit_fork_of_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleSheafConditionOneElement.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleSheafConditionOneElement.lean#L227). The attribute's comment: “the equalizer diagram”.

> Let `X` be an algebraic space over `S`, let `P` be a sheaf on the spaces-étale site of
> `X`, and write `F = (comparisonFunctor).op ⋙ P` for its restriction to the small étale site of
> `X`. Then for every algebraic space `U` étale over `X` there are an étale scheme chart `V` of
> `X`, a surjective étale morphism `f : V → U` of the spaces-étale site whose one-element family
> is a covering, and a second étale scheme chart `W` with morphisms `p, q : W → V` of the small
> étale site exhibiting `W` as `V ×_U V`, such that
>
> `P(U) → F(V) ⇉ F(W)`
>
> is an equalizer diagram, the two parallel arrows being restriction along `p` and along `q`.

```lean
theorem exists_isLimit_fork_of_isSheaf (P : (SpacesEtale B S hS X)ᵒᵖ ⥤ A)
    (hP : Presheaf.IsSheaf (SpacesEtale.topology B S hS X) P) (U : SpacesEtale B S hS X) :
    ∃ (V : SmallEtale B S hS X.1) (f : (comparisonFunctor B S hS X).obj V ⟶ U)
      (W : SmallEtale B S hS X.1) (p q : W ⟶ V)
      (_ : IsPullback ((comparisonFunctor B S hS X).map p)
        ((comparisonFunctor B S hS X).map q) f f)
      (w : P.map f.op ≫ ((comparisonFunctor B S hS X).op ⋙ P).map p.op =
        P.map f.op ≫
          ((comparisonFunctor B S hS X).op ⋙ P).map q.op),
      IsEtale B S hS ((SpacesEtale.toSpaces B S hS X).map f).hom ∧
      IsSurjective B S hS ((SpacesEtale.toSpaces B S hS X).map f).hom ∧
      SpacesEtale.IsCovering B S hS X ⟨U, PreZeroHypercover.singleton.{u + 1} f⟩ ∧
      Nonempty (IsLimit (Fork.ofι (P.map f.op) w))
```

**`AlgebraicGeometry.Space.exists_scheme_chart_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleComparison.lean, line 521](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleComparison.lean#L521). The attribute's comment: “a scheme chart covering the étale space”.

> **Stacks 03H7.** Every algebraic space étale over `X` is covered, in the spaces-étale site
> of `X`, by a single étale *scheme* chart of `X`, namely a chosen atlas of it composed with its
> structure morphism.

```lean
theorem exists_scheme_chart_cover (U : SpacesEtale B S hS X) :
    ∃ (V : SmallEtale B S hS X.1) (f : (comparisonFunctor B S hS X).obj V ⟶ U),
      Sieve.generate (Presieve.singleton f) ∈ SpacesEtale.topology B S hS X U
```

**`AlgebraicGeometry.Space.exists_smallEtaleDirectImageChartEqualizerEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleDirectImageChartEqualizer.lean, line 341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleDirectImageChartEqualizer.lean#L341). The attribute's comment: “the equalizer diagram, for the direct image on the small etale sites: the sections of f_{small,*}P over an etale scheme chart V of Y are the equalizer of the sections of P over an etale scheme chart W covering X x_Y V and over a chart W' presenting the self-fibre product of W over X x_Y V”.

> **Tag 03H7 for the direct image on the small étale sites.**  Let `f : X ⟶ Y` be a morphism
> of algebraic spaces, let `P` be a sheaf of sets on the small étale site of `X`, and let `V` be
> an étale scheme chart of `Y`.  Then there are étale scheme charts `W`, `W'` of `X` and two
> morphisms `a, b : W' ⟶ W` such that
>
> `(f_{small,*}P)(V) ⟶ P(W) ⇉ P(W')`
>
> is an equalizer: the sections of the direct image over `V` are in bijection with the sections of
> `P` over `W` on which restriction along `a` and restriction along `b` agree.

```lean
theorem exists_smallEtaleDirectImageChartEqualizerEquiv (f : X ⟶ Y)
    (P : Sheaf (SmallEtale.topology B S hS X.1) (Type u)) (V : SmallEtale B S hS Y.1) :
    ∃ (W W' : SmallEtale B S hS X.1) (a b : W' ⟶ W),
      Nonempty (((smallEtaleDirectImage B S hS f).obj P).obj.obj (op V) ≃
        {y : P.obj.obj (op W) // P.obj.map a.op y = P.obj.map b.op y})
```

**`AlgebraicGeometry.Space.exists_scheme_chart_self_intersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleSchemeChart.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleSchemeChart.lean#L61). The attribute's comment: “the scheme self-intersection”.

> The self-intersection of a scheme chart over an object of the spaces-étale site of `X` is
> again an étale scheme chart of `X`, with its canonical pullback projections.

```lean
theorem exists_scheme_chart_self_intersection {U : SpacesEtale B S hS X}
    {V : SmallEtale B S hS X.1} (f : (comparisonFunctor B S hS X).obj V ⟶ U) :
    ∃ (W : SmallEtale B S hS X.1)
      (p q : (comparisonFunctor B S hS X).obj W ⟶ (comparisonFunctor B S hS X).obj V),
      IsPullback p q f f
```

**`AlgebraicGeometry.Space.sections_equalizer_of_scheme_chart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleSchemeChart.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleSchemeChart.lean#L129). The attribute's comment: “the equalizer diagram”.

> The sections of a sheaf on the spaces-étale site of `X` over an object `U` are the equalizer
> of the two restriction maps from a scheme chart covering `U` to the scheme self-intersection of
> that chart.

```lean
theorem sections_equalizer_of_scheme_chart {U : SpacesEtale B S hS X}
    {V W : SmallEtale B S hS X.1} (f : (comparisonFunctor B S hS X).obj V ⟶ U)
    (p q : (comparisonFunctor B S hS X).obj W ⟶ (comparisonFunctor B S hS X).obj V)
    (hcover : Sieve.generate (Presieve.singleton f) ∈ SpacesEtale.topology B S hS X U)
    (hpullback : IsPullback p q f f)
    (G : Sheaf (SpacesEtale.topology B S hS X) (Type w)) :
    Nonempty (IsLimit (Fork.ofι (G.obj.map f.op) (f := G.obj.map p.op) (g := G.obj.map q.op)
      (by simp [← Functor.map_comp, ← op_comp, hpullback.w])))
```

## Tag 0H01, a definition

[Tag 0H01](https://stacks.math.columbia.edu/tag/0H01) in the Stacks Project.

**`AlgebraicGeometry.Space.AffineEtale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleSite.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleSite.lean#L57). The attribute's comment: “objects and morphisms”.

> The *affine étale site* of a presheaf `F` on the big fppf site of `S`, as a category: its
> objects are the étale charts of `F` with affine source, and its morphisms are the morphisms of
> schemes whose triangle over `F` commutes.

```lean
abbrev AffineEtale
```

**`AlgebraicGeometry.Space.AffineEtale.IsCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleSite.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleSite.lean#L85). The attribute's comment: “coverings”.

> A family of affine étale charts of `F` is a covering family exactly when it is a covering
> family of the small étale site and its index type is finite.

```lean
abbrev IsCovering (E : Covering (AffineEtale B S hS F)) : Prop
```

## Tag 04JS, a lemma

[Tag 04JS](https://stacks.math.columbia.edu/tag/04JS) in the Stacks Project.

**`AlgebraicGeometry.Space.AffineEtale.inclusion_isSpecialCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleDenseSubsite.lean, line 476](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleDenseSubsite.lean#L476).

> The inclusion of the affine étale charts of an algebraic space into all its étale charts is
> a special cocontinuous functor; in particular it is a dense subsite inclusion, and so induces an
> equivalence between the affine étale topos and the small étale topos.

```lean
theorem AffineEtale.inclusion_isSpecialCocontinuous
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (_hF : IsAlgebraicSpace B S hS F) :
    IsSpecialCocontinuous
      (AffineEtale.topology B S hS F)
      (SmallEtale.topology B S hS F)
      (AffineEtale.inclusion B S hS F)
```

## Tag 04JT, a definition

[Tag 04JT](https://stacks.math.columbia.edu/tag/04JT) in the Stacks Project.

**`AlgebraicGeometry.Space.smallEtaleTopos`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleTopos.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleTopos.lean#L48).

> **Stacks 04JT.** The category of sheaves of sets on the small étale site of a presheaf
> `F` on the big fppf site of `S`; for an algebraic space, its small étale topos.

```lean
abbrev smallEtaleTopos (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
```

## Tag 03G2, a lemma

[Tag 03G2](https://stacks.math.columbia.edu/tag/03G2) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_affine_chartDiagram_ofArrows`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineChartDiagramCofinal.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineChartDiagramCofinal.lean#L174). The attribute's comment: “affine chart diagrams are cofinal: covering family”.

> **Stacks 03G2: the affine chart diagrams over `f` are cofinal.**  Every étale scheme chart
> `U` of `X` carries a covering family of affine étale charts of `X`, each of which is the chart of
> `X` of a commuting square of étale scheme charts over `f` whose chart of `Y` is affine.

```lean
theorem exists_affine_chartDiagram_ofArrows (f : X ⟶ Y) (U : SmallEtale B S hS X.1) :
    ∃ (I : Type u) (W : I → SmallEtale B S hS X.1) (a : ∀ i, W i ⟶ U)
      (d : I → ChartDiagram B S hS X.1 Y.1 f.hom),
      (∀ i, (d i).U = W i) ∧
      (∀ i, IsAffine ((SmallEtale.toOver B S hS X.1 ⋙
        BigFppfOver.toScheme B S hS).obj (W i))) ∧
      (∀ i, IsAffine ((SmallEtale.toOver B S hS Y.1 ⋙
        BigFppfOver.toScheme B S hS).obj (d i).V)) ∧
      Sieve.ofArrows W a ∈ SmallEtale.topology B S hS X.1 U
```

**`AlgebraicGeometry.Space.generate_affineChartDiagram_mem_topology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineChartDiagramCofinal.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineChartDiagramCofinal.lean#L257). The attribute's comment: “affine chart diagrams are cofinal: covering sieve”.

> **Stacks 03G2: the affine chart diagrams over `f` are cofinal, in sieve form.**  The affine
> étale charts of `X` which are the chart of `X` of a commuting square of étale scheme charts over
> `f` whose chart of `Y` is affine and satisfies a condition `Q` holding on all affine charts
> generate a covering sieve of every étale chart of `X`.

```lean
theorem generate_affineChartDiagram_mem_topology (f : X ⟶ Y)
    (Q : SmallEtale B S hS Y.1 → Prop)
    (hQ : ∀ V : SmallEtale B S hS Y.1,
      IsAffine ((SmallEtale.toOver B S hS Y.1 ⋙ BigFppfOver.toScheme B S hS).obj V) → Q V)
    (U : SmallEtale B S hS X.1) :
    Sieve.generate (fun (Z : SmallEtale B S hS X.1) (_ : Z ⟶ U) =>
      IsAffine ((SmallEtale.toOver B S hS X.1 ⋙ BigFppfOver.toScheme B S hS).obj Z) ∧
      ∃ d : ChartDiagram B S hS X.1 Y.1 f.hom, ∃ _ : d.U = Z,
        IsAffine ((SmallEtale.toOver B S hS Y.1 ⋙ BigFppfOver.toScheme B S hS).obj d.V) ∧
          Q d.V) ∈ SmallEtale.topology B S hS X.1 U
```

**`AlgebraicGeometry.Space.smallToposMorphism_comp_abelianInverseImage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianInverseImageSquare.lean, line 258](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianInverseImageSquare.lean#L258). The attribute's comment: “part (3), inverse-image composition at abelian coefficients”.

> **Stacks 03G2, part (3), inverse-image composition, at abelian coefficients:**
> `(f ≫ g)⁻¹ ≅ g⁻¹ ⋙ f⁻¹` for the inverse image of *abelian* sheaves along the morphisms of small
> étale topoi.
>
> It is `AlgebraicGeometry.Space.smallToposMorphism_comp_inverseImage`, the same statement for
> sheaves of sets, carried over by `StacksTag03LR.abelianInverseImageCompIso`.

```lean
def smallToposMorphism_comp_abelianInverseImage (f : X ⟶ Y) (g : Y ⟶ Z) :
    Sites.abelianInverseImage (smallToposMorphism B S hS (f ≫ g)) ≅
      Sites.abelianInverseImage (smallToposMorphism B S hS g) ⋙
        Sites.abelianInverseImage (smallToposMorphism B S hS f)
```

**`AlgebraicGeometry.Space.smallBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleBaseChange.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleBaseChange.lean#L162). The attribute's comment: “part (4), base change on scheme charts”.

> For a morphism `f` whose underlying morphism of presheaves is representable, base change along
> `f` of étale scheme charts of `Y`, as a functor to étale scheme charts of `X`.

```lean
noncomputable def smallBaseChange {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hf : yoneda.relativelyRepresentable f.hom) :
    SmallEtale B S hS Y.1 ⥤ SmallEtale B S hS X.1
```

**`AlgebraicGeometry.Space.smallBaseChange_projection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleBaseChange.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleBaseChange.lean#L187). The attribute's comment: “part (4), projection of pulled-back scheme charts”.

> The cartesian projection from a pulled-back scheme chart to the original chart, viewed as a
> morphism of algebraic spaces.

```lean
noncomputable def smallBaseChange_projection {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hf : yoneda.relativelyRepresentable f.hom) :
    (smallBaseChange B S hS f hf ⋙ comparisonFunctor B S hS X) ⋙
        SpacesEtale.toSpaces B S hS X ⟶
      comparisonFunctor B S hS Y ⋙ SpacesEtale.toSpaces B S hS Y
```

**`AlgebraicGeometry.Space.smallBaseChange_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleBaseChange.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleBaseChange.lean#L204). The attribute's comment: “part (4), cartesian scheme-chart base change”.

> The base change of an étale scheme chart is cartesian after passage to algebraic spaces.

```lean
theorem smallBaseChange_isPullback {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hf : yoneda.relativelyRepresentable f.hom) (V : SmallEtale B S hS Y.1) :
    IsPullback ((smallBaseChange_projection B S hS f hf).app V)
      ((smallBaseChange B S hS f hf ⋙ comparisonFunctor B S hS X).obj V).1.hom
      ((comparisonFunctor B S hS Y).obj V).1.hom f
```

**`AlgebraicGeometry.Space.smallBaseChange_comparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleBaseChange.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleBaseChange.lean#L242). The attribute's comment: “part (4), comparison square”.

> The square formed by small and spaces-étale base change and the comparison functors commutes
> up to its canonical natural isomorphism.

```lean
noncomputable def smallBaseChange_comparison {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hf : yoneda.relativelyRepresentable f.hom) :
    smallBaseChange B S hS f hf ⋙ comparisonFunctor B S hS X ≅
      comparisonFunctor B S hS Y ⋙ (spacesBaseChange B S hS f).functor
```

**`AlgebraicGeometry.Space.smallBaseChange_comparison_projection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleBaseChange.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleBaseChange.lean#L284). The attribute's comment: “part (4), comparison of cartesian projections”.

> The comparison isomorphism `AlgebraicGeometry.Space.smallBaseChange_comparison` is compatible
> with the cartesian projections to the original chart.

```lean
theorem smallBaseChange_comparison_projection {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hf : yoneda.relativelyRepresentable f.hom) (V : SmallEtale B S hS Y.1) :
    ((smallBaseChange_comparison B S hS f hf).hom.app V).hom.left ≫
        (spacesBaseChange B S hS f).projection.app ((comparisonFunctor B S hS Y).obj V) =
      (smallBaseChange_projection B S hS f hf).app V
```

**`AlgebraicGeometry.Space.smallBaseChange_isMorphismOfSites`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleBaseChange.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleBaseChange.lean#L344). The attribute's comment: “part (4), small-site morphism”.

> Base change of étale scheme charts is a morphism of small étale sites.

```lean
theorem smallBaseChange_isMorphismOfSites {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hf : yoneda.relativelyRepresentable f.hom) :
    _root_.IsMorphismOfSites.{u + 1} (smallBaseChange B S hS f hf)
      (SmallEtale.topology B S hS Y.1) (SmallEtale.topology B S hS X.1)
```

**`AlgebraicGeometry.Space.smallBaseChange_topos`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleBaseChange.lean, line 364](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleBaseChange.lean#L364). The attribute's comment: “part (4), induced morphism of topoi”.

> The direct image of `AlgebraicGeometry.Space.smallToposMorphism` is isomorphic to the direct
> image along the morphism of small étale sites given by base change on scheme charts.

```lean
noncomputable def smallBaseChange_topos {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hf : yoneda.relativelyRepresentable f.hom) :
    letI := (smallBaseChange_isMorphismOfSites B S hS f hf).toIsContinuous
    (smallToposMorphism B S hS f).pushforward ≅
      (smallBaseChange B S hS f hf).sheafPushforwardContinuous (Type (u + 1))
        (SmallEtale.topology B S hS Y.1) (SmallEtale.topology B S hS X.1)
```

**`AlgebraicGeometry.Space.smallBaseChange_topos_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleBaseChange.lean, line 381](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleBaseChange.lean#L381). The attribute's comment: “part (4), canonical topos comparison coherence”.

> The isomorphism `AlgebraicGeometry.Space.smallBaseChange_topos`, composed with the comparison
> `AlgebraicGeometry.Space.smallBaseChange_pushforward_comparison`, is
> `AlgebraicGeometry.Space.smallToposMorphism_comparison`.

```lean
theorem smallBaseChange_topos_comparison {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hf : yoneda.relativelyRepresentable f.hom)
    (F : Sheaf (SpacesEtale.topology B S hS X) (Type (u + 1))) :
    letI := (smallBaseChange_isMorphismOfSites B S hS f hf).toIsContinuous
    (smallBaseChange_topos B S hS f hf).hom.app
        (((comparisonFunctor B S hS X).sheafPushforwardContinuous (Type (u + 1))
          (SmallEtale.topology B S hS X.1) (SpacesEtale.topology B S hS X)).obj F) ≫
      (smallBaseChange_pushforward_comparison B S hS f hf).hom.app F =
      (smallToposMorphism_comparison B S hS f).hom.app F
```

**`AlgebraicGeometry.Space.smallToposMorphism_comp_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleBaseChange.lean, line 400](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleBaseChange.lean#L400). The attribute's comment: “part (3), canonical composition coherence”.

> The small-site composition isomorphism
> `AlgebraicGeometry.Space.smallToposMorphism_comp` is precisely the transport of the cartesian
> composition on the spaces-étale site through the comparison equivalences, on every sheaf.

```lean
theorem smallToposMorphism_comp_comparison {X Y Z : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (g : Y ⟶ Z) (F : Sheaf (SpacesEtale.topology B S hS X) (Type (u + 1))) :
    (smallToposMorphism B S hS g).pushforward.map
        ((smallToposMorphism_comparison B S hS f).hom.app F) ≫
      (smallToposMorphism_comparison B S hS g).hom.app
        (((spacesBaseChange B S hS f).functor.sheafPushforwardContinuous (Type (u + 1))
          (SpacesEtale.topology B S hS Y) (SpacesEtale.topology B S hS X)).obj F) ≫
      ((comparisonFunctor B S hS Z).sheafPushforwardContinuous (Type (u + 1))
        (SmallEtale.topology B S hS Z.1) (SpacesEtale.topology B S hS Z)).map
          ((spacesBaseChange_pushforward_comp B S hS f g).hom.app F) =
    (smallToposMorphism_comp B S hS f g).hom.app
        (((comparisonFunctor B S hS X).sheafPushforwardContinuous (Type (u + 1))
          (SmallEtale.topology B S hS X.1) (SpacesEtale.topology B S hS X)).obj F) ≫
      (smallToposMorphism_comparison B S hS (f ≫ g)).hom.app F
```

**`AlgebraicGeometry.Space.smallToposMorphism_comp_mate`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleBaseChange.lean, line 426](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleBaseChange.lean#L426). The attribute's comment: “part (3), composition mate coherence”.

> The inverse-image composition isomorphism
> `AlgebraicGeometry.Space.smallToposMorphism_comp_inverseImage` is the adjoint mate of the
> direct-image composition isomorphism `AlgebraicGeometry.Space.smallToposMorphism_comp`.

```lean
theorem smallToposMorphism_comp_mate {X Y Z : AlgebraicSpaces B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (F : Sheaf (SmallEtale.topology B S hS Z.1) (Type (u + 1)))
    (G : Sheaf (SmallEtale.topology B S hS X.1) (Type (u + 1)))
    (h : ((MorphismOfTopoi.comp (smallToposMorphism B S hS g)
      (smallToposMorphism B S hS f)).inverseImage).obj F ⟶ G) :
    (smallToposMorphism B S hS (f ≫ g)).adj.homEquiv F G
        ((smallToposMorphism_comp_inverseImage B S hS f g).hom.app F ≫ h) =
      (MorphismOfTopoi.comp (smallToposMorphism B S hS g)
          (smallToposMorphism B S hS f)).adj.homEquiv F G h ≫
        (smallToposMorphism_comp B S hS f g).hom.app G
```

**`AlgebraicGeometry.Space.spacesBaseChange_comp_inv_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePushforwardAssoc.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePushforwardAssoc.lean#L195). The attribute's comment: “part (2), associativity of the composition isomorphism”.

> **Stacks 03G2, part (2), associativity.**  The base-change composition isomorphisms of the
> spaces-étale sites obey the associativity cocycle law.  This is the cocycle law for
> `CategoryTheory.Over.pullbackComp`, restricted to the objects étale over the base.

```lean
theorem spacesBaseChange_comp_inv_assoc (f : V ⟶ W) (g : W ⟶ X) (h : X ⟶ Y)
    (U : SpacesEtale B S hS Y) :
    (spacesBaseChange_comp B S hS (f ≫ g) h).inv.app U ≫
        (spacesBaseChange_comp B S hS f g).inv.app
          ((spacesBaseChange B S hS h).functor.obj U) =
      (spacesBaseChange_comp B S hS f (g ≫ h)).inv.app U ≫
        (spacesBaseChange B S hS f).functor.map
          ((spacesBaseChange_comp B S hS g h).inv.app U)
```

**`AlgebraicGeometry.Space.smallToposMorphismTypeU_comp_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePushforwardAssoc.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePushforwardAssoc.lean#L235). The attribute's comment: “part (3), associativity of the composition isomorphism”.

> **Stacks 03G2, part (3), associativity.**  The composition isomorphisms of the direct images
> of the small étale topoi obey the associativity cocycle law.

```lean
theorem smallToposMorphismTypeU_comp_assoc (f : V ⟶ W) (g : W ⟶ X) (h : X ⟶ Y)
    (M : Sheaf (SmallEtale.topology B S hS V.1) (Type u)) :
    (smallToposMorphismTypeU B S hS h).pushforward.map
          ((smallToposMorphismTypeU_comp B S hS f g).hom.app M) ≫
        (smallToposMorphismTypeU_comp B S hS (f ≫ g) h).hom.app M =
      (smallToposMorphismTypeU_comp B S hS g h).hom.app
          ((smallToposMorphismTypeU B S hS f).pushforward.obj M) ≫
        (smallToposMorphismTypeU_comp B S hS f (g ≫ h)).hom.app M
```

**`AlgebraicGeometry.Space.smallToposMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleToposMorphism.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleToposMorphism.lean#L107). The attribute's comment: “part (3), morphism of small étale topoi”.

> The morphism of small étale topoi induced by a morphism `f : X ⟶ Y` of algebraic spaces: the
> morphism of spaces-étale topoi of the base-change morphism of sites, transported along the
> comparison equivalences `AlgebraicGeometry.Space.smallEtaleToposEquiv`.

```lean
noncomputable def smallToposMorphism {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) :
    MorphismOfTopoi
      (Sheaf (SmallEtale.topology B S hS X.1) (Type (u + 1)))
      (Sheaf (SmallEtale.topology B S hS Y.1) (Type (u + 1)))
```

**`AlgebraicGeometry.Space.smallToposMorphism_comparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleToposMorphism.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleToposMorphism.lean#L117). The attribute's comment: “part (3), comparison with the spaces-étale topoi”.

> The small étale direct image agrees, through the comparison equivalences, with the direct
> image of the spaces-étale morphism of sites.

```lean
noncomputable def smallToposMorphism_comparison {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) :
    ((comparisonFunctor B S hS X).sheafPushforwardContinuous (Type (u + 1))
          (SmallEtale.topology B S hS X.1) (SpacesEtale.topology B S hS X)) ⋙
        (smallToposMorphism B S hS f).pushforward ≅
      ((spacesBaseChange B S hS f).functor.sheafPushforwardContinuous (Type (u + 1))
          (SpacesEtale.topology B S hS Y) (SpacesEtale.topology B S hS X)) ⋙
        (comparisonFunctor B S hS Y).sheafPushforwardContinuous (Type (u + 1))
          (SmallEtale.topology B S hS Y.1) (SpacesEtale.topology B S hS Y)
```

**`AlgebraicGeometry.Space.smallToposMorphism_comp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleToposMorphism.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleToposMorphism.lean#L145). The attribute's comment: “part (3), compatibility with composition”.

> The small étale direct image is compatible with composition: the composite of the morphisms
> of topoi of `f` and `g` has the same direct image as the morphism of topoi of `f ≫ g`.

```lean
noncomputable def smallToposMorphism_comp {X Y Z : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (g : Y ⟶ Z) :
    (MorphismOfTopoi.comp (smallToposMorphism B S hS g)
        (smallToposMorphism B S hS f)).pushforward ≅
      (smallToposMorphism B S hS (f ≫ g)).pushforward
```

**`AlgebraicGeometry.Space.smallToposMorphism_comp_inverseImage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleToposMorphism.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleToposMorphism.lean#L160). The attribute's comment: “part (3), inverse-image composition”.

> The inverse-image composition isomorphism, oriented for pullback of sheaves:
> `(f ≫ g)⁻¹ ≅ g⁻¹ ⋙ f⁻¹`. It is the adjoint mate of
> `AlgebraicGeometry.Space.smallToposMorphism_comp`.

```lean
noncomputable def smallToposMorphism_comp_inverseImage {X Y Z : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (g : Y ⟶ Z) :
    (smallToposMorphism B S hS (f ≫ g)).inverseImage ≅
      (smallToposMorphism B S hS g).inverseImage ⋙
        (smallToposMorphism B S hS f).inverseImage
```

**`AlgebraicGeometry.Space.spacesBaseChange_comp_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpacesBaseChangeAssoc.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SpacesBaseChangeAssoc.lean#L328). The attribute's comment: “part (2), associativity of the composition isomorphism”.

> **Stacks 03G2, part (2).** The composition isomorphism of spaces-étale base change is
> associative: for `f : X ⟶ Y`, `g : Y ⟶ Z` and `h : Z ⟶ W` the two ways of identifying the
> threefold iterated base change with base change along `f ≫ g ≫ h` — first contracting `g` and
> `h`, or first contracting `f` and `g` — agree.
>
> This is the coherence that makes `AlgebraicGeometry.Space.spacesBaseChange_comp` a genuine
> compatibility of base change with composition, and it is the spaces-étale analogue of
> `CategoryTheory.GrothendieckTopology.overMapPullback_assoc`.

```lean
theorem spacesBaseChange_comp_assoc {W X Y Z : AlgebraicSpaces B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (h : Z ⟶ W) :
    Functor.isoWhiskerRight (spacesBaseChange_comp B S hS g h)
          (spacesBaseChange B S hS f).functor ≪≫ spacesBaseChange_comp B S hS f (g ≫ h) =
      Functor.associator _ _ _ ≪≫
        Functor.isoWhiskerLeft (spacesBaseChange B S hS h).functor
          (spacesBaseChange_comp B S hS f g) ≪≫
        spacesBaseChange_comp B S hS (f ≫ g) h ≪≫
        eqToIso (congrArg (fun k => (spacesBaseChange B S hS k).functor)
          (Category.assoc f g h))
```

**`AlgebraicGeometry.Space.smallToposMorphism_comp_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpacesBaseChangeAssoc.lean, line 427](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SpacesBaseChangeAssoc.lean#L427). The attribute's comment: “part (3), associativity of the composition isomorphism”.

> **Stacks 03G2, part (3).** The direct-image composition isomorphism of the morphisms of small
> étale topoi is associative: for `f : X ⟶ Y`, `g : Y ⟶ Z` and `h : Z ⟶ W` the two ways of
> identifying the threefold composite of direct images with the direct image of `f ≫ g ≫ h` agree.
>
> This is the coherence that makes the construction of
> `AlgebraicGeometry.Space.smallToposMorphism` "compatible with compositions" in the sense of part
> (3) of the tag, rather than merely equipped with composition isomorphisms.  It is
> `AlgebraicGeometry.Space.spacesBaseChange_pushforward_comp_assoc'` transported along the comparison
> equivalences of Stacks 03G1 by
> `MorphismOfTopoi.transport_comp_pushforward_comp_assoc`.

```lean
theorem smallToposMorphism_comp_assoc {W X Y Z : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (g : Y ⟶ Z) (h : Z ⟶ W) :
    Functor.isoWhiskerRight (smallToposMorphism_comp B S hS f g)
          (smallToposMorphism B S hS h).pushforward ≪≫
        smallToposMorphism_comp B S hS (f ≫ g) h ≪≫
        eqToIso (congrArg (fun k => (smallToposMorphism B S hS k).pushforward)
          (Category.assoc f g h)) =
      Functor.associator _ _ _ ≪≫
        Functor.isoWhiskerLeft (smallToposMorphism B S hS f).pushforward
          (smallToposMorphism_comp B S hS g h) ≪≫
        smallToposMorphism_comp B S hS f (g ≫ h)
```

**`AlgebraicGeometry.Space.spacesBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleBaseChange.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleBaseChange.lean#L152). The attribute's comment: “part (1), the cartesian base-change functor”.

> **Stacks 03G2, part (1).** The canonical base-change datum on the spaces-étale sites: the
> base change `CategoryTheory.Over.pullback f` of the slice over `Y`, restricted to the objects
> étale over the base, with the first projection of the fibre product.

```lean
noncomputable def spacesBaseChange {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) :
    SpacesBaseChange B S hS f
```

**`AlgebraicGeometry.Space.spacesBaseChange_isMorphismOfSites`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleBaseChange.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleBaseChange.lean#L218). The attribute's comment: “part (1), morphism of sites”.

> **Stacks 03G2, part (1).** Base change defines a morphism of sites in the direction
> `X → Y`: it is continuous, the spaces-étale site of `Y` has a terminal object and fibre
> products, and base change preserves both.

```lean
theorem spacesBaseChange_isMorphismOfSites {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) :
    (spacesBaseChange B S hS f).functor.IsMorphismOfSites
      (SpacesEtale.topology B S hS Y) (SpacesEtale.topology B S hS X)
```

**`AlgebraicGeometry.Space.spacesBaseChange_comp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleBaseChange.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleBaseChange.lean#L230). The attribute's comment: “part (2), canonical composition isomorphism”.

> **Stacks 03G2, part (2).** Base change along a composite is canonically isomorphic to the
> iterated base change, by `CategoryTheory.Over.pullbackComp` restricted to the objects étale
> over the base.

```lean
noncomputable def spacesBaseChange_comp {X Y Z : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (g : Y ⟶ Z) :
    (spacesBaseChange B S hS g).functor ⋙ (spacesBaseChange B S hS f).functor ≅
      (spacesBaseChange B S hS (f ≫ g)).functor
```

**`AlgebraicGeometry.Space.spacesBaseChange_comp_projection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleBaseChange.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleBaseChange.lean#L245). The attribute's comment: “part (2), compatibility with cartesian projections”.

> **Stacks 03G2, part (2).** The composition isomorphism is compatible with the cartesian
> projections to the original object, which pins it down.

```lean
theorem spacesBaseChange_comp_projection {X Y Z : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (g : Y ⟶ Z) (V : SpacesEtale B S hS Z) :
    ((spacesBaseChange_comp B S hS f g).hom.app V).hom.left ≫
        (spacesBaseChange B S hS (f ≫ g)).projection.app V =
      (spacesBaseChange B S hS f).projection.app
          ((spacesBaseChange B S hS g).functor.obj V) ≫
        (spacesBaseChange B S hS g).projection.app V
```

## Tag 03G3, a definition

[Tag 03G3](https://stacks.math.columbia.edu/tag/03G3) in the Stacks Project.

**`AlgebraicGeometry.Space.FMap`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRingedToposHom.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRingedToposHom.lean#L229).

> A map of sections along a morphism of algebraic spaces, natural under simultaneous étale
> restriction of the source and target charts.

```lean
structure FMap (P : (SmallEtale B S hS F)ᵒᵖ ⥤ Type v)
    (Q : (SmallEtale B S hS G)ᵒᵖ ⥤ Type w)
```

## Tag 03G4, a lemma

[Tag 03G4](https://stacks.math.columbia.edu/tag/03G4) in the Stacks Project.

**`AlgebraicGeometry.Space.chartCorrespondence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ChartCorrespondence.lean, line 689](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ChartCorrespondence.lean#L689). The attribute's comment: “f-maps are exactly maps into the direct image”.

> The *chart correspondence* of a morphism `f : X ⟶ Y` of algebraic spaces: a bijection
> between the `f`-maps from a sheaf of sets `Q` on the small étale site of `Y` to a sheaf of sets
> `P` on the small étale site of `X`, and the homomorphisms from `Q` into the direct image of `P`
> along `AlgebraicGeometry.Space.smallEtaleRingedToposHom`, satisfying the sectionwise
> characterization `AlgebraicGeometry.Space.IsChartCorrespondence`.

```lean
noncomputable def chartCorrespondence (f : X ⟶ Y)
    (P : Sheaf (SmallEtale.topology B S hS X.1) (Type u))
    (Q : Sheaf (SmallEtale.topology B S hS Y.1) (Type u)) :
    { e : FMap B S hS X.1 Y.1 f.hom P.obj Q.obj ≃
        (Q ⟶ (smallEtaleRingedToposHom B S hS f).toToposHom.pushforward.obj P) //
      IsChartCorrespondence B S hS f P Q e }
```

**`AlgebraicGeometry.Space.fmapInverseImageEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ChartCorrespondence.lean, line 701](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ChartCorrespondence.lean#L701). The attribute's comment: “f-maps are exactly maps out of the inverse image”.

> `f`-maps from `Q` to `P` are exactly homomorphisms from the inverse image of `Q` into `P`,
> the inverse image being that of `AlgebraicGeometry.Space.smallEtaleRingedToposHom`.

```lean
noncomputable def fmapInverseImageEquiv (f : X ⟶ Y)
    (P : Sheaf (SmallEtale.topology B S hS X.1) (Type u))
    (Q : Sheaf (SmallEtale.topology B S hS Y.1) (Type u)) :
    FMap B S hS X.1 Y.1 f.hom P.obj Q.obj ≃
      ((smallEtaleRingedToposHom B S hS f).toToposHom.inverseImage.obj Q ⟶ P)
```

**`AlgebraicGeometry.Space.fMapEquivPushforwardHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartCorrespondence.lean, line 709](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartCorrespondence.lean#L709). The attribute's comment: “parts (1) and (3)”.

> A map on sections over every commutative pair of étale scheme charts over `f` is
> equivalently a map of sheaves into the small étale direct image.

```lean
noncomputable def fMapEquivPushforwardHom :
    FMap B S hS X.1 Y.1 f.hom F.obj G.obj ≃
      (G ⟶ (smallToposMorphism B S hS f).pushforward.obj F)
```

**`AlgebraicGeometry.Space.fMapEquivInverseImageHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartCorrespondence.lean, line 788](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartCorrespondence.lean#L788). The attribute's comment: “parts (2) and (3)”.

> A map on sections over every commutative pair of étale scheme charts over `f` is
> equivalently a map of sheaves out of the small étale inverse image. The bijection is the
> composite of `AlgebraicGeometry.Space.fMapEquivPushforwardHom` with the adjunction bijection of
> the morphism of small étale topoi.

```lean
noncomputable def fMapEquivInverseImageHom :
    FMap B S hS X.1 Y.1 f.hom F.obj G.obj ≃
      ((smallToposMorphism B S hS f).inverseImage.obj G ⟶ F)
```

**`AlgebraicGeometry.Space.fMapEquivPushforwardHom_chart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartCorrespondence.lean, line 803](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartCorrespondence.lean#L803). The attribute's comment: “canonical action on chart sections”.

> The bijection `AlgebraicGeometry.Space.fMapEquivPushforwardHom` is the canonical one.
> Transport a sheaf `F` on the small étale site of `X` through an isomorphism with the restriction
> of a spaces-étale sheaf `H`; then on a diagram `d` of étale scheme charts over `f` the transported
> `f`-map is restriction of the section of the direct image along any arrow from the chart of `X`
> into the cartesian base change of the chart of `Y` whose composite with the cartesian projection
> is the Yoneda morphism of the vertical morphism of `d`.

```lean
theorem fMapEquivPushforwardHom_chart
    (H : Sheaf (SpacesEtale.topology B S hS X) (Type (u + 1)))
    (F : Sheaf (SmallEtale.topology B S hS X.1) (Type (u + 1)))
    (i : F ≅ (comparisonRestriction B S hS X).obj H)
    (G : Sheaf (SmallEtale.topology B S hS Y.1) (Type (u + 1)))
    (ξ : FMap B S hS X.1 Y.1 f.hom F.obj G.obj)
    (d : ChartDiagram B S hS X.1 Y.1 f.hom)
    (h : (comparisonFunctor B S hS X).obj d.U ⟶ chartBaseChange B S hS f d.V)
    (hh : ((SpacesEtale.toSpaces B S hS X).map h ≫
        (spacesBaseChange B S hS f).projection.app
          ((comparisonFunctor B S hS Y).obj d.V)).hom = yoneda.map d.g)
    (s : G.obj.obj (op d.V)) :
    let ψ : G ⟶ (spacesDirectImageRestriction B S hS f).obj H :=
      fMapEquivPushforwardHom B S hS f F G ξ ≫
        (smallToposMorphism B S hS f).pushforward.map i.hom ≫
        (smallToposMorphism_comparison B S hS f).hom.app H
    (((sheafToPresheaf (SmallEtale.topology B S hS X.1)
      (Type (u + 1))).map i.hom).app (op d.U)) (ξ.app d s) =
      H.obj.map h.op
        (((sheafToPresheaf (SmallEtale.topology B S hS Y.1)
          (Type (u + 1))).map ψ).app (op d.V) s)
```

## Tag 03LP, a lemma

[Tag 03LP](https://stacks.math.columbia.edu/tag/03LP) in the Stacks Project.

**`AlgebraicGeometry.Space.abelianEtaleRestriction`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianExtensionByZero.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianExtensionByZero.lean#L61). The attribute's comment: “restriction of abelian sheaves”.

> **Restriction of abelian étale sheaves** along an étale morphism `f : X ⟶ Y` of algebraic
> spaces: restriction along postcomposition with `f`.

```lean
abbrev abelianEtaleRestriction (f : X ⟶ Y) (hf : IsEtale B S hS f.hom) :
    Sheaf (SmallEtale.topology B S hS Y.1) AddCommGrpCat.{u} ⥤
      Sheaf (SmallEtale.topology B S hS X.1) AddCommGrpCat.{u}
```

**`AlgebraicGeometry.Space.smallToposMorphism_abelianInverseImage_obj_obj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianRestrictionInverseImage.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianRestrictionInverseImage.lean#L149). The attribute's comment: “the displayed formula for the inverse image, at abelian coefficients”.

> **Stacks 03LP, the displayed formula for the inverse image, at abelian coefficients.** The
> sections of `h_{small}^{-1}G` over an étale chart `W` of `U` are the sections of `G` over the
> composite chart `jW`, as abelian groups.
>
> This is `AlgebraicGeometry.Space.smallToposMorphism_abelianInverseImageIso` evaluated at `G` and
> at `W`; on the right-hand side the sections of a restricted sheaf are the asserted ones by
> definition.

```lean
noncomputable def smallToposMorphism_abelianInverseImage_obj_obj (h : U ⟶ V)
    (hh : IsEtale B S hS h.hom)
    (G : Sheaf (SmallEtale.topology B S hS V.1) AddCommGrpCat.{u + 1})
    (W : SmallEtale B S hS U.1) :
    (((Sites.abelianInverseImage (smallToposMorphism B S hS h)).obj G).obj.obj (.op W)) ≅
      G.obj.obj (.op ((smallEtalePostcomp B S hS h hh).obj W))
```

**`AlgebraicGeometry.Space.smallEtalePostcomp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtalePostcomp.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtalePostcomp.lean#L58). The attribute's comment: “the postcomposition functor”.

> Postcomposition of an étale scheme chart with an étale morphism of algebraic spaces, as a
> functor between the small étale sites.  Its underlying scheme and scheme morphisms are
> unchanged.

```lean
def smallEtalePostcomp (f : X ⟶ Y) (hf : IsEtale B S hS f.hom) :
    SmallEtale B S hS X.1 ⥤ SmallEtale B S hS Y.1
```

**`AlgebraicGeometry.Space.smallEtalePostcomp_obj_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtalePostcomp.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtalePostcomp.lean#L66). The attribute's comment: “action on charts”.

> On charts, postcomposition replaces `U ⟶ X` by its composite with `f`.

```lean
theorem smallEtalePostcomp_obj_hom (f : X ⟶ Y) (hf : IsEtale B S hS f.hom)
    (U : SmallEtale B S hS X.1) :
    ((smallEtalePostcomp B S hS f hf).obj U).1.hom = U.1.hom ≫ f.hom
```

**`AlgebraicGeometry.Space.smallEtalePostcomp_map_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtalePostcomp.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtalePostcomp.lean#L72). The attribute's comment: “action on chart morphisms”.

> On chart morphisms, postcomposition leaves the underlying scheme map unchanged.

```lean
theorem smallEtalePostcomp_map_left (f : X ⟶ Y) (hf : IsEtale B S hS f.hom)
    {U V : SmallEtale B S hS X.1} (g : U ⟶ V) :
    ((smallEtalePostcomp B S hS f hf).map g).hom.left = g.hom.left
```

**`AlgebraicGeometry.Space.smallEtalePostcomp_isContinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtalePostcomp.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtalePostcomp.lean#L111). The attribute's comment: “continuity”.

> Postcomposition along an étale morphism of algebraic spaces is continuous for the small
> étale topologies, so that restriction along it carries sheaves on the small étale site of `Y`
> to sheaves on that of `X`.

```lean
instance smallEtalePostcomp_isContinuous (f : X ⟶ Y) (hf : IsEtale B S hS f.hom) :
    (smallEtalePostcomp B S hS f hf).IsContinuous
      (SmallEtale.topology B S hS X.1) (SmallEtale.topology B S hS Y.1)
```

**`AlgebraicGeometry.Space.smallEtalePostcomp_isCocontinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtalePostcompCocontinuous.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtalePostcompCocontinuous.lean#L96). The attribute's comment: “cocontinuity”.

> **Stacks 03LP.** Postcomposition along an étale morphism of algebraic spaces is
> cocontinuous for the small étale topologies: a covering sieve of the composite chart `jU` pulls
> back to a covering sieve of `U`.
>
> This is `AlgebraicGeometry.Space.SmallEtale.smallEtalePostcomp_cover_lift`, which in turn comes
> from the comparison of the slice of the small étale site of `X` at `U` with the slice of that of
> `Y` at `jU` — Stacks' remark that a covering of `jU` in `Y_étale` is the same thing as a
> covering of `U` in `X_étale`.

```lean
instance smallEtalePostcomp_isCocontinuous (f : X ⟶ Y) (hf : IsEtale B S hS f.hom) :
    (smallEtalePostcomp B S hS f hf).IsCocontinuous
      (SmallEtale.topology B S hS X.1) (SmallEtale.topology B S hS Y.1)
```

**`AlgebraicGeometry.Space.smallToposMorphism_pushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRestriction.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRestriction.lean#L129). The attribute's comment: “the associated morphism of topoi”.

> For an étale morphism of algebraic spaces the small étale direct image is the direct image
> attached to the cocontinuous postcomposition functor on charts.

```lean
def smallToposMorphism_pushforwardIso (f : X ⟶ Y) (hf : IsEtale B S hS f.hom) :
    (smallToposMorphism B S hS f).pushforward ≅
      (smallEtalePostcomp B S hS f hf).sheafPushforwardCocontinuous (Type (u + 1))
        (SmallEtale.topology B S hS X.1) (SmallEtale.topology B S hS Y.1)
```

**`AlgebraicGeometry.Space.smallToposMorphism_inverseImageObjObjIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRestriction.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRestriction.lean#L140). The attribute's comment: “the formula on sections”.

> Sections of the small étale inverse image along an étale morphism over a chart `U ⟶ X` are
> the sections of the original sheaf over the composite chart `U ⟶ Y`.

```lean
def smallToposMorphism_inverseImageObjObjIso (f : X ⟶ Y) (hf : IsEtale B S hS f.hom)
    (G : Sheaf (SmallEtale.topology B S hS Y.1) (Type (u + 1)))
    (U : SmallEtale B S hS X.1) :
    ((smallToposMorphism B S hS f).inverseImage.obj G).obj.obj (Opposite.op U) ≅
      G.obj.obj (Opposite.op ((smallEtalePostcomp B S hS f hf).obj U))
```

**`AlgebraicGeometry.Space.smallToposMorphism_inverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRestrictionInverseImage.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRestrictionInverseImage.lean#L215). The attribute's comment: “the morphism of topoi attached to j is f_small”.

> **Stacks 03LQ**, and the remaining assertion of **Stacks 03LP**: for an étale morphism
> `h : U ⟶ V` of algebraic spaces, the inverse image of the morphism of *small* étale topoi
> `h_{small}` of Stacks 03G2, part (3) is restriction along the postcomposition functor `j` of
> Stacks 03LP, i.e. `G|_{U_étale} = h_{small}^{-1}G`.
>
> The small étale morphism of topoi is the transport of the spaces-étale one along the comparison
> equivalences of Stacks 03G1, so this is
> `AlgebraicGeometry.Space.spacesToposMorphism_inverseImageIso` conjugated by those
> equivalences, the comparison with small étale postcomposition being the identity.

```lean
noncomputable def smallToposMorphism_inverseImageIso (h : U ⟶ V) (hh : IsEtale B S hS h.hom) :
    (smallToposMorphism B S hS h).inverseImage ≅
      (smallEtalePostcomp B S hS h hh).sheafPushforwardContinuous (Type (u + 1))
        (SmallEtale.topology B S hS U.1) (SmallEtale.topology B S hS V.1)
```

**`AlgebraicGeometry.Space.smallToposMorphism_inverseImage_obj_obj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRestrictionInverseImage.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRestrictionInverseImage.lean#L253). The attribute's comment: “the displayed formula for the inverse image”.

> **Stacks 03LP, the displayed formula for the inverse image.** The sections of
> `h_{small}^{-1}G` over an étale chart `W` of `U` are the sections of `G` over the composite
> chart `jW`.
>
> This is `AlgebraicGeometry.Space.smallToposMorphism_inverseImageIso` evaluated at `G` and at
> `W`, the sections of a restricted sheaf being the asserted ones by definition.

```lean
noncomputable def smallToposMorphism_inverseImage_obj_obj (h : U ⟶ V)
    (hh : IsEtale B S hS h.hom)
    (G : Sheaf (SmallEtale.topology B S hS V.1) (Type (u + 1)))
    (W : SmallEtale B S hS U.1) :
    (((smallToposMorphism B S hS h).inverseImage.obj G).obj.obj (.op W)) ≅
      G.obj.obj (.op ((smallEtalePostcomp B S hS h hh).obj W))
```

## Tag 03LQ, an equation

[Tag 03LQ](https://stacks.math.columbia.edu/tag/03LQ) in the Stacks Project.

**`AlgebraicGeometry.Space.smallToposMorphism_abelianInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianRestrictionInverseImage.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianRestrictionInverseImage.lean#L126). The attribute's comment: “at abelian coefficients: h_small^{-1} of an abelian sheaf is restriction along j”.

> **Stacks 03LQ at abelian coefficients.** For an étale morphism `h : U ⟶ V` of algebraic
> spaces, the inverse image of *abelian* sheaves along the morphism of small étale topoi
> `h_{small}` of Stacks 03G2, part (3) is restriction along the postcomposition functor `j` of
> Stacks 03LP, i.e. `G|_{U_étale} = h_{small}^{-1}G` for `G` an abelian sheaf.
>
> `AlgebraicGeometry.Space.smallToposMorphism_inverseImageIso` is the same statement for sheaves
> of sets, which is the form the source states it in.  The right-hand side is
> `AlgebraicGeometry.Space.etaleAbelianRestriction`.
>
> Both sides are the conjugate, by the identification of abelian sheaves with commutative group
> objects of the topos, of `CategoryTheory.Functor.mapCommGrp` of the corresponding set-level
> functor: for the inverse image that is the definition of
> `CategoryTheory.Sites.abelianInverseImage`, and for restriction along `j` it is
> `Stacks.Sites.AbelianPullback.abelianSheafPushforwardIso`.  So the set-level isomorphism is
> carried across by `CategoryTheory.Functor.mapCommGrpNatIso`.

```lean
noncomputable def smallToposMorphism_abelianInverseImageIso (h : U ⟶ V)
    (hh : IsEtale B S hS h.hom) :
    Sites.abelianInverseImage (smallToposMorphism B S hS h) ≅
      (smallEtalePostcomp B S hS h hh).sheafPushforwardContinuous AddCommGrpCat.{u + 1}
        (SmallEtale.topology B S hS U.1) (SmallEtale.topology B S hS V.1)
```

**`AlgebraicGeometry.Space.spacesToposMorphism_inverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRestrictionInverseImage.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRestrictionInverseImage.lean#L180). The attribute's comment: “on the spaces-étale topoi”.

> **Stacks 03LQ on the spaces-étale topoi.** The inverse image of the morphism of
> spaces-étale topoi attached to an étale morphism `h : U ⟶ V` is restriction along
> postcomposition with `h`.
>
> Its direct image is restriction along base change along `h`, and
> `AlgebraicGeometry.Space.spacesEtalePostcompSheafAdjunction` exhibits restriction along
> postcomposition as another left adjoint of that functor, so the two agree by uniqueness of
> left adjoints.

```lean
noncomputable def spacesToposMorphism_inverseImageIso (h : U ⟶ V)
    (hh : IsEtale B S hS h.hom) :
    ((spacesBaseChange_isMorphismOfSites B S hS h).morphismOfTopoi).inverseImage ≅
      (spacesEtalePostcomp B S hS h hh).sheafPushforwardContinuous (Type (u + 1))
        (SpacesEtale.topology B S hS U) (SpacesEtale.topology B S hS V)
```

**`AlgebraicGeometry.Space.smallToposMorphism_inverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRestrictionInverseImage.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRestrictionInverseImage.lean#L215).

> **Stacks 03LQ**, and the remaining assertion of **Stacks 03LP**: for an étale morphism
> `h : U ⟶ V` of algebraic spaces, the inverse image of the morphism of *small* étale topoi
> `h_{small}` of Stacks 03G2, part (3) is restriction along the postcomposition functor `j` of
> Stacks 03LP, i.e. `G|_{U_étale} = h_{small}^{-1}G`.
>
> The small étale morphism of topoi is the transport of the spaces-étale one along the comparison
> equivalences of Stacks 03G1, so this is
> `AlgebraicGeometry.Space.spacesToposMorphism_inverseImageIso` conjugated by those
> equivalences, the comparison with small étale postcomposition being the identity.

```lean
noncomputable def smallToposMorphism_inverseImageIso (h : U ⟶ V) (hh : IsEtale B S hS h.hom) :
    (smallToposMorphism B S hS h).inverseImage ≅
      (smallEtalePostcomp B S hS h hh).sheafPushforwardContinuous (Type (u + 1))
        (SmallEtale.topology B S hS U.1) (SmallEtale.topology B S hS V.1)
```

## Tag 03LR, a lemma

[Tag 03LR](https://stacks.math.columbia.edu/tag/03LR) in the Stacks Project.

**`AlgebraicGeometry.Space.smallEtaleAbelianInverseImageSquareIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianInverseImageSquare.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianInverseImageSquare.lean#L318). The attribute's comment: “the inverse-image footnote, at abelian coefficients”.

> **Stacks 03LR's inverse-image footnote, at abelian coefficients.**  For a cartesian square
> of algebraic spaces, the inverse image of *abelian* sheaves on the small étale sites may be
> taken around the square either way:
> `(f')_{small}^{-1}(G|_{Y'}) = (f_{small}^{-1}G)|_{X'}`, naturally in the abelian sheaf `G`.
>
> As at `Type` coefficients the hypothesis is only that the square commute, which is
> `AlgebraicGeometry.Space.smallEtaleAbelianInverseImageSquareIsoOfComm`; the identity is pure
> functoriality.
>
> Like `AlgebraicGeometry.Space.smallEtaleInverseImageSquareIso`, which is the same statement for
> sheaves of sets, this is the datum of which the inverse of
> `AlgebraicGeometry.Space.smallEtaleAbelianPushforwardBaseChangeIso` is *expected* to be the
> adjunction mate; that identification is not proved here either.

```lean
def smallEtaleAbelianInverseImageSquareIso (sq : IsPullback i f' f g) :
    Sites.abelianInverseImage (smallToposMorphism B S hS g) ⋙
        Sites.abelianInverseImage (smallToposMorphism B S hS f') ≅
      Sites.abelianInverseImage (smallToposMorphism B S hS f) ⋙
        Sites.abelianInverseImage (smallToposMorphism B S hS i)
```

**`AlgebraicGeometry.Space.smallEtalePushforwardBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtalePushforwardBaseChange.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtalePushforwardBaseChange.lean#L202). The attribute's comment: “part (1), sheaves of sets”.

> **Stacks 03LR, part (1).** For a cartesian square of algebraic spaces whose bottom arrow
> `g` is étale, direct image of sheaves of sets on the small étale sites commutes with
> restriction: `f'_{small,*}(F|_{X'}) = (f_{small,*}F)|_{Y'}`, naturally in the sheaf `F`.
>
> Restriction is the inverse image of the small étale morphism of topoi, by Stacks 03LQ.  Each of
> the four functors is the conjugate by the comparison equivalences of Stacks 03G1 of a
> restriction functor on the spaces-étale sites, where the statement is
> `AlgebraicGeometry.Space.spacesPushforwardBaseChangeIso`.

```lean
noncomputable def smallEtalePushforwardBaseChangeIso (sq : IsPullback i f' f g)
    (hg : IsEtale B S hS g.hom) :
    (smallToposMorphism B S hS i).inverseImage ⋙
        (smallToposMorphism B S hS f').pushforward ≅
      (smallToposMorphism B S hS f).pushforward ⋙
        (smallToposMorphism B S hS g).inverseImage
```

**`AlgebraicGeometry.Space.smallEtaleInverseImageSquareIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtalePushforwardBaseChange.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtalePushforwardBaseChange.lean#L267). The attribute's comment: “the inverse-image footnote”.

> The inverse-image identification around a cartesian square, built from the inverse-image
> composition isomorphism of Stacks 03G2, part (3) and the commutativity of the square.
>
> It is the datum of which the inverse of `smallEtalePushforwardBaseChangeIso` is expected to be
> the adjunction mate; that identification is not proved here.
>
> This is the parenthetical assertion of Stacks 03LR — "Also `(f')^{-1}_{small}(G|_{Y'}) =
> (f_{small}^{-1}G)|_{X'}` because of commutativity of the diagram and (03LQ)" — which is why the
> hypothesis is only `sq` and not the étaleness of `g`: the identity is pure functoriality.

```lean
noncomputable def smallEtaleInverseImageSquareIso (sq : IsPullback i f' f g) :
    (smallToposMorphism B S hS g).inverseImage ⋙
        (smallToposMorphism B S hS f').inverseImage ≅
      (smallToposMorphism B S hS f).inverseImage ⋙
        (smallToposMorphism B S hS i).inverseImage
```

**`AlgebraicGeometry.Space.isIso_smallEtaleAbelianHigherBaseChangeMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallEtaleAbelianBaseChangeMate.lean, line 348](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallEtaleAbelianBaseChangeMate.lean#L348). The attribute's comment: “part (2): for every abelian sheaf and every degree n, the canonical comparison (R^n f_{small,*} F)|_{Y'} ⟶ R^n f'_{small,*}(F|_{X'}) of higher direct images is an isomorphism”.

> **Étale base change for higher direct images.**  For a cartesian square of algebraic spaces
> over `S`
>
> ```
> X' --i--> X
> |f'       |f
> Y' --g--> Y
> ```
>
> with `g` étale, and for every `n`, the canonical comparison of higher direct images of abelian
> sheaves on the small étale sites is an isomorphism: `R^n f'_{small,*}(ℱ|_{X'})` and
> `(R^n f_{small,*} ℱ)|_{Y'}` are identified by it, naturally in the abelian sheaf `ℱ`.

```lean
theorem isIso_smallEtaleAbelianHigherBaseChangeMap (sq : IsPullback i f' f g)
    (hg : IsEtale B S hS g.hom) (n : ℕ) :
    IsIso (smallEtaleAbelianHigherBaseChangeMap B S hS i f' f g sq hg n)
```

**`AlgebraicGeometry.Space.smallEtalePushforwardEtaleBaseChange_allParts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallEtaleAbelianBaseChangeMate.lean, line 382](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallEtaleAbelianBaseChangeMate.lean#L382). The attribute's comment: “the whole statement as one conjunction, in the source's order: part (1), that the canonical base-change 2-cell of sheaves of sets is an isomorphism, i.e. f'_* (F|_X') = (f_* F)|_Y'; its inverse-image footnote, (f')^{-1}(G|_Y') = (f^{-1} G)|_X'; and part (2), that for every degree n the canonical comparison (R^n f_* F)|_Y' -> R^n f'_* (F|_X') of higher direct images of abelian sheaves is an isomorphism”.

> **Étale base change on the small étale sites.**  For a cartesian square of algebraic spaces
> over `S`
>
> ```
> X' --i--> X
> |f'       |f
> Y' --g--> Y
> ```
>
> with `g` étale, the following three assertions hold. First, the canonical base-change 2-cell
> `f_{small,*} ∘ g_{small}^{-1} ⟶ i_{small}^{-1} ∘ f'_{small,*}` of sheaves of sets is invertible,
> which is `f'_{small,*}(ℱ|_{X'}) = (f_{small,*}ℱ)|_{Y'}` naturally in `ℱ`. Second,
> `(f')_{small}^{-1}(𝒢|_{Y'}) = (f_{small}^{-1}𝒢)|_{X'}`. Third, in every degree `n` the canonical
> comparison `(R^n f_{small,*} ℱ)|_{Y'} ⟶ R^n f'_{small,*}(ℱ|_{X'})` of higher direct images of
> abelian sheaves is invertible.
>
> The second conjunct is stated as `Nonempty` of an isomorphism of functors; the canonical one is
> `AlgebraicGeometry.Space.smallEtaleInverseImageSquareIso`.

```lean
theorem smallEtalePushforwardEtaleBaseChange_allParts (sq : IsPullback i f' f g)
    (hg : IsEtale B S hS g.hom) :
    IsIso (properBaseChangeMap B S hS f g f' i sq) ∧
      Nonempty ((smallToposMorphism B S hS g).inverseImage ⋙
            (smallToposMorphism B S hS f').inverseImage ≅
          (smallToposMorphism B S hS f).inverseImage ⋙
            (smallToposMorphism B S hS i).inverseImage) ∧
      ∀ n : ℕ, IsIso (smallEtaleAbelianHigherBaseChangeMap B S hS i f' f g sq hg n)
```

**`AlgebraicGeometry.Space.isIso_properBaseChangeMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallEtaleBaseChangeMate.lean, line 821](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallEtaleBaseChangeMate.lean#L821). The attribute's comment: “part (1), invertibility of the canonical base-change 2-cell”.

> For a cartesian square of algebraic spaces whose bottom arrow `g` is étale, the base-change
> 2-cell `f_{small,*} ∘ g_{small}^{-1} ⟶ i_{small}^{-1} ∘ f'_{small,*}` is an isomorphism.

```lean
theorem isIso_properBaseChangeMap (sq : IsPullback i f' f g) (hg : IsEtale B S hS g.hom) :
    IsIso (properBaseChangeMap B S hS f g f' i sq)
```

## Tag 03LS, a lemma

[Tag 03LS](https://stacks.math.columbia.edu/tag/03LS) in the Stacks Project.

**`AlgebraicGeometry.Space.chartRestrictionComp_cocycle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartCanonicalGlueing.lean, line 274](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartCanonicalGlueing.lean#L274). The attribute's comment: “the cocycle condition for the chartwise restrictions”.

> **The cocycle condition of Stacks 03LS for the restrictions of a sheaf to the étale scheme
> charts of `X`**: restricting to a chart `U`, then to a chart `V` over it, then to a chart `W` over
> that, is the same whether the last two steps are taken one at a time or the two morphisms of
> charts are composed first.
>
> This is `AlgebraicGeometry.Space.smallToposMorphism_comp_inverseImage_cocycle` at the represented
> morphisms of the charts, where the three equalities of morphisms of algebraic spaces are
> `AlgebraicGeometry.Space.chartMap_comp_chartToSpace` twice and
> `AlgebraicGeometry.Space.chartMap_comp`.

```lean
theorem chartRestrictionComp_cocycle {W V U : SmallEtale B S hS X.1} (f : V ⟶ U) (g : W ⟶ V) :
    Functor.whiskerRight (chartRestrictionComp B S hS X f).hom
        (chartInverseImage B S hS X g) ≫ (chartRestrictionComp B S hS X g).hom =
    Functor.whiskerLeft (chartRestriction B S hS X U)
        (chartInverseImageComp B S hS X f g).hom ≫
      (chartRestrictionComp B S hS X (g ≫ f)).hom
```

**`AlgebraicGeometry.Space.chartGlueingEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartGlueingEquivalence.lean, line 598](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartGlueingEquivalence.lean#L598).

> **Stacks 03LS.**  A sheaf of sets on the small étale site of an algebraic space `X` is the
> same thing as a family of sheaves `F_U` on the small étale sites of the étale scheme charts `U`
> of `X`, together with isomorphisms `c_f : f^{-1}F_U ≅ F_V` for the morphisms `f : V ⟶ U` of
> charts satisfying the cocycle condition `c_g ∘ g^{-1}c_f = c_{g ≫ f}` — an *equivalence of
> categories*, given by sending a sheaf to the family of its restrictions to the charts.
>
> The proof is the one the source gives: the chartwise inverse image is restriction along
> postcomposition (Stacks 03LQ, through Stacks 03LP), so the chartwise data are the slice-indexed
> data of Stacks 0GWK read through the comparison equivalence of Stacks 04M0
> (`AlgebraicGeometry.Space.sliceToChartFunctor`, an equivalence), and the chartwise description is
> the slice-indexed one read through it
> (`AlgebraicGeometry.Space.chartGlueingFunctorIso`).

```lean
def chartGlueingEquivalence :
    Sheaf (SmallEtale.topology B S hS X.1) (Type (u + 1)) ≌ ChartGlueingData B S hS X
```

**`AlgebraicGeometry.Space.chartInverseImageComp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartSheaves.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartSheaves.lean#L112). The attribute's comment: “canonical comparison of inverse images”.

> **Stacks 03LS.** The canonical comparison of successive chartwise inverse images with the
> inverse image along the composite morphism of charts: it is the adjoint-mate composition
> isomorphism of Stacks 03G2, part (3), read through the equality `chartMap g ≫ chartMap f =
> chartMap (g ≫ f)`.

```lean
noncomputable def chartInverseImageComp {W V U : SmallEtale B S hS X.1} (f : V ⟶ U)
    (g : W ⟶ V) :
    chartInverseImage B S hS X f ⋙ chartInverseImage B S hS X g ≅
      chartInverseImage B S hS X (g ≫ f)
```

**`AlgebraicGeometry.Space.chartRestrictionComp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartSheaves.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartSheaves.lean#L132). The attribute's comment: “compatibility of chart restriction with inverse image”.

> **Stacks 03LS.** Restriction to a chart commutes canonically with further restriction along
> a morphism of charts: the composite of the structure morphism of the larger chart with the
> morphism of charts is the structure morphism of the smaller chart.

```lean
noncomputable def chartRestrictionComp {V U : SmallEtale B S hS X.1} (f : V ⟶ U) :
    chartRestriction B S hS X U ⋙ chartInverseImage B S hS X f ≅
      chartRestriction B S hS X V
```

## Tag 05YY, a lemma

[Tag 05YY](https://stacks.math.columbia.edu/tag/05YY) in the Stacks Project.

**`AlgebraicGeometry.Space.presentationPullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallEtalePresentationCocycle.lean, line 310](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallEtalePresentationCocycle.lean#L310). The attribute's comment: “the canonical isomorphism and its cocycle condition”.

> **Stacks 05YY.** Let `φ : U ⟶ X` be a morphism of algebraic spaces with `R = U ×_X U` and
> `t, s : R ⟶ U` the two projections, as for a presentation of `X` by a surjective étale `φ`. For
> a sheaf `ℱ` on the small étale site of `X`, the sheaf `𝒢 = φ⁻¹ℱ` on the small étale site of `U`
> carries a canonical isomorphism
>
> `α : t⁻¹𝒢 ⟶ s⁻¹𝒢`,
>
> natural in `ℱ`.
>
> It is the identification of the two iterated inverse images along `(t, φ)` and along `(s, φ)`,
> whose composites agree because `R` is the fibre product of `φ` with itself.

```lean
noncomputable def presentationPullbackIso (φ : U ⟶ X) (s t : R ⟶ U)
    (hR : IsPullback t s φ φ) :
    smallEtaleSheafInverseImage B S hS φ ⋙ smallEtaleSheafInverseImage B S hS t ≅
      smallEtaleSheafInverseImage B S hS φ ⋙ smallEtaleSheafInverseImage B S hS s
```

**`AlgebraicGeometry.Space.presentationPullbackIsoApp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallEtalePresentationCocycle.lean, line 341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallEtalePresentationCocycle.lean#L341). The attribute's comment: “the canonical isomorphism and its cocycle condition”.

> **Stacks 05YY.** The isomorphism
>
> `α : t⁻¹𝒢 ⟶ s⁻¹𝒢`
>
> canonically attached to the sheaf `𝒢 = φ⁻¹ℱ`, for `φ : U ⟶ X` with `R = U ×_X U` and
> `t, s : R ⟶ U` the two projections, as for a presentation of `X` by a surjective étale `φ`.
>
> By construction it is the value at `ℱ` of the natural isomorphism
> `AlgebraicGeometry.Space.presentationPullbackIso`.

```lean
noncomputable def presentationPullbackIsoApp (φ : U ⟶ X) (s t : R ⟶ U)
    (hR : IsPullback t s φ φ) (F : smallEtaleSheafCat B S hS X) :
    (smallEtaleSheafInverseImage B S hS t).obj
        ((smallEtaleSheafInverseImage B S hS φ).obj F) ≅
      (smallEtaleSheafInverseImage B S hS s).obj
        ((smallEtaleSheafInverseImage B S hS φ).obj F)
```

**`AlgebraicGeometry.Space.presentationPullbackIsoApp_cocycle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallEtalePresentationCocycle.lean, line 364](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallEtalePresentationCocycle.lean#L364). The attribute's comment: “the canonical isomorphism and its cocycle condition”.

> **Stacks 05YY.** The cocycle condition on `α`. Let `R₂ = R ×_{s, U, t} R` be the fibre
> product of `s` and `t`, with projections `pr₀` and `pr₁`, and let `c : R₂ ⟶ R` be the
> composition law of the groupoid, so that `c` has the target of the first arrow and the source of
> the second. Then the pentagon
>
> `pr₀⁻¹t⁻¹𝒢 → pr₀⁻¹s⁻¹𝒢 = pr₁⁻¹t⁻¹𝒢 → pr₁⁻¹s⁻¹𝒢 = c⁻¹s⁻¹𝒢`,
> `pr₀⁻¹t⁻¹𝒢 = c⁻¹t⁻¹𝒢 → c⁻¹s⁻¹𝒢`
>
> commutes: its three arrows are `pr₀⁻¹α`, `pr₁⁻¹α` and `c⁻¹α`, and its three equalities are the
> canonical identifications of iterated inverse images along pairs with the same composite.
>
> This is `CategoryTheory.compIsoOfEqApp_cocycle` for the small étale inverse images, whose
> associativity coherence is
> `AlgebraicGeometry.Space.smallToposMorphism_comp_inverseImage_assoc`.

```lean
theorem presentationPullbackIsoApp_cocycle (φ : U ⟶ X) (s t : R ⟶ U) (hR : IsPullback t s φ φ)
    (pr₀ pr₁ c : R₂ ⟶ R) (hR₂ : IsPullback pr₀ pr₁ s t) (hct : pr₀ ≫ t = c ≫ t)
    (hcs : pr₁ ≫ s = c ≫ s) (F : smallEtaleSheafCat B S hS X) :
    (smallEtaleSheafInverseImage B S hS pr₀).map
          (presentationPullbackIsoApp B S hS φ s t hR F).hom ≫
        (inverseImageCompIsoOfEqApp B S hS pr₀ pr₁ s t hR₂.w
          ((smallEtaleSheafInverseImage B S hS φ).obj F)).hom ≫
        (smallEtaleSheafInverseImage B S hS pr₁).map
          (presentationPullbackIsoApp B S hS φ s t hR F).hom ≫
        (inverseImageCompIsoOfEqApp B S hS pr₁ c s s hcs
          ((smallEtaleSheafInverseImage B S hS φ).obj F)).hom =
      (inverseImageCompIsoOfEqApp B S hS pr₀ c t t hct
          ((smallEtaleSheafInverseImage B S hS φ).obj F)).hom ≫
        (smallEtaleSheafInverseImage B S hS c).map
          (presentationPullbackIsoApp B S hS φ s t hR F).hom
```

**`AlgebraicGeometry.Space.SpacesEtale.isEquivalence_toPresentationDescentData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallEtalePresentationDescent.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallEtalePresentationDescent.lean#L245). The attribute's comment: “the equivalence of categories”.

> Let `X` be an algebraic space over a scheme `S`, let `φ : U ⟶ X` be a
> surjective étale morphism and let `(U, R, s, t, c, e, i)` be the groupoid of the presentation
> `X = U/R`, so that `R = U ×_X U` with `t` and `s` the two projections and `c` the composition
> law on `R₂ = R ×_{s, U, t} R`. Then the functor taking a sheaf `ℱ` on the small étale site of
> `X` to the pair `(𝒢, α)`, where `𝒢 = φ⁻¹ℱ` is a sheaf on the small étale site of `U` and
> `α : t⁻¹𝒢 ⟶ s⁻¹𝒢` is the canonical isomorphism, is an equivalence of categories onto the
> category of such pairs: pairs of a sheaf on the small étale site of `U` and an isomorphism
> `t⁻¹𝒢 ⟶ s⁻¹𝒢` whose pentagon over `R₂` commutes, with morphisms the maps of sheaves commuting
> with those isomorphisms.

```lean
theorem isEquivalence_toPresentationDescentData
    (hsurj : IsSurjective B S hS Uo.obj.hom.hom) :
    (toPresentationDescentData B S hS t s hR pr₀ pr₁ c hR₂ hct hcs).IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 66.18, Tag 03EB](https://stacks.math.columbia.edu/tag/03EB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
