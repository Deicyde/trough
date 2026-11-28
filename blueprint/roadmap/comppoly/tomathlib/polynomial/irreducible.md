---
catalog: module
lean: Polynomial.exists_factor_natDegree_le_of_reducible
statement: formalized
proof: formalized
---

# Small-factor extraction for reducible polynomials

`CompPoly.ToMathlib.Polynomial.Irreducible`, in [CompPoly/ToMathlib/Polynomial/Irreducible.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/ToMathlib/Polynomial/Irreducible.lean), by Derek Sorensen.

> A reducible polynomial of degree `n` always has an irreducible factor of degree at most
> `n / 2`: it splits as a product of two non-units whose degrees sum to `n`, and the smaller
> of the two dominates an irreducible factor.
>
> This is the pigeonhole step of Rabin's irreducibility test (see
> `CompPoly/Data/Polynomial/Rabin.lean`), which needs to bound the degree of a hypothetical
> small factor in order to derive a contradiction.
>
> ## Main statements
>
> * `Polynomial.exists_factor_natDegree_le_of_reducible`: a reducible polynomial of degree `n`
>   has an irreducible factor of degree at most `n / 2`.

`Polynomial.exists_factor_natDegree_le_of_reducible` (theorem, [line 41](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/ToMathlib/Polynomial/Irreducible.lean#L41))

> A reducible polynomial of positive degree `n` has an irreducible factor of degree at most
> `n / 2`.
>
> Writing `P = a * b` with both factors non-units, their degrees sum to `n`, so the smaller one
> has degree at most `n / 2`; any irreducible factor of it works.

```lean
theorem exists_factor_natDegree_le_of_reducible (P : R[X]) {n : ℕ}
    (h_deg : P.natDegree = n) (h_pos : 0 < n) (h_red : ¬ Irreducible P) :
    ∃ q, Irreducible q ∧ q ∣ P ∧ q.natDegree ≤ n / 2
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/ToMathlib/Polynomial/Irreducible.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/ToMathlib/Polynomial/Irreducible.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.ToMathlib.Polynomial.Irreducible.json)
