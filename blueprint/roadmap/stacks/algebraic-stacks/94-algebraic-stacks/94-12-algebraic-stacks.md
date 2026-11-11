---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.IsAlgebraicStack, AlgebraicGeometry.Stack.IsDeligneMumfordStack, AlgebraicGeometry.Stack.AlgebraicStacks, AlgebraicGeometry.Stack.isAlgebraicStack_iff_of_equivalence, AlgebraicGeometry.Stack.isDeligneMumfordStack_iff_of_equivalence, AlgebraicGeometry.Stack.isAlgebraicStack_iff_of_equivalence', AlgebraicGeometry.Stack.isAlgebraicStack_of_equivalenceOver
statement: formalized
proof: formalized
---

# 94.12 Algebraic stacks

Section 94.12 of the Stacks Project, [Tag 026N](https://stacks.math.columbia.edu/tag/026N). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 026O, a definition

[Tag 026O](https://stacks.math.columbia.edu/tag/026O) in the Stacks Project.

**`AlgebraicGeometry.Stack.IsAlgebraicStack`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicStack.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicStack.lean#L99).

> **Stacks 026O.** A category over the big fppf site of `S` is an *algebraic stack* when it is
> fibred in groupoids, is a stack for the fppf topology, has a diagonal representable
> by algebraic spaces, and has a presentation by a scheme: a 1-morphism from the category
> represented by a scheme `U` over `S`, representable by algebraic spaces, which is surjective and
> smooth in the sense that every algebraic space representing its base change along a scheme-valued
> point of the stack has surjective and smooth structural morphism.
>
> The stack clause is a conjunction of the two renderings of Stacks 02ZJ, the sieve-indexed
> `CategoryTheory.Functor.IsStack` of Stacks 026F and the family-indexed
> `CategoryTheory.Functor.IsStackInGroupoids` of Stacks 02ZI at the descent universe `w`. The
> second conjunct is a consequence of the first — see the implementation notes.

```lean
abbrev IsAlgebraicStack.{u, w, v, t}
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 : BasedCategory.{v, t} (BigFppfOver B S hS)) : Prop
```

## Tag 03YO, a definition

[Tag 03YO](https://stacks.math.columbia.edu/tag/03YO) in the Stacks Project.

**`AlgebraicGeometry.Stack.IsDeligneMumfordStack`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordStack.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordStack.lean#L73).

> **Stacks 03YO.** An algebraic stack over `S` is a *Deligne-Mumford stack* when it admits a
> presentation by a scheme which is surjective and étale: a 1-morphism from the category
> represented by a scheme `U` over `S`, representable by algebraic spaces, such that every
> algebraic space representing its base change along a scheme-valued point of the stack has
> surjective and étale structural morphism.

```lean
abbrev IsDeligneMumfordStack.{u, w}
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 : BasedCategory.{u, u + 1} (BigFppfOver B S hS)) : Prop
```

## Tag 03YP, a definition

[Tag 03YP](https://stacks.math.columbia.edu/tag/03YP) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicStack.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicStack.lean#L129).

> **Stacks 03YP.** The 2-category of algebraic stacks over `S`: the full sub-2-category of the
> 2-category of categories fibred in groupoids over the big fppf site of `S` whose objects are the
> algebraic stacks. Its 1-morphisms and 2-morphisms are those of the ambient 2-category, with no
> further condition.

```lean
abbrev AlgebraicStacks.{u, w}
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
```

## Tag 03YQ, a lemma

[Tag 03YQ](https://stacks.math.columbia.edu/tag/03YQ) in the Stacks Project.

**`AlgebraicGeometry.Stack.isAlgebraicStack_iff_of_equivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicStackEquivalence.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicStackEquivalence.lean#L143). The attribute's comment: “algebraic\_stack\_iff\_of\_equivalence”.

> Two categories over the big fppf site of `S` which are equivalent as categories over that
> site are algebraic stacks at the same time.

```lean
theorem isAlgebraicStack_iff_of_equivalence
    {𝒳 𝒴 : BasedCategory.{v, t} (BigFppfOver B S hS)}
    (e : BasedCategory.Equivalence 𝒳 𝒴) :
    IsAlgebraicStack.{u, w} B S hS 𝒳 ↔ IsAlgebraicStack.{u, w} B S hS 𝒴
```

**`AlgebraicGeometry.Stack.isDeligneMumfordStack_iff_of_equivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicStackEquivalence.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicStackEquivalence.lean#L191). The attribute's comment: “deligne\_mumford\_iff\_of\_equivalence”.

> Two categories over the big fppf site of `S` which are equivalent as categories over that
> site are Deligne-Mumford stacks at the same time.

```lean
theorem isDeligneMumfordStack_iff_of_equivalence
    {𝒳 𝒴 : BasedCategory.{u, u + 1} (BigFppfOver B S hS)}
    (e : BasedCategory.Equivalence 𝒳 𝒴) :
    IsDeligneMumfordStack.{u, w} B S hS 𝒳 ↔ IsDeligneMumfordStack.{u, w} B S hS 𝒴
```

**`AlgebraicGeometry.Stack.isAlgebraicStack_iff_of_equivalence'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicStackEquivalenceInvariance.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicStackEquivalenceInvariance.lean#L89). The attribute's comment: “algebraic stacks”.

> **Stacks 03YQ, the algebraic-stack assertion.** Two categories over the big fppf site of `S`
> which are equivalent as categories over the site are algebraic stacks at the same time.
>
> Stated for categories in the universes `CategoryTheory.BasedCategory.{u, u + 1}`, with both of
> them explicit; `AlgebraicGeometry.Stack.isAlgebraicStack_iff_of_equivalence` is the same
> assertion for categories in arbitrary universes.

```lean
theorem isAlgebraicStack_iff_of_equivalence'
    (𝒳 𝒴 : BasedCategory.{u, u + 1} (BigFppfOver B S hS))
    (e : BasedCategory.Equivalence 𝒳 𝒴) :
    IsAlgebraicStack.{u, w} B S hS 𝒳 ↔ IsAlgebraicStack.{u, w} B S hS 𝒴
```

**`AlgebraicGeometry.Stack.isAlgebraicStack_of_equivalenceOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicStackEquivalenceUniverses.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicStackEquivalenceUniverses.lean#L83). The attribute's comment: “the two categories in independent universes”.

> A category over the big fppf site of `S` which is equivalent over that site to an algebraic
> stack is an algebraic stack, the two categories being allowed independent object and morphism
> universes.

```lean
theorem isAlgebraicStack_of_equivalenceOver
    {𝒳 : BasedCategory.{v₁, t₁} (BigFppfOver B S hS)}
    {𝒴 : BasedCategory.{v₂, t₂} (BigFppfOver B S hS)}
    (e : StacksRepresentableCFG.EquivalenceOver 𝒳.p 𝒴.p)
    (h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳) :
    IsAlgebraicStack.{u, w} B S hS 𝒴
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 94.12, Tag 026N](https://stacks.math.columbia.edu/tag/026N)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
