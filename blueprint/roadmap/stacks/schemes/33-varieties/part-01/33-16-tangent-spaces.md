---
declaration: section
origin: cited
lean: DualNumber, DualNumber.eps, DualNumber.eps_mul_eps, AlgebraicGeometry.DottedTangentArrow, AlgebraicGeometry.dottedTangentArrowModule, AlgebraicGeometry.dottedTangentArrowAddCommGroup, AlgebraicGeometry.dottedTangentArrowModuleInstance, AlgebraicGeometry.tangentSpaceEquivFiber
statement: formalized
proof: formalized
---

# 33.16 Tangent spaces

Section 33.16 of the Stacks Project, [Tag 0B28](https://stacks.math.columbia.edu/tag/0B28). 10 tags here are carried by 19 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0B29, a definition

[Tag 0B29](https://stacks.math.columbia.edu/tag/0B29) in the Stacks Project.

Declarations registered for the tag:

- [`DualNumber`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DualNumber#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch33.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch33.lean#L41) (StacksFrontier): “the dual numbers `R[ε]`; as an `R`-module `R × R`, free on `1` and `ε`”. References: EGA 0 (22.1.3); EGA 0 (22.1.3.2); SGA 3 II (2.1), “special case”; SGA 3 II (3.14), “partial”; SGA 3 II (4.5.1); SGA 3 II (4.7.1), “special case”; SGA 3 III (4.38); SGA 3 VIIA (1.2.0), “partial”; SGA 3 VIIB (2.6); SGA 3 XI (1.9), “partial”; SGA 4½ Fonctions L (4.5); SGA 7 VI (1.2); SGA 7 VI (1.15), “special case”; SGA 7 VI (1.3(c)), “dual numbers k[ε] = k[k]”.
- [`DualNumber.eps`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DualNumber.eps#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch33.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch33.lean#L43) (StacksFrontier): “the element `ε`”. References: SGA 3 II (4.5.1); SGA 3 II (4.7.1), “partial”.
- [`DualNumber.eps_mul_eps`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DualNumber.eps_mul_eps#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch33.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch33.lean#L44) (StacksFrontier): “`ε² = 0`”. References: SGA 3 II (4.7.1), “partial”; SGA 7 VI (1.15), “relation ε² = 0”.

## Tag 0B2A, an equation

[Tag 0B2A](https://stacks.math.columbia.edu/tag/0B2A) in the Stacks Project.

**`AlgebraicGeometry.DottedTangentArrow`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Tangent/Defs.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Tangent/Defs.lean#L90). The attribute's comment: “the dotted arrows”.

> A dotted arrow in the tangent-space diagram: a morphism from the spectrum of the dual
> numbers which restricts to the point `x` and is a morphism over `S`. Carrying the canonical
> `κ(x)`-vector space structure below, this is the tangent space `T_{X/S, x}` of `X` over `S` at
> `x`, and its elements are the tangent vectors of `X/S` at `x`.

```lean
def DottedTangentArrow {X S : Scheme.{u}} (f : X ⟶ S) (x : X)
```

## Tag 0B2B, a lemma

[Tag 0B2B](https://stacks.math.columbia.edu/tag/0B2B) in the Stacks Project.

**`AlgebraicGeometry.dottedTangentArrowModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Tangent/Defs.lean, line 537](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Tangent/Defs.lean#L537).

> The dotted arrows in the tangent-space diagram carry a canonical vector space structure over
> the residue field `κ(x)`. Its operations are characterized by the square-zero pushout and by
> scaling the infinitesimal generator.

```lean
noncomputable def dottedTangentArrowModule {X S : Scheme.{u}} (f : X ⟶ S) (x : X) :
    TangentSpaceStructure f x
```

## Tag 0B2C, a definition

[Tag 0B2C](https://stacks.math.columbia.edu/tag/0B2C) in the Stacks Project.

**`AlgebraicGeometry.DottedTangentArrow`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Tangent/Defs.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Tangent/Defs.lean#L90). The attribute's comment: “the tangent space as a set”.

> A dotted arrow in the tangent-space diagram: a morphism from the spectrum of the dual
> numbers which restricts to the point `x` and is a morphism over `S`. Carrying the canonical
> `κ(x)`-vector space structure below, this is the tangent space `T_{X/S, x}` of `X` over `S` at
> `x`, and its elements are the tangent vectors of `X/S` at `x`.

```lean
def DottedTangentArrow {X S : Scheme.{u}} (f : X ⟶ S) (x : X)
```

**`AlgebraicGeometry.dottedTangentArrowAddCommGroup`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Tangent/Defs.lean, line 610](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Tangent/Defs.lean#L610). The attribute's comment: “the additive group of tangent vectors”.

> The canonical additive commutative group structure on dotted tangent arrows, i.e. the
> addition of tangent vectors of `X/S` at `x`.

```lean
noncomputable instance dottedTangentArrowAddCommGroup {X S : Scheme.{u}}
    (f : X ⟶ S) (x : X) : AddCommGroup (DottedTangentArrow f x)
```

**`AlgebraicGeometry.dottedTangentArrowModuleInstance`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Tangent/Defs.lean, line 617](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Tangent/Defs.lean#L617). The attribute's comment: “the canonical κ(x)-vector space structure on the tangent space”.

> The canonical `κ(x)`-vector space structure on dotted tangent arrows; with it the dotted
> arrows are the tangent space `T_{X/S, x}`.

```lean
noncomputable instance dottedTangentArrowModuleInstance {X S : Scheme.{u}}
    (f : X ⟶ S) (x : X) : Module (X.residueField x) (DottedTangentArrow f x)
```

## Tag 0BEA, an equation

[Tag 0BEA](https://stacks.math.columbia.edu/tag/0BEA) in the Stacks Project.

**`AlgebraicGeometry.tangentSpaceEquivFiber`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/TangentFibre.lean, line 767](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/TangentFibre.lean#L767).

> The tangent space of `X` over `S` at `x` is canonically identified with the tangent space of
> the fibre `X_{f(x)}` at its corresponding point.

```lean
noncomputable def tangentSpaceEquivFiber : TangentSpaceFiberEquiv f x
```

## Tag 0B2D, a lemma

[Tag 0B2D](https://stacks.math.columbia.edu/tag/0B2D) in the Stacks Project.

**`AlgebraicGeometry.tangentSpaceEquivCotangentSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Tangent/Cotangent.lean, line 279](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Tangent/Cotangent.lean#L279). References: EGA IV (16.5.13), “(16.5.13.1)”.

> **Stacks Project, Tag 0B2D.** The relative tangent space at a point is canonically the
> `𝒪_{X,x}`-linear dual of the stalk of relative differentials, as a vector space over the residue
> field: `T_{X/S,x} = Hom_{𝒪_{X,x}}(Ω_{X/S,x}, κ(x))`.

```lean
noncomputable def tangentSpaceEquivCotangentSpace :
    DottedTangentArrow f x ≃ₗ[X.residueField x] CotangentSpace f x
```

**`AlgebraicGeometry.tangentSpaceEquivCotangentSpace_apply_germ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Tangent/Cotangent.lean, line 298](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Tangent/Cotangent.lean#L298). The attribute's comment: “characterization”.

> **Stacks Project, Tag 0B2D.** The canonical equivalence sends a dual-number arrow to the
> functional which, on the germ `d a` of a universal relative differential, returns the
> coefficient of `ε` in the pullback of `a` along the arrow. This is what makes it canonical.

```lean
theorem tangentSpaceEquivCotangentSpace_apply_germ (θ : DottedTangentArrow f x)
    (U : X.Opens) (hx : x ∈ U) (hU : ⊤ ≤ θ.val ⁻¹ᵁ U) (a : X.presheaf.obj (op U)) :
    tangentSpaceEquivCotangentSpace f x θ
        (TopCat.Presheaf.germ (C := AddCommGrpCat.{u})
          (Scheme.Hom.relativeDifferentials f).val.presheaf U x hx
          ((Scheme.Hom.universalRelativeDerivation f).d a)) =
      pullbackInfinitesimalCoefficient θ U hU a
```

## Tag 0B2E, a lemma

[Tag 0B2E](https://stacks.math.columbia.edu/tag/0B2E) in the Stacks Project.

**`AlgebraicGeometry.relativeCotangentSpaceEquivDifferentialFiber`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Tangent/MaximalIdealCotangent.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Tangent/MaximalIdealCotangent.lean#L128). The attribute's comment: “cotangent space”. References: EGA IV (16.5.13), “partial”.

> Let `f : X ⟶ S` be a morphism of schemes and let `x` be a point of `X` whose residue field
> extension `κ(f x) → κ(x)` is separable.  The relative cotangent space
> `𝔪_x / (𝔪_x² + 𝔪_{f x} 𝒪_{X,x})` of the stalk map of `f` is canonically the residue-field fibre
> `κ(x) ⊗_{𝒪_{X,x}} Ω_{X/S,x}` of the stalk of the sheaf of relative differentials.

```lean
noncomputable def relativeCotangentSpaceEquivDifferentialFiber
    (hsep : Algebra.IsSeparable (S.residueField (f.base x)) (X.residueField x)) :
    Deformation.relativeCotangentSpace (f.stalkMap x).hom ≃ₗ[X.residueField x]
      X.residueField x ⊗[X.presheaf.stalk x] relativeDifferentialStalk f x
```

**`AlgebraicGeometry.relativeCotangentSpaceEquivDifferentialFiber_apply_germ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Tangent/MaximalIdealCotangent.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Tangent/MaximalIdealCotangent.lean#L155). The attribute's comment: “canonical map on differentials”.

> The identification of the relative cotangent space with the residue-field fibre of the
> relative differentials carries the class of the germ at `x` of a local section of `𝒪_X` vanishing
> at `x` to the germ of the universal relative differential of that section.  This is what makes it
> canonical.

```lean
theorem relativeCotangentSpaceEquivDifferentialFiber_apply_germ
    (hsep : Algebra.IsSeparable (S.residueField (f.base x)) (X.residueField x))
    (U : X.Opens) (hx : x ∈ U) (a : X.presheaf.obj (op U))
    (ha : (X.presheaf.germ U x hx).hom a ∈
      maximalIdeal (ToType (X.presheaf.stalk x))) :
    relativeCotangentSpaceEquivDifferentialFiber f x hsep
        (Submodule.Quotient.mk ⟨(X.presheaf.germ U x hx).hom a, ha⟩) =
      (1 : X.residueField x) ⊗ₜ[X.presheaf.stalk x]
        (show relativeDifferentialStalk f x from
          TopCat.Presheaf.germ (C := AddCommGrpCat.{u})
            (Scheme.Hom.relativeDifferentials f).val.presheaf U x hx
            ((Scheme.Hom.universalRelativeDerivation f).d a))
```

**`AlgebraicGeometry.dottedTangentArrowEquivDualRelativeCotangentSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Tangent/MaximalIdealCotangent.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Tangent/MaximalIdealCotangent.lean#L191). The attribute's comment: “tangent space”.

> If the residue field extension `κ(f x) → κ(x)` is separable, the relative tangent space at
> `x` — the space of dual-number arrows into `X` over `S` extending the residue-field point `x` — is
> canonically the `κ(x)`-linear dual of the relative cotangent space
> `𝔪_x / (𝔪_x² + 𝔪_{f x} 𝒪_{X,x})`.

```lean
noncomputable def dottedTangentArrowEquivDualRelativeCotangentSpace
    (hsep : Algebra.IsSeparable (S.residueField (f.base x)) (X.residueField x)) :
    DottedTangentArrow f x ≃ₗ[X.residueField x]
      (Deformation.relativeCotangentSpace (f.stalkMap x).hom →ₗ[X.residueField x]
        X.residueField x)
```

**`AlgebraicGeometry.dottedTangentArrowEquivDualRelativeCotangentSpace_apply_germ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Tangent/MaximalIdealCotangent.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Tangent/MaximalIdealCotangent.lean#L206). The attribute's comment: “canonical map on tangent vectors”.

> The identification of the relative tangent space with the dual of the relative cotangent space
> evaluates a dual-number arrow on the class of the germ of a local section vanishing at `x` by the
> coefficient of `ε` in the pullback of that section along the arrow.

```lean
theorem dottedTangentArrowEquivDualRelativeCotangentSpace_apply_germ
    (hsep : Algebra.IsSeparable (S.residueField (f.base x)) (X.residueField x))
    (θ : DottedTangentArrow f x) (U : X.Opens) (hx : x ∈ U) (hU : ⊤ ≤ θ.val ⁻¹ᵁ U)
    (a : X.presheaf.obj (op U))
    (ha : (X.presheaf.germ U x hx).hom a ∈
      maximalIdeal (ToType (X.presheaf.stalk x))) :
    dottedTangentArrowEquivDualRelativeCotangentSpace f x hsep θ
        (Submodule.Quotient.mk ⟨(X.presheaf.germ U x hx).hom a, ha⟩) =
      pullbackInfinitesimalCoefficient θ U hU a
```

## Tag 0B2F, a lemma

[Tag 0B2F](https://stacks.math.columbia.edu/tag/0B2F) in the Stacks Project.

**`AlgebraicGeometry.tangentMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Tangent/Functorial.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Tangent/Functorial.lean#L200). The attribute's comment: “canonical tangent map”. References: EGA IV (16.5.13), “(16.5.13.5)”.

> The tangent map of a morphism over `S`, with the scalar fields identified by the canonical
> residue-field isomorphism.

```lean
noncomputable def tangentMap (h : f ≫ q = p) (x : X) [IsIso (f.residueFieldMap x)] :
    DottedTangentArrow p x →ₛₗ[(inv (f.residueFieldMap x)).hom]
      DottedTangentArrow q (f x)
```

**`AlgebraicGeometry.tangentMap_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Tangent/Functorial.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Tangent/Functorial.lean#L216). The attribute's comment: “characterization by composition of dual-number arrows”.

> The tangent map is induced by composition of dual-number arrows: a tangent arrow is sent to its
> composite with `f`, pulled back along any ring homomorphism of dual numbers whose two components
> are the residue-field identification.

```lean
theorem tangentMap_apply (h : f ≫ q = p) (x : X) [IsIso (f.residueFieldMap x)]
    (θ : DottedTangentArrow p x)
    (α : DualNumber (X.residueField x) →+* DualNumber (Y.residueField (f x)))
    (hα₀ : ∀ z, TrivSqZeroExt.fst (α z) =
      (inv (f.residueFieldMap x)).hom (TrivSqZeroExt.fst z))
    (hα₁ : ∀ z, TrivSqZeroExt.snd (α z) =
      (inv (f.residueFieldMap x)).hom (TrivSqZeroExt.snd z)) :
    (tangentMap f p q h x θ).val =
      Spec.map (CommRingCat.ofHom α) ≫ θ.val ≫ f
```

**`AlgebraicGeometry.tangentSpaceEquivDualDifferentialFiber_tangentMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Tangent/TangentMapDual.lean, line 404](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Tangent/TangentMapDual.lean#L404). The attribute's comment: “dual to the map Ω\_\{Y/S,y} ⊗ κ(y) → Ω\_\{X/S,x} ⊗ κ(x) via the identifications of Tag 0B2D”. References: EGA IV (16.5.13), “partial, special case”.

> **The tangent map is dual to the map on residue-field fibres.** Let `f : X ⟶ Y` be a morphism
> of schemes over `S`, let `x` be a point of `X` with `κ(f x) = κ(x)`. Under the identifications
> `T_{X/S,x} = Hom_{κ(x)}(κ(x) ⊗ Ω_{X/S,x}, κ(x))` and
> `T_{Y/S,f x} = Hom_{κ(f x)}(κ(f x) ⊗ Ω_{Y/S,f x}, κ(f x))` of Tag 0B2D, the tangent map
> `d f : T_{X/S,x} → T_{Y/S,f x}` is the dual of the natural map
> `κ(f x) ⊗ Ω_{Y/S,f x} → κ(x) ⊗ Ω_{X/S,x}`.

```lean
theorem tangentSpaceEquivDualDifferentialFiber_tangentMap (h : f ≫ q = p) (x : X)
    [IsIso (f.residueFieldMap x)] (θ : DottedTangentArrow p x) :
    tangentSpaceEquivDualDifferentialFiber q (f.base x) (tangentMap f p q h x θ) =
      differentialFiberMapDual f p q h x (tangentSpaceEquivDualDifferentialFiber p x θ)
```

## Tag 0BEB, a lemma

[Tag 0BEB](https://stacks.math.columbia.edu/tag/0BEB) in the Stacks Project.

**`AlgebraicGeometry.tangentSpaceProductEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/TangentProduct.lean, line 545](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/TangentProduct.lean#L545).

> The tangent space of a fibre product at a pair of points rational over the same base point
> is the direct sum of the tangent spaces of the factors. The equivalence is induced by the
> projections.

```lean
noncomputable def tangentSpaceProductEquiv {X Y S : Scheme.{u}}
    (f : X ⟶ S) (g : Y ⟶ S) (z : ↑(pullback f g))
    [IsIso (f.residueFieldMap (pullback.fst f g z))]
    [IsIso (g.residueFieldMap (pullback.snd f g z))] :
    TangentSpaceProductEquiv f g z
```

**`AlgebraicGeometry.tangentSpaceProductFiberEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/TangentProductFibre.lean, line 404](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/TangentProductFibre.lean#L404). The attribute's comment: “T\_\{X ×\_S Y/S,(x,y)} = T\_\{X/S,x} ⊕ T\_\{Y/S,y} at the unique point (x,y): left to right by the projections, right to left by 1 × y and x × 1 on the fibres via 0BEA”. References: SGA 3 V (4.1.2), “more general”.

> **Stacks Project, Tag 0BEB.** Let `X`, `Y` be schemes over `S` and let `z = (x, y)` be a point
> of `X ×_S Y` whose projections `x ∈ X`, `y ∈ Y` have residue fields `κ(x) = κ(s) = κ(y)`, where
> `s` is their common image in `S` (every such pair `x`, `y` comes from a point `z`, by
> `AlgebraicGeometry.Scheme.Pullback.exists_preimage_pullback`). Then `z` is the only point over
> `x` and `y`, and `T_{X ×_S Y/S, (x, y)} = T_{X/S, x} ⊕ T_{Y/S, y}` canonically: from left to
> right by the tangent maps of the projections, from right to left by `1 × y : X_s → X_s ×_s Y_s`
> and `x × 1 : Y_s → X_s ×_s Y_s` via the identification of tangent spaces with tangent spaces of
> fibres (Stacks, Tag 0BEA).

```lean
noncomputable def tangentSpaceProductFiberEquiv {X Y S : Scheme.{u}}
    (f : X ⟶ S) (g : Y ⟶ S) (z : ↑(pullback f g))
    [IsIso (f.residueFieldMap (pullback.fst f g z))]
    [IsIso (g.residueFieldMap (pullback.snd f g z))] :
    TangentSpaceProductFiberEquiv f g z
```

## Tag 0B2G, a lemma

[Tag 0B2G](https://stacks.math.columbia.edu/tag/0B2G) in the Stacks Project.

**`AlgebraicGeometry.injective_tangentMap_iff_unramifiedAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Tangent/Unramified.lean, line 212](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Tangent/Unramified.lean#L212).

> **Stacks Project, Tag 0B2G.** Let `f : X ⟶ Y` be a morphism of schemes over `S`, locally of
> finite type, and let `x` be a point of `X` whose residue field agrees with that of `f x`. Then
> the tangent map `d f : T_{X/S, x} ⟶ T_{Y/S, f x}` is injective if and only if `f` is unramified
> at `x`.

```lean
theorem injective_tangentMap_iff_unramifiedAt (h : f ≫ q = p) [LocallyOfFiniteType f]
    [IsIso (f.residueFieldMap x)] :
    Function.Injective (tangentMap f p q h x) ↔ UnramifiedAt f x
```

**`AlgebraicGeometry.injective_tangentMap_iff_unramifiedAt_of_locallyOfFiniteType_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Tangent/Unramified.lean, line 223](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Tangent/Unramified.lean#L223). The attribute's comment: “with the source locally of finite type over the base”.

> **Stacks Project, Tag 0B2G** under the hypotheses of the source: for `X` locally of finite
> type over `S`, the tangent map of a morphism `f : X ⟶ Y` over `S` is injective at a point where
> the residue field is unchanged if and only if `f` is unramified there. Local finite type of `f`
> itself is Tag 01T8.

```lean
theorem injective_tangentMap_iff_unramifiedAt_of_locallyOfFiniteType_base (h : f ≫ q = p)
    [LocallyOfFiniteType p] [IsIso (f.residueFieldMap x)] :
    Function.Injective (tangentMap f p q h x) ↔ UnramifiedAt f x
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.16, Tag 0B28](https://stacks.math.columbia.edu/tag/0B28)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
