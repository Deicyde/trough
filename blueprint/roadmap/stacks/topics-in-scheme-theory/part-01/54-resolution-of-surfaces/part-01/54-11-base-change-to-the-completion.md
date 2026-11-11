---
declaration: section
origin: cited
lean: AlgebraicGeometry.stalkMap_adicCompletion_isomorphism, AlgebraicGeometry.isRegularLocalRing_stalk_of_completion, AlgebraicGeometry.isRegularLocalRing_stalk_pullback_completion_iff, AlgebraicGeometry.isRegular_pullback_completion_iff, Stacks.Blowup.exists_isAdmissibleBlowup_isPullback_completion, AlgebraicGeometry.isNormalDomain_adicCompletion_stalk_blowUp_maximalIdeal, AlgebraicGeometry.definesRationalSingularity_adicCompletion_and_isNormalDomain_stalk_blowUp, AlgebraicGeometry.Scheme.normalization_isFinite_of_etaleAt_genericPoints
statement: formalized
proof: formalized
---

# 54.11 Base change to the completion

Section 54.11 of the Stacks Project, [Tag 0BG4](https://stacks.math.columbia.edu/tag/0BG4). 7 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BG5, a lemma

[Tag 0BG5](https://stacks.math.columbia.edu/tag/0BG5) in the Stacks Project.

**`AlgebraicGeometry.stalkMap_adicCompletion_isomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/StalkBaseChange.lean, line 863](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/StalkBaseChange.lean#L863). References: EGA IV (7.9.3.1).

> After base change from a local ring to its completion, the map on local rings at a point
> over the closed point induces an isomorphism on completions.

```lean
theorem stalkMap_adicCompletion_isomorphism
    (A : Type u) [CommRing A] [IsLocalRing A]
    (hfg : (IsLocalRing.maximalIdeal A).FG)
    (X : Scheme.{u}) (f : X ⟶ Spec (.of A)) :
    let Ahat := AdicCompletion (IsLocalRing.maximalIdeal A) A
    let g : Spec (.of Ahat) ⟶ Spec (.of A) :=
      Spec.map (CommRingCat.ofHom (algebraMap A Ahat))
    let Y : Scheme.{u} := pullback f g
    let π : Y ⟶ X := pullback.fst f g
    ∀ (q : Y),
      f.base (π.base q) =
          (⟨IsLocalRing.maximalIdeal A, inferInstance⟩ : PrimeSpectrum A) →
        ∃ e : AdicCompletion
              (IsLocalRing.maximalIdeal (X.presheaf.stalk (π.base q)))
              (X.presheaf.stalk (π.base q)) ≃+*
            AdicCompletion (IsLocalRing.maximalIdeal (Y.presheaf.stalk q))
              (Y.presheaf.stalk q),
          e.toRingHom.comp
              (algebraMap (X.presheaf.stalk (π.base q))
                (AdicCompletion
                  (IsLocalRing.maximalIdeal (X.presheaf.stalk (π.base q)))
                  (X.presheaf.stalk (π.base q)))) =
            (algebraMap (Y.presheaf.stalk q)
              (AdicCompletion (IsLocalRing.maximalIdeal (Y.presheaf.stalk q))
                (Y.presheaf.stalk q))).comp (π.stalkMap q).hom
```

## Tag 0BG6, a lemma

[Tag 0BG6](https://stacks.math.columbia.edu/tag/0BG6) in the Stacks Project.

**`AlgebraicGeometry.isRegularLocalRing_stalk_of_completion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/RegularBaseChange.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/RegularBaseChange.lean#L66). The attribute's comment: “pointwise\_descent”. References: EGA 0 (17.1.5), “Â regular ⇒ A regular”.

> Regularity of a local ring of a scheme descends pointwise from its base change to the
> completion of a Noetherian local base ring.

```lean
theorem isRegularLocalRing_stalk_of_completion
    (R : Type u) [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    (X : Scheme.{u}) (f : X ⟶ Spec (.of R))
    (x : X)
    (y : (pullback f
      (Spec.map (CommRingCat.ofHom
        (algebraMap R (AdicCompletion (IsLocalRing.maximalIdeal R) R)))) : Scheme.{u}))
    (hy : (pullback.fst f
      (Spec.map (CommRingCat.ofHom
        (algebraMap R (AdicCompletion (IsLocalRing.maximalIdeal R) R))))).base y = x)
    (hregular : IsRegularLocalRing
      ((pullback f
        (Spec.map (CommRingCat.ofHom
          (algebraMap R (AdicCompletion (IsLocalRing.maximalIdeal R) R)))) :
          Scheme.{u}).presheaf.stalk y)) :
    IsRegularLocalRing (X.presheaf.stalk x)
```

**`AlgebraicGeometry.isRegularLocalRing_stalk_pullback_completion_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/RegularBaseChange.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/RegularBaseChange.lean#L110). The attribute's comment: “closed\_fibre\_equivalence”. References: EGA 0 (17.1.5).

> At a point of the closed fibre, regularity of the local ring is invariant under base change
> from a Noetherian local ring to its completion.

```lean
theorem isRegularLocalRing_stalk_pullback_completion_iff
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (X : Scheme.{u}) (f : X ⟶ Spec (.of A)) [LocallyOfFiniteType f]
    (x : X)
    (y : (pullback f (Spec.map (CommRingCat.ofHom
      (algebraMap A (AdicCompletion (IsLocalRing.maximalIdeal A) A)))) : Scheme.{u}))
    (hx : (pullback.fst f (Spec.map (CommRingCat.ofHom
      (algebraMap A (AdicCompletion (IsLocalRing.maximalIdeal A) A))))).base y = x)
    (hy : (pullback.snd f (Spec.map (CommRingCat.ofHom
      (algebraMap A (AdicCompletion (IsLocalRing.maximalIdeal A) A))))).base y =
      (⟨IsLocalRing.maximalIdeal (AdicCompletion (IsLocalRing.maximalIdeal A) A), inferInstance⟩ :
        PrimeSpectrum (AdicCompletion (IsLocalRing.maximalIdeal A) A))) :
    IsRegularLocalRing
        ((pullback f (Spec.map (CommRingCat.ofHom
          (algebraMap A (AdicCompletion (IsLocalRing.maximalIdeal A) A)))) :
          Scheme.{u}).presheaf.stalk y) ↔
      IsRegularLocalRing (X.presheaf.stalk x)
```

**`AlgebraicGeometry.isRegular_pullback_completion_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/RegularBaseChange.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/RegularBaseChange.lean#L168). The attribute's comment: “proper\_equivalence”.

> A proper scheme locally of finite type over a Noetherian local ring is regular if and only
> if its base change to the completion of the base ring is regular.

```lean
theorem isRegular_pullback_completion_iff
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (X : Scheme.{u}) (f : X ⟶ Spec (.of A)) [IsProper f] :
    IsRegular X ↔
      IsRegular
        (pullback f (Spec.map (CommRingCat.ofHom
          (algebraMap A (AdicCompletion (IsLocalRing.maximalIdeal A) A)))) : Scheme.{u})
```

## Tag 0AFK, a lemma

[Tag 0AFK](https://stacks.math.columbia.edu/tag/0AFK) in the Stacks Project.

**`Stacks.Blowup.exists_isAdmissibleBlowup_isPullback_completion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/AdmissibleCompletionDescent.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/AdmissibleCompletionDescent.lean#L268).

> **Stacks Project, Tag 0AFK.** An admissible blowup of the spectrum of the maximal-ideal
> completion of a Noetherian local ring `A`, relative to the punctured spectrum, is the base change
> of an admissible blowup of `Spec A` relative to its punctured spectrum.

```lean
theorem exists_isAdmissibleBlowup_isPullback_completion
    (A : Type u) [CommRing A] [IsLocalRing A] [IsNoetherianRing A]
    (Y : Scheme.{u})
    (g : Y ⟶ Spec (.of (AdicCompletion (maximalIdeal A) A)))
    (hg : IsAdmissibleBlowup
      (Stacks.Divisors.puncturedSpectrum (AdicCompletion (maximalIdeal A) A)) g) :
    ∃ (X : Scheme.{u}) (f : X ⟶ Spec (.of A)),
      IsAdmissibleBlowup (Stacks.Divisors.puncturedSpectrum A) f ∧
        ∃ h : Y ⟶ X,
          IsPullback h g f
            (Spec.map (CommRingCat.ofHom
              (algebraMap A (AdicCompletion (maximalIdeal A) A))))
```

## Tag 0BG7, a lemma

[Tag 0BG7](https://stacks.math.columbia.edu/tag/0BG7) in the Stacks Project.

**`AlgebraicGeometry.isNormalDomain_adicCompletion_stalk_blowUp_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalDoublePoints/BlowUpCompletedLocalRings.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalDoublePoints/BlowUpCompletedLocalRings.lean#L168). The attribute's comment: “clause (2): the completion of the local ring at every closed point of the blowup of Spec(A) in the maximal ideal is a normal domain. Tag 0B4Z at the completion — normality of the blowup of Spec(A^) in the maximal ideal of A^ — is carried as the hypothesis `hnormal`, and the source's hypotheses on A (normal Nagata domain of dimension two defining a rational singularity with normal completion) are exactly what Tag 0B4Z consumes there”.

> **Stacks Project, Tag 0BG7, clause (2).** For a Noetherian local ring `A` whose blowup of
> `Spec A^` in the maximal ideal of the completion `A^` is normal, the completion of the local ring
> of the blowup of `Spec A` in the maximal ideal of `A` is a normal domain at every closed point.
>
> The hypothesis `hnormal` is [Stacks, Tag 0B4Z] for `A^`, which this development does not carry;
> in the source it is supplied by the hypotheses that `A` is a normal Nagata domain of dimension
> two defining a rational singularity whose completion is normal.

```lean
public theorem isNormalDomain_adicCompletion_stalk_blowUp_maximalIdeal
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (hnormal : IsNormal (blowUp (maximalIdealSheaf (AdicCompletion (maximalIdeal A) A))))
    (x : blowUp (maximalIdealSheaf A))
    (hx : IsClosed ({x} : Set (blowUp (maximalIdealSheaf A)))) :
    IsNormalDomain (AdicCompletion
      (maximalIdeal ((blowUp (maximalIdealSheaf A)).presheaf.stalk x))
      ((blowUp (maximalIdealSheaf A)).presheaf.stalk x))
```

**`AlgebraicGeometry.definesRationalSingularity_adicCompletion_and_isNormalDomain_stalk_blowUp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalDoublePoints/BlowupStillGood.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalDoublePoints/BlowupStillGood.lean#L42).

> Let `(A, 𝔪, κ)` be a Nagata local normal domain of dimension two which defines a rational
> singularity and whose completion `A^` is normal. Then
>
> 1. `A^` defines a rational singularity, and
> 2. if `X ⟶ Spec(A)` is the blowup in `𝔪`, then for a closed point `x ∈ X` the completion of
>    `𝒪_{X, x}` is normal (indeed a normal domain).

```lean
theorem definesRationalSingularity_adicCompletion_and_isNormalDomain_stalk_blowUp
    (A : Type u) [CommRing A] [IsLocalRing A] [IsNormalDomain A] (hNagata : IsNagataRing A)
    [IsNormalDomain (AdicCompletion (maximalIdeal A) A)]
    (hdim : ringKrullDim A = 2) (hrat : DefinesRationalSingularity A) :
    DefinesRationalSingularity (AdicCompletion (maximalIdeal A) A) ∧
      ∀ x : blowUp (maximalIdealSheaf A), IsClosed ({x} : Set (blowUp (maximalIdealSheaf A))) →
        IsNormalDomain (AdicCompletion
          (maximalIdeal ((blowUp (maximalIdealSheaf A)).presheaf.stalk x))
          ((blowUp (maximalIdealSheaf A)).presheaf.stalk x))
```

## Tag 0BG8, a lemma

[Tag 0BG8](https://stacks.math.columbia.edu/tag/0BG8) in the Stacks Project.

**`AlgebraicGeometry.Scheme.normalization_isFinite_of_etaleAt_genericPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Finiteness.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Finiteness.lean#L178).

> If a scheme is locally of finite type over an analytically
> unramified Noetherian local ring and is étale over it at the generic points of its irreducible
> components, then its normalization morphism is finite.

```lean
theorem normalization_isFinite_of_etaleAt_genericPoints (A : Type u) [CommRing A]
    [IsNoetherianRing A] [IsLocalRing A] {X : Scheme.{u}} (f : X ⟶ Spec (.of A))
    [LocallyOfFiniteType f] (hA : IsAnalyticallyUnramified A)
    (hf : ∀ x : X, x ∈ genericPoints X → EtaleAt f x) :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian f
    let hX : ∀ U : X.Opens, IsCompact (U : Set X) →
        (irreducibleComponents U).Finite := fun U hU ↦ by
      let : CompactSpace U := isCompact_iff_compactSpace.mp hU
      let : NoetherianSpace U :=
        noetherianSpace_of_isLocallyNoetherianSpace U
          ((isLocallyNoetherianSpace_of_isLocallyNoetherian X).subtype U)
      exact NoetherianSpace.finite_irreducibleComponents
    IsFinite (normalization X hX)
```

## Tag 0BG9, a lemma

[Tag 0BG9](https://stacks.math.columbia.edu/tag/0BG9) in the Stacks Project.

**`AlgebraicGeometry.SemistableReduction.isFinite_normalization_of_isNormal_complementSpecialFiber_completion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Normalization/BaseChangeToCompletion.lean, line 1348](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Normalization/BaseChangeToCompletion.lean#L1348). The attribute's comment: “finiteness”.

> **Stacks Project, Tag 0BG9 (finiteness).** If the complement of the special fibre after
> completion is normal, then the normalization is finite.

```lean
public theorem isFinite_normalization_of_isNormal_complementSpecialFiber_completion
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of A)) [LocallyOfFiniteType f]
    (hnormal :
      let Ahat := AdicCompletion (maximalIdeal A) A
      let i : Spec (.of Ahat) ⟶ Spec (.of A) :=
        Spec.map (CommRingCat.ofHom (algebraMap A Ahat))
      let Y : Scheme.{u} := pullback f i
      let q : Y ⟶ Spec (.of Ahat) := pullback.snd f i
      IsNormal (complementSpecialFiber q)) :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian f
    let hX : ∀ U : X.Opens, IsCompact (U : Set X) →
        (irreducibleComponents U).Finite := fun U hU ↦ by
      have : CompactSpace U := isCompact_iff_compactSpace.mp hU
      have : NoetherianSpace U :=
        noetherianSpace_of_isLocallyNoetherianSpace U
          ((isLocallyNoetherianSpace_of_isLocallyNoetherian X).subtype U)
      exact NoetherianSpace.finite_irreducibleComponents
    IsFinite (Scheme.normalization X hX)
```

**`AlgebraicGeometry.SemistableReduction.exists_iso_pullback_normalization_completion_of_isNormal_complementSpecialFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Normalization/BaseChangeToCompletion.lean, line 1376](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Normalization/BaseChangeToCompletion.lean#L1376). The attribute's comment: “compatibility with completion”.

> **Stacks Project, Tag 0BG9 (compatibility with completion).** If the complement of the
> special fibre after completion is normal, base change to the completion carries the
> normalization of `X` to the normalization of the completed base change, compatibly with the
> maps to that base change.

```lean
public theorem exists_iso_pullback_normalization_completion_of_isNormal_complementSpecialFiber
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of A)) [LocallyOfFiniteType f]
    (hnormal :
      let Ahat := AdicCompletion (maximalIdeal A) A
      let i : Spec (.of Ahat) ⟶ Spec (.of A) :=
        Spec.map (CommRingCat.ofHom (algebraMap A Ahat))
      let Y : Scheme.{u} := pullback f i
      let q : Y ⟶ Spec (.of Ahat) := pullback.snd f i
      IsNormal (complementSpecialFiber q)) :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian f
    let Ahat := AdicCompletion (maximalIdeal A) A
    let i : Spec (.of Ahat) ⟶ Spec (.of A) :=
      Spec.map (CommRingCat.ofHom (algebraMap A Ahat))
    let Y : Scheme.{u} := pullback f i
    let p : Y ⟶ X := pullback.fst f i
    let hX : ∀ U : X.Opens, IsCompact (U : Set X) →
        (irreducibleComponents U).Finite := fun U hU ↦ by
      have : CompactSpace U := isCompact_iff_compactSpace.mp hU
      have : NoetherianSpace U :=
        noetherianSpace_of_isLocallyNoetherianSpace U
          ((isLocallyNoetherianSpace_of_isLocallyNoetherian X).subtype U)
      exact NoetherianSpace.finite_irreducibleComponents
    let νX := Scheme.normalization X hX
    letI : IsLocallyNoetherian Y := inferInstance
    let hY : ∀ V : Y.Opens, IsCompact (V : Set Y) →
        (irreducibleComponents V).Finite := fun V hV ↦ by
      have : CompactSpace V := isCompact_iff_compactSpace.mp hV
      have : NoetherianSpace V :=
        noetherianSpace_of_isLocallyNoetherianSpace V
          ((isLocallyNoetherianSpace_of_isLocallyNoetherian Y).subtype V)
      exact NoetherianSpace.finite_irreducibleComponents
    let νY := Scheme.normalization Y hY
    ∃ e : pullback νX p ≅ Scheme.normalizationScheme Y hY,
      e.hom ≫ νY = pullback.snd νX p
```

## Tag 0BGA, a lemma

[Tag 0BGA](https://stacks.math.columbia.edu/tag/0BGA) in the Stacks Project.

**`AlgebraicGeometry.exists_normalizedBlowUpSeqDescent_of_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Normalization/NormalizedBlowUpDescent.lean, line 349](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Normalization/NormalizedBlowUpDescent.lean#L349). The attribute's comment: “the whole statement, under the additional hypothesis that the completion is a Nagata ring; that is Tag 0335 item (2) for a Noetherian complete local ring, which is not available here”.

> **Stacks Project, Tag 0BGA.** Let `A` be a Noetherian local domain whose completion `A^` is
> normal. Every finite sequence of normalized blowups `Yₙ → ⋯ → Y₁ → Spec A^` is the base change
> to `A^` of a finite sequence of normalized blowups `Xₙ → ⋯ → X₁ → Spec A`, stage by stage, and
> the latter sequence is proper over `Spec A`.
>
> The hypothesis that `A^` is a Nagata ring is Tag 0335 for a Noetherian complete local ring; it is
> carried explicitly because that case of Tag 0335 is not available here. It is what makes every
> stage of the given sequence normal and proper over `Spec A^`, hence makes the centre of each
> normalized blowup lie over the closed point.

```lean
public theorem exists_normalizedBlowUpSeqDescent_of_adicCompletion
    (A : Type u) [CommRing A] [IsDomain A] [IsNoetherianRing A] [IsLocalRing A]
    (hnormal : IsNormalRing (AdicCompletion (maximalIdeal A) A))
    (hnagata : IsNagataRing (AdicCompletion (maximalIdeal A) A))
    {Y : Scheme.{u}} {g : Y ⟶ Spec (.of (AdicCompletion (maximalIdeal A) A))}
    (hseq : NormalizedBlowUpSeq (Spec (.of (AdicCompletion (maximalIdeal A) A))) Y g) :
    ∃ (X : Scheme.{u}) (f : X ⟶ Spec (.of A)) (p : Y ⟶ X),
      NormalizedBlowUpSeqDescent A X f Y g p ∧ IsProper f
```

**`AlgebraicGeometry.exists_normalizedBlowUpSeqDescent_of_adicCompletion_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Normalization/NormalizedBlowUpDescentExtra.lean, line 35](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Normalization/NormalizedBlowUpDescentExtra.lean#L35).

> **Stacks Project, Tag 0BGA.** Let `A` be a Noetherian local domain whose completion `A^` is
> normal. Every finite sequence of normalized blowups `Yₙ → ⋯ → Y₁ → Spec A^` is the base change
> to `A^` of a finite sequence of normalized blowups `Xₙ → ⋯ → X₁ → Spec A`, stage by stage, and
> the latter sequence is proper over `Spec A`.
>
> That `A^` is a Nagata ring is not a hypothesis here: `A^` is Noetherian, local, and complete for
> its own maximal ideal, so [Stacks, Tag 032W] applies to it.

```lean
public theorem exists_normalizedBlowUpSeqDescent_of_adicCompletion_unconditional
    (A : Type u) [CommRing A] [IsDomain A] [IsNoetherianRing A] [IsLocalRing A]
    (hnormal : IsNormalRing (AdicCompletion (maximalIdeal A) A))
    {Y : Scheme.{u}} {g : Y ⟶ Spec (.of (AdicCompletion (maximalIdeal A) A))}
    (hseq : NormalizedBlowUpSeq (Spec (.of (AdicCompletion (maximalIdeal A) A))) Y g) :
    ∃ (X : Scheme.{u}) (f : X ⟶ Spec (.of A)) (p : Y ⟶ X),
      NormalizedBlowUpSeqDescent A X f Y g p ∧ IsProper f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 54.11, Tag 0BG4](https://stacks.math.columbia.edu/tag/0BG4)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
