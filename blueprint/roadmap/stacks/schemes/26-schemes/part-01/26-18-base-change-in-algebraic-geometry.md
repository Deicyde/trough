---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.Over, AlgebraicGeometry.Scheme.Hom.IsOver, AlgebraicGeometry.Scheme.Hom.isOver_iff, AlgebraicGeometry.Scheme.asOver, AlgebraicGeometry.Scheme.canonicallyOverPullback, CategoryTheory.Over.pullback, AlgebraicGeometry.IsImmersion.isStableUnderBaseChange, AlgebraicGeometry.IsClosedImmersion.isStableUnderBaseChange
statement: formalized
proof: formalized
---

# 26.18 Base change in algebraic geometry

Section 26.18 of the Stacks Project, [Tag 01JW](https://stacks.math.columbia.edu/tag/01JW). 5 tags here are carried by 3 declarations of the repository (all in StacksFrontier) and 15 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01JX, a definition

[Tag 01JX](https://stacks.math.columbia.edu/tag/01JX) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.Over`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Over#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L194) (StacksFrontier): “(1) a scheme over S; (2) is the case S = Spec R”. References: EGA I (2.5.1); EGA II (8.3.1), “partial”; SGA 3 VIB (2.0); SGA 5 III (3.2), “more general”.
- [`AlgebraicGeometry.Scheme.Hom.IsOver`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Hom.IsOver#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L196) (StacksFrontier): “(3) a morphism of schemes over S”. References: EGA I (2.5.2); EGA I (2.5.5); EGA I (3.3.14); EGA IV (14.5.8).
- [`AlgebraicGeometry.Scheme.Hom.isOver_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Hom.isOver_iff#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L197) (StacksFrontier): “(3) the defining condition of a morphism over S”. References: EGA I (2.5.2); EGA I (2.5.5), “more general”; EGA I (3.3.14), “more general”.
- [`AlgebraicGeometry.Scheme.asOver`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.asOver#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L199) (StacksFrontier): “(4) Mor\_S(X, Y) as the hom-set from X.asOver S to Y.asOver S in Over S”. References: SGA 5 III (3.2), “more general”.
- [`AlgebraicGeometry.Scheme.canonicallyOverPullback`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.canonicallyOverPullback#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L201) (StacksFrontier): “(5) the base change of X as a scheme over S'; (7) is the affine case”. References: EGA I (3.3.6).
- [`CategoryTheory.Over.pullback`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.pullback#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L203) (StacksFrontier): “(5) and (6) base change of schemes and morphisms over S, as a functor”. References: EGA I (3.3.7), “more general”; EGA IV (8.2.6); SGA 3 I (1.6); SGA 4 III (5.5); SGA 4 IV (5.2), “more general”; SGA 4 IV (5.5).

## Tag 01JY, a lemma

[Tag 01JY](https://stacks.math.columbia.edu/tag/01JY) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.IsImmersion.isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsImmersion.isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/ImmersionBaseChange.lean, line 26](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/ImmersionBaseChange.lean#L26) (StacksFrontier): “immersion”. References: EGA I (4.3.1), “special case”; EGA I (4.3.2); EGA I (4.5.5), “(iii), special case”; EGA II (3.8.1), “Immersion clause”; EGA IV (17.13.1); SGA 3 VIB (10.1), “partial”.
- [`AlgebraicGeometry.IsClosedImmersion.isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsClosedImmersion.isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/ImmersionBaseChange.lean, line 33](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/ImmersionBaseChange.lean#L33) (StacksFrontier): “closed immersion”. References: EGA I (10.14.5), “(ii), ordinary schemes”; EGA I (4.3.1), “special case”; EGA I (4.3.2); EGA I (4.5.5), “(iii), special case”; EGA II (8.10.2), “j′ is a closed immersion”; EGA IV (17.13.1), “closed immersions”; EGA IV (2.7.1), “implication”; EGA IV (8.6.2), “more general”; SGA 1 VIII (5.5), “closed-immersion clause”; SGA 3 VIB (10.1), “partial”; SGA 4 XII (4.3), “Parenthetical clause”.
- [`AlgebraicGeometry.isOpenImmersion_stableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.isOpenImmersion_stableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/ImmersionBaseChange.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/ImmersionBaseChange.lean#L52) (StacksFrontier): “open immersion”. References: EGA I (4.3.1), “special case”; EGA I (4.3.2); EGA I (4.5.5), “(iii), special case”; EGA IV (11.9.5), “Geometric clause”; EGA IV (2.7.1), “(x)”; SGA 1 VIII (5.5), “open-immersion clause”; SGA 3 VIB (10.1), “open immersions”; SGA 6 VIII (1.6), “partial”.

## Tag 01JZ, a definition

[Tag 01JZ](https://stacks.math.columbia.edu/tag/01JZ) in the Stacks Project.

**`CategoryTheory.IsStableUnderBaseChange`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/BaseChange/Stability.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/BaseChange/Stability.lean#L62). The attribute's comment: “part (1): properties of objects over a base”.

> A family of properties of objects over a base is stable under base change if
> the property passes across every pullback square.

```lean
public class IsStableUnderBaseChange
    (P : (S : C) → ObjectProperty (Over S)) : Prop
```

**`CategoryTheory.MorphismPropertyOverBase.IsStableUnderBaseChange`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/BaseChange/Stability.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/BaseChange/Stability.lean#L85). The attribute's comment: “part (2): properties of morphisms over a base”. References: EGA I (3.5.1), “more general”; EGA I (5.5.12); SGA 3 VIB (2.0), “stable under base change”; SGA 3 IV (4.7), “more general”; SGA 3 VIB (10.1).

> A family of properties of morphisms over a base is stable under arbitrary
> base change if it passes across every pair of pullback squares defining the
> base change of a morphism.

```lean
public class IsStableUnderBaseChange : Prop
```

Declarations registered for the tag:

- [`CategoryTheory.MorphismProperty.IsStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.MorphismProperty.IsStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/BaseChange/Stability.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/BaseChange/Stability.lean#L169) (StacksFrontier): “part (2), base-independent properties”. References: EGA I (3.5.1); EGA I (5.5.12); SGA 3 IV (3.4.1), “(a)”; SGA 3 IV (4.6.3); SGA 3 IV (4.7); SGA 3 VIB (10.1); SGA 3 VIB (2.0); SGA 3 XXIV (7.1.9); SGA 4 IV (8.5.4); SGA 4 IV (9.1.7), “ST1”; SGA 4 VII (5.4); SGA 4 Vbis (3.3).

## Tag 01K0, a definition

[Tag 01K0](https://stacks.math.columbia.edu/tag/01K0) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.Hom.fiber`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Hom.fiber#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L205) (StacksFrontier): “the scheme theoretic fibre”. References: EGA I (3.6.2); EGA II (1.5.3); EGA II (6.1.7); EGA III (4.6.2); EGA III (4.6.7), “partial”; EGA III (6.9.10); EGA IV (6.15.3); EGA IV (8.11.5.1); EGA IV (9.4.1); EGA IV (11.2.8); EGA IV (15.4.1); EGA IV (1.8.7); SGA 1 II (2.4); SGA 6 III (4.6), “partial”; SGA 6 III (4.6.1); SGA 7 XVIII (5.1).
- [`AlgebraicGeometry.Scheme.Hom.fiberToSpecResidueField`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Hom.fiberToSpecResidueField#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L206) (StacksFrontier): “the projection from the fibre to Spec κ(s)”. References: EGA I (3.6.2); EGA II (1.5.3); EGA II (6.1.7); EGA III (4.6.2); EGA IV (6.15.3); EGA IV (8.11.5.1); EGA IV (11.2.8); EGA IV (17.8.2), “special case”; SGA 7 XVIII (5.1).
- [`AlgebraicGeometry.Scheme.Hom.fiberOverSpecResidueField`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Hom.fiberOverSpecResidueField#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L208) (StacksFrontier): “the fibre as a scheme over κ(s)”. References: EGA I (3.6.2); EGA I (3.7.2), “more general”; EGA II (1.5.3); EGA II (6.1.7); EGA III (4.2.1), “special case”; EGA IV (6.15.3); EGA IV (8.11.5.1); EGA IV (11.2.8); EGA IV (17.7.11), “partial”; SGA 1 IX (6.1); SGA 3 XXVI (7.15); SGA 7 VIII (7.0).

## Tag 01K1, a lemma

[Tag 01K1](https://stacks.math.columbia.edu/tag/01K1) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isEmbedding_fiberι_and_pullbackSnd_fromSpecStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/EmbeddingOverPoint.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/EmbeddingOverPoint.lean#L43).

> Let `f : X ⟶ S` be a morphism of schemes and `s ∈ S`. Both the inclusion of the fibre
> `X_s = X ×_S Spec κ(s) ⟶ X` and the projection `Spec 𝒪_{S,s} ×_S X ⟶ X` are homeomorphisms onto
> their images.

```lean
theorem isEmbedding_fiberι_and_pullbackSnd_fromSpecStalk {X S : Scheme.{u}} (f : X ⟶ S)
    (s : S) :
    IsEmbedding (f.fiberι s) ∧ IsEmbedding (pullback.snd (S.fromSpecStalk s) f)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.instIsPreimmersionFiberι`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.instIsPreimmersionFiberι#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L210) (StacksFrontier): “first diagram: X\_s → X is a preimmersion, so an embedding”. References: SGA 7 XVIII (5.1), “k is a preimmersion”.
- [`AlgebraicGeometry.Scheme.Hom.fiberHomeo`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Hom.fiberHomeo#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L212) (StacksFrontier): “first diagram: X\_s is homeomorphic to its image, the set-theoretic fibre”. References: EGA I (3.5.10), “special case”; EGA I (3.6.1), “special case”; EGA I (3.6.2); EGA II (1.5.3), “partial”; EGA III (4.6.2), “partial”; EGA IV (9.4.1); EGA IV (11.2.8); EGA IV (15.4.1); EGA IV (1.8.7), “partial”; SGA 7 XVIII (5.1), “partial”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 26.18, Tag 01JW](https://stacks.math.columbia.edu/tag/01JW)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
