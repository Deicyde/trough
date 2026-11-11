---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isAlgebraicStack_inertia, AlgebraicGeometry.Stack.isAlgebraicStack_relativeInertia, AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyOfFiniteType_inertiaProjection, AlgebraicGeometry.Stack.isLocallyOfFiniteType_inertiaProjection, AlgebraicGeometry.Stack.isLocallyOfFiniteType_relativeInertiaProjection, AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_inertiaProjection, AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_inertiaProjection_of_isAlgebraicStack, AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_relativeInertiaProjection_of_isAlgebraicStack
statement: formalized
proof: formalized
---

# 101.5 Inertia stacks

Section 101.5 of the Stacks Project, [Tag 050P](https://stacks.math.columbia.edu/tag/050P). 8 tags here are carried by 92 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 050Q, a lemma

[Tag 050Q](https://stacks.math.columbia.edu/tag/050Q) in the Stacks Project.

**`AlgebraicGeometry.Stack.isAlgebraicStack_inertia`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/InertiaAlgebraic.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/InertiaAlgebraic.lean#L55). The attribute's comment: “absolute inertia is algebraic”.

> The inertia `I_𝒳` of an algebraic stack `𝒳` over `S` is an algebraic stack over `S`.

```lean
theorem isAlgebraicStack_inertia
    (𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS))
    (h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳.val) :
    IsAlgebraicStack.{u, w} B S hS (inertia B S hS 𝒳).val
```

**`AlgebraicGeometry.Stack.isAlgebraicStack_relativeInertia`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/InertiaAlgebraic.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/InertiaAlgebraic.lean#L120). The attribute's comment: “relative inertia is algebraic”.

> The relative inertia `I_{𝒳/𝒴}` of a 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` is
> an algebraic stack over `S`.

```lean
theorem isAlgebraicStack_relativeInertia
    (𝒳 𝒴 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS))
    (f : 𝒳 ⟶ 𝒴)
    (h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳.val)
    (h𝒴 : IsAlgebraicStack.{u, w} B S hS 𝒴.val) :
    IsAlgebraicStack.{u, w} B S hS (RelativeInertia.basedCategory f.hom)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyOfFiniteType_inertiaProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/InertiaFieldSpectrumCover.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/InertiaFieldSpectrumCover.lean#L92). The attribute's comment: “local finite type of the inertia projection in the sense of Stacks 06FS part (1)”.

> **Stacks 050Q, local finite type of the inertia projection, in the sense of Stacks 06FS
> part (1).** The forgetful 1-morphism `I_𝒳 ⟶ 𝒳` of the inertia of an algebraic stack `𝒳` over `S`
> is locally of finite type as a 1-morphism of algebraic stacks.
>
> `AlgebraicGeometry.Stack.isLocallyOfFiniteType_inertiaProjection` is the same statement in the
> relative sense of Properties of Stacks, Section 04XB; the inertia projection is representable by
> algebraic spaces by Stacks 050Q, so **Stacks 06FM** for a representable 1-morphism converts the
> relative property into the existential smooth-diagram test, and the universal one follows because
> local finite type is smooth local on the source-and-target.

```lean
theorem isLocallyOfFiniteType_inertiaProjection (𝒳 : Stack.AlgebraicStacks.{u, w} B S hS) :
    IsLocallyOfFiniteType B S hS (Stack.inertiaProjectionAlgebraicStacks B S hS 𝒳)
```

**`AlgebraicGeometry.Stack.isLocallyOfFiniteType_inertiaProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/InertiaProjectionFiniteType.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/InertiaProjectionFiniteType.lean#L197). The attribute's comment: “local finite type of the absolute inertia projection”.

> **Stacks 050Q, local finite type of the inertia projection.** The forgetful 1-morphism
> `π : I_𝒳 ⟶ 𝒳` of the inertia of an algebraic stack `𝒳` over `S` is locally of finite type, in
> the sense of Properties of Stacks, Section 04XB.
>
> By Stacks 034H (1) the inertia is the 2-fibre product `𝒳 ×_{Δ, 𝒳 × 𝒳, Δ} 𝒳`, and under that
> identification `π` is the first projection of the canonical 2-fibre product square over the
> cospan `(Δ, Δ)`, hence a base change of `Δ`. So this is Stacks 045C applied to
> `AlgebraicGeometry.Stack.isLocallyOfFiniteType_diagonal_of_isAlgebraicStack` and transported
> along that equivalence of sources by Stacks 0457.

```lean
theorem isLocallyOfFiniteType_inertiaProjection (𝒳 : AlgebraicStacks.{u, w} B S hS) :
    IsLocallyOfFiniteType B S hS (inertiaProjectionAlgebraicStacks.{u, w} B S hS 𝒳).hom
```

**`AlgebraicGeometry.Stack.isLocallyOfFiniteType_relativeInertiaProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/InertiaProjectionFiniteType.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/InertiaProjectionFiniteType.lean#L216). The attribute's comment: “local finite type of the relative inertia projection”.

> **Stacks 050Q, local finite type of the relative inertia projection.** The forgetful
> 1-morphism `π : I_{𝒳/𝒴} ⟶ 𝒳` of the relative inertia of a 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic
> stacks over `S` is locally of finite type, in the sense of Properties of Stacks, Section 04XB.
>
> By Stacks 034H (1) the relative inertia is the 2-fibre product `𝒳 ×_{Δ_f, 𝒳 ×_𝒴 𝒳, Δ_f} 𝒳`, and
> under that identification `π` is the first projection of the canonical 2-fibre product square
> over the cospan `(Δ_f, Δ_f)`, hence a base change of the relative diagonal. So this is Stacks
> 045C applied to part (2) of Stacks 04XS, transported along that equivalence of sources by
> Stacks 0457.

```lean
theorem isLocallyOfFiniteType_relativeInertiaProjection
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) :
    IsLocallyOfFiniteType B S hS (relativeInertiaProjection B S hS f).hom
```

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_inertiaProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/InertiaProjectionRepresentable.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/InertiaProjectionRepresentable.lean#L55). The attribute's comment: “representability by algebraic spaces of the absolute inertia projection”.

> If the diagonal of a category fibred in groupoids `𝒳` over the big fppf site of `S` is
> representable by algebraic spaces, then so is the forgetful 1-morphism `π : I_𝒳 ⟶ 𝒳` of its
> inertia.

```lean
theorem isRepresentableByAlgebraicSpaces_inertiaProjection
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 : CatFiberedInGroupoids.{u, max u v, u + 1, max (u + 1) v w} (BigFppfOver B S hS))
    (hΔ : IsRepresentableByAlgebraicSpaces B S hS (diagonalBasedFunctor B S hS 𝒳)) :
    IsRepresentableByAlgebraicSpaces B S hS
      (RelativeInertia.basedProjection
        (𝒴 := BasedCategory.ofFunctor (𝟭 (BigFppfOver B S hS)))
        ⟨𝒳.val.p, rfl⟩)
```

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_inertiaProjection_of_isAlgebraicStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/InertiaProjectionRepresentable.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/InertiaProjectionRepresentable.lean#L100). The attribute's comment: “the inertia projection of an algebraic stack is representable by spaces”.

> The forgetful 1-morphism `π : I_𝒳 ⟶ 𝒳` of the inertia of an algebraic stack `𝒳` is
> representable by algebraic spaces.

```lean
theorem isRepresentableByAlgebraicSpaces_inertiaProjection_of_isAlgebraicStack
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 : CatFiberedInGroupoids.{u, max u v, u + 1, max (u + 1) v w} (BigFppfOver B S hS))
    (h𝒳 : IsAlgebraicStack.{u, t} B S hS 𝒳.val) :
    IsRepresentableByAlgebraicSpaces B S hS
      (RelativeInertia.basedProjection
        (𝒴 := BasedCategory.ofFunctor (𝟭 (BigFppfOver B S hS)))
        ⟨𝒳.val.p, rfl⟩)
```

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_relativeInertiaProjection_of_isAlgebraicStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaProjectionRepresentable.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaProjectionRepresentable.lean#L185). The attribute's comment: “representability by algebraic spaces of the relative inertia projection”.

> **Stacks 050Q for the relative inertia of a morphism of algebraic stacks.** The forgetful
> 1-morphism `π : I_{𝒳/𝒴} ⟶ 𝒳` of the relative inertia of a 1-morphism of algebraic stacks is
> representable by algebraic spaces. Only the representability of the two diagonals — the second
> clause of `AlgebraicGeometry.Stack.IsAlgebraicStack` — is used.
>
> The source's statement also asserts that `I_{𝒳/𝒴}` is an algebraic stack and that `π` is
> locally of finite type; neither is proved here.

```lean
theorem isRepresentableByAlgebraicSpaces_relativeInertiaProjection_of_isAlgebraicStack
    (𝒳 𝒴 : CatFiberedInGroupoids.{u, max u v, u + 1, max (max (u + 1) w) v}
      (BigFppfOver B S hS))
    (f : 𝒳 ⟶ 𝒴)
    (h𝒳 : IsAlgebraicStack.{u, t} B S hS 𝒳.val)
    (h𝒴 : IsAlgebraicStack.{u, t} B S hS 𝒴.val) :
    IsRepresentableByAlgebraicSpaces B S hS (RelativeInertia.basedProjection f.hom)
```

## Tag 050R, a remark

[Tag 050R](https://stacks.math.columbia.edu/tag/050R) in the Stacks Project.

**`CategoryTheory.RelativeInertia.inverse`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupAxioms.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupAxioms.lean#L96). The attribute's comment: “the inverse”.

> The inverse of the group law: the 1-morphism `i : I_{S/S'} ⟶ I_{S/S'}`,
> `(x, α) ↦ (x, α⁻¹)`, acting on morphisms by the identity.

```lean
def inverse (F : S ⥤ S') : RelativeInertia F ⥤ RelativeInertia F
```

**`CategoryTheory.RelativeInertia.inverse_comp_π`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupAxioms.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupAxioms.lean#L120). The attribute's comment: “the inverse is a morphism over the source”.

> **The inverse is a morphism over the source**: followed by the projection to `S` it is that
> projection again.

```lean
theorem inverse_comp_π (F : S ⥤ S') :
    inverse F ⋙ RelativeInertia.π F = RelativeInertia.π F
```

**`CategoryTheory.RelativeInertia.composition_pairIdNeutral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupAxioms.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupAxioms.lean#L247). The attribute's comment: “the right unit axiom”.

> The right unit axiom: `c ∘ ⟨id, e ∘ π⟩ = id`.

```lean
theorem composition_pairIdNeutral :
    pairIdNeutral F p ⋙ composition F p = 𝟭 (RelativeInertia F)
```

**`CategoryTheory.RelativeInertia.composition_pairNeutralId`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupAxioms.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupAxioms.lean#L261). The attribute's comment: “the left unit axiom”.

> The left unit axiom: `c ∘ ⟨e ∘ π, id⟩ = id`.

```lean
theorem composition_pairNeutralId :
    pairNeutralId F p ⋙ composition F p = 𝟭 (RelativeInertia F)
```

**`CategoryTheory.RelativeInertia.composition_pairIdInverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupAxioms.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupAxioms.lean#L276). The attribute's comment: “the right inverse axiom”.

> The right inverse axiom: `c ∘ ⟨id, i⟩ = e ∘ π`.

```lean
theorem composition_pairIdInverse :
    pairIdInverse F p ⋙ composition F p =
      RelativeInertia.π F ⋙ RelativeInertia.neutralSection F
```

**`CategoryTheory.RelativeInertia.composition_pairInverseId`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupAxioms.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupAxioms.lean#L292). The attribute's comment: “the left inverse axiom”.

> The left inverse axiom: `c ∘ ⟨i, id⟩ = e ∘ π`.

```lean
theorem composition_pairInverseId :
    pairInverseId F p ⋙ composition F p =
      RelativeInertia.π F ⋙ RelativeInertia.neutralSection F
```

**`CategoryTheory.RelativeInertia.composition_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupAxioms.lean, line 448](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupAxioms.lean#L448). The attribute's comment: “the associativity axiom”.

> The associativity axiom: `c ∘ (c × id) = c ∘ (id × c) ∘ assoc` as
> 1-morphisms `(I_{S/S'} ×_S I_{S/S'}) ×_S I_{S/S'} ⟶ I_{S/S'}` over `S`: both send
> `(((x, α), (x', α'), β), (x'', α''), δ)` to `(x, α ∘ β⁻¹ ∘ α' ∘ β ∘ δ⁻¹ ∘ α'' ∘ δ)`.

```lean
theorem composition_assoc :
    compFstPair F p ⋙ composition F p = idCompPair F p ⋙ composition F p
```

**`AlgebraicGeometry.Stack.relativeInertiaPairOverStack`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupAxioms.lean, line 473](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupAxioms.lean#L473). The attribute's comment: “the twofold product of the relative inertia in the 2-category of morphisms to the source representable by algebraic spaces”.

> `I_{𝒳/𝒴} ×_𝒳 I_{𝒳/𝒴}` as an object of `Spaces/𝒳`: the 2-fibre product of the projection
> with itself, with structure 1-morphism to `𝒳` the first projection followed by `π`.

```lean
noncomputable def relativeInertiaPairOverStack (f : 𝒳 ⟶ 𝒴) : SpacesOverStack B S hS 𝒳
```

**`AlgebraicGeometry.Stack.relativeInertiaCompositionHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupAxioms.lean, line 497](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupAxioms.lean#L497). The attribute's comment: “the composition law as a 1-morphism of the 2-category of morphisms to the source representable by algebraic spaces”.

> The composition law as a 1-morphism of `Spaces/𝒳`: the functor
> `c : I_{𝒳/𝒴} ×_𝒳 I_{𝒳/𝒴} ⟶ I_{𝒳/𝒴}`, `((x, α), (x', α'), β) ↦ (x, α ∘ β⁻¹ ∘ α' ∘ β)`, with
> the identity as comparison 2-morphism.

```lean
noncomputable def relativeInertiaCompositionHom (f : 𝒳 ⟶ 𝒴) :
    relativeInertiaPairOverStack B S hS f ⟶ relativeInertiaOverStack B S hS f
```

**`AlgebraicGeometry.Stack.relativeInertiaInverseHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupAxioms.lean, line 508](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupAxioms.lean#L508). The attribute's comment: “the inverse as a 1-morphism of the 2-category of morphisms to the source representable by algebraic spaces”.

> The inverse as a 1-morphism of `Spaces/𝒳`: the functor `i : I_{𝒳/𝒴} ⟶ I_{𝒳/𝒴}`,
> `(x, α) ↦ (x, α⁻¹)`, with the identity as comparison 2-morphism.

```lean
noncomputable def relativeInertiaInverseHom (f : 𝒳 ⟶ 𝒴) :
    relativeInertiaOverStack B S hS f ⟶ relativeInertiaOverStack B S hS f
```

**`AlgebraicGeometry.Stack.relativeInertiaNeutralHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupAxioms.lean, line 517](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupAxioms.lean#L517). The attribute's comment: “the neutral element as a 1-morphism of algebraic stacks”.

> The neutral element as a 1-morphism of algebraic stacks: `e : 𝒳 ⟶ I_{𝒳/𝒴}`,
> `x ↦ (x, id_x)`.

```lean
noncomputable def relativeInertiaNeutralHom (f : 𝒳 ⟶ 𝒴) :
    𝒳 ⟶ (relativeInertiaOverStack B S hS f).source
```

**`AlgebraicGeometry.Stack.relativeInertiaNeutralHom_comp_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupAxioms.lean, line 525](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupAxioms.lean#L525). The attribute's comment: “the neutral element is a section of the projection”.

> The neutral element is a section of the projection: `e ≫ π = 𝟙 𝒳`, an equality of
> 1-morphisms of algebraic stacks.

```lean
theorem relativeInertiaNeutralHom_comp_map (f : 𝒳 ⟶ 𝒴) :
    relativeInertiaNeutralHom B S hS f ≫ (relativeInertiaOverStack B S hS f).map = 𝟙 𝒳
```

**`CategoryTheory.RelativeInertia.composition`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupLaw.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupLaw.lean#L108). The attribute's comment: “the composition law”.

> **Stacks 050R, the composition law of the relative inertia.** On the 2-fibre product
> `I_{S/S'} ×_S I_{S/S'}`, whose objects are the triples `((x, α), (x', α'), β)` with
> `β : x ≅ x'` a vertical isomorphism, it is the functor
> `((x, α), (x', α'), β) ↦ (x, α ∘ β⁻¹ ∘ α' ∘ β)`, acting on morphisms by their first component.

```lean
def composition (F : S ⥤ S') (p : S ⥤ C) :
    TwoFibreProductOver (RelativeInertia.π F ⋙ p) (RelativeInertia.π F ⋙ p) p
        (RelativeInertia.π F) (RelativeInertia.π F) ⥤ RelativeInertia F
```

**`CategoryTheory.RelativeInertia.composition_comp_π`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupLaw.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupLaw.lean#L147). The attribute's comment: “the composition law is a morphism over the source”.

> **The composition law is a morphism over the source**: followed by the projection to `S` it
> is the first projection of the 2-fibre product followed by that projection.

```lean
theorem composition_comp_π (F : S ⥤ S') (p : S ⥤ C) :
    composition F p ⋙ RelativeInertia.π F =
      TwoFibreProductOver.fst (RelativeInertia.π F ⋙ p) (RelativeInertia.π F ⋙ p) p
        (RelativeInertia.π F) (RelativeInertia.π F) ⋙ RelativeInertia.π F
```

**`AlgebraicGeometry.Stack.relativeInertiaOverStack`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupLaw.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupLaw.lean#L169). The attribute's comment: “the relative inertia as an object of the 2-category of morphisms to the source representable by algebraic spaces”.

> **The relative inertia as an object of `Spaces/𝒳`.** For a 1-morphism `f : 𝒳 ⟶ 𝒴` of
> algebraic stacks, the relative inertia `I_{𝒳/𝒴}` is an algebraic stack and its projection to
> `𝒳` is representable by algebraic spaces, so the pair is an object of the 2-category of
> Stacks 04ZQ. This is the ambient object of which Stacks 050R asserts that it is a group
> object.

```lean
noncomputable def relativeInertiaOverStack
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) : SpacesOverStack B S hS 𝒳
```

**`AlgebraicGeometry.Stack.relativeInertiaGrpObj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupObject.lean, line 806](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupObject.lean#L806).

> **Stacks 050R.** For a 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks, the relative inertia
> `I_{𝒳/𝒴}` is a *group object* of the category of 1-morphisms to `𝒳` representable by algebraic
> spaces (Stacks 04ZQ): its multiplication is the composition law
> `c : I_{𝒳/𝒴} ×_𝒳 I_{𝒳/𝒴} ⟶ I_{𝒳/𝒴}`, `((x, α), (x', α'), β) ↦ (x, α ∘ β⁻¹ ∘ α' ∘ β)`, its unit
> is the neutral element `e : 𝒳 ⟶ I_{𝒳/𝒴}`, `x ↦ (x, id_x)`, and its inverse is
> `i : (x, α) ↦ (x, α⁻¹)`.

```lean
noncomputable def relativeInertiaGrpObj (f : 𝒳 ⟶ 𝒴) : GrpObj (IsoClassCategory.mk
  (relativeInertiaOverStack B S hS f))
```

**`AlgebraicGeometry.Stack.relativeInertiaGrpObj_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupObject.lean, line 853](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupObject.lean#L853). The attribute's comment: “the multiplication of the group object is the composition law”.

> **Stacks 050R.** The multiplication of the group object is the composition law `c`.

```lean
theorem relativeInertiaGrpObj_mul (f : 𝒳 ⟶ 𝒴) :
    letI := relativeInertiaGrpObj B S hS f
    MonObj.mul (X := IsoClassCategory.mk (relativeInertiaOverStack B S hS f)) =
      IsoClassCategory.homMk (C := SpacesOverStack B S hS 𝒳) (relativeInertiaMulHom B S hS f)
```

**`AlgebraicGeometry.Stack.relativeInertiaGrpObj_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupObject.lean, line 860](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupObject.lean#L860). The attribute's comment: “the unit of the group object is the neutral element”.

> **Stacks 050R.** The unit of the group object is the neutral element `e`.

```lean
theorem relativeInertiaGrpObj_one (f : 𝒳 ⟶ 𝒴) :
    letI := relativeInertiaGrpObj B S hS f
    MonObj.one (X := IsoClassCategory.mk (relativeInertiaOverStack B S hS f)) =
      IsoClassCategory.homMk (C := SpacesOverStack B S hS 𝒳) (relativeInertiaOneHom B S hS f)
```

**`AlgebraicGeometry.Stack.relativeInertiaGrpObj_inv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupObject.lean, line 867](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupObject.lean#L867). The attribute's comment: “the inverse of the group object”.

> **Stacks 050R.** The inverse of the group object is `i`.

```lean
theorem relativeInertiaGrpObj_inv (f : 𝒳 ⟶ 𝒴) :
    GrpObj.inv (X := IsoClassCategory.mk (relativeInertiaOverStack B S hS f)) (self :=
      relativeInertiaGrpObj B S hS f) =
      IsoClassCategory.homMk (C := SpacesOverStack B S hS 𝒳) (relativeInertiaInvHom B S hS f)
```

Declarations registered for the tag:

- [`CategoryTheory.RelativeInertia.neutralSection`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/RelativeInertia.lean#L191), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupLaw.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaGroupLaw.lean#L154) (StacksFrontier): “the neutral element”.

## Tag 0CPJ, an equation

[Tag 0CPJ](https://stacks.math.columbia.edu/tag/0CPJ) in the Stacks Project.

**`AlgebraicGeometry.Stack.isomSpaceMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismSequence.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismSequence.lean#L177). The attribute's comment: “the map Isom\_𝒳(x, x) → Isom\_𝒴(y, y)”.

> The map `Isom_𝒳(x, y) ⟶ Isom_𝒴(f(x), f(y))` of sheaves on the big fppf site of `U` induced
> by a 1-morphism `f : 𝒳 ⟶ 𝒴`: it applies `f` to a local isomorphism and compares the chosen
> pullbacks of `x` and `y` with those of their images.

```lean
def isomSpaceMap (x y : 𝒳.val.p.Fiber U) :
    isomSpace B S hS 𝒳 U x y ⟶
      isomSpace B S hS 𝒴 U (imageFiberObj B S hS 𝒳 𝒴 F U x)
        (imageFiberObj B S hS 𝒳 𝒴 F U y)
```

**`AlgebraicGeometry.Stack.relativeIsomSubfunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismSequence.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismSequence.lean#L201). The attribute's comment: “the sheaf Isom\_\{𝒳/𝒴}(x, x)”.

> The relative automorphism sheaf `Isom_{𝒳/𝒴}(x, x)`, as a subsheaf of `Isom_𝒳(x, x)`: its
> sections over `V` are the local automorphisms `α` of `x` with `f(α) = id`.

```lean
def relativeIsomSubfunctor (x : 𝒳.val.p.Fiber U) :
    Subfunctor (isomSpace B S hS 𝒳 U x x)
```

**`AlgebraicGeometry.Stack.relativeIsomSpaceGrpObj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismSequence.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismSequence.lean#L222). The attribute's comment: “the group structure on Isom\_\{𝒳/𝒴}(x, x)”.

> The group structure on `Isom_{𝒳/𝒴}(x, x)`, restricted from that of `Isom_𝒳(x, x)`.

```lean
def relativeIsomSpaceGrpObj (x : 𝒳.val.p.Fiber U) :
    GrpObj (relativeIsomSpace B S hS 𝒳 𝒴 F U x)
```

**`AlgebraicGeometry.Stack.isMonHom_relativeIsomSpaceι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismSequence.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismSequence.lean#L284). The attribute's comment: “the first map is a homomorphism of sheaves of groups”.

> The inclusion `Isom_{𝒳/𝒴}(x, x) ⟶ Isom_𝒳(x, x)` is a homomorphism of sheaves of groups.

```lean
theorem isMonHom_relativeIsomSpaceι (x : 𝒳.val.p.Fiber U) :
    letI : 𝒳.val.p.IsPreFibered := 𝒳.isFiberedInGroupoids.isFibered.toIsPreFibered
    letI : GrpObj (isomSpace B S hS 𝒳 U x x) := isomSpaceGrpObj B S hS 𝒳 U x
    letI : GrpObj (relativeIsomSpace B S hS 𝒳 𝒴 F U x) :=
      relativeIsomSpaceGrpObj B S hS 𝒳 𝒴 F U x
    IsMonHom (relativeIsomSubfunctor B S hS 𝒳 𝒴 F U x).ι
```

**`AlgebraicGeometry.Stack.isMonHom_isomSpaceMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismSequence.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismSequence.lean#L298). The attribute's comment: “the second map is a homomorphism of sheaves of groups”.

> The map `Isom_𝒳(x, x) ⟶ Isom_𝒴(f(x), f(x))` is a homomorphism of sheaves of groups.

```lean
theorem isMonHom_isomSpaceMap (x : 𝒳.val.p.Fiber U) :
    letI : 𝒳.val.p.IsPreFibered := 𝒳.isFiberedInGroupoids.isFibered.toIsPreFibered
    letI : 𝒴.val.p.IsPreFibered := 𝒴.isFiberedInGroupoids.isFibered.toIsPreFibered
    letI : GrpObj (isomSpace B S hS 𝒳 U x x) := isomSpaceGrpObj B S hS 𝒳 U x
    letI : GrpObj (isomSpace B S hS 𝒴 U (imageFiberObj B S hS 𝒳 𝒴 F U x)
        (imageFiberObj B S hS 𝒳 𝒴 F U x)) :=
      isomSpaceGrpObj B S hS 𝒴 U (imageFiberObj B S hS 𝒳 𝒴 F U x)
    IsMonHom (isomSpaceMap B S hS 𝒳 𝒴 F U x x)
```

**`AlgebraicGeometry.Stack.relativeIsomSpaceι_app_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismSequence.lean, line 323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismSequence.lean#L323). The attribute's comment: “injectivity of the first map”.

> The inclusion `Isom_{𝒳/𝒴}(x, x) ⟶ Isom_𝒳(x, x)` is injective on sections.

```lean
theorem relativeIsomSpaceι_app_injective (x : 𝒳.val.p.Fiber U)
    (V : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ)
    (a b : (relativeIsomSpace B S hS 𝒳 𝒴 F U x).obj V)
    (h : (relativeIsomSubfunctor B S hS 𝒳 𝒴 F U x).ι.app V a =
      (relativeIsomSubfunctor B S hS 𝒳 𝒴 F U x).ι.app V b) : a = b
```

**`AlgebraicGeometry.Stack.relativeIsom_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismSequence.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismSequence.lean#L334). The attribute's comment: “exactness at Isom\_𝒳(x, x)”.

> The sequence `0 → Isom_{𝒳/𝒴}(x, x) → Isom_𝒳(x, x) → Isom_𝒴(y, y)` is exact at the middle
> term: a local automorphism of `x` has identity image in `Isom_𝒴(y, y)` exactly when it comes from
> a relative automorphism of `x`.

```lean
theorem relativeIsom_exact (x : 𝒳.val.p.Fiber U)
    (V : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ)
    (m : (isomSpace B S hS 𝒳 U x x).obj V) :
    ((isomSpaceMap B S hS 𝒳 𝒴 F U x x).app V m).1 = 𝟙 _ ↔
      ∃ n : (relativeIsomSpace B S hS 𝒳 𝒴 F U x).obj V,
        (relativeIsomSubfunctor B S hS 𝒳 𝒴 F U x).ι.app V n = m
```

## Tag 06PP, a definition

[Tag 06PP](https://stacks.math.columbia.edu/tag/06PP) in the Stacks Project.

**`AlgebraicGeometry.Stack.relativeAutomorphismSpaceOverSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismSpaceOverAlgebraicSpace.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismSpaceOverAlgebraicSpace.lean#L181). The attribute's comment: “part (1): the relative sheaf of automorphisms, Z ×\_\{x, X} I\_\{X/Y}”.

> **Stacks 06PP, part (1): the relative sheaf of automorphisms of `x`.** For a 1-morphism
> `f : 𝒳 ⟶ 𝒴` of algebraic stacks and an algebraic-space-valued point `x : Z ⟶ 𝒳`, the 2-fibre
> product
>
> ```text
> Isom_{𝒳/𝒴}(x, x) = Z ×_{x, 𝒳} ℐ_{𝒳/𝒴}
> ```
>
> of `x` with the forgetful 1-morphism of the relative inertia, read in the 2-category of
> categories fibred in groupoids over the big fppf site of `S`. Its objects over a scheme `W` are
> the triples of a point `z` of `Z` over `W`, an object `(a, α)` of the relative inertia over `W` —
> that is, an object `a` of `𝒳` over `W` together with an automorphism `α` of `a` killed by `f` —
> and a vertical isomorphism `x(z) ≅ a`; so a section over `W` is an automorphism of `x(z)` killed
> by `f`, which is what the source calls an automorphism of `x` over `W` relative to `𝒴`.

```lean
noncomputable def relativeAutomorphismSpaceOverSpace (f : 𝒳 ⟶ 𝒴)
    (x : algebraicSpaceStack.{u, w} B S hS Z hZ ⟶ 𝒳) :
    CatFiberedInGroupoids (BigFppfOver B S hS)
```

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpace_relativeAutomorphismSpaceOverSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismSpaceOverAlgebraicSpace.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismSpaceOverAlgebraicSpace.lean#L208). The attribute's comment: “part (1): Isom\_\{X/Y}(x, x) is an algebraic space”.

> **Stacks 06PP, part (1): `Isom_{𝒳/𝒴}(x, x)` is an algebraic space.** The relative sheaf of
> automorphisms of an algebraic-space-valued point `x : Z ⟶ 𝒳` of an algebraic stack is
> represented by an algebraic space over `S`.
>
> Stacks 050Q makes the forgetful 1-morphism `ℐ_{𝒳/𝒴} ⟶ 𝒳` of the relative inertia representable
> by algebraic spaces — only the representability of the two diagonals, the second clause of
> `AlgebraicGeometry.Stack.IsAlgebraicStack`, is used for that — and `Z` represents the stack of
> `Z`, so Stacks 0300 applies to the cospan `(x, ℐ_{𝒳/𝒴} ⟶ 𝒳)`.

```lean
theorem isRepresentableByAlgebraicSpace_relativeAutomorphismSpaceOverSpace (f : 𝒳 ⟶ 𝒴)
    (x : algebraicSpaceStack.{u, w} B S hS Z hZ ⟶ 𝒳) :
    IsRepresentableByAlgebraicSpace B S hS
      (relativeAutomorphismSpaceOverSpace B S hS Z hZ f x)
```

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_relativeAutomorphismSpaceOverSpaceProj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismSpaceOverAlgebraicSpace.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismSpaceOverAlgebraicSpace.lean#L228). The attribute's comment: “part (1): Isom\_\{X/Y}(x, x) is an algebraic space over Z”.

> **Stacks 06PP, part (1): `Isom_{𝒳/𝒴}(x, x)` is an algebraic space over `Z`.** The projection
> of the relative sheaf of automorphisms of `x` to the stack of `Z` is representable by algebraic
> spaces, so — together with
> `AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpace_relativeAutomorphismSpaceOverSpace`, which
> makes its source an algebraic space — it is a morphism of algebraic spaces with target `Z`.
>
> This is Stacks 0302 for the base change of the representable 1-morphism `ℐ_{𝒳/𝒴} ⟶ 𝒳` of
> Stacks 050Q along `x`.

```lean
theorem isRepresentableByAlgebraicSpaces_relativeAutomorphismSpaceOverSpaceProj (f : 𝒳 ⟶ 𝒴)
    (x : algebraicSpaceStack.{u, w} B S hS Z hZ ⟶ 𝒳) :
    IsRepresentableByAlgebraicSpaces B S hS
      (relativeAutomorphismSpaceOverSpaceProj B S hS Z hZ f x)
```

**`AlgebraicGeometry.Stack.automorphismSpaceOverSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismSpaceOverAlgebraicSpace.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismSpaceOverAlgebraicSpace.lean#L251). The attribute's comment: “the sheaf of automorphisms of x, Z ×\_\{x, X} I\_X”.

> **Stacks 06PP: the sheaf of automorphisms of `x`.** For an algebraic-space-valued point
> `x : Z ⟶ 𝒳` of an algebraic stack, the 2-fibre product
>
> ```text
> Isom_𝒳(x, x) = Z ×_{x, 𝒳} ℐ_𝒳
> ```
>
> of `x` with the forgetful 1-morphism of the inertia. This is the object the last paragraph of
> Stacks 06PP writes `Isom_𝒳(x, x)`: part (1) of that definition when `𝒴` is an algebraic space,
> in which case the relative inertia of `𝒳` over `𝒴` is the absolute inertia of `𝒳`.

```lean
noncomputable def automorphismSpaceOverSpace
    (x : algebraicSpaceStack.{u, w} B S hS Z hZ ⟶ 𝒳) :
    CatFiberedInGroupoids (BigFppfOver B S hS)
```

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpace_automorphismSpaceOverSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismSpaceOverAlgebraicSpace.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismSpaceOverAlgebraicSpace.lean#L276). The attribute's comment: “Isom\_X(x, x) is an algebraic space”.

> **Stacks 06PP: `Isom_𝒳(x, x)` is an algebraic space.** The sheaf of automorphisms of an
> algebraic-space-valued point of an algebraic stack is represented by an algebraic space over
> `S`: Stacks 050Q for the absolute inertia projection, together with Stacks 0300.

```lean
theorem isRepresentableByAlgebraicSpace_automorphismSpaceOverSpace
    (x : algebraicSpaceStack.{u, w} B S hS Z hZ ⟶ 𝒳) :
    IsRepresentableByAlgebraicSpace B S hS (automorphismSpaceOverSpace B S hS Z hZ x)
```

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_automorphismSpaceOverSpaceProj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismSpaceOverAlgebraicSpace.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismSpaceOverAlgebraicSpace.lean#L289). The attribute's comment: “Isom\_X(x, x) is an algebraic space over Z”.

> **Stacks 06PP: `Isom_𝒳(x, x)` is an algebraic space over `Z`.** The projection of the sheaf
> of automorphisms of `x` to the stack of `Z` is representable by algebraic spaces — Stacks 0302 for
> the base change of the representable 1-morphism `ℐ_𝒳 ⟶ 𝒳` of Stacks 050Q along `x`.

```lean
theorem isRepresentableByAlgebraicSpaces_automorphismSpaceOverSpaceProj
    (x : algebraicSpaceStack.{u, w} B S hS Z hZ ⟶ 𝒳) :
    IsRepresentableByAlgebraicSpaces B S hS
      (automorphismSpaceOverSpaceProj B S hS Z hZ x)
```

**`AlgebraicGeometry.Stack.isomorphismSpaceOverSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismSpaceOverAlgebraicSpace.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismSpaceOverAlgebraicSpace.lean#L331). The attribute's comment: “the sheaf of isomorphisms from x₁ to x₂, as the fibre of the diagonal”.

> **Stacks 06PP: the sheaf of isomorphisms from `x₁` to `x₂`.** For two
> algebraic-space-valued points `x₁, x₂ : Z ⟶ 𝒳` of an algebraic stack, the 2-fibre product
>
> ```text
> Isom_𝒳(x₁, x₂) = Z ×_{(x₁, x₂), 𝒳 × 𝒳, Δ} 𝒳
> ```
>
> of the pair `(x₁, x₂)` with the diagonal of `𝒳`. Its objects over a scheme `W` are the
> quadruples of a point `z` of `Z` over `W`, an object `a` of `𝒳` over `W` and two vertical
> isomorphisms `x₁(z) ≅ a`, `x₂(z) ≅ a`, so a section over `W` is an isomorphism
> `x₁(z) ≅ x₂(z)` of the fibre of `𝒳` over `W` — which is what the last paragraph of Stacks 06PP
> calls the *sheaf of isomorphisms from `x₁` to `x₂`*.
>
> This is the presentation of `Isom` that the diagonal conditions (1) and (2) of Stacks 045G are
> stated with, and it is the one
> `CategoryTheory.TwoFibreProductOver.DiagonalFibre.equivalenceOver` identifies with the presheaf
> of vertical morphisms from `x₁` to `x₂`. The equivalent iterated form the source writes,
> `(Z ×_{x₁, 𝒳, x₂} Z) ×_{Z × Z, Δ_Z} Z`, is `AlgebraicGeometry.Stack.absoluteIsomorphismCategory`
> cut down by `AlgebraicGeometry.Stack.absoluteIsomorphismDiagonalSubcategory`; this file does not
> prove the comparison of the two forms.

```lean
noncomputable def isomorphismSpaceOverSpace
    (x₁ x₂ : algebraicSpaceStack.{u, w} B S hS Z hZ ⟶ 𝒳) :
    CatFiberedInGroupoids (BigFppfOver B S hS)
```

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpace_isomorphismSpaceOverSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismSpaceOverAlgebraicSpace.lean, line 356](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismSpaceOverAlgebraicSpace.lean#L356). The attribute's comment: “Isom\_X(x₁, x₂) is an algebraic space”.

> **Stacks 06PP: `Isom_𝒳(x₁, x₂)` is an algebraic space.** The sheaf of isomorphisms from one
> algebraic-space-valued point of an algebraic stack to another is represented by an algebraic
> space over `S`.
>
> It is the base change of the diagonal of `𝒳` along the pair `(x₁, x₂)`, the diagonal is
> representable by algebraic spaces because `𝒳` is an algebraic stack, and `Z` represents the stack
> of `Z`; so this is Stacks 0300.

```lean
theorem isRepresentableByAlgebraicSpace_isomorphismSpaceOverSpace
    (x₁ x₂ : algebraicSpaceStack.{u, w} B S hS Z hZ ⟶ 𝒳) :
    IsRepresentableByAlgebraicSpace B S hS (isomorphismSpaceOverSpace B S hS Z hZ x₁ x₂)
```

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_isomorphismSpaceOverSpaceProj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismSpaceOverAlgebraicSpace.lean, line 367](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismSpaceOverAlgebraicSpace.lean#L367). The attribute's comment: “Isom\_X(x₁, x₂) is an algebraic space over Z”.

> **Stacks 06PP: `Isom_𝒳(x₁, x₂)` is an algebraic space over `Z`.** Its projection to the stack
> of `Z` is representable by algebraic spaces — Stacks 0302 for the base change of the diagonal of
> `𝒳` along the pair `(x₁, x₂)`.

```lean
theorem isRepresentableByAlgebraicSpaces_isomorphismSpaceOverSpaceProj
    (x₁ x₂ : algebraicSpaceStack.{u, w} B S hS Z hZ ⟶ 𝒳) :
    IsRepresentableByAlgebraicSpaces B S hS
      (isomorphismSpaceOverSpaceProj B S hS Z hZ x₁ x₂)
```

**`AlgebraicGeometry.Stack.relativeIsomorphismSpaceOverSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismSpaceOverAlgebraicSpace.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismSpaceOverAlgebraicSpace.lean#L419). The attribute's comment: “part (2): the relative sheaf of isomorphisms, as the fibre of the relative diagonal”.

> **Stacks 06PP, part (2): the relative sheaf of isomorphisms from `x₁` to `x₂`.** For a
> 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks, two algebraic-space-valued points
> `x₁, x₂ : Z ⟶ 𝒳` and a 2-morphism `α : x₁ ≫ f ⟶ x₂ ≫ f`, the 2-fibre product
>
> ```text
> Isom^α_{𝒳/𝒴}(x₁, x₂) = Z ×_{(x₁, x₂, α), 𝒳 ×_𝒴 𝒳, Δ_f} 𝒳
> ```
>
> of the twisted point of `AlgebraicGeometry.Stack.relativeIsomorphismTwistedPoint` with the
> relative diagonal of `f`. Its sections over a scheme `W` are the isomorphisms
> `x₁(z) ≅ x₂(z)` of the fibre of `𝒳` over `W` whose image under `f` is the component of `α` at
> `z`, which is what the source calls the *relative sheaf of isomorphisms from `x₁` to `x₂`*.
>
> The source writes the same object as the iterated fibre product
> `(Z ×_{x₁, 𝒳, x₂} Z) ×_{Z ×_{y₁, 𝒴, y₂} Z, Δ^α} Z`; that is the fibre of `Δ^α` and this is the
> fibre of `Δ_f` along the twisted point, which is the form the representability of the relative
> diagonal is stated for. This file does not prove the comparison of the two forms, nor the
> comparison with the explicit sub-presheaf
> `AlgebraicGeometry.Stack.relativeIsomSpaceOverSpace`.

```lean
noncomputable def relativeIsomorphismSpaceOverSpace (f : 𝒳 ⟶ 𝒴)
    (x₁ x₂ : algebraicSpaceStack.{u, w} B S hS Z hZ ⟶ 𝒳) (α : x₁ ≫ f ⟶ x₂ ≫ f) :
    CatFiberedInGroupoids (BigFppfOver B S hS)
```

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpace_relativeIsomorphismSpaceOverSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismSpaceOverAlgebraicSpace.lean, line 459](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismSpaceOverAlgebraicSpace.lean#L459). The attribute's comment: “part (2): Isom^α\_\{X/Y}(x₁, x₂) is an algebraic space”.

> **Stacks 06PP, part (2): `Isom^α_{𝒳/𝒴}(x₁, x₂)` is an algebraic space.** The relative sheaf
> of isomorphisms from `x₁` to `x₂` lifting `α` is represented by an algebraic space over `S`.
>
> It is the base change of the relative diagonal `Δ_f : 𝒳 ⟶ 𝒳 ×_𝒴 𝒳` along the twisted point; the
> relative diagonal is representable by algebraic spaces as soon as the diagonals of `𝒳` and `𝒴`
> are (`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_relativeDiagonal`), which they are
> because `𝒳` and `𝒴` are algebraic stacks, and `Z` represents the stack of `Z`; so this is
> Stacks 0300.

```lean
theorem isRepresentableByAlgebraicSpace_relativeIsomorphismSpaceOverSpace (f : 𝒳 ⟶ 𝒴)
    (x₁ x₂ : algebraicSpaceStack.{u, w} B S hS Z hZ ⟶ 𝒳) (α : x₁ ≫ f ⟶ x₂ ≫ f) :
    IsRepresentableByAlgebraicSpace B S hS
      (relativeIsomorphismSpaceOverSpace B S hS Z hZ f x₁ x₂ α)
```

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_relativeIsomorphismSpaceOverSpaceProj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismSpaceOverAlgebraicSpace.lean, line 471](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismSpaceOverAlgebraicSpace.lean#L471). The attribute's comment: “part (2): Isom^α\_\{X/Y}(x₁, x₂) is an algebraic space over Z”.

> **Stacks 06PP, part (2): `Isom^α_{𝒳/𝒴}(x₁, x₂)` is an algebraic space over `Z`.** Its
> projection to the stack of `Z` is representable by algebraic spaces — Stacks 0302 for the base
> change of the relative diagonal of `f` along the twisted point.

```lean
theorem isRepresentableByAlgebraicSpaces_relativeIsomorphismSpaceOverSpaceProj (f : 𝒳 ⟶ 𝒴)
    (x₁ x₂ : algebraicSpaceStack.{u, w} B S hS Z hZ ⟶ 𝒳) (α : x₁ ≫ f ⟶ x₂ ≫ f) :
    IsRepresentableByAlgebraicSpaces B S hS
      (relativeIsomorphismSpaceOverSpaceProj B S hS Z hZ f x₁ x₂ α)
```

**`AlgebraicGeometry.Stack.isomSpaceOverSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/IsomSpaceOverAlgebraicSpace.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/IsomSpaceOverAlgebraicSpace.lean#L322). The attribute's comment: “the sheaf of isomorphisms from one algebraic-space-valued point to another”.

> **Stacks 06PP.** The presheaf `Isom_𝒳(x₁, x₂)` of isomorphisms of two
> algebraic-space-valued points of an algebraic stack: its sections over `W` are the pairs
> consisting of a point `z` of `Z` over `W` and an isomorphism `x₁(z) ≅ x₂(z)` in the fibre category
> of `𝒳` over `W`, and its restriction maps are `AlgebraicGeometry.Stack.pointRestrict`.
>
> This is the object the last paragraph of Stacks 06PP calls `Isom_𝒳(x₁, x₂)`, the *sheaf of
> isomorphisms from `x₁` to `x₂`*. That it is represented by an algebraic space over `Z` is the
> other half of that definition and is not asserted here; neither is its part (1), the group law
> on the relative sheaf of automorphisms.

```lean
noncomputable def isomSpaceOverSpace (x₁ x₂ : algebraicSpaceStack.{u, w} B S hS Z hZ ⟶ 𝒳) :
    (BigFppfOver B S hS)ᵒᵖ ⥤ Type u
```

**`AlgebraicGeometry.Stack.relativeIsomSpaceOverSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/IsomSpaceOverAlgebraicSpace.lean, line 530](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/IsomSpaceOverAlgebraicSpace.lean#L530). The attribute's comment: “part (2): the sheaf of isomorphisms lifting a 2-morphism”.

> **Stacks 06PP, part (2).** The presheaf `Isom^α_{𝒳/𝒴}(x₁, x₂)` of isomorphisms of two
> algebraic-space-valued points of `𝒳` lifting a given 2-morphism `α : x₁ ≫ f ⟶ x₂ ≫ f` of the
> target: it is the sub-presheaf of `AlgebraicGeometry.Stack.isomSpaceOverSpace` cut out by the
> condition that the image of the isomorphism under `f` be the prescribed component of `α`.
>
> That it is represented by an algebraic space over `Z` is the remaining half of Stacks 06PP part
> (2) and is not asserted here.

```lean
noncomputable def relativeIsomSpaceOverSpace (f : 𝒳 ⟶ 𝒴)
    (x₁ x₂ : algebraicSpaceStack.{u, w} B S hS Z hZ ⟶ 𝒳) (α : x₁ ≫ f ⟶ x₂ ≫ f) :
    (BigFppfOver B S hS)ᵒᵖ ⥤ Type u
```

**`AlgebraicGeometry.Stack.isAlgebraicSpace_isomSpaceOverSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/IsomSpaceOverAlgebraicSpaceRepresentability.lean, line 542](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/IsomSpaceOverAlgebraicSpaceRepresentability.lean#L542). The attribute's comment: “the sheaf of isomorphisms is an algebraic space over Z”.

> **Stacks 06PP: the sheaf of isomorphisms of two algebraic-space-valued points of an
> algebraic stack is an algebraic space over `Z`.** The structure morphism
> `AlgebraicGeometry.Stack.isomSpaceOverSpaceProj` to `Z` is representable by algebraic spaces,
> because its fibre over every scheme-valued point of `Z` is the sheaf of vertical morphisms
> between two scheme-valued points of `𝒳`, an algebraic space by condition (2) of Stacks 045G;
> `Z` is an algebraic space, so Stacks 02YS applies.
>
> This is the representability half of Stacks 06PP, which
> `AlgebraicGeometry.Stack.isomSpaceOverSpace` constructs the sheaf of.

```lean
theorem isAlgebraicSpace_isomSpaceOverSpace
    (x₁ x₂ : algebraicSpaceStack.{u, w} B S hS Z hZ ⟶ 𝒳) :
    IsAlgebraicSpace B S hS (isomSpaceOverSpace B S hS Z hZ x₁ x₂)
```

**`AlgebraicGeometry.Stack.isAlgebraicSpace_relativeIsomSpaceOverSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/IsomSpaceOverAlgebraicSpaceRepresentability.lean, line 557](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/IsomSpaceOverAlgebraicSpaceRepresentability.lean#L557). The attribute's comment: “part (2): the sheaf of isomorphisms lifting a 2-morphism is an algebraic space”.

> **Stacks 06PP part (2): the sheaf of isomorphisms lifting a 2-morphism is an algebraic space
> over `Z`.** It is the fibre product of `Isom_𝒳(x₁, x₂)` and `Z` over `Isom_𝒴(f x₁, f x₂)` by
> `AlgebraicGeometry.Stack.isPullback_relativeIsomSpaceOverSpace`, and all three of those are
> algebraic spaces over `S`, so Stacks 04T9 applies.

```lean
theorem isAlgebraicSpace_relativeIsomSpaceOverSpace (f : 𝒳 ⟶ 𝒴)
    (x₁ x₂ : algebraicSpaceStack.{u, w} B S hS Z hZ ⟶ 𝒳) (α : x₁ ≫ f ⟶ x₂ ≫ f) :
    IsAlgebraicSpace B S hS (relativeIsomSpaceOverSpace B S hS Z hZ f x₁ x₂ α)
```

**`AlgebraicGeometry.Stack.nonempty_equivalenceOver_isomorphismSpaceOverSpaceProj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/IsomSpaceRenderingComparison.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/IsomSpaceRenderingComparison.lean#L126). The attribute's comment: “the sheaf of isomorphisms from x₁ to x₂: the 2-fibre product is that sheaf”.

> **Stacks 06PP: `Isom_𝒳(x₁, x₂)` is the sheaf of isomorphisms from `x₁` to `x₂`.** The
> 2-fibre product `Z ×_{(x₁, x₂), 𝒳 × 𝒳, Δ} 𝒳` of
> `AlgebraicGeometry.Stack.isomorphismSpaceOverSpace` is equivalent, as a category over `Z`, to
> the category of elements of the presheaf on the category of elements of `Z` whose sections over a
> point `a` are the vertical morphisms `x₁(a) ⟶ x₂(a)` of `𝒳`. Those are exactly the isomorphisms
> `x₁(a) ≅ x₂(a)` of the fibre of `𝒳`, the fibres of an algebraic stack being groupoids
> (Stacks 003V), so this is the statement that the 2-fibre product the last paragraph of
> Stacks 06PP writes `Isom_𝒳(x₁, x₂)` is the *sheaf of isomorphisms from `x₁` to `x₂`*.
>
> This is `CategoryTheory.TwoFibreProductOver.DiagonalFibre.equivalenceOver` read at the pair
> `(x₁, x₂) = AlgebraicGeometry.Stack.isomorphismPairPoint`.

```lean
theorem nonempty_equivalenceOver_isomorphismSpaceOverSpaceProj
    (x₁ x₂ : algebraicSpaceStack.{u, w} B S hS Z hZ ⟶ 𝒳) :
    Nonempty (StacksRepresentableCFG.EquivalenceOver
      (isomorphismSpaceOverSpaceProj B S hS Z hZ x₁ x₂).toFunctor
      (PresheafOfCategories.discreteProjection
        (TwoFibreProductOver.DiagonalFibre.vertHomPresheaf 𝒳.val.isFiberedInGroupoids
          (isomorphismPairPoint B S hS Z hZ x₁ x₂).hom.w)))
```

**`AlgebraicGeometry.Stack.nonempty_equivalenceOver_relativeIsomorphismSpaceOverSpaceProj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/IsomSpaceRenderingComparison.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/IsomSpaceRenderingComparison.lean#L148). The attribute's comment: “part (2): the 2-fibre product is the sheaf of isomorphisms lifting α”.

> **Stacks 06PP, part (2): `Isom^α_{𝒳/𝒴}(x₁, x₂)` is the sheaf of isomorphisms lifting `α`.**
> The 2-fibre product `Z ×_{(x₁, x₂, α), 𝒳 ×_𝒴 𝒳, Δ_f} 𝒳` of
> `AlgebraicGeometry.Stack.relativeIsomorphismSpaceOverSpace` is equivalent, as a category over
> `Z`, to the category of elements of the presheaf on the category of elements of `Z` whose
> sections over a point `a` are the vertical morphisms `x₁(a) ⟶ x₂(a)` of `𝒳` whose image under
> `f` is the comparison isomorphism carried by the twisted point at `a`, that is the component
> `α_a`. So the object part (2) defines is the *relative sheaf of isomorphisms from `x₁` to `x₂`*
> that the source says it is.
>
> This is `CategoryTheory.TwoFibreProductOver.RelativeDiagonalFibre.equivalenceOver` —
> Stacks 04XT — read at the twisted point
> `AlgebraicGeometry.Stack.relativeIsomorphismTwistedPoint`.

```lean
theorem nonempty_equivalenceOver_relativeIsomorphismSpaceOverSpaceProj (f : 𝒳 ⟶ 𝒴)
    (x₁ x₂ : algebraicSpaceStack.{u, w} B S hS Z hZ ⟶ 𝒳) (α : x₁ ≫ f ⟶ x₂ ≫ f) :
    Nonempty (StacksRepresentableCFG.EquivalenceOver
      (relativeIsomorphismSpaceOverSpaceProj B S hS Z hZ f x₁ x₂ α).toFunctor
      (PresheafOfCategories.discreteProjection
        (TwoFibreProductOver.RelativeDiagonalFibre.relVertHomPresheaf
          𝒴.val.isFiberedInGroupoids 𝒳.val.isFiberedInGroupoids
          (relativeIsomorphismTwistedPoint B S hS Z hZ f x₁ x₂ α).w f.hom.hom.w)))
```

**`AlgebraicGeometry.Stack.isAlgebraicSpace_isomorphismTotalPresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/IsomTotalPresheafAlgebraic.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/IsomTotalPresheafAlgebraic.lean#L101). The attribute's comment: “Isom\_X(x₁, x₂) as a presheaf over Z on the big fppf site is an algebraic space”.

> **Stacks 06PP: the sheaf `Isom_𝒳(x₁, x₂)` on the big fppf site is an algebraic space over
> `Z`.** The presheaf whose sections over `W` are the pairs of a point `z` of `Z` over `W` and an
> isomorphism `x₁(z) ≅ x₂(z)` is an algebraic space over `S`, so together with its structure
> morphism to `Z` it is the algebraic space over `Z` that the last paragraph of Stacks 06PP
> asserts.

```lean
theorem isAlgebraicSpace_isomorphismTotalPresheaf
    (x₁ x₂ : algebraicSpaceStack.{u, w} B S hS Z hZ ⟶ 𝒳) :
    IsAlgebraicSpace B S hS (isomorphismTotalPresheaf B S hS Z hZ x₁ x₂)
```

**`AlgebraicGeometry.Stack.isAlgebraicSpace_relativeIsomorphismTotalPresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/IsomTotalPresheafAlgebraic.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/IsomTotalPresheafAlgebraic.lean#L137). The attribute's comment: “part (2): Isom^α\_\{X/Y}(x₁, x₂) as a presheaf over Z on the big fppf site is an algebraic space”.

> **Stacks 06PP, part (2): the sheaf `Isom^α_{𝒳/𝒴}(x₁, x₂)` on the big fppf site is an
> algebraic space over `Z`.** The presheaf whose sections over `W` are the pairs of a point `z` of
> `Z` over `W` and an isomorphism `x₁(z) ≅ x₂(z)` lifting the component `α_z` is an algebraic space
> over `S`, so together with its structure morphism to `Z` it is the algebraic space over `Z` that
> part (2) asserts.

```lean
theorem isAlgebraicSpace_relativeIsomorphismTotalPresheaf (f : 𝒳 ⟶ 𝒴)
    (x₁ x₂ : algebraicSpaceStack.{u, w} B S hS Z hZ ⟶ 𝒳) (α : x₁ ≫ f ⟶ x₂ ≫ f) :
    IsAlgebraicSpace B S hS (relativeIsomorphismTotalPresheaf B S hS Z hZ f x₁ x₂ α)
```

**`AlgebraicGeometry.Stack.relativeAutomorphismGroupAlgebraicSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismGroupAlgebraicSpace.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismGroupAlgebraicSpace.lean#L85). The attribute's comment: “part (1): Isom\_\{X/Y}(x, x) is a group algebraic space over Z, group law and algebraicity”.

> `Isom_{𝒳/𝒴}(x, x)` as a group algebraic space over `Z`: the presheaf on the big fppf site
> whose sections over `W` are the pairs of a point `z` of `Z` over `W` and an automorphism of `x(z)`
> killed by `f`, together with its structure morphism to `Z`, the group law given by composition of
> automorphisms, and the algebraicity of that presheaf.

```lean
noncomputable def relativeAutomorphismGroupAlgebraicSpace (f : 𝒳 ⟶ 𝒴)
    (x : algebraicSpaceStack.{u, w} B S hS Z hZ ⟶ 𝒳) :
    Space.GroupAlgebraicSpace B S hS Z hZ
```

**`AlgebraicGeometry.Stack.relativeAutomorphismGroupPresheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismGroupOverSpace.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismGroupOverSpace.lean#L247). The attribute's comment: “part (1): the group law on Isom\_\{X/Y}(x, x), as a presheaf of groups over Z”.

> The presheaf of groups on the category of elements of `Z` whose sections at a point `a` of
> `Z` are the vertical automorphisms of `x(a)` killed by `f`, with composition as the group law and
> restriction along a morphism of `Z` as the restriction map.

```lean
noncomputable def relativeAutomorphismGroupPresheaf :
    ((algebraicSpaceStack.{u, w} B S hS Z hZ).val.val.obj)ᵒᵖ ⥤ GrpCat.{u}
```

**`AlgebraicGeometry.Stack.relativeAutomorphismPresheafGrpObj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismGroupOverSpace.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismGroupOverSpace.lean#L294). The attribute's comment: “part (1): the group-object structure on Isom\_\{X/Y}(x, x) over Z”.

> The presheaf of relative automorphisms of `x`, read over the category of elements of `Z`, is a
> *group object* of the cartesian monoidal category of presheaves of sets on that category: its
> unit, multiplication and inverse are the identity automorphism, composition and the inverse
> automorphism, taken pointwise over the points of `Z`.

```lean
noncomputable def relativeAutomorphismPresheafGrpObj :
    GrpObj (relativeAutomorphismPresheaf B S hS Z hZ f x)
```

**`AlgebraicGeometry.Stack.relativeAutomorphismPresheafGrpObj_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismGroupOverSpace.lean, line 320](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismGroupOverSpace.lean#L320). The attribute's comment: “part (1): the multiplication of the group object is composition”.

> The multiplication of `AlgebraicGeometry.Stack.relativeAutomorphismPresheafGrpObj` is
> composition of relative automorphisms.

```lean
theorem relativeAutomorphismPresheafGrpObj_mul
    (a : ((algebraicSpaceStack.{u, w} B S hS Z hZ).val.val.obj)ᵒᵖ)
    (φ : (CategoryTheory.MonoidalCategoryStruct.tensorObj
      (relativeAutomorphismPresheaf B S hS Z hZ f x)
      (relativeAutomorphismPresheaf B S hS Z hZ f x)).obj a) :
    letI := relativeAutomorphismPresheafGrpObj B S hS Z hZ f x
    (MonObj.mul (X := relativeAutomorphismPresheaf B S hS Z hZ f x)).app a φ =
      (φ.1 * φ.2 : RelativeAutomorphism B S hS Z hZ f x a.unop)
```

**`AlgebraicGeometry.Stack.relativeAutomorphismPresheafGrpObj_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismGroupOverSpace.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismGroupOverSpace.lean#L332). The attribute's comment: “part (1): the unit of the group object is the identity automorphism”.

> The unit of `AlgebraicGeometry.Stack.relativeAutomorphismPresheafGrpObj` is the identity
> automorphism.

```lean
theorem relativeAutomorphismPresheafGrpObj_one
    (a : ((algebraicSpaceStack.{u, w} B S hS Z hZ).val.val.obj)ᵒᵖ)
    (t : (CategoryTheory.MonoidalCategoryStruct.tensorUnit
      (((algebraicSpaceStack.{u, w} B S hS Z hZ).val.val.obj)ᵒᵖ ⥤ Type u)).obj a) :
    letI := relativeAutomorphismPresheafGrpObj B S hS Z hZ f x
    (MonObj.one (X := relativeAutomorphismPresheaf B S hS Z hZ f x)).app a t =
      (1 : RelativeAutomorphism B S hS Z hZ f x a.unop)
```

**`AlgebraicGeometry.Stack.relativeAutomorphismPresheafGrpObj_inv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismGroupOverSpace.lean, line 343](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismGroupOverSpace.lean#L343). The attribute's comment: “part (1): the inverse of the group object is the inverse automorphism”.

> The inverse of `AlgebraicGeometry.Stack.relativeAutomorphismPresheafGrpObj` is the inverse
> automorphism.

```lean
theorem relativeAutomorphismPresheafGrpObj_inv
    (a : ((algebraicSpaceStack.{u, w} B S hS Z hZ).val.val.obj)ᵒᵖ)
    (φ : RelativeAutomorphism B S hS Z hZ f x a.unop) :
    (GrpObj.inv (X := relativeAutomorphismPresheaf B S hS Z hZ f x)
      (self := relativeAutomorphismPresheafGrpObj B S hS Z hZ f x)).app a φ = φ⁻¹
```

**`AlgebraicGeometry.Stack.RelativeAutomorphismSpace.nonempty_isEquivalenceOver_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismSpaceGroupLaw.lean, line 380](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismSpaceGroupLaw.lean#L380). The attribute's comment: “part (1): the group structure on Isom\_\{X/Y}(x, x) over Z”.

> **The group structure on `Isom_{𝒳/𝒴}(x, x)` over `Z`.** The comparison 1-morphism is an
> equivalence over `Z` from the category of elements of the presheaf of groups of relative
> automorphisms of `x` (`AlgebraicGeometry.Stack.relativeAutomorphismGroupPresheaf`) to
> `Isom_{𝒳/𝒴}(x, x) = Z ×_{x, 𝒳} ℐ_{𝒳/𝒴}`.

```lean
theorem nonempty_isEquivalenceOver_comparison :
    Nonempty (CategoryTheory.IsEquivalenceOver
      (PresheafOfCategories.discreteProjection (relativeAutomorphismPresheaf B S hS Z hZ f x))
      (relativeAutomorphismSpaceOverSpaceProj B S hS Z hZ f x).toFunctor
      (comparison B S hS Z hZ f x))
```

**`AlgebraicGeometry.Stack.RelativeAutomorphismSpace.nonempty_equivalenceOver_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismSpaceGroupLaw.lean, line 395](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismSpaceGroupLaw.lean#L395). The attribute's comment: “part (1): Isom\_\{X/Y}(x, x) is the presheaf of groups of relative automorphisms”.

> **`Isom_{𝒳/𝒴}(x, x)` is the presheaf of relative automorphisms, as a category over `Z`**:
> there is a `StacksRepresentableCFG.EquivalenceOver` from the projection of the category of
> elements of the presheaf of relative automorphisms of `x` to the projection
> `Isom_{𝒳/𝒴}(x, x) ⟶ Z`.

```lean
theorem nonempty_equivalenceOver_comparison :
    Nonempty (StacksRepresentableCFG.EquivalenceOver
      (PresheafOfCategories.discreteProjection (relativeAutomorphismPresheaf B S hS Z hZ f x))
      (relativeAutomorphismSpaceOverSpaceProj B S hS Z hZ f x).toFunctor)
```

**`AlgebraicGeometry.Stack.RelativeAutomorphismSpace.inertiaObj_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismSpaceGroupLaw.lean, line 429](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismSpaceGroupLaw.lean#L429). The attribute's comment: “part (1): the group law is the composition law of 050R pulled back along x”.

> **The multiplication of relative automorphisms is the composition law of the relative
> inertia.** The object of the relative inertia attached to the product `φ * ψ` of two
> relative automorphisms of `x` at a point of `Z` is the value at the corresponding object of
> `ℐ_{𝒳/𝒴} ×_𝒳 ℐ_{𝒳/𝒴}` of `CategoryTheory.RelativeInertia.composition`, the composition law
> `((x, α), (x', α'), β) ↦ (x, α ∘ β⁻¹ ∘ α' ∘ β)`.

```lean
theorem inertiaObj_mul {a : (algebraicSpaceStack.{u, w} B S hS Z hZ).val.val.obj}
    (φ ψ : RelativeAutomorphism B S hS Z hZ f x a) :
    inertiaObj B S hS Z hZ f x (φ * ψ) =
      (CategoryTheory.RelativeInertia.composition f.hom.hom.toFunctor 𝒳.val.val.p).obj
        (inertiaPair B S hS Z hZ f x φ ψ)
```

**`AlgebraicGeometry.Stack.RelativeAutomorphismSpace.inertiaObj_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismSpaceGroupLaw.lean, line 444](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismSpaceGroupLaw.lean#L444). The attribute's comment: “part (1): the unit is the neutral element of 050R pulled back along x”.

> **The unit of the group of relative automorphisms is the neutral section of the relative
> inertia.** The object of the relative inertia attached to the identity relative automorphism of
> `x` at a point `a` of `Z` is the value of `CategoryTheory.RelativeInertia.neutralSection`,
> `x ↦ (x, id_x)`, at `x(a)`.

```lean
theorem inertiaObj_one {a : (algebraicSpaceStack.{u, w} B S hS Z hZ).val.val.obj} :
    inertiaObj B S hS Z hZ f x (1 : RelativeAutomorphism B S hS Z hZ f x a) =
      (CategoryTheory.RelativeInertia.neutralSection f.hom.hom.toFunctor).obj
        (x.hom.hom.toFunctor.obj a)
```

**`AlgebraicGeometry.Stack.RelativeAutomorphismSpace.inertiaObj_inv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismSpaceGroupLaw.lean, line 457](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismSpaceGroupLaw.lean#L457). The attribute's comment: “part (1): the inverse is the inverse of 050R pulled back along x”.

> **The inverse of the group of relative automorphisms is the inverse of the relative
> inertia.** The object of the relative inertia attached to `φ⁻¹` is the value at the object
> attached to `φ` of `CategoryTheory.RelativeInertia.inverse`, `(x, α) ↦ (x, α⁻¹)`.

```lean
theorem inertiaObj_inv {a : (algebraicSpaceStack.{u, w} B S hS Z hZ).val.val.obj}
    (φ : RelativeAutomorphism B S hS Z hZ f x a) :
    inertiaObj B S hS Z hZ f x φ⁻¹ =
      (CategoryTheory.RelativeInertia.inverse f.hom.hom.toFunctor).obj
        (inertiaObj B S hS Z hZ f x φ)
```

**`AlgebraicGeometry.Stack.isAlgebraicSpace_relativeAutomorphismTotalPresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismTotalPresheaf.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeAutomorphismTotalPresheaf.lean#L112). The attribute's comment: “part (1): Isom\_\{X/Y}(x, x) as a presheaf over Z on the big fppf site is an algebraic space”.

> The presheaf `AlgebraicGeometry.Stack.relativeAutomorphismTotalPresheaf`, whose sections over
> `W` are the pairs of a point `z` of `Z` over `W` and an automorphism of `x(z)` killed by `f`, is
> an algebraic space over `S`.

```lean
theorem isAlgebraicSpace_relativeAutomorphismTotalPresheaf (f : 𝒳 ⟶ 𝒴)
    (x : algebraicSpaceStack.{u, w} B S hS Z hZ ⟶ 𝒳) :
    IsAlgebraicSpace B S hS (relativeAutomorphismTotalPresheaf B S hS Z hZ f x)
```

**`AlgebraicGeometry.Stack.exists_relativeIsomorphismDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeIsomorphismDiagram.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeIsomorphismDiagram.lean#L255). The attribute's comment: “part (2): functorial map and twisted diagonal”.

> For a 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks, two algebraic-space-valued points
> `x₁, x₂ : Z ⟶ 𝒳` and a 2-morphism `α : x₁ ≫ f ⟶ x₂ ≫ f` of the target, there are a 1-morphism `H`
> from the isomorphism category of `x₁`, `x₂` to that of `x₁ ≫ f`, `x₂ ≫ f` which keeps the two
> points of `Z` and applies `f` to the isomorphism between them, and a 1-morphism `Δ` from `Z` to the
> latter whose value at `z` is the pair `(z, z)` with comparison isomorphism `α_z`.
>
> The 2-fibre product of `H` along `Δ` is the category of isomorphisms `x₁ ≅ x₂` lifting `α`; that
> it is represented by an algebraic space over `Z` is the remaining half of part (2) and is not
> asserted here. The witnesses are
> `AlgebraicGeometry.Stack.absoluteIsomorphismImageBasedFunctor` and
> `AlgebraicGeometry.Stack.relativeIsomorphismTwistedDiagonalBasedFunctor`.

```lean
theorem exists_relativeIsomorphismDiagram
    (x₁ x₂ : algebraicSpaceStack.{u, w} B S hS Z hZ ⟶ 𝒳) (α : x₁ ≫ f ⟶ x₂ ≫ f) :
    let PX := absoluteIsomorphismCategory B S hS Z hZ 𝒳 x₁ x₂
    let PY := absoluteIsomorphismCategory B S hS Z hZ 𝒴 (x₁ ≫ f) (x₂ ≫ f)
    ∃ (H : PX.val ⥤ᵇ PY.val)
      (Δ : (algebraicSpaceStack.{u, w} B S hS Z hZ).val.val ⥤ᵇ PY.val),
      (∀ A : PX.val.obj,
        HEq (H.toFunctor.obj A).x A.x ∧
        HEq (H.toFunctor.obj A).y A.y ∧
        HEq (H.toFunctor.obj A).iso.hom
          (f.hom.hom.toFunctor.map A.iso.hom)) ∧
      (∀ A : (algebraicSpaceStack.{u, w} B S hS Z hZ).val.val.obj,
        HEq (Δ.toFunctor.obj A).x A ∧
        HEq (Δ.toFunctor.obj A).y A ∧
        HEq (Δ.toFunctor.obj A).iso.hom
          (α.hom.hom.toNatTrans.app A))
```

**`AlgebraicGeometry.Stack.relativeIsomorphismIteratedSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeIsomSpaceIteratedForm.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeIsomSpaceIteratedForm.lean#L162). The attribute's comment: “part (2): Isom^α\_\{X/Y}(x₁, x₂) as the iterated fibre product of the source”.

> **Stacks 06PP, part (2): the relative sheaf of isomorphisms from `x₁` to `x₂` lifting `α`,
> in the iterated form the source writes it in.** The 2-fibre product
>
> ```text
> Isom^α_{𝒳/𝒴}(x₁, x₂) = (Z ×_{x₁, 𝒳, x₂} Z) ×_{Z ×_{y₁, 𝒴, y₂} Z, Δ^α} Z
> ```
>
> of the map `H` on absolute isomorphism categories induced by `f` along the twisted diagonal
> `Δ^α` determined by `α`. Its objects over a scheme `W` are the isomorphisms `x₁(z) ≅ x₂(z)` of
> the fibre of `𝒳` over `W` whose image under `f` is the component of `α` at `z`.

```lean
noncomputable def relativeIsomorphismIteratedSpace (f : 𝒳 ⟶ 𝒴)
    (x₁ x₂ : algebraicSpaceStack.{u, w} B S hS Z hZ ⟶ 𝒳) (α : x₁ ≫ f ⟶ x₂ ≫ f) :
    CatFiberedInGroupoids (BigFppfOver B S hS)
```

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpace_relativeIsomorphismIteratedSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeIsomSpaceIteratedForm.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeIsomSpaceIteratedForm.lean#L195). The attribute's comment: “part (2): the iterated form of Isom^α\_\{X/Y}(x₁, x₂) is an algebraic space”.

> **Stacks 06PP, part (2): the iterated form of `Isom^α_{𝒳/𝒴}(x₁, x₂)` is an algebraic
> space.** It is the base change of the twisted diagonal `Δ^α` along `H`; `Δ^α` is representable by
> algebraic spaces and `Z ×_{x₁, 𝒳, x₂} Z` is represented by an algebraic space, so this is
> Stacks 0300.

```lean
theorem isRepresentableByAlgebraicSpace_relativeIsomorphismIteratedSpace (f : 𝒳 ⟶ 𝒴)
    (x₁ x₂ : algebraicSpaceStack.{u, w} B S hS Z hZ ⟶ 𝒳) (α : x₁ ≫ f ⟶ x₂ ≫ f) :
    IsRepresentableByAlgebraicSpace B S hS
      (relativeIsomorphismIteratedSpace B S hS Z hZ f x₁ x₂ α)
```

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_relativeIsomorphismIteratedSpaceProj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeIsomSpaceIteratedForm.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeIsomSpaceIteratedForm.lean#L215). The attribute's comment: “part (2): the iterated form of Isom^α\_\{X/Y}(x₁, x₂) is an algebraic space over Z”.

> **Stacks 06PP, part (2): the iterated form of `Isom^α_{𝒳/𝒴}(x₁, x₂)` is an algebraic space
> over `Z`.** Its structure 1-morphism to the stack of `Z` has an algebraic space as source and the
> stack of `Z` as target, so it is representable by algebraic spaces by Stacks 02ZZ; together with
> `AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpace_relativeIsomorphismIteratedSpace` it is
> therefore a morphism of algebraic spaces with target `Z`.

```lean
theorem isRepresentableByAlgebraicSpaces_relativeIsomorphismIteratedSpaceProj (f : 𝒳 ⟶ 𝒴)
    (x₁ x₂ : algebraicSpaceStack.{u, w} B S hS Z hZ ⟶ 𝒳) (α : x₁ ≫ f ⟶ x₂ ≫ f) :
    IsRepresentableByAlgebraicSpaces B S hS
      (relativeIsomorphismIteratedSpaceProj B S hS Z hZ f x₁ x₂ α)
```

## Tag 0CPK, a lemma

[Tag 0CPK](https://stacks.math.columbia.edu/tag/0CPK) in the Stacks Project.

**`AlgebraicGeometry.Stack.isomSpaceOverSpaceMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/IsomSpaceOverAlgebraicSpace.lean, line 394](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/IsomSpaceOverAlgebraicSpace.lean#L394). The attribute's comment: “part (3): the map on isomorphism sheaves”.

> **Stacks 0CPK, part (3): the map on isomorphism sheaves.** A 1-morphism `f : 𝒳 ⟶ 𝒴` of
> algebraic stacks carries `Isom_𝒳(x₁, x₂)` into `Isom_𝒴(x₁ ≫ f, x₂ ≫ f)`: it keeps the point of `Z`
> and applies `f` to the isomorphism of the fibre.
>
> The source calls this a map *of algebraic spaces*; that the source and target are algebraic
> spaces over `Z` is asserted by Stacks 06PP and is not proved here, so this is the map of the
> underlying sheaves.

```lean
noncomputable def isomSpaceOverSpaceMap (f : 𝒳 ⟶ 𝒴)
    (x₁ x₂ : algebraicSpaceStack.{u, w} B S hS Z hZ ⟶ 𝒳) :
    isomSpaceOverSpace B S hS Z hZ x₁ x₂ ⟶
      isomSpaceOverSpace B S hS Z hZ (x₁ ≫ f) (x₂ ≫ f)
```

**`AlgebraicGeometry.Stack.isPullback_relativeIsomSpaceOverSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/IsomSpaceOverAlgebraicSpace.lean, line 592](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/IsomSpaceOverAlgebraicSpace.lean#L592). The attribute's comment: “part (3): the cartesian square”.

> **Stacks 0CPK, part (3): the cartesian square.** The isomorphisms of `x₁` and `x₂` lifting the
> 2-morphism `α : x₁ ≫ f ⟶ x₂ ≫ f` are the fibre product of `Isom_𝒳(x₁, x₂)` and `Z` over
> `Isom_𝒴(x₁ ≫ f, x₂ ≫ f)`, along the map induced by `f` and the section determined by `α`.
>
> The square is cartesian pointwise and for an elementary reason: a section of `Isom_𝒳(x₁, x₂)` over
> `W` together with a point of `Z` over `W` having the same image in `Isom_𝒴(x₁ ≫ f, x₂ ≫ f)` is the
> same thing as a section of `Isom_𝒳(x₁, x₂)` whose image under `f` is the component of `α`, because
> the two images have the same point of `Z` as their first component.
>
> The square is the one Stacks 0CPK part (3) draws, as a square of sheaves on the big fppf site of
> `S`; that its four corners are algebraic spaces is asserted by Stacks 06PP and is not proved
> here. Together with `AlgebraicGeometry.Stack.relativeIsomSpaceOverSpace` it also identifies the
> explicit sub-presheaf with the fibre product of Stacks 06PP part (2).

```lean
theorem isPullback_relativeIsomSpaceOverSpace (f : 𝒳 ⟶ 𝒴)
    (x₁ x₂ : algebraicSpaceStack.{u, w} B S hS Z hZ ⟶ 𝒳) (α : x₁ ≫ f ⟶ x₂ ≫ f) :
    IsPullback (relativeIsomSpaceOverSpaceι B S hS Z hZ f x₁ x₂ α)
      (relativeIsomSpaceOverSpaceProj B S hS Z hZ f x₁ x₂ α)
      (isomSpaceOverSpaceMap B S hS Z hZ f x₁ x₂)
      (twistedSection B S hS Z hZ f x₁ x₂ α)
```

**`AlgebraicGeometry.Stack.relativeAutSpaceSliceGrpObj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeIsomGroupOverAlgebraicSpace.lean, line 492](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeIsomGroupOverAlgebraicSpace.lean#L492). The attribute's comment: “part (1): the relative automorphism sheaf is a group over Z”.

> The group structure over `Z` on the sheaf `Isom_{𝒳/𝒴}(x, x)` of automorphisms of an
> algebraic-space-valued point `x` of `𝒳` whose image under `f` is the identity: the law is
> composition of automorphisms, the unit is the identity and the inverse is the inverse
> automorphism.

```lean
noncomputable def relativeAutSpaceSliceGrpObj :
    GrpObj (relativeAutSpaceSlice B S hS Z hZ f x)
```

**`AlgebraicGeometry.Stack.relativeAutGroupAlgebraicSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeIsomGroupOverAlgebraicSpace.lean, line 521](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeIsomGroupOverAlgebraicSpace.lean#L521). The attribute's comment: “part (1): the relative automorphisms are a group algebraic space over Z”.

> The relative automorphism sheaf `Isom_{𝒳/𝒴}(x, x)` as a group algebraic space over `Z`, with
> the group structure `AlgebraicGeometry.Stack.relativeAutSpaceSliceGrpObj`.

```lean
noncomputable def relativeAutGroupAlgebraicSpace :
    Space.GroupAlgebraicSpace B S hS Z hZ
```

**`AlgebraicGeometry.Stack.relativeIsomSpaceSliceModObj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeIsomGroupOverAlgebraicSpace.lean, line 608](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeIsomGroupOverAlgebraicSpace.lean#L608). The attribute's comment: “part (4): the action by postcomposition”.

> The action of `Isom_{𝒳/𝒴}(x₂, x₂)` on `Isom^α_{𝒳/𝒴}(x₁, x₂)` over `Z`, by
> postcomposition.

```lean
noncomputable def relativeIsomSpaceSliceModObj :
    letI : GrpObj (relativeAutSpaceSlice B S hS Z hZ f x₂) :=
      relativeAutSpaceSliceGrpObj B S hS Z hZ f x₂
    ModObj (relativeAutSpaceSlice B S hS Z hZ f x₂)
      (relativeIsomSpaceSlice B S hS Z hZ f x₁ x₂ α)
```

**`AlgebraicGeometry.Stack.isPseudoTorsor_relativeIsomSpaceSlice`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeIsomGroupOverAlgebraicSpace.lean, line 679](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeIsomGroupOverAlgebraicSpace.lean#L679). The attribute's comment: “part (4): the relative isomorphisms are a pseudo-torsor”.

> The isomorphisms lifting `α` are a pseudo-torsor under the relative automorphisms of the
> target point, over `Z`: `Isom^α_{𝒳/𝒴}(x₁, x₂)` is a pseudo-torsor under `Isom_{𝒳/𝒴}(x₂, x₂)`.

```lean
theorem isPseudoTorsor_relativeIsomSpaceSlice :
    letI : GrpObj (relativeAutSpaceSlice B S hS Z hZ f x₂) :=
      relativeAutSpaceSliceGrpObj B S hS Z hZ f x₂
    letI : ModObj (relativeAutSpaceSlice B S hS Z hZ f x₂)
        (relativeIsomSpaceSlice B S hS Z hZ f x₁ x₂ α) :=
      relativeIsomSpaceSliceModObj B S hS Z hZ f x₁ x₂ α
    IsPseudoTorsor (relativeAutSpaceSlice B S hS Z hZ f x₂)
      (relativeIsomSpaceSlice B S hS Z hZ f x₁ x₂ α)
```

**`AlgebraicGeometry.Stack.isAlgebraicSpace_isPseudoTorsor_relativeIsomSpaceSlice`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeIsomGroupOverAlgebraicSpace.lean, line 707](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeIsomGroupOverAlgebraicSpace.lean#L707). The attribute's comment: “part (4): the relative isomorphisms are an algebraic space and a pseudo-torsor”.

> For every 2-morphism `α : x₁ ≫ f ⟶ x₂ ≫ f` the sheaf `Isom^α_{𝒳/𝒴}(x₁, x₂)` and the relative
> automorphism sheaf `Isom_{𝒳/𝒴}(x₂, x₂)` are algebraic spaces over `Z`, and the first is a
> pseudo-torsor under the second over `Z`.

```lean
theorem isAlgebraicSpace_isPseudoTorsor_relativeIsomSpaceSlice :
    letI : GrpObj (relativeAutSpaceSlice B S hS Z hZ f x₂) :=
      relativeAutSpaceSliceGrpObj B S hS Z hZ f x₂
    letI : ModObj (relativeAutSpaceSlice B S hS Z hZ f x₂)
        (relativeIsomSpaceSlice B S hS Z hZ f x₁ x₂ α) :=
      relativeIsomSpaceSliceModObj B S hS Z hZ f x₁ x₂ α
    IsAlgebraicSpace B S hS (relativeIsomSpaceOverSpace B S hS Z hZ f x₁ x₂ α) ∧
      IsAlgebraicSpace B S hS (relativeIsomSpaceOverSpace B S hS Z hZ f x₂ x₂ (𝟙 (x₂ ≫ f))) ∧
      IsPseudoTorsor (relativeAutSpaceSlice B S hS Z hZ f x₂)
        (relativeIsomSpaceSlice B S hS Z hZ f x₁ x₂ α)
```

**`AlgebraicGeometry.Stack.isAlgebraicSpace_isPullback_relativeIsomSpaceOverSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeIsomGroupOverAlgebraicSpace.lean, line 725](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeIsomGroupOverAlgebraicSpace.lean#L725). The attribute's comment: “part (3): the cartesian square of algebraic spaces over Z”.

> The sheaves `Isom_𝒳(x₁, x₂)`, `Isom_𝒴(f x₁, f x₂)` and `Isom^α_{𝒳/𝒴}(x₁, x₂)` are algebraic
> spaces over `Z`, and the square cutting out `Isom^α_{𝒳/𝒴}(x₁, x₂)` along
> `AlgebraicGeometry.Stack.isomSpaceOverSpaceMap` is cartesian.

```lean
theorem isAlgebraicSpace_isPullback_relativeIsomSpaceOverSpace :
    IsAlgebraicSpace B S hS (isomSpaceOverSpace B S hS Z hZ x₁ x₂) ∧
      IsAlgebraicSpace B S hS (isomSpaceOverSpace B S hS Z hZ (x₁ ≫ f) (x₂ ≫ f)) ∧
      IsAlgebraicSpace B S hS (relativeIsomSpaceOverSpace B S hS Z hZ f x₁ x₂ α) ∧
      IsPullback (relativeIsomSpaceOverSpaceι B S hS Z hZ f x₁ x₂ α)
        (relativeIsomSpaceOverSpaceProj B S hS Z hZ f x₁ x₂ α)
        (isomSpaceOverSpaceMap B S hS Z hZ f x₁ x₂)
        (twistedSection B S hS Z hZ f x₁ x₂ α)
```

**`AlgebraicGeometry.Stack.isMonHom_relativeAutSpaceSliceι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeIsomGroupOverAlgebraicSpace.lean, line 909](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeIsomGroupOverAlgebraicSpace.lean#L909). The attribute's comment: “part (2): the first map is a homomorphism of groups over Z”.

> The inclusion `Isom_{𝒳/𝒴}(x, x) ⟶ Isom_𝒳(x, x)` is a homomorphism of groups over `Z`.

```lean
theorem isMonHom_relativeAutSpaceSliceι :
    letI : GrpObj (relativeAutSpaceSlice B S hS Z hZ f x) :=
      relativeAutSpaceSliceGrpObj B S hS Z hZ f x
    letI : GrpObj (isomSpaceSlice B S hS Z hZ x x) := isomSpaceSliceGrpObj B S hS Z hZ x
    IsMonHom (relativeAutSpaceSliceι B S hS Z hZ x f)
```

**`AlgebraicGeometry.Stack.isMonHom_isomSpaceSliceMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeIsomGroupOverAlgebraicSpace.lean, line 935](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeIsomGroupOverAlgebraicSpace.lean#L935). The attribute's comment: “part (2): the second map is a homomorphism of groups over Z”.

> The map `Isom_𝒳(x, x) ⟶ Isom_𝒴(f x, f x)` induced by `f` is a homomorphism of groups over
> `Z`.

```lean
theorem isMonHom_isomSpaceSliceMap :
    letI : GrpObj (isomSpaceSlice B S hS Z hZ x x) := isomSpaceSliceGrpObj B S hS Z hZ x
    letI : GrpObj (isomSpaceSlice B S hS Z hZ (x ≫ f) (x ≫ f)) :=
      isomSpaceSliceGrpObj B S hS Z hZ (x ≫ f)
    IsMonHom (isomSpaceSliceMap B S hS Z hZ x f)
```

**`AlgebraicGeometry.Stack.relativeAutSpaceSliceι_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeIsomGroupOverAlgebraicSpace.lean, line 961](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeIsomGroupOverAlgebraicSpace.lean#L961). The attribute's comment: “part (2): injectivity of the first map”.

> The inclusion `Isom_{𝒳/𝒴}(x, x) ⟶ Isom_𝒳(x, x)` is a monomorphism.

```lean
theorem relativeAutSpaceSliceι_injective (Q : Over Z)
    (g h : Q ⟶ relativeAutSpaceSlice B S hS Z hZ f x)
    (hgh : g ≫ relativeAutSpaceSliceι B S hS Z hZ x f =
      h ≫ relativeAutSpaceSliceι B S hS Z hZ x f) : g = h
```

**`AlgebraicGeometry.Stack.relativeAutSpaceSlice_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeIsomGroupOverAlgebraicSpace.lean, line 973](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeIsomGroupOverAlgebraicSpace.lean#L973). The attribute's comment: “part (2): exactness at Isom\_𝒳(x, x)”.

> The sequence `0 ⟶ Isom_{𝒳/𝒴}(x, x) ⟶ Isom_𝒳(x, x) ⟶ Isom_𝒴(f x, f x)` of groups over `Z` is
> exact at the middle term: a point of `Isom_𝒳(x, x)` is killed by the second map exactly when it
> comes from a relative automorphism.

```lean
theorem relativeAutSpaceSlice_exact (Q : Over Z) (p : Q ⟶ isomSpaceSlice B S hS Z hZ x x) :
    letI : GrpObj (isomSpaceSlice B S hS Z hZ (x ≫ f) (x ≫ f)) :=
      isomSpaceSliceGrpObj B S hS Z hZ (x ≫ f)
    p ≫ isomSpaceSliceMap B S hS Z hZ x f = 1 ↔
      ∃ g : Q ⟶ relativeAutSpaceSlice B S hS Z hZ f x,
        g ≫ relativeAutSpaceSliceι B S hS Z hZ x f = p
```

**`AlgebraicGeometry.Stack.relativeIsomSpaceSlice_properties`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeIsomGroupOverAlgebraicSpace.lean, line 1019](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeIsomGroupOverAlgebraicSpace.lean#L1019). The attribute's comment: “the whole statement: parts (1), (2), (3) and (4)”.

> For a 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks, an algebraic space `Z` and two points
> `x₁, x₂ : Z ⟶ 𝒳`, the isomorphism sheaves attached to these data, read in the slice over `Z`,
> satisfy:
>
> * the relative automorphism sheaf `Isom_{𝒳/𝒴}(x₂, x₂)` is an algebraic space over `Z` and
>   carries a group structure over `Z`, i.e. is a group algebraic space over `Z`;
> * the sequence `0 ⟶ Isom_{𝒳/𝒴}(x₂, x₂) ⟶ Isom_𝒳(x₂, x₂) ⟶ Isom_𝒴(f x₂, f x₂)` is a sequence of
>   homomorphisms of groups over `Z`, injective at the first map and exact at the middle term;
> * the two isomorphism sheaves are algebraic spaces over `Z` and there is a map
>   `Isom_𝒳(x₁, x₂) ⟶ Isom_𝒴(f x₁, f x₂)` for which the square cutting out
>   `Isom^α_{𝒳/𝒴}(x₁, x₂)` is cartesian for every 2-morphism `α : x₁ ≫ f ⟶ x₂ ≫ f`;
> * that sheaf is an algebraic space over `Z` and a pseudo-torsor under `Isom_{𝒳/𝒴}(x₂, x₂)` over
>   `Z` for every such `α`.

```lean
theorem relativeIsomSpaceSlice_properties (f : 𝒳 ⟶ 𝒴)
    (x₁ x₂ : algebraicSpaceStack.{u, w} B S hS Z hZ ⟶ 𝒳) :
    letI : GrpObj (relativeAutSpaceSlice B S hS Z hZ f x₂) :=
      relativeAutSpaceSliceGrpObj B S hS Z hZ f x₂
    letI : GrpObj (isomSpaceSlice B S hS Z hZ x₂ x₂) := isomSpaceSliceGrpObj B S hS Z hZ x₂
    letI : GrpObj (isomSpaceSlice B S hS Z hZ (x₂ ≫ f) (x₂ ≫ f)) :=
      isomSpaceSliceGrpObj B S hS Z hZ (x₂ ≫ f)
    IsAlgebraicSpace B S hS (relativeIsomSpaceOverSpace B S hS Z hZ f x₂ x₂ (𝟙 (x₂ ≫ f))) ∧
      Nonempty (GrpObj (relativeAutSpaceSlice B S hS Z hZ f x₂)) ∧
      IsMonHom (relativeAutSpaceSliceι B S hS Z hZ x₂ f) ∧
      IsMonHom (isomSpaceSliceMap B S hS Z hZ x₂ f) ∧
      (∀ (Q : Over Z) (g h : Q ⟶ relativeAutSpaceSlice B S hS Z hZ f x₂),
        g ≫ relativeAutSpaceSliceι B S hS Z hZ x₂ f =
          h ≫ relativeAutSpaceSliceι B S hS Z hZ x₂ f → g = h) ∧
      (∀ (Q : Over Z) (p : Q ⟶ isomSpaceSlice B S hS Z hZ x₂ x₂),
        p ≫ isomSpaceSliceMap B S hS Z hZ x₂ f = 1 ↔
          ∃ g : Q ⟶ relativeAutSpaceSlice B S hS Z hZ f x₂,
            g ≫ relativeAutSpaceSliceι B S hS Z hZ x₂ f = p) ∧
      IsAlgebraicSpace B S hS (isomSpaceOverSpace B S hS Z hZ x₁ x₂) ∧
      IsAlgebraicSpace B S hS (isomSpaceOverSpace B S hS Z hZ (x₁ ≫ f) (x₂ ≫ f)) ∧
      (∀ α : x₁ ≫ f ⟶ x₂ ≫ f,
        IsPullback (relativeIsomSpaceOverSpaceι B S hS Z hZ f x₁ x₂ α)
          (relativeIsomSpaceOverSpaceProj B S hS Z hZ f x₁ x₂ α)
          (isomSpaceOverSpaceMap B S hS Z hZ f x₁ x₂)
          (twistedSection B S hS Z hZ f x₁ x₂ α)) ∧
      (∀ α : x₁ ≫ f ⟶ x₂ ≫ f,
        IsAlgebraicSpace B S hS (relativeIsomSpaceOverSpace B S hS Z hZ f x₁ x₂ α)) ∧
      (∀ α : x₁ ≫ f ⟶ x₂ ≫ f,
        letI : ModObj (relativeAutSpaceSlice B S hS Z hZ f x₂)
            (relativeIsomSpaceSlice B S hS Z hZ f x₁ x₂ α) :=
          relativeIsomSpaceSliceModObj B S hS Z hZ f x₁ x₂ α
        IsPseudoTorsor (relativeAutSpaceSlice B S hS Z hZ f x₂)
          (relativeIsomSpaceSlice B S hS Z hZ f x₁ x₂ α))
```

## Tag 06PQ, a lemma

[Tag 06PQ](https://stacks.math.columbia.edu/tag/06PQ) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_cartesianRelativeInertiaSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaBaseChange.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeInertiaBaseChange.lean#L214). The attribute's comment: “left square of algebraic stacks”.

> **Stacks 06PQ, the left square.** Both squares of the diagram of Stacks 06PQ are 2-fibre
> products of algebraic stacks: the right one is the defining base-change square of Stacks 04T2,
> and this provides the left one, a comparison 1-morphism from the relative inertia of the base
> change to the relative inertia of `π`, with the prescribed action on objects and automorphisms,
> exhibiting the left square as a 2-fibre product in the 2-category of algebraic stacks.

```lean
theorem exists_cartesianRelativeInertiaSquare :
    Nonempty (CartesianRelativeInertiaSquare B S hS π f)
```

**`AlgebraicGeometry.Stack.isTwoFibreProduct_twoFibreProductSquareAlgebraicStacks`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/TwoFibreProductSquareAlgebraicStack.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/TwoFibreProductSquareAlgebraicStack.lean#L112). The attribute's comment: “right square of algebraic stacks”.

> **Stacks 04T2, second assertion: the 2-categorical universal property.** The canonical
> square of a cospan of algebraic stacks over `S` is a 2-fibre product in the 2-category of
> algebraic stacks, and not merely in the ambient 2-category of categories fibred in groupoids:
> the square underlying it is the canonical one there, which is a 2-fibre product
> unconditionally, and the 2-category of algebraic stacks is a full sub-2-category.
>
> This is also the **right square of Stacks 06PQ**, whose left square is
> `AlgebraicGeometry.Stack.exists_cartesianRelativeInertiaSquare`: the right square of the
> diagram there is the defining base-change square of the cospan `(π, f)`.

```lean
noncomputable def isTwoFibreProduct_twoFibreProductSquareAlgebraicStacks
    {𝒳 𝒴 𝒵 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒵) (g : 𝒴 ⟶ 𝒵) :
    Bicategory.IsTwoFibreProduct (twoFibreProductSquareAlgebraicStacks B S hS f g)
```

## Tag 06R5, a lemma

[Tag 06R5](https://stacks.math.columbia.edu/tag/06R5) in the Stacks Project.

**`CategoryTheory.inertiaPullbackComparison_isEquivalenceOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/InertiaMonomorphism.lean, line 417](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/InertiaMonomorphism.lean#L417).

> For a fully faithful morphism, the inertia square is a 2-fibre product
> over the base, with its canonical comparison functor and vertical coherence.

```lean
public theorem inertiaPullbackComparison_isEquivalenceOver
    (hFF : F.FullyFaithful) :
    Nonempty (IsEquivalenceOver (RelativeInertia.toBase pX)
      (TwoFibreProductOver.structureFunctor (RelativeInertia.toBase pY) pX pY
        (RelativeInertia.π pY) F)
      (inertiaPullbackComparison pX pY F hF))
```

## Tag 06PR, a lemma

[Tag 06PR](https://stacks.math.columbia.edu/tag/06PR) in the Stacks Project.

**`AlgebraicGeometry.Stack.isTwoFibreProduct_inertiaPresentationSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/InertiaPresentationSquare.lean, line 456](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/InertiaPresentationSquare.lean#L456). The attribute's comment: “the diagram is 2-cartesian, given Stacks 06PC and Stacks 06PB part 2”.

> Let `[U/R] ⟶ 𝒳` be a presentation and let `G/U` be the stabilizer group
> algebraic space of the presenting groupoid `(U, R, s, t, c)`. Then
>
> ```
> 𝒮_G  ------>  𝒮_U
>  |             |
>  v             v
> ℐ_𝒳  ------>  𝒳
> ```
>
> is a fibre product diagram, i.e. a 2-fibre product in the sense of Stacks 003Q, given Groupoids in
> Spaces, Lemma 06PC and the second assertion of Stacks 06PB as the hypothesis `Z`.

```lean
noncomputable def isTwoFibreProduct_inertiaPresentationSquare
    (Z : InertiaQuotientStackInput B S hS P) :
    Bicategory.IsTwoFibreProduct (inertiaPresentationSquare B S hS P Z)
```

**`AlgebraicGeometry.Stack.nonempty_isTwoFibreProduct_inertiaPresentationSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/InertiaPresentationSquare.lean, line 468](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/InertiaPresentationSquare.lean#L468). The attribute's comment: “the diagram is a fibre product diagram”.

> The diagram of the stabilizer, the object space, the inertia of `𝒳` and `𝒳` attached to a
> presentation `[U/R] ⟶ 𝒳` is a fibre product diagram, given Groupoids in Spaces, Lemma 06PC with the
> inertia stack of `[U/R]` in its lower-left corner.

```lean
theorem nonempty_isTwoFibreProduct_inertiaPresentationSquare
    (Z : InertiaQuotientStackInput B S hS P) :
    Nonempty (Bicategory.IsTwoFibreProduct (inertiaPresentationSquare B S hS P Z))
```

**`AlgebraicGeometry.Stack.isTwoFibreProduct_inertiaPresentationSquareAlgebraicStacks`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/InertiaPresentationSquareAlgebraicStacks.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/InertiaPresentationSquareAlgebraicStacks.lean#L334). The attribute's comment: “the diagram is 2-cartesian in the 2-category of algebraic stacks”.

> Let `𝒳` be an algebraic stack over `S` and let `[U/R] ⟶ 𝒳` be a presentation. Let `G/U` be
> the stabilizer group algebraic space associated to the presenting groupoid `(U, R, s, t, c)`.
> Then
>
> ```
> 𝒮_G  ------>  𝒮_U
>  |             |
>  v             v
> ℐ_𝒳  ------>  𝒳
> ```
>
> is a 2-fibre product diagram in the 2-category of algebraic stacks over `S`.

```lean
noncomputable def isTwoFibreProduct_inertiaPresentationSquareAlgebraicStacks :
    Bicategory.IsTwoFibreProduct (inertiaPresentationSquareAlgebraicStacks B S hS P)
```

**`AlgebraicGeometry.Stack.nonempty_isTwoFibreProduct_inertiaPresentationSquareAlgebraicStacks`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/InertiaPresentationSquareAlgebraicStacks.lean, line 348](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/InertiaPresentationSquareAlgebraicStacks.lean#L348). The attribute's comment: “the diagram is a fibre product diagram of algebraic stacks”.

> For an algebraic stack `𝒳` over `S` with a
> presentation `[U/R] ⟶ 𝒳`, the diagram of the algebraic stack of the stabilizer, the algebraic
> stack of the object space, the inertia of `𝒳` and `𝒳` is a fibre product diagram in the
> 2-category of algebraic stacks over `S`.

```lean
theorem nonempty_isTwoFibreProduct_inertiaPresentationSquareAlgebraicStacks :
    Nonempty (Bicategory.IsTwoFibreProduct
      (inertiaPresentationSquareAlgebraicStacks B S hS P))
```

**`AlgebraicGeometry.Stack.isTwoFibreProduct_presentationInertiaSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/InertiaPresentationSquareCanonical.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/InertiaPresentationSquareCanonical.lean#L137). The attribute's comment: “the diagram is 2-cartesian”.

> **Stacks 06PR.** Let `𝒳` be a category fibred in groupoids over the big fppf site of `S` — in
> particular an algebraic stack — and let `[U/R] ⟶ 𝒳` be a presentation (Stacks 04TI). Let `G/U` be
> the stabilizer group algebraic space associated to the groupoid `(U, R, s, t, c)` (Stacks 0448).
> Then
>
> ```
> 𝒮_G  ------>  𝒮_U
>  |             |
>  v             v
> ℐ_𝒳  ------>  𝒳
> ```
>
> is a fibre product diagram, i.e. a 2-fibre product in the sense of Stacks 003Q.
>
> This is `AlgebraicGeometry.Stack.isTwoFibreProduct_inertiaPresentationSquare` at the canonical
> input of `AlgebraicGeometry.Stack.inertiaQuotientStackInput`, so the proof is the proof of the
> source — immediate from Groupoids in Spaces, Lemma 06PC
> (`AlgebraicGeometry.Stack.isTwoFibreProduct_inertiaQuotientStackSquareFibred` together with the
> second assertion of Stacks 06PB) pasted onto the inertia square of Stacks 06R5 for the
> presentation — and the only datum it consumes is the presentation.

```lean
noncomputable def isTwoFibreProduct_presentationInertiaSquare :
    Bicategory.IsTwoFibreProduct (presentationInertiaSquare P)
```

**`AlgebraicGeometry.Stack.nonempty_isTwoFibreProduct_presentationInertiaSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/InertiaPresentationSquareCanonical.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/InertiaPresentationSquareCanonical.lean#L145). The attribute's comment: “the diagram is a fibre product diagram”.

> **Stacks 06PR**, in propositional form: for a presentation `[U/R] ⟶ 𝒳` the diagram of the
> stack of the stabilizer, the stack of the object space, the inertia of `𝒳` and `𝒳` is a fibre
> product diagram.

```lean
theorem nonempty_isTwoFibreProduct_presentationInertiaSquare :
    Nonempty (Bicategory.IsTwoFibreProduct (presentationInertiaSquare P))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.5, Tag 050P](https://stacks.math.columbia.edu/tag/050P)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
