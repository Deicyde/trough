---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.Descent.essSurj_fibreDescentFunctor, AlgebraicGeometry.Space.Descent.fibreDescentFunctorEquivalence, AlgebraicGeometry.Space.Descent.isPullback_fibreDescentData_obj, AlgebraicGeometry.Space.Descent.fibreDescentFunctor, AlgebraicGeometry.Space.Descent.fibreDescentFunctorFullyFaithful, AlgebraicGeometry.Space.Descent.isAlgebraicSpace_iff_isEffective_fibreDescentData, AlgebraicGeometry.Space.Descent.fppfDescentDataSheafEquivalence, AlgebraicGeometry.Space.Descent.descendedFibreComponentIso
statement: formalized
proof: formalized
---

# 74.23 Descent data in terms of sheaves

Section 74.23 of the Stacks Project, [Tag 0ADS](https://stacks.math.columbia.edu/tag/0ADS). 1 tag here is carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0ADT, a lemma

[Tag 0ADT](https://stacks.math.columbia.edu/tag/0ADT) in the Stacks Project.

**`AlgebraicGeometry.Space.Descent.essSurj_fibreDescentFunctor`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/DescentDataQuotient.lean, line 621](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/DescentDataQuotient.lean#L621). The attribute's comment: “ESSENTIAL SURJECTIVITY of fibreDescentFunctor, i.e. the LEFT-TO-RIGHT FUNCTOR of the asserted equivalence on objects: every descent datum is the descent datum of a sheaf over T whose fibre products with the family are the components of the datum, namely of descentQuotient, the fppf sheafification of the presheaf of orbits of local lifts of the datum. That presheaf is the object the source builds as the coequalizer of the two maps from the pairwise overlaps V i x\_T X j to the disjoint union of the components V i; the two maps are equalized by toDescentQuotient\_move and the components are recovered by isPullback\_toDescentQuotient. The coequalizer UNIVERSAL PROPERTY is not stated here. Proved WITHOUT Stacks 0ADV and without the fppf covering hypothesis -- only that the target and the members of the family are algebraic spaces. The equivalence of categories, which needs full faithfulness as well, is fibreDescentFunctorEquivalence”.

> **Stacks 0ADT, essential surjectivity.** Every descent datum relative to a family of
> morphisms of algebraic spaces is the descent datum of a sheaf over the target whose fibre
> products with the members of the family are algebraic spaces, namely of the quotient sheaf
> `AlgebraicGeometry.Space.Descent.descentQuotient` of the datum.

```lean
public instance essSurj_fibreDescentFunctor : (fibreDescentFunctor f hT hX).EssSurj
```

**`AlgebraicGeometry.Space.Descent.fibreDescentFunctorEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/DescentDataQuotient.lean, line 649](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/DescentDataQuotient.lean#L649). The attribute's comment: “THE EQUIVALENCE OF CATEGORIES ASSERTED BY THE TAG, in full, for an fppf covering of algebraic spaces: sheaves over the target whose fibre products with the covering are algebraic spaces are equivalent to descent data relative to the covering. The functor is fibreDescentFunctor; full faithfulness is fibreDescentFunctorFullyFaithful and essential surjectivity is essSurj\_fibreDescentFunctor, which sends a datum to descentQuotient. Stacks 0ADV is neither used nor needed”.

> **Stacks 0ADT, the equivalence of categories.** For an fppf covering `{X i ⟶ T}` of
> algebraic spaces, sheaves over `T` whose fibre products with the covering are algebraic spaces
> are equivalent to descent data relative to the covering, by
> `AlgebraicGeometry.Space.Descent.fibreDescentFunctor`.

```lean
public def fibreDescentFunctorEquivalence (hcov : Space.IsFppfCovering B S hS X f) :
    SheavesWithSpaceFibres f ≌ DescentData f hT hX
```

**`AlgebraicGeometry.Space.Descent.isPullback_fibreDescentData_obj`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/DescentDataSheaves.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/DescentDataSheaves.lean#L264). The attribute's comment: “part (1) only: the component of the descent datum at i is the fibre product X i ×\_T F. Not the equivalence of categories, and not part (2)”.

> The component of the descent datum at `i` sits in the fibre product square for
> `X i ×_T F`: its structure map to `X i` and its projection to `F` are a fibre product of
> `f i` and the structure map of `F`.

```lean
public lemma isPullback_fibreDescentData_obj (F : SheavesWithSpaceFibres f) (i : ι) :
    IsPullback ((fibreDescentData f hT hX F).obj i).hom (pullback.fst F.obj.hom (f i)) (f i)
      F.obj.hom
```

**`AlgebraicGeometry.Space.Descent.fibreDescentFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/DescentDataSheaves.lean, line 300](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/DescentDataSheaves.lean#L300). The attribute's comment: “ONE FUNCTOR of the asserted equivalence, right to left: from sheaves over T whose fibre products with the family are algebraic spaces, to descent data. The cocycle condition is proved, not assumed. This declaration is that functor ALONE -- it asserts neither the equivalence nor part (2). Both are proved of this same functor elsewhere, in StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/DescentDataSheavesEquivalence.lean and DescentDataQuotient.lean: full faithfulness is fibreDescentFunctorFullyFaithful, essential surjectivity -- the left-to-right coequalizer direction, realized by the quotient sheaf descentQuotient -- is the instance essSurj\_fibreDescentFunctor, the equivalence of categories itself is fibreDescentFunctorEquivalence, and part (2) is isAlgebraicSpace\_iff\_isEffective\_fibreDescentData. The source's two natural isomorphisms are not built by hand: the equivalence is assembled from the two halves above”.

> The functor from sheaves over `T` whose fibre products with the members of the family are
> algebraic spaces to descent data relative to the family.

```lean
public def fibreDescentFunctor : SheavesWithSpaceFibres f ⥤ DescentData f hT hX
```

**`AlgebraicGeometry.Space.Descent.fibreDescentFunctorFullyFaithful`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/DescentDataSheavesEquivalence.lean, line 435](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/DescentDataSheavesEquivalence.lean#L435). The attribute's comment: “FULL FAITHFULNESS of the right-to-left functor of the asserted equivalence, for an fppf covering of algebraic spaces. The other half, essential surjectivity via the coequalizer, is NOT proved, so the equivalence is not claimed”.

> **Stacks 0ADT**, half of the asserted equivalence: for an fppf covering of algebraic
> spaces, the functor from sheaves over the target whose fibre products with the covering are
> algebraic spaces to descent data relative to the covering is fully faithful.

```lean
public def fibreDescentFunctorFullyFaithful (hcov : Space.IsFppfCovering B S hS X f) :
    (fibreDescentFunctor f hT hX).FullyFaithful
```

**`AlgebraicGeometry.Space.Descent.isAlgebraicSpace_iff_isEffective_fibreDescentData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/DescentDataSheavesEquivalence.lean, line 582](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/DescentDataSheavesEquivalence.lean#L582). The attribute's comment: “PART (2) IN FULL: the sheaf F is an algebraic space if and only if the corresponding descent datum is effective, against this library's DescentData.IsEffective. Proved WITHOUT Stacks 0ADV -- effectivity hands over an algebraic space and full faithfulness transports the isomorphism back. The equivalence of categories itself is NOT here: essential surjectivity, i.e. the left-to-right coequalizer functor, is unproved”.

> **Stacks 0ADT, part (2).** For an fppf covering of algebraic spaces, a sheaf over the
> target whose fibre products with the covering are algebraic spaces is itself an algebraic
> space exactly when its descent datum is effective.

```lean
public theorem isAlgebraicSpace_iff_isEffective_fibreDescentData
    (hcov : Space.IsFppfCovering B S hS X f) (F : SheavesWithSpaceFibres f) :
    IsAlgebraicSpace B S hS F.obj.left ↔
      DescentData.IsEffective (fibreDescentData f hT hX F)
```

**`AlgebraicGeometry.Space.Descent.fppfDescentDataSheafEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/DescentDataSheavesEssSurj.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/DescentDataSheavesEssSurj.lean#L222). The attribute's comment: “THE EQUIVALENCE OF CATEGORIES, for an fppf covering of algebraic spaces: descent data relative to the covering are the sheaves over the target whose fibre products with the covering are algebraic spaces. Full faithfulness is fibreDescentFunctorFullyFaithful, essential surjectivity is fibreDescentFunctor\_essSurj, which glues the members of the datum as the source's coequalizer and sheafifies”.

> **Stacks 0ADT.** For an fppf covering of algebraic spaces `{X i ⟶ T}`, the sheaves on the
> big fppf site endowed with a map to `T` whose fibre products `X i ×_T F` are all algebraic
> spaces are equivalent to the descent data relative to the covering. The functor takes a sheaf
> to the descent datum formed by those fibre products.

```lean
public def fppfDescentDataSheafEquivalence :
    SheavesWithSpaceFibres f ≌
      DescentData f hcov.target_isAlgebraicSpace hcov.source_isAlgebraicSpace
```

**`AlgebraicGeometry.Space.Descent.descendedFibreComponentIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/DescentDataSheavesEssSurj.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/DescentDataSheavesEssSurj.lean#L250). The attribute's comment: “PART (1): the algebraic space X i ×\_X F on the sheaf side of the equivalence is the member V i on the descent-datum side, as an object over X i”.

> **Stacks 0ADT, part (1).** Under the equivalence, the fibre product of the sheaf a descent
> datum corresponds to with the `i`-th member of the covering is the `i`-th member of the
> descent datum, as a space over that member of the covering.

```lean
public def descendedFibreComponentIso (i : ι) :
    fibreComponent f ((fppfDescentDataSheafEquivalence f hcov).inverse.obj D).obj i ≅
      D.obj i
```

**`AlgebraicGeometry.Space.Descent.isPullback_descentInclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/DescentDataSheavesEssSurj.lean, line 272](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/DescentDataSheavesEssSurj.lean#L272). The attribute's comment: “PART (1) in pullback form: V i, with its structure map to X i and its canonical map into the descended sheaf F, is the fibre product X i ×\_X F”.

> **Stacks 0ADT, part (1)** in pullback form: the `i`-th member of a descent datum, with its
> structure map to `X i` and its canonical map to the sheaf the datum descends to, is the fibre
> product of that sheaf with `X i`.

```lean
public theorem isPullback_descentInclusion (i : ι) :
    IsPullback (descentInclusion f hcov D i) (D.obj i).hom
      ((fppfDescentDataSheafEquivalence f hcov).inverse.obj D).obj.hom (f i)
```

**`AlgebraicGeometry.Space.Descent.isAlgebraicSpace_inverse_iff_isEffective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/DescentDataSheavesEssSurj.lean, line 288](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/DescentDataSheavesEssSurj.lean#L288). The attribute's comment: “PART (2) on the descent-datum side: the sheaf F corresponding to a descent datum is an algebraic space if and only if that datum is effective”.

> **Stacks 0ADT, part (2)** read on the descent-datum side: the sheaf a descent datum
> descends to is an algebraic space exactly when the descent datum is effective.

```lean
public theorem isAlgebraicSpace_inverse_iff_isEffective :
    IsAlgebraicSpace B S hS
        ((fppfDescentDataSheafEquivalence f hcov).inverse.obj D).obj.left ↔
      DescentData.IsEffective D
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 74.23, Tag 0ADS](https://stacks.math.columbia.edu/tag/0ADS)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
