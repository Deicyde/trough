---
declaration: section
origin: cited
lean: HenselianPair, etaleBaseChange_isEquivalence_and_henselianRing_of_le_nilradical, etaleBaseChange_isEquivalence_and_henselianPair_of_le_nilradical, henselianRing_ker_limit_π_of_surjective_of_ker_le_nilradical, IsAdicComplete.henselianRing, exists_integralClosure_quotient_prod_and_awayMap_bijective, eq_of_isRoot_of_sub_one_mem, henselianPair_tfae_exists
statement: formalized
proof: formalized
---

# 15.11 Henselian pairs

Section 15.11 of the Stacks Project, [Tag 09XD](https://stacks.math.columbia.edu/tag/09XD). 21 tags here are carried by 22 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09XE, a definition

[Tag 09XE](https://stacks.math.columbia.edu/tag/09XE) in the Stacks Project.

**`HenselianPair`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair.lean, line 33](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Pair.lean#L33). References: EGA IV (18.5.8); SGA 4 VIII (4.1); SGA 4 XII (6.13).

> A pair `(A, I)` is henselian if `I` lies in the Jacobson radical of `A` and every
> factorization modulo `I` of a monic polynomial into coprime monic factors lifts to `A`.

```lean
def HenselianPair (A : Type*) [CommRing A] (I : Ideal A) : Prop
```

## Tag 0ALI, a lemma

[Tag 0ALI](https://stacks.math.columbia.edu/tag/0ALI) in the Stacks Project.

**`etaleBaseChange_isEquivalence_and_henselianRing_of_le_nilradical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair/Nilpotent.lean, line 243](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Pair/Nilpotent.lean#L243). References: EGA IV (18.1.2), “affine case”; SGA 1 IX (1.7), “affine case”; SGA 1 IX (4.10), “affine, nilpotent ideal”.

> **Stacks 0ALI.** If every element of `I` is nilpotent, reduction modulo `I` induces an
> equivalence from étale `A`-algebras to étale `(A ⧸ I)`-algebras, and `(A, I)` is a henselian
> pair.

```lean
theorem etaleBaseChange_isEquivalence_and_henselianRing_of_le_nilradical {A : Type u} [CommRing A]
  (I : Ideal A)
    (hI : I ≤ nilradical A) :
    (etaleBaseChange I).IsEquivalence ∧ HenselianRing A I
```

**`etaleBaseChange_isEquivalence_and_henselianPair_of_le_nilradical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair/NilpotentFactorization.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Pair/NilpotentFactorization.lean#L96). The attribute's comment: “henselianness in the monic-factorization sense of Definition 09XE”.

> **Stacks 0ALI.** If every element of `I` is nilpotent, reduction modulo `I` induces an
> equivalence from étale `A`-algebras to étale `(A ⧸ I)`-algebras, and `(A, I)` is a henselian pair
> in the sense that coprime monic factorizations modulo `I` lift to `A`.

```lean
theorem etaleBaseChange_isEquivalence_and_henselianPair_of_le_nilradical
    {A : Type u} [CommRing A] (I : Ideal A) (hI : I ≤ nilradical A) :
    (etaleBaseChange I).IsEquivalence ∧ HenselianPair A I
```

## Tag 0CT7, a lemma

[Tag 0CT7](https://stacks.math.columbia.edu/tag/0CT7) in the Stacks Project.

**`henselianRing_ker_limit_π_of_surjective_of_ker_le_nilradical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair/Nilpotent.lean, line 505](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Pair/Nilpotent.lean#L505).

> **Stacks 0CT7.** Let `A` be the inverse limit of a sequence of commutative rings whose
> transition maps are surjective with locally nilpotent kernels. Then the pair consisting of `A`
> and the kernel of any limit projection `A → Aₙ` is henselian.

```lean
theorem henselianRing_ker_limit_π_of_surjective_of_ker_le_nilradical
    (F : ℕᵒᵖ ⥤ CommRingCat.{u}) (c : Cone F) (hc : IsLimit c)
    (hF : ∀ n : ℕ,
      Function.Surjective (F.map (homOfLE (Nat.le_succ n)).op).hom ∧
        RingHom.ker (F.map (homOfLE (Nat.le_succ n)).op).hom ≤
          nilradical (F.obj (.op (n + 1)))) (n : ℕ) :
    HenselianRing c.pt (RingHom.ker (c.π.app (.op n)).hom)
```

## Tag 0ALJ, a lemma

[Tag 0ALJ](https://stacks.math.columbia.edu/tag/0ALJ) in the Stacks Project.

Declarations registered for the tag:

- [`IsAdicComplete.henselianRing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsAdicComplete.henselianRing#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Henselian/Pair/Nilpotent.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Pair/Nilpotent.lean#L50) (StacksFrontier): “An `I`-adically complete ring is henselian at `I`; this is Mathlib's instance.”. References: EGA IV (18.5.14), “more general”; EGA IV (18.5.16), “more general”; SGA 3 X (4.0), “Recall 4.0”.

## Tag 09XH, a lemma

[Tag 09XH](https://stacks.math.columbia.edu/tag/09XH) in the Stacks Project.

**`exists_integralClosure_quotient_prod_and_awayMap_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair/Criteria/IntegralClosureSplitting.lean, line 601](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Pair/Criteria/IntegralClosureSplitting.lean#L601).

> Let `A → B` be a finite type map, let `I ⊆ A`, and suppose that `B / IB` is a product
> `C₁ × C₂` for which the canonical map `A / I → C₁` is finite. If `B'` is the
> integral closure of `A` in `B`, then `B' / IB'` decomposes as `C₁ × C₂'` compatibly
> with `B / IB`. Moreover, there is a `g ∈ B'` whose class is `(1, 0)` and for which the
> canonical map `B'_g → B_g` is an isomorphism.

```lean
theorem exists_integralClosure_quotient_prod_and_awayMap_bijective
    {A : Type u} [CommRing A] (I : Ideal A)
    {B : Type v} [CommRing B] [Algebra A B] [Algebra.FiniteType A B]
    {C₁ : Type w} [CommRing C₁] {C₂ : Type x} [CommRing C₂]
    (e : (B ⧸ I.map (algebraMap A B)) ≃+* C₁ × C₂)
    (hfinite : ((RingHom.fst C₁ C₂).comp (e.toRingHom.comp
      (Ideal.quotientMap (I.map (algebraMap A B)) (algebraMap A B)
        Ideal.le_comap_map))).Finite) :
    ∃ (C₂' : Type v) (_ : CommRing C₂')
      (e' : ((integralClosure A B) ⧸
        I.map (algebraMap A (integralClosure A B))) ≃+* C₁ × C₂')
      (f₂ : C₂' →+* C₂),
      (∀ z,
        e (Ideal.quotientMap (I.map (algebraMap A B))
          ((integralClosure A B).val : integralClosure A B →+* B) (by
            rw [Ideal.map_le_iff_le_comap]
            intro a ha
            simpa using Ideal.mem_map_of_mem (algebraMap A B) ha) z) =
          ((e' z).1, f₂ (e' z).2)) ∧
      ∃ g : integralClosure A B,
        e' (Ideal.Quotient.mk (I.map (algebraMap A (integralClosure A B))) g) = (1, 0) ∧
          Function.Bijective (Localization.awayMapₐ (integralClosure A B).val g)
```

## Tag 09XI, a lemma

[Tag 09XI](https://stacks.math.columbia.edu/tag/09XI) in the Stacks Project.

**`eq_of_isRoot_of_sub_one_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair/Criteria/Characterizations.lean, line 569](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Pair/Criteria/Characterizations.lean#L569). The attribute's comment: “moreover: the root in (5) is unique”.

> Gabber's polynomial `f = X ^ n (X - 1) + ∑ aᵢ X ^ i` with `aᵢ ∈ I` has at most one root in
> `1 + I` when `I` is contained in the Jacobson radical: its derivative at such a root lies in
> `1 + I`, so the difference of two roots is killed by a unit.

```lean
public theorem eq_of_isRoot_of_sub_one_mem {A : Type u} [CommRing A] {I : Ideal A}
    (hI : IsContainedInJacobson I) (f : A[X]) (n : ℕ) (a : Fin (n + 1) → I)
    (hform : f = X ^ n * (X - 1) + ∑ i : Fin (n + 1), C (a i : A) * X ^ (i : ℕ))
    {α β : A} (hα : α - 1 ∈ I ∧ f.IsRoot α) (hβ : β - 1 ∈ I ∧ f.IsRoot β) : β = α
```

**`henselianPair_tfae_exists`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair/Criteria/Characterizations.lean, line 622](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Pair/Criteria/Characterizations.lean#L622).

> The five characterizations of a henselian pair, in the order of the source: lifting maps from
> étale algebras, bijectivity on idempotents for finite or integral algebras, and Gabber's criterion
> that `I` lies in the Jacobson radical and every polynomial `X ^ n (X - 1) + ∑ aᵢ X ^ i` with
> `aᵢ ∈ I` and `n ≥ 1` has a root in `1 + I`. That root is unique by `eq_of_isRoot_of_sub_one_mem`.

```lean
public theorem henselianPair_tfae_exists (A : Type u) [CommRing A] (I : Ideal A) :
    List.TFAE
      [HenselianPair A I,
        ∀ (A' : Type (max u v)) [CommRing A'] [Algebra A A'] [Algebra.Etale A A'],
          ∀ σ : A' →ₐ[A] A ⧸ I,
            ∃ τ : A' →ₐ[A] A, (Ideal.Quotient.mkₐ A I).comp τ = σ,
        ∀ (B : Type (max u v)) [CommRing B] [Algebra A B] [Module.Finite A B],
          InducesBijectionOnIdempotents (I.map (algebraMap A B)),
        ∀ (B : Type (max u v)) [CommRing B] [Algebra A B] [Algebra.IsIntegral A B],
          InducesBijectionOnIdempotents (I.map (algebraMap A B)),
        IsContainedInJacobson I ∧
          ∀ (f : A[X]), f.Monic →
            ∀ (n : ℕ), 1 ≤ n →
              ∀ a : Fin (n + 1) → I,
                f = X ^ n * (X - 1) +
                    ∑ i : Fin (n + 1), C (a i : A) * X ^ (i : ℕ) →
                  ∃ α : A, α - 1 ∈ I ∧ f.IsRoot α]
```

## Tag 0EM1, an equation

[Tag 0EM1](https://stacks.math.columbia.edu/tag/0EM1) in the Stacks Project.

**`exists_quotient_algEquiv_prod_of_etale_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair/Criteria/ProductDecomposition.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Pair/Criteria/ProductDecomposition.lean#L168).

> Let `A'` be an étale `A`-algebra and let `A' → A/I` be an `A`-algebra map. Then `A'/IA'` is
> isomorphic, as an `A/I`-algebra, to a product `A/I × C`. Under this isomorphism, the map to the
> first factor is the map induced by the given section.

```lean
theorem exists_quotient_algEquiv_prod_of_etale_section
    (A : Type u) [CommRing A] (A' : Type v) [CommRing A'] [Algebra A A']
    [Algebra.Etale A A'] (I : Ideal A) (retraction : A' →ₐ[A] A ⧸ I) :
    ∃ (C : Type v) (_ : CommRing C) (_ : Algebra (A ⧸ I) C)
      (e : (A' ⧸ I.map (algebraMap A A')) ≃ₐ[A ⧸ I] ((A ⧸ I) × C)),
      ∀ x : A', (e (Ideal.Quotient.mk (I.map (algebraMap A A')) x)).1 = retraction x
```

## Tag 0EM2, an equation

[Tag 0EM2](https://stacks.math.columbia.edu/tag/0EM2) in the Stacks Project.

**`exists_integral_factor_decomposition_of_gabber_root_condition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair/Criteria/ProductDecomposition.lean, line 483](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Pair/Criteria/ProductDecomposition.lean#L483).

> Under Gabber's Jacobson-radical and root-lifting conditions, a section modulo `I` of an
> étale `A`-algebra comes from a product decomposition whose first factor is integral over `A`
> and has reduction `A ⧸ I`.

```lean
theorem exists_integral_factor_decomposition_of_gabber_root_condition
    (A : Type u) [CommRing A] (I : Ideal A)
    (hI : I ≤ Ideal.jacobson (⊥ : Ideal A))
    (hroot : ∀ (f : A[X]), f.Monic →
      ∀ (n : ℕ), 1 ≤ n →
        ∀ a : Fin (n + 1) → I,
          f = X ^ n * (X - 1) + ∑ i : Fin (n + 1), C (a i : A) * X ^ (i : ℕ) →
            ∃ α : A, α - 1 ∈ I ∧ f.IsRoot α)
    (A' : Type (max u v)) [CommRing A'] [Algebra A A'] [Algebra.Etale A A']
    (σ : A' →ₐ[A] A ⧸ I) :
    ∃ (A₁ A₂ : Type (max u v))
      (_ : CommRing A₁) (_ : CommRing A₂)
      (_ : Algebra A A₁) (_ : Algebra A A₂)
      (e : A' ≃ₐ[A] A₁ × A₂) (q : A₁ →ₐ[A] A ⧸ I),
      Algebra.IsIntegral A A₁ ∧
        Function.Surjective q ∧
        RingHom.ker q = I.map (algebraMap A A₁) ∧
        q.comp ((AlgHom.fst A A₁ A₂).comp e.toAlgHom) = σ
```

## Tag 0EM3, an equation

[Tag 0EM3](https://stacks.math.columbia.edu/tag/0EM3) in the Stacks Project.

**`exists_integralClosure_quotient_algEquiv_prod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair/Criteria/ProductDecomposition.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Pair/Criteria/ProductDecomposition.lean#L96).

> If the reduction of a finite type `A`-algebra `B` modulo `I` decomposes as `(A ⧸ I) × C`, then
> the reduction of the integral closure of `A` in `B` has a compatible decomposition `(A ⧸ I) × C'`.
> Compatibility is expressed using the canonical map induced by the inclusion
> `integralClosure A B → B`.

```lean
theorem exists_integralClosure_quotient_algEquiv_prod
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [Algebra A B]
    (I : Ideal A) [Algebra.FiniteType A B]
    (C : Type w) [CommRing C] [Algebra (A ⧸ I) C]
    (e : (B ⧸ I.map (algebraMap A B)) ≃ₐ[A ⧸ I] ((A ⧸ I) × C)) :
    let B' := integralClosure A B
    let IB' := I.map (algebraMap A B')
    let IB := I.map (algebraMap A B)
    let toReduction : (B' ⧸ IB') →+* (B ⧸ IB) :=
      Ideal.quotientMap IB (B'.val : B' →+* B) (by
        rw [Ideal.map_le_iff_le_comap]
        intro a ha
        change ((B'.val : B' →+* B) (algebraMap A B' a)) ∈ IB
        change algebraMap A B a ∈ IB
        exact Ideal.mem_map_of_mem (algebraMap A B) ha)
    ∃ (C' : Type (max u v)) (hC' : CommRing C'),
      let _ := hC'
      ∃ hAlg : Algebra (A ⧸ I) C',
        let _ := hAlg
        ∃ (e' : (B' ⧸ IB') ≃ₐ[A ⧸ I] ((A ⧸ I) × C'))
          (k : C' →ₐ[A ⧸ I] C),
          ∀ x, e (toReduction x) = ((e' x).1, k (e' x).2)
```

## Tag 0EM4, an equation

[Tag 0EM4](https://stacks.math.columbia.edu/tag/0EM4) in the Stacks Project.

**`exists_integralClosure_algEquiv_prod_lift_of_gabber_root_condition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair/Criteria/IntegralClosureLift.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Pair/Criteria/IntegralClosureLift.lean#L194). The attribute's comment: “the decomposition `B' ⧸ IB' ≅ A ⧸ I × C'` of the integral closure lifts to `B' ≅ B'₁ × B'₂` under Gabber's criterion; stated for any `A`-algebra `A'` and any decomposition”.

> Assume Gabber's criterion for `(A, I)`: `I` lies in the Jacobson radical of `A` and every
> monic `X ^ n (X - 1) + ∑ aᵢ X ^ i` with `aᵢ ∈ I` and `n ≥ 1` has a root in `1 + I`. Let `B'` be
> the integral closure of `A` in an `A`-algebra `A'`. Then every decomposition
> `B' ⧸ IB' ≅ A ⧸ I × C'` of `A ⧸ I`-algebras lifts to a decomposition `B' ≅ B'₁ × B'₂` of
> `A`-algebras: there are surjections `B'₁ → A ⧸ I` and `B'₂ → C'` with kernels `IB'₁` and `IB'₂`
> through which the reduction of `B'` is the given decomposition. In the source `A'` is étale over
> `A` and the decomposition is the one of Tag 0EM3; the lift holds for any `A'` and any
> decomposition.

```lean
theorem exists_integralClosure_algEquiv_prod_lift_of_gabber_root_condition
    (A : Type u) [CommRing A] (I : Ideal A)
    (hI : I ≤ Ideal.jacobson (⊥ : Ideal A))
    (hroot : ∀ (f : A[X]), f.Monic →
      ∀ (n : ℕ), 1 ≤ n →
        ∀ a : Fin (n + 1) → I,
          f = X ^ n * (X - 1) + ∑ i : Fin (n + 1), C (a i : A) * X ^ (i : ℕ) →
            ∃ α : A, α - 1 ∈ I ∧ f.IsRoot α)
    (A' : Type (max u v)) [CommRing A'] [Algebra A A']
    (C' : Type w) [CommRing C'] [Algebra (A ⧸ I) C']
    (e' : (integralClosure A A' ⧸ I.map (algebraMap A (integralClosure A A'))) ≃ₐ[A ⧸ I]
      ((A ⧸ I) × C')) :
    ∃ (B₁ B₂ : Type (max u v)) (_ : CommRing B₁) (_ : CommRing B₂) (_ : Algebra A B₁)
      (_ : Algebra A B₂) (E : integralClosure A A' ≃ₐ[A] B₁ × B₂) (ρ₁ : B₁ →+* A ⧸ I)
      (ρ₂ : B₂ →+* C'),
      Function.Surjective ρ₁ ∧ RingHom.ker ρ₁ = I.map (algebraMap A B₁) ∧
      Function.Surjective ρ₂ ∧ RingHom.ker ρ₂ = I.map (algebraMap A B₂) ∧
      ∀ x : integralClosure A A',
        e' (Ideal.Quotient.mk (I.map (algebraMap A (integralClosure A A'))) x) =
          (ρ₁ (E x).1, ρ₂ (E x).2)
```

## Tag 0EM5, an equation

[Tag 0EM5](https://stacks.math.columbia.edu/tag/0EM5) in the Stacks Project.

**`prodQuotientOfIsIdempotentElem_apply_idempotent_mod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair/Criteria/ProductDecomposition.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Pair/Criteria/ProductDecomposition.lean#L56).

> The canonical `A / I`-algebra product decomposition of `B / IB` associated to an idempotent is
> induced by the two quotient maps and sends that idempotent to `(1, 0)`.

```lean
theorem prodQuotientOfIsIdempotentElem_apply_idempotent_mod
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [Algebra A B]
    (I : Ideal A) (b : B)
    (hb : IsIdempotentElem (Ideal.Quotient.mk (I.map (algebraMap A B)) b)) :
    let Q := B ⧸ I.map (algebraMap A B)
    let bbar : Q := Ideal.Quotient.mk (I.map (algebraMap A B)) b
    let e : Q ≃ₐ[A ⧸ I]
        (Q ⧸ Ideal.span {1 - bbar}) × (Q ⧸ Ideal.span {bbar}) :=
      AlgEquiv.prodQuotientOfIsIdempotentElem (A ⧸ I)
        (e := 1 - bbar) (f := bbar) hb.one_sub hb (by simp) hb.one_sub_mul_self
    e bbar = (1, 0)
```

## Tag 09XJ, a lemma

[Tag 09XJ](https://stacks.math.columbia.edu/tag/09XJ) in the Stacks Project.

**`henselianPair_iff_of_zeroLocus_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair/Operations.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Pair/Operations.lean#L117).

> Two ideals with the same vanishing locus define henselian pairs simultaneously.

```lean
theorem henselianPair_iff_of_zeroLocus_eq
    {A : Type u} [CommRing A] (I J : Ideal A)
    (hIJ : PrimeSpectrum.zeroLocus (I : Set A) = PrimeSpectrum.zeroLocus (J : Set A)) :
    HenselianPair A I ↔ HenselianPair A J
```

## Tag 09XK, a lemma

[Tag 09XK](https://stacks.math.columbia.edu/tag/09XK) in the Stacks Project.

**`henselianPair_map_of_isIntegral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair/Operations.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Pair/Operations.lean#L52).

> An integral extension of a henselian pair is henselian along the extended ideal.

```lean
theorem henselianPair_map_of_isIntegral {A : Type u} {B : Type v} [CommRing A]
    [CommRing B] [Algebra A B] [Algebra.IsIntegral A B] (I : Ideal A)
    (hI : HenselianPair A I) :
    HenselianPair B (I.map (algebraMap A B))
```

## Tag 0DYD, a lemma

[Tag 0DYD](https://stacks.math.columbia.edu/tag/0DYD) in the Stacks Project.

**`henselianPair_iff_of_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair/Operations.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Pair/Operations.lean#L210).

> For nested ideals `I ⊆ J`, the pair `(A, J)` is henselian if and only if `(A, I)` and
> the induced pair `(A / I, J / I)` are henselian.

```lean
theorem henselianPair_iff_of_le {A : Type w} [CommRing A] {I J : Ideal A} (hIJ : I ≤ J) :
    (HenselianPair A I ∧
      HenselianPair (A ⧸ I) (J.map (Ideal.Quotient.mk I))) ↔
      HenselianPair A J
```

## Tag 0G1R, a lemma

[Tag 0G1R](https://stacks.math.columbia.edu/tag/0G1R) in the Stacks Project.

**`henselianPair_sup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair/Operations.lean, line 243](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Pair/Operations.lean#L243).

> The sum of two ideals defining henselian pairs also defines a henselian pair.

```lean
theorem henselianPair_sup {A : Type u} [CommRing A] {I J : Ideal A}
    (hI : HenselianPair A I) (hJ : HenselianPair A J) :
    HenselianPair A (I ⊔ J)
```

## Tag 0ATD, a lemma

[Tag 0ATD](https://stacks.math.columbia.edu/tag/0ATD) in the Stacks Project.

**`henselianPair_pi_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair/Limits.lean, line 835](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Pair/Limits.lean#L835).

> A product of pairs is henselian if and only if each component pair is henselian.

```lean
theorem henselianPair_pi_iff {J : Type u} (A : J → Type v) [∀ j, CommRing (A j)]
    (I : ∀ j, Ideal (A j)) :
    HenselianPair ((j : J) → A j) (Ideal.pi I) ↔
      ∀ j, HenselianPair (A j) (I j)
```

## Tag 0EM6, a lemma

[Tag 0EM6](https://stacks.math.columbia.edu/tag/0EM6) in the Stacks Project.

**`henselianPair_limit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair/Limits.lean, line 988](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Pair/Limits.lean#L988).

> A limit of henselian pairs is a henselian pair.

```lean
theorem henselianPair_limit
    {J : Type v} [SmallCategory J]
    (F : J ⥤ CommRingCat.{u}) (I : ∀ j, Ideal (F.obj j))
    (hI : ∀ ⦃j k⦄ (f : j ⟶ k), Ideal.map (F.map f).hom (I j) ≤ I k)
    (c : Cone F) (hc : IsLimit c)
    (h : ∀ j, HenselianPair (F.obj j) (I j)) :
    HenselianPair c.pt
      (⨅ j, Ideal.comap (c.π.app j).hom (I j))
```

## Tag 0FWT, a lemma

[Tag 0FWT](https://stacks.math.columbia.edu/tag/0FWT) in the Stacks Project.

**`henselianPair_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair/Limits.lean, line 320](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Pair/Limits.lean#L320).

> A filtered colimit of Henselian pairs is a Henselian pair.

```lean
theorem henselianPair_colimit
    {J : Type v} [SmallCategory J] [IsFiltered J]
    (F : J ⥤ CommRingCat.{max u v}) (I : ∀ j, Ideal (F.obj j))
    (hI : ∀ ⦃j k⦄ (f : j ⟶ k), Ideal.map (F.map f).hom (I j) ≤ I k)
    (c : Cocone F) (hc : IsColimit c)
    (hH : ∀ j, HenselianPair (F.obj j) (I j)) :
    HenselianPair c.pt (⨆ j, Ideal.map (c.ι.app j).hom (I j))
```

## Tag 0FWU, an example

[Tag 0FWU](https://stacks.math.columbia.edu/tag/0FWU) in the Stacks Project.

**`padicInt_tensorProduct_not_henselian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair/Limits.lean, line 702](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Pair/Limits.lean#L702).

> For an odd prime `p`, the coproduct over `ℤ` of two copies of the Henselian pair
> `(ℤ_[p], (p))` is not Henselian. Its residue ring is `ZMod p`, and an explicit nontrivial
> idempotent, built from a square root of an integer which is not a rational square, witnesses that
> its spectrum is disconnected.

```lean
theorem padicInt_tensorProduct_not_henselian (p : ℕ) [Fact p.Prime] (hp : Odd p) :
    let R := ℤ_[p]
    let A := R ⊗[ℤ] R
    let I : Ideal A := Ideal.span {algebraMap ℤ A (p : ℤ)}
    HenselianRing R (Ideal.span {(p : R)}) ∧
      Ideal.map (Algebra.TensorProduct.includeLeft : R →ₐ[ℤ] A).toRingHom
        (Ideal.span {(p : R)}) = I ∧
      Ideal.map (Algebra.TensorProduct.includeRight : R →ₐ[ℤ] A).toRingHom
        (Ideal.span {(p : R)}) = I ∧
      Nonempty ((A ⧸ I) ≃+* ZMod p) ∧
      (HenselianRing A I → IsLocalRing A) ∧
      ¬ IsLocalRing A ∧
      ¬ HenselianRing A I ∧
      ¬ ConnectedSpace (PrimeSpectrum A) ∧
      ∃ t u v w : R,
        t = algebraMap ℤ R (if p = 3 then 7 else 1 + (p : ℤ)) ∧
        ¬ IsSquare ((if p = 3 then (7 : ℤ) else 1 + (p : ℤ)) : ℚ) ∧
        u ^ 2 = t ∧ 2 * v = 1 ∧ t * w = 1 ∧
        let e : A := (v ⊗ₜ[ℤ] (1 : R)) *
          ((1 : R) ⊗ₜ[ℤ] (1 : R) - (w * u) ⊗ₜ[ℤ] u)
        IsIdempotentElem e ∧ e ≠ 0 ∧ e ≠ 1
```

## Tag 0G1S, a lemma

[Tag 0G1S](https://stacks.math.columbia.edu/tag/0G1S) in the Stacks Project.

**`exists_greatest_henselianPair`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair/Limits.lean, line 1091](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Pair/Limits.lean#L1091).

> Every commutative ring has a largest ideal with respect to which it forms a henselian pair.

```lean
theorem exists_greatest_henselianPair (A : Type u) [CommRing A] :
    ∃ I : Ideal A, HenselianPair A I ∧
      ∀ J : Ideal A, HenselianPair A J → J ≤ I
```

## Tag 09Y6, a lemma

[Tag 09Y6](https://stacks.math.columbia.edu/tag/09Y6) in the Stacks Project.

**`isConnected_zeroLocus_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair/Operations.lean, line 270](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Pair/Operations.lean#L270).

> For a henselian pair `(A, I)` and a prime ideal `p` of `A`, the closed subset
> `V(p + I)` of `Spec(A)` is connected.

```lean
theorem isConnected_zeroLocus_add {A : Type u} [CommRing A] (I p : Ideal A)
    (hI : HenselianPair A I) (hp : p.IsPrime) :
    IsConnected (zeroLocus ((p + I : Ideal A) : Set A) : Set (PrimeSpectrum A))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.11, Tag 09XD](https://stacks.math.columbia.edu/tag/09XD)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
