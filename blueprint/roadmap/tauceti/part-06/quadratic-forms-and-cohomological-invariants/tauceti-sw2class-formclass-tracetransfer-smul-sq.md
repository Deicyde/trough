---
declaration: theorem
origin: cited
lean: TauCeti.sw2Class_formClass_traceTransfer_smul_sq
statement: formalized
proof: formalized
---

# TauCeti.sw2Class_formClass_traceTransfer_smul_sq

**The relative Stiefel–Whitney formula in degree two, on the trace forms themselves** (Kahn,
Théorème 2 in degree two): for a quadratic extension `L/K`, which is separable as `2` is
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

- [TauCeti.ContCohomology.evensNormIndexTwo](../../part-02/continuous-cohomology-of-profinite-groups/tauceti-contcohomology-evensnormindextwo.md)
- [TauCeti.kummerIso](../../part-02/continuous-cohomology-of-profinite-groups/tauceti-kummeriso.md)

## Proof depends on

- [TauCeti.brauerCohomologyEquiv](tauceti-brauercohomologyequiv.md)
- [TauCeti.QuaternionAlgebra.nonempty_algEquiv_matrix_tfae](tauceti-quaternionalgebra-nonempty-algequiv-matr.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.sw2Class_formClass_traceTransfer_smul_sq`](https://taucetiproject.org/docs/TauCeti/FieldTheory/QuadraticForm/StiefelWhitney/QuadraticExtension.html#TauCeti.sw2Class_formClass_traceTransfer_smul_sq).

## Sources

- [Tau Ceti documentation: `TauCeti.sw2Class_formClass_traceTransfer_smul_sq`](https://taucetiproject.org/docs/TauCeti/FieldTheory/QuadraticForm/StiefelWhitney/QuadraticExtension.html#TauCeti.sw2Class_formClass_traceTransfer_smul_sq)
- [Source of `TauCeti.sw2Class_formClass_traceTransfer_smul_sq` in TauCeti/FieldTheory/QuadraticForm/StiefelWhitney/QuadraticExtension.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/QuadraticForm/StiefelWhitney/QuadraticExtension.lean#L238)
- [Tau Ceti roadmap status: Quadratic forms and cohomological invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/QuadraticFormInvariants/STATUS.md)
