---
declaration: section
origin: cited
lean: Deformation.Examples.SmoothingCriterion.smooth_genericFibre_of_pow_mem_fittingIdeal, Deformation.Examples.Smoothing.exists_nonempty_open_smooth_projection, Deformation.Examples.Smoothing.exists_flat_powerSeries_specialFiber_smooth_genericFiber, Deformation.Examples.Smoothing.exists_finite_powerSeries_specialFiber_etale_genericFiber, Deformation.Examples.Smoothing.exists_flat_essFiniteType_specialFiber_pow_mem_fittingIdeal, Deformation.Examples.Smoothing.exists_flat_isProjective_smoothing_of_isProper, Deformation.Examples.Smoothing.exists_flat_separated_finiteType_smoothing
statement: formalized
proof: formalized
---

# 93.17 Smoothings

Section 93.17 of the Stacks Project, [Tag 0E7S](https://stacks.math.columbia.edu/tag/0E7S). 7 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0E7T, a lemma

[Tag 0E7T](https://stacks.math.columbia.edu/tag/0E7T) in the Stacks Project.

**`Deformation.Examples.SmoothingCriterion.smooth_genericFibre_of_pow_mem_fittingIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SmoothingCriterion.lean, line 540](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/SmoothingCriterion.lean#L540).

> Let `k` be a field, `S = Spec k⟦t⟧` and `Sₙ = Spec (k⟦t⟧/(t^n))`. Let `f : Y ⟶ S` be
> proper and flat with Cohen–Macaulay special fibre, equidimensional of dimension `d`, and let
> `Xₙ = Y ×_S Sₙ` with projections `pr` and `gₙ`. If for some `n ≥ 1` the `d`-th Fitting ideal of
> `Ω_{Xₙ/Sₙ}` contains `t ^ (n - 1)`, then the generic fibre of `f`, taken over the residue field
> of the generic point of `S`, is smooth.

```lean
public theorem smooth_genericFibre_of_pow_mem_fittingIdeal (k : Type u) [Field k]
    {Y : Scheme.{u}} (f : Y ⟶ Spec (.of (PowerSeries k))) [IsProper f] [Flat f]
    (d n : ℕ) (hn : 1 ≤ n)
    (hCM : IsCohenMacaulay (f.fiber (IsLocalRing.closedPoint (PowerSeries k))))
    (hequi : TopologicalSpace.Equidimensional
      (f.fiber (IsLocalRing.closedPoint (PowerSeries k))))
    (hdim : topologicalKrullDim (f.fiber (IsLocalRing.closedPoint (PowerSeries k))) =
      (d : WithBot ℕ∞))
    {Xₙ : Scheme.{u}} {pr : Xₙ ⟶ Y}
    {gₙ : Xₙ ⟶ Spec (.of (PowerSeries k ⧸ Ideal.span
      {(PowerSeries.X : PowerSeries k) ^ n}))}
    (hcart : IsPullback pr gₙ f (Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk
      (Ideal.span {(PowerSeries.X : PowerSeries k) ^ n})))))
    (hfit : ∀ U : Xₙ.affineOpens,
      (pr ≫ f).appLE ⊤ U.1 (le_preimage_top (pr ≫ f) U.1)
          ((Scheme.ΓSpecIso (.of (PowerSeries k))).inv (PowerSeries.X ^ (n - 1))) ∈
        (fittingIdeal (Scheme.Hom.relativeDifferentials gₙ) (d : ℤ)).ideal U) :
    Smooth (f.fiberToSpecResidueField
      (⟨⊥, inferInstance⟩ : PrimeSpectrum (PowerSeries k)))
```

## Tag 0E7U, a lemma

[Tag 0E7U](https://stacks.math.columbia.edu/tag/0E7U) in the Stacks Project.

**`Deformation.Examples.Smoothing.exists_nonempty_open_smooth_projection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/Smoothing/GenericSmoothness.lean, line 472](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/Smoothing/GenericSmoothness.lean#L472).

> The generic affine-linear deformation is smooth over some nonempty open in
> the affine space of its coefficients.

```lean
public theorem exists_nonempty_open_smooth_projection
    (k : Type u) [Field k] (n c : ℕ) (hc : 1 ≤ c) (hcn : c ≤ n)
    (f : Fin c → MvPolynomial (Fin n) k) :
    let R := parameterRing k n c
    let A := deformedCoordinateRing k n c f
    let π : Spec (.of A) ⟶ Spec (.of R) :=
      Spec.map (CommRingCat.ofHom (algebraMap R A))
    ∃ U : (Spec (.of R)).Opens,
      U ≠ ⊥ ∧ Smooth (π.resLE U (π ⁻¹ᵁ U) le_rfl)
```

## Tag 0E7V, a lemma

[Tag 0E7V](https://stacks.math.columbia.edu/tag/0E7V) in the Stacks Project.

**`Deformation.Examples.Smoothing.exists_flat_powerSeries_specialFiber_smooth_genericFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/Smoothing/GlobalCompleteIntersection.lean, line 661](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/Smoothing/GlobalCompleteIntersection.lean#L661). The attribute's comment: “the smoothing of a global complete intersection”.

> **Stacks 0E7V.** A global complete intersection `A` over a field `k` is the special fibre
> `B/XB` of a flat finite type `k⟦X⟧`-algebra `B` whose generic fibre `k⸨X⸩ ⊗[k⟦X⟧] B` is smooth
> over `k⸨X⸩`, and `B` carries a relative global complete intersection presentation whose number
> of variables minus number of relations is the Krull dimension of `A` when `A` is nonzero.

```lean
public theorem exists_flat_powerSeries_specialFiber_smooth_genericFiber
    (k : Type u) [Field k] (A : Type v) [CommRing A] [Algebra k A]
    (hA : IsGlobalCompleteIntersection k A) :
    ∃ (B : Type u) (_ : CommRing B) (_ : Algebra (PowerSeries k) B)
      (_ : Algebra k B) (_ : IsScalarTower k (PowerSeries k) B)
      (_ : Module.Flat (PowerSeries k) B) (_ : Algebra.FiniteType (PowerSeries k) B),
      Nonempty
          ((B ⧸ Ideal.span ({algebraMap (PowerSeries k) B PowerSeries.X} : Set B)) ≃ₐ[k] A) ∧
        Algebra.Smooth (LaurentSeries k)
          (TensorProduct (PowerSeries k) (LaurentSeries k) B) ∧
        ∃ (n c : ℕ) (P : Algebra.Presentation (PowerSeries k) B (Fin n) (Fin c)),
          P.IsRelativeGlobalCompleteIntersection ∧
            (Nontrivial A → ringKrullDim A = ((n - c : ℕ) : WithBot ℕ∞))
```

## Tag 0E7W, a lemma

[Tag 0E7W](https://stacks.math.columbia.edu/tag/0E7W) in the Stacks Project.

**`Deformation.Examples.Smoothing.exists_finite_powerSeries_specialFiber_etale_genericFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/Smoothing/FiniteLocalCompleteIntersection.lean, line 378](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/Smoothing/FiniteLocalCompleteIntersection.lean#L378). The attribute's comment: “the smoothing of a finite local complete intersection”.

> **Stacks 0E7W.** A finite-dimensional local complete intersection `A` over a field `k` is
> the special fibre `B/XB` of a finite flat `k⟦X⟧`-algebra `B` whose generic fibre
> `k⸨X⸩ ⊗[k⟦X⟧] B` is étale over `k⸨X⸩`.

```lean
public theorem exists_finite_powerSeries_specialFiber_etale_genericFiber
    (k : Type u) [Field k] (A : Type v) [CommRing A] [Algebra k A]
    [FiniteDimensional k A] (hA : IsLocalCompleteIntersection k A) :
    ∃ (B : Type (max u v)) (_ : CommRing B) (_ : Algebra (PowerSeries k) B)
      (_ : Algebra k B) (_ : IsScalarTower k (PowerSeries k) B),
      Module.Finite (PowerSeries k) B ∧ Module.Flat (PowerSeries k) B ∧
        Nonempty
          ((B ⧸ Ideal.span ({algebraMap (PowerSeries k) B PowerSeries.X} : Set B)) ≃ₐ[k] A) ∧
      Algebra.Etale (LaurentSeries k)
          (TensorProduct (PowerSeries k) (LaurentSeries k) B)
```

## Tag 0E7X, a lemma

[Tag 0E7X](https://stacks.math.columbia.edu/tag/0E7X) in the Stacks Project.

**`Deformation.Examples.Smoothing.exists_flat_essFiniteType_specialFiber_pow_mem_fittingIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SmoothingEssFiniteType.lean, line 692](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/SmoothingEssFiniteType.lean#L692).

> **Stacks 0E7X.** Let `k` be a field and let `A` be a local `k`-algebra, essentially of finite
> type over `k` and a complete intersection over `k`. Then `A` is the special fibre `B/tB` of a flat
> `k⟦t⟧`-algebra `B` essentially of finite type over `k⟦t⟧`, and for some `n` the element `t^n` lies
> in the `d`-th Fitting ideal of `Ω_{B/k⟦t⟧}`, where `d = dim(A) + trdeg_k(κ)` for `κ` the residue
> field of `A`.

```lean
public theorem exists_flat_essFiniteType_specialFiber_pow_mem_fittingIdeal
    (k : Type u) [Field k] (A : Type v) [CommRing A] [Algebra k A]
    [IsLocalRing A] [Algebra.EssFiniteType k A]
    (hA : IsCompleteIntersectionLocalRing k A) :
    ∃ (dimA trdegResidue n : ℕ),
      ringKrullDim A = (dimA : WithBot ℕ∞) ∧
      Algebra.trdeg k (IsLocalRing.ResidueField A) = trdegResidue ∧
      ∃ (B : Type (max u v)) (_ : CommRing B) (_ : Algebra (PowerSeries k) B)
        (_ : Algebra.EssFiniteType (PowerSeries k) B) (_ : Module.Flat (PowerSeries k) B)
        (_ : Algebra k B) (_ : IsScalarTower k (PowerSeries k) B),
        Nonempty
          ((B ⧸ Ideal.span {algebraMap (PowerSeries k) B PowerSeries.X}) ≃ₐ[k] A) ∧
          algebraMap (PowerSeries k) B (PowerSeries.X ^ n) ∈
            fittingIdeal (M := KaehlerDifferential (PowerSeries k) B)
              ((dimA + trdegResidue : ℕ) : ℤ)
```

## Tag 0E7Y, a lemma

[Tag 0E7Y](https://stacks.math.columbia.edu/tag/0E7Y) in the Stacks Project.

**`Deformation.Examples.Smoothing.exists_flat_isProjective_smoothing_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SmoothingProperCurve.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/SmoothingProperCurve.lean#L104).

> **[Stacks, Tag 0E7Y].** Let `X` be a scheme over a field `k`. Assume (1) `X` is proper over
> `k`, (2) `X` is a local complete intersection over `k`, (3) `X` has dimension `≤ 1`, and (4)
> `X → Spec(k)` is smooth except at finitely many points. Then there exists a flat projective
> morphism `Y → Spec(k[[t]])` whose generic fibre is smooth and whose special fibre is isomorphic to
> `X`.
>
> The generic fibre is the fibre over the zero ideal of `k⟦t⟧`, smooth over its residue field. The
> special fibre is the base change along `Spec k ⟶ Spec k⟦t⟧` given by the constant coefficient,
> and the isomorphism with `X` is one of schemes over `Spec k`. Projectivity is
> `AlgebraicGeometry.IsProjective`, [Stacks, Tag 01W8].

```lean
theorem exists_flat_isProjective_smoothing_of_isProper {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [IsProper f] (hf : IsLocalCompleteIntersectionOverField f) (hdim : topologicalKrullDim X ≤ 1)
    (hfin : (f.smoothLocus : Set X)ᶜ.Finite) :
    ∃ (Y : Scheme.{u}) (g : Y ⟶ Spec (.of (PowerSeries k))),
      Flat g ∧ AlgebraicGeometry.IsProjective g ∧
      Smooth (g.fiberToSpecResidueField
        (⟨⊥, inferInstance⟩ : PrimeSpectrum (PowerSeries k))) ∧
      ∃ e : X ≅ pullback g
          (Spec.map (CommRingCat.ofHom (PowerSeries.constantCoeff (R := k)))),
        e.hom ≫ pullback.snd g
            (Spec.map (CommRingCat.ofHom (PowerSeries.constantCoeff (R := k)))) = f
```

## Tag 0E7Z, a lemma

[Tag 0E7Z](https://stacks.math.columbia.edu/tag/0E7Z) in the Stacks Project.

**`Deformation.Examples.Smoothing.exists_flat_separated_finiteType_smoothing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SmoothingSeparated.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/SmoothingSeparated.lean#L149).

> **[Stacks, Tag 0E7Z].** Let `k` be a field and let `X` be a scheme over `k`. Assume
> (1) `X` is separated, finite type over `k` and `dim(X) ≤ 1`, (2) `X` is a local complete
> intersection over `k`, and (3) `X → Spec(k)` is smooth except at finitely many points. Then there
> exists a flat, separated, finite type morphism `Y → Spec(k[[t]])` whose generic fibre is smooth and
> whose special fibre is isomorphic to `X`.
>
> Finite type is `LocallyOfFiniteType` together with `QuasiCompact`. The generic fibre is the fibre
> over the zero ideal of `k⟦t⟧`, smooth over its residue field. The special fibre is the base change
> along `Spec k ⟶ Spec k⟦t⟧` given by the constant coefficient, and the isomorphism with `X` is one
> of schemes over `Spec k`.

```lean
theorem exists_flat_separated_finiteType_smoothing {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [IsSeparated f] [LocallyOfFiniteType f] [QuasiCompact f]
    (hdim : topologicalKrullDim X ≤ 1) (hlci : IsLocalCompleteIntersectionOverField f)
    (hfin : ((f.smoothLocus : Set X)ᶜ).Finite) :
    ∃ (Y : Scheme.{u}) (g : Y ⟶ Spec (.of (PowerSeries k))),
      Flat g ∧ IsSeparated g ∧ LocallyOfFiniteType g ∧ QuasiCompact g ∧
        Smooth (g.fiberToSpecResidueField
          (⟨⊥, Ideal.isPrime_bot⟩ : PrimeSpectrum (PowerSeries k))) ∧
        ∃ e : X ≅
            pullback g (Spec.map (CommRingCat.ofHom (PowerSeries.constantCoeff (R := k)))),
          e.hom ≫ pullback.snd g
              (Spec.map (CommRingCat.ofHom (PowerSeries.constantCoeff (R := k)))) = f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 93.17, Tag 0E7S](https://stacks.math.columbia.edu/tag/0E7S)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
