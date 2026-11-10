---
declaration: section
origin: cited
lean: AlgebraicGeometry.CompleteDevissage, AlgebraicGeometry.CompleteDevissageAt, AlgebraicGeometry.exists_completeDevissage_baseChange, AlgebraicGeometry.CompleteDevissageAt.exists_isBaseChange, AlgebraicGeometry.NonemptyCompleteDevissageAt.StandardShrinking, AlgebraicGeometry.exists_standardShrinking_finalTarget, AlgebraicGeometry.NonemptyCompleteDevissageAt.exists_standardShrinking_base, AlgebraicGeometry.NonemptyCompleteDevissageAt.exists_standardShrinking_source
statement: formalized
proof: formalized
---

# 38.5 Complete dévissage

Section 38.5 of the Stacks Project, [Tag 05HG](https://stacks.math.columbia.edu/tag/05HG). 8 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05HH, a definition

[Tag 05HH](https://stacks.math.columbia.edu/tag/05HH) in the Stacks Project.

**`AlgebraicGeometry.CompleteDevissage`**, an inductive in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/Complete.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/Complete.lean#L151).

> A complete dévissage of `F/X/S` over `s`: either the empty dévissage, which exists
> precisely for the zero module, or a finite nonempty chain of stages.

```lean
inductive CompleteDevissage {X S : Scheme.{u}} (f : X ⟶ S) (F : X.Modules) (s : S)
    [hl : LocallyOfFiniteType f] [hq : F.IsQuasicoherent] [ht : F.IsFiniteType]
```

## Tag 05HI, a definition

[Tag 05HI](https://stacks.math.columbia.edu/tag/05HI) in the Stacks Project.

**`AlgebraicGeometry.CompleteDevissageAt`**, an inductive in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/Complete.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/Complete.lean#L212).

> A complete dévissage of `F/X/S` at `x`: either the empty dévissage, which exists precisely
> for the zero module, or a nonempty chain of stages with compatible distinguished points.

```lean
inductive CompleteDevissageAt {X S : Scheme.{u}} (f : X ⟶ S) (F : X.Modules) (x : X)
    [hl : LocallyOfFiniteType f] [hq : F.IsQuasicoherent] [ht : F.IsFiniteType]
```

## Tag 05HJ, a lemma

[Tag 05HJ](https://stacks.math.columbia.edu/tag/05HJ) in the Stacks Project.

**`AlgebraicGeometry.exists_completeDevissage_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/Complete/BaseChange.lean, line 410](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/Complete/BaseChange.lean#L410).

> **Stacks 05HJ.** A complete dévissage of `F/X/S` over `s` base-changes, stage by stage, to
> a complete dévissage of the base-changed module over `s'`, for any cartesian square whose
> new base is affine.

```lean
theorem exists_completeDevissage_baseChange {X X' : Scheme.{u}} {f : X ⟶ S} {f' : X' ⟶ S'}
    {F : X.Modules} {F' : X'.Modules} (hs : h s' = s) [IsAffine S'] [LocallyOfFiniteType f]
    [F.IsQuasicoherent] [F.IsFiniteType] [LocallyOfFiniteType f'] [F'.IsQuasicoherent]
    [F'.IsFiniteType] (D : NonemptyCompleteDevissage f F s) (pX : X' ⟶ X)
    (hX : IsPullback pX f' f h) (eF : (Scheme.Modules.pullback pX).obj F ≅ F') :
    ∃ D' : NonemptyCompleteDevissage f' F' s', ChainIsBaseChange h pX D.chain D'.chain
```

## Tag 05HK, a lemma

[Tag 05HK](https://stacks.math.columbia.edu/tag/05HK) in the Stacks Project.

**`AlgebraicGeometry.CompleteDevissageAt.exists_isBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/Complete/BaseChangeAt.lean, line 349](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/Complete/BaseChangeAt.lean#L349).

> **Stacks 05HK.** Let `(S', s') → (S, s)` be a morphism of pointed schemes inducing an
> isomorphism of residue fields, with `S'` affine, let `X'` be the base change of `X` and `F'`
> the pullback of `F`, and let `x' ∈ X'` lie over `x ∈ X` and `s'` (so `s = f x`, `s' = f' x'`).
> Then every complete dévissage of `F/X/S` at `x` base-changes, stage by stage as in Stacks 05HJ,
> to a complete dévissage of `F'/X'/S'` at `x'` whose distinguished points lie over the original
> ones. The finiteness properties of `f'` and `F'` are derived from the base change, not
> assumed.

```lean
theorem CompleteDevissageAt.exists_isBaseChange {h : S' ⟶ S} [IsAffine S']
    [LocallyOfFiniteType f] [F.IsQuasicoherent] [F.IsFiniteType]
    (hres : IsIso (h.residueFieldMap (f' x'))) (pX : X' ⟶ X) (hX : IsPullback pX f' f h)
    (eF : (Scheme.Modules.pullback pX).obj F ≅ F') (hx : pX x' = x)
    (D : CompleteDevissageAt f F x) :
    haveI := locallyOfFiniteType_of_isPullback hX
    haveI := isQuasicoherent_of_iso_pullback eF
    haveI := isFiniteType_of_iso_pullback eF
    ∃ D' : CompleteDevissageAt f' F' x', D.IsBaseChange h pX D'
```

## Tag 05HL, a definition

[Tag 05HL](https://stacks.math.columbia.edu/tag/05HL) in the Stacks Project.

**`AlgebraicGeometry.NonemptyCompleteDevissageAt.StandardShrinking`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/Complete/StandardShrinking.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/Complete/StandardShrinking.lean#L195).

> A standard shrinking of a complete dévissage of `F/X/S` at `x`: standard opens of the
> base and of the source, and standard opens in every stage, containing the distinguished
> points, whose restricted system is again a complete dévissage at `x`.

```lean
structure StandardShrinking {X S : Scheme.{u}} (f : X ⟶ S) (F : X.Modules) (x : X)
    [LocallyOfFiniteType f] [F.IsQuasicoherent] [F.IsFiniteType]
    (D : NonemptyCompleteDevissageAt f F x)
```

## Tag 05HM, a lemma

[Tag 05HM](https://stacks.math.columbia.edu/tag/05HM) in the Stacks Project.

**`AlgebraicGeometry.exists_standardShrinking_finalTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/Complete/ShrinkingFinalTarget.lean, line 339](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/Complete/ShrinkingFinalTarget.lean#L339). The attribute's comment: “final_target_shrinking”.

> **Stacks 05HM, final target shrinking.** Let `W` be a principal open neighbourhood of the
> distinguished point of the smooth scheme of the last stage of a complete dévissage of `F/X/S` at
> `x`. Then there is a standard shrinking of the dévissage whose last smooth open is `W` cut down
> to the inverse image of the new base.

```lean
theorem exists_standardShrinking_finalTarget {X S : Scheme.{u}} (f : X ⟶ S) (F : X.Modules)
    (x : X) [LocallyOfFiniteType f] [F.IsQuasicoherent] [F.IsFiniteType]
    (D : NonemptyCompleteDevissageAt f F x) (W : (finalTargetScheme D.pointed).Opens)
    (a : Γ(finalTargetScheme D.pointed, ⊤))
    (hW : W = (finalTargetScheme D.pointed).basicOpen a)
    (hy : finalTargetPoint D.pointed ∈ W) :
    ∃ E : NonemptyCompleteDevissageAt.StandardShrinking f F x D,
      letI := E.locally_finite_type
      letI := E.quasi_coherent
      letI := E.finite_type
      FinalTargetIsBaseRestriction E.S'.ι E.S' D.pointed E.restricted_devissage.pointed
        E.restricted_stages W
```

**`AlgebraicGeometry.NonemptyCompleteDevissageAt.exists_standardShrinking_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/Complete/ShrinkingOverBase.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/Complete/ShrinkingOverBase.lean#L169). The attribute's comment: “base_shrinking”.

> **Stacks 05HM, base shrinking.** Restricting a complete dévissage at `x` over a standard
> open neighbourhood of `f x` gives a standard shrinking whose base and source are that open
> and its inverse image, and all of whose stages are the corresponding base changes.

```lean
theorem exists_standardShrinking_base {X S : Scheme.{u}} (f : X ⟶ S) (F : X.Modules) (x : X)
    [LocallyOfFiniteType f] [F.IsQuasicoherent] [F.IsFiniteType]
    (D : NonemptyCompleteDevissageAt f F x)
    (V : S.Opens) (a : Γ(S, ⊤)) (hV : V = S.basicOpen a) (hs : f x ∈ V) :
    ∃ E : NonemptyCompleteDevissageAt.StandardShrinking f F x D,
      E.S' = V ∧ E.X' = f ⁻¹ᵁ V ∧
        (letI := E.locally_finite_type
         letI := E.quasi_coherent
         letI := E.finite_type
         PointedChainIsBaseChange E.S'.ι E.X'.ι D.pointed E.restricted_devissage.pointed)
```

**`AlgebraicGeometry.NonemptyCompleteDevissageAt.exists_standardShrinking_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/Complete/ShrinkingSource.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/Complete/ShrinkingSource.lean#L101). The attribute's comment: “source_shrinking”.

> **Stacks 05HM, source shrinking.** A complete dévissage of `F/X/S` at `x` admits a standard
> shrinking whose source open lies inside any prescribed open neighbourhood of `x`.

```lean
theorem exists_standardShrinking_source {X S : Scheme.{u}} (f : X ⟶ S) (F : X.Modules) (x : X)
    [LocallyOfFiniteType f] [F.IsQuasicoherent] [F.IsFiniteType]
    (D : NonemptyCompleteDevissageAt f F x) (U : X.Opens) (hx : x ∈ U) :
    ∃ E : NonemptyCompleteDevissageAt.StandardShrinking f F x D, E.X' ≤ U
```

## Tag 05HR, a proposition

[Tag 05HR](https://stacks.math.columbia.edu/tag/05HR) in the Stacks Project.

**`AlgebraicGeometry.hasEtaleNeighborhoodCompleteDevissageAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/Complete/Existence.lean, line 619](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/Complete/Existence.lean#L619).

> **Stacks Project, Tag 05HR.** A finite-type quasi-coherent module on a scheme locally of
> finite type over `S` acquires a complete dévissage at any chosen point after elementary étale
> neighbourhoods of that point and of its image.
>
> The induction is a well-founded recursion on `AlgebraicGeometry.fiberSupportDim`, which takes
> values in the well-founded order `WithBot ℕ∞`.

```lean
theorem hasEtaleNeighborhoodCompleteDevissageAt {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType] (x : X) :
    HasEtaleNeighborhoodCompleteDevissageAt f F x
```

## Tag 05HU, a lemma

[Tag 05HU](https://stacks.math.columbia.edu/tag/05HU) in the Stacks Project.

**`AlgebraicGeometry.exists_etaleNeighborhood_completeDevissage_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/Complete/Existence.lean, line 1041](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/Complete/Existence.lean#L1041).

> **Stacks Project, Tag 05HU.** Let `X ⟶ S` be a finite-type morphism of schemes and `F` a
> finite-type quasi-coherent module on `X`. For every point `s` of `S` there is an elementary étale
> neighbourhood `(S', s') ⟶ (S, s)` and finitely many étale morphisms `hᵢ : Yᵢ ⟶ X ×_S S'` whose
> images cover the fibre `(X ×_S S')_{s'} = X_s`, such that the pullback of `F` to each `Yᵢ` has a
> complete dévissage along `Yᵢ ⟶ S'` over `s'`.

```lean
theorem exists_etaleNeighborhood_completeDevissage_cover {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [QuasiCompact f] (F : X.Modules) [F.IsQuasicoherent]
    [F.IsFiniteType] (s : S) :
    ∃ (S' : EtaleNeighborhood S s) (_ : S'.IsElementary) (n : ℕ) (Y : Fin n → Scheme.{u})
      (h : ∀ i, Y i ⟶ pullback f S'.toBase) (_ : ∀ i, Etale (h i))
      (hl : ∀ i, LocallyOfFiniteType (h i ≫ pullback.snd f S'.toBase))
      (hq : ∀ i, ((Scheme.Modules.pullback
        (h i ≫ pullback.fst f S'.toBase)).obj F).IsQuasicoherent)
      (ht : ∀ i, ((Scheme.Modules.pullback
        (h i ≫ pullback.fst f S'.toBase)).obj F).IsFiniteType),
      (∀ i, Nonempty (@CompleteDevissage _ _ (h i ≫ pullback.snd f S'.toBase)
        ((Scheme.Modules.pullback (h i ≫ pullback.fst f S'.toBase)).obj F) S'.point
        (hl i) (hq i) (ht i))) ∧
        pullback.snd f S'.toBase ⁻¹' {S'.point} ⊆ ⋃ i, Set.range (h i)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.5, Tag 05HG](https://stacks.math.columbia.edu/tag/05HG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
