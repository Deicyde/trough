---
declaration: section
origin: cited
lean: IsDiscreteValuationRing.galAction_transitive_on_maximalIdeals_integralClosure, IsDiscreteValuationRing.exists_uniform_ramificationIdx_inertiaDeg_and_finrank_eq, IsDiscreteValuationRing.under_eq_maximalIdeal_and_ker_stabilizerHom_eq_inertia, MulAction.stabilizer, Ideal.inertia, Ideal.Quotient.stabilizerHom, Ideal.Quotient.ker_stabilizerHom, IsDiscreteValuationRing.residueField_normal_and_stabilizerHom_surjective_of_isGalois
statement: formalized
proof: formalized
---

# 15.114 Galois extensions and ramification

Section 15.114 of the Stacks Project, [Tag 09E3](https://stacks.math.columbia.edu/tag/09E3). 12 tags here are carried by 17 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09EA, a lemma

[Tag 09EA](https://stacks.math.columbia.edu/tag/09EA) in the Stacks Project.

**`IsDiscreteValuationRing.galAction_transitive_on_maximalIdeals_integralClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Galois.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DiscreteValuationRing/Galois.lean#L157).

> For a finite Galois extension `L / K`, the canonical action of `Gal(L/K)` on the integral
> closure of a discrete valuation ring `A` in `L` is transitive on its maximal ideals.

```lean
theorem galAction_transitive_on_maximalIdeals_integralClosure
    (A : Type*) [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    (K : Type*) [Field K] [Algebra A K] [IsFractionRing A K]
    (L : Type*) [Field L] [Algebra K L] [FiniteDimensional K L]
    [IsGalois K L] [Algebra A L] [IsScalarTower A K L] :
    let B := integralClosure A L
    letI := IsIntegralClosure.MulSemiringAction A K L B
    ∀ P Q : Ideal B, P.IsMaximal → Q.IsMaximal →
      ∃ σ : Gal(L/K), σ • P = Q
```

## Tag 09EB, a lemma

[Tag 09EB](https://stacks.math.columbia.edu/tag/09EB) in the Stacks Project.

**`IsDiscreteValuationRing.exists_uniform_ramificationIdx_inertiaDeg_and_finrank_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Galois.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DiscreteValuationRing/Galois.lean#L182).

> In a finite Galois extension of the fraction field of a discrete valuation ring, all primes
> of the integral closure over the maximal ideal have the same positive ramification index and
> inertia degree. The field degree is the number of these primes times the two common values.

```lean
theorem exists_uniform_ramificationIdx_inertiaDeg_and_finrank_eq
    (A : Type*) [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    (K : Type*) [Field K] [Algebra A K] [IsFractionRing A K]
    (L : Type*) [Field L] [Algebra K L] [FiniteDimensional K L]
    [IsGalois K L] [Algebra A L] [IsScalarTower A K L] :
    let B := integralClosure A L
    let p := IsLocalRing.maximalIdeal A
    ∃ e f : ℕ,
      1 ≤ e ∧
      1 ≤ f ∧
      (∀ P : p.primesOver B, P.1.ramificationIdx A = e ∧ P.1.inertiaDeg A = f) ∧
      (p.primesOver B).ncard * e * f = Module.finrank K L
```

## Tag 09EC, a definition

[Tag 09EC](https://stacks.math.columbia.edu/tag/09EC) in the Stacks Project.

**`IsDiscreteValuationRing.under_eq_maximalIdeal_and_ker_stabilizerHom_eq_inertia`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Galois.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DiscreteValuationRing/Galois.lean#L235). The attribute's comment: “The decomposition group is `MulAction.stabilizer` and the inertia group is `Ideal.inertia`, both of which Mathlib already has for an arbitrary action; what is recorded here is that they are the source's two groups, the ideal below `P` being the maximal ideal of `A` so that the extension acted on is `κ(P)/κ_A`. Stated without the fraction-field, finiteness and Galois hypotheses, which the comparison does not use, so the source's setting is a special case.”. References: SGA 7 I (0.3), “partial”.

> The decomposition and the inertia group at a maximal ideal `P` of the integral closure `B`
> of a discrete valuation ring `A` in a field extension `L / K`.
>
> The decomposition group is the stabilizer `{σ ∈ Gal(L/K) | σ P = P}`, and the ideal of `A` below
> `P` is the maximal ideal, so the residue extension the decomposition group acts on really is
> `κ(P) / κ_A`. The inertia group is the kernel of that action: it is `Ideal.inertia`, sitting
> inside the decomposition group, and an element of the decomposition group lies in it exactly when
> it acts trivially on `κ(P)`.

```lean
theorem under_eq_maximalIdeal_and_ker_stabilizerHom_eq_inertia
    (A : Type*) [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    (K : Type*) [Field K] [Algebra A K]
    (L : Type*) [Field L] [Algebra K L] [Algebra A L] [IsScalarTower A K L]
    (P : Ideal (integralClosure A L)) [P.IsMaximal] :
    let B := integralClosure A L
    let D := MulAction.stabilizer Gal(L/K) P
    let I := P.inertia Gal(L/K)
    (∀ σ : Gal(L/K), σ ∈ D ↔ σ • P = P) ∧
      P.under A = IsLocalRing.maximalIdeal A ∧
      I ≤ D ∧
      (Ideal.Quotient.stabilizerHom P (P.under A) Gal(L/K)).ker = I.subgroupOf D ∧
      (∀ σ : D, σ ∈ (Ideal.Quotient.stabilizerHom P (P.under A) Gal(L/K)).ker ↔
        ∀ b : B, Ideal.Quotient.mk P ((σ : Gal(L/K)) • b) = Ideal.Quotient.mk P b)
```

Declarations registered for the tag:

- [`MulAction.stabilizer`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=MulAction.stabilizer#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/DiscreteValuationRing/Galois.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DiscreteValuationRing/Galois.lean#L102) (StacksFrontier): “(1), the decomposition group”. References: SGA 1 V (6.13); SGA 3 I (2.3.3), “special case”; SGA 3 VIIB (2.5.A); SGA 3 XXI (6.7.2), “more general”; SGA 5 IIIB (5.13), “more general”; SGA 5 X (4.2).
- [`Ideal.inertia`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.inertia#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/DiscreteValuationRing/Galois.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DiscreteValuationRing/Galois.lean#L110) (StacksFrontier): “(2), the inertia group”. References: SGA 7 I (0.3); SGA 7 XIII (0.2).
- [`Ideal.Quotient.stabilizerHom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.Quotient.stabilizerHom#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/DiscreteValuationRing/Galois.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DiscreteValuationRing/Galois.lean#L114) (StacksFrontier): “The action of the decomposition group on the residue algebra”.
- [`Ideal.Quotient.ker_stabilizerHom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.Quotient.ker_stabilizerHom#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/DiscreteValuationRing/Galois.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DiscreteValuationRing/Galois.lean#L117) (StacksFrontier): “The inertia group as the kernel of the residue-algebra action”.

## Tag 09ED, a lemma

[Tag 09ED](https://stacks.math.columbia.edu/tag/09ED) in the Stacks Project.

**`IsDiscreteValuationRing.residueField_normal_and_stabilizerHom_surjective_of_isGalois`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Galois.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DiscreteValuationRing/Galois.lean#L263). References: SGA 1 V (1.1), “special case”; SGA 1 V (1.3), “special case”.

> In a finite Galois extension of the fraction field of a discrete valuation ring, every
> residue extension at a maximal ideal of the integral closure is normal, and its decomposition
> group surjects onto the relative automorphism group. Separability of one such residue extension is
> equivalent to separability of all of them; when this holds, the fixed residue extension is Galois
> and the same canonical map is surjective onto its Galois group.

```lean
theorem residueField_normal_and_stabilizerHom_surjective_of_isGalois
    (A : Type*) [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    (K : Type*) [Field K] [Algebra A K] [IsFractionRing A K]
    (L : Type*) [Field L] [Algebra K L] [FiniteDimensional K L]
    [IsGalois K L] [Algebra A L] [IsScalarTower A K L]
    (P : Ideal (integralClosure A L)) [P.IsMaximal] :
    let B := integralClosure A L
    let p := P.under A
    letI : Field (A ⧸ p) := Ideal.Quotient.field p
    letI : Field (B ⧸ P) := Ideal.Quotient.field P
    Normal (A ⧸ p) (B ⧸ P) ∧
      Function.Surjective (Ideal.Quotient.stabilizerHom P p Gal(L/K)) ∧
      ((∃ (Q : Ideal B) (_hQ : Q.IsMaximal),
          let q := Q.under A
          letI : Field (A ⧸ q) := Ideal.Quotient.field q
          letI : Field (B ⧸ Q) := Ideal.Quotient.field Q
          Algebra.IsSeparable (A ⧸ q) (B ⧸ Q)) ↔
        (∀ (Q : Ideal B) (_hQ : Q.IsMaximal),
          let q := Q.under A
          letI : Field (A ⧸ q) := Ideal.Quotient.field q
          letI : Field (B ⧸ Q) := Ideal.Quotient.field Q
          Algebra.IsSeparable (A ⧸ q) (B ⧸ Q))) ∧
      ((∃ (Q : Ideal B) (_hQ : Q.IsMaximal),
          let q := Q.under A
          letI : Field (A ⧸ q) := Ideal.Quotient.field q
          letI : Field (B ⧸ Q) := Ideal.Quotient.field Q
          Algebra.IsSeparable (A ⧸ q) (B ⧸ Q)) →
        IsGalois (A ⧸ p) (B ⧸ P) ∧
          Function.Surjective (Ideal.Quotient.stabilizerHom P p Gal(L/K)))
```

## Tag 09EE, a lemma

[Tag 09EE](https://stacks.math.columbia.edu/tag/09EE) in the Stacks Project.

**`IsDiscreteValuationRing.exists_wildInertia_exact_and_tameInertia_equiv_rootsOfUnity`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Galois.lean, line 847](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DiscreteValuationRing/Galois.lean#L847). References: SGA 1 XIII (2.0), “inertia structure”; SGA 7 I (0.3), “finite Galois case”.

> The inertia group at a maximal ideal of the integral closure in a finite Galois extension
> has a canonical wild–tame exact sequence. Wild inertia consists precisely of the elements of
> inertia acting trivially on the maximal ideal modulo its square; it is normal in the decomposition
> group and is a `p`-group in positive residue characteristic (and trivial in characteristic zero).
> The tame quotient is cyclic of prime-to-`p` order and is canonically isomorphic to the
> corresponding roots of unity in the residue field. If the residue extension is separable, wild
> inertia is also the kernel of the action on `B / P²`.

```lean
theorem exists_wildInertia_exact_and_tameInertia_equiv_rootsOfUnity
    (A : Type*) [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    (K : Type*) [Field K] [Algebra A K] [IsFractionRing A K]
    (L : Type*) [Field L] [Algebra K L] [FiniteDimensional K L]
    [IsGalois K L] [Algebra A L] [IsScalarTower A K L]
    (P : Ideal (integralClosure A L)) [P.IsMaximal] :
    let B := integralClosure A L
    letI := IsIntegralClosure.MulSemiringAction A K L B
    let D := MulAction.stabilizer Gal(L/K) P
    let I := P.inertia Gal(L/K)
    let inclusion : I →* D := I.subtype.codRestrict D
      (fun σ ↦ Ideal.inertia_le_stabilizer (M := Gal(L/K)) P σ.property)
    let e := P.ramificationIdx A
    let p := ringChar (IsLocalRing.ResidueField A)
    ∃ W : Subgroup I, ∃ _hW : W.Normal,
      (W.map inclusion).Normal ∧
      (∀ σ : I, σ ∈ W ↔ ∀ b : B, b ∈ P → (σ : Gal(L/K)) • b - b ∈ P ^ 2) ∧
      (∀ σ : D, σ ∈ W.map inclusion ↔
        (σ : Gal(L/K)) ∈ I ∧ ∀ b : B, b ∈ P → σ • b - b ∈ P ^ 2) ∧
      (0 < p → IsPGroup p W) ∧
      (p = 0 → W = ⊥) ∧
      (letI : Field (A ⧸ P.under A) := Ideal.Quotient.field (P.under A)
       Algebra.IsSeparable (A ⧸ P.under A) (B ⧸ P) →
         ∀ σ : D, σ ∈ W.map inclusion ↔ ∀ b : B, σ • b - b ∈ P ^ 2) ∧
      ∃ θ : I →* rootsOfUnity e (B ⧸ P),
        Function.Injective W.subtype ∧
        Function.MulExact W.subtype θ ∧
        Function.Surjective θ ∧
        IsCyclic (rootsOfUnity e (B ⧸ P)) ∧
        Nat.card (rootsOfUnity e (B ⧸ P)) = e / p ^ e.factorization p ∧
        (∀ (σ : I) (x a : B), x ∈ P → x ∉ P ^ 2 →
            Ideal.Quotient.mk P a = (θ σ).1.1 →
            (σ : Gal(L/K)) • x - a * x ∈ P ^ 2) ∧
        ∀ θ' : I →* rootsOfUnity e (B ⧸ P),
          (∀ (σ : I) (x a : B), x ∈ P → x ∉ P ^ 2 →
            Ideal.Quotient.mk P a = (θ' σ).1.1 →
            (σ : Gal(L/K)) • x - a * x ∈ P ^ 2) →
          θ' = θ
```

## Tag 0BU3, an equation

[Tag 0BU3](https://stacks.math.columbia.edu/tag/0BU3) in the Stacks Project.

**`IsDiscreteValuationRing.exists_uniformizerRatioMap_to_rootsOfUnity`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Galois.lean, line 992](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DiscreteValuationRing/Galois.lean#L992).

> Let a group act on a discrete valuation ring, trivially on its residue field. Suppose an
> invariant element is a unit times the `e`-th power of a uniformizer. For every group element, its
> action on the uniformizer differs from the uniformizer by a unit; the residues of these units are
> `e`-th roots of unity and hence define a map to the group of such roots.

```lean
theorem exists_uniformizerRatioMap_to_rootsOfUnity
    (C : Type u) [CommRing C] [IsDomain C] [IsDiscreteValuationRing C]
    (I : Type v) [Group I] [MulSemiringAction I C]
    (e : ℕ) (π a : C) (u : Cˣ)
    (hπ : Irreducible π)
    (ha : a = (u : C) * π ^ e)
    (ha_fixed : ∀ σ : I, σ • a = a)
    (hres : ∀ (σ : I) (x : C),
      Ideal.Quotient.mk (IsLocalRing.maximalIdeal C) (σ • x) =
        Ideal.Quotient.mk (IsLocalRing.maximalIdeal C) x) :
    ∃ (θ : I → rootsOfUnity e (C ⧸ IsLocalRing.maximalIdeal C))
      (θunit : I → Cˣ),
      (∀ σ : I, (θunit σ : C) * π = σ • π) ∧
        ∀ σ : I,
          (θ σ : (C ⧸ IsLocalRing.maximalIdeal C)ˣ) =
            Units.map (Ideal.Quotient.mk (IsLocalRing.maximalIdeal C)) (θunit σ)
```

## Tag 0BU4, a definition

[Tag 0BU4](https://stacks.math.columbia.edu/tag/0BU4) in the Stacks Project.

**`IsDiscreteValuationRing.inertiaCharacter`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Inertia/Character.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DiscreteValuationRing/Inertia/Character.lean#L176).

> **Stacks Project, Tag 0BU4.** The canonical character from inertia to the roots of unity of
> order the ramification index in the residue field.

```lean
noncomputable def inertiaCharacter
```

**`IsDiscreteValuationRing.wildInertiaGroup`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Inertia/Character.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DiscreteValuationRing/Inertia/Character.lean#L180). References: SGA 1 XIII (2.0), “partial”.

> **Stacks Project, Tag 0BU4.** The wild inertia group at `P`.

```lean
noncomputable def wildInertiaGroup
```

**`IsDiscreteValuationRing.tameInertiaGroup`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Inertia/Character.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DiscreteValuationRing/Inertia/Character.lean#L188). References: SGA 7 I (0.3).

> **Stacks Project, Tag 0BU4.** The tame inertia group, namely inertia modulo wild inertia.

```lean
abbrev tameInertiaGroup
```

**`IsDiscreteValuationRing.tameInertiaMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Inertia/Character.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DiscreteValuationRing/Inertia/Character.lean#L192).

> **Stacks Project, Tag 0BU4.** The quotient map from inertia to tame inertia.

```lean
noncomputable def tameInertiaMap : P.inertia Gal(L/K) →* tameInertiaGroup A K L P
```

**`IsDiscreteValuationRing.tameInertiaEquivRootsOfUnity`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Inertia/Character.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DiscreteValuationRing/Inertia/Character.lean#L205). References: SGA 7 I (0.3), “finite Galois case”.

> **Stacks Project, Tag 0BU4.** The canonical isomorphism from tame inertia to the roots of
> unity induced by the inertia character.

```lean
noncomputable def tameInertiaEquivRootsOfUnity :
    tameInertiaGroup A K L P ≃*
      rootsOfUnity (P.ramificationIdx A) (integralClosure A L ⧸ P)
```

## Tag 0BU5, a lemma

[Tag 0BU5](https://stacks.math.columbia.edu/tag/0BU5) in the Stacks Project.

**`IsDiscreteValuationRing.inertiaCharacter_conj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Inertia/Character.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DiscreteValuationRing/Inertia/Character.lean#L238). References: SGA 7 I (0.3), “finite Galois case”.

> **Stacks Tag 0BU5.** The inertia character is equivariant for conjugation by the
> decomposition group: conjugating an inertia element by a decomposition element has character
> equal to the image of the original character under the induced residue-field automorphism.

```lean
theorem inertiaCharacter_conj
    (A : Type*) [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    (K : Type*) [Field K] [Algebra A K] [IsFractionRing A K]
    (L : Type*) [Field L] [Algebra K L] [FiniteDimensional K L]
    [IsGalois K L] [Algebra A L] [IsScalarTower A K L]
    (P : Ideal (integralClosure A L)) [P.IsMaximal] :
    let B := integralClosure A L
    letI := IsIntegralClosure.MulSemiringAction A K L B
    let D := MulAction.stabilizer Gal(L/K) P
    let I := P.inertia Gal(L/K)
    let e := P.ramificationIdx A
    let conjugate : D → I → I := fun τ σ ↦
      ⟨(τ : Gal(L/K)) * (σ : Gal(L/K)) * (τ : Gal(L/K))⁻¹, by
        rw [Ideal.mem_inertia]
        intro x
        have hσ := (Ideal.mem_inertia.mp σ.property) ((τ : Gal(L/K))⁻¹ • x)
        have hτ := Ideal.smul_mem_pointwise_smul (τ : Gal(L/K)) _ P hσ
        rw [τ.property] at hτ
        simpa only [mul_smul, smul_sub, smul_inv_smul] using hτ⟩
    ∀ (θ : I →* rootsOfUnity e (B ⧸ P)),
      (∀ (σ : I) (x a : B), x ∈ P → x ∉ P ^ 2 →
        Ideal.Quotient.mk P a = (θ σ).1.1 →
        (σ : Gal(L/K)) • x - a * x ∈ P ^ 2) →
      ∀ (τ : D) (σ : I),
        θ (conjugate τ σ) =
          (Ideal.quotientEquiv P P
            ((MulSemiringAction.toRingEquiv Gal(L/K) B) (τ : Gal(L/K)))
            τ.property.symm).toMulEquiv.restrictRootsOfUnity e (θ σ)
```

## Tag 09EH, a lemma

[Tag 09EH](https://stacks.math.columbia.edu/tag/09EH) in the Stacks Project.

**`IsDiscreteValuationRing.inertia_fixedSubalgebra_isIntegralClosure_and_etale_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Inertia/InvariantRing.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DiscreteValuationRing/Inertia/InvariantRing.lean#L229). References: SGA 7 I (0.3), “partial”.

> **Stacks Tag 09EH.** The subring of the integral closure fixed by the inertia group is the
> integral closure in the fixed field, and its localization at the prime below the chosen maximal
> ideal is étale over the original discrete valuation ring.

```lean
theorem inertia_fixedSubalgebra_isIntegralClosure_and_etale_localization
    (A : Type*) [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    (K : Type*) [Field K] [Algebra A K] [IsFractionRing A K]
    (L : Type*) [Field L] [Algebra K L] [FiniteDimensional K L]
    [IsGalois K L] [Algebra A L] [IsScalarTower A K L]
    (P : Ideal (integralClosure A L)) [P.IsMaximal] :
    let B := integralClosure A L
    letI := IsIntegralClosure.MulSemiringAction A K L B
    letI : SMulCommClass Gal(L/K) A B :=
      ⟨fun g a b ↦ by
        simp only [Algebra.smul_def]
        change galRestrict A K L B g (algebraMap A B a * b) =
          algebraMap A B a * galRestrict A K L B g b
        rw [map_mul, AlgEquiv.commutes]⟩
    let I := P.inertia Gal(L/K)
    let B' := FixedPoints.subalgebra A B I
    let L' := IntermediateField.fixedField I
    let inclusion : B' →ₐ[A] L := (integralClosure A L).val.comp B'.val
    let iota : B' →ₐ[A] L' :=
      inclusion.codRestrict (L'.toSubalgebra.restrictScalars A) (fun b ↦ by
        change (inclusion b : L) ∈ L'
        rw [IntermediateField.mem_fixedField_iff]
        intro g hg
        exact (algebraMap_galRestrict_apply A g (b : B)).symm.trans
          (congrArg (algebraMap B L) (b.property ⟨g, hg⟩)))
    letI := iota.toAlgebra
    IsIntegralClosure B' A L' ∧
      Algebra.Etale A (Localization.AtPrime (P.under B'))
```

## Tag 0BU6, a remark

[Tag 0BU6](https://stacks.math.columbia.edu/tag/0BU6) in the Stacks Project.

**`IsDiscreteValuationRing.decomposition_inertia_wildInertia_tower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Inertia/DecompositionTower.lean, line 622](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DiscreteValuationRing/Inertia/DecompositionTower.lean#L622).

> **Stacks Tag 0BU6.** The fixed fields, invariant rings, contracted primes, localized
> rings, and residue fields attached to the wild inertia, inertia, and decomposition groups of
> a maximal ideal in a finite Galois extension form the standard ramification tower.

```lean
theorem decomposition_inertia_wildInertia_tower
    (A : Type*) [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    (K : Type*) [Field K] [Algebra A K] [IsFractionRing A K]
    (L : Type*) [Field L] [Algebra K L] [FiniteDimensional K L]
    [IsGalois K L] [Algebra A L] [IsScalarTower A K L]
    (m : Ideal (integralClosure A L)) [m.IsMaximal] :
    let B := integralClosure A L
    letI := IsIntegralClosure.MulSemiringAction A K L B
    letI : SMulCommClass Gal(L/K) A B :=
      ⟨fun g a b ↦ by
        simp only [Algebra.smul_def]
        change galRestrict A K L B g (algebraMap A B a * b) =
          algebraMap A B a * galRestrict A K L B g b
        rw [map_mul, AlgEquiv.commutes]⟩
    let D := MulAction.stabilizer Gal(L/K) m
    let I := m.inertia Gal(L/K)
    let hID : I ≤ D := Ideal.inertia_le_stabilizer (M := Gal(L/K)) m
    let iID : I →* D := I.subtype.codRestrict D (fun σ ↦ hID σ.property)
    ∃ (P : Subgroup I) (hP : P.Normal),
      let PG : Subgroup Gal(L/K) := P.map I.subtype
      let PD : Subgroup D := P.map iID
      (∀ σ : D, σ ∈ PD ↔ (σ : Gal(L/K)) ∈ I ∧
        ∀ b : B, b ∈ m → (σ : Gal(L/K)) • b - b ∈ m ^ 2) ∧
      let ID : Subgroup D := I.subgroupOf D
      let LD := IntermediateField.fixedField D
      let LI := IntermediateField.fixedField I
      let LP := IntermediateField.fixedField PG
      let BD := FixedPoints.subalgebra A B D
      let BI := FixedPoints.subalgebra A B I
      let BP := FixedPoints.subalgebra A B PG
      let hPGI : PG ≤ I := fun σ hσ ↦ by
        obtain ⟨τ, -, rfl⟩
```

## Tag 0BU7, a lemma

[Tag 0BU7](https://stacks.math.columbia.edu/tag/0BU7) in the Stacks Project.

**`IsDiscreteValuationRing.surjective_restrictions_commute_with_residue_and_inertiaCharacter`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Inertia/GaloisTower.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DiscreteValuationRing/Inertia/GaloisTower.lean#L197).

> **Stacks Project, Tag 0BU7.** In a tower of finite Galois extensions of the fraction field
> of a discrete valuation ring, restriction surjects on decomposition, inertia, and wild inertia
> groups.  The induced maps commute with residue-field automorphisms and with the canonical inertia
> characters; on roots of unity the latter vertical map is the `e' / e`-power map.

```lean
theorem surjective_restrictions_commute_with_residue_and_inertiaCharacter
    (A : Type*) [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    (K : Type*) [Field K] [Algebra A K] [IsFractionRing A K]
    (L : Type*) [Field L] [Algebra K L] [FiniteDimensional K L]
    [IsGalois K L] [Algebra A L] [IsScalarTower A K L]
    (M : Type*) [Field M] [Algebra K M] [FiniteDimensional K M]
    [IsGalois K M] [Algebra L M] [IsScalarTower K L M]
    [Algebra A M] [IsScalarTower A K M] [IsScalarTower A L M]
    (r : Ideal (integralClosure A M)) [r.IsMaximal] :
    let B := integralClosure A L
    let C := integralClosure A M
    let fBC : B →ₐ[A] C := (IsScalarTower.toAlgHom A L M).mapIntegralClosure
    letI : Algebra B C := fBC.toRingHom.toAlgebra
    letI : IsScalarTower A B C :=
      IsScalarTower.of_algebraMap_eq fun x ↦ (fBC.commutes x).symm
    letI : Algebra.IsIntegral B C :=
      ⟨fun x ↦ IsIntegral.tower_top (IsIntegralClosure.isIntegral A M x)⟩
    letI : MulSemiringAction Gal(M/K) C :=
      IsIntegralClosure.MulSemiringAction A K M C
    letI : MulSemiringAction Gal(L/K) B :=
      IsIntegralClosure.MulSemiringAction A K L B
    let q := r.under B
    let p := r.under A
    letI : r.LiesOver q := ⟨rfl⟩
    letI : q.LiesOver p := ⟨r.under_under.symm⟩
    letI : Field (A ⧸ p) := Ideal.Quotient.field p
    letI : Field (B ⧸ q) := Ideal.Quotient.field q
    letI : Field (C ⧸ r) := Ideal.Quotient.field r
    letI : Algebra (B ⧸ q) (C ⧸ r) := Ideal.Quotient.algebraOfLiesOver r q
    letI : Algebra (A ⧸ p) (B ⧸ q) := Ideal.Quotient.algebraOfLiesOver q p
    letI : Algebra (A ⧸ p) (C ⧸ r) := Ideal.Quotient.algebraOfLiesOver r p
    let res : Gal(M/K) →* Gal(L/K) := AlgEquiv.restrictNormalHom L
    let D' := MulAction.stabilizer Gal(M/K) r
    let D := MulAction.stabilizer Gal(L/K) q
    let e' := r.ramificationIdx A
    let e := q.ramificationIdx A
    ∃ (resD : D' →* D)
      (resI : r.inertia Gal(M/K) →* q.inertia Gal(L/K))
      (resP : wildInertiaGroup A K M r →*
        wildInertiaGroup A K L q),
      Function.Surjective resD ∧ Function.Surjective resI ∧ Function.Surjective resP ∧
      (∀ σ, ((resD σ : D) : Gal(L/K)) = res ((σ : D') : Gal(M/K))) ∧
      (∀ σ, (resI σ).1 = res σ.1) ∧
      (∀ σ, (resP σ).1.1 = res σ.1.1) ∧
      e ∣ e' ∧
      ∃ (residueRestriction : Gal((C ⧸ r)/(A ⧸ p)) →* Gal((B ⧸ q)/(A ⧸ p)))
        (rootRestriction : rootsOfUnity e' (C ⧸ r) →* rootsOfUnity e (B ⧸ q)),
        (∀ τ b, algebraMap (B ⧸ q) (C ⧸ r) (residueRestriction τ b) =
          τ (algebraMap (B ⧸ q) (C ⧸ r) b)) ∧
        (∀ ζ, algebraMap (B ⧸ q) (C ⧸ r) (rootRestriction ζ).1.1 =
          (ζ ^ (e' / e)).1.1) ∧
        (∀ σ b, algebraMap (B ⧸ q) (C ⧸ r)
            (Ideal.Quotient.mk q ((resD σ).1 • b)) =
          Ideal.Quotient.mk r (σ.1 • fBC b)) ∧
        ∀ σ, rootRestriction (inertiaCharacter A K M r σ) =
          inertiaCharacter A K L q (resI σ)
```

## Tag 0BU8, a remark

[Tag 0BU8](https://stacks.math.columbia.edu/tag/0BU8) in the Stacks Project.

**`IsDiscreteValuationRing.canonicalInertiaCharacter`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Inertia/GaloisTower.lean, line 486](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DiscreteValuationRing/Inertia/GaloisTower.lean#L486).

> **Stacks Project, Tag 0BU8.** The canonical inertia character, obtained by raising the
> ordinary inertia character to the residue-characteristic-primary part of the ramification
> index.

```lean
noncomputable def canonicalInertiaCharacter :
    P.inertia Gal(L/K) →*
      rootsOfUnity (tameRamificationIndex A L P) (integralClosure A L ⧸ P)
```

**`IsDiscreteValuationRing.canonicalInertiaCharacter_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Inertia/GaloisTower.lean, line 518](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DiscreteValuationRing/Inertia/GaloisTower.lean#L518). References: SGA 7 I (0.3), “finite Galois case”.

> **Stacks Project, Tag 0BU8.** The scaled inertia character identifies tame inertia with the
> roots of unity of order `|I_t|`.  Its order is the prime-to-residue-characteristic part of the
> ramification index, it is equivariant under the decomposition group, and these canonical
> characters form the stated power-map square in every finite Galois tower.

```lean
theorem canonicalInertiaCharacter_spec :
    let B := integralClosure A L
    letI := IsIntegralClosure.MulSemiringAction A K L B
    let D := MulAction.stabilizer Gal(L/K) P
    let I := P.inertia Gal(L/K)
    let e := P.ramificationIdx A
    let p := ringChar (IsLocalRing.ResidueField A)
    let q := wildRamificationFactor A L P
    let n := tameRamificationIndex A L P
    let conjugate : D → I → I := fun τ σ ↦
      ⟨(τ : Gal(L/K)) * (σ : Gal(L/K)) * (τ : Gal(L/K))⁻¹, by
        rw [Ideal.mem_inertia]
        intro x
        have hσ := (Ideal.mem_inertia.mp σ.property) ((τ : Gal(L/K))⁻¹ • x)
        have hτ := Ideal.smul_mem_pointwise_smul (τ : Gal(L/K)) _ P hσ
        rw [τ.property] at hτ
        simpa only [mul_smul, smul_sub, smul_inv_smul] using hτ⟩
    e = q * n ∧
    (p = 0 → q = 1) ∧
    (0 < p → ∃ a : ℕ, q = p ^ a) ∧
    rootsOfUnity e (B ⧸ P) = rootsOfUnity n (B ⧸ P) ∧
    Nat.card (tameInertiaGroup A K L P) = n ∧
    ∃ θcan : tameInertiaGroup A K L P ≃* rootsOfUnity n (B ⧸ P),
      (∀ σ : I, θcan (tameInertiaMap A K L P σ) =
        canonicalInertiaCharacter A K L P σ) ∧
      (∀ (τ : D) (σ : I),
        canonicalInertiaCharacter A K L P (conjugate τ σ) =
          (Ideal.quotientEquiv P P
            ((MulSemiringAction.toRingEquiv Gal(L/K) B) (τ : Gal(L/K)))
            τ.property.symm).toMulEquiv.restrictRootsOfUnity n
              (canonicalInertiaCharacter A K L P σ)) ∧
      ∀ (M : Type*) [Field M] [Algebra K M] [FiniteDimensional K M]
        [IsGalois K M] [Algebra L M] [IsScalarTower K L M]
        [Algebra A M] [IsScalarTower A K M] [IsScalarTower A L M]
        (r : Ideal (integralClosure A M)) [r.IsMaximal],
        let C := integralClosure A M
        let fBC : B →ₐ[A] C := (IsScalarTower.toAlgHom A L M).mapIntegralClosure
        letI : Algebra B C := fBC.toRingHom.toAlgebra
        letI : IsScalarTower A B C :=
          IsScalarTower.of_algebraMap_eq fun x ↦ (fBC.commutes x).symm
        letI : Algebra.IsIntegral B C :=
          ⟨fun x ↦ IsIntegral.tower_top (IsIntegralClosure.isIntegral A M x)⟩
        letI : MulSemiringAction Gal(M/K) C :=
          IsIntegralClosure.MulSemiringAction A K M C
        let Q := r.under B
        let pA := r.under A
        letI : r.LiesOver Q := ⟨rfl⟩
        letI : Q.LiesOver pA := ⟨r.under_under.symm⟩
        letI : Field (A ⧸ pA) := Ideal.Quotient.field pA
        letI : Field (B ⧸ Q) := Ideal.Quotient.field Q
        letI : Field (C ⧸ r) := Ideal.Quotient.field r
        letI : Algebra (B ⧸ Q) (C ⧸ r) := Ideal.Quotient.algebraOfLiesOver r Q
        let _e' := r.ramificationIdx A
        let n' := tameRamificationIndex A M r
        let n := tameRamificationIndex A L Q
        let res : Gal(M/K) →* Gal(L/K) := AlgEquiv.restrictNormalHom L
        ∃ (resI : r.inertia Gal(M/K) →* Q.inertia Gal(L/K))
          (rootRestriction : rootsOfUnity n' (C ⧸ r) →* rootsOfUnity n (B ⧸ Q)),
          (∀ σ, (resI σ).1 = res σ.1) ∧
          n ∣ n' ∧
          (∀ ζ, algebraMap (B ⧸ Q) (C ⧸ r) (rootRestriction ζ).1.1 =
            (ζ ^ (n' / n)).1.1) ∧
          ∀ σ, rootRestriction (canonicalInertiaCharacter A K M r σ) =
            canonicalInertiaCharacter A K L Q (resI σ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.114, Tag 09E3](https://stacks.math.columbia.edu/tag/09E3)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
