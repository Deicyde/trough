---
catalog: module
lean: CompPoly.CPolynomial.lcoeff, CompPoly.CPolynomial.lcoeff_apply, CompPoly.CPolynomial.degreeLE, CompPoly.CPolynomial.degreeLT, CompPoly.CPolynomial.mem_degreeLE, CompPoly.CPolynomial.mem_degreeLT, CompPoly.CPolynomial.mem_degreeLT_iff_size_le, CompPoly.CPolynomial.zero_mem_degreeLT, CompPoly.CPolynomial.ofFn_mem_degreeLT, CompPoly.CPolynomial.ofFn_coeff_of_mem_degreeLT, CompPoly.CPolynomial.ofFnEquiv, CompPoly.CPolynomial.ofFnEquiv_apply_val, CompPoly.CPolynomial.ofFnEquiv_symm_apply, CompPoly.CPolynomial.instFintypeDegreeLT, CompPoly.CPolynomial.card_degreeLT, CompPoly.CPolynomial.add_mem_degreeLT, CompPoly.CPolynomial.nsmul_mem_degreeLT, CompPoly.CPolynomial.smul_mem_degreeLT, CompPoly.CPolynomial.degreeLTCoeffs, CompPoly.CPolynomial.degreeLTCoeffs_apply, CompPoly.CPolynomial.ofFnEquiv_symm_eq_degreeLTCoeffs
statement: formalized
proof: formalized
---

# Linear Algebra API for Computable Univariate Polynomials

`CompPoly.Univariate.Linear`, in [CompPoly/Univariate/Linear.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Linear.lean), by Desmond Coles, Derek Sorensen, Alexander Hicks.

> This file defines coefficient linear maps and bounded-degree subtypes for `CPolynomial`.
> The subtypes depend only on `Zero R`.
>
> `ofFnEquiv n` identifies the coefficient vectors `Fin n → R` with the polynomials of degree below
> `n`. Over a finite coefficient type, it gives the executable enumeration `instFintypeDegreeLT`.

`CompPoly.CPolynomial.lcoeff` (definition, [line 34](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Linear.lean#L34))

> This is an R-linear function that returns the coefficient of X^n.

```lean
def lcoeff (n : ℕ) : (CPolynomial R) →ₗ[R] R
```

`CompPoly.CPolynomial.lcoeff_apply` (theorem, [line 41](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Linear.lean#L41))

> Applying `lcoeff n` returns the coefficient of degree `n`.

```lean
theorem lcoeff_apply (n : ℕ) (p : CPolynomial R) : lcoeff n p = coeff p n
```

`CompPoly.CPolynomial.degreeLE` (definition, [line 51](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Linear.lean#L51))

> The set of `CPolynomial R` consisting of polynomials of degree ≤ `n`.

```lean
def degreeLE (n : WithBot ℕ) : Set (CPolynomial R)
```

`CompPoly.CPolynomial.degreeLT` (definition, [line 55](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Linear.lean#L55))

> The set of `CPolynomial R` consisting of polynomials of degree < `n`.

```lean
def degreeLT (n : ℕ) : Set (CPolynomial R)
```

`CompPoly.CPolynomial.mem_degreeLE` (theorem, [line 59](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Linear.lean#L59))

> Membership in `degreeLE` is the corresponding degree bound.

```lean
theorem mem_degreeLE {n : WithBot ℕ} {p : CPolynomial R} :
    p ∈ degreeLE (R := R) n ↔ p.degree ≤ n
```

`CompPoly.CPolynomial.mem_degreeLT` (theorem, [line 64](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Linear.lean#L64))

> Membership in `degreeLT` is the corresponding strict degree bound.

```lean
theorem mem_degreeLT {n : ℕ} {p : CPolynomial R} :
    p ∈ degreeLT (R := R) n ↔ p.degree < n
```

`CompPoly.CPolynomial.mem_degreeLT_iff_size_le` (theorem, [line 69](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Linear.lean#L69))

> `degreeLT n` is exactly the bounded-size carrier storing at most `n` coefficients.

```lean
theorem mem_degreeLT_iff_size_le {n : ℕ} {p : CPolynomial R} :
    p ∈ degreeLT (R := R) n ↔ p.val.size ≤ n
```

`CompPoly.CPolynomial.zero_mem_degreeLT` (theorem, [line 78](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Linear.lean#L78))

> The zero polynomial has bounded degree for every cutoff.

```lean
theorem zero_mem_degreeLT (n : ℕ) : (0 : CPolynomial R) ∈ degreeLT (R := R) n
```

`CompPoly.CPolynomial.ofFn_mem_degreeLT` (theorem, [line 89](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Linear.lean#L89))

> `ofFn` on `n` coefficients has degree below `n`.

```lean
theorem ofFn_mem_degreeLT {n : ℕ} (f : Fin n → R) : ofFn f ∈ degreeLT (R := R) n
```

`CompPoly.CPolynomial.ofFn_coeff_of_mem_degreeLT` (theorem, [line 95](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Linear.lean#L95))

> A polynomial of degree below `n` is `ofFn` of its first `n` coefficients.

```lean
theorem ofFn_coeff_of_mem_degreeLT {n : ℕ} {p : CPolynomial R} (hp : p ∈ degreeLT (R := R) n) :
    ofFn (fun i : Fin n => coeff p i) = p
```

`CompPoly.CPolynomial.ofFnEquiv` (definition, [line 109](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Linear.lean#L109))

> `ofFnEquiv n` is the equivalence, through `ofFn`, from the coefficient vectors `Fin n → R` to
> the polynomials of degree below `n`. Its inverse reads the first `n` coefficients. Both directions
> are executable.

```lean
def ofFnEquiv (n : ℕ) : (Fin n → R) ≃ ↥(degreeLT (R := R) n)
```

`CompPoly.CPolynomial.ofFnEquiv_apply_val` (theorem, [line 117](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Linear.lean#L117))

> The polynomial that `ofFnEquiv n` assigns to `f` is `ofFn f`.

```lean
theorem ofFnEquiv_apply_val (n : ℕ) (f : Fin n → R) : (ofFnEquiv n f).val = ofFn f
```

`CompPoly.CPolynomial.ofFnEquiv_symm_apply` (theorem, [line 122](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Linear.lean#L122))

> The inverse of `ofFnEquiv n` reads the first `n` coefficients.

```lean
theorem ofFnEquiv_symm_apply (n : ℕ) (p : ↥(degreeLT (R := R) n)) (i : Fin n) :
    (ofFnEquiv n).symm p i = p.val.coeff i
```

`CompPoly.CPolynomial.instFintypeDegreeLT` (instance, [line 138](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Linear.lean#L138))

> Over a finite coefficient type, the polynomials of degree below `n` form a finite type.
>
> The enumeration converts each coefficient function `Fin n → R` to a polynomial with `ofFn`.
> At `n = 0` it lists only the zero polynomial.
>
> Downstream `by decide` can count small concrete enumerations. Use compiled evaluation such as
> `#guard` to test predicates that inspect the polynomials. For proofs about such searches, use the
> quantifier lemmas in `CompPoly.Univariate.ToPoly.Degree`.
>
> The enumeration uses `BEq R` to trim trailing zeros. When the `BEq R` instance changes,
> the subtype stays definitionally equal, but its enumerations may require a proof of equality.
> `card_degreeLT` applies to any enumeration.

```lean
instance instFintypeDegreeLT [Fintype R] (n : ℕ) : Fintype ↥(degreeLT (R := R) n)
```

`CompPoly.CPolynomial.card_degreeLT` (theorem, [line 145](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Linear.lean#L145))

> Over a finite coefficient type, there are `card R ^ n` polynomials of degree below `n`.
> The statement holds for every `Fintype` instance on `↥(degreeLT n)`.

```lean
theorem card_degreeLT [Zero R] [Fintype R] (n : ℕ) [Fintype ↥(degreeLT (R := R) n)] :
    Fintype.card ↥(degreeLT (R := R) n) = Fintype.card R ^ n
```

`CompPoly.CPolynomial.add_mem_degreeLT` (theorem, [line 155](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Linear.lean#L155))

> `degreeLT n` is closed under addition.

```lean
theorem add_mem_degreeLT {n : ℕ} {p q : CPolynomial R}
    (hp : p ∈ degreeLT (R := R) n) (hq : q ∈ degreeLT (R := R) n) :
    p + q ∈ degreeLT (R := R) n
```

`CompPoly.CPolynomial.nsmul_mem_degreeLT` (theorem, [line 166](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Linear.lean#L166))

> `degreeLT n` is closed under additive scalar multiplication.

```lean
theorem nsmul_mem_degreeLT {n m : ℕ} {p : CPolynomial R}
    (hp : p ∈ degreeLT (R := R) n) :
    m • p ∈ degreeLT (R := R) n
```

`CompPoly.CPolynomial.smul_mem_degreeLT` (theorem, [line 177](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Linear.lean#L177))

> `degreeLT n` is closed under semiring scalar multiplication.

```lean
theorem smul_mem_degreeLT {n : ℕ} (r : R) {p : CPolynomial R}
    (hp : p ∈ degreeLT (R := R) n) :
    r • p ∈ degreeLT (R := R) n
```

`CompPoly.CPolynomial.degreeLTCoeffs` (definition, [line 259](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Linear.lean#L259))

> The first `n` coefficients on `degreeLT n` form a computable linear map to `Fin n → R`.

```lean
def degreeLTCoeffs (n : ℕ) : ↥(degreeLT (R := R) n) →ₗ[R] (Fin n → R)
```

`CompPoly.CPolynomial.degreeLTCoeffs_apply` (theorem, [line 272](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Linear.lean#L272))

> Applying `degreeLTCoeffs` returns the corresponding bounded coefficient.

```lean
theorem degreeLTCoeffs_apply (n : ℕ) (p : ↥(degreeLT (R := R) n)) (i : Fin n) :
    degreeLTCoeffs n p i = coeff p.1 i
```

`CompPoly.CPolynomial.ofFnEquiv_symm_eq_degreeLTCoeffs` (theorem, [line 277](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Linear.lean#L277))

> The inverse of `ofFnEquiv` is the coefficient linear map.

```lean
theorem ofFnEquiv_symm_eq_degreeLTCoeffs (n : ℕ) :
    ((ofFnEquiv (R := R) n).symm : ↥(degreeLT (R := R) n) → (Fin n → R)) =
      degreeLTCoeffs n
```

## Depends on

- [Computable Univariate Polynomials](basic.md)

## Sources

- [CompPoly/Univariate/Linear.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Linear.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Univariate.Linear.json)
