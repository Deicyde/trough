---
catalog: module
lean: CompPoly.Extension.Ext.rt, CompPoly.Extension.Ext.degree_poly, CompPoly.Extension.Ext.toQuot, CompPoly.Extension.Ext.toQuot_zero, CompPoly.Extension.Ext.toQuot_add, CompPoly.Extension.Ext.toQuot_neg, CompPoly.Extension.Ext.toQuot_sub, CompPoly.Extension.Ext.toQuot_smul, CompPoly.Extension.Ext.toQuot_one, CompPoly.Extension.Ext.toQuot_natCast, CompPoly.Extension.Ext.toQuot_intCast, CompPoly.Extension.Ext.toQuot_eq_mk, CompPoly.Extension.Ext.toQuot_injective, CompPoly.Extension.Ext.toQuot_inj, CompPoly.Extension.Ext.toQuot_rangeForm, CompPoly.Extension.Ext.rt_relation, CompPoly.Extension.Ext.sum_lower_rangeForm, CompPoly.Extension.Ext.coeffNat_shiftReduce, CompPoly.Extension.Ext.toQuot_shiftReduce, CompPoly.Extension.Ext.monomialMod_zero, CompPoly.Extension.Ext.monomialMod_succ, CompPoly.Extension.Ext.toQuot_monomialMod, CompPoly.Extension.Ext.toQuot_mul, CompPoly.Extension.Ext.mul_assoc', CompPoly.Extension.Ext.toQuot_pow, CompPoly.Extension.Ext.instAddCommGroup, CompPoly.Extension.Ext.instCommRing, CompPoly.Extension.Ext.toQuot_ofBase, CompPoly.Extension.Ext.toQuot_gen, CompPoly.Extension.Ext.ofBaseRingHom, CompPoly.Extension.Ext.ofBaseRingHom_apply, CompPoly.Extension.Ext.instAlgebra, CompPoly.Extension.Ext.algebraMap_eq_ofBase, CompPoly.Extension.Ext.toQuot_sum, CompPoly.Extension.Ext.gen_pow_d, CompPoly.Extension.Ext.aeval_gen_poly, CompPoly.Extension.Ext.toQuotRingHom, CompPoly.Extension.Ext.rt_pow_d_binomial, CompPoly.Extension.Ext.gen_pow_d_binomial
statement: formalized
proof: formalized
---

# Bridging `Ext P` to `AdjoinRoot P.poly`

`CompPoly.Fields.Extension.Bridge`, in [CompPoly/Fields/Extension/Bridge.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean), by Derek Sorensen.

> The computable coefficient-vector arithmetic of `CompPoly/Fields/Extension/Defs.lean` is related
> to its specification `AdjoinRoot f` by
>
> `toQuot x = ∑ i, algebraMap F _ (x.coeff i) * root ^ i`,
>
> which is shown to be an injective ring homomorphism. The ring axioms on `Ext P` are then
> discharged by pushing through `toQuot` rather than proved on coordinates.
>
> The load-bearing lemma is `toQuot_shiftReduce`: `shiftReduce` is "multiply by `X`, reduce mod
> `f`", and correspondingly `toQuot (shiftReduce e) = rt * toQuot e`. Everything about
> multiplication follows from it: `monomialMod k = X^k mod f` satisfies `toQuot (monomialMod k) =
> rt ^ k` by a one-line induction, and `toQuot_mul` is then a direct double sum with no case
> analysis on wrap-around.
>
> ## Main definitions and statements
>
> * `Ext.toQuot`: the map to `AdjoinRoot P.poly`.
> * `Ext.rt_relation`: the defining relation `rt ^ d = -∑ lowerᵢ rt ^ i`, from `AdjoinRoot.mk_self`.
> * `Ext.toQuot_shiftReduce`: the multiply-by-`X` homomorphism law.
> * `Ext.toQuot_mul`, `Ext.toQuot_add`, ...: `toQuot` is a ring homomorphism.
> * `Ext.toQuot_injective`: injective for any monic modulus; irreducibility is not needed.
> * `Ext.instCommRing`: the `CommRing` structure.
> * `Ext.toQuotRingHom`: `toQuot` packaged as a `RingHom`.
>
> Bijectivity, cardinality and the `Field` structure are in
> `CompPoly/Fields/Extension/Field.lean`.

`CompPoly.Extension.Ext.rt` (definition, [line 54](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L54))

> The image of `X` in the quotient, i.e. the adjoined root of `f`.

```lean
noncomputable def rt (P : ExtensionParams F) : Quot[P]
```

`CompPoly.Extension.Ext.degree_poly` (theorem, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L57))

> The degree of the defining polynomial, as a `WithBot ℕ`.

```lean
theorem degree_poly : P.poly.degree = (P.d : WithBot ℕ)
```

`CompPoly.Extension.Ext.toQuot` (definition, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L60))

> The map from coefficient vectors to the quotient ring.

```lean
noncomputable def toQuot (x : Ext P) : Quot[P]
```

> ### `toQuot` is additive

`CompPoly.Extension.Ext.toQuot_zero` (theorem, [line 65](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L65))

```lean
theorem toQuot_zero : toQuot (0 : Ext P) = 0
```

`CompPoly.Extension.Ext.toQuot_add` (theorem, [line 67](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L67))

```lean
theorem toQuot_add (x y : Ext P) : toQuot (x + y) = toQuot x + toQuot y
```

`CompPoly.Extension.Ext.toQuot_neg` (theorem, [line 70](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L70))

```lean
theorem toQuot_neg (x : Ext P) : toQuot (-x) = -toQuot x
```

`CompPoly.Extension.Ext.toQuot_sub` (theorem, [line 73](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L73))

```lean
theorem toQuot_sub (x y : Ext P) : toQuot (x - y) = toQuot x - toQuot y
```

`CompPoly.Extension.Ext.toQuot_smul` (theorem, [line 76](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L76))

```lean
theorem toQuot_smul (c : F) (x : Ext P) :
    toQuot (c • x) = algebraMap F Quot[P] c * toQuot x
```

`CompPoly.Extension.Ext.toQuot_one` (theorem, [line 81](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L81))

> Only the constant coefficient of `1` is nonzero, so `toQuot 1` collapses to `1`.

```lean
theorem toQuot_one : toQuot (1 : Ext P) = 1
```

`CompPoly.Extension.Ext.toQuot_natCast` (theorem, [line 88](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L88))

```lean
theorem toQuot_natCast (n : ℕ) : toQuot (n : Ext P) = n
```

`CompPoly.Extension.Ext.toQuot_intCast` (theorem, [line 95](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L95))

```lean
theorem toQuot_intCast (n : ℤ) : toQuot (n : Ext P) = n
```

> ### Injectivity

`CompPoly.Extension.Ext.toQuot_eq_mk` (theorem, [line 105](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L105))

> `toQuot` as the class of an explicit degree-`< d` polynomial representative.

```lean
theorem toQuot_eq_mk (x : Ext P) :
    toQuot x = AdjoinRoot.mk P.poly (∑ i : Fin P.d, C (coeff x i) * X ^ (i : ℕ))
```

`CompPoly.Extension.Ext.toQuot_injective` (theorem, [line 129](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L129))

```lean
theorem toQuot_injective : Function.Injective (toQuot (P := P))
```

`CompPoly.Extension.Ext.toQuot_inj` (theorem, [line 140](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L140))

```lean
theorem toQuot_inj {x y : Ext P} : toQuot x = toQuot y ↔ x = y
```

> ### The defining relation and the multiply-by-`X` homomorphism law

`CompPoly.Extension.Ext.toQuot_rangeForm` (theorem, [line 147](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L147))

> `toQuot` as a sum over `Finset.range`, using the total `coeffNat`. Convenient for the shift
> reindexing in `toQuot_shiftReduce`.

```lean
theorem toQuot_rangeForm (x : Ext P) :
    toQuot x = ∑ k ∈ Finset.range P.d, algebraMap F Quot[P] (coeffNat x k) * (rt P) ^ k
```

`CompPoly.Extension.Ext.rt_relation` (theorem, [line 155](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L155))

> **The defining relation**, from `AdjoinRoot.mk_self`: the adjoined root `rt` satisfies
> `rt ^ d + ∑ lowerᵢ · rt ^ i = 0`.

```lean
theorem rt_relation :
    (rt P) ^ P.d + ∑ i : Fin P.d, algebraMap F Quot[P] (P.lowerCoeff i) * (rt P) ^ (i : ℕ)
      = 0
```

`CompPoly.Extension.Ext.sum_lower_rangeForm` (theorem, [line 172](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L172))

> In `range` form: `∑_{m < d} lowerₘ · rt ^ m = -rt ^ d`.

```lean
theorem sum_lower_rangeForm :
    (∑ m ∈ Finset.range P.d, algebraMap F Quot[P] (P.lowerCoeffNat m) * (rt P) ^ m)
      = -(rt P) ^ P.d
```

`CompPoly.Extension.Ext.coeffNat_shiftReduce` (theorem, [line 184](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L184))

> The coefficient formula for `shiftReduce`, in `coeffNat` form.

```lean
theorem coeffNat_shiftReduce (e : Ext P) {m : ℕ} (h : m < P.d) :
    coeffNat (shiftReduce e) m
      = (if m = 0 then 0 else coeffNat e (m - 1)) - coeffNat e (P.d - 1) * P.lowerCoeffNat m
```

`CompPoly.Extension.Ext.toQuot_shiftReduce` (theorem, [line 194](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L194))

> **The multiply-by-`X` homomorphism law.** `shiftReduce` is multiplication by `X` in the quotient,
> so `toQuot (shiftReduce e) = rt * toQuot e`. This is the one place `rt_relation` is consumed, and
> everything about multiplication reduces to it.

```lean
theorem toQuot_shiftReduce (e : Ext P) : toQuot (shiftReduce e) = rt P * toQuot e
```

> ### Reduced monomials

`CompPoly.Extension.Ext.monomialMod_zero` (theorem, [line 230](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L230))

```lean
theorem monomialMod_zero : (monomialMod 0 : Ext P) = 1
```

`CompPoly.Extension.Ext.monomialMod_succ` (theorem, [line 232](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L232))

```lean
theorem monomialMod_succ (k : ℕ) :
    (monomialMod (k + 1) : Ext P) = shiftReduce (monomialMod k)
```

`CompPoly.Extension.Ext.toQuot_monomialMod` (theorem, [line 237](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L237))

> `monomialMod k` really is `X^k` reduced: its image under `toQuot` is `rt ^ k`.

```lean
theorem toQuot_monomialMod (k : ℕ) : toQuot (monomialMod k : Ext P) = (rt P) ^ k
```

> ### `toQuot` is multiplicative

`CompPoly.Extension.Ext.toQuot_mul` (theorem, [line 244](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L244))

```lean
theorem toQuot_mul (x y : Ext P) : toQuot (x * y) = toQuot x * toQuot y
```

> ### Exponentiation
>
> `x ^ n` on `Ext P` is `npowBinRec`, i.e. repeated squaring, so it costs `O(log n)`
> multiplications. `npowBinRec_succ` needs only `Semigroup`, and associativity is already
> available from `toQuot_mul` plus injectivity — so exponentiation can be handled before the full
> ring structure is transported.

`CompPoly.Extension.Ext.mul_assoc'` (theorem, [line 275](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L275))

> Associativity. Kept out of the instance graph as a plain theorem to avoid a `Semigroup`
> diamond with the `CommRing` instance below.

```lean
theorem mul_assoc' (x y z : Ext P) : x * y * z = x * (y * z)
```

`CompPoly.Extension.Ext.toQuot_pow` (theorem, [line 278](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L278))

```lean
theorem toQuot_pow (x : Ext P) (n : ℕ) : toQuot (x ^ n) = toQuot x ^ n
```

> ### Algebraic structure
>
> The axioms are all discharged by pushing through the injective `toQuot`, but the instances are
> built field-by-field with `where` rather than via `Function.Injective.commRing`. That transport
> takes `toQuot` as *data*, which would make the resulting instance `noncomputable` and — because
> `Monoid.toNatPow` then outranks `Ext.instPow` — would silently break compiled `x ^ n`. Building
> by hand keeps every operation computable, matching how `CPolynomial` assembles its instances in
> `CompPoly/Univariate/Basic.lean`.

`CompPoly.Extension.Ext.instAddCommGroup` (instance, [line 294](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L294))

```lean
instance instAddCommGroup : AddCommGroup (Ext P)
```

`CompPoly.Extension.Ext.instCommRing` (instance, [line 311](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L311))

```lean
instance instCommRing : CommRing (Ext P)
```

> ### The base field and the adjoined root

`CompPoly.Extension.Ext.toQuot_ofBase` (theorem, [line 336](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L336))

> `ofBase` lands on the constant coefficient, so it agrees with `algebraMap` into the quotient.

```lean
theorem toQuot_ofBase (c : F) :
    toQuot (ofBase (P := P) c) = algebraMap F Quot[P] c
```

`CompPoly.Extension.Ext.toQuot_gen` (theorem, [line 345](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L345))

> `gen` is the class of `X`, i.e. the adjoined root.

```lean
theorem toQuot_gen : toQuot (gen : Ext P) = rt P
```

`CompPoly.Extension.Ext.ofBaseRingHom` (definition, [line 354](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L354))

> The base-field embedding, as a ring homomorphism.

```lean
def ofBaseRingHom (P : ExtensionParams F) : F →+* Ext P
```

`CompPoly.Extension.Ext.ofBaseRingHom_apply` (theorem, [line 361](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L361))

```lean
theorem ofBaseRingHom_apply (c : F) : ofBaseRingHom P c = ofBase c
```

`CompPoly.Extension.Ext.instAlgebra` (instance, [line 364](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L364))

> The extension is an `F`-algebra.

```lean
instance instAlgebra : Algebra F (Ext P)
```

`CompPoly.Extension.Ext.algebraMap_eq_ofBase` (theorem, [line 370](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L370))

```lean
theorem algebraMap_eq_ofBase (c : F) : algebraMap F (Ext P) c = ofBase c
```

`CompPoly.Extension.Ext.toQuot_sum` (theorem, [line 372](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L372))

```lean
theorem toQuot_sum {ι : Type*} (s : Finset ι) (f : ι → Ext P) :
    toQuot (∑ i ∈ s, f i) = ∑ i ∈ s, toQuot (f i)
```

`CompPoly.Extension.Ext.gen_pow_d` (theorem, [line 381](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L381))

> **The defining relation** at the level of `Ext`: `gen ^ d` equals the reduced monomial
> `monomialMod d`.

```lean
theorem gen_pow_d : (gen : Ext P) ^ P.d = monomialMod P.d
```

`CompPoly.Extension.Ext.aeval_gen_poly` (theorem, [line 385](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L385))

> `gen` is a root of the defining polynomial, in the form Mathlib's `aeval` expects.

```lean
theorem aeval_gen_poly : aeval (gen : Ext P) P.poly = 0
```

`CompPoly.Extension.Ext.toQuotRingHom` (definition, [line 401](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L401))

> `toQuot` packaged as a ring homomorphism.

```lean
noncomputable def toQuotRingHom (P : ExtensionParams F) : Ext P →+* Quot[P]
```

> ### Binomial compatibility
>
> For a binomial modulus `X^d - W`, the general defining relation `rt ^ d = -∑ lowerᵢ rt ^ i`
> collapses (the only nonzero lower coefficient is `lower₀ = -W`) to `rt ^ d = W`, recovering the
> `gen ^ d = ofBase W` law the degree-4 extensions rely on.

`CompPoly.Extension.Ext.rt_pow_d_binomial` (theorem, [line 416](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L416))

> The collapsed defining relation for a binomial modulus: `rt ^ d = W`.

```lean
theorem rt_pow_d_binomial (P : BinomialParams F) :
    (rt P.toExtensionParams) ^ P.d = algebraMap F Quot[P.toExtensionParams] P.W
```

`CompPoly.Extension.Ext.gen_pow_d_binomial` (theorem, [line 432](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean#L432))

> **The binomial defining relation** at the level of `Ext`: `gen ^ d = ofBase W`.

```lean
theorem gen_pow_d_binomial (P : BinomialParams F) :
    (gen : Ext P.toExtensionParams) ^ P.d = ofBase P.W
```

## Depends on

- [Polynomial specifications for monic quotient presentations](defs.md)

## Sources

- [CompPoly/Fields/Extension/Bridge.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bridge.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Extension.Bridge.json)
