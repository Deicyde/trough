---
catalog: module
lean: CompPoly.GuruswamiSudan.cpoly_val_coeff_ofArray, CompPoly.GuruswamiSudan.cpoly_coeff_eq_zero_of_size_le, CompPoly.GuruswamiSudan.cpoly_size_eq_natDegree_succ_of_ne_zero, CompPoly.GuruswamiSudan.cpoly_coeff_natDegree_ne_zero_of_ne_zero, CompPoly.GuruswamiSudan.cpoly_coeff_dropXPower, CompPoly.GuruswamiSudan.cpoly_toPoly_eq_X_pow_mul_dropXPower_of_coeff_eq_zero_lt, CompPoly.GuruswamiSudan.cbivar_coeff_divXPower, CompPoly.GuruswamiSudan.cbivar_coeffY_divXPower, CompPoly.GuruswamiSudan.cbivar_coeff_eq_zero_of_y_size_le, CompPoly.GuruswamiSudan.initialCoefficientPolynomial_coeff_fold, CompPoly.GuruswamiSudan.initialCoefficientPolynomial_coeff_of_lt, CompPoly.GuruswamiSudan.cpoly_xAdicOrder?_some_coeff_ne, CompPoly.GuruswamiSudan.cpoly_xAdicOrder?_some_coeff_eq_zero_of_lt, CompPoly.GuruswamiSudan.cpoly_xAdicOrder?_none_eq_zero, CompPoly.GuruswamiSudan.xAdicStep, CompPoly.GuruswamiSudan.xAdicWitness, CompPoly.GuruswamiSudan.cbivar_xAdicOrder?_step_witness, CompPoly.GuruswamiSudan.cbivar_xAdicOrder?_fold_witness, CompPoly.GuruswamiSudan.cbivar_xAdicOrder?_some_exists, CompPoly.GuruswamiSudan.cbivar_xAdicOrder?_step_some_le_best, CompPoly.GuruswamiSudan.cbivar_xAdicOrder?_step_some_le_row, CompPoly.GuruswamiSudan.cbivar_xAdicOrder?_fold_some_le_best, CompPoly.GuruswamiSudan.cbivar_xAdicOrder?_fold_some_le_row, CompPoly.GuruswamiSudan.cbivar_xAdicOrder?_some_coeff_eq_zero_of_lt, CompPoly.GuruswamiSudan.cbivar_toPoly_eq_C_X_pow_mul_divXPower_of_xAdicOrder, CompPoly.GuruswamiSudan.cbivar_xAdicOrder?_fold_none, CompPoly.GuruswamiSudan.cbivar_xAdicOrder?_none_eq_zero, CompPoly.GuruswamiSudan.cpoly_dropXPower_add, CompPoly.GuruswamiSudan.dropXPower_eq_C_add_X_mul_dropXPower_succ, CompPoly.GuruswamiSudan.polynomial_monomial_substitution_term, CompPoly.GuruswamiSudan.polynomial_monomial_substitution_sum, CompPoly.GuruswamiSudan.foldl_cpoly_toPoly_add, CompPoly.GuruswamiSudan.cpoly_monomial_substitution_sum
statement: formalized
proof: formalized
---

# Roth-Ruckenstein Correctness Support

`CompPoly.Bivariate.GuruswamiSudan.Root.RothRuckenstein.Lemmas`, in [CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean), by Valerii Huhnin.

> Coefficient, composition, and root-filter lemmas used by the Roth-Ruckenstein
> correctness proofs.

`CompPoly.GuruswamiSudan.cpoly_val_coeff_ofArray` (theorem, [line 27](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean#L27))

```lean
theorem cpoly_val_coeff_ofArray {R : Type*} [Zero R] [BEq R] [LawfulBEq R]
    (coeffs : Array R) (i : Nat) :
    (CPolynomial.ofArray coeffs).val.coeff i = coeffs.getD i 0
```

`CompPoly.GuruswamiSudan.cpoly_coeff_eq_zero_of_size_le` (theorem, [line 33](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean#L33))

```lean
theorem cpoly_coeff_eq_zero_of_size_le {R : Type*} [Zero R]
    (p : CPolynomial R) {i : Nat} (h : p.val.size ≤ i) : p.coeff i = 0
```

`CompPoly.GuruswamiSudan.cpoly_size_eq_natDegree_succ_of_ne_zero` (theorem, [line 39](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean#L39))

```lean
theorem cpoly_size_eq_natDegree_succ_of_ne_zero {R : Type*} [Zero R]
    {p : CPolynomial R} (hp : p ≠ 0) :
    p.val.size = p.natDegree + 1
```

`CompPoly.GuruswamiSudan.cpoly_coeff_natDegree_ne_zero_of_ne_zero` (theorem, [line 53](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean#L53))

```lean
theorem cpoly_coeff_natDegree_ne_zero_of_ne_zero {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    {p : CPolynomial R} (hp : p ≠ 0) :
    p.coeff p.natDegree ≠ 0
```

`CompPoly.GuruswamiSudan.cpoly_coeff_dropXPower` (theorem, [line 62](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean#L62))

```lean
theorem cpoly_coeff_dropXPower {R : Type*} [Zero R]
    (p : CPolynomial R) (n i : Nat) :
    (CPolynomial.dropXPower p n).coeff i = p.coeff (i + n)
```

`CompPoly.GuruswamiSudan.cpoly_toPoly_eq_X_pow_mul_dropXPower_of_coeff_eq_zero_lt` (theorem, [line 73](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean#L73))

```lean
theorem cpoly_toPoly_eq_X_pow_mul_dropXPower_of_coeff_eq_zero_lt {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] (p : CPolynomial R) (n : Nat)
    (hzero : ∀ i, i < n → p.coeff i = 0) :
    p.toPoly = Polynomial.X ^ n * (CPolynomial.dropXPower p n).toPoly
```

`CompPoly.GuruswamiSudan.cbivar_coeff_divXPower` (theorem, [line 89](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean#L89))

```lean
theorem cbivar_coeff_divXPower {R : Type*} [Zero R] [BEq R] [LawfulBEq R]
    (Q : CBivariate R) (n i j : Nat) :
    CBivariate.coeff (CBivariate.divXPower Q n) i j = CBivariate.coeff Q (i + n) j
```

`CompPoly.GuruswamiSudan.cbivar_coeffY_divXPower` (theorem, [line 112](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean#L112))

```lean
theorem cbivar_coeffY_divXPower {R : Type*} [Zero R] [BEq R] [LawfulBEq R]
    (Q : CBivariate R) (n j : Nat) :
    (CBivariate.divXPower Q n).val.coeff j = CPolynomial.dropXPower (Q.val.coeff j) n
```

`CompPoly.GuruswamiSudan.cbivar_coeff_eq_zero_of_y_size_le` (theorem, [line 122](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean#L122))

```lean
theorem cbivar_coeff_eq_zero_of_y_size_le {R : Type*} [Zero R]
    (Q : CBivariate R) {i j : Nat} (hj : Q.val.size ≤ j) :
    CBivariate.coeff Q i j = 0
```

`CompPoly.GuruswamiSudan.initialCoefficientPolynomial_coeff_fold` (theorem, [line 133](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean#L133))

```lean
theorem initialCoefficientPolynomial_coeff_fold {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (Q : CBivariate F) (j : Nat) :
    ∀ (ys : List Nat) (out : CPolynomial F),
      ys.Nodup →
        (List.foldl
          (fun out y ↦ out + CPolynomial.monomial y (CBivariate.coeff Q 0 y))
          out ys).coeff j =
          out.coeff j + if j ∈ ys then CBivariate.coeff Q 0 j else 0
```

`CompPoly.GuruswamiSudan.initialCoefficientPolynomial_coeff_of_lt` (theorem, [line 163](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean#L163))

```lean
theorem initialCoefficientPolynomial_coeff_of_lt {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (Q : CBivariate F) {j : Nat} (hj : j < Q.val.size) :
    (initialCoefficientPolynomial Q).coeff j = CBivariate.coeff Q 0 j
```

`CompPoly.GuruswamiSudan.cpoly_xAdicOrder?_some_coeff_ne` (theorem, [line 173](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean#L173))

```lean
theorem cpoly_xAdicOrder?_some_coeff_ne {R : Type*} [Zero R] [BEq R] [LawfulBEq R]
    {p : CPolynomial R} {i : Nat} (h : CPolynomial.xAdicOrder? p = some i) :
    p.coeff i ≠ 0
```

`CompPoly.GuruswamiSudan.cpoly_xAdicOrder?_some_coeff_eq_zero_of_lt` (theorem, [line 180](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean#L180))

```lean
theorem cpoly_xAdicOrder?_some_coeff_eq_zero_of_lt {R : Type*}
    [Zero R] [BEq R] [LawfulBEq R]
    {p : CPolynomial R} {order i : Nat}
    (h : CPolynomial.xAdicOrder? p = some order) (hi : i < order) :
    p.coeff i = 0
```

`CompPoly.GuruswamiSudan.cpoly_xAdicOrder?_none_eq_zero` (theorem, [line 195](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean#L195))

```lean
theorem cpoly_xAdicOrder?_none_eq_zero {R : Type*} [Zero R] [BEq R] [LawfulBEq R]
    {p : CPolynomial R} (h : CPolynomial.xAdicOrder? p = none) : p = 0
```

`CompPoly.GuruswamiSudan.xAdicStep` (definition, [line 217](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean#L217))

```lean
def xAdicStep {R : Type*} [Zero R] [BEq R]
    (Q : CBivariate R) (best : Option Nat) (y : Nat) : Option Nat
```

`CompPoly.GuruswamiSudan.xAdicWitness` (definition, [line 226](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean#L226))

```lean
def xAdicWitness {R : Type*} [Zero R] (Q : CBivariate R)
    (best : Option Nat) : Prop
```

`CompPoly.GuruswamiSudan.cbivar_xAdicOrder?_step_witness` (theorem, [line 230](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean#L230))

```lean
theorem cbivar_xAdicOrder?_step_witness {R : Type*}
    [Zero R] [BEq R] [LawfulBEq R]
    (Q : CBivariate R) (best : Option Nat) {y : Nat}
    (hw : xAdicWitness Q best) (hy : y < Q.val.size) :
    xAdicWitness Q (xAdicStep Q best y)
```

`CompPoly.GuruswamiSudan.cbivar_xAdicOrder?_fold_witness` (theorem, [line 273](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean#L273))

```lean
theorem cbivar_xAdicOrder?_fold_witness {R : Type*}
    [Zero R] [BEq R] [LawfulBEq R]
    (Q : CBivariate R) :
    ∀ (ys : List Nat) (best : Option Nat),
      xAdicWitness Q best →
        (∀ y, y ∈ ys → y < Q.val.size) →
          xAdicWitness Q (List.foldl (xAdicStep Q) best ys)
```

`CompPoly.GuruswamiSudan.cbivar_xAdicOrder?_some_exists` (theorem, [line 293](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean#L293))

```lean
theorem cbivar_xAdicOrder?_some_exists {R : Type*}
    [Zero R] [BEq R] [LawfulBEq R]
    {Q : CBivariate R} {order : Nat} (h : CBivariate.xAdicOrder? Q = some order) :
    ∃ y, y < Q.val.size ∧ CBivariate.coeff Q order y ≠ 0
```

`CompPoly.GuruswamiSudan.cbivar_xAdicOrder?_step_some_le_best` (theorem, [line 308](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean#L308))

```lean
theorem cbivar_xAdicOrder?_step_some_le_best {R : Type*}
    [Zero R] [BEq R] (Q : CBivariate R) {best : Option Nat} {current result y : Nat}
    (hbest : best = some current) (hstep : xAdicStep Q best y = some result) :
    result ≤ current
```

`CompPoly.GuruswamiSudan.cbivar_xAdicOrder?_step_some_le_row` (theorem, [line 325](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean#L325))

```lean
theorem cbivar_xAdicOrder?_step_some_le_row {R : Type*}
    [Zero R] [BEq R] (Q : CBivariate R) {best : Option Nat} {rowOrder result y : Nat}
    (hrow : CPolynomial.xAdicOrder? (Q.val.coeff y) = some rowOrder)
    (hstep : xAdicStep Q best y = some result) :
    result ≤ rowOrder
```

`CompPoly.GuruswamiSudan.cbivar_xAdicOrder?_fold_some_le_best` (theorem, [line 341](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean#L341))

```lean
theorem cbivar_xAdicOrder?_fold_some_le_best {R : Type*}
    [Zero R] [BEq R] (Q : CBivariate R) :
    ∀ (ys : List Nat) (best : Option Nat) (current result : Nat),
      best = some current →
        List.foldl (xAdicStep Q) best ys = some result →
          result ≤ current
```

`CompPoly.GuruswamiSudan.cbivar_xAdicOrder?_fold_some_le_row` (theorem, [line 372](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean#L372))

```lean
theorem cbivar_xAdicOrder?_fold_some_le_row {R : Type*}
    [Zero R] [BEq R] (Q : CBivariate R) :
    ∀ (ys : List Nat) (best : Option Nat) (result y rowOrder : Nat),
      List.foldl (xAdicStep Q) best ys = some result →
        y ∈ ys →
          CPolynomial.xAdicOrder? (Q.val.coeff y) = some rowOrder →
            result ≤ rowOrder
```

`CompPoly.GuruswamiSudan.cbivar_xAdicOrder?_some_coeff_eq_zero_of_lt` (theorem, [line 412](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean#L412))

```lean
theorem cbivar_xAdicOrder?_some_coeff_eq_zero_of_lt {R : Type*}
    [Zero R] [BEq R] [LawfulBEq R]
    {Q : CBivariate R} {order i y : Nat}
    (h : CBivariate.xAdicOrder? Q = some order) (hi : i < order) :
    CBivariate.coeff Q i y = 0
```

`CompPoly.GuruswamiSudan.cbivar_toPoly_eq_C_X_pow_mul_divXPower_of_xAdicOrder` (theorem, [line 435](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean#L435))

```lean
theorem cbivar_toPoly_eq_C_X_pow_mul_divXPower_of_xAdicOrder {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {Q : CBivariate F} {order : Nat} (horder : CBivariate.xAdicOrder? Q = some order) :
    CBivariate.toPoly Q =
      Polynomial.C (Polynomial.X ^ order : Polynomial F) *
        CBivariate.toPoly (CBivariate.divXPower Q order)
```

`CompPoly.GuruswamiSudan.cbivar_xAdicOrder?_fold_none` (theorem, [line 451](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean#L451))

```lean
theorem cbivar_xAdicOrder?_fold_none {R : Type*}
    [Zero R] [BEq R] (Q : CBivariate R) :
    ∀ (ys : List Nat) (best : Option Nat),
      List.foldl (xAdicStep Q) best ys = none →
        best = none ∧ ∀ y, y ∈ ys → CPolynomial.xAdicOrder? (Q.val.coeff y) = none
```

`CompPoly.GuruswamiSudan.cbivar_xAdicOrder?_none_eq_zero` (theorem, [line 485](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean#L485))

```lean
theorem cbivar_xAdicOrder?_none_eq_zero {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    {Q : CBivariate F} (h : CBivariate.xAdicOrder? Q = none) : Q = 0
```

`CompPoly.GuruswamiSudan.cpoly_dropXPower_add` (theorem, [line 502](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean#L502))

```lean
theorem cpoly_dropXPower_add {R : Type*} [Zero R]
    (p : CPolynomial R) (m n : Nat) :
    CPolynomial.dropXPower (CPolynomial.dropXPower p m) n =
      CPolynomial.dropXPower p (m + n)
```

`CompPoly.GuruswamiSudan.dropXPower_eq_C_add_X_mul_dropXPower_succ` (theorem, [line 515](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean#L515))

```lean
theorem dropXPower_eq_C_add_X_mul_dropXPower_succ {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (p : CPolynomial F) (depth : Nat) :
    CPolynomial.dropXPower p depth =
      CPolynomial.C (p.coeff depth) +
        CPolynomial.X * CPolynomial.dropXPower p (depth + 1)
```

`CompPoly.GuruswamiSudan.polynomial_monomial_substitution_term` (theorem, [line 539](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean#L539))

```lean
theorem polynomial_monomial_substitution_term {F : Type*} [Field F]
    (a coeff : F) (p : Polynomial F) (x y t : Nat) :
    Polynomial.monomial x coeff *
        ((Polynomial.X * p) ^ t * Polynomial.C a ^ (y - t) *
          Polynomial.C (Nat.choose y t : F)) =
      Polynomial.monomial (x + t) (coeff * (Nat.choose y t : F) * a ^ (y - t)) *
        p ^ t
```

`CompPoly.GuruswamiSudan.polynomial_monomial_substitution_sum` (theorem, [line 553](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean#L553))

```lean
theorem polynomial_monomial_substitution_sum {F : Type*} [Field F]
    (a coeff : F) (p : Polynomial F) (x y : Nat) :
    (∑ t ∈ Finset.range (y + 1),
        Polynomial.monomial (x + t) (coeff * (Nat.choose y t : F) * a ^ (y - t)) *
          p ^ t) =
      Polynomial.monomial x coeff * (Polynomial.C a + Polynomial.X * p) ^ y
```

`CompPoly.GuruswamiSudan.foldl_cpoly_toPoly_add` (theorem, [line 568](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean#L568))

```lean
theorem foldl_cpoly_toPoly_add {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (f : Nat → CPolynomial F) :
    ∀ (xs : List Nat) (acc : CPolynomial F) (accPoly : Polynomial F),
      acc.toPoly = accPoly →
        (xs.foldl (fun acc x ↦ acc + f x) acc).toPoly =
          xs.foldl (fun acc x ↦ acc + (f x).toPoly) accPoly
```

`CompPoly.GuruswamiSudan.cpoly_monomial_substitution_sum` (theorem, [line 586](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean#L586))

```lean
theorem cpoly_monomial_substitution_sum {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (a coeff : F) (p : CPolynomial F) (x y : Nat) :
    (List.range' 0 (y + 1)).foldl
        (fun acc t ↦
          acc + CPolynomial.monomial (x + t)
            (coeff * (Nat.choose y t : F) * a ^ (y - t)) * p ^ t)
        0 =
      CPolynomial.monomial x coeff * (CPolynomial.C a + CPolynomial.X * p) ^ y
```

## Depends on

- [Common Guruswami-Sudan Root Helpers](../common.md)

## Proof depends on

- [Common Guruswami-Sudan Root Helper Lemmas](../common-2/lemmas.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/RothRuckenstein/Lemmas.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Root.RothRuckenstein.Lemmas.json)
