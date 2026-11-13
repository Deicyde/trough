---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.IsDecent, AlgebraicGeometry.Stack.isDecent_of_isQuasiCompact_diagonal, AlgebraicGeometry.Stack.isDecent_of_isQuasiSeparated, AlgebraicGeometry.Stack.isDecent_of_representable_or_quasiSeparated, AlgebraicGeometry.Stack.isDecent_of_isQuasiCompactMorphism_of_isSurjective, AlgebraicGeometry.Stack.isDecent_of_isGerbeOver
statement: formalized
proof: formalized
---

# 101.48 Decent algebraic stacks

Section 101.48 of the Stacks Project, [Tag 0GW0](https://stacks.math.columbia.edu/tag/0GW0). 5 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GW1, a definition

[Tag 0GW1](https://stacks.math.columbia.edu/tag/0GW1) in the Stacks Project.

**`AlgebraicGeometry.Stack.IsDecent`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DecentStack.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DecentStack.lean#L105).

> A category fibred in groupoids over the big fppf site of `S` — in particular an algebraic
> stack — is *decent* when every one of its points admits a quasi-compact field-valued
> representative.

```lean
abbrev IsDecent : Prop
```

## Tag 0GW2, a lemma

[Tag 0GW2](https://stacks.math.columbia.edu/tag/0GW2) in the Stacks Project.

**`AlgebraicGeometry.Stack.isDecent_of_isQuasiCompact_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactDiagonalDecent.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactDiagonalDecent.lean#L88). The attribute's comment: “quasi-compact diagonal”.

> **An algebraic stack whose absolute diagonal is quasi-compact is decent.**

```lean
theorem isDecent_of_isQuasiCompact_diagonal
    (hZ : B.Contains (⊤_ Scheme.{u})) (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (hΔ : IsQuasiCompactMorphism.{u, w} B (⊤_ Scheme.{u}) hZ
      (relativeDiagonalAlgebraicStacks B (⊤_ Scheme.{u}) hZ
        (structureMorphism B (⊤_ Scheme.{u}) hZ
          (AlgebraicStacks.viewOverIntegers B S hS hZ 𝒳)))) :
    IsDecent B S hS 𝒳.val
```

**`AlgebraicGeometry.Stack.isDecent_of_isQuasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiSeparatedDecent.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/QuasiSeparatedDecent.lean#L44). The attribute's comment: “quasi-separated case”.

> **A quasi-separated algebraic stack is decent.** If `𝒳` is quasi-separated in the absolute
> sense, then every point of `𝒳` has a field-valued representative which is quasi-compact.

```lean
theorem isDecent_of_isQuasiSeparated (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (h𝒳 : AlgebraicStacks.IsAbsolutelyQuasiSeparated.{u, w} B S hS hZ 𝒳) :
    IsDecent B S hS 𝒳.val
```

## Tag 0GW3, a lemma

[Tag 0GW3](https://stacks.math.columbia.edu/tag/0GW3) in the Stacks Project.

**`AlgebraicGeometry.Stack.isDecent_of_representable_or_quasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RepresentableDecent.lean, line 446](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RepresentableDecent.lean#L446).

> **Stacks 0GW3.** The source of a 1-morphism of algebraic stacks over `S` with decent target
> is decent as soon as the 1-morphism is representable by schemes, or is representable by algebraic
> spaces and quasi-separated.
>
> The argument is the source's.  Fix a point `x` of `𝒳`; decency of `𝒴` supplies a *quasi-compact*
> field-valued representative `q` of the image of `x`, and the 1-morphism `g : Spec k ⟶ 𝒴` it
> determines is quasi-compact (**Stacks 050T**).  Form the 2-fibre product `P` of `g` and `f`
> (**Stacks 04T2**); its second projection is quasi-compact as a base change of `g`
> (**Stacks 050V**), and by **Stacks 04XH** the pair consisting of the point of `Spec k` named by
> `q` and of `x` lifts to a point `w` of `P`.  Any field-valued representative `p` of `w` then has
> quasi-compact 1-morphism — in the representable case because `P` is the stack of a scheme, in the
> quasi-separated case because the composite of that 1-morphism with the *first* projection is
> quasi-compact and the first projection is quasi-separated, so **Stacks 050Y** cancels it — and the
> field-valued point of `𝒳` it induces represents `x` with quasi-compact 1-morphism by
> **Stacks 050W**.
>
> Unlike the source, no appeal to **Stacks 0DTK** is needed: the representative is chosen
> downstream rather than tested, so only the existential form of decency is ever used.

```lean
theorem isDecent_of_representable_or_quasiSeparated
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (h𝒴 : IsDecent B S hS 𝒴.val)
    (hf : Stacks.RepresentableMorphism.IsRepresentableMorphism 𝒳.val.val.p 𝒴.val.val.p
        (CatFiberedInGroupoids.homFunctor f.hom) ∨
      (IsRepresentableByAlgebraicSpaces B S hS f.hom.hom ∧
        AlgebraicStacks.IsQuasiSeparated B S hS f)) :
    IsDecent B S hS 𝒳.val
```

## Tag 0GW4, a lemma

[Tag 0GW4](https://stacks.math.columbia.edu/tag/0GW4) in the Stacks Project.

**`AlgebraicGeometry.Stack.isDecent_of_isQuasiCompactMorphism_of_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactSurjectiveDecent.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactSurjectiveDecent.lean#L127).

> **Stacks 0GW4.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S`. If `f` is
> quasi-compact and surjective and `𝒳` is decent, then `𝒴` is decent.
>
> Let `y` be a point of `𝒴`. Surjectivity of `f` is surjectivity of the map on points
> (**Stacks 04ZS**), so `y` is the image of a point `x` of `𝒳`, and decency of `𝒳` supplies a
> field-valued representative `p` of `x` whose 1-morphism `Spec k ⟶ 𝒳` is quasi-compact
> (**Stacks 050T**). The image field-valued point `f ∘ p` has the same base, represents `y`, and
> its 1-morphism is the composite of that of `p` with `f`, hence quasi-compact by **Stacks 050W**.

```lean
theorem isDecent_of_isQuasiCompactMorphism_of_isSurjective
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : IsQuasiCompactMorphism.{u, w} B S hS f)
    (hsurj : IsSurjective.{u, w} B S hS f)
    (h𝒳 : IsDecent B S hS 𝒳.val) :
    IsDecent B S hS 𝒴.val
```

## Tag 0GW5, a lemma

[Tag 0GW5](https://stacks.math.columbia.edu/tag/0GW5) in the Stacks Project.

**`AlgebraicGeometry.Stack.isDecent_of_isGerbeOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeDecent.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GerbeDecent.lean#L109).

> **Stacks 0GW5.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S`. If `f`
> exhibits `𝒳` as a gerbe over `𝒴` (**Stacks 06QC**) and `𝒳` is decent (**Stacks 0GW1**), then `𝒴`
> is decent.
>
> By **Stacks 06R9** `f` is a universal homeomorphism (**Stacks 0CI7**), hence quasi-compact,
> through `AlgebraicGeometry.Stack.isQuasiCompactMorphism_of_universalHomeomorphism`; surjectivity
> of `f` comes from the gerbe condition directly, by the surjectivity clause of **Stacks 06QI**.
> With both in hand the conclusion is **Stacks 0GW4**.

```lean
theorem isDecent_of_isGerbeOver
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : AlgebraicStacks.IsGerbeOver.{u, w} B S hS f)
    (h𝒳 : IsDecent B S hS 𝒳.val) :
    IsDecent B S hS 𝒴.val
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.48, Tag 0GW0](https://stacks.math.columbia.edu/tag/0GW0)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
