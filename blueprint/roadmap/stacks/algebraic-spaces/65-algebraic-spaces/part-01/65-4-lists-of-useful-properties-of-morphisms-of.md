---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.finitePresentation_isStableUnderBaseChange, AlgebraicGeometry.Space.finiteType_isStableUnderBaseChange, AlgebraicGeometry.Space.quasiFinite_isStableUnderBaseChange, AlgebraicGeometry.isAffineHom_isStableUnderBaseChange, AlgebraicGeometry.Etale.etale_isStableUnderBaseChange, AlgebraicGeometry.IsFinite.instIsStableUnderBaseChangeScheme, AlgebraicGeometry.locallyOfFiniteType_isStableUnderBaseChange, AlgebraicGeometry.Flat.isStableUnderBaseChange
statement: formalized
proof: formalized
---

# 65.4 Lists of useful properties of morphisms of schemes

Section 65.4 of the Stacks Project, [Tag 02WE](https://stacks.math.columbia.edu/tag/02WE). 3 tags here are carried by 49 declarations of the repository (all in StacksFrontier) and 67 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02WF, a remark

[Tag 02WF](https://stacks.math.columbia.edu/tag/02WF) in the Stacks Project.

**`AlgebraicGeometry.Space.finitePresentation_isStableUnderBaseChange`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean#L200). The attribute's comment: “finite\_presentation”.

> Morphisms of schemes of finite presentation remain of finite presentation
> after arbitrary base change.

```lean
public instance finitePresentation_isStableUnderBaseChange :
    MorphismProperty.IsStableUnderBaseChange
      (@AlgebraicGeometry.FinitePresentation.{u})
```

**`AlgebraicGeometry.Space.finiteType_isStableUnderBaseChange`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChangeFiniteType.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChangeFiniteType.lean#L43). The attribute's comment: “of\_finite\_type”.

> Morphisms of schemes of finite type remain of finite type after arbitrary base
> change.

```lean
public instance finiteType_isStableUnderBaseChange :
    MorphismProperty.IsStableUnderBaseChange
      ((@LocallyOfFiniteType : MorphismProperty Scheme.{u}) ⊓ @QuasiCompact)
```

**`AlgebraicGeometry.Space.quasiFinite_isStableUnderBaseChange`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChangeQuasiFinite.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChangeQuasiFinite.lean#L42). The attribute's comment: “quasi\_finite”. References: EGA II (6.2.4).

> Quasi-finite morphisms of schemes remain quasi-finite after arbitrary base change.

```lean
public instance quasiFinite_isStableUnderBaseChange :
    MorphismProperty.IsStableUnderBaseChange
      (((@LocallyOfFiniteType : MorphismProperty Scheme.{u}) ⊓ @QuasiCompact) ⊓
        @LocallyQuasiFinite)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.isAffineHom_isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.isAffineHom_isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean#L82) (StacksFrontier): “affine”. References: EGA II (1.5.1); EGA II (1.5.5), “more general”; EGA II (1.6.2); EGA IV (14.5.11), “Necessity direction”; EGA IV (2.7.1), “(xiii)”; SGA 1 VIII (2.1), “partial”; SGA 1 VIII (5.6), “necessity”; SGA 3 I (4.6.4.1), “partial”; SGA 3 III (0.1.7), “(a)”; SGA 3 III (0.17), “partial”; SGA 3 VIB (10.1), “partial”; SGA 3 XIX (2.1), “more general”; SGA 4 VIII (5.1), “partial”.
- [`AlgebraicGeometry.Etale.etale_isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Etale.etale_isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean#L97) (StacksFrontier): “etale”. References: EGA IV (17.3.3), “(iii), étale case”; EGA IV (17.7.3), “(ii)”; SGA 1 I (4.6); SGA 1 IX (1.3); SGA 1 IX (4.2), “Étaleness of X₁' → S₁'”; SGA 3 VIB (10.1), “partial”; SGA 3 VIB (2.1.2), “partial”; SGA 3 VIIB (1.6.C), “special case”; SGA 4 VII (1.4), “partial”; SGA 4½ Arcata (2.1.3).
- [`AlgebraicGeometry.IsFinite.instIsStableUnderBaseChangeScheme`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsFinite.instIsStableUnderBaseChangeScheme#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean#L99) (StacksFrontier): “finite”. References: EGA I (6.4.12), “more general”; EGA I (6.4.6), “more general”; EGA II (6.1.5), “(iii), finite branch”; EGA III (2.6.2.1), “more general”; EGA IV (2.7.1), “implication”; EGA IV (21.10.16), “f₁ is finite”; SGA 1 VIII (5.7), “preservation (finite)”; SGA 1 VIII (6.6); SGA 3 VIB (10.1), “partial”; SGA 4 VIII (5.4), “more general”.
- [`AlgebraicGeometry.locallyOfFiniteType_isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.locallyOfFiniteType_isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean#L113) (StacksFrontier): “finite\_type”. References: EGA I (10.13.5), “(ii)”; EGA I (6.3.4), “clause (iv)”; EGA I (6.6.6); EGA II (3.5.5), “partial”; EGA IV (1.3.4); EGA IV (2.7.1), “(iii)”; SGA 3 VIB (2.1.2), “partial”.
- [`AlgebraicGeometry.Flat.isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Flat.isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean#L115) (StacksFrontier): “flat”. References: EGA III (7.7.2), “special case”; EGA III (7.9.7), “special case”; EGA IV (11.5.4), “necessity”; EGA IV (2.1.4); EGA IV (2.2.13), “(i)”; EGA IV (2.5.1), “special case”; EGA IV (20.6.9), “flatness of X' over S'”; EGA IV (21.15.9), “partial”; EGA IV (7.3.5), “partial”; SGA 3 III (0.13), “partial”; SGA 3 VIB (10.1), “partial”; SGA 3 VIB (11.1); SGA 3 VIB (2.1.2), “partial”; SGA 3 VIB (3.11), “fiber-flatness”; SGA 3 VIIB (1.3.3), “(iii), special case”; SGA 3 XIX (2.1); SGA 4 Vbis (3.3), “special case”; SGA 6 0 (2.9), “special case”; SGA 6 XII (2.3), “(a)”; SGA 6 XII (4.1), “(1)”; SGA 7 VII (1.3.8), “partial”.
- [`AlgebraicGeometry.gUnramified_isStableUnderBaseChange`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Properties.lean#L260), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean#L117) (StacksFrontier): “g\_unramified”.
- [`AlgebraicGeometry.IsIntegralHom.instIsStableUnderBaseChangeScheme`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsIntegralHom.instIsStableUnderBaseChangeScheme#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean#L119) (StacksFrontier): “integral”. References: EGA II (6.1.5), “(iii), integral branch”; EGA IV (2.7.1), “implication”; SGA 1 VIII (5.7), “preservation (integral)”.
- [`AlgebraicGeometry.locallyOfFinitePresentation_isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.locallyOfFinitePresentation_isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean#L127) (StacksFrontier): “locally\_finite\_presentation”. References: EGA IV (1.4.3); EGA IV (2.7.1), “(iv)”; EGA IV (20.6.9), “partial”; EGA IV (21.15.9), “partial”; EGA IV (8.6.2), “partial”; SGA 3 VIB (5.6.1.0), “partial”.
- [`CategoryTheory.MorphismProperty.IsStableUnderBaseChange.monomorphisms`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.MorphismProperty.IsStableUnderBaseChange.monomorphisms#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean#L130) (StacksFrontier): “monomorphism”. References: EGA I (3.3.12), “more general”; EGA IV (2.7.1), “(ix)”; SGA 3 IV (4.5.7), “more general”; SGA 3 VIB (10.1), “monomorphisms”.
- [`AlgebraicGeometry.IsProper.isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsProper.isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean#L133) (StacksFrontier): “proper”. References: EGA II (5.4.2), “more general”; EGA III (4.3.4), “more general”; EGA IV (2.7.1), “implication”; SGA 1 IX (2.4), “partial”; SGA 1 VIII (4.8), “partial”; SGA 3 VIB (10.1), “partial”; SGA 6 X (7.5), “partial”.
- [`AlgebraicGeometry.quasiSeparated_isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.quasiSeparated_isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean#L135) (StacksFrontier): “quasi\_separated”. References: EGA IV (1.2.2); EGA IV (2.7.1), “(ii)”; SGA 4 VI (1.8), “(ii), special case”; SGA 4 VI (1.9.1), “(ii), special case”; SGA 4 VIII (5.1), “partial”; SGA 7 VII (1.3.8), “partial”.
- [`AlgebraicGeometry.IsSeparated.isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsSeparated.isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean#L137) (StacksFrontier): “separated”. References: EGA I (10.15.3), “(iii), special case”; EGA I (5.5.1); EGA I (5.5.3), “more general”; EGA III (6.9.1), “separatedness of f′\_i”; EGA III (7.7.2), “separatedness of f'”; EGA IV (2.7.1), “implication”; SGA 1 IX (2.4), “partial”; SGA 1 IX (4.2), “partial”; SGA 1 VIII (4.8), “partial”; SGA 3 VIB (10.1), “separatedness”.
- [`AlgebraicGeometry.smooth_isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.smooth_isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean#L149) (StacksFrontier): “smooth”. References: EGA IV (17.3.3), “smooth branch of (iii)”; EGA IV (17.7.3), “(ii)”; EGA IV (6.8.2), “globally smooth f”; EGA IV (6.8.3), “more general”; SGA 1 II (1.3), “more general”; SGA 1 II (4.13), “global ascent”; SGA 3 VIB (10.1), “smooth morphisms”; SGA 3 VIB (2.1.2), “partial”; SGA 3 XIX (2.1), “(i)”; SGA 6 VIII (1.6), “partial”; SGA 6 VIII (1.8), “partial”; SGA 6 X (7.13.3), “partial”.
- [`AlgebraicGeometry.Surjective.instIsStableUnderBaseChangeScheme`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Surjective.instIsStableUnderBaseChangeScheme#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean#L151) (StacksFrontier): “surjective”. References: EGA I (3.5.2); SGA 1 VIII (3.1), “Surjectivity clause”; SGA 3 VIB (10.1), “partial, sufficiency”; SGA 3 VIIB (2.4.1), “special case”.
- [`CategoryTheory.MorphismProperty.universally_isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.MorphismProperty.universally_isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean#L160) (StacksFrontier): “universal\_homeomorphism”. References: EGA IV (14.3.4), “(ii), special case”; EGA IV (2.4.3), “more general”; EGA IV (2.6.4), “partial”; SGA 1 IX (4.2), “partial”; SGA 1 VIII (4.7), “more general”; SGA 3 IV (1.11), “partial”; SGA 4 VI (1.9.1), “more general”.
- [`AlgebraicGeometry.universallyClosed_isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.universallyClosed_isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean#L174) (StacksFrontier): “universally\_closed”. References: EGA II (5.4.9), “5.4.2(iii)”; EGA IV (2.4.3), “(iii)”; EGA IV (2.6.4), “(ii)”; SGA 1 IX (2.4), “partial”; SGA 1 VIII (4.7), “necessity”; SGA 3 V (6.1), “partial”.
- [`AlgebraicGeometry.UniversallyInjective.isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.UniversallyInjective.isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean#L176) (StacksFrontier): “universally\_injective”. References: SGA 3 VIB (10.1), “partial, sufficiency”; SGA 3 VIB (2.6), “more general”.
- [`AlgebraicGeometry.UniversallyOpen.instIsStableUnderBaseChangeScheme`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.UniversallyOpen.instIsStableUnderBaseChangeScheme#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean#L179) (StacksFrontier): “universally\_open”. References: EGA IV (14.3.4), “(ii), global form”; EGA IV (2.4.3), “(iii), universally open”; EGA IV (2.6.4), “necessity in (i)”; SGA 1 IX (2.4), “partial”; SGA 1 VIII (4.7), “necessity”; SGA 3 V (6.1), “special case”; SGA 3 VIB (2.1.2), “partial”.
- [`AlgebraicGeometry.unramified_isStableUnderBaseChange`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Properties.lean#L251), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChange.lean#L195) (StacksFrontier): “unramified”.
- [`AlgebraicGeometry.quasiCompact_isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.quasiCompact_isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChangeClauses.lean, line 30](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChangeClauses.lean#L30) (StacksFrontier): “quasi\_compact”. References: EGA I (6.3.4), “clause (iv)”; EGA I (6.6.4); EGA III (6.9.1), “partial”; EGA III (6.9.4), “more general”; EGA III (7.7.2), “quasi-compactness of f'”; EGA IV (1.1.2); EGA IV (2.3.7), “(i)”; EGA IV (2.6.4), “necessity in (v)”; SGA 1 VIII (3.3), “quasi-compact clause”; SGA 4 VI (1.8), “(ii), special case”; SGA 4 VI (1.9.1), “(ii), special case”; SGA 4 VIII (5.1), “partial”; SGA 7 VII (1.3.8), “partial”.
- [`CategoryTheory.MorphismProperty.universally_isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.MorphismProperty.universally_isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChangeClauses.lean, line 32](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChangeClauses.lean#L32) (StacksFrontier): “universally\_submersive”. References: EGA IV (14.3.4), “(ii), special case”; EGA IV (2.4.3), “more general”; EGA IV (2.6.4), “partial”; SGA 1 IX (4.2), “partial”; SGA 1 VIII (4.7), “more general”; SGA 3 IV (1.11), “partial”; SGA 4 VI (1.9.1), “more general”.
- [`AlgebraicGeometry.instIsStableUnderBaseChangeSchemeLocallyQuasiFinite`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.instIsStableUnderBaseChangeSchemeLocallyQuasiFinite#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChangeLocallyQuasiFinite.lean, line 24](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChangeLocallyQuasiFinite.lean#L24) (StacksFrontier): “locally\_quasi\_finite”. References: EGA II (6.2.4), “(iii)”; SGA 3 V (7.4), “special case”; SGA 3 VIB (10.1), “sufficiency”; SGA 3 VIB (2.8), “(i) ⇒ (ii), partial”.
- [`AlgebraicGeometry.IsClosedImmersion.isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsClosedImmersion.isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChangeRemainingClauses.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChangeRemainingClauses.lean#L67) (StacksFrontier): “closed immersion”. References: EGA I (10.14.5), “(ii), ordinary schemes”; EGA I (4.3.1), “special case”; EGA I (4.3.2); EGA I (4.5.5), “(iii), special case”; EGA II (8.10.2), “j′ is a closed immersion”; EGA IV (17.13.1), “closed immersions”; EGA IV (2.7.1), “implication”; EGA IV (8.6.2), “more general”; SGA 1 VIII (5.5), “closed-immersion clause”; SGA 3 VIB (10.1), “partial”; SGA 4 XII (4.3), “Parenthetical clause”.
- [`AlgebraicGeometry.isOpenImmersion_stableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.isOpenImmersion_stableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChangeRemainingClauses.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChangeRemainingClauses.lean#L70) (StacksFrontier): “open immersion”. References: EGA I (4.3.1), “special case”; EGA I (4.3.2); EGA I (4.5.5), “(iii), special case”; EGA IV (11.9.5), “Geometric clause”; EGA IV (2.7.1), “(x)”; SGA 1 VIII (5.5), “open-immersion clause”; SGA 3 VIB (10.1), “open immersions”; SGA 6 VIII (1.6), “partial”.
- [`AlgebraicGeometry.IsImmersion.isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsImmersion.isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChangeRemainingClauses.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChangeRemainingClauses.lean#L73) (StacksFrontier): “locally closed immersion”. References: EGA I (4.3.1), “special case”; EGA I (4.3.2); EGA I (4.5.5), “(iii), special case”; EGA II (3.8.1), “Immersion clause”; EGA IV (17.13.1); SGA 3 VIB (10.1), “partial”.
- [`AlgebraicGeometry.isQuasiAffineHom_isStableUnderBaseChange`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffineStability.lean#L201), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChangeRemainingClauses.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChangeRemainingClauses.lean#L76) (StacksFrontier): “quasi\_affine”.
- [`AlgebraicGeometry.syntomic_isStableUnderBaseChange`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/BaseChange.lean#L39), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChangeRemainingClauses.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChangeRemainingClauses.lean#L78) (StacksFrontier): “syntomic”.
- [`Stacks.Morphisms.isFiniteLocallyFree_isStableUnderBaseChange`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteLocallyFree/BaseChange.lean#L40), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChangeRemainingClauses.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChangeRemainingClauses.lean#L80) (StacksFrontier): “finite\_locally\_free”.
- [`AlgebraicGeometry.IsProjectiveMorphism.baseChange`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Proper/Projective.lean#L161), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChangeRemainingClauses.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChangeRemainingClauses.lean#L83) (StacksFrontier): “h\_projective”.
- [`AlgebraicGeometry.isStableUnderBaseChange_isProjective`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Projective/BaseChange.lean#L277), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChangeRemainingClauses.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChangeRemainingClauses.lean#L85) (StacksFrontier): “projective”.
- [`AlgebraicGeometry.IsLocallyProjective.pullback_fst`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Projective/BaseChange.lean#L324), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChangeRemainingClauses.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChangeRemainingClauses.lean#L87) (StacksFrontier): “locally\_projective”.
- [`AlgebraicGeometry.RelativeDimension.of_isPullback`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/BaseChange.lean#L74), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChangeRemainingClauses.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/BaseChangeRemainingClauses.lean#L89) (StacksFrontier): “relative\_dimension\_d”.

## Tag 02WG, a remark

[Tag 02WG](https://stacks.math.columbia.edu/tag/02WG) in the Stacks Project.

**`AlgebraicGeometry.Space.universalHomeomorphism_isStableUnderComposition`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean#L180). The attribute's comment: “universal\_homeomorphism”.

> Universal homeomorphisms of schemes are stable under composition.

```lean
public instance universalHomeomorphism_isStableUnderComposition :
    MorphismProperty.IsStableUnderComposition
      (@AlgebraicGeometry.UniversalHomeomorphism.{u} : MorphismProperty Scheme.{u})
```

**`AlgebraicGeometry.Space.universallySubmersive_isStableUnderComposition`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean#L191). The attribute's comment: “universally\_submersive”.

> The composite of universally submersive morphisms of schemes is universally
> submersive.

```lean
public instance universallySubmersive_isStableUnderComposition :
    (topologically @Topology.IsQuotientMap :
      MorphismProperty Scheme.{u}).universally.IsStableUnderComposition
```

Declarations registered for the tag:

- [`AlgebraicGeometry.instIsAffineHomCompScheme`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.instIsAffineHomCompScheme#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean#L83) (StacksFrontier): “affine”. References: EGA II (1.3.5); EGA II (1.3.6), “partial”; EGA II (1.6.2).
- [`AlgebraicGeometry.Etale.etale_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Etale.etale_comp#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean#L88) (StacksFrontier): “etale”. References: EGA IV (17.3.3), “(ii), étale case”; EGA IV (17.3.5), “étale clause”; SGA 1 I (4.6); SGA 1 V (3.3), “special case”.
- [`AlgebraicGeometry.IsFinite.instIsStableUnderCompositionScheme`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsFinite.instIsStableUnderCompositionScheme#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean#L90) (StacksFrontier): “finite\_integral”. References: EGA II (6.1.5), “(ii), finite branch”; EGA IV (21.10.15), “Condition a)”.
- [`AlgebraicGeometry.IsIntegralHom.instIsStableUnderCompositionScheme`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsIntegralHom.instIsStableUnderCompositionScheme#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean#L96) (StacksFrontier): “finite\_integral”. References: EGA II (6.1.5), “(ii), integral branch”.
- [`AlgebraicGeometry.locallyOfFinitePresentation_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.locallyOfFinitePresentation_comp#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean#L101) (StacksFrontier): “finite\_presentation”. References: EGA IV (1.4.3); SGA 6 III (1.14), “special case”.
- [`AlgebraicGeometry.quasiCompact_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.quasiCompact_comp#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean#L103) (StacksFrontier): “finite\_presentation”. References: EGA I (6.6.4); EGA IV (1.1.2); SGA 4 VI (1.8), “(i), special case”; SGA 4 VI (1.9.1), “(i), special case”.
- [`AlgebraicGeometry.quasiSeparated_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.quasiSeparated_comp#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean#L109) (StacksFrontier): “finite\_presentation”. References: EGA IV (1.2.2); SGA 4 VI (1.8), “(i), special case”; SGA 4 VI (1.9.1), “(i), special case”.
- [`AlgebraicGeometry.Flat.comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Flat.comp#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean#L114) (StacksFrontier): “flat”. References: EGA 0 (6.7.5), “Schemes (EGA preschemes)”; EGA IV (2.1.5), “global case Y' = Y”; EGA IV (2.1.6); EGA IV (2.2.11), “(iii), special case”; EGA IV (2.2.13), “(iii)”; EGA IV (6.6.1), “(i): flatness of h = g∘f”; EGA IV (7.3.5), “partial”; SGA 3 VIIB (1.3.3), “(i), special case”.
- [`AlgebraicGeometry.IsClosedImmersion.comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsClosedImmersion.comp#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean#L116) (StacksFrontier): “immersions”. References: EGA I (10.14.5), “(i), ordinary schemes”; EGA I (4.1.6); EGA I (4.2.5); EGA I (4.5.5), “(i), special case”.
- [`AlgebraicGeometry.IsOpenImmersion.comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsOpenImmersion.comp#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean#L122) (StacksFrontier): “immersions”. References: EGA I (4.2.5); EGA I (4.5.5), “(i), special case”.
- [`AlgebraicGeometry.IsImmersion.comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsImmersion.comp#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean#L126) (StacksFrontier): “immersions”. References: EGA I (4.1.6); EGA I (4.2.5); EGA I (4.5.5), “(i), special case”.
- [`CategoryTheory.mono_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.mono_comp#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean#L131) (StacksFrontier): “monomorphisms”.
- [`AlgebraicGeometry.IsProper.stableUnderComposition`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsProper.stableUnderComposition#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean#L133) (StacksFrontier): “proper”. References: EGA II (5.4.2).
- [`AlgebraicGeometry.quasiCompact_isStableUnderComposition`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.quasiCompact_isStableUnderComposition#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean#L135) (StacksFrontier): “quasi\_compact”. References: EGA I (6.6.4); EGA IV (1.1.2); SGA 4 VI (1.8), “(i), special case”; SGA 4 VI (1.9.1), “(i), special case”.
- [`AlgebraicGeometry.quasiSeparated_isStableUnderComposition`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.quasiSeparated_isStableUnderComposition#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean#L141) (StacksFrontier): “quasi\_separated”. References: EGA IV (1.2.2); SGA 4 VI (1.8), “(i), special case”; SGA 4 VI (1.9.1), “(i), special case”.
- [`AlgebraicGeometry.IsSeparated.stableUnderComposition`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsSeparated.stableUnderComposition#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean#L148) (StacksFrontier): “separated”. References: EGA I (10.15.3), “(i), ordinary preschemes”; EGA I (5.5.1).
- [`AlgebraicGeometry.smooth_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.smooth_comp#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean#L153) (StacksFrontier): “smooth”. References: EGA IV (17.3.3), “smooth branch of (ii)”; EGA IV (6.8.3), “more general”; SGA 1 II (1.3), “more general”.
- [`AlgebraicGeometry.instSurjectiveCompScheme`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.instSurjectiveCompScheme#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean#L158) (StacksFrontier): “surjective”. References: EGA I (2.2.7).
- [`AlgebraicGeometry.universallyClosed_isStableUnderComposition`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.universallyClosed_isStableUnderComposition#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean#L161) (StacksFrontier): “universally\_closed”. References: EGA II (5.4.9), “5.4.2(ii)”; EGA IV (2.4.3), “(ii)”.
- [`AlgebraicGeometry.universallyInjective_isStableUnderComposition`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.universallyInjective_isStableUnderComposition#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean#L164) (StacksFrontier): “universally\_injective”. References: EGA I (3.5.6); EGA IV (6.15.3.1), “(i), special case”.
- [`AlgebraicGeometry.UniversallyOpen.instCompScheme`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.UniversallyOpen.instCompScheme#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean#L170) (StacksFrontier): “universally\_open”. References: EGA IV (14.3.4), “(i), special case”; EGA IV (2.4.3), “(ii), universally open”.
- [`AlgebraicGeometry.unramified_isStableUnderComposition`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Properties.lean#L235), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean#L174) (StacksFrontier): “unramified”.
- [`AlgebraicGeometry.gUnramified_isStableUnderComposition`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Properties.lean#L243), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Composition.lean#L176) (StacksFrontier): “unramified”.
- [`Stacks.Morphisms.isFiniteLocallyFree_comp`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteLocallyFree/Comp.lean#L38), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/CompositionClauses.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/CompositionClauses.lean#L40) (StacksFrontier): “finite\_locally\_free”.
- [`AlgebraicGeometry.IsProjectiveMorphism.comp`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Proper/Projective.lean#L183), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/CompositionClauses.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/CompositionClauses.lean#L42) (StacksFrontier): “h\_projective”.
- [`AlgebraicGeometry.isQuasiAffineHom_isStableUnderComposition`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffineStability.lean#L185), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/CompositionClauses.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/CompositionClauses.lean#L44) (StacksFrontier): “quasi\_affine”.
- [`AlgebraicGeometry.locallyQuasiFinite_conditions_comp`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Composition.lean#L47), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/CompositionClauses.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/CompositionClauses.lean#L47) (StacksFrontier): “quasi\_finite”.
- [`AlgebraicGeometry.quasiFinite_conditions_comp`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Composition.lean#L56), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/CompositionClauses.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/CompositionClauses.lean#L49) (StacksFrontier): “quasi\_finite”.
- [`AlgebraicGeometry.syntomic_isStableUnderComposition`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Comp.lean#L63), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/CompositionClauses.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/CompositionClauses.lean#L51) (StacksFrontier): “syntomic”.
- [`AlgebraicGeometry.locallyOfFiniteType_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.locallyOfFiniteType_comp#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/CompositionFiniteType.lean, line 23](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/CompositionFiniteType.lean#L23) (StacksFrontier): “finite\_type”. References: EGA I (10.13.5), “(i), special case”; EGA I (6.3.4), “clause (ii)”; EGA I (6.6.6); EGA IV (1.3.4).
- [`AlgebraicGeometry.quasiCompact_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.quasiCompact_comp#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/CompositionFiniteType.lean, line 29](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/CompositionFiniteType.lean#L29) (StacksFrontier): “finite\_type”. References: EGA I (6.6.4); EGA IV (1.1.2); SGA 4 VI (1.8), “(i), special case”; SGA 4 VI (1.9.1), “(i), special case”.

## Tag 02WH, a remark

[Tag 02WH](https://stacks.math.columbia.edu/tag/02WH) in the Stacks Project.

**`AlgebraicGeometry.etale_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleFpqcLocalAtTarget.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EtaleFpqcLocalAtTarget.lean#L73). The attribute's comment: “etale”. References: SGA 3 VIB (2.1.2), “partial”.

> Étaleness of morphisms of schemes is fpqc local on the base.

```lean
instance etale_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget (@Etale : MorphismProperty Scheme.{u})
      Scheme.fpqcPrecoverage
```

**`AlgebraicGeometry.etale_isLocalAtTarget_fppf`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleFpqcLocalAtTarget.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EtaleFpqcLocalAtTarget.lean#L84). The attribute's comment: “etale”.

> Étaleness of morphisms of schemes is fppf local on the base.

```lean
instance etale_isLocalAtTarget_fppf :
    MorphismProperty.IsLocalAtTarget (@Etale : MorphismProperty Scheme.{u})
      Scheme.fppfPrecoverage
```

**`Stacks.Descent.isClosedImmersion_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L95). The attribute's comment: “entry (1)(a): closed immersions”. References: SGA 1 VIII (5.5), “more general”; SGA 3 VIB (12.1), “more general”; SGA 4 IV (8.5.5).

> **Stacks 02WH**, entry (1)(a): being a closed immersion is stable under base change, fpqc
> local on the base, and a fortiori fppf local on the base.

```lean
public theorem isClosedImmersion_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf :
    MorphismProperty.IsStableUnderBaseChange (@IsClosedImmersion : MorphismProperty Scheme.{u}) ∧
      MorphismProperty.IsLocalAtTarget
          (@IsClosedImmersion : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          (@IsClosedImmersion : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage
```

**`Stacks.Descent.isOpenImmersion_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L111). The attribute's comment: “entry (1)(b): open immersions”. References: EGA IV (2.7.1), “more general”; SGA 1 VIII (5.5), “more general”; SGA 4 IV (8.5.5).

> **Stacks 02WH**, entry (1)(b): being an open immersion is stable under base change, fpqc
> local on the base, and a fortiori fppf local on the base.

```lean
public theorem isOpenImmersion_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf :
    MorphismProperty.IsStableUnderBaseChange (@IsOpenImmersion : MorphismProperty Scheme.{u}) ∧
      MorphismProperty.IsLocalAtTarget
          (@IsOpenImmersion : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          (@IsOpenImmersion : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage
```

**`Stacks.Descent.isImmersion_inf_quasiCompact_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L126). The attribute's comment: “entry (1)(c): quasi-compact immersions”. References: EGA IV (2.7.1), “more general”; SGA 4 IV (8.5.5).

> **Stacks 02WH**, entry (1)(c): being a quasi-compact immersion is stable under base change,
> fpqc local on the base, and a fortiori fppf local on the base.

```lean
public theorem
    isImmersion_inf_quasiCompact_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf :
    MorphismProperty.IsStableUnderBaseChange
        (@IsImmersion ⊓ @QuasiCompact : MorphismProperty Scheme.{u}) ∧
      MorphismProperty.IsLocalAtTarget
          (@IsImmersion ⊓ @QuasiCompact : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          (@IsImmersion ⊓ @QuasiCompact : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage
```

**`Stacks.Descent.quasiCompact_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L143). The attribute's comment: “entry (2): quasi-compact”.

> **Stacks 02WH**, entry (2): being quasi-compact is stable under base change, fpqc local on
> the base, and a fortiori fppf local on the base.

```lean
public theorem quasiCompact_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf :
    MorphismProperty.IsStableUnderBaseChange (@QuasiCompact : MorphismProperty Scheme.{u}) ∧
      MorphismProperty.IsLocalAtTarget
          (@QuasiCompact : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          (@QuasiCompact : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage
```

**`Stacks.Descent.universallyClosed_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L158). The attribute's comment: “entry (3): universally closed”. References: EGA IV (2.6.4), “more general”.

> **Stacks 02WH**, entry (3): being universally closed is stable under base change, fpqc local
> on the base, and a fortiori fppf local on the base.

```lean
public theorem universallyClosed_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf :
    MorphismProperty.IsStableUnderBaseChange (@UniversallyClosed : MorphismProperty Scheme.{u}) ∧
      MorphismProperty.IsLocalAtTarget
          (@UniversallyClosed : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          (@UniversallyClosed : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage
```

**`Stacks.Descent.isSeparated_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L173). The attribute's comment: “entry (4): separated”.

> **Stacks 02WH**, entry (4), separated case: being separated is stable under base change, fpqc
> local on the base, and a fortiori fppf local on the base.

```lean
public theorem isSeparated_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf :
    MorphismProperty.IsStableUnderBaseChange (@IsSeparated : MorphismProperty Scheme.{u}) ∧
      MorphismProperty.IsLocalAtTarget
          (@IsSeparated : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          (@IsSeparated : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage
```

**`Stacks.Descent.quasiSeparated_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L186). The attribute's comment: “entry (4): quasi-separated”.

> **Stacks 02WH**, entry (4), quasi-separated case: being quasi-separated is stable under base
> change, fpqc local on the base, and a fortiori fppf local on the base.

```lean
public theorem quasiSeparated_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf :
    MorphismProperty.IsStableUnderBaseChange (@QuasiSeparated : MorphismProperty Scheme.{u}) ∧
      MorphismProperty.IsLocalAtTarget
          (@QuasiSeparated : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          (@QuasiSeparated : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage
```

**`Stacks.Descent.monomorphisms_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L201). The attribute's comment: “entry (5): monomorphism”. References: SGA 4 IV (8.5.5).

> **Stacks 02WH**, entry (5): being a monomorphism is stable under base change, fpqc local on
> the base, and a fortiori fppf local on the base.

```lean
public theorem monomorphisms_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf :
    MorphismProperty.IsStableUnderBaseChange (MorphismProperty.monomorphisms Scheme.{u}) ∧
      MorphismProperty.IsLocalAtTarget
          (MorphismProperty.monomorphisms Scheme.{u}) Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          (MorphismProperty.monomorphisms Scheme.{u}) Scheme.fppfPrecoverage
```

**`Stacks.Descent.surjective_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L216). The attribute's comment: “entry (6): surjective”. References: SGA 4 IV (8.5.5).

> **Stacks 02WH**, entry (6): being surjective is stable under base change, fpqc local on the
> base, and a fortiori fppf local on the base.

```lean
public theorem surjective_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf :
    MorphismProperty.IsStableUnderBaseChange (@Surjective : MorphismProperty Scheme.{u}) ∧
      MorphismProperty.IsLocalAtTarget
          (@Surjective : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          (@Surjective : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage
```

**`Stacks.Descent.universallyInjective_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L231). The attribute's comment: “entry (7): universally injective”.

> **Stacks 02WH**, entry (7): being universally injective is stable under base change, fpqc
> local on the base, and a fortiori fppf local on the base.

```lean
public theorem universallyInjective_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf :
    MorphismProperty.IsStableUnderBaseChange (@UniversallyInjective : MorphismProperty Scheme.{u}) ∧
      MorphismProperty.IsLocalAtTarget
          (@UniversallyInjective : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          (@UniversallyInjective : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage
```

**`Stacks.Descent.isAffineHom_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L246). The attribute's comment: “entry (8): affine”.

> **Stacks 02WH**, entry (8): being affine is stable under base change, fpqc local on the base,
> and a fortiori fppf local on the base.

```lean
public theorem isAffineHom_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf :
    MorphismProperty.IsStableUnderBaseChange (@IsAffineHom : MorphismProperty Scheme.{u}) ∧
      MorphismProperty.IsLocalAtTarget
          (@IsAffineHom : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          (@IsAffineHom : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage
```

**`Stacks.Descent.isQuasiAffineHom_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L261). The attribute's comment: “entry (9): quasi-affine”.

> **Stacks 02WH**, entry (9): being quasi-affine is stable under base change, fpqc local on the
> base, and a fortiori fppf local on the base.

```lean
public theorem isQuasiAffineHom_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf :
    MorphismProperty.IsStableUnderBaseChange (@IsQuasiAffineHom : MorphismProperty Scheme.{u}) ∧
      MorphismProperty.IsLocalAtTarget
          (@IsQuasiAffineHom : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          (@IsQuasiAffineHom : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage
```

**`Stacks.Descent.locallyOfFiniteType_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L276). The attribute's comment: “entry (10): locally of finite type”.

> **Stacks 02WH**, entry (10), locally of finite type case: being locally of finite type is
> stable under base change, fpqc local on the base, and a fortiori fppf local on the base.

```lean
public theorem locallyOfFiniteType_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf :
    MorphismProperty.IsStableUnderBaseChange (@LocallyOfFiniteType : MorphismProperty Scheme.{u}) ∧
      MorphismProperty.IsLocalAtTarget
          (@LocallyOfFiniteType : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          (@LocallyOfFiniteType : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage
```

**`Stacks.Descent.finiteType_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L289). The attribute's comment: “entry (10): of finite type”.

> **Stacks 02WH**, entry (10), finite type case: being of finite type is stable under base
> change, fpqc local on the base, and a fortiori fppf local on the base.

```lean
public theorem finiteType_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf :
    MorphismProperty.IsStableUnderBaseChange
        (@LocallyOfFiniteType ⊓ @QuasiCompact : MorphismProperty Scheme.{u}) ∧
      MorphismProperty.IsLocalAtTarget
          (@LocallyOfFiniteType ⊓ @QuasiCompact : MorphismProperty Scheme.{u})
          Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          (@LocallyOfFiniteType ⊓ @QuasiCompact : MorphismProperty Scheme.{u})
          Scheme.fppfPrecoverage
```

**`Stacks.Descent.locallyOfFiniteType_inf_locallyQuasiFinite_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L307). The attribute's comment: “entry (11): locally quasi-finite”.

> **Stacks 02WH**, entry (11), locally quasi-finite case: being locally quasi-finite is stable
> under base change, fpqc local on the base, and a fortiori fppf local on the base.

```lean
public theorem
  locallyOfFiniteType_inf_locallyQuasiFinite_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf :
    MorphismProperty.IsStableUnderBaseChange
        (@LocallyOfFiniteType ⊓ @LocallyQuasiFinite : MorphismProperty Scheme.{u}) ∧
      MorphismProperty.IsLocalAtTarget
          (@LocallyOfFiniteType ⊓ @LocallyQuasiFinite : MorphismProperty Scheme.{u})
          Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          (@LocallyOfFiniteType ⊓ @LocallyQuasiFinite : MorphismProperty Scheme.{u})
          Scheme.fppfPrecoverage
```

**`Stacks.Descent.finiteType_inf_locallyQuasiFinite_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 324](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L324). The attribute's comment: “entry (11): quasi-finite”.

> **Stacks 02WH**, entry (11), quasi-finite case: being quasi-finite is stable under base
> change, fpqc local on the base, and a fortiori fppf local on the base.

```lean
public theorem
    finiteType_inf_locallyQuasiFinite_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf :
    MorphismProperty.IsStableUnderBaseChange
        ((@LocallyOfFiniteType ⊓ @QuasiCompact : MorphismProperty Scheme.{u}) ⊓
          @LocallyQuasiFinite) ∧
      MorphismProperty.IsLocalAtTarget
          ((@LocallyOfFiniteType ⊓ @QuasiCompact : MorphismProperty Scheme.{u}) ⊓
            @LocallyQuasiFinite) Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          ((@LocallyOfFiniteType ⊓ @QuasiCompact : MorphismProperty Scheme.{u}) ⊓
            @LocallyQuasiFinite) Scheme.fppfPrecoverage
```

**`Stacks.Descent.locallyOfFinitePresentation_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L345). The attribute's comment: “entry (12): locally of finite presentation”. References: SGA 4 IV (8.5.5), “partial”.

> **Stacks 02WH**, entry (12), locally of finite presentation case: being locally of finite
> presentation is stable under base change, fpqc local on the base, and a fortiori fppf local on
> the base.

```lean
public theorem locallyOfFinitePresentation_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf :
    MorphismProperty.IsStableUnderBaseChange
        (@LocallyOfFinitePresentation : MorphismProperty Scheme.{u}) ∧
      MorphismProperty.IsLocalAtTarget
          (@LocallyOfFinitePresentation : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          (@LocallyOfFinitePresentation : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage
```

**`Stacks.Descent.finitePresentation_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 359](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L359). The attribute's comment: “entry (12): of finite presentation”. References: SGA 4 IV (8.5.5).

> **Stacks 02WH**, entry (12), finite presentation case: being of finite presentation is stable
> under base change, fpqc local on the base, and a fortiori fppf local on the base.

```lean
public theorem finitePresentation_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf :
    MorphismProperty.IsStableUnderBaseChange (@FinitePresentation : MorphismProperty Scheme.{u}) ∧
      MorphismProperty.IsLocalAtTarget
          (@FinitePresentation : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          (@FinitePresentation : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage
```

**`Stacks.Descent.locallyOfFiniteTypeRelativeDimension_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 374](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L374). The attribute's comment: “entry (13): locally of finite type of relative dimension d”.

> **Stacks 02WH**, entry (13): being locally of finite type of relative dimension `d` is stable
> under base change, fpqc local on the base, and a fortiori fppf local on the base.

```lean
public theorem
    locallyOfFiniteTypeRelativeDimension_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf
    (d : ℕ) :
    MorphismProperty.IsStableUnderBaseChange (locallyOfFiniteTypeRelativeDimension.{u} d) ∧
      MorphismProperty.IsLocalAtTarget
          (locallyOfFiniteTypeRelativeDimension.{u} d) Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          (locallyOfFiniteTypeRelativeDimension.{u} d) Scheme.fppfPrecoverage
```

**`Stacks.Descent.universallyOpen_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 391](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L391). The attribute's comment: “entry (14): universally open”. References: EGA IV (2.6.4), “more general”; SGA 4 IV (8.5.5).

> **Stacks 02WH**, entry (14): being universally open is stable under base change, fpqc local on
> the base, and a fortiori fppf local on the base.

```lean
public theorem universallyOpen_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf :
    MorphismProperty.IsStableUnderBaseChange (@UniversallyOpen : MorphismProperty Scheme.{u}) ∧
      MorphismProperty.IsLocalAtTarget
          (@UniversallyOpen : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          (@UniversallyOpen : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage
```

**`Stacks.Descent.flat_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 406](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L406). The attribute's comment: “entry (15): flat”.

> **Stacks 02WH**, entry (15): being flat is stable under base change, fpqc local on the base,
> and a fortiori fppf local on the base.

```lean
public theorem flat_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf :
    MorphismProperty.IsStableUnderBaseChange (@Flat : MorphismProperty Scheme.{u}) ∧
      MorphismProperty.IsLocalAtTarget
          (@Flat : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          (@Flat : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage
```

**`Stacks.Descent.syntomic_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 421](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L421). The attribute's comment: “entry (16): syntomic”.

> **Stacks 02WH**, entry (16): being syntomic is stable under base change, fpqc local on the
> base, and a fortiori fppf local on the base.

```lean
public theorem syntomic_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf :
    MorphismProperty.IsStableUnderBaseChange (@Syntomic : MorphismProperty Scheme.{u}) ∧
      MorphismProperty.IsLocalAtTarget
          (@Syntomic : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          (@Syntomic : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage
```

**`Stacks.Descent.smooth_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 436](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L436). The attribute's comment: “entry (17): smooth”. References: SGA 3 VIB (2.1.2); SGA 3 VIIA (8.3.1), “partial”.

> **Stacks 02WH**, entry (17): being smooth is stable under base change, fpqc local on the base,
> and a fortiori fppf local on the base.

```lean
public theorem smooth_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf :
    MorphismProperty.IsStableUnderBaseChange (@Smooth : MorphismProperty Scheme.{u}) ∧
      MorphismProperty.IsLocalAtTarget
          (@Smooth : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          (@Smooth : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage
```

**`Stacks.Descent.unramified_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 451](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L451). The attribute's comment: “entry (18): unramified”.

> **Stacks 02WH**, entry (18), unramified case: being unramified is stable under base change,
> fpqc local on the base, and a fortiori fppf local on the base.

```lean
public theorem unramified_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf :
    MorphismProperty.IsStableUnderBaseChange (@Unramified : MorphismProperty Scheme.{u}) ∧
      MorphismProperty.IsLocalAtTarget
          (@Unramified : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          (@Unramified : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage
```

**`Stacks.Descent.gUnramified_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 464](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L464). The attribute's comment: “entry (18): G-unramified”.

> **Stacks 02WH**, entry (18), G-unramified case: being G-unramified is stable under base
> change, fpqc local on the base, and a fortiori fppf local on the base.

```lean
public theorem gUnramified_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf :
    MorphismProperty.IsStableUnderBaseChange (@GUnramified : MorphismProperty Scheme.{u}) ∧
      MorphismProperty.IsLocalAtTarget
          (@GUnramified : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          (@GUnramified : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage
```

**`Stacks.Descent.etale_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 479](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L479). The attribute's comment: “entry (19): etale”.

> **Stacks 02WH**, entry (19): being étale is stable under base change, fpqc local on the base,
> and a fortiori fppf local on the base.

```lean
public theorem etale_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf :
    MorphismProperty.IsStableUnderBaseChange (@Etale : MorphismProperty Scheme.{u}) ∧
      MorphismProperty.IsLocalAtTarget
          (@Etale : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          (@Etale : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage
```

**`Stacks.Descent.isProper_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 495](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L495). The attribute's comment: “entry (20): proper”. References: SGA 4 IV (8.5.5).

> **Stacks 02WH**, entry (20) of the list: **proper**, Descent, Lemma 02L1. The source's
> "proper" is `AlgebraicGeometry.IsProper` in Lean. Being proper is stable under arbitrary base
> change, fpqc local on the base, and a fortiori fppf local on the base.

```lean
public theorem isProper_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf :
    MorphismProperty.IsStableUnderBaseChange (@IsProper : MorphismProperty Scheme.{u}) ∧
      MorphismProperty.IsLocalAtTarget
          (@IsProper : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          (@IsProper : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage
```

**`Stacks.Descent.isFinite_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 510](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L510). The attribute's comment: “entry (21): finite”.

> **Stacks 02WH**, entry (21), finite case: being finite is stable under base change, fpqc local
> on the base, and a fortiori fppf local on the base.

```lean
public theorem isFinite_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf :
    MorphismProperty.IsStableUnderBaseChange (@IsFinite : MorphismProperty Scheme.{u}) ∧
      MorphismProperty.IsLocalAtTarget
          (@IsFinite : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          (@IsFinite : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage
```

**`Stacks.Descent.isIntegralHom_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 523](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L523). The attribute's comment: “entry (21): integral”.

> **Stacks 02WH**, entry (21), integral case: being integral is stable under base change, fpqc
> local on the base, and a fortiori fppf local on the base.

```lean
public theorem isIntegralHom_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf :
    MorphismProperty.IsStableUnderBaseChange (@IsIntegralHom : MorphismProperty Scheme.{u}) ∧
      MorphismProperty.IsLocalAtTarget
          (@IsIntegralHom : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          (@IsIntegralHom : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage
```

**`Stacks.Descent.isFiniteLocallyFree_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 540](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L540). The attribute's comment: “entry (22): finite locally free”. References: SGA 1 VIII (5.7), “more general”.

> **Stacks 02WH**, entry (22) of the list: **finite locally free**, Descent, Lemma 02VO, with
> the rank left unconstrained. The source's "finite locally free" is
> `Stacks.Morphisms.IsFiniteLocallyFree` in Lean. Being finite locally free is stable under
> arbitrary base change, fpqc local on the base, and a fortiori fppf local on the base.

```lean
public theorem isFiniteLocallyFree_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf :
    MorphismProperty.IsStableUnderBaseChange
        (@Stacks.Morphisms.IsFiniteLocallyFree : MorphismProperty Scheme.{u}) ∧
      MorphismProperty.IsLocalAtTarget
          (@Stacks.Morphisms.IsFiniteLocallyFree : MorphismProperty Scheme.{u})
          Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          (@Stacks.Morphisms.IsFiniteLocallyFree : MorphismProperty Scheme.{u})
          Scheme.fppfPrecoverage
```

**`Stacks.Descent.isFiniteLocallyFreeOfRank_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 559](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L559). The attribute's comment: “entry (22): finite locally free of rank d”. References: SGA 1 VIII (5.7), “special case”.

> **Stacks 02WH**, entry (22) of the list: **finite locally free**, Descent, Lemma 02VO, for a
> fixed rank `d`. The source's "finite locally free" of rank `d` is
> `Stacks.Morphisms.IsFiniteLocallyFreeOfRank.property d` in Lean. Being finite locally free of
> rank `d` is stable under arbitrary base change, fpqc local on the base, and a fortiori fppf
> local on the base.

```lean
public theorem
    isFiniteLocallyFreeOfRank_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf
    (d : ℕ) :
    MorphismProperty.IsStableUnderBaseChange
        (Stacks.Morphisms.IsFiniteLocallyFreeOfRank.property.{u} d) ∧
      MorphismProperty.IsLocalAtTarget
          (Stacks.Morphisms.IsFiniteLocallyFreeOfRank.property.{u} d) Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          (Stacks.Morphisms.IsFiniteLocallyFreeOfRank.property.{u} d) Scheme.fppfPrecoverage
```

**`Stacks.Descent.universallyQuotientMap_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 583](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L583). The attribute's comment: “entry (23): universally submersive”. References: EGA IV (15.7.11.1), “fpqc-locality conjunct”; SGA 1 IX (4.2), “partial”.

> **Stacks 02WH**, entry (23) of the list: **universally submersive**, Descent, Lemma 0CEW.
> A submersive morphism is one whose underlying map of topological spaces is a quotient map, so the
> source's "universally submersive" is in Lean `(topologically Topology.IsQuotientMap).universally`
> — the Lean name `universallyQuotientMap` denotes exactly the source's "universally submersive".
> That property is stable under arbitrary base change, fpqc local on the base, and a fortiori fppf
> local on the base.

```lean
public theorem universallyQuotientMap_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf :
    MorphismProperty.IsStableUnderBaseChange
        ((topologically @Topology.IsQuotientMap : MorphismProperty Scheme.{u}).universally) ∧
      MorphismProperty.IsLocalAtTarget
          ((topologically @Topology.IsQuotientMap : MorphismProperty Scheme.{u}).universally)
          Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          ((topologically @Topology.IsQuotientMap : MorphismProperty Scheme.{u}).universally)
          Scheme.fppfPrecoverage
```

**`Stacks.Descent.universalHomeomorphism_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 605](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L605). The attribute's comment: “entry (24): universal homeomorphism”. References: EGA IV (2.6.2), “(iv), special case”; EGA IV (2.6.4), “more general”; SGA 1 VIII (4.7), “more general”; SGA 4 IV (8.5.5).

> **Stacks 02WH**, entry (24) of the list: **universal homeomorphism**, Descent, Lemma 0CEX.
> The source's "universal homeomorphism" is `AlgebraicGeometry.UniversalHomeomorphism` in Lean.
> Being a universal homeomorphism is stable under arbitrary base change, fpqc local on the base,
> and a fortiori fppf local on the base.

```lean
public theorem universalHomeomorphism_isStableUnderBaseChange_and_isLocalAtTarget_fpqc_fppf :
    MorphismProperty.IsStableUnderBaseChange
        (@UniversalHomeomorphism : MorphismProperty Scheme.{u}) ∧
      MorphismProperty.IsLocalAtTarget
          (@UniversalHomeomorphism : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          (@UniversalHomeomorphism : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage
```

**`Stacks.Descent.isImmersion_isStableUnderBaseChange_and_isLocalAtTarget_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean, line 630](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Entries.lean#L630). The attribute's comment: “last sentence (02YM): immersions are fppf local on the base”. References: EGA II (3.8.1), “more general”.

> **Stacks 02WH**, the closing sentence of the remark: **immersions are fppf local on the
> base**, Descent, Lemma 02YM. Being an immersion is stable under base change, and it is fppf local
> on the base — that fppf locality is exactly the content of 02YM, which the remark's last sentence
> cites. The remark records explicitly that being an immersion *may not be* fpqc local on the base,
> so no fpqc conjunct is asserted here; only the three cases of entry (1) — closed, open and
> quasi-compact immersions — are claimed fpqc local.

```lean
public theorem isImmersion_isStableUnderBaseChange_and_isLocalAtTarget_fppf :
    MorphismProperty.IsStableUnderBaseChange (@IsImmersion : MorphismProperty Scheme.{u}) ∧
      MorphismProperty.IsLocalAtTarget (@IsImmersion : MorphismProperty Scheme.{u})
        Scheme.fppfPrecoverage
```

**`Stacks.Descent.fpqcAndFppfLocalOnBase_allEntries_and_isImmersion_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Remark.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FppfLocalOnBase/Remark.lean#L111). The attribute's comment: “The remark in full, as one conjunction in the source's order: entry (n) is the n-th conjunct, and each conjunct states that the property that entry names is stable under arbitrary base change, local on the base for the fpqc precoverage, and a fortiori local on the base for the fppf precoverage. Entry (1) is the conjunction of its three cases, (a) closed, (b) open and (c) quasi-compact immersions; each entry with two readings, namely (4), (10), (11), (12), (18), (21) and (22), is the conjunction of both readings; and entries (13) and (22) are quantified over their numerical parameter. The twenty-fifth and last conjunct is the remark's closing sentence: being an immersion is stable under arbitrary base change and local on the base for the fppf precoverage, which is Descent, Lemma 02YM.”. References: EGA IV (17.3.3), “(iii)”; EGA IV (2.6.4), “more general”; EGA IV (2.7.1), “more general”; SGA 1 IX (2.4), “special case”; SGA 1 IX (4.2), “Étaleness”; SGA 1 VIII (5.5), “more general”; SGA 3 IV (4.7), “(a)”; SGA 3 IV (6.4.1); SGA 3 VIB (2.1.2); SGA 3 VIIA (8.3.1), “Smoothness entry (17)”; SGA 3 XI (6.8), “partial”.

> **Stacks Project, Remark 02WH, in full.** Of the properties of morphisms of schemes which are
> stable under base change, the following twenty-four are also *fpqc local on the base*, and a
> fortiori *fppf local on the base*:
>
> 1. immersions, in the three cases
>    (a) closed immersions (Descent, Lemma 02L6),
>    (b) open immersions (Descent, Lemma 02L3), and
>    (c) quasi-compact immersions (Descent, Lemma 02L8);
> 2. quasi-compact (Descent, Lemma 02KQ);
> 3. universally closed (Descent, Lemma 02KS);
> 4. (quasi-)separated (Descent, Lemmas 02KR and 02KU);
> 5. monomorphism (Descent, Lemma 02YK);
> 6. surjective (Descent, Lemma 02KV);
> 7. universally injective (Descent, Lemma 02KW);
> 8. affine (Descent, Lemma 02L5);
> 9. quasi-affine (Descent, Lemma 02L7);
> 10. (locally) of finite type (Descent, Lemmas 02KX and 02KZ);
> 11. (locally) quasi-finite (Descent, Lemma 02VI);
> 12. (locally) of finite presentation (Descent, Lemmas 02KY and 02L0);
> 13. locally of finite type of relative dimension `d` (Descent, Lemma 02VJ);
> 14. universally open (Descent, Lemma 02KT);
> 15. flat (Descent, Lemma 02L2);
> 16. syntomic (Descent, Lemma 02VK);
> 17. smooth (Descent, Lemma 02VL);
> 18. unramified, resp. G-unramified (Descent, Lemma 02VM);
> 19. étale (Descent, Lemma 02VN);
> 20. proper (Descent, Lemma 02L1);
> 21. finite or integral (Descent, Lemma 02LA);
> 22. finite locally free (Descent, Lemma 02VO), with the rank unconstrained or fixed;
> 23. universally submersive (Descent, Lemma 0CEW);
> 24. universal homeomorphism (Descent, Lemma 0CEX).
>
> The final conjunct is the remark's last sentence: the property of being an immersion may *not* be
> fpqc local on the base, but it is stable under base change and fppf local on the base, by Descent,
> Lemma 02YM. No fpqc locality is asserted of immersions in general.

```lean
public theorem fpqcAndFppfLocalOnBase_allEntries_and_isImmersion_fppf :
    -- entry (1)(a), (b), (c): closed, open and quasi-compact immersions
    ((MorphismProperty.IsStableUnderBaseChange (@IsClosedImmersion : MorphismProperty Scheme.{u}) ∧
       MorphismProperty.IsLocalAtTarget
           (@IsClosedImmersion : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
       MorphismProperty.IsLocalAtTarget
           (@IsClosedImmersion : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage) ∧
      (MorphismProperty.IsStableUnderBaseChange (@IsOpenImmersion : MorphismProperty Scheme.{u}) ∧
       MorphismProperty.IsLocalAtTarget
           (@IsOpenImmersion : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
       MorphismProperty.IsLocalAtTarget
           (@IsOpenImmersion : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage) ∧
      (MorphismProperty.IsStableUnderBaseChange
           (@IsImmersion ⊓ @QuasiCompact : MorphismProperty Scheme.{u}) ∧
       MorphismProperty.IsLocalAtTarget
           (@IsImmersion ⊓ @QuasiCompact : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
       MorphismProperty.IsLocalAtTarget
           (@IsImmersion ⊓ @QuasiCompact : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage)) ∧
    -- entry (2): quasi-compact
    (MorphismProperty.IsStableUnderBaseChange (@QuasiCompact : MorphismProperty Scheme.{u}) ∧
     MorphismProperty.IsLocalAtTarget
         (@QuasiCompact : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
     MorphismProperty.IsLocalAtTarget
         (@QuasiCompact : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage) ∧
    -- entry (3): universally closed
    (MorphismProperty.IsStableUnderBaseChange (@UniversallyClosed : MorphismProperty Scheme.{u}) ∧
     MorphismProperty.IsLocalAtTarget
         (@UniversallyClosed : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
     MorphismProperty.IsLocalAtTarget
         (@UniversallyClosed : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage) ∧
    -- entry (4): separated, and quasi-separated
    ((MorphismProperty.IsStableUnderBaseChange (@IsSeparated : MorphismProperty Scheme.{u}) ∧
       MorphismProperty.IsLocalAtTarget
           (@IsSeparated : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
       MorphismProperty.IsLocalAtTarget
           (@IsSeparated : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage) ∧
      (MorphismProperty.IsStableUnderBaseChange (@QuasiSeparated : MorphismProperty Scheme.{u}) ∧
       MorphismProperty.IsLocalAtTarget
           (@QuasiSeparated : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
       MorphismProperty.IsLocalAtTarget
           (@QuasiSeparated : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage)) ∧
    -- entry (5): monomorphism
    (MorphismProperty.IsStableUnderBaseChange (MorphismProperty.monomorphisms Scheme.{u}) ∧
     MorphismProperty.IsLocalAtTarget
         (MorphismProperty.monomorphisms Scheme.{u}) Scheme.fpqcPrecoverage ∧
     MorphismProperty.IsLocalAtTarget
         (MorphismProperty.monomorphisms Scheme.{u}) Scheme.fppfPrecoverage) ∧
    -- entry (6): surjective
    (MorphismProperty.IsStableUnderBaseChange (@Surjective : MorphismProperty Scheme.{u}) ∧
     MorphismProperty.IsLocalAtTarget
         (@Surjective : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
     MorphismProperty.IsLocalAtTarget
         (@Surjective : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage) ∧
    -- entry (7): universally injective
    (MorphismProperty.IsStableUnderBaseChange
         (@UniversallyInjective : MorphismProperty Scheme.{u}) ∧
     MorphismProperty.IsLocalAtTarget
         (@UniversallyInjective : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
     MorphismProperty.IsLocalAtTarget
         (@UniversallyInjective : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage) ∧
    -- entry (8): affine
    (MorphismProperty.IsStableUnderBaseChange (@IsAffineHom : MorphismProperty Scheme.{u}) ∧
     MorphismProperty.IsLocalAtTarget
         (@IsAffineHom : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
     MorphismProperty.IsLocalAtTarget
         (@IsAffineHom : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage) ∧
    -- entry (9): quasi-affine
    (MorphismProperty.IsStableUnderBaseChange (@IsQuasiAffineHom : MorphismProperty Scheme.{u}) ∧
     MorphismProperty.IsLocalAtTarget
         (@IsQuasiAffineHom : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
     MorphismProperty.IsLocalAtTarget
         (@IsQuasiAffineHom : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage) ∧
    -- entry (10): locally of finite type, and of finite type
    ((MorphismProperty.IsStableUnderBaseChange
           (@LocallyOfFiniteType : MorphismProperty Scheme.{u}) ∧
       MorphismProperty.IsLocalAtTarget
           (@LocallyOfFiniteType : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
       MorphismProperty.IsLocalAtTarget
           (@LocallyOfFiniteType : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage) ∧
      (MorphismProperty.IsStableUnderBaseChange
           (@LocallyOfFiniteType ⊓ @QuasiCompact : MorphismProperty Scheme.{u}) ∧
       MorphismProperty.IsLocalAtTarget
           (@LocallyOfFiniteType ⊓ @QuasiCompact : MorphismProperty Scheme.{u})
           Scheme.fpqcPrecoverage ∧
       MorphismProperty.IsLocalAtTarget
           (@LocallyOfFiniteType ⊓ @QuasiCompact : MorphismProperty Scheme.{u})
           Scheme.fppfPrecoverage)) ∧
    -- entry (11): locally quasi-finite, and quasi-finite
    ((MorphismProperty.IsStableUnderBaseChange
           (@LocallyOfFiniteType ⊓ @LocallyQuasiFinite : MorphismProperty Scheme.{u}) ∧
       MorphismProperty.IsLocalAtTarget
           (@LocallyOfFiniteType ⊓ @LocallyQuasiFinite : MorphismProperty Scheme.{u})
           Scheme.fpqcPrecoverage ∧
       MorphismProperty.IsLocalAtTarget
           (@LocallyOfFiniteType ⊓ @LocallyQuasiFinite : MorphismProperty Scheme.{u})
           Scheme.fppfPrecoverage) ∧
      (MorphismProperty.IsStableUnderBaseChange
           ((@LocallyOfFiniteType ⊓ @QuasiCompact : MorphismProperty Scheme.{u}) ⊓
             @LocallyQuasiFinite) ∧
       MorphismProperty.IsLocalAtTarget
           ((@LocallyOfFiniteType ⊓ @QuasiCompact : MorphismProperty Scheme.{u}) ⊓
             @LocallyQuasiFinite) Scheme.fpqcPrecoverage ∧
       MorphismProperty.IsLocalAtTarget
           ((@LocallyOfFiniteType ⊓ @QuasiCompact : MorphismProperty Scheme.{u}) ⊓
             @LocallyQuasiFinite) Scheme.fppfPrecoverage)) ∧
    -- entry (12): locally of finite presentation, and of finite presentation
    ((MorphismProperty.IsStableUnderBaseChange
           (@LocallyOfFinitePresentation : MorphismProperty Scheme.{u}) ∧
       MorphismProperty.IsLocalAtTarget
           (@LocallyOfFinitePresentation : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
       MorphismProperty.IsLocalAtTarget
           (@LocallyOfFinitePresentation : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage) ∧
      (MorphismProperty.IsStableUnderBaseChange
           (@FinitePresentation : MorphismProperty Scheme.{u}) ∧
       MorphismProperty.IsLocalAtTarget
           (@FinitePresentation : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
       MorphismProperty.IsLocalAtTarget
           (@FinitePresentation : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage)) ∧
    -- entry (13): locally of finite type of relative dimension `d`
    (∀ d : ℕ,
      MorphismProperty.IsStableUnderBaseChange (locallyOfFiniteTypeRelativeDimension.{u} d) ∧
      MorphismProperty.IsLocalAtTarget
          (locallyOfFiniteTypeRelativeDimension.{u} d) Scheme.fpqcPrecoverage ∧
      MorphismProperty.IsLocalAtTarget
          (locallyOfFiniteTypeRelativeDimension.{u} d) Scheme.fppfPrecoverage) ∧
    -- entry (14): universally open
    (MorphismProperty.IsStableUnderBaseChange (@UniversallyOpen : MorphismProperty Scheme.{u}) ∧
     MorphismProperty.IsLocalAtTarget
         (@UniversallyOpen : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
     MorphismProperty.IsLocalAtTarget
         (@UniversallyOpen : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage) ∧
    -- entry (15): flat
    (MorphismProperty.IsStableUnderBaseChange (@Flat : MorphismProperty Scheme.{u}) ∧
     MorphismProperty.IsLocalAtTarget
         (@Flat : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
     MorphismProperty.IsLocalAtTarget
         (@Flat : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage) ∧
    -- entry (16): syntomic
    (MorphismProperty.IsStableUnderBaseChange (@Syntomic : MorphismProperty Scheme.{u}) ∧
     MorphismProperty.IsLocalAtTarget
         (@Syntomic : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
     MorphismProperty.IsLocalAtTarget
         (@Syntomic : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage) ∧
    -- entry (17): smooth
    (MorphismProperty.IsStableUnderBaseChange (@Smooth : MorphismProperty Scheme.{u}) ∧
     MorphismProperty.IsLocalAtTarget
         (@Smooth : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
     MorphismProperty.IsLocalAtTarget
         (@Smooth : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage) ∧
    -- entry (18): unramified, and G-unramified
    ((MorphismProperty.IsStableUnderBaseChange (@Unramified : MorphismProperty Scheme.{u}) ∧
       MorphismProperty.IsLocalAtTarget
           (@Unramified : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
       MorphismProperty.IsLocalAtTarget
           (@Unramified : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage) ∧
      (MorphismProperty.IsStableUnderBaseChange (@GUnramified : MorphismProperty Scheme.{u}) ∧
       MorphismProperty.IsLocalAtTarget
           (@GUnramified : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
       MorphismProperty.IsLocalAtTarget
           (@GUnramified : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage)) ∧
    -- entry (19): étale
    (MorphismProperty.IsStableUnderBaseChange (@Etale : MorphismProperty Scheme.{u}) ∧
     MorphismProperty.IsLocalAtTarget
         (@Etale : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
     MorphismProperty.IsLocalAtTarget
         (@Etale : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage) ∧
    -- entry (20): proper
    (MorphismProperty.IsStableUnderBaseChange (@IsProper : MorphismProperty Scheme.{u}) ∧
     MorphismProperty.IsLocalAtTarget
         (@IsProper : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
     MorphismProperty.IsLocalAtTarget
         (@IsProper : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage) ∧
    -- entry (21): finite, and integral
    ((MorphismProperty.IsStableUnderBaseChange (@IsFinite : MorphismProperty Scheme.{u}) ∧
       MorphismProperty.IsLocalAtTarget
           (@IsFinite : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
       MorphismProperty.IsLocalAtTarget
           (@IsFinite : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage) ∧
      (MorphismProperty.IsStableUnderBaseChange (@IsIntegralHom : MorphismProperty Scheme.{u}) ∧
       MorphismProperty.IsLocalAtTarget
           (@IsIntegralHom : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
       MorphismProperty.IsLocalAtTarget
           (@IsIntegralHom : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage)) ∧
    -- entry (22): finite locally free, of unconstrained and of fixed rank
    ((MorphismProperty.IsStableUnderBaseChange
           (@Stacks.Morphisms.IsFiniteLocallyFree : MorphismProperty Scheme.{u}) ∧
       MorphismProperty.IsLocalAtTarget
           (@Stacks.Morphisms.IsFiniteLocallyFree : MorphismProperty Scheme.{u})
           Scheme.fpqcPrecoverage ∧
       MorphismProperty.IsLocalAtTarget
           (@Stacks.Morphisms.IsFiniteLocallyFree : MorphismProperty Scheme.{u})
           Scheme.fppfPrecoverage) ∧
      (∀ d : ℕ,
        MorphismProperty.IsStableUnderBaseChange
            (Stacks.Morphisms.IsFiniteLocallyFreeOfRank.property.{u} d) ∧
        MorphismProperty.IsLocalAtTarget
            (Stacks.Morphisms.IsFiniteLocallyFreeOfRank.property.{u} d) Scheme.fpqcPrecoverage ∧
        MorphismProperty.IsLocalAtTarget
            (Stacks.Morphisms.IsFiniteLocallyFreeOfRank.property.{u} d) Scheme.fppfPrecoverage)) ∧
    -- entry (23): universally submersive
    (MorphismProperty.IsStableUnderBaseChange
         ((topologically @Topology.IsQuotientMap : MorphismProperty Scheme.{u}).universally) ∧
     MorphismProperty.IsLocalAtTarget
         ((topologically @Topology.IsQuotientMap : MorphismProperty Scheme.{u}).universally)
         Scheme.fpqcPrecoverage ∧
     MorphismProperty.IsLocalAtTarget
         ((topologically @Topology.IsQuotientMap : MorphismProperty Scheme.{u}).universally)
         Scheme.fppfPrecoverage) ∧
    -- entry (24): universal homeomorphism
    (MorphismProperty.IsStableUnderBaseChange
         (@UniversalHomeomorphism : MorphismProperty Scheme.{u}) ∧
     MorphismProperty.IsLocalAtTarget
         (@UniversalHomeomorphism : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage ∧
     MorphismProperty.IsLocalAtTarget
         (@UniversalHomeomorphism : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage) ∧
    -- the last sentence (02YM): immersions in general are fppf local on the base, and no fpqc
    -- locality is claimed of them
    (MorphismProperty.IsStableUnderBaseChange (@IsImmersion : MorphismProperty Scheme.{u}) ∧
      MorphismProperty.IsLocalAtTarget (@IsImmersion : MorphismProperty Scheme.{u})
        Scheme.fppfPrecoverage)
```

**`Stacks.Descent.locallyOfFiniteType_isLocalAtTarget_fppf`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Diagonal.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Diagonal.lean#L238). The attribute's comment: “locally\_finite\_type”.

> **Stacks 02WH.** Being locally of finite type is fppf local on the base.

```lean
instance locallyOfFiniteType_isLocalAtTarget_fppf :
    MorphismProperty.IsLocalAtTarget
      (@AlgebraicGeometry.LocallyOfFiniteType : MorphismProperty AlgebraicGeometry.Scheme.{u})
      AlgebraicGeometry.Scheme.fppfPrecoverage
```

**`AlgebraicGeometry.instIsLocalAtTargetFppfMonomorphisms`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/FpqcLocal.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/FpqcLocal.lean#L81). The attribute's comment: “monomorphism”. References: SGA 4 IV (8.5.5), “special case”.

> Monomorphisms of schemes are local on the target for the fppf precoverage.

```lean
instance instIsLocalAtTargetFppfMonomorphisms :
    (MorphismProperty.monomorphisms Scheme).IsLocalAtTarget Scheme.fppfPrecoverage
```

**`AlgebraicGeometry.surjective_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/FpqcLocal.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/FpqcLocal.lean#L92). The attribute's comment: “surjective”. References: SGA 4 IV (8.5.5).

> **Stacks Project, Tag 02WH (surjective).** Surjectivity of scheme morphisms is local
> on the target for the fpqc precoverage.

```lean
public instance surjective_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget (@Surjective.{u}) Scheme.fpqcPrecoverage
```

**`AlgebraicGeometry.surjective_isLocalAtTarget_fppf`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/FpqcLocal.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/FpqcLocal.lean#L119). The attribute's comment: “surjective”.

> **Stacks Project, Tag 02WH (surjective).** Surjectivity of scheme morphisms is local
> on the target for the fppf precoverage.

```lean
public instance surjective_isLocalAtTarget_fppf :
    MorphismProperty.IsLocalAtTarget (@Surjective.{u}) Scheme.fppfPrecoverage
```

**`AlgebraicGeometry.universallyInjective_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/FpqcLocal.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/FpqcLocal.lean#L224). The attribute's comment: “universally\_injective”.

> Universal injectivity of morphisms of schemes is fpqc local on the target.

```lean
public instance universallyInjective_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget
      (@UniversallyInjective : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage
```

**`AlgebraicGeometry.universallyInjective_isLocalAtTarget_fppf`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/FpqcLocal.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/FpqcLocal.lean#L253). The attribute's comment: “universally\_injective”.

> Universal injectivity of morphisms of schemes is fppf local on the target.

```lean
public instance universallyInjective_isLocalAtTarget_fppf :
    MorphismProperty.IsLocalAtTarget
      (@UniversallyInjective : MorphismProperty Scheme.{u}) Scheme.fppfPrecoverage
```

**`Stacks.Descent.quasiCompact_isLocalAtTarget_fppf`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/QuasiCompactLocal.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/QuasiCompactLocal.lean#L66). The attribute's comment: “quasi\_compact”.

> **Stacks 02WH.** Quasi-compactness of a morphism of schemes is fppf local on the base.

```lean
public instance quasiCompact_isLocalAtTarget_fppf :
    MorphismProperty.IsLocalAtTarget (@QuasiCompact : MorphismProperty Scheme.{u})
      Scheme.fppfPrecoverage
```

Declarations registered for the tag:

- [`MorphismProperty.IsStableUnderBaseChange.monomorphisms`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=MorphismProperty.IsStableUnderBaseChange.monomorphisms#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/FpqcLocal.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/FpqcLocal.lean#L75) (StacksFrontier): “monomorphism”.
- [`AlgebraicGeometry.isLocalAtTarget_monomorphisms_fpqc`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/SchemeProperty/FpqcLocal.lean#L55), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/FpqcLocal.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/FpqcLocal.lean#L77) (StacksFrontier): “monomorphism”.
- [`AlgebraicGeometry.Surjective.instIsStableUnderBaseChangeScheme`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Surjective.instIsStableUnderBaseChangeScheme#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/FpqcLocal.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/FpqcLocal.lean#L87) (StacksFrontier): “surjective”. References: EGA I (3.5.2); SGA 1 VIII (3.1), “Surjectivity clause”; SGA 3 VIB (10.1), “partial, sufficiency”; SGA 3 VIIB (2.4.1), “special case”.
- [`AlgebraicGeometry.UniversallyInjective.isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.UniversallyInjective.isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/FpqcLocal.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/FpqcLocal.lean#L219) (StacksFrontier): “universally\_injective”. References: SGA 3 VIB (10.1), “partial, sufficiency”; SGA 3 VIB (2.6), “more general”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 65.4, Tag 02WE](https://stacks.math.columbia.edu/tag/02WE)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
