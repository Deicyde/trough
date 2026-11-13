---
declaration: section
origin: cited
lean: Rig.IsRigEtale, Rig.CompletedNaiveCotangentComplex.exists_annihilator_twoTerm_iff_forall_reducedComplex, Rig.isCohomologyAnnihilated_iff_isReductionCohomologyAnnihilated, Rig.isRigEtale_iff_exists_annihilator_cohomology, Rig.isArtinJacobian_of_isRigEtale, Rig.isArtinPreliminary_of_isArtinJacobian, Rig.isCohomologyAnnihilated_of_isArtinPreliminary, Rig.isRigEtale_iff_isJacobianCramerBounded
statement: formalized
proof: formalized
---

# 88.8 Rig-étale algebras

Section 88.8 of the Stacks Project, [Tag 0ALP](https://stacks.math.columbia.edu/tag/0ALP). 8 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GAY, a definition

[Tag 0GAY](https://stacks.math.columbia.edu/tag/0GAY) in the Stacks Project.

**`Rig.IsRigEtale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/RigSmoothDefs.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/RigSmoothDefs.lean#L73).

> **Stacks Project, Tag 0GAY.** An adically complete algebra of finite type modulo `I` is
> rig-étale over `(A, I)` if some power of `I` acts by zero on its completed naive cotangent
> complex in `D(B)`.  The condition is imposed for each completed polynomial presentation
> of `B`.

```lean
public abbrev IsRigEtale (B : AdicFiniteTypeAlgebra.{u, v} A I) : Prop
```

## Tag 0AJU, a lemma

[Tag 0AJU](https://stacks.math.columbia.edu/tag/0AJU) in the Stacks Project.

**`Rig.CompletedNaiveCotangentComplex.exists_annihilator_twoTerm_iff_forall_reducedComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/NaiveCotangent/Annihilation.lean, line 399](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/NaiveCotangent/Annihilation.lean#L399). The attribute's comment: “(3) iff (4) for the reduced complexes”.

> **Stacks 0AJU, the equivalence of (0AJW) and (0AJX).**  For a completed polynomial
> presentation `B = A⟨x₁, …, x_r⟩ / J` of an object `B` of the category (Stacks 0AL4) over a
> Noetherian ring `A`, the following are equivalent:
>
> * some power of `I` annihilates `H^i(NL^∧_{B/A})` for `i = -1, 0`;
> * some power of `I` annihilates `H^i(NL_{Bₙ/Aₙ})` for `i = -1, 0` and all `n ≥ 1`.
>
> Here `NL_{Bₙ/Aₙ}` is `Rig.CompletedNaiveCotangentComplex.reducedComplex`, the object the
> strict pro-isomorphism of Stacks 0AJS (1) produces: the quotient of `NL^∧_{B/A}` by the image
> of `J ∩ Iⁿ A⟨x⟩` in degree `-1` and by `IⁿB · (⨁ B dxᵢ)` in degree `0`.  The forward
> implication doubles the exponent and the backward one preserves it; see
> `annihilatesCohomology_reducedComplex` and `annihilatesCohomology_twoTerm`.  Annihilation by
> the ideal `IᶜB` is the source's elementwise condition by
> `annihilatesCohomology_adicIdeal_pow_iff`, and the left-hand side is condition (3) on the
> nose: `H⁻¹` is `LinearMap.ker K.differential` and `H⁰` is
> `(Fin r → B) ⧸ LinearMap.range K.differential`.
>
> The sublabel records that `NL_{Bₙ/Aₙ}` is taken in the shape Stacks 0AJS (1) produces; see
> the implementation notes for the identifications that would be needed to read condition (4)
> through `Algebra.naiveCotangentComplex Aₙ Bₙ` instead.

```lean
public theorem exists_annihilator_twoTerm_iff_forall_reducedComplex [IsNoetherianRing A]
    (K : CompletedNaiveCotangentComplex P) :
    (∃ c : ℕ, NaiveCotangent.AnnihilatesCohomology (B.adicIdeal ^ c) K.twoTerm) ↔
      ∃ c : ℕ, ∀ n ≥ 1, NaiveCotangent.AnnihilatesCohomology (B.adicIdeal ^ c)
        (K.reducedComplex n)
```

**`Rig.isCohomologyAnnihilated_iff_isReductionCohomologyAnnihilated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/NaiveCotangent/ReductionIdentification.lean, line 418](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/NaiveCotangent/ReductionIdentification.lean#L418). The attribute's comment: “(3) iff (4)”.

> **Stacks 0AJU, the equivalence of conditions (3) and (4).**  For a completed polynomial
> presentation `B = A⟨x₁, …, x_r⟩ / J` of an object `B` of the category (Stacks 0AL4) over a
> Noetherian ring `A`, the following are equivalent:
>
> * (3) some power `I^c` of `I` annihilates `H^{-1}` and `H^0` of `NL^∧_{B/A}`, that is, the
>   kernel and the cokernel of the differential of `Rig.completedNaiveCotangentComplex B P`;
> * (4) some power `I^c` of `I` annihilates, for every `n ≥ 1`, the degree-`1` and degree-`0`
>   homology of `Algebra.naiveCotangentComplex Aₙ Bₙ`, where `Aₙ = A / Iⁿ` and `Bₙ = B / IⁿB`.
>
> Condition (4) is the source's, and is *presentation-free*: `NL_{Bₙ/Aₙ}` is the naive cotangent
> complex of the tautological presentation `Aₙ[Bₙ] → Bₙ` and its cohomology is the categorical
> homology of a `HomologicalComplex.double`.  Three identifications turn it into a statement
> about the presentation `Bₙ = Aₙ[x₁, …, x_r] / Jₙ` of Stacks 0AJS, through which the source's
> argument runs: the homology of a `double` is the kernel and the cokernel of its differential;
> those are independent of the presentation; and `reducedComplex n`, the quotient of
> `NL^∧_{B/A}` by the image of `J ∩ Iⁿ A⟨x⟩` and by `IⁿB · (⨁ B dxᵢ)`, *is*
> `NL(Bₙ = Aₙ[x] / Jₙ)`.  The transport of the annihilation statement across those is then
> `Rig.CompletedNaiveCotangentComplex.exists_annihilator_twoTerm_iff_forall_reducedComplex`,
> whose forward direction doubles the exponent and whose backward direction spends the shift of
> Stacks 0AJS (1) and preserves it.

```lean
public theorem isCohomologyAnnihilated_iff_isReductionCohomologyAnnihilated
    {A : Type u} [CommRing A] [IsNoetherianRing A] {I : Ideal A}
    (B : AdicFiniteTypeAlgebra.{u, v} A I) (P : CompletedPolynomialPresentation I B) :
    (∃ c : ℕ,
        (I ^ c).map (algebraMap A B.carrier) ≤
          Module.annihilator B.carrier
            (LinearMap.ker (completedNaiveCotangentComplex B P).differential) ∧
        (I ^ c).map (algebraMap A B.carrier) ≤
          Module.annihilator B.carrier
            ((Fin P.variableCount → B.carrier) ⧸
              LinearMap.range (completedNaiveCotangentComplex B P).differential)) ↔
      ∃ c : ℕ, ∀ n : ℕ, 1 ≤ n →
        ∀ a : A, a ∈ I ^ c →
          ((Ideal.Quotient.mk ((I ^ n).map (algebraMap A B.carrier))
                (algebraMap A B.carrier a)) ∈
              Module.annihilator (B.carrier ⧸ (I ^ n).map (algebraMap A B.carrier))
                ((Algebra.naiveCotangentComplex (A ⧸ I ^ n)
                  (B.carrier ⧸ (I ^ n).map (algebraMap A B.carrier))).homology 1) ∧
            (Ideal.Quotient.mk ((I ^ n).map (algebraMap A B.carrier))
                (algebraMap A B.carrier a)) ∈
              Module.annihilator (B.carrier ⧸ (I ^ n).map (algebraMap A B.carrier))
                ((Algebra.naiveCotangentComplex (A ⧸ I ^ n)
                  (B.carrier ⧸ (I ^ n).map (algebraMap A B.carrier))).homology 0))
```

**`Rig.isRigEtale_iff_exists_annihilator_cohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/RigEtaleCriterion.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/RigEtaleCriterion.lean#L191). The attribute's comment: “(1) iff (3)”.

> **Stacks 0AJU, (1) ⇔ (3).**  For an `I`-adically complete `A`-algebra `B` of finite type
> modulo `I` over a Noetherian ring `A`, and any completed polynomial presentation
> `B = A⟨x₁, …, x_r⟩ / J`, rig-étaleness of `B` over `(A, I)` is equivalent to the existence of a
> `c` with `IᶜB` annihilating both cohomology modules `H⁻¹(NL^∧_{B/A}) = ker d` and
> `H⁰(NL^∧_{B/A}) = coker d`.
>
> Condition (1) is annihilation of the complex *in the derived category* and condition (3) is
> annihilation of its cohomology, which is weaker for a general complex; the two agree here
> because `NL^∧_{B/A}` has two terms and its degree-`0` term is free, so the annihilating scalar
> is realised by an honest two-sided splitting of the differential.  Passing from (3) to (1) costs
> a squaring of the ideal and passing back costs nothing, which is why the statement is an
> equivalence of the *existence* of an exponent rather than of a fixed one.

```lean
public theorem isRigEtale_iff_exists_annihilator_cohomology
    (B : AdicFiniteTypeAlgebra.{u, v} A I) (P : CompletedPolynomialPresentation I B) :
    IsRigEtale B ↔
      ∃ c : ℕ,
        (I ^ c).map (algebraMap A B.carrier) ≤
          Module.annihilator B.carrier
            (LinearMap.ker (completedNaiveCotangentComplex B P).differential) ∧
        (I ^ c).map (algebraMap A B.carrier) ≤
          Module.annihilator B.carrier
            ((Fin P.variableCount → B.carrier) ⧸
              LinearMap.range (completedNaiveCotangentComplex B P).differential)
```

**`Rig.isArtinJacobian_of_isRigEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/RigEtaleLifting.lean, line 309](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/RigEtaleLifting.lean#L309). The attribute's comment: “(1) implies (6)”.

> **Stacks 0AJU, (1) implies (6).**  A rig-étale adic algebra satisfies the elementwise
> Jacobian criterion: for every `a ∈ I` there are an exponent `c` and elements
> `f₁, …, f_r` of the kernel `J` of a completed polynomial presentation such that the Jacobian
> determinant `det(∂fⱼ/∂xᵢ)` divides `a ^ c` in `B` and `a ^ c · J ⊆ (f₁, …, f_r) + J²`.
>
> The proof is the one in the source.  Rig-étaleness gives an exponent `c₀` with
> `a ^ c₀ · 𝟙 NL^∧_{B/A} = 0` in `D(B)`, hence by Stacks 0ALN(1) a two-sided retraction
> `H : ⨁ i, B dxᵢ → J / J²` of the differential up to `a ^ c₀`
> (`Rig.exists_linearMap_twoSided_of_smul_id_eq_zero`).  Taking `fᵢ ∈ J` representing `H(dxᵢ)`,
> the identity `d ∘ H = a ^ c₀` says that the Jacobian matrix `(∂fⱼ/∂xᵢ)` is exactly
> `a ^ c₀` times the identity, so its determinant is `a ^ (c₀ r)`; and `H ∘ d = a ^ c₀` is the
> conormal Cramer relation.  The exponent is taken to be `c₀ (r + 1)`, which dominates both
> `c₀ r` and `c₀`, the latter being needed when `r = 0`.

```lean
public theorem isArtinJacobian_of_isRigEtale (B : AdicFiniteTypeAlgebra.{u, v} A I)
    (P : CompletedPolynomialPresentation I B) (hB : IsRigEtale B) :
    ∀ a : A, a ∈ I →
      ∃ (c : ℕ) (f : Fin P.variableCount → P.ker),
        Matrix.det (fun i j : Fin P.variableCount =>
          P.toAlgHom ((completedNaiveCotangentComplex B P).partialDeriv i
            (f j : P.completedPolynomialRing))) ∣ (algebraMap A B.carrier a) ^ c ∧
        ∀ g : P.ker,
          algebraMap A P.completedPolynomialRing (a ^ c) * (g : P.completedPolynomialRing) ∈
            Ideal.span (Set.range fun i => (f i : P.completedPolynomialRing)) + P.ker ^ 2
```

**`Rig.isArtinPreliminary_of_isArtinJacobian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/RigEtaleTFAE.lean, line 245](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/RigEtaleTFAE.lean#L245). The attribute's comment: “(6) implies (5)”.

> **Stacks 0AJU, (6) ⇒ (5).**  If the Jacobian determinant of `f₁, …, f_r ∈ J` divides
> `a ^ c`, then `a ^ c` annihilates `H⁰(NL^∧_{B/A})`.
>
> Cramer's rule `M · adj(M) = det(M) · 1` puts `det(M) · eᵢ` in the image of the Jacobian matrix,
> whose columns are images of the differential; so `det(M)`, and with it every multiple of it,
> carries `⨁ i, B dxᵢ` into the image of the differential.  The second half of the two
> conditions is literally the same sentence, so the exponent and the family carry over.

```lean
public theorem isArtinPreliminary_of_isArtinJacobian (B : AdicFiniteTypeAlgebra.{u, v} A I)
    (P : CompletedPolynomialPresentation I B) (h : IsArtinJacobian B P) :
    IsArtinPreliminary B P
```

**`Rig.isCohomologyAnnihilated_of_isArtinPreliminary`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/RigEtaleTFAE.lean, line 375](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/RigEtaleTFAE.lean#L375). The attribute's comment: “(5) implies (3)”.

> **Stacks 0AJU, (5) ⇒ (3).**  Condition (5) gives, for each `a ∈ I`, a power of `a`
> annihilating both cohomology modules of `NL^∧_{B/A}`: for `H⁰` this is its first half and for
> `H⁻¹` it is `Rig.pow_mem_annihilator_ker_differential_of_artinPreliminary`.  The scalars
> annihilating both form an ideal of the Noetherian ring `B`, and every element of `IB` has a
> power in it, so a single power of `IB` lies in it.

```lean
public theorem isCohomologyAnnihilated_of_isArtinPreliminary
    (B : AdicFiniteTypeAlgebra.{u, v} A I) (P : CompletedPolynomialPresentation I B)
    (h : IsArtinPreliminary B P) : IsCohomologyAnnihilated B P
```

**`Rig.isRigEtale_iff_isJacobianCramerBounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/RigEtaleTFAE.lean, line 411](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/RigEtaleTFAE.lean#L411). The attribute's comment: “(1) iff (7)”.

> **Stacks 0AJU, (1) ⇔ (7).**  Rig-étaleness of `B` over `(A, I)` is equivalent to the
> Jacobian ideal and the Cramer ideal of *every* finite generating family of `J` each containing
> a power of `IB`.
>
> For a single family this is Stacks 0AJY,
> `Rig.isRigEtale_iff_exists_pow_le_completedJacobianIdeal_and_completedCramerIdeal`; the
> quantified form follows because `J` is a finitely generated ideal of the Noetherian ring
> `A⟨x₁, …, x_r⟩`, so at least one such family exists.

```lean
public theorem isRigEtale_iff_isJacobianCramerBounded (B : AdicFiniteTypeAlgebra.{u, v} A I)
    (P : CompletedPolynomialPresentation I B) :
    IsRigEtale B ↔ IsJacobianCramerBounded B P
```

**`Rig.tfae_isRigEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/RigEtaleTFAE.lean, line 444](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/RigEtaleTFAE.lean#L444).

> **Stacks 0AJU.**  Let `A` be a Noetherian ring, `I ⊆ A` an ideal, `B` an `I`-adically
> complete `A`-algebra of finite type modulo `I` and `B = A⟨x₁, …, x_r⟩ / J` a completed
> polynomial presentation.  The seven Artin criteria are equivalent:
>
> 1. `B` is rig-étale over `(A, I)`;
> 2. some power of `I` annihilates the identity of `NL^∧_{B/A}` in `D(B)`;
> 3. some power of `IB` annihilates `H⁻¹(NL^∧_{B/A})` and `H⁰(NL^∧_{B/A})`;
> 4. some power of `I` annihilates `H^i(NL_{Bₙ/Aₙ})` for `i = -1, 0` and every `n ≥ 1`;
> 5. for every `a ∈ I` some `a ^ c` annihilates `H⁰(NL^∧_{B/A})` and there are `f₁, …, f_r ∈ J`
>    with `a ^ c · J ⊆ (f₁, …, f_r) + J²`;
> 6. for every `a ∈ I` there are `f₁, …, f_r ∈ J` whose Jacobian determinant divides `a ^ c` and
>    with `a ^ c · J ⊆ (f₁, …, f_r) + J²`;
> 7. the Jacobian ideal and the Cramer ideal of every finite generating family of `J` each
>    contain a power of `IB`.
>
> The cycle is closed as `(1) ⇒ (6) ⇒ (5) ⇒ (3) ⇒ (1)`, with `(1) ⇔ (2)`, `(3) ⇔ (4)` and
> `(1) ⇔ (7)` hung off it.

```lean
public theorem tfae_isRigEtale (B : AdicFiniteTypeAlgebra.{u, v} A I)
    (P : CompletedPolynomialPresentation I B) :
    List.TFAE [IsRigEtale B, IsDerivedAnnihilated B P, IsCohomologyAnnihilated B P,
      IsReductionCohomologyAnnihilated B, IsArtinPreliminary B P, IsArtinJacobian B P,
      IsJacobianCramerBounded B P]
```

## Tag 0AJY, an item

[Tag 0AJY](https://stacks.math.columbia.edu/tag/0AJY) in the Stacks Project.

**`Rig.isRigEtale_iff_exists_pow_le_completedJacobianIdeal_and_completedCramerIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/JacobianCramerCriterion.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/JacobianCramerCriterion.lean#L180). The attribute's comment: “(7) of 0AJU, as an equivalence with rig-étaleness”.

> **Stacks 0AJY**, part (7) of Stacks 0AJU.  For an `I`-adically complete `A`-algebra `B` of
> finite type modulo `I` over a Noetherian ring `A`, a completed polynomial presentation
> `B = A⟨x₁, …, x_r⟩ / J` and generators `f₁, …, f_t` of `J`, rig-étaleness of `B` over `(A, I)`
> is equivalent to the Jacobian ideal and the Cramer ideal of `B` over `A` each containing a
> power of `IB`.

```lean
public theorem isRigEtale_iff_exists_pow_le_completedJacobianIdeal_and_completedCramerIdeal
    (B : AdicFiniteTypeAlgebra.{u, v} A I) (P : CompletedPolynomialPresentation I B) {t : ℕ}
    (f : Fin t → P.completedPolynomialRing) (hf : P.ker = Ideal.span (Set.range f)) :
    IsRigEtale B ↔
      ((∃ c : ℕ, (I ^ c).map (algebraMap A B.carrier) ≤ completedJacobianIdeal B P f) ∧
        ∃ c : ℕ, (I ^ c).map (algebraMap A B.carrier) ≤ completedCramerIdeal B P)
```

## Tag 0GB1, a lemma

[Tag 0GB1](https://stacks.math.columbia.edu/tag/0GB1) in the Stacks Project.

**`Rig.isRigSmooth_of_isRigEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Restricted/RigEtale.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Restricted/RigEtale.lean#L95).

> **Stacks 0GB1.** A rig-étale adically finite type algebra over `(A, I)` is rig-smooth.

```lean
theorem isRigSmooth_of_isRigEtale {A : Type u} [CommRing A] [IsNoetherianRing A]
    {I : Ideal A} (B : AdicFiniteTypeAlgebra.{u, v} A I)
    (hB : IsRigEtale B) : IsRigSmooth B
```

## Tag 0ALQ, a lemma

[Tag 0ALQ](https://stacks.math.columbia.edu/tag/0ALQ) in the Stacks Project.

**`Rig.isRigEtale_adicCompletionObj_of_isEtaleOutside`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/RigEtaleLocus.lean, line 434](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/RigEtaleLocus.lean#L434). The attribute's comment: “part (1)”.

> **Stacks 0ALQ, part (1).**  Let `A` be a Noetherian ring, `I ⊆ A` an ideal and `B` a finite
> type `A`-algebra.  If `Spec(B) → Spec(A)` is étale over `Spec(A) ∖ V(I)`, then the `I`-adic
> completion `B^` satisfies the equivalent conditions of Stacks 0AJU, that is, `B^` is rig-étale
> over `(A, I)`.
>
> Étaleness off `V(I)` says that `H¹(L_{B/A})` and `Ω_{B/A}` are supported in `V(IB)`, so — both
> being finite modules over the Noetherian ring `B` — a power of `IB` annihilates them, hence
> also their base changes to `B^`.  The pivot
> `Rig.isRigEtale_adicCompletionObj_iff` turns that into rig-étaleness.

```lean
public theorem isRigEtale_adicCompletionObj_of_isEtaleOutside (h : IsEtaleOutside I B) :
    IsRigEtale (adicCompletionObj I (B := B))
```

**`Rig.exists_isEtaleOutside_localization_of_isRigEtale_adicCompletionObj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/RigEtaleLocus.lean, line 471](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/RigEtaleLocus.lean#L471). The attribute's comment: “part (2)”.

> **Stacks 0ALQ, part (2).**  Let `A` be a Noetherian ring, `I ⊆ A` an ideal and `B` a finite
> type `A`-algebra.  If the `I`-adic completion `B^` satisfies the equivalent conditions of
> Stacks 0AJU — that is, if `B^` is rig-étale over `(A, I)` — then there is `g ∈ 1 + IB` such that
> `Spec(B_g) → Spec(A)` is étale over `Spec(A) ∖ V(I)`.
>
> The element `g` is produced by Nakayama's lemma: rig-étaleness gives a `c` with `Iᶜ B^`
> annihilating `B^ ⊗_B H¹(L_{B/A})` and `B^ ⊗_B Ω_{B/A}`, so `Iᶜ B` annihilates both finite
> `B`-modules only modulo `⋂ₙ (IB)ⁿ`, and one element of `1 + IB` kills that intersection.  After
> inverting it, every prime of `B` off `V(IB)` contains no element of `Iᶜ B` and so lies outside
> the supports of the two modules, which is étaleness there.

```lean
public theorem exists_isEtaleOutside_localization_of_isRigEtale_adicCompletionObj
    (h : IsRigEtale (adicCompletionObj I (B := B))) :
    ∃ g : B, g - 1 ∈ I.map (algebraMap A B) ∧ IsEtaleOutside I (Localization.Away g)
```

**`Rig.isEtaleOutside_and_isRigEtale_adicCompletionObj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/RigEtaleLocus.lean, line 529](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/RigEtaleLocus.lean#L529).

> **Stacks 0ALQ.**  Let `A` be a Noetherian ring, `I ⊆ A` an ideal and `B` a finite type
> `A`-algebra, and write `B^` for the `I`-adic completion of `B`.
>
> 1. If `Spec(B) → Spec(A)` is étale over `Spec(A) ∖ V(I)`, then `B^` satisfies the equivalent
>    conditions of Stacks 0AJU, in the form of their first condition `Rig.IsRigEtale`.
> 2. If `B^` satisfies those conditions, then there exists `g ∈ 1 + IB` such that
>    `Spec(B_g) → Spec(A)` is étale over `Spec(A) ∖ V(I)`.
>
> The two implications are `Rig.isRigEtale_adicCompletionObj_of_isEtaleOutside` and
> `Rig.exists_isEtaleOutside_localization_of_isRigEtale_adicCompletionObj`.

```lean
public theorem isEtaleOutside_and_isRigEtale_adicCompletionObj :
    (IsEtaleOutside I B → IsRigEtale (adicCompletionObj I (B := B))) ∧
      (IsRigEtale (adicCompletionObj I (B := B)) →
        ∃ g : B, g - 1 ∈ I.map (algebraMap A B) ∧ IsEtaleOutside I (Localization.Away g))
```

## Tag 0AK2, a lemma

[Tag 0AK2](https://stacks.math.columbia.edu/tag/0AK2) in the Stacks Project.

**`Rig.smul_id_of_completedBaseChangeFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/NaiveCotangent/BaseChangeSmulId.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/NaiveCotangent/BaseChangeSmulId.lean#L102).

> With `(A₁, I₁) → (A₂, I₂)` as in Stacks Remark 0AL5, witnessed by `hc` and `hmap`, a scalar
> `f₁ ∈ B₁` acting by zero on `NL^∧_{B₁/A₁}` in `D(B₁)` has its image
> `Rig.CompletedBaseChange.scalar` in the base change `B₂ = C.functor.obj B₁` acting by zero on
> `NL^∧_{B₂/A₂}` in `D(B₂)`, for any completed polynomial presentations of the two algebras.

```lean
public theorem smul_id_of_completedBaseChangeFunctor
    (C : CompletedBaseChange (A₁ := A₁) (A₂ := A₂) (I₁ := I₁) (I₂ := I₂))
    (hc : 0 < c) (hmap : (I₁ ^ c).map (algebraMap A₁ A₂) ≤ I₂)
    (B₁ : AdicFiniteTypeAlgebra.{u₁, v} A₁ I₁)
    (P₁ : CompletedPolynomialPresentation I₁ B₁)
    (P₂ : CompletedPolynomialPresentation I₂ (C.functor.obj B₁)) (f₁ : B₁.carrier)
    (h : f₁ • 𝟙 (derivedCompletedNaiveCotangentComplex B₁ P₁) = 0) :
    C.scalar B₁ f₁ •
      𝟙 (derivedCompletedNaiveCotangentComplex (C.functor.obj B₁) P₂) = 0
```

## Tag 0GB2, a lemma

[Tag 0GB2](https://stacks.math.columbia.edu/tag/0GB2) in the Stacks Project.

**`Rig.isRigEtale_completedBaseChangeOfIsNoetherianRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/RigEtaleBaseChange.lean, line 227](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/RigEtaleBaseChange.lean#L227). The attribute's comment: “preservation of rig-étaleness”.

> Let `A₁ → A₂` be a map of Noetherian rings and let `Iᵢ ⊆ Aᵢ` be ideals with
> `V(I₁ A₂) = V(I₂)`. Let `B₁` be adically of finite type over `(A₁, I₁)` and let
> `B₂ = (B₁ ⊗_{A₁} A₂)^∧_{I₂}` be its base change as in Stacks Remark 0AL5, the functor
> `Rig.completedBaseChangeOfIsNoetherianRing`. If `B₁` is rig-étale over `(A₁, I₁)`, then `B₂` is
> rig-étale over `(A₂, I₂)`.

```lean
public theorem isRigEtale_completedBaseChangeOfIsNoetherianRing
    (hV : PrimeSpectrum.zeroLocus ((I₁.map (algebraMap A₁ A₂) : Ideal A₂) : Set A₂) =
      PrimeSpectrum.zeroLocus (I₂ : Set A₂))
    (B₁ : AdicFiniteTypeAlgebra.{u₁, v} A₁ I₁) (hB₁ : IsRigEtale B₁) :
    IsRigEtale ((completedBaseChangeOfIsNoetherianRing
      (exists_pos_pow_map_le_of_zeroLocus_eq hV)).functor.obj B₁)
```

## Tag 0AKJ, a lemma

[Tag 0AKJ](https://stacks.math.columbia.edu/tag/0AKJ) in the Stacks Project.

**`Rig.exists_etale_factorization_algHom_henselization`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/Henselization.lean, line 322](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/Henselization.lean#L322). The attribute's comment: “étale factorization”.

> **Stacks Project, Tag 0AKJ (étale factorization).** Every map from a
> finite type algebra to the henselization of `(C, IC)` factors through an
> étale `C`-algebra whose closed fibre is canonically isomorphic to that of
> `C`.

```lean
public lemma exists_etale_factorization_algHom_henselization
    (A : Type u) (B : Type v) (C : Type w)
    [CommRing A] [IsNoetherianRing A]
    [CommRing B] [Algebra A B] [Algebra.FiniteType A B]
    (I : Ideal A)
    [CommRing C] [Algebra A C] :
    let H := (henselization C (I.map (algebraMap A C)) : Type w)
    letI : Algebra A H :=
      ((algebraMap C H).comp (algebraMap A C)).toAlgebra
    letI : IsScalarTower A C H :=
      IsScalarTower.of_algebraMap_eq fun _ ↦ rfl
    ∀ f : B →ₐ[A] H,
    ∃ (Cp : Type (max u v w)) (_ : CommRing Cp) (_ : Algebra C Cp)
      (_ : Algebra A Cp) (_ : IsScalarTower A C Cp) (_ : Algebra.Etale C Cp)
      (g : B →ₐ[A] Cp)
      (k : Cp →ₐ[C] H),
      Function.Bijective
        (Ideal.quotientMap ((I.map (algebraMap A C)).map (algebraMap C Cp))
          (algebraMap C Cp) Ideal.le_comap_map) ∧
        (k.restrictScalars A).comp g = f
```

**`Rig.exists_unique_algHom_henselization_of_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/HenselizationDescent.lean, line 962](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/HenselizationDescent.lean#L962). The attribute's comment: “descent and uniqueness”.

> **Stacks Project, Tag 0AKJ (descent and uniqueness).**  Let `A` be a Noetherian ring,
> `I ⊆ A` an ideal and `B` a finite type `A`-algebra such that `Spec(B) → Spec(A)` is étale over
> `Spec(A) ∖ V(I)`, and let `C` be a Noetherian `A`-algebra.  Then every `A`-algebra map
> `B^∧ → C^∧` of `I`-adic completions comes from a *unique* `A`-algebra map `B → Cʰ` into the
> henselization of the pair `(C, IC)`.
>
> Uniqueness is `Rig.eq_of_henselizationToAdicCompletion_comp_eq`, which rests on the fact that
> `Cʰ` is a subring of `C^∧`.  For existence, follow the source and replace `(A, I, B, C)` by
> `(C, IC, C ⊗_A B, C)`: the given map makes `D = C ⊗_A B` a `C`-algebra over `C^∧`, and the
> étaleness hypothesis, which annihilates `Ω_{B/A}` by a power of `I`, annihilates `Ω_{D/C}` by
> the same power after base change.  `exists_algHom_henselization_of_annihilator_kaehlerDifferential`
> then lifts `D → C^∧` to `D → Cʰ`, and restricting along `B → D` gives the map sought.

```lean
public theorem exists_unique_algHom_henselization_of_adicCompletion
    (A : Type u) (B : Type v) (C : Type w)
    [CommRing A] [IsNoetherianRing A]
    [CommRing B] [Algebra A B] [Algebra.FiniteType A B]
    (I : Ideal A) (hEtale : IsEtaleOutside I B)
    [CommRing C] [Algebra A C] [IsNoetherianRing C] :
    let H := (henselization C (I.map (algebraMap A C)) : Type w)
    letI : Algebra A H :=
      ((algebraMap C H).comp (algebraMap A C)).toAlgebra
    letI : IsScalarTower A C H :=
      IsScalarTower.of_algebraMap_eq fun _ ↦ rfl
    ∀ φ : AdicCompletion (I.map (algebraMap A B)) B →ₐ[A]
          AdicCompletion (I.map (algebraMap A C)) C,
        ∃! ψ : B →ₐ[A] H,
          ((henselizationToAdicCompletion C
            (I.map (algebraMap A C))).val.restrictScalars A).comp ψ =
            φ.comp (IsScalarTower.toAlgHom A B
              (AdicCompletion (I.map (algebraMap A B)) B))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 88.8, Tag 0ALP](https://stacks.math.columbia.edu/tag/0ALP)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
