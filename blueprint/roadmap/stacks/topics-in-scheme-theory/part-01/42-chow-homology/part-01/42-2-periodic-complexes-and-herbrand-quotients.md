---
declaration: section
origin: cited
lean: CochainComplex, HomologicalComplex.homology, HomologicalComplex.ExactAt, HomologicalComplex.Acyclic, AlgebraicGeometry.twoPeriodicComplex, AlgebraicGeometry.periodicLength, AlgebraicGeometry.periodicLength_zero_eq_length_quotient_sub_length_ker, AlgebraicGeometry.finiteLengthHomology_X3_of_shortExact
statement: formalized
proof: formalized
---

# 42.2 Periodic complexes and Herbrand quotients

Section 42.2 of the Stacks Project, [Tag 02PF](https://stacks.math.columbia.edu/tag/02PF). 6 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02PG, a definition

[Tag 02PG](https://stacks.math.columbia.edu/tag/02PG) in the Stacks Project.

Declarations registered for the tag:

- [`CochainComplex`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesHerbrand/Length.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesHerbrand/Length.lean#L206) (StacksFrontier): “part (1): 2-periodic complexes”. References: EGA 0 (11.2.1); EGA 0 (13.2.3); EGA III (6.2.1); SGA 2 VIII (1.2); SGA 4 XVII (2.2.7), “special case”; SGA 4 XVII (5.5.3); SGA 4½ Etat 0 (1.2.1); SGA 6 I (1.1.5).
- [`HomologicalComplex.homology`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex.homology#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesHerbrand/Length.lean, line 215](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesHerbrand/Length.lean#L215) (StacksFrontier): “part (1): cohomology modules”. References: EGA 0 (11.2.1); EGA 0 (11.3.1), “more general”; EGA 0 (11.3.5); EGA III (7.6.11).
- [`HomologicalComplex.ExactAt`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex.ExactAt#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesHerbrand/Length.lean, line 220](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesHerbrand/Length.lean#L220) (StacksFrontier): “part (1): vanishing of cohomology in a degree”.
- [`HomologicalComplex.Acyclic`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomologicalComplex.Acyclic#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesHerbrand/Length.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesHerbrand/Length.lean#L221) (StacksFrontier): “part (1): exactness”. References: SGA 4½ Etat 0 (1.2.3), “more general”.
- [`AlgebraicGeometry.twoPeriodicComplex`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/CalculationMultiplicities/TwoPeriodic.lean#L75), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesHerbrand/Length.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesHerbrand/Length.lean#L222) (StacksFrontier): “part (2): (2, 1)-periodic complexes”.

## Tag 02PH, a definition

[Tag 02PH](https://stacks.math.columbia.edu/tag/02PH) in the Stacks Project.

**`AlgebraicGeometry.periodicLength`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesHerbrand/Defs.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesHerbrand/Defs.lean#L41).

> The multiplicity (or periodic length) of a two-periodic complex of modules. For a complex
> whose two objects agree, this is also known as its additive Herbrand quotient.

```lean
public noncomputable abbrev periodicLength {R : Type u} [Ring R]
    (C : CochainComplex (ModuleCat.{v} R) (ZMod 2)) : ℤ
```

## Tag 0EA6, an equation

[Tag 0EA6](https://stacks.math.columbia.edu/tag/0EA6) in the Stacks Project.

**`AlgebraicGeometry.periodicLength_zero_eq_length_quotient_sub_length_ker`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesHerbrand/Length.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesHerbrand/Length.lean#L191).

> The additive Herbrand quotient of a `(2, 1)`-periodic complex whose first map is zero is the
> length of the cokernel of its second map minus the length of the kernel of that map.

```lean
public lemma periodicLength_zero_eq_length_quotient_sub_length_ker {R : Type u} [Ring R]
    {M : Type v} [AddCommGroup M] [Module R M] (ψ : Module.End R M) :
    periodicLength (twoPeriodicComplex (0 : Module.End R M) ψ (zero_mul ψ) (mul_zero ψ)) =
      ((Module.length R (M ⧸ LinearMap.range ψ)).toNat : ℤ) -
        ((Module.length R (LinearMap.ker ψ)).toNat : ℤ)
```

## Tag 0EA7, a lemma

[Tag 0EA7](https://stacks.math.columbia.edu/tag/0EA7) in the Stacks Project.

**`AlgebraicGeometry.finiteLengthHomology_X3_of_shortExact`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesHerbrand/Additivity.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesHerbrand/Additivity.lean#L146). The attribute's comment: “two-out-of-three, third term”.

> In a short exact sequence of two-periodic complexes, finite-length cohomology of the first
> two terms implies finite-length cohomology of the third.

```lean
public lemma finiteLengthHomology_X3_of_shortExact {R : Type u} [Ring R]
    (S : ShortComplex (HomologicalComplex (ModuleCat.{v} R) (ComplexShape.up (ZMod 2))))
    (hS : S.ShortExact) (h₁ : HasFiniteLengthHomology S.X₁)
    (h₂ : HasFiniteLengthHomology S.X₂) : HasFiniteLengthHomology S.X₃
```

**`AlgebraicGeometry.finiteLengthHomology_X2_of_shortExact`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesHerbrand/Additivity.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesHerbrand/Additivity.lean#L157). The attribute's comment: “two-out-of-three, middle term”.

> In a short exact sequence of two-periodic complexes, finite-length cohomology of the outer
> terms implies finite-length cohomology of the middle term.

```lean
public lemma finiteLengthHomology_X2_of_shortExact {R : Type u} [Ring R]
    (S : ShortComplex (HomologicalComplex (ModuleCat.{v} R) (ComplexShape.up (ZMod 2))))
    (hS : S.ShortExact) (h₁ : HasFiniteLengthHomology S.X₁)
    (h₃ : HasFiniteLengthHomology S.X₃) : HasFiniteLengthHomology S.X₂
```

**`AlgebraicGeometry.finiteLengthHomology_X1_of_shortExact`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesHerbrand/Additivity.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesHerbrand/Additivity.lean#L167). The attribute's comment: “two-out-of-three, first term”.

> In a short exact sequence of two-periodic complexes, finite-length cohomology of the last
> two terms implies finite-length cohomology of the first.

```lean
public lemma finiteLengthHomology_X1_of_shortExact {R : Type u} [Ring R]
    (S : ShortComplex (HomologicalComplex (ModuleCat.{v} R) (ComplexShape.up (ZMod 2))))
    (hS : S.ShortExact) (h₂ : HasFiniteLengthHomology S.X₂)
    (h₃ : HasFiniteLengthHomology S.X₃) : HasFiniteLengthHomology S.X₁
```

**`AlgebraicGeometry.periodicLength_additive_of_shortExact`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesHerbrand/Additivity.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesHerbrand/Additivity.lean#L178). The attribute's comment: “additivity”.

> Periodic length is additive on a short exact sequence of two-periodic complexes as soon as
> the cohomology of any two of its terms has finite length.

```lean
public lemma periodicLength_additive_of_shortExact {R : Type u} [Ring R]
    (S : ShortComplex (HomologicalComplex (ModuleCat.{v} R) (ComplexShape.up (ZMod 2))))
    (hS : S.ShortExact)
    (hfin : (HasFiniteLengthHomology S.X₁ ∧ HasFiniteLengthHomology S.X₂) ∨
      (HasFiniteLengthHomology S.X₁ ∧ HasFiniteLengthHomology S.X₃) ∨
      (HasFiniteLengthHomology S.X₂ ∧ HasFiniteLengthHomology S.X₃)) :
    periodicLength S.X₂ = periodicLength S.X₁ + periodicLength S.X₃
```

## Tag 0EA8, a lemma

[Tag 0EA8](https://stacks.math.columbia.edu/tag/0EA8) in the Stacks Project.

**`AlgebraicGeometry.periodicLength_eq_length_sub_length`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesHerbrand/Length.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesHerbrand/Length.lean#L112). The attribute's comment: “the length formula”.

> The multiplicity of a two-periodic complex of finite-length modules is the difference of
> the lengths of its two terms.

```lean
public lemma periodicLength_eq_length_sub_length {R : Type u} [Ring R]
    (C : HomologicalComplex (ModuleCat.{v} R) (ComplexShape.up (ZMod 2)))
    (h₀ : IsFiniteLength R (C.X (0 : ZMod 2)))
    (h₁ : IsFiniteLength R (C.X (1 : ZMod 2))) :
    periodicLength C =
      ((Module.length R (C.X (0 : ZMod 2))).toNat : ℤ) -
        ((Module.length R (C.X (1 : ZMod 2))).toNat : ℤ)
```

**`AlgebraicGeometry.periodicLength_eq_zero_of_iso`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesHerbrand/Length.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesHerbrand/Length.lean#L147). The attribute's comment: “the (2, 1)-periodic case”.

> The multiplicity of a finite-length two-periodic complex with isomorphic terms vanishes.

```lean
public lemma periodicLength_eq_zero_of_iso {R : Type u} [Ring R]
    (C : HomologicalComplex (ModuleCat.{v} R) (ComplexShape.up (ZMod 2)))
    (hfin : IsFiniteLength R (C.X (0 : ZMod 2)))
    (e : C.X (0 : ZMod 2) ≅ C.X (1 : ZMod 2)) :
    periodicLength C = 0
```

## Tag 0EA9, a lemma

[Tag 0EA9](https://stacks.math.columbia.edu/tag/0EA9) in the Stacks Project.

**`AlgebraicGeometry.periodicLength_eq_of_finite_length_kernel_cokernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesHerbrand/Comparison.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesHerbrand/Comparison.lean#L62).

> A morphism between `(2, 1)`-periodic complexes with finite-length kernel and cokernel
> preserves their periodic length when the cohomology modules of both complexes have finite
> length.

```lean
public theorem periodicLength_eq_of_finite_length_kernel_cokernel
    {R : Type u} [Ring R]
    {C D : HomologicalComplex (ModuleCat.{v} R) (ComplexShape.up (ZMod 2))}
    (f : C ⟶ D)
    (hC : ∀ i, IsFiniteLength R (C.homology i))
    (hD : ∀ i, IsFiniteLength R (D.homology i))
    (hker : IsFiniteLength R ((kernel f).X (0 : ZMod 2)))
    (hcoker : IsFiniteLength R ((cokernel f).X (0 : ZMod 2)))
    (eker : (kernel f).X (0 : ZMod 2) ≅ (kernel f).X (1 : ZMod 2))
    (ecoker : (cokernel f).X (0 : ZMod 2) ≅ (cokernel f).X (1 : ZMod 2)) :
    periodicLength C = periodicLength D
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.2, Tag 02PF](https://stacks.math.columbia.edu/tag/02PF)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
