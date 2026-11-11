---
declaration: theorem
origin: cited
lean: TauCeti.exists_marked_tameQuotient_padic_two
statement: formalized
proof: formalized
---

# TauCeti.exists_marked_tameQuotient_padic_two

The tame quotient of `ℚ₂` has a marked arithmetic Frobenius and tame inertia generator,
with the relation `σ τ σ⁻¹ = τ²` and the marked Iwasawa isomorphism.

```lean
TauCeti.exists_marked_tameQuotient_padic_two :
  ∃ σ τ,
    TauCeti.IsArithFrobeniusLift ℚ_[2] σ ∧
      (Subgroup.zpowers ((TauCeti.toTameQuotient ℚ_[2]) ↑τ)).topologicalClosure =
          TauCeti.tameInertia ℚ_[2] ∧
        (TauCeti.toTameQuotient ℚ_[2]) σ * (TauCeti.toTameQuotient ℚ_[2]) ↑τ *
              ((TauCeti.toTameQuotient ℚ_[2]) σ)⁻¹ =
            (TauCeti.toTameQuotient ℚ_[2]) ↑τ ^ 2 ∧
          ∃ e,
            e ((TauCeti.toTameQuotient ℚ_[2]) σ) = TauCeti.iwasawaSigma ℚ_[2] ∧
              e ((TauCeti.toTameQuotient ℚ_[2]) ↑τ) = TauCeti.iwasawaTau ℚ_[2]
```

## Depends on

- [TauCeti.algebraicExtensionNormedField](tauceti-algebraicextensionnormedfield.md)
- [The wild inertia subgroup](the-wild-inertia-subgroup.md)

## Proof depends on

- [Dedekind's different theorem, the tame case](../../part-02/local-field/dedekinds-different-theorem-the-tame-case.md)
- [Euler's theorem on an `n`-th root of unity](../../../group-theory/other-results/eulers-theorem-on-an-n-th-root-of-unity.md)
- [The first half of Dedekind's different theorem](../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [The Galois group of the maximal unramified extension is the profinite integers](the-galois-group-of-the-maximal-unramified-exten.md)
- [The profinite power](../../../topology/profinite-integers-profinite-powers-and-continuo/the-profinite-power.md)
- [Tame inertia is the prime-to-`p` Tate module](tame-inertia-is-the-prime-to-p-tate-module.md)
- [TauCeti.topologicalClosure_zpowers_toTameQuotient_eq_iff](tauceti-topologicalclosure-zpowers-totamequotien.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_marked_tameQuotient_padic_two`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/WorkedExamples/Padic/Two/Tame.html#TauCeti.exists_marked_tameQuotient_padic_two).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_marked_tameQuotient_padic_two`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/WorkedExamples/Padic/Two/Tame.html#TauCeti.exists_marked_tameQuotient_padic_two)
- [Source of `TauCeti.exists_marked_tameQuotient_padic_two` in TauCeti/NumberTheory/LocalField/WorkedExamples/Padic/Two/Tame.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/WorkedExamples/Padic/Two/Tame.lean#L23)
- [Tau Ceti roadmap status: Local fields and ramification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/LocalFieldsRamification/STATUS.md)
