---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.AlgebraicStacks.IsQuasiFinite, AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiFinite_comp, AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiFinite_baseChange, AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiFinite_of_comp_of_isQuasiSeparated_of_isQuasiDM
statement: formalized
proof: formalized
---

# 101.24 Quasi-finite morphisms

Section 101.24 of the Stacks Project, [Tag 0G2L](https://stacks.math.columbia.edu/tag/0G2L). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0G2M, a definition

[Tag 0G2M](https://stacks.math.columbia.edu/tag/0G2M) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsQuasiFinite`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiFiniteAlgebraicStack.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/QuasiFiniteAlgebraicStack.lean#L50).

> A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` *is quasi-finite*
> when it is locally quasi-finite (**Stacks 06PU**) and quasi-compact (**Stacks 050U**).

```lean
abbrev IsQuasiFinite {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) : Prop
```

## Tag 0G2N, a lemma

[Tag 0G2N](https://stacks.math.columbia.edu/tag/0G2N) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiFinite_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiFiniteComposition.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/QuasiFiniteComposition.lean#L53).

> **Stacks 0G2N.** A composite of quasi-finite 1-morphisms of algebraic stacks over `S` is
> quasi-finite: local quasi-finiteness composes by **Stacks 06UD** and quasi-compactness by
> **Stacks 050W**.

```lean
theorem isQuasiFinite_comp
    {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : IsQuasiFinite B S hS f) (hg : IsQuasiFinite B S hS g) :
    IsQuasiFinite B S hS (f ≫ g)
```

## Tag 0G2P, a lemma

[Tag 0G2P](https://stacks.math.columbia.edu/tag/0G2P) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiFinite_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiFiniteBaseChange.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/QuasiFiniteBaseChange.lean#L60).

> **Stacks 0G2P.** A base change of a quasi-finite 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks
> over `S` is quasi-finite: the first projection of any 2-fibre product of the cospan `(g, f)` is
> quasi-finite as soon as `f` is.
>
> Quasi-finiteness is local quasi-finiteness together with quasi-compactness, and the two conjuncts
> are inherited by **Stacks 06UB** and **Stacks 050V** respectively.

```lean
theorem isQuasiFinite_baseChange {𝒳 𝒴 𝒴' : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴' ⟶ 𝒴)
    (P : Bicategory.TwoCommSq g f)
    (hP : Bicategory.IsTwoFibreProduct P)
    (hf : IsQuasiFinite B S hS f) :
    IsQuasiFinite B S hS P.fst
```

## Tag 0G2Q, a lemma

[Tag 0G2Q](https://stacks.math.columbia.edu/tag/0G2Q) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiFinite_of_comp_of_isQuasiSeparated_of_isQuasiDM`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiFiniteCancellation.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/QuasiFiniteCancellation.lean#L79).

> **Stacks 0G2Q.** If a composite of 1-morphisms of algebraic stacks over `S` is quasi-finite
> and its second factor is quasi-separated and quasi-DM, then its first factor is quasi-finite.
>
> Quasi-finiteness is local quasi-finiteness together with quasi-compactness, and the source's
> proof combines the cancellation of each conjunct: local quasi-finiteness cancels against the
> quasi-DM second factor by **Stacks 06UG** and quasi-compactness cancels against the
> quasi-separated second factor by **Stacks 050Y**.

```lean
theorem isQuasiFinite_of_comp_of_isQuasiSeparated_of_isQuasiDM
    {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hfg : IsQuasiFinite B S hS (f ≫ g)) (hgQuasiSeparated : IsQuasiSeparated B S hS g)
    (hgQuasiDM : IsQuasiDM B S hS g) :
    IsQuasiFinite B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.24, Tag 0G2L](https://stacks.math.columbia.edu/tag/0G2L)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
