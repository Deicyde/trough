---
declaration: section
origin: cited
lean: AlgebraicGeometry.CohenMacaulayCurveSituation.invertibleCurveDegree_le_and_lt_or_nonempty_iso_of_not_isZero_cohomology_idealTwist, AlgebraicGeometry.CohenMacaulayCurveSituation.isZero_cohomology_one_idealTwist_of_lt, AlgebraicGeometry.CohenMacaulayCurveSituation.not_isZero_cohomology_zero_idealTwist_or_of_lt, AlgebraicGeometry.CohenMacaulayCurveSituation.exists_isIso_projectiveLine_of_genus_eq_zero, AlgebraicGeometry.CohenMacaulayCurveSituation.isGeneratedByGlobalSections_of_two_mul_genus_le, AlgebraicGeometry.CohenMacaulayCurveSituation.isGeneratedByGlobalSections_and_surjective_subschemeRestrictionπ, AlgebraicGeometry.CohenMacaulayCurveSituation.isRelativelyVeryAmple_of_two_mul_genus_add_one_le, AlgebraicGeometry.exists_subcurve_invertibleCurveDegree_le_of_not_isZero_cohomology_idealTwist
statement: formalized
proof: formalized
---

# 53.22 More vanishing results

Section 53.22 of the Stacks Project, [Tag 0E39](https://stacks.math.columbia.edu/tag/0E39). 7 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0E3A, a lemma

[Tag 0E3A](https://stacks.math.columbia.edu/tag/0E3A) in the Stacks Project.

**`AlgebraicGeometry.CohenMacaulayCurveSituation.invertibleCurveDegree_le_and_lt_or_nonempty_iso_of_not_isZero_cohomology_idealTwist`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/IdealTwistVanishing.lean, line 441](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/IdealTwistVanishing.lean#L441).

> **Stacks Project, Tag 0E3A.** In Situation [Stacks, Tag 0B5D] assume `X` is integral of genus
> `g`. Let `ℒ` be an invertible `𝒪_X`-module and let `Z ⊆ X` be a closed subscheme of dimension at
> most zero with ideal sheaf `ℐ`. If `H^1(X, ℐℒ) ≠ 0`, then
>
>   `deg(ℒ) ≤ 2g - 2 + deg(Z)`,
>
> with strict inequality unless `ℐℒ ≅ ω_X`. Here `ℐℒ` is `ℒ ⊗ ℐ`, `deg(Z) = dim_k Γ(Z, 𝒪_Z)` and
> `ω_X` is the dualizing sheaf of [Stacks, Tag 0BS2].

```lean
theorem invertibleCurveDegree_le_and_lt_or_nonempty_iso_of_not_isZero_cohomology_idealTwist
    [IsIntegral S.X] (L : S.X.Modules)
    [SheafOfModules.IsInvertible S.X.presheaf S.X.ringCatSheaf.2 L]
    (Z : S.X.IdealSheafData) (hZ : topologicalKrullDim Z.subscheme ≤ 0)
    (h : ¬ IsZero (cohomologyOverField S.k S.f (S.idealTwist Z L) 1)) :
    invertibleCurveDegree S.k S.f (le_of_eq S.dimension_one) L ≤
        2 * (genus S.f : ℤ) - 2 + (S.subschemeDegree Z : ℤ) ∧
      (invertibleCurveDegree S.k S.f (le_of_eq S.dimension_one) L <
          2 * (genus S.f : ℤ) - 2 + (S.subschemeDegree Z : ℤ) ∨
        Nonempty (S.idealTwist Z L ≅ Stacks.Duality.dualizingSheafOverField S.f))
```

## Tag 0E3B, a lemma

[Tag 0E3B](https://stacks.math.columbia.edu/tag/0E3B) in the Stacks Project.

**`AlgebraicGeometry.CohenMacaulayCurveSituation.isZero_cohomology_one_idealTwist_of_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/IdealTwistSections.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/IdealTwistSections.lean#L62). The attribute's comment: “the vanishing of H^1(X, IL)”.

> **[Stacks, Tag 0E3B], the vanishing.** If `deg(ℒ) > 2g - 2 + deg(Z)` then
> `H¹(X, ℐℒ) = 0`: a nonzero `H¹(X, ℐℒ)` would force `deg(ℒ) ≤ 2g - 2 + deg(Z)` by
> [Stacks, Tag 0E3A].

```lean
theorem isZero_cohomology_one_idealTwist_of_lt (hZ : topologicalKrullDim Z.subscheme ≤ 0)
    (hdeg : 2 * (genus S.f : ℤ) - 2 + (S.subschemeDegree Z : ℤ) <
      invertibleCurveDegree S.k S.f (le_of_eq S.dimension_one) L) :
    IsZero (cohomologyOverField S.k S.f (S.idealTwist Z L) 1)
```

**`AlgebraicGeometry.CohenMacaulayCurveSituation.not_isZero_cohomology_zero_idealTwist_or_of_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/IdealTwistSections.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/IdealTwistSections.lean#L73). The attribute's comment: “possibilities (1) and (2)”.

> **[Stacks, Tag 0E3B], the alternative.** If `deg(ℒ) > 2g - 2 + deg(Z)` then either
> `H⁰(X, ℐℒ) ≠ 0`, or `g = 0` and `deg(ℒ) = deg(Z) - 1`. When `H⁰(X, ℐℒ) = 0` the Euler
> characteristic `χ(X, ℐℒ) = deg(ℒ) + 1 - g - deg(Z)` vanishes, `H¹(X, ℐℒ)` vanishing as well.

```lean
theorem not_isZero_cohomology_zero_idealTwist_or_of_lt (hZ : topologicalKrullDim Z.subscheme ≤ 0)
    (hdeg : 2 * (genus S.f : ℤ) - 2 + (S.subschemeDegree Z : ℤ) <
      invertibleCurveDegree S.k S.f (le_of_eq S.dimension_one) L) :
    ¬ IsZero (cohomologyOverField S.k S.f (S.idealTwist Z L) 0) ∨
      (genus S.f = 0 ∧ invertibleCurveDegree S.k S.f (le_of_eq S.dimension_one) L =
        (S.subschemeDegree Z : ℤ) - 1)
```

**`AlgebraicGeometry.CohenMacaulayCurveSituation.exists_isIso_projectiveLine_of_genus_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/IdealTwistSections.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/IdealTwistSections.lean#L104). The attribute's comment: “in case (2) with Z empty, X is P^1_k and L corresponds to O(-1)”.

> **[Stacks, Tag 0E3B], case (2) with `Z = ∅`.** If `g = 0` and `deg(ℒ) = -1`, then `X ≅ 𝐏¹_k`
> over `k`, and under this isomorphism `ℒ^{⊗ -1}` is the pullback of `𝒪(1)`, i.e. `ℒ` corresponds to
> `𝒪_{𝐏¹}(-1)`. The invertible module `ℒ^{⊗ -1}` has degree one, so a basis of its two-dimensional
> space of global sections defines an isomorphism `X ⟶ 𝐏¹_k` ([Stacks, Tag 0C6T]) along which
> `𝒪(1)` pulls back to `ℒ^{⊗ -1}`.

```lean
theorem exists_isIso_projectiveLine_of_genus_eq_zero
    (hgenus : genus S.f = 0)
    (hdeg : invertibleCurveDegree S.k S.f (le_of_eq S.dimension_one) L = -1) :
    ∃ p : S.X ⟶ projectiveSpaceOver 1 (Spec (.of S.k)),
      IsIso p ∧
      p ≫ Limits.pullback.fst (Limits.terminal.from (Spec (.of S.k)))
          (Limits.terminal.from (projectiveSpaceAtUniverse.{u} 1)) = S.f ∧
      Nonempty ((Scheme.Modules.pullback
          (p ≫ projectiveSpaceOver.toIntegralAtUniverse 1 (Spec (.of S.k)))).obj
            (Stacks.AmpleProjectiveImmersion.twistingSheafAtUniverse.{u} 1) ≅
          tensorPowerModule L (-1))
```

## Tag 0E3C, a lemma

[Tag 0E3C](https://stacks.math.columbia.edu/tag/0E3C) in the Stacks Project.

**`AlgebraicGeometry.CohenMacaulayCurveSituation.isGeneratedByGlobalSections_of_two_mul_genus_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/GlobalGenerationLargeDegree.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/GlobalGenerationLargeDegree.lean#L140).

> **Stacks Project, Tag 0E3C.** In Situation [Stacks, Tag 0B5D] assume `X` is integral of genus
> `g`, and let `ℒ` be an invertible `𝒪_X`-module. If `deg(ℒ) ≥ 2g`, then `ℒ` is generated by its
> global sections.

```lean
theorem isGeneratedByGlobalSections_of_two_mul_genus_le [IsIntegral S.X] (L : S.X.Modules)
    [SheafOfModules.IsInvertible S.X.presheaf S.X.ringCatSheaf.2 L]
    (hL : 2 * (genus S.f : ℤ) ≤ invertibleCurveDegree S.k S.f (le_of_eq S.dimension_one) L) :
    SheafOfModules.IsGeneratedByGlobalSections L
```

## Tag 0E3D, a lemma

[Tag 0E3D](https://stacks.math.columbia.edu/tag/0E3D) in the Stacks Project.

**`AlgebraicGeometry.CohenMacaulayCurveSituation.isGeneratedByGlobalSections_and_surjective_subschemeRestrictionπ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/GlobalGenerationLargeDegree.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/GlobalGenerationLargeDegree.lean#L306).

> **Stacks Project, Tag 0E3D.** In Situation [Stacks, Tag 0B5D] assume `X` is integral of genus
> `g`, let `ℒ` be an invertible `𝒪_X`-module, and let `Z ⊆ X` be a nonempty `0`-dimensional closed
> subscheme. If `deg(ℒ) ≥ 2g - 1 + deg(Z)`, then `ℒ` is generated by its global sections and
> `H⁰(X, ℒ) ⟶ H⁰(X, ℒ|_Z)` is surjective.
>
> Here `deg(Z) = dim_k Γ(Z, 𝒪_Z)` and `ℒ|_Z = ℒ ⊗ i_* 𝒪_Z`. Global generation is [Stacks, Tag 0E3C],
> as `deg(Z) ≥ 1`; the surjectivity follows from `H¹(X, ℐ_Z ℒ) = 0`, which is [Stacks, Tag 0E3A]
> since `deg(ℒ) > 2g - 2 + deg(Z)`.

```lean
theorem isGeneratedByGlobalSections_and_surjective_subschemeRestrictionπ [IsIntegral S.X]
    (L : S.X.Modules) [SheafOfModules.IsInvertible S.X.presheaf S.X.ringCatSheaf.2 L]
    (Z : S.X.IdealSheafData) (hZ : topologicalKrullDim Z.subscheme ≤ 0)
    (hZne : Nonempty Z.subscheme)
    (hL : 2 * (genus S.f : ℤ) - 1 + (S.subschemeDegree Z : ℤ) ≤
      invertibleCurveDegree S.k S.f (le_of_eq S.dimension_one) L) :
    SheafOfModules.IsGeneratedByGlobalSections L ∧
      Function.Surjective (cohomologyOverFieldMap S.k S.f (S.subschemeRestrictionπ Z L) 0)
```

## Tag 0H2V, a lemma

[Tag 0H2V](https://stacks.math.columbia.edu/tag/0H2V) in the Stacks Project.

**`AlgebraicGeometry.CohenMacaulayCurveSituation.isRelativelyVeryAmple_of_two_mul_genus_add_one_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/VeryAmpleLargeDegree.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/VeryAmpleLargeDegree.lean#L264).

> **Invertible modules of degree at least `2g + 1` are very ample.** In Situation
> [Stacks, Tag 0B5D] — a proper one-dimensional scheme `X` over a field `k` with `H⁰(X, 𝒪_X) = k` —
> assume `X` geometrically integral over `k` of genus `g`, and let `ℒ` be an invertible
> `𝒪_X`-module. If `deg(ℒ) ≥ 2g + 1`, then `ℒ` is very ample.

```lean
theorem isRelativelyVeryAmple_of_two_mul_genus_add_one_le
    [AlgebraicGeometry.GeometricallyIntegral S.f] (L : S.X.Modules)
    [SheafOfModules.IsInvertible S.X.presheaf S.X.ringCatSheaf.2 L]
    (hL : 2 * (genus S.f : ℤ) + 1 ≤
      invertibleCurveDegree S.k S.f (le_of_eq S.dimension_one) L) :
    Stacks.Tag01VMVeryAmple.IsRelativelyVeryAmple S.f L
```

## Tag 0E3E, a lemma

[Tag 0E3E](https://stacks.math.columbia.edu/tag/0E3E) in the Stacks Project.

**`AlgebraicGeometry.exists_subcurve_invertibleCurveDegree_le_of_not_isZero_cohomology_idealTwist`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/SubcurveDegreeBound.lean, line 452](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/SubcurveDegreeBound.lean#L452).

> **Stacks Project, Tag 0E3E.** Let `k` be a field and `X` a proper scheme over `k` which is
> reduced and of dimension `1`. Let `ℒ` be an invertible `𝒪_X`-module and `Z ⊆ X` a closed subscheme
> of dimension at most zero with ideal sheaf `ℐ`. If `H¹(X, ℐℒ) ≠ 0`, then there is a reduced
> connected closed subscheme `Y ⊆ X` of dimension `1` with
>
>   `deg(ℒ|_Y) ≤ -2 χ(Y, 𝒪_Y) + deg(Z ∩ Y)`,
>
> where `Z ∩ Y` is the scheme-theoretic intersection `Z ⊔ Y` and `deg(Z ∩ Y) = dim_k Γ(Z ∩ Y, 𝒪)`.
> Here `ℐℒ` is `ℒ ⊗ ℐ`, as in [Stacks, Tag 0E3A]; the source's hypothesis that `X` is connected is
> not needed.
>
> A nonzero map `ℐℒ ⟶ ω_X` from duality ([Stacks, Tag 0BS2]) kills nothing more than the zero
> module, `X` being reduced, and
> `AlgebraicGeometry.exists_le_invertibleCurveDegree_le_of_ne_zero` applies with `T₀ = X`.

```lean
theorem exists_subcurve_invertibleCurveDegree_le_of_not_isZero_cohomology_idealTwist
    {k : Type u} [Field k] (f : X ⟶ Spec (.of k)) [IsProper f] [IsReduced X]
    (hdim : topologicalKrullDim X = 1) (L : X.Modules)
    [hL : SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L]
    (Z : X.IdealSheafData) (hZ : topologicalKrullDim Z.subscheme ≤ 0)
    (h : ¬ IsZero (cohomologyOverField k f
      ((((Stacks.SheafOfModules.Tensor.sheafTensor.{u, u, u, u, u}
            ⟨X.toRingedSpace.presheaf, X.toRingedSpace.IsSheaf⟩).obj L).obj
          (Stacks.ClosedImmersion.idealSheaf Z.subschemeι.toLRSHom.toShHom))) 1)) :
    ∃ (Y : X.IdealSheafData) (_ : IsReduced Y.subscheme) (_ : ConnectedSpace Y.subscheme)
      (hY : topologicalKrullDim Y.subscheme = 1),
      letI := Stacks.AlgebraicGeometry.Tag09NY.isInvertible_modulePullback Y.subschemeι L hL
      letI : Algebra k Γ((Z ⊔ Y).subscheme, ⊤) :=
        ((Scheme.ΓSpecIso (.of k)).inv ≫ ((Z ⊔ Y).subschemeι ≫ f).appTop).hom.toAlgebra
      invertibleCurveDegree k (Y.subschemeι ≫ f) hY.le
          ((Scheme.Modules.pullback Y.subschemeι).obj L) ≤
        -2 * (∑ᶠ n : ℕ, (-1 : ℤ) ^ n * (Module.finrank k (cohomologyOverField k
          (Y.subschemeι ≫ f) (SheafOfModules.unit Y.subscheme.ringCatSheaf) n) : ℤ)) +
          (Module.finrank k Γ((Z ⊔ Y).subscheme, ⊤) : ℤ)
```

## Tag 0E3F, a lemma

[Tag 0E3F](https://stacks.math.columbia.edu/tag/0E3F) in the Stacks Project.

**`AlgebraicGeometry.isGeneratedByGlobalSections_of_forall_subcurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/SubcurveFieldExtension.lean, line 557](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/SubcurveFieldExtension.lean#L557).

> **Stacks Project, Tag 0E3F.** Let `k` be a field and `X` a proper scheme over `k` which is
> reduced and of dimension `1`, and let `ℒ` be an invertible `𝒪_X`-module such that
> `deg(ℒ|_Y) ≥ 2 dim_k H¹(Y, 𝒪_Y)` for every reduced connected closed subscheme `Y ⊆ X` of
> dimension `1`. Then `ℒ` is globally generated. The source's hypothesis that `X` is connected is
> not needed.
>
> As `h⁰(Y, 𝒪_Y) ≥ 1`, the bound gives `-2 χ(Y, 𝒪_Y) < deg(ℒ|_Y)` and
> `h¹(Y, 𝒪_Y) < deg(ℒ|_Y) + χ(Y, 𝒪_Y)`, and
> `AlgebraicGeometry.isGeneratedByGlobalSections_of_forall_subcurve_lt` applies.

```lean
theorem isGeneratedByGlobalSections_of_forall_subcurve (f : X ⟶ Spec (.of k)) [IsProper f]
    [IsReduced X] (hdim : topologicalKrullDim X = 1) (L : X.Modules)
    [hL : SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L]
    (h : ∀ (Y : X.IdealSheafData) [IsReduced Y.subscheme] [ConnectedSpace Y.subscheme]
      (hY : topologicalKrullDim Y.subscheme = 1),
      letI := Stacks.AlgebraicGeometry.Tag09NY.isInvertible_modulePullback Y.subschemeι L hL
      2 * (Module.finrank k (cohomologyOverField k (Y.subschemeι ≫ f)
        (SheafOfModules.unit Y.subscheme.ringCatSheaf) 1) : ℤ) ≤
        invertibleCurveDegree k (Y.subschemeι ≫ f) hY.le
          ((Scheme.Modules.pullback Y.subschemeι).obj L)) :
    _root_.SheafOfModules.IsGeneratedByGlobalSections L
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 53.22, Tag 0E39](https://stacks.math.columbia.edu/tag/0E39)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
