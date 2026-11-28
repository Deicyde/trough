---
catalog: module
lean: CompPoly.GuruswamiSudan.LeeOSullivan.foldl_range_add_eq_sum, CompPoly.GuruswamiSudan.LeeOSullivan.hasMultiplicityAtLeast_Y_mul, CompPoly.GuruswamiSudan.LeeOSullivan.hasMultiplicityAtLeast_ofYConstant_mul_eval_zero, CompPoly.GuruswamiSudan.LeeOSullivan.hasMultiplicityAtLeast_linearYDivisor_mul, CompPoly.GuruswamiSudan.LeeOSullivan.hasMultiplicityAtLeast_one_zero, CompPoly.GuruswamiSudan.LeeOSullivan.hasMultiplicityAtLeast_Y_pow_mul, CompPoly.GuruswamiSudan.LeeOSullivan.hasMultiplicityAtLeast_ofYConstant_pow_mul_eval_zero, CompPoly.GuruswamiSudan.LeeOSullivan.hasMultiplicityAtLeast_linearYDivisor_pow_mul, CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanBasisPolynomial_hasMultiplicityAtLeast, CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanBasisPolynomial_satisfiesMultiplicityConstraints, CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanBasisPolynomials_satisfiesMultiplicityConstraints, CompPoly.GuruswamiSudan.LeeOSullivan.ofYConstant_one, CompPoly.GuruswamiSudan.LeeOSullivan.ofYConstant_pow, CompPoly.GuruswamiSudan.LeeOSullivan.coeff_ofYConstant_mul_outer, CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanBasisPolynomial_coeffY_self, CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanBasisPolynomial_coeffY_eq_zero_of_idx_lt, CompPoly.GuruswamiSudan.LeeOSullivan.ofYConstant_neg, CompPoly.GuruswamiSudan.LeeOSullivan.ofYConstant_sub, CompPoly.GuruswamiSudan.LeeOSullivan.hasMultiplicityAtLeast_ofYConstant_mul, CompPoly.GuruswamiSudan.LeeOSullivan.hasMultiplicityAtLeast_sub, CompPoly.GuruswamiSudan.LeeOSullivan.satisfiesMultiplicityConstraints_sub
statement: formalized
proof: formalized
---

# Lee-O'Sullivan Basis Correctness Helpers

`CompPoly.Bivariate.GuruswamiSudan.Interpolation.LeeOSullivan.Correctness.Basis`, in [CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Basis.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Basis.lean), by Valerii Huhnin.

> Multiplicity, triangularity, and algebraic closure facts for Lee-O'Sullivan basis polynomials.

`CompPoly.GuruswamiSudan.LeeOSullivan.foldl_range_add_eq_sum` (theorem, [line 30](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Basis.lean#L30))

```lean
theorem foldl_range_add_eq_sum {α : Type*} [AddCommMonoid α]
    (f : Nat → α) :
    ∀ n, (List.range n).foldl (fun acc i ↦ acc + f i) 0 =
      ∑ i ∈ Finset.range n, f i
```

`CompPoly.GuruswamiSudan.LeeOSullivan.hasMultiplicityAtLeast_Y_mul` (theorem, [line 166](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Basis.lean#L166))

```lean
theorem hasMultiplicityAtLeast_Y_mul
    {P : CBivariate F} {x y : F} {m : Nat}
    (hP : CBivariate.HasMultiplicityAtLeast P x y m) :
    CBivariate.HasMultiplicityAtLeast
      ((CBivariate.Y : CBivariate F) * P) x y m
```

`CompPoly.GuruswamiSudan.LeeOSullivan.hasMultiplicityAtLeast_ofYConstant_mul_eval_zero` (theorem, [line 185](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Basis.lean#L185))

```lean
theorem hasMultiplicityAtLeast_ofYConstant_mul_eval_zero
    (A : CPolynomial F) {P : CBivariate F} {x y : F} {m : Nat}
    (hEval : CPolynomial.eval x A = 0)
    (hP : CBivariate.HasMultiplicityAtLeast P x y m) :
    CBivariate.HasMultiplicityAtLeast (CBivariate.ofYConstant A * P) x y (m + 1)
```

`CompPoly.GuruswamiSudan.LeeOSullivan.hasMultiplicityAtLeast_linearYDivisor_mul` (theorem, [line 197](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Basis.lean#L197))

```lean
theorem hasMultiplicityAtLeast_linearYDivisor_mul
    (R : CPolynomial F) {P : CBivariate F} {x y : F} {m : Nat}
    (hEval : CPolynomial.eval x R = y)
    (hP : CBivariate.HasMultiplicityAtLeast P x y m) :
    CBivariate.HasMultiplicityAtLeast
      (CBivariate.linearYDivisor R * P) x y (m + 1)
```

`CompPoly.GuruswamiSudan.LeeOSullivan.hasMultiplicityAtLeast_one_zero` (theorem, [line 224](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Basis.lean#L224))

```lean
theorem hasMultiplicityAtLeast_one_zero
    (x y : F) :
    CBivariate.HasMultiplicityAtLeast (1 : CBivariate F) x y 0
```

`CompPoly.GuruswamiSudan.LeeOSullivan.hasMultiplicityAtLeast_Y_pow_mul` (theorem, [line 230](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Basis.lean#L230))

```lean
theorem hasMultiplicityAtLeast_Y_pow_mul
    (n : Nat) {P : CBivariate F} {x y : F} {m : Nat}
    (hP : CBivariate.HasMultiplicityAtLeast P x y m) :
    CBivariate.HasMultiplicityAtLeast
      ((CBivariate.Y : CBivariate F) ^ n * P) x y m
```

`CompPoly.GuruswamiSudan.LeeOSullivan.hasMultiplicityAtLeast_ofYConstant_pow_mul_eval_zero` (theorem, [line 242](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Basis.lean#L242))

```lean
theorem hasMultiplicityAtLeast_ofYConstant_pow_mul_eval_zero
    (A : CPolynomial F) (n : Nat) {P : CBivariate F} {x y : F} {m : Nat}
    (hEval : CPolynomial.eval x A = 0)
    (hP : CBivariate.HasMultiplicityAtLeast P x y m) :
    CBivariate.HasMultiplicityAtLeast
      ((CBivariate.ofYConstant A) ^ n * P) x y (m + n)
```

`CompPoly.GuruswamiSudan.LeeOSullivan.hasMultiplicityAtLeast_linearYDivisor_pow_mul` (theorem, [line 261](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Basis.lean#L261))

```lean
theorem hasMultiplicityAtLeast_linearYDivisor_pow_mul
    (R : CPolynomial F) (n : Nat) {P : CBivariate F} {x y : F} {m : Nat}
    (hEval : CPolynomial.eval x R = y)
    (hP : CBivariate.HasMultiplicityAtLeast P x y m) :
    CBivariate.HasMultiplicityAtLeast
      ((CBivariate.linearYDivisor R) ^ n * P) x y (m + n)
```

`CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanBasisPolynomial_hasMultiplicityAtLeast` (theorem, [line 280](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Basis.lean#L280))

```lean
theorem leeOSullivanBasisPolynomial_hasMultiplicityAtLeast
    (R G : CPolynomial F) (params : GSInterpParams) (idx : Nat)
    {x y : F}
    (hR : CPolynomial.eval x R = y)
    (hG : CPolynomial.eval x G = 0) :
    CBivariate.HasMultiplicityAtLeast
      (leeOSullivanBasisPolynomial R G params idx) x y params.multiplicity
```

`CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanBasisPolynomial_satisfiesMultiplicityConstraints` (theorem, [line 316](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Basis.lean#L316))

```lean
theorem leeOSullivanBasisPolynomial_satisfiesMultiplicityConstraints
    (R G : CPolynomial F) (params : GSInterpParams) (idx : Nat)
    {points : Array (F × F)}
    (hR : ∀ point, point ∈ points.toList → CPolynomial.eval point.1 R = point.2)
    (hG : ∀ point, point ∈ points.toList → CPolynomial.eval point.1 G = 0) :
    CBivariate.SatisfiesMultiplicityConstraints
      (leeOSullivanBasisPolynomial R G params idx) points params.multiplicity
```

`CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanBasisPolynomials_satisfiesMultiplicityConstraints` (theorem, [line 327](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Basis.lean#L327))

```lean
theorem leeOSullivanBasisPolynomials_satisfiesMultiplicityConstraints
    (R G : CPolynomial F) (params : GSInterpParams)
    {points : Array (F × F)}
    (hR : ∀ point, point ∈ points.toList → CPolynomial.eval point.1 R = point.2)
    (hG : ∀ point, point ∈ points.toList → CPolynomial.eval point.1 G = 0) :
    ∀ idx, idx < (leeOSullivanBasisPolynomials (F := F) R G params).size →
      CBivariate.SatisfiesMultiplicityConstraints
        ((leeOSullivanBasisPolynomials (F := F) R G params).getD idx 0)
        points params.multiplicity
```

`CompPoly.GuruswamiSudan.LeeOSullivan.ofYConstant_one` (theorem, [line 343](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Basis.lean#L343))

```lean
theorem ofYConstant_one :
    CBivariate.ofYConstant (1 : CPolynomial F) = (1 : CBivariate F)
```

`CompPoly.GuruswamiSudan.LeeOSullivan.ofYConstant_pow` (theorem, [line 352](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Basis.lean#L352))

```lean
theorem ofYConstant_pow
    (P : CPolynomial F) :
    ∀ n, CBivariate.ofYConstant (P ^ n) =
      (CBivariate.ofYConstant P : CBivariate F) ^ n
```

`CompPoly.GuruswamiSudan.LeeOSullivan.coeff_ofYConstant_mul_outer` (theorem, [line 362](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Basis.lean#L362))

```lean
theorem coeff_ofYConstant_mul_outer
    (A : CPolynomial F) (P : CBivariate F) (j : Nat) :
    CPolynomial.coeff (CBivariate.ofYConstant A * P) j =
      A * CPolynomial.coeff P j
```

`CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanBasisPolynomial_coeffY_self` (theorem, [line 462](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Basis.lean#L462))

```lean
theorem leeOSullivanBasisPolynomial_coeffY_self
    (R G : CPolynomial F) (params : GSInterpParams) (idx : Nat) :
    CPolynomial.coeff (leeOSullivanBasisPolynomial R G params idx) idx =
      G ^ (params.multiplicity - leeOSullivanT params idx)
```

`CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanBasisPolynomial_coeffY_eq_zero_of_idx_lt` (theorem, [line 488](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Basis.lean#L488))

> Lee basis polynomials have no `Y` terms above their row index.

```lean
theorem leeOSullivanBasisPolynomial_coeffY_eq_zero_of_idx_lt
    (R G : CPolynomial F) (params : GSInterpParams) {idx j : Nat}
    (hj : idx < j) :
    CPolynomial.coeff (leeOSullivanBasisPolynomial R G params idx) j = 0
```

`CompPoly.GuruswamiSudan.LeeOSullivan.ofYConstant_neg` (theorem, [line 556](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Basis.lean#L556))

```lean
theorem ofYConstant_neg
    (P : CPolynomial F) :
    CBivariate.ofYConstant (-P) = -CBivariate.ofYConstant P
```

`CompPoly.GuruswamiSudan.LeeOSullivan.ofYConstant_sub` (theorem, [line 568](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Basis.lean#L568))

```lean
theorem ofYConstant_sub
    (P Q : CPolynomial F) :
    CBivariate.ofYConstant (P - Q) =
      CBivariate.ofYConstant P - CBivariate.ofYConstant Q
```

`CompPoly.GuruswamiSudan.LeeOSullivan.hasMultiplicityAtLeast_ofYConstant_mul` (theorem, [line 576](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Basis.lean#L576))

> Multiplication by a `Y`-constant polynomial preserves multiplicity
> constraints already satisfied by the bivariate factor.

```lean
theorem hasMultiplicityAtLeast_ofYConstant_mul
    (A : CPolynomial F) {P : CBivariate F} {x y : F} {m : Nat}
    (hP : CBivariate.HasMultiplicityAtLeast P x y m) :
    CBivariate.HasMultiplicityAtLeast (CBivariate.ofYConstant A * P) x y m
```

`CompPoly.GuruswamiSudan.LeeOSullivan.hasMultiplicityAtLeast_sub` (theorem, [line 586](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Basis.lean#L586))

```lean
theorem hasMultiplicityAtLeast_sub
    {P Q : CBivariate F} {x y : F} {m : Nat}
    (hP : CBivariate.HasMultiplicityAtLeast P x y m)
    (hQ : CBivariate.HasMultiplicityAtLeast Q x y m) :
    CBivariate.HasMultiplicityAtLeast (P - Q) x y m
```

`CompPoly.GuruswamiSudan.LeeOSullivan.satisfiesMultiplicityConstraints_sub` (theorem, [line 595](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Basis.lean#L595))

```lean
theorem satisfiesMultiplicityConstraints_sub
    {P Q : CBivariate F} {points : Array (F × F)} {m : Nat}
    (hP : CBivariate.SatisfiesMultiplicityConstraints P points m)
    (hQ : CBivariate.SatisfiesMultiplicityConstraints Q points m) :
    CBivariate.SatisfiesMultiplicityConstraints (P - Q) points m
```

## Depends on

- [Lee-O'Sullivan Correctness Common Helpers](common.md)

## Proof depends on

- [Generic Basis Combination Helpers](combinations.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Basis.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Basis.lean)
- [Declaration ledger](../../../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Interpolation.LeeOSullivan.Correctness.Basis.json)
