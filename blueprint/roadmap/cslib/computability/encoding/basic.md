---
catalog: module
lean: Cslib.Encoding.encDelimited, Cslib.Encoding.encBool, Cslib.Encoding.encBits, Nat.bits_injective, Nat.bits_inj, Nat.bits_eq_nil, Cslib.Encoding.encNat, Cslib.Encoding.encFin, Cslib.Encoding.encFin_apply, Cslib.Encoding.length_encFin, Cslib.Encoding.getElem_encFin, Cslib.Encoding.encFin_eq_nil, Cslib.Encoding.encFintype, Cslib.Encoding.encFintype_apply, Cslib.Encoding.length_encFintype, Cslib.Encoding.encFintype_eq_nil, Cslib.Encoding.encSubsingleton, Cslib.Encoding.encFintype_eq_encSubsingleton, Cslib.Encoding.encProd, Cslib.Encoding.encSigma, Cslib.Encoding.encProd_eq_encSigma, Cslib.Encoding.encSum, Cslib.Encoding.encOption, Cslib.Encoding.encList, Cslib.Encoding.encSum_inl, Cslib.Encoding.encSum_inr, Cslib.Encoding.encOption_none, Cslib.Encoding.encOption_some, Cslib.Encoding.encList_nil, Cslib.Encoding.encList_cons, Cslib.Encoding.encList_singleton, Cslib.Encoding.encList_append, Cslib.Encoding.length_encProd, Cslib.Encoding.length_encSigma, Cslib.Encoding.length_encSum, Cslib.Encoding.length_encOption, Cslib.Encoding.length_encOption_none, Cslib.Encoding.length_encOption_some, Cslib.Encoding.length_encList, Cslib.Encoding.length_le_length_encList
statement: formalized
proof: formalized
---

# Default encodings

`Cslib.Computability.Encoding.Basic`, in [Cslib/Computability/Encoding/Basic.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean), by Christian Reitwiessner.

> Provides default encodings and encoding combinators for basic Lean types such as natural numbers,
> finite types, products, dependent pairs, sums, options and lists into Boolean words.
>
> Since the complexity of a function depends on the exact encoding used, and thus the encoding
> is part of the definition of the function, we do not use a class but instead provide encodings
> merely as a convenience.
>
> The `delimit` function is used as the basic building block here: It creates a self-delimiting,
> prefix-free code by replacing each bit `b` of a word with `[true, b]` and appending `[false]`.
>
> The product encoding delimits the first component and appends the second, and lists are encoded by
> delimiting each element. Dependent pairs are encoded like products, with the second component
> encoded under the encoding selected by the first one. Sums prefix the code of the component with a
> tag bit, and options are encoded as the sum `Unit ⊕ α`. Booleans are their single bit, natural
> numbers use the little-endian binary code `Nat.bits`, and `Fin n` uses a fixed-width binary code of
> `Nat.clog 2 n` bits, which `encFintype` transfers to any finite type via `Fintype.equivFin`.
> Subsingletons, including propositions, are encoded as the empty word by `encSubsingleton`.
>
> Products delimit only their first component because the second one extends to the end of the code
> word, so a delimiter would add nothing for parsing; this keeps the second component undoubled and
> the size of right-nested products linear. Lists delimit every element since their number is not
> known in advance, and sums use a tag bit rather than a delimiter since it has a fixed length.
>
> In general, a code word followed by further data cannot be split again; for example,
> `encList enc [a]` is a prefix of `encList enc [a, b]`. Wrap an encoding with `encDelimited` (as
> `encList` does for its elements) when its end has to be recognizable, see `delimit_append_inj`.
>
> We do not use Mathlib's `Computability.Encoding` combinators since they change the alphabet
> (e.g. `encodingProd` encodes into `Γ₁ ⊕ Γ₂`), while here every encoding targets `List Bool`.

`Cslib.Encoding.encDelimited` (definition, [line 57](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L57))

> Wraps every code word of an encoding with `delimit`, so that it can be followed by further
> data.

```lean
def encDelimited (enc : α ↪ List Bool) : α ↪ List Bool
```

> ### Basic types

`Cslib.Encoding.encBool` (definition, [line 64](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L64))

> A Boolean is encoded by its single bit.

```lean
def encBool : Bool ↪ List Bool
```

`Cslib.Encoding.encBits` (definition, [line 69](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L69))

> Boolean words already are codes.

```lean
def encBits : List Bool ↪ List Bool
```

`Nat.bits_injective` (theorem, [line 72](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L72))

> `Nat.bits` is injective. Candidate for upstreaming to `Mathlib.Data.Nat.Bits`.

```lean
theorem _root_.Nat.bits_injective : Function.Injective Nat.bits
```

`Nat.bits_inj` (theorem, [line 78](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L78))

```lean
theorem _root_.Nat.bits_inj {m n : ℕ} : m.bits = n.bits ↔ m = n
```

`Nat.bits_eq_nil` (theorem, [line 81](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L81))

```lean
theorem _root_.Nat.bits_eq_nil {n : ℕ} : n.bits = [] ↔ n = 0
```

`Cslib.Encoding.encNat` (definition, [line 86](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L86))

> A natural number is encoded in binary, least significant bit first, as `Nat.bits`.

```lean
def encNat : ℕ ↪ List Bool
```

> ### Finite types

`Cslib.Encoding.encFin` (definition, [line 92](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L92))

> `Fin n` is encoded in binary as a fixed-width code of `Nat.clog 2 n` bits, least significant
> bit first.

```lean
def encFin (n : ℕ) : Fin n ↪ List Bool
```

`Cslib.Encoding.encFin_apply` (theorem, [line 99](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L99))

```lean
theorem encFin_apply (n : ℕ) (a : Fin n) :
    encFin n a = (List.range (Nat.clog 2 n)).map (a.val.testBit ·)
```

`Cslib.Encoding.length_encFin` (theorem, [line 103](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L103))

```lean
theorem length_encFin (n : ℕ) (a : Fin n) : (encFin n a).length = Nat.clog 2 n
```

`Cslib.Encoding.getElem_encFin` (theorem, [line 108](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L108))

> The `i`-th bit of the code is the `i`-th bit of the number.

```lean
theorem getElem_encFin (n : ℕ) (a : Fin n) (i : ℕ) (h : i < (encFin n a).length) :
    (encFin n a)[i] = a.val.testBit i
```

`Cslib.Encoding.encFin_eq_nil` (theorem, [line 114](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L114))

> Types with at most one element are encoded as the empty word.

```lean
theorem encFin_eq_nil {n : ℕ} (h : n ≤ 1) (a : Fin n) : encFin n a = []
```

`Cslib.Encoding.encFintype` (definition, [line 121](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L121))

> A finite type is encoded with the fixed width `Nat.clog 2 (Fintype.card α)` through
> `Fintype.equivFin`. The enumeration is not computable and depends on the `Fintype` instance, so
> this encoding serves existence results where only the code length matters. Concrete machines
> should instead compose an explicit embedding `α ↪ Fin n` with `encFin n`.

```lean
noncomputable def encFintype (α : Type*) [Fintype α] : α ↪ List Bool
```

`Cslib.Encoding.encFintype_apply` (theorem, [line 124](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L124))

```lean
theorem encFintype_apply [Fintype α] (a : α) :
    encFintype α a = encFin _ (Fintype.equivFin α a)
```

`Cslib.Encoding.length_encFintype` (theorem, [line 128](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L128))

```lean
theorem length_encFintype [Fintype α] (a : α) :
    (encFintype α a).length = Nat.clog 2 (Fintype.card α)
```

`Cslib.Encoding.encFintype_eq_nil` (theorem, [line 134](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L134))

> Subsingletons are encoded as the empty word via `encFintype`.

```lean
theorem encFintype_eq_nil [Fintype α] [Subsingleton α] (a : α) : encFintype α a = []
```

`Cslib.Encoding.encSubsingleton` (definition, [line 140](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L140))

> A type with at most one element, such as a proposition, is encoded as the empty word. Unlike
> `encFintype`, this is computable and needs no `Fintype` instance.

```lean
def encSubsingleton (α : Sort*) [Subsingleton α] : α ↪ List Bool
```

`Cslib.Encoding.encFintype_eq_encSubsingleton` (theorem, [line 144](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L144))

> On finite subsingletons, `encSubsingleton` agrees with `encFintype`.

```lean
theorem encFintype_eq_encSubsingleton [Fintype α] [Subsingleton α] :
    encFintype α = encSubsingleton α
```

> ### Combinators

`Cslib.Encoding.encProd` (definition, [line 154](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L154))

> A product is encoded as the delimited first component followed by the second component.
> Only the first component is delimited since the second one extends to the end of the code word;
> this keeps the second component undoubled and right-nested products linear in size.

```lean
def encProd (enc₁ : α ↪ List Bool) (enc₂ : β ↪ List Bool) : α × β ↪ List Bool
```

`Cslib.Encoding.encSigma` (definition, [line 161](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L161))

> A dependent pair is encoded as the delimited first component followed by the second component,
> encoded under the encoding selected by the first component. As for `encProd`, only the first
> component is delimited, which is exactly what is needed to know the encoding of the second one.

```lean
def encSigma {β : α → Type*} (enc₁ : α ↪ List Bool) (enc₂ : ∀ a, β a ↪ List Bool) :
    (a : α) × β a ↪ List Bool
```

`Cslib.Encoding.encProd_eq_encSigma` (theorem, [line 171](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L171))

> A product is a dependent pair with a constant second type.

```lean
theorem encProd_eq_encSigma (enc₁ : α ↪ List Bool) (enc₂ : β ↪ List Bool) (p : α × β) :
    encProd enc₁ enc₂ p = encSigma enc₁ (fun _ => enc₂) ⟨p.1, p.2⟩
```

`Cslib.Encoding.encSum` (definition, [line 177](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L177))

> A sum is encoded by a tag bit, `false` for `inl` and `true` for `inr`, followed by the code of
> the component. A tag bit is used instead of a delimiter since it has a fixed length and does not
> double the component.

```lean
def encSum (enc₁ : α ↪ List Bool) (enc₂ : β ↪ List Bool) : α ⊕ β ↪ List Bool
```

`Cslib.Encoding.encOption` (definition, [line 182](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L182))

> An option is encoded as the sum `Unit ⊕ α`: `none` is encoded as `[false]` and `some a` as
> `true` followed by the code of `a`.

```lean
def encOption (enc : α ↪ List Bool) : Option α ↪ List Bool
```

`Cslib.Encoding.encList` (definition, [line 187](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L187))

> A list is encoded as the concatenation of the delimited codes of its elements.

```lean
def encList (enc : α ↪ List Bool) : List α ↪ List Bool
```

`Cslib.Encoding.encSum_inl` (theorem, [line 197](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L197))

```lean
theorem encSum_inl (enc₁ : α ↪ List Bool) (enc₂ : β ↪ List Bool) (a : α) :
    encSum enc₁ enc₂ (.inl a) = false :: enc₁ a
```

`Cslib.Encoding.encSum_inr` (theorem, [line 200](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L200))

```lean
theorem encSum_inr (enc₁ : α ↪ List Bool) (enc₂ : β ↪ List Bool) (b : β) :
    encSum enc₁ enc₂ (.inr b) = true :: enc₂ b
```

`Cslib.Encoding.encOption_none` (theorem, [line 204](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L204))

```lean
theorem encOption_none (enc : α ↪ List Bool) : encOption enc none = [false]
```

`Cslib.Encoding.encOption_some` (theorem, [line 206](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L206))

```lean
theorem encOption_some (enc : α ↪ List Bool) (a : α) :
    encOption enc (some a) = true :: enc a
```

`Cslib.Encoding.encList_nil` (theorem, [line 209](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L209))

```lean
theorem encList_nil (enc : α ↪ List Bool) : encList enc [] = []
```

`Cslib.Encoding.encList_cons` (theorem, [line 211](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L211))

```lean
theorem encList_cons (enc : α ↪ List Bool) (a : α) (l : List α) :
    encList enc (a :: l) = delimit (enc a) ++ encList enc l
```

`Cslib.Encoding.encList_singleton` (theorem, [line 214](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L214))

```lean
theorem encList_singleton (enc : α ↪ List Bool) (a : α) :
    encList enc [a] = delimit (enc a)
```

`Cslib.Encoding.encList_append` (theorem, [line 218](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L218))

```lean
theorem encList_append (enc : α ↪ List Bool) (l l' : List α) :
    encList enc (l ++ l') = encList enc l ++ encList enc l'
```

> ### Lengths

`Cslib.Encoding.length_encProd` (theorem, [line 224](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L224))

```lean
theorem length_encProd (enc₁ : α ↪ List Bool) (enc₂ : β ↪ List Bool) (p : α × β) :
    (encProd enc₁ enc₂ p).length = 2 * (enc₁ p.1).length + 1 + (enc₂ p.2).length
```

`Cslib.Encoding.length_encSigma` (theorem, [line 228](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L228))

```lean
theorem length_encSigma {β : α → Type*} (enc₁ : α ↪ List Bool) (enc₂ : ∀ a, β a ↪ List Bool)
    (x : (a : α) × β a) :
    (encSigma enc₁ enc₂ x).length = 2 * (enc₁ x.1).length + 1 + (enc₂ x.1 x.2).length
```

`Cslib.Encoding.length_encSum` (theorem, [line 233](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L233))

```lean
theorem length_encSum (enc₁ : α ↪ List Bool) (enc₂ : β ↪ List Bool) (x : α ⊕ β) :
    (encSum enc₁ enc₂ x).length =
      x.elim (fun a => (enc₁ a).length + 1) (fun b => (enc₂ b).length + 1)
```

`Cslib.Encoding.length_encOption` (theorem, [line 238](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L238))

```lean
theorem length_encOption (enc : α ↪ List Bool) (o : Option α) :
    (encOption enc o).length = o.elim 1 (fun a => (enc a).length + 1)
```

`Cslib.Encoding.length_encOption_none` (theorem, [line 242](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L242))

```lean
theorem length_encOption_none (enc : α ↪ List Bool) : (encOption enc none).length = 1
```

`Cslib.Encoding.length_encOption_some` (theorem, [line 244](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L244))

```lean
theorem length_encOption_some (enc : α ↪ List Bool) (a : α) :
    (encOption enc (some a)).length = (enc a).length + 1
```

`Cslib.Encoding.length_encList` (theorem, [line 248](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L248))

> Each element contributes twice the length of its code plus one delimiter bit.

```lean
theorem length_encList (enc : α ↪ List Bool) (l : List α) :
    (encList enc l).length = 2 * (l.map fun a => (enc a).length).sum + l.length
```

`Cslib.Encoding.length_le_length_encList` (theorem, [line 253](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean#L253))

> Delimiters account for at least one bit per list element, even for empty element codes.

```lean
theorem length_le_length_encList (enc : α ↪ List Bool) (l : List α) :
    l.length ≤ (encList enc l).length
```

## Depends on

- [Delimited Boolean words](delimit.md)

## Sources

- [Cslib/Computability/Encoding/Basic.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Encoding/Basic.lean)
- [Declaration ledger](../../../../sources/cslib/Cslib.Computability.Encoding.Basic.json)
