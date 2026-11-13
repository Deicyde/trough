---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsDominant, AlgebraicGeometry.isDominant_of_genericPoints_subset_range, AlgebraicGeometry.isDominant_iff_genericPoints_subset_range, AlgebraicGeometry.isDominant_pullback_snd_of_liftsGeneralizations, AlgebraicGeometry.isDominant_pullback_snd_of_isOpenMap, AlgebraicGeometry.exists_open_nhds_disjoint_range_of_quasiCompact, AlgebraicGeometry.isDominant_iff_genericPoint_mem_range, AlgebraicGeometry.finite_irreducibleComponents_of_isDominant
statement: formalized
proof: formalized
---

# 29.8 Dominant morphisms

Section 29.8 of the Stacks Project, [Tag 01RI](https://stacks.math.columbia.edu/tag/01RI). 8 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01RJ, a definition

[Tag 01RJ](https://stacks.math.columbia.edu/tag/01RJ) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.IsDominant`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsDominant#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L137) (StacksFrontier). References: EGA I (2.2.6).

## Tag 01RK, a lemma

[Tag 01RK](https://stacks.math.columbia.edu/tag/01RK) in the Stacks Project.

**`AlgebraicGeometry.isDominant_of_genericPoints_subset_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Dominant.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Dominant.lean#L51).

> A morphism of schemes whose image contains the generic point of every irreducible component
> of the target is dominant.

```lean
theorem isDominant_of_genericPoints_subset_range {X S : Scheme.{u}} (f : X ⟶ S)
    (h : genericPoints S ⊆ Set.range f) : IsDominant f
```

## Tag 01RL, a lemma

[Tag 01RL](https://stacks.math.columbia.edu/tag/01RL) in the Stacks Project.

**`AlgebraicGeometry.isDominant_iff_genericPoints_subset_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Dominant/GenericPoints.lean, line 234](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Dominant/GenericPoints.lean#L234). References: EGA IV (1.1.5), “a) <=> b)”; EGA I (6.6.5).

> **Stacks Project, Tag 01RL.** A quasi-compact morphism of schemes is dominant if and only if
> its image contains every generic point of an irreducible component of the target.

```lean
theorem isDominant_iff_genericPoints_subset_range {X S : Scheme.{u}} (f : X ⟶ S)
    [QuasiCompact f] :
    IsDominant f ↔ genericPoints S ⊆ Set.range f
```

## Tag 0H3F, a lemma

[Tag 0H3F](https://stacks.math.columbia.edu/tag/0H3F) in the Stacks Project.

**`AlgebraicGeometry.isDominant_pullback_snd_of_liftsGeneralizations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Dominant/BaseChange.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Dominant/BaseChange.lean#L77).

> **Stacks Project, Tag 0H3F.** A generizing base change of a quasi-compact dominant morphism
> of schemes is dominant.

```lean
public theorem isDominant_pullback_snd_of_liftsGeneralizations
    {X S S' : Scheme.{u}} (f : X ⟶ S) (g : S' ⟶ S) [QuasiCompact f] [IsDominant f]
    (hg : LiftsGeneralizations g) : IsDominant (pullback.snd f g)
```

## Tag 0H8F, a lemma

[Tag 0H8F](https://stacks.math.columbia.edu/tag/0H8F) in the Stacks Project.

**`AlgebraicGeometry.isDominant_pullback_snd_of_isOpenMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Dominant/BaseChange.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Dominant/BaseChange.lean#L50).

> **Stacks Project, Tag 0H8F.** The base change of a dominant morphism of schemes along an
> open morphism is dominant.

```lean
public theorem isDominant_pullback_snd_of_isOpenMap {X S S' : Scheme.{u}}
    (f : X ⟶ S) (g : S' ⟶ S) [IsDominant f] (hg : IsOpenMap g) :
    IsDominant (pullback.snd f g)
```

## Tag 02NE, a lemma

[Tag 02NE](https://stacks.math.columbia.edu/tag/02NE) in the Stacks Project.

**`AlgebraicGeometry.exists_open_nhds_disjoint_range_of_quasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Dominant/GenericPoints.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Dominant/GenericPoints.lean#L219). References: EGA IV (9.7.5.1), “more general”.

> **Stacks Project, Tag 02NE.** If a generic point of an irreducible
> component is not in the image of a quasi-compact morphism of schemes, it has
> an open neighbourhood with empty inverse image.

```lean
theorem exists_open_nhds_disjoint_range_of_quasiCompact
    {X S : Scheme.{u}} (f : X ⟶ S) [QuasiCompact f]
    (η : S) (hη : η ∈ genericPoints S) (hηf : η ∉ Set.range f) :
    ∃ V : S.Opens, η ∈ V ∧ f ⁻¹ᵁ V = ⊥
```

## Tag 01RM, a lemma

[Tag 01RM](https://stacks.math.columbia.edu/tag/01RM) in the Stacks Project.

**`AlgebraicGeometry.isDominant_iff_genericPoint_mem_range`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Dominant/GenericPoints.lean, line 282](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Dominant/GenericPoints.lean#L282). The attribute's comment: “dominant\_iff\_generic\_points\_in\_image”.

> **Stacks Project, Tag 01RM.** A morphism from a scheme with finitely many irreducible
> components is dominant if and only if its image contains the generic point of every irreducible
> component of the target.

```lean
lemma isDominant_iff_genericPoint_mem_range
    {X S : Scheme.{u}} (f : X ⟶ S)
    [Finite (irreducibleComponents X)] :
      IsDominant f ↔
      ∀ Z : irreducibleComponents S, Z.2.1.genericPoint ∈ Set.range f
```

**`AlgebraicGeometry.finite_irreducibleComponents_of_isDominant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Dominant/GenericPoints.lean, line 313](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Dominant/GenericPoints.lean#L313). The attribute's comment: “finite\_irreducible\_components\_target”.

> A dominant morphism of schemes with finitely many irreducible components in its source has
> finitely many irreducible components in its target.

```lean
theorem finite_irreducibleComponents_of_isDominant
    {X S : Scheme.{u}} (f : X ⟶ S) [IsDominant f]
    (hX : (irreducibleComponents X).Finite) :
    (irreducibleComponents S).Finite
```

## Tag 0CC1, a lemma

[Tag 0CC1](https://stacks.math.columbia.edu/tag/0CC1) in the Stacks Project.

**`AlgebraicGeometry.tfae_isDominant_of_isIntegral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Dominant/IntegralSchemes.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Dominant/IntegralSchemes.lean#L99).

> **Stacks Project, Tag 0CC1.** For a morphism `f : X ⟶ Y` of integral schemes, the
> following are equivalent: `f` is dominant; it maps the generic point of `X` to that of `Y`;
> the map on sections is injective for some, or for every, pair of nonempty affine opens
> `U ⊆ X`, `V ⊆ Y` with `f(U) ⊆ V`; and the map on local rings is injective at some, or at
> every, point of `X`.

```lean
public theorem tfae_isDominant_of_isIntegral
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsIntegral X] [IsIntegral Y] :
    List.TFAE [
      IsDominant f,
      f (genericPoint X) = genericPoint Y,
      ∃ (U : X.affineOpens) (V : Y.affineOpens)
        (_ : Nonempty U.1) (_ : Nonempty V.1)
        (hUV : U.1 ≤ f ⁻¹ᵁ V.1),
        Function.Injective (f.appLE V.1 U.1 hUV),
      ∀ (U : X.affineOpens) (V : Y.affineOpens)
        (_ : Nonempty U.1) (_ : Nonempty V.1)
        (hUV : U.1 ≤ f ⁻¹ᵁ V.1),
        Function.Injective (f.appLE V.1 U.1 hUV),
      ∃ x : X, Function.Injective (f.stalkMap x),
      ∀ x : X, Function.Injective (f.stalkMap x)]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.8, Tag 01RI](https://stacks.math.columbia.edu/tag/01RI)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
