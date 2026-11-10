---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.hasReducedSingletonPointMonomorphism_of_isQuasiCompact_inertia, AlgebraicGeometry.Stack.exists_isResidualGerbeAt_of_isAbsolutelyQuasiDM, AlgebraicGeometry.Stack.exists_isResidualGerbeAt_of_isLocallyNoetherianStack
statement: formalized
proof: formalized
---

# 101.31 Existence of residual gerbes

Section 101.31 of the Stacks Project, [Tag 06UH](https://stacks.math.columbia.edu/tag/06UH). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06RD, a lemma

[Tag 06RD](https://stacks.math.columbia.edu/tag/06RD) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasReducedSingletonPointMonomorphism_of_isQuasiCompact_inertia`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeQuasiCompactInertia.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeQuasiCompactInertia.lean#L78).

> Let `𝒳` be an algebraic stack over `S` whose inertia projection `I_𝒳 ⟶ 𝒳` is
> quasi-compact. Then the residual gerbe of `𝒳` exists at every point `x` of `|𝒳|`, in the sense
> of Stacks 06MU (1), condition (2) of Stacks 06MT: there is a reduced algebraic stack `𝒵` with a
> monomorphism `𝒵 ⟶ 𝒳` whose space of points is a single point lying over `x`.

```lean
theorem hasReducedSingletonPointMonomorphism_of_isQuasiCompact_inertia
    (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (hqc : IsQuasiCompactMorphism.{u, w} B S hS (inertiaProjectionAlgebraicStacks B S hS 𝒳))
    (x : points B S hS 𝒳.val.val (Classical.choose 𝒳.property)) :
    HasReducedSingletonPointMonomorphism B S hS 𝒳 x
```

## Tag 06UI, a lemma

[Tag 06UI](https://stacks.math.columbia.edu/tag/06UI) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_isResidualGerbeAt_of_isAbsolutelyQuasiDM`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeQuasiDMExistence.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeQuasiDMExistence.lean#L68). The attribute's comment: “the residual gerbe of a quasi-DM algebraic stack exists at every point of its space, in the sense of 06MU: some strictly full subcategory meets the 06MT specification IsResidualGerbeAt, i.e. is a reduced locally Noetherian algebraic substack with one point lying over x. Nothing is left open: the source's chart comes from 06MF proved outright (hasQuasiDMPresentation_of_isAbsolutelyQuasiDM) and its 06S1 step from isLocallyQuasiFinite_comp_of_mono_to_field”.

> **Stacks 06UI.** Let `𝒳` be a quasi-DM algebraic stack over `S`. Then the residual gerbe of
> `𝒳` at `x` exists for every `x ∈ |𝒳|`: some strictly full subcategory `P` of `𝒳` meets the
> specification `AlgebraicGeometry.Stack.IsResidualGerbeAt` of **Stacks 06MT**, which by
> **Stacks 06MU** is what it means for the residual gerbe at `x` to exist.
>
> This is
> `AlgebraicGeometry.Stack.exists_isResidualGerbeAt_of_isAbsolutelyQuasiDM_of_hasQuasiDMPresentation`
> — the source's proof, with **Stacks 06S1** already supplied — applied to the substantial
> direction of **Stacks 06MF**,
> `AlgebraicGeometry.Stack.hasQuasiDMPresentation_of_isAbsolutelyQuasiDM`.

```lean
theorem exists_isResidualGerbeAt_of_isAbsolutelyQuasiDM
    (hZ : B.Contains (⊤_ Scheme.{u}))
    (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (h𝒳 : AlgebraicStacks.IsAbsolutelyQuasiDM B S hS hZ 𝒳)
    (x : AlgebraicStacks.points B S hS 𝒳) :
    ∃ P : ObjectProperty 𝒳.val.val.obj, IsResidualGerbeAt B S hS 𝒳 x P
```

## Tag 0H22, a lemma

[Tag 0H22](https://stacks.math.columbia.edu/tag/0H22) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_isResidualGerbeAt_of_isLocallyNoetherianStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeLocallyNoetherian.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeLocallyNoetherian.lean#L175).

> **Stacks 0H22.** Let `𝒳` be a locally Noetherian algebraic stack. Then the residual gerbe of
> `𝒳` at `x` exists for every `x ∈ |𝒳|`: some strictly full subcategory of `𝒳` meets the
> specification `AlgebraicGeometry.Stack.IsResidualGerbeAt` of Stacks 06MT at `x`.
>
> See the module documentation for the argument.

```lean
theorem exists_isResidualGerbeAt_of_isLocallyNoetherianStack (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (h𝒳 : IsLocallyNoetherianStack B S hS 𝒳) (x : AlgebraicStacks.points B S hS 𝒳) :
    ∃ P : ObjectProperty 𝒳.val.val.obj, IsResidualGerbeAt B S hS 𝒳 x P
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.31, Tag 06UH](https://stacks.math.columbia.edu/tag/06UH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
