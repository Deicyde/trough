---
declaration: section
origin: cited
lean: Stacks.Chow.IsRelativeCycle, Stacks.Chow.relativeCycles, Stacks.Chow.isRelativeCycle_baseChangeFamily, Stacks.Chow.isRelativeCycle_flatPullbackFamily, Stacks.Chow.isRelativeCycle_restrictedFamily, Stacks.Chow.isRelativeCycle_properPushforwardFamily, Stacks.Chow.isRelativeCycle_fiberCycleRestrict, Stacks.Chow.isRelativeCycle_iff_forall_isRelativeCycle_baseChangeFamily
statement: formalized
proof: formalized
---

# 62.6 Relative cycles

Section 62.6 of the Stacks Project, [Tag 0H4Z](https://stacks.math.columbia.edu/tag/0H4Z). 17 tags here are carried by 30 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0H50, a definition

[Tag 0H50](https://stacks.math.columbia.edu/tag/0H50) in the Stacks Project.

**`Stacks.Chow.IsRelativeCycle`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Relative.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Relative.lean#L53). The attribute's comment: “relative r-cycles”.

> A family `α` of `r`-cycles on the fibres of `X/S` is a *relative `r`-cycle* when for every
> discrete valuation ring `R` and every morphism `g : Spec R ⟶ S` the specialization of the generic
> member of the base change `g^*α` is its closed member: `sp_{X'/S'}(α_η) = α_0`.

```lean
def IsRelativeCycle {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    [IsLocallyNoetherian S] (r : ℕ) (α : FamilyOfCycles f r) : Prop
```

**`Stacks.Chow.relativeCycles`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Relative.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Relative.lean#L88). The attribute's comment: “the group z(X/S, r)”.

> The group `z(X/S, r)` of relative `r`-cycles on `X/S`: the subgroup of the group of families
> of `r`-cycles on the fibres of `X/S` cut out by the valuative condition.

```lean
def relativeCycles {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    [IsLocallyNoetherian S] (r : ℕ) : AddSubgroup (FamilyOfCycles f r)
```

## Tag 0H51, a lemma

[Tag 0H51](https://stacks.math.columbia.edu/tag/0H51) in the Stacks Project.

**`Stacks.Chow.isRelativeCycle_baseChangeFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/BaseChangeRelative.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/BaseChangeRelative.lean#L91). The attribute's comment: “base change along an arbitrary morphism of locally Noetherian bases”.

> **Stacks Project, Lemma 0H51, the base change clause.** The base change of a relative
> `r`-cycle along an arbitrary morphism `g : S' ⟶ S` of locally Noetherian schemes is a relative
> `r`-cycle on `X ×_S S'` over `S'`.

```lean
theorem isRelativeCycle_baseChangeFamily {X S S' : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [IsLocallyNoetherian S] [IsLocallyNoetherian S'] (g : S' ⟶ S)
    (r : ℕ) {α : FamilyOfCycles f r} (hα : IsRelativeCycle f r α) :
    IsRelativeCycle (pullback.snd f g) r (baseChangeFamily f g r α)
```

**`Stacks.Chow.isRelativeCycle_flatPullbackFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/FlatPullbackDescent.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/FlatPullbackDescent.lean#L237). The attribute's comment: “flat pullback along a flat morphism of relative dimension e”.

> **Stacks Project, Lemma 0H51, the flat pullback clause.** Let `f : X ⟶ S` be locally of
> finite type with `S` locally Noetherian and let `j : U ⟶ X` be a flat morphism, locally of finite
> type and of relative dimension `e`, with `j ≫ f = f_U`. Then the flat pullback `j^*α` of a
> relative `r`-cycle `α` on `X/S` is a relative `(r + e)`-cycle on `U/S`.
>
> The valuative condition for `j^*α` at a morphism `g : Spec R ⟶ S` from the spectrum of a discrete
> valuation ring is the valuative condition for `α` at `g`, pulled back along the base change of
> `j`: base change of the base scheme commutes with flat pullback by Lemma 0H4P part (3),
> `Stacks.Chow.baseChangeFamily_flatPullbackFamily`, and specialization commutes with flat pullback
> by Lemma 0H4L, `Stacks.Chow.specializationCycle_baseChangedFiberCycleFlatPullback`.
>
> No surjectivity is involved; this is the single-morphism statement whose family form is the
> forward direction of `Stacks.Chow.isRelativeCycle_iff_forall_flatPullbackFamily` below.

```lean
theorem isRelativeCycle_flatPullbackFamily {X S U : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [IsLocallyNoetherian S] (fU : U ⟶ S) [LocallyOfFiniteType fU]
    (j : U ⟶ X) [LocallyOfFiniteType j] [Flat j] (hj : j ≫ f = fU) (e : ℕ)
    (he : AlgebraicGeometry.RelativeDimension j e) (r : ℕ) {α : FamilyOfCycles f r}
    (hα : IsRelativeCycle f r α) :
    IsRelativeCycle fU (r + e) (flatPullbackFamily f fU j hj e he r α)
```

**`Stacks.Chow.isRelativeCycle_restrictedFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/GysinAction.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/GysinAction.lean#L169). The attribute's comment: “restriction to open subschemes of the source and of the base”.

> **Stacks Project, Lemma 0H51, restriction to open subschemes of the source and of the base.**
> For open immersions `j : U ⟶ X` and `i : V ⟶ S` with `j ≫ f = fU ≫ i`, the restriction to
> `U/V` of a relative `r`-cycle on `X/S` is a relative `r`-cycle.
>
> The restriction is the base change along `i`, restricted along the open immersion
> `U ⟶ X ×_S V` over `V`: the base change along an open immersion changes no coefficient, the
> residue fields being equal, and the fibre maps factor through the fibres of `X ×_S V`
> (`Stacks.Chow.fiberRestrict_pullbackLift_comp_restrictedFiberMap`). Both operations preserve
> relative cycles.

```lean
theorem isRelativeCycle_restrictedFamily {X S U V : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [IsLocallyNoetherian S] (fU : U ⟶ V) [LocallyOfFiniteType fU]
    (j : U ⟶ X) [IsOpenImmersion j] (i : V ⟶ S) [IsOpenImmersion i] (h : j ≫ f = fU ≫ i)
    (r : ℕ) {α : FamilyOfCycles f r} (hα : IsRelativeCycle f r α) :
    letI : IsLocallyNoetherian V := isLocallyNoetherian_of_isOpenImmersion i
    IsRelativeCycle fU r (restrictedFamily f fU j i h r α).1
```

**`Stacks.Chow.isRelativeCycle_properPushforwardFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ProperPushforwardRelative.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ProperPushforwardRelative.lean#L40). The attribute's comment: “proper pushforward”.

> Let `S` be locally Noetherian, let `sX : X ⟶ S` and `sY : Y ⟶ S` be locally of finite type, let
> `q : X ⟶ Y` be proper with `q ≫ sY = sX` and let `r ≥ 0`. The proper pushforward `q_*α` of a
> relative `r`-cycle `α` on `X/S` is a relative `r`-cycle on `Y/S`.

```lean
theorem isRelativeCycle_properPushforwardFamily {X Y S : Scheme.{u}} (sX : X ⟶ S)
    [LocallyOfFiniteType sX] (sY : Y ⟶ S) [LocallyOfFiniteType sY] [IsLocallyNoetherian S]
    (q : X ⟶ Y) [IsProper q] (hq : q ≫ sY = sX) (r : ℕ) {α : FamilyOfCycles sX r}
    (hα : IsRelativeCycle sX r α) :
    IsRelativeCycle sY r (properPushforwardFamily sX sY q hq r α)
```

**`Stacks.Chow.isRelativeCycle_fiberCycleRestrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SpecializationRestriction.lean, line 447](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SpecializationRestriction.lean#L447). The attribute's comment: “restriction along an open immersion of the source”.

> The restriction of a relative `r`-cycle on `X/S` to an open subscheme `U ⊆ X`, taken over the
> same base, is a relative `r`-cycle on `U/S`.

```lean
theorem isRelativeCycle_fiberCycleRestrict {X S U : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [IsLocallyNoetherian S] (fU : U ⟶ S) [LocallyOfFiniteType fU]
    (j : U ⟶ X) [IsOpenImmersion j] (h : j ≫ f = fU) (r : ℕ) {α : FamilyOfCycles f r}
    (hα : IsRelativeCycle f r α) :
    IsRelativeCycle fU r (fun s => fiberCycleRestrict f fU j h s r (α s))
```

## Tag 0H52, a lemma

[Tag 0H52](https://stacks.math.columbia.edu/tag/0H52) in the Stacks Project.

**`Stacks.Chow.isRelativeCycle_iff_forall_isRelativeCycle_baseChangeFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/HDescent.lean, line 497](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/HDescent.lean#L497).

> **Stacks Project, Lemma 0H52.** Let `S` be locally Noetherian, let `f : X ⟶ S` be locally of
> finite type, let `r ≥ 0` and let `α` be a family of `r`-cycles on the fibres of `X/S`. Let
> `{g i : S' i ⟶ S}` be an h covering. Then `α` is a relative `r`-cycle if and only if each base
> change `(g i)^*α` is a relative `r`-cycle.
>
> This is `Stacks.Chow.isRelativeCycle_iff_forall_baseChangeFamily` with its two inputs supplied:
> the two-step base change compatibility by
> `Stacks.Chow.specializationCycle_baseChangeFamily_baseChangeFamily_iff` and the descent along an
> extension of discrete valuation rings by
> `Stacks.Chow.specializationCycle_baseChangeFamily_of_isExtension`.

```lean
theorem isRelativeCycle_iff_forall_isRelativeCycle_baseChangeFamily {X S : Scheme.{u}}
    (f : X ⟶ S) [LocallyOfFiniteType f] [IsLocallyNoetherian S] (r : ℕ) (α : FamilyOfCycles f r)
    {I : Type v} (S' : I → Scheme.{u}) (g : ∀ i, S' i ⟶ S) (hg : IsHCovering S' g) :
    IsRelativeCycle f r α ↔
      ∀ i, @IsRelativeCycle _ _ (pullback.snd f (g i)) _ (hg.isLocallyNoetherian i) r
        (baseChangeFamily f (g i) r α)
```

## Tag 0H53, a lemma

[Tag 0H53](https://stacks.math.columbia.edu/tag/0H53) in the Stacks Project.

**`Stacks.Chow.isRelativeCycle_iff_forall_flatPullbackFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/FlatPullbackDescent.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/FlatPullbackDescent.lean#L265). The attribute's comment: “both directions, for a jointly surjective family of flat morphisms of relative dimension e”.

> **Stacks Project, Lemma 0H53.** Let `f : X ⟶ S` be a morphism of schemes with `S` locally
> Noetherian and `f` locally of finite type, let `r, e ≥ 0` and let `α` be a family of `r`-cycles
> on the fibres of `X/S`. Let `{f_i : X_i ⟶ X}` be a jointly surjective family of flat morphisms,
> locally of finite type and of relative dimension `e`. Then `α` is a relative `r`-cycle if and
> only if every flat pullback `f_i^*α` is a relative `(r+e)`-cycle.
>
> The proof is the one in the source. Both directions are read off after base change to the
> spectrum of a discrete valuation ring: there the valuative identity for `f_i^*α` is the identity
> `sp(f_{i,η}^*α_η) = f_{i,0}^*α_0`, and base change of a flat pullback
> (`Stacks.Chow.baseChangeFamily_flatPullbackFamily_apply`, Lemma 0H4P part (3)) with the
> commutation of specialization and flat pullback
> (`Stacks.Chow.specializationCycle_baseChangedFiberCycleFlatPullback`, Lemma 0H4L) turns it into
> `f_{i,0}^*(sp(α_η)) = f_{i,0}^*α_0`. That is implied by the valuative identity for `α`, which
> gives the forward direction, and implies it because the `f_{i,0}^*` are jointly injective by
> `Stacks.Chow.eq_of_forall_baseChangedFiberCycleFlatPullback`, which gives the converse.

```lean
theorem isRelativeCycle_iff_forall_flatPullbackFamily {Idx : Type v} {X S : Scheme.{u}}
    {Y : Idx → Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f] [IsLocallyNoetherian S]
    (p : ∀ i, Y i ⟶ X) [∀ i, LocallyOfFiniteType (p i)] [∀ i, Flat (p i)]
    (fY : ∀ i, Y i ⟶ S) [∀ i, LocallyOfFiniteType (fY i)] (hY : ∀ i, p i ≫ f = fY i) (e : ℕ)
    (he : ∀ i, AlgebraicGeometry.RelativeDimension (p i) e)
    (hsurj : ∀ x : X, ∃ i, ∃ y : Y i, (p i).base y = x) (r : ℕ) (α : FamilyOfCycles f r) :
    IsRelativeCycle f r α ↔
      ∀ i, IsRelativeCycle (fY i) (r + e)
        (flatPullbackFamily f (fY i) (p i) (hY i) e (he i) r α)
```

## Tag 0H54, a lemma

[Tag 0H54](https://stacks.math.columbia.edu/tag/0H54) in the Stacks Project.

**`Stacks.Chow.isRelativeCycle_iff_isRelativeCycle_properPushforwardFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ClosedImmersion.lean, line 530](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ClosedImmersion.lean#L530).

> Let `S` be a locally Noetherian scheme, let `i : X ⟶ Y` be a closed immersion of schemes
> locally of finite type over `S`, let `r ≥ 0` and let `α` be a family of `r`-cycles on the fibres of
> `X/S`. Then `α` is a relative `r`-cycle on `X/S` if and only if `i_*α` is a relative `r`-cycle on
> `Y/S`.

```lean
theorem isRelativeCycle_iff_isRelativeCycle_properPushforwardFamily [IsLocallyNoetherian S]
    (α : FamilyOfCycles sX r) :
    IsRelativeCycle sX r α ↔
      IsRelativeCycle sY r (properPushforwardFamily sX sY i hi r α)
```

## Tag 0H55, a lemma

[Tag 0H55](https://stacks.math.columbia.edu/tag/0H55) in the Stacks Project.

**`Stacks.Chow.IsRelativeCycle.eq_iff_eq_of_mem_genericPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/GenericFibres.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/GenericFibres.lean#L111).

> **Stacks Project, Lemma 0H55.** Let `S` be a locally Noetherian scheme, let `f : X ⟶ S` be
> locally of finite type and let `r ≥ 0`. Two relative `r`-cycles on `X/S` are equal if and only
> if their members over the generic points of the irreducible components of `S` agree.

```lean
theorem IsRelativeCycle.eq_iff_eq_of_mem_genericPoints {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [IsLocallyNoetherian S] (r : ℕ) {α β : FamilyOfCycles f r}
    (hα : IsRelativeCycle f r α) (hβ : IsRelativeCycle f r β) :
    α = β ↔ ∀ η ∈ genericPoints ↥S, α η = β η
```

## Tag 0H56, a lemma

[Tag 0H56](https://stacks.math.columbia.edu/tag/0H56) in the Stacks Project.

**`Stacks.Chow.isRelativeCycle_familyAssociatedToModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/FlatCycleClasses.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/FlatCycleClasses.lean#L125). The attribute's comment: “the source's hypothesis that the module is flat over the base in dimensions at least r, Stacks Definition 0CWG, written out as the dimension bound on the non-flat locus”.

> **Stacks Project, Lemma 0H56.** Let `S` be locally Noetherian, let `f : X ⟶ S` be locally of
> finite type and let `F` be a quasi-coherent `𝒪_X`-module of finite type whose fibrewise support
> has dimension at most `r`. If `F` is flat over `S` in dimensions `≥ r`, then `[F/X/S]_r` is a
> relative `r`-cycle on `X/S`.
>
> Flatness over `S` in dimensions `≥ r` is spelled out as Stacks Definition 0CWG defines it: for
> every point `s` of `S` the locus in the fibre `X_s` where `F` fails to be flat over `S` has
> dimension less than `r`.

```lean
theorem isRelativeCycle_familyAssociatedToModule {r : ℕ} {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [IsLocallyNoetherian S] (F : X.Modules) [F.IsFiniteType]
    [F.IsQuasicoherent]
    (hF : ∀ s : S, topologicalKrullDim
      ↥{y : f.fiber s | ¬ IsFlatOverAt f.toLRSHom.toShHom F (f.fiberι s y)} < (r : WithBot ℕ∞))
    (hdim : FiberSupportDimensionLE f F r) :
    IsRelativeCycle f r (familyAssociatedToModule f F r hdim)
```

## Tag 0H57, a lemma

[Tag 0H57](https://stacks.math.columbia.edu/tag/0H57) in the Stacks Project.

**`Stacks.Chow.isRelativeCycle_familyAssociatedToClosedSubscheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/FlatCycleClasses.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/FlatCycleClasses.lean#L158). The attribute's comment: “the source's hypothesis that the structure sheaf is flat over the base in dimensions at least r, Stacks Definition 0CWG, written out as the dimension bound on the non-flat locus”.

> **Stacks Project, Lemma 0H57.** Let `S` be locally Noetherian, let `f : X ⟶ S` be locally of
> finite type and let `i : Z ⟶ X` be a closed immersion. If the structure sheaf of `Z`, viewed on
> `X`, is flat over `S` in dimensions `≥ r` and its fibrewise support has dimension at most `r`,
> then `[Z/X/S]_r` is a relative `r`-cycle on `X/S`.
>
> This is the proof of the source: the cycle of a closed subscheme is the cycle of its structure
> sheaf by Tag 02QY, so Tag 0H56 applies to the direct image of that structure sheaf.
>
> Flatness over `S` in dimensions `≥ r` is spelled out as Stacks Definition 0CWG defines it: for
> every point `s` of `S` the locus in the fibre `X_s` where `i_* 𝒪_Z` fails to be flat over `S`
> has dimension less than `r`.

```lean
theorem isRelativeCycle_familyAssociatedToClosedSubscheme {r : ℕ} {X S Z : Scheme.{u}}
    (f : X ⟶ S) [LocallyOfFiniteType f] [IsLocallyNoetherian S] (i : Z ⟶ X)
    [IsClosedImmersion i] [(structureSheafPushforward i).IsFiniteType]
    [(structureSheafPushforward i).IsQuasicoherent]
    (hZ : ∀ s : S, topologicalKrullDim
      ↥{y : f.fiber s | ¬ IsFlatOverAt f.toLRSHom.toShHom (structureSheafPushforward i)
        (f.fiberι s y)} < (r : WithBot ℕ∞))
    (hdim : FiberSupportDimensionLE f (structureSheafPushforward i) r) :
    IsRelativeCycle f r (familyAssociatedToModule f (structureSheafPushforward i) r hdim)
```

## Tag 0H58, an equation

[Tag 0H58](https://stacks.math.columbia.edu/tag/0H58) in the Stacks Project.

**`Stacks.Chow.relativeCycleClassMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/FlatCycleClasses.lean, line 350](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/FlatCycleClasses.lean#L350). The attribute's comment: “the homomorphism into z(X/S, r)”.

> **Stacks Project, Equation 0H58.** Let `S` be locally Noetherian, let `f : X ⟶ S` be locally
> of finite type and let `r ≥ 0`. The cycle-class homomorphism from the free abelian group on
> `Hilb(X/S, r)` to the group `z(X/S, r)` of relative `r`-cycles on `X/S`, sending `∑ nᵢ [Zᵢ]` to
> `∑ nᵢ [Zᵢ/X/S]_r`. It refines the homomorphism of Tag 0H6V, whose values are families of
> `r`-cycles on fibres, by cutting its codomain down to the relative cycles: each `[Zᵢ/X/S]_r` is
> a relative `r`-cycle by Lemma 0H57.
>
> The source takes `f` of finite type; quasi-compactness of `f` is not needed, so it is not
> assumed. Under the source's hypotheses the members of `Hilb(X/S, r)` are exactly the closed
> subschemes flat and of relative dimension at most `r` over `S`, by
> `Stacks.Chow.HilbertCycleDatum.ofFlat`.

```lean
def relativeCycleClassMap {r : ℕ} {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [IsLocallyNoetherian S] :
    FreeAbelianGroup (HilbertCycleDatum f r) →+ relativeCycles f r
```

**`Stacks.Chow.relativeCycleClassMap_of`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/FlatCycleClasses.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/FlatCycleClasses.lean#L358). The attribute's comment: “on generators”.

> **Stacks Project, Equation 0H58.** On a generator the cycle-class homomorphism into
> `z(X/S, r)` is the family of cycles `[Z/X/S]_r` of the closed subscheme.

```lean
theorem relativeCycleClassMap_of {r : ℕ} {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [IsLocallyNoetherian S] (Z : HilbertCycleDatum f r) :
    (relativeCycleClassMap f (FreeAbelianGroup.of Z)).1 = Z.cycleFamily f
```

**`Stacks.Chow.relativeCycleClassMap_val`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/FlatCycleClasses.lean, line 367](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/FlatCycleClasses.lean#L367). The attribute's comment: “compatibility with the homomorphism of Tag 0H6V”.

> **Stacks Project, Equation 0H58.** The cycle-class homomorphism into `z(X/S, r)` is the
> homomorphism of Tag 0H6V followed by the inclusion of the relative cycles into the families of
> `r`-cycles on fibres.

```lean
theorem relativeCycleClassMap_val {r : ℕ} {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [IsLocallyNoetherian S]
    (α : FreeAbelianGroup (HilbertCycleDatum f r)) :
    (relativeCycleClassMap f α).1 = cycleClassMap f r α
```

## Tag 0H59, a lemma

[Tag 0H59](https://stacks.math.columbia.edu/tag/0H59) in the Stacks Project.

**`Stacks.Chow.exists_isProper_isCompletelyDecomposed_relativeCycleClassMap_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/CycleClassProperCover.lean, line 485](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/CycleClassProperCover.lean#L485).

> Let `f : X ⟶ S` be a finite type morphism of schemes with `S` Noetherian, let `r ≥ 0` and
> let `α` be a relative `r`-cycle on `X/S`. Then there is a proper, completely decomposed
> (Definition 0GTI) morphism `g : S' ⟶ S` from a Noetherian scheme `S'` such that `g^*α` is in the
> image of the cycle class map `FreeAbelianGroup (Hilb(X ×_S S' / S', r)) ⟶ z(X ×_S S' / S', r)` of
> Equation 0H58.

```lean
theorem exists_isProper_isCompletelyDecomposed_relativeCycleClassMap_eq {X S : Scheme.{u}}
    [IsNoetherian S] (f : X ⟶ S) [LocallyOfFiniteType f] [QuasiCompact f] (r : ℕ)
    (α : relativeCycles f r) :
    ∃ (S' : Scheme.{u}) (g : S' ⟶ S) (_ : IsNoetherian S'), IsProper g ∧
      IsCompletelyDecomposed g ∧
      ∃ c : FreeAbelianGroup (HilbertCycleDatum (pullback.snd f g) r),
        (relativeCycleClassMap (pullback.snd f g) c : FamilyOfCycles (pullback.snd f g) r) =
          baseChangeFamily f g r α
```

## Tag 0H5A, a lemma

[Tag 0H5A](https://stacks.math.columbia.edu/tag/0H5A) in the Stacks Project.

**`Stacks.Chow.surjective_relativeCycleClassMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/DvrCycleClasses.lean, line 515](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/DvrCycleClasses.lean#L515). The attribute's comment: “finite type is the source's hypothesis, stated as locally of finite type plus quasi-compact”.

> **Stacks Project, Lemma 0H5A.** Let `f : X ⟶ Spec R` be a morphism of finite type with `R` a
> discrete valuation ring and let `r ≥ 0`. Then the cycle-class homomorphism of Equation 0H58 is
> surjective: every relative `r`-cycle on `X/Spec R` is a combination of the classes `[Z/X/S]_r` of
> members of `Hilb(X/Spec R, r)`.
>
> A relative `r`-cycle is determined by its member over the generic point of `Spec R` by Tag 0H55,
> and that member is the generic member of a cycle class by
> `Stacks.Chow.exists_cycleClassMap_apply_genericPoint_eq`.

```lean
theorem surjective_relativeCycleClassMap {r : ℕ} {R : Type u} [CommRing R] [IsDomain R]
    [IsDiscreteValuationRing R] {X : Scheme.{u}} (f : X ⟶ Spec (.of R)) [LocallyOfFiniteType f]
    [QuasiCompact f] :
    Function.Surjective (relativeCycleClassMap (r := r) f)
```

## Tag 0H5B, a lemma

[Tag 0H5B](https://stacks.math.columbia.edu/tag/0H5B) in the Stacks Project.

**`Stacks.Chow.isClopen_supportOfFamily_of_specializes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SmoothSupportClopen.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SmoothSupportClopen.lean#L290). The attribute's comment: “the support is clopen once membership is invariant along specializations”.

> **Stacks Project, Lemma 0H5B**, reduction step. The support of a family of `r`-cycles on the
> fibres of a morphism locally of finite type over a locally Noetherian base is open and closed in
> the total space as soon as membership in it is unchanged along every specialization of points of
> the total space.
>
> This is the step of the source which replaces local constancy of the coefficient function
> `x ↦ n_x` by its invariance along specializations: the total space is locally Noetherian, being
> locally of finite type over a locally Noetherian base, and on a locally Noetherian scheme a
> subset invariant along specializations is open and closed.

```lean
theorem isClopen_supportOfFamily_of_specializes {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [IsLocallyNoetherian S] {r : ℕ} (α : FamilyOfCycles f r)
    (hα : ∀ x y : X, x ⤳ y → (x ∈ supportOfFamily f α ↔ y ∈ supportOfFamily f α)) :
    IsClopen (supportOfFamily f α)
```

**`Stacks.Chow.isClopen_irreducibleComponent_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SmoothSupportClopen.lean, line 347](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SmoothSupportClopen.lean#L347). The attribute's comment: “components of a smooth scheme over a field are open and closed”. References: SGA 7 VIII (5.2), “special case”.

> **Stacks Project, Lemma 0H5B**, geometric step. On a scheme smooth over a field every
> irreducible component is open and closed, so it is an open subscheme and is itself smooth over
> the field. This is what makes the unique component of a smooth fibre through a point reduced
> after any extension of the base field.

```lean
theorem isClopen_irreducibleComponent_of_smooth {k : Type u} [Field k] {Y : Scheme.{u}}
    (p : Y ⟶ Spec (.of k)) [Smooth p] (y : Y) : IsClopen (irreducibleComponent y)
```

**`Stacks.Chow.isLocallyConstant_of_specializes_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SmoothSupportClopen.lean, line 363](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SmoothSupportClopen.lean#L363). The attribute's comment: “the reduction of local constancy of the fibrewise coefficient function to its invariance along specializations; not that invariance itself”.

> **Stacks Project, Lemma 0H5B**, topological reduction for a function. A function on a
> quasi-sober locally Noetherian space whose value is unchanged along every specialization is
> locally constant: membership in each of its fibres is unchanged along specializations, hence
> each fibre is open.
>
> This is the sentence of the source which replaces local constancy of the coefficient function
> `x ↦ n_x` by the implication `x' ⤳ x → n_{x'} = n_x`.

```lean
theorem isLocallyConstant_of_specializes_eq {A : Type u} [TopologicalSpace A] [QuasiSober A]
    {β : Type*} (hA : IsLocallyNoetherianSpace A) {n : A → β}
    (hn : ∀ x y : A, x ⤳ y → n x = n y) : IsLocallyConstant n
```

**`Stacks.Chow.isClopen_tsupport_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SmoothSupportClopen.lean, line 450](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SmoothSupportClopen.lean#L450). The attribute's comment: “the support of a cycle of top relative dimension on a scheme smooth over a field is open and closed; neither the statement over a general base nor local constancy of the fibrewise coefficient function”.

> **Stacks Project, Lemma 0H5B** over the spectrum of a field. The support of a cycle of
> relative dimension `k` on a scheme smooth over a field is open and closed, provided every
> generic point of an irreducible component has relative dimension `k`; that proviso is what
> being smooth of relative dimension `k` supplies.
>
> Such a cycle is supported on generic points of irreducible components, and on a scheme smooth
> over a field the closure of a set of such points is a union of connected components.

```lean
theorem isClopen_tsupport_of_smooth {k : Type u} [Field k] {Y : Scheme.{u}}
    (p : Y ⟶ Spec (.of k)) [Smooth p] (j : ℤ)
    (hgen : ∀ ξ ∈ genericPoints ↥Y,
      relativeDimension (fieldChowSituation k).dimensionFunction p ξ = j)
    (c : CycleGroup (fieldChowSituation k) p j) :
    IsClopen (tsupport (c.1 : AlgebraicCycle Y ℤ))
```

**`Stacks.Chow.isClopen_supportOfFamily_of_smoothOfRelativeDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SmoothSupportSpecialization.lean, line 541](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SmoothSupportSpecialization.lean#L541).

> **Stacks Project, Lemma 0H5B.** Let `S` be a locally Noetherian scheme, let `f : X ⟶ S` be
> smooth of relative dimension `r` and let `α` be a relative `r`-cycle on `X/S`. Then the support
> of `α` is open and closed in `X`.
>
> By the reduction step it suffices to know that membership in the support is unchanged along
> every specialization `x ⤳ y` of points of `X`. Such a specialization is realized by the
> generic-to-closed specialization on the spectrum of a discrete valuation ring `R` mapping to
> `X`, and the base change `X ×_S Spec R ⟶ Spec R` — again smooth of relative dimension `r` —
> carries a section through which the two points are seen. The valuative condition applies there,
> and compatibility of supports with base change transports the conclusion back to `X`.

```lean
theorem isClopen_supportOfFamily_of_smoothOfRelativeDimension {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [IsLocallyNoetherian S] (r : ℕ) [SmoothOfRelativeDimension r f]
    (α : FamilyOfCycles f r) (hα : IsRelativeCycle f r α) :
    IsClopen (supportOfFamily f α)
```

## Tag 0H5C, a lemma

[Tag 0H5C](https://stacks.math.columbia.edu/tag/0H5C) in the Stacks Project.

**`Stacks.Chow.isClosed_setOf_fiberCycle_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/EqualityLocus.lean, line 576](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/EqualityLocus.lean#L576).

> **Stacks Project, Lemma 0H5C.** Let `f : X ⟶ S` be a morphism of schemes with `S` locally
> Noetherian and `f` locally of finite type, let `r ≥ 0` and let `α, β ∈ z(X/S, r)`. Then the set
> `E = {s ∈ S : α_s = β_s}` is closed in `S`.
>
> With `γ = α - β`, the set `E` is the vanishing locus of the relative cycle `γ`. It is stable
> under specialization, and every point `η ∉ E` has an open neighbourhood containing no point of
> `E` specializing from `η` (`Stacks.Chow.exists_isOpen_forall_specializes_ne_zero`); on a locally
> Noetherian space these two properties make `E` closed.

```lean
theorem isClosed_setOf_fiberCycle_eq {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [IsLocallyNoetherian S] {r : ℕ} (α β : relativeCycles f r) :
    IsClosed {s : S | (α : FamilyOfCycles f r) s = (β : FamilyOfCycles f r) s}
```

## Tag 0H5D, a lemma

[Tag 0H5D](https://stacks.math.columbia.edu/tag/0H5D) in the Stacks Project.

**`Stacks.Chow.nonempty_isColimit_relativeCyclesCocone`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/LimitColimit.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/LimitColimit.lean#L234).

> **Stacks Project, Lemma 0H5D.** Let `S = lim_{i ∈ I} S_i` be the limit of a cofiltered system
> of Noetherian schemes with affine transition morphisms, let `i₀ ∈ I` and let `X₀ ⟶ S_{i₀}` be of
> finite type; for a stage `a ≥ i₀` put `X_a = X₀ ×_{S_{i₀}} S_a`, and put `X = X₀ ×_{S_{i₀}} S`. If
> `S` is Noetherian, then `z(X/S, r) = colim_{a ≥ i₀} z(X_a/S_a, r)`, the transition maps being
> base change of relative `r`-cycles: the cocone `Stacks.Chow.relativeCyclesCocone` of base changes
> along the projections `S ⟶ S_a` is a colimit in the category of abelian groups.

```lean
theorem nonempty_isColimit_relativeCyclesCocone {I : Type u} [Category.{u} I] [IsCofiltered I]
    (D : I ⥤ Scheme.{u}) [∀ {i j : I} (v : i ⟶ j), IsAffineHom (D.map v)]
    [∀ i, IsNoetherian (D.obj i)] (c : Cone D) (hc : IsLimit c) [IsNoetherian c.pt] {i₀ : I}
    {X₀ : Scheme.{u}} (f₀ : X₀ ⟶ D.obj i₀) [LocallyOfFiniteType f₀] [QuasiCompact f₀] (r : ℕ) :
    Nonempty (IsColimit (relativeCyclesCocone D c f₀ r))
```

## Tag 0H5E, a lemma

[Tag 0H5E](https://stacks.math.columbia.edu/tag/0H5E) in the Stacks Project.

**`Stacks.Chow.relativeCyclesAddEquivOfIsThickening`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ClosedImmersion.lean, line 656](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ClosedImmersion.lean#L656). The attribute's comment: “the bijection i\_* : z(X/S, r) → z(X'/S, r) of relative r-cycles”.

> Let `S` be a locally Noetherian scheme and let `i : X ⟶ Y` be a thickening of schemes locally
> of finite type over `S`. For `r ≥ 0` proper pushforward along `i` is an additive equivalence
> `z(X/S, r) ≃ z(Y/S, r)` of groups of relative `r`-cycles.

```lean
def relativeCyclesAddEquivOfIsThickening (hthick : Stacks.Thickenings.IsThickening i) (r : ℕ) :
    ↥(relativeCycles sX r) ≃+ ↥(relativeCycles sY r)
```

**`Stacks.Chow.relativeCyclesAddEquivOfIsThickening_coe`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ClosedImmersion.lean, line 676](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ClosedImmersion.lean#L676). The attribute's comment: “the equivalence is the fibrewise proper pushforward of families of cycles”.

> The additive equivalence of relative `r`-cycles attached to a thickening is proper pushforward:
> the family of fibrewise cycles underlying the image of `α` is the fibrewise proper pushforward of
> the family underlying `α`.

```lean
theorem relativeCyclesAddEquivOfIsThickening_coe
    (hthick : Stacks.Thickenings.IsThickening i) (r : ℕ) (α : ↥(relativeCycles sX r)) :
    (relativeCyclesAddEquivOfIsThickening sX sY i hi hthick r α).1 =
      properPushforwardFamily sX sY i hi r α.1
```

## Tag 0H5F, a lemma

[Tag 0H5F](https://stacks.math.columbia.edu/tag/0H5F) in the Stacks Project.

**`Stacks.Chow.relativeCyclesRestrictEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/RestrictionBijection.lean, line 461](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/RestrictionBijection.lean#L461). The attribute's comment: “restriction is a bijection z(X/S, r) → z(U/S, r)”.

> **Stacks Project, Lemma 0H5F.** Let `S` be a locally Noetherian scheme, let `X` be a scheme
> locally of finite type over `S`, let `r ≥ 0` and let `j : U ⟶ X` be an open immersion over `S`
> such that the complement of `U` has relative dimension `< r` over `S`, that is
> `dim(X_s \ U_s) < r` for all `s ∈ S`. Then restriction is a bijection
> `z(X/S, r) ⟶ z(U/S, r)`.
>
> The inverse is extension by zero, not a chosen section: fibrewise, the cycle on `X_s` keeps the
> coefficients of the cycle on `U_s` and vanishes off `U_s`.

```lean
def relativeCyclesRestrictEquiv {X S U : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    [IsLocallyNoetherian S] (fU : U ⟶ S) [LocallyOfFiniteType fU] (j : U ⟶ X)
    [IsOpenImmersion j] (h : j ≫ f = fU) (r : ℕ)
    (hdim : ComplementFibreDimensionLT f fU j h r) :
    relativeCycles f r ≃+ relativeCycles fU r
```

## Tag 0H5G, a lemma

[Tag 0H5G](https://stacks.math.columbia.edu/tag/0H5G) in the Stacks Project.

**`Stacks.Chow.relativeCyclesAddEquivOfUniversalHomeomorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/BaseChangeSubintegral.lean, line 363](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/BaseChangeSubintegral.lean#L363). The attribute's comment: “the bijection z(X/S, r) → z(X'/S', r) determined by base change”.

> **Stacks Project, Lemma 0H5G.** Let `g : S' ⟶ S` be a universal homeomorphism of locally
> Noetherian schemes which induces isomorphisms on all residue fields, let `f : X ⟶ S` be locally
> of finite type, let `X' = S' ×_S X` and let `r ≥ 0`. Base change along `g` is an additive
> equivalence `z(X/S, r) ≃ z(X'/S', r)` of groups of relative `r`-cycles.

```lean
def relativeCyclesAddEquivOfUniversalHomeomorphism
    (hres : ∀ t : S', IsIso (g.residueFieldMap t)) (r : ℕ) :
    ↥(relativeCycles f r) ≃+ ↥(relativeCycles (pullback.snd f g) r)
```

**`Stacks.Chow.relativeCyclesAddEquivOfUniversalHomeomorphism_coe`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/BaseChangeSubintegral.lean, line 390](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/BaseChangeSubintegral.lean#L390). The attribute's comment: “the bijection is base change of families of cycles on fibres”.

> **Stacks Project, Lemma 0H5G.** The additive equivalence of relative `r`-cycles attached to a
> universal homeomorphism inducing isomorphisms on all residue fields is base change: the family of
> fibrewise cycles underlying the image of `α` is the base change of the family underlying `α`.

```lean
theorem relativeCyclesAddEquivOfUniversalHomeomorphism_coe
    (hres : ∀ t : S', IsIso (g.residueFieldMap t)) (r : ℕ) (α : ↥(relativeCycles f r)) :
    (relativeCyclesAddEquivOfUniversalHomeomorphism f g hres r α).1 =
      baseChangeFamily f g r α.1
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 62.6, Tag 0H4Z](https://stacks.math.columbia.edu/tag/0H4Z)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
