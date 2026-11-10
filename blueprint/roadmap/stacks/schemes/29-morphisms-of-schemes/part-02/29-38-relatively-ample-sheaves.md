---
declaration: section
origin: cited
lean: Stacks.RelativeAmple.IsRelativelyAmple, AlgebraicGeometry.Scheme.Modules.isRelativelyAmple_iff_tensorPower_isRelativelyAmple, AlgebraicGeometry.Scheme.Modules.IsRelativelyAmple.isSeparated, Stacks.RelativeAmple.IsRelativelyAmple.quasiSeparated, Stacks.RelativeAmple.isQuasicoherent_gradedDirectImage_of_isRelativelyAmple, Stacks.RelativeAmple.iSup_nonvanishingOpenOn_eq_top, Stacks.RelativeAmpleLocalOnBase.isRelativelyAmple_of_forall_exists_isAmple, Stacks.RelativeAmpleLocalOnBase.exists_affine_isAmple_cover_of_isRelativelyAmple
statement: formalized
proof: formalized
---

# 29.38 Relatively ample sheaves

Section 29.38 of the Stacks Project, [Tag 01VG](https://stacks.math.columbia.edu/tag/01VG). 10 tags here are carried by 23 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01VH, a definition

[Tag 01VH](https://stacks.math.columbia.edu/tag/01VH) in the Stacks Project.

**`Stacks.RelativeAmple.IsRelativelyAmple`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeAmple/Basic.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeAmple/Basic.lean#L164). References: EGA II (4.6.1).

> **Stacks Tag 01VH.** An invertible `𝒪_X`-module `L` is *ample relative to* `f : X ⟶ S` when
> `f` is quasi-compact and, for every affine open `V` of `S`, the restriction of `L` to the open
> subscheme `f⁻¹(V)` is ample. The restriction is the module pullback along the open immersion of
> `f⁻¹(V)`, whose invertibility is Stacks Tag 0B8L, and ampleness is Stacks Tag 01PS.

```lean
def IsRelativelyAmple {X S : Scheme.{u}} (f : X ⟶ S) (L : X.Modules)
    [Stacks.Ample.IsInvertibleModule X L] : Prop
```

## Tag 02NN, a lemma

[Tag 02NN](https://stacks.math.columbia.edu/tag/02NN) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.isRelativelyAmple_iff_tensorPower_isRelativelyAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeAmple/TensorPower.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeAmple/TensorPower.lean#L136). References: EGA II (4.6.9).

> An invertible sheaf of modules on a scheme is ample relative to a morphism if and only if any
> one of its positive tensor powers is.

```lean
theorem isRelativelyAmple_iff_tensorPower_isRelativelyAmple
    {X S : Scheme.{u}} (f : X ⟶ S) (L : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L]
    (n : ℕ) (hn : 1 ≤ n) :
    letI := Invertible.tensorPower_isInvertible X.presheaf X.ringCatSheaf.2 L (n : ℤ)
    Stacks.RelativeAmple.IsRelativelyAmple f L ↔
      Stacks.RelativeAmple.IsRelativelyAmple f
        (Invertible.tensorPower X.presheaf X.ringCatSheaf.2 L (n : ℤ))
```

## Tag 01VI, a lemma

[Tag 01VI](https://stacks.math.columbia.edu/tag/01VI) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.IsRelativelyAmple.isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativelyAmple/Separated.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativelyAmple/Separated.lean#L41). References: EGA II (4.6.3).

> A morphism of schemes admitting a relatively ample invertible sheaf is separated.

```lean
theorem IsRelativelyAmple.isSeparated {X S : Scheme.{u}} {f : X ⟶ S} {L : X.Modules}
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L]
    (hL : Stacks.RelativeAmple.IsRelativelyAmple f L) : IsSeparated f
```

## Tag 01VJ, a lemma

[Tag 01VJ](https://stacks.math.columbia.edu/tag/01VJ) in the Stacks Project.

**`Stacks.RelativeAmple.IsRelativelyAmple.quasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeAmple/GradedDirectImage.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeAmple/GradedDirectImage.lean#L125). The attribute's comment: “(5), the quasi-separatedness assertion: a morphism carrying a relatively ample invertible module is quasi-separated”.

> **Stacks Tag 01VJ, clause (5), the quasi-separatedness assertion.** A morphism carrying a
> relatively ample invertible module is quasi-separated. It is in fact separated, which is
> [Stacks, Tag 01VI] and is
> `AlgebraicGeometry.Scheme.Modules.IsRelativelyAmple.isSeparated`; a separated
> morphism is quasi-separated.

```lean
theorem IsRelativelyAmple.quasiSeparated {X S : Scheme.{u}} {f : X ⟶ S} {L : X.Modules}
    [IsInvertibleModule X L] (hL : IsRelativelyAmple f L) : QuasiSeparated f
```

**`Stacks.RelativeAmple.isQuasicoherent_gradedDirectImage_of_isRelativelyAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeAmple/GradedDirectImage.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeAmple/GradedDirectImage.lean#L185). The attribute's comment: “(5), the homogeneous pieces of the graded algebra A = f\_*(⨁\_\{d ≥ 0} L^\{⊗ d}) of the clause: their quasi-coherence in nonnegative degree (the step the source attributes to Schemes 26.24.1) and their vanishing in negative degree. The graded algebra A itself, with its multiplication, is Stacks.RelativeAmple.directImageAlgebra; see the module docstring”.

> **The pieces of `𝒜` in nonnegative degree are quasi-coherent**, for a relatively ample `L`:
> both hypotheses of [Stacks, Tag 01LC] are then available, quasi-compactness from
> [Stacks, Tag 01VH] and quasi-separatedness from
> `Stacks.RelativeAmple.IsRelativelyAmple.quasiSeparated`.

```lean
theorem isQuasicoherent_gradedDirectImage_of_isRelativelyAmple
    (hL : IsRelativelyAmple f L) (d : ℕ) :
    (gradedDirectImage f L (d : ℤ)).IsQuasicoherent
```

**`Stacks.RelativeAmple.iSup_nonvanishingOpenOn_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeAmple/GradedDirectImage.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeAmple/GradedDirectImage.lean#L219). The attribute's comment: “(5), the assertion U(psi) = X: for L ample relative to f, the nonvanishing opens of the positive-degree sections of A = f\_*(⨁\_\{d ≥ 0} L^\{⊗ d}) cover X”.

> **Stacks Tag 01VJ, clause (5), the assertion `U(ψ) = X`.** For `L` ample relative to `f`,
> the nonvanishing opens of the sections of positive degree of `𝒜 = f_*(⨁_{d ≥ 0} L^{⊗ d})` cover
> `X`.
>
> The supremum is over triples of an affine open `V` of `S`, a degree `d ≥ 1`, and a section of
> `𝒜_d` over `V`; `U(ψ)` is the union of exactly these nonvanishing opens, since the degree-`d`
> component of the adjunction map `ψ` is the identity on sections over `V` under
> `sections_gradedDirectImage`. See the section "Why `U(ψ) = X` is the supremum below" of the
> module docstring.

```lean
theorem iSup_nonvanishingOpenOn_eq_top (hL : IsRelativelyAmple f L) :
    (⨆ p : Σ' (V : S.Opens) (_ : IsAffineOpen V) (d : ℕ) (_ : 1 ≤ d),
        Γ(gradedDirectImage f L (d : ℤ), V),
      nonvanishingOpenOn (tensorPowModule X L (p.2.2.1 : ℤ)) (f ⁻¹ᵁ p.1) p.2.2.2.2) = ⊤
```

**`Stacks.RelativeAmpleLocalOnBase.isRelativelyAmple_of_forall_exists_isAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeAmple/LocalOnBase.lean, line 391](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeAmple/LocalOnBase.lean#L391). The attribute's comment: “(3) implies (1): relative ampleness may be checked on an affine open covering”. References: EGA II (4.6.4), “Sufficiency”; EGA II (8.10.6), “partial”.

> **Stacks Tag 01VJ, clause (3) implies clause (1).** Let `f : X ⟶ S` be a quasi-compact
> morphism of schemes and `L` an invertible `𝒪_X`-module. If every point of `S` has an affine open
> neighbourhood `V` with `L|_{f⁻¹V}` ample, then `L` is ample relative to `f`, that is, `L|_{f⁻¹V}`
> is ample for *every* affine open `V ⊆ S`.
>
> For an affine open `W ⊆ S` the preimage `f⁻¹W` is covered by the preimages of basic opens of `W`
> lying inside members of the given covering, and on each of those the restriction of `L` is ample
> by [Stacks, Tag 0B3E]; those preimages are the basic opens of the pullbacks to `f⁻¹W` of the
> cutting functions, so
> `Stacks.RelativeAmpleLocalOnBase.isAmple_of_basicOpen_cover` assembles them.

```lean
theorem isRelativelyAmple_of_forall_exists_isAmple {X S : Scheme.{u}} (f : X ⟶ S)
    (L : X.Modules) [IsInvertibleModule X L] (hf : QuasiCompact f)
    (hcov : ∀ x : S, ∃ V : S.Opens, IsAffineOpen V ∧ x ∈ V ∧
      IsAmple (f ⁻¹ᵁ V).toScheme (Stacks.AmpleLocallyClosed.pullbackModule (f ⁻¹ᵁ V).ι L)) :
    Stacks.RelativeAmple.IsRelativelyAmple f L
```

**`Stacks.RelativeAmpleLocalOnBase.exists_affine_isAmple_cover_of_isRelativelyAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeAmple/LocalOnBase.lean, line 440](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeAmple/LocalOnBase.lean#L440). The attribute's comment: “(1) implies (3): the affine opens of the base are such a covering”.

> **Stacks Tag 01VJ, clause (1) implies clause (3).** A relatively ample module restricts to an
> ample module on the preimage of *some* affine open neighbourhood of every point of the base,
> because the affine opens of the base are a basis of its topology.

```lean
theorem exists_affine_isAmple_cover_of_isRelativelyAmple {X S : Scheme.{u}} (f : X ⟶ S)
    (L : X.Modules) [IsInvertibleModule X L]
    (hL : Stacks.RelativeAmple.IsRelativelyAmple f L) (x : S) :
    ∃ V : S.Opens, IsAffineOpen V ∧ x ∈ V ∧
      IsAmple (f ⁻¹ᵁ V).toScheme (Stacks.AmpleLocallyClosed.pullbackModule (f ⁻¹ᵁ V).ι L)
```

**`Stacks.RelativeAmple.IsRelativelyAmple.isOpenImmersion_globalMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeAmple/ProjCharacterization.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeAmple/ProjCharacterization.lean#L271). The attribute's comment: “(1) implies (5), the assertion that r\_\{L,psi} is an open immersion”.

> **[Stacks, Tag 01VJ], (1) implies the open-immersion assertion of (5).** For `L` ample relative
> to `f`, with `𝒜 = f_*(⨁_{d ≥ 0} L^{⊗ d})` and `ψ` the adjunction map, the morphism
> `r_{L, ψ} : U(ψ) ⟶ Proj_S(𝒜)` is an open immersion.

```lean
theorem IsRelativelyAmple.isOpenImmersion_globalMorphism (hL : IsRelativelyAmple f L) :
    haveI := hL.quasiCompact
    haveI := hL.quasiSeparated
    IsOpenImmersion
      ((directImagePowerMap f L).globalMorphism (relativeProj (directImageAlgebra f L)))
```

**`Stacks.RelativeAmple.isRelativelyAmple_of_isImmersion_globalMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeAmple/ProjCharacterization.lean, line 305](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeAmple/ProjCharacterization.lean#L305). The attribute's comment: “(6) implies (1)”.

> **[Stacks, Tag 01VJ], (6) implies (1).** Let `f` be quasi-compact, `𝒜` a quasi-coherent
> graded `𝒪_S`-algebra and `ψ : f^*𝒜 ⟶ ⨁_{d ≥ 0} L^{⊗ d}` a graded map with `U(ψ) = X` such that
> `r_{L, ψ} : X ⟶ Proj_S(𝒜)` is an immersion. Then `L` is ample relative to `f`.
>
> Over an affine open `V` of `S` the morphism is an immersion `f⁻¹V ⟶ Proj 𝒜(V)` by
> `globalMorphism_iff`, and `isAmple_of_isImmersion_glued` gives ampleness of `L|_{f⁻¹V}`.

```lean
theorem isRelativelyAmple_of_isImmersion_globalMorphism (hf : QuasiCompact f)
    {A : SheafGradedAlgebra.{u} S} (P : GradedPowerMap A f) (e : P.L ≅ L)
    (hU : P.coveringOpen = ⊤) (hP : IsImmersion (P.globalMorphism (relativeProj A))) :
    IsRelativelyAmple f L
```

**`Stacks.RelativeAmple.isRelativelyAmple_of_isOpenImmersion_globalMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeAmple/ProjCharacterization.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeAmple/ProjCharacterization.lean#L325). The attribute's comment: “(4) implies (1)”.

> **[Stacks, Tag 01VJ], (4) implies (1)**: an open immersion is an immersion.

```lean
theorem isRelativelyAmple_of_isOpenImmersion_globalMorphism (hf : QuasiCompact f)
    {A : SheafGradedAlgebra.{u} S} (P : GradedPowerMap A f) (e : P.L ≅ L)
    (hU : P.coveringOpen = ⊤) (hP : IsOpenImmersion (P.globalMorphism (relativeProj A))) :
    IsRelativelyAmple f L
```

**`Stacks.RelativeAmple.isRelativelyAmple_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeAmple/ProjCharacterization.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeAmple/ProjCharacterization.lean#L345).

> **[Stacks, Tag 01VJ].** For a quasi-compact morphism of schemes `f : X ⟶ S` and an invertible
> `𝒪_X`-module `L` the following are equivalent:
>
> 1. `L` is ample relative to `f`;
> 2. every point of `S` has an open neighbourhood `V` with `L|_{f⁻¹V}` ample relative to
>    `f ∣_ V : f⁻¹V ⟶ V`;
> 3. every point of `S` has an affine open neighbourhood `V` with `L|_{f⁻¹V}` ample;
> 4. there are a quasi-coherent graded `𝒪_S`-algebra `𝒜` and a graded map
>    `ψ : f^*𝒜 ⟶ ⨁_{d ≥ 0} L^{⊗ d}` with `U(ψ) = X` and `r_{L, ψ} : U(ψ) ⟶ Proj_S(𝒜)` an open
>    immersion;
> 5. `f` is quasi-separated and, for `𝒜 = f_*(⨁_{d ≥ 0} L^{⊗ d})` and `ψ` the adjunction map,
>    `U(ψ) = X` and `r_{L, ψ}` is an open immersion;
> 6. as (4), with `r_{L, ψ}` an immersion.

```lean
theorem isRelativelyAmple_tfae (f : X ⟶ S) (L : X.Modules)
    [Stacks.Ample.IsInvertibleModule X L] [QuasiCompact f] :
    List.TFAE [
      IsRelativelyAmple f L,
      ∀ x : S, ∃ V : S.Opens, x ∈ V ∧
        IsRelativelyAmple (f ∣_ V) (Stacks.AmpleLocallyClosed.pullbackModule (f ⁻¹ᵁ V).ι L),
      ∀ x : S, ∃ V : S.Opens, IsAffineOpen V ∧ x ∈ V ∧
        Stacks.Ample.IsAmple (f ⁻¹ᵁ V).toScheme
          (Stacks.AmpleLocallyClosed.pullbackModule (f ⁻¹ᵁ V).ι L),
      ∃ (A : SheafGradedAlgebra.{u} S) (P : GradedPowerMap A f), Nonempty (P.L ≅ L) ∧
        P.coveringOpen = ⊤ ∧ IsOpenImmersion (P.globalMorphism (relativeProj A)),
      ∃ h : QuasiSeparated f,
        haveI := h
        (directImagePowerMap f L).coveringOpen = ⊤ ∧ IsOpenImmersion
          ((directImagePowerMap f L).globalMorphism (relativeProj (directImageAlgebra f L))),
      ∃ (A : SheafGradedAlgebra.{u} S) (P : GradedPowerMap A f), Nonempty (P.L ≅ L) ∧
        P.coveringOpen = ⊤ ∧ IsImmersion (P.globalMorphism (relativeProj A))]
```

**`Stacks.RelativeAmpleRestrictBase.isRelativelyAmple_morphismRestrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeAmple/RestrictBase.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeAmple/RestrictBase.lean#L214). The attribute's comment: “(1) implies (2): relative ampleness is inherited by the restriction of the morphism over an arbitrary open of the base, so every open covering witnesses clause (2)”. References: EGA II (4.6.4), “Necessity”.

> **Stacks Tag 01VJ, clause (1) implies clause (2).** If `L` is ample relative to `f : X ⟶ S`
> then, for *every* open `V ⊆ S`, the restriction `L|_{f⁻¹V}` is ample relative to the restricted
> morphism `f ∣_ V : f⁻¹V ⟶ V`. In particular every open covering of `S` — for instance the
> one-member covering `{S}` — witnesses clause (2) of [Stacks, Tag 01VJ].
>
> Quasi-compactness of `f ∣_ V` holds because quasi-compactness of a morphism is local on the
> target. For an affine open `A ⊆ V` the image `W = V.ι ''ᵁ A` is an affine open of `S`, where
> clause (1) gives ampleness of `L|_{f⁻¹W}`, and
> `Stacks.RelativeAmpleRestrictBase.isAmple_preimage_morphismRestrict_iff` moves it onto
> `(f ∣_ V)⁻¹A`.
>
> This also records that `Stacks.RelativeAmple.IsRelativelyAmple` restricts to an open of the
> base.

```lean
theorem isRelativelyAmple_morphismRestrict
    (hL : Stacks.RelativeAmple.IsRelativelyAmple f L) (V : S.Opens) :
    Stacks.RelativeAmple.IsRelativelyAmple (f ∣_ V) (pullbackModule (f ⁻¹ᵁ V).ι L)
```

**`Stacks.RelativeAmpleRestrictBase.isRelativelyAmple_of_forall_exists_isRelativelyAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeAmple/RestrictBase.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeAmple/RestrictBase.lean#L235). The attribute's comment: “(2) implies (1): relative ampleness over the members of an arbitrary open covering of the base implies relative ampleness”.

> **Stacks Tag 01VJ, clause (2) implies clause (1).** Let `f : X ⟶ S` be quasi-compact and `L`
> invertible. If every point of `S` has an open neighbourhood `V` such that `L|_{f⁻¹V}` is ample
> relative to `f ∣_ V : f⁻¹V ⟶ V`, then `L` is ample relative to `f`.
>
> The affine opens of `S` are a basis, so each `V` contains an affine open `W` around the given
> point, and `V.ι⁻¹W` is then an affine open of `V`. Relative ampleness over `V` gives ampleness
> on `(f ∣_ V)⁻¹(V.ι⁻¹W)`, which
> `Stacks.RelativeAmpleRestrictBase.isAmple_preimage_morphismRestrict_iff` turns into ampleness of
> `L|_{f⁻¹W}`. That is an affine open covering of the kind
> `Stacks.RelativeAmpleLocalOnBase.isRelativelyAmple_of_forall_exists_isAmple` — clause (3) implies
> clause (1) — consumes.

```lean
theorem isRelativelyAmple_of_forall_exists_isRelativelyAmple (hf : QuasiCompact f)
    (hcov : ∀ x : S, ∃ V : S.Opens, x ∈ V ∧ Stacks.RelativeAmple.IsRelativelyAmple (f ∣_ V)
      (pullbackModule (f ⁻¹ᵁ V).ι L)) :
    Stacks.RelativeAmple.IsRelativelyAmple f L
```

## Tag 01VK, a lemma

[Tag 01VK](https://stacks.math.columbia.edu/tag/01VK) in the Stacks Project.

**`Stacks.RelativeAmpleAffineBase.isRelativelyAmple_iff_isAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeAmpleAffineBase/Basic.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeAmpleAffineBase/Basic.lean#L167). References: EGA II (4.6.6).

> **Stacks Tag 01VK.** Over an affine base, an invertible `𝒪_X`-module is ample relative to
> `f : X ⟶ S` if and only if it is ample on `X`.
>
> Both implications are `Stacks.AmplePullback.isAmple_modulePullback_of_isAffineHom`, the
> unconditional case of Stacks Tag 0B3E for an affine morphism. Forwards, at `V = ⊤`: the hypothesis
> gives ampleness of the restriction of `L` to `f⁻¹(⊤) = ⊤`, and
> `Stacks.RelativeAmpleAffineBase.isAmple_of_isAmple_modulePullback` descends it along the
> isomorphism `⊤ ⟶ X`. Backwards: quasi-compactness of `f` over an affine base is quasi-compactness
> of `X`, and on each affine open `V` of `S` the open immersion of `f⁻¹V` is an affine morphism by
> `Stacks.RelativeAmpleAffineBase.isAffineHom_preimage_ι`.

```lean
theorem isRelativelyAmple_iff_isAmple {X S : Scheme.{u}} [IsAffine S] (f : X ⟶ S)
    (L : X.Modules) [IsInvertibleModule X L] :
    Stacks.RelativeAmple.IsRelativelyAmple f L ↔ IsAmple X L
```

## Tag 0891, a lemma

[Tag 0891](https://stacks.math.columbia.edu/tag/0891) in the Stacks Project.

**`Stacks.RelativeAmple.isRelativelyAmple_unitModule_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeAmple/Basic.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeAmple/Basic.lean#L212). References: EGA II (5.1.6), “(a) <=> (c')”.

> **Stacks Tag 0891.** The structure sheaf `𝒪_X` is ample relative to `f : X ⟶ S` if and only
> if the preimage under `f` of every affine open of `S` is a quasi-affine scheme — that is, if and
> only if `f` is quasi-affine.
>
> The quasi-compactness clause of Tag 01VH is not an extra condition on the right-hand side: it
> follows from quasi-affineness of the affine preimages by
> `Stacks.RelativeAmple.quasiCompact_of_forall_isQuasiAffine_preimage`. On each preimage the
> equivalence is Tag 01QE applied to `(f ⁻¹ᵁ V).ι^* 𝒪_X`, which
> `Stacks.RelativeAmple.pullbackUnitModuleIso` identifies with the structure sheaf of the open
> subscheme.

```lean
theorem isRelativelyAmple_unitModule_iff {X S : Scheme.{u}} (f : X ⟶ S) :
    IsRelativelyAmple f (Stacks.Ample.unitModule X) ↔
      ∀ V : S.Opens, IsAffineOpen V → (f ⁻¹ᵁ V).toScheme.IsQuasiAffine
```

## Tag 0892, a lemma

[Tag 0892](https://stacks.math.columbia.edu/tag/0892) in the Stacks Project.

**`Stacks.AmplePullbackDatum.exists_threshold_isAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmplePullbackDatum/Basic.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmplePullbackDatum/Basic.lean#L259). The attribute's comment: “part (1)”.

> **Part (1) of [Stacks, Tag 0892].** For `L` ample relative to `f : X ⟶ S` and `M` an ample
> invertible `𝒪_S`-module there is a threshold `n` with `L ⊗ f^* M ^⊗ a` ample on `X` for every
> `a ≥ n`.
>
> `Stacks.AmplePullbackPart1.exists_threshold_isAmple` with both of its inputs discharged:
> quasi-compactness of `X` by `Stacks.AmplePullbackPart1.compactSpace_of_isAmple`, and the pointwise
> datum by `Stacks.AmplePullbackDatum.eventualAffineDatum`. The module is
> `Stacks.AmplePullbackPart1.tensorPullbackPowModule`, that is `L ⊗ f^* (M ^⊗ a)`.
>
> The tree's nearest previous statement of part (1),
> `Stacks.AmplePullback.exists_isAmple_tensorPullbackPow_of_iso_unitModule`, assumes both
> `L ≅ 𝒪_X` and `M ≅ 𝒪_S` and carries no attribute; this statement assumes neither.

```lean
theorem exists_threshold_isAmple (hL : Stacks.RelativeAmple.IsRelativelyAmple f L)
    (hM : IsAmple S M) :
    ∃ n : ℕ, ∀ a : ℕ, n ≤ a →
      IsAmple X (Stacks.AmplePullbackPart1.tensorPullbackPowModule f L M a)
```

**`Stacks.SectionRatioNoAmple.isAmple_modulePullback_of_isQuasiAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRatioNoAmple/Pullback.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SectionRatioNoAmple/Pullback.lean#L93). The attribute's comment: “part (2)”. References: EGA II (5.1.12), “absolute case”.

> The pullback of an ample invertible module along a quasi-affine morphism is ample.

```lean
theorem isAmple_modulePullback_of_isQuasiAffineHom [IsQuasiAffineHom f] (hM : IsAmple S M) :
    IsAmple X ((modulePullback f.toLRSHom.toShHom).obj M)
```

## Tag 0C4K, a lemma

[Tag 0C4K](https://stacks.math.columbia.edu/tag/0C4K) in the Stacks Project.

**`Stacks.AmplePullbackDatum.exists_threshold_isRelativelyAmple_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmplePullbackDatum/Composition.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmplePullbackDatum/Composition.lean#L125).

> **[Stacks, Tag 0C4K].** Let `f : X ⟶ Y` and `g : Y ⟶ S` be morphisms of schemes, `L` an
> invertible `𝒪_X`-module and `M` an invertible `𝒪_Y`-module. If `S` is quasi-compact, `L` is ample
> relative to `f` and `M` is ample relative to `g`, then there is a threshold `n` beyond which
> `L ⊗ f^* M ^⊗ a` is ample relative to `g ∘ f`.
>
> `Stacks.RelativeAmpleCompositionThreshold.exists_threshold_isRelativelyAmple_comp` carries the
> datum of [Stacks, Tag 01PW] over each affine open of the base as an explicit premise;
> `Stacks.AmplePullbackDatum.relativeEventualAffineDatum` discharges it, so nothing is assumed here
> beyond the three hypotheses of the source.

```lean
theorem exists_threshold_isRelativelyAmple_comp [CompactSpace S]
    (hL : Stacks.RelativeAmple.IsRelativelyAmple f L)
    (hM : Stacks.RelativeAmple.IsRelativelyAmple g M) :
    ∃ n : ℕ, ∀ a : ℕ, n ≤ a → Stacks.RelativeAmple.IsRelativelyAmple (f ≫ g)
      (tensorPullbackPowModule f L M a)
```

**`Stacks.RelativeAmpleCompositionThreshold.exists_threshold_isRelativelyAmple_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeAmple/CompositionThreshold.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeAmple/CompositionThreshold.lean#L217). The attribute's comment: “on Tag 01PW as EventualAffineDatum over each affine open of the base”.

> **Stacks Tag 0C4K**, on the single premise
> `Stacks.RelativeAmpleCompositionThreshold.RelativeEventualAffineDatum` — [Stacks, Tag 01PW] over
> each affine open of the base.
>
> Let `f : X ⟶ Y` and `g : Y ⟶ S` be morphisms of schemes, `L` an invertible `𝒪_X`-module and `M` an
> invertible `𝒪_Y`-module. If `S` is quasi-compact, `L` is ample relative to `f` and `M` is ample
> relative to `g`, then there is a threshold `n` with `L ⊗ f^* M ^⊗ a` ample relative to `g ∘ f` for
> every `a ≥ n`.
>
> Relative ampleness of `L` and of `M` supplies quasi-compactness of `f` and of `g`, hence of the
> composite, so the preimage of an affine open of `S` is quasi-compact and
> `Stacks.RelativeAmpleCompositionThreshold.exists_threshold_isAmple_preimage` applies over each of
> them. Quasi-compactness of `S` extracts a finite subfamily of the affine opens so chosen, and the
> maximum of their thresholds serves for all of them at once; beyond it the finite family is an
> affine open covering of `S` on whose preimages the restriction is ample, which
> `Stacks.RelativeAmpleLocalOnBase.isRelativelyAmple_of_forall_exists_isAmple` — [Stacks, Tag 01VJ],
> clause (3) implies clause (1) — upgrades to relative ampleness over every affine open of `S`.

```lean
theorem exists_threshold_isRelativelyAmple_comp [CompactSpace S]
    (hdat : RelativeEventualAffineDatum f g L M)
    (hL : Stacks.RelativeAmple.IsRelativelyAmple f L)
    (hM : Stacks.RelativeAmple.IsRelativelyAmple g M) :
    ∃ n : ℕ, ∀ a : ℕ, n ≤ a → Stacks.RelativeAmple.IsRelativelyAmple (f ≫ g)
      (tensorPullbackPowModule f L M a)
```

## Tag 0893, a lemma

[Tag 0893](https://stacks.math.columbia.edu/tag/0893) in the Stacks Project.

**`Stacks.AmpleBridge.isRelativelyAmple_pullbackModule_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleBridge/BaseChange.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleBridge/BaseChange.lean#L111). The attribute's comment: “for an arbitrary cartesian square”.

> If `L` is ample relative to `f : X ⟶ S` and the square with sides `p : X' ⟶ X`,
> `f' : X' ⟶ S'`, `f` and `g : S' ⟶ S` is cartesian, then the pullback of `L` along `p` is ample
> relative to `f'`.

```lean
theorem isRelativelyAmple_pullbackModule_of_isPullback {X S X' S' : Scheme.{u}} {p : X' ⟶ X}
    {f' : X' ⟶ S'} {f : X ⟶ S} {g : S' ⟶ S} (hsq : IsPullback p f' f g) (L : X.Modules)
    [Stacks.Ample.IsInvertibleModule X L]
    (hL : Stacks.RelativeAmple.IsRelativelyAmple f L) :
    Stacks.RelativeAmple.IsRelativelyAmple f' (pullbackModule p L)
```

**`Stacks.RelativeAmpleBaseChange.isRelativelyAmple_modulePullback_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeAmpleBaseChange/Basic.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeAmpleBaseChange/Basic.lean#L262).

> If `L` is ample relative to `f : X ⟶ S`, then its pullback to `X ×_S S'` is ample relative
> to the base change `X ×_S S' ⟶ S'`, for any `g : S' ⟶ S`.

```lean
theorem isRelativelyAmple_modulePullback_unconditional
    (hL : Stacks.RelativeAmple.IsRelativelyAmple f L) :
    Stacks.RelativeAmple.IsRelativelyAmple (pullback.snd f g)
      (Stacks.AmpleLocallyClosed.pullbackModule (pullback.fst f g) L)
```

## Tag 0C4L, a lemma

[Tag 0C4L](https://stacks.math.columbia.edu/tag/0C4L) in the Stacks Project.

**`Stacks.RelativeAmpleCompositionPermanence.isRelativelyAmple_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeAmple/CompositionPermanence.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeAmple/CompositionPermanence.lean#L68).

> **Stacks Tag 0C4L.** Let `f : X ⟶ Y` and `g : Y ⟶ S` be morphisms of schemes and let `L` be
> an invertible `𝒪_X`-module. If `L` is ample relative to `g ∘ f` and `f` is quasi-compact, then
> `L` is ample relative to `f`.
>
> Through a point `y : Y` choose an affine open `U ⊆ S` containing `g(y)` and then, since the affine
> opens of `Y` are a basis, an affine open `V` with `y ∈ V ≤ g⁻¹U`. On that `V` the restriction of
> `L` is ample by `Stacks.RelativeAmpleComposition.isAmple_preimage_of_le_preimage`. These `V` cover
> `Y`, and `Stacks.RelativeAmpleLocalOnBase.relativeAmpleLocalOnBase` — [Stacks, Tag 01VJ], clause
> (3) implies clause (1) — upgrades them to every affine open of `Y`.

```lean
theorem isRelativelyAmple_of_comp {X Y S : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ S) (L : X.Modules)
    [IsInvertibleModule X L] (hL : Stacks.RelativeAmple.IsRelativelyAmple (f ≫ g) L)
    (hf : QuasiCompact f) :
    Stacks.RelativeAmple.IsRelativelyAmple f L
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.38, Tag 01VG](https://stacks.math.columbia.edu/tag/01VG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
