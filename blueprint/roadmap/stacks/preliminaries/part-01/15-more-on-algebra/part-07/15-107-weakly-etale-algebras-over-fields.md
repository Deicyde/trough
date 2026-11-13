---
declaration: section
origin: cited
lean: structure_of_weaklyEtale_over_field, exists_greatest_weaklyEtale_subalgebra, exists_maximalWeaklyEtaleSubalgebraFunctor, maximalWeaklyEtaleSubalgebra_baseChange
statement: formalized
proof: formalized
---

# 15.107 Weakly étale algebras over fields

Section 15.107 of the Stacks Project, [Tag 0CKQ](https://stacks.math.columbia.edu/tag/0CKQ). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CKR, a lemma

[Tag 0CKR](https://stacks.math.columbia.edu/tag/0CKR) in the Stacks Project.

**`structure_of_weaklyEtale_over_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/WeaklyEtale/Field.lean, line 573](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/WeaklyEtale/Field.lean#L573). References: EGA IV (18.3.3), “partial”; SGA 1 IX (1.8), “decomposition direction”; SGA 4½ Arcata (2.1.2), “partial”; SGA 4½ Arcata (2.4.2), “more general”.

> A weakly étale algebra `B` over a field `K` is reduced and integral. Every finitely
> generated `K`-subalgebra is a finite product of finite separable extensions of `K`. Moreover,
> `B` is a field or the zero ring exactly when it has no nontrivial idempotents; if it is a field,
> then it is a separable algebraic extension. Subalgebras and quotient algebras of `B` are weakly
> étale over `K`, as is the tensor product of `B` with any weakly étale `K`-algebra.

```lean
theorem structure_of_weaklyEtale_over_field
    (K : Type u) (B : Type v) [Field K] [CommRing B] [Algebra K B]
    (hB : Algebra.WeaklyEtale K B) :
    IsReduced B ∧
      Algebra.IsIntegral K B ∧
      (∀ A : Subalgebra K B, A.FG →
        ∃ (ι : Type v) (_ : Finite ι) (L : ι → Type v) (_ : ∀ i, Field (L i))
          (_ : ∀ i, Algebra K (L i)) (_ : A ≃ₐ[K] ∀ i, L i),
          ∀ i, Module.Finite K (L i) ∧ Algebra.IsSeparable K (L i)) ∧
      (((Subsingleton B ∨ IsField B) ↔
          ∀ e : B, IsIdempotentElem e → e = 0 ∨ e = 1) ∧
        (IsField B → Algebra.IsSeparable K B ∧ Algebra.IsAlgebraic K B)) ∧
      ((∀ S : Subalgebra K B, Algebra.WeaklyEtale K S) ∧
        (∀ (Q : Type w) [CommRing Q] [Algebra K Q],
          (∃ f : B →ₐ[K] Q, Function.Surjective f) → Algebra.WeaklyEtale K Q)) ∧
      (∀ (B' : Type w) [CommRing B'] [Algebra K B'],
        Algebra.WeaklyEtale K B' → Algebra.WeaklyEtale K (B ⊗[K] B'))
```

## Tag 0CKS, a lemma

[Tag 0CKS](https://stacks.math.columbia.edu/tag/0CKS) in the Stacks Project.

**`exists_greatest_weaklyEtale_subalgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/WeaklyEtale/MaximalSubalgebra.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/WeaklyEtale/MaximalSubalgebra.lean#L136).

> An algebra over a field has a greatest weakly étale subalgebra.

```lean
theorem exists_greatest_weaklyEtale_subalgebra
    (K : Type u) (A : Type v) [Field K] [CommRing A] [Algebra K A] :
    ∃ Bmax : Subalgebra K A,
      Algebra.WeaklyEtale K Bmax ∧
        ∀ B : Subalgebra K A, Algebra.WeaklyEtale K B → B ≤ Bmax
```

## Tag 0CKT, a lemma

[Tag 0CKT](https://stacks.math.columbia.edu/tag/0CKT) in the Stacks Project.

**`exists_maximalWeaklyEtaleSubalgebraFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/WeaklyEtale/MaximalSubalgebra.lean, line 722](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/WeaklyEtale/MaximalSubalgebra.lean#L722).

> The maximal weakly étale subalgebra over a field is functorial and commutes with filtered
> colimits, reduction, and finite products. It pulls back along injective algebra maps, and over an
> algebra without nontrivial idempotents it is either the zero ring or a separable algebraic field
> extension.

```lean
theorem exists_maximalWeaklyEtaleSubalgebraFunctor
    (K : Type u) [Field K] :
    ∃ (Bmax : CommAlgCat.{v} K ⥤ CommAlgCat.{v} K)
      (ι : Bmax ⟶ 𝟭 (CommAlgCat.{v} K)),
      (∀ A, Function.Injective (ι.app A)) ∧
      (∀ A, Algebra.WeaklyEtale K (Bmax.obj A)) ∧
      (∀ (A : CommAlgCat.{v} K) (S : Subalgebra K A),
        Algebra.WeaklyEtale K S →
          ∃ f : CommAlgCat.of K S ⟶ Bmax.obj A,
            f ≫ ι.app A = CommAlgCat.ofHom S.val) ∧
      (∀ (A' A : CommAlgCat.{v} K) (f : A' ⟶ A), Function.Injective f →
        ∀ x : A',
          (∃ b : Bmax.obj A', ι.app A' b = x) ↔
            ∃ b : Bmax.obj A, ι.app A b = f x) ∧
      PreservesFilteredColimits Bmax ∧
      (∀ A : CommAlgCat.{v} K,
        IsIso (Bmax.map (CommAlgCat.ofHom (Ideal.Quotient.mkₐ K (nilradical A))))) ∧
      (∀ (J : Type v) [Finite J], PreservesLimitsOfShape (Discrete J) Bmax) ∧
      (∀ A : CommAlgCat.{v} K,
        (∀ e : A, IsIdempotentElem e → e = 0 ∨ e = 1) →
          Subsingleton A ∨
            (IsField (Bmax.obj A) ∧ Algebra.IsSeparable K (Bmax.obj A) ∧
              Algebra.IsAlgebraic K (Bmax.obj A)))
```

## Tag 0CKU, a lemma

[Tag 0CKU](https://stacks.math.columbia.edu/tag/0CKU) in the Stacks Project.

**`maximalWeaklyEtaleSubalgebra_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/WeaklyEtale/MaximalSubalgebra.lean, line 1079](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/WeaklyEtale/MaximalSubalgebra.lean#L1079).

> Extending the base field carries the maximal weakly étale subalgebra to the maximal
> weakly étale subalgebra of the scalar extension.

```lean
theorem maximalWeaklyEtaleSubalgebra_baseChange
    (K : Type u) (L : Type v) (A : Type w)
    [Field K] [Field L] [CommRing A] [Algebra K L] [Algebra K A]
    (B : Subalgebra K A) (hB : Algebra.WeaklyEtale K B)
    (hBmax : ∀ C : Subalgebra K A, Algebra.WeaklyEtale K C → C ≤ B) :
    let f : L ⊗[K] B →ₐ[K] L ⊗[K] A :=
      Algebra.TensorProduct.map (AlgHom.id K L) B.val
    Function.Injective f ∧
      Algebra.WeaklyEtale L (L ⊗[K] B) ∧
      ∀ C : Subalgebra L (L ⊗[K] A), Algebra.WeaklyEtale L C →
        ∀ x : C, ∃ y : L ⊗[K] B, f y = x
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.107, Tag 0CKQ](https://stacks.math.columbia.edu/tag/0CKQ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
