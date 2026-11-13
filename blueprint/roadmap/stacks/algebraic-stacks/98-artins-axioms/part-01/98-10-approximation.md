---
declaration: section
origin: cited
lean: Deformation.Artin.Approximation.exists_finiteType_approximation, AdicCompletion.exists_surjective_adicCompletionMap
statement: formalized
proof: formalized
---

# 98.10 Approximation

Section 98.10 of the Stacks Project, [Tag 07XA](https://stacks.math.columbia.edu/tag/07XA). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07XB, a lemma

[Tag 07XB](https://stacks.math.columbia.edu/tag/07XB) in the Stacks Project.

**`Deformation.Artin.Approximation.exists_finiteType_approximation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Approximation/FiniteType.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Approximation/FiniteType.lean#L84). The attribute's comment: “clauses (1)-(6): the finite type algebra, its maximal ideal, the object, the isomorphism of Nth neighbourhoods, the compatible isomorphism of the restricted objects, and the isomorphism of graded k-algebras. Stacks 07QZ, the source's one external input here, is proved: `Stacks.Smoothing.exists_localEtaleSolution_of_isGRing`”.

> **Stacks Project, Tag 07XB.** Approximation of a fibred object over a Noetherian
> complete local ring by an object over a finite type `S`-algebra.
>
> Let `S` be a locally Noetherian scheme, let `𝒳` be a category fibred in groupoids over the
> big fppf site of `S`, and let `x` be an object of `𝒳` over `Spec R` for `R` a Noetherian
> complete local ring whose residue field is of finite type over `S`. Let `s ∈ S` be the image
> of `Spec k`. If `O_{S, s}` is a G-ring and the structure morphism of `𝒳` is limit preserving
> on objects, then for every `N ≥ 1` there are a finite type `S`-algebra `A`, a maximal ideal
> `m_A ⊆ A`, an object `x_A` of `𝒳` over `Spec A`, an `S`-isomorphism `R/m_R^N ≅ A/m_A^N`, an
> isomorphism of the restrictions of `x` and `x_A` to those truncations compatible with it,
> and an isomorphism of graded `k`-algebras `Gr_{m_R}(R) ≅ Gr_{m_A}(A)`.
>
> These are clauses (1)-(6) of the tag. Clause (6) is the final existential: a ring
> isomorphism of the associated graded rings which carries each homogeneous summand to the
> summand of the same degree and which, in degree zero, agrees with the truncation
> isomorphism `φ` of clause (4).
>
> Artin approximation over a G-ring (Stacks 07QZ) is used in the proof and is discharged by
> `Stacks.Smoothing.exists_localEtaleSolution_of_isGRing`, so the statement below carries no
> hypothesis beyond the source's own.

```lean
public theorem exists_finiteType_approximation
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    [IsLocallyNoetherian S]
    (𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (Site B S hS))
    (R : Type u) [CommRing R] [IsLocalRing R] [IsNoetherianRing R]
    [IsAdicComplete (maximalIdeal R) R]
    (hR : B.Contains (Spec (.of R)))
    (fR : Spec (.of R) ⟶ S)
    (hfinite : LocallyOfFiniteType
      (Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk (maximalIdeal R))) ≫ fR))
    (hquasi : QuasiCompact
      (Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk (maximalIdeal R))) ≫ fR))
    (s : S)
    (hs : fR (closedPoint R) = s)
    (hG : IsGRing (S.presheaf.stalk s))
    (hp : AlgebraicGeometry.BigFppfOver.IsLimitPreservingOnObjects.{u, u, u, u, u + 1} B S hS 𝒳
      (baseFiberedCategory B S hS) (structureMorphism B S hS 𝒳))
    (x : 𝒳.val.p.Fiber (siteObject B S hS hR fR))
    (N : ℕ) (hN : 1 ≤ N) :
    ∃ (A : Type u) (_ : CommRing A) (mA : Ideal A) (_ : mA.IsMaximal)
      (fA : Spec (.of A) ⟶ S)
      (hA : B.Contains (Spec (.of A)))
      (hRN : B.Contains (Spec (.of (R ⧸ maximalIdeal R ^ N))))
      (hAN : B.Contains (Spec (.of (A ⧸ mA ^ N))))
      (xA : 𝒳.val.p.Fiber (siteObject B S hS hA fA)),
      LocallyOfFiniteType fA ∧ QuasiCompact fA ∧
      ∃ (φ : (R ⧸ maximalIdeal R ^ N) ≃+* (A ⧸ mA ^ N)),
        Spec.map (CommRingCat.ofHom φ.symm.toRingHom) ≫
            Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk (mA ^ N))) ≫ fA =
          Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk ((maximalIdeal R) ^ N))) ≫ fR ∧
        ∃ (iR : siteObject B S hS hRN
              (Spec.map (CommRingCat.ofHom
                (Ideal.Quotient.mk ((maximalIdeal R) ^ N))) ≫ fR) ⟶
              siteObject B S hS hR fR)
          (iA : siteObject B S hS hAN
              (Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk (mA ^ N))) ≫ fA) ⟶
              siteObject B S hS hA fA)
          (eBase : siteObject B S hS hRN
              (Spec.map (CommRingCat.ofHom
                (Ideal.Quotient.mk ((maximalIdeal R) ^ N))) ≫ fR) ⟶
              siteObject B S hS hAN
                (Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk (mA ^ N))) ≫ fA))
          (xRN : 𝒳.val.p.Fiber (siteObject B S hS hRN
              (Spec.map (CommRingCat.ofHom
                (Ideal.Quotient.mk ((maximalIdeal R) ^ N))) ≫ fR)))
          (xAN : 𝒳.val.p.Fiber (siteObject B S hS hAN
              (Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk (mA ^ N))) ≫ fA)))
          (r : xRN.1 ⟶ x.1) (a : xAN.1 ⟶ xA.1)
          (e : xRN.1 ⟶ xAN.1),
          (AlgebraicGeometry.BigFppfOver.toScheme B S hS).map iR =
              Spec.map (CommRingCat.ofHom
                (Ideal.Quotient.mk ((maximalIdeal R) ^ N))) ∧
          (AlgebraicGeometry.BigFppfOver.toScheme B S hS).map iA =
              Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk (mA ^ N))) ∧
          (AlgebraicGeometry.BigFppfOver.toScheme B S hS).map eBase =
              Spec.map (CommRingCat.ofHom φ.symm.toRingHom) ∧
          𝒳.val.p.IsStronglyCartesian iR r ∧
          𝒳.val.p.IsStronglyCartesian iA a ∧
          𝒳.val.p.IsHomLift eBase e ∧ IsIso e ∧
          ∃ (gr : AssociatedGraded.gradedRing (maximalIdeal R) ≃+*
              AssociatedGraded.gradedRing mA),
            (∀ n (z : AssociatedGraded.piece (M := R) (maximalIdeal R) n),
              ∃ w : AssociatedGraded.piece (M := A) mA n,
                gr (DirectSum.of _ n z) = DirectSum.of _ n w) ∧
            ∀ (r₀ : R) (a₀ : A),
              φ (Ideal.Quotient.mk ((maximalIdeal R) ^ N) r₀) =
                  Ideal.Quotient.mk (mA ^ N) a₀ →
              gr (DirectSum.of _ 0
                    (AssociatedGraded.mk (maximalIdeal R) 0
                      (⟨r₀, by simp⟩ :
                        AssociatedGraded.power (M := R) (maximalIdeal R) 0))) =
                DirectSum.of _ 0
                  (AssociatedGraded.mk mA 0
                    (⟨a₀, by simp⟩ : AssociatedGraded.power (M := A) mA 0))
```

## Tag 07XC, an equation

[Tag 07XC](https://stacks.math.columbia.edu/tag/07XC) in the Stacks Project.

**`AdicCompletion.exists_surjective_adicCompletionMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/PolynomialSurjection.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/PolynomialSurjection.lean#L68).

> **Stacks Project, Tag 07XC.** A map from a polynomial ring to a Noetherian
> complete local ring which is surjective modulo the square of the maximal ideal
> extends to a surjective local map from the completion of its localization at
> the residue-field kernel.

```lean
theorem exists_surjective_adicCompletionMap
    (Λ R : Type*) [CommRing Λ] [CommRing R] [Algebra Λ R]
    [IsNoetherianRing Λ] [IsNoetherianRing R] [IsLocalRing R]
    [IsAdicComplete (maximalIdeal R) R]
    (s : ℕ) (p : Ideal (MvPolynomial (Fin s) Λ)) [p.IsMaximal]
    (f : MvPolynomial (Fin s) Λ →ₐ[Λ] R)
    (hp : Ideal.comap f.toRingHom (maximalIdeal R) = p)
    (hmod : Function.Surjective
      ((Ideal.Quotient.mk ((maximalIdeal R) ^ 2)).comp f.toRingHom)) :
    let A := Localization.AtPrime p
    let P := AdicCompletion (maximalIdeal A) A
    IsNoetherianRing P ∧ IsLocalRing P ∧
      IsAdicComplete (maximalIdeal P) P ∧
      ∃ g : A →+* R,
        g.comp (algebraMap (MvPolynomial (Fin s) Λ) A) = f.toRingHom ∧
        IsLocalHom g ∧
        ∃ φ : P →+* R,
          φ.comp (algebraMap A P) = g ∧
            Function.Surjective φ ∧ IsLocalHom φ ∧
              ∀ ψ : P →+* R,
                ψ.comp (algebraMap A P) = g → IsLocalHom ψ → ψ = φ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 98.10, Tag 07XA](https://stacks.math.columbia.edu/tag/07XA)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
