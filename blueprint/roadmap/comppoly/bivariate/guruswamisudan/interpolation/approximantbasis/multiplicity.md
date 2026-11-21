---
catalog: module
lean: CompPoly.GuruswamiSudan.ApproximantBasis.X_sub_C_pow_dvd_iff_hasseDeriv_eval_eq_zero, CompPoly.GuruswamiSudan.ApproximantBasis.X_sub_C_pow_dvd_hasseDeriv_eval_of_dvd_sub, CompPoly.GuruswamiSudan.ApproximantBasis.X_sub_C_pow_dvd_hasseDeriv_eval_iff_hasMultiplicity, CompPoly.GuruswamiSudan.ApproximantBasis.linearFactor_toPoly_eq, CompPoly.GuruswamiSudan.ApproximantBasis.vanishingPolynomialArray_toPoly, CompPoly.GuruswamiSudan.ApproximantBasis.vanishingPolynomialArray_toPoly_monic, CompPoly.GuruswamiSudan.ApproximantBasis.prod_X_sub_C_pow_dvd_of_nodup, CompPoly.GuruswamiSudan.ApproximantBasis.vanishing_pow_dvd_hasseDeriv_eval_iff_satisfiesMultiplicityConstraints
statement: formalized
proof: formalized
---

# Shear Equivalence for Guruswami-Sudan Multiplicity Constraints

`CompPoly.Bivariate.GuruswamiSudan.Interpolation.ApproximantBasis.Multiplicity`, in [CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Multiplicity.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Multiplicity.lean), by Valerii Huhnin.

> The approximant-basis backend reduces GS interpolation to diagonal modular
> congruences on the `Z^b`-coefficients of the sheared polynomial `Q(X, R + Z)`.
> This file proves the underlying semantic equivalence: for distinct
> interpolation nodes, the packed multiplicity constraints on `Q` hold iff every
> sheared coefficient `C_b = (hasseDeriv b Q.toPoly).eval R` is divisible by
> `G^(s-b)`, where `G` is the vanishing polynomial of the nodes and `R`
> interpolates the values.
>
> The proof works one node at a time.  Writing `M_b = (hasseDeriv b Q.toPoly)`
> for the outer `Y`-Hasse derivatives, multiplicity at `(x, y)` says that the
> family `M_b.eval (C y)` is `(X - x)^(s-b)`-divisible, while the modular
> congruence constrains the family `M_b.eval R`.  Because `R` and `C y` agree at
> `x`, an outer Taylor expansion transfers each divisibility family to the
> other; distinctness of the nodes then glues the per-node factors into powers
> of `G`.

`CompPoly.GuruswamiSudan.ApproximantBasis.X_sub_C_pow_dvd_iff_hasseDeriv_eval_eq_zero` (theorem, [line 53](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Multiplicity.lean#L53))

> `(X - x)^k` divides `A` iff the first `k` Hasse derivatives of `A` vanish
> at `x`.

```lean
theorem X_sub_C_pow_dvd_iff_hasseDeriv_eval_eq_zero
    (A : Polynomial F) (x : F) (k : Nat) :
    (X - C x) ^ k ∣ A ↔
      ∀ a, a < k → (Polynomial.hasseDeriv a A).eval x = 0
```

`CompPoly.GuruswamiSudan.ApproximantBasis.X_sub_C_pow_dvd_hasseDeriv_eval_of_dvd_sub` (theorem, [line 70](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Multiplicity.lean#L70))

> Shear-transfer core: the `(X - x)`-adic divisibility family of the outer
> Hasse-derivative evaluations of `P` moves between outer evaluation points `u`
> and `v` that agree modulo `X - x`.

```lean
theorem X_sub_C_pow_dvd_hasseDeriv_eval_of_dvd_sub
    {P : Polynomial (Polynomial F)} {u v : Polynomial F} {x : F} {s : Nat}
    (huv : (X - C x) ∣ (v - u))
    (h : ∀ b, b < s →
      (X - C x) ^ (s - b) ∣ (Polynomial.hasseDeriv b P).eval u)
    {b : Nat} (hb : b < s) :
    (X - C x) ^ (s - b) ∣ (Polynomial.hasseDeriv b P).eval v
```

`CompPoly.GuruswamiSudan.ApproximantBasis.X_sub_C_pow_dvd_hasseDeriv_eval_iff_hasMultiplicity` (theorem, [line 113](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Multiplicity.lean#L113))

> At a single node `(x, y)` with `R(x) = y`, the `(X - x)`-adic divisibility
> family of the sheared coefficients `(hasseDeriv b Q.toPoly).eval R` is
> equivalent to GS multiplicity of `Q` at the node.

```lean
theorem X_sub_C_pow_dvd_hasseDeriv_eval_iff_hasMultiplicity
    {Q : CBivariate F} {R : Polynomial F} {x y : F} {s : Nat}
    (hRx : R.eval x = y) :
    (∀ b, b < s →
      (X - C x) ^ (s - b) ∣ (Polynomial.hasseDeriv b Q.toPoly).eval R) ↔
      CBivariate.hasMultiplicity Q s x y
```

`CompPoly.GuruswamiSudan.ApproximantBasis.linearFactor_toPoly_eq` (theorem, [line 151](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Multiplicity.lean#L151))

> The linear factor of one node under `toPoly`.

```lean
theorem linearFactor_toPoly_eq (x : F) :
    (CPolynomial.linearFactor x).toPoly = (X - C x : Polynomial F)
```

`CompPoly.GuruswamiSudan.ApproximantBasis.vanishingPolynomialArray_toPoly` (theorem, [line 173](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Multiplicity.lean#L173))

> The array vanishing polynomial is the product of the node linear factors
> under `toPoly`.

```lean
theorem vanishingPolynomialArray_toPoly (xs : Array F) :
    (CPolynomial.vanishingPolynomialArray xs).toPoly =
      (((xs.toList : Multiset F).map fun x ↦
        (X - C x : Polynomial F))).prod
```

`CompPoly.GuruswamiSudan.ApproximantBasis.vanishingPolynomialArray_toPoly_monic` (theorem, [line 184](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Multiplicity.lean#L184))

> The array vanishing polynomial is monic over the underlying `toPoly`
> image.

```lean
theorem vanishingPolynomialArray_toPoly_monic (xs : Array F) :
    Polynomial.Monic (CPolynomial.vanishingPolynomialArray xs).toPoly
```

`CompPoly.GuruswamiSudan.ApproximantBasis.prod_X_sub_C_pow_dvd_of_nodup` (theorem, [line 193](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Multiplicity.lean#L193))

> Per-node `(X - x)^k` divisibility glues to divisibility by the `k`-th
> power of the product of distinct linear factors.

```lean
theorem prod_X_sub_C_pow_dvd_of_nodup
    {A : Polynomial F} {xs : List F} {k : Nat}
    (hA : A ≠ 0) (hnodup : xs.Nodup)
    (hroot : ∀ x, x ∈ xs → (X - C x) ^ k ∣ A) :
    (((xs : Multiset F).map fun x ↦ (X - C x : Polynomial F)).prod) ^ k ∣ A
```

`CompPoly.GuruswamiSudan.ApproximantBasis.vanishing_pow_dvd_hasseDeriv_eval_iff_satisfiesMultiplicityConstraints` (theorem, [line 223](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Multiplicity.lean#L223))

> Batch shear equivalence: over distinct nodes, divisibility of every
> sheared coefficient `C_b` by `G^(s-b)` is equivalent to the packed GS
> multiplicity constraints.

```lean
theorem vanishing_pow_dvd_hasseDeriv_eval_iff_satisfiesMultiplicityConstraints
    {points : Array (F × F)} {Q : CBivariate F} {R : CPolynomial F} {s : Nat}
    (hdistinct : DistinctXCoordinates points)
    (hR : ∀ point, point ∈ points.toList → CPolynomial.eval point.1 R = point.2) :
    (∀ b, b < s →
      (CPolynomial.vanishingPolynomialArray (points.map fun p ↦ p.1)).toPoly ^ (s - b) ∣
        (Polynomial.hasseDeriv b Q.toPoly).eval R.toPoly) ↔
      CBivariate.SatisfiesMultiplicityConstraints Q points s
```

## Depends on

- [Guruswami-Sudan Backend Contexts](../../context.md)
- [Vanishing Polynomials for Array Nodes](../../../../univariate/part-02/vanishing.md)

## Proof depends on

- [Guruswami-Sudan Polynomial Correctness Lemmas](../../polynomialcorrectness.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Multiplicity.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Multiplicity.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Interpolation.ApproximantBasis.Multiplicity.json)
