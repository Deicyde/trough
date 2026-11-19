---
catalog: module
lean: CompPoly.Extension.ExtensionParams, CompPoly.Extension.ExtensionParams.lowerCoeff, CompPoly.Extension.ExtensionParams.lowerCoeffNat, CompPoly.Extension.ExtensionParams.lowerCoeffNat_coe, CompPoly.Extension.ExtensionParams.lowerCoeffNat_of_ge, CompPoly.Extension.ExtensionParams.d_pos, CompPoly.Extension.Ext, CompPoly.Extension.Ext.ofVector, CompPoly.Extension.Ext.coeffs_ofVector, CompPoly.Extension.Ext.ofVector_coeffs, CompPoly.Extension.Ext.coeffs_injective, CompPoly.Extension.Ext.ofFn, CompPoly.Extension.Ext.coeff, CompPoly.Extension.Ext.coeff_ofFn, CompPoly.Extension.Ext.ext, CompPoly.Extension.Ext.ofFn_coeff, CompPoly.Extension.Ext.equivFn, CompPoly.Extension.Ext.coeffNat, CompPoly.Extension.Ext.coeffNat_coe, CompPoly.Extension.Ext.coeffNat_of_lt, CompPoly.Extension.Ext.coeffNat_of_ge, CompPoly.Extension.Ext.ofBase, CompPoly.Extension.Ext.gen, CompPoly.Extension.Ext.shiftReduce, CompPoly.Extension.Ext.monomialMod, CompPoly.Extension.Ext.mul, CompPoly.Extension.Ext.redScan, CompPoly.Extension.Ext.redScan_size, CompPoly.Extension.Ext.redScan_getElem, CompPoly.Extension.Ext.red, CompPoly.Extension.Ext.red_getElem, Fin.foldl_add_eq_add_sum, CompPoly.Extension.Ext.convCoeff, CompPoly.Extension.Ext.contractCoeff, CompPoly.Extension.Ext.mulTbl, CompPoly.Extension.Ext.convCoeff_zero, CompPoly.Extension.Ext.sum_fin_add_eq_sum_fin_ite, CompPoly.Extension.Ext.mul_eq_mulTbl, CompPoly.Extension.Ext.coeff_zero, CompPoly.Extension.Ext.coeff_one, CompPoly.Extension.Ext.coeff_add, CompPoly.Extension.Ext.coeff_neg, CompPoly.Extension.Ext.coeff_sub, CompPoly.Extension.Ext.coeff_smul, CompPoly.Extension.Ext.coeff_shiftReduce, CompPoly.Extension.Ext.coeff_mul, CompPoly.Extension.Ext.coeff_ofBase, CompPoly.Extension.Ext.coeff_gen, CompPoly.Extension.Ext.ofBase_one, CompPoly.Extension.Ext.ofBase_zero, CompPoly.Extension.Ext.ofBase_natCast, CompPoly.Extension.Ext.ofBase_intCast, CompPoly.Extension.Ext.coeff_natCast, CompPoly.Extension.Ext.coeff_intCast, CompPoly.Extension.Ext.pow_def, CompPoly.Extension.Ext.inv, CompPoly.Extension.Ext.instInv, CompPoly.Extension.Ext.instDiv, CompPoly.Extension.Ext.inv_def, CompPoly.Extension.Ext.div_def, CompPoly.Extension.BinomialParams, CompPoly.Extension.BinomialParams.d_pos, CompPoly.Extension.BinomialParams.toExtensionParams, CompPoly.Extension.BinomialParams.toExtensionParams_d, CompPoly.Extension.BinomialParams.toExtensionParams_q, CompPoly.Extension.BinomialParams.toExtensionParams_lowerCoeff
statement: formalized
proof: formalized
---

# Computable arithmetic for monic quotient presentations

`CompPoly.Fields.Extension.Arithmetic`, in [CompPoly/Fields/Extension/Arithmetic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean), by Derek Sorensen.

> `ExtensionParams F` stores the degree, lower modulus coefficients and an explicit inverse-exponent
> parameter `q`. `Ext P` is one nominal carrier with coefficient vectors in ascending degree order.
> Its coordinate maps require no algebraic structure; arithmetic uses a ring of coefficients.
> The presentation index separates parameter values for a fixed coefficient algebra. Operations
> and their theorems are relative to the supplied ring or field structure on `F`; the raw carrier
> does not separate alternative algebra structures on that same type. Distinct coefficient
> presentations should use nominal coefficient types and explicit ring maps. The polynomial quotient
> interpretation uses commutative coefficients; the raw formulas are defined for any ring.
>
> Multiplication reduces monomials with `shiftReduce`. The executable reduction-table implementation
> `mulTbl` is connected to `mul` by `mul_eq_mulTbl`. Power uses binary exponentiation, and the
> canonical inverse candidate uses the literal exponent `q^d - 2`.
>
> This module supplies no cardinality or irreducibility certificate. Polynomial specifications and
> quotient correspondence belong to `Extension/Defs.lean` and `Extension/Bridge.lean`; certified field
> laws belong to `Extension/Field.lean`. Raw parameters with an incorrect `q` still admit arithmetic
> but do not thereby acquire field laws. The binomial conversion describes the modulus `X^d - W`.

`CompPoly.Extension.ExtensionParams` (structure, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L49))

> The data defining an extension `F[X] / f` by a monic modulus `f` of degree `d`.
>
> The modulus is stored by its `d` lower coefficients: `f = X^d + ∑_{i < d} lower[i] · X^i`. The
> leading coefficient is an implicit `1`, so `f` is monic by construction.
>
> Irreducibility is not part of these parameters: the quotient is a commutative ring for every
> monic modulus over a commutative ring. Field laws additionally require finite-cardinality and
> irreducibility certificates.

```lean
structure ExtensionParams (F : Type*) where
  /-- The degree of the extension. -/
  d : ℕ
  /-- Degree at least two; a degree-one "extension" is just `F`. -/
  two_le : 2 ≤ d
  /-- The lower coefficients of the monic modulus, little-endian: `lower[i]` is the coefficient
  of `X^i` in `poly`, for `i < d`. The coefficient of `X^d` is an implicit `1`. -/
  lower : Vector F d
  /-- The proposed base cardinality, stored explicitly for the inverse exponent.

  Raw arithmetic does not certify this value. Field laws require a separate proof that
  `Nat.card F = q`, together with finiteness and irreducibility. -/
  q : ℕ
```

`CompPoly.Extension.ExtensionParams.lowerCoeff` (definition, [line 68](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L68))

> The coefficient of `X^i` in the lower part of the modulus.

```lean
def lowerCoeff (i : Fin P.d) : F
```

`CompPoly.Extension.ExtensionParams.lowerCoeffNat` (definition, [line 71](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L71))

> The lower modulus coefficient at index `k`, or zero when `P.d ≤ k`.

```lean
def lowerCoeffNat (k : ℕ) : F
```

`CompPoly.Extension.ExtensionParams.lowerCoeffNat_coe` (theorem, [line 73](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L73))

```lean
theorem lowerCoeffNat_coe (i : Fin P.d) : P.lowerCoeffNat (i : ℕ) = P.lowerCoeff i
```

`CompPoly.Extension.ExtensionParams.lowerCoeffNat_of_ge` (theorem, [line 76](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L76))

```lean
theorem lowerCoeffNat_of_ge {k : ℕ} (h : P.d ≤ k) : P.lowerCoeffNat k = 0
```

`CompPoly.Extension.ExtensionParams.d_pos` (theorem, [line 80](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L80))

```lean
theorem d_pos : 0 < P.d
```

`CompPoly.Extension.Ext` (structure, [line 88](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L88))

> The carrier of the quotient by the monic modulus in `P`, with coefficients in ascending
> order of powers. The parameter remains part of the type even when two moduli have equal degree.

```lean
structure Ext {F : Type*} (P : ExtensionParams F) : Type _ where
  /-- The coefficient of `X^i` is stored at index `i`. -/
  coeffs : Vector F P.d
```

`CompPoly.Extension.Ext.ofVector` (definition, [line 97](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L97))

> Build an element from coefficients in ascending order of powers.

```lean
def ofVector (v : Vector F P.d) : Ext P
```

`CompPoly.Extension.Ext.coeffs_ofVector` (theorem, [line 101](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L101))

> Extracting the coefficients of a constructed element returns the input vector.

```lean
theorem coeffs_ofVector (v : Vector F P.d) : coeffs (ofVector (P := P) v) = v
```

`CompPoly.Extension.Ext.ofVector_coeffs` (theorem, [line 105](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L105))

> Reconstructing an element from its coefficient vector returns that element.

```lean
theorem ofVector_coeffs (x : Ext P) : ofVector (coeffs x) = x
```

`CompPoly.Extension.Ext.coeffs_injective` (theorem, [line 109](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L109))

> The coefficient vector uniquely determines an element.

```lean
theorem coeffs_injective : Function.Injective (coeffs (P := P))
```

`CompPoly.Extension.Ext.ofFn` (definition, [line 113](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L113))

> Build an element from a coefficient function.

```lean
def ofFn (g : Fin P.d → F) : Ext P
```

`CompPoly.Extension.Ext.coeff` (definition, [line 116](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L116))

> The coefficient of `X^i`.

```lean
def coeff (x : Ext P) (i : Fin P.d) : F
```

`CompPoly.Extension.Ext.coeff_ofFn` (theorem, [line 119](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L119))

```lean
theorem coeff_ofFn (g : Fin P.d → F) (i : Fin P.d) : coeff (ofFn g) i = g i
```

`CompPoly.Extension.Ext.ext` (theorem, [line 124](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L124))

> Two elements with the same coefficients are equal.

```lean
theorem ext {x y : Ext P} (h : ∀ i, coeff x i = coeff y i) : x = y
```

`CompPoly.Extension.Ext.ofFn_coeff` (theorem, [line 128](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L128))

```lean
theorem ofFn_coeff (x : Ext P) : ofFn (coeff x) = x
```

`CompPoly.Extension.Ext.equivFn` (definition, [line 131](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L131))

> Coefficient vectors are exactly functions out of `Fin d`.

```lean
def equivFn (P : ExtensionParams F) : Ext P ≃ (Fin P.d → F)
```

`CompPoly.Extension.Ext.coeffNat` (definition, [line 138](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L138))

> The coefficient at index `i`, or zero when `P.d ≤ i`.

```lean
def coeffNat (x : Ext P) (i : ℕ) : F
```

`CompPoly.Extension.Ext.coeffNat_coe` (theorem, [line 140](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L140))

```lean
theorem coeffNat_coe (x : Ext P) (i : Fin P.d) : coeffNat x (i : ℕ) = coeff x i
```

`CompPoly.Extension.Ext.coeffNat_of_lt` (theorem, [line 143](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L143))

```lean
theorem coeffNat_of_lt (x : Ext P) {i : ℕ} (h : i < P.d) : coeffNat x i = coeff x ⟨i, h⟩
```

`CompPoly.Extension.Ext.coeffNat_of_ge` (theorem, [line 146](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L146))

```lean
theorem coeffNat_of_ge (x : Ext P) {i : ℕ} (h : P.d ≤ i) : coeffNat x i = 0
```

> ### Distinguished elements
>
> `ofBase` places a coefficient-ring element in the constant coordinate, and `gen` has the
> coordinates of `X`. The quotient bridge over a field promotes the constant embedding to an
> `Algebra` structure and identifies the reduced power `gen ^ d` with `monomialMod d`.

`CompPoly.Extension.Ext.ofBase` (definition, [line 157](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L157))

> Place a coefficient-ring element in the constant coordinate.

```lean
def ofBase (c : F) : Ext P
```

`CompPoly.Extension.Ext.gen` (definition, [line 160](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L160))

> The coordinate vector with coefficient one at `X` and zero elsewhere.

```lean
def gen : Ext P
```

> ### Operations
>
> Multiplication is defined in terms of `shiftReduce` — the "multiply by `X`, reduce mod `f`"
> map — whose iterates `monomialMod k = shiftReduce^[k] 1` are the reduced monomials `X^k mod f`.
> Everything downstream is proved from the single homomorphism law
> `toQuot (shiftReduce e) = rt * toQuot e`.

`CompPoly.Extension.Ext.shiftReduce` (definition, [line 184](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L184))

> Multiply by `X` and reduce modulo `f`.
>
> `X · (∑ eᵢ Xⁱ) = ∑ eᵢ X^(i+1)`, whose top term `e_{d-1} X^d` wraps via `X^d = -∑ lowerₘ Xᵐ`.
> So coefficient `m` of the reduced result is `e_{m-1} - e_{d-1} · lowerₘ`, with `e_{-1} = 0`.
> This is the single linear map whose iterates build the reduction table `red`.

```lean
def shiftReduce (e : Ext P) : Ext P
```

`CompPoly.Extension.Ext.monomialMod` (definition, [line 191](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L191))

> The reduced form of `X^k` modulo `f`, obtained by iterating `shiftReduce` (multiply by `X`,
> reduce) `k` times from `1 = X^0`. Its image under `toQuot` is `rt ^ k`.

```lean
def monomialMod (k : ℕ) : Ext P
```

`CompPoly.Extension.Ext.mul` (definition, [line 201](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L201))

> The monic-reduction product formula, representing multiplication in `F[X] / f`
> when the coefficient ring is commutative.
>
> Each product monomial `Xⁱ⁺ʲ` is reduced modulo `f` by `monomialMod (i + j)`, so coefficient `m`
> of the product collects `xᵢ · yⱼ · [X^(i+j) mod f]ₘ` over all pairs `(i, j)`.

```lean
def mul (x y : Ext P) : Ext P
```

`CompPoly.Extension.Ext.redScan` (definition, [line 208](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L208))

> Append `cur, shiftReduce cur, …`, `n` entries in all, to `acc`; the scan that builds `red`.
> This is the table the `shiftReduce` docstring above refers to.

```lean
def redScan : ℕ → Ext P → Array (Ext P) → Array (Ext P)
```

`CompPoly.Extension.Ext.redScan_size` (theorem, [line 212](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L212))

```lean
theorem redScan_size (n : ℕ) (cur : Ext P) (acc : Array (Ext P)) :
    (redScan n cur acc).size = acc.size + n
```

`CompPoly.Extension.Ext.redScan_getElem` (theorem, [line 219](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L219))

> Entry `k` of the scan is `shiftReduce^[k - acc.size] cur` past the prefix it was given.

```lean
theorem redScan_getElem (n : ℕ) (cur : Ext P) (acc : Array (Ext P)) (k : ℕ)
    (h : k < (redScan n cur acc).size) :
    (redScan n cur acc)[k] =
      if hlt : k < acc.size then acc[k] else shiftReduce^[k - acc.size] cur
```

`CompPoly.Extension.Ext.red` (definition, [line 253](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L253))

> The reduction table: `red P` holds `X^k mod f` for every `k ≤ 2d - 2`, i.e. every exponent a
> product of two reduced elements can reach.
>
> Built by one `redScan` from `1`, so the whole table costs `O(d^2)`; `Vector.ofFn (monomialMod ·)`
> would iterate `shiftReduce` from scratch for every entry, `O(d^3)` in all. It exists purely for
> speed: `mul` is the specification, and `mulTbl` below is the compiled implementation that
> consults this table.

```lean
def red (P : ExtensionParams F) : Vector (Ext P) (2 * P.d - 1)
```

`CompPoly.Extension.Ext.red_getElem` (theorem, [line 256](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L256))

```lean
theorem red_getElem {k : ℕ} (hk : k < 2 * P.d - 1) :
    (red P)[k] = monomialMod k
```

`Fin.foldl_add_eq_add_sum` (theorem, [line 264](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L264))

> A left fold that adds `f i` at each step is `a` plus the sum; the bridge from the loops the
> compiler runs to the `Finset.sum`s the specification is stated with.

```lean
theorem _root_.Fin.foldl_add_eq_add_sum {M : Type*} [AddCommMonoid M] {n : ℕ} (f : Fin n → M)
    (a : M) : Fin.foldl n (fun acc i => acc + f i) a = a + ∑ i, f i
```

`CompPoly.Extension.Ext.convCoeff` (definition, [line 286](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L286))

> Coefficient `k` of the unreduced product `x · y` in `F[X]`, the convolution `∑_{i + j = k} xᵢ yⱼ`,
> as one loop over `i` with `j = k - i`; a pair outside `[0, d)` contributes zero. `k` ranges over
> `[0, 2d - 1)`, the degrees a product of two reduced elements can reach.
>
> Deliberately a separate function over its own `Mul` and `Add` instances, `@[noinline]` and
> `@[nospecialize]`, and likewise `contractCoeff` below. Written inside `mulTbl`, or inlined or
> specialised on the `Ring F` instance, `*` and `+` on `F` are re-derived from the ring dictionary
> on every step of the innermost loop, through projections that allocate an intermediate structure
> each time; the emitted C of the first loop run had `instDistribOfSemiring` in the loop body.
> Here the two operations arrive as arguments, derived once per call of `mulTbl`, and the loop
> only applies them. (`nospecialize` matters: instance arguments are specialised even without
> `@[specialize]` on the callee.)

```lean
def convCoeff [Mul F] [Add F] [Zero F] (x y : Ext P) (k : ℕ) (init : F) : F
```

`CompPoly.Extension.Ext.contractCoeff` (definition, [line 295](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L295))

> Coefficient `m` of the reduction of the unreduced product `prod` against the table `tbl`:
> `∑_k prodₖ · [X^k mod f]ₘ`. See `convCoeff` for why this is a separate function.

```lean
def contractCoeff [Mul F] [Add F] (tbl : Vector (Ext P) (2 * P.d - 1))
    (prod : Vector F (2 * P.d - 1)) (m : Fin P.d) (init : F) : F
```

`CompPoly.Extension.Ext.mulTbl` (definition, [line 318](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L318))

> Table-driven multiplication: the compiled implementation of `mul`.
>
> Mathematically identical to `mul`, in two stages: the unreduced product `x · y` in `F[X]`,
> `2d - 1` coefficients by `convCoeff`, then one contraction of those against the reduction table
> `red` by `contractCoeff`. That is `d^2 + (2d - 1) d` coefficient multiplications where `mul`
> performs `d^3`, and the reduced monomials come from the table instead of being re-derived by
> `monomialMod` for every output coefficient. The sums are `Fin.foldl` loops rather than
> `Finset.sum`, which compiles to list-building `Multiset` machinery.
>
> `mul` remains the definition everything is proved about; `mul_eq_mulTbl` below swaps this in for
> compilation via `@[csimp]`. The loops live in `convCoeff` and `contractCoeff`, for the reason
> given there.
>
> Specialised on `P` as well as on the instances: at a call site whose modulus is a constant, which
> is every concrete extension field, the table `red P` is then a closed term the compiler
> evaluates once, rather than being rebuilt on every multiplication.

```lean
def mulTbl (x y : Ext P) : Ext P
```

`CompPoly.Extension.Ext.convCoeff_zero` (theorem, [line 324](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L324))

> `convCoeff` from zero is the convolution sum, with the second index as a `coeffNat`.

```lean
theorem convCoeff_zero (x y : Ext P) (k : ℕ) :
    convCoeff x y k 0 = ∑ i : Fin P.d,
      if (i : ℕ) ≤ k ∧ k - (i : ℕ) < P.d then coeff x i * coeffNat y (k - (i : ℕ)) else 0
```

`CompPoly.Extension.Ext.sum_fin_add_eq_sum_fin_ite` (theorem, [line 335](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L335))

> The reindexing behind `mul_eq_mulTbl`: summing `g (i + j)` over `j < d` is summing `g k` over
> the `k < 2d - 1` that `i + j` reaches, for a fixed `i < d`.

```lean
theorem sum_fin_add_eq_sum_fin_ite {M : Type*} [AddCommMonoid M] {d : ℕ} (i : Fin d)
    (g : ℕ → M) :
    ∑ j : Fin d, g ((i : ℕ) + (j : ℕ)) =
      ∑ k : Fin (2 * d - 1), if (i : ℕ) ≤ (k : ℕ) ∧ (k : ℕ) - (i : ℕ) < d then g k else 0
```

`CompPoly.Extension.Ext.mul_eq_mulTbl` (theorem, [line 355](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L355))

```lean
theorem mul_eq_mulTbl : @mul = @mulTbl
```

> ### Coefficients of the operations

`CompPoly.Extension.Ext.coeff_zero` (theorem, [line 392](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L392))

```lean
theorem coeff_zero (i : Fin P.d) : coeff (0 : Ext P) i = 0
```

`CompPoly.Extension.Ext.coeff_one` (theorem, [line 393](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L393))

```lean
theorem coeff_one (i : Fin P.d) :
    coeff (1 : Ext P) i = if (i : ℕ) = 0 then 1 else 0
```

`CompPoly.Extension.Ext.coeff_add` (theorem, [line 395](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L395))

```lean
theorem coeff_add (x y : Ext P) (i : Fin P.d) :
    coeff (x + y) i = coeff x i + coeff y i
```

`CompPoly.Extension.Ext.coeff_neg` (theorem, [line 397](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L397))

```lean
theorem coeff_neg (x : Ext P) (i : Fin P.d) : coeff (-x) i = -coeff x i
```

`CompPoly.Extension.Ext.coeff_sub` (theorem, [line 398](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L398))

```lean
theorem coeff_sub (x y : Ext P) (i : Fin P.d) :
    coeff (x - y) i = coeff x i - coeff y i
```

`CompPoly.Extension.Ext.coeff_smul` (theorem, [line 400](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L400))

```lean
theorem coeff_smul (c : F) (x : Ext P) (i : Fin P.d) :
    coeff (c • x) i = c * coeff x i
```

`CompPoly.Extension.Ext.coeff_shiftReduce` (theorem, [line 403](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L403))

```lean
theorem coeff_shiftReduce (e : Ext P) (m : Fin P.d) :
    coeff (shiftReduce e) m =
      (if (m : ℕ) = 0 then 0 else coeffNat e ((m : ℕ) - 1))
        - coeffNat e (P.d - 1) * P.lowerCoeff m
```

`CompPoly.Extension.Ext.coeff_mul` (theorem, [line 408](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L408))

```lean
theorem coeff_mul (x y : Ext P) (m : Fin P.d) :
    coeff (x * y) m =
      ∑ i : Fin P.d, ∑ j : Fin P.d,
        coeff x i * coeff y j * coeff (monomialMod ((i : ℕ) + (j : ℕ))) m
```

`CompPoly.Extension.Ext.coeff_ofBase` (theorem, [line 414](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L414))

```lean
theorem coeff_ofBase (c : F) (i : Fin P.d) :
    coeff (ofBase (P := P) c) i = if (i : ℕ) = 0 then c else 0
```

`CompPoly.Extension.Ext.coeff_gen` (theorem, [line 417](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L417))

```lean
theorem coeff_gen (i : Fin P.d) :
    coeff (gen : Ext P) i = if (i : ℕ) = 1 then 1 else 0
```

`CompPoly.Extension.Ext.ofBase_one` (theorem, [line 421](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L421))

> `ofBase` agrees with `1` on the multiplicative unit.

```lean
theorem ofBase_one : ofBase (P := P) (1 : F) = 1
```

`CompPoly.Extension.Ext.ofBase_zero` (theorem, [line 424](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L424))

> `ofBase` agrees with `0`.

```lean
theorem ofBase_zero : ofBase (P := P) (0 : F) = 0
```

`CompPoly.Extension.Ext.ofBase_natCast` (theorem, [line 428](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L428))

> `ofBase` agrees with the `ℕ`-cast, so scalars and numerals do not diverge.

```lean
theorem ofBase_natCast (n : ℕ) : ofBase (P := P) (n : F) = (n : Ext P)
```

`CompPoly.Extension.Ext.ofBase_intCast` (theorem, [line 431](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L431))

> `ofBase` agrees with the `ℤ`-cast.

```lean
theorem ofBase_intCast (n : ℤ) : ofBase (P := P) (n : F) = (n : Ext P)
```

`CompPoly.Extension.Ext.coeff_natCast` (theorem, [line 433](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L433))

```lean
theorem coeff_natCast (n : ℕ) (i : Fin P.d) :
    coeff (n : Ext P) i = if (i : ℕ) = 0 then (n : F) else 0
```

`CompPoly.Extension.Ext.coeff_intCast` (theorem, [line 436](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L436))

```lean
theorem coeff_intCast (n : ℤ) (i : Fin P.d) :
    coeff (n : Ext P) i = if (i : ℕ) = 0 then (n : F) else 0
```

`CompPoly.Extension.Ext.pow_def` (theorem, [line 439](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L439))

```lean
theorem pow_def (x : Ext P) (n : ℕ) : x ^ n = npowBinRec n x
```

`CompPoly.Extension.Ext.inv` (definition, [line 445](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L445))

> The canonical inverse candidate `x ^ (q^d - 2)`.
>
> Inverse laws require finite-cardinality and irreducibility certificates. For arbitrary `q`,
> this operation need not send zero to zero.

```lean
def inv (x : Ext P) : Ext P
```

`CompPoly.Extension.Ext.instInv` (instance, [line 447](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L447))

```lean
instance instInv : Inv (Ext P)
```

`CompPoly.Extension.Ext.instDiv` (instance, [line 448](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L448))

```lean
instance instDiv : Div (Ext P)
```

`CompPoly.Extension.Ext.inv_def` (theorem, [line 450](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L450))

```lean
theorem inv_def (x : Ext P) : x⁻¹ = x ^ (P.q ^ P.d - 2)
```

`CompPoly.Extension.Ext.div_def` (theorem, [line 451](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L451))

```lean
theorem div_def (x y : Ext P) : x / y = x * y⁻¹
```

> ### Binomial extensions as a special case
>
> A binomial extension `F[X] / (X^d - W)` is the case `lower = (-W, 0, …, 0)`. `BinomialParams`
> keeps the `W`-only interface; `toExtensionParams` maps it into the general framework. The
> polynomial correspondence and binomial irreducibility criterion are proved separately.

`CompPoly.Extension.BinomialParams` (structure, [line 466](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L466))

> Parameters for the quotient `F[X] / (X^d - W)`: the degree, constant `W`, and a proposed
> base cardinality. The modulus has lower coefficients `(-W, 0, …, 0)`.

```lean
structure BinomialParams (F : Type*) where
  /-- The degree of the extension. -/
  d : ℕ
  /-- The extension adjoins a `d`-th root of `W`. -/
  W : F
  /-- Degree at least two; a degree-one "extension" is just `F`. -/
  two_le : 2 ≤ d
  /-- The proposed base cardinality used by the inverse exponent. -/
  q : ℕ
```

`CompPoly.Extension.BinomialParams.d_pos` (theorem, [line 481](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L481))

```lean
theorem d_pos : 0 < P.d
```

`CompPoly.Extension.BinomialParams.toExtensionParams` (definition, [line 485](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L485))

> The general-framework parameters for the binomial modulus `X^d - W`: the lower coefficient
> vector is `(-W, 0, …, 0)`.

```lean
def toExtensionParams : ExtensionParams F
```

`CompPoly.Extension.BinomialParams.toExtensionParams_d` (theorem, [line 491](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L491))

```lean
theorem toExtensionParams_d : P.toExtensionParams.d = P.d
```

`CompPoly.Extension.BinomialParams.toExtensionParams_q` (theorem, [line 492](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L492))

```lean
theorem toExtensionParams_q : P.toExtensionParams.q = P.q
```

`CompPoly.Extension.BinomialParams.toExtensionParams_lowerCoeff` (theorem, [line 494](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean#L494))

```lean
theorem toExtensionParams_lowerCoeff (i : Fin P.toExtensionParams.d) :
    P.toExtensionParams.lowerCoeff i = if (i : ℕ) = 0 then -P.W else 0
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/Fields/Extension/Arithmetic.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Extension/Arithmetic.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Extension.Arithmetic.json)
