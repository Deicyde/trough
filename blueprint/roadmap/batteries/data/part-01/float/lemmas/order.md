---
catalog: module
lean: Float.Model.UnpackedFloat.Sign.compare_def, Float.Model.UnpackedFloat.compare_swap, Float.Model.UnpackedFloat.lt_irrefl, Float.Model.UnpackedFloat.lt_asymm, Float.Model.UnpackedFloat.lt_trans, Float.Model.UnpackedFloat.le_trans, Float.Model.UnpackedFloat.lt_of_lt_of_le, Float.Model.UnpackedFloat.lt_of_le_of_lt, Float.Model.UnpackedFloat.le_of_lt, Float.Model.UnpackedFloat.lt_iff_le_not_ge, Float.Model.UnpackedFloat.le_refl_iff, Float.Model.UnpackedFloat.not_le, Float.Model.UnpackedFloat.notANumber_le, Float.Model.UnpackedFloat.le_notANumber, Float.Model.UnpackedFloat.notANumber_lt, Float.Model.UnpackedFloat.lt_notANumber, Float.Model.UnpackedFloat.neg_lt_neg, Float.Model.UnpackedFloat.neg_le_neg, Float.Model.UnpackedFloat.minimum_comm, Float.Model.UnpackedFloat.maximum_comm, Float.Model.lt_iff_unpack_lt, Float.Model.le_iff_unpack_le, Float.Model.eq_nan_iff_unpack_eq, Float.Model.unpack_neg, Float.Model.lt_irrefl, Float.Model.lt_asymm, Float.Model.lt_trans, Float.Model.le_trans, Float.Model.lt_of_lt_of_le, Float.Model.lt_of_le_of_lt, Float.Model.le_of_lt, Float.Model.lt_iff_le_not_ge, Float.Model.le_refl_iff, Float.Model.not_le, Float.Model.not_nan_lt, Float.Model.not_lt_nan, Float.Model.not_nan_le, Float.Model.not_le_nan, Float.Model.neg_lt_neg_iff, Float.Model.neg_le_neg_iff, Float.Model.minimum_comm, Float.Model.maximum_comm, Float.toModel_nan, Float.toModel_neg, Float.lt_iff_toModel_lt, Float.le_iff_toModel_le, Float.eq_nan_iff_toModel_eq, Float.lt_irrefl, Float.lt_asymm, Float.lt_trans, Float.le_trans, Float.lt_of_lt_of_le, Float.lt_of_le_of_lt, Float.le_of_lt, Float.lt_iff_le_not_ge, Float.le_refl_iff, Float.not_le, Float.not_nan_lt, Float.not_lt_nan, Float.not_nan_le, Float.not_le_nan, Float.neg_lt_neg_iff, Float.neg_le_neg_iff, Float.min_comm, Float.max_comm, Float32.Model.lt_iff_unpack_lt, Float32.Model.le_iff_unpack_le, Float32.Model.eq_nan_iff_unpack_eq, Float32.Model.unpack_neg, Float32.Model.lt_irrefl, Float32.Model.lt_asymm, Float32.Model.lt_trans, Float32.Model.le_trans, Float32.Model.lt_of_lt_of_le, Float32.Model.lt_of_le_of_lt, Float32.Model.le_of_lt, Float32.Model.lt_iff_le_not_ge, Float32.Model.le_refl_iff, Float32.Model.not_le, Float32.Model.not_nan_lt, Float32.Model.not_lt_nan, Float32.Model.not_nan_le, Float32.Model.not_le_nan, Float32.Model.neg_lt_neg_iff, Float32.Model.neg_le_neg_iff, Float32.Model.minimum_comm, Float32.Model.maximum_comm, Float32.toModel_nan, Float32.toModel_neg, Float32.lt_iff_toModel_lt, Float32.le_iff_toModel_le, Float32.eq_nan_iff_toModel_eq, Float32.lt_irrefl, Float32.lt_asymm, Float32.lt_trans, Float32.le_trans, Float32.lt_of_lt_of_le, Float32.lt_of_le_of_lt, Float32.le_of_lt, Float32.lt_iff_le_not_ge, Float32.le_refl_iff, Float32.not_le, Float32.not_nan_lt, Float32.not_lt_nan, Float32.not_nan_le, Float32.not_le_nan, Float32.neg_lt_neg_iff, Float32.neg_le_neg_iff, Float32.min_comm, Float32.max_comm
statement: formalized
proof: formalized
---

# Order lemmas for `Float` and `Float32`

`Batteries.Data.Float.Lemmas.Order`, in [Batteries/Data/Float/Lemmas/Order.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean), by François G. Dorais.

> The lemmas are proved through the logical models `Float.Model` and `Float32.Model`. The order is
> the IEEE 754 partial order, in which `NaN` is incomparable with everything and `-0 = +0`.

`Float.Model.UnpackedFloat.Sign.compare_def` (theorem, [line 23](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L23))

```lean
theorem compare_def (s t : Sign) : compare s t =
    match s, t with
    | .negative, .positive => .lt | .positive, .negative => .gt | _, _ => .eq
```

`Float.Model.UnpackedFloat.compare_swap` (theorem, [line 41](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L41))

```lean
protected theorem compare_swap (a b : UnpackedFloat) :
    b.compare a = (a.compare b).map Ordering.swap
```

`Float.Model.UnpackedFloat.lt_irrefl` (theorem, [line 45](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L45))

```lean
protected theorem lt_irrefl (a : UnpackedFloat) : ¬ a.lt a
```

`Float.Model.UnpackedFloat.lt_asymm` (theorem, [line 48](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L48))

```lean
protected theorem lt_asymm {a b : UnpackedFloat} : a.lt b → ¬ b.lt a
```

`Float.Model.UnpackedFloat.lt_trans` (theorem, [line 51](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L51))

```lean
protected theorem lt_trans {a b c : UnpackedFloat} : a.lt b → b.lt c → a.lt c
```

`Float.Model.UnpackedFloat.le_trans` (theorem, [line 54](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L54))

```lean
protected theorem le_trans {a b c : UnpackedFloat} : a.le b → b.le c → a.le c
```

`Float.Model.UnpackedFloat.lt_of_lt_of_le` (theorem, [line 57](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L57))

```lean
protected theorem lt_of_lt_of_le {a b c : UnpackedFloat} : a.lt b → b.le c → a.lt c
```

`Float.Model.UnpackedFloat.lt_of_le_of_lt` (theorem, [line 60](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L60))

```lean
protected theorem lt_of_le_of_lt {a b c : UnpackedFloat} : a.le b → b.lt c → a.lt c
```

`Float.Model.UnpackedFloat.le_of_lt` (theorem, [line 63](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L63))

```lean
protected theorem le_of_lt {a b : UnpackedFloat} : a.lt b → a.le b
```

`Float.Model.UnpackedFloat.lt_iff_le_not_ge` (theorem, [line 66](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L66))

```lean
protected theorem lt_iff_le_not_ge {a b : UnpackedFloat} : a.lt b ↔ a.le b ∧ ¬ b.le a
```

`Float.Model.UnpackedFloat.le_refl_iff` (theorem, [line 69](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L69))

```lean
theorem le_refl_iff {a : UnpackedFloat} : a.le a ↔ a ≠ notANumber
```

`Float.Model.UnpackedFloat.not_le` (theorem, [line 72](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L72))

```lean
protected theorem not_le {a b : UnpackedFloat} (ha : a ≠ notANumber) (hb : b ≠ notANumber) :
    ¬ a.le b ↔ b.lt a
```

`Float.Model.UnpackedFloat.notANumber_le` (theorem, [line 76](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L76))

```lean
theorem notANumber_le (a : UnpackedFloat) : notANumber.le a = false
```

`Float.Model.UnpackedFloat.le_notANumber` (theorem, [line 77](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L77))

```lean
theorem le_notANumber (a : UnpackedFloat) : a.le notANumber = false
```

`Float.Model.UnpackedFloat.notANumber_lt` (theorem, [line 78](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L78))

```lean
theorem notANumber_lt (a : UnpackedFloat) : notANumber.lt a = false
```

`Float.Model.UnpackedFloat.lt_notANumber` (theorem, [line 79](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L79))

```lean
theorem lt_notANumber (a : UnpackedFloat) : a.lt notANumber = false
```

`Float.Model.UnpackedFloat.neg_lt_neg` (theorem, [line 81](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L81))

```lean
protected theorem neg_lt_neg (a b : UnpackedFloat) : a.neg.lt b.neg = b.lt a
```

`Float.Model.UnpackedFloat.neg_le_neg` (theorem, [line 84](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L84))

```lean
protected theorem neg_le_neg (a b : UnpackedFloat) : a.neg.le b.neg = b.le a
```

`Float.Model.UnpackedFloat.minimum_comm` (theorem, [line 87](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L87))

```lean
theorem minimum_comm (a b : UnpackedFloat) : a.minimum b = b.minimum a
```

`Float.Model.UnpackedFloat.maximum_comm` (theorem, [line 91](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L91))

```lean
theorem maximum_comm (a b : UnpackedFloat) : a.maximum b = b.maximum a
```

`Float.Model.lt_iff_unpack_lt` (theorem, [line 101](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L101))

```lean
theorem lt_iff_unpack_lt {a b : Float.Model} : a < b ↔ a.unpack.lt b.unpack
```

`Float.Model.le_iff_unpack_le` (theorem, [line 103](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L103))

```lean
theorem le_iff_unpack_le {a b : Float.Model} : a ≤ b ↔ a.unpack.le b.unpack
```

`Float.Model.eq_nan_iff_unpack_eq` (theorem, [line 105](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L105))

```lean
theorem eq_nan_iff_unpack_eq {a : Float.Model} : a = nan ↔ a.unpack = .notANumber
```

`Float.Model.unpack_neg` (theorem, [line 110](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L110))

```lean
theorem unpack_neg (a : Float.Model) : (-a).unpack = a.unpack.neg
```

`Float.Model.lt_irrefl` (theorem, [line 112](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L112))

```lean
protected theorem lt_irrefl (a : Float.Model) : ¬a < a
```

`Float.Model.lt_asymm` (theorem, [line 114](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L114))

```lean
protected theorem lt_asymm {a b : Float.Model} : a < b → ¬b < a
```

`Float.Model.lt_trans` (theorem, [line 116](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L116))

```lean
protected theorem lt_trans {a b c : Float.Model} : a < b → b < c → a < c
```

`Float.Model.le_trans` (theorem, [line 118](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L118))

```lean
protected theorem le_trans {a b c : Float.Model} : a ≤ b → b ≤ c → a ≤ c
```

`Float.Model.lt_of_lt_of_le` (theorem, [line 120](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L120))

```lean
protected theorem lt_of_lt_of_le {a b c : Float.Model} : a < b → b ≤ c → a < c
```

`Float.Model.lt_of_le_of_lt` (theorem, [line 123](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L123))

```lean
protected theorem lt_of_le_of_lt {a b c : Float.Model} : a ≤ b → b < c → a < c
```

`Float.Model.le_of_lt` (theorem, [line 126](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L126))

```lean
protected theorem le_of_lt {a b : Float.Model} : a < b → a ≤ b
```

`Float.Model.lt_iff_le_not_ge` (theorem, [line 128](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L128))

```lean
protected theorem lt_iff_le_not_ge {a b : Float.Model} : a < b ↔ a ≤ b ∧ ¬b ≤ a
```

`Float.Model.le_refl_iff` (theorem, [line 131](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L131))

```lean
theorem le_refl_iff {a : Float.Model} : a ≤ a ↔ a ≠ nan
```

`Float.Model.not_le` (theorem, [line 134](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L134))

```lean
protected theorem not_le {a b : Float.Model} (ha : a ≠ nan) (hb : b ≠ nan) : ¬a ≤ b ↔ b < a
```

`Float.Model.not_nan_lt` (theorem, [line 138](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L138))

```lean
theorem not_nan_lt (a : Float.Model) : ¬nan < a
```

`Float.Model.not_lt_nan` (theorem, [line 141](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L141))

```lean
theorem not_lt_nan (a : Float.Model) : ¬a < nan
```

`Float.Model.not_nan_le` (theorem, [line 144](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L144))

```lean
theorem not_nan_le (a : Float.Model) : ¬nan ≤ a
```

`Float.Model.not_le_nan` (theorem, [line 147](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L147))

```lean
theorem not_le_nan (a : Float.Model) : ¬a ≤ nan
```

`Float.Model.neg_lt_neg_iff` (theorem, [line 150](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L150))

```lean
protected theorem neg_lt_neg_iff {a b : Float.Model} : -a < -b ↔ b < a
```

`Float.Model.neg_le_neg_iff` (theorem, [line 153](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L153))

```lean
protected theorem neg_le_neg_iff {a b : Float.Model} : -a ≤ -b ↔ b ≤ a
```

`Float.Model.minimum_comm` (theorem, [line 156](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L156))

```lean
theorem minimum_comm (a b : Float.Model) : a.minimum b = b.minimum a
```

`Float.Model.maximum_comm` (theorem, [line 159](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L159))

```lean
theorem maximum_comm (a b : Float.Model) : a.maximum b = b.maximum a
```

`Float.toModel_nan` (theorem, [line 166](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L166))

```lean
theorem toModel_nan : nan.toModel = .nan
```

`Float.toModel_neg` (theorem, [line 168](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L168))

```lean
theorem toModel_neg (x : Float) : (-x).toModel = -x.toModel
```

`Float.lt_iff_toModel_lt` (theorem, [line 170](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L170))

```lean
theorem lt_iff_toModel_lt {x y : Float} : x < y ↔ x.toModel < y.toModel
```

`Float.le_iff_toModel_le` (theorem, [line 174](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L174))

```lean
theorem le_iff_toModel_le {x y : Float} : x ≤ y ↔ x.toModel ≤ y.toModel
```

`Float.eq_nan_iff_toModel_eq` (theorem, [line 178](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L178))

```lean
theorem eq_nan_iff_toModel_eq {x : Float} : x = nan ↔ x.toModel = .nan
```

`Float.lt_irrefl` (theorem, [line 181](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L181))

```lean
protected theorem lt_irrefl (x : Float) : ¬x < x
```

`Float.lt_asymm` (theorem, [line 184](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L184))

```lean
protected theorem lt_asymm {x y : Float} : x < y → ¬y < x
```

`Float.lt_trans` (theorem, [line 187](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L187))

```lean
protected theorem lt_trans {x y z : Float} : x < y → y < z → x < z
```

`Float.le_trans` (theorem, [line 190](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L190))

```lean
protected theorem le_trans {x y z : Float} : x ≤ y → y ≤ z → x ≤ z
```

`Float.lt_of_lt_of_le` (theorem, [line 193](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L193))

```lean
protected theorem lt_of_lt_of_le {x y z : Float} : x < y → y ≤ z → x < z
```

`Float.lt_of_le_of_lt` (theorem, [line 197](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L197))

```lean
protected theorem lt_of_le_of_lt {x y z : Float} : x ≤ y → y < z → x < z
```

`Float.le_of_lt` (theorem, [line 201](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L201))

```lean
protected theorem le_of_lt {x y : Float} : x < y → x ≤ y
```

`Float.lt_iff_le_not_ge` (theorem, [line 204](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L204))

```lean
protected theorem lt_iff_le_not_ge {x y : Float} : x < y ↔ x ≤ y ∧ ¬y ≤ x
```

`Float.le_refl_iff` (theorem, [line 207](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L207))

```lean
theorem le_refl_iff {x : Float} : x ≤ x ↔ x ≠ nan
```

`Float.not_le` (theorem, [line 210](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L210))

```lean
protected theorem not_le {x y : Float} (hx : x ≠ nan) (hy : y ≠ nan) : ¬x ≤ y ↔ y < x
```

`Float.not_nan_lt` (theorem, [line 214](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L214))

```lean
theorem not_nan_lt (x : Float) : ¬nan < x
```

`Float.not_lt_nan` (theorem, [line 217](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L217))

```lean
theorem not_lt_nan (x : Float) : ¬x < nan
```

`Float.not_nan_le` (theorem, [line 220](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L220))

```lean
theorem not_nan_le (x : Float) : ¬nan ≤ x
```

`Float.not_le_nan` (theorem, [line 223](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L223))

```lean
theorem not_le_nan (x : Float) : ¬x ≤ nan
```

`Float.neg_lt_neg_iff` (theorem, [line 226](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L226))

```lean
protected theorem neg_lt_neg_iff {x y : Float} : -x < -y ↔ y < x
```

`Float.neg_le_neg_iff` (theorem, [line 229](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L229))

```lean
protected theorem neg_le_neg_iff {x y : Float} : -x ≤ -y ↔ y ≤ x
```

`Float.min_comm` (theorem, [line 232](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L232))

```lean
protected theorem min_comm (x y : Float) : min x y = min y x
```

`Float.max_comm` (theorem, [line 236](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L236))

```lean
protected theorem max_comm (x y : Float) : max x y = max y x
```

`Float32.Model.lt_iff_unpack_lt` (theorem, [line 246](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L246))

```lean
theorem lt_iff_unpack_lt {a b : Float32.Model} : a < b ↔ a.unpack.lt b.unpack
```

`Float32.Model.le_iff_unpack_le` (theorem, [line 248](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L248))

```lean
theorem le_iff_unpack_le {a b : Float32.Model} : a ≤ b ↔ a.unpack.le b.unpack
```

`Float32.Model.eq_nan_iff_unpack_eq` (theorem, [line 250](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L250))

```lean
theorem eq_nan_iff_unpack_eq {a : Float32.Model} : a = nan ↔ a.unpack = .notANumber
```

`Float32.Model.unpack_neg` (theorem, [line 255](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L255))

```lean
theorem unpack_neg (a : Float32.Model) : (-a).unpack = a.unpack.neg
```

`Float32.Model.lt_irrefl` (theorem, [line 257](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L257))

```lean
protected theorem lt_irrefl (a : Float32.Model) : ¬a < a
```

`Float32.Model.lt_asymm` (theorem, [line 259](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L259))

```lean
protected theorem lt_asymm {a b : Float32.Model} : a < b → ¬b < a
```

`Float32.Model.lt_trans` (theorem, [line 261](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L261))

```lean
protected theorem lt_trans {a b c : Float32.Model} : a < b → b < c → a < c
```

`Float32.Model.le_trans` (theorem, [line 263](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L263))

```lean
protected theorem le_trans {a b c : Float32.Model} : a ≤ b → b ≤ c → a ≤ c
```

`Float32.Model.lt_of_lt_of_le` (theorem, [line 265](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L265))

```lean
protected theorem lt_of_lt_of_le {a b c : Float32.Model} : a < b → b ≤ c → a < c
```

`Float32.Model.lt_of_le_of_lt` (theorem, [line 268](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L268))

```lean
protected theorem lt_of_le_of_lt {a b c : Float32.Model} : a ≤ b → b < c → a < c
```

`Float32.Model.le_of_lt` (theorem, [line 271](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L271))

```lean
protected theorem le_of_lt {a b : Float32.Model} : a < b → a ≤ b
```

`Float32.Model.lt_iff_le_not_ge` (theorem, [line 273](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L273))

```lean
protected theorem lt_iff_le_not_ge {a b : Float32.Model} : a < b ↔ a ≤ b ∧ ¬b ≤ a
```

`Float32.Model.le_refl_iff` (theorem, [line 276](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L276))

```lean
theorem le_refl_iff {a : Float32.Model} : a ≤ a ↔ a ≠ nan
```

`Float32.Model.not_le` (theorem, [line 279](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L279))

```lean
protected theorem not_le {a b : Float32.Model} (ha : a ≠ nan) (hb : b ≠ nan) : ¬a ≤ b ↔ b < a
```

`Float32.Model.not_nan_lt` (theorem, [line 283](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L283))

```lean
theorem not_nan_lt (a : Float32.Model) : ¬nan < a
```

`Float32.Model.not_lt_nan` (theorem, [line 286](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L286))

```lean
theorem not_lt_nan (a : Float32.Model) : ¬a < nan
```

`Float32.Model.not_nan_le` (theorem, [line 289](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L289))

```lean
theorem not_nan_le (a : Float32.Model) : ¬nan ≤ a
```

`Float32.Model.not_le_nan` (theorem, [line 292](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L292))

```lean
theorem not_le_nan (a : Float32.Model) : ¬a ≤ nan
```

`Float32.Model.neg_lt_neg_iff` (theorem, [line 295](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L295))

```lean
protected theorem neg_lt_neg_iff {a b : Float32.Model} : -a < -b ↔ b < a
```

`Float32.Model.neg_le_neg_iff` (theorem, [line 298](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L298))

```lean
protected theorem neg_le_neg_iff {a b : Float32.Model} : -a ≤ -b ↔ b ≤ a
```

`Float32.Model.minimum_comm` (theorem, [line 301](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L301))

```lean
theorem minimum_comm (a b : Float32.Model) : a.minimum b = b.minimum a
```

`Float32.Model.maximum_comm` (theorem, [line 304](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L304))

```lean
theorem maximum_comm (a b : Float32.Model) : a.maximum b = b.maximum a
```

`Float32.toModel_nan` (theorem, [line 311](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L311))

```lean
theorem toModel_nan : nan.toModel = .nan
```

`Float32.toModel_neg` (theorem, [line 313](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L313))

```lean
theorem toModel_neg (x : Float32) : (-x).toModel = -x.toModel
```

`Float32.lt_iff_toModel_lt` (theorem, [line 315](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L315))

```lean
theorem lt_iff_toModel_lt {x y : Float32} : x < y ↔ x.toModel < y.toModel
```

`Float32.le_iff_toModel_le` (theorem, [line 319](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L319))

```lean
theorem le_iff_toModel_le {x y : Float32} : x ≤ y ↔ x.toModel ≤ y.toModel
```

`Float32.eq_nan_iff_toModel_eq` (theorem, [line 323](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L323))

```lean
theorem eq_nan_iff_toModel_eq {x : Float32} : x = nan ↔ x.toModel = .nan
```

`Float32.lt_irrefl` (theorem, [line 326](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L326))

```lean
protected theorem lt_irrefl (x : Float32) : ¬x < x
```

`Float32.lt_asymm` (theorem, [line 329](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L329))

```lean
protected theorem lt_asymm {x y : Float32} : x < y → ¬y < x
```

`Float32.lt_trans` (theorem, [line 332](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L332))

```lean
protected theorem lt_trans {x y z : Float32} : x < y → y < z → x < z
```

`Float32.le_trans` (theorem, [line 335](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L335))

```lean
protected theorem le_trans {x y z : Float32} : x ≤ y → y ≤ z → x ≤ z
```

`Float32.lt_of_lt_of_le` (theorem, [line 338](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L338))

```lean
protected theorem lt_of_lt_of_le {x y z : Float32} : x < y → y ≤ z → x < z
```

`Float32.lt_of_le_of_lt` (theorem, [line 342](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L342))

```lean
protected theorem lt_of_le_of_lt {x y z : Float32} : x ≤ y → y < z → x < z
```

`Float32.le_of_lt` (theorem, [line 346](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L346))

```lean
protected theorem le_of_lt {x y : Float32} : x < y → x ≤ y
```

`Float32.lt_iff_le_not_ge` (theorem, [line 349](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L349))

```lean
protected theorem lt_iff_le_not_ge {x y : Float32} : x < y ↔ x ≤ y ∧ ¬y ≤ x
```

`Float32.le_refl_iff` (theorem, [line 352](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L352))

```lean
theorem le_refl_iff {x : Float32} : x ≤ x ↔ x ≠ nan
```

`Float32.not_le` (theorem, [line 355](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L355))

```lean
protected theorem not_le {x y : Float32} (hx : x ≠ nan) (hy : y ≠ nan) : ¬x ≤ y ↔ y < x
```

`Float32.not_nan_lt` (theorem, [line 359](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L359))

```lean
theorem not_nan_lt (x : Float32) : ¬nan < x
```

`Float32.not_lt_nan` (theorem, [line 362](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L362))

```lean
theorem not_lt_nan (x : Float32) : ¬x < nan
```

`Float32.not_nan_le` (theorem, [line 365](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L365))

```lean
theorem not_nan_le (x : Float32) : ¬nan ≤ x
```

`Float32.not_le_nan` (theorem, [line 368](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L368))

```lean
theorem not_le_nan (x : Float32) : ¬x ≤ nan
```

`Float32.neg_lt_neg_iff` (theorem, [line 371](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L371))

```lean
protected theorem neg_lt_neg_iff {x y : Float32} : -x < -y ↔ y < x
```

`Float32.neg_le_neg_iff` (theorem, [line 374](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L374))

```lean
protected theorem neg_le_neg_iff {x y : Float32} : -x ≤ -y ↔ y ≤ x
```

`Float32.min_comm` (theorem, [line 377](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L377))

```lean
protected theorem min_comm (x y : Float32) : min x y = min y x
```

`Float32.max_comm` (theorem, [line 381](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean#L381))

```lean
protected theorem max_comm (x y : Float32) : max x y = max y x
```

## Depends on

Its statements use no other Batteries module's declarations.

## Proof depends on

- [Sign and commutativity lemmas for `Float` and `Float32`](arithmetic.md)

## Sources

- [Batteries/Data/Float/Lemmas/Order.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Order.lean)
- [Declaration ledger](../../../../../../sources/batteries/Batteries.Data.Float.Lemmas.Order.json)
