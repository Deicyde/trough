---
declaration: section
origin: cited
lean: Stacks.DeRham.isIso_coordinateFormsRestrictionHomology, Stacks.DeRham.isIso_homology_coordinateBlowupFormsDerivedComparison, Stacks.DeRham.isIso_coordinateBlowupFormsDirectImage_of_one, Stacks.DeRham.isIso_coordinateBundleFormsDirectImage_of_one, Stacks.DeRham.isIso_coordinateBlowupFormsDirectImage, Stacks.DeRham.isIso_coordinateBundleFormsDirectImage_zero, Stacks.DeRham.isIso_coordinateBundleFormsDirectImage, Stacks.DeRham.CoordinateCone.isIso_coneBundleFormsDirectImage
statement: formalized
proof: formalized
---

# 50.16 Calculations

Section 50.16 of the Stacks Project, [Tag 0FUB](https://stacks.math.columbia.edu/tag/0FUB). 3 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FUR, a lemma

[Tag 0FUR](https://stacks.math.columbia.edu/tag/0FUR) in the Stacks Project.

**`Stacks.DeRham.isIso_coordinateFormsRestrictionHomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/CoordinateBlowupFormsDerivedComparison.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/CoordinateBlowupFormsDerivedComparison.lean#L72). The attribute's comment: “clause (3), in the setting of Section 0FUB, which fixes a ring R and sets S = Spec(R), Z = A^m\_S ⊂ X = A^\{m+n}\_S with n ≥ 1”.

> **[Stacks, Tag 0FUR], clause (3).** For `n ≥ 1`, every `a ≥ 0` and every `q ≥ 1`, the map
> `H^q(Rb_*Ω^a_{L/S}) ⟶ H^q(Rb_*j_*Ω^a_{E/S})` induced by restricting forms to the exceptional
> divisor is an isomorphism; `Rb_*j_*Ω^a_{E/S} = i_*Rp_*Ω^a_{E/S}`, see
> `Stacks.DeRham.isIso_homology_coordinateBlowupFormsDerivedComparison` for the comparison map
> itself.

```lean
theorem isIso_coordinateFormsRestrictionHomology (hn : 1 ≤ n) (a : ℕ) (q : ℤ) (hq : 1 ≤ q) :
    IsIso (formsRestrictionHomology (coordinateBlowupToAmbient R m n) (coordinateExceptionalι R m n)
      (coordinateBlowupToAmbient R m n ≫ coordinateAmbientToBase R m n) a q)
```

**`Stacks.DeRham.isIso_homology_coordinateBlowupFormsDerivedComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/CoordinateBlowupFormsDerivedComparison.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/CoordinateBlowupFormsDerivedComparison.lean#L85). The attribute's comment: “clause (3), for the comparison map Rb\_*Ω^a ⟶ i\_*Rp\_*Ω^a, in the setting of Section 0FUB, which fixes a ring R and sets S = Spec(R), Z = A^m\_S ⊂ X = A^\{m+n}\_S with n ≥ 1”.

> **[Stacks, Tag 0FUR], clause (3), for the comparison map** `Rb_*Ω^a_{L/S} ⟶ i_*Rp_*Ω^a_{E/S}`
> (`Stacks.DeRham.blowupFormsDerivedComparison` of the coordinate closed immersion
> `i : Z = 𝐀^m_S ⟶ X`): for `n ≥ 1`, every `a ≥ 0` and every `q ≥ 1` it is an isomorphism on
> `H^q`.

```lean
theorem isIso_homology_coordinateBlowupFormsDerivedComparison (hn : 1 ≤ n) (a : ℕ) (q : ℤ)
    (hq : 1 ≤ q) :
    IsIso ((DerivedCategory.homologyFunctor _ q).map
      (blowupFormsDerivedComparison (coordinateAmbientToBase R m n)
        (Stacks.MoreMorphisms.coordinateEmbedding R m n) (a : ℤ)))
```

**`Stacks.DeRham.isIso_coordinateBlowupFormsDirectImage_of_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/CoordinateBlowupFormsDirectImage.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/CoordinateBlowupFormsDirectImage.lean#L252). The attribute's comment: “clause (1) for n = 1, in every degree a ≥ 0; n > 1 is not proved”.

> **[Stacks, Tag 0FUR], clause (1), in the case `n = 1`.** The canonical map
> `Ω^a_{X/S} ⟶ b_*Ω^a_{L/S}` is an isomorphism in every degree `a ≥ 0`, because for `n = 1` the
> centre of the blowup is an effective Cartier divisor and so `b` is an isomorphism. This is the
> case the source's own proof of clause (1) disposes of first.

```lean
theorem isIso_coordinateBlowupFormsDirectImage_of_one (a : ℕ) :
    IsIso (coordinateBlowupFormsDirectImage R m 1 a)
```

**`Stacks.DeRham.isIso_coordinateBundleFormsDirectImage_of_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/CoordinateBlowupFormsDirectImage.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/CoordinateBlowupFormsDirectImage.lean#L264). The attribute's comment: “clause (2) for n = 1, in every degree a ≥ 0; at general n only the single degree a = 0 is proved, by Stacks.DeRham.isIso\_coordinateBundleFormsDirectImage\_zero in StacksFrontier.AlgebraicGeometry.DeRham.CoordinateBundleFormsDegreeZero; the degrees a > 0 at general n are not proved”.

> **[Stacks, Tag 0FUR], clause (2), in the case `n = 1`.** The canonical map
> `Ω^a_{Z/S} ⟶ p_*Ω^a_{P/S}` is an isomorphism in every degree `a ≥ 0`, because for `n = 1` the
> projective bundle `P = 𝐏⁰_Z` is the centre itself.

```lean
theorem isIso_coordinateBundleFormsDirectImage_of_one (a : ℕ) :
    IsIso (coordinateBundleFormsDirectImage R m 1 a)
```

**`Stacks.DeRham.isIso_coordinateBlowupFormsDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/CoordinateBlowupFormsExtension.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/CoordinateBlowupFormsExtension.lean#L168). The attribute's comment: “clause (1), in the setting of Section 0FUB, which fixes a ring R and sets S = Spec(R), Z = A^m\_S ⊂ X = A^\{m+n}\_S with n ≥ 1”.

> **[Stacks, Tag 0FUR], clause (1).** For every ring `R`, every `m`, every `n ≥ 1` and every
> degree `a ≥ 0`, the canonical map `Ω^a_{X/S} ⟶ b_*Ω^a_{L/S}` is an isomorphism, where
> `X = 𝐀^{m+n}_S`, `S = Spec R`, and `b : L ⟶ X` is the blowup of `X` along `Z = 𝐀^m_S`. For `n = 1`
> the blowup is an isomorphism (`Stacks.DeRham.isIso_coordinateBlowupFormsDirectImage_of_one`); for
> `n ≥ 2` both sides are quasi-coherent on the affine `X`, so it suffices that the map be bijective
> on global sections, which is `Stacks.DeRham.bijective_coordinateBlowupFormsDirectImage_appTop`.

```lean
theorem isIso_coordinateBlowupFormsDirectImage (m n : ℕ) (hn : 1 ≤ n) (a : ℕ) :
    IsIso (coordinateBlowupFormsDirectImage R m n a)
```

**`Stacks.DeRham.isIso_coordinateBundleFormsDirectImage_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/CoordinateBundleFormsDegreeZero.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/CoordinateBundleFormsDegreeZero.lean#L210). The attribute's comment: “clause (2) in the single degree a = 0, at general n: the canonical map Ω^0\_\{Z/S} ⟶ p\_*Ω^0\_\{P/S} is an isomorphism for every n, with no restriction on n; the degrees a > 0 of clause (2) at n > 1, clause (1) at n > 1, and clause (3) in any case, are not proved here”.

> **[Stacks, Tag 0FUR], clause (2), in degree `a = 0`, for every `n`.** The canonical map
> `Ω^0_{Z/S} ⟶ p_*Ω^0_{P/S}` is an isomorphism, with no restriction on `n`.
>
> In degree zero both sides are structure sheaves: the comparison map is, after conjugation by the
> degree-zero identifications, the canonical map `𝒪_Z ⟶ p_*𝒪_P`
> (`AlgebraicGeometry.Scheme.Hom.formsDirectImageComparison_zero`), and that map is an isomorphism
> because the direct image of the structure sheaf of projective space over any base is the
> structure sheaf of the base, which is the degree-zero row of [Stacks, Tag 01XW] at the zeroth
> twist. This is the `s = 0` summand that the source's own proof of clause (2) is left with after
> the projection formula kills the others; what is avoided here is the decomposition of the forms
> of a product, at the cost of reaching only degree `0`.

```lean
theorem isIso_coordinateBundleFormsDirectImage_zero :
    IsIso (coordinateBundleFormsDirectImage R m n 0)
```

**`Stacks.DeRham.isIso_coordinateBundleFormsDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/CoordinateBundleFormsPushforward.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/CoordinateBundleFormsPushforward.lean#L273). The attribute's comment: “clause (2), in the setting of Section 0FUB, which fixes a ring R and sets S = Spec(R), Z = A^m\_S ⊂ X = A^\{m+n}\_S with n ≥ 1”.

> **[Stacks, Tag 0FUR], clause (2).** For every ring `R`, all `m, n` and every degree
> `a ≥ 0`, the canonical map `Ω^a_{Z/S} ⟶ p_*Ω^a_{P/S}` is an isomorphism, where `Z = 𝐀^m_S`,
> `S = Spec R`, and `p : P = 𝐏^{n-1}_Z ⟶ Z`. For `n ≤ 1` the bundle is the centre itself
> (`Stacks.DeRham.isIso_coordinateBundleFormsDirectImage_of_one`; with truncated subtraction `n = 0`
> gives the same bundle as `n = 1`), and `n ≥ 2` is
> `Stacks.DeRham.isIso_coordinateBundleFormsDirectImage_add_two`.

```lean
theorem isIso_coordinateBundleFormsDirectImage (a : ℕ) :
    IsIso (coordinateBundleFormsDirectImage R m n a)
```

**`Stacks.DeRham.CoordinateCone.isIso_coneBundleFormsDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/CoordinateConeFormsDirectImage.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/CoordinateConeFormsDirectImage.lean#L272). The attribute's comment: “clause (2): Ω^a\_\{Z/S} ⟶ p\_*Ω^a\_\{P/S} is an isomorphism, every a ≥ 0, every n ≥ 1, for P = Proj(A) and Z = Spec(A₀) as in Section 50.16”.

> **[Stacks, Tag 0FUR], clause (2).** In the standard situation of Section 50.16 — a ring `R`,
> `S = Spec R`, `m ≥ 0`, `n ≥ 1`, `A = R[x₁, …, x_m, y₁, …, y_n]` graded by `deg xᵢ = 0`,
> `deg yⱼ = 1`, the centre `Z = Spec(A₀) = 𝐀^m_S` and the projective bundle
> `P = Proj(A) = 𝐏^{n-1}_Z` with its projection `p : P ⟶ Z` — the canonical map
> `Ω^a_{Z/S} ⟶ p_*Ω^a_{P/S}` is an isomorphism for every `a ≥ 0`.
>
> Both sides are quasi-coherent on the affine `Z`, and on global sections the map is bijective by
> `bijective_coneBundleFormsPullback_top`: the cone `L = Proj(⨁_d A_{≥ d})` over `P` is the blowup
> of `X = Spec A` along `Z`, a form on `P` is the restriction along the zero section of its pullback
> to `L`, and by clause (1) that pullback comes from `X`.

```lean
theorem isIso_coneBundleFormsDirectImage (hn : 1 ≤ n) (a : ℕ) :
    IsIso (formsDirectImageComparison (coneBundleToCentre R m n) (coneCentreToBase R m n)
      (a : ℤ))
```

**`Stacks.DeRham.CoordinateCone.isIso_homology_coneFormsDerivedComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/CoordinateConeFormsKernelCech.lean, line 361](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/CoordinateConeFormsKernelCech.lean#L361). The attribute's comment: “clause (3): Rb\_*Ω^a\_\{L/S} ⟶ i\_*Rp\_*Ω^a\_\{P/S} is an isomorphism on cohomology sheaves in every degree q ≥ 1, every a ≥ 0, every n ≥ 1, for the blowup L of X = Spec(A) along Z = Spec(A₀) as in Section 50.16”.

> **Clause (3) of [Stacks, Tag 0FUR].** In the standard situation of Section 50.16 — `X = Spec A`
> for `A = R[x₁, …, x_m, y₁, …, y_n]`, `Z = Spec A₀ = V(y₁, …, y_n)`, `b : L ⟶ X` the blowing up of
> `X` along `Z` with exceptional divisor `P = Proj(A) = 𝐏^{n-1}_Z`, `p : P ⟶ Z` and `i : Z ⟶ X` —
> the canonical map `Rb_*Ω^a_{L/S} ⟶ i_*Rp_*Ω^a_{P/S}` is an isomorphism on cohomology sheaves in
> every degree `q ≥ 1`, for every `a ≥ 0`.
>
> By `isIso_homology_coneFormsDerivedComparison_of_vanishing` it is enough that `π_*r` is an
> epimorphism (`epi_pushforward_coneProjection_coneFormsRestriction`) and that its kernel has no
> cohomology on `P` in positive degrees (`isZero_rightDerived_coneFormsKernel`), where
> `π : L ⟶ P` is the cone projection and `r : Ω^a_{L/S} ⟶ 0_*Ω^a_{P/S}` the restriction of forms to
> the zero section.

```lean
theorem isIso_homology_coneFormsDerivedComparison (hn : 1 ≤ n) (a q : ℕ) (hq : 1 ≤ q) :
    IsIso ((DerivedCategory.homologyFunctor _ (q : ℤ)).map
      (coneFormsDerivedComparison R m n (a : ℤ)))
```

## Tag 0G5G, a lemma

[Tag 0G5G](https://stacks.math.columbia.edu/tag/0G5G) in the Stacks Project.

**`Stacks.DeRham.blowupFormsPullbackMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/BlowupDifferentialFormsComparison.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/BlowupDifferentialFormsComparison.lean#L131). The attribute's comment: “the first canonical map b^*Ω^a\_\{X/S} ⟶ Ω^a\_\{L/S}”.

> **Stacks Project, Tag 0G5G, the first canonical map.** The canonical map
> `b^*Ω^a_{X/S} ⟶ Ω^a_{L/S}` of the commutative square
>
> ```
> L → X
> ↓   ↓
> S = S
> ```
>
> attached to the coordinate blowup; this is the general construction of
> `AlgebraicGeometry.Scheme.Hom.relativeDifferentialFormsMap`, that is, of Section 50.2 of the
> source.
>
> This is the **first** of the two canonical maps asserted by Stacks 0G5G, in that tag's own
> Situation: `coordinateAmbient` is the tag's `X`, `coordinateBlowup` is the tag's global `L`,
> and the affine blowup charts `A[I/yᵢ]` enter only in the proof of the second map. The second
> map and the identification of the composite are not available yet, so only this clause of the
> tag is claimed here.

```lean
noncomputable def blowupFormsPullbackMap (a : ℕ) :
    (Scheme.Modules.pullback (coordinateBlowupToAmbient R m n)).obj
        (Scheme.Hom.relativeDifferentialForms (coordinateAmbientToBase R m n) a) ⟶
      Scheme.Hom.relativeDifferentialForms (coordinateBlowupToBase R m n) a
```

**`Stacks.DeRham.blowupFormsTwistedComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/BlowupFormsTwistedComparison.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/BlowupFormsTwistedComparison.lean#L77). The attribute's comment: “the second canonical map Ω^a\_\{L/S} ⟶ b^*Ω^a\_\{X/S} ⊗\_\{𝒪\_L} 𝒪\_L((n-1)E)”.

> **Stacks Project, Tag 0G5G, the second canonical map.** The map
> `Ω^a_{L/S} ⟶ b^*Ω^a_{X/S} ⊗_{𝒪_L} 𝒪_L((n-1)E)`.
>
> This is `Stacks.Divisors.twistedRetraction` at the effective Cartier divisor `(n-1)E` and the
> monomorphism `Stacks.DeRham.blowupFormsPullbackMap`: the pole bound
> `Stacks.DeRham.exceptionalPoleBound` says that `ℐ_{(n-1)E} · Ω^a_{L/S} ⊆ b^*Ω^a_{X/S}`, which
> lets the ideal sheaf act on `Ω^a_{L/S}` with values in `b^*Ω^a_{X/S}`, and untwisting that action
> by the evaluation pairing of `𝒪_L((n-1)E)` with `ℐ_{(n-1)E}` gives a map into the twist.

```lean
noncomputable def blowupFormsTwistedComparison (a : ℕ) :
    Scheme.Hom.relativeDifferentialForms (coordinateBlowupToBase R m n) a ⟶
      blowupFormsExceptionalTwist R m n a
```

**`Stacks.DeRham.blowupFormsPullbackMap_comp_twistedComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/BlowupFormsTwistedComparison.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/BlowupFormsTwistedComparison.lean#L91). The attribute's comment: “the composite of the two maps is induced by the inclusion 𝒪\_L ⊆ 𝒪\_L((n-1)E)”.

> **Stacks Project, Tag 0G5G, the composite of the two canonical maps.** The composite of
> `Stacks.DeRham.blowupFormsPullbackMap` with `Stacks.DeRham.blowupFormsTwistedComparison` is the
> map induced by the inclusion `𝒪_L ⊆ 𝒪_L((n-1)E)`.
>
> That induced map is `Stacks.DeRham.blowupFormsCanonicalSection`, multiplication by the canonical
> section of `𝒪_L((n-1)E)`; the identity is `Stacks.Divisors.comp_twistedRetraction`.

```lean
theorem blowupFormsPullbackMap_comp_twistedComparison (a : ℕ) :
    blowupFormsPullbackMap R m n a ≫ blowupFormsTwistedComparison R m n a =
      blowupFormsCanonicalSection R m n a
```

## Tag 0G5H, a lemma

[Tag 0G5H](https://stacks.math.columbia.edu/tag/0G5H) in the Stacks Project.

**`Stacks.DeRham.isIso_coordinateBlowupTwistDerivedMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/CoordinateBlowupTwistDerivedDirectImage.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/CoordinateBlowupTwistDerivedDirectImage.lean#L80).

> **Stacks Project, Tag 0G5H.** Let `b : L ⟶ X = 𝐀^{m+n}_R` be the blowing up of affine space
> along the coordinate subspace `𝐀^m_R`, `n ≥ 1`, with exceptional divisor `E`. For every locally
> free `𝒪_X`-module `ℰ`, of any rank, and every `0 ≤ i ≤ n - 1` the canonical map
> `ℰ ⟶ Rb_*(b^*ℰ ⊗ 𝒪_L(iE))` is an isomorphism in `D(𝒪_X)`.

```lean
theorem isIso_coordinateBlowupTwistDerivedMap (hn : 1 ≤ n) (i : ℕ) (hi : i ≤ n - 1)
    (E : (coordinateAmbient R m n).Modules) [SheafOfModules.IsLocallyFree.{u, u, u} E] :
    IsIso (TwistDerived.twistDerivedMap (coordinateBlowupToAmbient R m n)
      (coordinateExceptional R m n ^ i) E)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 50.16, Tag 0FUB](https://stacks.math.columbia.edu/tag/0FUB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
