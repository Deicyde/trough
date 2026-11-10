---
declaration: section
origin: cited
lean: AlgebraicGeometry.finitePresentationAwayPointsBaseChange, AlgebraicGeometry.finitePresentationAwayPointsBaseChange_full, AlgebraicGeometry.finitePresentationAwayPointsBaseChange_isEquivalence_unconditional, AlgebraicGeometry.finitePresentationAwayPointsBaseChange_faithful, AlgebraicGeometry.isSeparated_iff_forall_baseChangeLocal, AlgebraicGeometry.isProper_iff_forall_baseChangeLocal, AlgebraicGeometry.isFinite_iff_forall_baseChangeLocal, AlgebraicGeometry.baseChangeFibreIso
statement: formalized
proof: formalized
---

# 54.6 Modifying over local rings

Section 54.6 of the Stacks Project, [Tag 0AE1](https://stacks.math.columbia.edu/tag/0AE1). 6 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BFU, an equation

[Tag 0BFU](https://stacks.math.columbia.edu/tag/0BFU) in the Stacks Project.

**`AlgebraicGeometry.finitePresentationAwayPointsBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ModifyingLocalRings/Basic.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ModifyingLocalRings/Basic.lean#L138).

> **Stacks Project, Tag 0BFU.** Base change to the spectra of the local rings defines a
> functor from finitely presented modifications of `S` supported at the distinguished points to
> the product of the corresponding local categories.

```lean
noncomputable def finitePresentationAwayPointsBaseChange
    (D : FinitePresentationAwayPointsSituation.{u}) : BaseChangeFunctor D
```

## Tag 0BFV, a lemma

[Tag 0BFV](https://stacks.math.columbia.edu/tag/0BFV) in the Stacks Project.

**`AlgebraicGeometry.finitePresentationAwayPointsBaseChange_full`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ModifyingLocalRings/BaseChangeEquivalence.lean, line 681](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ModifyingLocalRings/BaseChangeEquivalence.lean#L681). The attribute's comment: “full”.

> **Stacks Project, Tag 0BFV**, the fullness constituent of the equivalence. Base change from
> finitely presented modifications supported at finitely many closed points to the corresponding
> local modifications is full.
>
> With `AlgebraicGeometry.finitePresentationAwayPointsBaseChange_faithful` this says that the
> functor is fully faithful: a global modification supported at the distinguished points is
> determined by its family of localizations, up to a unique isomorphism over `S`.

```lean
theorem finitePresentationAwayPointsBaseChange_full
    (D : FinitePresentationAwayPointsSituation.{u}) :
    (finitePresentationAwayPointsBaseChange D).functor.Full
```

**`AlgebraicGeometry.finitePresentationAwayPointsBaseChange_isEquivalence_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ModifyingLocalRings/BaseChangeEquivalenceSupplement.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ModifyingLocalRings/BaseChangeEquivalenceSupplement.lean#L316).

> **Stacks Project, Tag 0BFV.** Base change from finitely presented modifications supported
> at finitely many closed points to the corresponding local modifications is an equivalence of
> categories.

```lean
theorem finitePresentationAwayPointsBaseChange_isEquivalence_unconditional
    (D : FinitePresentationAwayPointsSituation.{u}) :
    (finitePresentationAwayPointsBaseChange D).functor.IsEquivalence
```

**`AlgebraicGeometry.finitePresentationAwayPointsBaseChange_faithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ModifyingLocalRings/BaseChangeFaithful.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ModifyingLocalRings/BaseChangeFaithful.lean#L162). The attribute's comment: “faithful”.

> The faithfulness constituent of the equivalence of [Stacks, Tag 0BFV]. Base change from
> finitely presented modifications supported at finitely many closed points to the corresponding
> local modifications is faithful.
>
> The equivalence itself, which carries the tag, is
> `AlgebraicGeometry.finitePresentationAwayPointsBaseChange_isEquivalence`.

```lean
theorem finitePresentationAwayPointsBaseChange_faithful
    (D : FinitePresentationAwayPointsSituation.{u}) :
    (finitePresentationAwayPointsBaseChange D).functor.Faithful
```

## Tag 0BFW, a lemma

[Tag 0BFW](https://stacks.math.columbia.edu/tag/0BFW) in the Stacks Project.

**`AlgebraicGeometry.isSeparated_iff_forall_baseChangeLocal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ModifyingLocalRings/MorphismProperties.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ModifyingLocalRings/MorphismProperties.lean#L205). The attribute's comment: “separated”.

> **Stacks Project, Tag 0BFW (separatedness).** If `f : X ⟶ S` corresponds to
> `g i : Y i ⟶ Spec 𝒪_{S, s i}` under the base-change functor of Tag 0BFU, then `f` is separated
> if and only if every `g i` is separated.

```lean
theorem isSeparated_iff_forall_baseChangeLocal
    {D : FinitePresentationAwayPointsSituation.{u}} (BC : BaseChangeFunctor D)
    (X : D.globalCategory) :
    IsSeparated X.obj.hom ↔ ∀ i, IsSeparated (BC.functor.obj X i).obj.hom
```

**`AlgebraicGeometry.isProper_iff_forall_baseChangeLocal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ModifyingLocalRings/MorphismProperties.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ModifyingLocalRings/MorphismProperties.lean#L218). The attribute's comment: “proper”.

> **Stacks Project, Tag 0BFW (properness).** If `f : X ⟶ S` corresponds to
> `g i : Y i ⟶ Spec 𝒪_{S, s i}` under the base-change functor of Tag 0BFU, then `f` is proper if
> and only if every `g i` is proper.

```lean
theorem isProper_iff_forall_baseChangeLocal
    {D : FinitePresentationAwayPointsSituation.{u}} (BC : BaseChangeFunctor D)
    (X : D.globalCategory) :
    IsProper X.obj.hom ↔ ∀ i, IsProper (BC.functor.obj X i).obj.hom
```

**`AlgebraicGeometry.isFinite_iff_forall_baseChangeLocal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ModifyingLocalRings/MorphismProperties.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ModifyingLocalRings/MorphismProperties.lean#L231). The attribute's comment: “finite”.

> **Stacks Project, Tag 0BFW (finiteness).** If `f : X ⟶ S` corresponds to
> `g i : Y i ⟶ Spec 𝒪_{S, s i}` under the base-change functor of Tag 0BFU, then `f` is finite if
> and only if every `g i` is finite.

```lean
theorem isFinite_iff_forall_baseChangeLocal
    {D : FinitePresentationAwayPointsSituation.{u}} (BC : BaseChangeFunctor D)
    (X : D.globalCategory) :
    IsFinite X.obj.hom ↔ ∀ i, IsFinite (BC.functor.obj X i).obj.hom
```

## Tag 0BFX, a lemma

[Tag 0BFX](https://stacks.math.columbia.edu/tag/0BFX) in the Stacks Project.

**`AlgebraicGeometry.baseChangeFibreIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ModifyingLocalRings/Fibre.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ModifyingLocalRings/Fibre.lean#L106).

> **Stacks Project, Tag 0BFX.** If `f : X ⟶ S` corresponds to `g i : Y i ⟶ Spec 𝒪_{S, s i}`
> under the base-change functor, then the fibre of `f` over `s i` is isomorphic to the fibre of
> `g i` over the closed point, as schemes over `κ(s i)`.

```lean
noncomputable def baseChangeFibreIso (D : FinitePresentationAwayPointsSituation.{u})
    (BC : BaseChangeFunctor D) (X : D.globalCategory) (i : Fin D.n) :
    (Over.pullback (D.S.fromSpecResidueField (D.points i))).obj
        ((ObjectProperty.ι (IsFinitePresentationAway D.complement)).obj X) ≅
      (Over.pullback (D.fromSpecResidueFieldLocal i)).obj
        ((ObjectProperty.ι (IsFinitePresentationAway (D.puncturedLocalScheme i))).obj
          (BC.functor.obj X i))
```

## Tag 0BFY, a lemma

[Tag 0BFY](https://stacks.math.columbia.edu/tag/0BFY) in the Stacks Project.

**`AlgebraicGeometry.FinitePresentationAwayPointsSituation.factorsAsPointBlowups_of_corresponds`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ModifyingLocalRings/PointBlowupSequence.lean, line 437](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ModifyingLocalRings/PointBlowupSequence.lean#L437). The attribute's comment: “necessity”.

> **Stacks Project, Tag 0BFY**, necessity, in the language of Tag 0BFU. If `f : X ⟶ S` factors
> as a finite sequence of blowups at closed points lying over the distinguished points, then every
> local modification `g i : Y i ⟶ Spec 𝒪_{S, s i}` corresponding to it under a base-change functor
> factors as a finite sequence of blowups at closed points lying over the closed point.
>
> Sufficiency is not proved: it needs full faithfulness of the base-change functor, which is
> [Stacks, Tag 0BFV] and is absent from this development.

```lean
theorem factorsAsPointBlowups_of_corresponds (D : FinitePresentationAwayPointsSituation.{u})
    (BC : BaseChangeFunctor D) (X : D.globalCategory) (i : Fin D.n) (Y : D.localCategory i)
    (hY : BC.functor.obj X i ≅ Y)
    (h : FactorsAsPointBlowups D.S (Set.range D.points) X.obj.left X.obj.hom) :
    FactorsAsPointBlowups (D.localScheme i)
      {IsLocalRing.closedPoint (D.S.presheaf.stalk (D.points i))} Y.obj.left Y.obj.hom
```

**`AlgebraicGeometry.FinitePresentationAwayPointsSituation.factorsAsPointBlowups_iff_forall_corresponds`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ModifyingLocalRings/PointBlowupSequenceConverse.lean, line 514](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ModifyingLocalRings/PointBlowupSequenceConverse.lean#L514).

> **Stacks Project, Tag 0BFY.** Let `S` be a scheme, let `s 1, …, s n` be pairwise distinct
> closed points whose open complement has quasi-compact inclusion, and let `f : X ⟶ S` correspond
> to `g i : Y i ⟶ Spec 𝒪_{S, s i}` under the base-change functor `F` of [Stacks, Tag 0BFU]. Then
> `f` admits a factorization `X = Z m ⟶ … ⟶ Z 0 = S` in which every step is the blowing up of its
> target at a closed point lying over the *set* `{s 1, …, s n}` if and only if, for every `i`, the
> morphism `g i` admits a factorization `Y i = Z i (m i) ⟶ … ⟶ Z i 0 = Spec 𝒪_{S, s i}` in which
> every step is the blowing up of its target at a closed point lying over the closed point, which
> is `s i` itself.

```lean
theorem factorsAsPointBlowups_iff_forall_corresponds
    (D : FinitePresentationAwayPointsSituation.{u}) (X : D.globalCategory)
    (Y : ∀ i, D.localCategory i)
    (hY : ∀ i, (finitePresentationAwayPointsBaseChange D).functor.obj X i ≅ Y i) :
    FactorsAsPointBlowups D.S (Set.range D.points) X.obj.left X.obj.hom ↔
      ∀ i, FactorsAsPointBlowups (D.localScheme i)
        {IsLocalRing.closedPoint (D.S.presheaf.stalk (D.points i))} (Y i).obj.left
        (Y i).obj.hom
```

**`AlgebraicGeometry.FinitePresentationAwayPointsSituation.factorsAsPointBlowups_iff_forall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ModifyingLocalRings/PointBlowupSequenceSufficiency.lean, line 503](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ModifyingLocalRings/PointBlowupSequenceSufficiency.lean#L503).

> **Stacks Project, Tag 0BFY.** Let `S` be a scheme with pairwise distinct closed points
> `s 0, …, s (n - 1)` whose open complement has quasi-compact inclusion, and let `f : X ⟶ S`, of
> finite presentation and an isomorphism over that complement, correspond under a base-change
> functor of Tag 0BFU to the local modifications `g i : Y i ⟶ Spec 𝒪_{S, s i}`. Then `f` factors as
> a finite sequence of blowups at closed points lying over the `s i` if and only if every `g i`
> factors as a finite sequence of blowups at closed points lying over the closed point of
> `Spec 𝒪_{S, s i}`.

```lean
theorem factorsAsPointBlowups_iff_forall (BC : BaseChangeFunctor D) (X : D.globalCategory)
    (Y : ∀ i, D.localCategory i) (hY : BC.functor.obj X ≅ Y) :
    FactorsAsPointBlowups D.S (Set.range D.points) X.obj.left X.obj.hom ↔
      ∀ i, FactorsAsPointBlowups (D.localScheme i)
        {IsLocalRing.closedPoint (D.S.presheaf.stalk (D.points i))} (Y i).obj.left
        (Y i).obj.hom
```

## Tag 0BFZ, a lemma

[Tag 0BFZ](https://stacks.math.columbia.edu/tag/0BFZ) in the Stacks Project.

**`AlgebraicGeometry.FinitePresentationAwayPointsSituation.factorsAsNormalizedPointBlowups_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ModifyingLocalRings/NormalizedPointBlowupCorrespondence.lean, line 561](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ModifyingLocalRings/NormalizedPointBlowupCorrespondence.lean#L561). The attribute's comment: “corrected: S normal added, the statement being false without it; both directions”.

> **Stacks Project, Tag 0BFZ**, for a normal base. Let `S, s i, S_i` be as in Tag 0BFU, with
> `S` normal and every quasi-compact open of `S` having finitely many irreducible components, and
> let `f : X ⟶ S` correspond to the `g i : Y i ⟶ S_i` under the base-change functor. Then `f` is a
> finite sequence of normalized blowups at closed points lying over the distinguished points if and
> only if, for each `i`, `g i` is a finite sequence of normalized blowups at closed points lying
> over the closed point of `S_i`.
>
> Normality is necessary: `AlgebraicGeometry.not_factorsAsNormalizedPointBlowups_iff` exhibits a
> scheme satisfying the remaining hypotheses for which the equivalence fails.

```lean
theorem factorsAsNormalizedPointBlowups_iff [IsNormal D.S]
    (hS : ∀ U : D.S.Opens, IsCompact (U : Set D.S) → (irreducibleComponents U).Finite)
    (BC : BaseChangeFunctor D) (X : D.globalCategory) (Y : ∀ i, D.localCategory i)
    (hY : ∀ i, BC.functor.obj X i ≅ Y i) :
    FactorsAsNormalizedPointBlowups D.S (Set.range D.points) X.obj.left X.obj.hom ↔
      ∀ i, FactorsAsNormalizedPointBlowups (D.localScheme i)
        {IsLocalRing.closedPoint (D.S.presheaf.stalk (D.points i))} (Y i).obj.left
        (Y i).obj.hom
```

**`AlgebraicGeometry.FinitePresentationAwayPointsSituation.factorsAsNormalizedPointBlowups_of_corresponds`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ModifyingLocalRings/NormalizedPointBlowupSequence.lean, line 504](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ModifyingLocalRings/NormalizedPointBlowupSequence.lean#L504). The attribute's comment: “necessity only; corrected: S normal added, the statement being false without it”.

> **Stacks Project, Tag 0BFZ**, necessity, for a normal base, in the language of Tag 0BFU. If
> `f : X ⟶ S` factors as a finite sequence of normalized blowups at closed points lying over the
> distinguished points, then every local modification `g i : Y i ⟶ Spec 𝒪_{S, s i}` corresponding
> to it under a base-change functor factors as a finite sequence of normalized blowups at closed
> points lying over the closed point.
>
> Both directions are
> `AlgebraicGeometry.FinitePresentationAwayPointsSituation.factorsAsNormalizedPointBlowups_iff`.

```lean
theorem factorsAsNormalizedPointBlowups_of_corresponds
    (D : FinitePresentationAwayPointsSituation.{u}) [IsNormal D.S] (BC : BaseChangeFunctor D)
    (X : D.globalCategory) (i : Fin D.n) (Y : D.localCategory i)
    (hY : BC.functor.obj X i ≅ Y)
    (h : FactorsAsNormalizedPointBlowups D.S (Set.range D.points) X.obj.left X.obj.hom) :
    FactorsAsNormalizedPointBlowups (D.localScheme i)
      {IsLocalRing.closedPoint (D.S.presheaf.stalk (D.points i))} Y.obj.left Y.obj.hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 54.6, Tag 0AE1](https://stacks.math.columbia.edu/tag/0AE1)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
