---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.spectralSpace_points_of_isQuasiCompact_diagonal, AlgebraicGeometry.Stack.spectralSpace_points_of_isAbsolutelyQuasiSeparated, AlgebraicGeometry.Stack.exists_spectralSpace_cover_and_stacksSober
statement: formalized
proof: formalized
---

# 101.30 The topological space of an algebraic stack

Section 101.30 of the Stacks Project, [Tag 0DQM](https://stacks.math.columbia.edu/tag/0DQM). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DQN, a lemma

[Tag 0DQN](https://stacks.math.columbia.edu/tag/0DQN) in the Stacks Project.

**`AlgebraicGeometry.Stack.spectralSpace_points_of_isQuasiCompact_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SpectralPointsAlgebraicStack.lean, line 248](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SpectralPointsAlgebraicStack.lean#L248).

> **Stacks 0DQN.** Let `𝒳` be a quasi-compact algebraic stack over `S` whose absolute diagonal
> `Δ : 𝒳 ⟶ 𝒳 ×_{Spec ℤ} 𝒳` is quasi-compact. Then the topological space of points `|𝒳|` is
> spectral.
>
> The absolute diagonal is read as in Stacks 050D: the relative diagonal of the structure
> morphism of `𝒳` viewed over the terminal scheme `Spec ℤ`, quasi-compact in the sense of
> Stacks 050U.

```lean
theorem spectralSpace_points_of_isQuasiCompact_diagonal (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (hqc : IsQuasiCompactStack.{u, w} B S hS 𝒳.val 𝒳.property)
    (hΔ : IsQuasiCompactMorphism.{u, w} B (⊤_ Scheme.{u}) B.contains_terminal
      (relativeDiagonalAlgebraicStacks B (⊤_ Scheme.{u}) B.contains_terminal
        (structureMorphism B (⊤_ Scheme.{u}) B.contains_terminal
          (AlgebraicStacks.viewOverIntegers B S hS B.contains_terminal 𝒳)))) :
    SpectralSpace (points B S hS 𝒳.val.val 𝒳.val.property)
```

## Tag 0DQP, a lemma

[Tag 0DQP](https://stacks.math.columbia.edu/tag/0DQP) in the Stacks Project.

**`AlgebraicGeometry.Stack.spectralSpace_points_of_isAbsolutelyQuasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SpectralPointsAlgebraicStack.lean, line 277](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SpectralPointsAlgebraicStack.lean#L277).

> **Stacks 0DQP.** The topological space of points `|𝒳|` of a quasi-compact and
> quasi-separated algebraic stack `𝒳` over `S` is spectral.
>
> Quasi-separatedness is absolute quasi-separatedness, part (8) of Stacks 050D; its first half is
> quasi-compactness of the absolute diagonal (Stacks 04Z0, part (2)), so this is the special case of
> Stacks 0DQN.

```lean
theorem spectralSpace_points_of_isAbsolutelyQuasiSeparated (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (hqc : IsQuasiCompactStack.{u, w} B S hS 𝒳.val 𝒳.property)
    (hqs : AlgebraicStacks.IsAbsolutelyQuasiSeparated.{u, w} B S hS B.contains_terminal 𝒳) :
    SpectralSpace (points B S hS 𝒳.val.val 𝒳.val.property)
```

## Tag 0DQQ, a lemma

[Tag 0DQQ](https://stacks.math.columbia.edu/tag/0DQQ) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_spectralSpace_cover_and_stacksSober`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SpectralPointsAlgebraicStack.lean, line 351](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SpectralPointsAlgebraicStack.lean#L351).

> **Stacks 0DQQ.** Let `𝒳` be an algebraic stack over `S` whose absolute diagonal
> `Δ : 𝒳 ⟶ 𝒳 ×_{Spec ℤ} 𝒳` is quasi-compact. Then `|𝒳|` has an open covering by spectral
> subspaces, and in particular `|𝒳|` is sober.
>
> The covering is by the images of the affine opens of a smooth surjective chart by a scheme. The
> absolute diagonal is read as in Stacks 050D, as in
> `AlgebraicGeometry.Stack.spectralSpace_points_of_isQuasiCompact_diagonal`.

```lean
theorem exists_spectralSpace_cover_and_stacksSober (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (hΔ : IsQuasiCompactMorphism.{u, w} B (⊤_ Scheme.{u}) B.contains_terminal
      (relativeDiagonalAlgebraicStacks B (⊤_ Scheme.{u}) B.contains_terminal
        (structureMorphism B (⊤_ Scheme.{u}) B.contains_terminal
          (AlgebraicStacks.viewOverIntegers B S hS B.contains_terminal 𝒳)))) :
    (∃ 𝒰 : Set (Set (points B S hS 𝒳.val.val 𝒳.val.property)),
      (∀ W ∈ 𝒰, IsOpen W ∧ SpectralSpace W) ∧ ⋃₀ 𝒰 = Set.univ) ∧
      StacksSober (points B S hS 𝒳.val.val 𝒳.val.property)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.30, Tag 0DQM](https://stacks.math.columbia.edu/tag/0DQM)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
