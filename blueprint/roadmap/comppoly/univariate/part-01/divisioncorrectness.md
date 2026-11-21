---
catalog: module
lean: CompPoly.CPolynomial.divByMonic_toPoly_eq_divByMonic, CompPoly.CPolynomial.modByMonic_toPoly_eq_modByMonic, CompPoly.CPolynomial.modByMonic_add_mul_divByMonic, CompPoly.CPolynomial.leadingCoeff_inv_smul_monic, CompPoly.CPolynomial.div_toPoly_eq_divByMonic, CompPoly.CPolynomial.mod_toPoly_eq_modByMonic, CompPoly.CPolynomial.div_toPoly_eq_div, CompPoly.CPolynomial.mod_toPoly_eq_smul_mod, CompPoly.CPolynomial.exactDiv_toPoly_iff, CompPoly.CPolynomial.modByMonicByReversal_eq_modByMonic
statement: formalized
proof: formalized
---

# Univariate Division Correctness

`CompPoly.Univariate.DivisionCorrectness`, in [CompPoly/Univariate/DivisionCorrectness.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/DivisionCorrectness.lean), by Valerii Huhnin, Juan Conejero.

> Correctness theorems for division-style univariate polynomial algorithms.

`CompPoly.CPolynomial.divByMonic_toPoly_eq_divByMonic` (theorem, [line 488](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/DivisionCorrectness.lean#L488))

> CompPoly's `divByMonic` is correct w.r.t. Mathlib's `divByMonic`

```lean
theorem divByMonic_toPoly_eq_divByMonic (p q : CPolynomial R)
    (hmonic : q.monic) :
    (p.divByMonic q).toPoly = p.toPoly /ₘ q.toPoly
```

`CompPoly.CPolynomial.modByMonic_toPoly_eq_modByMonic` (theorem, [line 494](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/DivisionCorrectness.lean#L494))

> CompPoly's `modByMonic` is correct w.r.t. Mathlib's `modByMonic`

```lean
theorem modByMonic_toPoly_eq_modByMonic (p q : CPolynomial R)
    (hmonic : q.monic) :
    (p.modByMonic q).toPoly = p.toPoly %ₘ q.toPoly
```

`CompPoly.CPolynomial.modByMonic_add_mul_divByMonic` (theorem, [line 506](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/DivisionCorrectness.lean#L506))

> Euclidean division identity for a monic divisor, stated directly on
> `CPolynomial`: `p.modByMonic q + q * p.divByMonic q = p` whenever `q` is monic.
>
> This holds over an arbitrary commutative ring, so it
> instantiates at nested coefficient rings, e.g. `CBivariate R =
> CPolynomial (CPolynomial R)`, giving Euclidean division by any monic divisor in
> the outer variable.

```lean
theorem modByMonic_add_mul_divByMonic (p q : CPolynomial R) (hmonic : q.monic) :
    p.modByMonic q + q * p.divByMonic q = p
```

`CompPoly.CPolynomial.leadingCoeff_inv_smul_monic` (theorem, [line 524](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/DivisionCorrectness.lean#L524))

> Any nonzero polynomial scaled by the inverse of its leading
> coefficient is monic.

```lean
theorem leadingCoeff_inv_smul_monic (p : CPolynomial R) (hp : p ≠ 0) :
    (p.leadingCoeff⁻¹ • p).monic
```

`CompPoly.CPolynomial.div_toPoly_eq_divByMonic` (theorem, [line 530](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/DivisionCorrectness.lean#L530))

> Equality between CompPoly's `div` and Mathlib's `divByMonic`

```lean
theorem div_toPoly_eq_divByMonic (p q : CPolynomial R) (hq : q ≠ 0) :
    (p.div q).toPoly =
      q.leadingCoeff⁻¹ • p.toPoly /ₘ (q.leadingCoeff⁻¹ • q.toPoly)
```

`CompPoly.CPolynomial.mod_toPoly_eq_modByMonic` (theorem, [line 538](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/DivisionCorrectness.lean#L538))

> Equality between CompPoly's `mod` and Mathlib's `modByMonic`

```lean
theorem mod_toPoly_eq_modByMonic (p q : CPolynomial R) (hq : q ≠ 0) :
    (p.mod q).toPoly =
      q.leadingCoeff⁻¹ • p.toPoly %ₘ (q.leadingCoeff⁻¹ • q.toPoly)
```

`CompPoly.CPolynomial.div_toPoly_eq_div` (theorem, [line 546](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/DivisionCorrectness.lean#L546))

> CompPoly's `div` is correct w.r.t. Mathlib's `div`.

```lean
theorem div_toPoly_eq_div (p q : CPolynomial R) :
    (p.div q).toPoly = p.toPoly / q.toPoly
```

`CompPoly.CPolynomial.mod_toPoly_eq_smul_mod` (theorem, [line 554](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/DivisionCorrectness.lean#L554))

> CompPoly's `mod` is Mathlib's `%` scaled by `q.leadingCoeff⁻¹`.

```lean
theorem mod_toPoly_eq_smul_mod (p q : CPolynomial R) :
    (p.mod q).toPoly = q.leadingCoeff⁻¹ • (p.toPoly % q.toPoly)
```

`CompPoly.CPolynomial.exactDiv_toPoly_iff` (theorem, [line 564](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/DivisionCorrectness.lean#L564))

> Exact-division bridge: `G.toPoly` factors as `f.toPoly * V.toPoly` iff the computable
> `mod` vanishes and the computable division recovers `f`.

```lean
theorem exactDiv_toPoly_iff (G V f : CPolynomial R) (hV : V.toPoly ≠ 0) :
    G.toPoly = f.toPoly * V.toPoly ↔ G.mod V = 0 ∧ (G / V).toPoly = f.toPoly
```

`CompPoly.CPolynomial.modByMonicByReversal_eq_modByMonic` (theorem, [line 737](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/DivisionCorrectness.lean#L737))

> The reversal monic remainder agrees with the canonical monic remainder.

```lean
theorem modByMonicByReversal_eq_modByMonic
    (M : Raw.MulLowContext R) (p q : CPolynomial R) :
    modByMonicByReversal M p q = modByMonic p q
```

## Depends on

- [Computable Univariate To `Polynomial`](../part-02/topoly/core.md)

## Proof depends on

- [Degrees and degree bounds under `toPoly`](../part-02/topoly/degree.md)

## Sources

- [CompPoly/Univariate/DivisionCorrectness.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/DivisionCorrectness.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Univariate.DivisionCorrectness.json)
