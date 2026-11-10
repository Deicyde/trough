---
declaration: section
origin: cited
lean: Stacks.Chow.flatPullbackChow_surjective_isAffineSpaceBundle, Stacks.Chow.flatPullbackChow_surjective_of_isAffineSpaceBundle_unconditional, Stacks.Chow.flatPullbackChow_injective_of_gysinRetracts, Stacks.Chow.flatPullbackChow_totalSpaceToBase_bijective, Stacks.Chow.flatPullbackChow_bijective_vectorBundle_and_affineSpaceBundle, Stacks.Chow.flatPullbackChow_bijective_vectorBundleToBase, Stacks.Chow.flatPullbackChow_bijective_of_isAffineSpaceBundle, Stacks.LineBundle.Situation.isRelativeEffectiveCartierDivisor_ker_zeroSection
statement: formalized
proof: formalized
---

# 42.32 Affine bundles

Section 42.32 of the Stacks Project, [Tag 02TS](https://stacks.math.columbia.edu/tag/02TS). 8 tags here are carried by 20 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02TT, a lemma

[Tag 02TT](https://stacks.math.columbia.edu/tag/02TT) in the Stacks Project.

**`Stacks.Chow.flatPullbackChow_surjective_isAffineSpaceBundle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/AffineBundleSurjectivity.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/AffineBundleSurjectivity.lean#L149).

> Let `(S, δ)` be the base situation of chapter 42, let `X` and `Y` be locally of finite type
> over `S` and let `f : X ⟶ Y` be flat of relative dimension `r` such that every point of `Y` has
> an open neighbourhood `U` over which `f` is the projection `𝔸^r_U ⟶ U`. Then
> `f^* : A_k(Y) ⟶ A_{k+r}(X)` is surjective for every `k`.

```lean
theorem flatPullbackChow_surjective_isAffineSpaceBundle (C : ChowSituation.{u})
    {X Y : Scheme.{u}} (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (f : X ⟶ Y)
    [LocallyOfFiniteType f] [AlgebraicGeometry.Flat f] (r : ℕ)
    (hf : AlgebraicGeometry.RelativeDimension f r) (hbundle : IsAffineSpaceBundle f r) (k : ℤ) :
    Function.Surjective (flatPullbackChowOfRelativeDimension C (f ≫ sY) sY f rfl r hf k)
```

**`Stacks.Chow.flatPullbackChow_surjective_of_isAffineSpaceBundle_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/Unconditional.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/Unconditional.lean#L99).

> **Stacks 02TT.** Let `(S, δ)` be the base situation of chapter 42, let `X` and `Y` be locally
> of finite type over `S`, and let `f : X ⟶ Y` be flat of relative dimension `r` such that every
> point of `Y` has an open neighbourhood `U` over which `f` is identified with the projection
> `U × 𝔸^r ⟶ U`. Then `f^* : A_k(Y) ⟶ A_{k+r}(X)` is surjective for every `k ∈ ℤ`.

```lean
theorem flatPullbackChow_surjective_of_isAffineSpaceBundle_unconditional (C : ChowSituation.{u})
    {X Y : Scheme.{u}} (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (f : X ⟶ Y)
    [LocallyOfFiniteType f] [Flat f] (r : ℕ) (hf : AlgebraicGeometry.RelativeDimension f r)
    (hbundle : IsAffineSpaceBundle f r) (k : ℤ) :
    Function.Surjective (flatPullbackChow C (f ≫ sY) sY f rfl r hf k
      (flatPullbackFactorsThroughRationalEquivalence_general C (f ≫ sY) sY f rfl r hf k))
```

## Tag 0B74, a lemma

[Tag 0B74](https://stacks.math.columbia.edu/tag/0B74) in the Stacks Project.

**`Stacks.Chow.flatPullbackChow_injective_of_gysinRetracts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/LineBundleChow.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/LineBundleChow.lean#L292). The attribute's comment: “injectivity only, from the zero section and Stacks 02TR”.

> **Stacks 0B74, the injectivity half.** Let `(S, δ)` be as in Situation 02QL, let `X` be
> locally of finite type over `S`, let `ℒ` be an invertible `𝒪_X`-module and let
> `p : L = \underline{\Spec}(\Sym^*(ℒ)) ⟶ X` be the associated line bundle. Then
>
>   `p^* : A_k(X) ⟶ A_{k+1}(L)`
>
> is injective for every `k`.
>
> This is the source's argument: the zero section `o : X ⟶ L` satisfies `p ∘ o = 𝟙_X`
> (`Stacks.LineBundle.Situation.zeroSection_comp_totalSpaceToBase`) and its image is a relative
> effective Cartier divisor on `L/X`, so Stacks 02TR gives `o^* ∘ p^* = \mathrm{id}` and `p^*` is
> split injective. The retraction is `Stacks.Chow.gysin_flatPullbackChow_zeroSection`; the
> hypotheses `gysin` and `h02TR` are Stacks 02TR on Chow groups, and `hfac` is Stacks 02S1 at
> relative dimension one, both carried for the reasons recorded in the module documentation.

```lean
theorem flatPullbackChow_injective_of_gysinRetracts
    (h02TR : GysinRetractsFlatPullbackChow C sX (D.totalSpaceToBase ≫ sX) sX
      D.totalSpaceToBase rfl hp (𝟙 D.X) (Category.id_comp sX) (relativeDimension_identity D.X) k
      hfac (flatPullbackFactorsThroughRationalEquivalence_id C sX k) gysin) :
    Function.Injective
      (flatPullbackChow C (D.totalSpaceToBase ≫ sX) sX D.totalSpaceToBase rfl 1 hp k hfac)
```

**`Stacks.Chow.flatPullbackChow_totalSpaceToBase_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/LineBundleChowBijective.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/LineBundleChowBijective.lean#L59).

> Let `(S, δ)` be as in Situation 02QL, let `X` be locally of finite type over `S`, let `ℒ` be an
> invertible `𝒪_X`-module and let `p : L = \underline{\Spec}(\Sym^*(ℒ)) ⟶ X` be the associated line
> bundle. Then
>
>   `p^* : A_k(X) ⟶ A_{k+1}(L)`
>
> is an isomorphism for every `k`.

```lean
theorem flatPullbackChow_totalSpaceToBase_bijective (k : ℤ) :
    Function.Bijective
      (flatPullbackChowOfRelativeDimension C (D.totalSpaceToBase ≫ sX) sX D.totalSpaceToBase
        rfl 1 D.relativeDimension_totalSpaceToBase k)
```

## Tag 02TU, a remark

[Tag 02TU](https://stacks.math.columbia.edu/tag/02TU) in the Stacks Project.

**`Stacks.Chow.flatPullbackChow_bijective_vectorBundle_and_affineSpaceBundle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/BundlePullbackIsomorphism.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/BundlePullbackIsomorphism.lean#L63). The attribute's comment: “the whole remark: both assertions”.

> **Remark 02TU.** Let `(S, δ)` be as in Situation 02QL.
>
> 1. If `X` is locally of finite type over `S`, `ℰ` is a finite locally free `𝒪_X`-module of rank
>    `r` and `p : E ⟶ X` is its vector bundle, then `p^* : A_k(X) ⟶ A_{k+r}(E)` is an isomorphism
>    for every `k` (Lemma 02TY).
> 2. If `X`, `Y` are locally of finite type over `S` and `f : X ⟶ Y` is flat of relative dimension
>    `r` and Zariski-locally on `Y` the projection `U × 𝔸^r ⟶ U`, as in Lemma 02TT, then
>    `f^* : A_k(Y) ⟶ A_{k+r}(X)` is an isomorphism for every `k` (Remark 0GUB).

```lean
theorem flatPullbackChow_bijective_vectorBundle_and_affineSpaceBundle (C : ChowSituation.{u}) :
    (∀ {X : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (E : X.Modules)
      [E.IsQuasicoherent] (r : ℕ) [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E r]
      (k : ℤ),
      letI := locallyOfFiniteType_vectorBundleToBase E r
      letI := flat_vectorBundleToBase E r
      Function.Bijective (flatPullbackChowOfRelativeDimension C
        (Scheme.Modules.vectorBundleToBase X E ≫ sX) sX (Scheme.Modules.vectorBundleToBase X E)
        rfl r (relativeDimension_vectorBundleToBase E r) k)) ∧
    (∀ {X Y : Scheme.{u}} (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (f : X ⟶ Y)
      [LocallyOfFiniteType f] [Flat f] (r : ℕ) (hf : AlgebraicGeometry.RelativeDimension f r)
      (_ : IsAffineSpaceBundle f r) (k : ℤ),
      Function.Bijective (flatPullbackChowOfRelativeDimension C (f ≫ sY) sY f rfl r hf k))
```

Declarations registered for the tag:

- [`Stacks.Chow.flatPullbackChow_bijective_vectorBundleToBase`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/VectorBundleChowBijective.lean#L340), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/BundlePullbackIsomorphism.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/BundlePullbackIsomorphism.lean#L45) (StacksFrontier): “first assertion: flat pullback along the vector bundle of a finite locally free module of rank r is an isomorphism of Chow groups in every degree (Lemma 02TY)”.
- [`Stacks.Chow.flatPullbackChow_bijective_of_isAffineSpaceBundle`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AffineBundleInjective/Bijectivity.lean#L89), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/BundlePullbackIsomorphism.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/BundlePullbackIsomorphism.lean#L49) (StacksFrontier): “second assertion: flat pullback along a morphism which is Zariski-locally on the target the projection U × A^r to U is an isomorphism of Chow groups in every degree (Remark 0GUB); flatness and relative dimension r follow from the local triviality”.

## Tag 0F96, a lemma

[Tag 0F96](https://stacks.math.columbia.edu/tag/0F96) in the Stacks Project.

**`Stacks.LineBundle.Situation.isRelativeEffectiveCartierDivisor_ker_zeroSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/AffineSpaceBundleSmooth.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/AffineSpaceBundleSmooth.lean#L112). The attribute's comment: “(1), the zero section is a relative effective Cartier divisor”.

> **The image of the zero section of a line bundle is a relative effective Cartier divisor**,
> part of clause (1) of [Stacks, Tag 0F96]. The projection of the total space is smooth of relative
> dimension one, and the closed subscheme cut out by the zero section is finite locally free over
> the base because the projection restricts on it to the comparison isomorphism with the base; so
> [Stacks, Tag 0B9D] applies.

```lean
theorem Situation.isRelativeEffectiveCartierDivisor_ker_zeroSection (D : Situation.{u}) :
    Stacks.Divisors.IsRelativeEffectiveCartierDivisor D.totalSpaceToBase
      D.zeroSection.ker
```

**`Stacks.Chow.zeroSectionGysinChow`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/ZeroSectionGysin.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/ZeroSectionGysin.lean#L210). The attribute's comment: “part (3)”.

> **Stacks 0F96, clause (3).** The image `o(X)` of the zero section of a line bundle
> `p : L ⟶ X` is an effective Cartier divisor on `L`, so it has a Gysin map; composed with the
> identification of `o(X)` with `X` it is
>
>   `o^* : \CH_{k + 1}(L) ⟶ \CH_k(X)`.
>
> The divisor is presented as clause (1) presents it, the zero scheme of the tautological global
> section of `p^*(ℒ^{⊗ -1})`, and the Gysin map of a zero scheme is the unconditional
> [Stacks, Tag 02TO] on Chow groups. That the divisor is an effective Cartier divisor — the
> clause's justification — is
> `Stacks.LineBundle.Situation.isRelativeEffectiveCartierDivisor_zeroScheme_tautologicalSectionBase`;
> it is a theorem here and so is not taken as a hypothesis.

```lean
def zeroSectionGysinChow (k : ℤ) :
    chowGroup C (D.totalSpaceToBase ≫ sX) (k + 1) →+ chowGroup C sX k
```

**`Stacks.Chow.zeroSectionGysinChow_comp_flatPullbackChowOfRelativeDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/ZeroSectionGysinRetraction.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/ZeroSectionGysinRetraction.lean#L248). The attribute's comment: “part (4)”.

> **Stacks 0F96, clause (4).** The source's phrasing: the composite
>
>   `o^* p^* : \CH_k(X) ⟶ \CH_k(X)`
>
> *is* the identity map. This is
> `Stacks.Chow.zeroSectionGysinChow_flatPullbackChowOfRelativeDimension` read as an equality of
> homomorphisms; the two are interchangeable, both sides of the equality being determined by their
> values.

```lean
theorem zeroSectionGysinChow_comp_flatPullbackChowOfRelativeDimension (k : ℤ) :
    (zeroSectionGysinChow C D sX k).comp
        (flatPullbackChowOfRelativeDimension C (D.totalSpaceToBase ≫ sX) sX D.totalSpaceToBase
          rfl 1 D.relativeDimension_totalSpaceToBase k) =
      AddMonoidHom.id (chowGroup C sX k)
```

**`Stacks.Chow.zeroSectionChowPushforward_eq_neg_flatPullbackChow_firstChernClassCapChow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/ZeroSectionProjectionFormula.lean, line 352](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/ZeroSectionProjectionFormula.lean#L352). The attribute's comment: “part (5)”.

> Let `(S, δ)` be the base situation of chapter 42, let `X` be locally of finite type over `S`,
> let `ℒ` be an invertible `𝒪_X`-module and let `p : L ⟶ X` be the associated line bundle with
> zero section `o : X ⟶ L`. Then
>
>   `o_* α = - p^*(c₁(ℒ) ∩ α)`  in  `A_{k+1}(L)`  for every  `α ∈ A_{k+1}(X)`.
>
> Here `c₁(ℒ) ∩ -` on `A_{k+1}(X)` is `firstChernClassCapChow C k`, and the flat pullback, which
> lands in `A_{k + ((1 : ℕ) : ℤ)}(L)`, is transported to `A_{k+1}(L)` by
> `Stacks.Chow.chowGroupCast`.

```lean
theorem zeroSectionChowPushforward_eq_neg_flatPullbackChow_firstChernClassCapChow (k : ℤ)
    (α : chowGroup C sX (k + 1)) :
    zeroSectionChowPushforward C D sX (k + 1) α =
      -chowGroupCast C (D.totalSpaceToBase ≫ sX)
        (show k + ((1 : ℕ) : ℤ) = k + 1 from by simp)
        (flatPullbackChowOfRelativeDimension C (D.totalSpaceToBase ≫ sX) sX D.totalSpaceToBase
          rfl 1 D.relativeDimension_totalSpaceToBase k (firstChernClassCapChow C k sX D.L α))
```

**`Stacks.Chow.zeroSectionChowPushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/ZeroSectionPushforward.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/ZeroSectionPushforward.lean#L64). The attribute's comment: “part (2)”.

> The proper pushforward on Chow groups along the zero section `o : X ⟶ L` of a line bundle,
>
> `o_* : \CH_k(X) ⟶ \CH_k(L)`.

```lean
def zeroSectionChowPushforward (k : ℤ) :
    chowGroup C sX k →+ chowGroup C (D.totalSpaceToBase ≫ sX) k
```

**`Stacks.Chow.zeroSectionGysinChow_zeroSectionChowPushforward_mk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/ZeroSectionSelfIntersection.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/ZeroSectionSelfIntersection.lean#L239). The attribute's comment: “part (6)”. References: SGA 5 VII (9.2), “special case”.

> **Stacks 0F96, clause (6).** The Gysin map of the zero section of a line bundle `p : L ⟶ X`
> composed with the pushforward along it is intersection with the first Chern class of `ℒ`, with a
> minus sign:
>
>   `o^* o_* α = - c₁(ℒ) ∩ α`,
>
> a map `\CH_{k+1}(X) ⟶ \CH_k(X)`.
>
> Both maps of the composite are the maps of clauses (2) and (3),
> `Stacks.Chow.zeroSectionChowPushforward` and `Stacks.Chow.zeroSectionGysinChow`, and the only
> hypothesis is theirs, that `X` be locally of finite type over `S`. The right hand side is the cap
> product of [Stacks, Tag 02SO] on a cycle representative, which is what makes it unconditional;
> see the module documentation.
>
> The proof is the source's: the self-intersection formula [Stacks, Tag 0F95] for the divisor
> `o(X)` on `L`, whose module is `p^*(ℒ^{⊗ -1})` by clause (1), followed by the identification of
> the restriction of that module with `ℒ^{⊗ -1}` and by [Stacks, Tag 02SP] in the form
> `c₁(ℒ^{⊗ -1}) ∩ α = -(c₁(ℒ) ∩ α)`, which is where the sign comes from.

```lean
theorem zeroSectionGysinChow_zeroSectionChowPushforward_mk (k : ℤ)
    (α : CycleGroup C sX (k + 1)) :
    zeroSectionGysinChow C D sX k
        (zeroSectionChowPushforward C D sX (k + 1)
          (QuotientAddGroup.mk' (rationalEquivalences C sX (k + 1)) α)) =
      -firstChernClassCapOfInvertible C sX k D.L α
```

**`Stacks.Chow.zeroSectionGysinChow_comp_zeroSectionChowPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/ZeroSectionSelfIntersection.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/ZeroSectionSelfIntersection.lean#L328). The attribute's comment: “part (6)”.

> **Stacks 0F96, clause (6).** The source's phrasing: the composite
>
>   `o^* o_* : \CH_{k+1}(X) ⟶ \CH_k(X)`
>
> *is* the map `α ↦ - c₁(ℒ) ∩ α`, as an equality of homomorphisms read on cycle representatives.
> Every Chow class is the class of a cycle, so this and
> `Stacks.Chow.zeroSectionGysinChow_zeroSectionChowPushforward_mk` are interchangeable.

```lean
theorem zeroSectionGysinChow_comp_zeroSectionChowPushforward (k : ℤ) :
    ((zeroSectionGysinChow C D sX k).comp
          (zeroSectionChowPushforward C D sX (k + 1))).comp
        (QuotientAddGroup.mk' (rationalEquivalences C sX (k + 1))) =
      -firstChernClassCapOfInvertible C sX k D.L
```

**`Stacks.LineBundle.Situation.isRegularSection_tautologicalSectionBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LineBundle/TautologicalSectionBaseRegular.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LineBundle/TautologicalSectionBaseRegular.lean#L54). The attribute's comment: “part (1), the section is regular”.

> The tautological global section of `p^*(L^{⊗ -1})` is a regular section, that is,
> multiplication by it is injective.

```lean
theorem Situation.isRegularSection_tautologicalSectionBase :
    AlgebraicGeometry.IsRegularSection D.totalSpace.sheaf.obj
      D.totalSpace.ringCatSheaf.property D.tautologicalSectionBaseSections
```

**`Stacks.LineBundle.Situation.zeroScheme_tautologicalSectionBase_eq_ker_zeroSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LineBundle/ZeroSectionZeroScheme.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LineBundle/ZeroSectionZeroScheme.lean#L190). The attribute's comment: “part (1), the zero scheme”.

> **Clause (1) of [Stacks, Tag 0F96], the zero scheme.** Let `L` be an invertible module on a
> scheme `X`, let `p : Tot(L) ⟶ X` be the associated line bundle and let `o : X ⟶ Tot(L)` be its
> zero section. Then the closed subscheme `o(X)` of `Tot(L)` is the zero scheme of the tautological
> global section of `p^*(L^{⊗ -1})`.
>
> The hypotheses of [Stacks, Tag 0B74] that `X` be locally of finite type over a base scheme with
> a dimension function are not needed and are omitted: clause (1) is a statement about the line
> bundle alone.

```lean
theorem Situation.zeroScheme_tautologicalSectionBase_eq_ker_zeroSection :
    Stacks.Divisors.zeroScheme D.totalSpace D.basePullbackInverse D.tautologicalSectionBase =
      D.zeroSection.ker
```

**`Stacks.LineBundle.Situation.isRegularSection_tautologicalSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LineBundle/ZeroSectionZeroScheme.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LineBundle/ZeroSectionZeroScheme.lean#L214). The attribute's comment: “part (1), the section is regular”.

> **Clause (1) of [Stacks, Tag 0F96], regularity of the section.** The tautological global
> section of `p^*(L^{⊗ -1})` is a regular section, that is, multiplication by it is injective:
> its zero scheme is the image of the zero section, which is an effective Cartier divisor on the
> total space by [Stacks, Tag 0B9D].

```lean
theorem Situation.isRegularSection_tautologicalSection :
    AlgebraicGeometry.IsRegularSection D.totalSpace.sheaf.obj
      D.totalSpace.ringCatSheaf.property
      (SheafOfModules.unitHomEquiv D.pullbackInverse D.tautologicalSectionHom)
```

## Tag 0F97, a lemma

[Tag 0F97](https://stacks.math.columbia.edu/tag/0F97) in the Stacks Project.

**`Stacks.Chow.TensorZeroScheme.pullbackTensorSection_proj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TensorZeroScheme/Basic.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TensorZeroScheme/Basic.lean#L279). The attribute's comment: “the construction and conditions (1), (3); (2) and (4)-(7) not proved here”.

> The pullback `p^*s` of the section to the zero scheme `L` of `z₁ ⊗ z₂ - q^*s`, read in
> `p^*L₁ ⊗ p^*L₂`, is the product `s₁ ⊗ s₂` of the two restricted fibre coordinates.

```lean
theorem pullbackTensorSection_proj :
    pullbackTensorSection (proj Y L₁ L₂ s) L₁ L₂ s =
      tensorSectionsAt (spaceIdeal Y L₁ L₂ s).subscheme.sheaf.obj
        (spaceIdeal Y L₁ L₂ s).subscheme.ringCatSheaf.property (op ⊤)
        ((Scheme.Modules.pullback (proj Y L₁ L₂ s)).obj L₁)
        ((Scheme.Modules.pullback (proj Y L₁ L₂ s)).obj L₂)
        (section₁ Y L₁ L₂ s) (section₂ Y L₁ L₂ s)
```

**`Stacks.Chow.TensorZeroScheme.exists_decomposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TensorZeroScheme/DecompositionExistence.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TensorZeroScheme/DecompositionExistence.lean#L100).

> **[Stacks, Tag 0F97].** Let `Y` be a scheme, `L₁`, `L₂` invertible `𝒪_Y`-modules, `s` a
> global section of `L₁ ⊗ L₂` and `i : D → Y` its zero scheme. There is a commutative diagram
> `D₁ → L ← D₂` over `D → Y ← D`, with `p : L ⟶ Y`, and sections `sᵢ` of `p^*Lᵢ` such that
> `p^*s = s₁ ⊗ s₂`; `p` is of finite type and flat of relative dimension `1`; `Dᵢ` is the zero
> scheme of `sᵢ`; `Dᵢ ≅ \underline{\Spec}(\Sym^*(L_{3-i}^{⊗ -1})|_D)` over `D`;
> `p^{-1}D = D₁ ∪ D₂`; `D₁ ∩ D₂ ⟶ D` is an isomorphism; and `D₁ ∩ D₂ ⟶ Dᵢ` is the zero section of
> the line bundle `Dᵢ ⟶ D` (the record `Stacks.Chow.TensorZeroScheme.Decomposition`). Moreover the
> formation of the diagram and of the sections commutes with arbitrary base change
> (`Stacks.Chow.TensorZeroScheme.Decomposition.IsStableUnderBaseChange`).

```lean
theorem exists_decomposition : ∃ R : Decomposition Y L₁ L₂ s, R.IsStableUnderBaseChange
```

## Tag 0F98, a lemma

[Tag 0F98](https://stacks.math.columbia.edu/tag/0F98) in the Stacks Project.

**`Stacks.Chow.TensorZeroScheme.gysinChowBranch₁_flatPullbackChowProj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/ZeroSectionBranchChowIdentity.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AffineBundle/ZeroSectionBranchChowIdentity.lean#L200).

> In the situation of [Stacks, Tag 0F97],
>
> `i₁^* p^* α = p₁^* i^* α`  in  `A_{k+1}(D₁)`  for every  `α ∈ A_{k+1}(Y)`.

```lean
theorem gysinChowBranch₁_flatPullbackChowProj (α : Stacks.Chow.chowGroup C sY (k + 1)) :
    gysinChowBranch₁ C Y L₁ L₂ s R sY (k + 1)
        (flatPullbackChowProj C Y L₁ L₂ s R sY (k + 1) α) =
      flatPullbackChowProj₁ C Y L₁ L₂ s R sY k (gysinChowZeroIdeal C Y L₁ L₂ s sY k α)
```

## Tag 0F99, a lemma

[Tag 0F99](https://stacks.math.columbia.edu/tag/0F99) in the Stacks Project.

**`Stacks.Chow.TensorZeroScheme.exists_principalReduction_isStableUnderBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TensorZeroScheme/PrincipalReductionExistence.lean, line 531](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TensorZeroScheme/PrincipalReductionExistence.lean#L531).

> **[Stacks, Tag 0F99].** For a scheme `X` locally of finite type over the base situation of
> chapter 42 and a triple `(ℒ, s, i : D ⟶ X)` as in [Stacks, Tag 02T8] there is a commutative
> square
>
>   `D' --i'--> X'`
>   `|p         |g`
>   `D --i-->   X`
>
> such that `p` and `g` are of finite type and flat of relative dimension `1`,
> `p^* : A_k(D) ⟶ A_{k+1}(D')` is injective for all `k`, `D' ⊆ X'` is the zero scheme of a
> global section of `𝒪_{X'}`, and `p^*i^* = (i')^*g^*`; and these properties remain true after
> arbitrary base change by morphisms `Y ⟶ X` locally of finite type.

```lean
theorem exists_principalReduction_isStableUnderBaseChange :
    ∃ R : PrincipalReduction C sX L s, R.IsStableUnderBaseChange
```

## Tag 0GUB, a remark

[Tag 0GUB](https://stacks.math.columbia.edu/tag/0GUB) in the Stacks Project.

**`Stacks.Chow.flatPullbackChow_bijective_of_isAffineSpaceBundle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AffineBundleInjective/Bijectivity.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AffineBundleInjective/Bijectivity.lean#L89).

> **Stacks 0GUB.** Let `(S, δ)` be as in Situation 02QL, let `Y` be locally of finite type over
> `S`, let `r ≥ 0` and let `f : X ⟶ Y` be a morphism of schemes such that every point of `Y` lies in
> an open `V ⊆ Y` with `f⁻¹(V) ≅ V × 𝔸^r` as schemes over `V`. Then flat pullback
>
>   `f^* : CH_k(Y) ⟶ CH_{k+r}(X)`
>
> is an isomorphism for every `k`. The morphism `f` is locally of finite type, flat and of relative
> dimension `r` because it is so locally on `Y`; these are not hypotheses but consequences of the
> local triviality, recorded through `letI`.

```lean
theorem flatPullbackChow_bijective_of_isAffineSpaceBundle (C : ChowSituation.{u})
    {X Y : Scheme.{u}} (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (f : X ⟶ Y) (r : ℕ)
    (hbundle : IsAffineSpaceBundle f r) (k : ℤ) :
    letI := locallyOfFiniteType_of_isAffineSpaceBundle f r hbundle
    letI := flat_of_isAffineSpaceBundle f r hbundle
    Function.Bijective (flatPullbackChowOfRelativeDimension C (f ≫ sY) sY f rfl r
      (relativeDimension_of_isAffineSpaceBundle f r hbundle) k)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.32, Tag 02TS](https://stacks.math.columbia.edu/tag/02TS)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
