---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_finitePresentation_isImmersion, AlgebraicGeometry.exists_finitePresentation_closedImmersion, AlgebraicGeometry.exists_isLimit_closedImmersion_finitePresentation, AlgebraicGeometry.isLimit_finitePresentationCone_of_qcqs, AlgebraicGeometry.exists_isLimit_finitePresentation_closedImmersion, AlgebraicGeometry.exists_isLimit_finitePresentation_isClosedImmersion, AlgebraicGeometry.exists_isClosedImmersion_into_isSeparated_finitePresentation, AlgebraicGeometry.exists_isFinite_finitePresentation_closedImmersion
statement: formalized
proof: formalized
---

# 32.9 Finite type closed in finite presentation

Section 32.9 of the Stacks Project, [Tag 01ZD](https://stacks.math.columbia.edu/tag/01ZD). 7 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01ZE, a lemma

[Tag 01ZE](https://stacks.math.columbia.edu/tag/01ZE) in the Stacks Project.

**`AlgebraicGeometry.exists_finitePresentation_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Finiteness/ImmersionIntoFinitePresentation.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Finiteness/ImmersionIntoFinitePresentation.lean#L221).

> **Stacks Project, Tag 01ZE.**  A quasi-compact, quasi-separated scheme locally of finite
> type over `S` immerses over `S` into a scheme of finite presentation over `S`.

```lean
theorem exists_finitePresentation_isImmersion {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [CompactSpace X] [QuasiSeparatedSpace X] :
    ∃ (X' : Scheme.{u}) (f' : X' ⟶ S) (i : X ⟶ X'),
      FinitePresentation f' ∧ IsImmersion i ∧ i ≫ f' = f
```

## Tag 01ZG, a lemma

[Tag 01ZG](https://stacks.math.columbia.edu/tag/01ZG) in the Stacks Project.

**`AlgebraicGeometry.exists_finitePresentation_closedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Finiteness/ClosedImmersionIntoFinitePresentation.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Finiteness/ClosedImmersionIntoFinitePresentation.lean#L57).

> **Stacks Project, Tag 01ZG.**  A morphism locally of finite type from a quasi-compact,
> quasi-separated scheme to a quasi-separated scheme factors as a closed immersion into a scheme
> of finite presentation over the target.

```lean
theorem exists_finitePresentation_closedImmersion {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [CompactSpace X] [QuasiSeparatedSpace X] [QuasiSeparatedSpace S] :
    ∃ (X' : Scheme.{u}) (p : X' ⟶ S) (i : X ⟶ X'),
      FinitePresentation p ∧ IsClosedImmersion i ∧ i ≫ p = f
```

## Tag 09ZP, a lemma

[Tag 09ZP](https://stacks.math.columbia.edu/tag/09ZP) in the Stacks Project.

**`AlgebraicGeometry.exists_isLimit_closedImmersion_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Finiteness/ClosedImmersionLimit.lean, line 281](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Finiteness/ClosedImmersionLimit.lean#L281).

> A closed immersion into a quasi-compact and quasi-separated scheme `Y` is a directed inverse
> limit, over `Y`, of closed immersions of finite presentation into `Y`.
>
> The system is the system of closed subschemes of `Y` cut out by the ideal sheaf data below
> `f.ker` whose closed immersion is of finite presentation.  Those are directed and have supremum
> `f.ker` ([Stacks, Tag 01PG] for ideal sheaf data), and a cone of closed subschemes whose ideal
> sheaves have supremum `f.ker` has `X` as its limit.

```lean
theorem exists_isLimit_closedImmersion_finitePresentation {X Y : Scheme.{u}} (f : X ⟶ Y)
    [IsClosedImmersion f] [CompactSpace Y] [QuasiSeparatedSpace Y] :
    ∃ (I : Type u) (_ : Preorder I) (_ : Nonempty I) (_ : IsDirected I (· ≤ ·))
      (D : Functor Iᵒᵖ Scheme.{u}) (t : D ⟶ (Functor.const Iᵒᵖ).obj Y)
      (p : (Functor.const Iᵒᵖ).obj X ⟶ D) (_ : IsLimit (Cone.mk X p)),
      p ≫ t = (Functor.const Iᵒᵖ).map f ∧
        ∀ i, IsClosedImmersion (t.app i) ∧ FinitePresentation (t.app i)
```

**`AlgebraicGeometry.isLimit_finitePresentationCone_of_qcqs`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/IdealSheafFiniteType/Basic.lean, line 493](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/IdealSheafFiniteType/Basic.lean#L493).

> **Limits, Tag 09ZP.** The source of a closed immersion into a quasi-compact and
> quasi-separated scheme `Y` is the limit, in `Over Y`, of the inverse system of
> finite-presentation closed subschemes of `Y` containing it.
>
> The index of that system is `Stacks.Flatness.FinitePresentationSubscheme f.ker`, whose every
> member is by definition a closed subscheme of `Y` of finite presentation, so the tag's
> assertion about the stages is carried by the statement itself; the directedness of the system
> is the unconditional
> `AlgebraicGeometry.isCofiltered_finitePresentationSubscheme_op`, which is the other half of the
> covering set and is left untagged where it stands.

```lean
def isLimit_finitePresentationCone_of_qcqs {X : Scheme.{u}} [CompactSpace Y]
    [QuasiSeparatedSpace Y] (f : X ⟶ Y) [IsClosedImmersion f] :
    IsLimit (finitePresentationCone f (le_refl f.ker))
```

## Tag 09ZQ, a lemma

[Tag 09ZQ](https://stacks.math.columbia.edu/tag/09ZQ) in the Stacks Project.

**`AlgebraicGeometry.exists_isLimit_finitePresentation_closedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Finiteness/FiniteLimitPresentation.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Finiteness/FiniteLimitPresentation.lean#L104).

> A quasi-compact and quasi-separated scheme locally of finite type over a quasi-separated
> base is a directed inverse limit of quasi-compact and quasi-separated schemes of finite
> presentation over that base, with closed immersions as the transition maps and as the limit
> projections.

```lean
theorem exists_isLimit_finitePresentation_closedImmersion {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [CompactSpace X] [QuasiSeparatedSpace X] [QuasiSeparatedSpace S] :
    ∃ (I : Type u) (_ : Preorder I) (_ : Nonempty I) (_ : IsDirected I (· ≤ ·))
      (D : Functor Iᵒᵖ Scheme.{u}) (t : D ⟶ (Functor.const Iᵒᵖ).obj S)
      (p : (Functor.const Iᵒᵖ).obj X ⟶ D) (_ : IsLimit (Cone.mk X p)),
      p ≫ t = (Functor.const Iᵒᵖ).map f ∧
        (∀ i, FinitePresentation (t.app i) ∧
          CompactSpace (D.obj i) ∧ QuasiSeparatedSpace (D.obj i)) ∧
        (∀ {i j : Iᵒᵖ} (g : i ⟶ j), IsClosedImmersion (D.map g)) ∧
        ∀ i, IsClosedImmersion (p.app i)
```

**`AlgebraicGeometry.exists_isLimit_finitePresentation_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FiniteTypeLimitFinitePresentation/Basic.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FiniteTypeLimitFinitePresentation/Basic.lean#L204).

> **Stacks, Tag 09ZQ.** A morphism `f : X ⟶ S` locally of finite type, with `X` quasi-compact
> and quasi-separated and `S` quasi-separated, presents `X` as the limit of a directed inverse
> system of quasi-compact quasi-separated schemes of finite presentation over `S` whose transition
> morphisms, and whose projections from `X`, are closed immersions.
>
> [Stacks, Tag 01ZE] immerses `X` over `S` into a scheme of finite presentation over `S`, and
> `AlgebraicGeometry.exists_qcqs_finitePresentation_isClosedImmersion_of_exists_immersion` converts
> that immersion into a closed immersion `j : X ⟶ Y` with `Y` quasi-compact, quasi-separated and of
> finite presentation over `S`. [Stacks, Tag 09ZP] then writes `X` as the directed inverse limit
> over `Y` of those closed subschemes of `Y` containing `X` whose closed immersion into `Y` is of
> finite presentation. Composing the structure morphisms of that system with `Y ⟶ S` leaves them of
> finite presentation; every stage, being a closed subscheme of `Y`, inherits quasi-compactness and
> quasi-separatedness from `Y`; and both the transition morphisms and the projections from `X` are
> closed immersions because their composites with the closed immersions into `Y` are.

```lean
theorem exists_isLimit_finitePresentation_isClosedImmersion (f : X ⟶ S) [LocallyOfFiniteType f]
    [CompactSpace X] [QuasiSeparatedSpace X] [QuasiSeparatedSpace S] :
    ∃ (I : Type u) (_ : Preorder I) (_ : Nonempty I) (_ : IsDirected I (· ≤ ·))
      (D : Iᵒᵖ ⥤ Scheme.{u}) (t : D ⟶ (Functor.const Iᵒᵖ).obj S)
      (p : (Functor.const Iᵒᵖ).obj X ⟶ D) (_ : IsLimit (Cone.mk X p)),
      p ≫ t = (Functor.const Iᵒᵖ).map f ∧
        (∀ i, FinitePresentation (t.app i) ∧ CompactSpace (D.obj i) ∧
          QuasiSeparatedSpace (D.obj i)) ∧
        (∀ (i i' : Iᵒᵖ) (g : i ⟶ i'), IsClosedImmersion (D.map g)) ∧
        ∀ i, IsClosedImmersion (p.app i)
```

## Tag 01ZJ, a proposition

[Tag 01ZJ](https://stacks.math.columbia.edu/tag/01ZJ) in the Stacks Project.

**`AlgebraicGeometry.exists_isClosedImmersion_into_isSeparated_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/SeparatedFinitePresentationEmbedding.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/SeparatedFinitePresentationEmbedding.lean#L51).

> A separated morphism of finite type onto a quasi-compact, quasi-separated scheme factors as
> a closed immersion followed by a separated morphism of finite presentation.

```lean
theorem exists_isClosedImmersion_into_isSeparated_finitePresentation
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f] [QuasiCompact f] [IsSeparated f]
    [CompactSpace S] [QuasiSeparatedSpace S] :
    ∃ (X' : Scheme.{u}) (f' : X' ⟶ S) (i : X ⟶ X'),
      IsSeparated f' ∧ FinitePresentation f' ∧ IsClosedImmersion i ∧ i ≫ f' = f
```

## Tag 01ZK, a lemma

[Tag 01ZK](https://stacks.math.columbia.edu/tag/01ZK) in the Stacks Project.

**`AlgebraicGeometry.exists_isFinite_finitePresentation_closedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Finiteness/FiniteIntoFinitePresentation.lean, line 37](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Finiteness/FiniteIntoFinitePresentation.lean#L37).

> A finite morphism `f : X ⟶ S` of schemes whose target is
> quasi-compact and quasi-separated factors as a closed immersion `X ⟶ X'` followed by a morphism
> `X' ⟶ S` which is finite and of finite presentation.

```lean
theorem exists_isFinite_finitePresentation_closedImmersion {X S : Scheme.{u}} (f : X ⟶ S)
    [IsFinite f] [CompactSpace S] [QuasiSeparatedSpace S] :
    ∃ (X' : Scheme.{u}) (f' : X' ⟶ S) (i : X ⟶ X'),
      IsFinite f' ∧ FinitePresentation f' ∧ IsClosedImmersion i ∧ i ≫ f' = f
```

## Tag 09YY, a lemma

[Tag 09YY](https://stacks.math.columbia.edu/tag/09YY) in the Stacks Project.

**`Stacks.FiniteAlgebraLimitPresentation.finiteLimitPresentationOfIsFinite`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FiniteAlgebraLimitPresentation/Basic.lean, line 560](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FiniteAlgebraLimitPresentation/Basic.lean#L560).

> **[Stacks, Tag 09YY].** A finite morphism over a quasi-compact and quasi-separated base is
> the inverse limit of a directed system of morphisms to that base which are finite and of finite
> presentation, with closed immersions as transition maps.
>
> [Stacks, Tag 09ZQ] supplies such a system of morphisms of finite presentation, finiteness of
> the stages failing only below some index; [Stacks, Tag 09ZN] produces that index, and the
> cofinal tail above it is an initial subcategory, so the restricted system has the same
> limit.

```lean
noncomputable def finiteLimitPresentationOfIsFinite {X S : Scheme.{u}} (f : X ⟶ S) [IsFinite f]
    [CompactSpace S] [QuasiSeparatedSpace S] : FiniteLimitPresentation f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 32.9, Tag 01ZD](https://stacks.math.columbia.edu/tag/01ZD)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
