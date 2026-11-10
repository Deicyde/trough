---
declaration: section
origin: cited
lean: Module.finitePresentation_of_projective, Module.Flat.of_projective, Module.Flat.projective_of_finitePresentation, Module.FinitePresentation.of_isBaseChange_of_faithfullyFlat, Module.Projective.of_finite_of_isBaseChange_of_faithfullyFlat
statement: formalized
proof: formalized
---

# 10.83 Descent for finite projective modules

Section 10.83 of the Stacks Project, [Tag 058Q](https://stacks.math.columbia.edu/tag/058Q). 3 tags here are carried by 2 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 058R, a lemma

[Tag 058R](https://stacks.math.columbia.edu/tag/058R) in the Stacks Project.

Declarations registered for the tag:

- [`Module.finitePresentation_of_projective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.finitePresentation_of_projective#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L265) (StacksFrontier): “(⇒) finitely presented”.
- [`Module.Flat.of_projective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.Flat.of_projective#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L266) (StacksFrontier): “(⇒) flat: projective modules are flat”. References: EGA 0 (6.1.1), “more general”; EGA 0 (6.1.2), “more general”; EGA IV (12.3.1), “a ⇒ b”; SGA 1 IV (4.3), “(ii) ⇒ (iii)”; SGA 3 VIIB (0.2.2), “projective implies flat”.
- [`Module.Flat.projective_of_finitePresentation`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.Flat.projective_of_finitePresentation#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L267) (StacksFrontier): “(⇐) projective; finiteness comes from `FinitePresentation` (instance)”. References: EGA 0 (10.1.3), “(ii): c ⇒ b, c ⇒ b”; EGA III (7.7.12), “more general”; EGA IV (12.3.1), “b ⇒ a”; SGA 1 IV (4.3), “case (b): (iii) ⇒ (ii)”; SGA 3 VIIB (0.2.2), “partial”; SGA 3 VIIB (1.2.1), “special case”; SGA 5 IIIB (5.10), “partial”; SGA 6 I (5.8.3), “(ii) ⇒ (i)”; SGA 6 VI (1.5.2), “Case B = A, n = 0”.

## Tag 03C4, a lemma

[Tag 03C4](https://stacks.math.columbia.edu/tag/03C4) in the Stacks Project.

**`Module.FinitePresentation.of_isBaseChange_of_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/FaithfullyFlat/Descent.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/FaithfullyFlat/Descent.lean#L184). The attribute's comment: “Part (2). Part (1) is `Module.Finite.of_finite_tensorProduct_of_faithfullyFlat` and part (3) is `Module.Flat.of_flat_tensorProduct`, both in Mathlib.”. References: EGA IV (2.5.2), “(ii), descent, affine”; EGA IV (2.5.3), “fin. pres., descent”; EGA IV (2.5.2), “(ii), descent, affine”; SGA 1 VIII (1.11), “fin. pres., descent”; SGA 1 VIII (1.10), “fin. pres., affine”; SGA 4½ Arcata (1.4.2), “(ii), fin. presentation”; SGA 1 VIII (1.11), “fin. pres., descent”; SGA 4½ Arcata (1.4.2), “(ii), fin. presentation”.

> **Stacks 03C4** (part 2). Let `R → S` be a faithfully flat ring map, let `M` be an `R`-module
> and let `f : M →ₗ[R] N` exhibit the `S`-module `N` as the base change of `M` along `R → S`. If `N`
> is a finitely presented `S`-module, then `M` is a finitely presented `R`-module.

```lean
theorem FinitePresentation.of_isBaseChange_of_faithfullyFlat {R : Type*} [CommRing R]
    {S : Type*} [CommRing S] [Algebra R S] [Module.FaithfullyFlat R S]
    {M : Type*} [AddCommGroup M] [Module R M]
    {N : Type*} [AddCommGroup N] [Module R N] [Module S N] [IsScalarTower R S N]
    (f : M →ₗ[R] N) (h : IsBaseChange S f) [Module.FinitePresentation S N] :
    Module.FinitePresentation R M
```

## Tag 058S, a proposition

[Tag 058S](https://stacks.math.columbia.edu/tag/058S) in the Stacks Project.

**`Module.Projective.of_finite_of_isBaseChange_of_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/FaithfullyFlat/Descent.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/FaithfullyFlat/Descent.lean#L209). The attribute's comment: “The projectivity half of the conclusion; the finiteness half is Mathlib's `Module.Finite.of_finite_tensorProduct_of_faithfullyFlat`.”. References: SGA 1 VIII (1.10), “loc. free, affine”; SGA 3 VIB (11.8.2), “finite projective case”; SGA 3 VIB (11.8.1), “(ii), special case”; SGA 3 VIB (11.9.1), “special case”.

> **Stacks 058S** (the projectivity half). Let `R → S` be a faithfully flat ring map, let `M` be
> an `R`-module and let `f : M →ₗ[R] N` exhibit the `S`-module `N` as the base change of `M` along
> `R → S`. If `N` is a finite projective `S`-module, then `M` is a projective `R`-module. Together
> with `Module.Finite.of_finite_tensorProduct_of_faithfullyFlat` this says that being a finite
> projective module descends along a faithfully flat ring map.

```lean
theorem Projective.of_finite_of_isBaseChange_of_faithfullyFlat {R : Type*} [CommRing R]
    {S : Type*} [CommRing S] [Algebra R S] [Module.FaithfullyFlat R S]
    {M : Type*} [AddCommGroup M] [Module R M]
    {N : Type*} [AddCommGroup N] [Module R N] [Module S N] [IsScalarTower R S N]
    (f : M →ₗ[R] N) (h : IsBaseChange S f)
    [Module.Finite S N] [Module.Projective S N] :
    Module.Projective R M
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.83, Tag 058Q](https://stacks.math.columbia.edu/tag/058Q)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
