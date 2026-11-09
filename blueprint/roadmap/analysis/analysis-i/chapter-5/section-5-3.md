---
declaration: theorem
origin: cited
lean: Chapter5.Sequence.equiv_trans, Chapter5.CauchySequence.instSetoid, Chapter5.Real.eq_lim, Chapter5.Real.LIM_eq_LIM, Chapter5.Sequence.IsCauchy.add, Chapter5.Sequence.add_equiv_left, Chapter5.Sequence.add_equiv_right, Chapter5.Sequence.add_equiv, Chapter5.Real.add_inst, Chapter5.Real.LIM_add, Chapter5.Sequence.IsCauchy.mul, Chapter5.Sequence.mul_equiv_left, Chapter5.Sequence.mul_equiv_right, Chapter5.Sequence.mul_equiv, Chapter5.Real.mul_inst, Chapter5.Real.ratCast_inj, Chapter5.Real.addGroup_inst, Chapter5.Real.instAddCommGroup, Chapter5.Real.instCommMonoid, Chapter5.Real.instCommRing, Chapter5.BoundedAwayZero, Chapter5.Real.boundedAwayZero_of_nonzero, Chapter5.Real.inv_isCauchy_of_boundedAwayZero, Chapter5.Real.inv_of_equiv, Chapter5.Real.instInv, Chapter5.Real.IsBounded.equiv, Chapter5.Real.LIM.harmonic
statement: formalized
---

# Section 5.3: The construction of the real numbers

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter. In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
>
> - Notion of a formal limit of a Cauchy sequence.
> - Construction of a real number type `Chapter5.Real`.
> - Basic arithmetic operations and properties.
>
> ## Tips from past users
>
> Users of the companion who have completed the exercises in this section are welcome to send their tips for future users in this section as PRs.
>
> - (Add tip here)

*Quoted from [Analysis/Section_5_3.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 18 labelled items, carried by 32 declarations: 13 proved here, 10 stated without proof (5 of them exercises) and 9 definitions (5 with a value left as `sorry`). It also has 46 declarations with no label, counted here but not shown.

## Proposition 5.3.3 / Exercise 5.3.1

`Chapter5.Sequence.equiv_trans` (theorem, [line 67](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean#L67)). An exercise, stated without proof.

> Proposition 5.3.3 / Exercise 5.3.1

```lean
theorem Sequence.equiv_trans {a b c:ℕ → ℚ} (hab: Equiv a b) (hbc: Equiv b c) :
  Equiv a c
```

`Chapter5.CauchySequence.instSetoid` (instance, [line 71](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean#L71)). A definition whose value is left as `sorry`.

> Proposition 5.3.3 / Exercise 5.3.1

```lean
instance CauchySequence.instSetoid : Setoid CauchySequence
```

## Definition 5.3.1

`Chapter5.Real.eq_lim` (theorem, [line 103](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean#L103)). Proved here.

> Definition 5.3.1 (Real numbers)

```lean
theorem Real.eq_lim (x:Real) : ∃ (a:ℕ → ℚ), (a:Sequence).IsCauchy ∧ x = LIM a
```

`Chapter5.Real.LIM_eq_LIM` (theorem, [line 111](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean#L111)). Proved here.

> Definition 5.3.1 (Real numbers)

```lean
theorem Real.LIM_eq_LIM {a b:ℕ → ℚ} (ha: (a:Sequence).IsCauchy) (hb: (b:Sequence).IsCauchy) :
  LIM a = LIM b ↔ Sequence.Equiv a b
```

## Lemma 5.3.6

`Chapter5.Sequence.IsCauchy.add` (theorem, [line 120](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean#L120)). Proved here.

> Lemma 5.3.6 (Sum of Cauchy sequences is Cauchy).

```lean
theorem Sequence.IsCauchy.add {a b:ℕ → ℚ}  (ha: (a:Sequence).IsCauchy) (hb: (b:Sequence).IsCauchy) :
    (a + b:Sequence).IsCauchy
```

## Lemma 5.3.7

`Chapter5.Sequence.add_equiv_left` (theorem, [line 136](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean#L136)). Proved here.

> Lemma 5.3.7 (Sum of equivalent sequences is equivalent, left).

```lean
theorem Sequence.add_equiv_left {a a':ℕ → ℚ} (b:ℕ → ℚ) (haa': Equiv a a') :
    Equiv (a + b) (a' + b)
```

`Chapter5.Sequence.add_equiv_right` (theorem, [line 150](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean#L150)). Proved here.

> Lemma 5.3.7 (Sum of equivalent sequences is equivalent, right).

```lean
theorem Sequence.add_equiv_right {b b':ℕ → ℚ} (a:ℕ → ℚ) (hbb': Equiv b b') :
    Equiv (a + b) (a + b')
```

`Chapter5.Sequence.add_equiv` (theorem, [line 154](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean#L154)). Proved here.

> Lemma 5.3.7 (Sum of equivalent sequences is equivalent).

```lean
theorem Sequence.add_equiv {a b a' b':ℕ → ℚ} (haa': Equiv a a')
  (hbb': Equiv b b') :
    Equiv (a + b) (a' + b')
```

## Definition 5.3.4

`Chapter5.Real.add_inst` (instance, [line 160](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean#L160)). A definition.

> Definition 5.3.4 (Addition of reals)

```lean
noncomputable instance Real.add_inst : Add Real
```

`Chapter5.Real.LIM_add` (theorem, [line 171](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean#L171)). Proved here.

> Definition 5.3.4 (Addition of reals)

```lean
theorem Real.LIM_add {a b:ℕ → ℚ} (ha: (a:Sequence).IsCauchy) (hb: (b:Sequence).IsCauchy) :
  LIM a + LIM b = LIM (a + b)
```

## Proposition 5.3.10

`Chapter5.Sequence.IsCauchy.mul` (theorem, [line 179](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean#L179)). Stated without proof.

> Proposition 5.3.10 (Product of Cauchy sequences is Cauchy)

```lean
theorem Sequence.IsCauchy.mul {a b:ℕ → ℚ}  (ha: (a:Sequence).IsCauchy) (hb: (b:Sequence).IsCauchy) :
    (a * b:Sequence).IsCauchy
```

## Proposition 5.3.10 / Exercise 5.3.2

`Chapter5.Sequence.mul_equiv_left` (theorem, [line 184](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean#L184)). An exercise, stated without proof.

> Proposition 5.3.10 (Product of equivalent sequences is equivalent, left) / Exercise 5.3.2.

```lean
theorem Sequence.mul_equiv_left {a a':ℕ → ℚ} (b:ℕ → ℚ) (hb : (b:Sequence).IsCauchy) (haa': Equiv a a') :
  Equiv (a * b) (a' * b)
```

`Chapter5.Sequence.mul_equiv_right` (theorem, [line 189](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean#L189)). Proved here.

> Proposition 5.3.10 (Product of equivalent sequences is equivalent, right) / Exercise 5.3.2.

```lean
theorem Sequence.mul_equiv_right {b b':ℕ → ℚ} (a:ℕ → ℚ)  (ha : (a:Sequence).IsCauchy)  (hbb': Equiv b b') :
  Equiv (a * b) (a * b')
```

`Chapter5.Sequence.mul_equiv` (theorem, [line 193](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean#L193)). Proved here.

> Proposition 5.3.10 (Product of equivalent sequences is equivalent) / Exercise 5.3.2.

```lean
theorem Sequence.mul_equiv
  {a b a' b':ℕ → ℚ}
  (ha : (a:Sequence).IsCauchy)
  (hb' : (b':Sequence).IsCauchy)
  (haa': Equiv a a')
  (hbb': Equiv b b') : Equiv (a * b) (a' * b')
```

## Definition 5.3.9

`Chapter5.Real.mul_inst` (instance, [line 202](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean#L202)). A definition.

> Definition 5.3.9 (Product of reals)

```lean
noncomputable instance Real.mul_inst : Mul Real
```

## Exercise 5.3.3

`Chapter5.Real.ratCast_inj` (theorem, [line 226](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean#L226)). An exercise, stated without proof.

> Exercise 5.3.3

```lean
theorem Real.ratCast_inj (q r:ℚ) : (q:Real) = (r:Real) ↔ q = r
```

## Proposition 5.3.11

`Chapter5.Real.addGroup_inst` (instance, [line 260](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean#L260)). A definition whose value is left as `sorry`.

> Proposition 5.3.11 (laws of algebra)

```lean
noncomputable instance Real.addGroup_inst : AddGroup Real
```

`Chapter5.Real.instAddCommGroup` (instance, [line 276](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean#L276)). A definition whose value is left as `sorry`.

> Proposition 5.3.11 (laws of algebra)

```lean
noncomputable instance Real.instAddCommGroup : AddCommGroup Real
```

`Chapter5.Real.instCommMonoid` (instance, [line 280](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean#L280)). A definition whose value is left as `sorry`.

> Proposition 5.3.11 (laws of algebra)

```lean
noncomputable instance Real.instCommMonoid : CommMonoid Real
```

`Chapter5.Real.instCommRing` (instance, [line 287](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean#L287)). A definition whose value is left as `sorry`.

> Proposition 5.3.11 (laws of algebra)

```lean
noncomputable instance Real.instCommRing : CommRing Real
```

## Definition 5.3.12

`Chapter5.BoundedAwayZero` (abbrev, [line 307](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean#L307)). A definition.

> Definition 5.3.12 (sequences bounded away from zero). Sequences are indexed to start from zero
> as this is more convenient for Mathlib purposes.

```lean
abbrev BoundedAwayZero (a:ℕ → ℚ) : Prop
```

## Examples 5.3.13

An `example` ([line 314](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean#L314)). Proved here.

> Examples 5.3.13

```lean
example : BoundedAwayZero (fun n ↦ (-1)^n)
```

An `example` ([line 317](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean#L317)). Stated without proof.

> Examples 5.3.13

```lean
example : ¬ BoundedAwayZero (fun n ↦ 10^(-(n:ℤ)-1))
```

An `example` ([line 320](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean#L320)). Stated without proof.

> Examples 5.3.13

```lean
example : ¬ BoundedAwayZero (fun n ↦ 1 - 10^(-(n:ℤ)))
```

An `example` ([line 323](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean#L323)). Proved here.

> Examples 5.3.13

```lean
example : BoundedAwayZero (fun n ↦ 10^(n+1))
```

An `example` ([line 330](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean#L330)). Stated without proof.

> Examples 5.3.13

```lean
example : ¬ ((fun (n:ℕ) ↦ (10:ℚ)^(n+1)):Sequence).IsBounded
```

## Lemma 5.3.14

`Chapter5.Real.boundedAwayZero_of_nonzero` (theorem, [line 333](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean#L333)). Stated without proof.

> Lemma 5.3.14

```lean
theorem Real.boundedAwayZero_of_nonzero {x:Real} (hx: x ≠ 0) :
    ∃ a:ℕ → ℚ, (a:Sequence).IsCauchy ∧ BoundedAwayZero a ∧ x = LIM a
```

## Lemma 5.3.15

`Chapter5.Real.inv_isCauchy_of_boundedAwayZero` (theorem, [line 365](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean#L365)). Proved here.

> Lemma 5.3.15

```lean
theorem Real.inv_isCauchy_of_boundedAwayZero {a:ℕ → ℚ} (ha: BoundedAwayZero a)
  (ha_cauchy: (a:Sequence).IsCauchy) :
    ((a⁻¹:ℕ → ℚ):Sequence).IsCauchy
```

## Lemma 5.3.17

`Chapter5.Real.inv_of_equiv` (theorem, [line 384](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean#L384)). Proved here.

> Lemma 5.3.17 (Reciprocation is well-defined)

```lean
theorem Real.inv_of_equiv {a b:ℕ → ℚ} (ha: BoundedAwayZero a)
  (ha_cauchy: (a:Sequence).IsCauchy) (hb: BoundedAwayZero b)
  (hb_cauchy: (b:Sequence).IsCauchy) (hlim: LIM a = LIM b) :
    LIM a⁻¹ = LIM b⁻¹
```

## Definition 5.3.16

`Chapter5.Real.instInv` (instance, [line 407](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean#L407)). A definition.

> Definition 5.3.16 (Reciprocation of real numbers).  Requires classical logic because we need to
> assign a "junk" value to the inverse of 0.

```lean
noncomputable instance Real.instInv : Inv Real
```

## Exercise 5.3.4

`Chapter5.Real.IsBounded.equiv` (theorem, [line 454](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean#L454)). An exercise, stated without proof.

> Exercise 5.3.4

```lean
theorem Real.IsBounded.equiv {a b:ℕ → ℚ} (ha: (a:Sequence).IsBounded) (hab: Sequence.Equiv a b) :
    (b:Sequence).IsBounded
```

## Exercise 5.3.5

`Chapter5.Real.LIM.harmonic` (theorem, [line 467](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean#L467)). An exercise, stated without proof.

> Exercise 5.3.5

```lean
theorem Real.LIM.harmonic : LIM (fun n ↦ 1/((n:ℚ)+1)) = 0
```

## Depends on

- [Section 5.2: Equivalent Cauchy sequences](section-5-2.md)

## Sources

- [Analysis/Section_5_3.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_3.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_5_3/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_5_3.html)
