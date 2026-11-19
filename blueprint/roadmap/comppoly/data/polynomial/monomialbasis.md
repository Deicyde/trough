---
catalog: module
lean: Polynomial.sum_degreeLT_monomial_eq_subtype, Polynomial.monomialBasisOfDegreeLT, Polynomial.finrank_degreeLT_n, Polynomial.finiteDimensional_degreeLT
statement: formalized
proof: formalized
---

# Monomial basis for algebra extensions

`CompPoly.Data.Polynomial.MonomialBasis`, in [CompPoly/Data/Polynomial/MonomialBasis.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/MonomialBasis.lean), by Chung Thai Nguyen, Quang Dao.

`Polynomial.sum_degreeLT_monomial_eq_subtype` (theorem, [line 35](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/MonomialBasis.lean#L35))

```lean
theorem sum_degreeLT_monomial_eq_subtype {n : ℕ} (p : L⦃< n⦄[X]) :
    (⟨p.val.sum (fun n a => Polynomial.monomial n a), by
    -- degree of sum is degree of p.val, which is < n
    rw [Polynomial.sum_monomial_eq p.val]
    exact p.property
  ⟩ : L⦃< n⦄[X]) = p
```

`Polynomial.monomialBasisOfDegreeLT` (definition, [line 44](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/MonomialBasis.lean#L44))

```lean
noncomputable def monomialBasisOfDegreeLT {n : ℕ} : Basis (Fin n) L (L⦃< n⦄[X])
```

`Polynomial.finrank_degreeLT_n` (theorem, [line 129](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/MonomialBasis.lean#L129))

```lean
theorem finrank_degreeLT_n (n : ℕ) : Module.finrank L (L⦃< n⦄[X]) = n
```

`Polynomial.finiteDimensional_degreeLT` (theorem, [line 134](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/MonomialBasis.lean#L134))

```lean
theorem finiteDimensional_degreeLT {n : ℕ} (h_n_pos : 0 < n) :
    FiniteDimensional L L⦃< n⦄[X]
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/Data/Polynomial/MonomialBasis.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/MonomialBasis.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Data.Polynomial.MonomialBasis.json)
