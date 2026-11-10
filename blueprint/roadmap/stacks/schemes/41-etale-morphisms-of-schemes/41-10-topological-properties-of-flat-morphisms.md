---
declaration: section
origin: cited
lean: AlgebraicGeometry.isOpen_setOf_isFlatAt_of_isLocallyNoetherian, AlgebraicGeometry.isOpen_setOf_coherent_flatOverAt, AlgebraicGeometry.UniversallyOpen.of_flat, AlgebraicGeometry.LocallyOfFinitePresentation.iff_locallyOfFiniteType, AlgebraicGeometry.Flat.isQuotientMap_of_surjective
statement: formalized
proof: formalized
---

# 41.10 Topological properties of flat morphisms

Section 41.10 of the Stacks Project, [Tag 0254](https://stacks.math.columbia.edu/tag/0254). 3 tags here are carried by 1 declaration of the repository (in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0255, a theorem

[Tag 0255](https://stacks.math.columbia.edu/tag/0255) in the Stacks Project.

**`AlgebraicGeometry.isOpen_setOf_isFlatAt_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/FlatLocusOpenness.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/FlatLocusOpenness.lean#L52). The attribute's comment: “flat locus of the morphism”. References: EGA IV (11.1.1), “F = O_X case”; EGA IV (11.1.6), “M = C = B case”; EGA IV (11.3.1), “Noetherian, F = O_X”; SGA 1 IV (6.10), “F = O_X case”.

> **Stacks Project, Tag 0255.** The flat locus of a morphism locally of finite type to a
> locally Noetherian scheme is open.

```lean
theorem isOpen_setOf_isFlatAt_of_isLocallyNoetherian
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsLocallyNoetherian Y] [LocallyOfFiniteType f] :
    IsOpen {x : X | IsFlatAt f.toLRSHom.toShHom x}
```

Declarations registered for the tag:

- [`AlgebraicGeometry.isOpen_setOf_coherent_flatOverAt`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/FlatLocus.lean#L42), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/FlatLocusOpenness.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/FlatLocusOpenness.lean#L42) (StacksFrontier): “relative flat locus of a coherent module”.

## Tag 039K, a theorem

[Tag 039K](https://stacks.math.columbia.edu/tag/039K) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.UniversallyOpen.of_flat`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.UniversallyOpen.of_flat#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch41.lean, line 20](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch41.lean#L20) (StacksFrontier): “flat and locally of finite presentation implies universally open”. References: EGA IV (1.10.4), “b) ⇒ a), special case”; EGA IV (11.3.1), “special case”; EGA IV (14.4.10), “special case”; EGA IV (15.2.1); EGA IV (15.2.4), “(ii), special case”; EGA IV (18.2.7), “partial”; EGA IV (2.4.6); EGA IV (2.4.7), “more general”; EGA IV (4.4.1), “special case”; SGA 1 IV (6.6), “F = O_X”; SGA 1 VIII (4.9), “more general”; SGA 3 V (10.1.1), “more general”; SGA 3 V (4.1.1), “flat and fp implies open”; SGA 3 VIA (2.5.4), “Final implication”; SGA 3 VIB (3.11), “more general”; SGA 3 VIB (4.3); SGA 3 VIB (7.5), “f|_V is an open morphism”; SGA 3 X (5.4), “partial”; SGA 3 XVI (2.1), “more general”; SGA 6 VIII (1.3), “more general”.
- [`AlgebraicGeometry.LocallyOfFinitePresentation.iff_locallyOfFiniteType`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.LocallyOfFinitePresentation.iff_locallyOfFiniteType#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch41.lean, line 22](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch41.lean#L22) (StacksFrontier): “over a locally Noetherian base, locally of finite type is locally of finite presentation”. References: SGA 1 IX (4.7), “partial”; SGA 1 IX (4.10), “more general”; SGA 1 IX (4.12), “partial”; SGA 3 V (6.1), “partial”.

## Tag 0256, a theorem

[Tag 0256](https://stacks.math.columbia.edu/tag/0256) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Flat.isQuotientMap_of_surjective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Flat.isQuotientMap_of_surjective#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch41.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch41.lean#L49) (StacksFrontier): “faithfully flat means flat and surjective”. References: EGA IV (15.7.8), “partial”; EGA IV (2.3.12), “special case”; SGA 1 IX (2.2), “partial”; SGA 1 VIII (4.2), “special case”; SGA 1 VIII (4.3).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 41.10, Tag 0254](https://stacks.math.columbia.edu/tag/0254)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
