---
declaration: module
origin: cited
lean: Prob, Prob.canLift, Prob.coe_zero, Prob.coe_one, Prob.coe_mul, Prob.coe_inf, Prob.coe_sup, Prob.instInhabited
statement: formalized
proof: formalized
---

# Probabilities

The module `QuantumInfo.ClassicalInfo.Prob`, [QuantumInfo/ClassicalInfo/Prob.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean): 75 declarations (2 instances with no name), 15 with a docstring.

> This defines a type `Prob`, which is simply any real number in the interval O to 1.
> This then comes with additional statements such as its application to convex sets, and
> it makes useful type alias for functions that only make sense on probabilities.
>
> A significant application is in the `Mixable` typeclass, also in this file, which is a
> general notion of convex combination that applies to types as opposed to sets;
> elements are `Mixable.mix`ed using `Prob`s.

**`Prob`**, a def, [line 31](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L31).

> `Prob` is a real number in the interval [0,1]. Similar to NNReal in many definitions, but this
> allows other nice things more 'safely' such as convex combination.

```lean
def Prob : Type _
```

**An instance with no name**, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L35).

```lean
instance : Coe Prob ℝ
```

**`Prob.canLift`**, an instance, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L37).

```lean
instance canLift : CanLift ℝ Prob Subtype.val fun r => 0 ≤ r ∧ r ≤ 1
```

**`Prob.coe_zero`**, a lemma, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L41).

```lean
lemma coe_zero : (0 : Prob).val = 0
```

**`Prob.coe_one`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L45).

```lean
lemma coe_one : (1 : Prob).val = 1
```

**`Prob.coe_mul`**, a lemma, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L49).

```lean
lemma coe_mul (x y : Prob) : (x * y).val = x.val * y.val
```

**`Prob.coe_inf`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L53).

```lean
lemma coe_inf (x y : Prob) : (x ⊓ y).val = x.val ⊓ y.val
```

**`Prob.coe_sup`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L57).

```lean
lemma coe_sup (x y : Prob) : (x ⊔ y).val = x.val ⊔ y.val
```

**`Prob.instInhabited`**, an instance, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L60).

```lean
instance instInhabited : Inhabited Prob
```

**`Prob.instConditionallyCompleteLinearOrder`**, an instance, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L68).

> Override `ordConnectedSubsetConditionallyCompleteLinearOrder` (activated by `instInhabited`)
> so that `ConditionallyCompleteLinearOrder Prob` agrees definitionally with
> `CompleteLinearOrder Prob`.
>
> This seems fixed in Mathlib master.

```lean
instance (priority := high) instConditionallyCompleteLinearOrder :
    ConditionallyCompleteLinearOrder Prob
```

**`Prob.zero_le_coe`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L73).

```lean
lemma zero_le_coe {p : Prob} : 0 ≤ (p : ℝ)
```

**`Prob.coe_le_one`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L77).

```lean
lemma coe_le_one {p : Prob} : (p : ℝ) ≤ 1
```

**`Prob.zero_le`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L81).

```lean
lemma zero_le {p : Prob} : 0 ≤ p
```

**`Prob.le_one`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L85).

```lean
lemma le_one {p : Prob} : p ≤ 1
```

**`Prob.mem_unitInterval_bounds`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L89).

```lean
lemma mem_unitInterval_bounds {x : ℝ} (h : x ∈ unitInterval) : 0 ≤ x ∧ x ≤ 1
```

**`Prob.mem_unitInterval_of_le`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L93).

```lean
lemma mem_unitInterval_of_le {x : ℝ} (h₀ : 0 ≤ x) (h₁ : x ≤ 1) : x ∈ unitInterval
```

**`Prob.ext`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L96).

```lean
protected lemma ext {n m : Prob} : (n : ℝ) = (m : ℝ) → n = m
```

**`Prob.ne_iff`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L99).

```lean
lemma ne_iff {x y : Prob} : (x : ℝ) ≠ (y : ℝ) ↔ x ≠ y
```

**`Prob.toReal_mul`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L103).

```lean
lemma toReal_mul (x y : Prob) : (x * y : Prob) = (x : ℝ) * (y : ℝ)
```

**`Prob.toNNReal`**, a def, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L107).

> Coercion `Prob → ℝ≥0`.

```lean
def toNNReal : Prob → ℝ≥0
```

**`Prob.toNNReal_mk`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L111).

```lean
lemma toNNReal_mk : toNNReal { val := x, property := hx} = { val := x, property := hx.1 }
```

**An instance with no name**, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L114).

```lean
instance : Coe Prob ℝ≥0
```

**`Prob.canLiftNN`**, an instance, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L116).

```lean
instance canLiftNN : CanLift ℝ≥0 Prob toNNReal fun r => r ≤ 1
```

**`Prob.eq_iff_nnreal`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L119).

```lean
protected lemma eq_iff_nnreal (n m : Prob) : (n : ℝ≥0) = (m : ℝ≥0) ↔ n = m
```

**`Prob.toNNReal_zero`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L125).

```lean
lemma toNNReal_zero : (0 : Prob) = (0 : ℝ≥0)
```

**`Prob.toNNReal_one`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L129).

```lean
lemma toNNReal_one : (1 : Prob) = (1 : ℝ≥0)
```

**`Prob.ofNNReal_toNNReal`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L132).

```lean
lemma ofNNReal_toNNReal : ENNReal.ofNNReal (toNNReal p) = ENNReal.ofReal (p : ℝ)
```

**`Prob.NNReal.asProb`**, a def, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L136).

```lean
def NNReal.asProb (p : ℝ≥0) (hp : p ≤ 1) : Prob
```

**`Prob.NNReal.asProb'`**, a def, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L139).

```lean
def NNReal.asProb' (p : ℝ≥0) (hp : p.1 ≤ 1) : Prob
```

**`Prob.zero_lt_coe`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L142).

```lean
lemma zero_lt_coe {p : Prob} (hp : p ≠ 0) : (0 : ℝ) < p
```

**`Prob.instSub`**, an instance, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L148).

> Subtract a probability from another. Truncates to zero, so this is often not great
> to work with, for the same reason that Nat subtraction is a pain. But, it lets you write
> `1 - p`, which is sufficiently useful on its own that this seems worth having.

```lean
instance instSub : Sub Prob
```

**`Prob.coe_sub`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L153).

```lean
lemma coe_sub (p q : Prob) : (p - q : Prob)  = (p.val - q.val) ⊔ (0 : ℝ)
```

**`Prob.coe_one_minus`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L157).

```lean
lemma coe_one_minus (p : Prob) : (1 - p : Prob) = 1 - (p : ℝ)
```

**`Prob.add_one_minus`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L160).

```lean
lemma add_one_minus (p : Prob) : p.val + (1 - p).val = 1
```

**`Prob.one_minus_inv`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L164).

```lean
lemma one_minus_inv (p : Prob) : 1 - (1 - p) = p
```

**`Prob.coe_iInf`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L170).

```lean
lemma coe_iInf {ι : Type*} [Nonempty ι] (f : ι → Prob) : ↑(⨅ t, f t) = (⨅ t, f t : ℝ)
```

**`Prob.top_eq_one`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L177).

```lean
lemma top_eq_one : (⊤ : Prob) = 1
```

**`Prob.sub_zero`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L181).

```lean
lemma sub_zero (p : Prob) : p - 0 = p
```

**`Prob.toNNReal_Continuous`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L185).

```lean
lemma toNNReal_Continuous : Continuous Prob.toNNReal
```

**`Prob.mul_eq_one_iff`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L190).

```lean
lemma mul_eq_one_iff (p q : Prob) : p * q = 1 ↔ p = 1 ∧ q = 1
```

**`Mixable`**, a class, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L217).

> A `Mixable T` typeclass instance gives a compact way of talking about the
> action of probabilities for forming linear combinations in convex spaces.
> The notation `p [ x₁ ↔ x₂ ]` means to take a convex
> combination, equal to `x₁` if `p=1` and to `x₂` if `p=0`.
>
> Mixable is defined by an "underlying" data type `U` with addition and scalar
> multiplication, and a bijection between the `T` and a convex set of `U`.
> For instance, in `Mixable (Distribution (Fin n))`, `U` is `n`-element vectors
> (which form the probability simplex, degenerate in one dimension). For
> `QuantumInfo.States.Mixed.MState` density matrices in quantum mechanics, which are
> PSD matrices of trace 1, `U` is the underlying matrix.
>
> Why not just stick with existing notions of `Convex`? `Convex` requires that
> the type already forms an `AddCommMonoid` and `Module ℝ`. But many types, such as `Distribution`,
> are not: there is no good notion of "multiplying a probability distribution by 0.3" to get another
> distribution. We can coerce the distribution nto, say, a vector or a function, but then we are not
> doing arithmetic with distributions. Accordingly, the expression `0.3 * distA + 0.7 * distB`
> cannot represent a distribution on its own.

```lean
class Mixable (U : outParam (Type u)) (T : Type v) [AddCommMonoid U] [Module ℝ U] where
  /-- Getter for the underlying data -/
  to_U : T → U
  /-- Proof that this getter is injective -/
  to_U_inj : ∀ {T₁ T₂}, to_U T₁ = to_U T₂ → T₁ = T₂
  /-- Proof that this image is convex -/
  convex : Convex ℝ (Set.range to_U)
  /-- Function to get a T from a proof that U is in the set. -/
  mkT : {u : U} → (∃ t, to_U t = u) → { t : T // to_U t = u }
```

**`Mixable.mix_ab`**, a def, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L232).

```lean
def mix_ab [inst : Mixable U T] {a b : ℝ} (ha : 0 ≤ a) (hb : 0 ≤ b) (hab : a + b = 1) (x₁ x₂ : T) : T
```

**`Mixable.mix`**, a def, [line 241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L241).

> `Mixable.mix` represents the notion of "convex combination" on the type `T`, afforded by the
> `Mixable` instance. It takes a `Prob`, that is, a `Real` between 0 and 1. For working directly
> with a Real, use `mix_ab`.

```lean
def mix [inst : Mixable U T] (p : Prob) (x₁ x₂ : T) : T
```

**`Mixable.to_U_of_mkT`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L245).

```lean
lemma to_U_of_mkT [inst : Mixable U T] (u : U) {h} : inst.to_U (mkT (u := u) h).1 = u
```

**`Mixable.mix_zero`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L254).

```lean
lemma mix_zero [inst : Mixable U T] (x₁ x₂ : T) : (0 : Prob) [ x₁ ↔ x₂ : inst] = x₂
```

**`Mixable.mix_one`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L260).

```lean
lemma mix_one [inst : Mixable U T] (x₁ x₂ : T) : (1 : Prob) [ x₁ ↔ x₂ : inst] = x₁
```

**`Mixable.instUniv`**, an instance, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L265).

> When T is the whole space, and T is a suitable vector space over ℝ, we get a Mixable instance.

```lean
instance instUniv [AddCommMonoid T] [Module ℝ T] : Mixable T T
```

**`Mixable.mkT_instUniv`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L274).

```lean
lemma mkT_instUniv [AddCommMonoid T] [Module ℝ T] {t : T} (h : ∃ t', to_U t' = t) :
    instUniv.mkT h = ⟨t, rfl⟩
```

**`Mixable.to_U_instUniv`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L279).

```lean
lemma to_U_instUniv [AddCommMonoid T] [Module ℝ T] {t : T} : instUniv.to_U t = t
```

**`Mixable.instPi.lem_1`**, a lemma, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L284).

```lean
lemma instPi.lem_1 {D : Type*} {T U : D → Type*} [∀i, AddCommMonoid (U i)] [∀ i, Module ℝ (U i)]
    [inst : ∀i, Mixable (U i) (T i)]
    {u : (i : D) → U i} (h : ∃ (t : (i : D) → T i), (fun d => to_U (t d)) = u) (d : D) :
    ∃ (t : T d), to_U t = u d
```

**`Mixable.instPi`**, an instance, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L296).

> Mixable instance on Pi types.

```lean
instance instPi : Mixable ((i:D) → U i) ((i:D) → T i)
```

**`Mixable.val_mkT_instPi`**, a lemma, [line 309](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L309).

```lean
lemma val_mkT_instPi (D : Type*) [inst : Mixable U T] {u : D → U} (h : ∃ t, to_U t = u) :
    (instPi.mkT h).val = fun d ↦ (inst.mkT (instPi.lem_1 h d)).val
```

**`Mixable.to_U_instPi`**, a lemma, [line 314](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L314).

```lean
lemma to_U_instPi (D : Type*) [inst : Mixable U T] {t : D → T} :
    (instPi).to_U t = fun d ↦ inst.to_U (t d)
```

**`Mixable.instSubtype`**, a def, [line 324](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L324).

> Mixable instances on subtypes (of other mixable types), assuming that they
> have the correct closure properties.

```lean
def instSubtype {T : Type*} {P : T → Prop} (inst : Mixable U T)
    (h : ∀{x y:T},
      ∀⦃a b : ℝ⦄, (ha : 0 ≤ a) → (hb : 0 ≤ b) → (hab : a + b = 1) →
      P x → P y → P (inst.mix_ab ha hb hab x y))
    : Mixable U { t // P t}
```

**`Prob.instMixable`**, an instance, [line 353](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L353).

> Probabilities `Prob` themselves are convex.

```lean
instance instMixable : Mixable ℝ Prob
```

**`Prob.to_U_mixable`**, a lemma, [line 365](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L365).

```lean
lemma to_U_mixable [AddCommMonoid T] [SMul ℝ T] (t : Prob) : instMixable.to_U t = t.val
```

**`Prob.mkT_mixable`**, a lemma, [line 369](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L369).

```lean
lemma mkT_mixable (u : ℝ) (h : ∃ t : Prob, Mixable.to_U t = u) : Mixable.mkT h =
    ⟨⟨u,Exists.casesOn h fun t ht ↦ ht ▸ t.2⟩, rfl⟩
```

**`Prob.mix`**, an abbrev, [line 375](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L375).

> `Prob.mix` is an alias of `Mixable.mix` so it can be accessed from a probability with
> dot notation, e.g. `p.mix x y`.

```lean
abbrev mix [AddCommMonoid U] [Module ℝ U] [inst : Mixable U T]
    (p : Prob) (x₁ x₂ : T)
```

**`Prob.negLog`**, a def, [line 384](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L384).

> Map a probability [0,1] to [0,+∞] with -log p. Special case that 0 maps to +∞ (not 0, as
> Real.log does). This makes it strictly antitone.

```lean
noncomputable def negLog : Prob → ENNReal
```

**`Prob.negLog_strictAnti`**, a lemma, [line 393](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L393).

> Smaller probabilities have strictly greater negative logarithms, including at zero.

```lean
lemma negLog_strictAnti : StrictAnti negLog
```

**`Prob.negLog_Antitone`**, a lemma, [line 402](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L402).

```lean
lemma negLog_Antitone : Antitone negLog
```

**`Prob.negLog_zero`**, a lemma, [line 406](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L406).

```lean
lemma negLog_zero : —log (0 : Prob) = ⊤
```

**`Prob.negLog_one`**, a lemma, [line 410](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L410).

```lean
lemma negLog_one : —log 1 = 0
```

**`Prob.negLog_eq_top_iff`**, a lemma, [line 415](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L415).

```lean
lemma negLog_eq_top_iff {p : Prob} : —log p = ⊤ ↔ p = 0
```

**`Prob.negLog_pos_ENNReal`**, a lemma, [line 418](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L418).

```lean
lemma negLog_pos_ENNReal {p : Prob} (hp : p ≠ 0) : —log p = .ofNNReal ⟨-Real.log p,
    Left.nonneg_neg_iff.mpr (Real.log_nonpos p.2.1 p.2.2)⟩
```

**`Prob.negLog_pos_Real`**, a lemma, [line 424](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L424).

```lean
lemma negLog_pos_Real {p : Prob} : (—log p).toReal = -Real.log p
```

**`Prob.le_negLog_of_le_exp`**, a lemma, [line 431](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L431).

```lean
lemma le_negLog_of_le_exp {p : Prob} {x : ℝ} (h : p ≤ Real.exp (-x)) : ENNReal.ofReal x ≤ —log p
```

**`Prob.negLog_ne_top`**, a lemma, [line 456](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L456).

```lean
lemma negLog_ne_top {p : Prob} (hp : 0 < p.val) : —log p ≠ ∞
```

**`Prob.negLog_eq_neg_ENNReal_log`**, a lemma, [line 462](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L462).

```lean
lemma negLog_eq_neg_ENNReal_log (p : Prob) : —log p = -ENNReal.log p
```

**`Prob.negLog_eq_ofReal_neg_log`**, a lemma, [line 473](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L473).

```lean
lemma negLog_eq_ofReal_neg_log {p : Prob} (hp : 0 < p) :
    ENNReal.ofReal (-Real.log p) = —log p
```

**`Prob.negLog_surjective`**, a lemma, [line 482](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L482).

> Every extended nonnegative value is the negative logarithm of a probability.

```lean
lemma negLog_surjective : Function.Surjective negLog
```

**`Prob.negLogOrderIso`**, a def, [line 494](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L494).

> The negative logarithm identifies probabilities with extended nonnegative values in reverse
> order, sending zero to infinity and one to zero.

```lean
def negLogOrderIso : Prob ≃o ENNRealᵒᵈ
```

**`Prob.negLogOrderIso_apply`**, a lemma, [line 499](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L499).

```lean
lemma negLogOrderIso_apply (p : Prob) : negLogOrderIso p = OrderDual.toDual (negLog p)
```

**`Prob.zero_lt_negLog`**, a lemma, [line 504](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L504).

```lean
lemma zero_lt_negLog {p : Prob} : 0 < —log p ↔ p ≠ 1
```

**`Prob.Continuous_negLog`**, a lemma, [line 522](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean#L522).

```lean
lemma Continuous_negLog : Continuous negLog
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [QuantumInfo/ClassicalInfo/Prob.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ClassicalInfo/Prob.lean)
