---
declaration: section
origin: cited
lean: Stacks.Smoothing.NeronSituation, Stacks.Smoothing.neron_affineBlowup_localization, Stacks.Smoothing.blowup_quotient_by_surjection, Stacks.Smoothing.affineBlowup_smoothAt, Stacks.Smoothing.affineBlowup_differentials_shortExact, Stacks.Smoothing.smoothAt_of_conormal_cokernel_free, Stacks.Smoothing.exists_finite_affineNeronBlowup_smoothAt, Stacks.Smoothing.ind_underSmooth_of_ramificationIdx_one
statement: formalized
proof: formalized
---

# 16.4 Intermezzo: Néron desingularization

Section 16.4 of the Stacks Project, [Tag 0BJ1](https://stacks.math.columbia.edu/tag/0BJ1). 6 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BJ2, a situation

[Tag 0BJ2](https://stacks.math.columbia.edu/tag/0BJ2) in the Stacks Project.

**`Stacks.Smoothing.NeronSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/NeronDesingularization.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smoothing/NeronDesingularization.lean#L76).

> The standing data and hypotheses of Stacks 0BJ2: an extension `R → Λ` of discrete
> valuation rings of ramification index one, factored as `R → A → Λ` with `A` flat and of finite
> type over `R`.

```lean
structure NeronSituation
```

## Tag 0BJ3, a lemma

[Tag 0BJ3](https://stacks.math.columbia.edu/tag/0BJ3) in the Stacks Project.

**`Stacks.Smoothing.neron_affineBlowup_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/NeronDesingularization.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smoothing/NeronDesingularization.lean#L181). The attribute's comment: “neron\_localization”.

> **Stacks 0BJ3.** The affine blowup at `𝔭` commutes with localizing away from an element
> outside `𝔭`: if `A' = A[𝔭/π]`, then the affine blowup of `A_a` is `A'_a`.

```lean
theorem neron_affineBlowup_localization
    (S : NeronSituation) (π : S.R)
    (_hπ : Irreducible π)
    (a : S.A)
    (_ha : a ∉ S.maximalIdealPreimage)
    (hπA : algebraMap S.R S.A π ∈ S.maximalIdealPreimage) :
    let A' : Type _ := affineBlowupAlgebra S.maximalIdealPreimage
      (algebraMap S.R S.A π) (Localization.Away (algebraMap S.R S.A π))
    let Aa := Localization.Away a
    let L := Localization.Away (algebraMap S.A A' a)
    let B : Type _ := affineBlowupAlgebra
      (S.maximalIdealPreimage.map (algebraMap S.A Aa))
      (algebraMap S.A Aa (algebraMap S.R S.A π))
      (Localization.Away (algebraMap S.A Aa (algebraMap S.R S.A π)))
    ∃ e : L ≃+* B,
      (∀ x : S.A, e (algebraMap A' L (algebraMap S.A A' x)) =
        algebraMap Aa B (algebraMap S.A Aa x)) ∧
      (∀ x : Aa, e (Localization.awayMap (algebraMap S.A A') a x) =
        algebraMap Aa B x)
```

**`Stacks.Smoothing.blowup_quotient_by_surjection`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/NeronDesingularization.lean, line 339](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smoothing/NeronDesingularization.lean#L339). The attribute's comment: “neron\_surjection”.

> **Stacks 0BJ3.** A surjection `B → A` of flat finite-type `R`-algebras presents the blowup
> of `A` at `𝔭`: it is the blowup of `B` at the preimage of `𝔭`, modulo the extended kernel and
> then modulo the `π`-power torsion.

```lean
lemma blowup_quotient_by_surjection (S : NeronSituation) (π : S.R)
    (hπ : Ideal.span ({π} : Set S.R) = IsLocalRing.maximalIdeal S.R)
    (B : Type*) [CommRing B] [Algebra S.R B] [Module.Flat S.R B]
    [Algebra.FiniteType S.R B]
    (f : B →ₐ[S.R] S.A) (hf : Function.Surjective f) :
    Nonempty <|
      let pB : Ideal B := Ideal.comap f.toRingHom S.maximalIdealPreimage
      let B' := affineBlowupAlgebra pB (algebraMap S.R B π)
        (Localization.Away (algebraMap S.R B π))
      let I : Ideal B := RingHom.ker f.toRingHom
      let IB' : Ideal B' := Ideal.map (algebraMap B B') I
      let T := B' ⧸ IB'
      let A' := affineBlowupAlgebra S.maximalIdealPreimage
        (algebraMap S.R S.A π) (Localization.Away (algebraMap S.R S.A π))
      (T ⧸ torsionIdeal T (algebraMap S.R T π)) ≃ₐ[S.R] A'
```

## Tag 0BJ4, a lemma

[Tag 0BJ4](https://stacks.math.columbia.edu/tag/0BJ4) in the Stacks Project.

**`Stacks.Smoothing.affineBlowup_smoothAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/NeronBlowupSmooth.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smoothing/NeronBlowupSmooth.lean#L373). The attribute's comment: “blowup\_smooth”.

> **Stacks 0BJ4, smoothness.** In a Néron situation with uniformizer `π`, if `A` is smooth over
> `R` at `𝔭` and the residue-field extension `κ(R) → κ(Λ)` is separable, then the affine blowup
> `A' = A[𝔭/π]` is smooth over `R` at the prime `𝔭'` induced by the canonical map `A' → Λ`.

```lean
theorem affineBlowup_smoothAt
    (S : NeronSituation) (π : S.R)
    (hπ : IsLocalRing.maximalIdeal S.R = Ideal.span ({π} : Set S.R))
    (hsep : @Algebra.IsSeparableExtension
      (IsLocalRing.maximalIdeal S.R).ResidueField
      (IsLocalRing.maximalIdeal S.Λ).ResidueField _ _ S.residueFieldExtension)
    (hS : Algebra.SmoothAt S.R S.A S.maximalIdealPreimage) :
    Algebra.SmoothAt S.R
      (affineBlowupAlgebra S.maximalIdealPreimage (algebraMap S.R S.A π)
        (Localization.Away (algebraMap S.R S.A π)))
      (Ideal.comap (canonicalNeronBlowupMap S π hπ).1
        (IsLocalRing.maximalIdeal S.Λ))
```

**`Stacks.Smoothing.affineBlowup_differentials_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/NeronBlowupSmooth.lean, line 788](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smoothing/NeronBlowupSmooth.lean#L788). The attribute's comment: “differentials\_sequence”.

> **Stacks 0BJ4, the differential sequence.** In a Néron situation with uniformizer `π`, if `A`
> is smooth over `R` at `𝔭` and the residue-field extension `κ(R) → κ(Λ)` is separable, then for
> `c = dim (A/πA)_𝔭` the relative differentials of the affine blowup `A'` at its prime `𝔭'` sit in a
> short exact sequence
> `0 → Ω_{A/R} ⊗_A A'_{𝔭'} → Ω_{A'/R} ⊗_{A'} A'_{𝔭'} → ((A'/πA')_{𝔭'})^c → 0`,
> whose first map is the base change of `Ω_{A/R} → Ω_{A'/R}`.

```lean
theorem affineBlowup_differentials_shortExact
    (S : NeronSituation) (π : S.R)
    (hπ : IsLocalRing.maximalIdeal S.R = Ideal.span ({π} : Set S.R))
    (hsep : @Algebra.IsSeparableExtension
      (IsLocalRing.maximalIdeal S.R).ResidueField
      (IsLocalRing.maximalIdeal S.Λ).ResidueField _ _ S.residueFieldExtension)
    (hsm : Algebra.SmoothAt S.R S.A S.maximalIdealPreimage)
    (c : ℕ)
    (hc : ringKrullDim
      ((Localization.AtPrime S.maximalIdealPreimage) ⧸
        Ideal.span ({algebraMap S.R (Localization.AtPrime S.maximalIdealPreimage) π} :
          Set (Localization.AtPrime S.maximalIdealPreimage))) = c) :
    let A' := affineBlowupAlgebra S.maximalIdealPreimage (algebraMap S.R S.A π)
      (Localization.Away (algebraMap S.R S.A π))
    ∀ (p' : Ideal A') [p'.IsPrime],
      p' = Ideal.comap (canonicalNeronBlowupMap S π hπ).1 (IsLocalRing.maximalIdeal S.Λ) →
      ∀ (B : Type w) [CommRing B] [Algebra A' B] [IsLocalization.AtPrime B p']
        [Algebra S.A B] [IsScalarTower S.A A' B],
        let Q := B ⧸ Ideal.span ({algebraMap A' B (algebraMap S.R A' π)} : Set B)
        ∃ (f : B ⊗[S.A] Ω[S.A⁄S.R] →ₗ[B] B ⊗[A'] Ω[A'⁄S.R])
          (_ : ∀ (x : B) (y : Ω[S.A⁄S.R]),
            f (x ⊗ₜ[S.A] y) = x ⊗ₜ[A'] KaehlerDifferential.map S.R S.R S.A A' y)
          (g : B ⊗[A'] Ω[A'⁄S.R] →ₗ[B] (Fin c → Q))
          (hzero : ModuleCat.ofHom f ≫ ModuleCat.ofHom g = 0),
          (ShortComplex.mk (ModuleCat.ofHom f) (ModuleCat.ofHom g) hzero).ShortExact
```

## Tag 0BJ5, a lemma

[Tag 0BJ5](https://stacks.math.columbia.edu/tag/0BJ5) in the Stacks Project.

**`Stacks.Smoothing.smoothAt_of_conormal_cokernel_free`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/NeronSmoothnessCriterion.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smoothing/NeronSmoothnessCriterion.lean#L276).

> **Stacks 0BJ5.** In a Néron situation, suppose `A` is smooth over `R` at the generic point
> `𝔮 = Ker(A → Λ)`, suppose `A` is a quotient of an `R`-algebra `B` which is smooth over `R` at the
> preimage of `𝔭`, and suppose the cokernel of the conormal map `I/I² ⊗_A Λ → Ω_{B/R} ⊗_B Λ` is a
> free `Λ`-module. Then `A` is smooth over `R` at `𝔭` too.

```lean
theorem smoothAt_of_conormal_cokernel_free
    (S : NeronSituation)
    (B : Type*) [CommRing B] [Algebra S.R B] [Algebra B S.A]
    [IsScalarTower S.R B S.A]
    (hsurj : Function.Surjective (algebraMap B S.A))
    (hA : Algebra.SmoothAt S.R S.A S.kernelIdeal)
    (_hB : Algebra.SmoothAt S.R B (Ideal.comap (algebraMap B S.A) S.maximalIdealPreimage))
    (hfree : let _ := ConormalSeq.cotangentModule hsurj
      Module.Free S.Λ
        ((S.Λ ⊗[S.A] (S.A ⊗[B] Ω[B⁄S.R])) ⧸
          LinearMap.range
            (LinearMap.baseChange S.Λ (ConormalSeq.conormalMap S.R hsurj)))) :
    Algebra.SmoothAt S.R S.A S.maximalIdealPreimage
```

## Tag 0BJ6, a lemma

[Tag 0BJ6](https://stacks.math.columbia.edu/tag/0BJ6) in the Stacks Project.

**`Stacks.Smoothing.exists_finite_affineNeronBlowup_smoothAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/NeronBlowupSequence/Desingularization.lean, line 741](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smoothing/NeronBlowupSequence/Desingularization.lean#L741).

> **Stacks 0BJ6.** In a Néron situation, if `A` is smooth over `R` at the generic prime
> `𝔮 = Ker(A → Λ)` and the residue-field extension `κ(R) → κ(Λ)` is separable, then finitely many
> affine Néron blowups produce a stage that is smooth over `R` at its distinguished prime
> `𝔭 = (· → Λ)^{-1}(𝔪_Λ)`.

```lean
theorem exists_finite_affineNeronBlowup_smoothAt
    (S : NeronSituation.{u, v, w})
    (hsm : Algebra.SmoothAt S.R S.A S.kernelIdeal)
    (hsep : @Algebra.IsSeparableExtension
      (IsLocalRing.maximalIdeal S.R).ResidueField
      (IsLocalRing.maximalIdeal S.Λ).ResidueField _ _ S.residueFieldExtension) :
    ∃ T : NeronStage S,
      Relation.ReflTransGen (IsAffineNeronBlowup S) (NeronStage.initial S) T ∧
        Algebra.SmoothAt S.R T.A T.maximalIdealPreimage
```

## Tag 0BJ7, a lemma

[Tag 0BJ7](https://stacks.math.columbia.edu/tag/0BJ7) in the Stacks Project.

**`Stacks.Smoothing.ind_underSmooth_of_ramificationIdx_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/NeronIndSmooth.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smoothing/NeronIndSmooth.lean#L260). The attribute's comment: “"`Λ` is a filtered colimit of smooth `R`-algebras" is `CategoryTheory.ObjectProperty.ind.{u}` of `UnderSmooth (CommRingCat.of R)` on the category `Under (CommRingCat.of R)` of `R`-algebras, the same spelling as the left-hand side of the library's Lemma 07C3. The residue fields are `Ideal.ResidueField` at the maximal ideals, as in the library's Lemmas 0BJ4-0BJ6, and the fraction fields are abstract, pinned by `IsFractionRing`. See the module docstring.”. References: SGA 7 I (0.5.1), “ind-smooth colimit”; SGA 7 I (0.5), “Lemma 0.5.1”.

> **Stacks 0BJ7 (Néron desingularization for discrete valuation rings).** Let `R ⊂ Λ` be an
> extension of discrete valuation rings which has ramification index `1` and induces a separable
> extension of residue fields and of fraction fields. Then `Λ` is a filtered colimit of smooth
> `R`-algebras.

```lean
theorem ind_underSmooth_of_ramificationIdx_one
    (hinj : Function.Injective (algebraMap R Λ))
    (hram : Stacks.DiscreteValuationRing.Ramification.ramificationIdx R Λ = 1)
    (hres : letI := Ideal.residueFieldAlgebra (IsLocalRing.maximalIdeal R)
                (IsLocalRing.maximalIdeal Λ)
      Algebra.IsSeparableExtension (IsLocalRing.maximalIdeal R).ResidueField
        (IsLocalRing.maximalIdeal Λ).ResidueField)
    [Algebra.IsSeparableExtension K L] :
    ObjectProperty.ind.{u} (UnderSmooth (CommRingCat.of R))
      (Under.mk (CommRingCat.ofHom (algebraMap R Λ)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 16.4, Tag 0BJ1](https://stacks.math.columbia.edu/tag/0BJ1)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
