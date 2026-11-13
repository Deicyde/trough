---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.IsThickening, AlgebraicGeometry.Stack.ThickeningMorphism, AlgebraicGeometry.Stack.ThickeningOver, AlgebraicGeometry.Stack.ThickeningMorphismOver, AlgebraicGeometry.Stack.isThickening_iff_isRelativeThickening, AlgebraicGeometry.Stack.isClosedImmersion_of_isThickening, AlgebraicGeometry.Stack.universalHomeomorphism_of_isThickening, AlgebraicGeometry.Stack.AlgebraicStacks.IsFirstOrderThickening
statement: formalized
proof: formalized
---

# 106.3 Thickenings

Section 106.3 of the Stacks Project, [Tag 0BPN](https://stacks.math.columbia.edu/tag/0BPN). 9 tags here are carried by 38 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BPP, a definition

[Tag 0BPP](https://stacks.math.columbia.edu/tag/0BPP) in the Stacks Project.

**`AlgebraicGeometry.Stack.IsThickening`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Thickening.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Thickening.lean#L82). The attribute's comment: “part (1): thickening”.

> **Stacks 0BPP**, part (1). A 1-morphism of algebraic stacks over `S` *is a thickening* when it
> is a closed immersion, in the sense of Stacks 04YL part (2), and is surjective on the underlying
> sets of points.
>
> The source's part (1) also asserts that the induced map of underlying topological spaces is a
> homeomorphism; that clause needs the point topology of Stacks 04XL, which has no library site, so
> it is not stated here.

```lean
abbrev IsThickening {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (i : 𝒳 ⟶ 𝒴) : Prop
```

**`AlgebraicGeometry.Stack.ThickeningMorphism`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Thickening.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Thickening.lean#L92). The attribute's comment: “part (2): morphisms of thickenings”.

> **Stacks 0BPP**, part (2). A *morphism of thickenings* from the thickening `i` to the
> thickening `j` of algebraic stacks over `S`: a 1-morphism of the ambient stacks, a 1-morphism of
> the closed substacks, and a 2-isomorphism saying that the former restricts to the latter.

```lean
structure ThickeningMorphism {𝒳 𝒳' 𝒴 𝒴' : AlgebraicStacks.{u, w} B S hS}
    (i : 𝒳 ⟶ 𝒳') (j : 𝒴 ⟶ 𝒴') (_hi : IsThickening i) (_hj : IsThickening j)
```

**`AlgebraicGeometry.Stack.ThickeningOver`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Thickening.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Thickening.lean#L105). The attribute's comment: “part (3): thickenings over a stack”.

> **Stacks 0BPP**, part (3). A thickening of algebraic stacks over `S` together with a
> 1-morphism from its ambient stack to a fixed algebraic stack `𝒵`.

```lean
structure ThickeningOver (𝒵 : AlgebraicStacks.{u, w} B S hS)
```

**`AlgebraicGeometry.Stack.ThickeningMorphismOver`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Thickening.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Thickening.lean#L121). The attribute's comment: “part (3): morphisms over a stack”.

> **Stacks 0BPP**, part (3). A morphism of thickenings of algebraic stacks over a fixed
> algebraic stack `𝒵`: a morphism of the underlying thickenings whose ambient component lies over
> the base up to 2-isomorphism.

```lean
structure ThickeningMorphismOver {𝒵 : AlgebraicStacks.{u, w} B S hS}
    (𝒳 𝒴 : ThickeningOver.{u, w} 𝒵)
```

## Tag 0CJ7, a lemma

[Tag 0CJ7](https://stacks.math.columbia.edu/tag/0CJ7) in the Stacks Project.

**`AlgebraicGeometry.Stack.isThickening_iff_isRelativeThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningUniversalHomeomorphism.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningUniversalHomeomorphism.lean#L97). The attribute's comment: “equivalence of (1) and (2)”.

> A 1-morphism of algebraic stacks over `S` is a thickening in the sense of **Stacks 0BPP** part
> (1) if and only if it is representable by algebraic spaces and is a thickening in the relative sense
> of §04XB, that is a closed immersion all of whose algebraic-space base changes are surjective.
>
> The closed-immersion clause is the same on both sides; the surjectivity clause is surjectivity on
> the points of Stacks 04XG on the left and the relative property of Stacks 03YK on the right, and
> the two agree by **Stacks 04XI**.

```lean
theorem isThickening_iff_isRelativeThickening (i : 𝒳 ⟶ 𝒳') :
    IsThickening i ↔ IsRelativeThickening B S hS i.hom
```

**`AlgebraicGeometry.Stack.isClosedImmersion_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningUniversalHomeomorphism.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningUniversalHomeomorphism.lean#L110). The attribute's comment: “closed immersion”.

> A thickening of algebraic stacks over `S` is a closed immersion in the sense of **Stacks 04YL**
> part (2).
>
> In this library that is a clause of the definition of a thickening: **Stacks 0BPP** part (1)
> realises the source as a *closed substack* of the target, and
> `AlgebraicGeometry.Stack.IsThickening` records that closed immersion rather than recovering it
> from a looser condition.

```lean
theorem isClosedImmersion_of_isThickening (hi : IsThickening i) :
    AlgebraicStacks.IsClosedImmersion B S hS i
```

**`AlgebraicGeometry.Stack.universalHomeomorphism_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningUniversalHomeomorphism.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningUniversalHomeomorphism.lean#L146). The attribute's comment: “universal homeomorphism”.

> A thickening of algebraic stacks over `S` is a universal homeomorphism in the sense of
> **Stacks 0CI7**: every base change of it induces a homeomorphism on the topological spaces of
> points of Stacks 04XG and 04XL.
>
> A base change of a thickening is a thickening (**Stacks 0BPR**,
> `AlgebraicGeometry.Stack.isThickening_fst_of_isTwoFibreProduct`), and a thickening is a
> homeomorphism on points by
> `AlgebraicGeometry.Stack.isHomeomorphOnPoints_of_isThickening`. The statement is at the
> model-independent `AlgebraicGeometry.Stack.UniversalHomeomorphism`, so it tests every 2-fibre
> product square of the cospan and not only the canonical one.

```lean
theorem universalHomeomorphism_of_isThickening (hi : IsThickening i) :
    UniversalHomeomorphism B S hS i
```

## Tag 0BPQ, a definition

[Tag 0BPQ](https://stacks.math.columbia.edu/tag/0BPQ) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsFirstOrderThickening`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FirstOrderThickening.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FirstOrderThickening.lean#L74).

> **Stacks 0BPQ.** A closed immersion `i : 𝒳 ⟶ 𝒳'` of algebraic stacks over `S` exhibits `𝒳'`
> as a *first-order thickening* of `𝒳` when, for every scheme-valued point `U ⟶ 𝒳'` and every
> algebraic space `F` representing the base change of `i` along it, the image of the structural
> morphism of `F` is a first-order thickening of the representable algebraic space of `U` in the
> sense of Stacks 05ZK, part (2) — that is, the ideal cutting it out is square-zero on every object
> of the small étale site.

```lean
abbrev IsFirstOrderThickening (i : 𝒳 ⟶ 𝒳') : Prop
```

## Tag 0BPR, a lemma

[Tag 0BPR](https://stacks.math.columbia.edu/tag/0BPR) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isFirstOrderThickening_fst_of_isTwoFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FirstOrderThickeningBaseChange.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FirstOrderThickeningBaseChange.lean#L55). The attribute's comment: “first order thickening base-changes to a first order thickening”.

> If `𝒴 ⊂ 𝒴'` is a first-order thickening of algebraic
> stacks over `S` and `𝒳 = 𝒴 ×_{𝒴'} 𝒳'` for a 1-morphism `g : 𝒳' ⟶ 𝒴'`, then `𝒳 ⊂ 𝒳'` — the
> projection `P.fst` — is a first-order thickening.

```lean
theorem isFirstOrderThickening_fst_of_isTwoFibreProduct
    {𝒴 𝒴' 𝒳' : Stack.AlgebraicStacks.{u, w} B S hS} {j : 𝒴 ⟶ 𝒴'} {g : 𝒳' ⟶ 𝒴'}
    (hj : IsFirstOrderThickening B S hS j)
    (P : Bicategory.TwoCommSq g j) (hP : Bicategory.IsTwoFibreProduct P) :
    IsFirstOrderThickening B S hS P.fst
```

**`AlgebraicGeometry.Stack.isThickening_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningBaseChange.lean, line 275](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningBaseChange.lean#L275). The attribute's comment: “base-changed thickening”.

> **Stacks 0BPR.** Let `i : 𝒴 ⟶ 𝒴'` be a thickening of algebraic stacks over `S`, let
> `f : 𝒳' ⟶ 𝒴'` be a 1-morphism of algebraic stacks, and let `P` be a 2-fibre product of that
> cospan in the 2-category of algebraic stacks. Then the second projection
> `P.snd : 𝒴 ×_{𝒴'} 𝒳' ⟶ 𝒳'` is a thickening.
>
> A thickening is a closed immersion which is surjective on points, and each of its three
> constituents base-changes: representability by algebraic spaces by Stacks 0302, the
> closed-immersion property of Stacks 04XB by Stacks 045C, and surjectivity on points by
> Stacks 04ZU.

```lean
theorem isThickening_baseChange (i : 𝒴 ⟶ 𝒴') (f : 𝒳' ⟶ 𝒴')
    (P : Bicategory.TwoCommSq i f) (hP : Bicategory.IsTwoFibreProduct P)
    (hi : IsThickening i) :
    IsThickening P.snd
```

**`AlgebraicGeometry.Stack.baseChangeThickeningMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningBaseChange.lean, line 289](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningBaseChange.lean#L289). The attribute's comment: “morphism of thickenings”.

> **Stacks 0BPR.** A 2-fibre product square of a thickening `i : 𝒴 ⟶ 𝒴'` of algebraic stacks
> along a 1-morphism `f : 𝒳' ⟶ 𝒴'` *is* a morphism of thickenings from the base-changed thickening
> `P.snd` to `i`: its ambient 1-morphism is `f`, its restricted 1-morphism is the first projection
> `P.fst`, and the 2-isomorphism filling the square is exactly the assertion that `f` restricts to
> `P.fst`.

```lean
def baseChangeThickeningMorphism (i : 𝒴 ⟶ 𝒴') (f : 𝒳' ⟶ 𝒴')
    (P : Bicategory.TwoCommSq i f) (hP : Bicategory.IsTwoFibreProduct P)
    (hi : IsThickening i) :
    ThickeningMorphism P.snd i (isThickening_baseChange B S hS i f P hP hi) hi
```

## Tag 0BPS, a lemma

[Tag 0BPS](https://stacks.math.columbia.edu/tag/0BPS) in the Stacks Project.

**`AlgebraicGeometry.Stack.isThickening_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningComposition.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningComposition.lean#L75). The attribute's comment: “the composite of two thickenings is a thickening”.

> **Stacks 0BPS.** A composite of thickenings of algebraic stacks over `S` is a thickening:
> the composite is a closed immersion by Stacks 0502, and it is surjective on points because each
> factor is.

```lean
theorem isThickening_comp
    {𝒳 𝒴 𝒵 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : IsThickening f) (hg : IsThickening g) :
    IsThickening (f ≫ g)
```

## Tag 0BPT, an example

[Tag 0BPT](https://stacks.math.columbia.edu/tag/0BPT) in the Stacks Project.

**`AlgebraicGeometry.Stack.isThickening_stackReductionInclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningReduction.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningReduction.lean#L148). The attribute's comment: “assertion (1): an algebraic stack is a thickening of its reduction”.

> **Stacks 0BPT, assertion (1).** An algebraic stack over `S` is a thickening of its reduction:
> the inclusion of the reduction is a closed immersion and is surjective on points, which are the
> two clauses of `AlgebraicGeometry.Stack.IsThickening` (**Stacks 0BPP**, part (1)).
>
> Surjectivity on points is the clause of Definition 050C that the set of points of the reduction is
> all of `|𝒳|`.

```lean
theorem isThickening_stackReductionInclusion (R : StackReduction B S hS 𝒳) :
    IsThickening R.inclusion
```

**`AlgebraicGeometry.Stack.isClosedSubstack_stackReductionEssImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningReduction.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningReduction.lean#L180). The attribute's comment: “assertion (1), substack form: the reduction is a closed substack with every point”.

> **Stacks 0BPT, assertion (1), substack form.** The reduction of an algebraic stack `𝒳` over
> `S` is realised as a closed substack of `𝒳` carrying every point of `𝒳`, which is what it means
> for `𝒳` to be a thickening of it in the substack language of **Stacks 04YM**, part (2).
>
> The substack is the essential image of the inclusion of the reduction, a closed substack by
> **Stacks 0506**.

```lean
theorem isClosedSubstack_stackReductionEssImage (R : StackReduction B S hS 𝒳) :
    ∃ hP : IsAlgebraicStack.{u, w} B S hS
        (fullSubcategoryBased 𝒳
          (CatFiberedInGroupoids.homFunctor R.inclusion.hom).essImage),
      AlgebraicStacks.IsClosedImmersion B S hS
          (fullSubcategoryInclusion 𝒳
            (CatFiberedInGroupoids.homFunctor R.inclusion.hom).essImage hP) ∧
        IsSurjective B S hS
          (fullSubcategoryInclusion 𝒳
            (CatFiberedInGroupoids.homFunctor R.inclusion.hom).essImage hP)
```

**`AlgebraicGeometry.Stack.stackReductionOfThickening`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningReduction.lean, line 203](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningReduction.lean#L203). The attribute's comment: “assertion (2): a thickening has the same reduction as its ambient stack”.

> **Stacks 0BPT, assertion (2).** Let `𝒳 ⊆ 𝒳'` be a thickening of algebraic stacks over `S`.
> Then the reduction of `𝒳` is a reduction of `𝒳'`, included through `𝒳`: this is the source's
> `𝒳'_red = 𝒳_red ⊆ 𝒳`.
>
> The inclusion is the composite of the inclusion of the reduction of `𝒳` with the given thickening,
> which is again a thickening by **Stacks 0BPS**, and the source stack is untouched, so it is still
> reduced.

```lean
def stackReductionOfThickening
    [(Space.closedImmersionProperty B S hS).IsLocalAtTarget
      (Space.Topology.fppf.precoverage.{u, u} B S hS)]
    (R : StackReduction B S hS 𝒳) (i : 𝒳 ⟶ 𝒳') (hi : IsThickening i) :
    StackReduction B S hS 𝒳'
```

**`AlgebraicGeometry.Stack.isReducedStack_iff_essImage_stackReduction_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningReduction.lean, line 279](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningReduction.lean#L279). The attribute's comment: “assertion (3): the reduction is the whole stack exactly when the stack is reduced”.

> **Stacks 0BPT, assertion (3).** Let `R` present the reduction of an algebraic stack `𝒳` over
> `S`. Then the closed substack of `𝒳` cut out by that reduction is all of `𝒳` exactly when `𝒳` is a
> reduced algebraic stack.
>
> Read through assertion (2) this is the source's assertion (3): for a thickening `𝒳 ⊆ 𝒳'` the
> reduction of `𝒳'` is the reduction of `𝒳`, so `𝒳 = 𝒳'_red` says precisely that the reduction of
> `𝒳` is all of `𝒳`.
>
> One direction is **Stacks 050A** at the closed substack cut out by the essential image of the
> inclusion of the reduction, which carries every point of `𝒳`. For the other, a reduction whose
> substack is all of `𝒳` has fully faithful and essentially surjective inclusion, so reducedness
> transports from the reduction to `𝒳`.

```lean
theorem isReducedStack_iff_essImage_stackReduction_eq_top (R : StackReduction B S hS 𝒳) :
    (CatFiberedInGroupoids.homFunctor R.inclusion.hom).essImage = ⊤ ↔
      IsReducedStack B S hS 𝒳
```

**`AlgebraicGeometry.Stack.isThickening_stackReduction_inclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningReductionCanonical.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningReductionCanonical.lean#L77). The attribute's comment: “assertion (1): an algebraic stack is a thickening of its reduction”.

> **Stacks 0BPT, assertion (1).** An algebraic stack `𝒳'` over `S` is a thickening of its
> reduction `𝒳'_red` (**Stacks 050C**): the inclusion of the reduction is a closed immersion which
> is surjective on points, the two clauses of `AlgebraicGeometry.Stack.IsThickening`
> (**Stacks 0BPP**).

```lean
theorem isThickening_stackReduction_inclusion (𝒳' : AlgebraicStacks.{u, w} B S hS) :
    IsThickening (stackReduction 𝒳').inclusion
```

**`AlgebraicGeometry.Stack.essImage_stackReduction_eq_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningReductionCanonical.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningReductionCanonical.lean#L114). The attribute's comment: “assertion (2): a thickening has the same reduction as its ambient stack”.

> **Stacks 0BPT, assertion (2).** Let `i : 𝒳 ⟶ 𝒳'` be a thickening of algebraic stacks over
> `S`. Then `𝒳'_red = 𝒳_red ⊆ 𝒳`: the reduction of `𝒳'` is the substack of `𝒳'` cut out by the
> reduction of `𝒳` included through `i`, and it lies in the substack cut out by `𝒳`.
>
> The composite of the inclusion of `𝒳_red` with `i` is again a thickening by **Stacks 0BPS** and
> has reduced source, so its essential image is a reduction of `𝒳'` in the sense of
> `AlgebraicGeometry.Stack.IsReduction`; so is that of the inclusion of `𝒳'_red`, and the two agree
> by uniqueness of the reduction (**Stacks 0509**).

```lean
theorem essImage_stackReduction_eq_of_isThickening {𝒳 𝒳' : AlgebraicStacks.{u, w} B S hS}
    (i : 𝒳 ⟶ 𝒳') (hi : IsThickening i) :
    (CatFiberedInGroupoids.homFunctor (stackReduction 𝒳').inclusion.hom).essImage =
        (CatFiberedInGroupoids.homFunctor ((stackReduction 𝒳).inclusion ≫ i).hom).essImage ∧
      (CatFiberedInGroupoids.homFunctor (stackReduction 𝒳').inclusion.hom).essImage ≤
        (CatFiberedInGroupoids.homFunctor i.hom).essImage
```

**`AlgebraicGeometry.Stack.essImage_stackReduction_eq_essImage_iff_isReducedStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningReductionCanonical.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningReductionCanonical.lean#L138). The attribute's comment: “assertion (3): a thickening is the reduction of its ambient stack exactly when it is reduced”.

> **Stacks 0BPT, assertion (3).** Let `i : 𝒳 ⟶ 𝒳'` be a thickening of algebraic stacks over
> `S`. Then `𝒳 = 𝒳'_red` — the reduction of `𝒳'` and `𝒳` cut out the same substack of `𝒳'` —
> exactly when `𝒳` is a reduced algebraic stack.
>
> By assertion (2) the reduction of `𝒳'` is the substack cut out by the reduction of `𝒳` through
> `i`; since `i` is fully faithful (**Stacks 0506**), that is the substack cut out by `i` exactly
> when the reduction of `𝒳` is all of `𝒳`, which is reducedness of `𝒳` by
> `AlgebraicGeometry.Stack.isReducedStack_iff_essImage_stackReduction_eq_top`.

```lean
theorem essImage_stackReduction_eq_essImage_iff_isReducedStack
    {𝒳 𝒳' : AlgebraicStacks.{u, w} B S hS} (i : 𝒳 ⟶ 𝒳') (hi : IsThickening i) :
    (CatFiberedInGroupoids.homFunctor (stackReduction 𝒳').inclusion.hom).essImage =
        (CatFiberedInGroupoids.homFunctor i.hom).essImage ↔
      IsReducedStack B S hS 𝒳
```

## Tag 0BPU, a lemma

[Tag 0BPU](https://stacks.math.columbia.edu/tag/0BPU) in the Stacks Project.

**`AlgebraicGeometry.Stack.isThickening_diagonalComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningDiagonal.lean, line 456](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningDiagonal.lean#L456). The attribute's comment: “first assertion”.

> **Stacks 0BPU, the first assertion.** In a morphism of thickenings
> `(f, f') : (𝒳 ⊂ 𝒳') → (𝒴 ⊂ 𝒴')` of algebraic stacks over `S`, the comparison 1-morphism
> `𝒳 ×_𝒴 𝒳 ⟶ 𝒳' ×_{𝒴'} 𝒳'` is a thickening.
>
> Since `𝒳 → 𝒴'` factors through the closed substack `𝒴`, the enlargement of the target
> identifies `𝒳 ×_𝒴 𝒳` with `𝒳 ×_{𝒴'} 𝒳` (**Stacks 04ZZ** (1) ⟹ (2) makes `j` fully faithful);
> the latter maps to `𝒳' ×_{𝒴'} 𝒳'` by two base changes of the thickening `i`, one factor at a
> time, each a thickening by **Stacks 0BPR**, so their composite is one by **Stacks 0BPS**.
>
> This carries the part key *first assertion* of Stacks 0BPU for *this* comparison 1-morphism. The
> other assertion of that tag, that the diagonal square is cartesian, is not proved for it — see
> the implementation notes, which name the obstruction. Both assertions are proved for the rebuilt
> comparison with an explicit body: the first by `isThickening_selfProductDiagonalMap` below, which
> carries the same part key, and the cartesian one by
> `isTwoFibreProduct_selfProductDiagonalSquare`. The 2-isomorphism between the two comparisons is
> still open, which is why the first assertion is registered twice rather than once.
>
> The fppf-target-locality instance is Stacks 0420. The library proves it at the fpqc precoverage,
> `isClosedImmersion_isLocalAtTarget_fpqc`, and restricts it to the fppf precoverage asked for
> here in `AlgebraicGeometry.Space.isClosedImmersion_isLocalAtTarget_fppf`, which is an instance;
> the hypothesis below is therefore discharged automatically.

```lean
theorem isThickening_diagonalComparison
    [(Space.closedImmersionProperty B S hS).IsLocalAtTarget
      (Space.Topology.fppf.precoverage.{u, u} B S hS)] :
    IsThickening (diagonalComparison B S hS m)
```

**`AlgebraicGeometry.Stack.isThickening_selfProductDiagonalMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningDiagonal.lean, line 797](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningDiagonal.lean#L797). The attribute's comment: “first assertion”.

> **Stacks 0BPU, the first assertion, for the comparison with an explicit body.** For a morphism
> of thickenings `(f, f') : (𝒳 ⊂ 𝒳') → (𝒴 ⊂ 𝒴')` of algebraic stacks over `S`, the canonical
> comparison 1-morphism `AlgebraicGeometry.Stack.selfProductDiagonalMap : 𝒳 ×_𝒴 𝒳 ⟶ 𝒳' ×_{𝒴'} 𝒳'`
> is a thickening.
>
> The source's factorisation of the comparison into two base changes of `i`, one factor at a time,
> is carried here *strictly*: the comparison is `AlgebraicGeometry.Stack.selfProductFstLift`
> followed by the base change of `i` along the first projection of `𝒳' ×_{𝒴'} 𝒳'`, on the nose
> (`AlgebraicGeometry.Stack.selfProductFstLift_comp_snd`, which holds by `rfl`). The second factor
> is a thickening by **Stacks 0BPR**
> (`AlgebraicGeometry.Stack.isThickening_ambientFstRestriction_snd`); the first is one because
> `AlgebraicGeometry.Stack.isTwoFibreProduct_selfProductSndSquare` exhibits it too as a base change
> of `i`, so **Stacks 0BPR** applies again; and their composite is a thickening by **Stacks 0BPS**,
> `AlgebraicGeometry.Stack.isThickening_comp`.
>
> This carries the part key *first assertion* of Stacks 0BPU, and together with
> `AlgebraicGeometry.Stack.isTwoFibreProduct_selfProductDiagonalSquare` — which carries the part key
> *cartesian diagonal square* — it puts **both** assertions of the tag on this one comparison
> 1-morphism. The part key *first assertion* is also carried by
> `AlgebraicGeometry.Stack.isThickening_diagonalComparison`, the same assertion for the other
> canonical comparison `AlgebraicGeometry.Stack.diagonalComparison`; that registration is kept, the
> two comparisons being 2-isomorphic but not yet identified in the library.
>
> The fppf-target-locality instance is Stacks 0420 and is discharged automatically, exactly as in
> `AlgebraicGeometry.Stack.isThickening_diagonalComparison`.

```lean
theorem isThickening_selfProductDiagonalMap
    [(Space.closedImmersionProperty B S hS).IsLocalAtTarget
      (Space.Topology.fppf.precoverage.{u, u} B S hS)] :
    IsThickening (selfProductDiagonalMap B S hS m)
```

**`AlgebraicGeometry.Stack.isTwoFibreProduct_selfProductDiagonalSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningDiagonal.lean, line 944](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningDiagonal.lean#L944). The attribute's comment: “cartesian diagonal square”.

> **Stacks 0BPU, the second assertion: the diagonal square of a morphism of thickenings of
> algebraic stacks is cartesian.** For a morphism of thickenings
> `(f, f') : (𝒳 ⊂ 𝒳') → (𝒴 ⊂ 𝒴')` of algebraic stacks over `S`, the square
>
> ```text
>   𝒳  --Δ-->  𝒳 ×_𝒴 𝒳
>   |              |
>   v              v
>   𝒳' --Δ'--> 𝒳' ×_{𝒴'} 𝒳'
> ```
>
> is a 2-fibre product in the 2-category of algebraic stacks over `(Sch/S)_fppf`, the right-hand
> leg being the canonical comparison
> `AlgebraicGeometry.Stack.selfProductDiagonalMap` — canonical strictly, by
> `AlgebraicGeometry.Stack.selfProductDiagonalMap_comp_fst` and `…_comp_snd`.
>
> The source proves this by applying **Stacks 0CBB** to `𝒳 ⟶ 𝒳' ⟶ 𝒴'`, using that the thickening
> `i : 𝒳 ⟶ 𝒳'` is a monomorphism. Here it is the over-the-base form of 0CBB with a growing target,
> `CategoryTheory.TwoFibreProductOver.isEquivalence_selfProductDiagonalComparison`, whose three
> hypotheses are met because a closed immersion of algebraic stacks is fully faithful
> (**Stacks 04ZZ** (1) ⟹ (2),
> `AlgebraicGeometry.Stack.AlgebraicStacks.full_and_faithful_homFunctor_of_isClosedImmersion`),
> applied to `i` for fullness and faithfulness and to `j` for the faithfulness the growing target
> costs. The passage from an equivalence of underlying categories to the universal property is
> `CategoryTheory.Bicategory.isTwoFibreProduct_of_isEquivalence_to` against the canonical 2-fibre
> product square of the cospan, and the passage from the 2-category of categories fibred in
> groupoids down to the full sub-2-category of algebraic stacks is
> `AlgebraicGeometry.Stack.AlgebraicStacks.isTwoFibreProduct_of_toCatFiberedInGroupoids`.
>
> This carries the part key *cartesian diagonal square* of Stacks 0BPU; the other assertion, that
> the comparison is a thickening, is
> `AlgebraicGeometry.Stack.isThickening_selfProductDiagonalMap`, for **this same** comparison
> 1-morphism, so the two assertions of the tag are both statements about
> `AlgebraicGeometry.Stack.selfProductDiagonalMap`. The first assertion is registered a second time
> on `AlgebraicGeometry.Stack.isThickening_diagonalComparison`, which asserts it of the other
> canonical comparison `AlgebraicGeometry.Stack.diagonalComparison`; the implementation note above
> says why the cartesian assertion cannot be carried by that one.
>
> **What identifying the two comparisons still lacks.** The two 1-morphisms are 2-isomorphic, being
> two canonical comparisons into a 2-fibre product, and
> `AlgebraicGeometry.Stack.isThickening_congr_twoIso` would then make either of the two
> first-assertion registrations redundant. The 2-isomorphism is *not* available from
> `CategoryTheory.Bicategory.twoFibreProduct_twoIso_of_legs`, however: that result needs the two
> comparison 2-cells to be compatible with the filler of `𝒳' ×_{𝒴'} 𝒳'`, and that compatibility
> mentions the filler whiskered by `AlgebraicGeometry.Stack.diagonalComparison`, which is the very
> thing the `Quotient.out` in `AlgebraicGeometry.Stack.selfProductComparison` makes uncomputable.
> It would instead have to come from
> `CategoryTheory.Bicategory.twoFibreProduct_twoIso_of_preHom`, i.e. by exhibiting
> `AlgebraicGeometry.Stack.diagonalComparison` as the 1-morphism of a pre-morphism of
> 2-commutative squares assembled by `CategoryTheory.Bicategory.TwoCommSq.PreHom.comp` from its
> four stages — the enlargement of the target, the comparison of the two models of the cospan
> `(f ≫ j, f ≫ j)`, and the two base changes of `i` — which is a chase through two cospan
> reindexings that the library does not currently assemble.

```lean
def isTwoFibreProduct_selfProductDiagonalSquare :
    Bicategory.IsTwoFibreProduct (selfProductDiagonalSquare B S hS m)
```

## Tag 0BPV, a lemma

[Tag 0BPV](https://stacks.math.columbia.edu/tag/0BPV) in the Stacks Project.

**`AlgebraicGeometry.Stack.thickeningMorphism_relativeDiagonal_inner_iff_outer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningDiagonalProperties.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningDiagonalProperties.lean#L99).

> **Stacks 0BPV.** Let `(f, f') : (𝒳 ⊂ 𝒳') → (𝒴 ⊂ 𝒴')` be a morphism of thickenings of
> algebraic stacks over `S`, `f = m.inner` and `f' = m.outer`, and let `Δ : 𝒳 ⟶ 𝒳 ×_𝒴 𝒳` and
> `Δ' : 𝒳' ⟶ 𝒳' ×_{𝒴'} 𝒳'` be the relative diagonals. Then `Δ` has each of the following
> properties if and only if `Δ'` has it:
> (a) representable by schemes, (b) affine, (c) surjective, (d) quasi-compact,
> (e) universally closed, (f) integral, (g) quasi-separated, (h) separated,
> (i) universally injective, (j) universally open, (k) locally quasi-finite, (l) finite,
> (m) unramified, (n) monomorphism, (o) immersion, (p) closed immersion, (q) proper.
>
> The conjuncts are, in order, the seventeen properties of the source; (b) and (d)–(q) are the
> conditions of Properties of Stacks, Section 04XB, at the corresponding properties of morphisms of
> algebraic spaces.

```lean
theorem thickeningMorphism_relativeDiagonal_inner_iff_outer (m : ThickeningMorphism i j hi hj) :
    -- (a) representable by schemes
    (Stacks.RepresentableMorphism.IsRepresentableMorphism 𝒳.val.val.p
        (AlgebraicStacks.twoFibreProduct B S hS m.inner m.inner).val.val.p
        (CatFiberedInGroupoids.homFunctor
          (AlgebraicStacks.relativeDiagonal B S hS m.inner).hom) ↔
      Stacks.RepresentableMorphism.IsRepresentableMorphism 𝒳'.val.val.p
        (AlgebraicStacks.twoFibreProduct B S hS m.outer m.outer).val.val.p
        (CatFiberedInGroupoids.homFunctor
          (AlgebraicStacks.relativeDiagonal B S hS m.outer).hom)) ∧
    -- (b) affine
    (Stack.IsAffineHom B S hS (AlgebraicStacks.relativeDiagonal B S hS m.inner).hom ↔
      Stack.IsAffineHom B S hS (AlgebraicStacks.relativeDiagonal B S hS m.outer).hom) ∧
    -- (c) surjective
    (IsSurjective B S hS (AlgebraicStacks.relativeDiagonal B S hS m.inner) ↔
      IsSurjective B S hS (AlgebraicStacks.relativeDiagonal B S hS m.outer)) ∧
    -- (d) quasi-compact
    (Stack.IsQuasiCompact B S hS (AlgebraicStacks.relativeDiagonal B S hS m.inner).hom ↔
      Stack.IsQuasiCompact B S hS (AlgebraicStacks.relativeDiagonal B S hS m.outer).hom) ∧
    -- (e) universally closed
    (Stack.UniversallyClosed B S hS (AlgebraicStacks.relativeDiagonal B S hS m.inner).hom ↔
      Stack.UniversallyClosed B S hS (AlgebraicStacks.relativeDiagonal B S hS m.outer).hom) ∧
    -- (f) integral
    (HasRelativeProperty.{u, u, u + 1, u} B S hS (Space.integralMorphismProperty B S hS)
        (AlgebraicStacks.relativeDiagonal B S hS m.inner).hom
        (isRepresentableByAlgebraicSpaces_relativeDiagonal_algebraicStacks B S hS m.inner) ↔
      HasRelativeProperty.{u, u, u + 1, u} B S hS (Space.integralMorphismProperty B S hS)
        (AlgebraicStacks.relativeDiagonal B S hS m.outer).hom
        (isRepresentableByAlgebraicSpaces_relativeDiagonal_algebraicStacks B S hS m.outer)) ∧
    -- (g) quasi-separated
    (Stack.IsQuasiSeparated B S hS (AlgebraicStacks.relativeDiagonal B S hS m.inner).hom ↔
      Stack.IsQuasiSeparated B S hS (AlgebraicStacks.relativeDiagonal B S hS m.outer).hom) ∧
    -- (h) separated
    (Stack.IsSeparated B S hS (AlgebraicStacks.relativeDiagonal B S hS m.inner).hom ↔
      Stack.IsSeparated B S hS (AlgebraicStacks.relativeDiagonal B S hS m.outer).hom) ∧
    -- (i) universally injective
    (UniversallyInjective B S hS (AlgebraicStacks.relativeDiagonal B S hS m.inner) ↔
      UniversallyInjective B S hS (AlgebraicStacks.relativeDiagonal B S hS m.outer)) ∧
    -- (j) universally open
    (HasRelativeProperty.{u, u, u + 1, u} B S hS (Space.universallyOpenMorphismProperty B S hS)
        (AlgebraicStacks.relativeDiagonal B S hS m.inner).hom
        (isRepresentableByAlgebraicSpaces_relativeDiagonal_algebraicStacks B S hS m.inner) ↔
      HasRelativeProperty.{u, u, u + 1, u} B S hS (Space.universallyOpenMorphismProperty B S hS)
        (AlgebraicStacks.relativeDiagonal B S hS m.outer).hom
        (isRepresentableByAlgebraicSpaces_relativeDiagonal_algebraicStacks B S hS m.outer)) ∧
    -- (k) locally quasi-finite
    (Stack.IsLocallyQuasiFinite B S hS (AlgebraicStacks.relativeDiagonal B S hS m.inner).hom ↔
      Stack.IsLocallyQuasiFinite B S hS
        (AlgebraicStacks.relativeDiagonal B S hS m.outer).hom) ∧
    -- (l) finite
    (HasRelativeProperty.{u, u, u + 1, u} B S hS (Space.finiteMorphismProperty B S hS)
        (AlgebraicStacks.relativeDiagonal B S hS m.inner).hom
        (isRepresentableByAlgebraicSpaces_relativeDiagonal_algebraicStacks B S hS m.inner) ↔
      HasRelativeProperty.{u, u, u + 1, u} B S hS (Space.finiteMorphismProperty B S hS)
        (AlgebraicStacks.relativeDiagonal B S hS m.outer).hom
        (isRepresentableByAlgebraicSpaces_relativeDiagonal_algebraicStacks B S hS m.outer)) ∧
    -- (m) unramified
    (haveI : (Space.unramifiedMorphismProperty B S hS).IsStableUnderBaseChange :=
      Space.isUnramified_isStableUnderBaseChange B S hS
    haveI : (Space.unramifiedMorphismProperty B S hS).IsLocalAtTarget
        (Space.Topology.fppf.precoverage.{u, u} B S hS) :=
      (Space.isUnramified_isLocalAtTarget_fpqc.{u, u} B S hS).of_le
        (Space.fppfPrecoverage_le_fpqcPrecoverage.{u, u} B S hS)
    HasRelativeProperty.{u, u, u + 1, u} B S hS (Space.unramifiedMorphismProperty B S hS)
        (AlgebraicStacks.relativeDiagonal B S hS m.inner).hom
        (isRepresentableByAlgebraicSpaces_relativeDiagonal_algebraicStacks B S hS m.inner) ↔
      HasRelativeProperty.{u, u, u + 1, u} B S hS (Space.unramifiedMorphismProperty B S hS)
        (AlgebraicStacks.relativeDiagonal B S hS m.outer).hom
        (isRepresentableByAlgebraicSpaces_relativeDiagonal_algebraicStacks B S hS m.outer)) ∧
    -- (n) monomorphism
    (HasRelativeProperty.{u, u, u + 1, u} B S hS
        (MorphismProperty.monomorphisms (AlgebraicSpaces B S hS))
        (AlgebraicStacks.relativeDiagonal B S hS m.inner).hom
        (isRepresentableByAlgebraicSpaces_relativeDiagonal_algebraicStacks B S hS m.inner) ↔
      HasRelativeProperty.{u, u, u + 1, u} B S hS
        (MorphismProperty.monomorphisms (AlgebraicSpaces B S hS))
        (AlgebraicStacks.relativeDiagonal B S hS m.outer).hom
        (isRepresentableByAlgebraicSpaces_relativeDiagonal_algebraicStacks B S hS m.outer)) ∧
    -- (o) immersion
    (Stack.IsImmersion B S hS (AlgebraicStacks.relativeDiagonal B S hS m.inner).hom ↔
      Stack.IsImmersion B S hS (AlgebraicStacks.relativeDiagonal B S hS m.outer).hom) ∧
    -- (p) closed immersion
    (Stack.IsClosedImmersion B S hS (AlgebraicStacks.relativeDiagonal B S hS m.inner).hom ↔
      Stack.IsClosedImmersion B S hS (AlgebraicStacks.relativeDiagonal B S hS m.outer).hom) ∧
    -- (q) proper
    (Stack.IsProper B S hS (AlgebraicStacks.relativeDiagonal B S hS m.inner).hom ↔
      Stack.IsProper B S hS (AlgebraicStacks.relativeDiagonal B S hS m.outer).hom)
```

## Tag 0BPW, a lemma

[Tag 0BPW](https://stacks.math.columbia.edu/tag/0BPW) in the Stacks Project.

**`AlgebraicGeometry.Stack.isRepresentableCFG_iff_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningIsScheme.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningIsScheme.lean#L48). The attribute's comment: “clause (2): scheme”.

> If `𝒳 ⊂ 𝒳'` is a thickening of algebraic stacks over `S`, then `𝒳` is a scheme if and only if
> `𝒳'` is a scheme.

```lean
theorem isRepresentableCFG_iff_of_isThickening (i : 𝒳 ⟶ 𝒳') (hi : IsThickening i) :
    Stacks.RepresentableMorphism.IsRepresentableCFG 𝒳.val.val.p ↔
      Stacks.RepresentableMorphism.IsRepresentableCFG 𝒳'.val.val.p
```

**`AlgebraicGeometry.Stack.isDMOver_iff_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningQuasiDMDeligneMumford.lean, line 429](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningQuasiDMDeligneMumford.lean#L429). The attribute's comment: “clause (3): DM over the base”.

> If `𝒳 ⊂ 𝒳'` is a thickening of algebraic stacks over `S`, then `𝒳` is DM over `S` if and only
> if `𝒳'` is DM over `S`.

```lean
theorem isDMOver_iff_isThickening (i : 𝒳 ⟶ 𝒳') (hi : IsThickening i) :
    IsDMOver B S hS 𝒳 ↔ IsDMOver B S hS 𝒳'
```

**`AlgebraicGeometry.Stack.isQuasiDMOver_iff_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningQuasiDMDeligneMumford.lean, line 436](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningQuasiDMDeligneMumford.lean#L436). The attribute's comment: “clause (4): quasi-DM over the base”.

> If `𝒳 ⊂ 𝒳'` is a thickening of algebraic stacks over `S`, then `𝒳` is quasi-DM over `S` if
> and only if `𝒳'` is quasi-DM over `S`.

```lean
theorem isQuasiDMOver_iff_isThickening (i : 𝒳 ⟶ 𝒳') (hi : IsThickening i) :
    IsQuasiDMOver B S hS 𝒳 ↔ IsQuasiDMOver B S hS 𝒳'
```

**`AlgebraicGeometry.Stack.isDMAbs_iff_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningQuasiDMDeligneMumford.lean, line 445](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningQuasiDMDeligneMumford.lean#L445). The attribute's comment: “clause (3): DM, the absolute axiom of Stacks 050D part (5)”.

> If `𝒳 ⊂ 𝒳'` is a thickening of algebraic stacks over `S`, then `𝒳` is Deligne–Mumford if and
> only if `𝒳'` is Deligne–Mumford, in the absolute sense of `AlgebraicGeometry.Stack.IsDMAbs`.

```lean
theorem isDMAbs_iff_isThickening (i : 𝒳 ⟶ 𝒳') (hi : IsThickening i) :
    IsDMAbs.{u, w, w'} B S hS 𝒳 ↔ IsDMAbs.{u, w, w'} B S hS 𝒳'
```

**`AlgebraicGeometry.Stack.isQuasiDMAbs_iff_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningQuasiDMDeligneMumford.lean, line 454](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningQuasiDMDeligneMumford.lean#L454). The attribute's comment: “clause (4): quasi-DM, the absolute axiom of Stacks 050D part (6)”.

> If `𝒳 ⊂ 𝒳'` is a thickening of algebraic stacks over `S`, then `𝒳` is quasi-DM if and only
> if `𝒳'` is quasi-DM, in the absolute sense of `AlgebraicGeometry.Stack.IsQuasiDMAbs`.

```lean
theorem isQuasiDMAbs_iff_isThickening (i : 𝒳 ⟶ 𝒳') (hi : IsThickening i) :
    IsQuasiDMAbs.{u, w, w'} B S hS 𝒳 ↔ IsQuasiDMAbs.{u, w, w'} B S hS 𝒳'
```

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpace_iff_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningQuasiDMDeligneMumford.lean, line 463](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningQuasiDMDeligneMumford.lean#L463). The attribute's comment: “clause (1): algebraic space, the whole equivalence”.

> If `𝒳 ⊂ 𝒳'` is a thickening of algebraic stacks over `S`, then `𝒳` is an algebraic space if
> and only if `𝒳'` is an algebraic space.

```lean
theorem isRepresentableByAlgebraicSpace_iff_isThickening (i : 𝒳 ⟶ 𝒳')
    (hi : IsThickening i) :
    IsRepresentableByAlgebraicSpace B S hS 𝒳.val ↔
      IsRepresentableByAlgebraicSpace B S hS 𝒳'.val
```

**`AlgebraicGeometry.Stack.isSeparatedAbs_iff_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningSeparationAbsolute.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningSeparationAbsolute.lean#L122). The attribute's comment: “clause (5): separated, the absolute axiom of Stacks 050D part (7)”.

> **Stacks 0BPW, clause (5).** If `𝒳 ⊂ 𝒳'` is a thickening of algebraic stacks over `S` then
> `𝒳` is separated if and only if `𝒳'` is — the absolute axiom, part (7) of **Stacks 050D**.
>
> Both sides are separatedness over `Spec(ℤ)` of the stacks viewed by **Stacks 04X6**, and the
> thickening viewed over `Spec(ℤ)` is a thickening
> (`AlgebraicGeometry.Stack.isThickening_changeBaseHomAlgebraicStacks`), so this is
> `AlgebraicGeometry.Stack.isSeparatedOver_iff_isThickening` at the base `Spec(ℤ)`.

```lean
theorem isSeparatedAbs_iff_isThickening (i : 𝒳 ⟶ 𝒳') (hi : IsThickening i) :
    IsSeparatedAbs.{u, w, w'} B S hS 𝒳 ↔ IsSeparatedAbs.{u, w, w'} B S hS 𝒳'
```

**`AlgebraicGeometry.Stack.isQuasiSeparatedAbs_iff_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningSeparationAbsolute.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningSeparationAbsolute.lean#L136). The attribute's comment: “clause (6): quasi-separated, the absolute axiom of Stacks 050D part (8)”.

> **Stacks 0BPW, clause (6).** If `𝒳 ⊂ 𝒳'` is a thickening of algebraic stacks over `S` then
> `𝒳` is quasi-separated if and only if `𝒳'` is — the absolute axiom, part (8) of
> **Stacks 050D**.
>
> The companion of `AlgebraicGeometry.Stack.isSeparatedAbs_iff_isThickening` at
> `AlgebraicGeometry.Stack.isQuasiSeparatedOver_iff_isThickening`.

```lean
theorem isQuasiSeparatedAbs_iff_isThickening (i : 𝒳 ⟶ 𝒳') (hi : IsThickening i) :
    IsQuasiSeparatedAbs.{u, w, w'} B S hS 𝒳 ↔ IsQuasiSeparatedAbs.{u, w, w'} B S hS 𝒳'
```

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpace_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningSeparationAxioms.lean, line 471](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningSeparationAxioms.lean#L471). The attribute's comment: “clause (1): algebraic space -- only part of the clause, namely the implication from the ambient stack to the closed substack; the whole equivalence is AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpace\_iff\_isThickening”.

> **Stacks 0BPW, clause (1), from the ambient stack to the closed substack.** If `𝒳 ⊂ 𝒳'` is a
> thickening of algebraic stacks over `S` and `𝒳'` is an algebraic space, then so is `𝒳`.
>
> The thickening `i` is a closed immersion, hence representable by algebraic spaces, and `𝒳` is the
> apex of the degenerate 2-fibre product `𝒳' ×_{𝒳'} 𝒳` of
> `CategoryTheory.Bicategory.TwoCommSq.idCospan`; so **Stacks 04ZP**, the implication (1) ⟹ (2)
> (`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpace_of_isTwoFibreProduct`), applies. Only
> the closed-immersion half of `AlgebraicGeometry.Stack.IsThickening` is used.

```lean
theorem isRepresentableByAlgebraicSpace_of_isThickening (i : 𝒳 ⟶ 𝒳') (hi : IsThickening i)
    (h : IsRepresentableByAlgebraicSpace B S hS 𝒳'.val) :
    IsRepresentableByAlgebraicSpace B S hS 𝒳.val
```

**`AlgebraicGeometry.Stack.isDMOver_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningSeparationAxioms.lean, line 495](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningSeparationAxioms.lean#L495). The attribute's comment: “clause (3): DM over the base -- only part of the clause, namely the implication from the ambient stack to the closed substack; the whole equivalence is AlgebraicGeometry.Stack.isDMOver\_iff\_isThickening”.

> **One half of Stacks 0BPW, clause (3).** If `𝒳 ⊂ 𝒳'` is a thickening of algebraic stacks
> over `S` and `𝒳'` is DM over `S`, then so is `𝒳`.
>
> The thickening is read as a morphism of thickenings over the base
> (`AlgebraicGeometry.Stack.structureThickeningMorphism`) and
> `AlgebraicGeometry.Stack.isDM_inner_of_outer` applies to it. The separation axiom is part (1) of
> **Stacks 050D**, DM over the base scheme of the site; see the implementation notes of this file
> for why the statement is not at the absolute form, part (5).
>
> Untagged: the clause itself is the equivalence
> `AlgebraicGeometry.Stack.isDMOver_iff_isThickening` in
> `StacksFrontier.AlgebraicGeometry.Stacks.ThickeningQuasiDMDeligneMumford`, which is item (9) of
> **Stacks 0CJ9** at the same viewing and carries the part key.

```lean
theorem isDMOver_of_isThickening (i : 𝒳 ⟶ 𝒳') (hi : IsThickening i)
    (h : IsDMOver B S hS 𝒳') : IsDMOver B S hS 𝒳
```

**`AlgebraicGeometry.Stack.isQuasiDMOver_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningSeparationAxioms.lean, line 510](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningSeparationAxioms.lean#L510). The attribute's comment: “clause (4): quasi-DM over the base -- only part of the clause, namely the implication from the ambient stack to the closed substack; the whole equivalence is AlgebraicGeometry.Stack.isQuasiDMOver\_iff\_isThickening”.

> **One half of Stacks 0BPW, clause (4).** If `𝒳 ⊂ 𝒳'` is a thickening of algebraic stacks
> over `S` and `𝒳'` is quasi-DM over `S`, then so is `𝒳`. The companion of
> `AlgebraicGeometry.Stack.isDMOver_of_isThickening` at part (2) of **Stacks 050D**.
>
> Untagged: the clause itself is the equivalence
> `AlgebraicGeometry.Stack.isQuasiDMOver_iff_isThickening` in
> `StacksFrontier.AlgebraicGeometry.Stacks.ThickeningQuasiDMDeligneMumford`, which is item (8) of
> **Stacks 0CJ9** at the same viewing and carries the part key.

```lean
theorem isQuasiDMOver_of_isThickening (i : 𝒳 ⟶ 𝒳') (hi : IsThickening i)
    (h : IsQuasiDMOver B S hS 𝒳') : IsQuasiDMOver B S hS 𝒳
```

**`AlgebraicGeometry.Stack.isSeparatedOver_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningSeparationAxioms.lean, line 525](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningSeparationAxioms.lean#L525). The attribute's comment: “clause (5): separated over the base -- only part of the clause, namely the implication from the ambient stack to the closed substack; the whole equivalence is AlgebraicGeometry.Stack.isSeparatedOver\_iff\_isThickening”.

> **One half of Stacks 0BPW, clause (5).** If `𝒳 ⊂ 𝒳'` is a thickening of algebraic stacks over
> `S` and `𝒳'` is separated over `S`, then so is `𝒳`. The companion of
> `AlgebraicGeometry.Stack.isDMOver_of_isThickening` at part (3) of **Stacks 050D**.
>
> Untagged: the clause itself is the equivalence
> `AlgebraicGeometry.Stack.isSeparatedOver_iff_isThickening` in
> `StacksFrontier.AlgebraicGeometry.Stacks.ThickeningSeparationConverse`, which is built from this
> implication and its converse and carries the part key.

```lean
theorem isSeparatedOver_of_isThickening (i : 𝒳 ⟶ 𝒳') (hi : IsThickening i)
    (h : IsSeparatedOver B S hS 𝒳') : IsSeparatedOver B S hS 𝒳
```

**`AlgebraicGeometry.Stack.isQuasiSeparatedOver_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningSeparationAxioms.lean, line 540](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningSeparationAxioms.lean#L540). The attribute's comment: “clause (6): quasi-separated over the base -- only part of the clause, namely the implication from the ambient stack to the closed substack; the whole equivalence is AlgebraicGeometry.Stack.isQuasiSeparatedOver\_iff\_isThickening”.

> **One half of Stacks 0BPW, clause (6).** If `𝒳 ⊂ 𝒳'` is a thickening of algebraic stacks over
> `S` and `𝒳'` is quasi-separated over `S`, then so is `𝒳`. The companion of
> `AlgebraicGeometry.Stack.isDMOver_of_isThickening` at part (4) of **Stacks 050D**.
>
> Untagged: the clause itself is the equivalence
> `AlgebraicGeometry.Stack.isQuasiSeparatedOver_iff_isThickening` in
> `StacksFrontier.AlgebraicGeometry.Stacks.ThickeningSeparationConverse`, which is built from this
> implication and its converse and carries the part key.

```lean
theorem isQuasiSeparatedOver_of_isThickening (i : 𝒳 ⟶ 𝒳') (hi : IsThickening i)
    (h : IsQuasiSeparatedOver B S hS 𝒳') : IsQuasiSeparatedOver B S hS 𝒳
```

**`AlgebraicGeometry.Stack.isQuasiSeparatedOver_iff_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningSeparationConverse.lean, line 424](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningSeparationConverse.lean#L424). The attribute's comment: “clause (6): quasi-separated over the base”.

> If `𝒳 ⊂ 𝒳'` is a thickening of algebraic stacks over `S` then `𝒳` is quasi-separated over `S`
> if and only if `𝒳'` is. Here quasi-separatedness over `S` is part (4) of **Stacks 050D**.

```lean
theorem isQuasiSeparatedOver_iff_isThickening (i : 𝒳 ⟶ 𝒳') (hi : IsThickening i) :
    IsQuasiSeparatedOver B S hS 𝒳 ↔ IsQuasiSeparatedOver B S hS 𝒳'
```

**`AlgebraicGeometry.Stack.isSeparatedOver_iff_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningSeparationConverse.lean, line 432](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningSeparationConverse.lean#L432). The attribute's comment: “clause (5): separated over the base”.

> If `𝒳 ⊂ 𝒳'` is a thickening of algebraic stacks over `S` then `𝒳` is separated over `S` if and
> only if `𝒳'` is. Here separatedness over `S` is part (3) of **Stacks 050D**.

```lean
theorem isSeparatedOver_iff_isThickening (i : 𝒳 ⟶ 𝒳') (hi : IsThickening i) :
    IsSeparatedOver B S hS 𝒳 ↔ IsSeparatedOver B S hS 𝒳'
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 106.3, Tag 0BPN](https://stacks.math.columbia.edu/tag/0BPN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
