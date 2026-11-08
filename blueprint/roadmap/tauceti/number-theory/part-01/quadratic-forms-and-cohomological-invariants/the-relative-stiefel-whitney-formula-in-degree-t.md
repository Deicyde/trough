---
declaration: theorem
origin: cited
lean: TauCeti.sw2Class_formClass_traceTransfer_smul_sq, TauCeti.sw1Class_traceTransfer_mk_rankOne, TauCeti.sw1_eq_add_galoisCor_of_equivalent_scharlauTransfer, TauCeti.sw1_eq_add_galoisCor_of_equivalent_traceTransfer, TauCeti.sw1Class_formClass_traceTransfer_smul_sq, TauCeti.sw2_eq_add_galoisEvens_add_cup_of_equivalent_traceTransfer
statement: formalized
proof: formalized
---

# The relative Stiefel–Whitney formula in degree two, on the trace forms themselves (Kahn, Théorème 2 in degree two)

for a quadratic extension `L/K`, which is separable as `2` is
invertible, and `a ∈ Lˣ` with Kummer class `(a) ∈ H¹(G_L, 𝔽₂)`,

```text
w₂(Tr_*⟨a⟩) = w₂(Tr_*⟨1⟩) + N^{Ev}((a)) + w₁(Tr_*⟨1⟩) ∪ cor (a),
```

where the Evens norm `N^{Ev}` and the corestriction `cor` are taken along any `K`-embedding `σ`
of `L` into a separable closure of `K`. The two sides are the classes of the regular forms
`y ↦ Tr_{L/K}(a y²)` and `y ↦ Tr_{L/K}(y²)` on `L`; their regularity is a hypothesis.

```lean
TauCeti.sw2Class_formClass_traceTransfer_smul_sq.{u} {K L : Type u} [Field K] [Invertible 2]
  [Field L] [Algebra K L] [FiniteDimensional K L] [Invertible 2] (σ : L →ₐ[K] SeparableClosure K)
  (hfin : Module.finrank K L = 2) (a : Lˣ) (ha : QuadraticMap.Nondegenerate)
  (h1 : QuadraticMap.Nondegenerate) :
  TauCeti.sw2Class (TauCeti.formClass (QuadraticMap.traceTransfer K (↑a • QuadraticMap.sq)) ha) =
    TauCeti.sw2Class (TauCeti.formClass (QuadraticMap.traceTransfer K QuadraticMap.sq) h1) +
        TauCeti.galoisEvens K L σ hfin (TauCeti.kummerClass a) +
      (((TauCeti.trivialF2TopPairing (TauCeti.AbsoluteGaloisGroup K)).cup 1 1)
          (TauCeti.sw1Class (TauCeti.formClass (QuadraticMap.traceTransfer K QuadraticMap.sq) h1)))
        ((CategoryTheory.ConcreteCategory.hom (TauCeti.galoisCor K L σ 1)) (TauCeti.kummerClass a))
```

## Depends on

- [The index-two degree-one Evens norm `Nᴱᵛ : H¹(U, 𝔽₂) → H²(G, 𝔽₂)` for an open subgroup `U` of index two](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-index-two-degree-one-evens-norm-nev-h1-u-f2.md)
- [The Kummer isomorphism `Kˣ ⧸ (Kˣ)ⁿ ≃* H¹(G_K, μₙ)` (NSW (6.2.1) and the display following it), for `n` invertible in `K`](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism-kx-kx-n-h1-g-k-n-nsw-6-2.md)
- [Shapiro's lemma in every degree](../../../representation-theory/homological/shapiros-lemma-in-every-degree.md)

## Proof depends on

- [The comparison isomorphism `Br(K) ≃ H²_cont(G_K, (Kˢ)ˣ)` with Mathlib's continuous cohomology, for `K` in any universe](the-comparison-isomorphism-br-k-h2-cont-g-k-ks-x.md)
- [The cup-norm theorem](../../../field-theory/other-results/the-cup-norm-theorem.md)
- [Serre's formula for the Evens norm of a Kummer class (Serre, Théorème 1′ at `n = 2`)](../../../field-theory/other-results/serres-formula-for-the-evens-norm-of-a-kummer-cl.md)
- [The Skolem-Noether theorem](../../../algebra/central-simple/the-skolem-noether-theorem.md)
- [The splitting criterion for quaternion algebras (Lam III.2.7 and III.4.2, Serre III.1, Gille-Szamuely 1.1.9)](the-splitting-criterion-for-quaternion-algebras.md)
- [Witt's chain theorem in its nontrivial range](../../../linear-algebra/quadratic-form/witts-chain-theorem-in-its-nontrivial-range.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.sw2Class_formClass_traceTransfer_smul_sq`](https://taucetiproject.org/docs/TauCeti/FieldTheory/QuadraticForm/StiefelWhitney/QuadraticExtension.html#TauCeti.sw2Class_formClass_traceTransfer_smul_sq).

## Other forms

**The relative Stiefel–Whitney formula in degree one.** Formalized in Tau Ceti as [`TauCeti.sw1Class_traceTransfer_mk_rankOne`](https://taucetiproject.org/docs/TauCeti/FieldTheory/QuadraticForm/StiefelWhitney/Transfer.html#TauCeti.sw1Class_traceTransfer_mk_rankOne).

```lean
TauCeti.sw1Class_traceTransfer_mk_rankOne.{u} {K L : Type u} [Field K] [Field L] [Algebra K L]
  [FiniteDimensional K L] [Invertible 2] [Invertible 2] (σ : L →ₐ[K] SeparableClosure K)
  [Algebra.IsSeparable K L] (a : Lˣ) :
  TauCeti.sw1Class ((TauCeti.RegularFormClass.traceTransfer K) ⟦⟨1, fun x => a⟩⟧) =
    TauCeti.sw1Class ((TauCeti.RegularFormClass.traceTransfer K) 1) +
      (CategoryTheory.ConcreteCategory.hom (TauCeti.galoisCor K L σ 1)) (TauCeti.kummerClass a)
```

**The relative Stiefel–Whitney formula in degree one, on diagonal presentations.** Formalized in Tau Ceti as [`TauCeti.sw1_eq_add_galoisCor_of_equivalent_scharlauTransfer`](https://taucetiproject.org/docs/TauCeti/FieldTheory/QuadraticForm/StiefelWhitney/Transfer.html#TauCeti.sw1_eq_add_galoisCor_of_equivalent_scharlauTransfer).

```lean
TauCeti.sw1_eq_add_galoisCor_of_equivalent_scharlauTransfer.{u} {K L : Type u} [Field K] [Field L]
  [Algebra K L] [FiniteDimensional K L] [Invertible 2] [Invertible 2]
  (σ : L →ₐ[K] SeparableClosure K) (s : L →ₗ[K] K) (a : Lˣ) {m n : ℕ} {t : Fin m → Kˣ}
  {b : Fin n → Kˣ}
  (ht :
    QuadraticMap.Equivalent (QuadraticMap.sq.scharlauTransfer s)
      (QuadraticMap.weightedSumSquares K fun i => ↑(t i)))
  (hb :
    QuadraticMap.Equivalent ((↑a • QuadraticMap.sq).scharlauTransfer s)
      (QuadraticMap.weightedSumSquares K fun i => ↑(b i))) :
  TauCeti.sw1 b =
    TauCeti.sw1 t +
      (CategoryTheory.ConcreteCategory.hom (TauCeti.galoisCor K L σ 1)) (TauCeti.kummerClass a)
```

**The relative Stiefel–Whitney formula in degree one, on diagonal presentations of the trace forms.** Formalized in Tau Ceti as [`TauCeti.sw1_eq_add_galoisCor_of_equivalent_traceTransfer`](https://taucetiproject.org/docs/TauCeti/FieldTheory/QuadraticForm/StiefelWhitney/Transfer.html#TauCeti.sw1_eq_add_galoisCor_of_equivalent_traceTransfer).

```lean
TauCeti.sw1_eq_add_galoisCor_of_equivalent_traceTransfer.{u} {K L : Type u} [Field K] [Field L]
  [Algebra K L] [FiniteDimensional K L] [Invertible 2] [Invertible 2]
  (σ : L →ₐ[K] SeparableClosure K) (a : Lˣ) {m n : ℕ} {t : Fin m → Kˣ} {b : Fin n → Kˣ}
  (ht :
    QuadraticMap.Equivalent (QuadraticMap.traceTransfer K QuadraticMap.sq)
      (QuadraticMap.weightedSumSquares K fun i => ↑(t i)))
  (hb :
    QuadraticMap.Equivalent (QuadraticMap.traceTransfer K (↑a • QuadraticMap.sq))
      (QuadraticMap.weightedSumSquares K fun i => ↑(b i))) :
  TauCeti.sw1 b =
    TauCeti.sw1 t +
      (CategoryTheory.ConcreteCategory.hom (TauCeti.galoisCor K L σ 1)) (TauCeti.kummerClass a)
```

**The relative Stiefel–Whitney formula in degree one, on the trace forms themselves.** Formalized in Tau Ceti as [`TauCeti.sw1Class_formClass_traceTransfer_smul_sq`](https://taucetiproject.org/docs/TauCeti/FieldTheory/QuadraticForm/StiefelWhitney/Transfer.html#TauCeti.sw1Class_formClass_traceTransfer_smul_sq).

```lean
TauCeti.sw1Class_formClass_traceTransfer_smul_sq.{u} {K L : Type u} [Field K] [Field L]
  [Algebra K L] [FiniteDimensional K L] [Invertible 2] [Invertible 2]
  (σ : L →ₐ[K] SeparableClosure K) (a : Lˣ) (ha : QuadraticMap.Nondegenerate)
  (h1 : QuadraticMap.Nondegenerate) :
  TauCeti.sw1Class (TauCeti.formClass (QuadraticMap.traceTransfer K (↑a • QuadraticMap.sq)) ha) =
    TauCeti.sw1Class (TauCeti.formClass (QuadraticMap.traceTransfer K QuadraticMap.sq) h1) +
      (CategoryTheory.ConcreteCategory.hom (TauCeti.galoisCor K L σ 1)) (TauCeti.kummerClass a)
```

**The relative Stiefel–Whitney formula in degree two, on diagonal presentations of the trace forms.** Formalized in Tau Ceti as [`TauCeti.sw2_eq_add_galoisEvens_add_cup_of_equivalent_traceTransfer`](https://taucetiproject.org/docs/TauCeti/FieldTheory/QuadraticForm/StiefelWhitney/QuadraticExtension.html#TauCeti.sw2_eq_add_galoisEvens_add_cup_of_equivalent_traceTransfer).

```lean
TauCeti.sw2_eq_add_galoisEvens_add_cup_of_equivalent_traceTransfer.{u} {K L : Type u} [Field K]
  [Invertible 2] [Field L] [Algebra K L] [FiniteDimensional K L] [Invertible 2]
  (σ : L →ₐ[K] SeparableClosure K) (hfin : Module.finrank K L = 2) (a : Lˣ) {m n : ℕ}
  {t : Fin m → Kˣ} {b : Fin n → Kˣ}
  (ht :
    QuadraticMap.Equivalent (QuadraticMap.traceTransfer K QuadraticMap.sq)
      (QuadraticMap.weightedSumSquares K fun i => ↑(t i)))
  (hb :
    QuadraticMap.Equivalent (QuadraticMap.traceTransfer K (↑a • QuadraticMap.sq))
      (QuadraticMap.weightedSumSquares K fun i => ↑(b i))) :
  TauCeti.sw2 b =
    TauCeti.sw2 t + TauCeti.galoisEvens K L σ hfin (TauCeti.kummerClass a) +
      (((TauCeti.trivialF2TopPairing (TauCeti.AbsoluteGaloisGroup K)).cup 1 1) (TauCeti.sw1 t))
        ((CategoryTheory.ConcreteCategory.hom (TauCeti.galoisCor K L σ 1)) (TauCeti.kummerClass a))
```

## Sources

- [Tau Ceti documentation: `TauCeti.sw2Class_formClass_traceTransfer_smul_sq`](https://taucetiproject.org/docs/TauCeti/FieldTheory/QuadraticForm/StiefelWhitney/QuadraticExtension.html#TauCeti.sw2Class_formClass_traceTransfer_smul_sq)
- [Source of `TauCeti.sw2Class_formClass_traceTransfer_smul_sq` in TauCeti/FieldTheory/QuadraticForm/StiefelWhitney/QuadraticExtension.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/QuadraticForm/StiefelWhitney/QuadraticExtension.lean#L238)
- [Tau Ceti roadmap status: Quadratic forms and cohomological invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/QuadraticFormInvariants/STATUS.md)
