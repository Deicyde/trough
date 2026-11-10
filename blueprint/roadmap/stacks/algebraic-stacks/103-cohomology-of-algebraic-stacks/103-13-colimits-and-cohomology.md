---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isIso_colimit_post_rightDerived_globalSections_associatedTopology, AlgebraicGeometry.Stack.isIso_colimit_post_rightDerived_globalSections_fppf, AlgebraicGeometry.Stack.isIso_colimit_post_rightDerived_globalSections_etale, AlgebraicGeometry.Stack.isIso_colimit_post_rightDerived_globalSections_fppf_of_isQuasiCompactStack, AlgebraicGeometry.Stack.isIso_colimit_post_rightDerived_globalSections_etale_of_isQuasiCompactStack, AlgebraicGeometry.Stack.isIso_colimit_post_rightDerived_globalSections_fppf_of_isQuasiCompact_absolute, AlgebraicGeometry.Stack.isIso_colimit_post_rightDerived_globalSections_etale_of_isQuasiCompact_absolute, AlgebraicGeometry.Stack.hasFiniteCoverRefinementsFrom_fppfTopology
statement: formalized
proof: formalized
---

# 103.13 Colimits and cohomology

Section 103.13 of the Stacks Project, [Tag 0GQU](https://stacks.math.columbia.edu/tag/0GQU). 5 tags here are carried by 26 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GQV, a lemma

[Tag 0GQV](https://stacks.math.columbia.edu/tag/0GQV) in the Stacks Project.

**`AlgebraicGeometry.Stack.isIso_colimit_post_rightDerived_globalSections_associatedTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomology.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomology.lean#L246). The attribute's comment: “the site-theoretic step, at an arbitrary one of the five topologies of Stacks 06TP, hence for the fppf and the étale assertion alike; all four conditions of 0GN4 are assumed here”.

> **Stacks 0GQV at any one of the sites of Stacks 06TP, from all four conditions of
> Stacks 0GN4.** Let `𝒳` be a category fibred in groupoids over the big fppf category of a scheme
> `S` contained in a big fppf site, let `τ` be a topology on the underlying category of schemes of
> `B`, give the total category of `𝒳` the topology it inherits from `τ` localized at `S`
> (Stacks 06TP), and assume of the collection `affineObjects` of its objects lying over affine
> schemes that
>
> 1. finitely many of them have sheafified representables jointly covering the final sheaf,
> 2. every covering sieve of a member of it contains a finite covering family by members of it,
> 3. the product of the sheafified representables of two of them is covered by a finite coproduct of
>    sheafified representables of members of it, and
> 4. the equalizer of the sheafified representables of two parallel morphisms between members of it
>    is covered by such a finite coproduct.
>
> Then `colim_i H^p(𝒳, F_i) ⟶ H^p(𝒳, colim_i F_i)` is an isomorphism in every degree `p`, for every
> filtered diagram `F` of abelian sheaves on that site.
>
> This is the site-theoretic step of the source's proof, and the source takes it at two values of
> `τ`: the big fppf topology and the big étale topology. Nothing below uses which topology was
> chosen — the step is an instance of
> `Stacks.Cohomology.ColimitsOfCohomology.isIso_colimit_post_rightDerived_globalSections_of_covers`,
> the form of Stacks 0GN4 for a site whose objects and morphisms do not share a universe, and the
> site of a category fibred in groupoids over the big fppf category of `S` does not, its objects
> lying in `Type (u + 1)` and its morphisms in `Type u`. Coefficients, sheaves of sets and the index
> category of the diagram all live at the join `u + 1` of those two universes.
>
> So the two assertions of the source differ only in the four conditions fed to this result. Its
> fppf and étale instances are
> `AlgebraicGeometry.Stack.isIso_colimit_post_rightDerived_globalSections_fppf`, where condition (2)
> is discharged, and
> `AlgebraicGeometry.Stack.isIso_colimit_post_rightDerived_globalSections_etale`, where none of the
> four is; see "What is proved and what is assumed" in the module docstring for the state of each
> condition in each topology.

```lean
theorem isIso_colimit_post_rightDerived_globalSections_associatedTopology
    (τ : GrothendieckTopology B.Schemes)
    (h_terminal : ∃ (m : ℕ) (U : Fin m → 𝒳.val.obj),
      (∀ i, U i ∈ affineObjects B S hS 𝒳) ∧
        Sheaf.IsLocallySurjective
          (Limits.Sigma.desc fun i => terminal.from
            ((Sheaf.sheafifiedYoneda (associatedTopology B S hS 𝒳.val.p τ)).obj (U i))))
    (h_refine : ∀ x ∈ affineObjects B S hS 𝒳,
      HasFiniteCoverRefinementsFrom (associatedTopology B S hS 𝒳.val.p τ)
        (affineObjects B S hS 𝒳) x)
    (h_product : ∀ U ∈ affineObjects B S hS 𝒳, ∀ U' ∈ affineObjects B S hS 𝒳,
      ∃ (m : ℕ) (V : Fin m → 𝒳.val.obj),
        (∀ i, V i ∈ affineObjects B S hS 𝒳) ∧
          ∃ (p : ∀ i, V i ⟶ U) (q : ∀ i, V i ⟶ U'),
          Sheaf.IsLocallySurjective (Limits.Sigma.desc fun i =>
            prod.lift ((Sheaf.sheafifiedYoneda (associatedTopology B S hS 𝒳.val.p τ)).map (p i))
              ((Sheaf.sheafifiedYoneda (associatedTopology B S hS 𝒳.val.p τ)).map (q i))))
    (h_equalizer : ∀ {U U' : 𝒳.val.obj} (a b : U ⟶ U'),
      U ∈ affineObjects B S hS 𝒳 → U' ∈ affineObjects B S hS 𝒳 →
      ∃ (m : ℕ) (V : Fin m → 𝒳.val.obj),
        (∀ i, V i ∈ affineObjects B S hS 𝒳) ∧
          ∃ (p : ∀ i, V i ⟶ U) (hp : ∀ i, p i ≫ a = p i ≫ b),
          Sheaf.IsLocallySurjective (Limits.Sigma.desc fun i =>
            equalizer.lift
              (f := (Sheaf.sheafifiedYoneda (associatedTopology B S hS 𝒳.val.p τ)).map a)
              (g := (Sheaf.sheafifiedYoneda (associatedTopology B S hS 𝒳.val.p τ)).map b)
              ((Sheaf.sheafifiedYoneda (associatedTopology B S hS 𝒳.val.p τ)).map (p i)) (by
                simpa only [Functor.map_comp] using
                  congrArg (Sheaf.sheafifiedYoneda (associatedTopology B S hS 𝒳.val.p τ)).map
                    (hp i))))
    (p : ℕ) {I : Type (u + 1)} [SmallCategory I] [IsFiltered I]
    (F : I ⥤ Sheaf (associatedTopology B S hS 𝒳.val.p τ) Ab.{u + 1}) :
    IsIso (colimit.post F
      ((Sheaf.Γ (associatedTopology B S hS 𝒳.val.p τ) Ab.{u + 1}).rightDerived p))
```

**`AlgebraicGeometry.Stack.isIso_colimit_post_rightDerived_globalSections_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomology.lean, line 311](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomology.lean#L311). The attribute's comment: “the site-theoretic step for the fppf site; conditions (1), (3) and (4) of 0GN4 are assumed here”.

> **Stacks 0GQV in the fppf topology, from conditions (1), (3) and (4) of Stacks 0GN4.** Let `𝒳`
> be a category fibred in groupoids over the big fppf category of a scheme `S` contained in a big
> fppf site, give its total category the fppf topology of Stacks 06TP, and assume of the collection
> `affineObjects` of its objects lying over affine schemes that
>
> 1. finitely many of them have sheafified representables jointly covering the final sheaf,
> 3. the product of the sheafified representables of two of them is covered by a finite coproduct of
>    sheafified representables of members of it, and
> 4. the equalizer of the sheafified representables of two parallel morphisms between members of it
>    is covered by such a finite coproduct.
>
> Then `colim_i H^p(𝒳, F_i) ⟶ H^p(𝒳, colim_i F_i)` is an isomorphism in every degree `p`, for every
> filtered diagram `F` of abelian fppf sheaves on `𝒳`.
>
> Condition (2) of Stacks 0GN4 is not assumed: it holds for every category fibred in groupoids, by
> `AlgebraicGeometry.Stack.hasFiniteCoverRefinementsFrom_fppfTopology`. Conditions (1), (3) and (4)
> are what the source derives from quasi-compactness and quasi-separatedness of an algebraic stack;
> see "What is proved and what is assumed" in the module docstring for the state of each, and
> `Stack.isIso_colimit_post_rightDerived_globalSections_fppf_of_isQuasiCompactStack` below for the
> form of this result in which (1) too is discharged.
>
> This is the fppf instance of
> `AlgebraicGeometry.Stack.isIso_colimit_post_rightDerived_globalSections_associatedTopology`, the
> site-theoretic step taken at an arbitrary topology; the fppf topology of Stacks 06TP is that
> construction at `AlgebraicGeometry.BigFppfSite.topology`.

```lean
theorem isIso_colimit_post_rightDerived_globalSections_fppf
    (h_terminal : ∃ (m : ℕ) (U : Fin m → 𝒳.val.obj),
      (∀ i, U i ∈ affineObjects B S hS 𝒳) ∧
        Sheaf.IsLocallySurjective
          (Limits.Sigma.desc fun i => terminal.from
            ((Sheaf.sheafifiedYoneda (fppfTopology B S hS 𝒳)).obj (U i))))
    (h_product : ∀ U ∈ affineObjects B S hS 𝒳, ∀ U' ∈ affineObjects B S hS 𝒳,
      ∃ (m : ℕ) (V : Fin m → 𝒳.val.obj),
        (∀ i, V i ∈ affineObjects B S hS 𝒳) ∧
          ∃ (p : ∀ i, V i ⟶ U) (q : ∀ i, V i ⟶ U'),
          Sheaf.IsLocallySurjective (Limits.Sigma.desc fun i =>
            prod.lift ((Sheaf.sheafifiedYoneda (fppfTopology B S hS 𝒳)).map (p i))
              ((Sheaf.sheafifiedYoneda (fppfTopology B S hS 𝒳)).map (q i))))
    (h_equalizer : ∀ {U U' : 𝒳.val.obj} (a b : U ⟶ U'),
      U ∈ affineObjects B S hS 𝒳 → U' ∈ affineObjects B S hS 𝒳 →
      ∃ (m : ℕ) (V : Fin m → 𝒳.val.obj),
        (∀ i, V i ∈ affineObjects B S hS 𝒳) ∧
          ∃ (p : ∀ i, V i ⟶ U) (hp : ∀ i, p i ≫ a = p i ≫ b),
          Sheaf.IsLocallySurjective (Limits.Sigma.desc fun i =>
            equalizer.lift
              (f := (Sheaf.sheafifiedYoneda (fppfTopology B S hS 𝒳)).map a)
              (g := (Sheaf.sheafifiedYoneda (fppfTopology B S hS 𝒳)).map b)
              ((Sheaf.sheafifiedYoneda (fppfTopology B S hS 𝒳)).map (p i)) (by
                simpa only [Functor.map_comp] using
                  congrArg (Sheaf.sheafifiedYoneda (fppfTopology B S hS 𝒳)).map (hp i))))
    (p : ℕ) {I : Type (u + 1)} [SmallCategory I] [IsFiltered I]
    (F : I ⥤ Sheaf (fppfTopology B S hS 𝒳) Ab.{u + 1}) :
    IsIso (colimit.post F
      ((Sheaf.Γ (fppfTopology B S hS 𝒳) Ab.{u + 1}).rightDerived p))
```

**`AlgebraicGeometry.Stack.isIso_colimit_post_rightDerived_globalSections_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomology.lean, line 372](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomology.lean#L372). The attribute's comment: “the second assertion, in the étale topology: the site-theoretic step for the étale site of Stacks 06TP; conditions (1), (3) and (4) of 0GN4 are assumed here”.

> **The second assertion of Stacks 0GQV: the same statement in the étale topology**, from
> conditions (1), (3) and (4) of Stacks 0GN4. Let `𝒳` be a category fibred in groupoids over the
> big fppf category of a scheme `S` contained in a big fppf site, give its total category the
> *étale* topology of Stacks 06TP — the one it inherits from the big étale topology
> `AlgebraicGeometry.etaleTopology` of Stacks 03FF localized at `S` — and assume of the collection
> `affineObjects` of its objects lying over affine schemes those three conditions. Then
> `colim_i H^p(𝒳, F_i) ⟶ H^p(𝒳, colim_i F_i)` is an isomorphism in every degree `p`, for every
> filtered diagram `F` of abelian étale sheaves on `𝒳`.
>
> This is
> `AlgebraicGeometry.Stack.isIso_colimit_post_rightDerived_globalSections_associatedTopology` at the
> big étale topology, and it is the shape in which the source's second assertion — "the same is true
> for abelian sheaves on `𝒳_étale` taking cohomology in the étale topology" — becomes a statement of
> this library.
>
> Condition (2) of Stacks 0GN4 is not assumed, exactly as in the fppf case: it holds for every
> category fibred in groupoids, by
> `AlgebraicGeometry.Stack.hasFiniteCoverRefinementsFrom_etaleTopology`, whose geometric input is
> **Stacks 0218** where the fppf proof uses Stacks 021P. Condition (1) is likewise available for
> the étale site, by
> `AlgebraicGeometry.Stack.exists_isAffineObject_isLocallySurjective_terminal_from_etale`, and
> `AlgebraicGeometry.Stack`
> `.isIso_colimit_post_rightDerived_globalSections_etale_of_isQuasiCompactStack`
> is the form of this result in which it too is discharged. Conditions (3) and (4) remain open for
> the étale site; see "What is proved and what is assumed" in the module docstring for the state of
> each of the four.

```lean
theorem isIso_colimit_post_rightDerived_globalSections_etale
    (h_terminal : ∃ (m : ℕ) (U : Fin m → 𝒳.val.obj),
      (∀ i, U i ∈ affineObjects B S hS 𝒳) ∧
        Sheaf.IsLocallySurjective
          (Limits.Sigma.desc fun i => terminal.from
            ((Sheaf.sheafifiedYoneda
              (associatedTopology B S hS 𝒳.val.p (etaleTopology B))).obj (U i))))
    (h_product : ∀ U ∈ affineObjects B S hS 𝒳, ∀ U' ∈ affineObjects B S hS 𝒳,
      ∃ (m : ℕ) (V : Fin m → 𝒳.val.obj),
        (∀ i, V i ∈ affineObjects B S hS 𝒳) ∧
          ∃ (p : ∀ i, V i ⟶ U) (q : ∀ i, V i ⟶ U'),
          Sheaf.IsLocallySurjective (Limits.Sigma.desc fun i =>
            prod.lift ((Sheaf.sheafifiedYoneda
                (associatedTopology B S hS 𝒳.val.p (etaleTopology B))).map (p i))
              ((Sheaf.sheafifiedYoneda
                (associatedTopology B S hS 𝒳.val.p (etaleTopology B))).map (q i))))
    (h_equalizer : ∀ {U U' : 𝒳.val.obj} (a b : U ⟶ U'),
      U ∈ affineObjects B S hS 𝒳 → U' ∈ affineObjects B S hS 𝒳 →
      ∃ (m : ℕ) (V : Fin m → 𝒳.val.obj),
        (∀ i, V i ∈ affineObjects B S hS 𝒳) ∧
          ∃ (p : ∀ i, V i ⟶ U) (hp : ∀ i, p i ≫ a = p i ≫ b),
          Sheaf.IsLocallySurjective (Limits.Sigma.desc fun i =>
            equalizer.lift
              (f := (Sheaf.sheafifiedYoneda
                (associatedTopology B S hS 𝒳.val.p (etaleTopology B))).map a)
              (g := (Sheaf.sheafifiedYoneda
                (associatedTopology B S hS 𝒳.val.p (etaleTopology B))).map b)
              ((Sheaf.sheafifiedYoneda
                (associatedTopology B S hS 𝒳.val.p (etaleTopology B))).map (p i)) (by
                simpa only [Functor.map_comp] using
                  congrArg (Sheaf.sheafifiedYoneda
                    (associatedTopology B S hS 𝒳.val.p (etaleTopology B))).map (hp i))))
    (p : ℕ) {I : Type (u + 1)} [SmallCategory I] [IsFiltered I]
    (F : I ⥤ Sheaf (associatedTopology B S hS 𝒳.val.p (etaleTopology B)) Ab.{u + 1}) :
    IsIso (colimit.post F
      ((Sheaf.Γ (associatedTopology B S hS 𝒳.val.p (etaleTopology B))
        Ab.{u + 1}).rightDerived p))
```

**`AlgebraicGeometry.Stack.isIso_colimit_post_rightDerived_globalSections_fppf_of_isQuasiCompactStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomology.lean, line 488](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomology.lean#L488). The attribute's comment: “for a quasi-compact algebraic stack; conditions (3) and (4) of 0GN4 are assumed”.

> **Stacks 0GQV in the fppf topology for a quasi-compact algebraic stack, from conditions (3) and
> (4) of Stacks 0GN4.** Let `𝒴` be a quasi-compact algebraic stack over a scheme `S` contained in a
> big fppf site and assume of the collection `affineObjects` of the objects of its fppf site lying
> over affine schemes that
>
> 3. the product of the sheafified representables of two of them is covered by a finite coproduct of
>    sheafified representables of members of it, and
> 4. the equalizer of the sheafified representables of two parallel morphisms between members of it
>    is covered by such a finite coproduct.
>
> Then `colim_i H^p(𝒴, F_i) ⟶ H^p(𝒴, colim_i F_i)` is an isomorphism in every degree `p`, for every
> filtered diagram `F` of abelian fppf sheaves on `𝒴`.
>
> This is `AlgebraicGeometry.Stack.isIso_colimit_post_rightDerived_globalSections_fppf` with its
> condition (1) discharged from quasi-compactness by
> `AlgebraicGeometry.Stack.exists_isAffineObject_isLocallySurjective_terminal_from`. The hypothesis
> is stated for an `AlgebraicGeometry.Stack.AlgebraicStacks` rather than for a bare category fibred
> in groupoids because that is what Stacks 04YC and Stacks 075S are about; the conclusion is the one
> of the previous result at the underlying category fibred in groupoids.
>
> Conditions (3) and (4) are the two the source derives from quasi-separatedness of `𝒴`, and both
> are available: (3) is
> `AlgebraicGeometry.Stack.exists_fin_affineObjects_isLocallySurjective_prodLift` and (4) is
> `AlgebraicGeometry.Stack.exists_fin_affineObjects_isLocallySurjective_equalizerLift`, each for a
> stack quasi-separated over a quasi-separated base scheme. They are hypotheses here because this
> statement asks nothing of quasi-separatedness — no hypothesis of it appears, the two conditions
> standing in for it — so this is not the full assertion of Stacks 0GQV, whose hypotheses are
> quasi-compactness and quasi-separatedness alone. That assertion is
> `AlgebraicGeometry.Stack.isIso_colimit_post_rightDerived_globalSections_fppf_of_isQuasiCompact`,
> in `StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomologyEqualizerAffineCover.lean`. See
> "What is proved and what is assumed" in the module docstring.

```lean
theorem isIso_colimit_post_rightDerived_globalSections_fppf_of_isQuasiCompactStack
    (𝒴 : AlgebraicStacks.{u, w} B S hS)
    (hqc : IsQuasiCompactStack.{u, w} B S hS 𝒴.val 𝒴.property)
    (h_product : ∀ U ∈ affineObjects B S hS 𝒴.val, ∀ U' ∈ affineObjects B S hS 𝒴.val,
      ∃ (m : ℕ) (V : Fin m → 𝒴.val.val.obj),
        (∀ i, V i ∈ affineObjects B S hS 𝒴.val) ∧
          ∃ (p : ∀ i, V i ⟶ U) (q : ∀ i, V i ⟶ U'),
          Sheaf.IsLocallySurjective (Limits.Sigma.desc fun i =>
            prod.lift ((Sheaf.sheafifiedYoneda (fppfTopology B S hS 𝒴.val)).map (p i))
              ((Sheaf.sheafifiedYoneda (fppfTopology B S hS 𝒴.val)).map (q i))))
    (h_equalizer : ∀ {U U' : 𝒴.val.val.obj} (a b : U ⟶ U'),
      U ∈ affineObjects B S hS 𝒴.val → U' ∈ affineObjects B S hS 𝒴.val →
      ∃ (m : ℕ) (V : Fin m → 𝒴.val.val.obj),
        (∀ i, V i ∈ affineObjects B S hS 𝒴.val) ∧
          ∃ (p : ∀ i, V i ⟶ U) (hp : ∀ i, p i ≫ a = p i ≫ b),
          Sheaf.IsLocallySurjective (Limits.Sigma.desc fun i =>
            equalizer.lift
              (f := (Sheaf.sheafifiedYoneda (fppfTopology B S hS 𝒴.val)).map a)
              (g := (Sheaf.sheafifiedYoneda (fppfTopology B S hS 𝒴.val)).map b)
              ((Sheaf.sheafifiedYoneda (fppfTopology B S hS 𝒴.val)).map (p i)) (by
                simpa only [Functor.map_comp] using
                  congrArg (Sheaf.sheafifiedYoneda (fppfTopology B S hS 𝒴.val)).map (hp i))))
    (p : ℕ) {I : Type (u + 1)} [SmallCategory I] [IsFiltered I]
    (F : I ⥤ Sheaf (fppfTopology B S hS 𝒴.val) Ab.{u + 1}) :
    IsIso (colimit.post F
      ((Sheaf.Γ (fppfTopology B S hS 𝒴.val) Ab.{u + 1}).rightDerived p))
```

**`AlgebraicGeometry.Stack.isIso_colimit_post_rightDerived_globalSections_etale_of_isQuasiCompactStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomology.lean, line 549](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomology.lean#L549). The attribute's comment: “the second assertion, in the étale topology, for a quasi-compact algebraic stack; conditions (1) and (2) of 0GN4 are now proved for the étale site, conditions (3) and (4) are assumed”.

> **The second assertion of Stacks 0GQV, in the étale topology, for a quasi-compact algebraic
> stack, from conditions (3) and (4) of Stacks 0GN4.** Let `𝒴` be a quasi-compact algebraic
> stack over a scheme `S` contained in a big fppf site and assume of the collection `affineObjects`
> of the objects of its *étale* site lying over affine schemes that
>
> 3. the product of the sheafified representables of two of them is covered by a finite coproduct of
>    sheafified representables of members of it, and
> 4. the equalizer of the sheafified representables of two parallel morphisms between members of it
>    is covered by such a finite coproduct.
>
> Then `colim_i H^p(𝒴, F_i) ⟶ H^p(𝒴, colim_i F_i)` is an isomorphism in every degree `p`, for every
> filtered diagram `F` of abelian étale sheaves on `𝒴`.
>
> This is `AlgebraicGeometry.Stack.isIso_colimit_post_rightDerived_globalSections_etale` with its
> condition (1) discharged from quasi-compactness by
> `AlgebraicGeometry.Stack.exists_isAffineObject_isLocallySurjective_terminal_from_etale`, exactly as
> `Stack.isIso_colimit_post_rightDerived_globalSections_fppf_of_isQuasiCompactStack` discharges it in
> the fppf topology — the two use **Stacks 06XH** part (2) and **Stacks 06QA** respectively on the
> one affine smooth presentation of **Stacks 04YC**.
>
> Condition (2) is not assumed, as it is not in the fppf case: for the étale site it is
> `AlgebraicGeometry.Stack.hasFiniteCoverRefinementsFrom_etaleTopology`, whose geometric input is
> Stacks 0218 where the fppf proof uses Stacks 021P. Conditions (3) and (4) are open in both
> topologies for the same reasons, about the 2-fibre products the source covers rather than about
> the topology; see "What is proved and what is assumed" in the module docstring. So this is *not*
> the full second assertion of Stacks 0GQV, whose hypotheses are quasi-compactness and
> quasi-separatedness alone; in particular no hypothesis of quasi-separatedness appears here at
> all, the two conditions standing in for it.

```lean
theorem isIso_colimit_post_rightDerived_globalSections_etale_of_isQuasiCompactStack
    (𝒴 : AlgebraicStacks.{u, w} B S hS)
    (hqc : IsQuasiCompactStack.{u, w} B S hS 𝒴.val 𝒴.property)
    (h_product : ∀ U ∈ affineObjects B S hS 𝒴.val, ∀ U' ∈ affineObjects B S hS 𝒴.val,
      ∃ (m : ℕ) (V : Fin m → 𝒴.val.val.obj),
        (∀ i, V i ∈ affineObjects B S hS 𝒴.val) ∧
          ∃ (p : ∀ i, V i ⟶ U) (q : ∀ i, V i ⟶ U'),
          Sheaf.IsLocallySurjective (Limits.Sigma.desc fun i =>
            prod.lift ((Sheaf.sheafifiedYoneda
                (associatedTopology B S hS 𝒴.val.val.p (etaleTopology B))).map (p i))
              ((Sheaf.sheafifiedYoneda
                (associatedTopology B S hS 𝒴.val.val.p (etaleTopology B))).map (q i))))
    (h_equalizer : ∀ {U U' : 𝒴.val.val.obj} (a b : U ⟶ U'),
      U ∈ affineObjects B S hS 𝒴.val → U' ∈ affineObjects B S hS 𝒴.val →
      ∃ (m : ℕ) (V : Fin m → 𝒴.val.val.obj),
        (∀ i, V i ∈ affineObjects B S hS 𝒴.val) ∧
          ∃ (p : ∀ i, V i ⟶ U) (hp : ∀ i, p i ≫ a = p i ≫ b),
          Sheaf.IsLocallySurjective (Limits.Sigma.desc fun i =>
            equalizer.lift
              (f := (Sheaf.sheafifiedYoneda
                (associatedTopology B S hS 𝒴.val.val.p (etaleTopology B))).map a)
              (g := (Sheaf.sheafifiedYoneda
                (associatedTopology B S hS 𝒴.val.val.p (etaleTopology B))).map b)
              ((Sheaf.sheafifiedYoneda
                (associatedTopology B S hS 𝒴.val.val.p (etaleTopology B))).map (p i)) (by
                simpa only [Functor.map_comp] using
                  congrArg (Sheaf.sheafifiedYoneda
                    (associatedTopology B S hS 𝒴.val.val.p (etaleTopology B))).map (hp i))))
    (p : ℕ) {I : Type (u + 1)} [SmallCategory I] [IsFiltered I]
    (F : I ⥤ Sheaf (associatedTopology B S hS 𝒴.val.val.p (etaleTopology B)) Ab.{u + 1}) :
    IsIso (colimit.post F
      ((Sheaf.Γ (associatedTopology B S hS 𝒴.val.val.p (etaleTopology B))
        Ab.{u + 1}).rightDerived p))
```

**`AlgebraicGeometry.Stack.isIso_colimit_post_rightDerived_globalSections_fppf_of_isQuasiCompact_absolute`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomologyAbsolute.lean, line 730](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomologyAbsolute.lean#L730). The attribute's comment: “the first assertion, in the fppf topology; all four conditions of 0GN4 proved, under the source's own hypotheses -- quasi-compactness of the stack and its absolute quasi-separatedness, with nothing asked of the base scheme of the site”.

> **Stacks 0GQV in the fppf topology: on a quasi-compact and quasi-separated algebraic stack,
> cohomology commutes with filtered colimits.** Let `𝒳` be such a stack and give its total category
> the fppf topology of Stacks 06TP. Then `colim_i H^p(𝒳, F_i) ⟶ H^p(𝒳, colim_i F_i)` is an
> isomorphism in every degree `p`, for every filtered diagram `F` of abelian fppf sheaves on `𝒳`.
>
> The hypotheses are the source's and nothing more: quasi-compactness in the sense of **Stacks 04YB**
> and quasi-separatedness in the *absolute* sense of **Stacks 050D** part (8), quasi-separatedness
> over `Spec ℤ`. In particular nothing is asked of the base scheme `S` of the big fppf site, which
> the source has no notion of; the containment of the terminal scheme that the absolute notion is
> stated with is discharged by `AlgebraicGeometry.BigFppfSite.contains_terminal` rather than assumed.
>
> All four conditions of Stacks 0GN4 are discharged: (1) from quasi-compactness by
> `AlgebraicGeometry.Stack.exists_isAffineObject_isLocallySurjective_terminal_from`, (2) for every
> category fibred in groupoids by
> `AlgebraicGeometry.Stack.hasFiniteCoverRefinementsFrom_fppfTopology`, (3) by
> `AlgebraicGeometry.Stack.exists_fin_affineObjects_isLocallySurjective_prodLift_absolute` and (4) by
> `AlgebraicGeometry.Stack.exists_fin_affineObjects_isLocallySurjective_equalizerLift_absolute`
> above.
>
> Conditions (3) and (4) need the 2-fibre products the source covers by an affine to be
> quasi-compact, and that is **Stacks 075S**. The repository's over-the-base statement of that tag,
> `AlgebraicGeometry.Stack.isQuasiCompactStack_and_isQuasiSeparatedOver_twoFibreProduct`, cannot
> serve: the proof of its part (1) cancels the structure morphism to `S`, so it needs that morphism
> to be quasi-compact for a quasi-compact `𝒳`, which is
> `AlgebraicGeometry.Stack.compactSpace_prod_of_quasiSeparatedSpace` — compactness of `V ×_S T` for
> affine objects `V`, `T` of the site — and that fails over a base scheme which is not
> quasi-separated, two affine opens of such a scheme being free to meet in a non-quasi-compact open.
> So it carries `QuasiSeparatedSpace S`, which the source does not ask for.
>
> What is used instead is the absolute form,
> `AlgebraicGeometry.Stack.isQuasiCompactMorphism_of_isQuasiCompactStack_absolute`, which cancels the
> structure morphism to `Spec ℤ` as the source does. It is proved by running the over-the-base
> statement at the terminal base, where `QuasiSeparatedSpace` is free — the terminal scheme is
> affine — and carrying its conclusion back to `S` along Construction A of **Stacks 04X5**. That
> passage is two results:
> `AlgebraicGeometry.Stack.changeBaseTwoFibreProductInv`, which identifies the 2-fibre product of the
> views with the view of the 2-fibre product, and
> `AlgebraicGeometry.Stack.isQuasiCompactStack_changeBaseAlgebraicStack_iff`, which descends
> quasi-compactness from the view to the stack itself through the presentation characterisation of
> **Stacks 04YC** and the bijection
> `AlgebraicGeometry.Stack.changeBasePointsEquiv` on the point sets of Stacks 04XG.

```lean
theorem isIso_colimit_post_rightDerived_globalSections_fppf_of_isQuasiCompact_absolute
    (hqc : IsQuasiCompactStack.{u, w} B S hS 𝒳.val 𝒳.property)
    (h𝒳qs : AlgebraicStacks.IsAbsolutelyQuasiSeparated.{u, w} B S hS B.contains_terminal 𝒳)
    (p : ℕ) {I : Type (u + 1)} [SmallCategory I] [IsFiltered I]
    (F : I ⥤ Sheaf (fppfTopology B S hS 𝒳.val) Ab.{u + 1}) :
    IsIso (colimit.post F
      ((Sheaf.Γ (fppfTopology B S hS 𝒳.val) Ab.{u + 1}).rightDerived p))
```

**`AlgebraicGeometry.Stack.isIso_colimit_post_rightDerived_globalSections_etale_of_isQuasiCompact_absolute`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomologyAbsolute.lean, line 831](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomologyAbsolute.lean#L831). The attribute's comment: “the second assertion, in the étale topology; all four conditions of 0GN4 proved, under the source's own hypotheses -- quasi-compactness of the stack and its absolute quasi-separatedness, with nothing asked of the base scheme of the site”.

> **The second assertion of Stacks 0GQV: the same statement in the étale topology.** Let `𝒳` be
> a quasi-compact and quasi-separated algebraic stack and give its total category the étale topology
> of Stacks 06TP. Then `colim_i H^p(𝒳, F_i) ⟶ H^p(𝒳, colim_i F_i)` is an isomorphism in every
> degree `p`, for every filtered diagram `F` of abelian étale sheaves on `𝒳`.
>
> All four conditions of Stacks 0GN4 are discharged for the étale site: (1) from quasi-compactness by
> `AlgebraicGeometry.Stack.exists_isAffineObject_isLocallySurjective_terminal_from_etale`, (2) for
> every category fibred in groupoids by
> `AlgebraicGeometry.Stack.hasFiniteCoverRefinementsFrom_etaleTopology`, (3) by
> `AlgebraicGeometry.Stack`
> `.exists_fin_affineObjects_isLocallySurjective_prodLift_etale_absolute` and (4) by
> `AlgebraicGeometry.Stack`
> `.exists_fin_affineObjects_isLocallySurjective_equalizerLift_etale_absolute` above.
>
> The hypotheses are the ones the fppf assertion
> `AlgebraicGeometry.Stack`
> `.isIso_colimit_post_rightDerived_globalSections_fppf_of_isQuasiCompact_absolute`
> carries, and they are the source's: quasi-compactness in the sense of **Stacks 04YB** and
> quasi-separatedness in the *absolute* sense of **Stacks 050D** part (8). Nothing is asked of the
> base scheme `S` of the big fppf site, and the containment of the terminal scheme the absolute
> notion is stated with is discharged by `AlgebraicGeometry.BigFppfSite.contains_terminal` rather
> than assumed.
>
> The two topologies agree on where quasi-separatedness is used, and on what form of it: conditions
> (3) and (4) are about the 2-fibre products the source covers by an affine scheme and not about the
> topology, so both reach **Stacks 075S** and both take it in the absolute form
> `AlgebraicGeometry.Stack.isQuasiCompactMorphism_of_isQuasiCompactStack_absolute`, which cancels the
> structure morphism to `Spec ℤ` as the source does rather than the one to `S`. See the docstring of
> the fppf assertion for why the over-the-base statement of Stacks 075S cannot serve, and
> `StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactQuasiSeparatedStackAbsolute.lean` for how the
> absolute form is proved from it.

```lean
theorem isIso_colimit_post_rightDerived_globalSections_etale_of_isQuasiCompact_absolute
    (hqc : IsQuasiCompactStack.{u, w} B S hS 𝒳.val 𝒳.property)
    (h𝒳qs : AlgebraicStacks.IsAbsolutelyQuasiSeparated.{u, w} B S hS B.contains_terminal 𝒳)
    (p : ℕ) {I : Type (u + 1)} [SmallCategory I] [IsFiltered I]
    (F : I ⥤ Sheaf (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B)) Ab.{u + 1}) :
    IsIso (colimit.post F
      ((Sheaf.Γ (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
        Ab.{u + 1}).rightDerived p))
```

**`AlgebraicGeometry.Stack.hasFiniteCoverRefinementsFrom_fppfTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomologyAffineRefinement.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomologyAffineRefinement.lean#L167). The attribute's comment: “condition (2) of Stacks 0GN4 for the fppf site, from Stacks 021P”.

> **Condition (2) of Stacks 0GN4 for the fppf site of a category fibred in groupoids over the big
> fppf category of `S`, at the objects lying over affine schemes.** Every covering sieve of an object
> of `𝒳` lying over an affine scheme contains a finite covering family whose members again lie over
> affine schemes.
>
> This is the second of the four conditions the proof of **Stacks 0GQV** checks, the collection `B`
> of that proof being the objects of the site lying over affine schemes; the source derives it from
> **Stacks 021P**, and so does the proof here.
>
> The refinement is produced downstairs by
> `AlgebraicGeometry.BigFppfOver.exists_finite_affine_covering_refinement` and transported to `𝒳` by
> `AlgebraicGeometry.Stack.exists_chosenCovering_le_of_mem_associatedTopology`; the transported
> family covers because its image is a chosen covering family of the big fppf category over `S` and
> because in a category fibred in groupoids every morphism is strongly cartesian over its image,
> which is what the covering families of **Stacks 06NU** ask of its members. See the module
> documentation for the two bookkeeping steps: restricting the base-level input to affine targets,
> and reindexing a finite index type by `Fin n`.
>
> The tag registers this one condition of the proof of **Stacks 0GQV** and nothing more: the
> assertion of Stacks 0GN4 is that the four conditions suffice, which is
> `Stacks.Cohomology.ColimitsOfCohomology.isIso_colimit_post_rightDerived_globalSections_of_covers`,
> and the full assertions of Stacks 0GQV are
> `AlgebraicGeometry.Stack.isIso_colimit_post_rightDerived_globalSections_fppf_of_isQuasiCompact`
> and
> `AlgebraicGeometry.Stack.isIso_colimit_post_rightDerived_globalSections_etale_of_isQuasiCompact`.

```lean
theorem hasFiniteCoverRefinementsFrom_fppfTopology
    {x : 𝒳.val.obj} (hx : IsAffineObject B S hS 𝒳.val.p x) :
    HasFiniteCoverRefinementsFrom (fppfTopology B S hS 𝒳)
      {y : 𝒳.val.obj | IsAffineObject B S hS 𝒳.val.p y} x
```

**`AlgebraicGeometry.Stack.exists_isAffineObject_isLocallySurjective_terminal_from`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomologyAtlasCovers.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomologyAtlasCovers.lean#L325). The attribute's comment: “condition (1) of Stacks 0GN4 for the fppf site, from Stacks 04YC and Stacks 06QA”.

> **Condition (1) of Stacks 0GN4 for the fppf site of a quasi-compact algebraic stack, with one
> object.** There is an object `x` of the site lying over an affine scheme for which the
> sheafification `h_x^#` of its representable surjects onto the final sheaf.
>
> This is `exists_isAffineObject_isLocallySurjective_terminal_from_associatedTopology` at the big
> fppf topology, with **Stacks 06QA** for the fibre lifts as in
> `AlgebraicGeometry.Stack.exists_isAffineObject_cover_nonempty_hom`.

```lean
theorem exists_isAffineObject_isLocallySurjective_terminal_from
    (hqc : IsQuasiCompactStack.{u, w} B S hS 𝒳.val 𝒳.property) :
    ∃ x : 𝒳.val.val.obj, IsAffineObject B S hS 𝒳.val.val.p x ∧
      Sheaf.IsLocallySurjective (terminal.from
        ((Sheaf.sheafifiedYoneda (fppfTopology B S hS 𝒳.val)).obj x))
```

**`AlgebraicGeometry.Stack.exists_isAffineObject_isLocallySurjective_terminal_from_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomologyAtlasCovers.lean, line 350](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomologyAtlasCovers.lean#L350). The attribute's comment: “condition (1) of Stacks 0GN4 for the étale site, from Stacks 04YC and Stacks 06XH part (2)”.

> **Condition (1) of Stacks 0GN4 for the étale site of a quasi-compact algebraic stack, with one
> object.** There is an object `x` of the site lying over an affine scheme for which the
> sheafification `h_x^#` of its representable surjects onto the final sheaf in the étale topology.
>
> This is the first of the four conditions the proof of **Stacks 0GQV** checks, for the second of
> the two topologies the source asserts the tag in. It is
> `exists_isAffineObject_isLocallySurjective_terminal_from_associatedTopology` at the big étale
> topology, with **Stacks 06XH** part (2) for the fibre lifts as in
> `AlgebraicGeometry.Stack.exists_isAffineObject_cover_nonempty_hom_etale`.
>
> The source checks this condition by saying that the affine smooth surjection of Stacks 04YC makes
> `h_x^# ⟶ *` an epimorphism of sheaves on `𝒳_τ`, which for `τ` the étale topology is the assertion
> that a surjective smooth 1-morphism has sections étale-locally. That is Stacks 06XH part (2), and
> it is the only place the étale proof of this condition differs from the fppf one.

```lean
theorem exists_isAffineObject_isLocallySurjective_terminal_from_etale
    (hqc : IsQuasiCompactStack.{u, w} B S hS 𝒳.val 𝒳.property) :
    ∃ x : 𝒳.val.val.obj, IsAffineObject B S hS 𝒳.val.val.p x ∧
      Sheaf.IsLocallySurjective (terminal.from
        ((Sheaf.sheafifiedYoneda
          (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))).obj x))
```

**`AlgebraicGeometry.Stack.isIso_colimit_post_rightDerived_globalSections_fppf_of_isQuasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomologyEqualizerAffineCover.lean, line 634](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomologyEqualizerAffineCover.lean#L634). The attribute's comment: “the first assertion, in the fppf topology, for a quasi-compact algebraic stack quasi-separated over a quasi-separated base scheme; all four conditions of 0GN4 proved”.

> **Stacks 0GQV in the fppf topology for a quasi-compact algebraic stack which is quasi-separated
> over a quasi-separated base scheme.** Let `𝒳` be such a stack and give its total category the fppf
> topology of Stacks 06TP. Then `colim_i H^p(𝒳, F_i) ⟶ H^p(𝒳, colim_i F_i)` is an isomorphism in
> every degree `p`, for every filtered diagram `F` of abelian fppf sheaves on `𝒳`.
>
> All four conditions of Stacks 0GN4 are discharged: (1) from quasi-compactness by
> `AlgebraicGeometry.Stack.exists_isAffineObject_isLocallySurjective_terminal_from`, (2) for every
> category fibred in groupoids by
> `AlgebraicGeometry.Stack.hasFiniteCoverRefinementsFrom_fppfTopology`, (3) by
> `AlgebraicGeometry.Stack.exists_fin_affineObjects_isLocallySurjective_prodLift` and (4) by
> `AlgebraicGeometry.Stack.exists_fin_affineObjects_isLocallySurjective_equalizerLift` above.
>
> The quasi-separatedness hypothesis is `AlgebraicGeometry.Stack.IsQuasiSeparatedOver` of `𝒳`
> together with quasi-separatedness of the base scheme `S`, which is what Stacks 075S asks for and
> what conditions (3) and (4) use.

```lean
theorem isIso_colimit_post_rightDerived_globalSections_fppf_of_isQuasiCompact
    (hqc : IsQuasiCompactStack.{u, w} B S hS 𝒳.val 𝒳.property)
    (p : ℕ) {I : Type (u + 1)} [SmallCategory I] [IsFiltered I]
    (F : I ⥤ Sheaf (fppfTopology B S hS 𝒳.val) Ab.{u + 1}) :
    IsIso (colimit.post F
      ((Sheaf.Γ (fppfTopology B S hS 𝒳.val) Ab.{u + 1}).rightDerived p))
```

**`AlgebraicGeometry.Stack.hasFiniteCoverRefinementsFrom_etaleTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomologyEtaleAffineRefinement.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomologyEtaleAffineRefinement.lean#L173). The attribute's comment: “condition (2) of Stacks 0GN4 for the étale site, from Stacks 0218”.

> **Condition (2) of Stacks 0GN4 for the étale site of a category fibred in groupoids over the
> big fppf category of `S`, at the objects lying over affine schemes.** Every covering sieve of an
> object of `𝒳` lying over an affine scheme contains a finite covering family whose members again
> lie over affine schemes, the topology on `𝒳` being the one it inherits (Stacks 06TP) from the big
> étale topology of **Stacks 03FF** localized at `S`.
>
> This is the second of the four conditions the proof of **Stacks 0GQV** checks, the collection `B`
> of that proof being the objects of the site lying over affine schemes. For the fppf site the
> source derives it from **Stacks 021P**; in the étale topology the corresponding input is
> **Stacks 0218**, and that is what is used here, through
> `AlgebraicGeometry.BigFppfOver.exists_finite_affine_etaleCovering_refinement`.
>
> The refinement is transported to `𝒳` by
> `AlgebraicGeometry.Stack.exists_chosenCovering_le_of_mem_associatedTopology` at the big étale
> topology; the transported family covers because its image is a selected étale covering family of
> the big fppf category over `S` and because in a category fibred in groupoids every morphism is
> strongly cartesian over its image, which is what the covering families of **Stacks 06NU** ask of
> its members. See the module documentation for the two bookkeeping steps: restricting the
> base-level input to affine targets, and reindexing a finite index type by `Fin n`.
>
> This is the étale counterpart of
> `AlgebraicGeometry.Stack.hasFiniteCoverRefinementsFrom_fppfTopology`, and like it holds for every
> category fibred in groupoids, with no quasi-compactness hypothesis.

```lean
theorem hasFiniteCoverRefinementsFrom_etaleTopology
    {x : 𝒳.val.obj} (hx : IsAffineObject B S hS 𝒳.val.p x) :
    HasFiniteCoverRefinementsFrom (associatedTopology B S hS 𝒳.val.p (etaleTopology B))
      {y : 𝒳.val.obj | IsAffineObject B S hS 𝒳.val.p y} x
```

**`AlgebraicGeometry.Stack.isIso_colimit_post_rightDerived_globalSections_etale_of_isQuasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomologyEtaleEqualizerAffineCover.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomologyEtaleEqualizerAffineCover.lean#L177). The attribute's comment: “the second assertion, in the étale topology, for a quasi-compact algebraic stack quasi-separated over a quasi-separated base scheme; all four conditions of 0GN4 proved”.

> **Stacks 0GQV in the étale topology for a quasi-compact algebraic stack which is
> quasi-separated over a quasi-separated base scheme.** Let `𝒳` be such a stack and give its total
> category the étale topology of Stacks 06TP. Then `colim_i H^p(𝒳, F_i) ⟶ H^p(𝒳, colim_i F_i)` is an
> isomorphism in every degree `p`, for every filtered diagram `F` of abelian étale sheaves on `𝒳`.
>
> All four conditions of Stacks 0GN4 are discharged for the étale site: (1) from quasi-compactness by
> `AlgebraicGeometry.Stack.exists_isAffineObject_isLocallySurjective_terminal_from_etale`, (2) for
> every category fibred in groupoids by
> `AlgebraicGeometry.Stack.hasFiniteCoverRefinementsFrom_etaleTopology`, (3) by
> `AlgebraicGeometry.Stack.exists_fin_affineObjects_isLocallySurjective_prodLift_etale` and (4) by
> `AlgebraicGeometry.Stack.exists_fin_affineObjects_isLocallySurjective_equalizerLift_etale` above.
>
> The quasi-separatedness hypothesis is `AlgebraicGeometry.Stack.IsQuasiSeparatedOver` of `𝒳`
> together with quasi-separatedness of the base scheme `S`, which is what Stacks 075S asks for and
> what conditions (3) and (4) use. It is the same hypothesis the fppf assertion
> `AlgebraicGeometry.Stack.isIso_colimit_post_rightDerived_globalSections_fppf_of_isQuasiCompact`
> carries, and for the same reason: quasi-compactness of the 2-fibre products the source covers by an
> affine scheme is **Stacks 075S** part (3).

```lean
theorem isIso_colimit_post_rightDerived_globalSections_etale_of_isQuasiCompact
    (hqsS : QuasiSeparatedSpace S)
    (hqc : IsQuasiCompactStack.{u, w} B S hS 𝒳.val 𝒳.property)
    (h𝒳 : IsQuasiSeparatedOver.{u, w} B S hS 𝒳)
    (p : ℕ) {I : Type (u + 1)} [SmallCategory I] [IsFiltered I]
    (F : I ⥤ Sheaf (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B)) Ab.{u + 1}) :
    IsIso (colimit.post F
      ((Sheaf.Γ (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
        Ab.{u + 1}).rightDerived p))
```

**`AlgebraicGeometry.Stack.isIso_colimit_post_rightDerived_globalSections_etale_of_isQuasiSeparatedOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomologyEtaleProductAffineCover.lean, line 428](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomologyEtaleProductAffineCover.lean#L428). The attribute's comment: “the second assertion, in the étale topology, for a quasi-compact algebraic stack quasi-separated over a quasi-separated base; conditions (1), (2) and (3) of 0GN4 are now proved for the étale site, condition (4) is still assumed”.

> **The second assertion of Stacks 0GQV, in the étale topology, for a quasi-compact algebraic
> stack which is quasi-separated over a quasi-separated base scheme, from condition (4) of
> Stacks 0GN4 alone.**
>
> This is `AlgebraicGeometry.Stack`
> `.isIso_colimit_post_rightDerived_globalSections_etale_of_isQuasiCompactStack`
> with its condition (3) discharged by
> `AlgebraicGeometry.Stack.exists_fin_affineObjects_isLocallySurjective_prodLift_etale`. Condition
> (4), the corresponding assertion for the equalizer of two parallel morphisms, is still assumed:
> the 2-fibre product the source covers by an affine scheme in that case is the one of a single
> 1-morphism against the diagonal, not of two 2-Yoneda 1-morphisms, so the quadruple of this file
> does not discharge it, in this topology any more than in the fppf one. So this is not yet the full
> second assertion of Stacks 0GQV.

```lean
theorem isIso_colimit_post_rightDerived_globalSections_etale_of_isQuasiSeparatedOver
    (hqsS : QuasiSeparatedSpace S)
    (hqc : IsQuasiCompactStack.{u, w} B S hS 𝒳.val 𝒳.property)
    (h𝒳 : IsQuasiSeparatedOver.{u, w} B S hS 𝒳)
    (h_equalizer : ∀ {U U' : 𝒳.val.val.obj} (a b : U ⟶ U'),
      U ∈ affineObjects B S hS 𝒳.val → U' ∈ affineObjects B S hS 𝒳.val →
      ∃ (m : ℕ) (V : Fin m → 𝒳.val.val.obj),
        (∀ i, V i ∈ affineObjects B S hS 𝒳.val) ∧
          ∃ (p : ∀ i, V i ⟶ U) (hp : ∀ i, p i ≫ a = p i ≫ b),
          Sheaf.IsLocallySurjective (Limits.Sigma.desc fun i =>
            equalizer.lift
              (f := (Sheaf.sheafifiedYoneda
                (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))).map a)
              (g := (Sheaf.sheafifiedYoneda
                (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))).map b)
              ((Sheaf.sheafifiedYoneda
                (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))).map (p i)) (by
                simpa only [Functor.map_comp] using
                  congrArg (Sheaf.sheafifiedYoneda
                    (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))).map (hp i))))
    (p : ℕ) {I : Type (u + 1)} [SmallCategory I] [IsFiltered I]
    (F : I ⥤ Sheaf (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B)) Ab.{u + 1}) :
    IsIso (colimit.post F
      ((Sheaf.Γ (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
        Ab.{u + 1}).rightDerived p))
```

**`AlgebraicGeometry.Stack.isIso_colimit_post_rightDerived_globalSections_fppf_of_isQuasiSeparatedOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomologyProductAffineCover.lean, line 433](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomologyProductAffineCover.lean#L433). The attribute's comment: “for a quasi-compact algebraic stack quasi-separated over a quasi-separated base; condition (3) of 0GN4 is proved here and condition (4) is a hypothesis, discharged in ColimitsOfCohomologyEqualizerAffineCover”.

> **Stacks 0GQV in the fppf topology for a quasi-compact algebraic stack which is quasi-separated
> over a quasi-separated base scheme, from condition (4) of Stacks 0GN4 alone.**
>
> This is `Stack.isIso_colimit_post_rightDerived_globalSections_fppf_of_isQuasiCompactStack` with
> its condition (3) discharged by
> `AlgebraicGeometry.Stack.exists_fin_affineObjects_isLocallySurjective_prodLift`. Condition (4), the
> corresponding assertion for the equalizer of two parallel morphisms, remains a hypothesis here
> because the quadruple of this file does not give it: the 2-fibre product it is about is not the one
> of two 2-Yoneda 1-morphisms but the one of the two *graphs* of `a` and `b` over that one. It is
> proved, for a stack quasi-separated over a quasi-separated base scheme, as
> `AlgebraicGeometry.Stack.exists_fin_affineObjects_isLocallySurjective_equalizerLift` in
> `StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfCohomologyEqualizerAffineCover.lean`, and
> discharging it there turns this result into the full fppf assertion of Stacks 0GQV,
> `AlgebraicGeometry.Stack.isIso_colimit_post_rightDerived_globalSections_fppf_of_isQuasiCompact`.

```lean
theorem isIso_colimit_post_rightDerived_globalSections_fppf_of_isQuasiSeparatedOver
    (hqsS : QuasiSeparatedSpace S)
    (hqc : IsQuasiCompactStack.{u, w} B S hS 𝒳.val 𝒳.property)
    (h𝒳 : IsQuasiSeparatedOver.{u, w} B S hS 𝒳)
    (h_equalizer : ∀ {U U' : 𝒳.val.val.obj} (a b : U ⟶ U'),
      U ∈ affineObjects B S hS 𝒳.val → U' ∈ affineObjects B S hS 𝒳.val →
      ∃ (m : ℕ) (V : Fin m → 𝒳.val.val.obj),
        (∀ i, V i ∈ affineObjects B S hS 𝒳.val) ∧
          ∃ (p : ∀ i, V i ⟶ U) (hp : ∀ i, p i ≫ a = p i ≫ b),
          Sheaf.IsLocallySurjective (Limits.Sigma.desc fun i =>
            equalizer.lift
              (f := (Sheaf.sheafifiedYoneda (fppfTopology B S hS 𝒳.val)).map a)
              (g := (Sheaf.sheafifiedYoneda (fppfTopology B S hS 𝒳.val)).map b)
              ((Sheaf.sheafifiedYoneda (fppfTopology B S hS 𝒳.val)).map (p i)) (by
                simpa only [Functor.map_comp] using
                  congrArg (Sheaf.sheafifiedYoneda (fppfTopology B S hS 𝒳.val)).map (hp i))))
    (p : ℕ) {I : Type (u + 1)} [SmallCategory I] [IsFiltered I]
    (F : I ⥤ Sheaf (fppfTopology B S hS 𝒳.val) Ab.{u + 1}) :
    IsIso (colimit.post F
      ((Sheaf.Γ (fppfTopology B S hS 𝒳.val) Ab.{u + 1}).rightDerived p))
```

## Tag 0GQW, a lemma

[Tag 0GQW](https://stacks.math.columbia.edu/tag/0GQW) in the Stacks Project.

**`AlgebraicGeometry.Stack.preservesColimitsOfShape_rightDerived_abelianDirectImage_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfHigherDirectImages.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfHigherDirectImages.lean#L254). The attribute's comment: “fppf topology; the sheafification step only — that the cohomology of the fibres of f commutes with the colimit is assumed, as is the value half of 075G that identifies it”.

> **The sheafification step of Stacks 0GQW in the fppf topology.** Let `f : 𝒳 ⟶ 𝒴` be a
> 1-morphism of algebraic stacks over a scheme `S` contained in a big fppf site. If for every
> object `y` of the fppf site of `𝒴` the `n`-th derived functor of
> `AlgebraicGeometry.Stack.fibreSections` at `y` commutes with colimits of shape `I`, then so does
> the `n`-th higher direct image `R^n f_*` of abelian fppf sheaves.
>
> This is `AlgebraicGeometry.Stack.preservesColimitsOfShape_rightDerived_abelianDirectImage` at the
> fppf topology of Stacks 06TP. It is the first of the two steps of the source's proof; the
> hypothesis is the second, and is what quasi-compactness and quasi-separatedness of `f` are used
> for. See "What is proved and what is assumed" in the module docstring for exactly what is
> missing: the value half of Stacks 075G, and conditions (3) and (4) of Stacks 0GN4 in the library's
> form of Stacks 0GQV.

```lean
theorem preservesColimitsOfShape_rightDerived_abelianDirectImage_fppf (n : ℕ)
    {I : Type v} [Category.{v'} I] [IsFiltered I]
    (h :
      letI := site_hasSheafify_addCommGrp.{u + 1, u, a}
        (J := BigFppfOver.associatedTopology B S hS 𝒳.val.val.p .fppf)
      letI := Sheaf.isGrothendieckAbelian_of_essentiallySmall.{max (u + 1) a}
        (BigFppfOver.associatedTopology B S hS 𝒳.val.val.p .fppf)
        AddCommGrpCat.{max (u + 1) a}
      letI := IsGrothendieckAbelian.enoughInjectives
        (C := Sheaf (BigFppfOver.associatedTopology B S hS 𝒳.val.val.p .fppf)
          AddCommGrpCat.{max (u + 1) a})
      ∀ y : 𝒴.val.val.obj, PreservesColimitsOfShape I
        ((fibreSections.{u, a} B S hS 𝒳.val.val.p
          (CatFiberedInGroupoids.homFunctor f.hom) .fppf y).rightDerived n)) :
    letI := site_hasSheafify_addCommGrp.{u + 1, u, a}
      (J := BigFppfOver.associatedTopology B S hS 𝒳.val.val.p .fppf)
    letI := site_hasSheafify_addCommGrp.{u + 1, u, a}
      (J := BigFppfOver.associatedTopology B S hS 𝒴.val.val.p .fppf)
    letI := Sheaf.isGrothendieckAbelian_of_essentiallySmall.{max (u + 1) a}
      (BigFppfOver.associatedTopology B S hS 𝒳.val.val.p .fppf) AddCommGrpCat.{max (u + 1) a}
    letI := IsGrothendieckAbelian.enoughInjectives
      (C := Sheaf (BigFppfOver.associatedTopology B S hS 𝒳.val.val.p .fppf)
        AddCommGrpCat.{max (u + 1) a})
    letI := abelianDirectImageAdditive.{u, w, a} B S hS f .fppf
    PreservesColimitsOfShape I
      (((CatFiberedInGroupoids.homFunctor f.hom).sheafPushforwardCocontinuous
        AddCommGrpCat.{max (u + 1) a}
        (BigFppfOver.associatedTopology B S hS 𝒳.val.val.p .fppf)
        (BigFppfOver.associatedTopology B S hS 𝒴.val.val.p .fppf)).rightDerived n)
```

**`AlgebraicGeometry.Stack.preservesColimitsOfShape_rightDerived_abelianDirectImage_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfHigherDirectImages.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfHigherDirectImages.lean#L299). The attribute's comment: “étale topology; the sheafification step only — that the cohomology of the fibres of f commutes with the colimit is assumed, as is the value half of 075G that identifies it”.

> **The sheafification step of Stacks 0GQW in the étale topology.** Let `f : 𝒳 ⟶ 𝒴` be a
> 1-morphism of algebraic stacks over a scheme `S` contained in a big fppf site. If for every
> object `y` of the étale site of `𝒴` the `n`-th derived functor of
> `AlgebraicGeometry.Stack.fibreSections` at `y` commutes with colimits of shape `I`, then so does
> the `n`-th higher direct image `R^n f_*` of abelian étale sheaves.
>
> This is `AlgebraicGeometry.Stack.preservesColimitsOfShape_rightDerived_abelianDirectImage` at the
> étale topology of Stacks 06TP. It is the first of the two steps of the source's proof; the
> hypothesis is the second, and is what quasi-compactness and quasi-separatedness of `f` are used
> for. See "What is proved and what is assumed" in the module docstring for exactly what is
> missing: the value half of Stacks 075G, and the étale analogues of conditions (3) and (4) of
> Stacks 0GN4 in the library's form of Stacks 0GQV.

```lean
theorem preservesColimitsOfShape_rightDerived_abelianDirectImage_etale (n : ℕ)
    {I : Type v} [Category.{v'} I] [IsFiltered I]
    (h :
      letI := site_hasSheafify_addCommGrp.{u + 1, u, a}
        (J := BigFppfOver.associatedTopology B S hS 𝒳.val.val.p .etale)
      letI := Sheaf.isGrothendieckAbelian_of_essentiallySmall.{max (u + 1) a}
        (BigFppfOver.associatedTopology B S hS 𝒳.val.val.p .etale)
        AddCommGrpCat.{max (u + 1) a}
      letI := IsGrothendieckAbelian.enoughInjectives
        (C := Sheaf (BigFppfOver.associatedTopology B S hS 𝒳.val.val.p .etale)
          AddCommGrpCat.{max (u + 1) a})
      ∀ y : 𝒴.val.val.obj, PreservesColimitsOfShape I
        ((fibreSections.{u, a} B S hS 𝒳.val.val.p
          (CatFiberedInGroupoids.homFunctor f.hom) .etale y).rightDerived n)) :
    letI := site_hasSheafify_addCommGrp.{u + 1, u, a}
      (J := BigFppfOver.associatedTopology B S hS 𝒳.val.val.p .etale)
    letI := site_hasSheafify_addCommGrp.{u + 1, u, a}
      (J := BigFppfOver.associatedTopology B S hS 𝒴.val.val.p .etale)
    letI := Sheaf.isGrothendieckAbelian_of_essentiallySmall.{max (u + 1) a}
      (BigFppfOver.associatedTopology B S hS 𝒳.val.val.p .etale) AddCommGrpCat.{max (u + 1) a}
    letI := IsGrothendieckAbelian.enoughInjectives
      (C := Sheaf (BigFppfOver.associatedTopology B S hS 𝒳.val.val.p .etale)
        AddCommGrpCat.{max (u + 1) a})
    letI := abelianDirectImageAdditive.{u, w, a} B S hS f .etale
    PreservesColimitsOfShape I
      (((CatFiberedInGroupoids.homFunctor f.hom).sheafPushforwardCocontinuous
        AddCommGrpCat.{max (u + 1) a}
        (BigFppfOver.associatedTopology B S hS 𝒳.val.val.p .etale)
        (BigFppfOver.associatedTopology B S hS 𝒴.val.val.p .etale)).rightDerived n)
```

**`AlgebraicGeometry.Stack.preservesColimitsOfShape_rightDerived_abelianDirectImage_fppf_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfHigherDirectImagesQcqs.lean, line 699](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfHigherDirectImagesQcqs.lean#L699). The attribute's comment: “first assertion: the fppf topology, for f quasi-compact and quasi-separated”.

> **Stacks 0GQW, first assertion: the fppf topology.** Let `f : 𝒳 ⟶ 𝒴` be a quasi-compact and
> quasi-separated 1-morphism of algebraic stacks. Then for every `p ≥ 0` the higher direct image
> `Rᵖf_*` of abelian fppf sheaves commutes with filtered colimits:
> `Rᵖf_*(colim_i ℱ_i) = colim_i Rᵖf_*ℱ_i`.
>
> The proof is the source's. `Rᵖf_*ℱ` is the sheaf associated to the presheaf
> `y ↦ Hᵖ((Sch/V) ×_{y, 𝒴} 𝒳, pr⁻¹ℱ)` (Stacks 075G: the sheafification half is
> `AlgebraicGeometry.Stack.abelianHigherDirectImage_iso_sheafify_fibreCohomology`, the value half
> `AlgebraicGeometry.Stack.rightDerivedFibreSectionsIso`), and the colimit of sheaves is the sheaf
> associated to the presheaf colimit. When `V` is affine the 2-fibre product is quasi-compact and
> quasi-separated
> (`AlgebraicGeometry.Stack`
> `.isQuasiCompactStack_and_isAbsolutelyQuasiSeparated_twoFibreProduct_objectMorphism`),
> so Stacks 0GQV applies to its cohomology
> (`AlgebraicGeometry.Stack.preservesColimitsOfShape_rightDerived_fibreSections_fppf`), and every
> object of the fppf site of `𝒴` has a covering by objects lying over affine schemes
> (`AlgebraicGeometry.FibredSite.exists_affine_ofArrows`), which is
> `AlgebraicGeometry.Stack`
> `.preservesColimitsOfShape_rightDerived_abelianDirectImage_of_isAffineObject`.
>
> Quasi-compactness is Stacks 050U (`AlgebraicGeometry.Stack.IsQuasiCompactMorphism`) and
> quasi-separatedness Stacks 04YW (`AlgebraicGeometry.Stack.AlgebraicStacks.IsQuasiSeparated`). The
> abelian sheaves take values in `AddCommGrpCat.{u + 1}` and the diagram is indexed by a small
> filtered category at that universe, as in Stacks 0GQV.

```lean
theorem preservesColimitsOfShape_rightDerived_abelianDirectImage_fppf_of_qcqs
    (hfqc : IsQuasiCompactMorphism.{u, w} B S hS f)
    (hfqs : AlgebraicStacks.IsQuasiSeparated.{u, w} B S hS f) (n : ℕ)
    (I : Type (u + 1)) [SmallCategory I] [IsFiltered I] :
    letI := site_hasSheafify_addCommGrp.{u + 1, u, 0}
      (J := BigFppfOver.associatedTopology B S hS 𝒳.val.val.p .fppf)
    letI := site_hasSheafify_addCommGrp.{u + 1, u, 0}
      (J := BigFppfOver.associatedTopology B S hS 𝒴.val.val.p .fppf)
    letI := Sheaf.isGrothendieckAbelian_of_essentiallySmall.{u + 1}
      (BigFppfOver.associatedTopology B S hS 𝒳.val.val.p .fppf) AddCommGrpCat.{u + 1}
    letI := IsGrothendieckAbelian.enoughInjectives
      (C := Sheaf (BigFppfOver.associatedTopology B S hS 𝒳.val.val.p .fppf) AddCommGrpCat.{u + 1})
    letI := abelianDirectImageAdditive.{u, w, 0} B S hS f .fppf
    PreservesColimitsOfShape I
      (((Fn).sheafPushforwardCocontinuous AddCommGrpCat.{u + 1}
        (BigFppfOver.associatedTopology B S hS 𝒳.val.val.p .fppf)
        (BigFppfOver.associatedTopology B S hS 𝒴.val.val.p .fppf)).rightDerived n)
```

**`AlgebraicGeometry.Stack.preservesColimitsOfShape_rightDerived_abelianDirectImage_etale_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfHigherDirectImagesQcqs.lean, line 733](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfHigherDirectImagesQcqs.lean#L733). The attribute's comment: “second assertion: the étale topology, for f quasi-compact and quasi-separated”.

> **Stacks 0GQW, second assertion: the étale topology.** Let `f : 𝒳 ⟶ 𝒴` be a quasi-compact and
> quasi-separated 1-morphism of algebraic stacks. Then for every `p ≥ 0` the higher direct image
> `Rᵖf_*` of abelian sheaves on the étale sites, taken in the étale topology, commutes with filtered
> colimits: `Rᵖf_*(colim_i ℱ_i) = colim_i Rᵖf_*ℱ_i`.
>
> The proof is that of the fppf assertion
> `AlgebraicGeometry.Stack.preservesColimitsOfShape_rightDerived_abelianDirectImage_fppf_of_qcqs`,
> with the étale assertion of Stacks 0GQV
> (`AlgebraicGeometry.Stack.preservesColimitsOfShape_rightDerived_fibreSections_etale`) and the
> covering of every object of the étale site of `𝒴` by objects lying over affine schemes
> (`AlgebraicGeometry.Stack.exists_affine_ofArrows_etale`).

```lean
theorem preservesColimitsOfShape_rightDerived_abelianDirectImage_etale_of_qcqs
    (hfqc : IsQuasiCompactMorphism.{u, w} B S hS f)
    (hfqs : AlgebraicStacks.IsQuasiSeparated.{u, w} B S hS f) (n : ℕ)
    (I : Type (u + 1)) [SmallCategory I] [IsFiltered I] :
    letI := site_hasSheafify_addCommGrp.{u + 1, u, 0}
      (J := BigFppfOver.associatedTopology B S hS 𝒳.val.val.p .etale)
    letI := site_hasSheafify_addCommGrp.{u + 1, u, 0}
      (J := BigFppfOver.associatedTopology B S hS 𝒴.val.val.p .etale)
    letI := Sheaf.isGrothendieckAbelian_of_essentiallySmall.{u + 1}
      (BigFppfOver.associatedTopology B S hS 𝒳.val.val.p .etale) AddCommGrpCat.{u + 1}
    letI := IsGrothendieckAbelian.enoughInjectives
      (C := Sheaf (BigFppfOver.associatedTopology B S hS 𝒳.val.val.p .etale) AddCommGrpCat.{u + 1})
    letI := abelianDirectImageAdditive.{u, w, 0} B S hS f .etale
    PreservesColimitsOfShape I
      (((Fn).sheafPushforwardCocontinuous AddCommGrpCat.{u + 1}
        (BigFppfOver.associatedTopology B S hS 𝒳.val.val.p .etale)
        (BigFppfOver.associatedTopology B S hS 𝒴.val.val.p .etale)).rightDerived n)
```

## Tag 0GQX, a lemma

[Tag 0GQX](https://stacks.math.columbia.edu/tag/0GQX) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.preservesCoproducts_and_filteredColimits_quasicoherentDirectImages_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentDirectImageFilteredColimits.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentDirectImageFilteredColimits.lean#L165). The attribute's comment: “the whole lemma, for f quasi-compact and quasi-separated and the functors f_{QCoh,*} and R^i f_{QCoh,*} (i ≥ 0) of Stacks 077A: each commutes with direct sums (indexed by ι : Type u) and with filtered colimits (indexed by filtered J : Type u)”.

> **Stacks 0GQX.** Let `f : 𝒳 ⟶ 𝒴` be a quasi-compact and quasi-separated 1-morphism of
> algebraic stacks. The functor `f_{QCoh,*}` and the functors `Rⁱf_{QCoh,*}` (`i ≥ 0`) of
> **Stacks 077A** commute with direct sums and filtered colimits:
>
> 1. `f_{QCoh,*}` commutes with direct sums indexed by any `ι : Type u`;
> 2. `f_{QCoh,*}` commutes with colimits indexed by any filtered category `J : Type u` (morphisms in
>    `u`);
> 3. for every `i`, `Rⁱf_{QCoh,*}` commutes with direct sums indexed by any `ι : Type u` and with
>    colimits indexed by any filtered category `J : Type u`.
>
> The functors are `quasicoherentDirectImage` and `quasicoherentHigherDirectImage`, the composites
> `Q ∘ f_* ∘ i` and `Q ∘ Rⁱf_* ∘ i` of the inclusion, the direct images of modules on the fppf
> sites and the coherator of **Stacks 0778**, at module universe `u`.

```lean
theorem preservesCoproducts_and_filteredColimits_quasicoherentDirectImages_of_qcqs :
    (∀ ι : Type u, PreservesColimitsOfShape (Discrete ι) (quasicoherentDirectImage B S hS f)) ∧
      (∀ (J : Type u) [Category.{u} J] [IsFiltered J],
        PreservesColimitsOfShape J (quasicoherentDirectImage B S hS f)) ∧
      ∀ i : ℕ,
        (∀ ι : Type u,
          PreservesColimitsOfShape (Discrete ι) (quasicoherentHigherDirectImage B S hS f i)) ∧
        (∀ (J : Type u) [Category.{u} J] [IsFiltered J],
          PreservesColimitsOfShape J (quasicoherentHigherDirectImage B S hS f i))
```

## Tag 0GQY, a lemma

[Tag 0GQY](https://stacks.math.columbia.edu/tag/0GQY) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isZero_quasicoherentHigherDirectImage_and_exact_preservesColimits_of_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/AffineQuasicoherentDirectImageExact.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/AffineQuasicoherentDirectImageExact.lean#L179). The attribute's comment: “the whole lemma, for an affine 1-morphism f of algebraic stacks and the functors R^i f_{QCoh,*} and f_{QCoh,*} of Stacks 077A: R^i f_{QCoh,*} = 0 for i > 0; f_{QCoh,*} is exact (preserves finite limits and finite colimits); it commutes with direct sums; it commutes with all colimits (indexed in the universe u of the site)”.

> **Stacks 0GQY.** Let `f : 𝒳 ⟶ 𝒴` be an affine 1-morphism of algebraic stacks. Then
>
> 1. the functors `Rⁱf_{QCoh,*}`, `i > 0`, vanish;
> 2. `f_{QCoh,*}` is exact: it preserves finite limits and finite colimits;
> 3. `f_{QCoh,*}` commutes with direct sums (indexed by any `ι : Type u`);
> 4. `f_{QCoh,*}` commutes with all colimits (indexed by categories `J : Type u` with morphisms in
>    `u`).
>
> The functors are those of **Stacks 077A**, `quasicoherentHigherDirectImage` and
> `quasicoherentDirectImage`, at module universe `u`.

```lean
theorem isZero_quasicoherentHigherDirectImage_and_exact_preservesColimits_of_isAffineHom :
    (∀ (i : ℕ), 0 < i → ∀ F : quasicoherentModules B S hS 𝒳,
        IsZero ((quasicoherentHigherDirectImage B S hS f i).obj F)) ∧
      (PreservesFiniteLimits (quasicoherentDirectImage B S hS f) ∧
        PreservesFiniteColimits (quasicoherentDirectImage B S hS f)) ∧
      (∀ ι : Type u, PreservesColimitsOfShape (Discrete ι) (quasicoherentDirectImage B S hS f)) ∧
      PreservesColimitsOfSize.{u, u} (quasicoherentDirectImage B S hS f)
```

## Tag 0GQZ, a lemma

[Tag 0GQZ](https://stacks.math.columbia.edu/tag/0GQZ) in the Stacks Project.

**`AlgebraicGeometry.FibredSite.isIso_colimit_post_hom_of_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfHom.lean, line 480](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfHom.lean#L480). The attribute's comment: “all modules; condition 0GMR (4) for the equi-universe model of the fppf site is a hypothesis, so quasi-compactness, quasi-separatedness and algebraicity of the stack do not appear; finite presentation is Mathlib's, not 03DL's; the index category is small”.

> **Stacks 0GQZ for all modules.** Let `𝒳` be a category fibred in groupoids over the big fppf
> category of a scheme `S` contained in a big fppf site, with the fppf topology of Stacks 06TP and
> the structure sheaf of Stacks 06TV, and assume its total category essentially small. Let `𝒢` be an
> `𝒪_𝒳`-module of finite presentation and `D` a filtered system of `𝒪_𝒳`-modules. Then the canonical
> comparison
>
> `colim_i Hom_𝒳(𝒢, ℱ_i) ⟶ Hom_𝒳(𝒢, colim_i ℱ_i)`
>
> is a bijection, granted the hypothesis `hX`.
>
> `hX` is the condition of Stacks 0GMR part (4) for the equi-universe model
> `AlgebraicGeometry.FibredSite.fppfModelRingedSite`, which is the site Stacks 0GN0 applies to and
> which the fppf site itself — whose objects lie one universe above its morphisms — is not. It is
> what the source checks for the objects of the site lying over affine schemes, through
> Stacks 0GMS case (2), using quasi-compactness and quasi-separatedness of the algebraic stack.
> Neither of those two hypotheses of the source appears here, and `𝒳` is not assumed to be an
> algebraic stack: they enter only through `hX`.
>
> Finite presentation is `SheafOfModules.IsFinitePresentation`, Mathlib's predicate, which is the
> one Stacks 0GN0 is stated over; the site predicate
> `SheafOfModules.IsFinitePresentationOnSite` of Stacks 03DL used elsewhere in the stacks
> development is not bridged to it anywhere in the tree. See "What is proved and what is assumed"
> in the module docstring.

```lean
theorem isIso_colimit_post_hom_of_isFinitePresentation (hp : p.IsFiberedInGroupoids)
    (G : SheafOfModules.{u} (ringStructureSheafCore B S hS p hp .fppf))
    (hG : G.IsFinitePresentation)
    {K : Type u} [Category.{u} K] [IsFiltered K]
    (D : K ⥤ SheafOfModules.{u} (ringStructureSheafCore B S hS p hp .fppf))
    (hX : ∃ T : Set (Sheaf (fppfModelRingedSite B S hS p hp).J (Type u)),
      (∀ H : Sheaf (fppfModelRingedSite B S hS p hp).J (Type u),
          Sheaf.IsLocallySurjective (terminal.from H) →
            ∃ L ∈ T, Nonempty (L ⟶ H) ∧ Sheaf.IsLocallySurjective (terminal.from L)) ∧
        ∀ L ∈ T, Sheaf.IsQuasiCompact (L ⨯ L))
    [HasColimit D] [HasColimit (D ⋙ coyoneda.obj (Opposite.op G))] :
    IsIso (colimit.post D (coyoneda.obj (Opposite.op G)))
```

**`AlgebraicGeometry.FibredSite.isIso_colimit_post_hom_quasicoherent_of_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfHom.lean, line 509](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfHom.lean#L509). The attribute's comment: “quasi-coherent modules; condition 0GMR (4) for the equi-universe model of the fppf site and preservation of the colimit by the inclusion of QCoh (the colimit clause of 03M1) are hypotheses, so quasi-compactness, quasi-separatedness and algebraicity of the stack do not appear; finite presentation is Mathlib's, not 03DL's; the index category is small”.

> **Stacks 0GQZ for quasi-coherent modules.** The same comparison, for a filtered colimit taken
> in the category `QCoh(𝒪_𝒳)` of Stacks 06WG rather than in all `𝒪_𝒳`-modules.
>
> Beyond the hypothesis `hX` of
> `AlgebraicGeometry.FibredSite.isIso_colimit_post_hom_of_isFinitePresentation` this carries one
> more: that the inclusion of the quasi-coherent modules into all modules preserves colimits of
> shape `K`, which is the colimit clause of Stacks 03M1 for the fppf site of `𝒳`. That clause is
> available for an algebraic space only conditionally, in
> `AlgebraicGeometry.Space.isQuasicoherent_colimit_of_h03DX`, and is not available for a stack.

```lean
theorem isIso_colimit_post_hom_quasicoherent_of_isFinitePresentation
    (hp : p.IsFiberedInGroupoids) (G : quasicoherentModules.{u, u + 1, u, u} B S hS p hp)
    (hG : G.obj.IsFinitePresentation)
    {K : Type u} [Category.{u} K] [IsFiltered K]
    (D : K ⥤ quasicoherentModules.{u, u + 1, u, u} B S hS p hp)
    (hX : ∃ T : Set (Sheaf (fppfModelRingedSite B S hS p hp).J (Type u)),
      (∀ H : Sheaf (fppfModelRingedSite B S hS p hp).J (Type u),
          Sheaf.IsLocallySurjective (terminal.from H) →
            ∃ L ∈ T, Nonempty (L ⟶ H) ∧ Sheaf.IsLocallySurjective (terminal.from L)) ∧
        ∀ L ∈ T, Sheaf.IsQuasiCompact (L ⨯ L))
    [PreservesColimitsOfShape K
      (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        (ringStructureSheafCore B S hS p hp .fppf)).ι]
    [HasColimit D] [HasColimit (D ⋙ coyoneda.obj (Opposite.op G))] :
    IsIso (colimit.post D (coyoneda.obj (Opposite.op G)))
```

**`AlgebraicGeometry.Stack.isIso_colimit_post_hom_of_isQuasiCompactStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfHomQuasiCompactStack.lean, line 452](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfHomQuasiCompactStack.lean#L452). The attribute's comment: “the displayed colimit equality, for all 𝒪_𝒳-modules”.

> **Stacks 0GQZ, the displayed equality.** Let `𝒳` be a quasi-compact and quasi-separated
> algebraic stack over a scheme `S` contained in a big fppf site, with the fppf topology of
> Stacks 06TP and the structure sheaf of Stacks 06TV. Let `𝒢` be an `𝒪_𝒳`-module of finite
> presentation (Stacks 03DL (7)) and `D` a filtered system `i ↦ ℱ_i` of `𝒪_𝒳`-modules. Then
>
> `colim_i Hom_𝒳(𝒢, ℱ_i) = Hom_𝒳(𝒢, colim_i ℱ_i)`,
>
> in the form that the canonical comparison map out of the colimit is a bijection. Both colimits
> exist (`AlgebraicGeometry.FibredSite.hasColimitsOfShape_sheafOfModules_ringStructureSheafCore`).
>
> Quasi-separatedness is that of Stacks 050D part (8), quasi-separatedness over `Spec(ℤ)`, and no
> condition is put on `S`. The index category is a small filtered category, the index set of the
> source being a set of the ambient universe.
>
> The proof is the source's. The equality is the case of Stacks 0GN0 for the fppf ringed site of
> `𝒳`, applied through its equi-universe model, which is
> `AlgebraicGeometry.FibredSite.preservesColimitsOfShape_coyoneda_fppf_of_isFinitePresentation_model`
> at the site hypothesis of Stacks 0GN0. That hypothesis is discharged by
> `AlgebraicGeometry.Stack.FppfModel.exists_set_isLocallySurjective_and_isQuasiCompact_prod_self`
> through Stacks 0GMS case (2), which is where quasi-compactness and quasi-separatedness are used.

```lean
theorem isIso_colimit_post_hom_of_isQuasiCompactStack
    (hqc : IsQuasiCompactStack.{u, w} B S hS 𝒳.val 𝒳.property)
    (h𝒳 : IsQuasiSeparatedAbs.{u, w, w'} B S hS 𝒳)
    (G : _root_.SheafOfModules.{u} (FibredSite.ringStructureSheafCore B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids .fppf))
    (hG : G.IsFinitePresentationOnSite)
    {K : Type u} [Category.{u} K] [IsFiltered K]
    (D : K ⥤ _root_.SheafOfModules.{u} (FibredSite.ringStructureSheafCore B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids .fppf)) :
    letI := FibredSite.hasColimitsOfShape_sheafOfModules_ringStructureSheafCore B S hS
      𝒳.val.val.p 𝒳.val.isFiberedInGroupoids .fppf K
    IsIso (colimit.post D (coyoneda.obj (Opposite.op G)))
```

**`AlgebraicGeometry.Stack.isIso_colimit_post_hom_quasicoherent_of_isQuasiCompactStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfHomQuasiCompactStack.lean, line 482](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfHomQuasiCompactStack.lean#L482). The attribute's comment: “the 'in particular' clause: filtered colimits in QCoh(𝒪_𝒳)”.

> **Stacks 0GQZ, the "in particular" clause.** For a quasi-compact and quasi-separated algebraic
> stack and an `𝒪_𝒳`-module `𝒢` of finite presentation, `Hom_𝒳(𝒢, -)` commutes with filtered
> colimits taken in the category `QCoh(𝒪_𝒳)` of Stacks 06WG: for a filtered system `D` of
> quasi-coherent modules the comparison map from `colim_i Hom_𝒳(𝒢, ℱ_i)` to `Hom_𝒳(𝒢, colim_i ℱ_i)`,
> the colimit taken in `QCoh(𝒪_𝒳)`, is a bijection. Both colimits exist
> (`AlgebraicGeometry.FibredSite.hasColimitsOfSize_quasicoherentModules'`).
>
> `Hom_𝒳(𝒢, -)` on `QCoh(𝒪_𝒳)` is `Hom` in all modules after the full inclusion, so no
> quasi-coherence of `𝒢` is asked for. This is not a restatement of the displayed equality: the
> colimit is the one of `QCoh(𝒪_𝒳)`, and the source's argument is the one used here, that the
> inclusion of `QCoh(𝒪_𝒳)` preserves colimits by the colimit clause of **Stacks 06WV (4)**,
> `AlgebraicGeometry.FibredSite.preservesColimitsOfSize_quasicoherentInclusion'`.

```lean
theorem isIso_colimit_post_hom_quasicoherent_of_isQuasiCompactStack
    (hqc : IsQuasiCompactStack.{u, w} B S hS 𝒳.val 𝒳.property)
    (h𝒳 : IsQuasiSeparatedAbs.{u, w, w'} B S hS 𝒳)
    (G : _root_.SheafOfModules.{u} (FibredSite.ringStructureSheafCore B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids .fppf))
    (hG : G.IsFinitePresentationOnSite)
    {K : Type u} [Category.{u} K] [IsFiltered K]
    (D : K ⥤ FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids) :
    letI := FibredSite.hasColimitsOfSize_quasicoherentModules' B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids
    IsIso (colimit.post D ((_root_.SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
      (FibredSite.ringStructureSheafCore B S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids
        .fppf)).ι ⋙ coyoneda.obj (Opposite.op G)))
```

**`AlgebraicGeometry.Stack.isIso_colimit_post_hom_and_quasicoherent_of_isQuasiCompactStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfHomQuasiCompactStack.lean, line 519](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ColimitsOfHomQuasiCompactStack.lean#L519). The attribute's comment: “the whole statement: the displayed colimit equality together with the 'in particular' clause for QCoh(𝒪_𝒳)”.

> **Stacks 0GQZ in full.** For a quasi-compact and quasi-separated algebraic stack `𝒳`
> (Stacks 04YB, Stacks 050D part (8)) and every small filtered index category `K`: for every
> `𝒪_𝒳`-module `𝒢` of finite presentation (Stacks 03DL (7)), the displayed equality
> `colim_i Hom_𝒳(𝒢, ℱ_i) = Hom_𝒳(𝒢, colim_i ℱ_i)` holds for every system `i ↦ ℱ_i` of `𝒪_𝒳`-modules
> indexed by `K`, *and* `Hom_𝒳(𝒢, -)` commutes with colimits of shape `K` taken in `QCoh(𝒪_𝒳)`.
>
> The two conjuncts are
> `AlgebraicGeometry.Stack.isIso_colimit_post_hom_of_isQuasiCompactStack` and
> `AlgebraicGeometry.Stack.isIso_colimit_post_hom_quasicoherent_of_isQuasiCompactStack`; the
> colimits involved exist in both module categories.

```lean
theorem isIso_colimit_post_hom_and_quasicoherent_of_isQuasiCompactStack
    (hqc : IsQuasiCompactStack.{u, w} B S hS 𝒳.val 𝒳.property)
    (h𝒳 : IsQuasiSeparatedAbs.{u, w, w'} B S hS 𝒳)
    (K : Type u) [Category.{u} K] [IsFiltered K] :
    ∀ (G : _root_.SheafOfModules.{u} (FibredSite.ringStructureSheafCore B S hS 𝒳.val.val.p
        𝒳.val.isFiberedInGroupoids .fppf)),
      G.IsFinitePresentationOnSite →
        (∀ (D : K ⥤ _root_.SheafOfModules.{u} (FibredSite.ringStructureSheafCore B S hS
            𝒳.val.val.p 𝒳.val.isFiberedInGroupoids .fppf)),
          letI := FibredSite.hasColimitsOfShape_sheafOfModules_ringStructureSheafCore B S hS
            𝒳.val.val.p 𝒳.val.isFiberedInGroupoids .fppf K
          IsIso (colimit.post D (coyoneda.obj (Opposite.op G)))) ∧
        ∀ (D : K ⥤ FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS 𝒳.val.val.p
            𝒳.val.isFiberedInGroupoids),
          letI := FibredSite.hasColimitsOfSize_quasicoherentModules' B S hS 𝒳.val.val.p
            𝒳.val.isFiberedInGroupoids
          IsIso (colimit.post D ((_root_.SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
            (FibredSite.ringStructureSheafCore B S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids
              .fppf)).ι ⋙ coyoneda.obj (Opposite.op G)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 103.13, Tag 0GQU](https://stacks.math.columbia.edu/tag/0GQU)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
