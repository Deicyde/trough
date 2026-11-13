---
declaration: section
origin: cited
lean: Deformation.Examples.ringDeformationCategory, Deformation.Examples.flatAlgebraCategory_projection_isCofiberedInGroupoids, FlatAlgebraCategory, FlatAlgebraCategory.Hom, FlatAlgebraCategory.instCategory, FlatAlgebraCategory.projection, residueFieldAlgebra, Deformation.Examples.flatAlgebraCategory_projection_satisfiesRS
statement: formalized
proof: formalized
---

# 93.8 Rings

Section 93.8 of the Stacks Project, [Tag 0DY0](https://stacks.math.columbia.edu/tag/0DY0). 11 tags here are carried by 17 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DY1, an example

[Tag 0DY1](https://stacks.math.columbia.edu/tag/0DY1) in the Stacks Project.

**`Deformation.Examples.ringDeformationCategory`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/Rings.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/Rings.lean#L182). The attribute's comment: “ring\_deformation\_category”.

> The category of deformations of the `k`-algebra `P`: flat algebras over Artinian local
> bases equipped with a base-change map to `(k, P)`.

```lean
abbrev ringDeformationCategory (P : Type w) [CommRing P] [Algebra k P]
```

**`Deformation.Examples.flatAlgebraCategory_projection_isCofiberedInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/Rings.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/Rings.lean#L189). The attribute's comment: “flat\_algebra\_category\_cofibered”.

> Base change makes the projection from flat algebras to their Artinian bases cofibered in
> groupoids.

```lean
theorem flatAlgebraCategory_projection_isCofiberedInGroupoids
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k] :
    IsCofiberedInGroupoids (FlatAlgebraCategory.projection (Λ := Λ) (k := k))
```

Declarations registered for the tag:

- [`FlatAlgebraCategory`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=FlatAlgebraCategory#doc) registered with `add_to_stacks` in [StacksFrontier/Deformation/Examples/Geometric/Rings.lean, line 271](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/Rings.lean#L271) (StacksFrontier): “flat\_algebra\_category”.
- [`FlatAlgebraCategory.Hom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=FlatAlgebraCategory.Hom#doc) registered with `add_to_stacks` in [StacksFrontier/Deformation/Examples/Geometric/Rings.lean, line 272](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/Rings.lean#L272) (StacksFrontier): “flat\_algebra\_category”.
- [`FlatAlgebraCategory.instCategory`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=FlatAlgebraCategory.instCategory#doc) registered with `add_to_stacks` in [StacksFrontier/Deformation/Examples/Geometric/Rings.lean, line 273](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/Rings.lean#L273) (StacksFrontier): “flat\_algebra\_category”.
- [`FlatAlgebraCategory.projection`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=FlatAlgebraCategory.projection#doc) registered with `add_to_stacks` in [StacksFrontier/Deformation/Examples/Geometric/Rings.lean, line 274](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/Rings.lean#L274) (StacksFrontier): “flat\_algebra\_category”.
- [`residueFieldAlgebra`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Length/SemiLocal.lean#L47), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Deformation/Examples/Geometric/Rings.lean, line 275](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/Rings.lean#L275) (StacksFrontier): “flat\_algebra\_category”.

## Tag 0DY2, a lemma

[Tag 0DY2](https://stacks.math.columbia.edu/tag/0DY2) in the Stacks Project.

**`Deformation.Examples.flatAlgebraCategory_projection_satisfiesRS`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RimSchlessinger/FibreProduct/Deformations.lean, line 348](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RimSchlessinger/FibreProduct/Deformations.lean#L348). The attribute's comment: “Rim–Schlessinger condition”.

> Flat algebras over Artinian local bases satisfy the Rim–Schlessinger condition.

```lean
theorem flatAlgebraCategory_projection_satisfiesRS
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k] :
    SatisfiesRS (FlatAlgebraCategory.projection (Λ := Λ) (k := k))
```

**`Deformation.Examples.ringDeformationCategory_isDeformationCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RimSchlessinger/FibreProduct/Deformations.lean, line 357](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RimSchlessinger/FibreProduct/Deformations.lean#L357). The attribute's comment: “deformation category”.

> Deformations of any `k`-algebra form a deformation category.

```lean
theorem ringDeformationCategory_isDeformationCategory
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    (P : Type w) [CommRing P] [Algebra k P] :
    IsDeformationCategory
      (objectsOverFunctor (FlatAlgebraCategory.projection (Λ := Λ) (k := k))
        (residueFieldAlgebra (Λ := Λ) (k := k) P))
```

## Tag 0DY3, a lemma

[Tag 0DY3](https://stacks.math.columbia.edu/tag/0DY3) in the Stacks Project.

**`Deformation.Examples.exists_infinitesimalAutomorphismGroupMulEquivDerivation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/RingsInfinitesimalAutomorphisms.lean, line 399](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/RingsInfinitesimalAutomorphisms.lean#L399). The attribute's comment: “infinitesimal automorphisms”. References: SGA 1 III (6.1), “special case”; SGA 3 VIIA (1.5), “partial”.

> **Stacks 0DY3.** The infinitesimal automorphisms of the deformation category of a
> commutative `k`-algebra `P` are the `k`-derivations of `P` into itself.
>
> The statement also records the coordinates in which this holds: for any point `xε` of the
> deformation category over the dual numbers and any lift `i` of the constant inclusion, there
> is a ring isomorphism `c` of the flat algebra of `xε` with `P[ε]` compatible with the
> reduction to `P` and carrying the lift to the constant inclusion, and the derivation attached
> to an infinitesimal automorphism is the `ε`-coefficient of its value on a constant. The
> scalar action of `k` on the derivations is reflected by the existence of a unique rescaled
> infinitesimal automorphism.

```lean
public theorem exists_infinitesimalAutomorphismGroupMulEquivDerivation
    {Λ : Type u} {k P : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    [CommRing P] [Algebra k P] :
    ∃ hp : IsPredeformationCategory (ringDeformationProjection Λ k P),
      ∀ {Aε : ArtinianLocalAlgCat.{u, w, w} Λ k}
        {x₀ : (ringDeformationProjection Λ k P).Fiber (residueFieldObject.{u, w, w} Λ k)}
        {xε : (ringDeformationProjection Λ k P).Fiber Aε}
        (g : residueFieldObject.{u, w, w} Λ k ⟶ Aε)
        (e : Aε ⟶ residueFieldObject.{u, w, w} Λ k)
        (hpair : IsCanonicalDualNumberPair g e)
        (i : x₀.1 ⟶ xε.1) (hi : (ringDeformationProjection Λ k P).IsHomLift g i),
        ∃ c : xε.1.left.fiber ≃+* DualNumber P,
          (∀ y : xε.1.left.fiber, (c y).fst = xε.1.hom.map y) ∧
          (∀ y : x₀.1.left.fiber,
            c (i.left.map y) = TrivSqZeroExt.inl (x₀.1.hom.map y)) ∧
          ∃ E : infinitesimalAutomorphismGroup hp g e hpair i hi ≃*
            Multiplicative (Derivation k P P),
            (∀ (a : infinitesimalAutomorphismGroup hp g e hpair i hi) (y : P),
              (c (a.val.asIso.hom.val.left.map (c.symm (TrivSqZeroExt.inl y)))).snd =
                (Multiplicative.toAdd (E a)) y) ∧
            (∀ (s : k) (a : infinitesimalAutomorphismGroup hp g e hpair i hi),
              ∃! b : infinitesimalAutomorphismGroup hp g e hpair i hi,
                ∀ y : P,
                  (c (b.val.asIso.hom.val.left.map (c.symm (TrivSqZeroExt.inl y)))).snd =
                    s • (c (a.val.asIso.hom.val.left.map
                      (c.symm (TrivSqZeroExt.inl y)))).snd)
```

**`Deformation.Examples.ringDeformationTangentSpaceLinearEquivExtOne`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/RingsTangentSpaceEquivTangent.lean, line 285](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/RingsTangentSpaceEquivTangent.lean#L285). The attribute's comment: “the tangent space”. References: SGA 7 VI (4.16), “(b), special case”.

> **Stacks 0DY3, the tangent space.** Let `k` be a field and `P` a `k`-algebra. The tangent
> space of the deformation category of `P` of Stacks 0DY1, with the canonical `k`-vector-space
> structure of Stacks 06IH, is `Ext¹_P(NL_{P/k}, P)`:
>
> `T𝓓_P = Ext¹_P(NL_{P/k}, P)`.
>
> The identification is the family of extension classes
> `Deformation.Examples.tangentExtClass`, which sends an isomorphism class of first-order flat
> deformations of `P` over `k ⊕ V` to the class of **Stacks 0GPT** of the square-zero extension
> of `P` by `P ⊗[k] V` it determines. That family is natural in `V`, injective by
> `Deformation.Examples.tangentExtClass_injective` and surjective by
> `Deformation.Examples.surjective_tangentExtClass`, so
> `Deformation.tangentSpaceLinearEquivOfNaturalBijection` turns it into a `k`-linear equivalence
> at `V = k`, and `Deformation.Examples.naiveCotangentExtOneTensorFunctorObjRankOne` replaces the
> coefficients `P ⊗[k] k` by `P`.
>
> The infinitesimal-automorphism clause `Inf(𝓓_P) = Der_k(P, P)` of the same tag is
> `Deformation.Examples.exists_infinitesimalAutomorphismGroupMulEquivDerivation`; the two
> declarations together cover the tag.

```lean
public def ringDeformationTangentSpaceLinearEquivExtOne :
    letI : Fact (IsPredeformationCategory (ringDeformationBasedCategory Λ k P).p) :=
      ⟨(ringDeformationCategory_isDeformationCategory P).predeformation⟩
    letI : Fact (SchlessingerConditionS2 (Functor.Elements.π
      (isomorphismClasses (ringDeformationBasedCategory Λ k P)
        isCofiberedInGroupoids_ringDeformationProjection))) :=
      ⟨schlessingerConditionS2_ringDeformation Λ k P⟩
    artinianTangentSpace Λ k
        (isomorphismClasses (ringDeformationBasedCategory Λ k P)
          isCofiberedInGroupoids_ringDeformationProjection)
      ≃ₗ[k] naiveCotangentExtOne k P P
```

**`Deformation.Examples.ringDeformationTangentSpaceLinearEquivExtOne_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/RingsTangentSpaceEquivTangent.lean, line 319](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/RingsTangentSpaceEquivTangent.lean#L319). The attribute's comment: “the tangent space”.

> **The identification of Stacks 0DY3 is the classification of Stacks 0GPT.** On the
> isomorphism class of a point of the fibre over the square-zero extension `k ⊕ k` of
> Stacks 06IB, the tangent-space identification is the class in `Ext¹_P(NL_{P/k}, P ⊗[k] k)` of
> the square-zero extension of `P` the point determines, read through `P ⊗[k] k ≅ P`.
>
> This pins the identification down: no content is left in the transport of the vector-space
> structure of Stacks 06IH.

```lean
public theorem ringDeformationTangentSpaceLinearEquivExtOne_apply
    (z : (associatedTangentSpaceSetFunctor (ringDeformationBasedCategory Λ k P)
      isCofiberedInGroupoids_ringDeformationProjection).obj (FGModuleCat.of k k)) :
    letI : Fact (IsPredeformationCategory (ringDeformationBasedCategory Λ k P).p) :=
      ⟨(ringDeformationCategory_isDeformationCategory P).predeformation⟩
    letI : Fact (SchlessingerConditionS2 (Functor.Elements.π
      (isomorphismClasses (ringDeformationBasedCategory Λ k P)
        isCofiberedInGroupoids_ringDeformationProjection))) :=
      ⟨schlessingerConditionS2_ringDeformation Λ k P⟩
    ringDeformationTangentSpaceLinearEquivExtOne Λ k P z
      = naiveCotangentExtOneTensorFunctorObjRankOne k P
        (tangentExtClass (FGModuleCat.of k k) z)
```

## Tag 0DZL, a lemma

[Tag 0DZL](https://stacks.math.columbia.edu/tag/0DZL) in the Stacks Project.

**`Deformation.Examples.existsUnique_ringDeformationClass_artinianDualNumbers_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/RingsSmooth.lean, line 701](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/RingsSmooth.lean#L701).

> **Stacks 0DZL.** For a smooth algebra `P` over a field `k`, the tangent space of the
> deformation category of `P` is zero: the flat deformations of `P` over the dual numbers
> form a single isomorphism class.

```lean
public theorem existsUnique_ringDeformationClass_artinianDualNumbers_of_smooth
    [Algebra.Smooth k P] :
    ∃ x : Quotient (isIsomorphicSetoid
        ((objectsOverFunctor (FlatAlgebraCategory.projection (Λ := Λ) (k := k))
          (residueFieldAlgebra (Λ := Λ) (k := k) P)).Fiber
          (artinianDualNumbers.{u, w, w} Λ k))),
      ∀ y, y = x
```

## Tag 0DY4, a lemma

[Tag 0DY4](https://stacks.math.columbia.edu/tag/0DY4) in the Stacks Project.

**`Deformation.Examples.finiteDimensional_naiveCotangentExtOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/RingsTangentSpaceFinite.lean, line 524](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/RingsTangentSpaceFinite.lean#L524). The attribute's comment: “part (2) for the Ext group”. References: SGA 7 VI (4.14), “more general”.

> **Stacks 0DY4(2)** for the Ext module. Let `k` be a field and `P` a `k`-algebra of finite
> type which is smooth over `k` outside a finite set of primes. Then the first Ext module
> `Ext¹_P(NL_{P/k}, P)` of the naive cotangent complex is finite-dimensional over `k`, for any
> `k`-module structure on it compatible with the `P`-action. Through the identification of that
> Ext module with the tangent space `T𝓓_P` of the deformation category of `P`, which is Tag
> 0DY3, this is the finite-dimensionality of the tangent space.

```lean
theorem finiteDimensional_naiveCotangentExtOne (k P : Type w) [Field k] [CommRing P]
    [Algebra k P] [Algebra.FiniteType k P]
    [Module k (Stacks.Deformation.naiveCotangentExtOne k P P)]
    [IsScalarTower k P (Stacks.Deformation.naiveCotangentExtOne k P P)]
    (hfinite : {q : PrimeSpectrum P | ¬ Algebra.IsSmoothAt k q.asIdeal}.Finite) :
    FiniteDimensional k (Stacks.Deformation.naiveCotangentExtOne k P P)
```

**`Algebra.finiteDimensional_derivation_iff_ringKrullDim_le_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Derivation/FiniteDimensional.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Derivation/FiniteDimensional.lean#L250). The attribute's comment: “part (1)”.

> **Stacks 0DY4(1).** For a `k`-algebra `P` of finite type over a field, the `k`-derivations
> of `P` into itself are a finite-dimensional `k`-vector space if and only if `P` has Krull
> dimension at most zero. Through Tag 0DY3 this is the finite-dimensionality criterion for the
> infinitesimal automorphisms of the deformation category of `P`.

```lean
theorem finiteDimensional_derivation_iff_ringKrullDim_le_zero
    (k : Type u) (P : Type v) [Field k] [CommRing P] [Algebra k P]
    [Algebra.FiniteType k P] :
    FiniteDimensional k (Derivation k P P) ↔ ringKrullDim P ≤ 0
```

## Tag 0ET4, a lemma

[Tag 0ET4](https://stacks.math.columbia.edu/tag/0ET4) in the Stacks Project.

**`Deformation.Examples.exists_hull_isomorphismClasses_ringDeformation_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/RingsHull.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/RingsHull.lean#L172).

> Let `Λ → k` be a classical base, let `P` be a `k`-algebra of finite type, and suppose
> `Spec(P) → Spec(k)` is smooth except at a finite number of points. Then the functor of fibrewise
> isomorphism classes of deformations of `P` has a hull: a versal formal object with bijective
> differential.

```lean
public theorem exists_hull_isomorphismClasses_ringDeformation_of_finiteType
    [Algebra.FiniteType k P]
    (hsmooth : {q : PrimeSpectrum P | ¬ Algebra.IsSmoothAt k q.asIdeal}.Finite)
    (hΛ : IsClassical Λ k) :
    ∃ ξ : FormalObject (Functor.Elements.π (Deformation.isomorphismClasses
        (BasedCategory.ofFunctor (ringDeformationProjection Λ k P))
        (isPredeformationCategory_ringDeformationProjection (Λ := Λ) (k := k) P).cofibered)),
      IsVersal (categoryOfElements_projection_isCofibered (Deformation.isomorphismClasses
          (BasedCategory.ofFunctor (ringDeformationProjection Λ k P))
          (isPredeformationCategory_ringDeformationProjection
            (Λ := Λ) (k := k) P).cofibered)) ξ ∧
        HasBijectiveDifferential
          (categoryOfElements_projection_isCofibered (Deformation.isomorphismClasses
            (BasedCategory.ofFunctor (ringDeformationProjection Λ k P))
            (isPredeformationCategory_ringDeformationProjection
              (Λ := Λ) (k := k) P).cofibered))
          ξ
```

## Tag 0DYS, a lemma

[Tag 0DYS](https://stacks.math.columbia.edu/tag/0DYS) in the Stacks Project.

**`Deformation.Examples.localizationFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/Localization.lean, line 446](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/Localization.lean#L446).

> Localization at `S` gives a natural functor from deformations of `P` to deformations of
> `S⁻¹P`, with the canonical localization map on every flat algebra.

```lean
noncomputable def localizationFunctor (S : Submonoid P) :
    LocalizationFunctorData (Λ := Λ) (k := k) S
```

## Tag 0DYT, a lemma

[Tag 0DYT](https://stacks.math.columbia.edu/tag/0DYT) in the Stacks Project.

**`Deformation.Examples.henselizationFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/Henselization.lean, line 527](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/Henselization.lean#L527).

> **Stacks 0DYT.** For a `k`-algebra `P` and an ideal `J ⊆ P`, henselization along the
> inverse image of `J` is a functor from the deformation category of `P` to that of the
> henselization of the pair `(P, J)`, over the category `𝒞_Λ` of Artinian local bases.

```lean
noncomputable def henselizationFunctor :
    HenselizationFunctorData (Λ := Λ) (k := k) (P := P) J
```

## Tag 0DYU, a lemma

[Tag 0DYU](https://stacks.math.columbia.edu/tag/0DYU) in the Stacks Project.

**`Deformation.Examples.strictHenselizationFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/StrictHenselization/Functor.lean, line 779](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/StrictHenselization/Functor.lean#L779).

> **Stacks 0DYU.** Let `P` be a local `k`-algebra and let `Pˢʰ` be a strict henselization of
> `P` with respect to a separable algebraic closure of its residue field. There is a natural
> functor from the deformation category of `P` to that of `Pˢʰ`, over the category `𝒞_Λ` of
> Artinian local bases: strict henselize the flat algebra of each deformation.

```lean
noncomputable def strictHenselizationFunctor
    (hsh : Stacks.StrictHenselization.IsStrictHenselization P κsep Psh) :
    StrictHenselizationFunctorData (Λ := Λ) (k := k) (P := P) Psh
```

## Tag 0DYV, a lemma

[Tag 0DYV](https://stacks.math.columbia.edu/tag/0DYV) in the Stacks Project.

**`Deformation.Examples.adicCompletionFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/Completion.lean, line 1069](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/Completion.lean#L1069).

> **The completion functor on deformations, Stacks 0DYV.** Completion at the inverse image of
> `J` is a functor over `𝒞_Λ` together with the identification of its fibres with the adic
> completions; this is one such datum, chosen from the base-compatible ones so that
> `Deformation.Examples.isBaseCompatible_adicCompletionFunctor` holds of it.

```lean
public noncomputable def adicCompletionFunctor [IsNoetherianRing P] :
    AdicCompletionFunctorData (Λ := Λ) (k := k) P J
```

## Tag 0DY5, a lemma

[Tag 0DY5](https://stacks.math.columbia.edu/tag/0DY5) in the Stacks Project.

**`Deformation.Examples.hypersurface_finiteDimensional_infinitesimalAutomorphisms_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/RingsHypersurface.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/RingsHypersurface.lean#L67). The attribute's comment: “part (1)”.

> **Stacks 0DY5(1).** Let `k` be a field, `n` a number of variables and `f` a nonzero formal
> power series in `k[[x_1, …, x_n]]` lying in the square of the ideal generated by the variables,
> and let `P = k[[x_1, …, x_n]]/(f)`. At any dual-number lift of any object of the deformation
> category of `P` over the residue field, the infinitesimal automorphism group carries a
> `k`-vector-space structure whose addition is composition and which is carried by the
> identification of Tag 0DY3 to the `k`-structure of `Derivation k P P`, and that vector space is
> finite-dimensional if and only if `n = 1`.

```lean
public theorem hypersurface_finiteDimensional_infinitesimalAutomorphisms_iff
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    (n : ℕ) (f : MvPowerSeries (Fin n) k) (hf : f ≠ 0)
    (hord : f ∈ (Ideal.span (Set.range
      (MvPowerSeries.X : Fin n → MvPowerSeries (Fin n) k))) ^ 2) :
    let P := MvPowerSeries (Fin n) k ⧸ Ideal.span {f}
    let hp := (ringDeformationCategory_isDeformationCategory (Λ := Λ) (k := k) P).predeformation
    ∀ {Aε : ArtinianLocalAlgCat.{u, w, w} Λ k}
      {x₀ : (ringDeformationProjection Λ k P).Fiber (residueFieldObject.{u, w, w} Λ k)}
      {xε : (ringDeformationProjection Λ k P).Fiber Aε}
      (g : residueFieldObject.{u, w, w} Λ k ⟶ Aε)
      (e : Aε ⟶ residueFieldObject.{u, w, w} Λ k)
      (hpair : IsCanonicalDualNumberPair g e)
      (i : x₀.1 ⟶ xε.1) (hi : (ringDeformationProjection Λ k P).IsHomLift g i),
      let G := infinitesimalAutomorphismGroup hp g e hpair i hi
      ∃ hA : AddCommGroup G,
        letI := hA
        ∃ hM : Module k G,
          letI := hM
          (∀ a b : G, a + b = a * b) ∧
          (∃ E : G ≃* Multiplicative (Derivation k P P), ∀ (s : k) (a : G),
            Multiplicative.toAdd (E (s • a)) = s • Multiplicative.toAdd (E a)) ∧
          (FiniteDimensional k G ↔ n = 1)
```

**`Deformation.Examples.hypersurface_finiteDimensional_tangentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/RingsHypersurfaceTangentSpaceFinite.lean, line 329](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/RingsHypersurfaceTangentSpaceFinite.lean#L329). The attribute's comment: “part (2)”.

> **Stacks 0DY5(2).** Let `k` be a field, `f` a nonzero formal power series in
> `k[[x_1, …, x_n]]` lying in the square of the ideal generated by the variables, and
> `P = k[[x_1, …, x_n]]/(f)` the formal hypersurface it cuts out. If the Jacobian ideal
> `(f, ∂f/∂x_1, …, ∂f/∂x_n)` has radical the ideal generated by the variables, then the tangent
> space `T𝓓_P` of the deformation category of `P` of Stacks 0DY1 — with the canonical
> `k`-vector-space structure of Stacks 06IH — is finite dimensional over `k`.
>
> The tangent space is `Ext¹_P(NL_{P/k}, P)` by the tangent-space clause of Stacks 0DY3, that
> group is the conormal cokernel of the canonical presentation of `P` by Stacks 0GPU, and the
> cokernel is finite dimensional by
> `Deformation.Examples.finiteDimensional_conormalCokernel_hypersurface`. The source's
> hypotheses that `f` is nonzero and lies in the square of the ideal of the variables are not
> used, so the statement omits them.

```lean
theorem hypersurface_finiteDimensional_tangentSpace {Λ : Type u} [CommRing Λ] [Algebra Λ k]
    (hjac : (Ideal.span ({f} ∪ Set.range
      (fun i : Fin n ↦ MvPowerSeries.pderiv (R := k) i f))).radical =
      Ideal.span (Set.range (MvPowerSeries.X : Fin n → MvPowerSeries (Fin n) k))) :
    letI : Fact (IsPredeformationCategory
        (ringDeformationBasedCategory Λ k (Hypersurface n f)).p) :=
      ⟨(ringDeformationCategory_isDeformationCategory (Hypersurface n f)).predeformation⟩
    letI : Fact (SchlessingerConditionS2 (Functor.Elements.π
      (isomorphismClasses (ringDeformationBasedCategory Λ k (Hypersurface n f))
        isCofiberedInGroupoids_ringDeformationProjection))) :=
      ⟨schlessingerConditionS2_ringDeformation Λ k (Hypersurface n f)⟩
    FiniteDimensional k (artinianTangentSpace Λ k
      (isomorphismClasses (ringDeformationBasedCategory Λ k (Hypersurface n f))
        isCofiberedInGroupoids_ringDeformationProjection))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 93.8, Tag 0DY0](https://stacks.math.columbia.edu/tag/0DY0)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
