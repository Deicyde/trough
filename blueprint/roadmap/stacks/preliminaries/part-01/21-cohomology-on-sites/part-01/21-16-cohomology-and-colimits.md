---
declaration: section
origin: cited
lean: Stacks.Cohomology.isIso_colimit_post_rightDerived_sheafSections, Stacks.Cohomology.ColimitsOfCohomology.isIso_colimit_post_rightDerived_globalSections, Stacks.Cohomology.ColimitsOfCohomology.isIso_colimit_post_rightDerived_globalSections_of_coveringSet, AlgebraicGeometry.Stack.exists_fin_affineObjects_isLocallySurjective_equalizerLift, AlgebraicGeometry.Stack.exists_fin_affineObjects_isLocallySurjective_equalizerLift_etale, Stacks.Cohomology.ColimitsOfCohomology.isQuasiCompact_of_finiteCoproductSheafifiedYoneda, Stacks.Cohomology.ColimitsOfCohomology.isIso_colimit_post_rightDerived_globalSections_of_finite_covers, Stacks.Cohomology.ColimitsOfCohomology.isIso_colimit_post_rightDerived_globalSections_of_covers
statement: formalized
proof: formalized
---

# 21.16 Cohomology and colimits

Section 21.16 of the Stacks Project, [Tag 0737](https://stacks.math.columbia.edu/tag/0737). 6 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0739, a lemma

[Tag 0739](https://stacks.math.columbia.edu/tag/0739) in the Stacks Project.

**`Stacks.Cohomology.isIso_colimit_post_rightDerived_sheafSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Recovery21/FilteredColimitsAndCohomology.lean, line 994](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Recovery21/FilteredColimitsAndCohomology.lean#L994).

> **Stacks 0739.** On a site, suppose a collection of finite covering families is cofinal
> among the coverings of each object in `B`, and all nonempty iterated fibre products occurring
> in those families remain in `B`. Then the canonical map from the filtered colimit of the
> cohomology groups to the cohomology of the filtered colimit is an isomorphism.

```lean
public theorem isIso_colimit_post_rightDerived_sheafSections
    {C : Type u} [SmallCategory C] (J : GrothendieckTopology C)
    (B : Set C) (Cov : ∀ U : C, Set (PreZeroHypercover.{w} U))
    (hCov : ∀ (U : C) (E : PreZeroHypercover.{w} U), Cov U E → E.sieve₀ ∈ J U)
    (hfinite : ∀ (U : C) (E : PreZeroHypercover.{w} U), Cov U E →
      HasIntersectionsIn B E)
    (hcofinal : ∀ (U : C), B U → ∀ S ∈ J U, ∃ E : PreZeroHypercover.{w} U,
      Cov U E ∧ E.sieve₀ ≤ S)
    (p : ℕ) (U : C) (hU : B U)
    {I : Type u} [SmallCategory I] [IsFiltered I]
    (F : CategoryTheory.Functor I (Sheaf J (Ab.{u}))) :
    IsIso (colimit.post F
      (((sheafSections J (Ab.{u})).obj (op U)).rightDerived p))
```

## Tag 0GN3, a lemma

[Tag 0GN3](https://stacks.math.columbia.edu/tag/0GN3) in the Stacks Project.

**`Stacks.Cohomology.ColimitsOfCohomology.isIso_colimit_post_rightDerived_globalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FilteredColimits/GlobalCohomology.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FilteredColimits/GlobalCohomology.lean#L140).

> **Stacks 0GN3.** Let `C` be a site and let `S` be a set of sheaves of sets on `C` such that
>
> 1. some `K ∈ S` surjects onto the final sheaf,
> 2. every surjection `G ⟶ K` onto a member of `S` admits a map `K' ⟶ G` from a member of `S` whose
>    composite to `K` is surjective,
> 3. every pair of members of `S` is covered by a member of `S` mapping onto their product,
> 4. the equalizer of every pair of maps between members of `S` is covered by a member of `S`, and
> 5. every member of `S` is quasi-compact.
>
> Then `colim_λ H^p(C, F_λ) ⟶ H^p(C, colim_λ F_λ)` is an isomorphism in every degree `p`, for every
> filtered diagram `F` of abelian sheaves.
>
> The proof is the source's induction on the degree. The base case is Stacks 0GMR (4), as
> `isIso_colimit_post_rightDerived_globalSections_zero`; the step is the long exact cohomology
> sequence of a functorial injective embedding of the diagram, as
> `isIso_colimit_post_rightDerived_globalSections_succ`, whose acyclicity input is
> `isZero_rightDerived_globalSections_colimit_of_isIso`. That input needs cohomology over the self
> powers `K^r` of a `K ∈ S` to commute with the colimit in the degrees already known, which is
> Stacks 07A0 (`isIso_colimit_post_extFunctorObj_freeAbelianSheafOn`) applied to Stacks 0GN3 on the
> localized site `C/K^r`, available because `C/K^r` again carries such a set
> (`Stacks.Cohomology.CoveringSet.exists_localized_coveringSet`). The induction is therefore strong
> in the degree and generalised over the site.

```lean
theorem isIso_colimit_post_rightDerived_globalSections
    (S : Set (Sheaf J (Type u)))
    (h_terminal : ∃ K ∈ S, Sheaf.IsLocallySurjective (terminal.from K))
    (h_lift : ∀ {G K : Sheaf J (Type u)} (f : G ⟶ K), K ∈ S →
      Sheaf.IsLocallySurjective f →
        ∃ K' ∈ S, ∃ g : K' ⟶ G, Sheaf.IsLocallySurjective (g ≫ f))
    (h_product : ∀ K ∈ S, ∀ K' ∈ S,
      ∃ K'' ∈ S, ∃ f : K'' ⟶ K ⨯ K', Sheaf.IsLocallySurjective f)
    (h_equalizer : ∀ {K K' : Sheaf J (Type u)} (a b : K ⟶ K'), K ∈ S → K' ∈ S →
      ∃ K'' ∈ S, ∃ f : K'' ⟶ equalizer a b, Sheaf.IsLocallySurjective f)
    (h_quasiCompact : ∀ K ∈ S, Sheaf.IsQuasiCompact K)
    (p : ℕ) {I : Type u} [SmallCategory I] [IsFiltered I]
    (F : I ⥤ Sheaf J (Ab.{u})) :
    IsIso (colimit.post F ((Sheaf.Γ J (Ab.{u})).rightDerived p))
```

**`Stacks.Cohomology.ColimitsOfCohomology.isIso_colimit_post_rightDerived_globalSections_of_coveringSet`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FilteredColimits/GlobalCohomologyOnALargeSite.lean, line 446](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FilteredColimits/GlobalCohomologyOnALargeSite.lean#L446). The attribute's comment: “for a site whose objects and morphisms need not share a universe”.

> **Stacks 0GN3 for an arbitrary site.** Let `C` be a site with objects in `Type u₁` and
> morphisms in `Type v`, and let `S` be a set of sheaves of sets on `C` with sections at the join
> `max u₁ v` of those two universes, such that
>
> 1. some `K ∈ S` surjects onto the final sheaf,
> 2. every surjection `G ⟶ K` onto a member of `S` admits a map `K' ⟶ G` from a member of `S` whose
>    composite to `K` is surjective,
> 3. every pair of members of `S` is covered by a member of `S` mapping onto their product,
> 4. the equalizer of every pair of maps between members of `S` is covered by a member of `S`, and
> 5. every member of `S` is quasi-compact.
>
> Then `colim_λ H^p(C, F_λ) ⟶ H^p(C, colim_λ F_λ)` is an isomorphism in every degree `p`, for every
> filtered diagram `F` of abelian sheaves with sections at that same universe.
>
> Unlike `isIso_colimit_post_rightDerived_globalSections`, the site need not be a `SmallCategory`:
> its objects and morphisms may live in different universes.

```lean
theorem isIso_colimit_post_rightDerived_globalSections_of_coveringSet
    (S : Set (Sheaf J (Type max u₁ v)))
    (h_terminal : ∃ K ∈ S, Sheaf.IsLocallySurjective (terminal.from K))
    (h_lift : ∀ {G K : Sheaf J (Type max u₁ v)} (f : G ⟶ K), K ∈ S →
      Sheaf.IsLocallySurjective f →
        ∃ K' ∈ S, ∃ g : K' ⟶ G, Sheaf.IsLocallySurjective (g ≫ f))
    (h_product : ∀ K ∈ S, ∀ K' ∈ S,
      ∃ K'' ∈ S, ∃ f : K'' ⟶ K ⨯ K', Sheaf.IsLocallySurjective f)
    (h_equalizer : ∀ {K K' : Sheaf J (Type max u₁ v)} (a b : K ⟶ K'), K ∈ S → K' ∈ S →
      ∃ K'' ∈ S, ∃ f : K'' ⟶ equalizer a b, Sheaf.IsLocallySurjective f)
    (h_quasiCompact : ∀ K ∈ S, Sheaf.IsQuasiCompact K)
    (p : ℕ) {I : Type max u₁ v} [SmallCategory I] [IsFiltered I]
    (F : I ⥤ Sheaf J (Ab.{max u₁ v})) :
    IsIso (colimit.post F ((Sheaf.Γ J (Ab.{max u₁ v})).rightDerived p))
```

## Tag 0GN4, a remark

[Tag 0GN4](https://stacks.math.columbia.edu/tag/0GN4) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_fin_affineObjects_isLocallySurjective_equalizerLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomologyEqualizerAffineCover.lean, line 598](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomologyEqualizerAffineCover.lean#L598). The attribute's comment: “condition (4) for the fppf site of an algebraic stack quasi-separated over a quasi-separated base scheme, with the collection B of Stacks 0GQV: the objects of the site lying over affine schemes; the family produced has one member, as in the source”.

> **Condition (4) of Stacks 0GN4 for the fppf site of an algebraic stack quasi-separated over a
> quasi-separated base scheme**, in the shape
> `AlgebraicGeometry.Stack.isIso_colimit_post_rightDerived_globalSections_fppf` consumes as its
> hypothesis `h_equalizer`: for two objects `x`, `x'` of the site lying over affine schemes and two
> morphisms `a, b : x ⟶ x'` there is a finite family of objects lying over affine schemes, each with
> a morphism to `x` equalizing `a` and `b`, whose sheafified representables jointly cover the
> equalizer of `h_a^#` and `h_b^#`.
>
> The family has one member, as in the source: the object the dominating object of
> `AlgebraicGeometry.Stack.exists_graph_dominating` classifies, with the equalizing morphism it
> classifies. This is
> `AlgebraicGeometry.Stack`
> `.exists_fin_affineObjects_isLocallySurjective_equalizerLift_associatedTopology` at the big fppf
> topology of `B`, its fibre-lifting hypothesis discharged by **Stacks 06QA**,
> `AlgebraicGeometry.Stack.exists_fppfCovering_fibre_lift`.

```lean
theorem exists_fin_affineObjects_isLocallySurjective_equalizerLift :
    ∀ {x x' : 𝒳.val.val.obj} (a b : x ⟶ x'),
      x ∈ affineObjects B S hS 𝒳.val → x' ∈ affineObjects B S hS 𝒳.val →
      ∃ (m : ℕ) (V : Fin m → 𝒳.val.val.obj),
        (∀ i, V i ∈ affineObjects B S hS 𝒳.val) ∧
          ∃ (p : ∀ i, V i ⟶ x) (hp : ∀ i, p i ≫ a = p i ≫ b),
          Sheaf.IsLocallySurjective (Limits.Sigma.desc fun i =>
            equalizer.lift
              (f := (Sheaf.sheafifiedYoneda (fppfTopology B S hS 𝒳.val)).map a)
              (g := (Sheaf.sheafifiedYoneda (fppfTopology B S hS 𝒳.val)).map b)
              ((Sheaf.sheafifiedYoneda (fppfTopology B S hS 𝒳.val)).map (p i)) (by
                simpa only [Functor.map_comp] using
                  congrArg (Sheaf.sheafifiedYoneda (fppfTopology B S hS 𝒳.val)).map (hp i)))
```

**`AlgebraicGeometry.Stack.exists_fin_affineObjects_isLocallySurjective_equalizerLift_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomologyEtaleEqualizerAffineCover.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomologyEtaleEqualizerAffineCover.lean#L135). The attribute's comment: “condition (4) for the étale site of an algebraic stack quasi-separated over a quasi-separated base scheme, with the collection B of Stacks 0GQV: the objects of the site lying over affine schemes; the family produced has one member, as in the source”.

> **Condition (4) of Stacks 0GN4 for the étale site of an algebraic stack quasi-separated over a
> quasi-separated base scheme**, in the shape
> `AlgebraicGeometry.Stack.isIso_colimit_post_rightDerived_globalSections_etale` consumes as its
> hypothesis `h_equalizer`: for two objects `x`, `x'` of the étale site lying over affine schemes and
> two morphisms `a, b : x ⟶ x'` there is a finite family of such objects, each with a morphism to `x`
> equalizing `a` and `b`, whose sheafified representables jointly cover the equalizer of `h_a^#` and
> `h_b^#`.
>
> This is
> `AlgebraicGeometry.Stack`
> `.exists_fin_affineObjects_isLocallySurjective_equalizerLift_associatedTopology` at the big étale
> topology, its fibre-lifting hypothesis discharged by **Stacks 06XH** part (2),
> `AlgebraicGeometry.Stack.exists_etaleCovering_fibre_lift`, which reads the fibre lifts of a
> surjective smooth 1-morphism off an *étale* covering of the base. The affine smooth presentation of
> **Stacks 04YC** is smooth and surjective, which is exactly what that tag asks for, so the étale
> case needs nothing of the presentation beyond what the fppf case needs — in particular no affine
> étale presentation of a quasi-compact algebraic stack. The family has one member, as in the
> source.
>
> The fppf statement is the same result at
> `AlgebraicGeometry.BigFppfSite.topology`,
> `AlgebraicGeometry.Stack.exists_fin_affineObjects_isLocallySurjective_equalizerLift`, where
> **Stacks 06QA** discharges the hypothesis instead.

```lean
theorem exists_fin_affineObjects_isLocallySurjective_equalizerLift_etale
    (hqsS : QuasiSeparatedSpace S) (h𝒳 : IsQuasiSeparatedOver.{u, w} B S hS 𝒳) :
    ∀ {U U' : 𝒳.val.val.obj} (u v : U ⟶ U'),
      U ∈ affineObjects B S hS 𝒳.val → U' ∈ affineObjects B S hS 𝒳.val →
      ∃ (m : ℕ) (V : Fin m → 𝒳.val.val.obj),
        (∀ i, V i ∈ affineObjects B S hS 𝒳.val) ∧
          ∃ (p : ∀ i, V i ⟶ U) (hp : ∀ i, p i ≫ u = p i ≫ v),
          Sheaf.IsLocallySurjective (Limits.Sigma.desc fun i =>
            equalizer.lift
              (f := (Sheaf.sheafifiedYoneda
                (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))).map u)
              (g := (Sheaf.sheafifiedYoneda
                (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))).map v)
              ((Sheaf.sheafifiedYoneda
                (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))).map (p i)) (by
                simpa only [Functor.map_comp] using
                  congrArg (Sheaf.sheafifiedYoneda
                    (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))).map (hp i)))
```

**`Stacks.Cohomology.ColimitsOfCohomology.isQuasiCompact_of_finiteCoproductSheafifiedYoneda`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FilteredColimits/FiniteCoproductsOfRepresentables.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FilteredColimits/FiniteCoproductsOfRepresentables.lean#L168). The attribute's comment: “quasi-compactness assertion”.

> **Stacks 0GN4, quasi-compactness assertion.** If every covering of every `U ∈ B` is refined by
> a finite covering family with sources in `B` — condition (2) — then every finite coproduct of
> sheafified representables of objects of `B` is a quasi-compact sheaf.
>
> Condition (2) makes each `U ∈ B` a quasi-compact object of the site, hence each `h_U^#` a
> quasi-compact sheaf by Stacks 0D06, and a finite coproduct of quasi-compact sheaves is
> quasi-compact by Stacks 0GMQ. The empty coproduct is handled separately, being initial.

```lean
theorem isQuasiCompact_of_finiteCoproductSheafifiedYoneda {C : Type u} [Category.{v} C]
    (J : GrothendieckTopology C) (B : Set C)
    (h_refine : ∀ U ∈ B, HasFiniteCoverRefinementsFrom J B U)
    {K : Sheaf J (Type max u v)} (hK : K ∈ FiniteCoproductSheafifiedYoneda J B) :
    Sheaf.IsQuasiCompact K
```

**`Stacks.Cohomology.ColimitsOfCohomology.isIso_colimit_post_rightDerived_globalSections_of_finite_covers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FilteredColimits/FiniteCoproductsOfRepresentables.lean, line 516](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FilteredColimits/FiniteCoproductsOfRepresentables.lean#L516). The attribute's comment: “criterion”.

> **Stacks 0GN4, the criterion.** Let `C` be a small site and `B ⊆ Ob(C)`, and assume
>
> 1. for some `n ≥ 0` and `U_1, …, U_n ∈ B` the map `∐_i h_{U_i}^# ⟶ *` is surjective,
> 2. every covering of a `U ∈ B` is refined by a finite covering family with sources in `B`,
> 3. for any `U, U' ∈ B` there are finitely many `V_i ∈ B` with maps to both for which
>    `∐_i h_{V_i}^# ⟶ h_U^# ⨯ h_{U'}^#` is surjective, and
> 4. for any `a, b : U ⟶ U'` between members of `B` there are finitely many `V_i ∈ B` with maps to
>    `U` equalizing `a` and `b` for which `∐_i h_{V_i}^# ⟶ Equalizer(h_a^#, h_b^#)` is surjective.
>
> Then `colim_λ H^p(C, F_λ) ⟶ H^p(C, colim_λ F_λ)` is an isomorphism in every degree, for every
> filtered diagram of abelian sheaves.
>
> The proof checks the five hypotheses of Stacks 0GN3 for the set `S` of finite coproducts of
> sheafified representables of objects of `B`. Hypotheses (1), (3) and (4) of Stacks 0GN3 come from
> (1), (3) and (4) here, after rewriting a coproduct of pairings as a map out of a coproduct and
> distributing a coproduct over a product. Hypothesis (2), the lifting property for a surjection
> `G ⟶ K` with `K ∈ S`, is obtained by applying (2) to the sieve of local liftings of the
> tautological section of each summand of `K`: this produces a finite covering of each summand by
> objects of `B` over which the surjection splits, and the resulting coproduct is again in `S`.
> Hypothesis (5) is `isQuasiCompact_of_finiteCoproductSheafifiedYoneda`.

```lean
theorem isIso_colimit_post_rightDerived_globalSections_of_finite_covers
    {C : Type u} [SmallCategory C] (J : GrothendieckTopology C) (B : Set C)
    (h_terminal : ∃ (m : ℕ) (U : Fin m → C),
      (∀ i, U i ∈ B) ∧
        Sheaf.IsLocallySurjective
          (Sigma.desc fun i => terminal.from ((Sheaf.sheafifiedYoneda J).obj (U i))))
    (h_refine : ∀ U ∈ B, HasFiniteCoverRefinementsFrom J B U)
    (h_product : ∀ U ∈ B, ∀ U' ∈ B,
      ∃ (m : ℕ) (V : Fin m → C),
        (∀ i, V i ∈ B) ∧ ∃ (p : ∀ i, V i ⟶ U) (q : ∀ i, V i ⟶ U'),
          Sheaf.IsLocallySurjective (Sigma.desc fun i =>
            prod.lift ((Sheaf.sheafifiedYoneda J).map (p i))
              ((Sheaf.sheafifiedYoneda J).map (q i))))
    (h_equalizer : ∀ {U U' : C} (a b : U ⟶ U'), U ∈ B → U' ∈ B →
      ∃ (m : ℕ) (V : Fin m → C),
        (∀ i, V i ∈ B) ∧ ∃ (p : ∀ i, V i ⟶ U) (hp : ∀ i, p i ≫ a = p i ≫ b),
          Sheaf.IsLocallySurjective (Sigma.desc fun i =>
            equalizer.lift (f := (Sheaf.sheafifiedYoneda J).map a)
              (g := (Sheaf.sheafifiedYoneda J).map b)
              ((Sheaf.sheafifiedYoneda J).map (p i)) (by
              simpa only [Functor.map_comp] using congrArg (Sheaf.sheafifiedYoneda J).map (hp i))))
    (n : ℕ) {I : Type u} [SmallCategory I] [IsFiltered I]
    (F : I ⥤ Sheaf J (Ab.{u})) :
    IsIso (colimit.post F ((Sheaf.Γ J (Ab.{u})).rightDerived n))
```

**`Stacks.Cohomology.ColimitsOfCohomology.isIso_colimit_post_rightDerived_globalSections_of_covers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FilteredColimits/FiniteCoveringCriterionOnALargeSite.lean, line 523](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FilteredColimits/FiniteCoveringCriterionOnALargeSite.lean#L523). The attribute's comment: “criterion, for a site whose objects and morphisms need not share a universe”.

> **Stacks 0GN4 for an arbitrary site.** Let `C` be a site with objects in `Type u₁` and
> morphisms in `Type v`, let `B ⊆ Ob(C)`, and assume
>
> 1. for some `n ≥ 0` and `U_1, …, U_n ∈ B` the map `∐_i h_{U_i}^# ⟶ *` is surjective,
> 2. every covering of a `U ∈ B` is refined by a finite covering family with sources in `B`,
> 3. for any `U, U' ∈ B` there are finitely many `V_i ∈ B` with maps to both for which
>    `∐_i h_{V_i}^# ⟶ h_U^# ⨯ h_{U'}^#` is surjective, and
> 4. for any `a, b : U ⟶ U'` between members of `B` there are finitely many `V_i ∈ B` with maps to
>    `U` equalizing `a` and `b` for which `∐_i h_{V_i}^# ⟶ Equalizer(h_a^#, h_b^#)` is surjective.
>
> Then `colim_λ H^p(C, F_λ) ⟶ H^p(C, colim_λ F_λ)` is an isomorphism in every degree, for every
> filtered diagram of abelian sheaves with sections at the join `max u₁ v` of the two universes of
> the site.
>
> The small-site form of the tag asks for `SmallCategory C`, that is for the objects and the morphisms
> of the site to live in one universe, which the sites of algebraic geometry do not satisfy. Here
> the site is arbitrary, every sheaf of sets and every abelian coefficient living at the join of its
> two universes.
>
> The proof is the source's: it checks the five hypotheses of Stacks 0GN3 for the set `S` of finite
> coproducts of sheafified representables of objects of `B`, and concludes by
> `isIso_colimit_post_rightDerived_globalSections_of_coveringSet`, the form of Stacks 0GN3 for an
> arbitrary site. Hypotheses (1), (3) and (4) of Stacks 0GN3 come from (1), (3) and (4) here, after
> rewriting a coproduct of pairings as a map out of a coproduct and distributing a coproduct over a
> product. Hypothesis (2), the lifting property for a surjection `G ⟶ K` with `K ∈ S`, is obtained
> by applying (2) to the sieve of local liftings of the tautological section of each summand of `K`:
> this produces a finite covering of each summand by objects of `B` over which the surjection
> splits, and the resulting coproduct is again in `S`. Hypothesis (5) is
> `isQuasiCompact_of_finiteCoproductSheafifiedYoneda`, which is already general.

```lean
theorem isIso_colimit_post_rightDerived_globalSections_of_covers
    {C : Type u₁} [Category.{v} C] (J : GrothendieckTopology C) (B : Set C)
    (h_terminal : ∃ (m : ℕ) (U : Fin m → C),
      (∀ i, U i ∈ B) ∧
        Sheaf.IsLocallySurjective
          (Sigma.desc fun i => terminal.from ((Sheaf.sheafifiedYoneda J).obj (U i))))
    (h_refine : ∀ U ∈ B, HasFiniteCoverRefinementsFrom J B U)
    (h_product : ∀ U ∈ B, ∀ U' ∈ B,
      ∃ (m : ℕ) (V : Fin m → C),
        (∀ i, V i ∈ B) ∧ ∃ (p : ∀ i, V i ⟶ U) (q : ∀ i, V i ⟶ U'),
          Sheaf.IsLocallySurjective (Sigma.desc fun i =>
            prod.lift ((Sheaf.sheafifiedYoneda J).map (p i))
              ((Sheaf.sheafifiedYoneda J).map (q i))))
    (h_equalizer : ∀ {U U' : C} (a b : U ⟶ U'), U ∈ B → U' ∈ B →
      ∃ (m : ℕ) (V : Fin m → C),
        (∀ i, V i ∈ B) ∧ ∃ (p : ∀ i, V i ⟶ U) (hp : ∀ i, p i ≫ a = p i ≫ b),
          Sheaf.IsLocallySurjective (Sigma.desc fun i =>
            equalizer.lift (f := (Sheaf.sheafifiedYoneda J).map a)
              (g := (Sheaf.sheafifiedYoneda J).map b)
              ((Sheaf.sheafifiedYoneda J).map (p i)) (by
              simpa only [Functor.map_comp] using congrArg (Sheaf.sheafifiedYoneda J).map (hp i))))
    (n : ℕ) {I : Type max u₁ v} [SmallCategory I] [IsFiltered I]
    (F : I ⥤ Sheaf J (Ab.{max u₁ v})) :
    IsIso (colimit.post F ((Sheaf.Γ J (Ab.{max u₁ v})).rightDerived n))
```

## Tag 0H7B, a lemma

[Tag 0H7B](https://stacks.math.columbia.edu/tag/0H7B) in the Stacks Project.

**`Stacks.Cohomology.HigherDirectImage.preservesColimit_rightDerived_sheafPushforwardContinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/HigherDirectImage/FilteredColimits.lean, line 409](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/HigherDirectImage/FilteredColimits.lean#L409).

> Let `u : D ⥤ C` be the continuous functor associated to a morphism of sites and let `F` be
> a diagram of abelian sheaves on `C`. If every object of `D` has a cover by objects over which
> degree-`p` cohomology commutes with the colimit of `F`, then the degree-`p` higher direct image
> commutes with that colimit.

```lean
public theorem preservesColimit_rightDerived_sheafPushforwardContinuous
    {C : Type a} {D : Type d} [SmallCategory C] [SmallCategory D]
    (J : GrothendieckTopology C) (K : GrothendieckTopology D)
    [HasSheafify J (Ab.{b})] [HasSheafify K (Ab.{b})]
    [EnoughInjectives (Sheaf J (Ab.{b}))]
    (u : D ⥤ C) [u.IsContinuous K J]
    (p : ℕ) {I : Type c} [SmallCategory I]
    (F : I ⥤ Sheaf J (Ab.{b}))
    (h : ∀ V : D, ∃ E : PreZeroHypercover.{d} V, E.sieve₀ ∈ K V ∧
      ∀ i : E.I₀, PreservesColimit F
        (((sheafSections J (Ab.{b})).obj (op (u.obj (E.X i)))).rightDerived p)) :
    PreservesColimit F
      ((u.sheafPushforwardContinuous (Ab.{b}) K J).rightDerived p)
```

## Tag 0EXZ, a lemma

[Tag 0EXZ](https://stacks.math.columbia.edu/tag/0EXZ) in the Stacks Project.

**`InverseSystemOfFiniteSites.AbelianSheafSystem.exists_mono_to_pointwise_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/InverseSystem/CohomologyOfColimitOfFiniteSites/AbelianSystemsAndSections.lean, line 1053](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/InverseSystem/CohomologyOfColimitOfFiniteSites/AbelianSystemsAndSections.lean#L1053). The attribute's comment: “weak-system variant (Stacks 00VH finite coverings)”.

> **Stacks 0EXZ.** Every system of abelian sheaves on an inverse system of sites admits a
> levelwise monomorphism to a system whose sheaf at every index is injective.

```lean
theorem exists_mono_to_pointwise_injective {D : InverseSystemOfFiniteSites.{v, u, w}}
    (F : AbelianSheafSystem.{v, u, w, t} D) :
    ∃ (G : AbelianSheafSystem.{v, u, w, t} D) (f : Hom.{v, u, w, t} F G),
      (∀ i, Mono (f.app i)) ∧ ∀ i, Injective (G.obj i)
```

**`InverseSystemOfSites.AbelianSheafSystem.exists_mono_to_pointwise_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/InverseSystem/InjectiveSystemsOnStrongSystems.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/InverseSystem/InjectiveSystemsOnStrongSystems.lean#L90).

> **Stacks 0EXZ.** Every system of abelian sheaves on an inverse system of sites admits a
> levelwise monomorphism to a system whose sheaf at every index is injective.
>
> The system here is one on an `InverseSystemOfSites`, that is on a system of sites all of whose
> covering sieves are finitely generated; see
> `InverseSystemOfFiniteSites.AbelianSheafSystem.exists_mono_to_pointwise_injective` for the same
> statement over the source-faithful finiteness condition of Stacks 00VH, which is where the
> construction of the source's proof is carried out, and of which this is the reading along
> `InverseSystemOfSites.toInverseSystemOfFiniteSites`.

```lean
theorem AbelianSheafSystem.exists_mono_to_pointwise_injective
    {D : InverseSystemOfSites.{v, u, w}} (F : AbelianSheafSystem.{v, u, w, t} D) :
    ∃ (G : AbelianSheafSystem.{v, u, w, t} D) (f : AbelianSheafSystem.Hom.{v, u, w, t} F G),
      (∀ i, Mono (f.app i)) ∧ ∀ i, Injective (G.obj i)
```

## Tag 09YP, a lemma

[Tag 09YP](https://stacks.math.columbia.edu/tag/09YP) in the Stacks Project.

**`Stacks.WeakSites.ColimitSiteCohomology.cohomologyCocone`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/InverseSystem/CohomologyOfColimitOfFiniteSites/CohomologyColimit.lean, line 2443](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/InverseSystem/CohomologyOfColimitOfFiniteSites/CohomologyColimit.lean#L2443). The attribute's comment: “weak-system variant (Stacks 00VH finite coverings): canonical cohomology diagram and cocone”.

> **Stacks 09YP, the canonical cohomology diagram and its cocone.** In the situation of
> Stacks 0EXZ, with the functors `uC i` exhibiting `C` as the colimit of the sites of the system
> (Stacks 09YL and 0A35) and with `𝒢 = colim fᵢ⁻¹Fᵢ`, the cohomology groups `Hᵖ(u_a(X), F_j)`
> over the arrows `a : j ⟶ i` form a diagram whose arrows are the canonical cohomology maps,
> together with the canonical cocone at `Hᵖ(uᵢ(X), 𝒢)`.

```lean
public def cohomologyCocone : CohomologyCocone.{v, u, max u v w, max u v w} D uC hu K F 𝒢 ι i X p
```

**`Stacks.WeakSites.ColimitSiteCohomology.isColimitCohomologyCocone`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/InverseSystem/CohomologyOfColimitOfFiniteSites/CohomologyColimit.lean, line 2521](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/InverseSystem/CohomologyOfColimitOfFiniteSites/CohomologyColimit.lean#L2521). The attribute's comment: “weak-system variant (Stacks 00VH finite coverings): the canonical cocone is a colimit cocone”.

> **Stacks 09YP.** In the situation of Stacks 0EXZ, set `𝒢 = colim fᵢ⁻¹Fᵢ`. For every index
> `i`, every object `X` of the site at `i` and every `p`, the cohomology `Hᵖ(uᵢ(X), 𝒢)` is the
> filtered colimit, over the arrows `a : j ⟶ i`, of the cohomology groups `Hᵖ(u_a(X), F_j)`: the
> canonical cocone is a colimit cocone. The case `p = 0` is Stacks 09YN.
>
> The colimit structure is a choice; it is unique, `CategoryTheory.Limits.IsColimit` being a
> subsingleton.

```lean
public def isColimitCohomologyCocone
    (E : CohomologyCocone.{v, u, max u v w, max u v w} D uC hu K F 𝒢 ι i X p :=
      cohomologyCocone.{v, u, w} D uC hu hobj hhom hhom_inj K hK F 𝒢 ι hcolim
        i X p) :
    IsColimit E.cocone
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.16, Tag 0737](https://stacks.math.columbia.edu/tag/0737)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
