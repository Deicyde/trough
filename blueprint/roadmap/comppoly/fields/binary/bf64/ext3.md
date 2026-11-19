---
catalog: module
lean: BF64.ext3Poly, BF64.ext3Poly_natDegree, BF64.ext3Poly_degree, BF64.ext3Poly_monic, BF64.ext3Poly_no_root, BF64.ext3Poly_irreducible, BF64.ext3Params, BF64.ext3Params_d, BF64.ext3Params_q, BF64.ext3Params_poly, BF64.Ext3, BF64.ext3Gen, BF64.ext3Gen_eq_gen, BF64.toQuot_ext3Gen, BF64.aeval_ext3Gen, BF64.ext3Gen_pow_three, BF64.nat_card_ext3, BF64.card_ext3
statement: formalized
proof: formalized
---

# The degree-3 extension of `GF(2^64)`

`CompPoly.Fields.Binary.BF64.Ext3`, in [CompPoly/Fields/Binary/BF64/Ext3.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Ext3.lean), by Nicolas Schleicher.

> ```text
> GF(2^64)[y] / (y^3 + y + 1),   giving GF(2^192)
> ```
>
> An element is `c0 + c1 * y + c2 * y^2` with each coefficient in `BF64`. The carrier comes
> from the computable extension framework in `CompPoly/Fields/Extension/`. Its coefficient
> vector is `Vector BF64 3`, with the three limbs ordered as `c0`, `c1`, and `c2`.
> `Ext.coeffs` and `Ext.ofVector` give inverse maps between elements and these coordinates.
>
> Irreducibility needs no certificate here, unlike the degree-64 base modulus: a cubic is
> irreducible exactly when it has no root, and a short characteristic-two argument rules one
> out. See `CompPoly/Fields/KoalaBear/Ext5.lean` for the general monic-modulus pattern this
> follows.
>
> ## Main definitions
>
> * `ext3Poly` — the modulus `y^3 + y + 1` over `BF64`.
> * `ext3Params` — its `CompPoly.Extension.ExtensionParams`.
> * `Ext3` — the extension field itself.
>
> ## Main statements
>
> * `ext3Poly_irreducible` — the cubic is irreducible over `BF64`.
> * `ext3Params_poly` — the coefficient vector `#v[1, 1, 0]` denotes that cubic.
> * `nat_card_ext3` — `Nat.card Ext3 = 2 ^ 192`.
>
> ## Implementation notes
>
> `ext3Params_poly` is load-bearing: it ties the coefficient vector `#v[1, 1, 0]` to
> `y ^ 3 + y + 1`. A wrong vector there would still compile and would silently give a
> different field, so it is checked against reference vectors in
> `tests/CompPolyTests/Fields/Binary/BF64.lean` rather than only re-derived.

> ## The defining cubic

`BF64.ext3Poly` (definition, [line 58](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Ext3.lean#L58))

> The extension modulus `y^3 + y + 1` over `GF(2^64)`.

```lean
noncomputable def ext3Poly : Polynomial BF64
```

`BF64.ext3Poly_natDegree` (theorem, [line 61](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Ext3.lean#L61))

> The cubic has degree `3`.

```lean
theorem ext3Poly_natDegree : ext3Poly.natDegree = 3
```

`BF64.ext3Poly_degree` (theorem, [line 65](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Ext3.lean#L65))

> `ext3Poly_natDegree` in `degree` form.

```lean
theorem ext3Poly_degree : ext3Poly.degree = (3 : ℕ)
```

`BF64.ext3Poly_monic` (theorem, [line 69](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Ext3.lean#L69))

> The cubic is monic, as the extension framework requires.

```lean
theorem ext3Poly_monic : ext3Poly.Monic
```

> ## Irreducibility
>
> A cubic is irreducible exactly when it has no root. A root `a` of `y^3 + y + 1` satisfies
> `a^3 = a + 1`, from which `a^7 = 1`. The multiplicative group of `GF(2^64)` has order
> `2^64 - 1`, which is coprime to `7`, so `a = 1` — and `1` is not a root.

`BF64.ext3Poly_no_root` (theorem, [line 101](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Ext3.lean#L101))

> The cubic has no root in `GF(2^64)`.
>
> A root has `a ^ 7 = 1`, so its multiplicative order divides `7`. It also divides
> `Fintype.card BF64 - 1 = 2 ^ 64 - 1`, which is coprime to `7`, so the order is `1` and
> `a = 1`. But `1` is not a root.

```lean
theorem ext3Poly_no_root (a : BF64) : ¬ext3Poly.IsRoot a
```

`BF64.ext3Poly_irreducible` (theorem, [line 127](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Ext3.lean#L127))

> The cubic `y^3 + y + 1` is irreducible over `GF(2^64)`.

```lean
theorem ext3Poly_irreducible : Irreducible ext3Poly
```

> ## The extension field

`BF64.ext3Params` (definition, [line 137](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Ext3.lean#L137))

> Parameters of `GF(2^64)[y] / (y^3 + y + 1)`: degree three, with lower coefficients
> `(1, 1, 0)` encoding `1 + y` below the leading `y^3`.

```lean
def ext3Params : ExtensionParams BF64
```

`BF64.ext3Params_d` (theorem, [line 147](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Ext3.lean#L147))

> The extension has degree three.

```lean
theorem ext3Params_d : ext3Params.d = 3
```

`BF64.ext3Params_q` (theorem, [line 149](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Ext3.lean#L149))

> The base field has `2 ^ 64` elements.

```lean
theorem ext3Params_q : ext3Params.q = 2 ^ 64
```

`BF64.ext3Params_poly` (theorem, [line 152](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Ext3.lean#L152))

> The parameters' defining polynomial is the cubic.

```lean
theorem ext3Params_poly : ext3Params.poly = ext3Poly
```

`BF64.Ext3` (abbreviation, [line 172](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Ext3.lean#L172))

> `GF(2^192)`, the degree-three extension `GF(2^64)[y] / (y^3 + y + 1)`.
>
> Its coefficient vector has three limbs representing `c0 + c1 * y + c2 * y^2` in that order.

```lean
abbrev Ext3 : Type
```

`BF64.ext3Gen` (definition, [line 179](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Ext3.lean#L179))

> The adjoined root `y` of `y^3 + y + 1`, as an element of `Ext3`.

```lean
def ext3Gen : Ext3
```

`BF64.ext3Gen_eq_gen` (theorem, [line 187](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Ext3.lean#L187))

> `ext3Gen` is the framework's `Ext.gen`.
>
> Deliberately **not** `@[simp]`: as a rewrite it fires before `ext3Gen_pow_three` can match,
> which would knock that lemma out of the simp set.

```lean
theorem ext3Gen_eq_gen : ext3Gen = Ext.gen
```

`BF64.toQuot_ext3Gen` (theorem, [line 190](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Ext3.lean#L190))

> `ext3Gen` maps to the adjoined root of the specification.

```lean
theorem toQuot_ext3Gen : Ext.toQuot ext3Gen = Ext.rt ext3Params
```

`BF64.aeval_ext3Gen` (theorem, [line 193](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Ext3.lean#L193))

> `ext3Gen` is a root of `y^3 + y + 1`, in the form `aeval` expects.

```lean
theorem aeval_ext3Gen : aeval ext3Gen ext3Params.poly = 0
```

`BF64.ext3Gen_pow_three` (theorem, [line 196](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Ext3.lean#L196))

> **The defining relation**: the adjoined root satisfies `y^3 = y + 1`.

```lean
theorem ext3Gen_pow_three : ext3Gen ^ 3 = ext3Gen + 1
```

`BF64.nat_card_ext3` (theorem, [line 203](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Ext3.lean#L203))

> `Ext3` has `2 ^ 192` elements, independently of an enumeration.

```lean
theorem nat_card_ext3 : Nat.card Ext3 = 2 ^ 192
```

`BF64.card_ext3` (theorem, [line 209](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Ext3.lean#L209))

> Any enumeration of `Ext3` has `2 ^ 192` elements.

```lean
theorem card_ext3 [Fintype Ext3] : Fintype.card Ext3 = 2 ^ 192
```

## Depends on

- [The computable `GF(2^64)` carrier](impl.md)
- [The field structure on an extension](../../extension/field.md)

## Sources

- [CompPoly/Fields/Binary/BF64/Ext3.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Ext3.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Fields.Binary.BF64.Ext3.json)
