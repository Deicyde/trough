---
catalog: module
lean: CompPoly.CPolynomial.natDegree_mem_support_of_nonzero, CompPoly.DenseMatrix.get_ofFn, CompPoly.DenseMatrix.foldl_range_one_special, CompPoly.DenseMatrix.foldl_range_single_index, CompPoly.DenseMatrix.foldl_range_eq_zero_of_zero, CompPoly.CBivariate.coeff_zero, CompPoly.CBivariate.coeff_eq_zero_of_y_size_le, CompPoly.CBivariate.ofMonomialCoeffs_coeff, CompPoly.CBivariate.monomialGrid_nodup, CompPoly.CBivariate.monomialsWeightedDegreeLE_nodup, CompPoly.CBivariate.monomialsWeightedDegreeLE_sound, CompPoly.CBivariate.array_getD_inj_of_nodup, CompPoly.CBivariate.ofMonomialCoeffs_coeff_getD, CompPoly.CBivariate.ofMonomialCoeffs_ne_zero_of_coeff_getD_ne_zero, CompPoly.CBivariate.natWeightedDegree_le_of_coeff_zero, CompPoly.CBivariate.ofMonomialCoeffs_coeff_eq_zero_of_weight_gt, CompPoly.CBivariate.ofMonomialCoeffs_natWeightedDegree_le, CompPoly.CBivariate.hasseDerivativeFromTerms_coeff, CompPoly.CBivariate.hasseDerivativeEvalFromTerms_append_single, CompPoly.CBivariate.hasseDerivativeTermList_coeff_fold, CompPoly.CBivariate.hasseDerivativeTermList_coeff_inner_fold, CompPoly.CBivariate.hasseDerivativeTermList_coeff_value, CompPoly.CBivariate.hasseDerivative_coeff, CompPoly.CBivariate.hasseDerivative_add, CompPoly.CBivariate.hasseDerivative_zero, CompPoly.CBivariate.hasseDerivative_monomialXY, CompPoly.CBivariate.evalEval_add, CompPoly.CBivariate.evalEval_zero, CompPoly.CBivariate.evalEval_monomialXY, CompPoly.CBivariate.hasseDerivativeTerms_eval_aux, CompPoly.CBivariate.hasseDerivativeFromTerms_eval, CompPoly.CBivariate.hasseDerivative_eval_eq_eval, CompPoly.CBivariate.eval_hasseDeriv_eval_hasseDeriv_toPoly, CompPoly.CBivariate.coeff_shiftC_eq_hasseDerivativeEval, CompPoly.CBivariate.hasMultiplicity_iff_hasMultiplicityAtLeast, CompPoly.CBivariate.satisfiesMultiplicityConstraints_iff_hasMultiplicity, CompPoly.CBivariate.multiplicityAtLeastBool_iff_hasMultiplicity, CompPoly.CBivariate.satisfiesMultiplicityConstraintsBool_iff_hasMultiplicity, CompPoly.CBivariate.multiplicityAtLeastBool_iff_checkMultiplicity, CompPoly.CBivariate.satisfiesMultiplicityConstraintsBool_iff_checkMultiplicity, CompPoly.CBivariate.hasseDerivativeEval_add, CompPoly.CBivariate.hasseDerivativeEval_zero
statement: formalized
proof: formalized
---

# Guruswami-Sudan Polynomial Correctness Lemmas

`CompPoly.Bivariate.GuruswamiSudan.PolynomialCorrectness`, in [CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean), by Valerii Huhnin.

> Correctness lemmas for dense bivariate coefficient assembly, weighted-degree
> enumeration, and executable Hasse derivatives.

`CompPoly.CPolynomial.natDegree_mem_support_of_nonzero` (theorem, [line 29](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L29))

> The natural degree of a nonzero computable polynomial lies in its support.

```lean
theorem natDegree_mem_support_of_nonzero {R : Type*} [Zero R] [BEq R] [LawfulBEq R]
    {p : CPolynomial R} (hp : p ≠ 0) : p.natDegree ∈ p.support
```

`CompPoly.DenseMatrix.get_ofFn` (theorem, [line 42](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L42))

> Reading an in-bounds entry from a matrix constructed by `ofFn` returns that entry.

```lean
theorem get_ofFn [Zero F] (rows cols : Nat) (f : Nat → Nat → F)
    {row col : Nat} (hrow : row < rows) (hcol : col < cols) :
    (ofFn rows cols f).get row col = f row col
```

`CompPoly.DenseMatrix.foldl_range_one_special` (theorem, [line 62](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L62))

> Fold over a range with one distinguished nonzero entry.

```lean
theorem foldl_range_one_special {F : Type*} [AddCommMonoid F] {pivot : Nat} (x : F) :
    ∀ start len (init : F),
    (List.range' start len).foldl (fun acc j ↦ acc + if j = pivot then x else 0) init =
      init + if start ≤ pivot ∧ pivot < start + len then x else 0
```

`CompPoly.DenseMatrix.foldl_range_single_index` (theorem, [line 92](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L92))

> A range fold with a single distinguished index.

```lean
theorem foldl_range_single_index {F : Type*} [AddCommMonoid F] {n k : Nat}
    (hk : k < n) (x : F) :
    (List.range' 0 n).foldl (fun acc j ↦ acc + if j = k then x else 0) 0 = x
```

`CompPoly.DenseMatrix.foldl_range_eq_zero_of_zero` (theorem, [line 100](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L100))

> A range fold with identically zero contributions is zero.

```lean
theorem foldl_range_eq_zero_of_zero {F : Type*} [AddMonoid F] {n : Nat} {f : Nat → F}
    (hzero : ∀ c, c < n → f c = 0) :
    (List.range' 0 n).foldl (fun acc c ↦ acc + f c) 0 = 0
```

`CompPoly.CBivariate.coeff_zero` (theorem, [line 128](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L128))

> All bivariate coefficients of zero are zero.

```lean
theorem coeff_zero {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] (i j : Nat) :
    coeff (0 : CBivariate R) i j = 0
```

`CompPoly.CBivariate.coeff_eq_zero_of_y_size_le` (theorem, [line 137](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L137))

> Bivariate coefficients past the stored outer array are zero.

```lean
theorem coeff_eq_zero_of_y_size_le {R : Type*} [Zero R] (Q : CBivariate R)
    {i j : Nat} (hj : Q.val.size ≤ j) : coeff Q i j = 0
```

`CompPoly.CBivariate.ofMonomialCoeffs_coeff` (theorem, [line 145](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L145))

> Coefficients of a polynomial assembled from a monomial array are the folded
> sum of matching monomial coefficients.

```lean
theorem ofMonomialCoeffs_coeff {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (monomials : Array Monomial) (coeffs : Array R) (i j : Nat) :
    coeff (ofMonomialCoeffs monomials coeffs) i j =
      (List.range' 0 monomials.size).foldl
        (fun acc col ↦
          let monomial := monomials.getD col ⟨0, 0⟩
          acc + if i = monomial.xDegree ∧ j = monomial.yDegree then coeffs.getD col 0
            else 0)
        0
```

`CompPoly.CBivariate.monomialGrid_nodup` (theorem, [line 183](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L183))

> The executable monomial grid has no duplicate exponent pairs.

```lean
theorem monomialGrid_nodup (bound : Nat) : (monomialGrid bound).Nodup
```

`CompPoly.CBivariate.monomialsWeightedDegreeLE_nodup` (theorem, [line 201](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L201))

> Weighted-degree monomial enumeration has no duplicate exponent pairs.

```lean
theorem monomialsWeightedDegreeLE_nodup (xWeight yWeight bound : Nat) :
    (monomialsWeightedDegreeLE xWeight yWeight bound).toList.Nodup
```

`CompPoly.CBivariate.monomialsWeightedDegreeLE_sound` (theorem, [line 208](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L208))

> All returned weighted-degree monomials satisfy the requested bound.

```lean
theorem monomialsWeightedDegreeLE_sound
    {xWeight yWeight bound : Nat} {m : Monomial}
    (hm : m ∈ (monomialsWeightedDegreeLE xWeight yWeight bound).toList) :
    xWeight * m.xDegree + yWeight * m.yDegree ≤ bound
```

`CompPoly.CBivariate.array_getD_inj_of_nodup` (theorem, [line 216](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L216))

> In a nodup array, equal in-bounds `getD` entries have equal indices.

```lean
theorem array_getD_inj_of_nodup {α : Type*} [DecidableEq α] {xs : Array α}
    {default : α} (hnodup : xs.toList.Nodup) {i j : Nat}
    (hi : i < xs.size) (hj : j < xs.size)
    (h : xs.getD i default = xs.getD j default) : i = j
```

`CompPoly.CBivariate.ofMonomialCoeffs_coeff_getD` (theorem, [line 232](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L232))

> For a nodup monomial array, the assembled polynomial recovers the matching
> coefficient at each listed monomial.

```lean
theorem ofMonomialCoeffs_coeff_getD {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    {monomials : Array Monomial} {coeffs : Array R}
    (hnodup : monomials.toList.Nodup) {k : Nat} (hk : k < monomials.size) :
    coeff (ofMonomialCoeffs monomials coeffs)
        (monomials.getD k ⟨0, 0⟩).xDegree (monomials.getD k ⟨0, 0⟩).yDegree =
      coeffs.getD k 0
```

`CompPoly.CBivariate.ofMonomialCoeffs_ne_zero_of_coeff_getD_ne_zero` (theorem, [line 302](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L302))

> A nonzero coefficient at a listed monomial makes the assembled bivariate
> polynomial nonzero.

```lean
theorem ofMonomialCoeffs_ne_zero_of_coeff_getD_ne_zero {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    {monomials : Array Monomial} {coeffs : Array R}
    (hnodup : monomials.toList.Nodup) {k : Nat} (hk : k < monomials.size)
    (hcoeff : coeffs.getD k 0 ≠ 0) :
    ofMonomialCoeffs monomials coeffs ≠ 0
```

`CompPoly.CBivariate.natWeightedDegree_le_of_coeff_zero` (theorem, [line 322](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L322))

> If all coefficients above a weighted-degree bound are zero, the executable
> weighted degree is below that bound.

```lean
theorem natWeightedDegree_le_of_coeff_zero {R : Type*} [Zero R] [BEq R] [LawfulBEq R]
    (f : CBivariate R) (u v bound : Nat)
    (hzero : ∀ i j, bound < u * i + v * j → coeff f i j = 0) :
    natWeightedDegree f u v ≤ bound
```

`CompPoly.CBivariate.ofMonomialCoeffs_coeff_eq_zero_of_weight_gt` (theorem, [line 344](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L344))

> Coefficients above a bound are zero for a polynomial assembled from monomials
> all below that bound.

```lean
theorem ofMonomialCoeffs_coeff_eq_zero_of_weight_gt {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    {monomials : Array Monomial} {coeffs : Array R} {u v bound i j : Nat}
    (hall : ∀ monomial, monomial ∈ monomials.toList →
      u * monomial.xDegree + v * monomial.yDegree ≤ bound)
    (hgt : bound < u * i + v * j) :
    coeff (ofMonomialCoeffs monomials coeffs) i j = 0
```

`CompPoly.CBivariate.ofMonomialCoeffs_natWeightedDegree_le` (theorem, [line 371](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L371))

> A polynomial assembled from bounded monomials has weighted degree below the
> same bound.

```lean
theorem ofMonomialCoeffs_natWeightedDegree_le {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    {monomials : Array Monomial} {coeffs : Array R} {u v bound : Nat}
    (hall : ∀ monomial, monomial ∈ monomials.toList →
      u * monomial.xDegree + v * monomial.yDegree ≤ bound) :
    natWeightedDegree (ofMonomialCoeffs monomials coeffs) u v ≤ bound
```

`CompPoly.CBivariate.hasseDerivativeFromTerms_coeff` (theorem, [line 383](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L383))

> Coefficients of a polynomial materialized from Hasse terms are the folded
> sum of matching term coefficients.

```lean
theorem hasseDerivativeFromTerms_coeff {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (terms : List (HasseTerm R)) (i j : Nat) :
    coeff (hasseDerivativeFromTerms terms) i j =
      terms.foldl
        (fun acc term ↦ acc + if i = term.xDegree ∧ j = term.yDegree then term.coeff else 0)
        0
```

`CompPoly.CBivariate.hasseDerivativeEvalFromTerms_append_single` (theorem, [line 411](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L411))

> Evaluating after appending one Hasse term adds that term's contribution.

```lean
theorem hasseDerivativeEvalFromTerms_append_single {R : Type*} [Semiring R]
    (terms : List (HasseTerm R)) (term : HasseTerm R) (x y : R) :
    hasseDerivativeEvalFromTerms (terms ++ [term]) x y =
      hasseDerivativeEvalFromTerms terms x y +
        term.coeff * x ^ term.xDegree * y ^ term.yDegree
```

`CompPoly.CBivariate.hasseDerivativeTermList_coeff_fold` (theorem, [line 421](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L421))

> The fixed coefficient of the executable Hasse term list is the matching
> coefficient fold over the same degree ranges.

```lean
theorem hasseDerivativeTermList_coeff_fold {R : Type*} [Semiring R]
    (a b i j : Nat) (Q : CBivariate R) :
    (hasseDerivativeTermList a b Q).foldl
        (fun acc term ↦ acc + if i = term.xDegree ∧ j = term.yDegree then term.coeff else 0)
        0 =
      (List.range' 0 Q.val.size).foldl
        (fun acc yDeg ↦
          let coeffY := Q.val.coeff yDeg
          if b ≤ yDeg then
            (List.range' 0 coeffY.val.size).foldl
              (fun acc xDeg ↦
                if a ≤ xDeg then
                  acc +
                    if i = xDeg - a ∧ j = yDeg - b then
                      (Nat.choose xDeg a : R) * (Nat.choose yDeg b : R) * coeffY.coeff xDeg
                    else 0
                else acc)
              acc
          else acc)
        0
```

`CompPoly.CBivariate.hasseDerivativeTermList_coeff_inner_fold` (theorem, [line 534](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L534))

> Collapse the inner `x`-fold in a fixed Hasse coefficient calculation.

```lean
theorem hasseDerivativeTermList_coeff_inner_fold {R : Type*} [Semiring R]
    (a b i j yDeg : Nat) (coeffY : CPolynomial R) (acc : R) (hy : b ≤ yDeg) :
    (List.range' 0 coeffY.val.size).foldl
        (fun acc xDeg ↦
          if a ≤ xDeg then
            acc +
              if i = xDeg - a ∧ j = yDeg - b then
                (Nat.choose xDeg a : R) * (Nat.choose yDeg b : R) * coeffY.coeff xDeg
              else 0
          else acc)
        acc =
      acc +
        if yDeg = j + b ∧ i + a < coeffY.val.size then
          (Nat.choose (i + a) a : R) * (Nat.choose yDeg b : R) * coeffY.coeff (i + a)
        else 0
```

`CompPoly.CBivariate.hasseDerivativeTermList_coeff_value` (theorem, [line 627](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L627))

> The fixed coefficient of the executable Hasse term list has the closed
> coefficient-shift formula.

```lean
theorem hasseDerivativeTermList_coeff_value {R : Type*} [Semiring R]
    (a b i j : Nat) (Q : CBivariate R) :
    (hasseDerivativeTermList a b Q).foldl
        (fun acc term ↦ acc + if i = term.xDegree ∧ j = term.yDegree then term.coeff else 0)
        0 =
      (Nat.choose (i + a) a : R) * (Nat.choose (j + b) b : R) *
        coeff Q (i + a) (j + b)
```

`CompPoly.CBivariate.hasseDerivative_coeff` (theorem, [line 698](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L698))

> Coefficients of the executable Hasse derivative are shifted source
> coefficients scaled by the corresponding binomial factors.

```lean
theorem hasseDerivative_coeff {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (a b i j : Nat) (Q : CBivariate R) :
    coeff (hasseDerivative a b Q) i j =
      (Nat.choose (i + a) a : R) * (Nat.choose (j + b) b : R) *
        coeff Q (i + a) (j + b)
```

`CompPoly.CBivariate.hasseDerivative_add` (theorem, [line 709](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L709))

> Hasse derivatives are additive.

```lean
theorem hasseDerivative_add {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (a b : Nat) (P Q : CBivariate R) :
    hasseDerivative a b (P + Q) = hasseDerivative a b P + hasseDerivative a b Q
```

`CompPoly.CBivariate.hasseDerivative_zero` (theorem, [line 722](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L722))

> The Hasse derivative of zero is zero.

```lean
theorem hasseDerivative_zero {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (a b : Nat) :
    hasseDerivative a b (0 : CBivariate R) = 0
```

`CompPoly.CBivariate.hasseDerivative_monomialXY` (theorem, [line 732](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L732))

> Hasse derivative of a single bivariate monomial.

```lean
theorem hasseDerivative_monomialXY {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (a b n m : Nat) (c : R) :
    hasseDerivative a b (monomialXY n m c) =
      if a ≤ n ∧ b ≤ m then
        monomialXY (n - a) (m - b)
          ((Nat.choose n a : R) * (Nat.choose m b : R) * c)
      else 0
```

`CompPoly.CBivariate.evalEval_add` (theorem, [line 768](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L768))

> Full evaluation is additive.

```lean
theorem evalEval_add {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (x y : R) (P Q : CBivariate R) :
    evalEval x y (P + Q) = evalEval x y P + evalEval x y Q
```

`CompPoly.CBivariate.evalEval_zero` (theorem, [line 776](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L776))

> Full evaluation of zero is zero.

```lean
theorem evalEval_zero {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (x y : R) : evalEval x y (0 : CBivariate R) = 0
```

`CompPoly.CBivariate.evalEval_monomialXY` (theorem, [line 783](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L783))

> Full evaluation of a bivariate monomial has the expected closed form.

```lean
theorem evalEval_monomialXY {R : Type*}
    [CommSemiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (x y c : R) (n m : Nat) :
    evalEval x y (monomialXY n m c) = c * x ^ n * y ^ m
```

`CompPoly.CBivariate.hasseDerivativeTerms_eval_aux` (theorem, [line 791](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L791))

> Evaluating the materialized derivative-term fold matches the direct scalar fold.

```lean
theorem hasseDerivativeTerms_eval_aux {R : Type*}
    [CommSemiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (x y : R) (terms : List (HasseTerm R)) (acc : CBivariate R) :
    evalEval x y (terms.foldl
      (fun out term ↦ out + monomialXY term.xDegree term.yDegree term.coeff) acc) =
    terms.foldl
      (fun z term ↦ z + term.coeff * x ^ term.xDegree * y ^ term.yDegree)
      (evalEval x y acc)
```

`CompPoly.CBivariate.hasseDerivativeFromTerms_eval` (theorem, [line 808](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L808))

> Evaluating a materialized derivative-term polynomial matches direct term evaluation.

```lean
theorem hasseDerivativeFromTerms_eval {R : Type*}
    [CommSemiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (x y : R) (terms : List (HasseTerm R)) :
    evalEval x y (hasseDerivativeFromTerms terms) =
      hasseDerivativeEvalFromTerms terms x y
```

`CompPoly.CBivariate.hasseDerivative_eval_eq_eval` (theorem, [line 818](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L818))

> Correctness of executable Hasse derivative evaluation.

```lean
theorem hasseDerivative_eval_eq_eval {R : Type*}
    [CommSemiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (a b : Nat) (x y : R) (Q : CBivariate R) :
    evalEval x y (hasseDerivative a b Q) = hasseDerivativeEval a b x y Q
```

`CompPoly.CBivariate.eval_hasseDeriv_eval_hasseDeriv_toPoly` (theorem, [line 936](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L936))

> Evaluating the univariate `X`-Hasse derivative of the evaluated `Y`-Hasse
> derivative matches the executable bivariate Hasse derivative.

```lean
theorem eval_hasseDeriv_eval_hasseDeriv_toPoly {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (Q : CBivariate F) (x y : F) (a b : Nat) :
    Polynomial.eval x (Polynomial.hasseDeriv a
        (Polynomial.eval (Polynomial.C y) (Polynomial.hasseDeriv b Q.toPoly))) =
      CBivariate.hasseDerivativeEval a b x y Q
```

`CompPoly.CBivariate.coeff_shiftC_eq_hasseDerivativeEval` (theorem, [line 950](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L950))

> The coefficient of the generic Taylor shift is the direct Hasse derivative
> evaluation at the shift point.

```lean
theorem coeff_shiftC_eq_hasseDerivativeEval {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (Q : CBivariate F) (x y : F) (a b : Nat) :
    CBivariate.coeff (CBivariate.shiftC x y Q) a b =
      CBivariate.hasseDerivativeEval a b x y Q
```

`CompPoly.CBivariate.hasMultiplicity_iff_hasMultiplicityAtLeast` (theorem, [line 968](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L968))

> The generic multiplicity predicate agrees with the direct GS Hasse
> multiplicity predicate.

```lean
theorem hasMultiplicity_iff_hasMultiplicityAtLeast {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (Q : CBivariate F) (r : Nat) (x y : F) :
    CBivariate.hasMultiplicity Q r x y ↔
      CBivariate.HasMultiplicityAtLeast Q x y r
```

`CompPoly.CBivariate.satisfiesMultiplicityConstraints_iff_hasMultiplicity` (theorem, [line 984](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L984))

> The GS batch Hasse predicate agrees with the generic multiplicity
> predicate over every packed point.

```lean
theorem satisfiesMultiplicityConstraints_iff_hasMultiplicity {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (Q : CBivariate F) (points : Array (F × F)) (r : Nat) :
    CBivariate.SatisfiesMultiplicityConstraints Q points r ↔
      ∀ point, point ∈ points.toList →
        CBivariate.hasMultiplicity Q r point.1 point.2
```

`CompPoly.CBivariate.multiplicityAtLeastBool_iff_hasMultiplicity` (theorem, [line 1001](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L1001))

> The executable GS point checker agrees with the generic multiplicity
> predicate.

```lean
theorem multiplicityAtLeastBool_iff_hasMultiplicity {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (Q : CBivariate F) (x y : F) (r : Nat) :
    CBivariate.multiplicityAtLeastBool Q x y r = true ↔
      CBivariate.hasMultiplicity Q r x y
```

`CompPoly.CBivariate.satisfiesMultiplicityConstraintsBool_iff_hasMultiplicity` (theorem, [line 1030](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L1030))

> The executable GS batch checker agrees with the generic multiplicity
> predicate over every packed point.

```lean
theorem satisfiesMultiplicityConstraintsBool_iff_hasMultiplicity {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (Q : CBivariate F) (points : Array (F × F)) (r : Nat) :
    CBivariate.satisfiesMultiplicityConstraintsBool Q points r = true ↔
      ∀ point, point ∈ points.toList →
        CBivariate.hasMultiplicity Q r point.1 point.2
```

`CompPoly.CBivariate.multiplicityAtLeastBool_iff_checkMultiplicity` (theorem, [line 1054](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L1054))

> The executable GS point checker agrees with the generic boolean
> checker.

```lean
theorem multiplicityAtLeastBool_iff_checkMultiplicity {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (Q : CBivariate F) (x y : F) (r : Nat) :
    CBivariate.multiplicityAtLeastBool Q x y r = true ↔
      CBivariate.checkMultiplicity Q r x y = true
```

`CompPoly.CBivariate.satisfiesMultiplicityConstraintsBool_iff_checkMultiplicity` (theorem, [line 1063](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L1063))

> The executable GS batch checker agrees pointwise with the generic
> boolean checker over the packed point array.

```lean
theorem satisfiesMultiplicityConstraintsBool_iff_checkMultiplicity {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (Q : CBivariate F) (points : Array (F × F)) (r : Nat) :
    CBivariate.satisfiesMultiplicityConstraintsBool Q points r = true ↔
      ∀ point, point ∈ points.toList →
        CBivariate.checkMultiplicity Q r point.1 point.2 = true
```

`CompPoly.CBivariate.hasseDerivativeEval_add` (theorem, [line 1077](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L1077))

> Direct Hasse evaluation is additive in the input polynomial.

```lean
theorem hasseDerivativeEval_add {R : Type*}
    [CommSemiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (a b : Nat) (x y : R) (P Q : CBivariate R) :
    hasseDerivativeEval a b x y (P + Q) =
      hasseDerivativeEval a b x y P + hasseDerivativeEval a b x y Q
```

`CompPoly.CBivariate.hasseDerivativeEval_zero` (theorem, [line 1088](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean#L1088))

> Direct Hasse evaluation of zero is zero.

```lean
theorem hasseDerivativeEval_zero {R : Type*}
    [CommSemiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (a b : Nat) (x y : R) :
    hasseDerivativeEval a b x y (0 : CBivariate R) = 0
```

## Depends on

- [Partial Derivatives and Multiplicity of Computable Bivariate Polynomials](../deriv.md)
- [Guruswami-Sudan Polynomial Helpers](polynomial.md)
- [Dense Row-Major Matrices](../../linearalgebra/dense/basic.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/PolynomialCorrectness.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.PolynomialCorrectness.json)
