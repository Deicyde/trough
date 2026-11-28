---
catalog: module
lean: MvPolynomial.finOneEquiv
statement: formalized
proof: formalized
---

# Useful Notation

`CompPoly.Data.MvPolynomial.Notation`, in [CompPoly/Data/MvPolynomial/Notation.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/MvPolynomial/Notation.lean), by Quang Dao.

> We define notation `R[X σ]` to be `MvPolynomial σ R`.
>
>   For a Finset `s` and a natural number `n`, we also define `s ^ᶠ n` to be
>   `Fintype.piFinset (fun (_ : Fin n) => s)`. This matches the intuition that `s ^ᶠ n`
>   is the set of all tuples of length `n` with elements in `s`.

`MvPolynomial.finOneEquiv` (definition, [line 33](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/MvPolynomial/Notation.lean#L33))

> Equivalence between `MvPolynomial (Fin 1) R` and `Polynomial R`

```lean
def finOneEquiv : MvPolynomial (Fin 1) R ≃ₐ[R] Polynomial R
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/Data/MvPolynomial/Notation.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/MvPolynomial/Notation.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Data.MvPolynomial.Notation.json)
