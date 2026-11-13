---
declaration: section
origin: cited
lean: Stacks.Chow.exteriorProductDedekindTensor, Stacks.Chow.existsUnique_exteriorProductDedekindChowTensor, Stacks.Chow.IsDedekindChowBase.exteriorProductFactorsThroughRationalEquivalence, Stacks.Chow.IsDedekindChowBase.exteriorProductChow, Stacks.Chow.bivariantChowClassCapBaseFundamentalClass_bijective, Stacks.Chow.chowCohomologyDedekindEquiv, Stacks.Chow.bivariantCapBaseFundamentalClass_bijective, Stacks.Chow.bivariantCapBaseFundamentalClassEquiv
statement: formalized
proof: formalized
---

# 42.63 Exterior product over Dedekind domains

Section 42.63 of the Stacks Project, [Tag 0FC3](https://stacks.math.columbia.edu/tag/0FC3). 5 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FC4, a lemma

[Tag 0FC4](https://stacks.math.columbia.edu/tag/0FC4) in the Stacks Project.

**`Stacks.Chow.exteriorProductDedekindTensor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductDedekind/ChowGroups.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductDedekind/ChowGroups.lean#L147). The attribute's comment: “the map CH\_n(X) ⊗\_ℤ CH\_m(Y) → CH\_\{n+m-1}(X ×\_S Y) is well defined, given that the cycle-level exterior product carries rational equivalences to rational equivalences in each variable (the step the source proves with the bivariant classes of Stacks 0B78, 0B79 and 0B75, none of which is in this repository)”.

> The exterior product over a Dedekind base as a map out of the tensor product,
>
>   `× : CH_n(X) ⊗_ℤ CH_m(Y) ⟶ CH_{n+m-1}(X ×_S Y)`,
>
> determined by `[X'] ⊗ [Y'] ↦ [X' ×_S Y']_{n+m-1}` on integral closed subschemes `X' ⊆ X` and
> `Y' ⊆ Y` of delta-dimensions `n` and `m` with one of them dominating an irreducible component of
> the base, and by `[X'] ⊗ [Y'] ↦ 0` when neither does, given that the cycle-level exterior
> product respects rational equivalence in each variable (`hfac`).

```lean
def exteriorProductDedekindTensor :
    TensorProduct ℤ (chowGroup C f n) (chowGroup C g m) →+
      chowGroup C (pullback.fst f g ≫ f) (n + m - 1)
```

**`Stacks.Chow.existsUnique_exteriorProductDedekindChowTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductDedekind/RationalEquivalence.lean, line 927](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductDedekind/RationalEquivalence.lean#L927).

> Let `(S, δ)` be as in Stacks section 42.63 — locally the spectrum of a Dedekind domain, with
> `δ = 0` at closed points and `δ = 1` elsewhere — and let `X`, `Y` be locally of finite type over
> `S`. The map `× : CH_n(X) ⊗_ℤ CH_m(Y) ⟶ CH_{n+m-1}(X ×_S Y)` is well defined: there is exactly
> one additive map out of the tensor product sending `[α] ⊗ [β]` to the class of the exterior
> product `α × β` of the two cycles.

```lean
theorem existsUnique_exteriorProductDedekindChowTensor (hC : IsDedekindChowBase C) :
    ∃! F : TensorProduct ℤ (chowGroup C f n) (chowGroup C g m) →+
        chowGroup C (pullback.fst f g ≫ f) (n + m - 1),
      ∀ (α : CycleGroup C f n) (β : CycleGroup C g m),
        F (TensorProduct.tmul ℤ (QuotientAddGroup.mk' (rationalEquivalences C f n) α)
            (QuotientAddGroup.mk' (rationalEquivalences C g m) β)) =
          QuotientAddGroup.mk' (rationalEquivalences C (pullback.fst f g ≫ f) (n + m - 1))
            (exteriorProductDedekindCycles C f g n m α β)
```

**`Stacks.Chow.IsDedekindChowBase.exteriorProductFactorsThroughRationalEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductDedekind/RespectsRationalEquivalence.lean, line 1224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductDedekind/RespectsRationalEquivalence.lean#L1224). The attribute's comment: “the exterior product of cycles over a Dedekind base is compatible with rational equivalence in each variable; the source's bivariant classes `i_* ∘ (p')^*` and `i_* ∘ (p')^* ∘ c` are read on cycles as a flat pullback and a flat pullback of the Gysin map of a principal divisor with trivial normal bundle”.

> **Stacks 0FC4.** Over a Dedekind base the exterior product of cycles carries rational
> equivalences to rational equivalences in each variable, for all `X`, `Y` locally of finite type
> over the base and all `n`, `m`. This discharges the hypothesis of
> `Stacks.Chow.exteriorProductDedekindTensor`.

```lean
theorem IsDedekindChowBase.exteriorProductFactorsThroughRationalEquivalence
    (hS : IsDedekindChowBase C) : ExteriorProductFactorsThroughRationalEquivalence C f g n m
```

**`Stacks.Chow.IsDedekindChowBase.exteriorProductChow`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductDedekind/RespectsRationalEquivalence.lean, line 1242](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductDedekind/RespectsRationalEquivalence.lean#L1242). The attribute's comment: “the map CH\_n(X) ⊗\_ℤ CH\_m(Y) → CH\_\{n+m-1}(X ×\_S Y) is well defined, unconditionally”.

> **Stacks 0FC4.** The exterior product on Chow groups over a Dedekind base,
>
>   `× : CH_n(X) ⊗_ℤ CH_m(Y) ⟶ CH_{n+m-1}(X ×_S Y)`,
>
> well defined with no hypothesis beyond the base being as in Stacks section 42.63. It is
> `Stacks.Chow.exteriorProductDedekindTensor` with its compatibility with rational equivalence
> supplied by `Stacks.Chow.IsDedekindChowBase.exteriorProductFactorsThroughRationalEquivalence`; on
> a pure tensor of the classes of integral closed subschemes `X'` and `Y'` of delta-dimensions `n`
> and `m` it is the class of `[X' ×_S Y']_{n+m-1}` when one of them dominates an irreducible
> component of the base and zero otherwise.

```lean
def IsDedekindChowBase.exteriorProductChow (hS : IsDedekindChowBase C) :
    TensorProduct ℤ (chowGroup C f n) (chowGroup C g m) →+
      chowGroup C (pullback.fst f g ≫ f) (n + m - 1)
```

## Tag 0FC5, a lemma

[Tag 0FC5](https://stacks.math.columbia.edu/tag/0FC5) in the Stacks Project.

**`Stacks.Chow.bivariantChowClassCapBaseFundamentalClass_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductDedekind/ChowCohomology.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductDedekind/ChowCohomology.lean#L120). The attribute's comment: “the canonical map A^p(X → S) → CH\_\{1-p}(X), c ↦ c ∩ [S]₁, is bijective; the components of S are curves, as in Example 02QN (for S the spectrum of a field the statement fails)”.

> **Bivariant classes towards a Dedekind base are Chow classes.** Let `(S, δ)` be as in Stacks
> section 42.63 — locally the spectrum of a Dedekind domain, with `δ = 0` at the closed points and
> `δ = 1` elsewhere — every irreducible component of `S` being of dimension one, and let `X` be a
> scheme locally of finite type over `S`. For every `p ∈ ℤ` the canonical map
> `A^p(X ⟶ S) ⟶ CH_{1-p}(X)`, `c ↦ c ∩ [S]₁`, is bijective. Here `A^p(X ⟶ S)` is the group of
> bivariant classes of Stacks 0B76 for the structure morphism of `X`, and `c ∩ [S]₁` is read on `X`
> through `X ×_S S ≅ X`.

```lean
theorem bivariantChowClassCapBaseFundamentalClass_bijective :
    Function.Bijective (bivariantChowClassCapBaseFundamentalClass sX p)
```

**`Stacks.Chow.chowCohomologyDedekindEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductDedekind/ChowCohomology.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductDedekind/ChowCohomology.lean#L134). The attribute's comment: “the canonical identification A^p(X → S) = CH\_\{1-p}(X) as an isomorphism of groups, c ↦ c ∩ [S]₁, with inverse α ↦ c\_α; the components of S are curves, as in Example 02QN”.

> The canonical identification `A^p(X ⟶ S) = CH_{1-p}(X)` over a Dedekind base whose
> irreducible components are curves, as an isomorphism of groups: `c ↦ c ∩ [S]₁`. Its inverse
> sends `α` to the class `c_α` with `c_α ∩ α' = α × α'` (`chowCohomologyDedekindEquiv_symm`).

```lean
def chowCohomologyDedekindEquiv (p : ℤ) (hC : IsDedekindChowBase C)
    (hdim : ∀ Z : irreducibleComponents C.S, topologicalKrullDim (Z : Set C.S) = 1) :
    BivariantChowClass C sX (𝟙 C.S) sX (Category.comp_id sX) p ≃+ chowGroup C sX (1 - p)
```

**`Stacks.Chow.bivariantCapBaseFundamentalClass_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductDedekindBivariantIdentification.lean, line 1130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductDedekindBivariantIdentification.lean#L1130). The attribute's comment: “corrected form: the base is assumed to have no zero-dimensional component (`Stacks.Chow.HasNoZeroDimensionalComponent`, every closed point a proper specialization); the source admits such components, a field being a Dedekind domain, and for `S = Spec k` the map `c ↦ c ∩ [S]₁` is zero while `A^0(S → S)` contains `1`. Bivariant classes are those of the Gysin system of invertible modules, `Stacks.Chow.gysinSystemOfInvertible`”.

> **Stacks 0FC5**, corrected form. Let `(S, δ)` be a base as in section 42.63 of the Stacks
> Project with no zero-dimensional component, and let `X` be locally of finite type over `S`. Then
> `c ↦ c ∩ [S]₁` is a bijection `A^p(X → S) → CH_{1-p}(X)` for every `p ∈ ℤ`.
>
> The hypothesis `hS1` is the correction. A field is a Dedekind domain, so the source's statement
> also admits a component `Spec k` of `S` with `δ ≡ 0`, and there it fails: `[S]₁` restricts to
> `[Spec k]₁ = 0`, so the map kills the nonzero class `1 ∈ A^0(Spec k → S)`.

```lean
theorem bivariantCapBaseFundamentalClass_bijective (hS : IsDedekindChowBase C)
    (hS1 : HasNoZeroDimensionalComponent C) :
    Function.Bijective
      (bivariantCapBaseFundamentalClass C (gysinSystemOfInvertible C) sX p)
```

**`Stacks.Chow.bivariantCapBaseFundamentalClassEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductDedekindBivariantIdentification.lean, line 1142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductDedekindBivariantIdentification.lean#L1142). The attribute's comment: “corrected form: the base is assumed to have no zero-dimensional component (`Stacks.Chow.HasNoZeroDimensionalComponent`); the identification A^p(X → S) = CH\_\{1-p}(X) as an isomorphism of groups, at the Gysin system of invertible modules”.

> **Stacks 0FC5**, corrected form, as an isomorphism of groups: over a base as in section 42.63
> with no zero-dimensional component, `A^p(X → S) ≃+ CH_{1-p}(X)`, `c ↦ c ∩ [S]₁`.

```lean
def bivariantCapBaseFundamentalClassEquiv (hS : IsDedekindChowBase C)
    (hS1 : HasNoZeroDimensionalComponent C) :
    BivariantClass C (gysinSystemOfInvertible C) sX (𝟙 C.S) sX (Category.comp_id sX) p ≃+
      chowGroup C sX (1 - p)
```

**`Stacks.Chow.exists_isExteriorProductOverBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductDedekindRepresentation/InverseMap.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductDedekindRepresentation/InverseMap.lean#L116). The attribute's comment: “corrected form: the inverse α ↦ c\_α acts by exterior product, c\_α ∩ α' = α × α'”.

> **Stacks 0FC5, the inverse map**, corrected form. Over a base as in section 42.63 with no
> zero-dimensional component, every `α ∈ CH_{1-p}(X)` is `c_α ∩ [S]₁` for a bivariant class
> `c_α ∈ A^p(X → S)` acting by exterior product with `α`, `c_α ∩ α' = α × α'`; by
> `Stacks.Chow.bivariantCapBaseFundamentalClass_injective` it is unique.

```lean
theorem exists_isExteriorProductOverBase (hS : IsDedekindChowBase C)
    (hS1 : HasNoZeroDimensionalComponent C) (α : chowGroup C sX (1 - p)) :
    ∃ c : BivariantClass C (gysinSystemOfInvertible C) sX (𝟙 C.S) sX (Category.comp_id sX) p,
      IsExteriorProductOverBase C (gysinSystemOfInvertible C) sX (1 - p) p α c ∧
        bivariantCapBaseFundamentalClass C (gysinSystemOfInvertible C) sX p c = α
```

## Tag 0FC6, a lemma

[Tag 0FC6](https://stacks.math.columbia.edu/tag/0FC6) in the Stacks Project.

**`Stacks.Chow.bivariantCommuteOverBase_of_isChowOperationGenerated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/CommuteOverDedekindBase.lean, line 515](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/CommuteOverDedekindBase.lean#L515). The attribute's comment: “the commutation c ∘ c' = c' ∘ c, read on the cap operations of the two composites, for c an integral combination of flat pullbacks towards the base, the generators of the presentation in the proof of Stacks 0FC5 other than proper pushforwards and Gysin maps; given Stacks 02S1 for every flat morphism over the base”.

> **Stacks 0FC6.** Let `(S, δ)` be as in Stacks section 42.63, let `X` be a scheme locally of
> finite type over `S` and let `c ∈ A^p(X ⟶ S)`. Let `Y ⟶ Z` be a morphism of schemes locally of
> finite type over `S` and let `c' ∈ A^q(Y ⟶ Z)`. Then `c ∘ c' = c' ∘ c`: capping with `c` and
> capping with `c'` may be performed in either order, the two results being read on the two
> iterated fibre products `X ×_S (Y ×_Z T)` and `Y ×_Z (X ×_S T)` of a test scheme through the
> canonical comparison isomorphism.

```lean
theorem bivariantCommuteOverBase_of_isChowOperationGenerated
    (hfd : ∀ {A B : Scheme.{u}} (sA : A ⟶ C.S) [LocallyOfFiniteType sA]
      (sB : B ⟶ C.S) [LocallyOfFiniteType sB] (v : A ⟶ B) [LocallyOfFiniteType v] [Flat v]
      (hv : v ≫ sB = sA) (r : ℕ) (hr : AlgebraicGeometry.RelativeDimension v r) (k : ℤ),
      FlatPullbackFactorsThroughRationalEquivalence C sA sB v hv r hr k)
    (hgen : IsChowOperationGenerated C G sX p c) :
    BivariantCommuteOverBase C G sX sZ w p q c c'
```

**`Stacks.Chow.bivariantCommuteOverBase_of_isDedekindChowBase_general`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/CommuteOverDedekindBaseGeneral.lean, line 821](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/CommuteOverDedekindBaseGeneral.lean#L821). The attribute's comment: “the commutation c ∘ c' = c' ∘ c read on the cap operations of the two composites (`Stacks.Chow.BivariantCommuteOverBase`), for the bivariant classes of the Gysin system of invertible modules `Stacks.Chow.gysinSystemOfInvertible`”.

> Let `(S, δ)` be as in section 42.63 of the Stacks Project, let `X` be a scheme locally of
> finite type over `S` and let `c ∈ A^p(X ⟶ S)`. Let `Y ⟶ Z` be a morphism of schemes locally of
> finite type over `S` and let `c' ∈ A^q(Y ⟶ Z)`. Then `c ∘ c' = c' ∘ c`:
> capping with `c` and capping with `c'` may be performed in either order, the two results being
> read on `X ×_S (Y ×_Z T)` and `Y ×_Z (X ×_S T)` through the canonical comparison isomorphism.

```lean
theorem bivariantCommuteOverBase_of_isDedekindChowBase_general (hS : IsDedekindChowBase C)
    {Y Z : Scheme.{u}} (sZ : Z ⟶ C.S) [LocallyOfFiniteType sZ] (w : Y ⟶ Z)
    [LocallyOfFiniteType w] (q : ℤ)
    (c : BivariantClass C (gysinSystemOfInvertible C) sX (𝟙 C.S) sX (Category.comp_id sX) p)
    (c' : BivariantClass C (gysinSystemOfInvertible C) (w ≫ sZ) sZ w rfl q) :
    BivariantCommuteOverBase C (gysinSystemOfInvertible C) sX sZ w p q c c'
```

**`Stacks.Chow.bivariantCommuteOverBase_of_isChowOperationProperGenerated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/CommuteOverDedekindBaseProper.lean, line 365](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/CommuteOverDedekindBaseProper.lean#L365). The attribute's comment: “the commutation c ∘ c' = c' ∘ c, read on the cap operations of the two composites, for a c in the subgroup of A^p(X ⟶ S) generated by the flat pullbacks towards the base and by their proper pushforwards: of the generators the proof of Stacks 0FC5 exhibits this covers flat pullback, proper pushforward and integral combinations and not the Gysin maps; given Stacks 02S1 for flat and 02S2 for proper maps over the base”.

> **Stacks 0FC6.** Let `(S, δ)` be as in Stacks section 42.63, let `X` be a scheme locally of
> finite type over `S` and let `c ∈ A^p(X ⟶ S)`. Let `Y ⟶ Z` be a morphism of schemes locally of
> finite type over `S` and let `c' ∈ A^q(Y ⟶ Z)`. Then `c ∘ c' = c' ∘ c`: capping with `c` and
> capping with `c'` may be performed in either order, the two results being read on the two
> iterated fibre products `X ×_S (Y ×_Z T)` and `Y ×_Z (X ×_S T)` of a test scheme through the
> canonical comparison isomorphism.

```lean
theorem bivariantCommuteOverBase_of_isChowOperationProperGenerated
    (hfd : ∀ {A B : Scheme.{u}} (sA : A ⟶ C.S) [LocallyOfFiniteType sA]
      (sB : B ⟶ C.S) [LocallyOfFiniteType sB] (v : A ⟶ B) [LocallyOfFiniteType v] [Flat v]
      (hv : v ≫ sB = sA) (r : ℕ) (hr : AlgebraicGeometry.RelativeDimension v r) (k : ℤ),
      FlatPullbackFactorsThroughRationalEquivalence C sA sB v hv r hr k)
    (hgen : IsChowOperationProperGenerated C G hpp sX p c) :
    BivariantCommuteOverBase C G sX sZ w p q c c'
```

**`Stacks.Chow.BivariantChowClass.comp_comm_of_isDedekindChowBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductDedekind/CommuteCompositeGeneral.lean, line 304](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductDedekind/CommuteCompositeGeneral.lean#L304). The attribute's comment: “c ∘ c' = c' ∘ c in A^\{p+q}(X ×\_S Y → Z) for c ∈ A^p(X → S) and c' ∈ A^q(Y → Z), the composites read as in Stacks 0FA2”.

> **Stacks 0FC6.** Let `(S, δ)` be as in Stacks section 42.63 — locally the spectrum of a
> Dedekind domain, with `δ = 0` at the closed points and `δ = 1` elsewhere. Let `X` be a scheme
> locally of finite type over `S` and `c ∈ A^p(X ⟶ S)`. Let `f : Y ⟶ Z` be a morphism of schemes
> locally of finite type over `S` and `c' ∈ A^q(Y ⟶ Z)`. Then `c ∘ c' = c' ∘ c` in
> `A^{p+q}(X ×_S Y ⟶ Z)`.
>
> Here `c ∘ c' = res(c) ∘ c'` with `res(c) ∈ A^p(X ×_S Y ⟶ Y)` the restriction of `c` along
> `Y ⟶ S`, and `c' ∘ c = res(c') ∘ res(c)` with `res(c) ∈ A^p(X ×_S Z ⟶ Z)` the restriction of `c`
> along `Z ⟶ S` and `res(c') ∈ A^q(Y ×_Z (X ×_S Z) ⟶ X ×_S Z)` the restriction of `c'` along
> `X ×_S Z ⟶ Z` (Stacks 0F9Z, 0FA2). The second composite lives on `Y ×_Z (X ×_S Z)` and in degree
> `q + p`; it is read on `X ×_S Y` through the canonical isomorphism and in degree `p + q`.

```lean
theorem BivariantChowClass.comp_comm_of_isDedekindChowBase (hC : IsDedekindChowBase C)
    (c : BivariantChowClass C sX (𝟙 C.S) sX (Category.comp_id sX) p)
    (c' : BivariantChowClass C sY sZ f hf q) :
    (c.restrict sY (Category.comp_id sY)).comp c' =
      (((c'.restrict (pullback.snd sX sZ)
          (BivariantChowClass.restrict_structure_eq (Category.comp_id sX) sZ
            (Category.comp_id sZ))).comp
        (c.restrict sZ (Category.comp_id sZ))).degreeCongr (add_comm q p)).transport
        (comp_comp_structureMorphism_eq
          (BivariantChowClass.restrict_structure_eq (Category.comp_id sX) sY
            (Category.comp_id sY)) hf)
        (pointClassCompositeIso C sX sZ f hf) (pointClassCompositeIso_hom_comp C sX sZ f hf)
```

## Tag 0FC7, a remark

[Tag 0FC7](https://stacks.math.columbia.edu/tag/0FC7) in the Stacks Project.

**`Stacks.Chow.exteriorProductDedekindChowTensor_cap_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductDedekind/CapCommute.lean, line 803](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductDedekind/CapCommute.lean#L803). The attribute's comment: “α × (c' ∩ β) = c' ∩ (α × β) for every c' ∈ A^q(Y → Z) and every test scheme T → Z (the remark is the case T = Z), over every base as in Section 42.63, with the exterior product of Stacks 0FC4 on the tensor product of Chow groups”.

> **The exterior product over a Dedekind base commutes with capping.** Let `(S, δ)` be as in
> Stacks section 42.63 — locally the spectrum of a Dedekind domain, with `δ = 0` at the closed points
> and `δ = 1` elsewhere — let `X` be locally of finite type over `S`, let `Y ⟶ Z` be a morphism of
> schemes locally of finite type over `S` and let `c' ∈ A^q(Y ⟶ Z)`. Then for `α ∈ CH_n(X)` and
> `β ∈ CH_m(T)`, `t : T ⟶ Z` a test scheme,
>
>   `α × (c' ∩ β) = c' ∩ (α × β)`,
>
> the left hand side living on `X ×_S (Y ×_Z T)` and the right hand side on `Y ×_Z (X ×_S T)`,
> compared through the canonical isomorphism `Stacks.Chow.mixedCommuteHom`, and in the degrees
> `n + (m - q) - 1` and `(n + m - 1) - q`. The source's statement is the case `T = Z`. The exterior
> product is the map of Stacks 0FC4 and `c'` ranges over the whole group `A^q(Y ⟶ Z)` of
> Stacks 0B76.

```lean
theorem exteriorProductDedekindChowTensor_cap_comm {T : Scheme.{u}} (t : T ⟶ Z)
    [LocallyOfFiniteType t] (α : chowGroup C sX n) (β : chowGroup C (t ≫ sZ) m) :
    chowPushforwardOfIso C (pullback.fst sX (pullback.fst w t ≫ (w ≫ sZ)) ≫ sX)
        (pullback.fst w (pullback.snd sX (t ≫ sZ) ≫ t) ≫ (w ≫ sZ))
        (mixedCommuteHom sX sZ w t) (mixedCommuteHom_comp_structureMorphism sX sZ w t)
        (n + (m - q) - 1)
        (exteriorProductDedekindChowTensor C sX (pullback.fst w t ≫ (w ≫ sZ)) n (m - q) hC
          (α ⊗ₜ[ℤ] c'.cap t m β)) =
      chowGroupDegreeEquiv C (pullback.fst w (pullback.snd sX (t ≫ sZ) ≫ t) ≫ (w ≫ sZ))
        (by ring : (n + m - 1) - q = n + (m - q) - 1)
        (c'.cap (pullback.snd sX (t ≫ sZ) ≫ t) (n + m - 1)
          (chowGroupCongr C
            (by rw [Category.assoc]; exact pullback.condition (f := sX) (g := t ≫ sZ))
            (n + m - 1)
            (exteriorProductDedekindChowTensor C sX (t ≫ sZ) n m hC (α ⊗ₜ[ℤ] β))))
```

**`Stacks.Chow.exteriorProductDedekindChow_cap_comm_of_isDedekindChowBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductDedekindCapCommuteGeneral.lean, line 349](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductDedekindCapCommuteGeneral.lean#L349). The attribute's comment: “α × (c' ∩ β) = c' ∩ (α × β) for every bivariant class c' ∈ A^q(Y → Z) and every test scheme T → Z (the remark is the case T = Z), over every base as in Section 42.63, including bases with zero-dimensional components; the exterior product is that of Stacks 0FC4”.

> **Stacks 0FC7.** Let `(S, δ)` be as in section 42.63 of the Stacks Project, let `X` be locally
> of finite type over `S` and `α ∈ CH_n(X)`, let `Y ⟶ Z` be a morphism of schemes locally of finite
> type over `S` and `c' ∈ A^q(Y ⟶ Z)`. Then for every test scheme `t : T ⟶ Z` and `β ∈ CH_m(T)`,
>
>   `α × (c' ∩ β) = c' ∩ (α × β)`
>
> on `X ×_S Y ×_Z T`, the two iterated fibre products being compared through
> `Stacks.Chow.mixedCommuteHom`, the exterior product being that of Stacks 0FC4.
>
> Write `α = c ∩ [S]₁ + [a₀]` with `c ∩ [S₀]₀ = 0` and `a₀` supported over the zero-dimensional
> locus (`Stacks.Chow.exists_bivariantCapBaseFundamentalClass_add_mk_eq`). The exterior product with
> `[a₀]` vanishes, `c` acts by exterior product with `c ∩ [S]₁`, and `c` commutes with `c'` by
> Stacks 0FC6 (`Stacks.Chow.bivariantCommuteOverBase_of_isDedekindChowBase_general`), so
> `Stacks.Chow.exteriorProductDedekindChow_cap_comm` applies.

```lean
theorem exteriorProductDedekindChow_cap_comm_of_isDedekindChowBase (hS : IsDedekindChowBase C)
    {X Y Z : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sZ : Z ⟶ C.S)
    [LocallyOfFiniteType sZ] (w : Y ⟶ Z) [LocallyOfFiniteType w] (n q : ℤ) (α : chowGroup C sX n)
    (c' : BivariantClass C (gysinSystemOfInvertible C) (w ≫ sZ) sZ w rfl q)
    {T : Scheme.{u}} (t : T ⟶ Z) [LocallyOfFiniteType t] (m : ℤ) (β : chowGroup C (t ≫ sZ) m) :
    chowPushforwardOfIso C (pullback.fst sX (pullback.fst w t ≫ (w ≫ sZ)) ≫ sX)
        (pullback.fst w (pullback.snd sX (t ≫ sZ) ≫ t) ≫ (w ≫ sZ))
        (mixedCommuteHom sX sZ w t) (mixedCommuteHom_comp_structureMorphism sX sZ w t)
        (n + (m - q) - 1)
        (exteriorProductDedekindChow C sX (pullback.fst w t ≫ (w ≫ sZ)) n (m - q)
          (hS.exteriorProductFactorsThroughRationalEquivalence sX _ n (m - q)) α
          (c'.cap t m β)) =
      chowGroupDegreeEquiv C (pullback.fst w (pullback.snd sX (t ≫ sZ) ≫ t) ≫ (w ≫ sZ))
        (by ring : (n + m - 1) - q = n + (m - q) - 1)
        (c'.cap (pullback.snd sX (t ≫ sZ) ≫ t) (n + m - 1)
          (chowGroupCongr C
            (by rw [Category.assoc]; exact pullback.condition (f := sX) (g := t ≫ sZ))
            (n + m - 1) (exteriorProductDedekindChow C sX (t ≫ sZ) n m
              (hS.exteriorProductFactorsThroughRationalEquivalence sX (t ≫ sZ) n m) α β)))
```

## Tag 0FC8, a lemma

[Tag 0FC8](https://stacks.math.columbia.edu/tag/0FC8) in the Stacks Project.

**`Stacks.Chow.exteriorProductDedekindChow_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductDedekind/Associativity.lean, line 212](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductDedekind/Associativity.lean#L212). The attribute's comment: “associativity on Chow groups, together with the associator of the triple fibre product over the base and the agreement of the two iterated delta-dimensions; the cycle-level identity is a hypothesis, since it needs the multiplicity of a point of a triple fibre product to factor through the two iterated double products, which this repository does not have”.

> **Stacks 0FC8.** Associativity of the exterior product over a Dedekind base, on Chow
> groups: for Chow classes `a`, `b`, `c` the two iterated exterior products agree after transport
> along the associator of the triple fibre product and along the equality of the two iterated
> delta-dimensions.
>
> Proved from the cycle-level identity `hassoc`, which is the step the source leaves to
> "associativity of fibre product of schemes"; see the implementation notes of
> `StacksFrontier.AlgebraicGeometry.Chow.ExteriorProductDedekind.Associativity` for why that step is
> not formal. The remaining hypotheses are the Stacks 0FC4 descent conditions for the three
> exterior products involved and the Stacks 02S2 condition for the pushforward along the
> associator, exactly as everywhere else in this repository.

```lean
theorem exteriorProductDedekindChow_assoc
    (hXY : ExteriorProductFactorsThroughRationalEquivalence C f' g' n m)
    (hXYZ : ExteriorProductFactorsThroughRationalEquivalence C
      (pullback.fst f' g' ≫ f') h' (n + m - 1) l)
    (hYZ : ExteriorProductFactorsThroughRationalEquivalence C g' h' m l)
    (hXYZ' : ExteriorProductFactorsThroughRationalEquivalence C f'
      (pullback.fst g' h' ≫ g') n (m + l - 1))
    (hpf : ProperPushforwardFactorsThroughRationalEquivalence C
      (pullback.fst (pullback.fst f' g' ≫ f') h' ≫ (pullback.fst f' g' ≫ f'))
      (pullback.fst f' (pullback.fst g' h' ≫ g') ≫ f')
      (tripleFibreProductAssoc f' g' h').hom
      (tripleFibreProductAssoc_hom_structureMorphism f' g' h')
      (n + m - 1 + l - 1))
    (hassoc : IsExteriorProductDedekindAssociative C f' g' h' n m l)
    (α : CycleGroup C f' n) (β : CycleGroup C g' m) (γ : CycleGroup C h' l) :
    exteriorProductDedekind_degree_assoc n m l ▸
        properChowPushforward C
          (pullback.fst (pullback.fst f' g' ≫ f') h' ≫ (pullback.fst f' g' ≫ f'))
          (pullback.fst f' (pullback.fst g' h' ≫ g') ≫ f')
          (tripleFibreProductAssoc f' g' h').hom
          (tripleFibreProductAssoc_hom_structureMorphism f' g' h')
          (n + m - 1 + l - 1) hpf
          (exteriorProductDedekindChow C (pullback.fst f' g' ≫ f') h' (n + m - 1) l hXYZ
            (exteriorProductDedekindChow C f' g' n m hXY
              (QuotientAddGroup.mk' (rationalEquivalences C f' n) α)
              (QuotientAddGroup.mk' (rationalEquivalences C g' m) β))
            (QuotientAddGroup.mk' (rationalEquivalences C h' l) γ)) =
      exteriorProductDedekindChow C f' (pullback.fst g' h' ≫ g') n (m + l - 1) hXYZ'
        (QuotientAddGroup.mk' (rationalEquivalences C f' n) α)
        (exteriorProductDedekindChow C g' h' m l hYZ
          (QuotientAddGroup.mk' (rationalEquivalences C g' m) β)
          (QuotientAddGroup.mk' (rationalEquivalences C h' l) γ))
```

**`Stacks.Chow.exteriorProductDedekindChow_assoc_of_isDedekindChowBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductDedekind/AssociativityCycles.lean, line 1169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ExteriorProductDedekind/AssociativityCycles.lean#L1169).

> **Associativity of the exterior product.** Let `(S, δ)` be as in Stacks section 42.63,
> let `X`, `Y`, `Z` be locally of finite type over `S`, and let `a ∈ CH_n(X)`, `b ∈ CH_m(Y)`,
> `c ∈ CH_l(Z)`. Then `(a × b) × c = a × (b × c)` in `CH_*(X ×_S Y ×_S Z)`.
>
> The two sides live on the two bracketings `(X ×_S Y) ×_S Z` and `X ×_S (Y ×_S Z)` of the triple
> fibre product and in the two spellings `(n + m - 1) + l - 1` and `n + (m + l - 1) - 1` of the same
> delta-dimension, so the left side is carried across by proper pushforward along the associator of
> the fibre product and by the equality of the two degrees.

```lean
theorem exteriorProductDedekindChow_assoc_of_isDedekindChowBase (hC : IsDedekindChowBase C)
    (a : chowGroup C f n) (b : chowGroup C g m) (c : chowGroup C h l) :
    exteriorProductDedekind_degree_assoc n m l ▸
        properChowPushforward C
          (pullback.fst (pullback.fst f g ≫ f) h ≫ (pullback.fst f g ≫ f))
          (pullback.fst f (pullback.fst g h ≫ g) ≫ f)
          (tripleFibreProductAssoc f g h).hom
          (tripleFibreProductAssoc_hom_structureMorphism f g h)
          (n + m - 1 + l - 1)
          (properPushforwardFactorsThroughRationalEquivalence_of_isClosedImmersion
            (tripleFibreProductAssoc f g h).hom C _ _
            (tripleFibreProductAssoc_hom_structureMorphism f g h) (n + m - 1 + l - 1))
          (exteriorProductDedekindChow C (pullback.fst f g ≫ f) h (n + m - 1) l
            (exteriorProductFactorsThroughRationalEquivalence_of_isDedekindChowBase C
              (pullback.fst f g ≫ f) h (n + m - 1) l hC)
            (exteriorProductDedekindChow C f g n m
              (exteriorProductFactorsThroughRationalEquivalence_of_isDedekindChowBase C f g n m hC)
              a b) c) =
      exteriorProductDedekindChow C f (pullback.fst g h ≫ g) n (m + l - 1)
        (exteriorProductFactorsThroughRationalEquivalence_of_isDedekindChowBase C f
          (pullback.fst g h ≫ g) n (m + l - 1) hC) a
        (exteriorProductDedekindChow C g h m l
          (exteriorProductFactorsThroughRationalEquivalence_of_isDedekindChowBase C g h m l hC)
          b c)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.63, Tag 0FC3](https://stacks.math.columbia.edu/tag/0FC3)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
