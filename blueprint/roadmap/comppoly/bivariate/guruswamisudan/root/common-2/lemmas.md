---
catalog: module
lean: CompPoly.array_mem_eraseDups_fold, CompPoly.array_mem_of_mem_eraseDups, CompPoly.array_mem_eraseDups_fold_of_mem, CompPoly.array_mem_eraseDups_of_mem, CompPoly.GuruswamiSudan.degreeLt_of_degreeLtBool, CompPoly.GuruswamiSudan.degreeLtBool_of_degreeLt, CompPoly.GuruswamiSudan.cpoly_truncate_coeff, CompPoly.GuruswamiSudan.cbivar_coeff_truncateX, CompPoly.GuruswamiSudan.polynomialPrefix_zero, CompPoly.GuruswamiSudan.polynomialPrefix_succ, CompPoly.GuruswamiSudan.polynomialPrefix_eq_self_of_degreeLt, CompPoly.GuruswamiSudan.list_foldl_add_eq_sum, CompPoly.GuruswamiSudan.list_sum_map_range_eq_finset_sum, CompPoly.GuruswamiSudan.composeY_add, CompPoly.GuruswamiSudan.composeY_outer_monomial, CompPoly.GuruswamiSudan.cpoly_powCoeff_eq_coeff_pow, CompPoly.GuruswamiSudan.cpoly_mulPowCoeff_eq_coeff_mul_pow, CompPoly.GuruswamiSudan.cpoly_coeff_zero_mul, CompPoly.GuruswamiSudan.cpoly_coeff_zero_pow, CompPoly.GuruswamiSudan.cpoly_coeff_zero_pow_monomial_zero, CompPoly.GuruswamiSudan.cpoly_mulPowCoeff_monomial_zero_depth_zero, CompPoly.GuruswamiSudan.composeY_coeff_zero_zipIdx_eq_range_aux, CompPoly.GuruswamiSudan.composeY_coeff_zero_fold_eq, CompPoly.GuruswamiSudan.composeY_coeff_zipIdx_eq_range_aux, CompPoly.GuruswamiSudan.composeY_coeff_fold_eq, CompPoly.GuruswamiSudan.composeYCoeff_eq_composeY_coeff, CompPoly.GuruswamiSudan.fold_range_coeff_add_mul_pow, CompPoly.GuruswamiSudan.composeY_eq_range_fold, CompPoly.GuruswamiSudan.composeY_zero, CompPoly.GuruswamiSudan.composeY_toPoly, CompPoly.GuruswamiSudan.initialCoefficientPolynomial_evalHorner_eq_composeYCoeff_monomial_zero, CompPoly.GuruswamiSudan.composeYCoeff_monomial_zero_eq_composeY_coeff_zero, CompPoly.GuruswamiSudan.initialCoefficientPolynomial_eval_eq_composeY_coeff_zero, CompPoly.GuruswamiSudan.rootsInFieldForNonzeroEquation_complete, CompPoly.GuruswamiSudan.composeY_of_composeYHorner_eq_zero, CompPoly.GuruswamiSudan.composeYHorner_eq_zero_of_composeY, CompPoly.GuruswamiSudan.isRootYDegreeLtBool_of_root, CompPoly.GuruswamiSudan.rootsYDegreeLtFromCandidates_sound, CompPoly.GuruswamiSudan.rootsYDegreeLtFromCandidates_eraseDups_sound, CompPoly.GuruswamiSudan.rootsYDegreeLtFromCandidates_complete_of_mem, CompPoly.GuruswamiSudan.rootsYDegreeLtFromCandidates_eraseDups_complete_of_mem
statement: formalized
proof: formalized
---

# Common Guruswami-Sudan Root Helper Lemmas

`CompPoly.Bivariate.GuruswamiSudan.Root.Common.Lemmas`, in [CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean), by Valerii Huhnin.

> Reusable proof facts for bounded bivariate root backends.

`CompPoly.array_mem_eraseDups_fold` (theorem, [line 22](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L22))

```lean
theorem array_mem_eraseDups_fold {α : Type*} [BEq α] [LawfulBEq α]
    (a : α) : ∀ (xs : List α) (out : Array α),
      a ∈ List.foldl (fun out x ↦ if x ∈ out then out else out.push x) out xs →
        a ∈ out ∨ a ∈ xs
```

`CompPoly.array_mem_of_mem_eraseDups` (theorem, [line 48](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L48))

```lean
theorem array_mem_of_mem_eraseDups {α : Type*} [BEq α] [LawfulBEq α]
    {xs : Array α} {a : α} (h : a ∈ xs.eraseDups) : a ∈ xs
```

`CompPoly.array_mem_eraseDups_fold_of_mem` (theorem, [line 56](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L56))

```lean
theorem array_mem_eraseDups_fold_of_mem {α : Type*} [BEq α] [LawfulBEq α]
    (a : α) : ∀ (xs : List α) (out : Array α),
      a ∈ out ∨ a ∈ xs →
        a ∈ List.foldl (fun out x ↦ if x ∈ out then out else out.push x) out xs
```

`CompPoly.array_mem_eraseDups_of_mem` (theorem, [line 84](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L84))

```lean
theorem array_mem_eraseDups_of_mem {α : Type*} [BEq α] [LawfulBEq α]
    {xs : Array α} {a : α} (h : a ∈ xs) : a ∈ xs.eraseDups
```

`CompPoly.GuruswamiSudan.degreeLt_of_degreeLtBool` (theorem, [line 93](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L93))

```lean
theorem degreeLt_of_degreeLtBool {F : Type*} [Zero F]
    {p : CPolynomial F} {k : Nat} (h : degreeLtBool p k = true) : degreeLt p k
```

`CompPoly.GuruswamiSudan.degreeLtBool_of_degreeLt` (theorem, [line 104](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L104))

```lean
theorem degreeLtBool_of_degreeLt {F : Type*} [Zero F]
    {p : CPolynomial F} {k : Nat} (h : degreeLt p k) : degreeLtBool p k = true
```

`CompPoly.GuruswamiSudan.cpoly_truncate_coeff` (theorem, [line 117](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L117))

```lean
theorem cpoly_truncate_coeff {R : Type*} [Zero R] [BEq R] [LawfulBEq R]
    (p : CPolynomial R) (n i : Nat) :
    (CPolynomial.truncate p n).coeff i = if i < n then p.coeff i else 0
```

`CompPoly.GuruswamiSudan.cbivar_coeff_truncateX` (theorem, [line 130](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L130))

```lean
theorem cbivar_coeff_truncateX {R : Type*} [Zero R] [BEq R] [LawfulBEq R]
    (Q : CBivariate R) (n i j : Nat) :
    CBivariate.coeff (CBivariate.truncateX Q n) i j =
      if i < n then CBivariate.coeff Q i j else 0
```

`CompPoly.GuruswamiSudan.polynomialPrefix_zero` (theorem, [line 156](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L156))

```lean
theorem polynomialPrefix_zero {R : Type*} [Zero R] [BEq R] [LawfulBEq R]
    (p : CPolynomial R) : polynomialPrefix p 0 = 0
```

`CompPoly.GuruswamiSudan.polynomialPrefix_succ` (theorem, [line 165](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L165))

```lean
theorem polynomialPrefix_succ {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (p : CPolynomial F) (depth : Nat) :
    polynomialPrefix p (depth + 1) =
      extendPrefix (polynomialPrefix p depth) depth (p.coeff depth)
```

`CompPoly.GuruswamiSudan.polynomialPrefix_eq_self_of_degreeLt` (theorem, [line 184](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L184))

```lean
theorem polynomialPrefix_eq_self_of_degreeLt {F : Type*}
    [Zero F] [BEq F] [LawfulBEq F]
    {p : CPolynomial F} {k : Nat} (hdegree : degreeLt p k) :
    polynomialPrefix p k = p
```

`CompPoly.GuruswamiSudan.list_foldl_add_eq_sum` (theorem, [line 200](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L200))

```lean
theorem list_foldl_add_eq_sum {R : Type*} [AddMonoid R]
    (f : Nat → R) : ∀ (xs : List Nat) (acc : R),
    List.foldl (fun acc i ↦ acc + f i) acc xs = acc + (xs.map f).sum
```

`CompPoly.GuruswamiSudan.list_sum_map_range_eq_finset_sum` (theorem, [line 208](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L208))

```lean
theorem list_sum_map_range_eq_finset_sum {R : Type*} [AddCommMonoid R]
    (f : Nat → R) : ∀ n : Nat,
    (List.map f (List.range n)).sum = ∑ i ∈ Finset.range n, f i
```

`CompPoly.GuruswamiSudan.composeY_add` (theorem, [line 215](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L215))

```lean
theorem composeY_add {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (P Q : CBivariate R) (p : CPolynomial R) :
    CBivariate.composeY (P + Q) p = CBivariate.composeY P p + CBivariate.composeY Q p
```

`CompPoly.GuruswamiSudan.composeY_outer_monomial` (theorem, [line 222](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L222))

```lean
theorem composeY_outer_monomial {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (c p : CPolynomial R) (y : Nat) :
    CBivariate.composeY (CPolynomial.monomial y c : CBivariate R) p = c * p ^ y
```

`CompPoly.GuruswamiSudan.cpoly_powCoeff_eq_coeff_pow` (theorem, [line 229](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L229))

```lean
theorem cpoly_powCoeff_eq_coeff_pow {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (p : CPolynomial R) (k n : Nat) :
    CPolynomial.powCoeff p k n = (p ^ k : CPolynomial R).coeff n
```

`CompPoly.GuruswamiSudan.cpoly_mulPowCoeff_eq_coeff_mul_pow` (theorem, [line 245](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L245))

```lean
theorem cpoly_mulPowCoeff_eq_coeff_mul_pow {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (a p : CPolynomial R) (k n : Nat) :
    CPolynomial.mulPowCoeff a p k n = (a * (p ^ k : CPolynomial R)).coeff n
```

`CompPoly.GuruswamiSudan.cpoly_coeff_zero_mul` (theorem, [line 255](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L255))

```lean
theorem cpoly_coeff_zero_mul {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (p q : CPolynomial F) :
    (p * q).coeff 0 = p.coeff 0 * q.coeff 0
```

`CompPoly.GuruswamiSudan.cpoly_coeff_zero_pow` (theorem, [line 264](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L264))

```lean
theorem cpoly_coeff_zero_pow {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (p : CPolynomial F) :
    ∀ n : Nat, (p ^ n : CPolynomial F).coeff 0 = p.coeff 0 ^ n
```

`CompPoly.GuruswamiSudan.cpoly_coeff_zero_pow_monomial_zero` (theorem, [line 281](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L281))

```lean
theorem cpoly_coeff_zero_pow_monomial_zero {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (c : F) :
    ∀ n : Nat, ((CPolynomial.monomial 0 c) ^ n : CPolynomial F).coeff 0 = c ^ n
```

`CompPoly.GuruswamiSudan.cpoly_mulPowCoeff_monomial_zero_depth_zero` (theorem, [line 290](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L290))

```lean
theorem cpoly_mulPowCoeff_monomial_zero_depth_zero {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (a : CPolynomial F) (c : F) (y : Nat) :
    CPolynomial.mulPowCoeff a (CPolynomial.monomial 0 c) y 0 = a.coeff 0 * c ^ y
```

`CompPoly.GuruswamiSudan.composeY_coeff_zero_zipIdx_eq_range_aux` (theorem, [line 301](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L301))

```lean
theorem composeY_coeff_zero_zipIdx_eq_range_aux {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (xs : List (CPolynomial F)) (p accPoly : CPolynomial F) (accCoeff : F)
    (offset : Nat) (hacc : accPoly.coeff 0 = accCoeff) :
    List.foldl
        (fun acc y ↦ acc + (xs.getD (y - offset) 0).coeff 0 * p.coeff 0 ^ y)
        accCoeff (List.range' offset xs.length) =
      (List.foldl (fun acc x ↦ acc + x.1 * p ^ x.2) accPoly
        (xs.zipIdx offset)).coeff 0
```

`CompPoly.GuruswamiSudan.composeY_coeff_zero_fold_eq` (theorem, [line 333](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L333))

```lean
theorem composeY_coeff_zero_fold_eq {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (coeffs : Array (CPolynomial F)) (p : CPolynomial F) :
    List.foldl (fun acc y ↦ acc + (coeffs.getD y 0).coeff 0 * p.coeff 0 ^ y) 0
        (List.range' 0 coeffs.size) =
      (Array.foldl (fun acc x ↦ acc + x.1 * p ^ x.2) 0 coeffs.zipIdx).coeff 0
```

`CompPoly.GuruswamiSudan.composeY_coeff_zipIdx_eq_range_aux` (theorem, [line 344](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L344))

```lean
theorem composeY_coeff_zipIdx_eq_range_aux {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (xs : List (CPolynomial R)) (p accPoly : CPolynomial R) (accCoeff : R)
    (offset n : Nat) (hacc : accPoly.coeff n = accCoeff) :
    List.foldl
        (fun acc y ↦ acc + ((xs.getD (y - offset) 0) * p ^ y).coeff n)
        accCoeff (List.range' offset xs.length) =
      (List.foldl (fun acc x ↦ acc + x.1 * p ^ x.2) accPoly
        (xs.zipIdx offset)).coeff n
```

`CompPoly.GuruswamiSudan.composeY_coeff_fold_eq` (theorem, [line 376](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L376))

```lean
theorem composeY_coeff_fold_eq {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (coeffs : Array (CPolynomial R)) (p : CPolynomial R) (n : Nat) :
    List.foldl (fun acc y ↦ acc + ((coeffs.getD y 0) * p ^ y).coeff n) 0
        (List.range' 0 coeffs.size) =
      (Array.foldl (fun acc x ↦ acc + x.1 * p ^ x.2) 0 coeffs.zipIdx).coeff n
```

`CompPoly.GuruswamiSudan.composeYCoeff_eq_composeY_coeff` (theorem, [line 387](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L387))

```lean
theorem composeYCoeff_eq_composeY_coeff {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (Q : CBivariate R) (p : CPolynomial R) (depth : Nat) :
    CBivariate.composeYCoeff Q p depth = (CBivariate.composeY Q p).coeff depth
```

`CompPoly.GuruswamiSudan.fold_range_coeff_add_mul_pow` (theorem, [line 395](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L395))

```lean
theorem fold_range_coeff_add_mul_pow {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (coeffs : Array (CPolynomial R)) (p : CPolynomial R) :
    ∀ (ys : List Nat) (acc : CPolynomial R) (accCoeff : R) (n : Nat),
      acc.coeff n = accCoeff →
        (List.foldl (fun acc y ↦ acc + coeffs.getD y 0 * p ^ y) acc ys).coeff n =
          List.foldl
            (fun acc y ↦ acc + ((coeffs.getD y 0) * p ^ y).coeff n)
            accCoeff ys
```

`CompPoly.GuruswamiSudan.composeY_eq_range_fold` (theorem, [line 415](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L415))

```lean
theorem composeY_eq_range_fold {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (Q : CBivariate R) (p : CPolynomial R) :
    CBivariate.composeY Q p =
      (List.range' 0 Q.val.size).foldl
        (fun acc y ↦ acc + Q.val.coeff y * p ^ y) 0
```

`CompPoly.GuruswamiSudan.composeY_zero` (theorem, [line 429](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L429))

```lean
theorem composeY_zero {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (p : CPolynomial R) :
    CBivariate.composeY (0 : CBivariate R) p = 0
```

`CompPoly.GuruswamiSudan.composeY_toPoly` (theorem, [line 436](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L436))

```lean
theorem composeY_toPoly {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (Q : CBivariate F) (p : CPolynomial F) :
    (CBivariate.composeY Q p).toPoly = (CBivariate.toPoly Q).eval p.toPoly
```

`CompPoly.GuruswamiSudan.initialCoefficientPolynomial_evalHorner_eq_composeYCoeff_monomial_zero` (theorem, [line 454](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L454))

```lean
theorem initialCoefficientPolynomial_evalHorner_eq_composeYCoeff_monomial_zero
    {F : Type*} [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (Q : CBivariate F) (c : F) :
    (initialCoefficientPolynomial Q).evalHorner c =
      CBivariate.composeYCoeff Q (CPolynomial.monomial 0 c) 0
```

`CompPoly.GuruswamiSudan.composeYCoeff_monomial_zero_eq_composeY_coeff_zero` (theorem, [line 487](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L487))

```lean
theorem composeYCoeff_monomial_zero_eq_composeY_coeff_zero {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (Q : CBivariate F) (p : CPolynomial F) :
    CBivariate.composeYCoeff Q (CPolynomial.monomial 0 (p.coeff 0)) 0 =
      (CBivariate.composeY Q p).coeff 0
```

`CompPoly.GuruswamiSudan.initialCoefficientPolynomial_eval_eq_composeY_coeff_zero` (theorem, [line 496](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L496))

```lean
theorem initialCoefficientPolynomial_eval_eq_composeY_coeff_zero {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (Q : CBivariate F) (p : CPolynomial F) :
    CPolynomial.eval (p.coeff 0) (initialCoefficientPolynomial Q) =
      (CBivariate.composeY Q p).coeff 0
```

`CompPoly.GuruswamiSudan.rootsInFieldForNonzeroEquation_complete` (theorem, [line 505](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L505))

```lean
theorem rootsInFieldForNonzeroEquation_complete {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (fieldRoots : FieldRootContext F) {p : CPolynomial F} {a : F}
    (hp : p ≠ 0) (ha : CPolynomial.eval a p = 0) :
    a ∈ (rootsInFieldForNonzeroEquation fieldRoots p).toList
```

`CompPoly.GuruswamiSudan.composeY_of_composeYHorner_eq_zero` (theorem, [line 516](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L516))

```lean
theorem composeY_of_composeYHorner_eq_zero {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    {Q : CBivariate F} {p : CPolynomial F}
    (h : CBivariate.composeYHorner Q p = 0) : CBivariate.composeY Q p = 0
```

`CompPoly.GuruswamiSudan.composeYHorner_eq_zero_of_composeY` (theorem, [line 522](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L522))

```lean
theorem composeYHorner_eq_zero_of_composeY {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    {Q : CBivariate F} {p : CPolynomial F}
    (h : CBivariate.composeY Q p = 0) : CBivariate.composeYHorner Q p = 0
```

`CompPoly.GuruswamiSudan.isRootYDegreeLtBool_of_root` (theorem, [line 528](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L528))

```lean
theorem isRootYDegreeLtBool_of_root {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    {Q : CBivariate F} {p : CPolynomial F} {k : Nat}
    (hdegree : degreeLt p k) (hroot : CBivariate.composeY Q p = 0) :
    isRootYDegreeLtBool Q k p = true
```

`CompPoly.GuruswamiSudan.rootsYDegreeLtFromCandidates_sound` (theorem, [line 537](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L537))

```lean
theorem rootsYDegreeLtFromCandidates_sound {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    {candidates : Array (CPolynomial F)} {Q : CBivariate F} {k : Nat}
    {p : CPolynomial F}
    (h : p ∈ (rootsYDegreeLtFromCandidates candidates Q k).toList) :
    degreeLt p k ∧ CBivariate.composeY Q p = 0
```

`CompPoly.GuruswamiSudan.rootsYDegreeLtFromCandidates_eraseDups_sound` (theorem, [line 547](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L547))

```lean
theorem rootsYDegreeLtFromCandidates_eraseDups_sound {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    {candidates : Array (CPolynomial F)} {Q : CBivariate F} {k : Nat}
    {p : CPolynomial F}
    (h : p ∈ (rootsYDegreeLtFromCandidates candidates Q k).eraseDups.toList) :
    degreeLt p k ∧ CBivariate.composeY Q p = 0
```

`CompPoly.GuruswamiSudan.rootsYDegreeLtFromCandidates_complete_of_mem` (theorem, [line 557](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L557))

```lean
theorem rootsYDegreeLtFromCandidates_complete_of_mem {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    {candidates : Array (CPolynomial F)} {Q : CBivariate F} {k : Nat}
    {p : CPolynomial F}
    (hmem : p ∈ candidates.toList)
    (hdegree : degreeLt p k) (hroot : CBivariate.composeY Q p = 0) :
    p ∈ (rootsYDegreeLtFromCandidates candidates Q k).toList
```

`CompPoly.GuruswamiSudan.rootsYDegreeLtFromCandidates_eraseDups_complete_of_mem` (theorem, [line 567](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean#L567))

```lean
theorem rootsYDegreeLtFromCandidates_eraseDups_complete_of_mem {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    {candidates : Array (CPolynomial F)} {Q : CBivariate F} {k : Nat}
    {p : CPolynomial F}
    (hmem : p ∈ candidates.toList)
    (hdegree : degreeLt p k) (hroot : CBivariate.composeY Q p = 0) :
    p ∈ (rootsYDegreeLtFromCandidates candidates Q k).eraseDups.toList
```

## Depends on

- [Common Guruswami-Sudan Root Helpers](../common.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Root/Common/Lemmas.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Root.Common.Lemmas.json)
