---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.exists_etale_coordinateSubspaceEmbedding_isPullback, Stacks.MoreMorphisms.coordinateEmbedding_ker_eq_span, Stacks.MoreMorphisms.coordinateChart_equiv_polynomial, Stacks.MoreMorphisms.coordinateChart_exceptionalIdeal, Stacks.MoreMorphisms.blowUp_smooth, Stacks.MoreMorphisms.exceptionalDivisor_smooth, Stacks.MoreMorphisms.exists_coordinateReesPresentation, Stacks.MoreMorphisms.coordinateEmbedding_isClosedImmersion
statement: formalized
proof: formalized
---

# 37.17 Closed immersions between smooth schemes

Section 37.17 of the Stacks Project, [Tag 0H1G](https://stacks.math.columbia.edu/tag/0H1G). 3 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FUE, a lemma

[Tag 0FUE](https://stacks.math.columbia.edu/tag/0FUE) in the Stacks Project.

**`Stacks.AlgebraicGeometry.exists_etale_coordinateSubspaceEmbedding_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SmoothClosedImmersionCoordinates.lean, line 1010](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SmoothClosedImmersionCoordinates.lean#L1010).

> **Stacks Project, Tag 0FUE.** Let `S` be a scheme and let `i : Y ⟶ X` be a closed immersion
> of schemes smooth over `S`. For every `y : Y` there are integers `m, n ≥ 0`, an open
> `U ⊆ X` whose inverse image `V = i⁻¹(U)` contains `y`, an étale morphism
> `π : U ⟶ 𝐀^{m+n}_S` over `S` and a morphism `q : V ⟶ 𝐀^m_S` making
> ```
> Y ←── V ──→ 𝐀^m_S
> │      │        │
> ↓      ↓        ↓
> X ←── U ──→ 𝐀^{m+n}_S
> ```
> commute with cartesian right-hand square, i.e. `V = π⁻¹(𝐀^m_S)`.

```lean
theorem exists_etale_coordinateSubspaceEmbedding_isPullback
    {S X Y : Scheme.{u}} (f : X ⟶ S) (i : Y ⟶ X)
    [IsClosedImmersion i] [Smooth f] [Smooth (i ≫ f)] (y : Y) :
    ∃ (m n : ℕ) (U : X.Opens) (_ : y ∈ i ⁻¹ᵁ U)
      (π : U.toScheme ⟶ AffineSpace (ULift.{u} (Fin (m + n))) S)
      (q : (i ⁻¹ᵁ U).toScheme ⟶ AffineSpace (ULift.{u} (Fin m)) S),
      Etale π ∧
        π ≫ (AffineSpace.over (ULift.{u} (Fin (m + n))) S).hom = U.ι ≫ f ∧
        IsPullback
          (i.resLE U (i ⁻¹ᵁ U) le_rfl) q π (coordinateSubspaceEmbedding S m n)
```

## Tag 0H1H, a remark

[Tag 0H1H](https://stacks.math.columbia.edu/tag/0H1H) in the Stacks Project.

**`Stacks.MoreMorphisms.coordinateEmbedding_ker_eq_span`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/CoordinateBlowup.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/CoordinateBlowup.lean#L139). The attribute's comment: “ideal of the center”.

> The scheme-theoretic centre is cut out by exactly the last `n` coordinates.

```lean
public theorem coordinateEmbedding_ker_eq_span :
    coordinateRingIdeal R m n = RingHom.ker (coordinateProjection R m n)
```

**`Stacks.MoreMorphisms.coordinateChart_equiv_polynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/CoordinateBlowup.lean, line 406](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/CoordinateBlowup.lean#L406). The attribute's comment: “polynomial affine blowup charts”.

> The `i`-th standard blowup chart is polynomial affine space, with its original coordinates
> given by `x_k`, `y_i`, and `y_j = y_i t_j`.

```lean
public theorem coordinateChart_equiv_polynomial :
    ∃ e : coordinateChartAlgebra R m n i ≃+*
        MvPolynomial (coordinateChartVariables m n i) R,
      (∀ r : R,
        e (algebraMap R (coordinateChartAlgebra R m n i) r) = C r) ∧
      (∀ k : Fin m,
        e (algebraMap (MvPolynomial (Fin m ⊕ Fin n) R)
          (coordinateChartAlgebra R m n i) (X (Sum.inl k))) = X (Sum.inl k)) ∧
      (e (algebraMap (MvPolynomial (Fin m ⊕ Fin n) R)
          (coordinateChartAlgebra R m n i) (X (Sum.inr i))) = X (Sum.inr (Sum.inl ()))) ∧
      (∀ j : Fin n, ∀ h : j ≠ i,
        e (algebraMap (MvPolynomial (Fin m ⊕ Fin n) R)
          (coordinateChartAlgebra R m n i) (X (Sum.inr j))) =
          X (Sum.inr (Sum.inl ())) * X (Sum.inr (Sum.inr ⟨j, h⟩)))
```

**`Stacks.MoreMorphisms.coordinateChart_exceptionalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/CoordinateBlowup.lean, line 435](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/CoordinateBlowup.lean#L435). The attribute's comment: “equation of the exceptional divisor in each chart”.

> On the `i`-th affine chart, the exceptional ideal is generated by the single coordinate
> `y_i`.

```lean
public theorem coordinateChart_exceptionalIdeal (i : Fin n) :
    Ideal.map (algebraMap (MvPolynomial (Fin m ⊕ Fin n) R) (coordinateChartAlgebra R m n i))
        (coordinateRingIdeal R m n) =
      Ideal.span {(algebraMap (MvPolynomial (Fin m ⊕ Fin n) R) (coordinateChartAlgebra R m n i)
        (X (Sum.inr i)))}
```

**`Stacks.MoreMorphisms.blowUp_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/CoordinateBlowupSmooth.lean, line 548](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/CoordinateBlowupSmooth.lean#L548). The attribute's comment: “smoothness of the blowup”.

> **Stacks Project, Tag 0H1H.** The blowup of affine `(m + n)`-space along the coordinate
> affine `m`-subspace is smooth over the base ring.
>
> The hypothesis `0 < n` is the one the source carries and is not used; see
> `Stacks.MoreMorphisms.blowUp_smooth_of_pos` for the same statement without it.

```lean
public theorem blowUp_smooth (_hn : 0 < n) :
    Smooth (blowUpToBase (coordinateIdeal R m n) ≫
      Spec.map (CommRingCat.ofHom (C : R →+* MvPolynomial (Fin m ⊕ Fin n) R)))
```

**`Stacks.MoreMorphisms.exceptionalDivisor_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/CoordinateExceptionalSmooth.lean, line 552](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/CoordinateExceptionalSmooth.lean#L552). The attribute's comment: “smoothness of the exceptional divisor”.

> The exceptional divisor of the blowup of affine `(m + n)`-space along the coordinate affine
> `m`-subspace is smooth over the base ring.
>
> The hypothesis `0 < n` is the one the source carries and is not used; see
> `Stacks.MoreMorphisms.exceptionalDivisor_smooth_of_pos` for the same theorem without it.

```lean
public theorem exceptionalDivisor_smooth (_hn : 0 < n) :
    Smooth ((exceptionalIdeal (coordinateIdeal R m n)).subschemeι ≫
      blowUpToBase (coordinateIdeal R m n) ≫
      Spec.map (CommRingCat.ofHom (C : R →+* MvPolynomial (Fin m ⊕ Fin n) R)))
```

**`Stacks.MoreMorphisms.exists_coordinateReesPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/CoordinateReesPresentation.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/CoordinateReesPresentation.lean#L43). The attribute's comment: “the Rees algebra is A[T]/(y_i T_j - y_j T_i)”.

> The Rees algebra of `A = R[x₁,…,x_m,y₁,…,y_n]` with respect to the ideal `(y₁,…,y_n)` is
> `A[T₁,…,T_n]/(y_i T_j − y_j T_i)`, with `T_i` going to the degree-one element `y_i`.

```lean
public theorem exists_coordinateReesPresentation :
    ∃ E : (MvPolynomial (Fin n) (MvPolynomial (Fin m ⊕ Fin n) R) ⧸
        Ideal.span (Set.range fun p : Fin n × Fin n ↦
          C (X (Sum.inr p.1)) * X p.2 - C (X (Sum.inr p.2)) * X p.1))
        ≃ₐ[MvPolynomial (Fin m ⊕ Fin n) R] reesAlgebra (coordinateRingIdeal R m n),
      ∀ j : Fin n,
        (E (Ideal.Quotient.mk _ (X j)) : Polynomial (MvPolynomial (Fin m ⊕ Fin n) R)) =
          Polynomial.monomial 1 (X (Sum.inr j))
```

**`Stacks.MoreMorphisms.coordinateEmbedding_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/CoordinateSubspace.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/CoordinateSubspace.lean#L78). The attribute's comment: “coordinate closed immersion”.

> The coordinate affine subspace is closed in the ambient affine space.

```lean
public theorem coordinateEmbedding_isClosedImmersion (R : Type*) [CommRing R] (m n : ℕ) :
    IsClosedImmersion (coordinateEmbedding R m n)
```

## Tag 0FUT, a lemma

[Tag 0FUT](https://stacks.math.columbia.edu/tag/0FUT) in the Stacks Project.

**`Stacks.AlgebraicGeometry.smooth_exceptionalDivisor_isoProjectiveBundle_twistOne_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ExceptionalProjectiveBundle.lean, line 408](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/ExceptionalProjectiveBundle.lean#L408). The attribute's comment: “all four assertions, for a closed immersion of schemes smooth over the base”.

> **Stacks Project, Tag 0FUT.**  Let `S` be a scheme and let `i : Z ⟶ X` be a closed immersion
> of schemes smooth over `S`, with ideal sheaf `ℐ = ker(i) ⊂ 𝒪_X`.  Let `b : X' ⟶ X` be the blowup
> of `X` in `ℐ` and `E ⊆ X'` its exceptional divisor.  Then `X'` and `E` are smooth over `S`; the
> morphism `p : E ⟶ Z` is canonically isomorphic to the projective space bundle
> `𝐏(ℐ/ℐ²) ⟶ Z`; and the relative `𝒪_E(1)` of that bundle structure is the restriction of
> `𝒪_{X'}(-E)` to `E`.
>
> The morphisms to the centre are the two morphisms `p : E ⟶ Z` and `q : 𝐏(ℐ/ℐ²) ⟶ Z` over `X`,
> each determined by its composite with the closed immersion `i`, and the third assertion is that
> the identification `E ≅ 𝐏(ℐ/ℐ²)` carries `p` to `q`.
>
> This is `Stacks.AlgebraicGeometry.smooth_exceptionalDivisor_isoProjectiveBundle_twistOne` read at
> the ideal sheaf `i.ker` of the closed immersion, whose closed subscheme `V(i.ker)` receives `Z`
> by the canonical isomorphism `AlgebraicGeometry.Scheme.Hom.toImage` onto the scheme-theoretic
> image; smoothness transports along that isomorphism, and `p` and `q` are read on `Z` through its
> inverse.

```lean
theorem smooth_exceptionalDivisor_isoProjectiveBundle_twistOne_of_isClosedImmersion
    (i : Z ⟶ X) [IsClosedImmersion i] [Smooth f] [Smooth (i ≫ f)] :
    Smooth (blowUpToBase i.ker ≫ f) ∧
      Smooth ((exceptionalIdeal i.ker).subschemeι ≫ blowUpToBase i.ker ≫ f) ∧
      ∃ (p : exceptionalDivisor i.ker ⟶ Z)
        (q : projectiveBundle i.ker.subscheme
            (Stacks.Conormal.conormalSheafDegreeOne i.ker.subschemeι) ⟶ Z)
        (e : exceptionalDivisor i.ker ≅
          projectiveBundle i.ker.subscheme
            (Stacks.Conormal.conormalSheafDegreeOne i.ker.subschemeι)),
        p ≫ i = (exceptionalIdeal i.ker).subschemeι ≫ blowUpToBase i.ker ∧
          q ≫ i = projectiveBundleToBase i.ker.subscheme
                (Stacks.Conormal.conormalSheafDegreeOne i.ker.subschemeι) ≫ i.ker.subschemeι ∧
            e.hom ≫ q = p ∧
              Nonempty ((Scheme.Modules.pullback e.hom).obj
                  (Situation.twistSheaf (symmetricSituationOfQuasicoherent i.ker.subscheme
                    (Stacks.Conormal.conormalSheafDegreeOne i.ker.subschemeι)) 1)
                ≅ (Scheme.Modules.pullback (exceptionalIdeal i.ker).subschemeι).obj
                    (exceptionalIdealModule i.ker))
```

**`Stacks.AlgebraicGeometry.smooth_blowUpToBase_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/SmoothCentre.lean, line 377](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/SmoothCentre.lean#L377). The attribute's comment: “smoothness of the blowup”. References: SGA 7 II (2.1), “more general”; SGA 7 XVIII (2.1), “Smoothness of tilde X”; SGA 7 XVIII (3.1), “more general”.

> **Stacks Project, Tag 0FUT**, first assertion. Let `S` be a scheme and let `i : Z ⟶ X` be a
> closed immersion of schemes smooth over `S`. Then the blowup of `X` in `Z` is smooth over `S`.

```lean
theorem smooth_blowUpToBase_comp {S X Z : Scheme.{u}} (f : X ⟶ S) (i : Z ⟶ X)
    [IsClosedImmersion i] [Smooth f] [Smooth (i ≫ f)] :
    Smooth (blowUpToBase i.ker ≫ f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.17, Tag 0H1G](https://stacks.math.columbia.edu/tag/0H1G)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
