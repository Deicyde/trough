---
declaration: section
origin: cited
lean: AlgebraicGeometry.GroupoidInAlgebraicSpaces.sectionCompHom_source, AlgebraicGeometry.GroupoidInAlgebraicSpaces.sectionComp, AlgebraicGeometry.GroupoidInAlgebraicSpaces.conormalMap_sectionTarget_eq_conormalMap_id, AlgebraicGeometry.GroupoidInAlgebraicSpaces.conormalMap_sectionTarget_comp_inv_eq_id, AlgebraicGeometry.GroupoidInAlgebraicSpaces.bijective_vadd_unitInfinitesimalSection, AlgebraicGeometry.GroupoidInAlgebraicSpaces.unitVAddEquiv, AlgebraicGeometry.GroupoidInAlgebraicSpaces.unitVAddEquiv_add, AlgebraicGeometry.GroupoidInAlgebraicSpaces.unitVAddMulEquiv
statement: formalized
proof: formalized
---

# 79.5 Groupoid of sections

Section 79.5 of the Stacks Project, [Tag 0CKB](https://stacks.math.columbia.edu/tag/0CKB). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CKC, an equation

[Tag 0CKC](https://stacks.math.columbia.edu/tag/0CKC) in the Stacks Project.

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.sectionCompHom_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/Sections.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/Sections.lean#L72). The attribute's comment: “well-definedness of composition”.

> The groupoid composition formula applied to two sections is again a section of the source
> morphism.

```lean
theorem sectionCompHom_source (δ₁ δ₂ : Section G) :
    sectionCompHom G δ₁ δ₂ ≫ G.source = 𝟙 G.objects
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.sectionComp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/Sections.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/Sections.lean#L114). The attribute's comment: “composition formula”.

> Composition of sections of a groupoid in algebraic spaces: `δ₁ ∘ δ₂ = c(δ₁ ∘ t ∘ δ₂, δ₂)`,
> which is again a section by `sectionCompHom_source`.

```lean
noncomputable def sectionComp (δ₁ δ₂ : Section G) : Section G
```

## Tag 0CKD, a lemma

[Tag 0CKD](https://stacks.math.columbia.edu/tag/0CKD) in the Stacks Project.

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.conormalMap_sectionTarget_eq_conormalMap_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/SectionsConormalAction.lean, line 420](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/SectionsConormalAction.lean#L420). The attribute's comment: “the conormal map induced by f = t ∘ δ equals the conormal map induced by the identity; only flatness of s is assumed”.

> **Stacks 0CKD.**  Let `G = (U, R, s, t, c)` be a groupoid in algebraic spaces, let
> `U₀ ⊆ U` be a closed subspace whose inverse images along the source and the target agree — the
> invariance of `AlgebraicGeometry.GroupoidInAlgebraicSpaces.IsInvariantClosed` — and let
> `δ : U ⟶ R` be a section of the source agreeing with the unit on `U₀`, and let `s` be flat.
> Then the conormal map of `𝒞_{U₀/U}` induced by `f = t ∘ δ` is the conormal map induced by
> `id_U`, which is the canonical identification of `(id_{U₀})^*𝒞_{U₀/U}` with `𝒞_{U₀/U}`.  In the
> language of the source, `f` acts as the identity on `𝒞_{U₀/U}`.
>
> The source assumes `s` and `t` flat and `U` a first-order thickening of `U₀`; only flatness of
> `s` is used.

```lean
theorem conormalMap_sectionTarget_eq_conormalMap_id (δ : Section G)
    (hδ : subspaceInclusion C S hS G.objects U₀ ≫ δ.1 =
      subspaceInclusion C S hS G.objects U₀ ≫ identityArrow G)
    (hinv : U₀.1.preimage G.target.hom = U₀.1.preimage G.source.hom)
    (hs : Space.IsFlat C S hS G.source.hom)
    (hsq : subspaceInclusion C S hS G.objects U₀ ≫ (δ.1 ≫ G.target) =
      𝟙 _ ≫ subspaceInclusion C S hS G.objects U₀)
    (hsqId : subspaceInclusion C S hS G.objects U₀ ≫ 𝟙 G.objects =
      𝟙 _ ≫ subspaceInclusion C S hS G.objects U₀) :
    conormalMap C S hS U₀ U₀ (δ.1 ≫ G.target) (𝟙 _) hsq =
      conormalMap C S hS U₀ U₀ (𝟙 G.objects) (𝟙 _) hsqId
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.conormalMap_sectionTarget_comp_inv_eq_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/SectionsConormalAction.lean, line 523](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/SectionsConormalAction.lean#L523). The attribute's comment: “f = t ∘ δ acts as the identity on the conormal module, read through the conormal map of the identity; only flatness of s is assumed”.

> **Stacks 0CKD, read as the identity.**  Transported across the conormal map of the identity
> square — the canonical identification of `(id_{U₀})^*𝒞_{U₀/U}` with `𝒞_{U₀/U}`, an isomorphism by
> `AlgebraicGeometry.Space.isIso_conormalMap_id` — the conormal map induced by `f = t ∘ δ` is the
> identity: followed by the inverse of that identification it is the identity of
> `(id_{U₀})^*𝒞_{U₀/U}`.  As in
> `AlgebraicGeometry.GroupoidInAlgebraicSpaces.conormalMap_sectionTarget_eq_conormalMap_id`, only
> flatness of `s` is assumed.

```lean
theorem conormalMap_sectionTarget_comp_inv_eq_id (δ : Section G)
    (hδ : subspaceInclusion C S hS G.objects U₀ ≫ δ.1 =
      subspaceInclusion C S hS G.objects U₀ ≫ identityArrow G)
    (hinv : U₀.1.preimage G.target.hom = U₀.1.preimage G.source.hom)
    (hs : Space.IsFlat C S hS G.source.hom)
    (hsq : subspaceInclusion C S hS G.objects U₀ ≫ (δ.1 ≫ G.target) =
      𝟙 _ ≫ subspaceInclusion C S hS G.objects U₀)
    (hsqId : subspaceInclusion C S hS G.objects U₀ ≫ 𝟙 G.objects =
      𝟙 _ ≫ subspaceInclusion C S hS G.objects U₀) :
    conormalMap C S hS U₀ U₀ (δ.1 ≫ G.target) (𝟙 _) hsq ≫
        @inv _ _ _ _ (conormalMap C S hS U₀ U₀ (𝟙 G.objects) (𝟙 _) hsqId)
          (isIso_conormalMap_id C S hS U₀ hsqId) = 𝟙 _
```

## Tag 0CKE, an equation

[Tag 0CKE](https://stacks.math.columbia.edu/tag/0CKE) in the Stacks Project.

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.bijective_vadd_unitInfinitesimalSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/SectionsInfinitesimalBijection.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/SectionsInfinitesimalBijection.lean#L234). The attribute's comment: “the displayed bijection Hom\_\{O\_\{U\_0}}(e\_0^*Omega\_\{R\_0/U\_0}, C\_\{U\_0/U}) -> Gamma\_0, theta |-> theta . e, for a groupoid in algebraic spaces and a first order thickening U\_0 of U”.

> **The displayed bijection of Equation (0CKE).**  Translation of the unit is a bijection from
> the `𝒪_{U₀}`-linear maps `θ : e₀^*Ω_{R₀/U₀} ⟶ 𝒞_{U₀/U}` onto the sections `Γ₀` of the source
> which agree with the unit on `U₀`: every `δ ∈ Γ₀` is `θ · e` for exactly one `θ`.

```lean
theorem bijective_vadd_unitInfinitesimalSection :
    letI := (infinitesimalSectionDifference G U₀ hU₀).addAction
    Function.Bijective
      (fun θ : InfinitesimalSectionsHom G U₀ => θ +ᵥ unitInfinitesimalSection G U₀)
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.unitVAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/SectionsInfinitesimalBijection.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/SectionsInfinitesimalBijection.lean#L246). The attribute's comment: “the displayed arrow Hom\_\{O\_\{U\_0}}(e\_0^*Omega\_\{R\_0/U\_0}, C\_\{U\_0/U}) -> Gamma\_0 bundled as a bijection, for a groupoid in algebraic spaces and a first order thickening U\_0 of U”.

> **Equation (0CKE) as a bijection.**  The map `θ ↦ θ · e` from the `𝒪_{U₀}`-linear maps
> `e₀^*Ω_{R₀/U₀} ⟶ 𝒞_{U₀/U}` to the sections `Γ₀` infinitesimally close to the unit, bundled with
> its inverse.

```lean
noncomputable def unitVAddEquiv :
    InfinitesimalSectionsHom G U₀ ≃ InfinitesimalSections G U₀
```

## Tag 0CKF, a lemma

[Tag 0CKF](https://stacks.math.columbia.edu/tag/0CKF) in the Stacks Project.

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.unitVAddEquiv_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/SectionsInfinitesimalGroup.lean, line 365](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/SectionsInfinitesimalGroup.lean#L365). The attribute's comment: “the bijection theta |-> theta . e of (0CKE) carries the sum of two linear maps e\_0^*Omega\_\{R\_0/U\_0} -> C\_\{U\_0/U} to the composite of the two sections in Gamma\_0, for an R-invariant first order thickening U\_0 of U”.

> **Lemma 0CKF.**  Let `(U, R, s, t, c)` be a groupoid in algebraic spaces, `U₀ ⊆ U` an
> `R`-invariant closed subspace such that `U` is a first order thickening of `U₀`.  The bijection
> of Equation [Stacks Project, Tag 0CKE],
> `θ ↦ θ · e` from `Hom_{𝒪_{U₀}}(e₀^*Ω_{R₀/U₀}, 𝒞_{U₀/U})` onto `Γ₀`, sends a sum of linear maps
> to the composite of the corresponding sections:
>
> `(θ₁ + θ₂) · e = (θ₁ · e) ∘ (θ₂ · e)`.
>
> With `InfinitesimalSectionDifference.unitVAddEquiv_zero` (`0 · e = e`) this says that the
> bijection is an isomorphism of groups.

```lean
theorem unitVAddEquiv_add (hinv : U₀.1.preimage G.target.hom = U₀.1.preimage G.source.hom)
    (θ₁ θ₂ : InfinitesimalSectionsHom G U₀) :
    unitVAddEquiv G U₀ hU₀ (θ₁ + θ₂) =
      infinitesimalSectionComp G U₀ (unitVAddEquiv G U₀ hU₀ θ₁) (unitVAddEquiv G U₀ hU₀ θ₂)
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.unitVAddMulEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/SectionsInfinitesimalGroup.lean, line 399](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/SectionsInfinitesimalGroup.lean#L399). The attribute's comment: “the bijection Hom\_\{O\_\{U\_0}}(e\_0^*Omega\_\{R\_0/U\_0}, C\_\{U\_0/U}) -> Gamma\_0 of (0CKE) as an isomorphism from the additive group of linear maps onto Gamma\_0 with its composition, for an R-invariant first order thickening U\_0 of U”.

> **Lemma 0CKF, bundled: the bijection (0CKE) is an isomorphism of groups.**  For an
> `R`-invariant closed subspace `U₀ ⊆ U` of which `U` is a first order thickening, the bijection
> `θ ↦ θ · e` of Equation [Stacks Project, Tag 0CKE] is a multiplicative equivalence from the
> additive group of the `𝒪_{U₀}`-linear maps `e₀^*Ω_{R₀/U₀} ⟶ 𝒞_{U₀/U}` (written
> multiplicatively) onto `Γ₀` with the composition of [Stacks Project, Tag 0CKC].

```lean
noncomputable def unitVAddMulEquiv
    (hinv : U₀.1.preimage G.target.hom = U₀.1.preimage G.source.hom) :
    Multiplicative (InfinitesimalSectionsHom G U₀) ≃* InfinitesimalSections G U₀
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 79.5, Tag 0CKB](https://stacks.math.columbia.edu/tag/0CKB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
