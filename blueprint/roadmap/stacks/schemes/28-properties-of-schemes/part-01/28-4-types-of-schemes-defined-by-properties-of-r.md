---
declaration: section
origin: cited
lean: CommRing.PropertyIsLocal, AlgebraicGeometry.IsLocally, AlgebraicGeometry.isLocally_iff_forall_affineOpens, AlgebraicGeometry.isLocally_iff_exists_affineOpenCover, AlgebraicGeometry.isLocally_open, AlgebraicGeometry.isLocally_iff_exists_openCover, AlgebraicGeometry.isReduced_iff_isLocally_isReduced, CommRing.finiteType_int_isLocal
statement: formalized
proof: formalized
---

# 28.4 Types of schemes defined by properties of rings

Section 28.4 of the Stacks Project, [Tag 01OO](https://stacks.math.columbia.edu/tag/01OO). 5 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01OP, a definition

[Tag 01OP](https://stacks.math.columbia.edu/tag/01OP) in the Stacks Project.

**`CommRing.PropertyIsLocal`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/LocalRingProperty.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/LocalRingProperty.lean#L81).

> A property of commutative rings is local if it is preserved by localization away from
> an element and descends from every finite family of such localizations whose elements
> generate the unit ideal.

```lean
structure PropertyIsLocal (P : ∀ (R : Type u) [CommRing R], Prop) : Prop
```

## Tag 01OQ, a definition

[Tag 01OQ](https://stacks.math.columbia.edu/tag/01OQ) in the Stacks Project.

**`AlgebraicGeometry.IsLocally`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/LocalRingProperty.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/LocalRingProperty.lean#L206).

> A scheme is locally `P` if every point belongs to an affine open whose ring of sections
> satisfies `P`.

```lean
abbrev IsLocally (P : (R : Type u) → [CommRing R] → Prop) (X : Scheme.{u}) :
    Prop
```

## Tag 01OR, a lemma

[Tag 01OR](https://stacks.math.columbia.edu/tag/01OR) in the Stacks Project.

**`AlgebraicGeometry.isLocally_iff_forall_affineOpens`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NagataNormalization/LocalProperty.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/NagataNormalization/LocalProperty.lean#L153). The attribute's comment: “part (1) iff part (2)”.

> **Stacks Project, Tag 01OR (part (1) iff part (2)).** A scheme locally satisfies a local ring
> property precisely when the ring of sections over every affine open satisfies it.

```lean
theorem isLocally_iff_forall_affineOpens (hP : CommRing.PropertyIsLocal P) (X : Scheme.{u}) :
    IsLocally P X ↔ ∀ U : X.affineOpens, P Γ(X, U.1)
```

**`AlgebraicGeometry.isLocally_iff_exists_affineOpenCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NagataNormalization/LocalProperty.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/NagataNormalization/LocalProperty.lean#L163). The attribute's comment: “part (1) iff part (3)”.

> **Stacks Project, Tag 01OR (part (1) iff part (3)).** A scheme locally satisfies a ring
> property precisely when it has an affine open cover on whose rings of sections the property
> holds.

```lean
theorem isLocally_iff_exists_affineOpenCover (P : (R : Type u) → [CommRing R] → Prop)
    (X : Scheme.{u}) :
    IsLocally P X ↔
      ∃ (ι : Type u) (U : ι → X.affineOpens),
        IsOpenCover (fun i ↦ (U i : X.Opens)) ∧ ∀ i, P Γ(X, (U i).1)
```

**`AlgebraicGeometry.isLocally_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NagataNormalization/LocalProperty.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/NagataNormalization/LocalProperty.lean#L176). The attribute's comment: “open subschemes”.

> **Stacks Project, Tag 01OR (open subschemes).** Every open subscheme of a scheme locally
> satisfying a local ring property also locally satisfies that property.

```lean
theorem isLocally_open (hP : CommRing.PropertyIsLocal P) (X : Scheme.{u}) (hX : IsLocally P X)
    (U : X.Opens) : IsLocally P U.toScheme
```

**`AlgebraicGeometry.isLocally_iff_exists_openCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NagataNormalization/LocalProperty.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/NagataNormalization/LocalProperty.lean#L187). The attribute's comment: “part (1) iff part (4)”.

> **Stacks Project, Tag 01OR (part (1) iff part (4)).** A scheme locally satisfies a local ring
> property precisely when it has an open cover by open subschemes locally satisfying the
> property.

```lean
theorem isLocally_iff_exists_openCover (hP : CommRing.PropertyIsLocal P) (X : Scheme.{u}) :
    IsLocally P X ↔
      ∃ (ι : Type u) (U : ι → X.Opens),
        IsOpenCover U ∧ ∀ i, IsLocally P (U i).toScheme
```

## Tag 01OS, a lemma

[Tag 01OS](https://stacks.math.columbia.edu/tag/01OS) in the Stacks Project.

**`AlgebraicGeometry.isReduced_iff_isLocally_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/LocalRingProperty.lean, line 215](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/LocalRingProperty.lean#L215). The attribute's comment: “Both directions, for an arbitrary scheme and with no further hypotheses: `AlgebraicGeometry.IsReduced X` is equivalent to `IsLocally` applied to reducedness of rings, which is `locally reduced` in the sense of Definition 01OQ.”.

> A scheme is reduced exactly when it is locally reduced: every point has an affine open
> neighbourhood whose ring of sections is a reduced ring.

```lean
theorem isReduced_iff_isLocally_isReduced (X : Scheme.{u}) :
    IsReduced X ↔ IsLocally (fun (R : Type u) [CommRing R] => _root_.IsReduced R) X
```

## Tag 01OT, a lemma

[Tag 01OT](https://stacks.math.columbia.edu/tag/01OT) in the Stacks Project.

**`CommRing.finiteType_int_isLocal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/LocalRingProperty.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/LocalRingProperty.lean#L97). The attribute's comment: “part (3) (absolutely Noetherian): being of finite type over ℤ is a local property”.

> Being a finite-type algebra over the integers is a local property of
> commutative rings.

```lean
theorem finiteType_int_isLocal :
    PropertyIsLocal
      (fun (R : Type u) [CommRing R] => Algebra.FiniteType ℤ R)
```

**`CommRing.isNoetherianCohenMacaulayRing_propertyIsLocal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/LocalRingProperty.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/LocalRingProperty.lean#L158). The attribute's comment: “part (1) (Cohen-Macaulay): being Noetherian and Cohen-Macaulay is a local property”.

> The property of a commutative ring of being Noetherian and Cohen–Macaulay is local.

```lean
public theorem isNoetherianCohenMacaulayRing_propertyIsLocal :
    PropertyIsLocal
      (fun (R : Type u) [hR : CommRing R] =>
        ∃ hN : IsNoetherianRing R, @IsCohenMacaulayRing R hR hN)
```

**`CommRing.isRegularRing_propertyIsLocal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/LocalRingProperty.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/LocalRingProperty.lean#L184). The attribute's comment: “part (2) (regular): being Noetherian and regular is a local property”.

> Being a Noetherian regular ring is local on the spectrum.

```lean
theorem isRegularRing_propertyIsLocal :
    PropertyIsLocal (fun (R : Type u) [CommRing R] => IsRegularRing R)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 28.4, Tag 01OO](https://stacks.math.columbia.edu/tag/01OO)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
