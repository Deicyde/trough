---
declaration: section
origin: cited
lean: Stacks.WeilCohomology.eq_of_cohomologicalChernCharacter, Stacks.WeilCohomology.exists_cohomologicalChernCharacter, Stacks.WeilCohomology.eq_of_cohomologicalChernCharacter', Stacks.WeilCohomology.exists_cohomologicalChernCharacter_of_source, Stacks.WeilCohomology.FirstChernClassData.existsUnique_cohomologicalChernCharacter, Stacks.WeilCohomology.FirstChernClassData.existsUnique_codimensionCycleClass, Stacks.WeilCohomology.FirstChernClassData.existsUnique_cycleClassMap, Stacks.WeilCohomology.CycleClassSetup.isCycleClassRule_cycleClassMap
statement: formalized
proof: formalized
---

# 45.14 Weil cohomology theories, III

Section 45.14 of the Stacks Project, [Tag 0FID](https://stacks.math.columbia.edu/tag/0FID). 18 tags here are carried by 32 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FIE, a lemma

[Tag 0FIE](https://stacks.math.columbia.edu/tag/0FIE) in the Stacks Project.

**`Stacks.WeilCohomology.eq_of_cohomologicalChernCharacter`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/CohomologicalChernCharacter.lean, line 238](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/CohomologicalChernCharacter.lean#L238). The attribute's comment: “uniqueness, for the class of a finite locally free module of constant rank: two rules compatible with pullbacks and taking the value `exp(c₁^H(ℒ))` on an invertible module agree there. Constant rank is the source's reduction by condition (2) of the situation of Section 45.12, which `ChernSetup` does not transcribe, and the pullback homomorphism of `K₀(Vect(-))`, which this repository does not construct, is a hypothesis”.

> **The uniqueness half of Stacks Tag 0FIE.** Two rules assigning to every object `X` of `𝒞` a
> ring homomorphism `K₀(Vect(X)) ⟶ ∏_{i ≥ 0} H^{2i}(X)(i)`, compatible with pullbacks and taking
> the value `exp(c_1^H(ℒ))` on every invertible module, agree on the class of every finite locally
> free module of constant rank.
>
> The splitting principle of Tag 0FI7 supplies `p : P ⟶ X` with `p^*` injective on `A` and a
> filtration of `p^*ℰ` with invertible successive quotients. That filtration writes `[p^*ℰ]` as a
> sum of classes of invertible modules in `K₀(Vect(P))`, where additivity and the prescribed value
> determine the character; compatibility with pullbacks identifies the result with
> `p^*ch^H([ℰ])`, and `p^*` is injective.

```lean
theorem eq_of_cohomologicalChernCharacter
    (hκ : ∀ {X Y : C} (f : X ⟶ Y) (E : (S.obj Y).Modules),
      Stacks.FiniteLocallyFree.IsFiniteLocallyFree.{u, u, u} E →
        κ f (VectorBundleKZero.classOf (S.obj Y) E) =
          VectorBundleKZero.classOf (S.obj X) ((Scheme.Modules.pullback (S.map f)).obj E))
    {ch ch' : ∀ X : C, VectorBundleKZero (S.obj X) →+* PowerSeries (𝔄.A X)}
    (hpull : ∀ {X Y : C} (f : X ⟶ Y) (α : VectorBundleKZero (S.obj Y)),
      PowerSeries.map (𝔄.pull f) (ch Y α) = ch X (κ f α))
    (hpull' : ∀ {X Y : C} (f : X ⟶ Y) (α : VectorBundleKZero (S.obj Y)),
      PowerSeries.map (𝔄.pull f) (ch' Y α) = ch' X (κ f α))
    (hinv : ∀ (X : C) (L : (S.obj X).Modules)
      (hL : AlgebraicGeometry.SheafOfModules.IsInvertible (S.obj X).presheaf
        (S.obj X).ringCatSheaf.2 L),
      ch X (VectorBundleKZero.classOf (S.obj X) L) =
        expFirstChernClass 𝔄 X (picardClassOf (S.obj X) L hL))
    (hinv' : ∀ (X : C) (L : (S.obj X).Modules)
      (hL : AlgebraicGeometry.SheafOfModules.IsInvertible (S.obj X).presheaf
        (S.obj X).ringCatSheaf.2 L),
      ch' X (VectorBundleKZero.classOf (S.obj X) L) =
        expFirstChernClass 𝔄 X (picardClassOf (S.obj X) L hL))
    (X : C) (E : (S.obj X).Modules) (r : ℕ)
    (hE : AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E r) :
    ch X (VectorBundleKZero.classOf (S.obj X) E) =
      ch' X (VectorBundleKZero.classOf (S.obj X) E)
```

**`Stacks.WeilCohomology.exists_cohomologicalChernCharacter`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/CohomologicalChernCharacter.lean, line 287](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/CohomologicalChernCharacter.lean#L287). The attribute's comment: “existence: the rule, as a ring homomorphism out of `K₀(Vect(X))` into `∏_{i ≥ 0} H^{2i}(X)(i)`, together with its grading, its compatibility with pullbacks and its value `exp(c₁^H(ℒ))` on an invertible module. The cohomological Chern character of a single finite locally free module, which Tag 0FI9's existence half constructs from the locally constant rank `r^A` and the Chern classes of Tag 0FI5 on all of `K₀` — neither available here, both resting on condition (2) of the situation, which `ChernSetup` does not transcribe — is a hypothesis, as is the pullback homomorphism of `K₀(Vect(-))`”.

> **The existence half of Stacks Tag 0FIE.** The cohomological Chern character of a single
> finite locally free module extends to a ring homomorphism
> `ch^H : K₀(Vect(X)) ⟶ ∏_{i ≥ 0} H^{2i}(X)(i)` for every object `X` of `𝒞`, which is graded,
> compatible with pullbacks, and takes the value `exp(c_1^H(ℒ))` on an invertible module.
>
> The extension is Tag 0FEM's universal property of the Grothendieck ring, applied to the given
> additive, multiplicative and unital assignment; the grading and the compatibility with pullbacks
> pass from the generators to all of `K₀(Vect(X))` because the graded series form a subgroup and
> because both sides of the pullback equation are additive.

```lean
theorem exists_cohomologicalChernCharacter
    (hκ : ∀ {X Y : C} (f : X ⟶ Y) (E : (S.obj Y).Modules),
      Stacks.FiniteLocallyFree.IsFiniteLocallyFree.{u, u, u} E →
        κ f (VectorBundleKZero.classOf (S.obj Y) E) =
          VectorBundleKZero.classOf (S.obj X) ((Scheme.Modules.pullback (S.map f)).obj E))
    (chM : ∀ X : C, (S.obj X).Modules → PowerSeries (𝔄.A X))
    (hzero : ∀ (X : C) (M : (S.obj X).Modules),
      ¬ Stacks.FiniteLocallyFree.IsFiniteLocallyFree.{u, u, u} M → chM X M = 0)
    (hadd : ∀ (X : C) {E F G : (S.obj X).Modules} (f : E ⟶ F) (g : F ⟶ G) (w : f ≫ g = 0),
      Stacks.FiniteLocallyFree.IsFiniteLocallyFree.{u, u, u} E →
        Stacks.FiniteLocallyFree.IsFiniteLocallyFree.{u, u, u} F →
          Stacks.FiniteLocallyFree.IsFiniteLocallyFree.{u, u, u} G →
            Mono f → Epi g → (ShortComplex.mk f g w).Exact →
              chM X F = chM X E + chM X G)
    (hmul : ∀ (X : C) (M N : (S.obj X).Modules),
      Stacks.FiniteLocallyFree.IsFiniteLocallyFree.{u, u, u} M →
        Stacks.FiniteLocallyFree.IsFiniteLocallyFree.{u, u, u} N →
          chM X (Scheme.Modules.tensorObjRingedSpace (S.obj X) M N) = chM X M * chM X N)
    (hone : ∀ X : C, chM X (SheafOfModules.unit (S.obj X).ringCatSheaf) = 1)
    (hgrade : ∀ (X : C) (M : (S.obj X).Modules), chM X M ∈ gradedPowerSeries 𝔄 X)
    (hinvM : ∀ (X : C) (L : (S.obj X).Modules)
      (hL : AlgebraicGeometry.SheafOfModules.IsInvertible (S.obj X).presheaf
        (S.obj X).ringCatSheaf.2 L),
      chM X L = expFirstChernClass 𝔄 X (picardClassOf (S.obj X) L hL))
    (hpullM : ∀ {X Y : C} (f : X ⟶ Y) (E : (S.obj Y).Modules),
      Stacks.FiniteLocallyFree.IsFiniteLocallyFree.{u, u, u} E →
        PowerSeries.map (𝔄.pull f) (chM Y E) =
          chM X ((Scheme.Modules.pullback (S.map f)).obj E))
    (hflf : ∀ {X Y : C} (f : X ⟶ Y) (E : (S.obj Y).Modules),
      Stacks.FiniteLocallyFree.IsFiniteLocallyFree.{u, u, u} E →
        Stacks.FiniteLocallyFree.IsFiniteLocallyFree.{u, u, u}
          ((Scheme.Modules.pullback (S.map f)).obj E)) :
    ∃ ch : ∀ X : C, VectorBundleKZero (S.obj X) →+* PowerSeries (𝔄.A X),
      (∀ (X : C) (M : (S.obj X).Modules),
          Stacks.FiniteLocallyFree.IsFiniteLocallyFree.{u, u, u} M →
          ch X (VectorBundleKZero.classOf (S.obj X) M) = chM X M) ∧
        (∀ (X : C) (α : VectorBundleKZero (S.obj X)), ch X α ∈ gradedPowerSeries 𝔄 X) ∧
          (∀ {X Y : C} (f : X ⟶ Y) (α : VectorBundleKZero (S.obj Y)),
            PowerSeries.map (𝔄.pull f) (ch Y α) = ch X (κ f α)) ∧
            ∀ (X : C) (L : (S.obj X).Modules)
              (hL : AlgebraicGeometry.SheafOfModules.IsInvertible (S.obj X).presheaf
                (S.obj X).ringCatSheaf.2 L),
              ch X (VectorBundleKZero.classOf (S.obj X) L) =
                expFirstChernClass 𝔄 X (picardClassOf (S.obj X) L hL)
```

**`Stacks.WeilCohomology.eq_of_cohomologicalChernCharacter'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/CohomologicalChernCharacterConstructed.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/CohomologicalChernCharacterConstructed.lean#L180). The attribute's comment: “uniqueness: two rules assigning to every object a ring homomorphism out of `K₀(Vect(X))`, compatible with pullbacks and taking the value `exp(c₁^H(ℒ))` on an invertible module, agree on every class and at every object. Every input is discharged here: compatibility with pullbacks is read against the CONSTRUCTED pullback homomorphism AlgebraicGeometry.VectorBundleKZero.pullbackRingHom of `K₀(Vect(-))`”.

> **The uniqueness half of Stacks Tag 0FIE.** Two rules assigning to every object `X` of `𝒞` a
> ring homomorphism `K₀(Vect(X)) ⟶ ∏_{i ≥ 0} H^{2i}(X)(i)`, compatible with pullbacks and taking
> the value `exp(c_1^H(ℒ))` on every invertible module, are equal: they agree on every class of
> `K₀(Vect(X))`, for every object `X` of `𝒞`.
>
> Both rules are additive, so it is enough that they agree on the classes `[ℰ]` of finite locally
> free modules, which generate `K₀(Vect(X))`. For `ℰ` of constant rank that is
> `eq_classOf_of_isFiniteLocallyFreeOfRank`, read off the splitting principle. An arbitrary `ℰ` is
> reduced to that case by `Stacks.WeilCohomology.SourceChernSetup.exists_clopenRankPieces`:
> restriction
> to the finitely many loci where the rank of `ℰ` is constant is injective on `A(X)` by condition
> (2) of the situation, and both rules commute with those restrictions.

```lean
theorem eq_of_cohomologicalChernCharacter'
    {ch ch' : ∀ X : C, VectorBundleKZero (S.obj X) →+* PowerSeries (𝔄.A X)}
    (hpull : ∀ {X Y : C} (f : X ⟶ Y) (α : VectorBundleKZero (S.obj Y)),
      PowerSeries.map (𝔄.pull f) (ch Y α) = ch X (VectorBundleKZero.pullbackRingHom (S.map f) α))
    (hpull' : ∀ {X Y : C} (f : X ⟶ Y) (α : VectorBundleKZero (S.obj Y)),
      PowerSeries.map (𝔄.pull f) (ch' Y α) = ch' X (VectorBundleKZero.pullbackRingHom (S.map f) α))
    (hinv : ∀ (X : C) (L : (S.obj X).Modules)
      (hL : AlgebraicGeometry.SheafOfModules.IsInvertible (S.obj X).presheaf
        (S.obj X).ringCatSheaf.2 L),
      ch X (VectorBundleKZero.classOf (S.obj X) L) =
        expFirstChernClass 𝔄.toChernSetup X (picardClassOf (S.obj X) L hL))
    (hinv' : ∀ (X : C) (L : (S.obj X).Modules)
      (hL : AlgebraicGeometry.SheafOfModules.IsInvertible (S.obj X).presheaf
        (S.obj X).ringCatSheaf.2 L),
      ch' X (VectorBundleKZero.classOf (S.obj X) L) =
        expFirstChernClass 𝔄.toChernSetup X (picardClassOf (S.obj X) L hL))
    (X : C) (α : VectorBundleKZero (S.obj X)) :
    ch X α = ch' X α
```

**`Stacks.WeilCohomology.exists_cohomologicalChernCharacter_of_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/CohomologicalChernCharacterConstructed.lean, line 527](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/CohomologicalChernCharacterConstructed.lean#L527). The attribute's comment: “existence: the rule, as a ring homomorphism out of `K₀(Vect(X))` into `∏_{i ≥ 0} H^{2i}(X)(i)`, together with its grading, its compatibility with the CONSTRUCTED pullback homomorphism AlgebraicGeometry.VectorBundleKZero.pullbackRingHom of `K₀(Vect(-))` and its value `exp(c₁^H(ℒ))` on an invertible module, stated over the data and the conditions of Sections 45.12 and 45.14 themselves and over NO structure argument. The standing situation is the structure Stacks.WeilCohomology.ChernSetup -- the data the source fixes, with clause (1), clause (2), clause (3)(a), condition (1), condition (2), condition (4) and the source's grading A(X) = sum of the A^i(X) as isInternal\_grade -- together with the section's three remaining conditions: condition (3) at f^*L itself, in the source's own form (PullbackFirstChernCondition); clause (3)(b) as the closure property IsBundleCompare at f^*E itself, in the source's own form (BundleCompareClause); clause (3)(c) as the closure property IsBundleEmbedding with condition (5) read at c\_1^A(O\_P(P')) for the divisor module characterized divisor-theoretically by IsSubbundleDivisorModule (DivisorDatumClause); and the Q-structure of A as data (D0) and (D1) of Section 45.14 read for A, that is Stacks.WeilCohomology.ChernSetup.IsRationallyGraded. The structure Stacks.WeilCohomology.ChernSituation is built inside the proof by Stacks.WeilCohomology.chernSituationOfSource and is not an argument, and no RationalChernSituation occurs. PROVED and not assumed: the cohomological Chern character of a single finite locally free module, which the source's proof cites from Tag 0FI9's existence half and which Stacks.WeilCohomology.exists\_cohomologicalChernCharacter leaves open as `chM` with seven properties, discharged here by Stacks.WeilCohomology.chernCharacterOfModule and its seven lemmas; the total Chern classes of Tag 0FI5 those rest on, at the constructed situation (ChernSituation.isTotalChernClass\_totalChernClass); the rank class `r^A`, which is Stacks.WeilCohomology.SourceChernSetup.rankClass, built from condition (2); the pullback homomorphism of K\_0(Vect(-)), which is AlgebraicGeometry.VectorBundleKZero.pullbackRingHom; the Whitney formula this half needs, proved from clause (3)(c) with condition (5); and the one-degree form of the Q-structure, the rationals lying in A^0(X), DERIVED from (D0) and (D1) by Stacks.WeilCohomology.ChernSetup.algebraMap\_mem\_grade\_zero\_of\_isRationallyGraded. Nothing outside the data and the conditions of Sections 45.12 and 45.14 is assumed, and NO hypothesis is read more strongly than the source states it: the invariance of the total Chern class under an isomorphism of modules, which K\_0(Vect(X)) forces on any rule out of it and which a comparison of P(E) with P(E') would get only by asking clause (3)(b) at every module isomorphic to f^*E, is PROVED (chernSeries\_eq\_of\_iso), as is the pseudofunctoriality coherence isomorphism h^*(g^*E) = (h . g)^*E (pull\_chernSeries\_coeff\_of\_iso)”.

> **Stacks Project, Tag 0FIE, existence half.** In the standing situation of Section 45.12,
> read with the `𝐐`-structure data (D0) and (D1) of Section 45.14 give, there is a rule assigning
> to every object `X` of `𝒞` a ring homomorphism
>
> `ch^H : K₀(Vect(X)) ⟶ ∏_{i ≥ 0} H^{2i}(X)(i)`
>
> which is graded, is compatible with pullbacks, and takes the value `exp(c_1^H(ℒ))` on every
> invertible module. With `Stacks.WeilCohomology.eq_of_cohomologicalChernCharacter'` for
> uniqueness this is the tag.
>
> **What the situation is.** `Stacks.WeilCohomology.ChernSetup` is the source's own standing
> situation — the data the source fixes, with clause (1), clause (2), clause (3)(a), condition
> (1), condition (2), condition (4) and the grading `A(X) = ⨁_{i ≥ 0} A^i(X)`; in particular
> `Stacks.WeilCohomology.ChernSetup.bundleDatum` is a definition and not a field. The section's
> three remaining conditions, each in the source's own form, are the arguments `hpull`,
> `hcompare` and `hdivisor` (`Stacks.WeilCohomology.PullbackFirstChernCondition`,
> `Stacks.WeilCohomology.BundleCompareClause`, `Stacks.WeilCohomology.DivisorDatumClause`), and
> the `𝐐`-structure is the `ℚ`-algebra structure on the `A X` together with
> `Stacks.WeilCohomology.ChernSetup.IsRationallyGraded`, which is data (D0) and (D1) of Section
> 45.14 read for `A`. The `Stacks.WeilCohomology.ChernSituation` the development is written over
> is assembled from those three by `Stacks.WeilCohomology.chernSituationOfSource` inside the
> proof, so it is not an argument of this statement, and no
> `Stacks.WeilCohomology.RationalChernSituation` occurs: condition (5), together with clause
> (3)(c), is the argument `hdivisor` rather than a field, and the one-degree form of the
> `𝐐`-structure is derived by
> `Stacks.WeilCohomology.ChernSetup.algebraMap_mem_grade_zero_of_isRationallyGraded`.
>
> **All three conditions are in the source's own form.** In particular
> `Stacks.WeilCohomology.BundleCompareClause` is clause (3)(b) at `f^*ℰ` itself, and not at every
> `ℰ'` carrying an isomorphism `f^*ℰ ≅ ℰ'` — that reading would be a closure property clauses (1),
> (2) and (3) do not give, since at `f = 𝟙 X` it is the closure of `𝒞` under the `𝐏(ℰ') ⟶ 𝐏(ℰ)`
> induced by an arbitrary `ℰ ≅ ℰ'`. The invariance of the total Chern class under an isomorphism of
> modules, which `K₀(Vect(X))` forces on any rule out of it, and the pseudofunctoriality coherence
> isomorphism `h^*(g^*ℰ) ≅ (h ∘ g)^*ℰ`, which the source has for free, are both theorems:
> `Stacks.WeilCohomology.ChernSituation.chernSeries_eq_of_iso` and
> `Stacks.WeilCohomology.ChernSituation.pull_chernSeries_coeff_of_iso`.
>
> Nothing is assumed beyond that data and those conditions. The
> cohomological Chern character of
> a single finite locally free module, which the source's proof of this tag cites from the
> existence half of Tag 0FI9 and which
> `Stacks.WeilCohomology.exists_cohomologicalChernCharacter` leaves open as `chM` with seven
> properties, is `Stacks.WeilCohomology.chernCharacterOfModule` with its seven lemmas; the total
> Chern classes of Tag 0FI5 those rest on are
> `Stacks.WeilCohomology.ChernSituation.isTotalChernClass_totalChernClass` at the constructed
> situation; the rank class `r^A` is `Stacks.WeilCohomology.SourceChernSetup.rankClass`, built from
> condition (2); and the pullback homomorphism of `K₀(Vect(-))` is
> `AlgebraicGeometry.VectorBundleKZero.pullbackRingHom`.

```lean
theorem exists_cohomologicalChernCharacter_of_source (𝔄 : SourceChernSetup.{u, v, v₁, w} C S)
    [∀ X : C, Algebra ℚ (𝔄.A X)] (hgr : 𝔄.IsRationallyGraded)
    (hpull : PullbackFirstChernCondition 𝔄) (hcompare : BundleCompareClause 𝔄)
    (hdivisor : DivisorDatumClause 𝔄) :
    ∃ ch : ∀ X : C, VectorBundleKZero (S.obj X) →+* PowerSeries (𝔄.A X),
      (∀ (X : C) (M : (S.obj X).Modules),
          Stacks.FiniteLocallyFree.IsFiniteLocallyFree.{u, u, u} M →
          ch X (VectorBundleKZero.classOf (S.obj X) M) =
            chernCharacterOfModule (𝔄 := 𝔄) (chernSituationOfSource 𝔄 hpull hcompare
              hdivisor).isTotalChernClass_totalChernClass X M) ∧
        (∀ (X : C) (α : VectorBundleKZero (S.obj X)), ch X α ∈ gradedPowerSeries 𝔄.toChernSetup X) ∧
          (∀ {X Y : C} (f : X ⟶ Y) (α : VectorBundleKZero (S.obj Y)),
            PowerSeries.map (𝔄.pull f) (ch Y α) =
              ch X (VectorBundleKZero.pullbackRingHom (S.map f) α)) ∧
            ∀ (X : C) (L : (S.obj X).Modules)
              (hL : AlgebraicGeometry.SheafOfModules.IsInvertible (S.obj X).presheaf
                (S.obj X).ringCatSheaf.2 L),
              ch X (VectorBundleKZero.classOf (S.obj X) L) =
                expFirstChernClass 𝔄.toChernSetup X (picardClassOf (S.obj X) L hL)
```

**`Stacks.WeilCohomology.FirstChernClassData.existsUnique_cohomologicalChernCharacter`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/WeilChernCharacter.lean, line 334](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/WeilChernCharacter.lean#L334). The attribute's comment: “under exactly (D0), (D1), (D2') and (A1)-(A4), for all smooth projective schemes over k (not necessarily irreducible or nonempty), with the tensor-defined Tate twists: existence and uniqueness of the rule K\_0(Vect(X)) -> prod\_\{i >= 0} H^\{2i}(X)(i), a ring homomorphism for the cup product of the product. (D1) is Z-graded as in the chapter's conventions; the proof uses condition (4) of Section 45.12 only through injectivity and the resolution of the top power, which is what (A3) gives on A when H^* has negative-degree classes”.

> **Stacks Project, Tag 0FIE.** Assume given data (D0), (D1), (D2') satisfying axioms (A1),
> (A2), (A3) and (A4). There is a unique rule which assigns to every smooth projective `X` over `k`
> a ring homomorphism
>
> `ch^H : K₀(Vect(X)) ⟶ ∏_{i ≥ 0} H^{2i}(X)(i)`
>
> compatible with pullbacks such that `ch^H(ℒ) = exp(c₁^H(ℒ))` for every invertible
> `𝒪_X`-module `ℒ`.
>
> The twists are the tensor-defined ones, `Stacks.WeilCohomology.tateTwist`. A family
> `(a_i)_{i ≥ 0}` with `a_i ∈ H^*(X)(i)` lies in `∏_{i ≥ 0} H^{2i}(X)(i)` when each `a_i` lies in the
> image of `H^{2i}(X)(i)`. The ring structure of the product is the cup product
> `Stacks.WeilCohomology.FirstChernClassData.cupConv`, `(a ∪ b)_n = ∑_{i + j = n} a_i ∪ b_j`, with
> unit `Stacks.WeilCohomology.FirstChernClassData.oneConv`; a ring homomorphism is an additive,
> multiplicative and unital map. Compatibility with pullbacks is `f^* ∘ ch^H = ch^H ∘ f^*`, the
> pullback of `K₀(Vect(-))` being `AlgebraicGeometry.VectorBundleKZero.pullbackRingHom`, and
> `exp(c₁^H(ℒ)) = ∑_n (1/n!) c₁^H(ℒ)^n` is `Stacks.WeilCohomology.FirstChernClassData.expTw`.
>
> The proof is the source's: Proposition 45.12.4 (Tag 0FI9) for the category of smooth projective
> schemes over `k`, the functor `A : X ↦ ⨁_{i ≥ 0} H^{2i}(X)(i)` and `c₁^H`, whose standing
> assumptions are (A1)–(A4). The projective bundle formula is used in the weak form that (A3)
> provides when `H^*` is nonzero in negative degrees; see the module documentation.

```lean
theorem existsUnique_cohomologicalChernCharacter [CharZero F] (hA1 : 𝔇.CoproductAxiom)
    (hA2 : 𝔇.PullbackAxiom) (hA3 : 𝔇.ProjectiveBundleAxiom) (hA4 : 𝔇.DivisorAxiom) :
    ∃! ch : ∀ X : (SmoothProjectiveScheme k).FullSubcategory,
        VectorBundleKZero ((toScheme k).obj X) → ∀ n : ℕ, tateTwist F 𝔇.tate (𝔇.H X) n,
      (∀ X α (n : ℕ), ch X α n ∈
          LinearMap.range (tateTwistMap (L := 𝔇.tate) (𝔇.grade X (2 * (n : ℤ))).subtype n)) ∧
        (∀ X α β, ch X (α + β) = ch X α + ch X β) ∧
        (∀ X α β, ch X (α * β) = 𝔇.cupConv X (ch X α) (ch X β)) ∧
        (∀ X, ch X 1 = 𝔇.oneConv X) ∧
        (∀ {X Y : (SmoothProjectiveScheme k).FullSubcategory} (f : X ⟶ Y) α (n : ℕ),
          ch X (VectorBundleKZero.pullbackRingHom ((toScheme k).map f) α) n =
            𝔇.pullTw f n (ch Y α n)) ∧
          ∀ X (L : ((toScheme k).obj X).Modules)
            (hL : AlgebraicGeometry.SheafOfModules.IsInvertible ((toScheme k).obj X).presheaf
              ((toScheme k).obj X).ringCatSheaf.2 L),
            ch X (VectorBundleKZero.classOf _ L) = 𝔇.expTw X (𝔇.c₁ X (picardClassOf _ L hL))
```

## Tag 0FIF, a lemma

[Tag 0FIF](https://stacks.math.columbia.edu/tag/0FIF) in the Stacks Project.

**`Stacks.WeilCohomology.FirstChernClassData.existsUnique_codimensionCycleClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClassCycleClassIntegral.lean, line 302](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClassCycleClassIntegral.lean#L302). The attribute's comment: “the integral form: existence and uniqueness, under exactly (D0), (D1), (D2') and (A1)-(A4), of γ on the integral Chow groups CH^i(X) = prod\_d CH\_\{d-i}(X\_d) of every smooth projective X over k, with values in H^\{2i}(X)(i), additive, multiplicative for the intersection product of 0FC0 and the cup product, γ([X]) = 1, compatible with the codimension-graded Gysin pullbacks f^! of 0FF3, and with γ(ch(α)) = ch^H(α) read through CH -> CH ⊗ Q (the Q-linear extension of γ sends ch(α) ∩ [X] to ch^H(α), ch^H as in 0FIE). Derived from the rational form existsUnique\_cycleClassMap; nothing is assumed”.

> **Stacks Project, Tag 0FIF, on the integral Chow ring.** Assume given (D0), (D1), (D2')
> satisfying axioms (A1), (A2), (A3) and (A4). There is a unique rule which assigns to every smooth
> projective `X` over `k` a graded ring homomorphism
>
>   `γ : CH^*(X) ⟶ ⨁_{i ≥ 0} H^{2i}(X)(i)`
>
> compatible with pullbacks such that `γ(ch(α)) = ch^H(α)` for `α ∈ K₀(Vect(X))`.
>
> `CH^*(X) = ⨁_i CH^i(X)` is the integral Chow ring, `CH^i(X) = ∏_d CH_{d-i}(X_d)` with the
> intersection product of Chow Homology, Section 0FC0, and unit the fundamental class `[X]`;
> pullback is the Gysin map `f^!` of Chow Homology, Tag 0FF3, graded by codimension. A graded ring
> homomorphism is given by its components `γ : CH^i(X) ⟶ H^{2i}(X)(i)`: additive, multiplicative
> for the cup product, and sending `[X]` to `1`. The equation `γ(ch(α)) = ch^H(α)` involves the
> rational class `ch(α) ∩ [X] ∈ CH^*(X) ⊗ 𝐐` and is read through `CH^*(X) ⟶ CH^*(X) ⊗ 𝐐`: the
> `𝐐`-linear extension `γ_𝐐` of `γ` to `CH^*(X) ⊗ 𝐐` (an additive map agreeing with `γ` on the
> integral classes) satisfies `γ_𝐐(ch(α) ∩ [X]) = ch^H(α)`, `ch^H` being the cohomological Chern
> character of Tag 0FIE.

```lean
theorem existsUnique_codimensionCycleClass (hA1 : 𝔇.CoproductAxiom) (hA2 : 𝔇.PullbackAxiom)
    (hA3 : 𝔇.ProjectiveBundleAxiom) (hA4 : 𝔇.DivisorAxiom) :
    ∃! γ : ∀ (X : (SmoothProjectiveScheme k).FullSubcategory) (i : ℕ),
        codimensionChowGroup k X.obj.hom i →+ tateTwist F 𝔇.tate (𝔇.H X) i,
      (∀ (X : (SmoothProjectiveScheme k).FullSubcategory) (i : ℕ)
          (a : codimensionChowGroup k X.obj.hom i),
        γ X i a ∈
          LinearMap.range (tateTwistMap (L := 𝔇.tate) (𝔇.grade X (2 * (i : ℤ))).subtype i)) ∧
      (∀ (X : (SmoothProjectiveScheme k).FullSubcategory) (i j : ℕ)
          (a : codimensionChowGroup k X.obj.hom i)
        (b : codimensionChowGroup k X.obj.hom j),
        γ X (i + j) (codimensionIntersectionProduct k X.obj.hom i j a b) =
          tateCup 𝔇.finrank_tate (𝔇.cup X) i j (i + j) (by ring) (γ X i a)
            (γ X j b)) ∧
      (∀ X : (SmoothProjectiveScheme k).FullSubcategory, γ X 0 (fundamentalClass X) = 𝔇.unitTw X) ∧
      (∀ {X Y : (SmoothProjectiveScheme k).FullSubcategory} (f : X ⟶ Y) (i : ℕ)
        (b : codimensionChowGroup k Y.obj.hom i),
        γ X i (codimensionGysin X.obj.hom Y.obj.hom (w f) i b) = 𝔇.pullTw f i (γ Y i b)) ∧
      ∀ ch : ∀ X : (SmoothProjectiveScheme k).FullSubcategory,
          VectorBundleKZero ((toScheme k).obj X) → ∀ n : ℕ, tateTwist F 𝔇.tate (𝔇.H X) n,
        𝔇.IsCohomologicalChernCharacter ch →
        ∃ γℚ : ∀ X : (SmoothProjectiveScheme k).FullSubcategory,
            smoothRationalChowRing (k := k) X.obj.hom → ∀ n : ℕ, tateTwist F 𝔇.tate (𝔇.H X) n,
          (∀ (X : (SmoothProjectiveScheme k).FullSubcategory)
              (α β : smoothRationalChowRing (k := k) X.obj.hom),
            γℚ X (α + β) = γℚ X α + γℚ X β) ∧
          (∀ (X : (SmoothProjectiveScheme k).FullSubcategory) (i : ℕ)
              (a : codimensionChowGroup k X.obj.hom i),
            γℚ X (smoothChowEquiv X.obj.hom (codimensionToRationalChow k X.obj.hom i a)) i =
              γ X i a ∧
            ∀ n : ℕ, n ≠ i →
              γℚ X (smoothChowEquiv X.obj.hom (codimensionToRationalChow k X.obj.hom i a)) n =
                0) ∧
          ∀ (X : (SmoothProjectiveScheme k).FullSubcategory)
              (a : VectorBundleKZero ((toScheme k).obj X)),
            γℚ X (rationalChernCharacterAlgEquiv (isRegular_of_smooth_over_field X.obj.hom)
              (exists_bounds_relativeDimension_fieldChowSituation k X.obj.hom) (1 ⊗ₜ[ℤ] a)) =
              ch X a
```

**`Stacks.WeilCohomology.FirstChernClassData.existsUnique_cycleClassMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClassCycleClassMap.lean, line 335](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClassCycleClassMap.lean#L335). The attribute's comment: “existence and uniqueness, under exactly (D0), (D1), (D2') and (A1)-(A4) (FirstChernClassData with its four axioms), for all smooth projective X over k: γ on CH^*(X) ⊗ Q (the actual rational Chow group of X with the intersection product of Chow Homology, Section 0FEX, and its codimension grading) is graded, additive, multiplicative and unital for the cup product of prod\_i H^\{2i}(X)(i), compatible with the actual Gysin pullbacks f^!, and γ(ch(α) ∩ [X]) = ch^H(α) for every α in K\_0(Vect(X)) and the ch^H of Tag 0FIE. The source prints the last equation as ch^H(α) = γ(ch(α)), which typechecks only after capping with [X], and takes γ on CH^*(X); its proof defines γ on CH^*(X) ⊗ Q, where the equation lives, and so does this statement. 0FEY, 0FEM, 0FF8, 0FEN, 0FEX and 0FIA are proved, not assumed”.

> **Stacks Project, Tag 0FIF.** Assume given (D0), (D1), (D2') satisfying axioms (A1), (A2),
> (A3) and (A4). There is a unique rule which assigns to every smooth projective `X` over `k` a
> graded ring homomorphism
>
>   `γ : CH^*(X) ⊗ 𝐐 ⟶ ⨁_{i ≥ 0} H^{2i}(X)(i)`
>
> compatible with pullbacks such that `γ(ch(α) ∩ [X]) = ch^H(α)` for `α ∈ K₀(Vect(X))`, `ch^H` being
> the cohomological Chern character of Tag 0FIE.
>
> `CH^*(X) ⊗ 𝐐` is `CH_*(X) ⊗ 𝐐` with the intersection product of Chow Homology, Section 0FEX, and
> its codimension grading; pullback is the Gysin map `f^!` of Chow Homology, Tag 0FF3; `ch(α) ∩ [X]`
> is the isomorphism of Chow Homology, Tags 0FEY and 0FEM. A value of `γ` is a family
> `(γ(α)_n)_{n ≥ 0}`, `γ(α)_n ∈ H^*(X)(n)`; graded means that a class of codimension `i` has
> `γ(α)_i ∈ H^{2i}(X)(i)` and all other components zero (so `γ(α) ∈ ⨁_{i ≥ 0} H^{2i}(X)(i)`), and
> the ring structure of the target is the cup product `cupConv` with unit `oneConv`, as in Tag 0FIE.
> The rule `ch^H` is quantified over: Tag 0FIE says exactly one rule has its properties.

```lean
theorem existsUnique_cycleClassMap (hA1 : 𝔇.CoproductAxiom) (hA2 : 𝔇.PullbackAxiom)
    (hA3 : 𝔇.ProjectiveBundleAxiom) (hA4 : 𝔇.DivisorAxiom) :
    ∃! γ : ∀ X : (SmoothProjectiveScheme k).FullSubcategory,
        smoothRationalChowRing (k := k) X.obj.hom → ∀ n : ℕ, tateTwist F 𝔇.tate (𝔇.H X) n,
      (∀ (X : (SmoothProjectiveScheme k).FullSubcategory) (i : ℕ)
          (α : smoothRationalChowRing (k := k) X.obj.hom),
        (smoothChowEquiv X.obj.hom).symm α ∈
            codimensionChowSubmodule (fieldChowSituation k) X.obj.hom i →
          γ X α i ∈
              LinearMap.range (tateTwistMap (L := 𝔇.tate) (𝔇.grade X (2 * (i : ℤ))).subtype i) ∧
            ∀ n : ℕ, n ≠ i → γ X α n = 0) ∧
      (∀ (X : (SmoothProjectiveScheme k).FullSubcategory)
          (α β : smoothRationalChowRing (k := k) X.obj.hom),
        γ X (α + β) = γ X α + γ X β) ∧
      (∀ (X : (SmoothProjectiveScheme k).FullSubcategory)
          (α β : smoothRationalChowRing (k := k) X.obj.hom),
        γ X (α * β) = 𝔇.cupConv X (γ X α) (γ X β)) ∧
      (∀ (X : (SmoothProjectiveScheme k).FullSubcategory), γ X 1 = 𝔇.oneConv X) ∧
      (∀ {X Y : (SmoothProjectiveScheme k).FullSubcategory} (f : X ⟶ Y)
          (α : smoothRationalChowRing (k := k) Y.obj.hom) (n : ℕ),
        γ X (smoothGysinRingHom X.obj.hom Y.obj.hom (w f) α) n = 𝔇.pullTw f n (γ Y α n)) ∧
      ∀ ch : ∀ X : (SmoothProjectiveScheme k).FullSubcategory,
          VectorBundleKZero ((toScheme k).obj X) → ∀ n : ℕ, tateTwist F 𝔇.tate (𝔇.H X) n,
        𝔇.IsCohomologicalChernCharacter ch → ∀ (X : (SmoothProjectiveScheme k).FullSubcategory)
          (a : VectorBundleKZero ((toScheme k).obj X)),
          γ X (rationalChernCharacterAlgEquiv (isRegular_of_smooth_over_field X.obj.hom)
            (exists_bounds_relativeDimension_fieldChowSituation k X.obj.hom) (1 ⊗ₜ[ℤ] a)) =
            ch X a
```

**`Stacks.WeilCohomology.CycleClassSetup.isCycleClassRule_cycleClassMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/CycleClassMap.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/CycleClassMap.lean#L204). The attribute's comment: “existence: the rule, constructed rather than chosen, together with its three properties — graded, compatible with pullbacks, and `γ(ch(α) ∩ [X]) = ch^H(α)`. The source prints that equation as `ch^H(α) = γ(ch(α))`, which typechecks only after capping with `[X]`; the form proved is the one the source's own proof defines, and `γ` is correspondingly taken on `CH^*(X) ⊗ ℚ`, where the equation lives. Tag 0FIE (`ch^H`), Tags 0FEY and 0FEM (the ring isomorphism `K₀(Vect(X)) ⊗ ℚ ≅ CH^*(X) ⊗ ℚ`), Tag 0FEJ (`ψ²`) and Tags 0FEX and 0FIA (the two eigenvalue statements) are hypotheses, carried by `CycleClassSetup`”.

> **The existence half of Stacks Tag 0FIF.** The transported cohomological Chern character is
> graded, compatible with pullbacks, and satisfies `γ(ch(α) ∩ [X]) = ch^H(α)`.
>
> The grading is the source's Adams operator argument: a class of codimension `i` answers to a
> `2^i`-eigenvector of `ψ²`, whose cohomological Chern character lies in `H^{2i}(X)(i)` by Tag
> 0FIA. Compatibility with pullbacks is that of `ch^H` and of the Chern character isomorphism, the
> latter transported through its inverse. The defining equation holds by construction.

```lean
theorem isCycleClassRule_cycleClassMap : IsCycleClassRule S S.cycleClassMap
```

**`Stacks.WeilCohomology.eq_of_isCycleClassRule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/CycleClassMap.lean, line 224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/CycleClassMap.lean#L224). The attribute's comment: “uniqueness: the defining equation `γ(ch(α) ∩ [X]) = ch^H(α)` alone determines the rule, the Chern character isomorphism of Tags 0FEY and 0FEM being surjective. As in the existence half the equation is the corrected form of the source's `ch^H(α) = γ(ch(α))` and `γ` is taken on `CH^*(X) ⊗ ℚ`”.

> **The uniqueness half of Stacks Tag 0FIF.** Two rules with the three properties are equal.
>
> Only the defining equation is used: the Chern character isomorphism of Tags 0FEY and 0FEM is
> surjective, so a rule is determined by its values on the classes `ch(α) ∩ [X]`.

```lean
theorem eq_of_isCycleClassRule {S : CycleClassSetup.{v, v₁, w} C}
    {γ γ' : ∀ X : C, S.CH X →+* S.A X} (h : IsCycleClassRule S γ) (h' : IsCycleClassRule S γ') :
    γ = γ'
```

## Tag 0FIH, a lemma

[Tag 0FIH](https://stacks.math.columbia.edu/tag/0FIH) in the Stacks Project.

**`Stacks.WeilCohomology.SmoothProjectiveScheme.exists_blowup_relations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/BlowupRelationGeneral.lean, line 856](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/BlowupRelationGeneral.lean#L856).

> **Lemma 0FIH.** Let `b : X' ⟶ X` be the blowing up of a smooth projective scheme `X` over `k`
> (not necessarily equidimensional) in a smooth closed subscheme `i : Z ⟶ X`, with exceptional
> divisor `j : E ⟶ X'` and `π : E ⟶ Z`. Assume that some element of `K_0(Vect(X))` restricts on
> `Z` to the class of `𝒞_{Z/X}`, and that every irreducible component of `Z` has codimension
> `r ≥ 1` in `X` (its generic point has coheight `r` in `X`). Then there is a cycle
> `θ ∈ CH^{r-1}(X')` such that
>
> * `b^![Z] = [E] · θ` in `CH^r(X')`, with `b^!` the Gysin map of Stacks 0FF3 and `·` the
>   intersection product of Stacks 0FC0, both graded by codimension; and
> * `π_*(j^!θ) = [Z]`: for every `e`, on the part `X'_{e+1}` of `X'` of dimension `e + 1` the
>   Gysin map of the regular immersion `j` (`Stacks.Chow.regularImmersionPartGysin`) carries `θ`
>   to a class of `CH_{e-(r-1)}(E ×_{X'} X'_{e+1})` whose pushforward to `Z` is the fundamental
>   class `[Z]_{e-(r-1)}`, the sum of the components of `Z` of dimension `e - (r - 1)`.
>
> Since `CH_*(E)` is the direct sum of the `CH_*(E ×_{X'} X'_d)`, the piece over `X'_0` is empty,
> and `[Z] = ∑_m [Z]_m`, the second family of equalities is `π_*(j^!θ) = [Z]` in
> `CH_*(Z) = ⊕_m CH_m(Z)`. The source writes `[Z] ∈ CH^r(Z)`; as `π_*j^!θ` has codimension `0` in
> `Z`, this is the fundamental class `[Z] ∈ CH^0(Z)`. The hypothesis `r ≥ 1` is implicit in the
> source (`θ ∈ CH^{r-1}(X')`): for `r = 0` and `Z` nonempty, `Z` is a union of components of `X`,
> `E` is empty and `π_*(j^!θ) = 0 ≠ [Z]`.
>
> The cycle is `θ = c_{r-1}(b^*α^∨ - [𝒪_{X'}(E)]) ∩ [X']`
> (`Stacks.WeilCohomology.SmoothProjectiveScheme.blowupTheta`), as in the source.

```lean
theorem exists_blowup_relations {r : ℕ} (hr0 : 0 < r)
    (hr : ∀ z : Z.obj.left, closure ({z} : Set Z.obj.left) ∈ irreducibleComponents Z.obj.left →
      Order.coheight (i.hom.left z) = r)
    (hK : ∃ α : VectorBundleKZero X.obj.left,
      VectorBundleKZero.pullback i.hom.left α = classOf _ (centreConormal i)) :
    ∃ θ : codimensionChowGroup k (blowupObj i).obj.hom ((r - 1 : ℕ) : ℤ),
      codimensionGysin (blowupObj i).obj.hom X.obj.hom (Over.w (blowupHom i).hom) (r : ℤ)
          (closedSubschemeClass X.obj.hom i.hom.left (r : ℤ)) ≍
        codimensionIntersectionProduct k (blowupObj i).obj.hom 1 ((r - 1 : ℕ) : ℤ)
          (closedSubschemeClass (blowupObj i).obj.hom (exceptionalHom i).hom.left 1) θ ∧
      ∀ e : ℕ, properChowPushforward (fieldChowSituation k)
          (pullback.fst (exceptionalHom i).hom.left (dimPart (blowupObj i).obj.hom (e + 1)).ι ≫
            (exceptionalHom i).hom.left ≫ (blowupObj i).obj.hom)
          Z.obj.hom
          (pullback.fst (exceptionalHom i).hom.left (dimPart (blowupObj i).obj.hom (e + 1)).ι ≫
            (exceptionalProj i).hom.left)
          (by rw [Category.assoc, Over.w (exceptionalProj i).hom, Over.w (exceptionalHom i).hom])
          ((e : ℤ) - ((r - 1 : ℕ) : ℤ))
          (properPushforwardFactorsThroughRationalEquivalence_of_isProper _ _ _ _ _ _)
          (regularImmersionPartGysin (blowupObj i).obj.hom (exceptionalHom i).hom.left
            (isRegularImmersion_of_isClosedImmersion (exceptionalHom i)) e (e + 1)
            ((r - 1 : ℕ) : ℤ) (θ (e + 1))) =
        fundamentalChowClass (fieldChowSituation k) Z.obj.hom ((e : ℤ) - ((r - 1 : ℕ) : ℤ))
```

## Tag 0FII, a lemma

[Tag 0FII](https://stacks.math.columbia.edu/tag/0FII) in the Stacks Project.

**`Stacks.WeilCohomology.FirstChernClassData.IsCohomologicalChernCharacter.cup_codimensionCycleClass_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CycleClassCupVanishingGeneral.lean, line 370](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CycleClassCupVanishingGeneral.lean#L370). The attribute's comment: “for any smooth projective X and smooth closed Z all of whose irreducible components have codimension r, with [C\_\{Z/X}] restricted from K\_0(X): a|\_Z = 0 implies γ([Z]) ∪ a = 0, γ the cycle class map of 0FIF; the case r = 0 by (A1)”.

> **Stacks Project, Lemma 0FII.** Let (D0), (D1), (D2') satisfy (A1)–(A4) and (A7), with `γ` the
> cycle class map of Tag 0FIF. Let `X` be a smooth projective scheme over `k` and `i : Z ⟶ X` a
> smooth closed subscheme every irreducible component of which has codimension `r` in `X`, such that
> the class of `𝒞_{Z/X}` in `K_0(Z)` is the restriction of an element of `K_0(X)`. If `a ∈ H^*(X)`
> restricts to `0` on `Z`, then `γ([Z]) ∪ a = 0`, written `a ∪ γ([Z])` with `γ([Z])` twisted.
>
> "Every irreducible component of `Z` has codimension `r`" is read at the generic points of the
> components: the codimension in `X` of the closure of the image of such a point is its coheight.
> For `r ≥ 1` the proof is the source's, on each part of `X` of constant dimension
> (`mul_κ_codimensionCycleClass_eq_zero_of_pos`). For `r = 0` the source's argument does not
> apply, `Z` not being nowhere dense; there `Z` is open and closed
> (`isOpenImmersion_of_coheight_eq_zero`) and (A1) gives the vanishing directly
> (`cup_codimensionCycleClass_eq_zero_of_isOpenImmersion`).

```lean
theorem cup_codimensionCycleClass_eq_zero (hA1 : 𝔇.CoproductAxiom)
    (hA3 : 𝔇.ProjectiveBundleAxiom) (hA4 : 𝔇.DivisorAxiom) (hA7 : 𝔇.BlowupAxiom)
    {Z X : (SmoothProjectiveScheme k).FullSubcategory} (i : Z ⟶ X) [IsClosedImmersion i.hom.left]
    (r : ℕ)
    (hr : ∀ z : Z.obj.left, closure ({z} : Set Z.obj.left) ∈ irreducibleComponents Z.obj.left →
      Order.coheight (i.hom.left z) = r)
    (hK : ∃ α : VectorBundleKZero X.obj.left,
      VectorBundleKZero.pullback i.hom.left α = VectorBundleKZero.classOf _ (centreConormal i))
    (a : 𝔇.H X) (ha : 𝔇.pull i a = 0) :
    tateCupLeft (𝔇.cup X) (r : ℤ) a
      (h.codimensionCycleClass X r (closedSubschemeClass X.obj.hom i.hom.left r)) = 0
```

**`Stacks.WeilCohomology.FirstChernClassData.IsCohomologicalChernCharacter.codimensionCycleClass_cup_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CycleClassCupVanishingGeneral.lean, line 394](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CycleClassCupVanishingGeneral.lean#L394). The attribute's comment: “in the source's order γ([Z]) ∪ a = 0, for any smooth projective X and smooth closed Z all of whose irreducible components have codimension r, with [C\_\{Z/X}] restricted from K\_0(X), and a|\_Z = 0; γ the cycle class map of 0FIF”.

> **Stacks Project, Lemma 0FII, in the source's order: `γ([Z]) ∪ a = 0`.** Here `γ([Z]) ∪ a` is
> the cup product with the twisted class on the left, `tateCupLeft` of the flipped cup product. It
> follows from `cup_codimensionCycleClass_eq_zero` by graded commutativity of `H^*(X)`, `γ([Z])`
> having even degree `2r`.

```lean
theorem codimensionCycleClass_cup_eq_zero (hA1 : 𝔇.CoproductAxiom)
    (hA3 : 𝔇.ProjectiveBundleAxiom) (hA4 : 𝔇.DivisorAxiom) (hA7 : 𝔇.BlowupAxiom)
    {Z X : (SmoothProjectiveScheme k).FullSubcategory} (i : Z ⟶ X) [IsClosedImmersion i.hom.left]
    (r : ℕ)
    (hr : ∀ z : Z.obj.left, closure ({z} : Set Z.obj.left) ∈ irreducibleComponents Z.obj.left →
      Order.coheight (i.hom.left z) = r)
    (hK : ∃ α : VectorBundleKZero X.obj.left,
      VectorBundleKZero.pullback i.hom.left α = VectorBundleKZero.classOf _ (centreConormal i))
    (a : 𝔇.H X) (ha : 𝔇.pull i a = 0) :
    tateCupLeft (𝔇.cup X).flip (r : ℤ) a
      (h.codimensionCycleClass X r (closedSubschemeClass X.obj.hom i.hom.left r)) = 0
```

## Tag 0FIJ, a lemma

[Tag 0FIJ](https://stacks.math.columbia.edu/tag/0FIJ) in the Stacks Project.

**`Stacks.WeilCohomology.FirstChernClassData.IsCohomologicalChernCharacter.poincareDuality_toWeilData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/PoincareDualityWeilThree.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/PoincareDualityWeilThree.lean#L127). The attribute's comment: “axiom (A) for the data of (A1)-(A7), with trace map λ of (A6) and γ the cycle class map of 0FIF”.

> **Stacks Project, Lemma 0FIJ.** Let (D0), (D1), (D2') satisfy axioms (A1)–(A7). Then axiom
> (A) of Section 0FHA holds with `∫_X = λ` as in axiom (A6): for `X` nonempty and equidimensional
> of dimension `d`, `H^i(X)` is finite dimensional and `H^i(X) × H^{2d-i}(X)(d) ⟶ F`,
> `(a, b) ↦ λ(a ∪ b)`, is a perfect pairing.

```lean
theorem poincareDuality_toWeilData : (h.toWeilData hA1 hA3 hA5 hA6).PoincareDuality
```

## Tag 0FIK, a remark

[Tag 0FIK](https://stacks.math.columbia.edu/tag/0FIK) in the Stacks Project.

**`Stacks.WeilCohomology.FirstChernClassData.IsCohomologicalChernCharacter.perfectDuality_diagonalClass_and_existsUnique_trace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/TraceUniqueness.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/TraceUniqueness.lean#L244). The attribute's comment: “for X nonempty smooth projective equidimensional of dimension d and data satisfying (A1)-(A7): γ([Δ]) defines a perfect duality between H^i(X) and H^\{2d-i}(X)(d) for all i (both finite dimensional, contraction (H^\{2d-i}(X)(d))^* → H^i(X) bijective), and the trace map λ of (A6) is unique”.

> **Stacks Project, Remark 0FIK: uniqueness of trace maps.** Let (D0), (D1), (D2') satisfy
> (A1)–(A7), with `γ` the cycle class map of Tag 0FIF, and let `X` be a nonempty smooth projective
> scheme over `k`, equidimensional of dimension `d`. Then:
>
> * `γ([Δ]) ∈ ⨁_i H^i(X) ⊗ H^{2d-i}(X)(d)` defines a perfect duality between `H^i(X)` and
>   `H^{2d-i}(X)(d)` for all `i`: both are finite dimensional, and contraction against the
>   `(i, 2d-i)` Künneth component of `γ([Δ])`, `μ ↦ (1 ⊗ μ)γ([Δ])_{i,2d-i}`, is a bijection
>   `(H^{2d-i}(X)(d))^* ⟶ H^i(X)`;
> * the linear map `∫_X = λ : H^{2d}(X)(d) ⟶ F` of axiom (A6), normalised by
>   `(1 ⊗ λ)γ([Δ]) = 1`, exists and is unique.
>
> The proof is the remark's: the left-dual structure of Lemma 0FIJ, through the identity
> `γ([Δ]) ∪ p₁^*a = γ([Δ]) ∪ p₂^*a` (`key_diagonalClass`), and the linear algebra of Tag 0FFV
> (`...Concrete.DiagonalExpansion`). Axiom (A2) enters only through `γ`.

```lean
theorem perfectDuality_diagonalClass_and_existsUnique_trace (hA1 : 𝔇.CoproductAxiom)
    (hA3 : 𝔇.ProjectiveBundleAxiom) (hA4 : 𝔇.DivisorAxiom) (hA5 : 𝔇.KunnethAxiom)
    (hA6 : 𝔇.TraceAxiomFor hA5 h.codimensionCycleClass) (hA7 : 𝔇.BlowupAxiom)
    (X : (SmoothProjectiveScheme k).FullSubcategory) (d : ℕ)
    (hX : IsNonemptyEquidimensional X d) :
    (∀ i j : ℤ, i + j = 2 * (d : ℤ) →
      FiniteDimensional F (𝔇.grade X i) ∧
        FiniteDimensional F (tateTwist F 𝔇.tate (𝔇.grade X j) d) ∧
        Function.Bijective (𝔇.diagonalContract hA5 X d
          (h.codimensionCycleClass (prod X X) d (diagonalClass X d)) i j)) ∧
      ∃! lam : tateTwist F 𝔇.tate (𝔇.grade X (2 * (d : ℤ))) d →ₗ[F] F,
        𝔇.traceContract hA5 X d lam
          (h.codimensionCycleClass (prod X X) d (diagonalClass X d)) = 1
```

## Tag 0FIL, a lemma

[Tag 0FIL](https://stacks.math.columbia.edu/tag/0FIL) in the Stacks Project.

**`Stacks.WeilCohomology.WeilChernData.kunneth_toWeilData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/KunnethWeilThree.lean, line 419](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/KunnethWeilThree.lean#L419). The attribute's comment: “axiom (B) of 0FHA for the data of (A1)-(A7): the Künneth map is an isomorphism and ∫\_\{X×Y} = ∫\_X ⊗ ∫\_Y, with ∫ = λ of (A6) and γ the cycle class map of 0FIF”.

> **Stacks Project, Lemma 0FIL.** Let (D0), (D1), (D2') be data satisfying axioms (A1)–(A7) of
> Section 45.14. Then axiom (B) of Section 0FHA holds for the data (D0)–(D3) they define
> (`WeilChernData.toWeilData`: `γ` the cycle class map of Tag 0FIF, `∫_X = λ` the trace map of
> (A6)): for smooth projective `X`, `Y` over `k`, (a) `H^*(X) ⊗_F H^*(Y) ⟶ H^*(X × Y)`,
> `α ⊗ β ↦ pr₁^*α ∪ pr₂^*β`, is an isomorphism, and (b) if `X` and `Y` are nonempty and
> equidimensional, `∫_{X × Y} = ∫_X ⊗ ∫_Y` via (a).

```lean
theorem kunneth_toWeilData (𝔚 : WeilChernData k F) : 𝔚.toWeilData.Kunneth
```

## Tag 0FIM, a lemma

[Tag 0FIM](https://stacks.math.columbia.edu/tag/0FIM) in the Stacks Project.

**`Stacks.WeilCohomology.WeilChernData.cycleClassPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CycleClassPointWeilThree.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CycleClassPointWeilThree.lean#L115).

> **Stacks Project, Lemma 0FIM.** Assume given data (D0), (D1) and (D2') satisfying axioms
> (A1)–(A7). Then axiom (C)(d) of Section 0FHA holds for the data of Section 0FHA they define:
> `∫_{Spec k} γ([Spec k]) = 1`, where `γ` is the cycle class map of Tag 0FIF and `∫ = λ` is the
> trace map of axiom (A6).

```lean
theorem cycleClassPoint : 𝔚.toWeilData.CycleClassPoint
```

## Tag 0FIN, a lemma

[Tag 0FIN](https://stacks.math.columbia.edu/tag/0FIN) in the Stacks Project.

**`Stacks.WeilCohomology.WeilChernData.cycleClass_equidimensionalPushforward_bundleProj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveBundlePushforward.lean, line 309](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveBundlePushforward.lean#L309). The attribute's comment: “the whole lemma, under exactly (A1)-(A7) (WeilChernData): for p : P(E) -> X with E of rank r + 1 >= 1 and X nonempty equidimensional, gamma(p\_* alpha) = p\_* gamma(alpha) for every alpha in CH^i(P), with the pushforward of Section 0FHA for toWeilData; nothing assumed”.

> **Stacks Project, Lemma 0FIN.** Let (D0), (D1), (D2') satisfy axioms (A1)–(A7), let `ℰ` be
> a finite locally free module of rank `r + 1 ≥ 1` on a nonempty equidimensional smooth projective
> `X` over `k` and `p : P = 𝐏(ℰ) ⟶ X` its projective bundle, as in axiom (A3). Then `γ` commutes
> with pushforward along `p`: for `P` and `X` of dimensions `e` and `d` and `α ∈ CH^i(P)`,
> `γ(p_*α) = p_*γ(α)` in `H^{2j}(X)(j)`, `j = i + d - e`, where `p_*α` is proper pushforward of
> cycles and `p_*γ(α)` the pushforward on cohomology of Section 0FHA, for the data
> `WeilChernData.toWeilData` (`∫_X = λ` of (A6), `γ` of Tag 0FIF). This is clause (C)(b),
> `WeilData.CycleClassPushforward`, for the morphism `p`.

```lean
theorem cycleClass_equidimensionalPushforward_bundleProj {d e : ℕ}
    (hX : IsNonemptyEquidimensional X d) (hP : IsNonemptyEquidimensional (bundle X E r) e)
    (i j : ℤ) (hij : j = i + d - e) (α : codimensionChowGroup k (bundle X E r).obj.hom i) :
    𝔚.toWeilData.cycleClass X j (equidimensionalPushforward (bundleProj X E r) e d i j hij α) =
      𝔚.toWeilData.pushforward 𝔚.perfectPairing (bundleProj X E r) hP hX (2 * i) i
        (2 * j) j (by omega) (by omega) (𝔚.toWeilData.cycleClass (bundle X E r) i α)
```

## Tag 0FVR, a lemma

[Tag 0FVR](https://stacks.math.columbia.edu/tag/0FVR) in the Stacks Project.

**`Stacks.WeilCohomology.WeilChernData.untwistTrace_one_spec_galois`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/GaloisTraceDegree.lean, line 372](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/GaloisTraceDegree.lean#L372). The attribute's comment: “the source's statement on the actual data (D0), (D1), (D2') satisfying (A1)-(A7) (WeilChernData, with γ of 0FIF): every λ normalised as in (A6) at Spec(k'), i.e. ∫\_\{Spec(k')} (unique by 0FIK), takes the unit class to [k' : k]; the nonvanishing of H^*(Spec(k')) needed to cancel the unit is derived from (A3), (A4), (A5)”.

> **Stacks Project, Tag 0FVR.** Assume given data (D0), (D1), (D2') satisfying axioms
> (A1)–(A7), and let `k'/k` be a finite Galois extension. Then `∫_{Spec(k')} 1 = [k' : k]`: every
> `F`-linear map `λ : H^0(Spec(k'))(0) ⟶ F` with `(id ⊗ λ) γ([Δ]) = 1` (axiom (A6), `γ` the cycle
> class map of Tag 0FIF; such a `λ` is unique by Remark 0FIK and is `∫_{Spec(k')}`) takes the unit
> class to `[k' : k]`.

```lean
theorem untwistTrace_one_spec_galois
    (lam : tateTwist F 𝔚.tate (𝔚.grade (spec k k') (2 * ((0 : ℕ) : ℤ))) (0 : ℕ) →ₗ[F] F)
    (hlam : 𝔚.traceContract 𝔚.kunneth (spec k k') 0 lam
      (𝔚.γ (prod (spec k k') (spec k k')) 0 (diagonalClass (spec k k') 0)) = 1) :
    𝔚.untwistTrace (spec k k') 0 lam 1 = (Module.finrank k k' : F)
```

**`Stacks.WeilCohomology.WeilChernData.toWeilData_trace_one_spec_galois`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/GaloisTraceDegree.lean, line 388](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/GaloisTraceDegree.lean#L388). The attribute's comment: “the source's statement for the trace map ∫\_\{Spec(k')} of 𝔚.toWeilData, the λ of (A6) at Spec(k'), on the data (D0), (D1), (D2') satisfying (A1)-(A7): ∫\_\{Spec(k')} 1 = [k' : k]”.

> **Stacks 0FVR for the trace map `∫_X` of the data of Section 0FHA defined by `𝔚`**:
> `∫_{Spec(k')} 1 = [k' : k]`, where `∫_{Spec(k')}` is the trace map of `𝔚.toWeilData`, the `λ`
> of the axiom (A6) at `Spec(k')`.

```lean
theorem toWeilData_trace_one_spec_galois :
    𝔚.untwistTrace (spec k k') 0 (𝔚.toWeilData.trace (spec k k') 0
      (isNonemptyEquidimensional_of_dimension_zero
        (FirstChernClassData.topologicalKrullDim_spec_field (k := k) (K' := k')))) 1 =
      (Module.finrank k k' : F)
```

## Tag 0FIP, a lemma

[Tag 0FIP](https://stacks.math.columbia.edu/tag/0FIP) in the Stacks Project.

**`Stacks.WeilCohomology.WeilChernData.cycleClassPushforward_of_closedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CycleClassPushforwardOfClosedImmersion.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CycleClassPushforwardOfClosedImmersion.lean#L52). The attribute's comment: “the whole lemma, under exactly (A1)-(A7) (WeilChernData): if i\_*(1) = gamma([Z]) for every closed immersion i : Z -> X of nonempty equidimensional smooth projective schemes over k, then gamma commutes with pushforward (axiom (C)(b) for toWeilData); nothing assumed”.

> **Stacks Project, Lemma 0FIP.** Assume given data (D0), (D1), (D2') satisfying axioms
> (A1)–(A7). In order to show that `γ` commutes with pushforward (axiom (C)(b) of Section 0FHA for
> the data `𝔚.toWeilData`) it suffices to show that `i_*(1) = γ([Z])` in `H^{2c}(X)(c)`,
> `c = d - e`, whenever `i : Z ⟶ X` is a closed immersion of nonempty smooth projective
> equidimensional schemes over `k`, of dimensions `e` and `d`. Here `[Z] ∈ CH^c(X)` is the class of
> the closed subscheme `Z` and `i_*` the pushforward on cohomology defined by Poincaré duality.

```lean
theorem cycleClassPushforward_of_closedImmersion
    (hi : ∀ {Z X : (SmoothProjectiveScheme k).FullSubcategory} (i : Z ⟶ X)
      [IsClosedImmersion i.hom.left] {e d : ℕ} (hZ : IsNonemptyEquidimensional Z e)
      (hX : IsNonemptyEquidimensional X d) (c : ℤ) (hc : c = d - e),
      𝔚.toWeilData.pushforward 𝔚.perfectPairing i hZ hX 0 0 (2 * c) c (by omega) (by omega)
          (𝔚.toWeilData.unitTw Z 0 0 rfl) =
        𝔚.toWeilData.cycleClass X c (closedSubschemeClass X.obj.hom i.hom.left c)) :
    𝔚.toWeilData.CycleClassPushforward 𝔚.perfectPairing
```

## Tag 0FIQ, a lemma

[Tag 0FIQ](https://stacks.math.columbia.edu/tag/0FIQ) in the Stacks Project.

**`Stacks.WeilCohomology.WeilChernData.pushforwardCompatible_fst_grassmannian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/GrassmannianProjectionPushforward.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/GrassmannianProjectionPushforward.lean#L130). The attribute's comment: “the whole lemma, under exactly (A1)-(A7) (WeilChernData): for l < n (so in particular 0 < l < n) and X nonempty equidimensional, gamma commutes with pushforward along p : X × G(l, n) -> X, gamma(p\_* alpha) = p\_* gamma(alpha) for every alpha in CH^i(X × G(l, n)), with the pushforward of Section 0FHA for toWeilData; nothing assumed”.

> Let data (D0), (D1), (D2') satisfy axioms (A1)–(A7) of Section 45.14 (`WeilChernData`), with
> `γ` the cycle class map of Tag 0FIF and the pushforward on cohomology of Section 45.9 built from
> the trace maps `λ` of (A6) (`WeilChernData.toWeilData`, Poincaré duality being Lemma 0FIJ). For
> integers `l < n` (in particular `0 < l < n`) and a smooth projective scheme `X` over `k`, `γ`
> commutes with pushforward along the projection `p : X × G(l, n) ⟶ X`: whenever `X` is nonempty and
> equidimensional of dimension `d` and `X × G(l, n)` of dimension `d'`, `γ(p_*α) = p_*γ(α)` in
> `H^{2q}(X)(q)` for every `α ∈ CH^i(X × G(l, n))`, `q = i + d - d'`.

```lean
theorem pushforwardCompatible_fst_grassmannian {l n : ℕ} (hln : l < n)
    (X : (SmoothProjectiveScheme k).FullSubcategory) :
    𝔚.toWeilData.PushforwardCompatible 𝔚.perfectPairing
      (fst X (SmoothProjectiveScheme.grassmannian k l n))
```

## Tag 0FIR, a lemma

[Tag 0FIR](https://stacks.math.columbia.edu/tag/0FIR) in the Stacks Project.

**`Stacks.WeilCohomology.WeilChernData.cycleClassPushforward_of_extendableConormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CycleClassPushforwardOfExtendableConormal.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CycleClassPushforwardOfExtendableConormal.lean#L65). The attribute's comment: “the whole lemma, under exactly (A1)-(A7) (WeilChernData): if i\_*(1) = gamma([Z]) for every closed immersion i : Z -> X of nonempty equidimensional smooth projective schemes over k whose conormal class in K\_0(Z) is the pullback of a class in K\_0(X), then gamma commutes with pushforward (axiom (C)(b) for toWeilData); nothing assumed”.

> **Stacks Project, Lemma 0FIR.** Assume given data (D0), (D1), (D2') satisfying axioms
> (A1)–(A7). In order to show that `γ` commutes with pushforward (axiom (C)(b) of Section 0FHA for
> the data `𝔚.toWeilData`) it suffices to show that `i_*(1) = γ([Z])` in `H^{2c}(X)(c)`,
> `c = d - e`, whenever `i : Z ⟶ X` is a closed immersion of nonempty smooth projective
> equidimensional schemes over `k`, of dimensions `e` and `d`, such that the class of the conormal
> sheaf `𝒞_{Z/X}` in `K₀(Z)` is the pullback of a class in `K₀(X)`. Here `[Z] ∈ CH^c(X)` is the
> class of the closed subscheme `Z` and `i_*` the pushforward on cohomology defined by Poincaré
> duality.

```lean
theorem cycleClassPushforward_of_extendableConormal
    (hi : ∀ {Z X : (SmoothProjectiveScheme k).FullSubcategory} (i : Z ⟶ X)
      [IsClosedImmersion i.hom.left]
      {e d : ℕ} (hZ : IsNonemptyEquidimensional Z e) (hX : IsNonemptyEquidimensional X d)
      (c : ℤ) (hc : c = d - e),
      (∃ β : VectorBundleKZero X.obj.left, pullbackRingHom i.hom.left β =
        classOf Z.obj.left (Stacks.Conormal.conormalSheaf i.hom.left)) →
      𝔚.toWeilData.pushforward 𝔚.perfectPairing i hZ hX 0 0 (2 * c) c (by omega) (by omega)
          (𝔚.toWeilData.unitTw Z 0 0 rfl) =
        𝔚.toWeilData.cycleClass X c (closedSubschemeClass X.obj.hom i.hom.left c)) :
    𝔚.toWeilData.CycleClassPushforward 𝔚.perfectPairing
```

## Tag 0FVS, a lemma

[Tag 0FVS](https://stacks.math.columbia.edu/tag/0FVS) in the Stacks Project.

**`Stacks.WeilCohomology.FirstChernClassData.injective_pull_specMap_of_nontrivial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/SeparableExtensionCohomology.lean, line 402](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/SeparableExtensionCohomology.lean#L402). The attribute's comment: “the source's statement, on the actual data (D0), (D1), (D2') over smooth projective k-schemes: with H^*(Spec K) ≠ 0 for a finite normal separable K ⊇ k'' (a normal closure), H^*(Spec k') ⟶ H^*(Spec k'') is injective, from (A1) and (A5)”.

> For finite separable field extensions `k''/k'/k` and a finite normal separable extension `K/k`
> containing `k''` (for instance a normal closure of `k''/k`) with `H^*(Spec(K)) ≠ 0`, pullback
> `H^*(Spec(k')) ⟶ H^*(Spec(k''))` is injective, under axioms (A1) and (A5) (the source assumes
> (A1)–(A7)); in particular it is injective on `H^0`.

```lean
theorem injective_pull_specMap_of_nontrivial (hA1 : 𝔇.CoproductAxiom) (hA5 : 𝔇.KunnethAxiom)
    {k' : Type u} [Field k'] [Algebra k k'] [FiniteDimensional k k'] [Algebra.IsSeparable k k']
    {k'' : Type u} [Field k''] [Algebra k k''] [FiniteDimensional k k''] [Algebra.IsSeparable k k'']
    (incl : k' →ₐ[k] k'') {E : Type u} [Field E] [Algebra k E] [FiniteDimensional k E]
    [Algebra.IsSeparable k E] [Normal k E] (ι : k'' →ₐ[k] E) (hE : Nontrivial (𝔇.H (spec k E))) :
    Function.Injective (𝔇.pull (specMap incl))
```

**`Stacks.WeilCohomology.FirstChernClassData.injective_pull_specMap_of_axioms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/SeparableExtensionCohomology.lean, line 463](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/SeparableExtensionCohomology.lean#L463). The attribute's comment: “unconditional form: the nonvanishing hypothesis is derived from (A3), (A4), (A5)”.

> For finite separable field extensions `k''/k'/k`, pullback `H^*(Spec(k')) ⟶ H^*(Spec(k''))` is
> injective under axioms (A1), (A3), (A4) and (A5), `F` having characteristic zero: the hypothesis
> `H^0(Spec(K)) ≠ 0` of the source is a consequence of the axioms
> (`Stacks.WeilCohomology.FirstChernClassData.nontrivial_H_spec`). This is the form in which the
> proof of Stacks 0FIS uses 0FVS.

```lean
theorem injective_pull_specMap_of_axioms [CharZero F] (hA1 : 𝔇.CoproductAxiom)
    (hA3 : 𝔇.ProjectiveBundleAxiom) (hA4 : 𝔇.DivisorAxiom) (hA5 : 𝔇.KunnethAxiom)
    {k' : Type u} [Field k'] [Algebra k k'] [FiniteDimensional k k'] [Algebra.IsSeparable k k']
    {k'' : Type u} [Field k''] [Algebra k k''] [FiniteDimensional k k''] [Algebra.IsSeparable k k'']
    (incl : k' →ₐ[k] k'') : Function.Injective (𝔇.pull (specMap incl))
```

**`Stacks.WeilCohomology.injective_pullback_of_separable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/SeparableExtension.lean, line 418](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/SeparableExtension.lean#L418). The attribute's comment: “injectivity on cohomology for a tower of finite separable field extensions; the Künneth decomposition of Spec(k') x Spec(K) as a product over the embeddings, the functoriality relations, and the nonvanishing of the cohomology of Spec(K) are derived from the functor of (D1) together with axioms (A1), (A5), (A6) and (C)(b), which are explicit arguments here, as elsewhere in Section 45.14”.

> Let `k''/k'/k` be finite separable field extensions. Then pullback
> `H^0(Spec(k')) → H^0(Spec(k''))` is injective.
>
> Here `H` is the cohomology functor of `(D1)`, read on the spectra of finite étale `k`-algebras;
> since these schemes are zero dimensional, `H^0` is the total cohomology `H^*`. The hypothesis
> `kunneth` is axiom `(A5)` and `disjointUnion` is axiom `(A1)`; `traceMap` is the trace map
> `∫_{Spec(L)}` of axiom `(A6)` for the zero-dimensional scheme `Spec(L)`, `cycleClass` is the
> cycle class map `γ` of `(D2')` on the zero cycles of `Spec(L)`, free of rank one on `[Spec(L)]`,
> and `traceMap_cycleClass` is axiom `(C)(b)` for the structure morphism of `Spec(L)`, which
> evaluates that trace on `γ(n · [Spec(L)])` as its degree `n · [L : k]`.

```lean
theorem injective_pullback_of_separable
    (k k' k'' : Type u) [Field k] [Field k'] [Field k'']
    [Algebra k k'] [Algebra k k''] [Algebra k' k''] [IsScalarTower k k' k'']
    [FiniteDimensional k k'] [Algebra.IsSeparable k k']
    [FiniteDimensional k' k''] [Algebra.IsSeparable k' k'']
    (F : Type v) [Field F] [CharZero F] (H : FinEtaleAlg k ⥤ CommAlgCat.{w} F)
    (kunneth : ∀ X Y : FinEtaleAlg k, Function.Bijective (finEtaleKunnethMap H X Y))
    (disjointUnion : ∀ (ι : Type u) [Fintype ι] (X : ι → FinEtaleAlg k),
      Function.Bijective (componentRestriction H X))
    (cycleClass : ∀ (L : Type u) [Field L] [Algebra k L] (hfin : Module.Finite k L)
      (hsep : Algebra.IsSeparable k L), ℤ →+ H.obj (ofField k L hfin hsep))
    (traceMap : ∀ (L : Type u) [Field L] [Algebra k L] (hfin : Module.Finite k L)
      (hsep : Algebra.IsSeparable k L), H.obj (ofField k L hfin hsep) →ₗ[F] F)
    (traceMap_cycleClass : ∀ (L : Type u) [Field L] [Algebra k L]
      (hfin : Module.Finite k L) (hsep : Algebra.IsSeparable k L) (n : ℤ),
      traceMap L hfin hsep (cycleClass L hfin hsep n) =
        (n : F) * (Module.finrank k L : F)) :
    Function.Injective (H.map (algHomMk (X := ofField k k' inferInstance inferInstance)
      (Y := ofField k k'' (Module.Finite.trans k' k'') (Algebra.IsSeparable.trans k k' k''))
      (IsScalarTower.toAlgHom k k' k'')))
```

## Tag 0FIS, a lemma

[Tag 0FIS](https://stacks.math.columbia.edu/tag/0FIS) in the Stacks Project.

**`Stacks.WeilCohomology.integration_comp_pullback_eq_integration`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/BlowupPushforward.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/BlowupPushforward.lean#L148). The attribute's comment: “integration agrees with integration after pullback to the blowup”.

> **Stacks Project, Tag 0FIS.** For a blowup `b : X' ⟶ X` of a nonempty equidimensional smooth
> projective scheme of dimension `d` in a nowhere dense smooth centre, integration over `X'` after
> pullback is integration over `X`: both satisfy the normalization `(1 ⊗ ∫)(η) = 1` of `(A6)`
> against the degree-zero Künneth component of the diagonal class of `X`, which determines the
> trace map.

```lean
theorem integration_comp_pullback_eq_integration
    (pullbackZero : A →ₗ[F] A') (pullbackTop : T →ₗ[F] T') (restrict : A' →ₗ[F] P)
    (one : A) (one' : A') (integration : T →ₗ[F] F) (integration' : T' →ₗ[F] F)
    (η : A ⊗[F] T) (η' : A' ⊗[F] T')
    (restrict_injective : Function.Injective restrict)
    (pullbackZero_injective : Function.Injective pullbackZero)
    (pullbackZero_one : pullbackZero one = one')
    (restrict_eq : TensorProduct.map (restrict ∘ₗ pullbackZero) pullbackTop η =
      TensorProduct.map restrict LinearMap.id η')
    (normalization : tensorContractRight integration η = one)
    (normalization' : tensorContractRight integration' η' = one')
    (nondegenerate : Function.Injective fun μ : T →ₗ[F] F => tensorContractRight μ η) :
    integration' ∘ₗ pullbackTop = integration
```

**`Stacks.WeilCohomology.pushforwardOne_blowup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/BlowupPushforward.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/BlowupPushforward.lean#L174).

> **Stacks Project, Tag 0FIS.** For a blowup `b : X' ⟶ X` of a nonempty equidimensional smooth
> projective scheme of dimension `d` in a nowhere dense smooth centre, the Poincaré-dual
> pushforward carries the unit class of `X'` to the unit class of `X`: `b_*(1) = 1`.

```lean
theorem pushforwardOne_blowup
    (pullbackZero : A →ₗ[F] A') (pullbackTop : T →ₗ[F] T') (restrict : A' →ₗ[F] P)
    (one : A) (one' : A') (integration : T →ₗ[F] F) (integration' : T' →ₗ[F] F)
    (pairing : T →ₗ[F] A →ₗ[F] F) [pairing.IsPerfPair] (pairing' : T' →ₗ[F] A' →ₗ[F] F)
    (η : A ⊗[F] T) (η' : A' ⊗[F] T')
    (restrict_injective : Function.Injective restrict)
    (pullbackZero_injective : Function.Injective pullbackZero)
    (pullbackZero_one : pullbackZero one = one')
    (restrict_eq : TensorProduct.map (restrict ∘ₗ pullbackZero) pullbackTop η =
      TensorProduct.map restrict LinearMap.id η')
    (normalization : tensorContractRight integration η = one)
    (normalization' : tensorContractRight integration' η' = one')
    (nondegenerate : Function.Injective fun μ : T →ₗ[F] F => tensorContractRight μ η)
    (pairing_one : ∀ β, pairing β one = integration β)
    (pairing_one' : ∀ β, pairing' β one' = integration' β) :
    poincareDualPushforward pairing' pairing pullbackTop one' = one
```

**`Stacks.WeilCohomology.FirstChernClassData.trace_comp_pullGradeTw_blowupHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/BlowupPushforwardOne.lean, line 203](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/BlowupPushforwardOne.lean#L203). The attribute's comment: “∫\_\{X'} ∘ b^* = ∫\_X on H^\{2d}(X)(d) for the blowing up in a nowhere dense smooth centre, the trace maps being the λ of (A6) and γ the cycle class map of 0FIF, under (A1)-(A8); the form b\_*(1) = 1 of the statement is this identity read through Poincaré duality”.

> **Stacks Project, Tag 0FIS.** Let data (D0), (D1), (D2') satisfy axioms (A1)–(A8) of
> Section 45.14 (of which (A1), (A3), (A4), (A5), (A7), (A8) are used), with `γ` the cycle class map
> of Tag 0FIF. Let `b : X' ⟶ X` be the blowing up of a smooth projective scheme `X` over `k`,
> nonempty and equidimensional of dimension `d`, in a nowhere dense smooth centre `Z ⊆ X`. Then the
> trace map `∫_{X'}` of `X'` composed with `b^* : H^{2d}(X)(d) ⟶ H^{2d}(X')(d)` is the trace map
> `∫_X` of `X`: for the linear maps `λ`, `λ'` of axiom (A6) for `X` and `X'` (unique by Remark 0FIK),
> `λ' ∘ b^* = λ`. This is the identity the source's proof establishes ("`∫_X` is equal to `∫_{X'}`
> composed with the pullback map"), equivalent to `b_*(1) = 1` for the pushforward of Section 45.9
> built from these trace maps.

```lean
theorem trace_comp_pullGradeTw_blowupHom (h : 𝔇.IsCohomologicalChernCharacter ch)
    (hA1 : 𝔇.CoproductAxiom) (hA3 : 𝔇.ProjectiveBundleAxiom) (hA4 : 𝔇.DivisorAxiom)
    (hA5 : 𝔇.KunnethAxiom) (hA7 : 𝔇.BlowupAxiom) (hA8 : 𝔇.GlobalSectionsAxiom)
    {Z X : (SmoothProjectiveScheme k).FullSubcategory} (i : Z ⟶ X) [IsClosedImmersion i.hom.left]
    (hZ : IsNowhereDense (Set.range i.hom.left.base)) {d : ℕ}
    (hX : IsNonemptyEquidimensional X d)
    (lam : tateTwist F 𝔇.tate (𝔇.grade X (2 * (d : ℤ))) d →ₗ[F] F)
    (lam' : tateTwist F 𝔇.tate (𝔇.grade (blowupObj i) (2 * (d : ℤ))) d →ₗ[F] F)
    (hlam : 𝔇.traceContract hA5 X d lam
      (h.codimensionCycleClass (prod X X) d (diagonalClass X d)) = 1)
    (hlam' : 𝔇.traceContract hA5 (blowupObj i) d lam'
      (h.codimensionCycleClass (prod (blowupObj i) (blowupObj i)) d
        (diagonalClass (blowupObj i) d)) = 1) :
    lam' ∘ₗ 𝔇.pullGradeTw (blowupHom i) (2 * (d : ℤ)) d = lam
```

**`Stacks.WeilCohomology.FirstChernClassData.pushforward_unitTw_blowupHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/BlowupPushforwardOne.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/BlowupPushforwardOne.lean#L229). The attribute's comment: “b\_*(1) = 1 for the blowing up in a nowhere dense smooth centre, for the pushforward of Section 45.9 attached to the data of (A1)-(A8) with the trace maps of (A6) and γ of 0FIF”.

> **Stacks Project, Tag 0FIS: `b_*(1) = 1`.** Let data (D0), (D1), (D2') satisfy axioms
> (A1)–(A8) of Section 45.14 (of which (A1), (A3)–(A8) are used), `γ` the cycle class map of
> Tag 0FIF, and let `W` be the data (D0)–(D3) of Section 45.9 they define, with trace maps the `λ`
> of (A6) (`IsCohomologicalChernCharacter.toWeilData`), which satisfy axiom (A) by Lemma 0FIJ. Let
> `b : X' ⟶ X` be the blowing up of a smooth projective scheme `X` over `k`, nonempty and
> equidimensional of dimension `d`, in a nowhere dense smooth centre. Then the pushforward
> `b_* : H^0(X') ⟶ H^0(X)` of Section 45.9 sends `1` to `1`.

```lean
theorem pushforward_unitTw_blowupHom (h : 𝔇.IsCohomologicalChernCharacter ch)
    (hA1 : 𝔇.CoproductAxiom) (hA3 : 𝔇.ProjectiveBundleAxiom) (hA4 : 𝔇.DivisorAxiom)
    (hA5 : 𝔇.KunnethAxiom) (hA6 : 𝔇.TraceAxiomFor hA5 h.codimensionCycleClass)
    (hA7 : 𝔇.BlowupAxiom) (hA8 : 𝔇.GlobalSectionsAxiom)
    {Z X : (SmoothProjectiveScheme k).FullSubcategory} (i : Z ⟶ X) [IsClosedImmersion i.hom.left]
    (hZ : IsNowhereDense (Set.range i.hom.left.base)) {d : ℕ}
    (hX : IsNonemptyEquidimensional X d) :
    (h.toWeilData hA1 hA3 hA5 hA6).pushforward
        (h.poincareDuality_toWeilData hA1 hA3 hA5 hA6 hA4 hA7).perfectPairing (blowupHom i)
        (isNonemptyEquidimensional_blowupObj i hX hZ) hX 0 0 0 0 rfl rfl
        ((h.toWeilData hA1 hA3 hA5 hA6).unitTw (blowupObj i) 0 0 rfl) =
      (h.toWeilData hA1 hA3 hA5 hA6).unitTw X 0 0 rfl
```

## Tag 0FIT, a lemma

[Tag 0FIT](https://stacks.math.columbia.edu/tag/0FIT) in the Stacks Project.

**`Stacks.WeilCohomology.WeilChernData.cycleClassPushforward_of_globalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CycleClassPushforwardGlobalSections.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CycleClassPushforwardGlobalSections.lean#L144). The attribute's comment: “the whole lemma, under exactly (A1)-(A8): WeilChernData bundles (A1)-(A7) and the only hypothesis is (A8) GlobalSections; conclusion: gamma commutes with pushforward (axiom (C)(b) for toWeilData) for every morphism of nonempty equidimensional smooth projective schemes; nothing assumed, (A9) is not used”.

> **Tag 0FIT**: for data (D0), (D1), (D2') satisfying axioms (A1)–(A8) (a `WeilChernData`,
> which bundles (A1)–(A7), and (A8) `GlobalSections`), the cycle class map `γ` commutes with
> pushforward: axiom (C)(b) of Section 0FHA for `WeilChernData.toWeilData`, i.e.
> `γ(f_*α) = f_*γ(α)` for every morphism `f : X ⟶ Y` of nonempty equidimensional smooth projective
> schemes over `k` and every `α ∈ CH^p(X)`. This is Lemma 0FIP's reduction
> (`cycleClassPushforward_of_grassmannian`) applied to
> `pushforward_unitTw_eq_cycleClass_of_globalSections`. The source's proof cites (A9) for
> `j_*1 = γ([E])`; here that step is `cycleClass_exceptional_eq_pushforward_unitTw_of_lt`, proved
> from (A1)–(A8).

```lean
theorem cycleClassPushforward_of_globalSections (hA8 : 𝔚.GlobalSections) :
    𝔚.toWeilData.CycleClassPushforward 𝔚.perfectPairing
```

## Tag 0FIU, a proposition

[Tag 0FIU](https://stacks.math.columbia.edu/tag/0FIU) in the Stacks Project.

**`Stacks.WeilCohomology.WeilChernData.exists_weilCohomologyTheory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/WeilCohomologyTheoryOfWeilChern.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/WeilCohomologyTheoryOfWeilChern.lean#L85). The attribute's comment: “the whole proposition, under exactly (A1)-(A8): WeilChernData bundles (A1)-(A7) and the only hypothesis is (A8) GlobalSections; conclusion: a Weil cohomology theory (Definition 0FI2) whose data (D0)-(D3) are F(1), H^*, gamma of 0FIF and the trace of (A6); nothing assumed, (A9) is not used”.

> **Proposition 0FIU: data (D0), (D1), (D2') satisfying (A1)–(A8) give a Weil cohomology
> theory**: there is a Weil cohomology theory (Definition 0FI2) whose data (D0)–(D3) are
> `𝔚.toWeilData`, i.e. the given `F(1)` and `H^*`, the cycle class map `γ` of Tag 0FIF and the trace
> map `∫_X = λ` of axiom (A6).

```lean
theorem exists_weilCohomologyTheory (hA8 : 𝔚.GlobalSections) :
    ∃ T : WeilCohomologyTheory k F, T.toWeilData = 𝔚.toWeilData
```

## Tag 0FVT, a lemma

[Tag 0FVT](https://stacks.math.columbia.edu/tag/0FVT) in the Stacks Project.

**`Stacks.WeilCohomology.exists_axioms_of_fieldExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/BaseFieldExtension/Descent.lean, line 215](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/BaseFieldExtension/Descent.lean#L215).

> **Stacks Tag 0FVT.** Let `k'/k` be an extension of fields and `F'/F` an extension of fields
> of characteristic zero. Let `𝔇 = (F(1), H^*, c₁^H)` be data (D0), (D1), (D2') for `k` and `F`
> and `𝔚' = (F'(1), (H')^*, c₁^{H'})` data (D0), (D1), (D2') for `k'` and `F'`, given with an
> isomorphism `F(1) ⊗_F F' ≅ F'(1)` and isomorphisms `H^*(X) ⊗_F F' ≅ (H')^*(X_{k'})` of graded
> `F'`-algebras, functorial in the smooth projective scheme `X` over `k`, under which `c₁^H` and
> `c₁^{H'}` correspond (`Φ`, a `Stacks.WeilCohomology.FieldExtensionComparison`). If
> `F'(1), (H')^*, c₁^{H'}` satisfy (A1)–(A9) — (A1)–(A7) being the fields of
> `Stacks.WeilCohomology.WeilChernData`, (A8) `GlobalSections`, (A9) `DivisorTrace` — then
> `F(1), H^*, c₁^H` satisfy (A1)–(A9): (A1)–(A5), (A6) for the cycle class map `γ` of Tag 0FIF of
> the data `𝔇` (which (A1)–(A4) determine), (A7), (A8), and (A9) for that `γ`.

```lean
theorem exists_axioms_of_fieldExtension [CharZero F] [CharZero F'] (𝔇 : FirstChernClassData k F)
    (𝔚' : WeilChernData k' F') (Φ : FieldExtensionComparison 𝔇 𝔚'.toFirstChernClassData)
    (h8 : 𝔚'.GlobalSections) (h9 : 𝔚'.DivisorTrace) :
    ∃ (hA1 : 𝔇.CoproductAxiom) (hA2 : 𝔇.PullbackAxiom) (hA3 : 𝔇.ProjectiveBundleAxiom)
      (hA4 : 𝔇.DivisorAxiom) (hA5 : 𝔇.KunnethAxiom),
      𝔇.TraceAxiomFor hA5 (𝔇.cycleClassOf hA1 hA2 hA3 hA4) ∧ 𝔇.BlowupAxiom ∧
        𝔇.GlobalSectionsAxiom ∧ 𝔇.DivisorTraceAxiomFor hA5 (𝔇.cycleClassOf hA1 hA2 hA3 hA4)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 45.14, Tag 0FID](https://stacks.math.columbia.edu/tag/0FID)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
