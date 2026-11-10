---
declaration: section
origin: cited
lean: Stacks.Norm.MorphismNorm, Stacks.Divisors.exists_isTrivial_restrict_preimage_of_isFinite, Stacks.Divisors.hasNormPullbackPower_normPicardData, Stacks.Divisors.exists_normPicardAddMonoidHom, Stacks.Divisors.normMap, Stacks.Divisors.normMap_generator, Stacks.Divisors.normMap_zeroAt_iff, Stacks.Divisors.exists_isAmple_of_morphismNorm
statement: formalized
proof: formalized
---

# 31.18 Norms

Section 31.18 of the Stacks Project, [Tag 0BCX](https://stacks.math.columbia.edu/tag/0BCX). 11 tags here are carried by 22 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BCX, the section

[Tag 0BCX](https://stacks.math.columbia.edu/tag/0BCX) in the Stacks Project.

**`Stacks.Norm.MorphismNorm`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteLocallyFree/Norm.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteLocallyFree/Norm.lean#L125). The attribute's comment: “norm of degree d”.

> **Stacks Project, Section 0BCX.** A norm of degree `d` for a morphism of schemes: a
> multiplicative map of sheaves preserving pointwise vanishing whose value on a function pulled
> back from the target is its `d`-th power.

```lean
structure MorphismNorm {X Y : Scheme.{u}} (f : X ⟶ Y) (d : ℕ) extends MorphismNormMap f
```

## Tag 0BUT, a lemma

[Tag 0BUT](https://stacks.math.columbia.edu/tag/0BUT) in the Stacks Project.

**`Stacks.Divisors.exists_isTrivial_restrict_preimage_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FiniteTrivialize/TargetCover.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FiniteTrivialize/TargetCover.lean#L188).

> **Stacks Project, Tag 0BUT**, written with `Stacks.SheafOfModules.IsTrivial`: for a finite
> morphism `f : X ⟶ Y`, an invertible `𝒪_X`-module `L` and a point `y` of `Y`, there is an open
> neighbourhood `V` of `y` over which `L` becomes trivial on the inverse image.

```lean
theorem exists_isTrivial_restrict_preimage_of_isFinite {X Y : Scheme.{u}} (f : X ⟶ Y)
    [IsFinite f] (L : X.Modules)
    [IsInvertible X.presheaf (structureSheafRing X.toRingedSpace).property L] (y : Y) :
    ∃ V : Y.Opens, y ∈ V ∧
      IsTrivial (f ⁻¹ᵁ V).toScheme.presheaf
        (structureSheafRing (f ⁻¹ᵁ V).toScheme.toRingedSpace).property
        (L.restrict (f ⁻¹ᵁ V).ι)
```

## Tag 0BCY, a lemma

[Tag 0BCY](https://stacks.math.columbia.edu/tag/0BCY) in the Stacks Project.

**`Stacks.Divisors.hasNormPullbackPower_normPicardData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormInvertible/PullbackPower.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NormInvertible/PullbackPower.lean#L270). The attribute's comment: “the pullback-power formula”.

> **Stacks Project, Tag 0BCY**, the pullback--power clause: the homomorphism of Picard groups
> induced by a norm of degree `d` carries the class of `f^*𝒩` to the class of `𝒩^{⊗ d}`, for every
> invertible `𝒪_Y`-module `𝒩`.
>
> Together with `Stacks.Divisors.exists_normPicardAddMonoidHom`, which is the tag's other clause,
> this completes Tag 0BCY.

```lean
theorem hasNormPullbackPower_normPicardData (g : X ⟶ Y) [IsFinite g] (e : ℕ)
    (M : MorphismNorm g e) :
    HasNormPullbackPower g e (normPicardData g e M).picardMap
```

**`Stacks.Divisors.exists_normPicardAddMonoidHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormInvertible/TensorAdditive.lean, line 335](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NormInvertible/TensorAdditive.lean#L335). The attribute's comment: “the homomorphism of abelian groups”.

> **The norm descends to a homomorphism of Picard groups.**

```lean
theorem exists_normPicardAddMonoidHom (f : X ⟶ Y) [IsFinite f] {d : ℕ}
    (N : MorphismNorm f d) :
    ∃ F : X.picardGroup →+ Y.picardGroup,
      ∀ (L : X.Modules) (hL : IsInvertible X.presheaf (structureSheaf X.sheaf).property L),
        F (picardClass X.presheaf (structureSheaf X.sheaf).property L hL) =
          picardClass Y.presheaf (structureSheaf Y.sheaf).property
            (normInvertible f N.toMorphismNormMap L)
            (isInvertible_normInvertible f N.toMorphismNormMap L
              (hasTrivializingTargetCover_of_isFinite_of_isInvertible f L hL))
```

## Tag 0BCZ, a lemma

[Tag 0BCZ](https://stacks.math.columbia.edu/tag/0BCZ) in the Stacks Project.

**`Stacks.Divisors.normMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormInvertible/Map.lean, line 571](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NormInvertible/Map.lean#L571). The attribute's comment: “the norm map”.

> **The norm of a map of invertible modules.** A norm `N` of degree `d` on functions along a
> finite morphism `f : X ⟶ Y` carries a map `φ : L ⟶ L'` of invertible `𝒪_X`-modules to a map of
> the norms of `L` and `L'`.

```lean
noncomputable def normMap :
    normInvertible f N.toMorphismNormMap L ⟶ normInvertible f N.toMorphismNormMap L'
```

**`Stacks.Divisors.normMap_generator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormInvertible/Map.lean, line 582](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NormInvertible/Map.lean#L582). The attribute's comment: “local generator formula”.

> **In local frames the norm map is multiplication by the norm of the coefficient.** If `φ`
> carries a frame `s` of `L` over `f ⁻¹ᵁ U` to `a` times a frame `t` of `L'` there, then the norm
> of `φ` carries the normed frame of `s` to `N(a)` times the normed frame of `t`. This pins the
> norm map down rather than merely asserting that some map with the right vanishing locus
> exists.

```lean
theorem normMap_generator (U : Y.Opens)
    (s : GeneratorSections X.toRingedSpace L (f ⁻¹ᵁ U))
    (t : GeneratorSections X.toRingedSpace L' (f ⁻¹ᵁ U)) (a : Γ(X, f ⁻¹ᵁ U))
    (ha : φ.val.app (op (f ⁻¹ᵁ U)) s.val =
      @SMul.smul ((structureSheaf X.sheaf).obj.obj (op (f ⁻¹ᵁ U)))
        (L'.val.obj (op (f ⁻¹ᵁ U))) _ a t.val) :
    (normMap f N L L' φ).val.app (op U)
        (normGenerator f N.toMorphismNormMap L
          (hasTrivializingTargetCover_of_isInvertible f L) U s).val =
      @SMul.smul ((structureSheaf Y.sheaf).obj.obj (op U))
        ((normInvertible f N.toMorphismNormMap L').val.obj (op U)) _ (N.app U a)
        (normGenerator f N.toMorphismNormMap L'
          (hasTrivializingTargetCover_of_isInvertible f L') U t).val
```

**`Stacks.Divisors.normMap_zeroAt_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormInvertible/Map.lean, line 603](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NormInvertible/Map.lean#L603). The attribute's comment: “vanishing locus”.

> **The norm map vanishes at `y` exactly when the original map vanishes at some point of the
> fibre over `y`**: the vanishing locus of the norm of `φ` is the image of the vanishing locus
> of `φ`.

```lean
theorem normMap_zeroAt_iff (y : Y) :
    zeroAt (normInvertible f N.toMorphismNormMap L) (normInvertible f N.toMorphismNormMap L')
        (normMap f N L L' φ) y ↔
      ∃ x : X, f x = y ∧ zeroAt L L' φ x
```

## Tag 0BD0, a lemma

[Tag 0BD0](https://stacks.math.columbia.edu/tag/0BD0) in the Stacks Project.

**`Stacks.Divisors.exists_isAmple_of_morphismNorm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormAmple/Basic.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NormAmple/Basic.lean#L95).

> Let `f : X ⟶ Y` be a finite morphism of schemes admitting a norm of degree `d ≥ 1`. If `X`
> has an ample invertible sheaf, then so has `Y`.

```lean
theorem exists_isAmple_of_morphismNorm (f : X ⟶ Y) [IsFinite f] {d : ℕ} (hd : 1 ≤ d)
    (N : MorphismNorm f d) (L : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf
      (structureSheafRing X.toRingedSpace).property L]
    (hL : AlgebraicGeometry.Scheme.Modules.IsAmple X L) :
    ∃ (M : Y.Modules) (hM : AlgebraicGeometry.SheafOfModules.IsInvertible Y.presheaf
        (structureSheafRing Y.toRingedSpace).property M),
      @AlgebraicGeometry.Scheme.Modules.IsAmple Y M hM
```

**`Stacks.Divisors.exists_isAmple_of_hasNormOfDegree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormInvertible/Ample.lean, line 467](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NormInvertible/Ample.lean#L467).

> **Stacks Project, Tag 0BD0.** Let `f : X ⟶ Y` be a finite morphism of schemes carrying a
> norm of positive degree. If `X` has an ample invertible `𝒪_X`-module then so does `Y`: the norm
> of a sufficiently high tensor power of the given one.
>
> Positivity of the degree is used exactly once, to see that `f` is surjective; the rest is
> `Stacks.Divisors.exists_isAmple_of_morphismNormMap`.

```lean
theorem exists_isAmple_of_hasNormOfDegree (f : X ⟶ Y) [IsFinite f] (L : X.Modules)
    [IsInvertibleModule X L] (hL : Stacks.Ample.IsAmple X L) {d : ℕ} (hd : 0 < d)
    (hN : HasNormOfDegree f d) :
    ∃ (M : Y.Modules) (hM : IsInvertibleModule Y M), @Stacks.Ample.IsAmple Y M hM
```

## Tag 0BD1, a lemma

[Tag 0BD1](https://stacks.math.columbia.edu/tag/0BD1) in the Stacks Project.

**`Stacks.Divisors.isQuasiAffine_of_isFinite_of_hasNormOfDegree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Norm/QuasiAffine.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Norm/QuasiAffine.lean#L144).

> **Stacks Project, Tag 0BD1.** The target of a finite morphism carrying a norm of positive
> degree is quasi-affine as soon as its source is.

```lean
theorem isQuasiAffine_of_isFinite_of_hasNormOfDegree (f : X ⟶ Y) [IsFinite f]
    [Scheme.IsQuasiAffine X] {d : ℕ} (hd : 0 < d) (hN : HasNormOfDegree f d) :
    Scheme.IsQuasiAffine Y
```

**`Stacks.Divisors.isQuasiAffine_of_morphismNorm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormQuasiAffine/Basic.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NormQuasiAffine/Basic.lean#L46).

> Let `f : X ⟶ Y` be a finite morphism of schemes admitting a norm of degree `d ≥ 1`. If `X`
> is quasi-affine, then so is `Y`.

```lean
public theorem isQuasiAffine_of_morphismNorm (f : X ⟶ Y) [IsFinite f] {d : ℕ} (hd : 1 ≤ d)
    (N : MorphismNorm f d) [X.IsQuasiAffine] : Y.IsQuasiAffine
```

## Tag 0BD2, a lemma

[Tag 0BD2](https://stacks.math.columbia.edu/tag/0BD2) in the Stacks Project.

**`Stacks.Divisors.finiteLocallyFreeNorm`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Norm/Basic.lean, line 409](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Norm/Basic.lean#L409). The attribute's comment: “the canonical norm”. References: EGA II (6.5.1), “special case”; SGA 3 V (4.1.1), “more general”.

> **Stacks Project, Tag 0BD2.** The canonical determinant norm constructed in the proof,
> for an arbitrary finite locally free morphism, including varying and zero rank.
>
> Its defining property is `finiteLocallyFreeNorm_app_affine_eq_projectiveNorm`: on an affine
> open of the target it is the determinant of multiplication. Taken with the two fields of
> `DeterminantNorm` — the determinant formula on affine opens where the algebra is free, and the
> power law at constant rank — this pins the norm down.

```lean
noncomputable def finiteLocallyFreeNorm {X Y : Scheme.{u}} (f : X ⟶ Y)
    [Morphisms.IsFiniteLocallyFree f] : DeterminantNorm f
```

**`Stacks.Divisors.finiteLocallyFreeNormOfRank`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Norm/Basic.lean, line 454](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Norm/Basic.lean#L454). The attribute's comment: “the norm of positive constant degree”. References: EGA II (6.5.1), “special case”.

> **Stacks Project, Tag 0BD2.** At positive constant rank `d`, the canonical determinant
> norm is a norm of degree `d` in the sense of the Norms section.

```lean
noncomputable def finiteLocallyFreeNormOfRank {X Y : Scheme.{u}} (f : X ⟶ Y) (d : ℕ)
    [Morphisms.IsFiniteLocallyFreeOfRank f d] (_hd : 0 < d) :
    {N : MorphismNorm f d // IsDeterminantNorm N.toMorphismNormMap}
```

**`Stacks.Divisors.finiteLocallyFreeNorm_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormBaseChange/Basic.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NormBaseChange/Basic.lean#L64). The attribute's comment: “compatibility with arbitrary base change”.

> **Stacks Project, Tag 0BD2.** Formation of the canonical determinant norm commutes with
> arbitrary base change, even when the rank is not constant: around a cartesian square the base
> change `f'` of a finite locally free morphism `f` is again finite locally free, and the norm of a
> section of the structure sheaf pulled back around the square is the pullback of its norm.

```lean
theorem finiteLocallyFreeNorm_baseChange
    {X Y X' Y' : Scheme.{u}} (f : X ⟶ Y) (f' : X' ⟶ Y')
    (g' : X' ⟶ X) (g : Y' ⟶ Y)
    [Morphisms.IsFiniteLocallyFree f]
    (sq : IsPullback g' f' f g) :
    ∃ h' : Morphisms.IsFiniteLocallyFree f',
      letI := h'
      ∀ (U : Y.Opens) (s : Γ(X, f ⁻¹ᵁ U)),
        (finiteLocallyFreeNorm f').app (g ⁻¹ᵁ U)
            (g'.appLE (f ⁻¹ᵁ U) (f' ⁻¹ᵁ (g ⁻¹ᵁ U)) (by
              intro x hx
              change f (g' x) ∈ U
              rw [← Scheme.Hom.comp_apply, sq.w, Scheme.Hom.comp_apply]
              exact hx) s) =
          g.app U ((finiteLocallyFreeNorm f).app U s)
```

**`Stacks.Divisors.finiteLocallyFreeNormOfRank_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormBaseChange/Rank.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NormBaseChange/Rank.lean#L58). The attribute's comment: “compatibility of the degree-d norm with arbitrary base change”.

> **Stacks Project, Tag 0BD2.** At positive constant rank, arbitrary base change preserves the
> specified degree and the norm on sections: around a cartesian square the base change `f'` of a
> morphism `f` that is finite locally free of rank `d` is again finite locally free of rank `d`,
> and the degree-`d` norm of a section of the structure sheaf pulled back around the square is the
> pullback of its degree-`d` norm.

```lean
theorem finiteLocallyFreeNormOfRank_baseChange
    {X Y X' Y' : Scheme.{u}} (f : X ⟶ Y) (f' : X' ⟶ Y')
    (g' : X' ⟶ X) (g : Y' ⟶ Y) (d : ℕ)
    [Morphisms.IsFiniteLocallyFreeOfRank f d] (hd : 0 < d)
    (sq : IsPullback g' f' f g) :
    ∃ h' : Morphisms.IsFiniteLocallyFreeOfRank f' d,
      letI := h'
      ∀ (U : Y.Opens) (s : Γ(X, f ⁻¹ᵁ U)),
        (finiteLocallyFreeNormOfRank f' d hd).1.app (g ⁻¹ᵁ U)
            (g'.appLE (f ⁻¹ᵁ U) (f' ⁻¹ᵁ (g ⁻¹ᵁ U)) (by
              intro x hx
              change f (g' x) ∈ U
              rw [← Scheme.Hom.comp_apply, sq.w, Scheme.Hom.comp_apply]
              exact hx) s) =
          g.app U ((finiteLocallyFreeNormOfRank f d hd).1.app U s)
```

## Tag 0BD3, a lemma

[Tag 0BD3](https://stacks.math.columbia.edu/tag/0BD3) in the Stacks Project.

**`Stacks.Divisors.exists_norm_of_finite_surjective_of_normal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Norm/FunctionFieldDegree.lean, line 551](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Norm/FunctionFieldDegree.lean#L551).

> **Stacks Project, Tag 0BD3.** A finite surjective morphism of integral schemes with
> normal target carries a norm of the function-field extension degree.

```lean
theorem exists_norm_of_finite_surjective_of_normal
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsFinite f] [Surjective f]
    [IsIntegral X] [IsIntegral Y] [IsNormal Y] :
    ∃ φ : Y.functionField →+* X.functionField,
      (∀ (U : Y.Opens) [Nonempty U] [Nonempty (f ⁻¹ᵁ U)]
        (s : Γ(Y, U)),
        φ (Y.germToFunctionField U s) =
          X.germToFunctionField (f ⁻¹ᵁ U) (f.app U s)) ∧
      (letI : Algebra Y.functionField X.functionField := φ.toAlgebra
       HasNormOfDegree f (Module.finrank Y.functionField X.functionField))
```

## Tag 0BDZ, a lemma

[Tag 0BDZ](https://stacks.math.columbia.edu/tag/0BDZ) in the Stacks Project.

**`Stacks.Divisors.exists_normOfDegree_reduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Norm/Reduction.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Norm/Reduction.lean#L201).

> **Stacks Project, Tag 0BDZ.** On a Noetherian scheme in prime characteristic `p` a
> sufficiently high Frobenius power supplies a norm of degree a positive power of `p` for the
> canonical morphism from the reduction.

```lean
theorem exists_normOfDegree_reduction (X : Scheme.{u}) [IsNoetherian X]
    (p : ℕ) (hp : p.Prime) (hchar : (p : Γ(X, ⊤)) = 0) :
    ∃ e : ℕ, 0 < e ∧
      HasNormOfDegree (Scheme.IdealSheafData.vanishingIdeal (⊤ : Closeds X)).subschemeι
        (p ^ e)
```

## Tag 0BD4, a proposition

[Tag 0BD4](https://stacks.math.columbia.edu/tag/0BD4) in the Stacks Project.

**`Stacks.Divisors.exists_isAmple_of_isFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormInvertible/Ample.lean, line 482](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NormInvertible/Ample.lean#L482). The attribute's comment: “finite_locally_free_case”. References: EGA II (6.6.1), “absolute, loc free case”; EGA II (6.6.2), “locally free case”.

> **Stacks Project, Tag 0BD4, case (1).** A finite locally free, finite surjective morphism
> descends the existence of an ample invertible module. The canonical determinant norm of
> [Stacks, Tag 0BD2] is available at *varying* rank, and no constant degree is needed: the degree
> is what Tag 0BD0 uses to get surjectivity, and here surjectivity is a hypothesis.

```lean
theorem exists_isAmple_of_isFiniteLocallyFree (f : X ⟶ Y) [IsFinite f] [Surjective f]
    [Morphisms.IsFiniteLocallyFree f] (L : X.Modules) [IsInvertibleModule X L]
    (hL : Stacks.Ample.IsAmple X L) :
    ∃ (M : Y.Modules) (hM : IsInvertibleModule Y M), @Stacks.Ample.IsAmple Y M hM
```

**`Stacks.Divisors.exists_isAmple_of_isAmple_reduction_char_p`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormInvertible/Ample.lean, line 494](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NormInvertible/Ample.lean#L494). The attribute's comment: “reduction_characteristic_p_case”.

> **Stacks Project, Tag 0BD4, case (3).** On a Noetherian scheme of prime characteristic `p`,
> an ample invertible module on the reduction descends to an ample invertible module on the scheme:
> a Frobenius power supplies a norm of degree a positive power of `p` for the canonical morphism
> from the reduction ([Stacks, Tag 0BDZ]).

```lean
theorem exists_isAmple_of_isAmple_reduction_char_p (Y : Scheme.{u}) [IsNoetherian Y] (p : ℕ)
    (hp : p.Prime) (hchar : (p : Γ(Y, ⊤)) = 0)
    (L : (Scheme.IdealSheafData.vanishingIdeal (⊤ : Closeds Y)).subscheme.Modules)
    [IsInvertibleModule (Scheme.IdealSheafData.vanishingIdeal (⊤ : Closeds Y)).subscheme L]
    (hL : Stacks.Ample.IsAmple
      (Scheme.IdealSheafData.vanishingIdeal (⊤ : Closeds Y)).subscheme L) :
    ∃ (M : Y.Modules) (hM : IsInvertibleModule Y M), @Stacks.Ample.IsAmple Y M hM
```

**`Stacks.Divisors.exists_isAmple_of_isIntegral_isNormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NormInvertible/Ample.lean, line 511](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NormInvertible/Ample.lean#L511). The attribute's comment: “integral_normal_case”. References: EGA II (6.6.1), “absolute, Y normal”; EGA II (6.6.2), “Y integral normal”.

> **Stacks Project, Tag 0BD4, case (2).** A finite surjective morphism onto an integral normal
> scheme descends the existence of an ample invertible module. The source is replaced by an
> irreducible component dominating the target, viewed as a reduced closed subscheme; that component
> is integral, so [Stacks, Tag 0BD3] supplies a norm of the function-field degree.

```lean
theorem exists_isAmple_of_isIntegral_isNormal {X Y : Scheme.{u}} (f : X ⟶ Y) [IsFinite f]
    [Surjective f] [IsIntegral Y] [IsNormal Y] (L : X.Modules) [IsInvertibleModule X L]
    (hL : Stacks.Ample.IsAmple X L) :
    ∃ (M : Y.Modules) (hM : IsInvertibleModule Y M), @Stacks.Ample.IsAmple Y M hM
```

## Tag 0BD5, a lemma

[Tag 0BD5](https://stacks.math.columbia.edu/tag/0BD5) in the Stacks Project.

**`Stacks.Divisors.isQuasiAffine_of_isFinite_surjective_of_isNormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Norm/QuasiAffineFiniteSurjective.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Norm/QuasiAffineFiniteSurjective.lean#L132). The attribute's comment: “integral normal target case”.

> **Stacks Project, Tag 0BD5, case (2).** Quasi-affineness descends along a finite surjective
> morphism onto an integral normal scheme.

```lean
theorem isQuasiAffine_of_isFinite_surjective_of_isNormal {X Y : Scheme.{u}} (f : X ⟶ Y)
    [IsFinite f] [Surjective f] [IsIntegral Y] [IsNormal Y] [Scheme.IsQuasiAffine X] :
    Scheme.IsQuasiAffine Y
```

**`Stacks.Divisors.isQuasiAffine_of_isFiniteLocallyFree_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Norm/QuasiAffineFiniteSurjective.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Norm/QuasiAffineFiniteSurjective.lean#L176). The attribute's comment: “finite locally free case”.

> **Stacks Project, Tag 0BD5, case (1).** Quasi-affineness descends along a finite locally
> free surjective morphism.

```lean
theorem isQuasiAffine_of_isFiniteLocallyFree_surjective {X Y : Scheme.{u}} (f : X ⟶ Y)
    [IsFinite f] [Surjective f] [Morphisms.IsFiniteLocallyFree f] [Scheme.IsQuasiAffine X] :
    Scheme.IsQuasiAffine Y
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 31.18, Tag 0BCX](https://stacks.math.columbia.edu/tag/0BCX)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
