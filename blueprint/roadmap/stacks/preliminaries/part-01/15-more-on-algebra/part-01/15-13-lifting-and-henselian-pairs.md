---
declaration: section
origin: cited
lean: henselianPair_finiteProjective_quotient_bijective, isEquivalence_baseChange_quotient, exists_lift_of_smooth_of_henselianPair, finiteProjective_limit_of_finiteFlat_of_isBaseChange
statement: formalized
proof: formalized
---

# 15.13 Lifting and henselian pairs

Section 15.13 of the Stacks Project, [Tag 0D49](https://stacks.math.columbia.edu/tag/0D49). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0D4A, a lemma

[Tag 0D4A](https://stacks.math.columbia.edu/tag/0D4A) in the Stacks Project.

**`henselianPair_finiteProjective_quotient_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair/Lifting/Projective.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/Pair/Lifting/Projective.lean#L198).

> **Stacks 0D4A.** Reduction modulo the ideal of a henselian pair induces a bijection on
> isomorphism classes of finite projective modules. Concretely, every finite projective module
> over the quotient lifts, and two finite projective modules lift the same isomorphism class
> exactly when they were already isomorphic.

```lean
theorem henselianPair_finiteProjective_quotient_bijective
    {R : Type u} [CommRing R] (I : Ideal R) (hI : HenselianPair R I) :
    (∀ (Pbar : Type v) [AddCommGroup Pbar] [Module (R ⧸ I) Pbar]
        [Module.Finite (R ⧸ I) Pbar] [Module.Projective (R ⧸ I) Pbar],
      ∃ (P : Type (max u v)) (_ : AddCommGroup P) (_ : Module R P),
        Module.Finite R P ∧ Module.Projective R P ∧
          Nonempty ((P ⧸ (I • (⊤ : Submodule R P))) ≃ₗ[R ⧸ I] Pbar)) ∧
    (∀ (P₁ : Type v) [AddCommGroup P₁] [Module R P₁]
        [Module.Finite R P₁] [Module.Projective R P₁]
        (P₂ : Type w) [AddCommGroup P₂] [Module R P₂]
        [Module.Finite R P₂] [Module.Projective R P₂],
      Nonempty
          ((P₁ ⧸ (I • (⊤ : Submodule R P₁))) ≃ₗ[R ⧸ I]
            (P₂ ⧸ (I • (⊤ : Submodule R P₂)))) ↔
        Nonempty (P₁ ≃ₗ[R] P₂))
```

## Tag 09ZL, a lemma

[Tag 09ZL](https://stacks.math.columbia.edu/tag/09ZL) in the Stacks Project.

**`isEquivalence_baseChange_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair/FiniteEtale.lean, line 362](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/Pair/FiniteEtale.lean#L362). References: EGA IV (18.3.2); EGA IV (18.5.15); SGA 3 X (4.0), “ÉtCov(S)≃ÉtCov(S₀)”.

> For a henselian pair `(A, I)`, reduction modulo `I` is an equivalence between finite étale
> `A`-algebras and finite étale `A ⧸ I`-algebras.

```lean
theorem isEquivalence_baseChange_quotient
    (A : Type u) [CommRing A] (I : Ideal A) (h : HenselianPair A I) :
    (CommAlgCat.FiniteEtale.baseChange.{u, u, u} A (A ⧸ I)).IsEquivalence
```

## Tag 0H74, a lemma

[Tag 0H74](https://stacks.math.columbia.edu/tag/0H74) in the Stacks Project.

**`exists_lift_of_smooth_of_henselianPair`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair/Lifting/Algebra.lean, line 35](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/Pair/Lifting/Algebra.lean#L35).

> **Stacks 0H74.** Every map from a smooth algebra to the quotient of a henselian pair lifts
> to the original ring.

```lean
theorem exists_lift_of_smooth_of_henselianPair
    {R : Type u} {S : Type v} {A : Type w}
    [CommRing R] [CommRing S] [CommRing A] [Algebra R S] [Algebra R A]
    [Algebra.Smooth R S] (I : Ideal A) (hI : HenselianPair A I)
    (f : S →ₐ[R] A ⧸ I) :
    ∃ f' : S →ₐ[R] A, (Ideal.Quotient.mkₐ R I).comp f' = f
```

## Tag 0D4B, a lemma

[Tag 0D4B](https://stacks.math.columbia.edu/tag/0D4B) in the Stacks Project.

**`finiteProjective_limit_of_finiteFlat_of_isBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair/Lifting/Projective.lean, line 554](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/Pair/Lifting/Projective.lean#L554). References: EGA IV (18.3.2.1), “(ii)”.

> **Stacks 0D4B.** A compatible inverse system of finite flat modules over a surjective
> inverse system of rings with locally nilpotent transition kernels has finite projective inverse
> limit, provided its first term is finite projective. The limit commutes with base change to every
> ring in the system.

```lean
theorem finiteProjective_limit_of_finiteFlat_of_isBaseChange
    (A : ℕᵒᵖ ⥤ CommRingCat.{u}) (c : Cone A) (hc : IsLimit c)
    (M : ℕᵒᵖ ⥤ ModuleCat.{v} c.pt)
    (moduleStructure : ∀ n : ℕ, Module (A.obj (.op n)) (M.obj (.op n)))
    (hscalar : ∀ n : ℕ,
      letI := moduleStructure n
      letI : Algebra c.pt (A.obj (.op n)) := (c.π.app (.op n)).hom.toAlgebra
      IsScalarTower c.pt (A.obj (.op n)) (M.obj (.op n)))
    (d : ∀ n : ℕ,
      letI := moduleStructure (n + 1)
      letI := moduleStructure n
      ModuleCat.of (A.obj (.op (n + 1))) (M.obj (.op (n + 1))) ⟶
        (ModuleCat.restrictScalars (A.map (homOfLE (Nat.le_succ n)).op).hom).obj
          (ModuleCat.of (A.obj (.op n)) (M.obj (.op n))))
    (hd : ∀ (n : ℕ) (x : M.obj (.op (n + 1))),
      letI := moduleStructure (n + 1)
      letI := moduleStructure n
      d n x = M.map (homOfLE (Nat.le_succ n)).op x)
    (hA : ∀ n : ℕ,
      Function.Surjective (A.map (homOfLE (Nat.le_succ n)).op).hom ∧
        RingHom.ker (A.map (homOfLE (Nat.le_succ n)).op).hom ≤
          nilradical (A.obj (.op (n + 1))))
    (hfirst :
      letI := moduleStructure 0
      Module.Finite (A.obj (.op 0)) (M.obj (.op 0)) ∧
        Module.Projective (A.obj (.op 0)) (M.obj (.op 0)))
    (hflat : ∀ n : ℕ,
      letI := moduleStructure n
      Module.Finite (A.obj (.op n)) (M.obj (.op n)) ∧
        Module.Flat (A.obj (.op n)) (M.obj (.op n)))
    (hbaseChange : ∀ n : ℕ,
      letI := moduleStructure (n + 1)
      letI := moduleStructure n
      letI : Algebra (A.obj (.op (n + 1))) (A.obj (.op n)) :=
        (A.map (homOfLE (Nat.le_succ n)).op).hom.toAlgebra
      ∃ e : TensorProduct (A.obj (.op (n + 1))) (A.obj (.op n)) (M.obj (.op (n + 1)))
          ≃ₗ[A.obj (.op n)] M.obj (.op n),
        ∀ (a : A.obj (.op n)) (x : M.obj (.op (n + 1))),
          e (TensorProduct.tmul (A.obj (.op (n + 1))) a x) = a • d n x) :
    Module.Finite c.pt (limit M : ModuleCat.{v} c.pt) ∧
      Module.Projective c.pt (limit M : ModuleCat.{v} c.pt) ∧
      ∀ n : ℕ,
        letI := moduleStructure n
        letI : Algebra c.pt (A.obj (.op n)) := (c.π.app (.op n)).hom.toAlgebra
        ∃ e : TensorProduct c.pt (A.obj (.op n)) (limit M : ModuleCat.{v} c.pt)
            ≃ₗ[A.obj (.op n)] M.obj (.op n),
          ∀ (a : A.obj (.op n)) (x : (limit M : ModuleCat.{v} c.pt)),
            e (TensorProduct.tmul c.pt a x) = a • (limit.π M (.op n) x)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.13, Tag 0D49](https://stacks.math.columbia.edu/tag/0D49)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
