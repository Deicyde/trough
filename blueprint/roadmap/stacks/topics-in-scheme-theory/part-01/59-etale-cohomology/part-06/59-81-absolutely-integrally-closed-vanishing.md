---
declaration: section
origin: cited
lean: exists_monic_adjoinRoot_isUnit_sub_mul_root, localizationMap_X, localization_isAdjoinRootMonic_of_power_eq, AlgebraicGeometry.MultiplicativeDeformation.isogenyOnPoints_add, AlgebraicGeometry.MultiplicativeDeformation.constantPoint_add, AlgebraicGeometry.MultiplicativeDeformation.isogenyOnPoints_constantPoint, AlgebraicGeometry.MultiplicativeDeformation.kernelCoordinateRing_algEquiv_pi, AlgebraicGeometry.MultiplicativeDeformation.isogeny_faithfullyFlat
statement: formalized
proof: formalized
---

# 59.81 Absolutely integrally closed vanishing

Section 59.81 of the Stacks Project, [Tag 0GY1](https://stacks.math.columbia.edu/tag/0GY1). 6 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GY2, a lemma

[Tag 0GY2](https://stacks.math.columbia.edu/tag/0GY2) in the Stacks Project.

**`exists_monic_adjoinRoot_isUnit_sub_mul_root`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/AbsolutelyIntegrallyClosed/MonogenicExtension.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/AbsolutelyIntegrallyClosed/MonogenicExtension.lean#L78).

> A monogenic extension in which `a - b y` is a unit, when `a` and `b`
> are coprime and `a` is a root of unity modulo `b`.

```lean
public theorem exists_monic_adjoinRoot_isUnit_sub_mul_root
    {A : Type*} [CommRing A] (a b : A)
    (hab : IsCoprime a b)
    (ha : IsOfFinOrder (Ideal.Quotient.mk (Ideal.span {b}) a)) :
    ∃ P : A[X], P.Monic ∧ Function.Injective (algebraMap A (AdjoinRoot P)) ∧
      IsUnit (algebraMap A (AdjoinRoot P) a -
        algebraMap A (AdjoinRoot P) b * AdjoinRoot.root P)
```

## Tag 0GY3, a lemma

[Tag 0GY3](https://stacks.math.columbia.edu/tag/0GY3) in the Stacks Project.

**`localizationMap_X`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/AbsolutelyIntegrallyClosed/MonogenicPresentation.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/AbsolutelyIntegrallyClosed/MonogenicPresentation.lean#L73). The attribute's comment: “the canonical substitution map on the generator”.

> The canonical map sends `t` to `Φ(s)`.

```lean
theorem localizationMap_X
    (A : Type*) [CommRing A] (π : A) (ℓ : ℕ) (Φ : A[X])
    (hΦ : (C π * X + 1) ^ ℓ = C (π ^ ℓ) * Φ + 1) :
    localizationMap A π ℓ Φ hΦ
      (algebraMap A[X] (Localization.Away (C (π ^ ℓ) * X + 1)) X) =
      aeval (algebraMap A[X] (Localization.Away (C π * X + 1)) X) Φ
```

**`localization_isAdjoinRootMonic_of_power_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/AbsolutelyIntegrallyClosed/MonogenicPresentation.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/AbsolutelyIntegrallyClosed/MonogenicPresentation.lean#L91). The attribute's comment: “the monic presentation”.

> For `Φ` monic of positive degree, the target localization is obtained from
> the source localization by adjoining the target variable as a root of the
> monic equation `Φ(s) - t`.

```lean
theorem localization_isAdjoinRootMonic_of_power_eq
    (A : Type*) [CommRing A] (π : A) (ℓ : ℕ) (Φ : A[X])
    (hΦ : (C π * X + 1) ^ ℓ = C (π ^ ℓ) * Φ + 1)
    (hMonic : Φ.Monic) (hDegree : 0 < Φ.natDegree) :
    ∃ h : @IsAdjoinRootMonic (Localization.Away (C (π ^ ℓ) * X + 1))
        (Localization.Away (C π * X + 1)) _ _
        (localizationMap A π ℓ Φ hΦ).toRingHom.toAlgebra
        (Φ.map (algebraMap A (Localization.Away (C (π ^ ℓ) * X + 1))) -
          C (algebraMap A[X] (Localization.Away (C (π ^ ℓ) * X + 1)) X)),
      @IsAdjoinRoot.map (Localization.Away (C (π ^ ℓ) * X + 1))
        (Localization.Away (C π * X + 1)) _ _
        (localizationMap A π ℓ Φ hΦ).toRingHom.toAlgebra _
        (@IsAdjoinRootMonic.toIsAdjoinRoot
          (Localization.Away (C (π ^ ℓ) * X + 1))
          (Localization.Away (C π * X + 1)) _ _
          (localizationMap A π ℓ Φ hΦ).toRingHom.toAlgebra _ h) X =
        algebraMap A[X] (Localization.Away (C π * X + 1)) X
```

## Tag 0GY4, an equation

[Tag 0GY4](https://stacks.math.columbia.edu/tag/0GY4) in the Stacks Project.

**`AlgebraicGeometry.MultiplicativeDeformation.isogenyOnPoints_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/MultiplicativeDeformation/Exactness.lean, line 485](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/MultiplicativeDeformation/Exactness.lean#L485).

> The map `f` is a morphism of group schemes: it is additive on points.

```lean
theorem isogenyOnPoints_add {R : Type v} [CommRing R] [Algebra A R]
    (x y : DeformedPoint (ζ - 1) R) :
    isogenyOnPoints ℓ ζ hsplit (x + y)
      = isogenyOnPoints ℓ ζ hsplit x + isogenyOnPoints ℓ ζ hsplit y
```

**`AlgebraicGeometry.MultiplicativeDeformation.constantPoint_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/MultiplicativeDeformation/Exactness.lean, line 524](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/MultiplicativeDeformation/Exactness.lean#L524).

> The points `σ_i` form a homomorphism from `ℤ/ℓℤ` to the `A`-points of `G^{(ζ - 1)}`, as in
> `σ_i +_G σ_j = σ_{i + j}`.

```lean
theorem constantPoint_add
    (hsplit : ∏ k : ZMod ℓ, (X - C (ζ ^ k.val)) = X ^ ℓ - 1)
    (i j : ZMod ℓ) :
    constantPoint ℓ ζ hζ (i + j) = constantPoint ℓ ζ hζ i + constantPoint ℓ ζ hζ j
```

**`AlgebraicGeometry.MultiplicativeDeformation.isogenyOnPoints_constantPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/MultiplicativeDeformation/Exactness.lean, line 543](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/MultiplicativeDeformation/Exactness.lean#L543).

> The composition of `ℤ/ℓℤ → G^{(ζ - 1)}` with `f` is trivial: the points `σ_i` lie in the
> kernel of `f`.

```lean
theorem isogenyOnPoints_constantPoint (i : ZMod ℓ) :
    isogenyOnPoints ℓ ζ hsplit (constantPoint ℓ ζ hζ i) = 0
```

**`AlgebraicGeometry.MultiplicativeDeformation.kernelCoordinateRing_algEquiv_pi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/MultiplicativeDeformation/Exactness.lean, line 660](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/MultiplicativeDeformation/Exactness.lean#L660).

> Exactness at `G^{(ζ - 1)}`: for `ℓ` prime, the closed immersion of the constant group scheme
> of `ℤ/ℓℤ` into the kernel of `f` which sends `i` to `σ_i` is an isomorphism. Dually, the
> `A`-algebra map from the coordinate ring of the kernel to the functions on `ℤ/ℓℤ` sending `s`
> to `i ↦ σ_i` is an isomorphism.

```lean
theorem kernelCoordinateRing_algEquiv_pi (hℓ : ℓ.Prime) :
    ∃ e : kernelCoordinateRing ℓ ζ hsplit ≃ₐ[A] (ZMod ℓ → A),
      ∀ i : ZMod ℓ,
        e (Ideal.Quotient.mk _ (coordinateGenerator (ζ - 1))) i = sigmaPoint ℓ ζ i
```

**`AlgebraicGeometry.MultiplicativeDeformation.isogeny_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/MultiplicativeDeformation/Exactness.lean, line 673](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/MultiplicativeDeformation/Exactness.lean#L673).

> Exactness at `G^{((ζ - 1) ^ ℓ)}`: the morphism `f` is faithfully flat.

```lean
theorem isogeny_faithfullyFlat : (isogeny ℓ ζ hsplit).toRingHom.FaithfullyFlat
```

**`AlgebraicGeometry.MultiplicativeDeformation.exists_shortExactSequence_of_groupSchemes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/MultiplicativeDeformation/GroupSchemes.lean, line 744](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/Examples/MultiplicativeDeformation/GroupSchemes.lean#L744).

> The short exact sequence `0 → ℤ/ℓℤ → G^{(ζ - 1)} → G^{((ζ - 1) ^ ℓ)} → 0` is a sequence of
> group schemes over `Spec A`, not merely a sequence of groups of `A`-points. The left-hand group
> scheme is the constant group scheme of `ℤ/ℓℤ`; the right-hand map is the scheme morphism dual
> to the explicitly specified algebra homomorphism `isogeny`. The coordinate of the left-hand map
> is pinned to the points `σ_i`, and the pullback square says that it identifies the constant
> group scheme with the kernel.

```lean
theorem exists_shortExactSequence_of_groupSchemes (hℓ : ℓ.Prime) :
    ∃ (g : Grp (Over (Spec (.of A)))) (h : Grp (Over (Spec (.of A))))
      (i : constantGroupScheme (Multiplicative (ZMod ℓ)) (Spec (.of A)) ⟶ g) (f : g ⟶ h),
      ∃ (eg : g.X ≅ (Spec (.of (coordinateRing (ζ - 1)))).asOver (Spec (.of A)))
        (eh : h.X ≅ (Spec (.of (coordinateRing ((ζ - 1) ^ ℓ)))).asOver (Spec (.of A))),
        (((eg.inv ⊗ₘ eg.inv) ≫ MonObj.mul (X := g.X) ≫ eg.hom).left =
          (pullbackSpecIso A (coordinateRing (ζ - 1)) (coordinateRing (ζ - 1))).hom ≫
            Spec.map (CommRingCat.ofHom (comultiplication (ζ - 1)).toRingHom)) ∧
        (((eh.inv ⊗ₘ eh.inv) ≫ MonObj.mul (X := h.X) ≫ eh.hom).left =
          (pullbackSpecIso A (coordinateRing ((ζ - 1) ^ ℓ))
            (coordinateRing ((ζ - 1) ^ ℓ))).hom ≫
            Spec.map (CommRingCat.ofHom (comultiplication ((ζ - 1) ^ ℓ)).toRingHom)) ∧
        (CategoryTheory.IsPullback i.hom.hom (toUnit _)
          f.hom.hom (MonObj.one : (𝟙_ (Over (Spec (.of A)))) ⟶ h.X)) ∧
        (Flat f.hom.hom.left ∧ Surjective f.hom.hom.left) ∧
        (eg.inv ≫ f.hom.hom ≫ eh.hom).left =
          Spec.map (CommRingCat.ofHom (isogeny ℓ ζ hsplit).toRingHom) ∧
        (∀ j : ZMod ℓ,
          (Spec.preimage
            (constantComponentOver (A := A) ℓ (Multiplicative.ofAdd j) ≫
              i.hom.hom ≫ eg.hom).left).hom
            (coordinateGenerator (ζ - 1)) = sigmaPoint ℓ ζ j)
```

## Tag 0GY5, a lemma

[Tag 0GY5](https://stacks.math.columbia.edu/tag/0GY5) in the Stacks Project.

**`surjective_precomp_localizationMap_of_isAbsolutelyIntegrallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/AbsolutelyIntegrallyClosed/LiftingPoints.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/AbsolutelyIntegrallyClosed/LiftingPoints.lean#L41).

> Every point of the target of the monogenic map lifts over an absolutely
> integrally closed `A`-algebra.

```lean
public theorem surjective_precomp_localizationMap_of_isAbsolutelyIntegrallyClosed
    (A : Type*) [CommRing A] (π : A) (ℓ : ℕ) (Φ : A[X])
    (hΦ : (C π * X + 1) ^ ℓ = C (π ^ ℓ) * Φ + 1)
    (hMonic : Φ.Monic)
    (hDegree : 0 < Φ.natDegree)
    (R : Type*) [CommRing R] [Algebra A R]
    (hR : IsAbsolutelyIntegrallyClosed R) :
    Function.Surjective (fun g : Localization.Away (C π * X + 1) →ₐ[A] R =>
      g.comp (localizationMap A π ℓ Φ hΦ))
```

## Tag 0GY6, a lemma

[Tag 0GY6](https://stacks.math.columbia.edu/tag/0GY6) in the Stacks Project.

**`exists_isUnit_one_add_mul_of_comaximal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/AbsolutelyIntegrallyClosed/Interpolation.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/AbsolutelyIntegrallyClosed/Interpolation.lean#L51).

> Let `R` be absolutely integrally closed and `π ∈ R` with `1 + π` of finite order. For
> comaximal ideals `I` and `J` of `R` there is `s ∈ I` with `s - 1 ∈ J` and `1 + π s` a unit.

```lean
public theorem exists_isUnit_one_add_mul_of_comaximal
    {R : Type*} [CommRing R]
    (hR : IsAbsolutelyIntegrallyClosed R) (π : R) (hπ : IsOfFinOrder (1 + π))
    (I J : Ideal R) (hIJ : I + J = ⊤) :
    ∃ s : R, IsUnit (1 + π * s) ∧ s ∈ I ∧ s - 1 ∈ J
```

## Tag 0GY7, a proposition

[Tag 0GY7](https://stacks.math.columbia.edu/tag/0GY7) in the Stacks Project.

**`Stacks.EtaleCohomology.AbsolutelyIntegrallyClosed.subsingleton_H_constantSheaf_smallEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/AbsolutelyIntegrallyClosed/Vanishing.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/AbsolutelyIntegrallyClosed/Vanishing.lean#L182).

> **Stacks 0GY7.** Let `R` be an absolutely integrally closed ring and let `M` be a finite
> abelian group. Then `H^i_étale(Spec R, M) = 0` for `i > 0`.
>
> This is `subsingleton_H_constantSheaf_of_finite` read on Mathlib's small étale site of `Spec R`,
> to which the one-universe model used there is a dense subsite.

```lean
theorem subsingleton_H_constantSheaf_smallEtale (hR : IsAbsolutelyIntegrallyClosed R)
    (M : AddCommGrpCat.{u + 1}) [Finite M] (q : ℕ) (hq : 0 < q) :
    Subsingleton (Sheaf.H.{u + 1}
      ((constantSheaf (Spec (CommRingCat.of R)).smallEtaleTopology
        AddCommGrpCat.{u + 1}).obj M) q)
```

**`Stacks.EtaleCohomology.AbsolutelyIntegrallyClosed.subsingleton_H_constantSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/AbsolutelyIntegrallyClosedVanishing.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/AbsolutelyIntegrallyClosedVanishing.lean#L225). The attribute's comment: “assuming degree-zero sections over an overlap are differences (hypothesis hsub)”.

> **Stacks 0GY7, with the degree-zero gluing hypothesis `hsub` carried.** Let `R` be an
> absolutely integrally closed ring and let `M` be a finite abelian group. Then the étale
> cohomology of `Spec R` with coefficients in the constant sheaf `M` vanishes in every positive
> degree, provided every section of that constant sheaf over `D(f(f + g)) ∩ D(g(f + g))` is a
> difference of sections over `D(f(f + g))` and over `D(g(f + g))`.
>
> This is weaker than Stacks 0GY7, which carries no such hypothesis. In the source, the gluing
> statement is where finiteness of `M` is used, through the group-scheme argument of Stacks 0GY4,
> 0GY5 and 0GY6; here it is a hypothesis, and `[Finite M]` is therefore not used by the proof.

```lean
theorem subsingleton_H_constantSheaf (hR : IsAbsolutelyIntegrallyClosed R)
    (M : AddCommGrpCat.{u + 1}) [Finite M]
    (hsub : ∀ f g : R,
      SectionsSub ((constantSheaf (MayerVietoris.topology (Spec (CommRingCat.of R)))
          AddCommGrpCat.{u + 1}).obj M)
        (PrimeSpectrum.basicOpen (f * (f + g))) (PrimeSpectrum.basicOpen (g * (f + g))))
    (q : ℕ) (hq : 0 < q) :
    Subsingleton (Sheaf.H.{u + 1}
      ((constantSheaf (MayerVietoris.topology (Spec (CommRingCat.of R)))
        AddCommGrpCat.{u + 1}).obj M) q)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.81, Tag 0GY1](https://stacks.math.columbia.edu/tag/0GY1)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
