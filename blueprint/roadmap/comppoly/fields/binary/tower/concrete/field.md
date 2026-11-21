---
catalog: module
lean: ConcreteBinaryTower.concrete_mul_eq, ConcreteBinaryTower.concrete_zero_mul, ConcreteBinaryTower.concrete_mul_zero, ConcreteBinaryTower.concrete_one_mul, ConcreteBinaryTower.concrete_mul_one, ConcreteBinaryTower.concrete_pow_base_one, ConcreteBinaryTower.concrete_mul_comm, ConcreteBinaryTower.concrete_mul_assoc, ConcreteBinaryTower.concrete_mul_left_distrib, ConcreteBinaryTower.concrete_mul_right_distrib, ConcreteBinaryTower.norm_of_ne_zero_is_ne_zero, ConcreteBinaryTower.concrete_mul_inv_cancel, ConcreteBinaryTower.concrete_inv_one, ConcreteBinaryTower.Z_square_eq, ConcreteBinaryTower.liftBTFieldProps, ConcreteBinaryTower.liftConcreteBTField, ConcreteBinaryTower.concreteCanonicalEmbedding, ConcreteBinaryTower.instAlgebraLiftConcreteBTField, ConcreteBinaryTower.Z_square_mul_form, ConcreteBinaryTower.sum_inv_Z_next_eq, ConcreteBinaryTower.getBTFResult, ConcreteBinaryTower.instFieldConcrete, ConcreteBinaryTower.npow_def, ConcreteBinaryTower.zpow_def, ConcreteBinaryTower.concrete_pow_nat_eq_pow, ConcreteBinaryTower.instCharP2, ConcreteBinaryTower.instFintype, ConcreteBinaryTower.𝕏
statement: formalized
proof: formalized
---

# Concrete Binary Tower Field

`CompPoly.Fields.Binary.Tower.Concrete.Field`, in [CompPoly/Fields/Binary/Tower/Concrete/Field.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Concrete/Field.lean), by Chung Thai Nguyen, Quang Dao.

> Field-structure lemmas for successive levels of the concrete binary tower. The field
> dictionary uses binary natural powers and integer powers that invert the natural-power
> result for negative exponents. The named raw binary-power routine agrees with field powers.
>
> Norm nonvanishing is certified using `QuadraticAlgebra.norm_eq_zero_iff_eq_zero` over the
> predecessor field. This argument does not assume a field structure on the successor level.

> Lemmas of field properties at level k that depends on field properties at level (k-1)

`ConcreteBinaryTower.concrete_mul_eq` (theorem, [line 36](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Concrete/Field.lean#L36))

```lean
theorem concrete_mul_eq
    (prevBTFieldProps : ConcreteBTFieldProps (k := k - 1))
  (a b : ConcreteBTField k) {a₁ a₀ b₁ b₀ : ConcreteBTField (k - 1)}
  (h_a : (a₁, a₀) = split h_k a) (h_b : (b₁, b₀) = split h_k b) :
  concrete_mul a b =
    《 concrete_mul a₀ b₁ + concrete_mul b₀ a₁ + concrete_mul (concrete_mul a₁ b₁) (Z (k - 1)),
      concrete_mul a₀ b₀ + concrete_mul a₁ b₁ 》
```

`ConcreteBinaryTower.concrete_zero_mul` (lemma, [line 97](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Concrete/Field.lean#L97))

```lean
lemma concrete_zero_mul
    (prevBTFieldProps : ConcreteBTFieldProps (k := k - 1))
  (a : ConcreteBTField k) : concrete_mul (zero (k:=k)) a = zero (k:=k)
```

`ConcreteBinaryTower.concrete_mul_zero` (lemma, [line 118](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Concrete/Field.lean#L118))

```lean
lemma concrete_mul_zero
    (prevBTFieldProps : ConcreteBTFieldProps (k := k - 1))
  (a : ConcreteBTField k) : concrete_mul a (zero (k:=k)) = zero (k:=k)
```

`ConcreteBinaryTower.concrete_one_mul` (lemma, [line 142](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Concrete/Field.lean#L142))

```lean
lemma concrete_one_mul
    (prevBTFieldProps : ConcreteBTFieldProps (k := k - 1))
  (a : ConcreteBTField k) : concrete_mul (one (k:=k)) a = a
```

`ConcreteBinaryTower.concrete_mul_one` (lemma, [line 164](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Concrete/Field.lean#L164))

```lean
lemma concrete_mul_one
    (prevBTFieldProps : ConcreteBTFieldProps (k := k - 1))
  (a : ConcreteBTField k) : concrete_mul a (one (k:=k)) = a
```

`ConcreteBinaryTower.concrete_pow_base_one` (lemma, [line 190](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Concrete/Field.lean#L190))

```lean
lemma concrete_pow_base_one
    (prevBTFieldProps : ConcreteBTFieldProps (k := k - 1)) (n : ℕ) :
  concrete_pow_nat (k:=k) (x:=1) n = 1
```

`ConcreteBinaryTower.concrete_mul_comm` (lemma, [line 229](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Concrete/Field.lean#L229))

```lean
lemma concrete_mul_comm
    {h_k : k > 0} (prevBTFieldProps : ConcreteBTFieldProps (k := k - 1))
  (a b : ConcreteBTField k) :
  concrete_mul a b = concrete_mul b a
```

`ConcreteBinaryTower.concrete_mul_assoc` (lemma, [line 268](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Concrete/Field.lean#L268))

> The recursive multiplication is associative at a positive level whenever the predecessor
> level satisfies its field laws.

```lean
lemma concrete_mul_assoc
    {h_k : k > 0} (prevBTFieldProps : ConcreteBTFieldProps (k := k - 1))
  (a b c : ConcreteBTField k) :
  concrete_mul (concrete_mul a b) c = concrete_mul a (concrete_mul b c)
```

`ConcreteBinaryTower.concrete_mul_left_distrib` (lemma, [line 280](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Concrete/Field.lean#L280))

> At a positive level, recursive multiplication distributes over addition in its second
> argument whenever the predecessor level satisfies its field laws.

```lean
lemma concrete_mul_left_distrib
    {h_k : k > 0} (prevBTFieldProps : ConcreteBTFieldProps (k := k - 1))
  (a b c : ConcreteBTField k) :
    concrete_mul a (b + c) = concrete_mul a b + concrete_mul a c
```

`ConcreteBinaryTower.concrete_mul_right_distrib` (lemma, [line 290](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Concrete/Field.lean#L290))

```lean
lemma concrete_mul_right_distrib
    {h_k : k > 0} (prevBTFieldProps : ConcreteBTFieldProps (k := k - 1))
  (a b c : ConcreteBTField k) :
    concrete_mul (a + b) c = concrete_mul a c + concrete_mul b c
```

`ConcreteBinaryTower.norm_of_ne_zero_is_ne_zero` (lemma, [line 316](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Concrete/Field.lean#L316))

> For a nonzero element at a positive level, `lo * (lo + hi * z) + hi * hi` is nonzero
> in the predecessor field, where `lo` and `hi` are its low and high halves and `z = Z (k - 1)`.
> This is the denominator in the quadratic inverse formula.

```lean
lemma norm_of_ne_zero_is_ne_zero {k : ℕ}
    {h_k_gt_0 : k > 0} (prevBTFieldResult : ConcreteBTFStepResult (k := k - 1))
  (a : ConcreteBTField k) (h_a_ne_zero : a ≠ 0) :
  let a₁ := (split h_k_gt_0 a).1
  let a₀ := (split h_k_gt_0 a).2
  concrete_mul a₀ (a₀ + concrete_mul a₁ (Z (k - 1))) + concrete_mul a₁ a₁ ≠ 0
```

`ConcreteBinaryTower.concrete_mul_inv_cancel` (lemma, [line 343](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Concrete/Field.lean#L343))

```lean
lemma concrete_mul_inv_cancel
    (prevBTFieldResult : ConcreteBTFStepResult (k := k - 1))
  (a : ConcreteBTField k) (h : a ≠ 0) :
  concrete_mul a (concrete_inv a) = one
```

`ConcreteBinaryTower.concrete_inv_one` (lemma, [line 431](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Concrete/Field.lean#L431))

```lean
lemma concrete_inv_one :
    concrete_inv (k:=k) 1 = 1
```

> Inductive tower construction, using lemmas from `BTFieldPropsOneLevelLiftingLemmas`

`ConcreteBinaryTower.Z_square_eq` (lemma, [line 443](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Concrete/Field.lean#L443))

```lean
lemma Z_square_eq (k : ℕ) (prevBTFieldProps : ConcreteBTFieldProps (k := k))
    (curBTFieldProps : ConcreteBTFieldProps (k := (k + 1))) :
  letI : Field (ConcreteBTField (k + 1)) := mkFieldInstance curBTFieldProps
  (Z (k + 1)) ^ 2 = 《 Z (k), 1 》
```

`ConcreteBinaryTower.liftBTFieldProps` (theorem, [line 464](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Concrete/Field.lean#L464))

```lean
theorem liftBTFieldProps (k : ℕ) (prevBTFResult : ConcreteBTFStepResult (k := k)) :
  ConcreteBTFieldProps (k + 1)
```

`ConcreteBinaryTower.liftConcreteBTField` (definition, [line 498](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Concrete/Field.lean#L498))

```lean
def liftConcreteBTField (k : ℕ) (prevBTFResult : ConcreteBTFStepResult (k := k)) :
  Field (ConcreteBTField (k + 1))
```

`ConcreteBinaryTower.concreteCanonicalEmbedding` (definition, [line 507](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Concrete/Field.lean#L507))

> The canonical ring homomorphism embedding `ConcreteBTField k` into
> `ConcreteBTField (k + 1)`.
> This is the `AdjoinRoot.of` map.

```lean
def concreteCanonicalEmbedding (k : ℕ)
    (prevBTFieldProps : ConcreteBTFieldProps (k := (k)))
    (curBTFieldProps : ConcreteBTFieldProps (k := (k + 1))) :
  letI := mkFieldInstance prevBTFieldProps
  letI := mkFieldInstance curBTFieldProps
  ConcreteBTField k →+* ConcreteBTField (k + 1)
```

`ConcreteBinaryTower.instAlgebraLiftConcreteBTField` (instance, [line 554](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Concrete/Field.lean#L554))

```lean
instance instAlgebraLiftConcreteBTField (k : ℕ)
  (prevBTFResult : ConcreteBTFStepResult (k := k)) :
  letI := mkFieldInstance (prevBTFResult.toConcreteBTFieldProps)
  letI := liftConcreteBTField (k:=k) prevBTFResult
  Algebra (ConcreteBTField k) (ConcreteBTField (k + 1))
```

`ConcreteBinaryTower.Z_square_mul_form` (lemma, [line 566](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Concrete/Field.lean#L566))

```lean
lemma Z_square_mul_form
    (k : ℕ)
  (prev : ConcreteBTFStepResult (k := k)) :
  letI : Field (ConcreteBTField k) := mkFieldInstance (prev.toConcreteBTFieldProps)
  letI : Field (ConcreteBTField (k + 1)) := mkFieldInstance (k:=k+1)
    (props:=liftBTFieldProps (k:=k) (prevBTFResult:=prev))
  letI : Algebra (ConcreteBTField k) (ConcreteBTField (k + 1)) :=
    instAlgebraLiftConcreteBTField k prev
  Z (k + 1) ^ 2
    = Z (k + 1)
      * (algebraMap (ConcreteBTField k) (ConcreteBTField (k + 1))) (Z k)
      + 1
```

`ConcreteBinaryTower.sum_inv_Z_next_eq` (lemma, [line 602](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Concrete/Field.lean#L602))

```lean
lemma sum_inv_Z_next_eq
    (k : ℕ)
  (prev : ConcreteBTFStepResult (k := k)) :
  letI : Field (ConcreteBTField k) := mkFieldInstance (prev.toConcreteBTFieldProps)
  letI : Field (ConcreteBTField (k + 1)) := mkFieldInstance (k:=k+1)
    (props:=liftBTFieldProps (k:=k) (prevBTFResult:=prev))
  letI : Algebra (ConcreteBTField k) (ConcreteBTField (k + 1)) :=
    instAlgebraLiftConcreteBTField k prev
  Z (k + 1) + (Z (k + 1))⁻¹ = (algebraMap (ConcreteBTField k) (ConcreteBTField (k + 1))) (Z k)
```

`ConcreteBinaryTower.getBTFResult` (definition, [line 624](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Concrete/Field.lean#L624))

```lean
noncomputable def getBTFResult (k : ℕ) : ConcreteBTFStepResult k
```

`ConcreteBinaryTower.instFieldConcrete` (instance, [line 826](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Concrete/Field.lean#L826))

```lean
instance instFieldConcrete {k : ℕ} : Field (ConcreteBTField k)
```

`ConcreteBinaryTower.npow_def` (theorem, [line 830](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Concrete/Field.lean#L830))

> Natural powers use binary exponentiation of the concrete multiplication.

```lean
theorem npow_def (a : ConcreteBTField k) (n : ℕ) : a ^ n = npowBinRec n a
```

`ConcreteBinaryTower.zpow_def` (theorem, [line 833](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Concrete/Field.lean#L833))

> Integer powers use binary exponentiation, followed by inversion for negative exponents.

```lean
theorem zpow_def (a : ConcreteBTField k) (n : ℤ) :
    a ^ n = zpowRec npowBinRec n a
```

`ConcreteBinaryTower.concrete_pow_nat_eq_pow` (theorem, [line 837](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Concrete/Field.lean#L837))

> The raw binary-power routine agrees with natural powers in the field.

```lean
theorem concrete_pow_nat_eq_pow (a : ConcreteBTField k) (n : ℕ) :
    concrete_pow_nat a n = a ^ n
```

`ConcreteBinaryTower.instCharP2` (instance, [line 856](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Concrete/Field.lean#L856))

```lean
instance instCharP2 {k : ℕ} : CharP (ConcreteBTField k) 2
```

`ConcreteBinaryTower.instFintype` (instance, [line 859](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Concrete/Field.lean#L859))

```lean
noncomputable instance instFintype {k : ℕ} : Fintype (ConcreteBTField k)
```

`ConcreteBinaryTower.𝕏` (definition, [line 864](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Concrete/Field.lean#L864))

> adjoined root of poly k, generator of successor field BTField (k + 1)

```lean
def 𝕏 (k : ℕ) : ConcreteBTField (k + 1)
```

## Depends on

- [Concrete binary tower field construction interface](core.md)

## Proof depends on

- [Binary Tower Irreducibility and Trace](../support/irreducibilityandtracemapproperty.md)

## Sources

- [CompPoly/Fields/Binary/Tower/Concrete/Field.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Concrete/Field.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Fields.Binary.Tower.Concrete.Field.json)
