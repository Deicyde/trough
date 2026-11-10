---
declaration: section
origin: cited
lean: AlgebraicGeometry.HasResolutionProperty, AlgebraicGeometry.hasResolutionProperty_of_isAmple, AlgebraicGeometry.hasResolutionProperty_of_isRelativelyAmple, AlgebraicGeometry.hasResolutionProperty_of_isAffineHom, AlgebraicGeometry.hasResolutionProperty_of_isAffineHom_or_isQuasiAffineHom, AlgebraicGeometry.hasResolutionProperty_of_surjective_isFiniteLocallyFree, AlgebraicGeometry.exists_isFiniteLocallyFree_epi_of_isIdealAffineCovering, AlgebraicGeometry.hasResolutionProperty_iff_forall_exists_epi_idealPow_of_isIdealAffineCovering
statement: formalized
proof: formalized
---

# 36.36 The resolution property

Section 36.36 of the Stacks Project, [Tag 0F85](https://stacks.math.columbia.edu/tag/0F85). 10 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0F86, a definition

[Tag 0F86](https://stacks.math.columbia.edu/tag/0F86) in the Stacks Project.

**`AlgebraicGeometry.HasResolutionProperty`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ResolutionProperty.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ResolutionProperty.lean#L46).

> A scheme has the resolution property if every finite type quasi-coherent module on it is a
> quotient of a finite locally free module.

```lean
class HasResolutionProperty (X : Scheme.{u}) : Prop
```

## Tag 0F87, a lemma

[Tag 0F87](https://stacks.math.columbia.edu/tag/0F87) in the Stacks Project.

**`AlgebraicGeometry.hasResolutionProperty_of_isAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ResolutionPropertyAmple.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ResolutionPropertyAmple.lean#L128).

> A scheme carrying an ample invertible module has the resolution property: every finite type
> quasi-coherent module on it is a quotient of a finite locally free module.

```lean
theorem hasResolutionProperty_of_isAmple {X : Scheme.{u}} (L : X.Modules)
    [IsInvertibleModule X L] (hL : IsAmple X L) : HasResolutionProperty X
```

## Tag 0FDD, a lemma

[Tag 0FDD](https://stacks.math.columbia.edu/tag/0FDD) in the Stacks Project.

**`AlgebraicGeometry.hasResolutionProperty_of_isRelativelyAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ResolutionPropertyRelativelyAmple.lean, line 450](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ResolutionPropertyRelativelyAmple.lean#L450).

> **Stacks Tag 0FDD.** If `f : X ⟶ Y` is a morphism of schemes, `Y` is quasi-compact,
> quasi-separated and has the resolution property, and `L` is an invertible `𝒪_X`-module ample
> relative to `f`, then `X` has the resolution property.

```lean
theorem hasResolutionProperty_of_isRelativelyAmple {X Y : Scheme.{u}} (f : X ⟶ Y)
    [CompactSpace Y] [QuasiSeparatedSpace Y] [HasResolutionProperty Y]
    (L : X.Modules) [Stacks.Ample.IsInvertibleModule X L]
    (hL : Stacks.RelativeAmple.IsRelativelyAmple f L) : HasResolutionProperty X
```

## Tag 0F88, a lemma

[Tag 0F88](https://stacks.math.columbia.edu/tag/0F88) in the Stacks Project.

**`AlgebraicGeometry.hasResolutionProperty_of_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ResolutionPropertyAffineHom.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ResolutionPropertyAffineHom.lean#L91). The attribute's comment: “the affine case”.

> **The affine case of [Stacks, Tag 0F88].** The source of an affine morphism onto a
> quasi-compact, quasi-separated scheme with the resolution property has the resolution property.
>
> The quasi-affine case is
> `AlgebraicGeometry.hasResolutionProperty_of_isQuasiAffineHom`, by way of [Stacks, Tag 0FDD] — so
> the tag below carries the clause string naming the case that is.

```lean
theorem hasResolutionProperty_of_isAffineHom {X Y : Scheme.{u}} (f : X ⟶ Y) [IsAffineHom f]
    [CompactSpace Y] [QuasiSeparatedSpace Y] [HasResolutionProperty Y] :
    HasResolutionProperty X
```

**`AlgebraicGeometry.hasResolutionProperty_of_isAffineHom_or_isQuasiAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ResolutionPropertyQuasiAffineHom.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ResolutionPropertyQuasiAffineHom.lean#L60). The attribute's comment: “affine or quasi-affine f; the whole statement”.

> **Stacks 0F88**. Let `f : X ⟶ Y` be an affine or quasi-affine morphism of schemes with `Y`
> quasi-compact and quasi-separated. If `Y` has the resolution property, so does `X`.

```lean
theorem hasResolutionProperty_of_isAffineHom_or_isQuasiAffineHom {X Y : Scheme.{u}} (f : X ⟶ Y)
    (hf : IsAffineHom f ∨ IsQuasiAffineHom f) [CompactSpace Y] [QuasiSeparatedSpace Y]
    [HasResolutionProperty Y] : HasResolutionProperty X
```

## Tag 0GTC, a lemma

[Tag 0GTC](https://stacks.math.columbia.edu/tag/0GTC) in the Stacks Project.

**`AlgebraicGeometry.hasResolutionProperty_of_surjective_isFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ResolutionPropertyFiniteLocallyFree.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ResolutionPropertyFiniteLocallyFree.lean#L276).

> **Stacks Project, Tag 0GTC.** If `f : X ⟶ Y` is a surjective finite locally free morphism of
> schemes and `X` has the resolution property, then so does `Y`.

```lean
theorem hasResolutionProperty_of_surjective_isFiniteLocallyFree {X Y : Scheme.{u}} (f : X ⟶ Y)
    [Surjective f] [Stacks.Morphisms.IsFiniteLocallyFree f] [HasResolutionProperty X] :
    HasResolutionProperty Y
```

## Tag 0F89, a lemma

[Tag 0F89](https://stacks.math.columbia.edu/tag/0F89) in the Stacks Project.

**`AlgebraicGeometry.exists_isFiniteLocallyFree_epi_of_isIdealAffineCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ResolutionPropertyIdealCovering.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ResolutionPropertyIdealCovering.lean#L105). The attribute's comment: “the direction that is immediate: resolution property implies each ideal is a finite-locally-free quotient”.

> Let `X` be a scheme with a finite affine open covering `U` and finite type quasi-coherent
> sheaves of ideals `I j` whose vanishing loci are the complements of the `U j`.  If `X` has the
> resolution property then each `I j` is the quotient of a finite locally free `𝒪_X`-module.

```lean
theorem exists_isFiniteLocallyFree_epi_of_isIdealAffineCovering [HasResolutionProperty X] {m : ℕ}
    {U : Fin m → X.Opens} {I : Fin m → X.IdealSheafData} (h : IsIdealAffineCovering X U I)
    (j : Fin m) :
    ∃ (E : X.Modules)
      (_ : SheafOfModules.IsFiniteLocallyFree (R := X.ringCatSheaf) E)
      (q : E ⟶ idealPow (I j) 1), Epi q
```

**`AlgebraicGeometry.hasResolutionProperty_iff_forall_exists_epi_idealPow_of_isIdealAffineCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ResolutionPropertyIdealCoveringConverse.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ResolutionPropertyIdealCoveringConverse.lean#L61).

> **[Stacks, Tag 0F89].** Let `X` be a scheme with
> 1. a finite affine open covering `X = U 0 ∪ ⋯ ∪ U (m - 1)`, and
> 2. finite type quasi-coherent sheaves of ideals `I j` with `V(I j) = X ∖ U j`.
>
> Then `X` has the resolution property if and only if each `I j` is the quotient of a finite
> locally free `𝒪_X`-module.
>
> The forward direction is `exists_isFiniteLocallyFree_epi_of_isIdealAffineCovering`, the
> converse `hasResolutionProperty_of_isIdealAffineCovering`.

```lean
theorem hasResolutionProperty_iff_forall_exists_epi_idealPow_of_isIdealAffineCovering {m : ℕ}
    {U : Fin m → X.Opens} {I : Fin m → X.IdealSheafData} (h : IsIdealAffineCovering X U I) :
    HasResolutionProperty X ↔
      ∀ j, ∃ (E : X.Modules)
        (_ : SheafOfModules.IsFiniteLocallyFree (R := X.ringCatSheaf) E)
        (q : E ⟶ idealPow (I j) 1), Epi q
```

**`AlgebraicGeometry.hasResolutionProperty_of_isIdealAffineCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ResolutionPropertyIdealCoveringSubstantial.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ResolutionPropertyIdealCoveringSubstantial.lean#L234). The attribute's comment: “the substantial direction, at the source's generality: finite-locally-free quotients of the ideals give the resolution property”.

> **The substantial direction of [Stacks, Tag 0F89].**  Let `X` be a scheme with a finite
> affine open covering `U` and finite type quasi-coherent sheaves of ideals `I j` whose vanishing
> loci are the complements of the `U j`.  If each `I j` is the quotient of a finite locally free
> `𝒪_X`-module then `X` has the resolution property.
>
> `X` need not be Noetherian: this is the tag at the generality the source states it.  Together with
> `AlgebraicGeometry.exists_isFiniteLocallyFree_epi_of_isIdealAffineCovering`, which is the
> direction the source calls trivial, it is the equivalence the tag asserts.

```lean
theorem hasResolutionProperty_of_isIdealAffineCovering {X : Scheme.{u}} {m : ℕ}
    {U : Fin m → X.Opens} {I : Fin m → X.IdealSheafData} (h : IsIdealAffineCovering X U I)
    (E : Fin m → X.Modules)
    (hE : ∀ j, SheafOfModules.IsFiniteLocallyFree (R := X.ringCatSheaf) (E j))
    (q : ∀ j, E j ⟶ idealPow (I j) 1) (hq : ∀ j, Epi (q j)) :
    HasResolutionProperty X
```

## Tag 0GMM, a lemma

[Tag 0GMM](https://stacks.math.columbia.edu/tag/0GMM) in the Stacks Project.

**`AlgebraicGeometry.Scheme.IsAmpleFamily.hasResolutionProperty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ResolutionPropertyAmpleFamilyIdealCovering.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ResolutionPropertyAmpleFamilyIdealCovering.lean#L197). References: EGA III (7.7.9), “(ii)”.

> **[Stacks, Tag 0GMM].** A scheme carrying an ample family of invertible modules has the
> resolution property.
>
> The ample family supplies a finite covering of `X` by affine opens `U k = X_{s k}`, the
> nonvanishing loci of global sections `s k` of positive tensor powers `M k` of members of the
> family.  The image of evaluation at `s k`, a morphism `M k ^∨ ⟶ 𝒪_X` out of the invertible,
> hence finite locally free, dual, is a finite type quasi-coherent sheaf of ideals whose vanishing
> locus is the complement of `U k`, and it is a quotient of `M k ^∨`.  The substantial direction
> of [Stacks, Tag 0F89] then gives the resolution property.

```lean
theorem Scheme.IsAmpleFamily.hasResolutionProperty {ι : Type v} {X : Scheme.{u}}
    {L : ι → X.Modules} (hL : X.IsAmpleFamily L) : HasResolutionProperty X
```

## Tag 0F8A, a lemma

[Tag 0F8A](https://stacks.math.columbia.edu/tag/0F8A) in the Stacks Project.

**`AlgebraicGeometry.IsRegular.hasResolutionProperty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ResolutionPropertyAmpleFamilyIdealCovering.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ResolutionPropertyAmpleFamilyIdealCovering.lean#L229). References: SGA 3 VIB (13.3), “more general”.

> **[Stacks, Tag 0F8A].** A quasi-compact regular scheme with affine diagonal has the resolution
> property.
>
> Quasi-compactness is `CompactSpace X`, the affine diagonal is
> `IsAffineHom (pullback.diagonal (terminal.from X))`, and regularity is
> `AlgebraicGeometry.IsRegular` ([Stacks, Tag 02IS]); these are exactly the conditions of the
> source.
>
> The proof is the one of `StacksFrontier/AlgebraicGeometry/Perfect/ResolutionPropertyRegular.lean`:
> regularity gives Noetherianness and unique
> factorization in the local rings, a regular scheme is normal so every point lies in a dense affine
> open, [Stacks, Tag 0EGJ] cuts out the complement of each of those by an effective Cartier divisor,
> quasi-compactness makes the covering finite, and
> `AlgebraicGeometry.hasResolutionProperty_of_isNoetherian_of_isEffectiveCartierDivisor` concludes.

```lean
theorem IsRegular.hasResolutionProperty (X : Scheme.{u}) [CompactSpace X]
    [IsAffineHom
      (CategoryTheory.Limits.pullback.diagonal (CategoryTheory.Limits.terminal.from X))]
    (hX : IsRegular X) : HasResolutionProperty X
```

## Tag 0F8B, a lemma

[Tag 0F8B](https://stacks.math.columbia.edu/tag/0F8B) in the Stacks Project.

**`AlgebraicGeometry.hasResolutionProperty_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ResolutionPropertyLimit.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ResolutionPropertyLimit.lean#L59). The attribute's comment: “the direction that is immediate: if a stage of the diagram has the resolution property then so does the limit”.

> Let `c` be a limit cone over a cofiltered diagram `D` of quasi-compact, quasi-separated
> schemes with affine transition morphisms.  If some stage `D.obj i` has the resolution property,
> then so does the limit `c.pt`.
>
> The projection `c.π.app i : c.pt ⟶ D.obj i` is affine, so this is the affine case of
> [Stacks, Tag 0F88]; it is one direction of [Stacks, Tag 0F8B]
> (`AlgebraicGeometry.hasResolutionProperty_iff_exists_of_isLimit`).

```lean
theorem hasResolutionProperty_of_isLimit [IsCofiltered I]
    [∀ {i j : I} (g : i ⟶ j), IsAffineHom (D.map g)] (hc : IsLimit c)
    [∀ i : I, CompactSpace (D.obj i)] [∀ i : I, QuasiSeparatedSpace (D.obj i)]
    (i : I) [HasResolutionProperty (D.obj i)] :
    HasResolutionProperty c.pt
```

**`AlgebraicGeometry.hasResolutionProperty_iff_exists_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ResolutionPropertyLimitStageQcqs.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ResolutionPropertyLimitStageQcqs.lean#L197).

> **[Stacks, Tag 0F8B].**  Let `c` be a limit cone over a cofiltered diagram `D` of
> quasi-compact, quasi-separated schemes with affine transition morphisms.  The limit `c.pt` has
> the resolution property if and only if some stage `D.obj i` has it.

```lean
theorem hasResolutionProperty_iff_exists_of_isLimit (hc : IsLimit c) :
    HasResolutionProperty c.pt ↔ ∃ i, HasResolutionProperty (D.obj i)
```

## Tag 0F8C, a lemma

[Tag 0F8C](https://stacks.math.columbia.edu/tag/0F8C) in the Stacks Project.

**`AlgebraicGeometry.HasResolutionProperty.isAffineHom_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ResolutionPropertyAffineDiagonal.lean, line 734](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ResolutionPropertyAffineDiagonal.lean#L734).

> **Stacks Project, Tag 0F8C.** A quasi-compact and quasi-separated scheme with the resolution
> property has affine diagonal.
>
> This is
> `AlgebraicGeometry.isAffineHom_diagonal_of_exists_isAffineHom_isNoetherian_hasResolutionProperty`
> composed with `AlgebraicGeometry.exists_isAffineHom_isNoetherian_hasResolutionProperty`, which
> supplies the required affine morphism from the converse of
> `AlgebraicGeometry.hasResolutionProperty_of_isLimit` at Noetherian stages
> (`AlgebraicGeometry.hasResolutionProperty_stage`).

```lean
theorem HasResolutionProperty.isAffineHom_diagonal (X : Scheme.{u})
    [CompactSpace X] [QuasiSeparatedSpace X] [HasResolutionProperty X] :
    IsAffineHom (pullback.diagonal (terminal.from X))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.36, Tag 0F85](https://stacks.math.columbia.edu/tag/0F85)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
