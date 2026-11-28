---
catalog: module
lean: GF_2_fintype, GF_2_pow_card, GF_2_card, non_zero_divisors_iff, neZero_one_of_nontrivial_comm_monoid_zero, unit_of_nontrivial_comm_monoid_with_zero_is_not_zero, GF_2_value_eq_zero_or_one, GF_2_one_add_one_eq_zero, withBot_lt_one_cases, is_unit_iff_deg_0, non_trivial_factors_of_non_trivial_poly_have_deg_ge_1, prod_univ_twos, unique_repr, linear_sum_repr, unique_linear_sum_repr, linear_form_of_elements_in_adjoined_commring, unique_linear_form_of_elements_in_adjoined_commring, GaloisAutomorphism, TraceMapProperty, SpecialElementRelation, two_eq_zero_in_char2_field, sum_of_pow_exp_of_2, sum_square_char2, singleton_subset_Icc, sum_Icc_shift, two_le_two_pow_n_plus_1, one_le_two_pow_n, zero_lt_pow_n, one_le_sub_consecutive_two_pow, two_pow_ne_zero, pow_exp_of_2_repr_given_x_square_repr, inverse_is_root_of_prevPoly, sum_of_root_and_inverse_is_t1, self_sum_eq_zero, sum_zero_iff_eq_of_self_sum_zero, prod_mul_erase, eval₂_quadratic_prevField_coeff, galois_eval_in_BTField, galois_automorphism_power, lifted_trace_map_eval_at_roots_prev_BTField, rsum_eq_t1_square_aux, charP_eq_2_of_add_self_eq_zero
statement: formalized
proof: formalized
---

# Binary Tower Preliminaries

`CompPoly.Fields.Binary.Tower.Support.Preliminaries`, in [CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean), by Quang Dao, Chung Thai Nguyen.

> Shared finite-field and bitwise preliminaries for the binary tower development.

`GF_2_fintype` (instance, [line 30](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L30))

```lean
instance GF_2_fintype : Fintype (GF(2))
```

`GF_2_pow_card` (theorem, [line 33](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L33))

```lean
theorem GF_2_pow_card (x : GF(2)) : x ^ Fintype.card (GF(2)) = x
```

`GF_2_card` (theorem, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L37))

```lean
theorem GF_2_card : Fintype.card (GF(2)) = 2^(2^0)
```

`non_zero_divisors_iff` (theorem, [line 45](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L45))

```lean
theorem non_zero_divisors_iff (M₀ : Type*) [Mul M₀] [Zero M₀] :
    NoZeroDivisors M₀ ↔ ∀ {a b : M₀}, a * b = 0 → a = 0 ∨ b = 0
```

`neZero_one_of_nontrivial_comm_monoid_zero` (instance, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L49))

```lean
instance neZero_one_of_nontrivial_comm_monoid_zero {M₀ : Type*}
  [CommMonoidWithZero M₀] [instNontrivial : Nontrivial M₀] : NeZero (1 : M₀)
```

`unit_of_nontrivial_comm_monoid_with_zero_is_not_zero` (theorem, [line 72](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L72))

```lean
theorem unit_of_nontrivial_comm_monoid_with_zero_is_not_zero
    {R : Type*} [CommMonoidWithZero R] [Nontrivial R] {a : R}
    (h_unit : IsUnit a) : NeZero a
```

`GF_2_value_eq_zero_or_one` (theorem, [line 93](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L93))

> Any element in `GF(2)` is either `0` or `1`.

```lean
theorem GF_2_value_eq_zero_or_one (x : GF(2)) : x = 0 ∨ x = 1
```

`GF_2_one_add_one_eq_zero` (theorem, [line 114](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L114))

```lean
theorem GF_2_one_add_one_eq_zero : (1 + 1 : GF(2)) = 0
```

`withBot_lt_one_cases` (theorem, [line 146](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L146))

```lean
theorem withBot_lt_one_cases (x : WithBot ℕ) (h : x < (1 : ℕ)) : x = ⊥ ∨ x = (0 : ℕ)
```

`is_unit_iff_deg_0` (theorem, [line 159](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L159))

```lean
theorem is_unit_iff_deg_0 {R : Type*} [Field R] {p : R[X]} : p.degree = 0 ↔ IsUnit p
```

`non_trivial_factors_of_non_trivial_poly_have_deg_ge_1` (theorem, [line 189](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L189))

```lean
theorem non_trivial_factors_of_non_trivial_poly_have_deg_ge_1 {R : Type*} [Field R]
    {p a b : R[X]}
    (h_prod : p = a * b)
    (h_p_nonzero : p ≠ 0)
    (h_a_non_unit : ¬IsUnit a)
    (h_b_non_unit : ¬IsUnit b) :
    1 ≤ a.degree ∧ 1 ≤ b.degree
```

`prod_univ_twos` (lemma, [line 221](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L221))

```lean
lemma prod_univ_twos {M : Type*} [CommMonoid M] {n : ℕ} (hn : n = 2) (f : Fin n → M) :
    (∏ i, f i) = f (Fin.cast hn.symm 0) * f (Fin.cast hn.symm 1)
```

`unique_repr` (theorem, [line 227](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L227))

```lean
theorem unique_repr {R : Type*} [CommRing R] {S : Type*} [CommRing S] [Algebra R S]
    (pb : PowerBasis R S) (repr1 repr2 : Fin pb.dim →₀ R)
    (h : ∑ i : Fin pb.dim, repr1 i • pb.basis i = ∑ i : Fin pb.dim, repr2 i • pb.basis i) :
    repr1 = repr2
```

`linear_sum_repr` (theorem, [line 261](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L261))

```lean
theorem linear_sum_repr (R : Type*) [CommRing R] (S : Type*) [CommRing S] [Algebra R S]
    (pb : PowerBasis R S) (h_dim : pb.dim = (2 : ℕ)) (s : S) :
    ∃ a b : R, s = a • pb.gen + algebraMap R S b
```

`unique_linear_sum_repr` (theorem, [line 308](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L308))

```lean
theorem unique_linear_sum_repr (R : Type*) [CommRing R] (S : Type*) [CommRing S] [Algebra R S]
    (pb : PowerBasis R S) (h_dim : pb.dim = 2) (s : S) :
    ∃! p : R × R, s = p.fst • pb.gen + algebraMap R S p.snd
```

`linear_form_of_elements_in_adjoined_commring` (theorem, [line 395](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L395))

```lean
theorem linear_form_of_elements_in_adjoined_commring
    {R : Type*} [CommRing R] (f : R[X]) (hf_deg : f.natDegree = 2)
    (hf_monic : Monic f) (c1 : AdjoinRoot f) :
    ∃ a b : R, c1 = (AdjoinRoot.of f) a * root f + (AdjoinRoot.of f) b
```

`unique_linear_form_of_elements_in_adjoined_commring` (theorem, [line 417](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L417))

```lean
theorem unique_linear_form_of_elements_in_adjoined_commring
    {R : Type*} [CommRing R] (f : R[X]) (hf_deg : f.natDegree = 2)
    (hf_monic : Monic f) (c1 : AdjoinRoot f) :
    ∃! p : R × R, c1 = (AdjoinRoot.of f) p.1 * root f + (AdjoinRoot.of f) p.2
```

`GaloisAutomorphism` (structure, [line 443](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L443))

> Galois automorphism properties for a special element in a binary tower field.
> Encapsulates the key relationship : u^(2^(2^k)) = u⁻¹ and (u⁻¹)^(2^(2^k)) = u

```lean
structure GaloisAutomorphism (F : Type*) [Field F] (u : F) (k : ℕ) : Prop where
  forward : u ^ (2 ^ (2 ^ k)) = u⁻¹
  reverse : (u⁻¹) ^ (2 ^ (2 ^ k)) = u
```

`TraceMapProperty` (structure, [line 451](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L451))

> Trace map properties for elements in a binary tower field extension.
> Asserts that the trace of both an element and its inverse equals 1.

```lean
structure TraceMapProperty (F : Type*) [Field F] (u : F) (k : ℕ) : Prop where
  element_trace : ∑ i ∈ Finset.range (2 ^ k), u ^ (2 ^ i) = 1
  inverse_trace : ∑ i ∈ Finset.range (2 ^ k), (u⁻¹) ^ (2 ^ i) = 1
```

`SpecialElementRelation` (structure, [line 459](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L459))

> Special element relationship in binary tower fields.
> Captures the key equation : u + u⁻¹ = t₁ (lifted previous special element)

```lean
structure SpecialElementRelation {F_prev : Type*} [Field F_prev] (t1 : F_prev)
  {F_cur : Type*} [Field F_cur] (u : F_cur) [Algebra F_prev F_cur] : Prop where
    sum_inv_eq : u + u⁻¹ = algebraMap F_prev F_cur t1
    h_u_square : u^2 = u * (algebraMap F_prev F_cur t1) + 1
```

`two_eq_zero_in_char2_field` (theorem, [line 466](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L466))

```lean
theorem two_eq_zero_in_char2_field {F : Type*} [Field F]
    (sumZeroIffEq : ∀ (x y : F), x + y = 0 ↔ x = y) :
    (2 : F) = 0
```

`sum_of_pow_exp_of_2` (theorem, [line 475](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L475))

```lean
theorem sum_of_pow_exp_of_2 {F : Type*} [Field F]
    (sumZeroIffEq : ∀ (x y : F), x + y = 0 ↔ x = y)
    (i : ℕ) : ∀ (a b c : F), a + b = c → a^(2^i) + b^(2^i) = c^(2^i)
```

`sum_square_char2` (theorem, [line 518](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L518))

```lean
theorem sum_square_char2 {F : Type*} [Field F] (sumZeroIffEq : ∀ (x y : F), x + y = 0 ↔ x = y)
    (s : Finset ℕ) (f : ℕ → F) :
    (∑ j ∈ s, f j)^2 = ∑ j ∈ s, (f j)^2
```

`singleton_subset_Icc` (theorem, [line 537](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L537))

```lean
theorem singleton_subset_Icc (n : ℕ) : {1} ⊆ Finset.Icc 1 (n + 1)
```

`sum_Icc_shift` (theorem, [line 544](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L544))

```lean
theorem sum_Icc_shift {M : Type*} [AddCommMonoid M] (f : ℕ → M) (a b shift : ℕ) :
    ∑ j ∈ Finset.Icc a b, f (j + shift) = ∑ j ∈ Finset.Icc (a + shift) (b + shift), f j
```

`two_le_two_pow_n_plus_1` (theorem, [line 556](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L556))

```lean
theorem two_le_two_pow_n_plus_1 (n : ℕ) : 2 ≤ 2 ^ (n + 1)
```

`one_le_two_pow_n` (theorem, [line 561](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L561))

```lean
theorem one_le_two_pow_n (n : ℕ) : 1 ≤ 2 ^ n
```

`zero_lt_pow_n` (theorem, [line 566](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L566))

```lean
theorem zero_lt_pow_n (m : ℕ) (n : ℕ) (h_m : m > 0): 0 < m^n
```

`one_le_sub_consecutive_two_pow` (theorem, [line 570](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L570))

```lean
theorem one_le_sub_consecutive_two_pow (n : ℕ): 1 ≤ 2^(n+1) - 2^n
```

`two_pow_ne_zero` (theorem, [line 577](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L577))

```lean
theorem two_pow_ne_zero (n : ℕ) : 2 ^ n ≠ 0
```

`pow_exp_of_2_repr_given_x_square_repr` (theorem, [line 586](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L586))

> For any field element (x : F) where x^2 = x*z + 1, this theorem gives
> a closed form for x^(2^i).

```lean
theorem pow_exp_of_2_repr_given_x_square_repr {F : Type*} [instField : Field F]
    (sumZeroIffEq : ∀ (x y : F), x + y = 0 ↔ x = y) (x z : F) (h_z_non_zero : z ≠ 0)
    (h_x_square : x ^ 2 = x * z + 1) :
    ∀ i : ℕ, x^(2^i) = x * z^(2^i - 1) + ∑ j ∈ Finset.Icc 1 i, z^(2^i - 2^j)
```

`inverse_is_root_of_prevPoly` (theorem, [line 784](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L784))

```lean
theorem inverse_is_root_of_prevPoly
    {prevBTField : Type*} [Field prevBTField]
    {curBTField : Type*} [Field curBTField]
    (of_prev : prevBTField →+* curBTField)
    (u : curBTField) (t1 : prevBTField)
    (specialElementNeZero : u ≠ 0)
    (eval_prevPoly_at_root : u ^ 2 + of_prev t1 * u + 1 = 0)
    (h_eval : ∀ (x : curBTField),
      eval₂ of_prev x (X ^ 2 + (C t1 * X + 1)) = x ^ 2 + of_prev t1 * x + 1) :
    eval₂ of_prev u⁻¹ (X ^ 2 + (C t1 * X + 1)) = 0
```

`sum_of_root_and_inverse_is_t1` (theorem, [line 825](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L825))

```lean
theorem sum_of_root_and_inverse_is_t1
    {curBTField : Type*} [Field curBTField]
    (u : curBTField) (t1 : curBTField) -- here t1 is already lifted to curBTField
    (specialElementNeZero : u ≠ 0)
    (eval_prevPoly_at_root : u ^ 2 + t1 * u + 1 = 0)
    (sumZeroIffEq : ∀ (x y : curBTField), x + y = 0 ↔ x = y) :
    u + u⁻¹ = t1
```

`self_sum_eq_zero` (theorem, [line 854](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L854))

```lean
theorem self_sum_eq_zero
    {prevBTField : Type*} [CommRing prevBTField]
    (sumZeroIffEqPrev : ∀ (x y : prevBTField), x + y = 0 ↔ x = y)
    (prevPoly : Polynomial prevBTField)
    (hf_deg : prevPoly.natDegree = 2)
    (hf_monic : Monic prevPoly) :
    ∀ (x : AdjoinRoot prevPoly), x + x = 0
```

`sum_zero_iff_eq_of_self_sum_zero` (theorem, [line 883](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L883))

```lean
theorem sum_zero_iff_eq_of_self_sum_zero {F : Type*} [AddGroup F]
    (h_self_sum_eq_zero : ∀ (x : F), x + x = 0) :
    ∀ (x y : F), x + y = 0 ↔ x = y
```

`prod_mul_erase` (theorem, [line 903](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L903))

> A variant of `Finset.mul_prod_erase` with the multiplication swapped.

```lean
theorem prod_mul_erase {α β : Type*} [CommMonoid β] [DecidableEq α] (s : Finset α) (f : α → β)
    {a : α} (h : a ∈ s) :
    f a * (∏ x ∈ s.erase a, f x) = ∏ x ∈ s, f x
```

`eval₂_quadratic_prevField_coeff` (theorem, [line 908](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L908))

```lean
theorem eval₂_quadratic_prevField_coeff
    {prevBTField : Type*} [CommRing prevBTField]
    {curBTField : Type*} [CommRing curBTField]
    (of_prev : prevBTField →+* curBTField)
    (t1 : prevBTField)
    (x : curBTField) :
    eval₂ of_prev x (X^2 + (C t1 * X + 1)) = x^2 + of_prev t1 * x + 1
```

`galois_eval_in_BTField` (lemma, [line 920](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L920))

```lean
lemma galois_eval_in_BTField
    {curBTField : Type*} [Field curBTField]
    (u : curBTField) (t1 : curBTField) -- here t1 is already lifted to curBTField
    (k : ℕ)
    (sumZeroIffEq : ∀ (x y : curBTField), x + y = 0 ↔ x = y)
    (prevSpecialElementNeZero : t1 ≠ 0)
    (u_plus_inv_eq_t1 : u + u⁻¹ = t1)
    (h_u_square : u^2 = u*t1 + 1)
    (h_t1_pow : t1^(2^(2^k)-1) = 1 ∧ (t1⁻¹)^(2^(2^k)-1) = 1)
    (h_t1_pow_2_pow_2_pow_k :  t1^(2^(2^k)) = t1)
    (h_t1_inv_pow_2_pow_2_pow_k :  (t1⁻¹)^(2^(2^k)) = t1⁻¹)
    (trace_map_at_inv : ∑ i ∈ Finset.range (2 ^ k), t1⁻¹ ^ (2 ^ i) = 1) :
    u^(2^(2^k)) = u⁻¹
```

`galois_automorphism_power` (theorem, [line 1011](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L1011))

```lean
theorem galois_automorphism_power
    {curBTField : Type*} [Field curBTField]
    (u : curBTField) (t1 : curBTField) -- here t1 is already lifted to curBTField
    (k : ℕ)
    (sumZeroIffEq : ∀ (x y : curBTField), x + y = 0 ↔ x = y)
    (specialElementNeZero : u ≠ 0)
    (prevSpecialElementNeZero : t1 ≠ 0)
    (u_plus_inv_eq_t1 : u + u⁻¹ = t1)
    (h_u_square : u ^ 2 = u * t1 + 1)
    (h_t1_pow : t1 ^ (2 ^ (2 ^ k) - 1) = 1 ∧ (t1⁻¹) ^ (2 ^ (2 ^ k) - 1) = 1)
    (trace_map_roots : ∑ i ∈ Finset.range (2 ^ k), t1 ^ (2 ^ i) = 1 ∧
                      ∑ i ∈ Finset.range (2 ^ k), t1⁻¹ ^ (2 ^ i) = 1) :
    u^(2^(2^k)) = u⁻¹ ∧ (u⁻¹)^(2^(2^k)) = u
```

`lifted_trace_map_eval_at_roots_prev_BTField` (lemma, [line 1077](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L1077))

```lean
lemma lifted_trace_map_eval_at_roots_prev_BTField
    {curBTField : Type*} [Field curBTField]
    (u : curBTField) (t1 : curBTField) -- here t1 is already lifted to curBTField
    (k : ℕ)
    (sumZeroIffEq : ∀ (x y : curBTField), x + y = 0 ↔ x = y)
    (u_plus_inv_eq_t1 : u + u⁻¹ = t1)
    (galois_automorphism : u^(2^(2^k)) = u⁻¹ ∧ (u⁻¹)^(2^(2^k)) = u)
    (trace_map_at_prev_root : ∑ i ∈ Finset.range (2 ^ k), t1 ^ (2 ^ i) = 1) :
    ∑ i ∈ Finset.range (2 ^ (k+1)), u ^ (2 ^ i) = 1
```

`rsum_eq_t1_square_aux` (theorem, [line 1178](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L1178))

```lean
theorem rsum_eq_t1_square_aux
    {curBTField : Type*} [Field curBTField] -- curBTField ≃ 𝔽_{2^{2^k}}
    (u : curBTField) -- here u is already lifted to curBTField
    (k : ℕ)
    (x_pow_card : ∀ (x : curBTField), x ^ (2 ^ (2 ^ (k))) = x)
    (u_ne_zero : u ≠ 0)
    (trace_map_prop : TraceMapProperty curBTField u k) :
    ∑ j ∈ Finset.Icc 1 (2 ^ (k)), u ^ (2 ^ 2 ^ (k) - 2 ^ j) = u
```

`charP_eq_2_of_add_self_eq_zero` (theorem, [line 1291](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean#L1291))

```lean
theorem charP_eq_2_of_add_self_eq_zero {F : Type*} [Field F]
    (sumZeroIffEq : ∀ (x y : F), x + y = 0 ↔ x = y) : CharP F 2
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Proof depends on

- [More lemmas about Fin and big operators](../../../../data/fin/bigoperators.md)

## Sources

- [CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/Support/Preliminaries.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Fields.Binary.Tower.Support.Preliminaries.json)
