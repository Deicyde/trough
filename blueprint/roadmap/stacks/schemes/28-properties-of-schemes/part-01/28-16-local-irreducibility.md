---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsUnibranchAt, AlgebraicGeometry.IsGeometricallyUnibranchAt, AlgebraicGeometry.IsUnibranch, AlgebraicGeometry.IsGeometricallyUnibranch, AlgebraicGeometry.isGeometricallyUnibranch_of_isNormal, AlgebraicGeometry.isGeometricallyUnibranch_iff_isConnected_puncturedSpectrum, AlgebraicGeometry.numberOfBranches, AlgebraicGeometry.numberOfGeometricBranches
statement: formalized
proof: formalized
---

# 28.16 Local irreducibility

Section 28.16 of the Stacks Project, [Tag 0BQ1](https://stacks.math.columbia.edu/tag/0BQ1). 6 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BQ2, a definition

[Tag 0BQ2](https://stacks.math.columbia.edu/tag/0BQ2) in the Stacks Project.

**`AlgebraicGeometry.IsUnibranchAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Unibranch.lean, line 284](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Unibranch.lean#L284). The attribute's comment: “unibranch at a point”. References: EGA IV (6.15.1).

> A scheme is unibranch at a point if its local ring there is unibranch.

```lean
public abbrev IsUnibranchAt
    (X : AlgebraicGeometry.Scheme.{u}) (x : X) : Prop
```

**`AlgebraicGeometry.IsGeometricallyUnibranchAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Unibranch.lean, line 292](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Unibranch.lean#L292). The attribute's comment: “geometrically unibranch at a point”. References: EGA IV (6.15.1), “geom. unibranch at x”.

> A scheme is geometrically unibranch at a point if its local ring there is geometrically
> unibranch.

```lean
public abbrev IsGeometricallyUnibranchAt
    (X : AlgebraicGeometry.Scheme.{u}) (x : X) : Prop
```

**`AlgebraicGeometry.IsUnibranch`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Unibranch.lean, line 300](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Unibranch.lean#L300). The attribute's comment: “unibranch schemes”. References: EGA III (4.3.6), “unibranch point”; EGA IV (6.15.1), “unibranch, global”.

> A scheme is unibranch if it is unibranch at every point.

```lean
public abbrev IsUnibranch
    (X : AlgebraicGeometry.Scheme.{u}) : Prop
```

**`AlgebraicGeometry.IsGeometricallyUnibranch`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Unibranch.lean, line 307](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Unibranch.lean#L307). The attribute's comment: “geometrically unibranch schemes”. References: EGA IV (6.15.1), “geom. unibranch, global”; SGA 3 X (5.14.0).

> A scheme is geometrically unibranch if it is geometrically unibranch at every point.

```lean
public abbrev IsGeometricallyUnibranch
    (X : AlgebraicGeometry.Scheme.{u}) : Prop
```

## Tag 0BQ3, a lemma

[Tag 0BQ3](https://stacks.math.columbia.edu/tag/0BQ3) in the Stacks Project.

**`AlgebraicGeometry.isGeometricallyUnibranch_of_isNormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Unibranch.lean, line 572](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Unibranch.lean#L572). References: EGA III (4.3.6), “normal ⇒ unibranch”; EGA IV (6.15.6), “k' = k”; SGA 4 IX (2.14.1); SGA 4 XVII (6.2.6), “more general”.

> A normal scheme is geometrically unibranch.

```lean
public theorem isGeometricallyUnibranch_of_isNormal {X : Scheme.{u}}
    [IsNormal X] : IsGeometricallyUnibranch X
```

## Tag 0BQ4, a lemma

[Tag 0BQ4](https://stacks.math.columbia.edu/tag/0BQ4) in the Stacks Project.

**`AlgebraicGeometry.isGeometricallyUnibranch_iff_isConnected_puncturedSpectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/UnibranchPuncturedSpectrum.lean, line 415](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/UnibranchPuncturedSpectrum.lean#L415).

> A locally Noetherian scheme is geometrically unibranch exactly when, at every point which is
> not the generic point of an irreducible component, the punctured spectrum of a strict
> henselization of the local ring is connected.

```lean
theorem isGeometricallyUnibranch_iff_isConnected_puncturedSpectrum
    (X : Scheme.{u}) [IsLocallyNoetherian X] :
    IsGeometricallyUnibranch X ↔
      ∀ x : X, x ∉ genericPoints X →
        ∀ (κsep : Type u) [Field κsep] [Algebra (ResidueField (X.presheaf.stalk x)) κsep]
          [IsSepClosure (ResidueField (X.presheaf.stalk x)) κsep]
          (Ash : Type u) [CommRing Ash] [IsLocalRing Ash]
          [Algebra (X.presheaf.stalk x) Ash]
          [IsHenselization (X.presheaf.stalk x) κsep Ash],
          IsConnected ({closedPoint Ash}ᶜ : Set (PrimeSpectrum Ash))
```

## Tag 0C38, a definition

[Tag 0C38](https://stacks.math.columbia.edu/tag/0C38) in the Stacks Project.

**`AlgebraicGeometry.numberOfBranches`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Unibranch.lean, line 314](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Unibranch.lean#L314). The attribute's comment: “number of branches”.

> The number of branches of a scheme at a point is the number of branches of its local ring at
> that point.

```lean
public noncomputable abbrev numberOfBranches (X : AlgebraicGeometry.Scheme.{u}) (x : X) : ℕ∞
```

**`AlgebraicGeometry.numberOfGeometricBranches`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Unibranch.lean, line 320](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Unibranch.lean#L320). The attribute's comment: “number of geometric branches”.

> The number of geometric branches of a scheme at a point is the number of geometric branches
> of its local ring at that point.

```lean
public noncomputable abbrev numberOfGeometricBranches
    (X : AlgebraicGeometry.Scheme.{u}) (x : X) : ℕ∞
```

## Tag 0E20, a lemma

[Tag 0E20](https://stacks.math.columbia.edu/tag/0E20) in the Stacks Project.

**`AlgebraicGeometry.numberOfGeometricBranches_eq_iSup_sum_components`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/PrincipalOpens/GeometricBranches.lean, line 1042](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/PrincipalOpens/GeometricBranches.lean#L1042). The attribute's comment: “geometric\_branches\_sum”.

> The geometric branches at a point are the geometric branches of its reduced irreducible
> components through that point, counted with multiplicity one per component.

```lean
public theorem numberOfGeometricBranches_eq_iSup_sum_components
    (X : Scheme.{u}) (x : X) :
    numberOfGeometricBranches X x =
      ⨆ s : Finset {Z : Set X // Z ∈ irreducibleComponents X ∧ x ∈ Z},
        ∑ Z ∈ s,
        let C : Closeds X :=
          ⟨Z.1, isClosed_of_mem_irreducibleComponents Z.1 Z.property.1⟩
        let I := Scheme.IdealSheafData.vanishingIdeal C
        numberOfGeometricBranches I.subscheme
          (⟨x, by
            change x ∈ ((Scheme.IdealSheafData.vanishingIdeal C).support : Set X)
            have h := Scheme.IdealSheafData.coe_support_vanishingIdeal C
            exact h.symm ▸ (show x ∈ (C : Set X) from Z.property.2)⟩ : I.subscheme)
```

**`AlgebraicGeometry.numberOfBranches_eq_iSup_sum_components`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/PrincipalOpens/GeometricBranches.lean, line 1093](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/PrincipalOpens/GeometricBranches.lean#L1093). The attribute's comment: “branches\_sum”.

> The branches at a point are the branches of its reduced irreducible components through that
> point, counted with multiplicity one per component.

```lean
public theorem numberOfBranches_eq_iSup_sum_components
    (X : Scheme.{u}) (x : X) :
    numberOfBranches X x =
      ⨆ s : Finset {Z : Set X // Z ∈ irreducibleComponents X ∧ x ∈ Z},
        ∑ Z ∈ s,
        let C : Closeds X :=
          ⟨Z.1, isClosed_of_mem_irreducibleComponents Z.1 Z.property.1⟩
        let I := Scheme.IdealSheafData.vanishingIdeal C
        numberOfBranches I.subscheme
          (⟨x, by
            change x ∈ ((Scheme.IdealSheafData.vanishingIdeal C).support : Set X)
            have h := Scheme.IdealSheafData.coe_support_vanishingIdeal C
            exact h.symm ▸ (show x ∈ (C : Set X) from Z.property.2)⟩ : I.subscheme)
```

## Tag 0C39, a lemma

[Tag 0C39](https://stacks.math.columbia.edu/tag/0C39) in the Stacks Project.

**`AlgebraicGeometry.numberOfBranches_eq_one_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Unibranch.lean, line 511](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Unibranch.lean#L511). The attribute's comment: “part (1)”.

> A scheme has exactly one branch at a point if and only if it is unibranch at that point.

```lean
public theorem numberOfBranches_eq_one_iff (X : Scheme.{u}) (x : X) :
    numberOfBranches X x = 1 ↔ IsUnibranchAt X x
```

**`AlgebraicGeometry.numberOfGeometricBranches_eq_one_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Unibranch.lean, line 518](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Unibranch.lean#L518). The attribute's comment: “part (2)”.

> A scheme has exactly one geometric branch at a point if and only if it is geometrically
> unibranch at that point.

```lean
public theorem numberOfGeometricBranches_eq_one_iff (X : Scheme.{u}) (x : X) :
    numberOfGeometricBranches X x = 1 ↔ IsGeometricallyUnibranchAt X x
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 28.16, Tag 0BQ1](https://stacks.math.columbia.edu/tag/0BQ1)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
