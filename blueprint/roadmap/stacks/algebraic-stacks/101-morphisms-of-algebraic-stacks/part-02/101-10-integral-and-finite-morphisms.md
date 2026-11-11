---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.AlgebraicStacks.IsIntegralHom, AlgebraicGeometry.Stack.AlgebraicStacks.IsFinite, AlgebraicGeometry.Stack.AlgebraicStacks.isIntegralHom_baseChange, AlgebraicGeometry.Stack.AlgebraicStacks.isFinite_baseChange, AlgebraicGeometry.Stack.AlgebraicStacks.isIntegralHom_comp, AlgebraicGeometry.Stack.AlgebraicStacks.isFinite_comp
statement: formalized
proof: formalized
---

# 101.10 Integral and finite morphisms

Section 101.10 of the Stacks Project, [Tag 0CHT](https://stacks.math.columbia.edu/tag/0CHT). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CHU, a definition

[Tag 0CHU](https://stacks.math.columbia.edu/tag/0CHU) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsIntegralHom`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/IntegralFiniteMorphism.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/IntegralFiniteMorphism.lean#L113). The attribute's comment: “part (1): integral morphisms”.

> **Stacks 0CHU**, part (1). A 1-morphism of algebraic stacks over `S` *is integral* when it is
> representable by algebraic spaces and is integral in the sense of Stacks 04XB: every algebraic
> space representing its base change along a scheme-valued point of the target has integral
> structural morphism, read as a morphism of algebraic spaces over `S`.

```lean
abbrev IsIntegralHom (f : 𝒳 ⟶ 𝒴) : Prop
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Stack.AlgebraicStacks.IsFinite`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/WellNighAffine.lean#L90), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/IntegralFiniteMorphism.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/IntegralFiniteMorphism.lean#L128) (StacksFrontier): “part (2): finite morphisms”.

## Tag 0CHV, a lemma

[Tag 0CHV](https://stacks.math.columbia.edu/tag/0CHV) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isIntegralHom_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/IntegralFiniteMorphism.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/IntegralFiniteMorphism.lean#L163). The attribute's comment: “integral”.

> **Stacks 0CHV**, the integral case. A base change of an integral 1-morphism of algebraic
> stacks over `S` is integral: if `g : 𝒵 ⟶ 𝒴` is integral and `P` is a 2-fibre product of the
> cospan `(f, g)` for a 1-morphism `f : 𝒳 ⟶ 𝒴`, then `P.fst : 𝒵 ×_𝒴 𝒳 ⟶ 𝒳` is integral.
>
> Representability by algebraic spaces base changes by **Stacks 0302** and the relative property
> of Stacks 04XB by **Stacks 045C**, which applies because integrality of morphisms of algebraic
> spaces is stable under base change and local at the target for the fppf precoverage.

```lean
theorem isIntegralHom_baseChange (f : 𝒳 ⟶ 𝒴) (g : 𝒵 ⟶ 𝒴)
    (P : Bicategory.TwoCommSq f g) (hP : Bicategory.IsTwoFibreProduct P)
    (hg : IsIntegralHom B S hS g) :
    IsIntegralHom B S hS P.fst
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isFinite_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/IntegralFiniteMorphism.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/IntegralFiniteMorphism.lean#L184). The attribute's comment: “finite”.

> **Stacks 0CHV**, the finite case. A base change of a finite 1-morphism of algebraic stacks
> over `S` is finite: if `g : 𝒵 ⟶ 𝒴` is finite and `P` is a 2-fibre product of the cospan
> `(f, g)` for a 1-morphism `f : 𝒳 ⟶ 𝒴`, then `P.fst : 𝒵 ×_𝒴 𝒳 ⟶ 𝒳` is finite.
>
> Representability by algebraic spaces base changes by **Stacks 0302** and the relative property
> of Stacks 04XB by **Stacks 045C**, which applies because finiteness of morphisms of algebraic
> spaces is stable under base change and local at the target for the fppf precoverage.

```lean
theorem isFinite_baseChange (f : 𝒳 ⟶ 𝒴) (g : 𝒵 ⟶ 𝒴)
    (P : Bicategory.TwoCommSq f g) (hP : Bicategory.IsTwoFibreProduct P)
    (hg : IsFinite B S hS g) :
    IsFinite B S hS P.fst
```

## Tag 0CHW, a lemma

[Tag 0CHW](https://stacks.math.columbia.edu/tag/0CHW) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isIntegralHom_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/IntegralFiniteMorphism.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/IntegralFiniteMorphism.lean#L211). The attribute's comment: “integral”.

> **Stacks 0CHW**, the integral case: a composite of integral 1-morphisms of algebraic stacks
> over `S` is integral.
>
> Representability by algebraic spaces composes by **Stacks 0301** and the relative property of
> Stacks 04XB by **Stacks 045B**, which applies because
> integrality of morphisms of algebraic spaces is stable under base change and under composition
> (**Stacks 03ZR**) and local at the target for the fppf precoverage.

```lean
theorem isIntegralHom_comp (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : IsIntegralHom B S hS f) (hg : IsIntegralHom B S hS g) :
    IsIntegralHom B S hS (f ≫ g)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isFinite_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/IntegralFiniteMorphism.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/IntegralFiniteMorphism.lean#L228). The attribute's comment: “finite”.

> **Stacks 0CHW**, the finite case: a composite of finite 1-morphisms of algebraic stacks over
> `S` is finite.
>
> Representability by algebraic spaces composes by **Stacks 0301** and the relative property of
> Stacks 04XB by **Stacks 045B**, which applies because finiteness of morphisms of algebraic
> spaces is stable under base change and under composition (**Stacks 03ZR**) and local at the
> target for the fppf precoverage.

```lean
theorem isFinite_comp (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : IsFinite B S hS f) (hg : IsFinite B S hS g) :
    IsFinite B S hS (f ≫ g)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.10, Tag 0CHT](https://stacks.math.columbia.edu/tag/0CHT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
