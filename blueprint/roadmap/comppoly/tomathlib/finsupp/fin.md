---
catalog: module
lean: Finsupp.init, Finsupp.removeNth, Finsupp.snoc, Finsupp.insertNth, Finsupp.removeNth_apply, Finsupp.removeNth_zero, Finsupp.removeNth_last, Finsupp.removeNth_update, Finsupp.init_apply, Finsupp.init_update_last, Finsupp.init_update_castSucc, Finsupp.tail_init_eq_init_tail, Finsupp.snoc_last, Finsupp.snoc_castSucc, Finsupp.insertNth_zero, Finsupp.insertNth_last, Finsupp.insertNth_apply_same, Finsupp.insertNth_apply_succAbove, Finsupp.init_snoc, Finsupp.snoc_init_self, Finsupp.insertNth_removeNth, Finsupp.insertNth_self_removeNth, Finsupp.snoc_zero_zero, Finsupp.insertNth_zero_zero, Finsupp.snoc_ne_zero_of_left, Finsupp.snoc_ne_zero_of_right, Finsupp.snoc_ne_zero_iff, Finsupp.insertNth_ne_zero_of_left, Finsupp.insertNth_ne_zero_of_right, Finsupp.insertNth_ne_zero_iff, Finsupp.snoc_support, Finsupp.snoc_left_injective, Finsupp.insertNth_support, Finsupp.insertNth_right_injective, Finsupp.sum_insertNth, Finsupp.sum_insertNth'
statement: formalized
proof: formalized
---

# Tuple operations on maps `Fin n →₀ M`

`CompPoly.ToMathlib.Finsupp.Fin`, in [CompPoly/ToMathlib/Finsupp/Fin.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean), by Ivan Sadofschi Costa, Quang Dao.

> We interpret maps `Fin n →₀ M` as `n`-tuples of elements of `M`, and define the following
> operations:
> * `Finsupp.tail` : the tail of a map `Fin (n + 1) →₀ M`, i.e., its last `n` entries;
> * `Finsupp.init` : the initial of a map `Fin n →₀ M`, i.e., its first `n - 1` entries;
> * `Finsupp.removeNth` : removing an element at a given entry of a map `Fin (n + 1) →₀ M`;
> * `Finsupp.cons` : adding an element at the beginning of an `n`-tuple, to get an `n + 1`-tuple;
> * `Finsupp.snoc` : adding an element at the end of an `n`-tuple, to get an `n + 1`-tuple;
> * `Finsupp.insertNth` : adding an element at a given entry of an `n`-tuple, to get an `n + 1`-tuple.
>
> In this context, we prove some usual properties of these operations, analogous to those of
> `Data.Fin.Tuple.Basic`.

`Finsupp.init` (definition, [line 42](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L42))

> `init` for maps `Fin n →₀ M`. See `Fin.init` for more details.

```lean
def init (s : Fin (n + 1) →₀ M) : Fin n →₀ M
```

`Finsupp.removeNth` (definition, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L46))

> `removeNth` for maps `Fin n →₀ M`. See `Fin.removeNth` for more details.

```lean
def removeNth (p : Fin (n + 1)) (s : Fin (n + 1) →₀ M) : Fin n →₀ M
```

`Finsupp.snoc` (definition, [line 54](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L54))

> `snoc` for maps `Fin n →₀ M`. See `Fin.snoc` for more details.

```lean
def snoc (s : Fin n →₀ M) (y : M) : Fin (n + 1) →₀ M
```

`Finsupp.insertNth` (definition, [line 58](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L58))

> `insertNth` for maps `Fin n →₀ M`. See `Fin.insertNth` for more details.

```lean
def insertNth (p : Fin (n + 1)) (y : M) (s : Fin n →₀ M) : Fin (n + 1) →₀ M
```

`Finsupp.removeNth_apply` (theorem, [line 66](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L66))

```lean
theorem removeNth_apply : removeNth p s i = s (p.succAbove i)
```

`Finsupp.removeNth_zero` (theorem, [line 69](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L69))

```lean
theorem removeNth_zero : removeNth 0 s = tail s
```

`Finsupp.removeNth_last` (theorem, [line 72](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L72))

```lean
theorem removeNth_last : removeNth (Fin.last n) s = init s
```

`Finsupp.removeNth_update` (theorem, [line 76](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L76))

> Updating the `i`-th entry does not affect removing the `i`-th entry.

```lean
theorem removeNth_update : removeNth p (update s p y) = removeNth p s
```

`Finsupp.init_apply` (theorem, [line 88](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L88))

```lean
theorem init_apply : init s i = s i.castSucc
```

`Finsupp.init_update_last` (theorem, [line 91](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L91))

```lean
theorem init_update_last : init (update s (Fin.last n) y) = init s
```

`Finsupp.init_update_castSucc` (theorem, [line 94](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L94))

```lean
theorem init_update_castSucc : init (update s i.castSucc y) = update (init s) i y
```

`Finsupp.tail_init_eq_init_tail` (theorem, [line 97](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L97))

```lean
theorem tail_init_eq_init_tail (s : Fin (n + 2) →₀ M) : tail (init s) = init (tail s)
```

`Finsupp.snoc_last` (theorem, [line 113](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L113))

```lean
theorem snoc_last : snoc s y (Fin.last n) = y
```

`Finsupp.snoc_castSucc` (theorem, [line 116](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L116))

```lean
theorem snoc_castSucc : snoc s y i.castSucc = s i
```

`Finsupp.insertNth_zero` (theorem, [line 119](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L119))

```lean
theorem insertNth_zero : insertNth 0 y s = cons y s
```

`Finsupp.insertNth_last` (theorem, [line 122](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L122))

```lean
theorem insertNth_last : insertNth (Fin.last n) y s = snoc s y
```

`Finsupp.insertNth_apply_same` (theorem, [line 125](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L125))

```lean
theorem insertNth_apply_same : insertNth p y s p = y
```

`Finsupp.insertNth_apply_succAbove` (theorem, [line 128](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L128))

```lean
theorem insertNth_apply_succAbove : insertNth p y s (p.succAbove i) = s i
```

`Finsupp.init_snoc` (theorem, [line 142](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L142))

```lean
theorem init_snoc : init (snoc s y) = s
```

`Finsupp.snoc_init_self` (theorem, [line 146](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L146))

```lean
theorem snoc_init_self : snoc (init t) (t (Fin.last n)) = t
```

`Finsupp.insertNth_removeNth` (theorem, [line 151](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L151))

```lean
theorem insertNth_removeNth : insertNth p y (removeNth p t) = update t p y
```

`Finsupp.insertNth_self_removeNth` (theorem, [line 156](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L156))

```lean
theorem insertNth_self_removeNth : insertNth p (t p) (removeNth p t) = t
```

`Finsupp.snoc_zero_zero` (theorem, [line 168](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L168))

```lean
theorem snoc_zero_zero : snoc (0 : Fin n →₀ M) 0 = 0
```

`Finsupp.insertNth_zero_zero` (theorem, [line 174](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L174))

```lean
theorem insertNth_zero_zero : insertNth p 0 (0 : Fin n →₀ M) = 0
```

`Finsupp.snoc_ne_zero_of_left` (theorem, [line 195](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L195))

```lean
theorem snoc_ne_zero_of_left (h : s ≠ 0) : snoc s y ≠ 0
```

`Finsupp.snoc_ne_zero_of_right` (theorem, [line 200](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L200))

```lean
theorem snoc_ne_zero_of_right (h : y ≠ 0) : snoc s y ≠ 0
```

`Finsupp.snoc_ne_zero_iff` (theorem, [line 204](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L204))

```lean
theorem snoc_ne_zero_iff : snoc s y ≠ 0 ↔ s ≠ 0 ∨ y ≠ 0
```

`Finsupp.insertNth_ne_zero_of_left` (theorem, [line 209](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L209))

```lean
theorem insertNth_ne_zero_of_left (h : y ≠ 0) : insertNth p y s ≠ 0
```

`Finsupp.insertNth_ne_zero_of_right` (theorem, [line 213](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L213))

```lean
theorem insertNth_ne_zero_of_right (h : s ≠ 0) : insertNth p y s ≠ 0
```

`Finsupp.insertNth_ne_zero_iff` (theorem, [line 218](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L218))

```lean
theorem insertNth_ne_zero_iff : insertNth p y s ≠ 0 ↔ y ≠ 0 ∨ s ≠ 0
```

`Finsupp.snoc_support` (theorem, [line 234](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L234))

```lean
theorem snoc_support :
    (s.snoc y).support ⊆ insert (Fin.last n) (s.support.map Fin.castSuccEmb)
```

`Finsupp.snoc_left_injective` (theorem, [line 242](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L242))

```lean
theorem snoc_left_injective : Injective (Finsupp.snoc · y : (Fin n →₀ M) → Fin (n + 1) →₀ M)
```

`Finsupp.insertNth_support` (theorem, [line 246](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L246))

```lean
theorem insertNth_support :
    (insertNth p y s).support ⊆ insert p (s.support.map (Fin.succAboveEmb p))
```

`Finsupp.insertNth_right_injective` (theorem, [line 254](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L254))

```lean
theorem insertNth_right_injective :
    Injective (Finsupp.insertNth p y : (Fin n →₀ M) → Fin (n + 1) →₀ M)
```

`Finsupp.sum_insertNth` (lemma, [line 265](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L265))

```lean
lemma sum_insertNth [AddCommMonoid M] {n : ℕ} (σ : Fin n →₀ M) (i : M) (p : Fin (n + 1)) :
    (insertNth p i σ).sum (fun _ e ↦ e) = i + σ.sum (fun _ e ↦ e)
```

`Finsupp.sum_insertNth'` (lemma, [line 270](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean#L270))

```lean
lemma sum_insertNth' [AddCommMonoid M] [AddCommMonoid N] {n : ℕ} (σ : Fin n →₀ M) (i : M)
    (p : Fin (n + 1)) (f : Fin (n+1) → M → N) (h : ∀ x, f x 0 = 0) :
    sum (insertNth p i σ) f = f p i + sum σ (Fin.removeNth p f)
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/ToMathlib/Finsupp/Fin.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/Finsupp/Fin.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.ToMathlib.Finsupp.Fin.json)
