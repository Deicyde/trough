---
declaration: section
origin: cited
lean: Stacks.ProjectiveBundleSplitting.exists_modification_hasInvertibleFiltration', Stacks.Divisors.exists_proper_modification_resolving_partialMap
statement: formalized
proof: formalized
---

# 31.37 Modifications

Section 31.37 of the Stacks Project, [Tag 0AYN](https://stacks.math.columbia.edu/tag/0AYN). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AYP, a lemma

[Tag 0AYP](https://stacks.math.columbia.edu/tag/0AYP) in the Stacks Project.

**`Stacks.ProjectiveBundleSplitting.exists_modification_hasInvertibleFiltration'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveBundleSplitting/InvertibleFiltration.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjectiveBundleSplitting/InvertibleFiltration.lean#L47).

> **Stacks Project, Tag 0AYP.** Let `X` be an integral scheme and `ℰ` a finite locally free
> `𝒪_X`-module of rank `r`. There is a modification `f : X' ⟶ X` such that `f^*ℰ` has a filtration
> `0 = ℰ_0 ⊆ ℰ_1 ⊆ … ⊆ ℰ_r = f^*ℰ` by finite locally free submodules whose successive quotients
> are invertible `𝒪_{X'}`-modules.
>
> This is `exists_modification_hasInvertibleFiltration_of_epi` with its one input, the epimorphy
> of the tautological map of a projective bundle, supplied by `epi_tautologicalMap`.

```lean
theorem exists_modification_hasInvertibleFiltration' (r : ℕ) (X : Scheme.{u}) [IsIntegral X]
    (E : X.Modules)
    (hE : AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E r) :
    ∃ (X' : Scheme.{u}) (f : X' ⟶ X), IsModification f ∧
      HasInvertibleFiltration X' ((Scheme.Modules.pullback f).obj E) r
```

## Tag 0C4V, a lemma

[Tag 0C4V](https://stacks.math.columbia.edu/tag/0C4V) in the Stacks Project.

**`Stacks.Divisors.exists_proper_modification_resolving_partialMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Modification/RationalMap.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Modification/RationalMap.lean#L63).

> **Stacks Project, Tag 0C4V.** An `S`-rational map from a Noetherian scheme to a scheme
> proper over `S` extends to an `S`-morphism after a proper modification which is unchanged over
> the rational map's domain.

```lean
theorem exists_proper_modification_resolving_partialMap
    {S X Y : Scheme.{u}} [X.Over S] [Y.Over S] [IsNoetherian X]
    [IsProper (Y ↘ S)] (f : X.PartialMap Y) [f.IsOver S] :
    ∃ (X' : Scheme.{u}) (p : X' ⟶ X) (f' : X' ⟶ Y),
      IsProper p ∧
        f' ≫ (Y ↘ S) = p ≫ (X ↘ S) ∧
        IsIso (pullback.snd p f.domain.ι) ∧
        pullback.fst p f.domain.ι ≫ f' = pullback.snd p f.domain.ι ≫ f.hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 31.37, Tag 0AYN](https://stacks.math.columbia.edu/tag/0AYN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
