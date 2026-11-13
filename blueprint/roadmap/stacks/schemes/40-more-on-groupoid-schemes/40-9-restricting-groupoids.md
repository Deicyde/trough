---
declaration: section
origin: cited
lean: AlgebraicGeometry.GroupoidScheme.restrict, AlgebraicGeometry.restrictionSource_locallyOfFiniteType, AlgebraicGeometry.restrictionTarget_locallyOfFiniteType, AlgebraicGeometry.restrictionSource_locallyOfFinitePresentation, AlgebraicGeometry.restrictionTarget_locallyOfFinitePresentation, AlgebraicGeometry.restrictionSource_flat, AlgebraicGeometry.restrictionTarget_flat, AlgebraicGeometry.restriction_source_mem
statement: formalized
proof: formalized
---

# 40.9 Restricting groupoids

Section 40.9 of the Stacks Project, [Tag 04MM](https://stacks.math.columbia.edu/tag/04MM). 5 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04MN, an equation

[Tag 04MN](https://stacks.math.columbia.edu/tag/04MN) in the Stacks Project.

**`AlgebraicGeometry.GroupoidScheme.restrict`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/RestrictionGroupoid.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/RestrictionGroupoid.lean#L69). The attribute's comment: “R' is the iterated fibre product of the displayed diagram and s', t' are its”.

> Restriction of a groupoid scheme along a morphism to its scheme of objects.

```lean
noncomputable def restrict {S : Scheme.{u}} (G : Stacks.Groupoids.GroupoidScheme S)
    {U' : Over S} (g : U' ⟶ G.objects) : Restriction G g
```

## Tag 04MP, a lemma

[Tag 04MP](https://stacks.math.columbia.edu/tag/04MP) in the Stacks Project.

**`AlgebraicGeometry.restrictionSource_locallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/RestrictionProperties.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/More/RestrictionProperties.lean#L173). The attribute's comment: “part (1), source map”.

> The source map of a restriction is locally of finite type if the original source map
> and the restricting morphism are locally of finite type.

```lean
public theorem restrictionSource_locallyOfFiniteType {S : Scheme.{u}}
    (G : GroupoidScheme S) {U' : Scheme.{u}} (g : U' ⟶ G.objects.left)
    [LocallyOfFiniteType G.source.left] [LocallyOfFiniteType g] :
    let U'_S : Over S := Over.mk (g ≫ G.objects.hom)
    let g' : U'_S ⟶ G.objects := Over.homMk g
    LocallyOfFiniteType (GroupoidScheme.restrict G g').groupoid.source.left
```

**`AlgebraicGeometry.restrictionTarget_locallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/RestrictionProperties.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/More/RestrictionProperties.lean#L185). The attribute's comment: “part (1), target map”.

> The target map of a restriction is locally of finite type if the original target map
> and the restricting morphism are locally of finite type.

```lean
public theorem restrictionTarget_locallyOfFiniteType {S : Scheme.{u}}
    (G : GroupoidScheme S) {U' : Scheme.{u}} (g : U' ⟶ G.objects.left)
    [LocallyOfFiniteType G.target.left] [LocallyOfFiniteType g] :
    let U'_S : Over S := Over.mk (g ≫ G.objects.hom)
    let g' : U'_S ⟶ G.objects := Over.homMk g
    LocallyOfFiniteType (GroupoidScheme.restrict G g').groupoid.target.left
```

**`AlgebraicGeometry.restrictionSource_locallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/RestrictionProperties.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/More/RestrictionProperties.lean#L197). The attribute's comment: “part (2), source map”.

> The source map of a restriction is locally of finite presentation if the original source map
> and the restricting morphism are locally of finite presentation.

```lean
public theorem restrictionSource_locallyOfFinitePresentation {S : Scheme.{u}}
    (G : GroupoidScheme S) {U' : Scheme.{u}} (g : U' ⟶ G.objects.left)
    [LocallyOfFinitePresentation G.source.left] [LocallyOfFinitePresentation g] :
    let U'_S : Over S := Over.mk (g ≫ G.objects.hom)
    let g' : U'_S ⟶ G.objects := Over.homMk g
    LocallyOfFinitePresentation
      (GroupoidScheme.restrict G g').groupoid.source.left
```

**`AlgebraicGeometry.restrictionTarget_locallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/RestrictionProperties.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/More/RestrictionProperties.lean#L210). The attribute's comment: “part (2), target map”.

> The target map of a restriction is locally of finite presentation if the original target map
> and the restricting morphism are locally of finite presentation.

```lean
public theorem restrictionTarget_locallyOfFinitePresentation {S : Scheme.{u}}
    (G : GroupoidScheme S) {U' : Scheme.{u}} (g : U' ⟶ G.objects.left)
    [LocallyOfFinitePresentation G.target.left] [LocallyOfFinitePresentation g] :
    let U'_S : Over S := Over.mk (g ≫ G.objects.hom)
    let g' : U'_S ⟶ G.objects := Over.homMk g
    LocallyOfFinitePresentation
      (GroupoidScheme.restrict G g').groupoid.target.left
```

**`AlgebraicGeometry.restrictionSource_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/RestrictionProperties.lean, line 223](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/More/RestrictionProperties.lean#L223). The attribute's comment: “part (3), source map”.

> The source map of a restriction is flat if the original source map and the restricting
> morphism are flat.

```lean
public theorem restrictionSource_flat {S : Scheme.{u}} (G : GroupoidScheme S)
    {U' : Scheme.{u}} (g : U' ⟶ G.objects.left) [Flat G.source.left] [Flat g] :
    let U'_S : Over S := Over.mk (g ≫ G.objects.hom)
    let g' : U'_S ⟶ G.objects := Over.homMk g
    Flat (GroupoidScheme.restrict G g').groupoid.source.left
```

**`AlgebraicGeometry.restrictionTarget_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/RestrictionProperties.lean, line 234](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/More/RestrictionProperties.lean#L234). The attribute's comment: “part (3), target map”.

> The target map of a restriction is flat if the original target map and the restricting
> morphism are flat.

```lean
public theorem restrictionTarget_flat {S : Scheme.{u}} (G : GroupoidScheme S)
    {U' : Scheme.{u}} (g : U' ⟶ G.objects.left) [Flat G.target.left] [Flat g] :
    let U'_S : Over S := Over.mk (g ≫ G.objects.hom)
    let g' : U'_S ⟶ G.objects := Over.homMk g
    Flat (GroupoidScheme.restrict G g').groupoid.target.left
```

## Tag 04MV, a lemma

[Tag 04MV](https://stacks.math.columbia.edu/tag/04MV) in the Stacks Project.

**`AlgebraicGeometry.restriction_source_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/RestrictionProperties.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/More/RestrictionProperties.lean#L149). The attribute's comment: “source map”.

> The source map of a restriction has every morphism property which is stable under base
> change and holds for the source map after pulling back the target.

```lean
public theorem restriction_source_mem {S : Scheme.{u}} (G : GroupoidScheme S) {U' : Over S}
    (g : U' ⟶ G.objects) (R : GroupoidScheme.Restriction G g)
    (P : MorphismProperty Scheme) [P.IsStableUnderBaseChange]
    (hP : P ((pullback.snd g G.target ≫ G.source).left)) :
    P R.groupoid.source.left
```

**`AlgebraicGeometry.restriction_target_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/RestrictionProperties.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/More/RestrictionProperties.lean#L159). The attribute's comment: “target map”.

> The target map of a restriction has every morphism property which is stable under base
> change and holds for the source map after pulling back the target.

```lean
public theorem restriction_target_mem {S : Scheme.{u}} (G : GroupoidScheme S) {U' : Over S}
    (g : U' ⟶ G.objects) (R : GroupoidScheme.Restriction G g)
    (P : MorphismProperty Scheme) [P.IsStableUnderBaseChange]
    (hP : P ((pullback.snd g G.target ≫ G.source).left)) :
    P R.groupoid.target.left
```

## Tag 04MW, a lemma

[Tag 04MW](https://stacks.math.columbia.edu/tag/04MW) in the Stacks Project.

**`AlgebraicGeometry.doubleRestrictionDiagram`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/DoubleRestriction.lean, line 326](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/More/DoubleRestriction.lean#L326).

> **Stacks Project, Tag 04MW.** Restricting a groupoid scheme successively
> along `g` and `g'` gives a comparison diagram whose two squares are cartesian;
> the comparison arrow is given by composing the second arrow with the inverse of
> the first.

```lean
public noncomputable def doubleRestrictionDiagram {S : Scheme.{u}} (G : GroupoidScheme S)
    {U' U'' : Over S} (g : U' ⟶ G.objects) (g' : U'' ⟶ U') :
    DoubleRestrictionDiagram G g g'
```

## Tag 04MX, a lemma

[Tag 04MX](https://stacks.math.columbia.edu/tag/04MX) in the Stacks Project.

**`AlgebraicGeometry.restrictionSource_mem_of_composite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/DoubleRestrictionDescent.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/More/DoubleRestrictionDescent.lean#L64). The attribute's comment: “pullback\_to\_second\_restriction”.

> A property of the source map over a composite restriction descends to the
> source map over the second restriction when the original target map covers.

```lean
public theorem restrictionSource_mem_of_composite {S : Scheme.{u}} (G : GroupoidScheme S)
    {U' U'' : Over S} (g : U' ⟶ G.objects) (g' : U'' ⟶ U')
    (K : Precoverage Scheme.{u}) [K.IsStableUnderBaseChange]
    (P : MorphismProperty Scheme.{u}) [P.IsStableUnderBaseChange]
    [P.IsLocalAtTarget K]
    (ht : Presieve.singleton G.target.left ∈ K G.objects.left)
    (hP : P ((pullback.snd (g' ≫ g) G.target ≫ G.source).left)) :
    P ((pullback.snd g' (restrictionTarget G g) ≫ restrictionSource G g).left)
```

**`AlgebraicGeometry.descent_to_open_image`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/DoubleRestrictionDescent.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/More/DoubleRestrictionDescent.lean#L99). The attribute's comment: “descent\_to\_open\_image”.

> A morphism property local on the target descends from the source map of a
> restriction to the source map after a further restriction, viewed over the
> open image of the first source map.

```lean
public theorem descent_to_open_image {S : Scheme.{u}} (G : GroupoidScheme S)
    {U' U'' : Over S} (g : U' ⟶ G.objects) (g' : U'' ⟶ U')
    (K : Precoverage Scheme.{u}) (P : MorphismProperty Scheme.{u})
    [P.IsStableUnderBaseChange] [P.IsLocalAtTarget K]
    (V : G.objects.left.Opens)
    (hV : (firstArrowSource G g).left ⟶ V.toScheme)
    (hV_fac : hV ≫ V.ι = (firstSourceMap G g).left)
    (_hV_range : Set.range (firstSourceMap G g).left = (V : Set G.objects.left))
    (hV_cover : Presieve.singleton hV ∈ K V.toScheme)
    (hP : P (secondSourceMap G g g').left) :
    ∃ hV' : (compositeArrowSource G g g').left ⟶ V.toScheme,
      hV' ≫ V.ι = (compositeSourceMap G g g').left ∧ P hV'
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 40.9, Tag 04MM](https://stacks.math.columbia.edu/tag/04MM)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
