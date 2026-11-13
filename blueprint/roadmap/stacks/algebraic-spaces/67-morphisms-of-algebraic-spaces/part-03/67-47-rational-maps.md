---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.PartialMap.Equivalent, AlgebraicGeometry.Space.PartialMap.equivalence_equivalent, AlgebraicGeometry.Space.RationalMap, AlgebraicGeometry.Space.RationalMap.IsOver, AlgebraicGeometry.Space.rationalFunctions, AlgebraicGeometry.Space.rationalFunctionsRing, AlgebraicGeometry.Space.RationalMap.IsDefinedAt, AlgebraicGeometry.Space.RationalMap.domainOfDefinition
statement: formalized
proof: formalized
---

# 67.47 Rational maps

Section 67.47 of the Stacks Project, [Tag 0EML](https://stacks.math.columbia.edu/tag/0EML). 8 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EMM, a definition

[Tag 0EMM](https://stacks.math.columbia.edu/tag/0EMM) in the Stacks Project.

**`AlgebraicGeometry.Space.PartialMap.Equivalent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RationalFunctions.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RationalFunctions.lean#L173). The attribute's comment: “part (1): equivalence of representatives”. References: EGA I (7.1.1), “equivalence definition”.

> Two partial maps agree after restriction to a common dense open subspace.

```lean
def Equivalent (f g : PartialMap B S hS hX Y) : Prop
```

**`AlgebraicGeometry.Space.PartialMap.equivalence_equivalent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RationalFunctions.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RationalFunctions.lean#L186). The attribute's comment: “part (1): equivalence relation”. References: EGA I (7.1.1), “is an equivalence rel.”.

> **Stacks 0EMM, part (1).** Agreement on a common dense open subspace is an equivalence
> relation.
>
> Transitivity restricts to the dense open subspace common to the two witnesses, which exists
> by `AlgebraicGeometry.Space.exists_isDenseOpenSubspace_le`.

```lean
theorem equivalence_equivalent :
    Equivalence (Equivalent B S hS (X := X) (Y := Y) (hX := hX))
```

**`AlgebraicGeometry.Space.RationalMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RationalFunctions.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RationalFunctions.lean#L214). The attribute's comment: “part (2): rational maps”. References: EGA I (7.1.2), “rational map”.

> **Stacks 0EMM, part (2).** A rational map of algebraic spaces is a class of dense-open
> representatives.

```lean
def RationalMap (hX : IsAlgebraicSpace B S hS X)
    (Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) : Type _
```

**`AlgebraicGeometry.Space.RationalMap.IsOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RationalFunctions.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RationalFunctions.lean#L250). The attribute's comment: “part (3): relative rational maps”.

> **Stacks 0EMM, part (3).** A rational map is over another algebraic space if one
> representative is.

```lean
abbrev IsOver {T : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (xToT : X ⟶ T) (yToT : Y ⟶ T)
    (φ : RationalMap B S hS hX Y) : Prop
```

## Tag 0EMN, a definition

[Tag 0EMN](https://stacks.math.columbia.edu/tag/0EMN) in the Stacks Project.

**`AlgebraicGeometry.Space.rationalFunctions`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RationalFunctions.lean, line 490](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RationalFunctions.lean#L490). The attribute's comment: “rational functions as rational maps to the relative affine line”.

> A rational function is a rational map to the relative affine line.

```lean
noncomputable abbrev rationalFunctions (hX : IsAlgebraicSpace B S hS X) : Type (u + 1)
```

## Tag 0EMP, a definition

[Tag 0EMP](https://stacks.math.columbia.edu/tag/0EMP) in the Stacks Project.

**`AlgebraicGeometry.Space.rationalFunctionsRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RationalFunctions.lean, line 499](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RationalFunctions.lean#L499).

> **Stacks 0EMP.** Pointwise ring operations on common dense-open representatives
> determine the commutative ring structure on rational functions.
>
> The ring is the direct limit of the rings of sections over the dense open subspaces, which
> is a directed system because two dense open subspaces contain a common one.

```lean
theorem rationalFunctionsRing (hX : IsAlgebraicSpace B S hS X) :
    ∃ R : CommRing (rationalFunctions B S hS hX),
      letI := R
      (∀ (U : Subfunctor X) (hU : IsDenseOpenSubspace B S hS hX U)
          (f g : U.toFunctor ⟶ affineLineFunctor B S hS),
        ∃ a m : U.toFunctor ⟶ affineLineFunctor B S hS,
          (∀ T x, affineLineCoordinate B S hS T (a.app T x) =
            affineLineCoordinate B S hS T (f.app T x) +
              affineLineCoordinate B S hS T (g.app T x)) ∧
          (∀ T x, affineLineCoordinate B S hS T (m.app T x) =
            affineLineCoordinate B S hS T (f.app T x) *
              affineLineCoordinate B S hS T (g.app T x)) ∧
          (PartialMap.toRationalMap B S hS
            (⟨U, hU, a⟩ : PartialMap B S hS hX (affineLineFunctor B S hS)) =
            PartialMap.toRationalMap B S hS
              (⟨U, hU, f⟩ : PartialMap B S hS hX (affineLineFunctor B S hS)) +
            PartialMap.toRationalMap B S hS
              (⟨U, hU, g⟩ : PartialMap B S hS hX (affineLineFunctor B S hS))) ∧
          (PartialMap.toRationalMap B S hS
            (⟨U, hU, m⟩ : PartialMap B S hS hX (affineLineFunctor B S hS)) =
            PartialMap.toRationalMap B S hS
              (⟨U, hU, f⟩ : PartialMap B S hS hX (affineLineFunctor B S hS)) *
            PartialMap.toRationalMap B S hS
              (⟨U, hU, g⟩ : PartialMap B S hS hX (affineLineFunctor B S hS)))) ∧
      (∀ (U : Subfunctor X) (hU : IsDenseOpenSubspace B S hS hX U),
        ∃ z o : U.toFunctor ⟶ affineLineFunctor B S hS,
          (∀ T x, affineLineCoordinate B S hS T (z.app T x) = 0) ∧
          (∀ T x, affineLineCoordinate B S hS T (o.app T x) = 1) ∧
          (PartialMap.toRationalMap B S hS
            (⟨U, hU, z⟩ : PartialMap B S hS hX (affineLineFunctor B S hS)) = 0) ∧
          (PartialMap.toRationalMap B S hS
            (⟨U, hU, o⟩ : PartialMap B S hS hX (affineLineFunctor B S hS)) = 1)) ∧
      (∀ (U : Subfunctor X) (hU : IsDenseOpenSubspace B S hS hX U)
          (f : U.toFunctor ⟶ affineLineFunctor B S hS),
        ∃ n : U.toFunctor ⟶ affineLineFunctor B S hS,
          (∀ T x, affineLineCoordinate B S hS T (n.app T x) =
            -affineLineCoordinate B S hS T (f.app T x)) ∧
          (PartialMap.toRationalMap B S hS
            (⟨U, hU, n⟩ : PartialMap B S hS hX (affineLineFunctor B S hS)) =
            -PartialMap.toRationalMap B S hS
              (⟨U, hU, f⟩ : PartialMap B S hS hX (affineLineFunctor B S hS))))
```

## Tag 0EMQ, a definition

[Tag 0EMQ](https://stacks.math.columbia.edu/tag/0EMQ) in the Stacks Project.

**`AlgebraicGeometry.Space.RationalMap.IsDefinedAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RationalMaps.lean, line 211](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RationalMaps.lean#L211). The attribute's comment: “defined at a point”. References: EGA I (7.2.1), “defined at a point”; EGA IV (20.2.3), “defined at a point”.

> A rational map is *defined at a point* of its source when it has a representative whose
> domain contains that point.

```lean
abbrev IsDefinedAt (φ : RationalMap B S hS hX Y) (x : points B S hS X) : Prop
```

**`AlgebraicGeometry.Space.RationalMap.domainOfDefinition`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RationalMaps.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RationalMaps.lean#L219). The attribute's comment: “domain of definition”. References: EGA I (7.2.1), “domain of definition”; EGA IV (20.2.3), “dom(ω)”.

> The *domain of definition* of a rational map is the set of points at which it is defined.

```lean
abbrev domainOfDefinition (φ : RationalMap B S hS hX Y) : Set (points B S hS X)
```

## Tag 0EMR, a lemma

[Tag 0EMR](https://stacks.math.columbia.edu/tag/0EMR) in the Stacks Project.

**`AlgebraicGeometry.Space.existsUnique_hom_of_eq_domainOfDefinition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RationalMapDomainOfDefinition.lean, line 401](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RationalMapDomainOfDefinition.lean#L401). References: EGA I (7.2.2).

> **Stacks 0EMR.** Let `X` be a reduced algebraic space over `S` and let `Y` be an algebraic
> space separated over `S`. A rational map from `X` to `Y` is represented by exactly one morphism
> on the open subspace of `X` whose point set is its domain of definition.

```lean
theorem existsUnique_hom_of_eq_domainOfDefinition
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hXred : HasEtaleLocalProperty B S hS X (fun T : Scheme.{u} => IsReduced T))
    (hYsep : IsSeparatedOver B S hS Y)
    (φ : RationalMap B S hS hX Y)
    (U : Subfunctor X) (hU : IsOpenSubspace B S hS U)
    (hUdom : Set.range (pointsMap B S hS U.toFunctor U.ι) =
      RationalMap.domainOfDefinition B S hS φ) :
    ∃! f : U.toFunctor ⟶ Y, ∃ hUd : IsDenseOpenSubspace B S hS hX U,
      PartialMap.toRationalMap B S hS ⟨U, hUd, f⟩ = φ
```

## Tag 0EMS, a definition

[Tag 0EMS](https://stacks.math.columbia.edu/tag/0EMS) in the Stacks Project.

**`AlgebraicGeometry.Space.RationalMap.IsDominant`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RationalMaps.lean, line 225](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RationalMaps.lean#L225).

> A rational map is *dominant* when every one of its dense-open representatives is a dominant
> morphism.

```lean
abbrev IsDominant (φ : RationalMap B S hS hX Y) : Prop
```

## Tag 0EMT, a definition

[Tag 0EMT](https://stacks.math.columbia.edu/tag/0EMT) in the Stacks Project.

**`AlgebraicGeometry.Space.Birational`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RationalMaps.lean, line 273](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RationalMaps.lean#L273).

> Two algebraic spaces over `S` with irreducible point spaces are *birational* when they have
> mutually inverse dominant rational maps: two dominant rational maps whose composites agree with
> the respective identities on dense open subspaces.

```lean
abbrev Birational (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (_hXirr : IrreducibleSpace (points B S hS X))
    (_hYirr : IrreducibleSpace (points B S hS Y)) : Prop
```

## Tag 0EMU, a lemma

[Tag 0EMU](https://stacks.math.columbia.edu/tag/0EMU) in the Stacks Project.

**`AlgebraicGeometry.Space.birational_iff_exists_isOpenSubspace_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RationalMaps.lean, line 319](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RationalMaps.lean#L319).

> Two algebraic spaces over `S` with irreducible point spaces are birational if and only if
> they contain nonempty open subspaces which are isomorphic as algebraic spaces over `S`.

```lean
theorem birational_iff_exists_isOpenSubspace_iso (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (hXirr : IrreducibleSpace (points B S hS X))
    (hYirr : IrreducibleSpace (points B S hS Y)) :
    Birational B S hS hX hY hXirr hYirr ↔
      ∃ (U : Subfunctor X) (V : Subfunctor Y), IsOpenSubspace B S hS U ∧
        IsOpenSubspace B S hS V ∧ Nonempty (points B S hS U.toFunctor) ∧
        Nonempty (points B S hS V.toFunctor) ∧ Nonempty (U.toFunctor ≅ V.toFunctor)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.47, Tag 0EML](https://stacks.math.columbia.edu/tag/0EML)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
