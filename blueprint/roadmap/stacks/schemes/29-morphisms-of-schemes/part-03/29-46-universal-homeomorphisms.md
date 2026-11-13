---
declaration: section
origin: cited
lean: AlgebraicGeometry.UniversalHomeomorphism, AlgebraicGeometry.universalHomeomorphism_iff_integral_universallyInjective_surjective, AlgebraicGeometry.universalHomeomorphism_nilradical_subschemeι, AlgebraicGeometry.isClosedImmersion_of_infinitesimal_baseChange, AlgebraicGeometry.universalHomeomorphism_hasTwoOutOfThreeProperty
statement: formalized
proof: formalized
---

# 29.46 Universal homeomorphisms

Section 29.46 of the Stacks Project, [Tag 04DC](https://stacks.math.columbia.edu/tag/04DC). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04DD, a definition

[Tag 04DD](https://stacks.math.columbia.edu/tag/04DD) in the Stacks Project.

**`AlgebraicGeometry.UniversalHomeomorphism`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Defs/Basic.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Defs/Basic.lean#L44). References: EGA IV (2.4.2), “universal homeomorphism”; SGA 4 VIII (1.4).

> A morphism of schemes is a universal homeomorphism if every base change is
> a homeomorphism on the underlying topological spaces.

```lean
class UniversalHomeomorphism {X Y : Scheme.{u}} (f : X ⟶ Y) : Prop
```

## Tag 04DF, a lemma

[Tag 04DF](https://stacks.math.columbia.edu/tag/04DF) in the Stacks Project.

**`AlgebraicGeometry.universalHomeomorphism_iff_integral_universallyInjective_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Defs/Integral.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Defs/Integral.lean#L43). References: EGA IV (18.12.11), “integral case”; EGA IV (2.4.5), “(i)”; EGA IV (15.2.4), “more general”; SGA 4 VIII (1.4).

> A morphism of schemes is a universal homeomorphism if and only if it is integral,
> universally injective, and surjective.

```lean
theorem universalHomeomorphism_iff_integral_universallyInjective_surjective
    {X Y : Scheme.{u}} (f : X ⟶ Y) :
    UniversalHomeomorphism f ↔
      IsIntegralHom f ∧ UniversallyInjective f ∧ Surjective f
```

## Tag 054M, a lemma

[Tag 054M](https://stacks.math.columbia.edu/tag/054M) in the Stacks Project.

**`AlgebraicGeometry.universalHomeomorphism_nilradical_subschemeι`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Reduction.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Reduction.lean#L41). References: EGA IV (2.4.8), “(ii) univ. homeo”.

> The reduction of a scheme is universally homeomorphic to the scheme through its canonical
> closed immersion.

```lean
instance universalHomeomorphism_nilradical_subschemeι (X : Scheme.{u}) :
    UniversalHomeomorphism X.nilradical.subschemeι
```

## Tag 0896, a lemma

[Tag 0896](https://stacks.math.columbia.edu/tag/0896) in the Stacks Project.

**`AlgebraicGeometry.isClosedImmersion_of_infinitesimal_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/ClosedImmersionInfinitesimal.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/ClosedImmersionInfinitesimal.lean#L214).

> A closed immersion can be detected after a closed, point-bijective base change
> under a finite-type or finite-presentation hypothesis.

```lean
public theorem isClosedImmersion_of_infinitesimal_baseChange
    {X S S' : Scheme.{u}} (f : X ⟶ S) (g : S' ⟶ S)
    [IsClosedImmersion g] (hg : Function.Bijective g.base)
    [IsClosedImmersion (pullback.snd f g)]
    (hfinite : (LocallyOfFiniteType f ∧ QuasiCompact f) ∨ FinitePresentation g) :
    IsClosedImmersion f
```

## Tag 0H2M, a lemma

[Tag 0H2M](https://stacks.math.columbia.edu/tag/0H2M) in the Stacks Project.

**`AlgebraicGeometry.universalHomeomorphism_hasTwoOutOfThreeProperty`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Defs/TwoOutOfThree.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Defs/TwoOutOfThree.lean#L128).

> Universal homeomorphisms of schemes satisfy the two-out-of-three property.

```lean
instance universalHomeomorphism_hasTwoOutOfThreeProperty :
    MorphismProperty.HasTwoOutOfThreeProperty
      (@UniversalHomeomorphism.{u} : MorphismProperty Scheme.{u})
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.46, Tag 04DC](https://stacks.math.columbia.edu/tag/04DC)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
