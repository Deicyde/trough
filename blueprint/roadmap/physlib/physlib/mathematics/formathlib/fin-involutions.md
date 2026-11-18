---
declaration: module
origin: cited
lean: Physlib.Fin.involutionCons, Physlib.Fin.involutionCons_ext, Physlib.Fin.involutionAddEquiv, Physlib.Fin.involutionAddEquiv_none_image_zero, Physlib.Fin.involutionAddEquiv_cast, Physlib.Fin.involutionAddEquiv_cast', Physlib.Fin.involutionAddEquiv_none_succ, Physlib.Fin.involutionNoFixedEquivSum
statement: formalized
proof: formalized
---

# Fin involutions

The module `Physlib.Mathematics.ForMathlib.Fin.Involutions`, [Physlib/Mathematics/ForMathlib/Fin/Involutions.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin/Involutions.lean): 22 declarations (1 instance with no name), 12 with a docstring.

> Some properties of involutions of `Fin n`.
>
> These involutions are used in e.g. proving results about Wick contractions.

**`Physlib.Fin.involutionCons`**, a def, [line 29](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin/Involutions.lean#L29).

> There is an equivalence between involutions of `Fin n.succ` and involutions of
> `Fin n` and an optional valid choice of an element in `Fin n` (which is where `0`
>   in `Fin n.succ` will be sent).

```lean
def involutionCons (n : ℕ) : {f : Fin n.succ → Fin n.succ // Function.Involutive f } ≃
    (f : {f : Fin n → Fin n // Function.Involutive f}) × {i : Option (Fin n) //
      ∀ (h : i.isSome), f.1 (Option.get i h) = (Option.get i h)}
```

**`Physlib.Fin.involutionCons_ext`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin/Involutions.lean#L146).

```lean
lemma involutionCons_ext {n : ℕ} {f1 f2 : (f : {f : Fin n → Fin n // Function.Involutive f}) ×
    {i : Option (Fin n) // ∀ (h : i.isSome), f.1 (Option.get i h) = (Option.get i h)}}
    (h1 : f1.1 = f2.1) (h2 : f1.2 = Equiv.subtypeEquivRight (by rw [h1]; simp) f2.2) : f1 = f2
```

**`Physlib.Fin.involutionAddEquiv`**, a def, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin/Involutions.lean#L164).

> Given an involution of `Fin n`, the optional choice of an element in `Fin n` which
> maps to itself is equivalent to the optional choice of an element in
> `Fin (Finset.univ.filter fun i => f.1 i = i).card`.

```lean
def involutionAddEquiv {n : ℕ} (f : {f : Fin n → Fin n // Function.Involutive f}) :
    {i : Option (Fin n) // ∀ (h : i.isSome), f.1 (Option.get i h) = (Option.get i h)} ≃
    Option (Fin (Finset.univ.filter fun i => f.1 i = i).card)
```

**`Physlib.Fin.involutionAddEquiv_none_image_zero`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin/Involutions.lean#L188).

```lean
lemma involutionAddEquiv_none_image_zero {n : ℕ} :
    {f : {f : Fin n.succ → Fin n.succ // Function.Involutive f}}
    → involutionAddEquiv (involutionCons n f).1 (involutionCons n f).2 = none
    → f.1 ⟨0, Nat.zero_lt_succ n⟩ = ⟨0, Nat.zero_lt_succ n⟩
```

**`Physlib.Fin.involutionAddEquiv_cast`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin/Involutions.lean#L199).

```lean
lemma involutionAddEquiv_cast {n : ℕ} {f1 f2 : {f : Fin n → Fin n // Function.Involutive f}}
    (hf : f1 = f2) :
    involutionAddEquiv f1 = (Equiv.subtypeEquivRight (by rw [hf]; simp)).trans
      ((involutionAddEquiv f2).trans (Equiv.optionCongr (finCongr (by rw [hf]))))
```

**`Physlib.Fin.involutionAddEquiv_cast'`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin/Involutions.lean#L207).

```lean
lemma involutionAddEquiv_cast' {m : ℕ} {f1 f2 : {f : Fin m → Fin m // Function.Involutive f}}
    {N : ℕ} (hf : f1 = f2) (n : Option (Fin N))
    (hn1 : N = (Finset.filter (fun i => f1.1 i = i) Finset.univ).card)
    (hn2 : N = (Finset.filter (fun i => f2.1 i = i) Finset.univ).card) :
    HEq ((involutionAddEquiv f1).symm (Option.map (finCongr hn1) n))
    ((involutionAddEquiv f2).symm (Option.map (finCongr hn2) n))
```

**`Physlib.Fin.involutionAddEquiv_none_succ`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin/Involutions.lean#L216).

```lean
lemma involutionAddEquiv_none_succ {n : ℕ}
    {f : {f : Fin n.succ → Fin n.succ // Function.Involutive f}}
    (h : involutionAddEquiv (involutionCons n f).1 (involutionCons n f).2 = none)
    (x : Fin n) : f.1 x.succ = x.succ ↔ (involutionCons n f).1.1 x = x
```

## Equivalences of involutions with no fixed points.

> The main aim of these equivalences is to define `involutionNoFixedZeroEquivProd`.

**`Physlib.Fin.involutionNoFixedEquivSum`**, a def, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin/Involutions.lean#L236).

> Fixed point free involutions of `Fin n.succ` can be separated based on where they sent
> `0`.

```lean
def involutionNoFixedEquivSum {n : ℕ} :
    {f : Fin n.succ → Fin n.succ // Function.Involutive f
    ∧ ∀ i, f i ≠ i} ≃ Σ (k : Fin n), {f : Fin n.succ → Fin n.succ // Function.Involutive f
    ∧ (∀ i, f i ≠ i) ∧ f 0 = k.succ}
```

**`Physlib.Fin.involutionNoFixedZeroSetEquivEquiv`**, a def, [line 247](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin/Involutions.lean#L247).

> The condition on fixed point free involutions of `Fin n.succ` for a fixed value of `f 0`,
> can be modified by conjugation with an equivalence.

```lean
def involutionNoFixedZeroSetEquivEquiv {n : ℕ}
    (k : Fin n) (e : Fin n.succ ≃ Fin n.succ) :
    {f : Fin n.succ → Fin n.succ // Function.Involutive f ∧ (∀ i, f i ≠ i) ∧ f 0 = k.succ} ≃
    {f : Fin n.succ → Fin n.succ // Function.Involutive (e.symm ∘ f ∘ e) ∧
      (∀ i, (e.symm ∘ f ∘ e) i ≠ i) ∧ (e.symm ∘ f ∘ e) 0 = k.succ}
```

**`Physlib.Fin.involutionNoFixedZeroSetEquivSetEquiv`**, a def, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin/Involutions.lean#L265).

> The condition on fixed point free involutions of `Fin n.succ` for a fixed value of `f 0`
> given an equivalence `e`,
> can be modified so that only the condition on `f 0` is up-to the equivalence `e`.

```lean
def involutionNoFixedZeroSetEquivSetEquiv {n : ℕ} (k : Fin n)
    (e : Fin n.succ ≃ Fin n.succ) :
    {f : Fin n.succ → Fin n.succ // Function.Involutive (e.symm ∘ f ∘ e) ∧
    (∀ i, (e.symm ∘ f ∘ e) i ≠ i) ∧ (e.symm ∘ f ∘ e) 0 = k.succ} ≃
    {f : Fin n.succ → Fin n.succ // Function.Involutive f ∧
      (∀ i, f i ≠ i) ∧ (e.symm ∘ f ∘ e) 0 = k.succ}
```

**`Physlib.Fin.involutionNoFixedZeroSetEquivEquiv'`**, a def, [line 290](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin/Involutions.lean#L290).

> Fixed point free involutions of `Fin n.succ` fixing `(e.symm ∘ f ∘ e) = k.succ` for a given `e`
> are equivalent to fixing `f (e 0) = e k.succ`.

```lean
def involutionNoFixedZeroSetEquivEquiv' {n : ℕ} (k : Fin n) (e : Fin n.succ ≃ Fin n.succ) :
    {f : Fin n.succ → Fin n.succ // Function.Involutive f ∧
    (∀ i, f i ≠ i) ∧ (e.symm ∘ f ∘ e) 0 = k.succ} ≃
    {f : Fin n.succ → Fin n.succ // Function.Involutive f ∧
    (∀ i, f i ≠ i) ∧ f (e 0) = e k.succ}
```

**`Physlib.Fin.involutionNoFixedZeroSetEquivSetOne`**, a def, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin/Involutions.lean#L302).

> Fixed point involutions of `Fin n.succ.succ` with `f 0 = k.succ` are equivalent
> to fixed point involutions with `f 0 = 1`.

```lean
def involutionNoFixedZeroSetEquivSetOne {n : ℕ} (k : Fin n.succ) :
    {f : Fin n.succ.succ → Fin n.succ.succ // Function.Involutive f ∧
      (∀ i, f i ≠ i) ∧ f 0 = k.succ}
      ≃ {f : Fin n.succ.succ → Fin n.succ.succ // Function.Involutive f ∧
      (∀ i, f i ≠ i) ∧ f 0 = 1}
```

**`Physlib.Fin.involutionNoFixedSetOne`**, a def, [line 319](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin/Involutions.lean#L319).

> Fixed point involutions of `Fin n.succ.succ` fixing `f 0 = 1` are equivalent to
> fixed point involutions of `Fin n`.

```lean
def involutionNoFixedSetOne {n : ℕ} :
    {f : Fin n.succ.succ → Fin n.succ.succ // Function.Involutive f ∧
    (∀ i, f i ≠ i) ∧ f 0 = 1} ≃ {f : Fin n → Fin n // Function.Involutive f ∧
    (∀ i, f i ≠ i)}
```

**`Physlib.Fin.involutionNoFixedZeroSetEquiv`**, a def, [line 411](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin/Involutions.lean#L411).

> Fixed point involutions of `Fin n.succ.succ` for fixed `f 0 = k.succ` are
> equivalent to fixed point involutions of `Fin n`.

```lean
def involutionNoFixedZeroSetEquiv {n : ℕ} (k : Fin n.succ) :
    {f : Fin n.succ.succ → Fin n.succ.succ // Function.Involutive f ∧
      (∀ i, f i ≠ i) ∧ f 0 = k.succ}
        ≃ {f : Fin n → Fin n // Function.Involutive f ∧ (∀ i, f i ≠ i)}
```

**`Physlib.Fin.involutionNoFixedEquivSumSame`**, a def, [line 419](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin/Involutions.lean#L419).

> The type of fixed point free involutions of `Fin n.succ.succ` is equivalent to the sum
> of `Fin n.succ` copies of fixed point involutions of `Fin n`.

```lean
def involutionNoFixedEquivSumSame {n : ℕ} :
    {f : Fin n.succ.succ → Fin n.succ.succ // Function.Involutive f ∧ (∀ i, f i ≠ i)}
    ≃ Σ (_ : Fin n.succ), {f : Fin n → Fin n // Function.Involutive f ∧ (∀ i, f i ≠ i)}
```

**`Physlib.Fin.involutionNoFixedZeroEquivProd`**, a def, [line 427](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin/Involutions.lean#L427).

> Ever fixed-point free involutions of `Fin n.succ.succ` can be decomposed into a
> element of `Fin n.succ` (where `0` is sent) and a fixed-point free involution of
> `Fin n`.

```lean
def involutionNoFixedZeroEquivProd {n : ℕ} :
    {f : Fin n.succ.succ → Fin n.succ.succ // Function.Involutive f ∧ (∀ i, f i ≠ i)}
    ≃ Fin n.succ × {f : Fin n → Fin n // Function.Involutive f ∧ (∀ i, f i ≠ i)}
```

## Cardinality

**An instance with no name**, [line 439](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin/Involutions.lean#L439).

> The type of fixed-point free involutions of `Fin n` is finite.

```lean
instance {n : ℕ} : Fintype { f // Function.Involutive f ∧ ∀ (i : Fin n), f i ≠ i }
```

**`Physlib.Fin.involutionNoFixed_card_succ`**, a lemma, [line 444](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin/Involutions.lean#L444).

```lean
lemma involutionNoFixed_card_succ {n : ℕ} :
    Fintype.card
    {f : Fin n.succ.succ → Fin n.succ.succ // Function.Involutive f ∧ (∀ i, f i ≠ i)}
    = n.succ *
    Fintype.card {f : Fin n → Fin n // Function.Involutive f ∧ (∀ i, f i ≠ i)}
```

**`Physlib.Fin.involutionNoFixed_card_mul_two`**, a lemma, [line 451](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin/Involutions.lean#L451).

```lean
lemma involutionNoFixed_card_mul_two : (n : ℕ) →
    Fintype.card {f : Fin (2 * n) → Fin (2 * n) // Function.Involutive f ∧ (∀ i, f i ≠ i)}
    = (2 * n - 1)‼
```

**`Physlib.Fin.involutionNoFixed_card_mul_two_plus_one`**, a lemma, [line 459](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin/Involutions.lean#L459).

```lean
lemma involutionNoFixed_card_mul_two_plus_one : (n : ℕ) →
    Fintype.card {f : Fin (2 * n + 1) → Fin (2 * n + 1) // Function.Involutive f ∧ (∀ i, f i ≠ i)}
    = 0
```

**`Physlib.Fin.involutionNoFixed_card_even`**, a lemma, [line 467](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin/Involutions.lean#L467).

```lean
lemma involutionNoFixed_card_even : (n : ℕ) → (he : Even n) →
    Fintype.card {f : Fin n → Fin n // Function.Involutive f ∧ (∀ i, f i ≠ i)} = (n - 1)‼
```

**`Physlib.Fin.involutionNoFixed_card_odd`**, a lemma, [line 475](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin/Involutions.lean#L475).

```lean
lemma involutionNoFixed_card_odd : (n : ℕ) → (ho : Odd n) →
    Fintype.card {f : Fin n → Fin n // Function.Involutive f ∧ (∀ i, f i ≠ i)} = 0
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/ForMathlib/Fin/Involutions.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Fin/Involutions.lean)
