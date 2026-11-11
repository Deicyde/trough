---
declaration: section
origin: cited
lean: AlgebraicGeometry.finiteTypeAt, AlgebraicGeometry.LocallyOfFiniteType, AlgebraicGeometry.QuasiCompact, AlgebraicGeometry.locallyOfFiniteType_iff, AlgebraicGeometry.locallyOfFiniteType_comp, AlgebraicGeometry.quasiCompact_comp, AlgebraicGeometry.locallyOfFiniteType_isStableUnderBaseChange, AlgebraicGeometry.quasiCompact_isStableUnderBaseChange
statement: formalized
proof: formalized
---

# 29.15 Morphisms of finite type

Section 29.15 of the Stacks Project, [Tag 01T0](https://stacks.math.columbia.edu/tag/01T0). 8 tags here are carried by 3 declarations of the repository (all in StacksFrontier) and 10 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01T1, a definition

[Tag 01T1](https://stacks.math.columbia.edu/tag/01T1) in the Stacks Project.

**`AlgebraicGeometry.finiteTypeAt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteTypePoint.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteTypePoint.lean#L70). The attribute's comment: “part (1)”. References: EGA IV (1.3.2), “finite type at x”.

> A morphism of schemes is of finite type at `x` if it induces a finite-type ring map on
> some affine open neighbourhood of `x` mapping into an affine open of the target.

```lean
def finiteTypeAt {X Y : Scheme.{u}} (f : X ⟶ Y) (x : X) : Prop
```

Declarations registered for the tag:

- [`AlgebraicGeometry.LocallyOfFiniteType`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.LocallyOfFiniteType#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteTypePoint.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteTypePoint.lean#L85) (StacksFrontier): “part (2), and the local finite-type condition in part (3)”. References: EGA I (6.3.1), “partial”; EGA I (6.6.2); EGA IV (1.3.2); SGA 3 VIB (1.3); SGA 4 Vbis (5.2.0), “partial”.
- [`AlgebraicGeometry.QuasiCompact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.QuasiCompact#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteTypePoint.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteTypePoint.lean#L95) (StacksFrontier): “the quasi-compact condition in part (3)”. References: EGA 0 (9.1.1), “special case”; EGA I (6.6.1); EGA IV (1.1.1); SGA 1 XIII (1.5); SGA 4 Vbis (4.2.0), “partial”; SGA 6 II (3.0); SGA 7 VII (1.3.8), “partial”.

## Tag 01T2, a lemma

[Tag 01T2](https://stacks.math.columbia.edu/tag/01T2) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.locallyOfFiniteType_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.locallyOfFiniteType_iff#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FiniteTypeClosedInFinitePresentation/QuasiAffine.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FiniteTypeClosedInFinitePresentation/QuasiAffine.lean#L71) (StacksFrontier): “(1) implies (2) and conversely”. References: SGA 3 VIB (1.3), “locally of finite type”.

## Tag 01T3, a lemma

[Tag 01T3](https://stacks.math.columbia.edu/tag/01T3) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.locallyOfFiniteType_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.locallyOfFiniteType_comp#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L191) (StacksFrontier): “locally of finite type (also the first component of the finite type clause)”. References: EGA I (10.13.5), “(i), special case”; EGA I (6.3.4), “clause (ii)”; EGA I (6.6.6); EGA IV (1.3.4).
- [`AlgebraicGeometry.quasiCompact_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.quasiCompact_comp#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L193) (StacksFrontier): “finite type: the quasi-compact component”. References: EGA I (6.6.4); EGA IV (1.1.2); SGA 4 VI (1.8), “(i), special case”; SGA 4 VI (1.9.1), “(i), special case”.

## Tag 01T4, a lemma

[Tag 01T4](https://stacks.math.columbia.edu/tag/01T4) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.locallyOfFiniteType_isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.locallyOfFiniteType_isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L220) (StacksFrontier): “locally of finite type (also the first component of the finite type clause)”. References: EGA I (10.13.5), “(ii)”; EGA I (6.3.4), “clause (iv)”; EGA I (6.6.6); EGA II (3.5.5), “partial”; EGA IV (1.3.4); EGA IV (2.7.1), “(iii)”; SGA 3 VIB (2.1.2), “partial”.
- [`AlgebraicGeometry.quasiCompact_isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.quasiCompact_isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L222) (StacksFrontier): “finite type: the quasi-compact component”. References: EGA I (6.3.4), “clause (iv)”; EGA I (6.6.4); EGA III (6.9.1), “partial”; EGA III (6.9.4), “more general”; EGA III (7.7.2), “quasi-compactness of f'”; EGA IV (1.1.2); EGA IV (2.3.7), “(i)”; EGA IV (2.6.4), “necessity in (v)”; SGA 1 VIII (3.3), “quasi-compact clause”; SGA 4 VI (1.8), “(ii), special case”; SGA 4 VI (1.9.1), “(ii), special case”; SGA 4 VIII (5.1), “partial”; SGA 7 VII (1.3.8), “partial”.

## Tag 01T5, a lemma

[Tag 01T5](https://stacks.math.columbia.edu/tag/01T5) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.instLocallyOfFiniteTypeOfIsClosedImmersion`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.instLocallyOfFiniteTypeOfIsClosedImmersion#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L225) (StacksFrontier): “a closed immersion is of finite type: the locally of finite type component”. References: EGA I (6.3.4), “clause (i)”; EGA I (6.6.6), “(i), closed immersions”; EGA IV (1.3.4), “(i), closed immersions”.
- [`AlgebraicGeometry.IsImmersion.instLocallyOfFiniteType`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsImmersion.instLocallyOfFiniteType#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L227) (StacksFrontier): “an immersion is locally of finite type”. References: EGA I (6.3.4), “(i)”; EGA I (6.3.5), “partial”; EGA I (6.6.6), “(i), for immersions”; EGA IV (1.3.4), “(i), immersions”; EGA IV (1.5.4), “(i)”.

## Tag 01T6, a lemma

[Tag 01T6](https://stacks.math.columbia.edu/tag/01T6) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.LocallyOfFiniteType.isLocallyNoetherian`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.LocallyOfFiniteType.isLocallyNoetherian#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/NoetherianSource.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/NoetherianSource.lean#L43) (StacksFrontier): “the locally Noetherian half, with the morphism locally of finite type”. References: EGA I (6.3.7), “more general”; EGA II (7.4.1), “partial”; EGA IV (1.3.3); EGA IV (1.3.5), “identity base change”; EGA IV (4.7.3), “partial”.

## Tag 01T7, a lemma

[Tag 01T7](https://stacks.math.columbia.edu/tag/01T7) in the Stacks Project.

**`AlgebraicGeometry.quasiSeparated_of_locallyOfFiniteType`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/LocallyNoetherian.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteType/LocallyNoetherian.lean#L34).

> A morphism locally of finite type over a locally Noetherian scheme is quasi-separated.

```lean
instance quasiSeparated_of_locallyOfFiniteType {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [IsLocallyNoetherian S] : QuasiSeparated f
```

## Tag 01T8, a lemma

[Tag 01T8](https://stacks.math.columbia.edu/tag/01T8) in the Stacks Project.

**`AlgebraicGeometry.LocallyOfFiniteType.of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/FiniteTypeLocalAtSource.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/FiniteTypeLocalAtSource.lean#L103). References: EGA IV (1.3.4).

> **Stacks Project, Tag 01T8.** If a composite of morphisms of schemes is locally of finite
> type, then so is its first factor.

```lean
theorem LocallyOfFiniteType.of_comp {X Y Z : Scheme.{u}} {f : X ⟶ Y} {g : Y ⟶ Z}
    (h : LocallyOfFiniteType (f ≫ g)) : LocallyOfFiniteType f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.15, Tag 01T0](https://stacks.math.columbia.edu/tag/01T0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
