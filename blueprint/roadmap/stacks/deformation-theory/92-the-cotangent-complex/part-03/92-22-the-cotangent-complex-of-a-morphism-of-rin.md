---
declaration: section
origin: cited
lean: AlgebraicGeometry.RingedToposHom.cotangentComplex, AlgebraicGeometry.RingedToposHom.cotangentComplexDerived, AlgebraicGeometry.RingedToposHom.cotangentComplex_homologyZeroIso, AlgebraicGeometry.RingedToposHom.exists_distTriang_transitivity, AlgebraicGeometry.RingedToposHom.canonicalNaiveComparison, AlgebraicGeometry.RingedToposHom.canonicalNaiveComparison_isIso_homologyMap, AlgebraicGeometry.RingedToposHom.naiveComparison, AlgebraicGeometry.RingedToposHom.naiveComparison_isIso_homologyMap
statement: formalized
proof: formalized
---

# 92.22 The cotangent complex of a morphism of ringed topoi

Section 92.22 of the Stacks Project, [Tag 08SQ](https://stacks.math.columbia.edu/tag/08SQ). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08SU, a definition

[Tag 08SU](https://stacks.math.columbia.edu/tag/08SU) in the Stacks Project.

**`AlgebraicGeometry.RingedToposHom.cotangentComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/RingedToposCotangentComplex.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SheavesOfRings/RingedToposCotangentComplex.lean#L58).

> **Stacks 08SU.** The cotangent complex `L_f = L_{𝒪_C/f⁻¹𝒪_D}` of a morphism of ringed
> topoi `(f, f♯) : (Sh(C), 𝒪_C) ⟶ (Sh(D), 𝒪_D)`: the cotangent complex of the inverse-image
> form `f⁻¹𝒪_D ⟶ 𝒪_C` of its structure map.

```lean
noncomputable def cotangentComplex :
    CochainComplex (Sheaf.targetModules.{u, v, w} X.J X.O) ℤ
```

**`AlgebraicGeometry.RingedToposHom.cotangentComplexDerived`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/RingedToposCotangentComplex.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SheavesOfRings/RingedToposCotangentComplex.lean#L65). The attribute's comment: “the derived object”.

> **Stacks 08SU.** The cotangent complex of a morphism of ringed topoi, regarded as an object
> of the derived category of sheaves of `𝒪_C`-modules.

```lean
noncomputable abbrev cotangentComplexDerived
    [HasDerivedCategory.{t} (Sheaf.targetModules.{u, v, w} X.J X.O)] :
    DerivedCategory (Sheaf.targetModules.{u, v, w} X.J X.O)
```

## Tag 08V0, a lemma

[Tag 08V0](https://stacks.math.columbia.edu/tag/08V0) in the Stacks Project.

**`AlgebraicGeometry.RingedToposHom.cotangentComplex_homologyZeroIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/RingedToposHomologyZero.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SheavesOfRings/RingedToposHomologyZero.lean#L106).

> **Stacks 08V0.** The zeroth homology of the cotangent complex of a morphism of ringed topoi
> is its sheaf of relative differentials: `H⁰(L_f) = Ω_f`.

```lean
noncomputable def cotangentComplex_homologyZeroIso :
    (f.cotangentComplex).homology 0 ≅ f.differentials
```

## Tag 08V1, a lemma

[Tag 08V1](https://stacks.math.columbia.edu/tag/08V1) in the Stacks Project.

**`AlgebraicGeometry.RingedToposHom.exists_distTriang_transitivity`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/RingedToposTransitivityTriangleDerived.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SheavesOfRings/RingedToposTransitivityTriangleDerived.lean#L330).

> **Stacks 08V1.** Let `f : (Sh(C₁), 𝒪₁) ⟶ (Sh(C₂), 𝒪₂)` and `g : (Sh(C₂), 𝒪₂) ⟶ (Sh(C₃), 𝒪₃)`
> be morphisms of ringed topoi. The canonical triangle
>
> `Lf^* L_g ⟶ L_{g ∘ f} ⟶ L_f ⟶ Lf^* L_g[1]`
>
> is distinguished in `D(𝒪₁)`. Its first two arrows are `transitivityUnit` and
> `transitivityCounit`, those of the fundamental triangle of the tower
> `(g ∘ f)⁻¹𝒪₃ = f⁻¹g⁻¹𝒪₃ ⟶ f⁻¹𝒪₂ ⟶ 𝒪₁` of Tag 08SZ; its first vertex is the derived pullback of
> `L_g`, which `L_g` being a bounded above complex of flat modules computes degreewise as
> `L_{f⁻¹𝒪₂/f⁻¹g⁻¹𝒪₃} ⊗_{f⁻¹𝒪₂} 𝒪₁` (Tags 06YY and 08SV).

```lean
theorem exists_distTriang_transitivity :
    ∃ δ : G.cotangentComplexDerived ⟶ ((derivedPullback G).obj F.cotangentComplexDerived)⟦(1 : ℤ)⟧,
      Triangle.mk (transitivityUnit F G) (transitivityCounit F G) δ ∈
        distTriang (DerivedCategory (Sheaf.targetModules.{u, v, w} X.J X.O))
```

## Tag 08V2, a lemma

[Tag 08V2](https://stacks.math.columbia.edu/tag/08V2) in the Stacks Project.

**`AlgebraicGeometry.RingedToposHom.canonicalNaiveComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/NaiveComparisonCanonical.lean, line 440](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SheavesOfRings/NaiveComparisonCanonical.lean#L440). The attribute's comment: “the canonical map `L_f → NL_f` of a morphism of ringed topoi, into the naive cotangent complex `NL_{𝒪_C/f⁻¹𝒪_D}` of Tag 08TW”.

> **Stacks 08V2, the canonical map.** The canonical map `L_f ⟶ NL_f` of a morphism of ringed
> topoi `(f, f♯) : (Sh(C), 𝒪_C) ⟶ (Sh(D), 𝒪_D)`, into `NL_f = NL_{𝒪_C/f⁻¹𝒪_D}` of Tag 08TW: the
> special case at `f⁻¹𝒪_D ⟶ 𝒪_C` of the map of Tag 08US.

```lean
noncomputable def canonicalNaiveComparison :
    f.cotangentComplex ⟶
      Stacks.SheafOfModules.naiveCotangentComplex.{v, u, max u v w, u} X.J _ X.O
        f.fSharpInverseImage
```

**`AlgebraicGeometry.RingedToposHom.canonicalNaiveComparison_isIso_homologyMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/NaiveComparisonCanonical.lean, line 452](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SheavesOfRings/NaiveComparisonCanonical.lean#L452). The attribute's comment: “the canonical map identifies the naive cotangent complex `NL_f` with the truncation `τ_{≥ -1} L_f`: it is an isomorphism on the cohomology sheaf of every degree `≥ -1`, the naive complex having no terms outside degrees `-1` and `0`; the special case of Tag 08US”.

> **Stacks 08V2.** The canonical map `L_f ⟶ NL_f` is an isomorphism on the cohomology sheaf of
> every degree `≥ -1`; since `NL_f` has no terms outside degrees `-1` and `0`, it identifies the
> naive cotangent complex with the truncation `τ_{≥ -1} L_f`.

```lean
theorem canonicalNaiveComparison_isIso_homologyMap (i : ℤ) (hi : -1 ≤ i) :
    IsIso (HomologicalComplex.homologyMap f.canonicalNaiveComparison i)
```

**`AlgebraicGeometry.RingedToposHom.naiveComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/RingedToposNaiveComparison.lean, line 352](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SheavesOfRings/RingedToposNaiveComparison.lean#L352). The attribute's comment: “the canonical map `L_f → NL_f` of a morphism of ringed topoi, as a map of complexes of sheaves of `𝒪_C`-modules. Hypotheses beyond the source: `NL_f` is realized as the conormal sequence of the presentation `P₀ ⟶ 𝒪_C` by the degree-zero term of the standard resolution of `f⁻¹𝒪_D ⟶ 𝒪_C`, and the identification of that presentation with `Stacks.Sites.FreeAlgebra.canonicalPresentation` is not carried, so the map is not transported to `Stacks.SheafOfModules.naiveCotangentComplex`. The second assertion of the tag, that this map identifies `NL_f` with the truncation `τ_{≥ -1} L_f`, is the separate carrier `AlgebraicGeometry.RingedToposHom.naiveComparison_isIso_homologyMap`”.

> The canonical map `L_f ⟶ NL_f` from the cotangent complex of a morphism of ringed topoi to its
> naive cotangent complex: `CategoryTheory.Sheaf.naiveComparison` at the inverse-image form
> `f⁻¹𝒪_D ⟶ 𝒪_C` of the structure map. It is `d x ⊗ b ↦ b · [d₀ x - d₁ x]` in degree `-1`, it is
> `d p ⊗ b ↦ b ⊗ d p` in degree `0`, and it is zero in every other degree.

```lean
noncomputable def naiveComparison : f.cotangentComplex ⟶ f.naiveCotangentComplex
```

**`AlgebraicGeometry.RingedToposHom.naiveComparison_isIso_homologyMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/RingedToposNaiveComparison.lean, line 370](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SheavesOfRings/RingedToposNaiveComparison.lean#L370). The attribute's comment: “the second assertion of the tag: the canonical map identifies `NL_f` with the truncation `τ_{≥ -1} L_f`, stated as: it is an isomorphism on the cohomology sheaf of every degree `≥ -1`, the naive complex having no cohomology below degree `-1` by `AlgebraicGeometry.RingedToposHom.naiveCotangentComplex_isZero_homology`. Hypotheses carried: `homologyZeroIsIso` and `homologyNegOneIsIso`, the isomorphisms on `H⁰` and on `H^{-1}`, which are the final step of the proof of Tag 08US that this tag is the special case of — the comparison with the chaotic topology, reducing them to the ring-level map of Tag 08UP and transporting along the inverse-image isomorphism of Tag 08TZ. That tag IS carried as an isomorphism of complexes, `Stacks.SheafOfModules.inverseImageNaiveCotangentComplexIso`; what is not carried is the comparison with the chaotic topology”.

> If the canonical map `L_f ⟶ NL_f` is an isomorphism on the cohomology sheaves of degrees `0`
> and `-1` (the hypotheses `homologyZeroIsIso` and `homologyNegOneIsIso`), then it is an isomorphism
> on the cohomology sheaf of every degree `≥ -1`. Since `NL_f` has no cohomology below degree `-1`,
> by `AlgebraicGeometry.RingedToposHom.naiveCotangentComplex_isZero_homology`, this says that the
> canonical map identifies the naive cotangent complex with the truncation `τ_{≥ -1} L_f`.

```lean
theorem naiveComparison_isIso_homologyMap
    (homologyZeroIsIso : IsIso (HomologicalComplex.homologyMap f.naiveComparison 0))
    (homologyNegOneIsIso : IsIso (HomologicalComplex.homologyMap f.naiveComparison (-1)))
    (i : ℤ) (hi : -1 ≤ i) :
    IsIso (HomologicalComplex.homologyMap f.naiveComparison i)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 92.22, Tag 08SQ](https://stacks.math.columbia.edu/tag/08SQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
