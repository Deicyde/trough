---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.RelativeDualizingComplex, AlgebraicGeometry.Space.RelativeDualizingComplex.isIso_smallEtaleDerivedHomothety_and_isLE, AlgebraicGeometry.Space.RelativeDualizingComplex.existsUnique_iso_of_relativeDualizingComplex, AlgebraicGeometry.Space.RelativeDualizingPair.isAffineBaseChangePair_of_isEtaleCovering_of_isProper, AlgebraicGeometry.Space.RelativeDualizingComplex.nonempty, AlgebraicGeometry.Space.RelativeDualizingComplex.baseChange_spec
statement: formalized
proof: formalized
---

# 86.9 Relative dualizing complexes for proper flat morphisms

Section 86.9 of the Stacks Project, [Tag 0E5W](https://stacks.math.columbia.edu/tag/0E5W). 6 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0E5X, a definition

[Tag 0E5X](https://stacks.math.columbia.edu/tag/0E5X) in the Stacks Project.

**`AlgebraicGeometry.Space.RelativeDualizingComplex`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeDualizingComplex.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeDualizingComplex.lean#L189).

> Let `f : X ⟶ Y` be a proper, flat morphism of algebraic spaces over `S` of finite
> presentation. A *relative dualizing complex* for `X/Y` is a pair `(ω, τ)` of a `Y`-perfect object
> `ω` of `D(𝒪_X)` and a map `τ : Rf_* ω ⟶ 𝒪_Y` such that for every cartesian square
> `g' ≫ f = f' ≫ g` with `Y'` an affine scheme, the pair `(L(g')^* ω, Lg^* τ)` is isomorphic to the
> pair `(a'(𝒪_{Y'}), Tr_{f', 𝒪_{Y'}})` of the right adjoint `a'` of `Rf'_*` (Stacks 0E55) and its
> trace map (Stacks 0E5K).

```lean
structure RelativeDualizingComplex {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (_hf : IsProper B S hS f.hom) (hfl : IsFlat B S hS f.hom)
    (hfp : IsFinitePresentation B S hS f.hom) extends RelativeDualizingPair f hfl hfp
```

## Tag 0E5Y, a lemma

[Tag 0E5Y](https://stacks.math.columbia.edu/tag/0E5Y) in the Stacks Project.

**`AlgebraicGeometry.Space.RelativeDualizingComplex.isIso_smallEtaleDerivedHomothety_and_isLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeDualizingComplexAffinePerfect.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeDualizingComplexAffinePerfect.lean#L159).

> **Stacks 0E5Y.** Let `f : X ⟶ Y` be a proper, flat morphism of algebraic spaces of finite
> presentation. For a relative dualizing complex `(ω, τ)`, the map `𝒪_X ⟶ R𝓗om(ω, ω)` is an
> isomorphism and `Rf_* ω` has vanishing cohomology sheaves in positive degrees.

```lean
theorem isIso_smallEtaleDerivedHomothety_and_isLE (ω : RelativeDualizingComplex hZ f hf hfl hfp) :
    IsIso (smallEtaleDerivedHomothety B S hS X ω.ω) ∧
      ((derivedModulePushforward B S hS f).obj ω.ω).IsLE 0
```

## Tag 0E5Z, a lemma

[Tag 0E5Z](https://stacks.math.columbia.edu/tag/0E5Z) in the Stacks Project.

**`AlgebraicGeometry.Space.RelativeDualizingComplex.existsUnique_iso_of_relativeDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeDualizingComplexAffinePerfect.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeDualizingComplexAffinePerfect.lean#L169).

> **Stacks 0E5Z.** Let `f : X ⟶ Y` be a proper, flat morphism of algebraic spaces of finite
> presentation. Two relative dualizing complexes `(ω₁, τ₁)`, `(ω₂, τ₂)` on `X/Y` have a unique
> isomorphism of pairs: a unique `e : ω₁ ≅ ω₂` with `τ₂ ∘ Rf_* e = τ₁`.

```lean
theorem existsUnique_iso_of_relativeDualizingComplex
    (D₁ D₂ : RelativeDualizingComplex hZ f hf hfl hfp) :
    ∃! e : D₁.ω ≅ D₂.ω, (derivedModulePushforward B S hS f).map e.hom ≫ D₂.τ = D₁.τ
```

## Tag 0E60, a lemma

[Tag 0E60](https://stacks.math.columbia.edu/tag/0E60) in the Stacks Project.

**`AlgebraicGeometry.Space.RelativeDualizingPair.isAffineBaseChangePair_of_isEtaleCovering_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeDualizingComplexAffinePerfect.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeDualizingComplexAffinePerfect.lean#L189).

> **Stacks 0E60.** Let `f : X ⟶ Y` be a proper, flat morphism of algebraic spaces of finite
> presentation, `(ω, τ)` a pair of a `Y`-perfect object of `D(𝒪_X)` and a map
> `τ : Rf_* ω ⟶ 𝒪_Y`, and `X_i ⟶ Y_i` the base changes of `f` to the members of an étale covering
> `{Y_i ⟶ Y}` by affines, over which `(ω, τ)` is isomorphic to `(a_i(𝒪_{Y_i}), Tr)`. Then
> `(ω, τ)` is a relative dualizing complex: its base change to every affine `Y'` is isomorphic to
> `(a'(𝒪_{Y'}), Tr)`.

```lean
theorem isAffineBaseChangePair_of_isEtaleCovering_of_isProper
    (P : RelativeDualizingPair f hfl hfp) (hf : IsProper B S hS f.hom)
    {ι : Type v} {Yi Xi : ι → AlgebraicSpaces B S hS} {fi : ∀ i, Xi i ⟶ Yi i}
    {gi : ∀ i, Yi i ⟶ Y} {g'i : ∀ i, Xi i ⟶ X} (sqi : ∀ i, IsPullback (g'i i) (fi i) f (gi i))
    (hYi : ∀ i, IsAffineSpace B S hS (Yi i).1)
    (hcov : IsEtaleCovering B S hS (fun i => (Yi i).1) (fun i => (gi i).hom))
    (hi : ∀ i, IsAffineBaseChangePair hZ (sqi i) hfp (hYi i) P.ω P.τ)
    ⦃X' Y' : AlgebraicSpaces B S hS⦄ (f' : X' ⟶ Y') (g : Y' ⟶ Y) (g' : X' ⟶ X)
    (sq : IsPullback g' f' f g) (hY' : IsAffineSpace B S hS Y'.1) :
    IsAffineBaseChangePair hZ sq hfp hY' P.ω P.τ
```

## Tag 0E61, a lemma

[Tag 0E61](https://stacks.math.columbia.edu/tag/0E61) in the Stacks Project.

**`AlgebraicGeometry.Space.RelativeDualizingComplex.nonempty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeDualizingComplexExistence.lean, line 412](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeDualizingComplexExistence.lean#L412).

> **Stacks 0E61: existence of relative dualizing complexes.** Let `f : X ⟶ Y` be a proper,
> flat morphism of algebraic spaces over `S` which is of finite presentation. Then there exists a
> relative dualizing complex `(ω_{X/Y}, τ)` for `X/Y` (Stacks 0E5X).

```lean
theorem RelativeDualizingComplex.nonempty (hZ : B.Contains (⊤_ Scheme.{u}))
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (hf : IsProper B S hS f.hom)
    (hfl : IsFlat B S hS f.hom) (hfp : IsFinitePresentation B S hS f.hom) :
    Nonempty (RelativeDualizingComplex hZ f hf hfl hfp)
```

## Tag 0E6C, a lemma

[Tag 0E6C](https://stacks.math.columbia.edu/tag/0E6C) in the Stacks Project.

**`AlgebraicGeometry.Space.RelativeDualizingComplex.baseChange_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeDualizingComplexBaseChange.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeDualizingComplexBaseChange.lean#L237).

> **Stacks 0E6C.** Let `g' ≫ f = f' ≫ g` be a cartesian square of algebraic spaces over `S`
> with `f : X ⟶ Y` proper, flat and of finite presentation, and let `(ω, τ)` be a relative
> dualizing complex for `f`. Then `(L(g')^* ω, Lg^* τ)` is a relative dualizing complex for `f'`:
> `L(g')^* ω` is `Y'`-perfect, and the map `τ' : Rf'_* L(g')^* ω ⟶ 𝒪_{Y'}` which is `Lg^* τ`
> through the base change map has the base change property of Stacks 0E5X.

```lean
theorem baseChange_spec :
    IsPerfectRelativeToCanonical.{u, u + 1, u + 1} B S hS f'
        ((isFlat_isStableUnderBaseChange B S hS).of_isPullback sq hfl)
        ((isLocallyOfFinitePresentation_isStableUnderBaseChange B S hS).of_isPullback sq
          hfp.1)
        ((smallEtaleDerivedModulePullback B S hS g').obj D.ω) ∧
      ∃ τ' : (derivedModulePushforward B S hS f').obj
          ((smallEtaleDerivedModulePullback B S hS g').obj D.ω) ⟶
            (derivedStructureSheaf B S hS Y'.1 Y'.2).obj,
        smallEtaleDerivedModuleBaseChangeMap B S hS f g f' g' sq.w D.ω ≫ τ' =
            (smallEtaleDerivedModulePullback B S hS g).map D.τ ≫
              (smallEtaleDerivedModulePullbackUnitIso (B := B) (S := S) (hS := hS) g).hom ∧
          ∀ ⦃X'' Y'' : AlgebraicSpaces B S hS⦄ (f'' : X'' ⟶ Y'') (h : Y'' ⟶ Y')
            (g'' : X'' ⟶ X') (sq₂ : IsPullback g'' f'' f' h) (hY'' : IsAffineSpace B S hS Y''.1),
            IsAffineBaseChangePair hZ sq₂
              ((isFinitePresentation_isStableUnderBaseChange B S hS).of_isPullback sq hfp)
              hY'' ((smallEtaleDerivedModulePullback B S hS g').obj D.ω) τ'
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 86.9, Tag 0E5W](https://stacks.math.columbia.edu/tag/0E5W)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
