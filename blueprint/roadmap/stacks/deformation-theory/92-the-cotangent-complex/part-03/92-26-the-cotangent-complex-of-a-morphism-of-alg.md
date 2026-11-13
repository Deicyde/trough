---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.cotangentComplex, AlgebraicGeometry.Space.cotangentComplexDerived, AlgebraicGeometry.Space.etaleRestrictionCotangentComplexIso, AlgebraicGeometry.Space.quasiIso_representedCotangentComparison, AlgebraicGeometry.Space.representedCotangentComplexDerivedIso, AlgebraicGeometry.RingedToposHom.cotangentComplexOverConstantRingIso, AlgebraicGeometry.Space.cotangentComplexOverConstantSheafIso
statement: formalized
proof: formalized
---

# 92.26 The cotangent complex of a morphism of algebraic spaces

Section 92.26 of the Stacks Project, [Tag 08VC](https://stacks.math.columbia.edu/tag/08VC). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08VD, a definition

[Tag 08VD](https://stacks.math.columbia.edu/tag/08VD) in the Stacks Project.

**`AlgebraicGeometry.Space.cotangentComplex`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Spaces/CotangentComplex.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/Spaces/CotangentComplex.lean#L114).

> **Stacks Project, Tag 08VD.** The cotangent complex `L_{X/Y}` of a morphism `f : X ⟶ Y` of
> algebraic spaces over a scheme `S`: the cotangent complex of the canonical morphism of ringed
> topoi `f_small` between the small étale sites of `X` and `Y`, that is, the cotangent complex of
> the map of sheaves of commutative rings `f_small⁻¹𝒪_Y ⟶ 𝒪_X` on the small étale site of `X`.
>
> It is a complex of modules over `𝒪_X`, so it depends on `X` alone.

```lean
noncomputable abbrev cotangentComplex (f : X ⟶ Y) :
    CochainComplex (smallEtaleModulesULift B S hS X) ℤ
```

**`AlgebraicGeometry.Space.cotangentComplexDerived`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Spaces/CotangentComplex.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/Spaces/CotangentComplex.lean#L123). The attribute's comment: “the derived object”.

> **Stacks Project, Tag 08VD.** The cotangent complex `L_{X/Y}` regarded as an object of the
> derived category `D(𝒪_X)`.

```lean
noncomputable abbrev cotangentComplexDerived (f : X ⟶ Y)
    [HasDerivedCategory.{t} (smallEtaleModulesULift B S hS X)] :
    DerivedCategory (smallEtaleModulesULift B S hS X)
```

## Tag 08VE, a lemma

[Tag 08VE](https://stacks.math.columbia.edu/tag/08VE) in the Stacks Project.

**`AlgebraicGeometry.Space.etaleRestrictionCotangentComplexIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Spaces/EtaleRestriction.lean, line 395](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/Spaces/EtaleRestriction.lean#L395).

> For a commutative diagram of algebraic spaces over a scheme `S`
>
> ```
> U --g--> V
> |p       |q
> X --f--> Y
> ```
>
> with `p` and `q` étale, the restriction of the cotangent complex `L_{X/Y}` to the small étale
> site of `U` is the cotangent complex `L_{U/V}`:
>
> `L_{X/Y}|_{U_étale} = L_{U/V}`.
>
> Formation of the cotangent complex commutes with inverse image (Stacks 08SV), and the structure
> maps of `f` and of `g` are carried to one another by the comparisons of Stacks 03LV and
> Stacks 03G8, which commute by `AlgebraicGeometry.Space.etaleRestrictionCotangentSquare`; square
> functoriality of the cotangent complex then transports the complex.

```lean
noncomputable def etaleRestrictionCotangentComplexIso {p : U ⟶ X} {f : X ⟶ Y} {g : U ⟶ V}
    {q : V ⟶ Y} (hp : IsEtale B S hS p.hom) (hq : IsEtale B S hS q.hom) (h : p ≫ f = g ≫ q) :
    ((etaleRestrictModules B S hS p hp).mapHomologicalComplex (ComplexShape.up ℤ)).obj
        (cotangentComplex B S hS f) ≅
      cotangentComplex B S hS g
```

## Tag 08VF, a lemma

[Tag 08VF](https://stacks.math.columbia.edu/tag/08VF) in the Stacks Project.

**`AlgebraicGeometry.Space.quasiIso_representedCotangentComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Spaces/RepresentableComparison.lean, line 303](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/Spaces/RepresentableComparison.lean#L303). The attribute's comment: “the canonical map `ε^*L_{X₀/Y₀} ⟶ L_{X/Y}` is a quasi-isomorphism, for the morphism of algebraic spaces represented by a morphism `T₁ ⟶ T₂` of the big fppf site over `S` (so `X` and `Y` are represented by the schemes `X₀`, `Y₀` underlying `T₁`, `T₂`); `ε` is the comparison of Section 071P (`representedToZariskiRingedToposHom`), `L_{X₀/Y₀}` the cotangent complex of Definition 08T2 lifted to the universe of the small étale site, `ε^*` the degreewise pullback of sheaves of modules along `ε`. The map is `representedCotangentComparison`; its transpose is the functoriality of the cotangent complex over the square of Remark 08GH (`towerCotangentUnit_comp_representedBaseChangedComparison`)”.

> **Stacks 08VF.** Let `f : X ⟶ Y` be the morphism of algebraic spaces over `S` represented by
> a morphism `T₁ ⟶ T₂` of the big fppf site, so that `X` and `Y` are representable by the schemes
> `X₀` and `Y₀` underlying `T₁` and `T₂`. Then the canonical map `ε^*L_{X₀/Y₀} ⟶ L_{X/Y}`
> (`AlgebraicGeometry.Space.representedCotangentComparison`) is a quasi-isomorphism.
>
> The source's proof checks this on stalks at geometric points; here the map is factored through
> the two canonical arrows of the fundamental triangles of Stacks 08SZ, and the two vertices that
> must vanish, `L_{𝒪_X/ε⁻¹𝒪_{X₀}}` and `L_{f_small⁻¹𝒪_Y/ε⁻¹f₀⁻¹𝒪_{Y₀}} ⊗ 𝒪_X`, vanish because
> their stalks at the geometric points are the cotangent complexes of the strict henselizations
> `𝒪_{X₀,x} ⟶ 𝒪_{X,x̄}` and `𝒪_{Y₀,y} ⟶ 𝒪_{Y,ȳ}` (Stacks 04K5, 08T0, 05V1, 04KF, 08R2); this is the
> content of Lemma 08UN that the source invokes.

```lean
theorem quasiIso_representedCotangentComparison :
    QuasiIso (representedCotangentComparison B S hS h)
```

**`AlgebraicGeometry.Space.representedCotangentComplexDerivedIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Spaces/RepresentableComparison.lean, line 323](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/Spaces/RepresentableComparison.lean#L323). The attribute's comment: “the canonical identification `ε^*L_{X₀/Y₀} ≅ L_{X/Y}` in `D(𝒪_X)`, for the morphism of algebraic spaces represented by a morphism `T₁ ⟶ T₂` of the big fppf site over `S`, as the image in the derived category of the canonical map `representedCotangentComparison`; any derived category of `Mod(𝒪_X)` may be used”.

> **Stacks 08VF.** The canonical identification `L_{X/Y} = ε^*L_{X₀/Y₀}` in `D(𝒪_X)`, for the
> morphism `f : X ⟶ Y` of algebraic spaces represented by a morphism `T₁ ⟶ T₂` of the big fppf
> site over `S`: the image in the derived category of the canonical map
> `AlgebraicGeometry.Space.representedCotangentComparison`, which is a quasi-isomorphism
> (`AlgebraicGeometry.Space.quasiIso_representedCotangentComparison`).

```lean
noncomputable def representedCotangentComplexDerivedIso
    [HasDerivedCategory.{t}
      (smallEtaleModulesULift B S hS ⟨yoneda.obj T₁, isAlgebraicSpace_yoneda B S hS T₁⟩)] :
    DerivedCategory.Q.obj (representedPulledBackCotangentComplex B S hS h) ≅
      cotangentComplexDerived B S hS (representedSpaceMap B S hS h)
```

## Tag 08VG, a lemma

[Tag 08VG](https://stacks.math.columbia.edu/tag/08VG) in the Stacks Project.

**`AlgebraicGeometry.RingedToposHom.cotangentComplexOverConstantRingIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/ConstantBaseRing.lean, line 255](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/ConstantBaseRing.lean#L255). The attribute's comment: “an isomorphism in `D(𝒪_X)` rather than an equality of complexes, as the source's own proof produces. `L_{X/Spec(Λ)}` is the cotangent complex of the morphism of ringed topoi (Tag 08SU) and `L_{𝒪_X/Λ̲}` is the cotangent complex of `Λ̲ ⟶ 𝒪_X` with `Λ̲` the constant sheaf of Mathlib's `constantSheaf`, so no identification of `Λ̲` with an iterated inverse image is used. TWO carried hypotheses, both inputs of the source's argument and neither the conclusion: (1) the short exact sequence `S`, `hS`, `e₁`, `e₂`, `e₃` giving the fundamental triangle of Tag 08SZ for the tower `Λ̲ ⟶ G⁻¹𝒪_Y ⟶ 𝒪_X`, carried in the same shape and for the same reason as in Tag 08V1 (the sheaf-level analogue of Tag 08SD is absent here); (2) `hv`, the acyclicity of the FIRST vertex `L_{G⁻¹𝒪_Y/Λ̲} ⊗ 𝒪_X`, which is the source's `L_q = 0` for `q : Spec(Λ)_étale ⟶ (*, Λ)` pulled back to `X` — `firstVertexOverInverseImageBaseIso` proves that a first vertex over an inverse-image base is `G^*G⁻¹L_{𝒪_Y/Λ_Y}` — and which the source obtains from Tags 04K5, 08T0, 04KF and 08R2, none of which this library has in a form applying to acyclicity of a complex of sheaves of modules on a site. The conclusion's two objects do not occur in either hypothesis. What is proved: the passage from the short exact sequence to a distinguished triangle, the identification of the first vertex over an inverse-image base through Tag 08SV, and the degeneration of the triangle. The first vertex carries the DEGREEWISE extension of scalars, as in Tag 08V1”.

> **Stacks 08VG.** Let `Λ` be a commutative ring and let `X` be a space over `Λ`, with
> structure morphism `G : X ⟶ Y` of ringed topoi and with `b : Λ̲ ⟶ G⁻¹𝒪_Y` the `Λ`-algebra
> structure of its base, `Λ̲` being the constant sheaf with value `Λ` on the site of `X`. Then
>
> `L_{X/Y} ≅ L_{𝒪_X/Λ̲}`
>
> in `D(𝒪_X)`: the cotangent complex of the morphism agrees with the cotangent complex of the
> homomorphism of sheaves of rings `Λ̲ ⟶ 𝒪_X`.
>
> Two hypotheses are carried, both inputs of the source's proof: the fundamental triangle of the
> tower `Λ̲ ⟶ G⁻¹𝒪_Y ⟶ 𝒪_X`, in the shape Tag 08V1 carries it, and the acyclicity `hv` of its
> first vertex, which is the source's `L_q = 0` pulled back to `X` by
> `firstVertexOverInverseImageBaseIso`. See the module documentation.

```lean
def cotangentComplexOverConstantRingIso
    (b : X.constantRing Λ ⟶ G.toToposHom.inverseImageRing.obj Y.O)
    (S : ShortComplex (CochainComplex (Sheaf.targetModules.{u, v, w} X.J X.O) ℤ))
    (hS : S.ShortExact)
    (e₁ : S.X₁ ≅ firstVertexOverBase G b)
    (e₂ : S.X₂ ≅ cotangentComplexOverBase G b)
    (e₃ : S.X₃ ≅ G.cotangentComplex)
    (hv : IsZero (DerivedCategory.Q.obj (firstVertexOverBase G b))) :
    G.cotangentComplexDerived ≅ DerivedCategory.Q.obj (cotangentComplexOverBase G b)
```

**`AlgebraicGeometry.Space.cotangentComplexOverConstantSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Spaces/ConstantBaseRing.lean, line 759](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/Spaces/ConstantBaseRing.lean#L759). The attribute's comment: “an isomorphism in `D(𝒪_X)`, as the source's proof produces. `Λ̲` is Mathlib's `constantSheaf` with value `Λ` on `X_et`, and `Λ̲ ⟶ 𝒪_X` is the canonical map, adjoint to the structure map `Λ → Γ(X, 𝒪_X)`, global sections being taken at the terminal object of the spaces-étale site of `X` (Stacks 03G1). Both cotangent complexes are formed after lifting sections to universe `u + 1` (`SheafOfModules.sheafULift`), the universe in which Tag 08VD defines `L_{X/Spec Λ}`.”.

> Let `Λ` be a ring and `X` an algebraic space over `Λ`, with structure morphism
> `p : X ⟶ Spec Λ`. Let `Λ̲` be the constant sheaf with value `Λ` on `X_et` and `Λ̲ ⟶ 𝒪_X` its
> canonical map, the one adjoint to the structure map `Λ → Γ(X, 𝒪_X)`
> (`AlgebraicGeometry.Space.constantStructureMapOfSpace`). Then the cotangent complex of
> `Λ̲ ⟶ 𝒪_X` is isomorphic in `D(𝒪_X)` to the cotangent complex `L_{X/Spec Λ}` of Tag 08VD.
>
> The tower `Λ̲ ⟶ p⁻¹𝒪_{Spec Λ} ⟶ 𝒪_X` composes to the canonical map
> (`AlgebraicGeometry.Space.towerConstantLower_comp_towerUpper`); its fundamental triangle
> (Tag 08SZ) has first vertex `L_{p⁻¹𝒪/Λ̲} ⊗ 𝒪_X`, which vanishes stalkwise: at a geometric point
> its stalk is the base change of the cotangent complex of the germ map
> `Λ → 𝒪_{Spec Λ, p(x̄)}`, a strict henselization of a localization of `Λ` (Tags 04KF, 08R2).

```lean
def cotangentComplexOverConstantSheafIso
    [HasDerivedCategory.{t} (smallEtaleModulesULift B (Spec (CommRingCat.of Λ)) hS X)] :
    DerivedCategory.Q.obj (CategoryTheory.Sheaf.cotangentComplex.{u + 1, u, u}
        (smallEtaleRingedTopos B (Spec (CommRingCat.of Λ)) hS X).J
        ((SheafOfModules.sheafULift.{u, u + 1, u}
          (smallEtaleRingedTopos B (Spec (CommRingCat.of Λ)) hS X).J).map
          (constantStructureMapOfSpace Λ B hS X))) ≅
      cotangentComplexDerived B (Spec (CommRingCat.of Λ)) hS (structureToSpec Λ B hS X)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 92.26, Tag 08VC](https://stacks.math.columbia.edu/tag/08VC)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
