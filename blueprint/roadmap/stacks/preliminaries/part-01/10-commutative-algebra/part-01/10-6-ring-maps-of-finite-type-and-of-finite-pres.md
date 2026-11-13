---
declaration: section
origin: cited
lean: RingHom.FinitePresentation, RingHom.FiniteType, RingHom.finiteType_finitePresentation_comp_and_of_comp, RingHom.FinitePresentation.comp, RingHom.FinitePresentation.of_comp_finiteType, RingHom.FiniteType.comp, RingHom.FiniteType.of_comp_finiteType, Algebra.FinitePresentation.ker_fg_of_mvPolynomial
statement: formalized
proof: formalized
---

# 10.6 Ring maps of finite type and of finite presentation

Section 10.6 of the Stacks Project, [Tag 00F2](https://stacks.math.columbia.edu/tag/00F2). 4 tags here are carried by 2 declarations of the repository (all in StacksFrontier) and 7 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00F3, a definition

[Tag 00F3](https://stacks.math.columbia.edu/tag/00F3) in the Stacks Project.

Declarations registered for the tag:

- [`RingHom.FinitePresentation`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingHom.FinitePresentation#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/FinitePresentation.lean, line 10](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/FinitePresentation.lean#L10) (StacksCore). References: EGA IV (1.4.1); SGA 1 VIII (3.6).
- [`RingHom.FiniteType`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingHom.FiniteType#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/FiniteType.lean, line 14](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/FiniteType.lean#L14) (StacksCore). References: EGA 0 (1.0.5); EGA I (6.3.1), “(P)”; EGA IV (1.3.1).

## Tag 00F4, a lemma

[Tag 00F4](https://stacks.math.columbia.edu/tag/00F4) in the Stacks Project.

**`RingHom.finiteType_finitePresentation_comp_and_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FinitePresentation.lean, line 35](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FinitePresentation.lean#L35). The attribute's comment: “the four parts of the lemma”.

> **Stacks 00F4 (Lemma 10.6.2).** Let `f : R →+* S'` and `g : S' →+* S` be ring maps.
> 1. If `f` and `g` are of finite type, so is `g.comp f` (`RingHom.FiniteType.comp`).
> 2. If `f` and `g` are of finite presentation, so is `g.comp f`
>    (`RingHom.FinitePresentation.comp`).
> 3. If `g.comp f` is of finite type, so is `g` (`RingHom.FiniteType.of_comp_finiteType`).
> 4. If `g.comp f` is of finite presentation and `f` is of finite type, then `g` is of finite
>    presentation (`RingHom.FinitePresentation.of_comp_finiteType`).

```lean
theorem finiteType_finitePresentation_comp_and_of_comp {R : Type u} {S' : Type v} {S : Type w}
    [CommRing R] [CommRing S'] [CommRing S] (f : R →+* S') (g : S' →+* S) :
    (f.FiniteType → g.FiniteType → (g.comp f).FiniteType) ∧
      (f.FinitePresentation → g.FinitePresentation → (g.comp f).FinitePresentation) ∧
      ((g.comp f).FiniteType → g.FiniteType) ∧
      ((g.comp f).FinitePresentation → f.FiniteType → g.FinitePresentation)
```

Declarations registered for the tag:

- [`RingHom.FinitePresentation.comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingHom.FinitePresentation.comp#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/FinitePresentation.lean, line 11](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/FinitePresentation.lean#L11) (StacksCore). References: EGA IV (1.4.3), “(ii), affine schemes”; EGA IV (1.6.2), “(ii), affine case”; SGA 1 VIII (3.6), “special case”.
- [`RingHom.FinitePresentation.of_comp_finiteType`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingHom.FinitePresentation.of_comp_finiteType#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/FinitePresentation.lean, line 12](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/FinitePresentation.lean#L12) (StacksCore). References: EGA IV (1.4.3), “(v), affine schemes”; EGA IV (1.6.2), “(v), affine case”.
- [`RingHom.FiniteType.comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingHom.FiniteType.comp#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/FiniteType.lean, line 15](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/FiniteType.lean#L15) (StacksCore). References: EGA I (6.3.4), “clause (ii), affine case”; EGA I (6.6.6), “(ii), affine schemes”; EGA I (10.13.5), “(i), special case”; EGA IV (1.3.1); EGA IV (1.5.4), “(ii) for affine schemes”.
- [`RingHom.FiniteType.of_comp_finiteType`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingHom.FiniteType.of_comp_finiteType#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/FiniteType.lean, line 16](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/FiniteType.lean#L16) (StacksCore). References: EGA I (6.3.4), “clause (v), affine case”; EGA I (6.3.6), “affine case”; EGA I (6.6.6), “(v), affine schemes”; EGA IV (10.10.3), “more general”; EGA IV (1.5.4), “special case”.

## Tag 00R2, a lemma

[Tag 00R2](https://stacks.math.columbia.edu/tag/00R2) in the Stacks Project.

Declarations registered for the tag:

- [`Algebra.FinitePresentation.ker_fg_of_mvPolynomial`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.FinitePresentation.ker_fg_of_mvPolynomial#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/FinitePresentation.lean, line 13](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/FinitePresentation.lean#L13) (StacksCore). References: EGA IV (1.4.4), “necessity”; SGA 3 V (9.1), “special case”; SGA 3 VIB (1.3.0).

## Tag 0561, a lemma

[Tag 0561](https://stacks.math.columbia.edu/tag/0561) in the Stacks Project.

**`Module.FinitePresentation.of_restrictScalars_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/BlowupFiniteTypeReduction.lean, line 238](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/BlowupFiniteTypeReduction.lean#L238). The attribute's comment: “the module statement, not the analogue for algebras”.

> **Stacks 0561.** Let `R → S` be a ring map of finite type and let `M` be an `S`-module which
> is finitely presented as an `R`-module. Then `M` is finitely presented as an `S`-module.
>
> Mathlib's `Module.FinitePresentation.trans` is the converse implication: it deduces finite
> presentation over `R` from finite presentation over `S` together with finite presentation of `S`
> over `R`. Mathlib's own declaration carrying the tag `0561`,
> `Algebra.FinitePresentation.of_restrict_scalars_finitePresentation`, is not this lemma but the
> analogue for algebras in place of modules.

```lean
theorem Module.FinitePresentation.of_restrictScalars_of_finiteType (R S M : Type*) [CommRing R]
    [CommRing S] [Algebra R S] [AddCommGroup M] [Module R M] [Module S M] [IsScalarTower R S M]
    [Algebra.FiniteType R S] [Module.FinitePresentation R M] : Module.FinitePresentation S M
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.6, Tag 00F2](https://stacks.math.columbia.edu/tag/00F2)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
