---
declaration: section
origin: cited
lean: AlgebraicGeometry.SheafOfModules.deRhamDifferential, AlgebraicGeometry.SheafOfModules.relativeDeRhamComplex, AlgebraicGeometry.SheafOfModules.deRhamDifferential_unique, AlgebraicGeometry.SheafOfModules.inverseImageExteriorAlgebraIso, AlgebraicGeometry.SheafOfModules.inverseImageDifferentialForms, AlgebraicGeometry.SheafOfModules.inverseImageDeRhamComplexIso, AlgebraicGeometry.SheafOfModules.inverseImageDeRhamComplexIso_canonical, AlgebraicGeometry.SheafOfModules.inverseImageDeRhamComplexIso_unique
statement: formalized
proof: formalized
---

# 17.30 The de Rham complex

Section 17.30 of the Stacks Project, [Tag 0FKL](https://stacks.math.columbia.edu/tag/0FKL). 5 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FKM, a definition

[Tag 0FKM](https://stacks.math.columbia.edu/tag/0FKM) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.deRhamDifferential`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/DeRhamExistence.lean, line 369](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/DeRhamExistence.lean#L369). The attribute's comment: “existence: the de Rham differential exists. The tag defines the complex by a uniqueness property, so the covering set is this construction, `relativeDeRhamComplex` and `deRhamDifferential_unique`.”. References: EGA IV (16.6.2), “existence”.

> **The relative de Rham differential of `φ` exists.** The differential in each degree is the
> sheafification of the ring-level de Rham differential, read on `⋀ᵖ Ω` through the exact-wedge
> comparison; it squares to zero and obeys the de Rham rule because the sectionwise differential
> does.

```lean
noncomputable def deRhamDifferential : DeRhamDifferential B
```

**`AlgebraicGeometry.SheafOfModules.relativeDeRhamComplex`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/DeRhamExistence.lean, line 378](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/DeRhamExistence.lean#L378). The attribute's comment: “the canonical complex: the de Rham complex of `B` over `A`, assembled from the differential of `deRhamDifferential`. Its terms and arrows are `deRhamComplex_X` and `deRhamComplex_d`.”.

> **The relative de Rham complex** `⋀⁰ Ω → ⋀¹ Ω → ⋀² Ω → ⋯` of sheaves of `A`-modules.

```lean
noncomputable abbrev relativeDeRhamComplex :
    CochainComplex
      (_root_.SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf.{u, u, u} A)) ℕ
```

**`AlgebraicGeometry.SheafOfModules.deRhamDifferential_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/DeRhamExistence.lean, line 388](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/DeRhamExistence.lean#L388). The attribute's comment: “uniqueness: a de Rham differential is the one constructed here, so the complex of Tag 0FKM is well defined. The general two-differential form is `DeRhamDifferential.eq` of `StacksFrontier.Topology.Sheaves.Modules.DeRhamUniqueness`.”. References: EGA IV (16.6.2), “uniqueness”.

> **The relative de Rham differential is unique.** This is
> `AlgebraicGeometry.SheafOfModules.DeRhamDifferential.eq` read at the constructed differential.

```lean
theorem deRhamDifferential_unique (D : DeRhamDifferential B) : D = deRhamDifferential B
```

## Tag 0FKP, a lemma

[Tag 0FKP](https://stacks.math.columbia.edu/tag/0FKP) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.inverseImageExteriorAlgebraIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/DeRhamInverseImage.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/DeRhamInverseImage.lean#L209). The attribute's comment: “canonicality of the identification of the terms, as sheaves of `f⁻¹ℬ`-modules: the comparison is the one compatible with the exterior products, the units and the exact differentials, and that determines it. The complex-level statement of the tag is `inverseImageDeRhamComplexIso` below.”.

> **Stacks Project, Tag 0FKP, canonicality.** The canonical comparison between the inverse image
> of the exterior algebra of `Ω_{ℬ/𝒜}` and the exterior algebra of `Ω_{f⁻¹ℬ/f⁻¹𝒜}`, in every degree
> and on the underlying direct-sum sheaf, together with its compatibility with the exterior products,
> the degree-zero units and the degree-one generators. Those compatibilities determine the
> comparison, by `Stacks.PullbackExteriorAlgebra.exteriorAlgebraPullbackIso_unique`.

```lean
def inverseImageExteriorAlgebraIso :
    ExteriorAlgebraPullbackIso (RingedSpace.inverseImageProjection X f)
      (differentialAlgebras.{u} φ).exterior (differentialAlgebras.{u} φ).exteriorGenerator
      (differentialAlgebras.{u} (inverseImageRingMap φ f)).exterior
      (inverseImageExteriorGenerator φ f)
```

**`AlgebraicGeometry.SheafOfModules.inverseImageDifferentialForms`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/DeRhamInverseImage.lean, line 224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/DeRhamInverseImage.lean#L224). The attribute's comment: “the identification of the terms: in each degree `p` the inverse image of `Ωᵖ_{ℬ/𝒜}` is `Ωᵖ_{f⁻¹ℬ/f⁻¹𝒜}`, as sheaves of `f⁻¹ℬ`-modules. The identification of the complexes of `f⁻¹𝒜`-modules is `inverseImageDeRhamComplexIso` below, which is built from this one by `inverseImageRestrictScalarsIso`.”.

> **Stacks Project, Tag 0FKP, on the terms.** The canonical identification
> `f⁻¹ Ωᵖ_{ℬ/𝒜} = Ωᵖ_{f⁻¹ℬ/f⁻¹𝒜}` of the inverse image of the sheaf of relative differential
> `p`-forms with the sheaf of relative differential `p`-forms of the inverse-image rings.

```lean
def inverseImageDifferentialForms (p : ℕ) :
    (pullbackFunctor (RingedSpace.inverseImageProjection X f)).obj (differentialForms.{u} φ p) ≅
      differentialForms.{u} (inverseImageRingMap φ f) p
```

**`AlgebraicGeometry.SheafOfModules.inverseImageDeRhamComplexIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/DeRhamInverseImage.lean, line 716](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/DeRhamInverseImage.lean#L716). The attribute's comment: “the identification of the de Rham COMPLEXES: `f⁻¹Ω•_{ℬ/𝒜} = Ω•_{f⁻¹ℬ/f⁻¹𝒜}` as complexes of sheaves of `f⁻¹𝒜`-modules”.

> **Stacks Project, Tag 0FKP.** The canonical identification
> `f⁻¹Ω•_{ℬ/𝒜} = Ω•_{f⁻¹ℬ/f⁻¹𝒜}` of de Rham complexes: the degreewise identification of the
> differential forms, moved into sheaves of `f⁻¹𝒜`-modules and assembled into an isomorphism of
> complexes.

```lean
noncomputable def inverseImageDeRhamComplexIso :
    inverseImageDeRhamComplex φ f ≅
      relativeDeRhamComplex (differentialAlgebras.{u} (inverseImageRingMap φ f))
```

**`AlgebraicGeometry.SheafOfModules.inverseImageDeRhamComplexIso_canonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/DeRhamInverseImage.lean, line 730](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/DeRhamInverseImage.lean#L730). The attribute's comment: “canonicality of the identification of the complexes: it is the map determined by `b · d b₁ ∧ ⋯ ∧ d bₚ ↦ f⁻¹b · d(f⁻¹b₁) ∧ ⋯ ∧ d(f⁻¹bₚ)` on the inverse-image sections”.

> **Stacks Project, Tag 0FKP, canonicality.** The identification of the complexes is the one
> that carries each local multiple of an ordered product of exact differentials to the same
> expression in the inverse-image rings.

```lean
theorem inverseImageDeRhamComplexIso_canonical :
    IsCanonicalInverseImageDeRhamIso φ f (inverseImageDeRhamComplexIso φ f)
```

**`AlgebraicGeometry.SheafOfModules.inverseImageDeRhamComplexIso_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/DeRhamInverseImage.lean, line 739](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/DeRhamInverseImage.lean#L739). The attribute's comment: “uniqueness: a canonical identification of the de Rham complexes is the one constructed here”.

> **Stacks Project, Tag 0FKP, uniqueness.** Canonicality determines the identification of the
> complexes: the local multiples of the ordered products of exact differentials generate the terms
> locally, so an isomorphism of complexes prescribed on them is prescribed.

```lean
theorem inverseImageDeRhamComplexIso_unique
    (e : inverseImageDeRhamComplex φ f ≅
      relativeDeRhamComplex (differentialAlgebras.{u} (inverseImageRingMap φ f)))
    (he : IsCanonicalInverseImageDeRhamIso φ f e) :
    e = inverseImageDeRhamComplexIso φ f
```

## Tag 0G3Y, a lemma

[Tag 0G3Y](https://stacks.math.columbia.edu/tag/0G3Y) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.deRhamDifferentialHom_isGlobalDiffOpOfOrder_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/DeRhamDifferentialOperator.lean, line 256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/DeRhamDifferentialOperator.lean#L256).

> **Stacks Project, Tag 0G3Y.** For a morphism `φ : A ⟶ B` of sheaves of commutative rings on
> a topological space, every differential `d : ⋀ᵖ Ω ⟶ ⋀ᵖ⁺¹ Ω` of the relative de Rham complex is a
> differential operator of order at most one relative to `φ`.

```lean
theorem deRhamDifferentialHom_isGlobalDiffOpOfOrder_one (p : ℕ) :
    DiffOp.IsGlobalDiffOpOfOrder (underlyingRingHom (φ := φ)) 1 (deRhamGlobalOp B p)
```

## Tag 0FKQ, a definition

[Tag 0FKQ](https://stacks.math.columbia.edu/tag/0FKQ) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.deRhamComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/SchemeComplex.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/SchemeComplex.lean#L106). The attribute's comment: “the morphism-of-schemes case”.

> **The relative de Rham complex** `Ω^•_{X/S}` of a morphism of schemes `f : X ⟶ S`: the de
> Rham complex of `𝒪_X` over `f^{-1}𝒪_S`, a cochain complex of sheaves of `f^{-1}𝒪_S`-modules
> on `X`.

```lean
noncomputable def deRhamComplex :
    CochainComplex (_root_.SheafOfModules.{u}
      (AlgebraicGeometry.SheafOfModules.underlyingRingSheaf
        ((TopCat.Sheaf.pullback CommRingCat.{u} f.base).obj S.sheaf))) ℕ
```

**`AlgebraicGeometry.SheafOfModules.relativeDeRhamComplex`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/DeRhamExistence.lean, line 378](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/DeRhamExistence.lean#L378). The attribute's comment: “the morphism-of-ringed-spaces case, at `A := f⁻¹𝒪_Y`”.

> **The relative de Rham complex** `⋀⁰ Ω → ⋀¹ Ω → ⋀² Ω → ⋯` of sheaves of `A`-modules.

```lean
noncomputable abbrev relativeDeRhamComplex :
    CochainComplex
      (_root_.SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf.{u, u, u} A)) ℕ
```

## Tag 0G3Z, a lemma

[Tag 0G3Z](https://stacks.math.columbia.edu/tag/0G3Z) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.deRhamDifferentialHom_isGlobalDiffOpOfOrder_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/DeRhamDifferentialOperator.lean, line 256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/DeRhamDifferentialOperator.lean#L256). The attribute's comment: “the case of a morphism of ringed spaces f : X -> Y, at phi : f^\{-1} O\_Y -> O\_X”.

> **Stacks Project, Tag 0G3Y.** For a morphism `φ : A ⟶ B` of sheaves of commutative rings on
> a topological space, every differential `d : ⋀ᵖ Ω ⟶ ⋀ᵖ⁺¹ Ω` of the relative de Rham complex is a
> differential operator of order at most one relative to `φ`.

```lean
theorem deRhamDifferentialHom_isGlobalDiffOpOfOrder_one (p : ℕ) :
    DiffOp.IsGlobalDiffOpOfOrder (underlyingRingHom (φ := φ)) 1 (deRhamGlobalOp B p)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 17.30, Tag 0FKL](https://stacks.math.columbia.edu/tag/0FKL)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
