---
catalog: module
lean: CPoly.CMvPolynomial.partialEvalFirst, CPoly.CMvPolynomial.partialEvalFirst_eval, CPoly.CMvPolynomial.partialEvalFirst_degreeOf_le
statement: formalized
proof: formalized
---

# Partial evaluation of the first variable of a `CMvPolynomial`

`CompPoly.Multivariate.PartialEval`, in [CompPoly/Multivariate/PartialEval.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/PartialEval.lean), by Cody Gunton.

> `partialEvalFirst a p` fixes variable `0` of a multivariate computable
> polynomial to a scalar value, together with its evaluation lemma and the
> per-variable degree-bound lemma.

> ## Core operation

`CPoly.CMvPolynomial.partialEvalFirst` (definition, [line 114](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/PartialEval.lean#L114))

> Fix variable 0 of a multivariate polynomial to a scalar value `a`.

```lean
def partialEvalFirst (a : R) (p : CMvPolynomial (n + 1) R) : CMvPolynomial n R
```

> ## Evaluation lemma

`CPoly.CMvPolynomial.partialEvalFirst_eval` (theorem, [line 120](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/PartialEval.lean#L120))

> `partialEvalFirst a p` correctly implements partial evaluation.

```lean
theorem partialEvalFirst_eval (a : R) (p : CMvPolynomial (n + 1) R) (v : Fin n → R) :
    (partialEvalFirst a p).eval v = p.eval (Fin.cons a v)
```

> ## Degree preservation

`CPoly.CMvPolynomial.partialEvalFirst_degreeOf_le` (theorem, [line 147](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/PartialEval.lean#L147))

> `partialEvalFirst` preserves degree bounds for each remaining variable.

```lean
theorem partialEvalFirst_degreeOf_le [Nontrivial R] {deg : ℕ} (a : R)
    (i : Fin n) (p : CMvPolynomial (n + 1) R)
    (hDeg : ∀ mono ∈ Lawful.monomials p, mono.degreeOf i.succ ≤ deg) :
    ∀ mono ∈ Lawful.monomials (partialEvalFirst a p), mono.degreeOf i ≤ deg
```

## Depends on

- [Computable multivariate polynomials (extended operations)](operations.md)

## Sources

- [CompPoly/Multivariate/PartialEval.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/PartialEval.lean)
- [Declaration ledger](../../../sources/comppoly/CompPoly.Multivariate.PartialEval.json)
