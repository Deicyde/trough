---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.IsFormallySmoothOnObjects, AlgebraicGeometry.BigFppfOver.isFormallySmoothOnObjects_baseChange, AlgebraicGeometry.BigFppfOver.isFormallySmoothOnObjects_comp, AlgebraicGeometry.BigFppfOver.isRelativelyFormallySmooth_of_isFormallySmoothOnObjects, AlgebraicGeometry.BigFppfOver.isFormallySmoothOnObjects_of_isRelativelyFormallySmooth, AlgebraicGeometry.BigFppfOver.isFormallySmoothOnObjects_iff_isRelativelyFormallySmooth
statement: formalized
proof: formalized
---

# 97.6 Formally smooth on objects

Section 97.6 of the Stacks Project, [Tag 06CZ](https://stacks.math.columbia.edu/tag/06CZ). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06D0, an equation

[Tag 06D0](https://stacks.math.columbia.edu/tag/06D0) in the Stacks Project.

**`AlgebraicGeometry.Stack.IsFormallySmoothOnObjects`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FormallySmoothOnObjects.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FormallySmoothOnObjects.lean#L53).

> The first-order lifting condition for a 1-morphism of categories fibred in groupoids, with
> the comparison square required to commute: the restriction along a first-order thickening of
> affine objects is the chosen pullback `CategoryTheory.Functor.pullbackFiber`.

```lean
def IsFormallySmoothOnObjects
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 𝒴 : CatFiberedInGroupoids.{u, v, u + 1, w}
      (BigFppfOver B S hS)) (p : 𝒳 ⟶ 𝒴) : Prop
```

## Tag 06D1, a lemma

[Tag 06D1](https://stacks.math.columbia.edu/tag/06D1) in the Stacks Project.

**`AlgebraicGeometry.BigFppfOver.isFormallySmoothOnObjects_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/FormallySmoothOnObjects.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/FormallySmoothOnObjects.lean#L199).

> **Stacks 06D1.** Formal smoothness on objects is stable under base change.

```lean
theorem isFormallySmoothOnObjects_baseChange
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 𝒴 𝒵 : CatFiberedInGroupoids.{u, max u v, u + 1, max (u + 1) v w}
      (BigFppfOver B S hS))
    (p : 𝒳 ⟶ 𝒴) (q : 𝒵 ⟶ 𝒴)
    (hp : Stack.IsFormallySmoothOnObjects B S hS 𝒳 𝒴 p) :
    Stack.IsFormallySmoothOnObjects B S hS
      (twoFibreProduct B S hS 𝒳 𝒴 𝒵 p q) 𝒵
      (twoFibreProductSnd B S hS 𝒳 𝒴 𝒵 p q)
```

## Tag 06D2, a lemma

[Tag 06D2](https://stacks.math.columbia.edu/tag/06D2) in the Stacks Project.

**`AlgebraicGeometry.BigFppfOver.isFormallySmoothOnObjects_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/FormallySmoothOnObjects.lean, line 413](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/FormallySmoothOnObjects.lean#L413).

> **Stacks 06D2.** A composite of morphisms formally smooth on objects is formally smooth on
> objects.

```lean
theorem isFormallySmoothOnObjects_comp
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 𝒴 𝒵 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS))
    (p : 𝒳 ⟶ 𝒴) (q : 𝒴 ⟶ 𝒵)
    (hp : Stack.IsFormallySmoothOnObjects B S hS 𝒳 𝒴 p)
    (hq : Stack.IsFormallySmoothOnObjects B S hS 𝒴 𝒵 q) :
    Stack.IsFormallySmoothOnObjects B S hS 𝒳 𝒵 (p ≫ q)
```

## Tag 06D3, a lemma

[Tag 06D3](https://stacks.math.columbia.edu/tag/06D3) in the Stacks Project.

**`AlgebraicGeometry.BigFppfOver.isRelativelyFormallySmooth_of_isFormallySmoothOnObjects`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/FormallySmoothOnObjects.lean, line 727](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/FormallySmoothOnObjects.lean#L727). The attribute's comment: “formally smooth on objects implies formally smooth”.

> **Stacks 06D3**, that (1) implies (2): a 1-morphism of categories fibred in groupoids over
> the big fppf site of `S` which is formally smooth on objects is formally smooth, that is, every
> algebraic space representing a base change of it along a scheme-valued point of the target has
> formally smooth structural morphism.
>
> Representability by algebraic spaces, which the source assumes throughout, is not needed for
> this implication: the lifting problem of formal smoothness is transported to a lifting problem
> for objects of the 2-fibre product through whatever equivalence with the category of elements of
> the representing space is supplied.

```lean
theorem isRelativelyFormallySmooth_of_isFormallySmoothOnObjects
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS)} (p : 𝒳 ⟶ 𝒴)
    (hobj : Stack.IsFormallySmoothOnObjects B S hS 𝒳 𝒴 p) :
    IsRelativelyFormallySmooth B S hS p
```

**`AlgebraicGeometry.BigFppfOver.isFormallySmoothOnObjects_of_isRelativelyFormallySmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/FormallySmoothOnObjects.lean, line 1367](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/FormallySmoothOnObjects.lean#L1367). The attribute's comment: “formally smooth implies formally smooth on objects”.

> **Stacks 06D3**, that (2) implies (1): a 1-morphism of categories fibred in groupoids over
> the big fppf site of `S` which is representable by algebraic spaces and formally smooth is
> formally smooth on objects.
>
> Representability is used here, and twice: to produce an algebraic space representing the base
> change of `p` along the scheme-valued point of `𝒴` classifying the given object, which is where
> the hypothesis is applied, and through the 2-Yoneda classifying functor of Stacks 02Y4 that
> turns that object into such a point.

```lean
theorem isFormallySmoothOnObjects_of_isRelativelyFormallySmooth
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS)} (p : 𝒳 ⟶ 𝒴)
    (hp : Stack.IsRepresentableByAlgebraicSpaces B S hS p.hom)
    (hform : IsRelativelyFormallySmooth B S hS p) :
    Stack.IsFormallySmoothOnObjects B S hS 𝒳 𝒴 p
```

**`AlgebraicGeometry.BigFppfOver.isFormallySmoothOnObjects_iff_isRelativelyFormallySmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/FormallySmoothOnObjects.lean, line 1383](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/FormallySmoothOnObjects.lean#L1383). The attribute's comment: “the equivalence”.

> **Stacks 06D3.** For a 1-morphism of categories fibred in groupoids over the big fppf site
> of `S` which is representable by algebraic spaces, being formally smooth on objects and being
> formally smooth — the relative property of Stacks 03YK at formal smoothness, by
> `AlgebraicGeometry.BigFppfOver.isRelativelyFormallySmooth_iff_hasRelativeProperty` — are
> equivalent.

```lean
theorem isFormallySmoothOnObjects_iff_isRelativelyFormallySmooth
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS)} (p : 𝒳 ⟶ 𝒴)
    (hp : Stack.IsRepresentableByAlgebraicSpaces B S hS p.hom) :
    Stack.IsFormallySmoothOnObjects B S hS 𝒳 𝒴 p ↔ IsRelativelyFormallySmooth B S hS p
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 97.6, Tag 06CZ](https://stacks.math.columbia.edu/tag/06CZ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
