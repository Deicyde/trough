---
declaration: def
origin: cited
lean: TauCeti.padicCompletionUnitsNormCokernelEquiv
statement: formalized
---

# The cokernel of the completed norm

`A(L) → A(K)` is `Gal(L/K)^ab / (Gal(L/K)^ab)^(p^m)`,
the maximal `p`-quotient of `Gal(L/K)^ab`, once `p ^ m` contains the full power of `p` dividing
`#Gal(L/K)^ab`. The isomorphism is induced by the completed norm residue map
(`TauCeti.padicCompletionUnitsNormCokernelEquiv_mk`).

```lean
TauCeti.padicCompletionUnitsNormCokernelEquiv.{u_1} (p : ℕ) (K : Type) [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] (L : Type u_1) [Field L] [Algebra K L]
  [FiniteDimensional K L] [IsGalois K L] [Fact (Nat.Prime p)] (hpK : ↑p ≠ 0) {m : ℕ}
  (hm : (Nat.card (Abelianization Gal(L/K))).factorization p ≤ m) :
  Additive ↥(TauCeti.padicCompletionUnits p K) ⧸
      (TauCeti.padicCompletionUnitsNorm p K L).range.toAddSubgroup ≃+
    Additive (TauCeti.powerClassQuotient (Abelianization Gal(L/K)) (p ^ m))
```

## Depends on

- [The local class formation](../../part-01/class-field-theory/the-local-class-formation.md)
- [Tate's theorem for a class formation](../../part-01/class-field-theory/tates-theorem-for-a-class-formation.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.padicCompletionUnitsNormCokernelEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/MultiplicativeCompletion/Norm/Cokernel.html#TauCeti.padicCompletionUnitsNormCokernelEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.padicCompletionUnitsNormCokernelEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/MultiplicativeCompletion/Norm/Cokernel.html#TauCeti.padicCompletionUnitsNormCokernelEquiv)
- [Source of `TauCeti.padicCompletionUnitsNormCokernelEquiv` in TauCeti/NumberTheory/Padics/MultiplicativeCompletion/Norm/Cokernel.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Padics/MultiplicativeCompletion/Norm/Cokernel.lean#L222)
- [Tau Ceti roadmap status: Local Galois groups of p-adic fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/LocalGaloisGroups/STATUS.md)
