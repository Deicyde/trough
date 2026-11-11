---
declaration: section
origin: cited
lean: AlgebraicGeometry.pushforward_injective_cechCohomology_isZero, AlgebraicGeometry.pushforward_injective_rightAcyclic_pushforward_of_smallEtale, AlgebraicGeometry.pushforward_injective_rightAcyclic_sections_of_smallEtale, AlgebraicGeometry.exists_abutsTo_leraySpectralSequence_smallEtale
statement: formalized
proof: formalized
---

# 59.54 The Leray spectral sequence

Section 59.54 of the Stacks Project, [Tag 03QA](https://stacks.math.columbia.edu/tag/03QA). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03QB, a lemma

[Tag 03QB](https://stacks.math.columbia.edu/tag/03QB) in the Stacks Project.

**`AlgebraicGeometry.pushforward_injective_cechCohomology_isZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PushforwardAcyclic/CechVanishing.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PushforwardAcyclic/CechVanishing.lean#L43). The attribute's comment: “cech\_vanishing”.

> **Stacks 03QB.** The direct image of an injective abelian sheaf on the small étale site of
> `X` has vanishing positive-degree Čech cohomology for every family of morphisms in the small
> étale site of `Y`.

```lean
public theorem pushforward_injective_cechCohomology_isZero
    (B : BigEtaleSite.{u}) {X Y : B.Scheme} (f : X ⟶ Y)
    (I : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{u + 1})
    [Injective I]
    (E : Covering.{u + 1, u, u + 1} (SmallEtale B Y.obj Y.property))
    (p : ℕ) (hp : 0 < p) :
    IsZero (Stacks.CechSite.cechCohomology E.2
      (((smallEtaleBaseChange B f).sheafPushforwardContinuous
        AddCommGrpCat.{u + 1}
        (SmallEtale.topology B Y.obj Y.property)
        (SmallEtale.topology B X.obj X.property)).obj I).obj p)
```

**`AlgebraicGeometry.pushforward_injective_rightAcyclic_pushforward_of_smallEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PushforwardAcyclic/Pushforward.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PushforwardAcyclic/Pushforward.lean#L120). The attribute's comment: “pushforward\_acyclic”.

> **Stacks 03QB, with no homological-algebra side condition.** The direct image of an injective
> abelian étale sheaf is acyclic for a further direct image.
>
> This is `AlgebraicGeometry.pushforward_injective_rightAcyclic_pushforward` with all three of its
> instance binders discharged, exactly as in
> `AlgebraicGeometry.pushforward_injective_rightAcyclic_sections_of_smallEtale`: sheafification
> comes from Mathlib's plus construction at the coefficient universe `u + 1` and the enough
> injectives from `AlgebraicGeometry.SmallEtale.isGrothendieckAbelian_sheaf_succ`.

```lean
public theorem pushforward_injective_rightAcyclic_pushforward_of_smallEtale
    (B : BigEtaleSite.{u}) {X Y Z : B.Scheme} (f : X ⟶ Y) (g : Y ⟶ Z)
    (I : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{u + 1})
    [Injective I] :
    ((smallEtaleBaseChange B g).sheafPushforwardContinuous
      AddCommGrpCat.{u + 1}
      (SmallEtale.topology B Z.obj Z.property)
      (SmallEtale.topology B Y.obj Y.property)).rightAcyclic
      (((smallEtaleBaseChange B f).sheafPushforwardContinuous
        AddCommGrpCat.{u + 1}
        (SmallEtale.topology B Y.obj Y.property)
        (SmallEtale.topology B X.obj X.property)).obj I)
```

**`AlgebraicGeometry.pushforward_injective_rightAcyclic_sections_of_smallEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PushforwardAcyclic/Sections.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PushforwardAcyclic/Sections.lean#L105). The attribute's comment: “sections\_acyclic”.

> **Stacks 03QB, with no homological-algebra side condition.** The direct image of an injective
> abelian étale sheaf is acyclic for sections over any object of the small étale site of the
> target.
>
> This is `AlgebraicGeometry.pushforward_injective_rightAcyclic_sections` with both of its instance
> binders discharged: abelian presheaves on the small étale site of a scheme in `Scheme.{u}` have a
> sheafification with coefficients in `AddCommGrpCat.{u + 1}` by Mathlib's plus construction, the
> site having its objects in `Type (u + 1)`, and the resulting abelian category of sheaves has
> enough injectives because `AlgebraicGeometry.SmallEtale.isGrothendieckAbelian_sheaf_succ` makes it
> Grothendieck abelian at that coefficient universe.

```lean
public theorem pushforward_injective_rightAcyclic_sections_of_smallEtale
    (B : BigEtaleSite.{u}) {X Y : B.Scheme} (f : X ⟶ Y)
    (I : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{u + 1})
    [Injective I] (V : SmallEtale B Y.obj Y.property) :
    ((sheafSections (SmallEtale.topology B Y.obj Y.property)
      AddCommGrpCat.{u + 1}).obj (Opposite.op V)).rightAcyclic
      (((smallEtaleBaseChange B f).sheafPushforwardContinuous
        AddCommGrpCat.{u + 1}
        (SmallEtale.topology B Y.obj Y.property)
        (SmallEtale.topology B X.obj X.property)).obj I)
```

## Tag 03QC, a proposition

[Tag 03QC](https://stacks.math.columbia.edu/tag/03QC) in the Stacks Project.

**`AlgebraicGeometry.exists_abutsTo_leraySpectralSequence_smallEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LeraySpectralSequence.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LeraySpectralSequence.lean#L226). References: SGA 4½ Arcata (2.3.4), “first spectral sequence”; SGA 4 V (5.3), “small étale sites”; SGA 4 V (5.4), “étale sites, Z = point”; SGA 4 VII (1.5), “H^p(Y,R^qf\_*F) SS”; SGA 4 IX (4.2), “more general”; SGA 4½ Th finitude (1.3), “partial”.

> **The Leray spectral sequence for the small étale site** (Stacks 03QC). Let `f : X ⟶ Y` be
> a morphism in a big étale site and let `F` be an abelian sheaf on the small étale site of `X`.
> There is a cohomological spectral sequence with second page
>
> ```
> E₂^{p,q} ≅ H^p_ét(Y, R^q f_* F),
> ```
>
> the étale cohomology of `Y` with coefficients in the higher direct images of `F`, which abuts
> to the graded family `n ↦ H^n_ét(X, F)` of étale cohomology groups of `X`: some finite
> decreasing filtration of each `H^n_ét(X, F)` has the terms `E_∞^{p,n-p}` as its graded pieces.
>
> Both the second page and the abutment are taken in the derived-functor form of étale
> cohomology, `CategoryTheory.Functor.rightDerivedPlus` of global sections, and `R^q f_*` is the
> `q`-th right derived functor of direct image.
>
> This is `exists_abutsTo_leraySpectralSequence_smallEtale_sections` for the final object of the
> small étale site of `Y`, whose base change is a final object of the small étale site of `X`.

```lean
public theorem exists_abutsTo_leraySpectralSequence_smallEtale
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{u + 1}) :
    ∃ E : CohomologicalSpectralSequence AddCommGrpCat.{u + 1} 0,
      (∀ p q : ℤ, Nonempty ((E.page 2 zero_le_two).X (p, q) ≅
        ((smallEtaleGlobalSections B Y).rightDerivedPlus p).obj
          ((Stacks.HigherDirectImage.pushforward.{u, u + 1} B f).rightDerivedPlus q |>.obj
            F))) ∧
      SpectralSequence.AbutsTo E
        (fun n => ((smallEtaleGlobalSections B X).rightDerivedPlus n).obj F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.54, Tag 03QA](https://stacks.math.columbia.edu/tag/03QA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
