---
catalog: module
lean: CompPoly.GuruswamiSudan.ApproximantBasis.ofFn_rowGet, CompPoly.GuruswamiSudan.ApproximantBasis.ofFn_size, CompPoly.GuruswamiSudan.ApproximantBasis.ofFn_matrixWidth, CompPoly.GuruswamiSudan.ApproximantBasis.modByMonicWith_toPoly, CompPoly.GuruswamiSudan.ApproximantBasis.dvd_modByMonicWith_sub, CompPoly.GuruswamiSudan.ApproximantBasis.modByMonicWith_eq_zero_iff_dvd, CompPoly.GuruswamiSudan.ApproximantBasis.gsModuli_eq, CompPoly.GuruswamiSudan.ApproximantBasis.gsModuli_size, CompPoly.GuruswamiSudan.ApproximantBasis.gsModuli_getD, CompPoly.GuruswamiSudan.ApproximantBasis.gsRelationColumn_size, CompPoly.GuruswamiSudan.ApproximantBasis.gsRelationColumn_getD_of_lt, CompPoly.GuruswamiSudan.ApproximantBasis.gsRelationColumn_getD_congr, CompPoly.GuruswamiSudan.ApproximantBasis.gsModuli_getD_one, CompPoly.GuruswamiSudan.ApproximantBasis.gsRelationMatrixWithModuli_entry, CompPoly.GuruswamiSudan.ApproximantBasis.gsRelationMatrixWithModuli_size, CompPoly.GuruswamiSudan.ApproximantBasis.gsRelationMatrixWithModuli_matrixWidth, CompPoly.GuruswamiSudan.ApproximantBasis.hasseDeriv_toPoly_ofCoeffRow_eval, CompPoly.GuruswamiSudan.ApproximantBasis.rowMulMatrixWith_congr_of_agree, CompPoly.GuruswamiSudan.ApproximantBasis.rowSatisfiesModularBool_congr_of_agree, CompPoly.GuruswamiSudan.ApproximantBasis.rowSatisfiesModularBool_gsRelationMatrix_iff
statement: formalized
proof: formalized
---

# Executable GS Modular-Data Bridges

`CompPoly.Bivariate.GuruswamiSudan.Interpolation.ApproximantBasis.ModularData`, in [CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/ModularData.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/ModularData.lean), by Valerii Huhnin.

> Semantic characterizations of the executable approximant-basis modular data:
> the modulus array `gsModuli`, the incrementally built binomial relation matrix
> `gsRelationColumn` / `gsRelationMatrixWithModuli`, and the executable row
> predicate `rowSatisfiesModularBool`.  The main result identifies the modular
> row predicate over the GS data with divisibility of every sheared coefficient
> `(hasseDeriv b Q.toPoly).eval R` by `G^(s-b)`.

> ## Generic helpers

`CompPoly.GuruswamiSudan.ApproximantBasis.ofFn_rowGet` (theorem, [line 95](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/ModularData.lean#L95))

> Entry access for `PolynomialMatrix.ofFn`.

```lean
theorem ofFn_rowGet (rows width : Nat) (entry : Nat → Nat → CPolynomial F)
    {i j : Nat} (hi : i < rows) (hj : j < width) :
    rowGet ((PolynomialMatrix.ofFn rows width entry).getD i #[]) j = entry i j
```

`CompPoly.GuruswamiSudan.ApproximantBasis.ofFn_size` (theorem, [line 107](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/ModularData.lean#L107))

> Row count of `PolynomialMatrix.ofFn`.

```lean
theorem ofFn_size (rows width : Nat) (entry : Nat → Nat → CPolynomial F) :
    (PolynomialMatrix.ofFn rows width entry).size = rows
```

`CompPoly.GuruswamiSudan.ApproximantBasis.ofFn_matrixWidth` (theorem, [line 113](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/ModularData.lean#L113))

> Width of `PolynomialMatrix.ofFn` with at least one row.

```lean
theorem ofFn_matrixWidth (rows width : Nat) (entry : Nat → Nat → CPolynomial F)
    (hrows : 0 < rows) :
    MatrixWidth (PolynomialMatrix.ofFn rows width entry) = width
```

> ## Modular reduction semantics

`CompPoly.GuruswamiSudan.ApproximantBasis.modByMonicWith_toPoly` (theorem, [line 128](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/ModularData.lean#L128))

> `modByMonicWith` computes the Mathlib monic remainder under `toPoly`.

```lean
theorem modByMonicWith_toPoly (modCtx : CPolynomial.ModContext F)
    {p M : CPolynomial F} (hM : Polynomial.Monic M.toPoly) :
    (PolynomialMatrix.modByMonicWith modCtx p M).toPoly = p.toPoly %ₘ M.toPoly
```

`CompPoly.GuruswamiSudan.ApproximantBasis.dvd_modByMonicWith_sub` (theorem, [line 143](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/ModularData.lean#L143))

> `modByMonicWith` is congruent to the identity modulo the modulus.

```lean
theorem dvd_modByMonicWith_sub (modCtx : CPolynomial.ModContext F)
    {p M : CPolynomial F} (hM : Polynomial.Monic M.toPoly) :
    M.toPoly ∣ (PolynomialMatrix.modByMonicWith modCtx p M).toPoly - p.toPoly
```

`CompPoly.GuruswamiSudan.ApproximantBasis.modByMonicWith_eq_zero_iff_dvd` (theorem, [line 153](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/ModularData.lean#L153))

> The executable remainder vanishes exactly on multiples of the modulus.

```lean
theorem modByMonicWith_eq_zero_iff_dvd (modCtx : CPolynomial.ModContext F)
    {p M : CPolynomial F} (hM : Polynomial.Monic M.toPoly) :
    PolynomialMatrix.modByMonicWith modCtx p M = 0 ↔ M.toPoly ∣ p.toPoly
```

> ## The GS modulus array

`CompPoly.GuruswamiSudan.ApproximantBasis.gsModuli_eq` (theorem, [line 208](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/ModularData.lean#L208))

> Closed form for the GS modulus array before reversal.

```lean
theorem gsModuli_eq (mulCtx : CPolynomial.MulContext F) (G : CPolynomial F) (s : Nat) :
    gsModuli mulCtx G s = (((List.range s).map fun i ↦ G ^ (i + 1)).toArray).reverse
```

`CompPoly.GuruswamiSudan.ApproximantBasis.gsModuli_size` (theorem, [line 230](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/ModularData.lean#L230))

> The GS modulus array has one modulus per multiplicity level.

```lean
theorem gsModuli_size (mulCtx : CPolynomial.MulContext F) (G : CPolynomial F) (s : Nat) :
    (gsModuli mulCtx G s).size = s
```

`CompPoly.GuruswamiSudan.ApproximantBasis.gsModuli_getD` (theorem, [line 237](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/ModularData.lean#L237))

> The `b`-th GS modulus is `G^(s-b)`.

```lean
theorem gsModuli_getD (mulCtx : CPolynomial.MulContext F) (G : CPolynomial F)
    {b s : Nat} (hb : b < s) :
    (gsModuli mulCtx G s).getD b 0 = G ^ (s - b)
```

> ## The GS relation column

`CompPoly.GuruswamiSudan.ApproximantBasis.gsRelationColumn_size` (theorem, [line 411](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/ModularData.lean#L411))

> Size of the GS relation column.

```lean
theorem gsRelationColumn_size (mulCtx : CPolynomial.MulContext F)
    (modCtx : CPolynomial.ModContext F) (R modulus : CPolynomial F) (width b : Nat) :
    (gsRelationColumn mulCtx modCtx R modulus width b).size = width
```

`CompPoly.GuruswamiSudan.ApproximantBasis.gsRelationColumn_getD_of_lt` (theorem, [line 422](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/ModularData.lean#L422))

> Entries of the GS relation column below the diagonal vanish.

```lean
theorem gsRelationColumn_getD_of_lt (mulCtx : CPolynomial.MulContext F)
    (modCtx : CPolynomial.ModContext F) (R modulus : CPolynomial F)
    {width b j : Nat} (hj : j < b) :
    (gsRelationColumn mulCtx modCtx R modulus width b).getD j 0 = 0
```

`CompPoly.GuruswamiSudan.ApproximantBasis.gsRelationColumn_getD_congr` (theorem, [line 435](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/ModularData.lean#L435))

> Entries of the GS relation column are congruent to the binomial powers.

```lean
theorem gsRelationColumn_getD_congr (mulCtx : CPolynomial.MulContext F)
    (modCtx : CPolynomial.ModContext F) {R modulus : CPolynomial F}
    (hM : Polynomial.Monic modulus.toPoly)
    {width b j : Nat} (hbj : b ≤ j) (hj : j < width) :
    modulus.toPoly ∣
      ((gsRelationColumn mulCtx modCtx R modulus width b).getD j 0).toPoly -
        Polynomial.C ((j.choose b : F)) * R.toPoly ^ (j - b)
```

> ## The GS relation matrix and the modular row predicate

`CompPoly.GuruswamiSudan.ApproximantBasis.gsModuli_getD_one` (theorem, [line 454](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/ModularData.lean#L454))

> The `b`-th GS modulus is `G^(s-b)`, with default value `1`.

```lean
theorem gsModuli_getD_one (mulCtx : CPolynomial.MulContext F) (G : CPolynomial F)
    {b s : Nat} (hb : b < s) :
    (gsModuli mulCtx G s).getD b 1 = G ^ (s - b)
```

`CompPoly.GuruswamiSudan.ApproximantBasis.gsRelationMatrixWithModuli_entry` (theorem, [line 465](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/ModularData.lean#L465))

> Entry access for the GS relation matrix.

```lean
theorem gsRelationMatrixWithModuli_entry (mulCtx : CPolynomial.MulContext F)
    (modCtx : CPolynomial.ModContext F) (R : CPolynomial F)
    (moduli : Array (CPolynomial F)) (params : GSInterpParams) {k b : Nat}
    (hk : k < interpolationWidth params) (hb : b < params.multiplicity) :
    rowGet ((gsRelationMatrixWithModuli mulCtx modCtx R moduli params).getD k #[]) b =
      (gsRelationColumn mulCtx modCtx R (moduli.getD b 1)
        (interpolationWidth params) b).getD k 0
```

`CompPoly.GuruswamiSudan.ApproximantBasis.gsRelationMatrixWithModuli_size` (theorem, [line 479](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/ModularData.lean#L479))

> The GS relation matrix has one row per interpolation coefficient.

```lean
theorem gsRelationMatrixWithModuli_size (mulCtx : CPolynomial.MulContext F)
    (modCtx : CPolynomial.ModContext F) (R : CPolynomial F)
    (moduli : Array (CPolynomial F)) (params : GSInterpParams) :
    (gsRelationMatrixWithModuli mulCtx modCtx R moduli params).size =
      interpolationWidth params
```

`CompPoly.GuruswamiSudan.ApproximantBasis.gsRelationMatrixWithModuli_matrixWidth` (theorem, [line 488](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/ModularData.lean#L488))

> The GS relation matrix has one column per multiplicity level.

```lean
theorem gsRelationMatrixWithModuli_matrixWidth (mulCtx : CPolynomial.MulContext F)
    (modCtx : CPolynomial.ModContext F) (R : CPolynomial F)
    (moduli : Array (CPolynomial F)) (params : GSInterpParams) :
    MatrixWidth (gsRelationMatrixWithModuli mulCtx modCtx R moduli params) =
      params.multiplicity
```

`CompPoly.GuruswamiSudan.ApproximantBasis.hasseDeriv_toPoly_ofCoeffRow_eval` (theorem, [line 520](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/ModularData.lean#L520))

> Sheared coefficients of a coefficient row: the outer Hasse derivative of
> `ofCoeffRow row` evaluated at `R` is the binomial-weighted power sum.

```lean
theorem hasseDeriv_toPoly_ofCoeffRow_eval (row : PolynomialRow F)
    (R : Polynomial F) (b : Nat) :
    (Polynomial.hasseDeriv b (CBivariate.ofCoeffRow row).toPoly).eval R =
      ∑ k ∈ Finset.range row.size,
        Polynomial.C ((k.choose b : F)) * (row.getD k 0).toPoly * R ^ (k - b)
```

`CompPoly.GuruswamiSudan.ApproximantBasis.rowMulMatrixWith_congr_of_agree` (theorem, [line 574](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/ModularData.lean#L574))

> The row-by-matrix product only sees the first `M.size` row entries.

```lean
theorem rowMulMatrixWith_congr_of_agree (mulCtx : CPolynomial.MulContext F)
    {row row' : PolynomialRow F} (M : PolynomialMatrix F)
    (hagree : ∀ k, k < M.size → rowGet row k = rowGet row' k) :
    rowMulMatrixWith mulCtx row M = rowMulMatrixWith mulCtx row' M
```

`CompPoly.GuruswamiSudan.ApproximantBasis.rowSatisfiesModularBool_congr_of_agree` (theorem, [line 587](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/ModularData.lean#L587))

> The modular row predicate only sees the first `M.size` row entries.

```lean
theorem rowSatisfiesModularBool_congr_of_agree (mulCtx : CPolynomial.MulContext F)
    (modCtx : CPolynomial.ModContext F) {row row' : PolynomialRow F}
    (M : PolynomialMatrix F) (moduli : Array (CPolynomial F))
    (hagree : ∀ k, k < M.size → rowGet row k = rowGet row' k) :
    rowSatisfiesModularBool mulCtx modCtx row M moduli =
      rowSatisfiesModularBool mulCtx modCtx row' M moduli
```

`CompPoly.GuruswamiSudan.ApproximantBasis.rowSatisfiesModularBool_gsRelationMatrix_iff` (theorem, [line 623](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/ModularData.lean#L623))

> The executable GS modular row predicate over the relation matrix and
> modulus array is exactly divisibility of every sheared coefficient
> `(hasseDeriv b (ofCoeffRow row).toPoly).eval R` by `G^(s-b)`.

```lean
theorem rowSatisfiesModularBool_gsRelationMatrix_iff
    (mulCtx : CPolynomial.MulContext F) (modCtx : CPolynomial.ModContext F)
    {G : CPolynomial F} (hG : Polynomial.Monic G.toPoly)
    (R : CPolynomial F) (params : GSInterpParams) {row : PolynomialRow F}
    (hwidth : row.size ≤ interpolationWidth params) :
    rowSatisfiesModularBool mulCtx modCtx row
        (gsRelationMatrixWithRG mulCtx modCtx R G params)
        (gsModuli mulCtx G params.multiplicity) = true ↔
      ∀ b, b < params.multiplicity →
        G.toPoly ^ (params.multiplicity - b) ∣
          (Polynomial.hasseDeriv b (CBivariate.ofCoeffRow row).toPoly).eval R.toPoly
```

## Depends on

- [Approximant-Basis Guruswami-Sudan Modular Data](basic.md)

## Proof depends on

- [Filtered Modular Solver Completeness](../../../../linearalgebra/polynomialmatrix/approximant/modularequation-2/completeness.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/ModularData.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/ModularData.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Interpolation.ApproximantBasis.ModularData.json)
