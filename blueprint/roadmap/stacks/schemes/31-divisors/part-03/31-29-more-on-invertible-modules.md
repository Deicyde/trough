---
declaration: section
origin: cited
lean: Stacks.InvertiblePullback.exists_isInvertible_pullback_iso_of_isTrivial_genericFiber_of_flat, AlgebraicGeometry.exists_isEffectiveCartierDivisor_comap_eq, AlgebraicGeometry.exists_isInvertible_pullback_iso_of_isLocallyNoetherian, Stacks.PicardUFD.subsingleton_picardGroup_open_spectrum, Stacks.PicardUFD.subsingleton_picardGroup_open_affineSpace, Stacks.PicardUFD.twistPicardHom_injective, Stacks.PicardUFD.twistPicardHom_surjective, Stacks.PicardUFD.twistPicardHom_surjective_general
statement: formalized
proof: formalized
---

# 31.29 More on invertible modules

Section 31.29 of the Stacks Project, [Tag 0BD6](https://stacks.math.columbia.edu/tag/0BD6). 5 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BD7, a lemma

[Tag 0BD7](https://stacks.math.columbia.edu/tag/0BD7) in the Stacks Project.

**`Stacks.InvertiblePullback.exists_isInvertible_pullback_iso_of_isTrivial_genericFiber_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/InvertiblePullbackFlat/LocalFamilyAgreement.lean, line 330](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/InvertiblePullbackFlat/LocalFamilyAgreement.lean#L330).

> **Stacks Project, Tag 0BD7.** Let `φ : X ⟶ Y` be a morphism of schemes and `ℒ` an invertible
> `𝒪_X`-module. Assume `X` is locally Noetherian, `Y` is locally Noetherian, integral and normal,
> `φ` is flat with integral fibres, `φ` is quasi-compact or locally of finite type, and `ℒ` is
> trivial on the generic fibre of `φ`. Then `ℒ ≅ φ^*𝒩` for an invertible `𝒪_Y`-module `𝒩`.
>
> The family of meromorphic multipliers of the penultimate paragraph of the source's proof is no
> longer a hypothesis: it is
> `Stacks.InvertiblePullback.exists_span_eq_top_isPullMeromorphicFamily`.
>
> Invertibility of `ℒ` is the hypothesis `hL` alone: the class instance that
> `FamilyDescent.lean` carries beside it is the same statement in another spelling and is
> obtained from `hL` inside the proof, so no hypothesis here is absent from
> [Stacks, Tag 0BD7].

```lean
theorem exists_isInvertible_pullback_iso_of_isTrivial_genericFiber_of_flat
    [IsLocallyNoetherian X] [IsLocallyNoetherian Y]
    [AlgebraicGeometry.IsIntegral Y] [IsNormal Y]
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj
      (Stacks.Sheaves.Differentials.ringSheaf (J := Opens.grothendieckTopology X) X.sheaf).property
        L)
    (hfibre : ∀ y : Y, AlgebraicGeometry.IsIntegral (f.fiber y))
    (hfinite : QuasiCompact f ∨ LocallyOfFiniteType f)
    (hgeneric : AlgebraicGeometry.SheafOfModules.IsTrivial
      (f.fiber (genericPoint Y)).presheaf
      (Presheaf.isSheaf_comp_of_isSheaf _ _ (forget₂ CommRingCat RingCat)
        (f.fiber (genericPoint Y)).IsSheaf)
      ((Scheme.Modules.pullback (f.fiberι (genericPoint Y))).obj L)) :
    ∃ N : Y.Modules,
      AlgebraicGeometry.SheafOfModules.IsInvertible Y.presheaf
          ((Presheaf.isSheaf_iff_isSheaf_comp _ Y.presheaf
            (forget₂ CommRingCat RingCat)).mp Y.IsSheaf) N ∧
        Nonempty ((Scheme.Modules.pullback f).obj N ≅ L)
```

## Tag 0BD8, a lemma

[Tag 0BD8](https://stacks.math.columbia.edu/tag/0BD8) in the Stacks Project.

**`AlgebraicGeometry.exists_isEffectiveCartierDivisor_comap_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/EffectiveCartier/UFDExtension.lean, line 377](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/EffectiveCartier/UFDExtension.lean#L377).

> **Stacks Project, Tag 0BD8.** An effective Cartier divisor on an open subscheme of a locally
> Noetherian scheme extends to an effective Cartier divisor on the whole scheme, provided the local
> rings at the points outside the open are unique factorization domains. The extension is the
> scheme-theoretic image.

```lean
theorem exists_isEffectiveCartierDivisor_comap_eq {X : Scheme.{u}} [IsLocallyNoetherian X]
    (U : X.Opens) (D : U.toScheme.IdealSheafData) (hD : IsEffectiveCartierDivisor D)
    (hUFD : ∀ x : X, x ∉ U → UniqueFactorizationMonoid (X.presheaf.stalk x)) :
    ∃ D' : X.IdealSheafData, IsEffectiveCartierDivisor D' ∧ D'.comap U.ι = D
```

## Tag 0BD9, a lemma

[Tag 0BD9](https://stacks.math.columbia.edu/tag/0BD9) in the Stacks Project.

**`AlgebraicGeometry.exists_isInvertible_pullback_iso_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/EffectiveCartier/UFDExtensionInvertibleLocallyNoetherian.lean, line 676](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/EffectiveCartier/UFDExtensionInvertibleLocallyNoetherian.lean#L676). The attribute's comment: “the locally Noetherian case, i.e. the tag itself”.

> **[Stacks, Tag 0BD9].** Let `X` be a locally Noetherian scheme, let `U ⊆ X` be an open
> subscheme, and let `L` be an invertible `𝒪_U`-module. If the local ring `𝒪_{X, x}` is a unique
> factorization domain at every point `x` outside `U`, then `L` is the restriction of an invertible
> `𝒪_X`-module.

```lean
theorem exists_isInvertible_pullback_iso_of_isLocallyNoetherian {X : Scheme.{u}}
    [IsLocallyNoetherian X] (U : X.Opens) (L : U.toScheme.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible U.toScheme.sheaf.obj
      U.toScheme.ringCatSheaf.property L]
    (hUFD : ∀ x : X, x ∉ U → UniqueFactorizationMonoid (X.presheaf.stalk x)) :
    ∃ L' : X.Modules,
      AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L' ∧
        Nonempty (L ≅ (Scheme.Modules.pullback U.ι).obj L')
```

## Tag 0BDA, a lemma

[Tag 0BDA](https://stacks.math.columbia.edu/tag/0BDA) in the Stacks Project.

**`Stacks.PicardUFD.subsingleton_picardGroup_open_spectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardGroup/OpenUFD.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PicardGroup/OpenUFD.lean#L205). The attribute's comment: “part (1)”. References: SGA 1 XI (6.5), “factorial-ring example”.

> **Stacks Project, Tag 0BDA, part (1).** The Picard group of any open subscheme of the
> spectrum of a unique factorization domain is trivial.
>
> The empty open is handled separately; for a nonempty one, prime avoidance gives two principal
> opens `D(f), D(g) ⊆ U` whose union has trivial Picard group and across whose complement in `U`
> regular functions extend, so triviality descends to `U`.

```lean
theorem subsingleton_picardGroup_open_spectrum (R : Type u) [CommRing R] [IsDomain R]
    [UniqueFactorizationMonoid R] (U : (Spec (.of R)).Opens) :
    Subsingleton (PicardGroup U.toScheme.presheaf U.toScheme.ringCatSheaf.2)
```

**`Stacks.PicardUFD.subsingleton_picardGroup_open_affineSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardGroup/OpenUFD.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PicardGroup/OpenUFD.lean#L229). The attribute's comment: “part (2)”. References: EGA I (2.4.8), “more general”.

> **Stacks Project, Tag 0BDA, part (2).** The Picard group of any open subscheme of affine
> space over a unique factorization domain is trivial. In particular this holds over a field.
>
> Affine space over `R` is the spectrum of `R[ι]`, which is again a unique factorization domain
> (Tag 0BC1, Mathlib's instance for `MvPolynomial`), so this is part (1) transported along
> `AlgebraicGeometry.AffineSpace.SpecIso`.

```lean
theorem subsingleton_picardGroup_open_affineSpace (R : Type u) [CommRing R] [IsDomain R]
    [UniqueFactorizationMonoid R] (ι : Type u) (U : (AffineSpace ι (Spec (.of R))).Opens) :
    Subsingleton (PicardGroup U.toScheme.presheaf U.toScheme.ringCatSheaf.2)
```

## Tag 0BXJ, a lemma

[Tag 0BXJ](https://stacks.math.columbia.edu/tag/0BXJ) in the Stacks Project.

**`Stacks.PicardUFD.twistPicardHom_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardUFD/ProjectiveSpace.lean, line 1037](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PicardUFD/ProjectiveSpace.lean#L1037). The attribute's comment: “injectivity of m ↦ 𝒪(m), for 0 < n; the source states no restriction, but at n = 0 the map is the zero map into the trivial Picard group of ℙ⁰\_R ≅ Spec R and is not injective”.

> **The homomorphism `ℤ ⟶ Pic(ℙⁿ_R)`, `m ↦ 𝒪(m)`, is injective** for `R` a domain and
> `0 < n`. A trivialization of `𝒪(m)` makes the transition unit `(T₀ / T₁) ^ m` a ratio of
> constants, which at the generic point reads `T₀^{m⁺} T₁^{m⁻} · s = r · T₀^{m⁻} T₁^{m⁺}` and
> forces `m⁺ = m⁻`, hence `m = 0`.

```lean
theorem twistPicardHom_injective [IsDomain R] (hn : 0 < n) :
    Function.Injective (twistPicardHom R n)
```

**`Stacks.PicardUFD.twistPicardHom_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardUFD/ProjectiveSpace.lean, line 1470](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PicardUFD/ProjectiveSpace.lean#L1470). The attribute's comment: “surjectivity of m ↦ 𝒪(m) for the projective line, i.e. for n = 1”.

> **Stacks Project, Tag 0BXJ.** The homomorphism `ℤ ⟶ Pic(ℙ¹_R)`, `m ↦ 𝒪(m)`, is surjective for
> `R` a unique factorization domain: every invertible module on the projective line is a twist.

```lean
theorem twistPicardHom_surjective [IsDomain R] [UniqueFactorizationMonoid R] :
    Function.Surjective (twistPicardHom R 1)
```

**`Stacks.PicardUFD.twistPicardHom_surjective_general`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardUFD/ProjectiveSpaceCocycle.lean, line 672](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PicardUFD/ProjectiveSpaceCocycle.lean#L672). The attribute's comment: “surjectivity of m ↦ 𝒪(m), for every n”.

> **Stacks Project, Tag 0BXJ.** The homomorphism `ℤ ⟶ Pic(ℙⁿ_R)`, `m ↦ 𝒪(m)`, is surjective
> for `R` a unique factorization domain and every `n`.

```lean
theorem twistPicardHom_surjective_general :
    Function.Surjective (twistPicardHom R n)
```

**`Stacks.PicardUFD.twistPicardAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardUFD/ProjectiveSpaceCocycle.lean, line 694](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PicardUFD/ProjectiveSpaceCocycle.lean#L694). The attribute's comment: “the isomorphism ℤ ≃+ Pic(ℙⁿ\_R) carrying m to the class of 𝒪(m), for 0 < n”.

> **Stacks Project, Tag 0BXJ.** The Picard group of `ℙⁿ_R` is `ℤ` for `R` a unique
> factorization domain and `0 < n`, the isomorphism sending `m` to the class of `𝒪(m)`.

```lean
def twistPicardAddEquiv (hn : 0 < n) :
    ℤ ≃+ (AlgebraicGeometry.Proj
      (MvPolynomial.homogeneousSubmodule (Fin (n + 1)) R)).picardGroup
```

**`Stacks.PicardUFD.not_injective_twistPicardHom_dim_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardUFD/ProjectiveSpaceCocycle.lean, line 727](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PicardUFD/ProjectiveSpaceCocycle.lean#L727). The attribute's comment: “the n = 0 boundary case: m ↦ 𝒪(m) is the zero map into the trivial group Pic(ℙ⁰\_R) and is not injective, so the unrestricted source statement fails there”.

> **The boundary case of Tag 0BXJ.** The source states no restriction on `n`, but at `n = 0`
> the Picard group of `ℙ⁰_R` is trivial, so `m ↦ 𝒪(m)` is the zero map and is not injective.

```lean
theorem not_injective_twistPicardHom_dim_zero :
    ¬ Function.Injective (twistPicardHom R 0)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 31.29, Tag 0BD6](https://stacks.math.columbia.edu/tag/0BD6)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
