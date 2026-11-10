---
declaration: section
origin: cited
lean: Stacks.Chow.IsEffectiveRelativeCycle, Stacks.Chow.effectiveRelativeCycles, Stacks.Chow.isEffectiveFamily_restrictedFamily, Stacks.Chow.isEffectiveFamily_baseChangeFamily, Stacks.Chow.isEffectiveFamily_flatPullbackFamily, Stacks.Chow.isEffectiveFamily_properPushforwardFamily, Stacks.Chow.isEffectiveFamily_iff_forall_restrictedFamily, Stacks.Chow.isEffectiveFamily_iff_baseChangeFamily
statement: formalized
proof: formalized
---

# 62.9 Effective relative cycles

Section 62.9 of the Stacks Project, [Tag 0H5Q](https://stacks.math.columbia.edu/tag/0H5Q). 8 tags here are carried by 20 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0H5R, a definition

[Tag 0H5R](https://stacks.math.columbia.edu/tag/0H5R) in the Stacks Project.

**`Stacks.Chow.IsEffectiveRelativeCycle`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/EffectiveRelative.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/EffectiveRelative.lean#L55). The attribute's comment: “effectivity of a relative r-cycle”.

> A relative `r`-cycle `α` on `X/S` is *effective* when for every point `s` of `S` the
> `r`-cycle `α_s` it carries on the scheme-theoretic fibre over `s` is an effective cycle.

```lean
def IsEffectiveRelativeCycle {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    [IsLocallyNoetherian S] (r : ℕ) (α : ↥(relativeCycles f r)) : Prop
```

**`Stacks.Chow.effectiveRelativeCycles`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/EffectiveRelative.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/EffectiveRelative.lean#L82). The attribute's comment: “the monoid z^eff(X/S, r)”.

> The monoid `z^eff(X/S, r)` of *effective relative `r`-cycles* on `X/S`: the submonoid of the
> group `z(X/S, r)` of relative `r`-cycles consisting of those whose cycle on every fibre is
> effective.

```lean
def effectiveRelativeCycles {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    [IsLocallyNoetherian S] (r : ℕ) : AddSubmonoid ↥(relativeCycles f r)
```

## Tag 0H5S, a lemma

[Tag 0H5S](https://stacks.math.columbia.edu/tag/0H5S) in the Stacks Project.

**`Stacks.Chow.isEffectiveFamily_restrictedFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Effective.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Effective.lean#L146). The attribute's comment: “restriction”.

> **Stacks Project, Tag 0H5S.** The restriction of an effective family of `r`-cycles on the
> fibres of `X/S` to open subschemes `U ⊆ X` and `V ⊆ S` with `f(U) ⊆ V` is effective.

```lean
theorem isEffectiveFamily_restrictedFamily {X S U V : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [IsLocallyNoetherian S] (fU : U ⟶ V) (j : U ⟶ X)
    [IsOpenImmersion j] (i : V ⟶ S) [IsOpenImmersion i] (h : j ≫ f = fU ≫ i) (r : ℕ)
    (α : FamilyOfCycles f r) (hα : IsEffectiveFamily f r α) :
    letI : LocallyOfFiniteType fU := by
      let : LocallyOfFiniteType (fU ≫ i) := h ▸ inferInstance
      exact locallyOfFiniteType_of_comp fU i
    IsEffectiveFamily fU r (restrictedFamily f fU j i h r α).1
```

**`Stacks.Chow.isEffectiveFamily_baseChangeFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Effective.lean, line 592](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Effective.lean#L592). The attribute's comment: “base change”.

> **Stacks Project, Tag 0H5S, base change.** The base change of an effective family of
> `r`-cycles on the fibres of `X/S` along any morphism `g : S' ⟶ S` of bases is effective; no
> surjectivity of `g` is needed.

```lean
theorem isEffectiveFamily_baseChangeFamily {X S S' : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [IsLocallyNoetherian S] (g : S' ⟶ S) (r : ℕ)
    (α : FamilyOfCycles f r) (hα : IsEffectiveFamily f r α) :
    IsEffectiveFamily (pullback.snd f g) r (baseChangeFamily f g r α)
```

**`Stacks.Chow.isEffectiveFamily_flatPullbackFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Effective.lean, line 674](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Effective.lean#L674). The attribute's comment: “flat pullback”.

> **Stacks Project, Tag 0H5S, flat pullback.** The flat pullback of an effective family of
> `r`-cycles on the fibres of `X/S` along a flat morphism `j : U ⟶ X` of schemes over `S`, locally
> of finite type and of relative dimension `e`, is an effective family of `(r+e)`-cycles on the
> fibres of `U/S`.

```lean
theorem isEffectiveFamily_flatPullbackFamily {X S U : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [IsLocallyNoetherian S] (fU : U ⟶ S) [LocallyOfFiniteType fU]
    (j : U ⟶ X) [LocallyOfFiniteType j] [Flat j] (h : j ≫ f = fU) (e : ℕ)
    (he : AlgebraicGeometry.RelativeDimension j e) (r : ℕ) (α : FamilyOfCycles f r)
    (hα : IsEffectiveFamily f r α) :
    IsEffectiveFamily fU (r + e) (flatPullbackFamily f fU j h e he r α)
```

**`Stacks.Chow.isEffectiveFamily_properPushforwardFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Effective.lean, line 689](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Effective.lean#L689). The attribute's comment: “proper pushforward”.

> **Stacks Project, Tag 0H5S, proper pushforward.** The proper pushforward of an effective
> family of `r`-cycles on the fibres of `X/S` along a proper morphism `p : X ⟶ Y` of schemes over
> `S` is an effective family of `r`-cycles on the fibres of `Y/S`.

```lean
theorem isEffectiveFamily_properPushforwardFamily {X Y S : Scheme.{u}} (sX : X ⟶ S)
    [LocallyOfFiniteType sX] [IsLocallyNoetherian S] (sY : Y ⟶ S) [LocallyOfFiniteType sY]
    (p : X ⟶ Y) [IsProper p] (hp : p ≫ sY = sX) (r : ℕ) (α : FamilyOfCycles sX r)
    (hα : IsEffectiveFamily sX r α) :
    IsEffectiveFamily sY r (properPushforwardFamily sX sY p hp r α)
```

## Tag 0H5T, a lemma

[Tag 0H5T](https://stacks.math.columbia.edu/tag/0H5T) in the Stacks Project.

**`Stacks.Chow.isEffectiveFamily_iff_forall_restrictedFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Effective.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Effective.lean#L199).

> **Stacks Project, Tag 0H5T.** Effectivity of a family of `r`-cycles on the fibres of `X/S`
> may be checked Zariski locally on `X` and on `S`: given open subschemes `U a ⊆ X` and
> `V a ⊆ S` with `f(U a) ⊆ V a` and with the `U a` covering `X`, the family is effective exactly
> when each of its restrictions is.

```lean
theorem isEffectiveFamily_iff_forall_restrictedFamily {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [IsLocallyNoetherian S] {ι : Type v} {U V : ι → Scheme.{u}}
    (fU : ∀ a : ι, U a ⟶ V a) (j : ∀ a : ι, U a ⟶ X) [∀ a : ι, IsOpenImmersion (j a)]
    (i : ∀ a : ι, V a ⟶ S) [∀ a : ι, IsOpenImmersion (i a)]
    (h : ∀ a : ι, j a ≫ f = fU a ≫ i a) (hcover : ∀ x : X, ∃ a : ι, x ∈ Set.range (j a))
    (r : ℕ) (α : FamilyOfCycles f r) :
    letI : ∀ a : ι, LocallyOfFiniteType (fU a) := fun a => by
      let : LocallyOfFiniteType (fU a ≫ i a) := h a ▸ inferInstance
      exact locallyOfFiniteType_of_comp (fU a) (i a)
    IsEffectiveFamily f r α ↔
      ∀ a : ι, IsEffectiveFamily (fU a) r
        (restrictedFamily f (fU a) (j a) (i a) (h a) r α).1
```

## Tag 0H5U, a lemma

[Tag 0H5U](https://stacks.math.columbia.edu/tag/0H5U) in the Stacks Project.

**`Stacks.Chow.isEffectiveFamily_iff_baseChangeFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Effective.lean, line 611](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Effective.lean#L611).

> **Stacks Project, Tag 0H5U.** Let `α` be a family of `r`-cycles on the fibres of `X/S` and
> let `g : S' ⟶ S` be surjective. Then `α` is effective if and only if its base change `g^*α` is
> effective.
>
> Effectivity is a condition on each coefficient separately, and a coefficient of `g^*α` is a
> coefficient of `α` times a multiplicity. The multiplicity is nonnegative, which gives the
> forward implication. For the converse, surjectivity supplies a point `t` of `S'` over a given
> point of `S`, and over `t` the fibre of the base change has a point lying over the chosen point
> of the fibre of `f` at which that multiplicity is nonzero, hence positive; so a negative
> coefficient of `α` would make a coefficient of `g^*α` negative.

```lean
theorem isEffectiveFamily_iff_baseChangeFamily {X S S' : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [IsLocallyNoetherian S] (g : S' ⟶ S) [Surjective g] (r : ℕ)
    (α : FamilyOfCycles f r) :
    IsEffectiveFamily f r α ↔
      IsEffectiveFamily (pullback.snd f g) r (baseChangeFamily f g r α)
```

## Tag 0H5V, a lemma

[Tag 0H5V](https://stacks.math.columbia.edu/tag/0H5V) in the Stacks Project.

**`Stacks.Chow.isEffectiveFamily_iff_forall_flatPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Effective.lean, line 547](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Effective.lean#L547).

> **Stacks Project, Tag 0H5V.** Let `α` be a family of `r`-cycles on the fibres of `X/S` and
> let `{g i : X' i ⟶ X}` be a jointly surjective family of flat morphisms, locally of finite type
> and of relative dimension `e`. If `β i` is the flat pullback of `α` along `g i`, then `α` is
> effective if and only if every `β i` is.
>
> The fibres of `g i ≫ f` map to those of `f` by the base changes of the `g i`, again flat,
> locally of finite type and of relative dimension `e`, and jointly surjective on every fibre, so
> this is the fibrewise `Stacks.Chow.isEffectiveFamily_iff_forall`.

```lean
theorem isEffectiveFamily_iff_forall_flatPullback {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] {r e : ℕ} (α : FamilyOfCycles f r) {Idx : Type*}
    {X' : Idx → Scheme.{u}} (g : ∀ i, X' i ⟶ X) [∀ i, LocallyOfFiniteType (g i)]
    [∀ i, Flat (g i)] (hrel : ∀ i, AlgebraicGeometry.RelativeDimension (g i) e)
    (hsurj : ∀ x : X, ∃ i, ∃ x' : X' i, (g i).base x' = x)
    (β : ∀ i, FamilyOfCycles (g i ≫ f) (r + e))
    (hβ : ∀ (i : Idx) (s : S) (x : (g i ≫ f).fiber s),
      (β i s : AlgebraicCycle ((g i ≫ f).fiber s) ℤ) x =
        (α s : AlgebraicCycle (f.fiber s) ℤ) ((f.fiberMap (g i) s).base x) *
          flatPullbackWeight (fieldChowSituation (S.residueField s))
            ((g i ≫ f).fiberToSpecResidueField s) (f.fiberMap (g i) s)
            ((r : ℤ) + (e : ℤ)) x) :
    IsEffectiveFamily f r α ↔ ∀ i, IsEffectiveFamily (g i ≫ f) (r + e) (β i)
```

## Tag 0H5W, a lemma

[Tag 0H5W](https://stacks.math.columbia.edu/tag/0H5W) in the Stacks Project.

**`Stacks.Chow.isClosed_supportOfFamily_of_isEffectiveFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/EffectiveSupportClosed.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/EffectiveSupportClosed.lean#L332).

> **Stacks Project, Tag 0H5W.** Let `f : X ⟶ S` be a morphism of schemes with `S` locally
> Noetherian and `f` locally of finite type, let `r ≥ 0` be an integer and let `α` be a relative
> `r`-cycle on `X/S`. If `α` is effective then its support is closed in `X`.

```lean
theorem isClosed_supportOfFamily_of_isEffectiveFamily (f : X ⟶ S) [LocallyOfFiniteType f]
    [IsLocallyNoetherian S] (r : ℕ) (α : FamilyOfCycles f r) (hα : IsRelativeCycle f r α)
    (heff : IsEffectiveFamily f r α) : IsClosed (supportOfFamily f α)
```

## Tag 0H5X, a lemma

[Tag 0H5X](https://stacks.math.columbia.edu/tag/0H5X) in the Stacks Project.

**`Stacks.Chow.isEquidimensional_of_isEffectiveFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/EffectiveEquidimensional.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/EffectiveEquidimensional.lean#L131).

> **Stacks Project, Tag 0H5X.** Let `f : X ⟶ S` be a morphism of schemes with `S` locally
> Noetherian and `f` locally of finite type, let `r ≥ 0` be an integer and let `α` be a relative
> `r`-cycle on `X/S`. If `α` is effective then `α` is equidimensional.

```lean
theorem isEquidimensional_of_isEffectiveFamily (f : X ⟶ S) [LocallyOfFiniteType f]
    [IsLocallyNoetherian S] (r : ℕ) (α : FamilyOfCycles f r) (hα : IsRelativeCycle f r α)
    (heff : IsEffectiveFamily f r α) : IsEquidimensional f r α
```

## Tag 0H5Y, a remark

[Tag 0H5Y](https://stacks.math.columbia.edu/tag/0H5Y) in the Stacks Project.

**`Stacks.Chow.effectiveRelativeCyclesFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/EffectiveFunctor.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/EffectiveFunctor.lean#L163). The attribute's comment: “the functor S' ↦ z^eff(X'/S', r), X' = S' ×_S X, on schemes locally of finite type over S”.

> The contravariant functor `S' ↦ z^eff(X'/S', r)`, `X' = S' ×_S X`, on the category of
> schemes locally of finite type over `S`, the map attached to a morphism `S'' ⟶ S'` over `S` being
> base change of effective relative `r`-cycles.

```lean
def effectiveRelativeCyclesFunctor : (LocallyOfFiniteTypeOver S)ᵒᵖ ⥤ Type u
```

**`Stacks.Chow.not_isRepresentable_effectiveRelativeCyclesFunctor_specFieldExt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/NonRepresentable.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/NonRepresentable.lean#L217). The attribute's comment: “the functor S' ↦ z^eff(X'/S', r) is not representable, the counter example the remark leaves to the reader, built from z(X'/S', r) = z(X'_red/S'_red, r)”.

> **Stacks Project, Remark 0H5Y.** Let `k` be a field and let `K/k` be a finite purely
> inseparable extension of degree `> 1`, so that `S = Spec k` is Noetherian and
> `f : X = Spec K ⟶ S` is finite. The functor `S' ↦ z^eff(X'/S', 0)`, `X' = S' ×_S X`, on schemes
> locally of finite type over `S` is not representable.
>
> This is the reason the source gives, made into a counter example: relative cycles do not see
> nilpotents. If `M` represented the functor, the diagonal cycle `ξ ∈ z^eff(X_K/Spec K, 0)` would
> be a morphism `Spec K ⟶ M` whose two pullbacks to `Spec K ×_k Spec K` agree, because they agree
> on the reduction and base change to the reduction is injective; as `Spec K ⟶ Spec k` is an
> effective epimorphism, `ξ` would come from `z^eff(X/S, 0)`. But the cycle `ξ` is one rational
> point with coefficient one, while every base change of a cycle along `K/k` has coefficients
> divisible by `[K : k]` at such a point.

```lean
theorem not_isRepresentable_effectiveRelativeCyclesFunctor_specFieldExt
    [IsPurelyInseparable k K] (hK : Module.finrank k K ≠ 1) :
    ¬ (effectiveRelativeCyclesFunctor (specFieldExt k K) 0).IsRepresentable
```

**`Stacks.Chow.exists_not_isRepresentable_effectiveRelativeCyclesFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/NonRepresentable.lean, line 310](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/NonRepresentable.lean#L310). The attribute's comment: “the functor S' ↦ z^eff(X'/S', r) cannot be representable in general”.

> **Stacks Project, Remark 0H5Y.** The functor `S' ↦ z^eff(X'/S', r)`, `X' = S' ×_S X`, on
> schemes locally of finite type over `S` is not representable in general: there are a locally
> Noetherian scheme `S`, a morphism `f : X ⟶ S` locally of finite type and an `r ≥ 0` for which it is
> not representable. One may take `S = Spec 𝔽₂`, `X = A²` and `r = 0`
> (`Stacks.Chow.SymPlane.not_isRepresentable`).

```lean
theorem exists_not_isRepresentable_effectiveRelativeCyclesFunctor :
    ∃ (S X : Scheme.{u}) (f : X ⟶ S) (_ : LocallyOfFiniteType f) (_ : IsLocallyNoetherian S)
      (r : ℕ), ¬ (effectiveRelativeCyclesFunctor f r).IsRepresentable
```

**`Stacks.Chow.relativeCyclesAddEquivReductionReduction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ReducedInvariance.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ReducedInvariance.lean#L233). The attribute's comment: “the invariance z(X/S, r) = z(X_red/S_red, r)”.

> **Stacks Project, Remark 0H5Y.** `z(X/S, r) = z(X_red/S_red, r)`: the group of relative
> `r`-cycles does not change when both the source and the base are replaced by their reductions.
> Base change along `S_red ⟶ S` identifies `z(X/S, r)` with `z(X ×_S S_red / S_red, r)`
> (`Stacks.Chow.relativeCyclesAddEquivReduction`), and `X_red ⟶ X ×_S S_red` is a thickening over
> `S_red`, along which proper pushforward identifies the groups of relative cycles (Tag 0H5E).

```lean
noncomputable def relativeCyclesAddEquivReductionReduction :
    ↥(relativeCycles f r) ≃+ ↥(relativeCycles (Scheme.reductionMap f) r)
```

**`Stacks.Chow.SymPlane.baseChange_quot_ne_alpha`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SymmetricSquarePlane.lean, line 475](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SymmetricSquarePlane.lean#L475). The attribute's comment: “in characteristic 2 the cycle α on A² × A² does not descend to Sym²(A²): there is no cycle β whose pullback to W is α”.

> **Stacks Project, Remark 0H5Y, the characteristic `2` example: there is no cycle `β`.** Let
> `k` be a field of characteristic `2`, `X = A²_k`, `W = X ×_k X` and `Sym²(X) = Spec B` with
> `B = k[u₁ + u₂, u₁u₂, v₁ + v₂, v₁v₂, u₁v₁ + u₂v₂]`. No family `β` of `0`-cycles on the fibres of
> `X ×_k Sym²(X) ⟶ Sym²(X)`, in particular no relative `0`-cycle, pulls back along the quotient
> morphism `W ⟶ Sym²(X)` to the cycle `α` with `α_{(x₁, x₂)} = [x₁] + [x₂]`: at the generic point
> `η` of the image `V = Spec k[u₁², v₁²]` of the diagonal the cycle `β_η` would be a `0`-cycle on
> `A²_{k(u₁², v₁²)}` whose pullback to `A²_{k(u₁, v₁)}` is twice the rational point `(u₁, v₁)`, which
> is impossible.

```lean
theorem baseChange_quot_ne_alpha
    (β : FamilyOfCycles (pullback.snd (planeHom k) (symObj k).obj.hom) 0) :
    baseChangeFamilyOfIsPullback (pullback.snd (planeHom k) (symObj k).obj.hom)
      (isPullback_overBaseChange (planeHom k) (quot k).hom) 0 β ≠ (alpha k).1.1
```

**`Stacks.Chow.SymPlane.not_isRepresentable_of_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SymmetricSquarePlane.lean, line 625](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SymmetricSquarePlane.lean#L625). The attribute's comment: “in characteristic 2 the functor is not representable on any category of schemes of finite type over k containing W and the principal opens of W and of Sym²(X)”.

> **Stacks Project, Remark 0H5Y, the characteristic `2` example.** Let `k` be a field of
> characteristic `2` and `X = A²_k`. On any full subcategory of the schemes of finite type over
> `k` containing `W = X ×_k X` and the principal open subschemes of `W` and of
> `Sym²(X) = W/⟨σ⟩`, the functor `S' ↦ z^eff(S' ×_k X / S', 0)` is not representable. Such is the
> category of weakly normal schemes of finite type over `k`
> (`Stacks.Chow.SymPlane.not_isRepresentable_weaklyNormal`), so replacing seminormality by weak
> normality does not make the functor representable when the base has points of positive
> characteristic.
>
> If `M` represented the functor, the cycle `α` would be a morphism `W ⟶ M` invariant under the
> involution `σ` exchanging the factors, because `α` is; near the generic point of the image of the
> diagonal it would factor through `W ⟶ Sym²(X)`, and the cycle `β` on `Sym²(X)` corresponding to
> the factorization would pull back to `α`. There is no such cycle
> (`Stacks.Chow.SymPlane.map_quotAway_ne`).

```lean
theorem not_isRepresentable_of_le (P : ObjectProperty (LocallyOfFiniteTypeOver (Spec (.of k))))
    (hW : P (squareObj k))
    (hP : ∀ h : sym k, h ≠ 0 → P (squareAwayObj k h) ∧ P (symAwayObj k h)) :
    ¬ (P.ι.op ⋙ effectiveRelativeCyclesFunctor (planeHom k) 0).IsRepresentable
```

**`Stacks.Chow.SymPlane.map_sym_diagonalRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SymmetricSquarePlane.lean, line 701](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SymmetricSquarePlane.lean#L701). The attribute's comment: “the image of the diagonal in Sym²(X) is V = Spec k[u₁², v₁²]”.

> **The image of the diagonal in `Sym²(X)` is `V = Spec k[u², v²]`**, in characteristic `2`:
> the coordinate ring of `Sym²(X)` restricts on the diagonal to `k[u², v²]`.

```lean
theorem map_sym_diagonalRestriction :
    (sym k).map (diagonalRestriction k) =
      Algebra.adjoin k {(X 0 : MvPolynomial (Fin 2) k) ^ 2, X 1 ^ 2}
```

**`Stacks.Chow.SymPlane.not_isRepresentable_weaklyNormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SymmetricSquarePlane.lean, line 827](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SymmetricSquarePlane.lean#L827). The attribute's comment: “in characteristic 2 the functor is not representable on the category of weakly normal schemes of finite type over k”.

> **Stacks Project, Remark 0H5Y, the characteristic `2` example, on weakly normal schemes.**
> Let `k` be a field of characteristic `2` and `X = A²_k`. Call a scheme weakly normal if every
> birational universal homeomorphism onto it has a section. On the category of weakly normal
> schemes of finite type over `k` the functor `S' ↦ z^eff(S' ×_k X / S', 0)` is not representable:
> `W = X ×_k X` is normal, hence weakly normal, `Sym²(X)` is normal, and so are their principal
> opens (`Stacks.Chow.SymPlane.not_isRepresentable_of_le`).

```lean
theorem not_isRepresentable_weaklyNormal :
    ¬ ((weaklyNormalOfFiniteType k).ι.op ⋙
      effectiveRelativeCyclesFunctor (planeHom k) 0).IsRepresentable
```

**`Stacks.Chow.SymPlane.mem_sym_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SymmetricSquarePlaneRing.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/SymmetricSquarePlaneRing.lean#L337). The attribute's comment: “Sym²(X) = W/⟨σ⟩ is the spectrum of k[u₁ + u₂, u₁u₂, v₁ + v₂, v₁v₂, u₁v₁ + u₂v₂]”.

> **The invariants of the swap.** In characteristic `2`, an element of `k[u₁, u₂, v₁, v₂]` is
> fixed by the involution exchanging the two factors exactly when it lies in
> `k[u₁ + u₂, u₁u₂, v₁ + v₂, v₁v₂, u₁v₁ + u₂v₂]`.

```lean
theorem mem_sym_iff (x : ring k) : x ∈ sym k ↔ swap k x = x
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 62.9, Tag 0H5Q](https://stacks.math.columbia.edu/tag/0H5Q)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
