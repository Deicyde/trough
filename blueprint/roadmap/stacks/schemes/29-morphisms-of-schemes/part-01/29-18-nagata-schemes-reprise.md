---
declaration: section
origin: cited
lean: AlgebraicGeometry.isUniversallyJapaneseScheme_of_locallyOfFiniteType, AlgebraicGeometry.isNagataScheme_of_locallyOfFiniteType, AlgebraicGeometry.isNagataScheme_of_locallyOfFiniteType_over_isPrecomplete, AlgebraicGeometry.isNagataScheme_of_locallyOfFiniteType_over_int, AlgebraicGeometry.isNagataScheme_of_locallyOfFiniteType_over_uliftInt, AlgebraicGeometry.isNagataScheme_of_locallyOfFiniteType_over_isDedekindDomain_of_charZero, AlgebraicGeometry.isNagataScheme_of_locallyOfFiniteType_over_field, isNagataScheme_of_isNagataRing
statement: formalized
proof: formalized
---

# 29.18 Nagata schemes, reprise

Section 29.18 of the Stacks Project, [Tag 0359](https://stacks.math.columbia.edu/tag/0359). 2 tags here are carried by 7 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 035A, a lemma

[Tag 035A](https://stacks.math.columbia.edu/tag/035A) in the Stacks Project.

**`AlgebraicGeometry.isUniversallyJapaneseScheme_of_locallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/UniversallyJapanese.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/UniversallyJapanese.lean#L42). The attribute's comment: “universally_japanese”. References: EGA IV (7.7.2), “finite type stability”.

> **Stacks Project, Tag 035A (universally Japanese case).** The source of a locally finite type
> morphism to a universally Japanese scheme is universally Japanese.

```lean
public theorem isUniversallyJapaneseScheme_of_locallyOfFiniteType {X S : Scheme.{u}}
    (f : X ⟶ S) [LocallyOfFiniteType f] (hS : IsUniversallyJapaneseScheme S) :
    IsUniversallyJapaneseScheme X
```

**`AlgebraicGeometry.isNagataScheme_of_locallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NagataNormalization/FiniteType.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NagataNormalization/FiniteType.lean#L51). The attribute's comment: “nagata”. References: EGA IV (7.7.2), “finite type stability”.

> **Stacks Project, Tag 035A (Nagata case).** The source of a locally finite type morphism to a
> Nagata scheme is Nagata.

```lean
theorem isNagataScheme_of_locallyOfFiniteType {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (hS : IsNagataScheme S) : IsNagataScheme X
```

## Tag 035B, a lemma

[Tag 035B](https://stacks.math.columbia.edu/tag/035B) in the Stacks Project.

**`AlgebraicGeometry.isNagataScheme_of_locallyOfFiniteType_over_isPrecomplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NagataNormalization/Examples.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NagataNormalization/Examples.lean#L64). The attribute's comment: “(2) A scheme locally of finite type over a Noetherian complete local ring; completeness is `IsPrecomplete (IsLocalRing.maximalIdeal R) R`, the hypothesis of Tag 032W.”.

> **Stacks Project, Tag 035B (2).** A scheme locally of finite type over a Noetherian complete
> local ring is a Nagata scheme: such a ring is Nagata by Tag 032W.

```lean
theorem isNagataScheme_of_locallyOfFiniteType_over_isPrecomplete (R : Type u) [CommRing R]
    [IsNoetherianRing R] [IsLocalRing R] [IsPrecomplete (IsLocalRing.maximalIdeal R) R]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of R)) [LocallyOfFiniteType f] : IsNagataScheme X
```

**`AlgebraicGeometry.isNagataScheme_of_locallyOfFiniteType_over_int`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NagataNormalization/Examples.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NagataNormalization/Examples.lean#L74). The attribute's comment: “(3) A scheme locally of finite type over `ℤ`, for the base `Spec ℤ`, which forces the source to live at universe 0; `isNagataScheme_of_locallyOfFiniteType_over_uliftInt` is the same statement for a source at an arbitrary universe.”.

> **Stacks Project, Tag 035B (3).** A scheme locally of finite type over `ℤ` is a Nagata
> scheme: `ℤ` is a Nagata ring by Tag 0335 (3).

```lean
theorem isNagataScheme_of_locallyOfFiniteType_over_int {X : Scheme.{0}} (f : X ⟶ Spec (.of ℤ))
    [LocallyOfFiniteType f] : IsNagataScheme X
```

**`AlgebraicGeometry.isNagataScheme_of_locallyOfFiniteType_over_uliftInt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NagataNormalization/Examples.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NagataNormalization/Examples.lean#L82). The attribute's comment: “(3) A scheme locally of finite type over `ℤ` with the source at an arbitrary universe, the base being `Spec (ULift ℤ)`, the terminal scheme.”.

> **Stacks Project, Tag 035B (3), at an arbitrary universe.** A scheme locally of finite type
> over `Spec (ULift ℤ)`, the terminal scheme, is a Nagata scheme.

```lean
theorem isNagataScheme_of_locallyOfFiniteType_over_uliftInt {X : Scheme.{u}}
    (f : X ⟶ Spec (.of (ULift.{u} ℤ))) [LocallyOfFiniteType f] : IsNagataScheme X
```

**`AlgebraicGeometry.isNagataScheme_of_locallyOfFiniteType_over_isDedekindDomain_of_charZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NagataNormalization/Examples.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NagataNormalization/Examples.lean#L92). The attribute's comment: “(4) A scheme locally of finite type over a Dedekind ring of characteristic zero, the characteristic condition read as `CharZero R` as in Tag 0335 (4).”.

> **Stacks Project, Tag 035B (4).** A scheme locally of finite type over a Dedekind domain
> whose fraction field has characteristic zero is a Nagata scheme: such a ring is Nagata by
> Tag 0335 (4).

```lean
theorem isNagataScheme_of_locallyOfFiniteType_over_isDedekindDomain_of_charZero (R : Type u)
    [CommRing R] [IsDedekindDomain R] [CharZero R] {X : Scheme.{u}} (f : X ⟶ Spec (.of R))
    [LocallyOfFiniteType f] : IsNagataScheme X
```

**`AlgebraicGeometry.isNagataScheme_of_locallyOfFiniteType_over_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NagataNormalization/FiniteType.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NagataNormalization/FiniteType.lean#L76). The attribute's comment: “field”.

> **Stacks Project, Tag 035B (field case).** A scheme locally of finite type over a field is
> Nagata.

```lean
theorem isNagataScheme_of_locallyOfFiniteType_over_field (k : Type u) [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [LocallyOfFiniteType f] : IsNagataScheme X
```

Declarations registered for the tag:

- [`isNagataScheme_of_isNagataRing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isNagataScheme_of_isNagataRing#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/NagataNormalization/Examples.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NagataNormalization/Examples.lean#L99) (StacksFrontier): “(5) "And so on": a scheme locally of finite type over an arbitrary Nagata ring.”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.18, Tag 0359](https://stacks.math.columbia.edu/tag/0359)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
