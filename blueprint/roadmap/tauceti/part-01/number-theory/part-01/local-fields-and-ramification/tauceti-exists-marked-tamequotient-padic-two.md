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
- [Euler's theorem on an `n`-th root of unity](../../../group-theory/other-results/part-01/eulers-theorem-on-an-n-th-root-of-unity.md)
- [The first half of Dedekind's different theorem](../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [The Galois group of the maximal unramified extension is the profinite integers](the-galois-group-of-the-maximal-unramified-exten.md)
- [The profinite power](../../../../part-02/topology/profinite-integers-profinite-powers-and-continuo/the-profinite-power.md)
- [Tame inertia is the prime-to-`p` Tate module](tame-inertia-is-the-prime-to-p-tate-module.md)
- [The wild inertia subgroup is closed in the Krull topology](the-wild-inertia-subgroup-is-closed-in-the-krull.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_marked_tameQuotient_padic_two`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/WorkedExamples/Padic/Two/Tame.html#TauCeti.exists_marked_tameQuotient_padic_two).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_marked_tameQuotient_padic_two`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/WorkedExamples/Padic/Two/Tame.html#TauCeti.exists_marked_tameQuotient_padic_two)
- [Source of `TauCeti.exists_marked_tameQuotient_padic_two` in TauCeti/NumberTheory/LocalField/WorkedExamples/Padic/Two/Tame.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LocalField/WorkedExamples/Padic/Two/Tame.lean#L23)
- [Tau Ceti roadmap status: Local fields and ramification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/LocalFieldsRamification/STATUS.md)
