---
declaration: section
origin: cited
lean: AlgebraicGeometry.universallyInjective_iff_forall_injective_pullback_fst, AlgebraicGeometry.IsRadicial, AlgebraicGeometry.UniversallyInjective, AlgebraicGeometry.universallyInjective_of_subsingleton_of_section, AlgebraicGeometry.Scheme.Hom.injective, AlgebraicGeometry.isSeparated_of_injective, AlgebraicGeometry.UniversallyInjective.isStableUnderBaseChange, AlgebraicGeometry.universallyInjective_isStableUnderComposition
statement: formalized
proof: formalized
---

# 29.10 Radicial and universally injective morphisms

Section 29.10 of the Stacks Project, [Tag 01S2](https://stacks.math.columbia.edu/tag/01S2). 5 tags here are carried by 3 declarations of the repository (all in StacksFrontier) and 6 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01S3, a definition

[Tag 01S3](https://stacks.math.columbia.edu/tag/01S3) in the Stacks Project.

**`AlgebraicGeometry.universallyInjective_iff_forall_injective_pullback_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Radicial.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Radicial.lean#L51). The attribute's comment: “(1) universally injective: every base change `S' ×_S X ⟶ S'` is injective on points; the definition is Mathlib's `AlgebraicGeometry.UniversallyInjective`, and this states it in the source's form”.

> Mathlib's `AlgebraicGeometry.UniversallyInjective` is the definition of the source: `f` is
> universally injective if and only if for every morphism `g : S' ⟶ S` the base change
> `S' ×_S X ⟶ S'` (the first projection of the chosen pullback) is injective on points.

```lean
theorem universallyInjective_iff_forall_injective_pullback_fst :
    UniversallyInjective f ↔
      ∀ (S' : Scheme.{u}) (g : S' ⟶ S), Function.Injective (pullback.fst g f)
```

**`AlgebraicGeometry.IsRadicial`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Radicial.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Radicial.lean#L63). The attribute's comment: “(2) radicial: injective on points, with every residue field extension `κ(x)/κ(f x)` purely inseparable”.

> A morphism of schemes `f : X ⟶ S` is *radicial* if it is injective on underlying
> topological spaces and, for every point `x` of `X`, the residue field extension
> `κ(x)/κ(f x)` given by `f.residueFieldMap x` is purely inseparable.

```lean
class IsRadicial : Prop
```

Declarations registered for the tag:

- [`AlgebraicGeometry.UniversallyInjective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.UniversallyInjective#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L146) (StacksFrontier): “(1) universally injective (Mathlib's definition)”. References: EGA I (3.5.4).

## Tag 01S4, a lemma

[Tag 01S4](https://stacks.math.columbia.edu/tag/01S4) in the Stacks Project.

**`AlgebraicGeometry.universallyInjective_of_subsingleton_of_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/UniversallyInjectiveSection.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/UniversallyInjectiveSection.lean#L61). The attribute's comment: “a morphism with a subsingleton source and a section is universally injective”.

> **A morphism of schemes whose source is a subsingleton and which admits a section is
> universally injective.**  This is condition (3) of **Stacks 01S4**: injectivity on points is the
> subsingleton hypothesis, and at a point `x` of the source the residue field map is an
> isomorphism because `x` coincides with the image under the section of its own image.

```lean
theorem universallyInjective_of_subsingleton_of_section {X Y : Scheme.{u}} [Subsingleton X]
    (f : X ⟶ Y) (s : Y ⟶ X) (hs : s ≫ f = 𝟙 Y) : UniversallyInjective f
```

## Tag 05VE, a lemma

[Tag 05VE](https://stacks.math.columbia.edu/tag/05VE) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.Hom.injective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Hom.injective#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L148) (StacksFrontier): “universally injective => injective”.
- [`AlgebraicGeometry.isSeparated_of_injective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.isSeparated_of_injective#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L149) (StacksFrontier): “injective on points => separated”. References: EGA I (5.5.1), “more general”; EGA IV (1.8.7.1), “more general”.

## Tag 0472, a lemma

[Tag 0472](https://stacks.math.columbia.edu/tag/0472) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.UniversallyInjective.isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.UniversallyInjective.isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 340](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L340) (StacksFrontier). References: SGA 3 VIB (10.1), “partial, sufficiency”; SGA 3 VIB (2.6), “more general”.

## Tag 02V1, a lemma

[Tag 02V1](https://stacks.math.columbia.edu/tag/02V1) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.universallyInjective_isStableUnderComposition`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.universallyInjective_isStableUnderComposition#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L183) (StacksFrontier): “composition of universally injective morphisms”. References: EGA I (3.5.6); EGA IV (6.15.3.1), “(i), special case”.
- [`AlgebraicGeometry.tfae_universallyInjective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.tfae_universallyInjective#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L185) (StacksFrontier): “radicial (condition (3)) is equivalent to universally injective”. References: EGA I (3.5.4); EGA I (3.5.8).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.10, Tag 01S2](https://stacks.math.columbia.edu/tag/01S2)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
