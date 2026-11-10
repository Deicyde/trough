---
declaration: section
origin: cited
lean: AlgebraicGeometry.LocallyRingedSpace, AlgebraicGeometry.LocallyRingedSpace.isLocalRing, AlgebraicGeometry.LocallyRingedSpace.residueField, AlgebraicGeometry.LocallyRingedSpace.Hom, AlgebraicGeometry.LocallyRingedSpace.isoOfSheafedSpaceIso, AlgebraicGeometry.LocallyRingedSpace.homOfSheafedSpaceHomOfIsIso
statement: formalized
proof: formalized
---

# 26.2 Locally ringed spaces

Section 26.2 of the Stacks Project, [Tag 01HA](https://stacks.math.columbia.edu/tag/01HA). 2 tags here are carried by 6 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01HB, a definition

[Tag 01HB](https://stacks.math.columbia.edu/tag/01HB) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.LocallyRingedSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.LocallyRingedSpace#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L106) (StacksFrontier): “Part 1: a locally ringed space is a topological space with a sheaf of rings all of whose stalks are local rings.”. References: EGA 0 (5.5.1); EGA I (1.8.2).
- [`AlgebraicGeometry.LocallyRingedSpace.isLocalRing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.LocallyRingedSpace.isLocalRing#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L109) (StacksFrontier): “Part 2: the local ring O_{X,x} of X at x is the stalk, which is local (the maximal ideal m_x is `IsLocalRing.maximalIdeal` of the stalk).”.
- [`AlgebraicGeometry.LocallyRingedSpace.residueField`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.LocallyRingedSpace.residueField#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L113) (StacksFrontier): “Part 2: the residue field kappa(x) = O_{X,x}/m_x of X at x.”. References: EGA 0 (5.5.1); SGA 1 I (7.5), “more general”.
- [`AlgebraicGeometry.LocallyRingedSpace.Hom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.LocallyRingedSpace.Hom#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L116) (StacksFrontier): “Part 3: a morphism of locally ringed spaces is a morphism of ringed spaces whose stalk maps are local ring maps.”. References: EGA I (1.8.2); EGA I (2.2.1), “more general”; EGA I (10.4.5), “special case”.

## Tag 01HC, a lemma

[Tag 01HC](https://stacks.math.columbia.edu/tag/01HC) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.LocallyRingedSpace.isoOfSheafedSpaceIso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.LocallyRingedSpace.isoOfSheafedSpaceIso#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L119) (StacksFrontier): “An isomorphism of ringed spaces between locally ringed spaces is an isomorphism of locally ringed spaces.”.
- [`AlgebraicGeometry.LocallyRingedSpace.homOfSheafedSpaceHomOfIsIso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.LocallyRingedSpace.homOfSheafedSpaceHomOfIsIso#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L129) (StacksFrontier): “The lift of the isomorphism of ringed spaces has the same underlying morphism.”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 26.2, Tag 01HA](https://stacks.math.columbia.edu/tag/01HA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
