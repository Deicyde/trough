---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.IsIntegral, AlgebraicGeometry.Stack.stacksSober_and_exists_openSubstack_isGerbeOver_of_isIntegral, AlgebraicGeometry.Stack.isIntegral_of_isReducedStack_of_isAbsolutelyQuasiSeparated, AlgebraicGeometry.Stack.bijective_pointClosure_and_bijective_support
statement: formalized
proof: formalized
---

# 101.50 Integral algebraic stacks

Section 101.50 of the Stacks Project, [Tag 0GWA](https://stacks.math.columbia.edu/tag/0GWA). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GWB, a definition

[Tag 0GWB](https://stacks.math.columbia.edu/tag/0GWB) in the Stacks Project.

**`AlgebraicGeometry.Stack.IsIntegral`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/IntegralAlgebraicStack.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/IntegralAlgebraicStack.lean#L72).

> An algebraic stack `𝒳` over `S` is *integral* when it is reduced, it is
> decent, its inertia projection `I_𝒳 ⟶ 𝒳` is quasi-compact, and its space of points `|𝒳|` is
> irreducible.

```lean
abbrev IsIntegral (𝒳 : AlgebraicStacks.{u, w} B S hS) : Prop
```

## Tag 0GWC, a lemma

[Tag 0GWC](https://stacks.math.columbia.edu/tag/0GWC) in the Stacks Project.

**`AlgebraicGeometry.Stack.stacksSober_and_exists_openSubstack_isGerbeOver_of_isIntegral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/IntegralAlgebraicStackStructure.lean, line 266](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/IntegralAlgebraicStackStructure.lean#L266).

> **Stacks 0GWC.** Let `𝒳` be an integral algebraic stack over `S` (**Stacks 0GWB**). Then
> 1. `|𝒳|` is sober (Stacks 004X), irreducible, and has a unique generic point;
> 2. there is an open substack `𝒰 ⊆ 𝒳` which is a gerbe over an integral scheme `U`: a 1-morphism
>    from `𝒰` to the algebraic stack of `U` making `𝒰` a gerbe over it (**Stacks 06QC**).
>
> The two parts are
> `AlgebraicGeometry.Stack.stacksSober_irreducibleSpace_existsUnique_isGenericPoint_of_isIntegral`
> and `AlgebraicGeometry.Stack.exists_openSubstack_isGerbeOver_isIntegral`.

```lean
theorem stacksSober_and_exists_openSubstack_isGerbeOver_of_isIntegral
    (𝒳 : AlgebraicStacks.{u, w} B S hS) (h𝒳 : IsIntegral B S hS 𝒳) :
    (letI := pointTopology B S hS 𝒳.val;
      StacksSober (AlgebraicStacks.points B S hS 𝒳) ∧
        IrreducibleSpace (AlgebraicStacks.points B S hS 𝒳) ∧
          ∃! x : AlgebraicStacks.points B S hS 𝒳, IsGenericPoint x Set.univ) ∧
      ∃ (𝒰 : OpenSubstack 𝒳) (U : BigFppfOver B S hS),
        AlgebraicGeometry.IsIntegral ((BigFppfOver.toScheme B S hS).obj U) ∧
          ∃ f : 𝒰.toAlgebraicStack ⟶ schemeStack.{u, w} B S hS U,
            AlgebraicStacks.IsGerbeOver B S hS f
```

## Tag 0GWD, a lemma

[Tag 0GWD](https://stacks.math.columbia.edu/tag/0GWD) in the Stacks Project.

**`AlgebraicGeometry.Stack.isIntegral_of_isReducedStack_of_isAbsolutelyQuasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/IntegralQuasiSeparatedStack.lean, line 198](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/IntegralQuasiSeparatedStack.lean#L198).

> **Stacks 0GWD.** An algebraic stack `𝒳` over `S` which is reduced and quasi-separated and
> whose space of points `|𝒳|` is irreducible is integral in the sense of Stacks 0GWB.
>
> Two of the four conditions of Stacks 0GWB are hypotheses. Decency is Stacks 0GW2 for a
> quasi-separated algebraic stack. Quasi-compactness of the inertia projection `I_𝒳 ⟶ 𝒳` holds
> because that 1-morphism is the base change of the absolute diagonal `Δ : 𝒳 ⟶ 𝒳 × 𝒳` along
> itself, and `Δ` is quasi-compact since `𝒳` is quasi-separated.

```lean
theorem isIntegral_of_isReducedStack_of_isAbsolutelyQuasiSeparated
    (hZ : B.Contains (⊤_ Scheme.{u})) (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (hred : IsReducedStack.{u, w} B S hS 𝒳)
    (hqs : AlgebraicStacks.IsAbsolutelyQuasiSeparated.{u, w} B S hS hZ 𝒳)
    (hirr : @IrreducibleSpace (points B S hS 𝒳.val.val 𝒳.val.property)
      (pointTopology B S hS 𝒳.val)) :
    IsIntegral.{u, w} B S hS 𝒳
```

## Tag 0GWE, a lemma

[Tag 0GWE](https://stacks.math.columbia.edu/tag/0GWE) in the Stacks Project.

**`AlgebraicGeometry.Stack.bijective_pointClosure_and_bijective_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/IntegralClosedSubstack.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/IntegralClosedSubstack.lean#L114).

> **Stacks 0GWE.** Let `𝒳` be a decent algebraic stack over `S` whose inertia projection
> `I_𝒳 ⟶ 𝒳` is quasi-compact. Then the map `x ↦ closure {x}` from the points of `𝒳` to the
> irreducible closed subsets of `|𝒳|` is bijective, and so is the map `𝒵 ↦ |𝒵|` from the integral
> closed substacks of `𝒳` to the irreducible closed subsets of `|𝒳|`.

```lean
theorem bijective_pointClosure_and_bijective_support
    (hd : IsDecent B S hS 𝒳.val)
    (hqc : IsQuasiCompactMorphism.{u, w} B S hS (inertiaProjectionAlgebraicStacks B S hS 𝒳)) :
    Function.Bijective (pointClosure B S hS 𝒳) ∧
      Function.Bijective (IntegralClosedSubstack.support (𝒳 := 𝒳))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.50, Tag 0GWA](https://stacks.math.columbia.edu/tag/0GWA)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
