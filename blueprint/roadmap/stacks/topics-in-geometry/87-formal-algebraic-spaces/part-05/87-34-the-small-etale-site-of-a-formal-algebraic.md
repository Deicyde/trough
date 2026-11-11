---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.Reduction.SmallEtale, AlgebraicGeometry.FormalSpace.Reduction.smallEtaleTopology, AlgebraicGeometry.FormalSpace.Reduction.SpacesEtale, AlgebraicGeometry.FormalSpace.Reduction.spacesEtaleTopology, AlgebraicGeometry.FormalSpace.Reduction.AffineEtale, AlgebraicGeometry.FormalSpace.Reduction.affineEtaleTopology, AlgebraicGeometry.FormalSpace.canonicalSmallEtale, AlgebraicGeometry.FormalSpace.canonicalSmallEtaleTopology
statement: formalized
proof: formalized
---

# 87.34 The small étale site of a formal algebraic space

Section 87.34 of the Stacks Project, [Tag 0DE9](https://stacks.math.columbia.edu/tag/0DE9). 8 tags here are carried by 75 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DEA, a definition

[Tag 0DEA](https://stacks.math.columbia.edu/tag/0DEA) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.Reduction.SmallEtale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSite.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSite.lean#L224). The attribute's comment: “(1) the small étale site, as a category; read against a given reduction, which Stacks 0AIN supplies”.

> The *small étale site* `X_étale` of a formal algebraic space `X`
> with reduction `X_red`, as a category: the small étale site `X_{red, étale}` of the reduction,
> in the sense of Stacks 03ED, whose objects are the étale scheme charts of `X_red`.

```lean
abbrev SmallEtale (R : Reduction B S hS X)
```

**`AlgebraicGeometry.FormalSpace.Reduction.smallEtaleTopology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSite.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSite.lean#L230). The attribute's comment: “(1) the topology of the small étale site; read against a given reduction, which Stacks 0AIN supplies”.

> The topology of the small étale site of `X`: that of
> `X_{red, étale}`.

```lean
abbrev smallEtaleTopology (R : Reduction B S hS X) : GrothendieckTopology R.SmallEtale
```

**`AlgebraicGeometry.FormalSpace.Reduction.SpacesEtale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSite.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSite.lean#L239). The attribute's comment: “(2) the spaces-étale site, as a category; read against a given reduction, which Stacks 0AIN supplies”.

> The site `X_{spaces, étale}` of a formal algebraic space `X`
> with reduction `X_red`, as a category: the spaces-étale site `X_{red, spaces, étale}` of the
> reduction, in the sense of Stacks 03G0, whose objects are the algebraic spaces étale over
> `X_red`.

```lean
abbrev SpacesEtale (R : Reduction B S hS X)
```

**`AlgebraicGeometry.FormalSpace.Reduction.spacesEtaleTopology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSite.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSite.lean#L245). The attribute's comment: “(2) the topology of the spaces-étale site; read against a given reduction, which Stacks 0AIN supplies”.

> The topology of `X_{spaces, étale}`: that of
> `X_{red, spaces, étale}`.

```lean
abbrev spacesEtaleTopology (R : Reduction B S hS X) : GrothendieckTopology R.SpacesEtale
```

**`AlgebraicGeometry.FormalSpace.Reduction.AffineEtale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSite.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSite.lean#L253). The attribute's comment: “(3) the affine étale site, as a category; read against a given reduction, which Stacks 0AIN supplies”.

> The site `X_{affine, étale}` of a formal algebraic space `X`
> with reduction `X_red`, as a category: the affine étale site `X_{red, affine, étale}` of the
> reduction, whose objects are the étale charts of `X_red` with affine source.

```lean
abbrev AffineEtale (R : Reduction B S hS X)
```

**`AlgebraicGeometry.FormalSpace.Reduction.affineEtaleTopology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSite.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSite.lean#L259). The attribute's comment: “(3) the topology of the affine étale site; read against a given reduction, which Stacks 0AIN supplies”.

> The topology of `X_{affine, étale}`: that of
> `X_{red, affine, étale}`.

```lean
abbrev affineEtaleTopology (R : Reduction B S hS X) : GrothendieckTopology R.AffineEtale
```

**`AlgebraicGeometry.FormalSpace.canonicalSmallEtale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonical.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonical.lean#L158). The attribute's comment: “(1) the small étale site, as a category”.

> **Stacks 0DEA, part (1).** The *small étale site* `X_étale` of a formal algebraic space `X`
> over `S`, as a category: the small étale site `X_{red, étale}` of its reduction, in the sense of
> Stacks 03ED, whose objects are the étale scheme charts of `X_red`.

```lean
abbrev canonicalSmallEtale (hX : IsFormalAlgebraicSpace B S hS X)
```

**`AlgebraicGeometry.FormalSpace.canonicalSmallEtaleTopology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonical.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonical.lean#L164). The attribute's comment: “(1) the topology of the small étale site”.

> **Stacks 0DEA, part (1).** The topology of the small étale site of `X`: that of
> `X_{red, étale}`.

```lean
noncomputable abbrev canonicalSmallEtaleTopology (hX : IsFormalAlgebraicSpace B S hS X) :
    GrothendieckTopology (canonicalSmallEtale hX)
```

**`AlgebraicGeometry.FormalSpace.canonicalSpacesEtale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonical.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonical.lean#L172). The attribute's comment: “(2) the spaces-étale site, as a category”.

> **Stacks 0DEA, part (2).** The site `X_{spaces, étale}` of a formal algebraic space `X` over
> `S`, as a category: the spaces-étale site `X_{red, spaces, étale}` of its reduction, in the
> sense of Stacks 03G0, whose objects are the algebraic spaces étale over `X_red`.

```lean
abbrev canonicalSpacesEtale (hX : IsFormalAlgebraicSpace B S hS X)
```

**`AlgebraicGeometry.FormalSpace.canonicalSpacesEtaleTopology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonical.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonical.lean#L178). The attribute's comment: “(2) the topology of the spaces-étale site”.

> **Stacks 0DEA, part (2).** The topology of `X_{spaces, étale}`: that of
> `X_{red, spaces, étale}`.

```lean
noncomputable abbrev canonicalSpacesEtaleTopology (hX : IsFormalAlgebraicSpace B S hS X) :
    GrothendieckTopology (canonicalSpacesEtale hX)
```

**`AlgebraicGeometry.FormalSpace.canonicalAffineEtale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonical.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonical.lean#L186). The attribute's comment: “(3) the affine étale site, as a category”.

> **Stacks 0DEA, part (3).** The site `X_{affine, étale}` of a formal algebraic space `X` over
> `S`, as a category: the affine étale site `X_{red, affine, étale}` of its reduction, whose
> objects are the étale charts of `X_red` with affine source.

```lean
abbrev canonicalAffineEtale (hX : IsFormalAlgebraicSpace B S hS X)
```

**`AlgebraicGeometry.FormalSpace.canonicalAffineEtaleTopology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonical.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonical.lean#L192). The attribute's comment: “(3) the topology of the affine étale site”.

> **Stacks 0DEA, part (3).** The topology of `X_{affine, étale}`: that of
> `X_{red, affine, étale}`.

```lean
noncomputable abbrev canonicalAffineEtaleTopology (hX : IsFormalAlgebraicSpace B S hS X) :
    GrothendieckTopology (canonicalAffineEtale hX)
```

**`AlgebraicGeometry.FormalSpace.SmallEtale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteChosenReduction.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteChosenReduction.lean#L74). The attribute's comment: “(1) the small étale site, as a category”.

> **Stacks 0DEA, part (1).** The *small étale site* `X_étale` of a formal algebraic space `X`
> over `S`, as a category: the small étale site `X_{red, étale}` of the reduction, in the sense of
> Stacks 03ED, whose objects are the étale scheme charts of `X_red`.

```lean
abbrev SmallEtale (X : FppfSheaf B S hS) (hX : IsFormalAlgebraicSpace B S hS X)
```

**`AlgebraicGeometry.FormalSpace.smallEtaleTopology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteChosenReduction.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteChosenReduction.lean#L80). The attribute's comment: “(1) the topology of the small étale site”.

> **Stacks 0DEA, part (1).** The topology of the small étale site of `X`: that of
> `X_{red, étale}`.

```lean
noncomputable abbrev smallEtaleTopology (X : FppfSheaf B S hS)
    (hX : IsFormalAlgebraicSpace B S hS X) :
    GrothendieckTopology (SmallEtale B S hS X hX)
```

**`AlgebraicGeometry.FormalSpace.SpacesEtale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteChosenReduction.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteChosenReduction.lean#L89). The attribute's comment: “(2) the spaces-étale site, as a category”.

> **Stacks 0DEA, part (2).** The site `X_{spaces, étale}` of a formal algebraic space `X` over
> `S`, as a category: the spaces-étale site `X_{red, spaces, étale}` of the reduction, in the
> sense of Stacks 03G0, whose objects are the algebraic spaces étale over `X_red`.

```lean
abbrev SpacesEtale (X : FppfSheaf B S hS) (hX : IsFormalAlgebraicSpace B S hS X)
```

**`AlgebraicGeometry.FormalSpace.spacesEtaleTopology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteChosenReduction.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteChosenReduction.lean#L95). The attribute's comment: “(2) the topology of the spaces-étale site”.

> **Stacks 0DEA, part (2).** The topology of `X_{spaces, étale}`: that of
> `X_{red, spaces, étale}`.

```lean
noncomputable abbrev spacesEtaleTopology (X : FppfSheaf B S hS)
    (hX : IsFormalAlgebraicSpace B S hS X) :
    GrothendieckTopology (SpacesEtale B S hS X hX)
```

**`AlgebraicGeometry.FormalSpace.AffineEtale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteChosenReduction.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteChosenReduction.lean#L106). The attribute's comment: “(3) the affine étale site, as a category”.

> **Stacks 0DEA, part (3).** The site `X_{affine, étale}` of a formal algebraic space `X` over
> `S`, as a category: the affine étale site `X_{red, affine, étale}` of the reduction, whose
> objects are the étale charts of `X_red` with affine source. The site named by Properties of
> Spaces Lemma 04JS is `AlgebraicGeometry.Space.AffineEtale`, which in this library carries the
> tag Stacks 0H01.

```lean
abbrev AffineEtale (X : FppfSheaf B S hS) (hX : IsFormalAlgebraicSpace B S hS X)
```

**`AlgebraicGeometry.FormalSpace.affineEtaleTopology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteChosenReduction.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteChosenReduction.lean#L112). The attribute's comment: “(3) the topology of the affine étale site”.

> **Stacks 0DEA, part (3).** The topology of `X_{affine, étale}`: that of
> `X_{red, affine, étale}`.

```lean
noncomputable abbrev affineEtaleTopology (X : FppfSheaf B S hS)
    (hX : IsFormalAlgebraicSpace B S hS X) :
    GrothendieckTopology (AffineEtale B S hS X hX)
```

## Tag 0DEB, an equation

[Tag 0DEB](https://stacks.math.columbia.edu/tag/0DEB) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.canonicalSmallEtaleToposEquivSpacesEtale`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleTopos.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleTopos.lean#L134). The attribute's comment: “`Sh(X_étale) = Sh(X_spaces,étale)`, for sheaves in any category with the limits of the Comparison Lemma”.

> **Stacks 0DEB**, `Sh(X_étale) = Sh(X_{spaces, étale})`. For a formal algebraic space `X` over
> `S`, the topos of the small étale site `X_étale` of Stacks 0DEA, part (1), is equivalent to that
> of the site `X_{spaces, étale}` of Stacks 0DEA, part (2): restriction along the inclusion of
> étale scheme charts of `X_red` among algebraic spaces étale over `X_red` is an equivalence. This
> holds for sheaves valued in any category `A` with the limits the Comparison Lemma asks for, which
> includes sheaves of sets; see
> `AlgebraicGeometry.FormalSpace.canonicalSmallEtaleToposEquivSpacesEtaleSets`.

```lean
noncomputable def canonicalSmallEtaleToposEquivSpacesEtale (A : Type w) [Category.{w'} A]
    [∀ Y, HasLimitsOfShape
      (StructuredArrow Y (canonicalReduction hX).smallEtaleToSpacesEtale.op) A] :
    Sheaf (canonicalSmallEtaleTopology hX) A ≌ Sheaf (canonicalSpacesEtaleTopology hX) A
```

**`AlgebraicGeometry.FormalSpace.canonicalSmallEtaleToposEquivAffineEtale`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleTopos.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleTopos.lean#L148). The attribute's comment: “`Sh(X_étale) = Sh(X_affine,étale)`, for sheaves in any category with the limits of the Comparison Lemma”.

> **Stacks 0DEB**, `Sh(X_étale) = Sh(X_{affine, étale})`. For a formal algebraic space `X` over
> `S`, the topos of the small étale site `X_étale` of Stacks 0DEA, part (1), is equivalent to that
> of the site `X_{affine, étale}` of Stacks 0DEA, part (3): restriction along the inclusion of the
> étale charts of `X_red` with affine source is an equivalence. This holds for sheaves valued in
> any category `A` with the limits the Comparison Lemma asks for, which includes sheaves of sets;
> see `AlgebraicGeometry.FormalSpace.canonicalSmallEtaleToposEquivAffineEtaleSets`.

```lean
noncomputable def canonicalSmallEtaleToposEquivAffineEtale (A : Type w) [Category.{w'} A]
    [∀ Y, HasLimitsOfShape
      (StructuredArrow Y (canonicalReduction hX).affineEtaleInclusion.op) A] :
    Sheaf (canonicalSmallEtaleTopology hX) A ≌ Sheaf (canonicalAffineEtaleTopology hX) A
```

**`AlgebraicGeometry.FormalSpace.canonicalSmallEtaleToposEquivSpacesEtaleSets`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleTopos.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleTopos.lean#L179). The attribute's comment: “`Sh(X_étale) = Sh(X_spaces,étale)`, for sheaves of sets”.

> **Stacks 0DEB**, `Sh(X_étale) = Sh(X_{spaces, étale})`, for sheaves of sets. These are sets
> in `Type (u + 1)`, the universe of the small étale topoi of Stacks 0DEC, part (3), which pass
> through this identification.

```lean
noncomputable def canonicalSmallEtaleToposEquivSpacesEtaleSets :
    Sheaf (canonicalSmallEtaleTopology hX) (Type (u + 1)) ≌
      Sheaf (canonicalSpacesEtaleTopology hX) (Type (u + 1))
```

**`AlgebraicGeometry.FormalSpace.canonicalSmallEtaleToposEquivAffineEtaleSets`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleTopos.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleTopos.lean#L188). The attribute's comment: “`Sh(X_étale) = Sh(X_affine,étale)`, for sheaves of sets”.

> **Stacks 0DEB**, `Sh(X_étale) = Sh(X_{affine, étale})`, for sheaves of sets. These are sets
> in `Type (u + 1)`, the universe of the small étale topoi of Stacks 0DEC, part (3).

```lean
noncomputable def canonicalSmallEtaleToposEquivAffineEtaleSets :
    Sheaf (canonicalSmallEtaleTopology hX) (Type (u + 1)) ≌
      Sheaf (canonicalAffineEtaleTopology hX) (Type (u + 1))
```

## Tag 0DEC, a lemma

[Tag 0DEC](https://stacks.math.columbia.edu/tag/0DEC) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.Reduction.spacesBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSite.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSite.lean#L308). The attribute's comment: “(1) the base-change functor `Y_spaces,étale ⟶ X_spaces,étale`; read against given reductions, which Stacks 0AIN supplies”.

> The functor `Y_{spaces, étale} ⟶ X_{spaces, étale}` induced by a
> morphism `f : X ⟶ Y` of formal algebraic spaces: base change along the induced morphism of
> reductions, together with its cartesian projection, by Stacks 03G2, part (1).

```lean
noncomputable def spacesBaseChange (RX : Reduction B S hS X) (RY : Reduction B S hS Y)
    (f : X ⟶ Y) : Space.SpacesBaseChange B S hS (RX.map RY f)
```

**`AlgebraicGeometry.FormalSpace.Reduction.isContinuous_spacesBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSite.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSite.lean#L316). The attribute's comment: “(1) continuity of the functor; read against given reductions, which Stacks 0AIN supplies”.

> The functor `Y_{spaces, étale} ⟶ X_{spaces, étale}` is
> continuous.

```lean
theorem isContinuous_spacesBaseChange (RX : Reduction B S hS X) (RY : Reduction B S hS Y)
    (f : X ⟶ Y) :
    (RX.spacesBaseChange RY f).functor.IsContinuous RY.spacesEtaleTopology
      RX.spacesEtaleTopology
```

**`AlgebraicGeometry.FormalSpace.Reduction.spacesBaseChange_isMorphismOfSites`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSite.lean, line 327](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSite.lean#L327). The attribute's comment: “(1) the induced morphism of sites `f_spaces,étale`; read against given reductions, which Stacks 0AIN supplies”.

> The continuous functor `Y_{spaces, étale} ⟶ X_{spaces, étale}`
> induces a morphism of sites
> `f_{spaces, étale} : X_{spaces, étale} ⟶ Y_{spaces, étale}`, in the sense of Stacks 00X1.

```lean
theorem spacesBaseChange_isMorphismOfSites (RX : Reduction B S hS X)
    (RY : Reduction B S hS Y) (f : X ⟶ Y) :
    (RX.spacesBaseChange RY f).functor.IsMorphismOfSites RY.spacesEtaleTopology
      RX.spacesEtaleTopology
```

**`AlgebraicGeometry.FormalSpace.Reduction.spacesBaseChangeComp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSite.lean, line 339](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSite.lean#L339). The attribute's comment: “(2) compatibility with composition, as a canonical isomorphism of the underlying functors; read against given reductions, which Stacks 0AIN supplies”.

> The rule `f ↦ f_{spaces, étale}` is compatible with composition:
> the underlying functor of `(f ≫ g)_{spaces, étale}` is canonically isomorphic to the composite
> of those of `g_{spaces, étale}` and `f_{spaces, étale}`, which is the composition of morphisms
> of sites of Stacks 03CC.

```lean
noncomputable def spacesBaseChangeComp (RX : Reduction B S hS X) (RY : Reduction B S hS Y)
    (RZ : Reduction B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z) :
    (RY.spacesBaseChange RZ g).functor ⋙ (RX.spacesBaseChange RY f).functor ≅
      (RX.spacesBaseChange RZ (f ≫ g)).functor
```

**`AlgebraicGeometry.FormalSpace.Reduction.spacesBaseChangeComp_projection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSite.lean, line 350](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSite.lean#L350). The attribute's comment: “(2) the composition isomorphism is compatible with the cartesian projections, which pins it down; read against given reductions, which Stacks 0AIN supplies”.

> The composition isomorphism is compatible with the cartesian
> projections to the original object of `Z_{spaces, étale}`.

```lean
theorem spacesBaseChangeComp_projection (RX : Reduction B S hS X) (RY : Reduction B S hS Y)
    (RZ : Reduction B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z) (V : RZ.SpacesEtale) :
    ((RX.spacesBaseChangeComp RY RZ f g).hom.app V).hom.left ≫
        (RX.spacesBaseChange RZ (f ≫ g)).projection.app V =
      (RX.spacesBaseChange RY f).projection.app
          ((RY.spacesBaseChange RZ g).functor.obj V) ≫
        (RY.spacesBaseChange RZ g).projection.app V
```

**`AlgebraicGeometry.FormalSpace.Reduction.smallToposMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSite.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSite.lean#L366). The attribute's comment: “(3) the morphism of small étale topoi `f_small`, through the identification (0DEB); read against given reductions, which Stacks 0AIN supplies”.

> The morphism of topoi
> `f_small : Sh(X_étale) ⟶ Sh(Y_étale)` associated to `f_{spaces, étale}`, via the
> identification (0DEB) of the small étale topos with the spaces-étale topos. It is the morphism
> of small étale topoi of Stacks 03G2, part (3), at the induced morphism of reductions.

```lean
noncomputable def smallToposMorphism (RX : Reduction B S hS X) (RY : Reduction B S hS Y)
    (f : X ⟶ Y) :
    MorphismOfTopoi (Sheaf RX.smallEtaleTopology (Type (u + 1)))
      (Sheaf RY.smallEtaleTopology (Type (u + 1)))
```

**`AlgebraicGeometry.FormalSpace.Reduction.smallToposMorphismComp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSite.lean, line 377](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSite.lean#L377). The attribute's comment: “(3) compatibility with composition of the morphisms of small étale topoi, on direct images; read against given reductions, which Stacks 0AIN supplies”.

> The construction of `f_small` is compatible with composition:
> the direct image of the composite of `g_small` and `f_small` is canonically isomorphic to the
> direct image of `(f ≫ g)_small`.

```lean
noncomputable def smallToposMorphismComp (RX : Reduction B S hS X) (RY : Reduction B S hS Y)
    (RZ : Reduction B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z) :
    (MorphismOfTopoi.comp (RY.smallToposMorphism RZ g)
        (RX.smallToposMorphism RY f)).pushforward ≅
      (RX.smallToposMorphism RZ (f ≫ g)).pushforward
```

**`AlgebraicGeometry.FormalSpace.canonicalSpacesBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonical.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonical.lean#L202). The attribute's comment: “(1) the base-change functor `Y_spaces,étale ⟶ X_spaces,étale`”.

> **Stacks 0DEC, part (1).** The functor `Y_{spaces, étale} ⟶ X_{spaces, étale}` induced by a
> morphism `f : X ⟶ Y` of formal algebraic spaces: base change along the induced morphism of
> reductions, together with its cartesian projection, by Stacks 03G2, part (1).

```lean
noncomputable def canonicalSpacesBaseChange (hX : IsFormalAlgebraicSpace B S hS X)
    (hY : IsFormalAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    Space.SpacesBaseChange B S hS ((canonicalReduction hX).map (canonicalReduction hY) f)
```

**`AlgebraicGeometry.FormalSpace.isContinuous_canonicalSpacesBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonical.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonical.lean#L210). The attribute's comment: “(1) continuity of the functor”.

> **Stacks 0DEC, part (1).** The functor `Y_{spaces, étale} ⟶ X_{spaces, étale}` is
> continuous.

```lean
theorem isContinuous_canonicalSpacesBaseChange (hX : IsFormalAlgebraicSpace B S hS X)
    (hY : IsFormalAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    (canonicalSpacesBaseChange hX hY f).functor.IsContinuous
      (canonicalSpacesEtaleTopology hY) (canonicalSpacesEtaleTopology hX)
```

**`AlgebraicGeometry.FormalSpace.canonicalSpacesBaseChange_isMorphismOfSites`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonical.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonical.lean#L220). The attribute's comment: “(1) the induced morphism of sites `f_spaces,étale`”.

> **Stacks 0DEC, part (1).** The continuous functor `Y_{spaces, étale} ⟶ X_{spaces, étale}`
> induces a morphism of sites `f_{spaces, étale} : X_{spaces, étale} ⟶ Y_{spaces, étale}`, in the
> sense of Stacks 00X1.

```lean
theorem canonicalSpacesBaseChange_isMorphismOfSites (hX : IsFormalAlgebraicSpace B S hS X)
    (hY : IsFormalAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    (canonicalSpacesBaseChange hX hY f).functor.IsMorphismOfSites
      (canonicalSpacesEtaleTopology hY) (canonicalSpacesEtaleTopology hX)
```

**`AlgebraicGeometry.FormalSpace.canonicalSpacesBaseChangeComp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonical.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonical.lean#L232). The attribute's comment: “(2) compatibility with composition, as a canonical isomorphism of the underlying functors”.

> **Stacks 0DEC, part (2).** The rule `f ↦ f_{spaces, étale}` is compatible with composition:
> the underlying functor of `(f ≫ g)_{spaces, étale}` is canonically isomorphic to the composite
> of those of `g_{spaces, étale}` and `f_{spaces, étale}`, which is the composition of morphisms
> of sites of Stacks 03CC.

```lean
noncomputable def canonicalSpacesBaseChangeComp (hX : IsFormalAlgebraicSpace B S hS X)
    (hY : IsFormalAlgebraicSpace B S hS Y) (hZ : IsFormalAlgebraicSpace B S hS Z) (f : X ⟶ Y)
    (g : Y ⟶ Z) :
    (canonicalSpacesBaseChange hY hZ g).functor ⋙ (canonicalSpacesBaseChange hX hY f).functor ≅
      (canonicalSpacesBaseChange hX hZ (f ≫ g)).functor
```

**`AlgebraicGeometry.FormalSpace.canonicalSpacesBaseChangeComp_projection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonical.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonical.lean#L244). The attribute's comment: “(2) the composition isomorphism is compatible with the cartesian projections, which pins it down”.

> **Stacks 0DEC, part (2).** The composition isomorphism is compatible with the cartesian
> projections to the original object of `Z_{spaces, étale}`, which pins it down.

```lean
theorem canonicalSpacesBaseChangeComp_projection (hX : IsFormalAlgebraicSpace B S hS X)
    (hY : IsFormalAlgebraicSpace B S hS Y) (hZ : IsFormalAlgebraicSpace B S hS Z) (f : X ⟶ Y)
    (g : Y ⟶ Z) (V : canonicalSpacesEtale hZ) :
    ((canonicalSpacesBaseChangeComp hX hY hZ f g).hom.app V).hom.left ≫
        (canonicalSpacesBaseChange hX hZ (f ≫ g)).projection.app V =
      (canonicalSpacesBaseChange hX hY f).projection.app
          ((canonicalSpacesBaseChange hY hZ g).functor.obj V) ≫
        (canonicalSpacesBaseChange hY hZ g).projection.app V
```

**`AlgebraicGeometry.FormalSpace.canonicalSmallToposMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonical.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonical.lean#L261). The attribute's comment: “(3) the morphism of small étale topoi `f_small`, through the identification (0DEB)”.

> **Stacks 0DEC, part (3).** The morphism of topoi `f_small : Sh(X_étale) ⟶ Sh(Y_étale)`
> associated to `f_{spaces, étale}`, via the identification (0DEB) of the small étale topos with
> the spaces-étale topos. It is the morphism of small étale topoi of Stacks 03G2, part (3), at the
> induced morphism of reductions.

```lean
noncomputable def canonicalSmallToposMorphism (hX : IsFormalAlgebraicSpace B S hS X)
    (hY : IsFormalAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    MorphismOfTopoi (Sheaf (canonicalSmallEtaleTopology hX) (Type (u + 1)))
      (Sheaf (canonicalSmallEtaleTopology hY) (Type (u + 1)))
```

**`AlgebraicGeometry.FormalSpace.canonicalSmallToposMorphismComp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonical.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonical.lean#L272). The attribute's comment: “(3) compatibility with composition of the morphisms of small étale topoi, on direct images”.

> **Stacks 0DEC, part (3).** The construction of `f_small` is compatible with composition:
> the direct image of the composite of `g_small` and `f_small` is canonically isomorphic to the
> direct image of `(f ≫ g)_small`.

```lean
noncomputable def canonicalSmallToposMorphismComp (hX : IsFormalAlgebraicSpace B S hS X)
    (hY : IsFormalAlgebraicSpace B S hS Y) (hZ : IsFormalAlgebraicSpace B S hS Z) (f : X ⟶ Y)
    (g : Y ⟶ Z) :
    (MorphismOfTopoi.comp (canonicalSmallToposMorphism hY hZ g)
        (canonicalSmallToposMorphism hX hY f)).pushforward ≅
      (canonicalSmallToposMorphism hX hZ (f ≫ g)).pushforward
```

**`AlgebraicGeometry.FormalSpace.spacesBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteChosenReduction.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteChosenReduction.lean#L125). The attribute's comment: “(1) the base-change functor `Y_spaces,étale ⟶ X_spaces,étale`”.

> **Stacks 0DEC, part (1).** The functor `Y_{spaces, étale} ⟶ X_{spaces, étale}` induced by a
> morphism `f : X ⟶ Y` of formal algebraic spaces: base change along the induced morphism of
> reductions, together with its cartesian projection, by Stacks 03G2, part (1).

```lean
noncomputable def spacesBaseChange (hX : IsFormalAlgebraicSpace B S hS X)
    (hY : IsFormalAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    Space.SpacesBaseChange B S hS
      ((reduction B S hS X hX).map (reduction B S hS Y hY) f)
```

**`AlgebraicGeometry.FormalSpace.isContinuous_spacesBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteChosenReduction.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteChosenReduction.lean#L134). The attribute's comment: “(1) continuity of the functor”.

> **Stacks 0DEC, part (1).** The functor `Y_{spaces, étale} ⟶ X_{spaces, étale}` is
> continuous.

```lean
theorem isContinuous_spacesBaseChange (hX : IsFormalAlgebraicSpace B S hS X)
    (hY : IsFormalAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    (spacesBaseChange B S hS hX hY f).functor.IsContinuous
      (spacesEtaleTopology B S hS Y hY) (spacesEtaleTopology B S hS X hX)
```

**`AlgebraicGeometry.FormalSpace.spacesBaseChange_isMorphismOfSites`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteChosenReduction.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteChosenReduction.lean#L144). The attribute's comment: “(1) the induced morphism of sites `f_spaces,étale`”.

> **Stacks 0DEC, part (1).** The continuous functor `Y_{spaces, étale} ⟶ X_{spaces, étale}`
> induces a morphism of sites
> `f_{spaces, étale} : X_{spaces, étale} ⟶ Y_{spaces, étale}`, in the sense of Stacks 00X1.

```lean
theorem spacesBaseChange_isMorphismOfSites (hX : IsFormalAlgebraicSpace B S hS X)
    (hY : IsFormalAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    (spacesBaseChange B S hS hX hY f).functor.IsMorphismOfSites
      (spacesEtaleTopology B S hS Y hY) (spacesEtaleTopology B S hS X hX)
```

**`AlgebraicGeometry.FormalSpace.spacesBaseChangeComp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteChosenReduction.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteChosenReduction.lean#L156). The attribute's comment: “(2) compatibility with composition, as a canonical isomorphism of the underlying functors”.

> **Stacks 0DEC, part (2).** The rule `f ↦ f_{spaces, étale}` is compatible with composition:
> the underlying functor of `(f ≫ g)_{spaces, étale}` is canonically isomorphic to the composite
> of those of `g_{spaces, étale}` and `f_{spaces, étale}`, which is the composition of morphisms
> of sites of Stacks 03CC.

```lean
noncomputable def spacesBaseChangeComp (hX : IsFormalAlgebraicSpace B S hS X)
    (hY : IsFormalAlgebraicSpace B S hS Y) (hZ : IsFormalAlgebraicSpace B S hS Z) (f : X ⟶ Y)
    (g : Y ⟶ Z) :
    (spacesBaseChange B S hS hY hZ g).functor ⋙ (spacesBaseChange B S hS hX hY f).functor ≅
      (spacesBaseChange B S hS hX hZ (f ≫ g)).functor
```

**`AlgebraicGeometry.FormalSpace.spacesBaseChangeComp_projection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteChosenReduction.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteChosenReduction.lean#L168). The attribute's comment: “(2) the composition isomorphism is compatible with the cartesian projections, which pins it down”.

> **Stacks 0DEC, part (2).** The composition isomorphism is compatible with the cartesian
> projections to the original object of `Z_{spaces, étale}`, which pins it down.

```lean
theorem spacesBaseChangeComp_projection (hX : IsFormalAlgebraicSpace B S hS X)
    (hY : IsFormalAlgebraicSpace B S hS Y) (hZ : IsFormalAlgebraicSpace B S hS Z) (f : X ⟶ Y)
    (g : Y ⟶ Z) (V : SpacesEtale B S hS Z hZ) :
    ((spacesBaseChangeComp B S hS hX hY hZ f g).hom.app V).hom.left ≫
        (spacesBaseChange B S hS hX hZ (f ≫ g)).projection.app V =
      (spacesBaseChange B S hS hX hY f).projection.app
          ((spacesBaseChange B S hS hY hZ g).functor.obj V) ≫
        (spacesBaseChange B S hS hY hZ g).projection.app V
```

**`AlgebraicGeometry.FormalSpace.smallToposMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteChosenReduction.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteChosenReduction.lean#L185). The attribute's comment: “(3) the morphism of small étale topoi `f_small`, through the identification (0DEB)”.

> **Stacks 0DEC, part (3).** The morphism of topoi
> `f_small : Sh(X_étale) ⟶ Sh(Y_étale)` associated to `f_{spaces, étale}`, via the identification
> (0DEB) of the small étale topos with the spaces-étale topos. It is the morphism of small étale
> topoi of Stacks 03G2, part (3), at the induced morphism of reductions.

```lean
noncomputable def smallToposMorphism (hX : IsFormalAlgebraicSpace B S hS X)
    (hY : IsFormalAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    MorphismOfTopoi (Sheaf (smallEtaleTopology B S hS X hX) (Type (u + 1)))
      (Sheaf (smallEtaleTopology B S hS Y hY) (Type (u + 1)))
```

**`AlgebraicGeometry.FormalSpace.smallToposMorphismComp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteChosenReduction.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteChosenReduction.lean#L196). The attribute's comment: “(3) compatibility with composition of the morphisms of small étale topoi, on direct images”.

> **Stacks 0DEC, part (3).** The construction of `f_small` is compatible with composition:
> the direct image of the composite of `g_small` and `f_small` is canonically isomorphic to the
> direct image of `(f ≫ g)_small`.

```lean
noncomputable def smallToposMorphismComp (hX : IsFormalAlgebraicSpace B S hS X)
    (hY : IsFormalAlgebraicSpace B S hS Y) (hZ : IsFormalAlgebraicSpace B S hS Z) (f : X ⟶ Y)
    (g : Y ⟶ Z) :
    (MorphismOfTopoi.comp (smallToposMorphism B S hS hY hZ g)
        (smallToposMorphism B S hS hX hY f)).pushforward ≅
      (smallToposMorphism B S hS hX hZ (f ≫ g)).pushforward
```

## Tag 0DED, a lemma

[Tag 0DED](https://stacks.math.columbia.edu/tag/0DED) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isEtale_canonicalReductionMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonicalReduction.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonicalReduction.lean#L83). The attribute's comment: “étaleness of the induced morphism of reductions, which is the content of the proof”.

> **Stacks 0DED**, the content of the proof. Let `f : X ⟶ Y` be a morphism of formal algebraic
> spaces over `S` which is representable by algebraic spaces and étale. Then the induced morphism
> of reductions `X_red ⟶ Y_red` is an étale morphism of algebraic spaces over `S`.

```lean
theorem isEtale_canonicalReductionMap (hX : IsFormalAlgebraicSpace B S hS X)
    (hY : IsFormalAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hrep : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom)
    (het : Space.HasPropertyULift.{u + 1} B S hS
      (fun _ _ g ↦ Space.IsEtaleULift.{u + 1} B S hS g.hom) f.hom hrep) :
    Space.IsEtale B S hS ((canonicalReduction hX).map (canonicalReduction hY) f).hom
```

**`AlgebraicGeometry.FormalSpace.canonicalSmallEtalePostcomp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonicalReduction.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonicalReduction.lean#L96). The attribute's comment: “the functor `j : X_étale ⟶ Y_étale`”.

> **Stacks 0DED.** The functor `j : X_étale ⟶ Y_étale` attached to a morphism `f : X ⟶ Y` of
> formal algebraic spaces over `S` which is representable by algebraic spaces and étale:
> postcomposition of an étale scheme chart of `X_red` with the induced étale morphism of
> reductions, which is the functor of Stacks 03LP at that morphism.

```lean
noncomputable def canonicalSmallEtalePostcomp (hX : IsFormalAlgebraicSpace B S hS X)
    (hY : IsFormalAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hrep : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom)
    (het : Space.HasPropertyULift.{u + 1} B S hS
      (fun _ _ g ↦ Space.IsEtaleULift.{u + 1} B S hS g.hom) f.hom hrep) :
    (canonicalReduction hX).SmallEtale ⥤ (canonicalReduction hY).SmallEtale
```

**`AlgebraicGeometry.FormalSpace.canonicalSmallEtalePostcomp_isCocontinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonicalReduction.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonicalReduction.lean#L107). The attribute's comment: “cocontinuity of `j`”.

> **Stacks 0DED.** The functor `j` is cocontinuous: a covering sieve of `jU` in `Y_étale`
> pulls back to a covering sieve of `U` in `X_étale`.

```lean
instance canonicalSmallEtalePostcomp_isCocontinuous (hX : IsFormalAlgebraicSpace B S hS X)
    (hY : IsFormalAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hrep : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom)
    (het : Space.HasPropertyULift.{u + 1} B S hS
      (fun _ _ g ↦ Space.IsEtaleULift.{u + 1} B S hS g.hom) f.hom hrep) :
    (canonicalSmallEtalePostcomp hX hY f hrep het).IsCocontinuous
      (canonicalReduction hX).smallEtaleTopology (canonicalReduction hY).smallEtaleTopology
```

**`AlgebraicGeometry.FormalSpace.canonicalSmallEtalePostcomp_isContinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonicalReduction.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonicalReduction.lean#L119). The attribute's comment: “continuity of `j`, which is what makes Sites 00XR applicable”.

> **Stacks 0DED.** The functor `j` is continuous as well, so Sites 00XR applies to it.

```lean
instance canonicalSmallEtalePostcomp_isContinuous (hX : IsFormalAlgebraicSpace B S hS X)
    (hY : IsFormalAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hrep : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom)
    (het : Space.HasPropertyULift.{u + 1} B S hS
      (fun _ _ g ↦ Space.IsEtaleULift.{u + 1} B S hS g.hom) f.hom hrep) :
    (canonicalSmallEtalePostcomp hX hY f hrep het).IsContinuous
      (canonicalReduction hX).smallEtaleTopology (canonicalReduction hY).smallEtaleTopology
```

**`AlgebraicGeometry.FormalSpace.canonicalSmallToposMorphism_pushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonicalReduction.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonicalReduction.lean#L135). The attribute's comment: “`f_small` is the morphism of topoi that Sites 00XO attaches to `j`, identified on direct images”.

> **Stacks 0DED.** The morphism of topoi `f_small` of Stacks 0DEC, part (3), is the morphism
> of topoi that Sites 00XO attaches to the cocontinuous functor `j`: its direct image is the
> direct image of `j`.

```lean
noncomputable def canonicalSmallToposMorphism_pushforwardIso
    (hX : IsFormalAlgebraicSpace B S hS X) (hY : IsFormalAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hrep : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom)
    (het : Space.HasPropertyULift.{u + 1} B S hS
      (fun _ _ g ↦ Space.IsEtaleULift.{u + 1} B S hS g.hom) f.hom hrep) :
    ((canonicalReduction hX).smallToposMorphism (canonicalReduction hY) f).pushforward ≅
      (canonicalSmallEtalePostcomp hX hY f hrep het).sheafPushforwardCocontinuous
        (Type (u + 1)) (canonicalReduction hX).smallEtaleTopology
        (canonicalReduction hY).smallEtaleTopology
```

**`AlgebraicGeometry.FormalSpace.canonicalSmallToposMorphism_inverseImageObjObjIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonicalReduction.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSiteCanonicalReduction.lean#L152). The attribute's comment: “the formula on sections which Sites 00XR gives for `j`, continuous as well as cocontinuous”.

> **Stacks 0DED**, the consequence of continuity of `j` recorded by Sites 00XR: the inverse
> image of `f_small` is restriction along `j`, so a section of `f_small^{-1} G` over an étale
> chart `U` of `X_red` is a section of `G` over the chart `jU` of `Y_red`.

```lean
noncomputable def canonicalSmallToposMorphism_inverseImageObjObjIso
    (hX : IsFormalAlgebraicSpace B S hS X) (hY : IsFormalAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hrep : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom)
    (het : Space.HasPropertyULift.{u + 1} B S hS
      (fun _ _ g ↦ Space.IsEtaleULift.{u + 1} B S hS g.hom) f.hom hrep)
    (G : Sheaf (canonicalReduction hY).smallEtaleTopology (Type (u + 1)))
    (U : (canonicalReduction hX).SmallEtale) :
    (((canonicalReduction hX).smallToposMorphism (canonicalReduction hY) f).inverseImage.obj
        G).obj.obj (Opposite.op U) ≅
      G.obj.obj (Opposite.op ((canonicalSmallEtalePostcomp hX hY f hrep het).obj U))
```

**`AlgebraicGeometry.FormalSpace.Reduction.isEtale_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSitePostcomposition.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSitePostcomposition.lean#L196). The attribute's comment: “étaleness of the induced morphism of reductions, which is the content of the proof; read against given reductions, which Stacks 0AIN supplies”.

> **Stacks 0DED**, the content of the proof. Let `f : X ⟶ Y` be a morphism of formal algebraic
> spaces over `S` which is representable by algebraic spaces and étale. Then the induced morphism
> of reductions `X_red ⟶ Y_red` is an étale morphism of algebraic spaces over `S`.
>
> The fibre product `X ×_Y Y_red` is a reduction of `X` and every comparison morphism
> `X_red ⟶ X ×_Y Y_red` over `X` is an isomorphism — this is Stacks 0GB7, applicable because an
> étale morphism is smooth — so the morphism of reductions is, up to that isomorphism, the second
> projection of the fibre product. That projection is a base change of `f`, hence étale after
> every further base change along a scheme-valued point of `Y_red`; étaleness being étale local on
> the source and target, it satisfies the every-étale-chart condition of Stacks 03MJ, which
> descends to the value universe of the algebraic spaces.

```lean
theorem isEtale_map (hX : IsFormalAlgebraicSpace B S hS X)
    (hY : IsFormalAlgebraicSpace B S hS Y) (RX : Reduction B S hS X) (RY : Reduction B S hS Y)
    (f : X ⟶ Y) (hrep : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom)
    (het : Space.HasPropertyULift.{u + 1} B S hS
      (fun _ _ g ↦ Space.IsEtaleULift.{u + 1} B S hS g.hom) f.hom hrep) :
    Space.IsEtale B S hS (RX.map RY f).hom
```

**`AlgebraicGeometry.FormalSpace.Reduction.smallEtalePostcomp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSitePostcomposition.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSitePostcomposition.lean#L268). The attribute's comment: “the functor `j : X_étale ⟶ Y_étale`; read against given reductions, which Stacks 0AIN supplies”.

> **Stacks 0DED.** The functor `j : X_étale ⟶ Y_étale` attached to a morphism `f : X ⟶ Y` of
> formal algebraic spaces over `S` which is representable by algebraic spaces and étale:
> postcomposition of an étale scheme chart of `X_red` with the induced étale morphism of
> reductions, which is the functor of Stacks 03LP at that morphism.

```lean
noncomputable def smallEtalePostcomp (hX : IsFormalAlgebraicSpace B S hS X)
    (hY : IsFormalAlgebraicSpace B S hS Y) (RX : Reduction B S hS X)
    (RY : Reduction B S hS Y) (f : X ⟶ Y)
    (hrep : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom)
    (het : Space.HasPropertyULift.{u + 1} B S hS
      (fun _ _ g ↦ Space.IsEtaleULift.{u + 1} B S hS g.hom) f.hom hrep) :
    RX.SmallEtale ⥤ RY.SmallEtale
```

**`AlgebraicGeometry.FormalSpace.Reduction.smallEtalePostcomp_isCocontinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSitePostcomposition.lean, line 281](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSitePostcomposition.lean#L281). The attribute's comment: “cocontinuity of `j`; read against given reductions, which Stacks 0AIN supplies”.

> **Stacks 0DED.** The functor `j` is cocontinuous: a covering sieve of `jU` in `Y_étale`
> pulls back to a covering sieve of `U` in `X_étale`.

```lean
instance smallEtalePostcomp_isCocontinuous (hX : IsFormalAlgebraicSpace B S hS X)
    (hY : IsFormalAlgebraicSpace B S hS Y) (RX : Reduction B S hS X)
    (RY : Reduction B S hS Y) (f : X ⟶ Y)
    (hrep : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom)
    (het : Space.HasPropertyULift.{u + 1} B S hS
      (fun _ _ g ↦ Space.IsEtaleULift.{u + 1} B S hS g.hom) f.hom hrep) :
    (smallEtalePostcomp hX hY RX RY f hrep het).IsCocontinuous RX.smallEtaleTopology
      RY.smallEtaleTopology
```

**`AlgebraicGeometry.FormalSpace.Reduction.smallEtalePostcomp_isContinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSitePostcomposition.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSitePostcomposition.lean#L295). The attribute's comment: “continuity of `j`, which is what makes Sites 00XR applicable; read against given reductions, which Stacks 0AIN supplies”.

> **Stacks 0DED.** The functor `j` is continuous as well, so Sites 00XR applies to it.

```lean
instance smallEtalePostcomp_isContinuous (hX : IsFormalAlgebraicSpace B S hS X)
    (hY : IsFormalAlgebraicSpace B S hS Y) (RX : Reduction B S hS X)
    (RY : Reduction B S hS Y) (f : X ⟶ Y)
    (hrep : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom)
    (het : Space.HasPropertyULift.{u + 1} B S hS
      (fun _ _ g ↦ Space.IsEtaleULift.{u + 1} B S hS g.hom) f.hom hrep) :
    (smallEtalePostcomp hX hY RX RY f hrep het).IsContinuous RX.smallEtaleTopology
      RY.smallEtaleTopology
```

**`AlgebraicGeometry.FormalSpace.Reduction.smallToposMorphism_pushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSitePostcomposition.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSitePostcomposition.lean#L312). The attribute's comment: “`f_small` is the morphism of topoi that Sites 00XO attaches to `j`, identified on direct images; read against given reductions, which Stacks 0AIN supplies”.

> **Stacks 0DED.** The morphism of topoi `f_small` of Stacks 0DEC, part (3), is the morphism
> of topoi that Sites 00XO attaches to the cocontinuous functor `j`: its direct image is the
> direct image of `j`.

```lean
noncomputable def smallToposMorphism_pushforwardIso (hX : IsFormalAlgebraicSpace B S hS X)
    (hY : IsFormalAlgebraicSpace B S hS Y) (RX : Reduction B S hS X)
    (RY : Reduction B S hS Y) (f : X ⟶ Y)
    (hrep : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom)
    (het : Space.HasPropertyULift.{u + 1} B S hS
      (fun _ _ g ↦ Space.IsEtaleULift.{u + 1} B S hS g.hom) f.hom hrep) :
    (RX.smallToposMorphism RY f).pushforward ≅
      (smallEtalePostcomp hX hY RX RY f hrep het).sheafPushforwardCocontinuous
        (Type (u + 1)) RX.smallEtaleTopology RY.smallEtaleTopology
```

**`AlgebraicGeometry.FormalSpace.Reduction.smallToposMorphism_inverseImageObjObjIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSitePostcomposition.lean, line 329](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSitePostcomposition.lean#L329). The attribute's comment: “the formula on sections which Sites 00XR gives for `j`, continuous as well as cocontinuous; read against given reductions, which Stacks 0AIN supplies”.

> **Stacks 0DED**, the consequence of continuity of `j` recorded by Sites 00XR: the inverse
> image of `f_small` is restriction along `j`, so a section of `f_small^{-1} G` over an étale
> chart `U` of `X_red` is a section of `G` over the chart `jU` of `Y_red`.

```lean
noncomputable def smallToposMorphism_inverseImageObjObjIso
    (hX : IsFormalAlgebraicSpace B S hS X) (hY : IsFormalAlgebraicSpace B S hS Y)
    (RX : Reduction B S hS X) (RY : Reduction B S hS Y) (f : X ⟶ Y)
    (hrep : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom)
    (het : Space.HasPropertyULift.{u + 1} B S hS
      (fun _ _ g ↦ Space.IsEtaleULift.{u + 1} B S hS g.hom) f.hom hrep)
    (G : Sheaf RY.smallEtaleTopology (Type (u + 1))) (U : RX.SmallEtale) :
    ((RX.smallToposMorphism RY f).inverseImage.obj G).obj.obj (Opposite.op U) ≅
      G.obj.obj (Opposite.op ((smallEtalePostcomp hX hY RX RY f hrep het).obj U))
```

## Tag 0DEE, a lemma

[Tag 0DEE](https://stacks.math.columbia.edu/tag/0DEE) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.AffineEtaleFormalCharts`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/EtaleSite.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/EtaleSite.lean#L130). The attribute's comment: “the category of the morphisms satisfying (1) and (2)”.

> **Stacks 0DEE**, the category on the right-hand side: the morphisms `φ : U ⟶ X` of formal
> algebraic spaces with `U` an affine formal algebraic space and `φ` representable by algebraic
> spaces and étale, with the morphisms of fppf sheaves over `X` between them.

```lean
abbrev AffineEtaleFormalCharts (X : FppfSheaf B S hS)
```

**`AlgebraicGeometry.FormalSpace.reductionAffineEtaleComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/EtaleSite.lean, line 468](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/EtaleSite.lean#L468). The attribute's comment: “the comparison functor from the category of the morphisms satisfying (1) and (2) to the affine étale site of `X`, carrying the reduction of `X` and its affineness as data rather than chosen from Stacks 0AIN; the functor is not shown to be an equivalence”.

> **Stacks 0DEE**, the comparison functor into the affine étale site of `X`. Let `X` be an
> affine formal algebraic space over `S` whose reduction is the sheaf represented by an object
> `V` of the site with affine underlying scheme, by a morphism `i`. By Stacks 0DEA the affine
> étale site of `X` is the affine étale site of its reduction, that is of `V`, and this is the
> functor to it from the category of the morphisms `φ : U ⟶ X` with `U` an affine formal
> algebraic space and `φ` representable by algebraic spaces and étale, sending `φ` to
> `U ×_X X_red`.
>
> The reduction is carried as data, with its affineness, rather than chosen from Stacks 0AIN;
> for an affine formal algebraic space the reduction is an affine scheme, which is why the datum
> is not a restriction. Stacks 0DEE asserts that this functor is an equivalence; the
> quasi-inverse is not constructed here.

```lean
noncomputable def reductionAffineEtaleComparison {X : FppfSheaf B S hS}
    (hX : IsAffineFormalAlgebraicSpace B S hS X) (V : BigFppfOver B S hS)
    (hV : IsAffine ((BigFppfOver.toScheme B S hS).obj V))
    (i : (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).obj V ⟶ X)
    (_hred : IsReduction B S hS X
      ((Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).obj V) i) :
    AffineEtaleFormalCharts B S hS X ⥤ Space.AffineEtale B S hS (yoneda.obj V)
```

**`AlgebraicGeometry.FormalSpace.affineEtaleEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/EtaleSiteEquivalence.lean, line 528](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/EtaleSiteEquivalence.lean#L528). The attribute's comment: “the equivalence of `X_affine,étale` with the category of the morphisms satisfying (1) and (2); fullness, faithfulness and essential surjectivity are all proved, and the affine étale site of Stacks 0DEA(3) is identified with the one the comparison functor targets”.

> **Stacks 0DEE.** Let `X` be an affine formal algebraic space over `S`. Then
> `X_{affine, étale}` — the affine étale site of the reduction of `X`, in the sense of Stacks
> 0DEA part (3), at an arbitrary reduction datum — is equivalent to the category whose objects
> are the morphisms `φ : U ⟶ X` of formal algebraic spaces such that
>
> 1. `U` is an affine formal algebraic space,
> 2. `φ` is representable by algebraic spaces and étale.
>
> The functor is the source's, `(U ⟶ X) ↦ U ×_X X_red`: it is
> `AlgebraicGeometry.FormalSpace.reductionAffineEtaleComparison`, read backwards and composed
> with the identification of `X_{affine, étale}` with the affine étale site of the Yoneda
> presheaf of the chosen affine reduction chart. Full faithfulness is
> `AlgebraicGeometry.FormalSpace.full_affineEtaleComparison` and
> `AlgebraicGeometry.FormalSpace.faithful_affineEtaleComparison`, both out of the unique
> extension of a morphism along a representable thickening; essential surjectivity is
> `AlgebraicGeometry.FormalSpace.essSurj_affineEtaleComparison`, whose quasi-inverse is the
> dependent product `U_{W, q}` and whose affineness is
> `AlgebraicGeometry.FormalSpace.isAffineFormalAlgebraicSpace_liftAlong_of_affine`. The source's
> omitted "verification that the constructions are mutually inverse to each other" is therefore
> supplied.
>
> The reduction datum is a parameter, not a weakening: `X_{affine, étale}` is defined, in Stacks
> 0DEA, only for a formal algebraic space with a given reduction, and the datum exists for every
> affine formal algebraic space by Stacks 0AIN — in the shape used here by
> `AlgebraicGeometry.FormalSpace.nonempty_affineReductionChart`.

```lean
noncomputable def affineEtaleEquivalence (hX : IsAffineFormalAlgebraicSpace B S hS X)
    (R : Reduction B S hS X) : R.AffineEtale ≌ AffineEtaleFormalCharts B S hS X
```

**`AlgebraicGeometry.FormalSpace.reductionAffineEtaleComparison_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/EtaleSiteEquivalence.lean, line 545](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/EtaleSiteEquivalence.lean#L545). The attribute's comment: “the comparison functor is an equivalence: it is full, faithful and essentially surjective”.

> **Stacks 0DEE.** The comparison functor
> `AlgebraicGeometry.FormalSpace.reductionAffineEtaleComparison` of Stacks 0DEE is an equivalence
> of categories: it is full, faithful and essentially surjective. Its target is the affine étale
> site of `X`, which is identified with the site `X_{affine, étale}` of Stacks 0DEA part (3) by
> `AlgebraicGeometry.FormalSpace.Reduction.affineEtaleIsoYonedaAffineReductionChart`; the
> resulting equivalence stated with that site is
> `AlgebraicGeometry.FormalSpace.affineEtaleEquivalence`.

```lean
theorem reductionAffineEtaleComparison_isEquivalence
    (hX : IsAffineFormalAlgebraicSpace B S hS X) :
    (reductionAffineEtaleComparison' B S hS hX).IsEquivalence
```

**`AlgebraicGeometry.FormalSpace.reductionAffineEtaleComparison'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/EtaleSiteSupplement.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/EtaleSiteSupplement.lean#L255). The attribute's comment: “the comparison functor from the category of the morphisms satisfying (1) and (2) to the affine étale site of `X`; that it is an equivalence is AlgebraicGeometry.FormalSpace.reductionAffineEtaleComparison\_isEquivalence”.

> **Stacks 0DEE**, the comparison functor into the affine étale site of `X`. Let `X` be an
> affine formal algebraic space over `S`. Its reduction `X_red` is the sheaf represented by an
> object of the site with affine underlying scheme — this is Stacks 0AIN for an affine formal
> algebraic space, in the form
> `AlgebraicGeometry.FormalSpace.nonempty_affineReductionChart` — and by Stacks 0DEA the affine
> étale site of `X` is the affine étale site of `X_red`. This is the functor to it from the
> category of the morphisms `φ : U ⟶ X` with `U` an affine formal algebraic space and `φ`
> representable by algebraic spaces and étale, sending `φ` to `U ×_X X_red`.
>
> Nothing is carried as a hypothesis beyond `X` being an affine formal algebraic space: the
> reduction and its affineness are constructed, and which reduction is chosen is immaterial by
> `AlgebraicGeometry.FormalSpace.AffineReductionChart.iso`. Stacks 0DEE asserts that this functor
> is an equivalence; that is
> `AlgebraicGeometry.FormalSpace.reductionAffineEtaleComparison_isEquivalence`, in
> `StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/EtaleSiteEquivalence.lean`.

```lean
noncomputable def reductionAffineEtaleComparison' {X : FppfSheaf B S hS}
    (hX : IsAffineFormalAlgebraicSpace B S hS X) :
    AffineEtaleFormalCharts B S hS X ⥤
      Space.AffineEtale B S hS (yoneda.obj (affineReductionChart B S hS hX).obj)
```

## Tag 0DEF, a lemma

[Tag 0DEF](https://stacks.math.columbia.edu/tag/0DEF) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.completionAffineEtale`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SmallEtaleSite/CompletionToAffineEtale.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SmallEtaleSite/CompletionToAffineEtale.lean#L346). The attribute's comment: “the functor from the category of the completions `B^∧` of its items (1) and (2) to the opposite of an affine étale site, on objects the quotient stage `B^∧ ↦ Spec (B ⧸ JB)` and on morphisms the map of quotient stages a continuous `A`-algebra homomorphism of completions induces. The site is the affine étale site of the stage `Spec (A ⧸ J)`, the target of this library's Stacks 0DEE comparison functor at that affine object, rather than of the reduction of `Spf A`, which would have to be chosen from Stacks 0AIN. The functor is not shown to be an equivalence: the quasi-inverse would have to make `Spf B^∧ ⟶ Spf A` representable étale, which needs Stacks 0AKN and the locality on the target of the universe-lifted representability and étaleness conditions, neither of which this library carries”.

> **Stacks 0DEF**, the functor from the category of the `A`-algebras `B^∧ = lim B/JB` of its
> items (1) and (2) to the *opposite* of an affine étale site, which is the direction in which
> Stacks 0DEF identifies that category with `(X_{affine,étale})^{opp}`. It sends an étale ring map
> `A → B` to the affine object `Spec (B ⧸ JB)` of the site, étale over `Spec (A ⧸ J)`, and a
> continuous `A`-algebra homomorphism `B₁^∧ → B₂^∧` to the morphism `Spec (B₂ ⧸ JB₂) ⟶
> Spec (B₁ ⧸ JB₁)` it induces on quotient stages.
>
> The site is the affine étale site of the stage `Spec (A ⧸ J)`, which is the target of the
> comparison functor `AlgebraicGeometry.FormalSpace.affineEtaleComparison` of Stacks 0DEE at the
> affine object `Spec (A ⧸ J)` of the site and the stage inclusion `Spec (A ⧸ J) ⟶ Spf A`.

```lean
noncomputable def completionAffineEtale (D : QuotientSystem B S hS A)
    (J : WeakIdealOfDefinitionIndex A) :
    EtaleCompletion A ⥤ (Space.AffineEtale B S hS
      (yoneda.obj ((BigAffineFppf.inclusion B S hS).obj (D.stage J))))ᵒᵖ
```

**`AlgebraicGeometry.FormalSpace.EtaleCompletion`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SmallEtaleSite/McQuillanAffineEtale.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SmallEtaleSite/McQuillanAffineEtale.lean#L102). The attribute's comment: “item (1), the objects: an `A`-algebra of the form `B^∧ = lim B/JB` for an étale ring map `A → B`, named here by that ring map together with its étaleness, the completion being `TopologicalRing.CompletionOver` of it. The equivalence with `(X_affine,étale)^opp` is not constructed: it needs Stacks 0DEE as an equivalence, which this library has only as a comparison functor, and Stacks 0AN8 as an equivalence, which this library has only in the ring-theoretic form `EtaleCompletion.etale_quotientMap`”.

> **Stacks 0DEF**, item (1): the datum naming an object of the category attached to a weakly
> admissible topological ring `A`.  It is an étale ring map `A → B`; the `A`-algebra it names is
> the completion `B^∧ = lim B/JB`, the limit being over the weak ideals of definition `J` of `A`,
> see `AlgebraicGeometry.FormalSpace.EtaleCompletion.completion`.

```lean
structure EtaleCompletion
```

**`AlgebraicGeometry.FormalSpace.EtaleCompletion.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SmallEtaleSite/McQuillanAffineEtale.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SmallEtaleSite/McQuillanAffineEtale.lean#L135). The attribute's comment: “item (2), the morphisms: the continuous `A`-algebra homomorphisms between the objects, with the `A`-algebra structure of `B^∧` given by the canonical map `TopologicalRing.CompletionOver.canonicalMap`. The equivalence with `(X_affine,étale)^opp` is not constructed, for the reasons recorded on `EtaleCompletion`”.

> **Stacks 0DEF**, item (2): a morphism of the category, a continuous `A`-algebra
> homomorphism `B₁^∧ → B₂^∧` between the completions named by two objects.  The `A`-algebra
> structures are the canonical maps of Stacks 0AN6, so being an `A`-algebra homomorphism is the
> displayed commuting triangle.

```lean
structure Hom (Y Z : EtaleCompletion A)
```

**`AlgebraicGeometry.FormalSpace.mcQuillanAffineEtaleEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SmallEtaleSite/McQuillanEtaleEquivalence.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SmallEtaleSite/McQuillanEtaleEquivalence.lean#L111). The attribute's comment: “the equivalence of `(X_affine,étale)^opp` with the category whose objects are the `A`-algebras `B^∧ = lim B/JB` for an étale ring map `A → B` (item (1)) and whose morphisms are the continuous `A`-algebra homomorphisms (item (2)), namely `AlgebraicGeometry.FormalSpace.EtaleCompletion`. It is the source's proof: Stacks 0DEE, `affineEtaleEquivalence`, composed with Stacks 0AN8, `isEquivalence_etaleCompletionCharts`, whose opposite is taken on the algebra side because `Spf` is contravariant; `CategoryTheory.Equivalence.leftOp` moves that one opposite to the geometric side, where the source writes it. The reduction datum is a parameter for the same reason as in Stacks 0DEE -- `X_affine,étale` of Stacks 0DEA(3) is defined only relative to one, and one exists by Stacks 0AIN -- and the quotient system `D` with its large-site condition is this library's spelling of `A` being a weakly admissible topological `S`-algebra whose `Spf` is an affine formal algebraic space, which is the source's hypothesis on `X`”.

> **Stacks 0DEF.** Let `S` be a scheme contained in a big fppf site `B` and let
> `X = Spf A` be a McQuillan affine formal algebraic space over `S`: `A` is a weakly admissible
> topological ring presented over `S` by a quotient system `D` whose atlas lies in the site. Then
> `(X_{affine,étale})^{opp}` — the opposite of the affine étale site of Stacks 0DEA part (3), at
> an arbitrary reduction datum of `X` — is equivalent to the category whose
>
> 1. objects are the `A`-algebras `B^∧ = lim B/JB` for an étale ring map `A → B`, the limit being
>    over the weak ideals of definition `J` of `A`, and
> 2. morphisms are the continuous `A`-algebra homomorphisms,
>
> which is `AlgebraicGeometry.FormalSpace.EtaleCompletion`.
>
> This is the source's proof: combine Stacks 0DEE,
> `AlgebraicGeometry.FormalSpace.affineEtaleEquivalence`, with Stacks 0AN8,
> `AlgebraicGeometry.FormalSpace.isEquivalence_etaleCompletionCharts`. The first identifies
> `X_{affine,étale}` with the category of the affine formal algebraic spaces representable étale
> over `X`, the second identifies that category with `(EtaleCompletion A)ᵒᵖ`; taking the opposite
> of the composite moves the single opposite from the algebra side, where `Spf` being
> contravariant puts it, to the geometric side, where Stacks 0DEF writes it.

```lean
def mcQuillanAffineEtaleEquivalence (hA : TopologicalRing.IsWeaklyAdmissible A)
    (D : QuotientSystem B S hS A) (hD : D.HasLargeSite)
    (R : Reduction B S hS (formalSpectrum D)) :
    R.AffineEtaleᵒᵖ ≌ EtaleCompletion A
```

## Tag 0DEG, a lemma

[Tag 0DEG](https://stacks.math.columbia.edu/tag/0DEG) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.spacesEtaleComparison_isEquivalence'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/LiftAlongAffineBase.lean, line 440](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/LiftAlongAffineBase.lean#L440). The attribute's comment: “the equivalence; full faithfulness and essential surjectivity are both proved, the latter from the source's assertion that `U_{V, ψ}` is a formal algebraic space, which is AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace\_liftAlong”.

> **Stacks 0DEG.** The comparison functor from the category of the formal algebraic spaces
> representable étale over a formal algebraic space `X` to `X_{spaces, étale}` is an equivalence
> of categories.
>
> Full faithfulness is `AlgebraicGeometry.FormalSpace.bijective_spacesEtaleComparison_map` and
> essential surjectivity is `AlgebraicGeometry.FormalSpace.essSurj_spacesEtaleComparison`. Every
> assertion of the source is proved: the sheaf `U_{V, ψ}` the source produces is constructed, in
> `StacksFrontier/AlgebraicGeometry/FormalSpace/SpacesEtaleQuasiInverse.lean`, its fibre product with
> `X_red` over `X` is identified with `V`, the source's omitted verification that
> `U_{V, ψ} ⟶ X` is representable by algebraic spaces and étale is proved, in
> `StacksFrontier/AlgebraicGeometry/FormalSpace/SpacesEtaleQuasiInverseRepresentable.lean`, and that
> `U_{V, ψ}` is a formal algebraic space is
> `AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_liftAlong`.
>
> The reduction of `X` is a parameter, not a weakening: `X_{spaces, étale}` is defined, in Stacks
> 0DEA, only for a formal algebraic space with a given reduction, and the datum exists for every
> formal algebraic space by Stacks 0AIN.

```lean
theorem spacesEtaleComparison_isEquivalence' {X : FppfSheaf B S hS}
    (hX : IsFormalAlgebraicSpace B S hS X) (R : Reduction B S hS X) :
    (spacesEtaleComparison hX R).IsEquivalence
```

**`AlgebraicGeometry.FormalSpace.spacesEtaleComparison_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SpacesEtaleIdentification.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SpacesEtaleIdentification.lean#L295). The attribute's comment: “the equivalence; bijectivity on morphisms and essential surjectivity — the two verifications the source omits — are hypotheses, and the equivalence is read against a given reduction of `X`, which Stacks 0AIN supplies”.

> The comparison functor from the category of the formal algebraic spaces representable étale
> over a formal algebraic space `X` to `X_{spaces, étale}` is an equivalence of categories.
>
> Two hypotheses are carried, and they are exactly the two verifications the source omits.
> `hhom` is bijectivity on morphisms, which is the source's "we omit the verification that the
> constructions are mutually inverse to each other": it amounts to lifting a morphism over `X`
> along the thickening `X_red ⟶ X` against an étale target. `hess` is essential surjectivity,
> which is the source's construction of the quasi-inverse `U_{V, ψ}` together with its "we omit
> the verification that `U_{V, ψ} ⟶ X` is representable by algebraic spaces and étale". The
> reduction of `X` is a given as well, which is no weakening: `X_{spaces, étale}` is defined, in
> Stacks 0DEA, only for a formal algebraic space with a given reduction, and Stacks 0AIN supplies
> one.

```lean
theorem spacesEtaleComparison_isEquivalence {X : FppfSheaf B S hS}
    (hX : IsFormalAlgebraicSpace B S hS X) (R : Reduction B S hS X)
    (hhom : ∀ U U' : RepresentableEtaleFormalSpacesOver X,
      Function.Bijective fun f : U ⟶ U' ↦ (spacesEtaleComparison hX R).map f)
    (hess : ∀ V : R.SpacesEtale, ∃ U : RepresentableEtaleFormalSpacesOver X,
      Nonempty ((spacesEtaleComparison hX R).obj U ≅ V)) :
    (spacesEtaleComparison hX R).IsEquivalence
```

**`AlgebraicGeometry.FormalSpace.bijective_spacesEtaleComparison_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SpacesEtaleIdentificationSupplement.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SpacesEtaleIdentificationSupplement.lean#L284). The attribute's comment: “bijectivity on morphisms: the source's 'we omit the verification that the constructions are mutually inverse to each other'”.

> The comparison functor is bijective on morphisms: for `φ : U ⟶ X` and
> `φ' : U' ⟶ X` representable by algebraic spaces and étale, with `U` and `U'` formal algebraic
> spaces, the morphisms `U ⟶ U'` over `X` correspond bijectively to the morphisms
> `U_red ⟶ U'_red` over `X_red`.
>
> This is the source's "we omit the verification that the constructions are mutually inverse to
> each other", on the side that needs the lifting of a morphism along the thickening
> `U_red ⟶ U`: a morphism of reductions over `X_red` is, by the fibre-product description
> `U'_red = U' ×_X X_red` of
> `AlgebraicGeometry.FormalSpace.isPullback_inclusion_liftSheafMap_map`, the same thing as a
> morphism `U_red ⟶ U'` over `X`, and such a morphism extends uniquely to `U ⟶ U'` over `X` by
> `AlgebraicGeometry.FormalSpace.existsUnique_hom_of_isRepresentableThickening`. In both
> directions the morphism of reductions is recovered from the extension by the characterisation
> `AlgebraicGeometry.FormalSpace.Reduction.eq_map`, so no naturality has to be checked.

```lean
theorem bijective_spacesEtaleComparison_map {X : FppfSheaf B S hS}
    (hX : IsFormalAlgebraicSpace B S hS X) (R : Reduction B S hS X)
    (U U' : RepresentableEtaleFormalSpacesOver X) :
    Function.Bijective fun f : U ⟶ U' ↦ (spacesEtaleComparison hX R).map f
```

**`AlgebraicGeometry.FormalSpace.faithful_spacesEtaleComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SpacesEtaleIdentificationSupplement.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SpacesEtaleIdentificationSupplement.lean#L292). The attribute's comment: “faithfulness of the comparison functor”.

> The comparison functor is faithful.

```lean
theorem faithful_spacesEtaleComparison {X : FppfSheaf B S hS}
    (hX : IsFormalAlgebraicSpace B S hS X) (R : Reduction B S hS X) :
    (spacesEtaleComparison hX R).Faithful
```

**`AlgebraicGeometry.FormalSpace.full_spacesEtaleComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SpacesEtaleIdentificationSupplement.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SpacesEtaleIdentificationSupplement.lean#L299). The attribute's comment: “fullness of the comparison functor”.

> The comparison functor is full.

```lean
theorem full_spacesEtaleComparison {X : FppfSheaf B S hS}
    (hX : IsFormalAlgebraicSpace B S hS X) (R : Reduction B S hS X) :
    (spacesEtaleComparison hX R).Full
```

**`AlgebraicGeometry.FormalSpace.spacesEtaleQuasiInverse`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SpacesEtaleQuasiInverse.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SpacesEtaleQuasiInverse.lean#L223). The attribute's comment: “the quasi-inverse `U_{V, ψ}` of the proof, as an fppf sheaf; that `U_{V, ψ} ⟶ X` is representable by algebraic spaces and étale is proved in StacksFrontier/AlgebraicGeometry/FormalSpace/SpacesEtaleQuasiInverseRepresentable.lean, that `U_{V, ψ}` is a formal algebraic space is not, see the implementation notes”.

> **Stacks 0DEG.** The quasi-inverse of the proof, at an object `ψ : V ⟶ X_red` of
> `X_{spaces, étale}`: the fppf sheaf `U_{V, ψ}` whose sections over `T` are the pairs `(a, b)`
> with `a : T ⟶ X` a morphism of formal algebraic spaces and
> `b : T ×_{a, X} X_red ⟶ V` a morphism over `X_red`.
>
> This is the functor the source writes down, as an fppf sheaf. That it is a sheaf is
> `AlgebraicGeometry.FormalSpace.isSheaf_liftAlongPresheaf`.

```lean
def spacesEtaleQuasiInverse {X : FppfSheaf B S hS} (R : Reduction B S hS X)
    (V : R.SpacesEtale) : FppfSheaf B S hS
```

**`AlgebraicGeometry.FormalSpace.spacesEtaleQuasiInverseBase`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SpacesEtaleQuasiInverse.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SpacesEtaleQuasiInverse.lean#L230). The attribute's comment: “the transformation `U_{V, ψ} ⟶ X`, `(a, b) ↦ a`”.

> **Stacks 0DEG.** The transformation `U_{V, ψ} ⟶ X`, `(a, b) ↦ a`, which the source claims
> defines an object of the category of formal algebraic spaces representable étale over `X`.

```lean
def spacesEtaleQuasiInverseBase {X : FppfSheaf B S hS} (R : Reduction B S hS X)
    (V : R.SpacesEtale) : spacesEtaleQuasiInverse B S hS R V ⟶ X
```

**`AlgebraicGeometry.FormalSpace.isPullback_spacesEtaleQuasiInverseSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SpacesEtaleQuasiInverse.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SpacesEtaleQuasiInverse.lean#L250). The attribute's comment: “the quasi-inverse is a right inverse: `U_{V, ψ} ×_X X_red = V` over `X_red`, which is one half of the source's 'the constructions are mutually inverse to each other'”.

> **Stacks 0DEG.** `V` is the fibre product `U_{V, ψ} ×_X X_red`.
>
> Since the comparison functor of Stacks 0DEG sends `φ : U ⟶ X` to `U ×_X X_red` — which is
> `AlgebraicGeometry.FormalSpace.isPullback_inclusion_liftSheafMap_map` — this says that the
> comparison functor applied to the quasi-inverse at `(V, ψ)` returns `(V, ψ)`. It is the half of
> the source's "the constructions are mutually inverse to each other" that does not need the
> lifting of morphisms along the thickening `X_red ⟶ X`.

```lean
theorem isPullback_spacesEtaleQuasiInverseSection {X : FppfSheaf B S hS}
    (R : Reduction B S hS X) (V : R.SpacesEtale) :
    IsPullback (spacesEtaleQuasiInverseSection B S hS R V)
      (liftSheafMap B S hS V.obj.hom) (spacesEtaleQuasiInverseBase B S hS R V) R.inclusion
```

**`AlgebraicGeometry.FormalSpace.spacesEtaleQuasiInverseFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SpacesEtaleQuasiInverse.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SpacesEtaleQuasiInverse.lean#L298). The attribute's comment: “the quasi-inverse as a functor into the slice over `X` — the source's 'thus we obtain our functor `(V, ψ) ↦ (U_{V, ψ} ⟶ X)` in the other direction'. That its values lie in the subcategory of the formal algebraic spaces representable étale over `X` is proved, in both of the source's assertions: `isRepresentableEtale_spacesEtaleQuasiInverseBase` here and `isFormalAlgebraicSpace_liftAlong` further down the import order; the codomain restriction and the equivalence assembled from them are `spacesEtaleComparison_isEquivalence`. The slice is an import-order artefact, not a missing step”.

> **Stacks 0DEG.** The quasi-inverse as a functor, which is what the source produces: an
> object `ψ : V ⟶ X_red` of `X_{spaces, étale}` goes to the formal-space-shaped sheaf
> `U_{V, ψ}` with its morphism to `X`, and a morphism of `X_{spaces, étale}` goes to the
> morphism over `X` obtained by postcomposition on the second component.
>
> It lands in the slice `Over X` rather than in the category of Stacks 0DEG for a reason of import
> order only. Both of the source's assertions about its values are proved: that the structure
> morphism is representable by algebraic spaces and étale is
> `AlgebraicGeometry.FormalSpace.isRepresentableEtale_spacesEtaleQuasiInverseBase`, and that
> `U_{V, ψ}` is a formal algebraic space is
> `AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_liftAlong`, which lives further down the
> import order, in `StacksFrontier/AlgebraicGeometry/FormalSpace/LiftAlongAffineBase.lean`. The
> equivalence assembled from them is there as well,
> `AlgebraicGeometry.FormalSpace.spacesEtaleComparison_isEquivalence`. See the module
> documentation.

```lean
def spacesEtaleQuasiInverseFunctor {X : FppfSheaf B S hS} (R : Reduction B S hS X) :
    R.SpacesEtale ⥤ Over X
```

**`AlgebraicGeometry.FormalSpace.isRepresentableEtale_spacesEtaleQuasiInverseBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SpacesEtaleQuasiInverseRepresentable.lean, line 471](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SpacesEtaleQuasiInverseRepresentable.lean#L471). The attribute's comment: “the omitted verification that `U_{V, ψ} ⟶ X` is representable by algebraic spaces and étale”.

> **Stacks 0DEG.** The structure morphism `U_{V, ψ} ⟶ X` of the quasi-inverse of the proof is
> representable by algebraic spaces and étale. This is one of the two verifications the source
> omits — "we omit the verification that `U_{V, ψ} ⟶ X` is representable by algebraic spaces and
> étale" — and it is proved here outright.

```lean
theorem isRepresentableEtale_spacesEtaleQuasiInverseBase {X : FppfSheaf B S hS}
    (R : Reduction B S hS X) (V : R.SpacesEtale) :
    IsRepresentableEtale B S hS (spacesEtaleQuasiInverseBase B S hS R V)
```

## Tag 0DEH, a lemma

[Tag 0DEH](https://stacks.math.columbia.edu/tag/0DEH) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.affineEtaleReductionEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffineEtaleReductionEquivalence.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AffineEtaleReductionEquivalence.lean#L241).

> **Stacks 0DEH.** Let `S` be a scheme and `X` a formal algebraic space over `S`. Then
> `X_{affine, étale}` is equivalent to the category whose objects are the morphisms `φ : U ⟶ X`
> of formal algebraic spaces with `U` an affine formal algebraic space and `φ` representable by
> algebraic spaces and étale; the equivalence is the functor `U ↦ U_red`,
> `AlgebraicGeometry.FormalSpace.affineEtaleReductionFunctor`.

```lean
def affineEtaleReductionEquivalence {X : FppfSheaf B S hS}
    (hX : IsFormalAlgebraicSpace B S hS X) (R : Reduction B S hS X) :
    AffineEtaleFormalCharts B S hS X ≌ R.AffineEtale
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.34, Tag 0DE9](https://stacks.math.columbia.edu/tag/0DE9)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
