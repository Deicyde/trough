---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsHQuasiProjective, AlgebraicGeometry.IsLocallyQuasiProjective, AlgebraicGeometry.IsQuasiProjective, AlgebraicGeometry.IsQuasiProjective.of_isPullback, AlgebraicGeometry.IsQuasiProjective.comp, AlgebraicGeometry.IsQuasiProjective.locallyOfFiniteType, AlgebraicGeometry.IsQuasiProjective.quasiCompact, AlgebraicGeometry.IsHQuasiProjective.locallyOfFiniteType
statement: formalized
proof: formalized
---

# 29.41 Quasi-projective morphisms

Section 29.41 of the Stacks Project, [Tag 01VV](https://stacks.math.columbia.edu/tag/01VV). 8 tags here are carried by 21 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01VW, a definition

[Tag 01VW](https://stacks.math.columbia.edu/tag/01VW) in the Stacks Project.

**`AlgebraicGeometry.IsHQuasiProjective`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/QuasiProjective.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Blowup/QuasiProjective.lean#L53). The attribute's comment: “H-quasi-projective”.

> **Stacks Project, Tag 01VW.** A quasi-compact immersion into relative
> finite-dimensional projective space.  This is `Stacks.HProjective.IsHQuasiProjective`, which
> states the same thing with the structure morphism of `ℙⁿ_S` spelled `↘`.

```lean
abbrev IsHQuasiProjective {X S : Scheme.{u}} (f : X ⟶ S) : Prop
```

**`AlgebraicGeometry.IsLocallyQuasiProjective`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/QuasiProjective.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Blowup/QuasiProjective.lean#L59). The attribute's comment: “locally quasi-projective”.

> **Stacks Project, Tag 01VW.** A morphism quasi-projective after restriction over an open
> cover of the base.

```lean
abbrev IsLocallyQuasiProjective {X S : Scheme.{u}} (f : X ⟶ S) : Prop
```

**`AlgebraicGeometry.IsQuasiProjective`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiProjective/Basic.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiProjective/Basic.lean#L77). The attribute's comment: “quasi-projective”. References: EGA II (5.3.1).

> A morphism of schemes is *quasi-projective* when it is of finite type — locally of finite type
> and quasi-compact — and the source carries an invertible sheaf that is ample relative to it.

```lean
public abbrev IsQuasiProjective {X S : Scheme.{u}} (f : X ⟶ S) : Prop
```

## Tag 0B3G, a lemma

[Tag 0B3G](https://stacks.math.columbia.edu/tag/0B3G) in the Stacks Project.

**`AlgebraicGeometry.IsQuasiProjective.of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiProjective/BaseChange.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiProjective/BaseChange.lean#L78).

> **[Stacks, Tag 0B3G].** A base change of a quasi-projective morphism is quasi-projective: if
> `f' : X' ⟶ S'` fits into a cartesian square over a quasi-projective `f : X ⟶ S`, then `f'` is
> quasi-projective.
>
> Finite type is stable under base change, which is the finite-type half of [Stacks, Tag 01T4],
> and the pullback along `X' ⟶ X` of a sheaf ample relative to `f` is ample relative to `f'`,
> which is [Stacks, Tag 0893] in the form `Stacks.AmpleBridge.relativelyAmpleBaseChange`.

```lean
public theorem of_isPullback {X S X' S' : Scheme.{u}} {p : X' ⟶ X} {f' : X' ⟶ S'} {f : X ⟶ S}
    {g : S' ⟶ S} (hsq : IsPullback p f' f g) (hf : IsQuasiProjective f) :
    IsQuasiProjective f'
```

## Tag 0C4M, a lemma

[Tag 0C4M](https://stacks.math.columbia.edu/tag/0C4M) in the Stacks Project.

**`AlgebraicGeometry.IsQuasiProjective.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiProjective/Composite.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiProjective/Composite.lean#L67). References: EGA I (6.6.4), “(ii), special case”.

> **[Stacks, Tag 0C4M].** Let `f : X ⟶ Y` and `g : Y ⟶ S` be morphisms of schemes with `S`
> quasi-compact. If `f` and `g` are quasi-projective, then so is `f ≫ g`.
>
> Finite type composes. The relatively ample sheaf is produced by [Stacks, Tag 0C4K],
> `Stacks.AmplePullbackDatum.exists_threshold_isRelativelyAmple_comp`: from sheaves `L` on `X` ample
> relative to `f` and `M` on `Y` ample relative to `g` it gives a threshold beyond which
> `L ⊗ f^* M ^⊗ a` is ample relative to `f ≫ g`, and the threshold itself is used as the
> exponent.

```lean
public theorem comp {X Y S : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ S) [CompactSpace S]
    (hf : IsQuasiProjective f) (hg : IsQuasiProjective g) : IsQuasiProjective (f ≫ g)
```

## Tag 01VX, a lemma

[Tag 01VX](https://stacks.math.columbia.edu/tag/01VX) in the Stacks Project.

**`AlgebraicGeometry.IsQuasiProjective.locallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiProjective/Basic.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiProjective/Basic.lean#L101). The attribute's comment: “finite\_type”.

> **Stacks Project, Tag 01VX, quasi-projective case.** A quasi-projective morphism is locally
> of finite type; here this is part of the definition.

```lean
public theorem locallyOfFiniteType (h : IsQuasiProjective f) : LocallyOfFiniteType f
```

**`AlgebraicGeometry.IsQuasiProjective.quasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiProjective/Basic.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiProjective/Basic.lean#L106). The attribute's comment: “finite\_type”.

> **Stacks Project, Tag 01VX, quasi-projective case.** A quasi-projective morphism is
> quasi-compact; here this is part of the definition.

```lean
public theorem quasiCompact (h : IsQuasiProjective f) : QuasiCompact f
```

**`AlgebraicGeometry.IsHQuasiProjective.locallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiProjective/SeparatedFiniteType.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiProjective/SeparatedFiniteType.lean#L72). The attribute's comment: “finite\_type”.

> An H-quasi-projective morphism of schemes is locally of finite type.

```lean
theorem locallyOfFiniteType (hf : IsHQuasiProjective f) : LocallyOfFiniteType f
```

**`AlgebraicGeometry.IsHQuasiProjective.quasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiProjective/SeparatedFiniteType.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiProjective/SeparatedFiniteType.lean#L78). The attribute's comment: “finite\_type”.

> An H-quasi-projective morphism of schemes is quasi-compact.

```lean
theorem quasiCompact (hf : IsHQuasiProjective f) : QuasiCompact f
```

**`AlgebraicGeometry.IsHQuasiProjective.isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiProjective/SeparatedFiniteType.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiProjective/SeparatedFiniteType.lean#L84). The attribute's comment: “separated”.

> An H-quasi-projective morphism of schemes is separated.

```lean
theorem isSeparated (hf : IsHQuasiProjective f) : IsSeparated f
```

**`AlgebraicGeometry.IsQuasiProjective.isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiProjective/SeparatedFiniteType.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiProjective/SeparatedFiniteType.lean#L94). The attribute's comment: “separated”. References: EGA II (4.6.3), “special case”.

> A quasi-projective morphism of schemes is separated.

```lean
theorem isSeparated (hf : IsQuasiProjective f) : IsSeparated f
```

**`AlgebraicGeometry.IsLocallyQuasiProjective.locallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiProjective/SeparatedFiniteType.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiProjective/SeparatedFiniteType.lean#L104). The attribute's comment: “finite\_type”.

> A locally quasi-projective morphism of schemes is locally of finite type.

```lean
theorem locallyOfFiniteType (hf : IsLocallyQuasiProjective f) : LocallyOfFiniteType f
```

**`AlgebraicGeometry.IsLocallyQuasiProjective.quasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiProjective/SeparatedFiniteType.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiProjective/SeparatedFiniteType.lean#L112). The attribute's comment: “finite\_type”.

> A locally quasi-projective morphism of schemes is quasi-compact.

```lean
theorem quasiCompact (hf : IsLocallyQuasiProjective f) : QuasiCompact f
```

**`AlgebraicGeometry.IsLocallyQuasiProjective.isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiProjective/SeparatedFiniteType.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiProjective/SeparatedFiniteType.lean#L120). The attribute's comment: “separated”.

> A locally quasi-projective morphism of schemes is separated.

```lean
theorem isSeparated (hf : IsLocallyQuasiProjective f) : IsSeparated f
```

## Tag 01VY, a lemma

[Tag 01VY](https://stacks.math.columbia.edu/tag/01VY) in the Stacks Project.

**`Stacks.HProjective.isQuasiProjective_of_isHQuasiProjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/HProjective/QuasiProjectiveOfHQuasiProjective.lean, line 213](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/HProjective/QuasiProjectiveOfHQuasiProjective.lean#L213).

> **Stacks Tag 01VY: an H-quasi-projective morphism is quasi-projective.** Let
> `i : X ⟶ ℙⁿ_S` be a quasi-compact immersion with `i ≫ (ℙⁿ_S ↘ S) = f`. Then `f` is of finite
> type, because `i` is an immersion and `ℙⁿ_S ⟶ S` is proper, and `i^* 𝒪(1)` is an invertible
> module ample relative to `f` by [Stacks, Tag 01VN], `𝒪(1)` being ample relative to
> `ℙⁿ_S ⟶ S`.

```lean
theorem isQuasiProjective_of_isHQuasiProjective {X S : Scheme.{u}} (f : X ⟶ S)
    (hf : IsHQuasiProjective f) : IsQuasiProjective f
```

## Tag 01VZ, a lemma

[Tag 01VZ](https://stacks.math.columbia.edu/tag/01VZ) in the Stacks Project.

**`Stacks.HProjective.isLocallyQuasiProjective_of_exists_openCover_isHQuasiProjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/HProjective/QuasiProjectiveOfHQuasiProjective.lean, line 312](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/HProjective/QuasiProjectiveOfHQuasiProjective.lean#L312). The attribute's comment: “(2) implies (1): H-quasi-projective over a cover of the base”.

> **Stacks Tag 01VZ, the implication (2) ⟹ (1).** If the base carries an open covering over
> whose members `f` is H-quasi-projective, then `f` is locally quasi-projective.
>
> This is [Stacks, Tag 01VY] applied over each member of the covering, which is the source's own
> proof of this implication.

```lean
theorem isLocallyQuasiProjective_of_exists_openCover_isHQuasiProjective {X S : Scheme.{u}}
    (f : X ⟶ S) (h : ∃ 𝒰 : Scheme.OpenCover.{u} S, ∀ i : 𝒰.I₀,
      AlgebraicGeometry.IsHQuasiProjective (pullback.snd f (𝒰.f i))) :
    AlgebraicGeometry.IsLocallyQuasiProjective f
```

**`Stacks.HProjective.exists_openCover_isHQuasiProjective_of_isLocallyQuasiProjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/HProjective/QuasiProjectiveOfHQuasiProjective.lean, line 333](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/HProjective/QuasiProjectiveOfHQuasiProjective.lean#L333). The attribute's comment: “(1) implies (2): a cover of the base over which f is H-quasi-projective”.

> **Stacks Tag 01VZ, the implication (1) ⟹ (2).** A locally quasi-projective morphism admits an
> open covering of the base over whose members it is H-quasi-projective.
>
> Local quasi-projectivity gives a covering `𝒰` of the base over whose members `f` becomes
> quasi-projective. Refining `𝒰` to an affine covering —
> `AlgebraicGeometry.Scheme.OpenCover.affineRefinement`, whose members are the affine covers of the
> members of `𝒰` — reduces to an affine base, where
> `Stacks.HProjective.isHQuasiProjective_pullbackSnd_of_isQuasiProjective` applies. The refinement's
> base change is identified with the iterated one by
> `AlgebraicGeometry.Scheme.OpenCover.pullbackCoverAffineRefinementObjIso_inv_pullbackHom`, and
> H-quasi-projectivity travels across that identification by
> `Stacks.HProjective.isHQuasiProjective_of_iso`.

```lean
theorem exists_openCover_isHQuasiProjective_of_isLocallyQuasiProjective {X S : Scheme.{u}}
    (f : X ⟶ S) (hf : AlgebraicGeometry.IsLocallyQuasiProjective f) :
    ∃ 𝒰 : Scheme.OpenCover.{u} S, ∀ i : 𝒰.I₀,
      AlgebraicGeometry.IsHQuasiProjective (pullback.snd f (𝒰.f i))
```

**`Stacks.HProjective.isLocallyQuasiProjective_iff_exists_openCover_isHQuasiProjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/HProjective/QuasiProjectiveOfHQuasiProjective.lean, line 352](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/HProjective/QuasiProjectiveOfHQuasiProjective.lean#L352). The attribute's comment: “(1) iff (2): the equivalence the tag states”.

> **Stacks Tag 01VZ.** A morphism of schemes is locally quasi-projective if and only if the base
> has an open covering over whose members it is H-quasi-projective.

```lean
theorem isLocallyQuasiProjective_iff_exists_openCover_isHQuasiProjective {X S : Scheme.{u}}
    (f : X ⟶ S) :
    AlgebraicGeometry.IsLocallyQuasiProjective f ↔
      ∃ 𝒰 : Scheme.OpenCover.{u} S, ∀ i : 𝒰.I₀,
        AlgebraicGeometry.IsHQuasiProjective (pullback.snd f (𝒰.f i))
```

**`Stacks.HProjective.exists_opens_isHQuasiProjective_of_isLocallyQuasiProjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/HProjective/QuasiProjectiveOfHQuasiProjective.lean, line 370](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/HProjective/QuasiProjectiveOfHQuasiProjective.lean#L370). The attribute's comment: “(1) implies (2), with the cover as opens Vⱼ of S and f⁻¹(Vⱼ) → Vⱼ”.

> **Stacks Tag 01VZ, condition (2) in the source's own phrasing.** A locally quasi-projective
> `f : X ⟶ S` admits a family of opens `Vⱼ` of `S` with `S = ⋃ Vⱼ` such that every
> `f⁻¹(Vⱼ) ⟶ Vⱼ` is H-quasi-projective.
>
> The opens are the images of the covering produced by
> `Stacks.HProjective.exists_openCover_isHQuasiProjective_of_isLocallyQuasiProjective`; they cover
> `S` by `AlgebraicGeometry.Scheme.OpenCover.iSup_opensRange`, and over each of them the base
> change and the restriction are isomorphic as arrows by
> `AlgebraicGeometry.morphismRestrictOpensRange`.

```lean
theorem exists_opens_isHQuasiProjective_of_isLocallyQuasiProjective
    {X S : Scheme.{u}} (f : X ⟶ S) (hf : AlgebraicGeometry.IsLocallyQuasiProjective f) :
    ∃ (ι : Type u) (V : ι → S.Opens), (⨆ j, V j) = ⊤ ∧
      ∀ j, AlgebraicGeometry.IsHQuasiProjective (f ∣_ V j)
```

## Tag 0B3H, a lemma

[Tag 0B3H](https://stacks.math.columbia.edu/tag/0B3H) in the Stacks Project.

**`Stacks.HProjective.isQuasiProjective_of_isQuasiAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/HProjective/QuasiProjective.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/HProjective/QuasiProjective.lean#L194). References: EGA II (5.3.4), “(i)”.

> **Stacks Tag 0B3H.** A quasi-affine morphism of finite type is quasi-projective: the
> structure sheaf `𝒪_X` is ample relative to a quasi-affine morphism by [Stacks, Tag 0891].
>
> Finite type is the conjunction of local finite type and quasi-compactness, as in Tag 01T1, and
> quasi-compactness is already a consequence of quasi-affineness, so only the local finite type
> half is a hypothesis.

```lean
theorem isQuasiProjective_of_isQuasiAffineHom {X S : Scheme.{u}} (f : X ⟶ S)
    [IsQuasiAffineHom f] (hf : LocallyOfFiniteType f) : IsQuasiProjective f
```

## Tag 0C4N, a lemma

[Tag 0C4N](https://stacks.math.columbia.edu/tag/0C4N) in the Stacks Project.

**`AlgebraicGeometry.IsQuasiProjective.of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiProjective/Composition.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiProjective/Composition.lean#L43).

> Let `f : X ⟶ Y` and `g : Y ⟶ S` be morphisms of schemes. If `f ≫ g` is quasi-projective and
> `f` is quasi-compact, then `f` is quasi-projective.

```lean
public theorem of_comp {X Y S : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ S)
    (hfg : IsQuasiProjective (f ≫ g)) (hf : QuasiCompact f) : IsQuasiProjective f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.41, Tag 01VV](https://stacks.math.columbia.edu/tag/01VV)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
