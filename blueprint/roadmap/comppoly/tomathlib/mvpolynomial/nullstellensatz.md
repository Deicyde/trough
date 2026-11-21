---
catalog: module
lean: MvPolynomial.eq_of_degreeOf_le_one_of_eval_zeroOne
statement: formalized
proof: formalized
---

# Polynomials of degree at most one per variable

`CompPoly.ToMathlib.MvPolynomial.Nullstellensatz`, in [CompPoly/ToMathlib/MvPolynomial/Nullstellensatz.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/ToMathlib/MvPolynomial/Nullstellensatz.lean), by Thomas Coratger.

> Such a polynomial is fixed by its values on the Boolean hypercube $\{0, 1\}^\sigma$.
>
> This is a corollary of the combinatorial Nullstellensatz.

`MvPolynomial.eq_of_degreeOf_le_one_of_eval_zeroOne` (theorem, [line 30](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/ToMathlib/MvPolynomial/Nullstellensatz.lean#L30))

> Two polynomials of degree at most one per variable that agree on the hypercube are equal.
>
> This is Lemma 3.6 of Thaler, "Proofs, Arguments, and Zero-Knowledge".

```lean
theorem eq_of_degreeOf_le_one_of_eval_zeroOne {p q : MvPolynomial σ R}
    (hp : ∀ i, p.degreeOf i ≤ 1) (hq : ∀ i, q.degreeOf i ≤ 1)
    (h : ∀ x : σ → R, (∀ i, x i = 0 ∨ x i = 1) → eval x p = eval x q) : p = q
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/ToMathlib/MvPolynomial/Nullstellensatz.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/ToMathlib/MvPolynomial/Nullstellensatz.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.ToMathlib.MvPolynomial.Nullstellensatz.json)
