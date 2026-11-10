---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_iso_algebraPullback_integralClosureSheaf_unconditional, AlgebraicGeometry.Space.IsRelativeNormalization.existsUnique_iso_baseChange_of_isSmooth, AlgebraicGeometry.Space.existsUnique_iso_normalizationInQcqs_baseChange_of_isSmooth, AlgebraicGeometry.Space.IsRelativeNormalization.existsUnique_baseChangeComparison
statement: formalized
proof: formalized
---

# 76.25 Normalization revisited

Section 76.25 of the Stacks Project, [Tag 082D](https://stacks.math.columbia.edu/tag/082D). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 082E, a lemma

[Tag 082E](https://stacks.math.columbia.edu/tag/082E) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_iso_algebraPullback_integralClosureSheaf_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralClosureSmoothPullbackUnconditional.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/IntegralClosureSmoothPullbackUnconditional.lean#L243). References: SGA 3 X (8.9), “partial”.

> **Stacks 082E.** Let `f : Y ⟶ X` be a smooth morphism of algebraic spaces over `S` and let
> `A` be a quasi-coherent sheaf of commutative `𝒪_X`-algebras. The integral closure of `𝒪_Y` in
> `f^*A` is `f^*A'`, where `A' ⊆ A` is the integral closure of `𝒪_X` in `A`: there is an
> isomorphism `f^*A' ≅ (f^*A)'` of algebra sheaves on `Y` whose composite with the inclusion of
> `(f^*A)'` into `f^*A` is the pullback of the inclusion of `A'` into `A`.

```lean
theorem exists_iso_algebraPullback_integralClosureSheaf_unconditional (f : Y ⟶ X)
    (hf : IsSmooth B S hS f.hom)
    (A : AlgebraSheaf.{u, u} B S hS X.1 X.2) (hA : A.IsQuasicoherent) :
    ∃ e : (algebraPullback B S hS f).obj (AlgebraSheaf.integralClosureSheaf A) ≅
        AlgebraSheaf.integralClosureSheaf ((algebraPullback B S hS f).obj A),
      e.hom ≫ AlgebraSheaf.integralClosureInclusion ((algebraPullback B S hS f).obj A) =
        (algebraPullback B S hS f).map (AlgebraSheaf.integralClosureInclusion A)
```

## Tag 082F, a lemma

[Tag 082F](https://stacks.math.columbia.edu/tag/082F) in the Stacks Project.

**`AlgebraicGeometry.Space.IsRelativeNormalization.existsUnique_iso_baseChange_of_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInSmoothBaseChange.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInSmoothBaseChange.lean#L174). The attribute's comment: “X₂' ≅ X₂ ×_{X₁} X₁' for f qcqs and φ smooth, for normalizations given by the universal property of Tag 0823”.

> **Stacks 082F.**  Let `Y₂ = X₂ ×_{X₁} Y₁` be a fibre square of algebraic spaces over `S`
> with `f : Y₁ ⟶ X₁` quasi-compact and quasi-separated and `φ : X₂ ⟶ X₁` smooth, and let
> `Yᵢ ⟶ Xᵢ' ⟶ Xᵢ` be the normalization of `Xᵢ` in `Yᵢ` (Stacks 0823).  Then `X₂' ≅ X₂ ×_{X₁} X₁'`,
> by a unique isomorphism compatible with the two factorizations of `f₂` and with the two
> morphisms to `X₂`.

```lean
theorem existsUnique_iso_baseChange_of_isSmooth
    (hnorm₁ : IsRelativeNormalization B S hS f ν₁ f₁')
    (hnorm₂ : IsRelativeNormalization B S hS f₂ ν₂ f₂')
    (hX₁ : IsAlgebraicSpace B S hS X₁) (hX₂ : IsAlgebraicSpace B S hS X₂)
    (hY₁ : IsAlgebraicSpace B S hS Y₁) (hX₁' : IsAlgebraicSpace B S hS X₁')
    (hX₂' : IsAlgebraicSpace B S hS X₂')
    (hfqc : IsQuasiCompact B S hS f) (hfqs : IsQuasiSeparated B S hS f)
    (hφ : IsSmooth B S hS φ)
    (sq : IsPullback g f₂ f φ) (sqP : IsPullback p q φ ν₁) :
    ∃! e : X₂' ≅ P, f₂' ≫ e.hom = hnorm₁.baseChangeFactorization sq sqP ∧ e.hom ≫ p = ν₂
```

**`AlgebraicGeometry.Space.existsUnique_iso_normalizationInQcqs_baseChange_of_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInSmoothBaseChange.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInSmoothBaseChange.lean#L203). The attribute's comment: “X₂' ≅ X₂ ×_{X₁} X₁' for f qcqs and φ smooth, for the normalizations of Tag 0822”.

> **Stacks 082F, for the normalizations of Stacks 0822.**  Let `Y₂ = X₂ ×_{X₁} Y₁` be a fibre
> square of algebraic spaces over `S` with `f : Y₁ ⟶ X₁` quasi-compact and quasi-separated and
> `φ : X₂ ⟶ X₁` smooth, and let `P = X₂ ×_{X₁} X₁'` for `X₁'` the normalization of `X₁` in `Y₁`,
> with `f₂P : Y₂ ⟶ P` the base change of `Y₁ ⟶ X₁'`.  Then `f₂ : Y₂ ⟶ X₂` is quasi-compact and
> quasi-separated, and the normalization `X₂'` of `X₂` in `Y₂` is isomorphic to `P` by a unique
> isomorphism compatible with the two factorizations of `f₂` and the two morphisms to `X₂`.

```lean
theorem existsUnique_iso_normalizationInQcqs_baseChange_of_isSmooth (f : Y₁ ⟶ X₁)
    (hfqc : IsQuasiCompact B S hS f.hom) (hfqs : IsQuasiSeparated B S hS f.hom)
    {φ : X₂ ⟶ X₁} (hφ : IsSmooth B S hS φ.hom) {g : Y₂ ⟶ Y₁} {f₂ : Y₂ ⟶ X₂}
    (sq : IsPullback g f₂ f φ) {p : P ⟶ X₂} {q : P ⟶ normalizationInQcqs B S hS f hfqc hfqs}
    (sqP : IsPullback p q φ (normalizationInQcqsHom B S hS f hfqc hfqs)) {f₂P : Y₂ ⟶ P}
    (h₁ : f₂P ≫ q = g ≫ toNormalizationInQcqs f hfqc hfqs) (h₂ : f₂P ≫ p = f₂) :
    ∃ (hqc₂ : IsQuasiCompact B S hS f₂.hom) (hqs₂ : IsQuasiSeparated B S hS f₂.hom),
      ∃! e : (normalizationInQcqs B S hS f₂ hqc₂ hqs₂).1 ≅ P.1,
        (toNormalizationInQcqs f₂ hqc₂ hqs₂).hom ≫ e.hom = f₂P.hom ∧
          e.hom ≫ p.hom = (normalizationInQcqsHom B S hS f₂ hqc₂ hqs₂).hom
```

**`AlgebraicGeometry.Space.IsRelativeNormalization.existsUnique_baseChangeComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationSmoothBaseChange.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationSmoothBaseChange.lean#L166). The attribute's comment: “the morphism h of the proof: the base change X₂ ×_{X₁} X₁' ⟶ X₂ is integral and f₂ factors through it, so the universal property of Tag 0823 supplies a unique h”.

> **Stacks 082F, the morphism `h`.**  The base change `X₂ ×_{X₁} X₁' ⟶ X₂` is an integral
> morphism through which `f₂` factors, so the universal property of the normalization `X₂'` of
> `X₂` in `Y₂` supplies a unique morphism `h : X₂' ⟶ X₂ ×_{X₁} X₁'` compatible with the two
> factorizations of `f₂` and with the two morphisms to `X₂`.

```lean
theorem existsUnique_baseChangeComparison
    (hnorm₁ : IsRelativeNormalization B S hS f ν₁ f₁')
    (hnorm₂ : IsRelativeNormalization B S hS f₂ ν₂ f₂')
    (hX₁ : IsAlgebraicSpace B S hS X₁) (hX₂ : IsAlgebraicSpace B S hS X₂)
    (hX₁' : IsAlgebraicSpace B S hS X₁')
    (sq : IsPullback g f₂ f φ) (sqP : IsPullback p q φ ν₁) :
    ∃! h : X₂' ⟶ P, f₂' ≫ h = hnorm₁.baseChangeFactorization sq sqP ∧ h ≫ p = ν₂
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.25, Tag 082D](https://stacks.math.columbia.edu/tag/082D)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
