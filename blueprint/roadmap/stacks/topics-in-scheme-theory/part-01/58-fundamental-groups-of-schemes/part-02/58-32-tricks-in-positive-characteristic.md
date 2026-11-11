---
declaration: section
origin: cited
lean: Stacks.Etale.exists_etalePresentation_nonfiniteGeneratorNumber_lt, AlgebraicGeometry.exists_finiteEtale_to_affineSpace, AlgebraicGeometry.exists_finiteEtale_openClosed_pullback, AlgebraicGeometry.injective_etaleFundamentalGroupMap_of_isClosedImmersion
statement: formalized
proof: formalized
---

# 58.32 Tricks in positive characteristic

Section 58.32 of the Stacks Project, [Tag 0G1E](https://stacks.math.columbia.edu/tag/0G1E). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0G1F, a lemma

[Tag 0G1F](https://stacks.math.columbia.edu/tag/0G1F) in the Stacks Project.

**`Stacks.Etale.exists_etalePresentation_nonfiniteGeneratorNumber_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/NonfiniteGenerators.lean, line 421](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/NonfiniteGenerators.lean#L421).

> In positive characteristic, an étale presentation of a finite étale algebra whose
> nonfinite-generator invariant is positive can be replaced by a compatible étale presentation
> with strictly smaller invariant.

```lean
theorem exists_etalePresentation_nonfiniteGeneratorNumber_lt
    (k : Type u) [Field k] (p : ℕ) [CharP k p] (hp : 0 < p)
    (n : ℕ) (I : Ideal (MvPolynomial (Fin n) k))
    (B : Type w) [CommRing B]
    [Algebra ((MvPolynomial (Fin n) k) ⧸ I) B]
    [Algebra k B] [IsScalarTower k ((MvPolynomial (Fin n) k) ⧸ I) B]
    [Module.Finite ((MvPolynomial (Fin n) k) ⧸ I) B]
    [Algebra.Etale ((MvPolynomial (Fin n) k) ⧸ I) B]
    (C : Type v) [CommRing C] [Algebra k C]
    (φ : MvPolynomial (Fin n) k →ₐ[k] C) (hφ : φ.toRingHom.Etale)
    (τ : (C ⧸ Ideal.map φ.toRingHom I) →ₐ[k] B) (hτ : Function.Surjective τ)
    (hcomm : ∀ f : MvPolynomial (Fin n) k,
      τ (Ideal.Quotient.mk (Ideal.map φ.toRingHom I) (φ f)) =
        algebraMap ((MvPolynomial (Fin n) k) ⧸ I) B (Ideal.Quotient.mk I f))
    (hpos : 0 < nonfiniteGeneratorNumber φ.toRingHom) :
    ∃ (φ' : MvPolynomial (Fin n) k →ₐ[k] C),
      φ'.toRingHom.Etale ∧
      ∃ τ' : (C ⧸ Ideal.map φ'.toRingHom I) →ₐ[k] B,
        Function.Surjective τ' ∧
        (∀ f : MvPolynomial (Fin n) k,
          τ' (Ideal.Quotient.mk (Ideal.map φ'.toRingHom I) (φ' f)) =
            algebraMap ((MvPolynomial (Fin n) k) ⧸ I) B (Ideal.Quotient.mk I f)) ∧
        nonfiniteGeneratorNumber φ'.toRingHom < nonfiniteGeneratorNumber φ.toRingHom
```

## Tag 0G1G, a lemma

[Tag 0G1G](https://stacks.math.columbia.edu/tag/0G1G) in the Stacks Project.

**`AlgebraicGeometry.exists_finiteEtale_to_affineSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FiniteEtaleOverAffineSpace.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FiniteEtaleOverAffineSpace.lean#L82).

> An affine scheme étale over affine space in positive characteristic admits a
> (possibly different) finite étale morphism to the same affine space.

```lean
theorem exists_finiteEtale_to_affineSpace
    (k : Type u) [Field k] (p : ℕ) [CharP k p] (hp : 0 < p) (n : ℕ)
    {X : Scheme.{u}} [IsAffine X]
    (f : X ⟶ AffineSpace (ULift.{u} (Fin n)) (Spec (.of k))) [Etale f] :
    ∃ g : X ⟶ AffineSpace (ULift.{u} (Fin n)) (Spec (.of k)),
      IsFinite g ∧ Etale g
```

## Tag 0G1H, a lemma

[Tag 0G1H](https://stacks.math.columbia.edu/tag/0G1H) in the Stacks Project.

**`AlgebraicGeometry.exists_finiteEtale_openClosed_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FiniteEtaleOverClosedSubschemeOfAffineSpace.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FiniteEtaleOverClosedSubschemeOfAffineSpace.lean#L166).

> **Stacks Project, Tag 0G1H.** In positive characteristic, a finite étale cover of a closed
> subscheme of affine space is an open-and-closed part of the restriction of a finite étale cover
> of affine space.

```lean
theorem exists_finiteEtale_openClosed_pullback
    (k : Type u) [Field k] (p : ℕ) [CharP k p] (hp : 0 < p) (n : ℕ)
    {Z : Scheme.{u}}
    (i : Z ⟶ Spec (.of (MvPolynomial (Fin n) k))) [IsClosedImmersion i]
    {Y : Scheme.{u}} (g : Y ⟶ Z) [IsFinite g] [Etale g] :
    ∃ (U : Scheme.{u}) (f : U ⟶ Spec (.of (MvPolynomial (Fin n) k)))
      (_ : IsFinite f) (_ : Etale f)
      (j : Y ⟶ pullback f i),
      IsOpenImmersion j ∧ IsClosedImmersion j ∧
        j ≫ pullback.snd f i = g
```

## Tag 0G1I, a proposition

[Tag 0G1I](https://stacks.math.columbia.edu/tag/0G1I) in the Stacks Project.

**`AlgebraicGeometry.injective_etaleFundamentalGroupMap_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/ClosedImmersionPositiveCharacteristic.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/ClosedImmersionPositiveCharacteristic.lean#L294).

> **Stacks Project, Tag 0G1I.** A closed immersion of connected affine schemes over `𝐅_p`
> induces an injection on étale fundamental groups. Being a scheme over `𝐅_p` is spelled as
> `p` being zero in the ring of global sections of the ambient scheme.

```lean
theorem injective_etaleFundamentalGroupMap_of_isClosedImmersion (p : ℕ) (hp : p.Prime)
    {Z X : Scheme.{u}} [ConnectedSpace Z] [ConnectedSpace X] [IsAffine Z] [IsAffine X]
    (i : Z ⟶ X) [IsClosedImmersion i] (hX : (p : Γ(X, ⊤)) = 0) (z : GeometricPoint Z) :
    Function.Injective (etaleFundamentalGroupMap i z)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 58.32, Tag 0G1E](https://stacks.math.columbia.edu/tag/0G1E)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
