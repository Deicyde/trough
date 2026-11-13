---
declaration: section
origin: cited
lean: Stacks.IntegralClosure.SmoothPullback.bijective_toIntegralClosure_sections, Stacks.IntegralClosure.SmoothPullback.range_integralClosureAlgebraι_app_pullback, Stacks.IntegralClosure.SheafLevel.range_integralClosureAlgebraι_app_algebraPullback_eq, Stacks.IntegralClosure.SheafLevel.range_integralClosureAlgebraι_app_pullback_eq, Stacks.IntegralClosure.SheafLevel.range_integralClosureAlgebraι_app_pullback_relativeSpec_eq, AlgebraicGeometry.existsUnique_normalizationScheme_iso_pullback_of_smooth, AlgebraicGeometry.normalization_baseChange_henselization, AlgebraicGeometry.normalization_baseChange_strictHenselization
statement: formalized
proof: formalized
---

# 37.19 Normalization revisited

Section 37.19 of the Stacks Project, [Tag 081J](https://stacks.math.columbia.edu/tag/081J). 3 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 081K, a lemma

[Tag 081K](https://stacks.math.columbia.edu/tag/081K) in the Stacks Project.

**`Stacks.IntegralClosure.SmoothPullback.bijective_toIntegralClosure_sections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/IntegralClosure.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/IntegralClosure.lean#L183). The attribute's comment: “affine-open comparison map. The equality of subsheaves is asserted over a pair of affine opens `V ⊆ Y`, `U ⊆ S` with `V ⊆ g⁻¹U`, as bijectivity of the canonical map out of the base change of the sections of the integral closure, the quasi-coherent algebra being presented as `f_*𝒪_X` for `f` quasi-compact and quasi-separated. The identification of the sections of the pullback is `sectionsBaseChangeEquiv`, pinned by `sectionsBaseChangeEquiv_tmul_one` and `sectionsBaseChangeEquiv_one_tmul`. The same assertion in terms of the integral-closure subalgebra itself is `range_integralClosureAlgebraι_app_pullback`. The sheaf-level equality is not asserted here. See the module docstring.”. References: EGA IV (18.12.15); EGA IV (6.14.5), “smooth, affine opens”.

> **Stacks Project, Tag 081K**, over a pair of affine opens. Let `g : Y ⟶ S` be a smooth
> morphism, let `𝒜 = f_*𝒪_X` be a quasi-coherent sheaf of `𝒪_S`-algebras and let `𝒜'` be the
> integral closure of `𝒪_S` in `𝒜`. Over an affine open `V ⊆ Y` lying over an affine open
> `U ⊆ S`, the canonical map from `𝒜'(U) ⊗_{Γ(S, U)} Γ(Y, V)` to the integral closure of `Γ(Y, V)`
> in `(g^*𝒜)(V) = Γ(X ×_S Y, q⁻¹V)` is bijective.

```lean
public theorem bijective_toIntegralClosure_sections [QuasiCompact f] [QuasiSeparated f] [Smooth g]
    {U : S.Opens} {V : Y.Opens} (hU : IsAffineOpen U) (hV : IsAffineOpen V)
    (hVU : V ≤ g ⁻¹ᵁ U) :
    letI := (f.app U).hom.toAlgebra
    letI := (g.appLE U V hVU).hom.toAlgebra
    letI := ((pullback.snd f g).app V).hom.toAlgebra
    Function.Bijective
      ((sectionsBaseChangeEquiv f g hU hV hVU).mapIntegralClosure.toAlgHom.comp
        (TensorProduct.toIntegralClosure Γ(S, U) Γ(Y, V) Γ(X, f ⁻¹ᵁ U)))
```

**`Stacks.IntegralClosure.SmoothPullback.range_integralClosureAlgebraι_app_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/IntegralClosure.lean, line 211](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/IntegralClosure.lean#L211). The attribute's comment: “affine sections of the integral-closure subalgebra. Both sides are read over a pair of affine opens `V ⊆ Y`, `U ⊆ S` with `V ⊆ g⁻¹U`: the left is the sections of the integral-closure subalgebra of Stacks 035F in the pullback, the right the image of the base change of `𝒜'(U)`, which is the sections of that subalgebra over `U` by `AlgebraicGeometry.Scheme.QuasicoherentAlgebra.range_integralClosureAlgebraι_app_of_isAffineOpen`. The pullback is presented as `f_*𝒪_{X ×_S Y}`, not as `algebraPullback g`; the two agree by `Stacks.AffineAlgebraEquivalence.isIso_baseChangeAlgebraHom`, whose sections over an open are not computed in this repository, so the sheaf-level equality is not asserted here. See the module docstring.”. References: EGA IV (18.12.15); EGA IV (6.14.5), “smooth, affine opens”.

> **Stacks Project, Tag 081K**, over a pair of affine opens and in terms of the integral-closure
> subalgebra itself. For `g` smooth and `𝒜 = f_*𝒪_X` with `f` affine, the sections over `V` of the
> integral closure of `𝒪_Y` in `g^*𝒜` are the image of `Γ(Y, V) ⊗_{Γ(S, U)} 𝒜'(U)`.

```lean
public theorem range_integralClosureAlgebraι_app_pullback [IsAffineHom f] [Smooth g]
    {U : S.Opens} {V : Y.Opens} (hU : IsAffineOpen U) (hV : IsAffineOpen V)
    (hVU : V ≤ g ⁻¹ᵁ U) :
    haveI := IsSeparated.of_isAffineHom f
    haveI : IsAffineHom (pullback.snd f g) := MorphismProperty.IsStableUnderBaseChange.of_isPullback
      (IsPullback.of_hasPullback f g) ‹IsAffineHom f›
    letI := (f.app U).hom.toAlgebra
    letI := (g.appLE U V hVU).hom.toAlgebra
    letI := ((pullback.snd f g).app V).hom.toAlgebra
    Set.range ((integralClosureAlgebraι
        (pushforwardAlgebra (pullback.snd f g))).right.hom.app (op V)) =
      Set.range ((sectionsBaseChangeEquiv f g hU hV hVU).toAlgHom.comp
        (Algebra.TensorProduct.map (AlgHom.id Γ(Y, V) Γ(Y, V))
          (integralClosure Γ(S, U) Γ(X, f ⁻¹ᵁ U)).val))
```

**`Stacks.IntegralClosure.SheafLevel.range_integralClosureAlgebraι_app_algebraPullback_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/IntegralClosurePullback.lean, line 437](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/IntegralClosurePullback.lean#L437). The attribute's comment: “the whole statement, in the development's own terms: the integral closure `integralClosureAlgebra` of the structure sheaf, the pullback `algebraPullback` of algebra sheaves, an arbitrary quasi-coherent `𝒜`, an arbitrary open of `Y`, and no hypothesis beyond `g` smooth. The two subsheaves of `g^*𝒜` are compared by the ranges of their sections, which is how the development writes an inclusion of algebra sheaves. The mathematics is `range_integralClosureAlgebraι_app_pullback_eq`, where Stacks 03GG and 03GV are consumed; what is added here is the transport `image_range_integralClosureAlgebraι_app` of the integral closure along an isomorphism of algebra sheaves, together with `normalizationAlgebraIso` and `Stacks.AlgebraPullbackQcoh.baseChangeAlgebraHom_naturality`.”. References: EGA IV (18.12.15).

> **Stacks Project, Tag 081K.** Let `g : Y ⟶ S` be a smooth morphism of schemes, let `𝒜` be a
> quasi-coherent sheaf of commutative `𝒪_S`-algebras and let `𝒜' = integralClosureAlgebra 𝒜` be
> the integral closure of `𝒪_S` in `𝒜`. Then the integral closure of `𝒪_Y` in `g^*𝒜` is `g^*𝒜'`:
> the two subsheaves `integralClosureAlgebra (g^*𝒜)` and `g^*𝒜'` of `g^*𝒜` have the same sections
> over every open `W` of `Y`. No hypothesis is placed on `𝒜` beyond quasi-coherence, and none on
> `g` beyond smoothness.

```lean
public theorem range_integralClosureAlgebraι_app_algebraPullback_eq (W : Y.Opens) :
    Set.range ((integralClosureAlgebraι ((algebraPullback g).obj A)).right.hom.app (op W)) =
      Set.range (((algebraPullback g).map (integralClosureAlgebraι A)).right.hom.app (op W))
```

**`Stacks.IntegralClosure.SheafLevel.range_integralClosureAlgebraι_app_pullback_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/IntegralClosureSheaf.lean, line 329](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/IntegralClosureSheaf.lean#L329). The attribute's comment: “the equality of subsheaves, over an arbitrary open of `Y`. The quasi-coherent algebra is presented as `f_* 𝒪_X` for `f` affine rather than as an abstract quasi-coherent algebra, and the pullback as a direct image from a fibre product rather than through `algebraPullback`; the latter two agree by `isIso_baseChangeAlgebraHom_fromNormalization`, and the integral-closure subalgebra `𝒜'` is identified with the relative normalization by `range_integralClosureAlgebraι_app_eq_range_normalizationAlgebraι_app`. The affine-open comparison map, which is where Stacks 03GG is consumed, is `Stacks.IntegralClosure.SmoothPullback.bijective_toIntegralClosure_sections`. Transport of the integral-closure subalgebra along an isomorphism of algebra sheaves, which removes the presentation of `𝒜` as `f_* 𝒪_X`, is `Stacks.IntegralClosure.SheafLevel.image_range_integralClosureAlgebraι_app`, and the resulting presentation-free form of this clause is `Stacks.IntegralClosure.SheafLevel.range_integralClosureAlgebraι_app_algebraPullback_eq`. See the module docstring.”. References: EGA IV (18.12.15); EGA IV (6.14.5), “smooth base change”.

> Let `g : Y ⟶ S` be a smooth morphism, let `𝒜 = f_* 𝒪_X` be a quasi-coherent sheaf of
> `𝒪_S`-algebras with `f : X ⟶ S` affine, and let `𝒜' ⊆ 𝒜` be the integral closure of `𝒪_S` in
> `𝒜`. Then `g^*𝒜'` is the integral closure of `𝒪_Y` in `g^*𝒜`: inside `g^*𝒜 = (X ×_S Y)_* 𝒪`,
> the two subsheaves have the same sections over every open `W` of `Y`. Here `𝒜'` is presented as
> `(f.fromNormalization)_* 𝒪`, by
> `range_integralClosureAlgebraι_app_eq_range_normalizationAlgebraι_app`, and its pullback as the
> direct image of the structure sheaf of `f.normalization ×_S Y`, which is `g^*𝒜'` by
> `isIso_baseChangeAlgebraHom_fromNormalization`.

```lean
public theorem range_integralClosureAlgebraι_app_pullback_eq [IsAffineHom f] (W : Y.Opens) :
    Set.range ((integralClosureAlgebraι
        (pushforwardAlgebra (pullback.snd f g))).right.hom.app (op W)) =
      Set.range ((baseChangeNormalizationAlgebraι f g).right.hom.app (op W))
```

**`Stacks.IntegralClosure.SheafLevel.range_integralClosureAlgebraι_app_pullback_relativeSpec_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/IntegralClosureSheaf.lean, line 383](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/IntegralClosureSheaf.lean#L383). The attribute's comment: “the equality of subsheaves for an arbitrary quasi-coherent `𝒪_S`-algebra `𝒜`, over an arbitrary open of `Y`. `𝒜` enters through its relative spectrum, so that `𝒜` itself is `(relativeSpecToBase 𝒜)_* 𝒪` up to the isomorphism `Stacks.AffineAlgebraEquivalence.pushforwardAlgebraIso`. Invariance of the integral-closure subalgebra under an isomorphism of algebra sheaves, which lets the statement be read off `integralClosureAlgebra 𝒜` directly, is `Stacks.IntegralClosure.SheafLevel.image_range_integralClosureAlgebraι_app`, and the resulting statement — the equality of the subsheaves `integralClosureAlgebra (g^*𝒜)` and `g^*(integralClosureAlgebra 𝒜)` of `g^*𝒜` — is `Stacks.IntegralClosure.SheafLevel.range_integralClosureAlgebraι_app_algebraPullback_eq`. See the module docstring and `range_integralClosureAlgebraι_app_pullback_eq`.”. References: EGA IV (18.12.15).

> Let `g : Y ⟶ S` be smooth and let `𝒜` be any quasi-coherent sheaf of `𝒪_S`-algebras, with
> `𝒜' ⊆ 𝒜` the integral closure of `𝒪_S` in `𝒜`. Writing `X = Spec_S(𝒜)` for the relative
> spectrum, so that `𝒜 ≅ (relativeSpecToBase 𝒜)_* 𝒪_X` by
> `Stacks.AffineAlgebraEquivalence.pushforwardAlgebraIso` and `g^*𝒜 ≅ (X ×_S Y)_* 𝒪` by
> `isIso_baseChangeAlgebraHom_self` at `X`, the integral closure of `𝒪_Y` in `g^*𝒜` is `g^*𝒜'`:
> the two subsheaves have the same sections over every open `W` of `Y`. No hypothesis is placed on
> `𝒜` beyond quasi-coherence.

```lean
public theorem range_integralClosureAlgebraι_app_pullback_relativeSpec_eq (W : Y.Opens) :
    haveI : IsSeparated (relativeSpecToBase A) := IsSeparated.of_isAffineHom _
    Set.range ((integralClosureAlgebraι (pushforwardAlgebra
        (pullback.snd (relativeSpecToBase A) g))).right.hom.app (op W)) =
      Set.range ((baseChangeNormalizationAlgebraι (relativeSpecToBase A) g).right.hom.app
        (op W))
```

## Tag 07TD, a lemma

[Tag 07TD](https://stacks.math.columbia.edu/tag/07TD) in the Stacks Project.

**`AlgebraicGeometry.existsUnique_normalizationScheme_iso_pullback_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/SmoothBaseChange.lean, line 275](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/SmoothBaseChange.lean#L275).

> **Normalization and smooth morphisms.** Let `φ : X ⟶ Y` be a smooth morphism of schemes and
> assume every quasi-compact open of `Y` has finitely many irreducible components. Then the same is
> true for `X`, and there is a unique isomorphism `X^ν ≅ X ×_Y Y^ν` over `X`, where `X^ν` and `Y^ν`
> are the normalizations of `X` and `Y`.
>
> Existence is the cartesian square `AlgebraicGeometry.isPullback_normalizationSchemeMap_of_smooth`;
> uniqueness holds because the only endomorphism of `X^ν` over `X` is the identity, by the universal
> property `AlgebraicGeometry.Scheme.existsUnique_lift_normalization`.

```lean
theorem existsUnique_normalizationScheme_iso_pullback_of_smooth {X Y : Scheme.{u}} (φ : X ⟶ Y)
    [Smooth φ] (hY : ∀ U : Y.Opens, IsCompact (U : Set Y) → (irreducibleComponents U).Finite) :
    ∃ hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite,
      ∃! e : X.normalizationScheme hX ≅ pullback φ (Y.normalization hY),
        e.hom ≫ pullback.fst φ (Y.normalization hY) = X.normalization hX
```

## Tag 0CBM, a lemma

[Tag 0CBM](https://stacks.math.columbia.edu/tag/0CBM) in the Stacks Project.

**`AlgebraicGeometry.normalization_baseChange_henselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Henselization.lean, line 294](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Henselization.lean#L294). The attribute's comment: “henselization”.

> The base change of the normalization morphism of a locally Noetherian scheme `X` to the
> spectrum of the henselization of the local ring of `X` at a point is the normalization morphism
> of that spectrum.

```lean
public theorem normalization_baseChange_henselization (X : Scheme.{u}) [IsLocallyNoetherian X]
    (x : X) (Ah : Type u) [CommRing Ah] [IsLocalRing Ah] [Algebra (X.presheaf.stalk x) Ah]
    [IsHenselization (X.presheaf.stalk x) (ResidueField (X.presheaf.stalk x)) Ah] :
    haveI : IsNoetherianRing Ah :=
      IsLocalRing.isNoetherianRing_of_isHenselization (A := X.presheaf.stalk x) (B := Ah)
        (ResidueField (X.presheaf.stalk x))
    Nonempty
      (Over.mk (pullback.snd
          (Scheme.normalization X (finite_irreducibleComponents_of_isCompact X))
          (Spec.map (CommRingCat.ofHom (algebraMap (X.presheaf.stalk x) Ah)) ≫
            X.fromSpecStalk x)) ≅
        Over.mk (Scheme.normalization (Spec (.of Ah))
          (finite_irreducibleComponents_of_isCompact (Spec (.of Ah)))))
```

**`AlgebraicGeometry.normalization_baseChange_strictHenselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Henselization.lean, line 313](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Henselization.lean#L313). The attribute's comment: “strict\_henselization”.

> The base change of the normalization morphism of a locally Noetherian scheme `X` to the
> spectrum of a strict henselization of the local ring of `X` at a point is the normalization
> morphism of that spectrum.

```lean
public theorem normalization_baseChange_strictHenselization (X : Scheme.{u})
    [IsLocallyNoetherian X] (x : X) (Ash : Type u) [CommRing Ash] [IsLocalRing Ash]
    [Algebra (X.presheaf.stalk x) Ash] (ksep : Type v) [Field ksep]
    [Algebra (ResidueField (X.presheaf.stalk x)) ksep]
    [IsSepClosure (ResidueField (X.presheaf.stalk x)) ksep]
    [IsHenselization (X.presheaf.stalk x) ksep Ash] :
    haveI : IsNoetherianRing Ash :=
      IsLocalRing.isNoetherianRing_of_isHenselization (A := X.presheaf.stalk x) (B := Ash) ksep
    Nonempty
      (Over.mk (pullback.snd
          (Scheme.normalization X (finite_irreducibleComponents_of_isCompact X))
          (Spec.map (CommRingCat.ofHom (algebraMap (X.presheaf.stalk x) Ash)) ≫
            X.fromSpecStalk x)) ≅
        Over.mk (Scheme.normalization (Spec (.of Ash))
          (finite_irreducibleComponents_of_isCompact (Spec (.of Ash)))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.19, Tag 081J](https://stacks.math.columbia.edu/tag/081J)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
