---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isStackInGroupoids_finiteCoverProjection, AlgebraicGeometry.Stack.isStackInGroupoids_finiteHilbertProjection, AlgebraicGeometry.Stack.finiteHilbertCategory, AlgebraicGeometry.Stack.absoluteHilbertCategory, AlgebraicGeometry.Stack.finiteCoverCategory, AlgebraicGeometry.Stack.forgetRelativeStructure, AlgebraicGeometry.Stack.forgetTarget, AlgebraicGeometry.Stack.forgetAbsoluteStructure
statement: formalized
proof: formalized
---

# 95.18 Finite Hilbert stacks

Section 95.18 of the Stacks Project, [Tag 05WA](https://stacks.math.columbia.edu/tag/05WA). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05WB, a lemma

[Tag 05WB](https://stacks.math.columbia.edu/tag/05WB) in the Stacks Project.

**`AlgebraicGeometry.Stack.isStackInGroupoids_finiteCoverProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/FiniteCoverStack.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/FiniteCoverStack.lean#L47). The attribute's comment: “The category `ℋ_d` of degree-`d` finite locally free covers, i.e. the case `𝒳 = 𝒴 = S` of the source's `ℋ_d(𝒳/𝒴)`, is a stack in groupoids over the big fppf site of `S`. All three conditions of Stacks 02ZI are discharged: condition (1) is `AlgebraicGeometry.Stack.isFiberedInGroupoids_finiteCoverProjection`, condition (2) is `AlgebraicGeometry.Stack.isom_isSheaf_finiteCoverProjection`, and condition (3), effectivity of descent data, is `AlgebraicGeometry.Stack.descentDatum_isEffective_finiteCoverProjection`.”. References: SGA 3 IV (4.5.13), “special case”.

> **The category `ℋ_d` of degree-`d` finite locally free covers is a stack in groupoids over
> the big fppf site of `S`.**

```lean
theorem isStackInGroupoids_finiteCoverProjection :
    (finiteCoverProjection (B := B) (S := S) (hS := hS) (d := d)).IsStackInGroupoids.{w}
      (BigFppfOver.topology B S hS)
```

**`AlgebraicGeometry.Stack.isStackInGroupoids_finiteHilbertProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/StackDescent.lean, line 959](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/StackDescent.lean#L959).

> The relative finite Hilbert category `ℋ_d(𝒳/𝒴)` of a 1-morphism `F : 𝒳 ⟶ 𝒴` of stacks in
> groupoids over the big fppf site of a scheme `S`, endowed with its forgetful functor to the site,
> is a stack in groupoids over `(Sch/S)_fppf`.

```lean
theorem isStackInGroupoids_finiteHilbertProjection :
    (finiteHilbertProjection (B := B) (S := S) (hS := hS)
      (𝒳 := 𝒳) (𝒴 := 𝒴) (F := F) (d := d)).IsStackInGroupoids.{w}
      (BigFppfOver.topology B S hS)
```

## Tag 05WC, a definition

[Tag 05WC](https://stacks.math.columbia.edu/tag/05WC) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Stack.finiteHilbertCategory`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/Basic.lean#L196), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/StackDefinition.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/StackDefinition.lean#L63) (StacksFrontier): “the stack ℋ\_d(𝒳/𝒴)”.
- [`AlgebraicGeometry.Stack.absoluteHilbertCategory`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/Diagram.lean#L261), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/StackDefinition.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/StackDefinition.lean#L65) (StacksFrontier): “ℋ\_d(𝒳), the case 𝒴 = S”.
- [`AlgebraicGeometry.Stack.finiteCoverCategory`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/Diagram.lean#L150), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/StackDefinition.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/StackDefinition.lean#L67) (StacksFrontier): “ℋ\_d, the case 𝒳 = 𝒴 = S”.

## Tag 05WD, an equation

[Tag 05WD](https://stacks.math.columbia.edu/tag/05WD) in the Stacks Project.

**`AlgebraicGeometry.Stack.forgetRelativeStructure`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/Diagram.lean, line 322](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/Diagram.lean#L322). The attribute's comment: “relative Hilbert stack to absolute Hilbert stack”.

> **Stacks 05WD.** The 1-morphism `ℋ_d(𝒳/𝒴) ⟶ ℋ_d(𝒳)` from the relative to the absolute
> finite Hilbert category: forget the object of `𝒴` and the identification, keeping the cover and
> the object of `𝒳`.

```lean
def forgetRelativeStructure :
    finiteHilbertCategory (B := B) (S := S) (hS := hS) (𝒳 := 𝒳) (𝒴 := 𝒴) (F := F) (d := d) ⥤ᵇ
      absoluteHilbertCategory (B := B) (S := S) (hS := hS) (d := d) (𝒳 := 𝒳)
```

**`AlgebraicGeometry.Stack.forgetTarget`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/Diagram.lean, line 338](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/Diagram.lean#L338). The attribute's comment: “relative Hilbert stack to the target stack”.

> **Stacks 05WD.** The 1-morphism `ℋ_d(𝒳/𝒴) ⟶ 𝒴` to the target stack: forget the cover and
> the object of `𝒳`, keeping the object of `𝒴`.

```lean
def forgetTarget :
    finiteHilbertCategory (B := B) (S := S) (hS := hS) (𝒳 := 𝒳) (𝒴 := 𝒴) (F := F) (d := d) ⥤ᵇ
      𝒴.toBasedCategory
```

**`AlgebraicGeometry.Stack.forgetAbsoluteStructure`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/Diagram.lean, line 356](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/Diagram.lean#L356). The attribute's comment: “absolute Hilbert stack to finite covers”.

> **Stacks 05WD.** The 1-morphism `ℋ_d(𝒳) ⟶ ℋ_d` from the absolute finite Hilbert category to
> the category of finite locally free covers: forget the object of `𝒳`.

```lean
def forgetAbsoluteStructure :
    absoluteHilbertCategory (B := B) (S := S) (hS := hS) (d := d) (𝒳 := 𝒳) ⥤ᵇ
      finiteCoverCategory (B := B) (S := S) (hS := hS) (d := d)
```

**`AlgebraicGeometry.Stack.forgetRelativeToFiniteCover`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/Diagram.lean, line 370](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/Diagram.lean#L370). The attribute's comment: “relative Hilbert stack to finite covers”.

> **Stacks 05WD.** The 1-morphism `ℋ_d(𝒳/𝒴) ⟶ ℋ_d` from the relative finite Hilbert category
> to the category of finite locally free covers: forget both stack objects and the
> identification, keeping the cover.

```lean
def forgetRelativeToFiniteCover :
    finiteHilbertCategory (B := B) (S := S) (hS := hS) (𝒳 := 𝒳) (𝒴 := 𝒴) (F := F) (d := d) ⥤ᵇ
      finiteCoverCategory (B := B) (S := S) (hS := hS) (d := d)
```

**`AlgebraicGeometry.Stack.forgetToProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/ProductMorphism.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/ProductMorphism.lean#L188). The attribute's comment: “the 1-morphism of the equation, as the pairing of the two legs”.

> **Stacks 05WD.** The 1-morphism `ℋ_d(𝒳/𝒴) ⟶ ℋ_d(𝒳) × 𝒴` of the equation: the pairing of
> the two legs `AlgebraicGeometry.Stack.forgetRelativeStructure` and
> `AlgebraicGeometry.Stack.forgetTarget`.

```lean
noncomputable def forgetToProduct :
    finiteHilbertCategory (B := B) (S := S) (hS := hS) (𝒳 := 𝒳) (𝒴 := 𝒴) (F := F) (d := d) ⥤ᵇ
      absoluteHilbertTargetProduct
        (B := B) (S := S) (hS := hS) (d := d) (𝒳 := 𝒳) (𝒴 := 𝒴)
```

## Tag 05XV, a lemma

[Tag 05XV](https://stacks.math.columbia.edu/tag/05XV) in the Stacks Project.

**`AlgebraicGeometry.Stack.forgetRelativeStructure_faithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/Faithful.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/Faithful.lean#L123).

> For a positive degree `d`, the 1-morphism `ℋ_d(𝒳/𝒴) ⟶ ℋ_d(𝒳)` from the relative to the
> absolute finite Hilbert category is faithful.

```lean
theorem forgetRelativeStructure_faithful (hd : 0 < d) :
    (forgetRelativeStructure (B := B) (S := S) (hS := hS)
      (d := d) (𝒳 := 𝒳) (𝒴 := 𝒴) (F := F)).toFunctor.Faithful
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 95.18, Tag 05WA](https://stacks.math.columbia.edu/tag/05WA)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
