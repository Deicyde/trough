---
declaration: theorem
origin: cited
lean: TauCeti.isIndecomposableModule_iff_exists_linearEquiv_quotient_span_op_root_X_pow_pow
statement: formalized
proof: formalized
---

# The indecomposable finitely generated right modules over `A = K[X]/(Xⁿ)` are exactly the `M_i`, up to isomorphism

such a module is indecomposable exactly when it is isomorphic to
`A ⧸ (x ^ i)` for some `0 < i ≤ n`.

```lean
TauCeti.isIndecomposableModule_iff_exists_linearEquiv_quotient_span_op_root_X_pow_pow.{u, v}
  {K : Type u} [Field K] {n : ℕ} {M : Type v} [AddCommGroup M]
  [_root_.Module (AdjoinRoot (Polynomial.X ^ n))ᵐᵒᵖ M]
  [Module.Finite (AdjoinRoot (Polynomial.X ^ n))ᵐᵒᵖ M] :
  TauCeti.IsIndecomposableModule (AdjoinRoot (Polynomial.X ^ n))ᵐᵒᵖ M ↔
    ∃ i,
      0 < i ∧
        i ≤ n ∧
          Nonempty
            (M ≃ₗ[(AdjoinRoot (Polynomial.X ^ n))ᵐᵒᵖ]
              (AdjoinRoot (Polynomial.X ^ n))ᵐᵒᵖ ⧸
                Ideal.span {MulOpposite.op (AdjoinRoot.root (Polynomial.X ^ n) ^ i)})
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isIndecomposableModule_iff_exists_linearEquiv_quotient_span_op_root_X_pow_pow`](https://taucetiproject.org/docs/TauCeti/RingTheory/Polynomial/Truncated/Module.html#TauCeti.isIndecomposableModule_iff_exists_linearEquiv_quotient_span_op_root_X_pow_pow).

## Sources

- [Tau Ceti documentation: `TauCeti.isIndecomposableModule_iff_exists_linearEquiv_quotient_span_op_root_X_pow_pow`](https://taucetiproject.org/docs/TauCeti/RingTheory/Polynomial/Truncated/Module.html#TauCeti.isIndecomposableModule_iff_exists_linearEquiv_quotient_span_op_root_X_pow_pow)
- [Source of `TauCeti.isIndecomposableModule_iff_exists_linearEquiv_quotient_span_op_root_X_pow_pow` in TauCeti/RingTheory/Polynomial/Truncated/Module.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Polynomial/Truncated/Module.lean#L193)
- [Tau Ceti roadmap status: Stable, periodic, and curved homological algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/StablePeriodicCurved/STATUS.md)
