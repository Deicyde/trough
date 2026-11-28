---
catalog: module
lean: CompPoly.CBivariate.coeff_neg, CompPoly.CBivariate.coeff_sub, CompPoly.CBivariate.coeff_CC_mul, CompPoly.CBivariate.coeff_X_mul_zero, CompPoly.CBivariate.coeff_X_mul_succ, CompPoly.CBivariate.evalEval_CC_mul, CompPoly.CBivariate.evalEval_X_mul, CompPoly.CBivariate.evalEval_sub, CompPoly.CBivariate.hasseDerivative_sub, CompPoly.CBivariate.hasseDerivative_CC_mul, CompPoly.CBivariate.hasseDerivative_X_mul_zero_xOrder, CompPoly.CBivariate.hasseDerivative_X_mul_succ_xOrder, CompPoly.CBivariate.hasseDerivativeEval_CC_mul, CompPoly.CBivariate.hasseDerivativeEval_sub, CompPoly.CBivariate.hasseDerivativeEval_X_mul_zero_xOrder, CompPoly.CBivariate.hasseDerivativeEval_X_mul_succ_xOrder, CompPoly.GuruswamiSudan.koetterYCap, CompPoly.GuruswamiSudan.coeff_ofYCoefficient, CompPoly.GuruswamiSudan.coeff_ofYConstant, CompPoly.GuruswamiSudan.coeff_ofYConstant_mul, CompPoly.GuruswamiSudan.natWeightedDegree_ofYConstant_mul_le, CompPoly.GuruswamiSudan.validWitness_coeffY_eq_zero_of_yCap_lt, CompPoly.GuruswamiSudan.ofYConstant_zero, CompPoly.GuruswamiSudan.ofYConstant_add, CompPoly.GuruswamiSudan.ofYConstant_C, CompPoly.GuruswamiSudan.ofYConstant_mul, CompPoly.GuruswamiSudan.ofYConstant_X_mul, CompPoly.GuruswamiSudan.cpoly_eq_zero_of_val_size_eq_zero, CompPoly.GuruswamiSudan.hasseDerivativeEval_ofYConstant_mul_eq_eval_mul_of_lower, CompPoly.GuruswamiSudan.hasseDerivativeEval_ofYConstant_mul_eq_zero_of_lower, CompPoly.GuruswamiSudan.foldl_add_congr_terms, CompPoly.GuruswamiSudan.foldl_add_distrib_terms_aux, CompPoly.GuruswamiSudan.foldl_add_distrib_terms, CompPoly.GuruswamiSudan.foldl_add_single_beq_of_not_mem, CompPoly.GuruswamiSudan.foldl_add_single_beq_of_nodup_mem, CompPoly.GuruswamiSudan.koetterBasisCombination, CompPoly.GuruswamiSudan.koetterBasisSpanContains, CompPoly.GuruswamiSudan.koetterBasisCombination_eq_zero_of_weights_zero, CompPoly.GuruswamiSudan.coeff_koetterBasisCombination
statement: formalized
proof: formalized
---

# Generic Basis Combination Helpers

`CompPoly.Bivariate.GuruswamiSudan.Interpolation.LeeOSullivan.Correctness.Combinations`, in [CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean), by Valerii Huhnin.

> Generic finite-Y and basis-combination lemmas used by Lee-O'Sullivan correctness.

`CompPoly.CBivariate.coeff_neg` (theorem, [line 23](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L23))

```lean
theorem coeff_neg {R : Type*}
    [Ring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (P : CBivariate R) (i j : Nat) :
    coeff (-P) i j = -coeff P i j
```

`CompPoly.CBivariate.coeff_sub` (theorem, [line 34](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L34))

```lean
theorem coeff_sub {R : Type*}
    [Ring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (P Q : CBivariate R) (i j : Nat) :
    coeff (P - Q) i j = coeff P i j - coeff Q i j
```

`CompPoly.CBivariate.coeff_CC_mul` (theorem, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L46))

```lean
theorem coeff_CC_mul {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (c : R) (Q : CBivariate R) (i j : Nat) :
    coeff (CC c * Q) i j = c * coeff Q i j
```

`CompPoly.CBivariate.coeff_X_mul_zero` (theorem, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L57))

```lean
theorem coeff_X_mul_zero {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (Q : CBivariate R) (j : Nat) :
    coeff (X * Q) 0 j = 0
```

`CompPoly.CBivariate.coeff_X_mul_succ` (theorem, [line 67](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L67))

```lean
theorem coeff_X_mul_succ {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (Q : CBivariate R) (i j : Nat) :
    coeff (X * Q) (i + 1) j = coeff Q i j
```

`CompPoly.CBivariate.evalEval_CC_mul` (theorem, [line 78](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L78))

```lean
theorem evalEval_CC_mul {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (c x y : F) (Q : CBivariate F) :
    evalEval x y (CC c * Q) = c * evalEval x y Q
```

`CompPoly.CBivariate.evalEval_X_mul` (theorem, [line 85](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L85))

```lean
theorem evalEval_X_mul {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (x y : F) (Q : CBivariate F) :
    evalEval x y (X * Q) = x * evalEval x y Q
```

`CompPoly.CBivariate.evalEval_sub` (theorem, [line 92](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L92))

```lean
theorem evalEval_sub {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (x y : F) (P Q : CBivariate F) :
    evalEval x y (P - Q) = evalEval x y P - evalEval x y Q
```

`CompPoly.CBivariate.hasseDerivative_sub` (theorem, [line 102](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L102))

```lean
theorem hasseDerivative_sub {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (a b : Nat) (P Q : CBivariate F) :
    hasseDerivative a b (P - Q) =
      hasseDerivative a b P - hasseDerivative a b Q
```

`CompPoly.CBivariate.hasseDerivative_CC_mul` (theorem, [line 113](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L113))

```lean
theorem hasseDerivative_CC_mul {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (c : F) (a b : Nat) (Q : CBivariate F) :
    hasseDerivative a b (CC c * Q) = CC c * hasseDerivative a b Q
```

`CompPoly.CBivariate.hasseDerivative_X_mul_zero_xOrder` (theorem, [line 122](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L122))

```lean
theorem hasseDerivative_X_mul_zero_xOrder {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (b : Nat) (Q : CBivariate F) :
    hasseDerivative 0 b (X * Q) = X * hasseDerivative 0 b Q
```

`CompPoly.CBivariate.hasseDerivative_X_mul_succ_xOrder` (theorem, [line 137](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L137))

```lean
theorem hasseDerivative_X_mul_succ_xOrder {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (a b : Nat) (Q : CBivariate F) :
    hasseDerivative (a + 1) b (X * Q) =
      X * hasseDerivative (a + 1) b Q + hasseDerivative a b Q
```

`CompPoly.CBivariate.hasseDerivativeEval_CC_mul` (theorem, [line 168](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L168))

```lean
theorem hasseDerivativeEval_CC_mul {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (c : F) (a b : Nat) (x y : F) (Q : CBivariate F) :
    hasseDerivativeEval a b x y (CC c * Q) =
      c * hasseDerivativeEval a b x y Q
```

`CompPoly.CBivariate.hasseDerivativeEval_sub` (theorem, [line 178](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L178))

```lean
theorem hasseDerivativeEval_sub {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (a b : Nat) (x y : F) (P Q : CBivariate F) :
    hasseDerivativeEval a b x y (P - Q) =
      hasseDerivativeEval a b x y P - hasseDerivativeEval a b x y Q
```

`CompPoly.CBivariate.hasseDerivativeEval_X_mul_zero_xOrder` (theorem, [line 188](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L188))

```lean
theorem hasseDerivativeEval_X_mul_zero_xOrder {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (b : Nat) (x y : F) (Q : CBivariate F) :
    hasseDerivativeEval 0 b x y (X * Q) =
      x * hasseDerivativeEval 0 b x y Q
```

`CompPoly.CBivariate.hasseDerivativeEval_X_mul_succ_xOrder` (theorem, [line 198](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L198))

```lean
theorem hasseDerivativeEval_X_mul_succ_xOrder {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (a b : Nat) (x y : F) (Q : CBivariate F) :
    hasseDerivativeEval (a + 1) b x y (X * Q) =
      x * hasseDerivativeEval (a + 1) b x y Q +
        hasseDerivativeEval a b x y Q
```

`CompPoly.GuruswamiSudan.koetterYCap` (definition, [line 214](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L214))

> Finite `Y` cap shared by positive-`Y`-weight interpolation proofs.

```lean
def koetterYCap (params : GSInterpParams) : Nat
```

`CompPoly.GuruswamiSudan.coeff_ofYCoefficient` (theorem, [line 217](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L217))

```lean
theorem coeff_ofYCoefficient {F : Type*}
    [Semiring F] [BEq F] [LawfulBEq F] [Nontrivial F] [DecidableEq F]
    (j : Nat) (P : CPolynomial F) (i k : Nat) :
    CBivariate.coeff (CBivariate.ofYCoefficient j P) i k =
      if k = j then P.coeff i else 0
```

`CompPoly.GuruswamiSudan.coeff_ofYConstant` (theorem, [line 239](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L239))

```lean
theorem coeff_ofYConstant {F : Type*}
    [Semiring F] [BEq F] [LawfulBEq F] [Nontrivial F]
    (P : CPolynomial F) (i j : Nat) :
    CBivariate.coeff (CBivariate.ofYConstant P) i j =
      if j = 0 then P.coeff i else 0
```

`CompPoly.GuruswamiSudan.coeff_ofYConstant_mul` (theorem, [line 260](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L260))

```lean
theorem coeff_ofYConstant_mul {F : Type*}
    [Semiring F] [BEq F] [LawfulBEq F] [Nontrivial F]
    (A : CPolynomial F) (P : CBivariate F) (i j : Nat) :
    CBivariate.coeff (CBivariate.ofYConstant A * P) i j =
      (A * P.val.coeff j).coeff i
```

`CompPoly.GuruswamiSudan.natWeightedDegree_ofYConstant_mul_le` (theorem, [line 275](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L275))

```lean
theorem natWeightedDegree_ofYConstant_mul_le {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (A : CPolynomial F) (P : CBivariate F) (w : Nat) :
    CBivariate.natWeightedDegree (CBivariate.ofYConstant A * P) 1 w ≤
      A.natDegree + CBivariate.natWeightedDegree P 1 w
```

`CompPoly.GuruswamiSudan.validWitness_coeffY_eq_zero_of_yCap_lt` (theorem, [line 305](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L305))

```lean
theorem validWitness_coeffY_eq_zero_of_yCap_lt {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {points : Array (F × F)} {params : GSInterpParams} {Q : CBivariate F}
    (hMessage : ¬ params.messageDegree ≤ 1)
    (hQ : ValidInterpolationWitness points params Q) {j : Nat}
    (hj : koetterYCap params < j) :
    Q.val.coeff j = 0
```

`CompPoly.GuruswamiSudan.ofYConstant_zero` (theorem, [line 332](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L332))

```lean
theorem ofYConstant_zero {F : Type*}
    [Semiring F] [BEq F] [LawfulBEq F] [Nontrivial F] :
    CBivariate.ofYConstant (0 : CPolynomial F) = 0
```

`CompPoly.GuruswamiSudan.ofYConstant_add` (theorem, [line 343](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L343))

```lean
theorem ofYConstant_add {F : Type*}
    [Semiring F] [BEq F] [LawfulBEq F] [Nontrivial F]
    (P Q : CPolynomial F) :
    CBivariate.ofYConstant (P + Q) =
      CBivariate.ofYConstant P + CBivariate.ofYConstant Q
```

`CompPoly.GuruswamiSudan.ofYConstant_C` (theorem, [line 356](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L356))

```lean
theorem ofYConstant_C {F : Type*}
    [Semiring F] [BEq F] [LawfulBEq F] [Nontrivial F] (c : F) :
    CBivariate.ofYConstant (CPolynomial.C c) = CBivariate.CC c
```

`CompPoly.GuruswamiSudan.ofYConstant_mul` (theorem, [line 361](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L361))

```lean
theorem ofYConstant_mul {F : Type*}
    [Semiring F] [BEq F] [LawfulBEq F] [Nontrivial F]
    (P Q : CPolynomial F) :
    CBivariate.ofYConstant (P * Q) =
      CBivariate.ofYConstant P * CBivariate.ofYConstant Q
```

`CompPoly.GuruswamiSudan.ofYConstant_X_mul` (theorem, [line 394](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L394))

```lean
theorem ofYConstant_X_mul {F : Type*}
    [Semiring F] [BEq F] [LawfulBEq F] [Nontrivial F]
    (P : CPolynomial F) :
    CBivariate.ofYConstant (CPolynomial.X * P) =
      CBivariate.X * CBivariate.ofYConstant P
```

`CompPoly.GuruswamiSudan.cpoly_eq_zero_of_val_size_eq_zero` (theorem, [line 428](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L428))

```lean
theorem cpoly_eq_zero_of_val_size_eq_zero {F : Type*}
    [Zero F] [BEq F] [LawfulBEq F] (P : CPolynomial F)
    (hsize : P.val.size = 0) :
    P = 0
```

`CompPoly.GuruswamiSudan.hasseDerivativeEval_ofYConstant_mul_eq_eval_mul_of_lower` (theorem, [line 440](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L440))

```lean
theorem hasseDerivativeEval_ofYConstant_mul_eq_eval_mul_of_lower {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (x y : F) (b : Nat) :
    ∀ (A : CPolynomial F) (P : CBivariate F) (order : Nat),
      (∀ a, a < order → CBivariate.hasseDerivativeEval a b x y P = 0) →
        CBivariate.hasseDerivativeEval order b x y
            (CBivariate.ofYConstant A * P) =
          CPolynomial.eval x A * CBivariate.hasseDerivativeEval order b x y P
```

`CompPoly.GuruswamiSudan.hasseDerivativeEval_ofYConstant_mul_eq_zero_of_lower` (theorem, [line 498](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L498))

```lean
theorem hasseDerivativeEval_ofYConstant_mul_eq_zero_of_lower {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (x y : F) (b : Nat) (A : CPolynomial F) (P : CBivariate F) (order : Nat)
    (hLower : ∀ a, a ≤ order →
      CBivariate.hasseDerivativeEval a b x y P = 0) :
    CBivariate.hasseDerivativeEval order b x y (CBivariate.ofYConstant A * P) = 0
```

`CompPoly.GuruswamiSudan.foldl_add_congr_terms` (theorem, [line 510](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L510))

```lean
theorem foldl_add_congr_terms {α : Type*} [Add α]
    (xs : List Nat) (f g : Nat → α) (z : α)
    (h : ∀ x, x ∈ xs → f x = g x) :
    xs.foldl (fun out x ↦ out + f x) z =
      xs.foldl (fun out x ↦ out + g x) z
```

`CompPoly.GuruswamiSudan.foldl_add_distrib_terms_aux` (theorem, [line 523](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L523))

```lean
theorem foldl_add_distrib_terms_aux {α : Type*} [AddCommMonoid α]
    (xs : List Nat) (f g : Nat → α) (a b : α) :
    xs.foldl (fun out x ↦ out + (f x + g x)) (a + b) =
      xs.foldl (fun out x ↦ out + f x) a +
        xs.foldl (fun out x ↦ out + g x) b
```

`CompPoly.GuruswamiSudan.foldl_add_distrib_terms` (theorem, [line 536](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L536))

```lean
theorem foldl_add_distrib_terms {α : Type*} [AddCommMonoid α]
    (xs : List Nat) (f g : Nat → α) :
    xs.foldl (fun out x ↦ out + (f x + g x)) 0 =
      xs.foldl (fun out x ↦ out + f x) 0 +
        xs.foldl (fun out x ↦ out + g x) 0
```

`CompPoly.GuruswamiSudan.foldl_add_single_beq_of_not_mem` (theorem, [line 543](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L543))

```lean
theorem foldl_add_single_beq_of_not_mem {α : Type*} [AddCommMonoid α]
    (xs : List Nat) (target : Nat) (term acc : α)
    (hnot : target ∉ xs) :
    xs.foldl (fun out idx ↦ out + if idx == target then term else 0) acc =
      acc
```

`CompPoly.GuruswamiSudan.foldl_add_single_beq_of_nodup_mem` (theorem, [line 561](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L561))

```lean
theorem foldl_add_single_beq_of_nodup_mem {α : Type*} [AddCommMonoid α]
    (xs : List Nat) (target : Nat) (term : α)
    (hnodup : xs.Nodup) (hmem : target ∈ xs) :
    xs.foldl (fun out idx ↦ out + if idx == target then term else 0) 0 =
      term
```

`CompPoly.GuruswamiSudan.koetterBasisCombination` (definition, [line 586](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L586))

```lean
def koetterBasisCombination {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (weights : Nat → CPolynomial F) (basis : Array (CBivariate F)) : CBivariate F
```

`CompPoly.GuruswamiSudan.koetterBasisSpanContains` (definition, [line 592](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L592))

```lean
def koetterBasisSpanContains {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (basis : Array (CBivariate F)) (Q : CBivariate F) : Prop
```

`CompPoly.GuruswamiSudan.koetterBasisCombination_eq_zero_of_weights_zero` (theorem, [line 597](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L597))

```lean
theorem koetterBasisCombination_eq_zero_of_weights_zero {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (weights : Nat → CPolynomial F) (basis : Array (CBivariate F))
    (hzero : ∀ idx, idx < basis.size → weights idx = 0) :
    koetterBasisCombination weights basis = 0
```

`CompPoly.GuruswamiSudan.coeff_koetterBasisCombination` (theorem, [line 623](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean#L623))

```lean
theorem coeff_koetterBasisCombination {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (weights : Nat → CPolynomial F) (basis : Array (CBivariate F))
    (i j : Nat) :
    CBivariate.coeff (koetterBasisCombination weights basis) i j =
      (List.range basis.size).foldl
        (fun out idx ↦
          out + CBivariate.coeff
            (CBivariate.ofYConstant (weights idx) * basis.getD idx 0) i j)
        0
```

## Depends on

- [Guruswami-Sudan Backend Contexts](../../../context.md)

## Proof depends on

- [Guruswami-Sudan Polynomial Correctness Lemmas](../../../polynomialcorrectness.md)
- [Degrees and degree bounds under `toPoly`](../../../../../univariate/part-02/topoly/degree.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Combinations.lean)
- [Declaration ledger](../../../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Interpolation.LeeOSullivan.Correctness.Combinations.json)
