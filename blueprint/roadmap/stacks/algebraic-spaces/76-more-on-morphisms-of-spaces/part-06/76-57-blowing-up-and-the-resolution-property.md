---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_isQuasiCompact_dense_isAdmissibleBlowup_hasResolutionProperty, AlgebraicGeometry.Space.exists_closedFiltration_admissibleBlowups_resolutionProperty_unconditional
statement: formalized
proof: formalized
---

# 76.57 Blowing up and the resolution property

Section 76.57 of the Stacks Project, [Tag 0GV4](https://stacks.math.columbia.edu/tag/0GV4). 2 tags here are carried by 1 declaration of the repository (in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GV5, a lemma

[Tag 0GV5](https://stacks.math.columbia.edu/tag/0GV5) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.exists_isQuasiCompact_dense_isAdmissibleBlowup_hasResolutionProperty`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyDenseBlowupUnconditional.lean#L624), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyAfterAdmissibleBlowup.lean, line 24](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyAfterAdmissibleBlowup.lean#L24) (StacksFrontier).

## Tag 0GV6, a lemma

[Tag 0GV6](https://stacks.math.columbia.edu/tag/0GV6) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_closedFiltration_admissibleBlowups_resolutionProperty_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyDenseBlowupUnconditional.lean, line 679](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyDenseBlowupUnconditional.lean#L679).

> **Stacks 0GV6 for an algebraic space over an arbitrary base scheme, with no hypothesis
> beyond the tag's own.**  For a quasi-compact, quasi-separated algebraic space `X` over a scheme
> `S` of the site there are closed subspaces `Z₀ ⊇ Z₁ ⊇ ⋯ ⊇ Z_t` of `X`, each of finite
> presentation over `X`, with `Z₀ ⊆ X` a thickening, with `Z_t` carrying no points, and with a
> `(Z_i ∖ Z_{i+1})`-admissible blowing up of `Z_i` whose source has the resolution property for
> every `i < t`.
>
> This is `AlgebraicGeometry.Space.exists_closedFiltration_admissibleBlowups_resolutionProperty`
> with its hypothesis `h0GV5` discharged by
> `AlgebraicGeometry.Space.forall_exists_isQuasiCompact_dense_isAdmissibleBlowup_`
> `hasResolutionProperty`, read over the terminal scheme.
>
> **The index direction, and an erratum in the source.**  The tag's statement reads "for each
> `i = 0, …, t - 1` there exists a `(Z_i ∖ Z_{i - 1})`-admissible blowing up", with the chain
> `X ⊃ Z_0 ⊃ Z_1 ⊃ ⋯ ⊃ Z_t = ∅`.  That index cannot be meant.  The chain gives `Z_i ⊆ Z_{i - 1}`,
> so `Z_i ∖ Z_{i - 1}` is empty for every `i ≥ 1`, and at `i = 0` it names a `Z_{-1}` the statement
> never introduces.  A `∅`-admissible blowing up is one whose centre is disjoint from `∅`, that is
> any blowing up at all, so the literal reading collapses the clause to "some blowing up of `Z_i`
> has the resolution property" — strictly weaker than intended.  The tag's own proof settles it:
> its induction produces blowing ups admissible with respect to `Z_{1, i} ∖ Z_{1, i + 1}`.  So the
> sets meant are the strata `Z_i ∖ Z_{i + 1}`, which partition `Z_0`, and that is what is proved
> here.

```lean
theorem exists_closedFiltration_admissibleBlowups_resolutionProperty_unconditional
    (X : AlgebraicSpaces B S hS) (hqc : IsQuasiCompactSpace B S hS X.1)
    (hqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X.1) :
    ∃ (t : ℕ) (Z : ℕ → Subfunctor X.1) (hZ : ∀ i, IsClosedSubspace B S hS (Z i)),
      (∀ i, IsFinitePresentation B S hS (Z i).ι) ∧
      (∀ i, Z (i + 1) ≤ Z i) ∧
      IsThickening B S hS X (Z 0) ∧
      IsEmpty (points B S hS (Z t).toFunctor) ∧
      ∀ i < t, ∃ (U : OpenSubspaces B S hS (Z i).toFunctor) (Y : AlgebraicSpaces B S hS)
          (f : Y ⟶ (⟨(Z i).toFunctor, (hZ i).1⟩ : AlgebraicSpaces B S hS)),
        Set.range (pointsMap B S hS U.1.toFunctor (U.1.ι ≫ (Z i).ι)) =
            subspacePointSet B S hS X.1 (Z i) \ subspacePointSet B S hS X.1 (Z (i + 1)) ∧
          IsAdmissibleBlowup B S hS U f ∧
          HasResolutionProperty.{u, u} B S hS Y.1 Y.2
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.57, Tag 0GV4](https://stacks.math.columbia.edu/tag/0GV4)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
