---
declaration: section
origin: cited
lean: AlgebraicGeometry.instHasFiniteLimitsScheme, AlgebraicGeometry.specZIsTerminal, AlgebraicGeometry.Scheme.Pullback.instHasPullbacks, AlgebraicGeometry.Scheme.isPullback_toLRSHom, AlgebraicGeometry.LocallyRingedSpace.hasPullback_of_scheme
statement: formalized
proof: formalized
---

# 26.16 Existence of fibre products of schemes

Section 26.16 of the Stacks Project, [Tag 01JL](https://stacks.math.columbia.edu/tag/01JL). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01JM, a lemma

[Tag 01JM](https://stacks.math.columbia.edu/tag/01JM) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.instHasFiniteLimitsScheme`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.instHasFiniteLimitsScheme#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 331](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L331) (StacksFrontier): “finite limits”. References: EGA I (3.2.6), “more general”; EGA I (3.3.5), “more general”.
- [`AlgebraicGeometry.specZIsTerminal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.specZIsTerminal#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 332](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L332) (StacksFrontier): “the final object `Spec ℤ`”. References: EGA I (3.3.15).
- [`AlgebraicGeometry.Scheme.Pullback.instHasPullbacks`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Pullback.instHasPullbacks#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 333](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L333) (StacksFrontier): “fibre products”. References: EGA I (3.2.6); EGA I (3.3.5), “existence for n = 2”.

## Tag 01JN, a remark

[Tag 01JN](https://stacks.math.columbia.edu/tag/01JN) in the Stacks Project.

**`AlgebraicGeometry.Scheme.isPullback_toLRSHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/LocallyRingedSpaceFibreProduct.lean, line 477](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/LocallyRingedSpaceFibreProduct.lean#L477).

> The fibre product of two morphisms of schemes, formed in `Scheme`, is already the fibre
> product in locally ringed spaces. Neither leg of the cospan is assumed to be
> an open immersion.

```lean
theorem isPullback_toLRSHom {X Y S : Scheme.{u}} (f : X ⟶ S) (g : Y ⟶ S) :
    IsPullback (pullback.fst f g).toLRSHom (pullback.snd f g).toLRSHom f.toLRSHom g.toLRSHom
```

**`AlgebraicGeometry.LocallyRingedSpace.hasPullback_of_scheme`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/LocallyRingedSpaceFibreProduct.lean, line 518](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/LocallyRingedSpaceFibreProduct.lean#L518).

> The fibre product of two morphisms of schemes exists in the category of locally ringed
> spaces.

```lean
instance hasPullback_of_scheme {X Y S : Scheme.{u}} (f : X ⟶ S) (g : Y ⟶ S) :
    HasPullback f.toLRSHom g.toLRSHom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 26.16, Tag 01JL](https://stacks.math.columbia.edu/tag/01JL)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
