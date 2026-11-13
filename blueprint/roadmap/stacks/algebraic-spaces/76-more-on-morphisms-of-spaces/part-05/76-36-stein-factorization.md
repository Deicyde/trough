---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.universallyClosed_toNormalizationIn, AlgebraicGeometry.Space.isQuasiCompact_toNormalizationIn, AlgebraicGeometry.Space.isQuasiSeparated_toNormalizationIn, AlgebraicGeometry.Space.isSurjective_toNormalizationIn, AlgebraicGeometry.Space.isIntegralHom_normalizationIn, AlgebraicGeometry.Space.isRelativeNormalization_steinFactorization, AlgebraicGeometry.Space.steinFactorization_of_universallyClosed, AlgebraicGeometry.Space.isSurjective_toNormalizationInQcqs
statement: formalized
proof: formalized
---

# 76.36 Stein factorization

Section 76.36 of the Stacks Project, [Tag 0A18](https://stacks.math.columbia.edu/tag/0A18). 10 tags here are carried by 20 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0A19, a lemma

[Tag 0A19](https://stacks.math.columbia.edu/tag/0A19) in the Stacks Project.

**`AlgebraicGeometry.Space.universallyClosed_toNormalizationIn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorization.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorization.lean#L174). The attribute's comment: “part (1): the morphism to the normalization is universally closed”.

> **Stacks 0A19, clause (1): `f'` is universally closed.**  By Stacks 04NX part (1), since the
> composite `f = f' ≫ π` is universally closed and `π` is separated.

```lean
theorem universallyClosed_toNormalizationIn
    (hfuc : UniversallyClosed B S hS f.hom) :
    UniversallyClosed B S hS (toNormalizationIn B S hS E C f hqc hqc' hid).left.hom
```

**`AlgebraicGeometry.Space.isQuasiCompact_toNormalizationIn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorization.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorization.lean#L186). The attribute's comment: “part (1): the morphism to the normalization is quasi-compact”.

> **Stacks 0A19, clause (1): `f'` is quasi-compact.**  By Stacks 03KS, since the composite
> `f = f' ≫ π` is quasi-compact — a universally closed morphism is quasi-compact by
> Stacks 04XW — and `π` is quasi-separated.

```lean
theorem isQuasiCompact_toNormalizationIn
    (hfuc : UniversallyClosed B S hS f.hom) :
    IsQuasiCompact B S hS (toNormalizationIn B S hS E C f hqc hqc' hid).left.hom
```

**`AlgebraicGeometry.Space.isQuasiSeparated_toNormalizationIn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorization.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorization.lean#L197). The attribute's comment: “part (1): the morphism to the normalization is quasi-separated”.

> **Stacks 0A19, clause (1): `f'` is quasi-separated.**  By Stacks 03KR, since the composite
> `f = f' ≫ π` is quasi-separated.  Nothing is required of `π`.

```lean
theorem isQuasiSeparated_toNormalizationIn
    (hfqs : IsQuasiSeparated B S hS f.hom) :
    IsQuasiSeparated B S hS (toNormalizationIn B S hS E C f hqc hqc' hid).left.hom
```

**`AlgebraicGeometry.Space.isSurjective_toNormalizationIn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorization.lean, line 253](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorization.lean#L253). The attribute's comment: “part (1): the morphism to the normalization is surjective”.

> **Stacks 0A19, clause (1): `f'` is surjective.**  The scheme-theoretic image of `f'` inside
> the normalization `Y'` of `Y` in `X` is a closed subspace, hence integral over `Y`, through
> which `f` factors; the characterization of Stacks 0823 therefore retracts `Y'` onto it, and
> `f'` has closed image because it is universally closed.

```lean
theorem isSurjective_toNormalizationIn
    (P : RelativeSpecUniversalProperty B S hS E C) (D : IntegralAlgebraDictionary B S hS E)
    (hloc : (pushforwardAlgebra B S hS (Over.mk f)).IsIntegralLocalOnAffineCharts)
    (hfuc : UniversallyClosed B S hS f.hom) :
    IsSurjective B S hS (toNormalizationIn B S hS E C f hqc hqc' hid).left.hom
```

**`AlgebraicGeometry.Space.isIntegralHom_normalizationIn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorization.lean, line 274](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorization.lean#L274). The attribute's comment: “part (2): the normalization morphism is integral”.

> **Stacks 0A19, clause (2): `π` is integral.**  This is clause (1) of Stacks 0823 for the
> same factorization, proved as
> `AlgebraicGeometry.Space.isRelativeNormalization_toNormalizationIn`, and it carries that
> theorem's inputs: the universal property `P` of the relative spectrum, the dictionary `D` of
> Stacks 03ZP between integral morphisms affine over `Y` and integral algebras, and the clause
> `hloc` of Stacks 0820 that a locally integral section over an affine chart is integral.

```lean
theorem isIntegralHom_normalizationIn
    (P : RelativeSpecUniversalProperty B S hS E C) (D : IntegralAlgebraDictionary B S hS E)
    (hloc : (pushforwardAlgebra B S hS (Over.mk f)).IsIntegralLocalOnAffineCharts) :
    IsIntegralHom B S hS (normalizationIn B S hS E f hqc').obj.hom.hom
```

**`AlgebraicGeometry.Space.isRelativeNormalization_steinFactorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorization.lean, line 288](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorization.lean#L288). The attribute's comment: “part (5): the intermediate space is the normalization of Y in X”.

> **Stacks 0A19, clause (5): `Y'` is the normalization of `Y` in `X`.**  The factorization
> `f = f' ≫ π` has the two properties of Stacks 0823 which characterize the normalization:
> `π` is integral, and every factorization of `f` through an integral morphism of algebraic
> spaces to `Y` receives a unique compatible morphism from `Y'`.

```lean
theorem isRelativeNormalization_steinFactorization
    (P : RelativeSpecUniversalProperty B S hS E C) (D : IntegralAlgebraDictionary B S hS E)
    (hloc : (pushforwardAlgebra B S hS (Over.mk f)).IsIntegralLocalOnAffineCharts) :
    IsRelativeNormalization B S hS f.hom
      (normalizationIn B S hS E f hqc').obj.hom.hom
      (toNormalizationIn B S hS E C f hqc hqc' hid).left.hom
```

**`AlgebraicGeometry.Space.steinFactorization_of_universallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorizationFlatBaseChange.lean, line 297](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorizationFlatBaseChange.lean#L297). The attribute's comment: “all five clauses and the compatibility with flat base change, for the factorization through the normalization of Stacks 0822”. References: EGA III (4.3.4), “more general”; EGA III (7.8.10), “partial”.

> **Stacks 0A19 (Stein factorization).**  Let `f : X ⟶ Y` be a universally closed and
> quasi-separated morphism of algebraic spaces over `S`.  It is quasi-compact (Stacks 04XW); let
> `Y'` be the normalization of `Y` in `X` (Stacks 0822), with `π : Y' ⟶ Y` and the canonical
> `f' : X ⟶ Y'`.  Then `f = π ∘ f'`, and
>
> 1. `f'` is universally closed, quasi-compact, quasi-separated and surjective;
> 2. `π` is integral;
> 3. `f'_* 𝒪_X = 𝒪_{Y'}`: the structure map `𝒪_{Y'} ⟶ f'_* 𝒪_X` is an isomorphism;
> 4. `Y' = \underline{Spec}_Y(f_* 𝒪_X)`: `π` is affine and the map `π_* 𝒪_{Y'} ⟶ f_* 𝒪_X` of
>    `𝒪_Y`-algebras induced by `f'` is an isomorphism;
> 5. `Y'` is the normalization of `Y` in `X`, here in the characterizing form of Stacks 0823 (it is
>    that normalization by construction).
>
> Moreover formation of the factorization commutes with flat base change: for a flat `g : Y₁ ⟶ Y`,
> a fibre product `X₁ = Y₁ ×_Y X` with `f₁ : X₁ ⟶ Y₁`, a fibre product `P = Y₁ ×_Y Y'` with
> `p : P ⟶ Y₁`, and the base change `h : X₁ ⟶ P` of `f'`, the morphism `f₁` is again universally
> closed and quasi-separated (so quasi-compact), the factorization `X₁ ⟶ P ⟶ Y₁` is the normalization
> of `Y₁` in `X₁` in the sense of Stacks 0823, and it is identified with the factorization of `f₁`
> through its own normalization by a unique isomorphism compatible with both factorizations.

```lean
theorem steinFactorization_of_universallyClosed (huc : UniversallyClosed B S hS f.hom)
    (hfqs : IsQuasiSeparated B S hS f.hom) :
    let hfqc := isQuasiCompact_of_universallyClosed B S hS X.2 Y.2 f.hom huc
    toNormalizationInQcqs f hfqc hfqs ≫ normalizationInQcqsHom B S hS f hfqc hfqs = f ∧
      (UniversallyClosed B S hS (toNormalizationInQcqs f hfqc hfqs).hom ∧
        IsQuasiCompact B S hS (toNormalizationInQcqs f hfqc hfqs).hom ∧
        IsQuasiSeparated B S hS (toNormalizationInQcqs f hfqc hfqs).hom ∧
        IsSurjective B S hS (toNormalizationInQcqs f hfqc hfqs).hom) ∧
      IsIntegralHom B S hS (normalizationInQcqsHom B S hS f hfqc hfqs).hom ∧
      IsIso (smallEtaleRingedToposHom B S hS (toNormalizationInQcqs f hfqc hfqs)).fSharp ∧
      (IsAffineHom B S hS (normalizationInQcqsHom B S hS f hfqc hfqs).hom ∧
        IsIso (pushforwardAlgebraMap B S hS (toNormalizationInQcqsOver f hfqc hfqs))) ∧
      IsRelativeNormalization B S hS f.hom (normalizationInQcqsHom B S hS f hfqc hfqs).hom
        (toNormalizationInQcqs f hfqc hfqs).hom ∧
      ∀ {X₁ Y₁ P : AlgebraicSpaces B S hS} {g : Y₁ ⟶ Y} {f₁ : X₁ ⟶ Y₁} {g' : X₁ ⟶ X},
        IsPullback g' f₁ f g → IsFlat B S hS g.hom →
        ∀ {q : P ⟶ normalizationInQcqs B S hS f hfqc hfqs} {p : P ⟶ Y₁},
          IsPullback q p (normalizationInQcqsHom B S hS f hfqc hfqs) g →
          ∀ h : X₁ ⟶ P, h ≫ q = g' ≫ toNormalizationInQcqs f hfqc hfqs → h ≫ p = f₁ →
            UniversallyClosed B S hS f₁.hom ∧
              ∃ (hf₁qc : IsQuasiCompact B S hS f₁.hom) (hf₁qs : IsQuasiSeparated B S hS f₁.hom),
                IsRelativeNormalization B S hS f₁.hom p.hom h.hom ∧
                  ∃! e : normalizationInQcqs B S hS f₁ hf₁qc hf₁qs ≅ P,
                    toNormalizationInQcqs f₁ hf₁qc hf₁qs ≫ e.hom = h ∧
                      e.hom ≫ p = normalizationInQcqsHom B S hS f₁ hf₁qc hf₁qs
```

**`AlgebraicGeometry.Space.isSurjective_toNormalizationInQcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorizationGeneral.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorizationGeneral.lean#L207). The attribute's comment: “clause (1): the morphism f' : X ⟶ Y' to the normalization of Y in X is surjective, for a universally closed f”.

> **`f'` is surjective**, which is the remaining assertion of clause (1) of Stacks 0A19.  The
> factorization `f = f' ≫ π` has the characterizing property of Stacks 0823
> (`AlgebraicGeometry.Space.isRelativeNormalization_normalizationInQcqs`), and `f'` is
> quasi-compact and universally closed, so
> `AlgebraicGeometry.Space.isSurjective_of_isRelativeNormalization` applies.

```lean
theorem isSurjective_toNormalizationInQcqs (hfuc : UniversallyClosed B S hS f.hom) :
    IsSurjective B S hS (toNormalizationInQcqs f hfqc hfqs).hom
```

## Tag 0E1C, a lemma

[Tag 0E1C](https://stacks.math.columbia.edu/tag/0E1C) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isAffine_finite_fibres_normalizationInQcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorizationQcqsFiniteFibres.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorizationQcqsFiniteFibres.lean#L70).

> **Stacks 0E1C.**  Let `f : X ⟶ Y` be a universally closed and quasi-separated morphism of
> algebraic spaces over `S` and `X ⟶ Y' ⟶ Y` its Stein factorization of Stacks 0A19, the
> normalization `π : Y' ⟶ Y` of `Y` in `X`.  Assume in addition that `f` is locally of finite type
> and that `Y` is affine, represented by an affine `T`.  Then `Y'` is represented by an affine
> `T'`, with `π` represented by `p : T' ⟶ T`, and for every point `y` of `Y` the fibre
> `π⁻¹({y})` is finite and the residue field extension `κ(y')/κ(y)` is finite for every `y'` in
> it.

```lean
theorem exists_isAffine_finite_fibres_normalizationInQcqs {X Y : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (huc : UniversallyClosed B S hS f.hom) (hfqs : IsQuasiSeparated B S hS f.hom)
    (hlft : IsLocallyOfFiniteType B S hS f.hom)
    (T : BigFppfOver B S hS) (hT : IsAffine ((BigFppfOver.toScheme B S hS).obj T))
    (eY : yoneda.obj T ⟶ Y.obj) [IsIso eY] :
    ∃ (T' : BigFppfOver B S hS) (p : T' ⟶ T)
      (e : yoneda.obj T' ⟶ (normalizationInQcqs B S hS f
        (isQuasiCompact_of_universallyClosed B S hS X.property Y.property f.hom huc) hfqs).obj),
      IsAffine ((BigFppfOver.toScheme B S hS).obj T') ∧ IsIso e ∧
      yoneda.map p ≫ eY = e ≫ (normalizationInQcqsHom B S hS f
        (isQuasiCompact_of_universallyClosed B S hS X.property Y.property f.hom huc) hfqs).hom ∧
      ∀ y : (BigFppfOver.toScheme B S hS).obj T,
        (((BigFppfOver.toScheme B S hS).map p) ⁻¹' {y}).Finite ∧
        ∀ y' ∈ ((BigFppfOver.toScheme B S hS).map p) ⁻¹' {y},
          (((BigFppfOver.toScheme B S hS).map p).residueFieldMap y').hom.Finite
```

## Tag 0A1A, a lemma

[Tag 0A1A](https://stacks.math.columbia.edu/tag/0A1A) in the Stacks Project.

**`AlgebraicGeometry.Space.connectedSpace_geometricFiber_iff_forall_scheme_etaleNeighborhood`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricFibreConnected.lean, line 270](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GeometricFibreConnected.lean#L270).

> **Stacks 0A1A.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over a scheme `S` of a big
> fppf site and let `y` be a geometric point of `Y`. The geometric fibre of `f` above `y` is
> connected if and only if, for every étale neighbourhood of `y` whose underlying algebraic space is
> isomorphic to a scheme `W` of the site, the base change of `f` to that neighbourhood has connected
> fibre above the point of `W` underlying the chosen lift of `y`.
>
> Both fibres are presheaf fibre products, and the fibre above the point of `W` is the one above the
> residue field point there
> (`AlgebraicGeometry.Space.representedResidueFieldPointInNeighborhood`).

```lean
theorem connectedSpace_geometricFiber_iff_forall_scheme_etaleNeighborhood
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (y : GeometricPoint B S hS Y) :
    ConnectedPullback B S hS f (yonedaEquiv.symm y.val.value) ↔
      ∀ (U : EtaleNeighborhood B S hS Y hY y) (W : BigFppfOver B S hS)
        (e : U.space ≅ yoneda.obj W),
        ConnectedPullback B S hS f
          (yonedaEquiv.symm (representedResidueFieldPointInNeighborhood B S hS U W e).value ≫
            U.toBase)
```

## Tag 0A1B, a theorem

[Tag 0A1B](https://stacks.math.columbia.edu/tag/0A1B) in the Stacks Project.

**`AlgebraicGeometry.Space.isFinite_normalizationInQcqsHom_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInFiniteOfProper.lean, line 251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInFiniteOfProper.lean#L251). The attribute's comment: “part (2): for f proper with Y locally Noetherian, the morphism pi : Y' -> Y from the normalization of Y in X (Stacks 0822), through which f factors as X -> Y' -> Y, is finite”.

> **Stacks 0A1B, clause (2): `π : Y' ⟶ Y` is finite.**  For a proper morphism `f : X ⟶ Y` of
> algebraic spaces with `Y` locally Noetherian, the normalization `ν : Y' ⟶ Y` of `Y` in `X`
> (Stacks 0822) is a finite morphism: it is the relative spectrum of the integral closure `𝒪'` of
> `𝒪_Y` in `f_* 𝒪_X`, which is a finite `𝒪_Y`-algebra.

```lean
theorem isFinite_normalizationInQcqsHom_of_isProper (hf : IsProper B S hS f.hom)
    (hY : HasEtaleLocalProperty B S hS Y.1 (fun T : Scheme.{u} => IsLocallyNoetherian T)) :
    IsFinite B S hS (normalizationInQcqsHom B S hS f hf.2.1.2
      (isQuasiSeparated_of_isSeparated B S hS hf.1)).hom
```

**`AlgebraicGeometry.Space.isProper_toNormalizationIn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorization.lean, line 362](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorization.lean#L362). The attribute's comment: “part (1): the morphism to the normalization is proper”.

> **Stacks 0A1B, clause (1): `f'` is proper.**  By Stacks 04NX part (2), since the composite
> `f = f' ≫ π` is proper and `π` is separated.

```lean
theorem isProper_toNormalizationIn (hf : IsProper B S hS f.hom) :
    IsProper B S hS (toNormalizationIn B S hS E C f hqc hqc' hid).left.hom
```

**`AlgebraicGeometry.Space.isProper_and_connectedPullback_toNormalizationInQcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorizationNoetherianConnectedFibres.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorizationNoetherianConnectedFibres.lean#L55). The attribute's comment: “part (1): for f proper with Y locally Noetherian, the morphism f' : X -> Y' to the normalization of Y in X (Stacks 0822), with f = pi o f', is proper and its geometric fibres are connected”.

> **Stacks 0A1B, clause (1).**  Let `f : X ⟶ Y` be a proper morphism of algebraic spaces with
> `Y` locally Noetherian.  The morphism `f' : X ⟶ Y'` to the normalization of `Y` in `X`
> (Stacks 0822), through which `f` factors as `f = π ∘ f'`, is proper, and its geometric fibres are
> connected: for every geometric point `ȳ` of `Y'` the fibre `X ×_{Y'} ȳ` has connected point
> space.

```lean
theorem isProper_and_connectedPullback_toNormalizationInQcqs (f : X ⟶ Y)
    (hf : IsProper B S hS f.hom)
    (hY : HasEtaleLocalProperty B S hS Y.1 (fun T : Scheme.{u} => IsLocallyNoetherian T)) :
    IsProper B S hS
        (toNormalizationInQcqs f hf.2.1.2 (isQuasiSeparated_of_isSeparated B S hS hf.1)).hom ∧
      ∀ y : GeometricPoint B S hS (normalizationInQcqs B S hS f hf.2.1.2
          (isQuasiSeparated_of_isSeparated B S hS hf.1)).1,
        ConnectedPullback B S hS
          (toNormalizationInQcqs f hf.2.1.2 (isQuasiSeparated_of_isSeparated B S hS hf.1)).hom
          (yonedaEquiv.symm y.val.value)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.isIso_fSharp_toNormalizationInQcqs`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorizationQcqs.lean#L118), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorizationNoetherianQcqs.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorizationNoetherianQcqs.lean#L86) (StacksFrontier): “part (3): f'\_*O\_X = O\_\{Y'} for the factorization X -> Y' -> Y through the normalization of Stacks 0822 -- the structure map O\_\{Y'} -> f'\_*O\_X is an isomorphism of sheaves of rings; proved for every quasi-compact, quasi-separated, universally closed f, which a proper f is”.
- [`AlgebraicGeometry.Space.isIso_pushforwardAlgebraMap_toNormalizationInQcqsOver_of_universallyClosed`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInUniversallyClosed.lean#L118), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorizationNoetherianQcqs.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorizationNoetherianQcqs.lean#L92) (StacksFrontier): “part (4): Y' = Spec\_Y(f\_*O\_X) for the factorization through the normalization of Stacks 0822 -- pi is affine and the map pi\_*O\_\{Y'} -> f\_*O\_X induced by f' is an isomorphism of O\_Y-algebras; proved for every quasi-compact, quasi-separated, universally closed f, which a proper f is”.
- [`AlgebraicGeometry.Space.isRelativeNormalization_normalizationInQcqs`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInQcqsUniversalProperty.lean#L117), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorizationNoetherianQcqs.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorizationNoetherianQcqs.lean#L98) (StacksFrontier): “part (5): the intermediate space Y' of the factorization X -> Y' -> Y is the normalization of Y in X, in the characterization of Stacks 0823; proved for every quasi-compact quasi-separated f, which a proper f is”.

## Tag 0A1C, a theorem

[Tag 0A1C](https://stacks.math.columbia.edu/tag/0A1C) in the Stacks Project.

**`AlgebraicGeometry.Space.isProper_toNormalizationInQcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorizationGeneral.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorizationGeneral.lean#L176). The attribute's comment: “clause (1): the morphism f' : X ⟶ Y' to the normalization of Y in X is proper, for a proper f and an arbitrary base Y”.

> **Clause (1) of Stacks 0A1C: `f'` is proper.**  By Stacks 04NX part (2), since the composite
> `f = f' ≫ π` is proper and `π` is separated.

```lean
theorem isProper_toNormalizationInQcqs (hf : IsProper B S hS f.hom) :
    IsProper B S hS (toNormalizationInQcqs f hfqc hfqs).hom
```

**`AlgebraicGeometry.Space.steinFactorization_general`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorizationGeneral.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorizationGeneral.lean#L241). The attribute's comment: “clause (1) properness together with the surjectivity of f', clause (2) integrality of pi, clause (4) and clause (5), for a proper morphism of algebraic spaces over an arbitrary base. Clause (3) and the connectedness of the geometric fibres of f' in clause (1) are not asserted”. References: EGA III (7.8.10), “partial”.

> **Stacks 0A1C, clauses (1) properness, (2), (4) and (5).**  Let `f : X ⟶ Y` be a proper
> morphism of algebraic spaces over `S`, let `Y'` be the normalization of `Y` in `X` and let
> `f = f' ≫ π` be the factorization of Stacks 0822.  Then
>
> * `f'` is proper, and surjective — the properness assertion of clause (1), together with the
>   surjectivity that clause (1) of Stacks 0A19 states separately;
> * `π : Y' ⟶ Y` is integral, clause (2) in the form the general case asserts it;
> * `Y' = \underline{Spec}_Y(f_* 𝒪_X)`, clause (4), in the form of Stacks 0A0Q: the map
>   `π_* 𝒪_{Y'} ⟶ f_* 𝒪_X` of `𝒪_Y`-algebras induced by `f'` is invertible;
> * `Y'` is the normalization of `Y` in `X`, clause (5), in the sense of
>   `AlgebraicGeometry.Space.IsRelativeNormalization`.
>
> The conclusion also records the factorization equation itself.
>
> Nothing is assumed about `Y`;  no finiteness enters, which is the point of the general case
> against Stacks 0A1B.  The two statements of the tag that do not appear here are clause (3) and
> the connectedness of the geometric fibres of `f'` in clause (1);  the module documentation says
> what each would need, and
> `AlgebraicGeometry.Space.steinFactorization_general_of_connectedFibres` adds them as named
> inputs.

```lean
theorem steinFactorization_general (hf : IsProper B S hS f.hom) :
    toNormalizationInQcqs f hfqc hfqs ≫ normalizationInQcqsHom B S hS f hfqc hfqs = f ∧
      IsProper B S hS (toNormalizationInQcqs f hfqc hfqs).hom ∧
      IsSurjective B S hS (toNormalizationInQcqs f hfqc hfqs).hom ∧
      IsIntegralHom B S hS (normalizationInQcqsHom B S hS f hfqc hfqs).hom ∧
      IsIso (pushforwardAlgebraMap B S hS (toNormalizationInQcqsOver f hfqc hfqs)) ∧
      IsRelativeNormalization B S hS f.hom
        (normalizationInQcqsHom B S hS f hfqc hfqs).hom
        (toNormalizationInQcqs f hfqc hfqs).hom
```

**`AlgebraicGeometry.Space.steinFactorization_general_complete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorizationGeneralRegistration.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorizationGeneralRegistration.lean#L191). The attribute's comment: “all five clauses, for the factorization X ⟶ Y' ⟶ Y through the normalization of Y in X (0822): f' proper with connected geometric fibres, π integral, f'\_*O\_X = O\_\{Y'} as the invertibility of the structure map, Y' = Spec\_Y(f\_*O\_X) as π affine with π\_*O\_\{Y'} ≅ f\_*O\_X, and the 0823 characterization of the normalization”.

> **Stacks 0A1C (Stein factorization; general case).**  Let `f : X ⟶ Y` be a proper morphism
> of algebraic spaces over a scheme `S`.  Let `π : Y' ⟶ Y` be the normalization of `Y` in `X`
> (Stacks 0822, `AlgebraicGeometry.Space.normalizationInQcqs`, which needs `f` quasi-compact and
> quasi-separated, as a proper morphism is) and `f' : X ⟶ Y'` the canonical morphism, so that
> `f = π ∘ f'`.  Then:
>
> 1. `f'` is proper with connected geometric fibres: for every geometric point `ȳ` of `Y'` the
>    fibre `X ×_{Y'} ȳ` has connected point space;
> 2. `π : Y' ⟶ Y` is integral;
> 3. `f'_*𝒪_X = 𝒪_{Y'}`: the structure map `𝒪_{Y'} ⟶ f'_*𝒪_X` of Stacks 03G8 is an isomorphism;
> 4. `Y' = \underline{Spec}_Y(f_*𝒪_X)`: `π` is affine and the map `π_*𝒪_{Y'} ⟶ f_*𝒪_X` of
>    `𝒪_Y`-algebras induced by `f'` is an isomorphism;
> 5. `Y'` is the normalization of `Y` in `X`: the factorization has the two properties of
>    Stacks 0823 which characterize it.
>
> The conclusion also records the factorization `f = π ∘ f'` itself.  No hypothesis beyond
> properness of `f` is used.

```lean
theorem steinFactorization_general_complete (f : X ⟶ Y) (hf : IsProper B S hS f.hom) :
    let hfqc := isQuasiCompact_of_universallyClosed B S hS X.2 Y.2 f.hom hf.2.2
    let hfqs := isQuasiSeparated_of_isSeparated B S hS hf.1
    toNormalizationInQcqs f hfqc hfqs ≫ normalizationInQcqsHom B S hS f hfqc hfqs = f ∧
      (IsProper B S hS (toNormalizationInQcqs f hfqc hfqs).hom ∧
        ∀ y : GeometricPoint B S hS (normalizationInQcqs B S hS f hfqc hfqs).1,
          ConnectedPullback B S hS (toNormalizationInQcqs f hfqc hfqs).hom
            (yonedaEquiv.symm y.val.value)) ∧
      IsIntegralHom B S hS (normalizationInQcqsHom B S hS f hfqc hfqs).hom ∧
      IsIso (smallEtaleRingedToposHom B S hS (toNormalizationInQcqs f hfqc hfqs)).fSharp ∧
      (IsAffineHom B S hS (normalizationInQcqsHom B S hS f hfqc hfqs).hom ∧
        IsIso (pushforwardAlgebraMap B S hS (toNormalizationInQcqsOver f hfqc hfqs))) ∧
      IsRelativeNormalization B S hS f.hom (normalizationInQcqsHom B S hS f hfqc hfqs).hom
        (toNormalizationInQcqs f hfqc hfqs).hom
```

## Tag 0AYI, a lemma

[Tag 0AYI](https://stacks.math.columbia.edu/tag/0AYI) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_fSharp_and_connectedPullback_of_isNormal_of_isIntegralSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperNormalIntegralBaseFibres.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ProperNormalIntegralBaseFibres.lean#L167).

> **Stacks 0AYI.**  Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` such that
>
> 1. `f` is proper,
> 2. `Y` is integral (Stacks 0AD4, `AlgebraicGeometry.Space.IsIntegralSpace`) with generic point `ξ`,
> 3. `Y` is normal,
> 4. `X` is reduced,
> 5. every generic point of an irreducible component of `|X|` maps to `ξ`,
> 6. `H⁰(X_ξ, 𝒪) = κ(ξ)`: for the monomorphism `Spec κ(ξ) ⟶ Y` from the spectrum of the residue
>    field at `ξ` (Stacks 0EMW) and the fibre `X_ξ = X ×_Y Spec κ(ξ)`, pullback of global functions
>    `κ(ξ) = Γ(Spec κ(ξ), 𝒪) ⟶ Γ(X_ξ, 𝒪)` along the projection is bijective.
>
> Then
>
> * `f_* 𝒪_X = 𝒪_Y`: the canonical map `𝒪_Y ⟶ f_* 𝒪_X` (Stacks 03G8) is an isomorphism;
> * `f` has geometrically connected fibres: for every field `k` and every morphism `Spec k ⟶ Y`, the
>   fibre `X ×_Y Spec k` has connected point space.  Taking `Spec k ⟶ Spec κ(y) ⟶ Y` for the field
>   extensions `k` of the residue field at a point `y`, this says that the fibre `X_y` is
>   geometrically connected over `κ(y)`.
>
> Normality and reducedness are the étale-local properties of schemes of Stacks 03E6, as elsewhere
> in the library.

```lean
theorem isIso_fSharp_and_connectedPullback_of_isNormal_of_isIntegralSpace
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hf : IsProper B S hS f.hom) (hYint : IsIntegralSpace B S hS Y.1)
    {ξ : points B S hS Y.1} (hξ : IsGenericPoint ξ Set.univ)
    (hYnormal : HasEtaleLocalProperty B S hS Y.1 (fun T : Scheme.{u} => IsNormal T))
    (hXred : HasEtaleLocalProperty B S hS X.1 (fun T : Scheme.{u} => IsReduced T))
    (hgen : ∀ x ∈ genericPoints (points B S hS X.1), pointsMap B S hS X.1 f.hom x = ξ)
    (h6 : Function.Bijective (globalFunctionsMap B S hS (pullback.snd f
      (ObjectProperty.homMk (residueFieldMorphism B S hS Y.1 hYint.2.1 ξ) :
        schemeSpace ((residueFieldRepresentative B S hS Y.1 hYint.2.1 ξ).1.siteObject B S hS Y.1) ⟶
          Y)))) :
    IsIso (smallEtaleRingedToposHom B S hS f).fSharp ∧
      ∀ p : FieldValuedPoint B S hS Y.1,
        ConnectedPullback B S hS f.hom (fieldMorphism B S hS Y.1 p)
```

## Tag 0E1D, a lemma

[Tag 0E1D](https://stacks.math.columbia.edu/tag/0E1D) in the Stacks Project.

**`AlgebraicGeometry.Space.lowerSemicontinuous_numberGeometricConnectedComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/GeometricComponentsLowerSemicontinuous.lean, line 473](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/GeometricComponentsLowerSemicontinuous.lean#L473). References: EGA IV (15.5.9), “more general”.

> **Stacks 0E1D.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which is proper,
> flat and of finite presentation.  Then the function `n_{X/Y} : |Y| → ℕ∞` counting the geometric
> connected components of the fibres of `f` (Stacks 0E1B,
> `AlgebraicGeometry.Space.numberGeometricConnectedComponents`) is lower semicontinuous.

```lean
theorem lowerSemicontinuous_numberGeometricConnectedComponents
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hproper : IsProper B S hS f)
    (hflat : IsFlat B S hS f) (hfp : IsFinitePresentation B S hS f) :
    LowerSemicontinuous (numberGeometricConnectedComponents B S hS f)
```

## Tag 0E1E, a lemma

[Tag 0E1E](https://stacks.math.columbia.edu/tag/0E1E) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyConstant_numberGeometricConnectedComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/GeometricComponentsLocallyConstantUnconditional.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/GeometricComponentsLocallyConstantUnconditional.lean#L192).

> **Stacks 0E1E.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which is proper,
> flat and of finite presentation, and whose geometric fibres are reduced. Then the function
> `n_{X/Y} : |Y| → ℕ∞` counting the geometric connected components of the fibres of `f`
> (Stacks 0E1B) is locally constant.

```lean
theorem isLocallyConstant_numberGeometricConnectedComponents
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf : IsProper B S hS f) (hfl : IsFlat B S hS f) (hfp : IsFinitePresentation B S hS f)
    (hred : ∀ y, IsGeometricallyReducedFibreAt B S hS f hX hY y) :
    IsLocallyConstant (numberGeometricConnectedComponents B S hS f)
```

## Tag 0E0D, a lemma

[Tag 0E0D](https://stacks.math.columbia.edu/tag/0E0D) in the Stacks Project.

**`AlgebraicGeometry.Space.isFinite_and_isEtale_normalizationInQcqsHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorizationFlatProperFiniteEtale.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SteinFactorizationFlatProperFiniteEtale.lean#L50). The attribute's comment: “for the Stein factorization X ⟶ Y' ⟶ Y of 0A1C, Y' the normalization of Y in X: Y' ⟶ Y is finite and étale when f is proper, flat, of finite presentation, with geometrically reduced fibres”.

> **Stacks 0E0D.**  Let `f : X ⟶ Y` be a proper morphism of algebraic spaces over `S`, and let
> `X ⟶ Y' ⟶ Y` be its Stein factorization (Stacks 0A1C): `Y'` is the normalization of `Y` in `X`,
> `AlgebraicGeometry.Space.normalizationInQcqs`, with structure morphism
> `AlgebraicGeometry.Space.normalizationInQcqsHom`.  If `f` is of finite presentation, flat, with
> geometrically reduced fibres (Stacks 0E08), then `Y' ⟶ Y` is finite étale.

```lean
theorem isFinite_and_isEtale_normalizationInQcqsHom
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (hf : IsProper B S hS f.hom)
    (hfp : IsFinitePresentation B S hS f.hom) (hfl : IsFlat B S hS f.hom)
    (hred : ∀ y, IsGeometricallyReducedFibreAt B S hS f.hom X.2 Y.2 y) :
    let h := isQuasiCompact_isQuasiSeparated_of_isProper B S hS f hf
    IsFinite B S hS (normalizationInQcqsHom B S hS f h.1 h.2).hom ∧
      IsEtale B S hS (normalizationInQcqsHom B S hS f h.1 h.2).hom
```

## Tag 0CWI, a lemma

[Tag 0CWI](https://stacks.math.columbia.edu/tag/0CWI) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.exists_isOpenSubspace_isClosedSubspace_isProper_of_henselianPair`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClopenLiftOverHenselianPair.lean#L216), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/ProperPartOverHenselianPairTag.lean, line 24](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ProperPartOverHenselianPairTag.lean#L24) (StacksFrontier): “the whole tag, on the theorem proved in ClopenLiftOverHenselianPair”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.36, Tag 0A18](https://stacks.math.columbia.edu/tag/0A18)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
