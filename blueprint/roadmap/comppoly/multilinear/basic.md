---
catalog: module
lean: CompPoly.CMlPolynomial, CompPoly.CMlPolynomial.mk, CompPoly.CMlPolynomialEval, CompPoly.CMlPolynomialEval.mk, CompPoly.CMlPolynomial.inhabited, CompPoly.CMlPolynomial.ofArray, CompPoly.CMlPolynomial.zero, CompPoly.CMlPolynomial.zero_def, CompPoly.CMlPolynomial.add, CompPoly.CMlPolynomial.neg, CompPoly.CMlPolynomial.smul, CompPoly.CMlPolynomial.nsmul, CompPoly.CMlPolynomial.zsmul, CompPoly.CMlPolynomial.monomialBasis, CompPoly.CMlPolynomial.map_monomialBasis, CompPoly.CMlPolynomial.monomialBasis_zero, CompPoly.CMlPolynomial.monomialBasis_getElem, CompPoly.CMlPolynomial.map, CompPoly.CMlPolynomial.evalHornerStep, CompPoly.CMlPolynomial.evalHornerCoeffs, CompPoly.CMlPolynomial.evalHorner, CompPoly.CMlPolynomial.eval₂Horner, CompPoly.CMlPolynomial.eval, CompPoly.CMlPolynomial.map_eval, CompPoly.CMlPolynomial.evalWithProducts, CompPoly.CMlPolynomial.evalWithProducts_eq_eval, CompPoly.CMlPolynomial.eval₂, CompPoly.CMlPolynomial.eval_horner_eq_eval, CompPoly.CMlPolynomial.eval₂_horner_eq_eval₂, CompPoly.CMlPolynomial.eval_add, CompPoly.CMlPolynomial.eval_zero, CompPoly.CMlPolynomial.eval_smul, CompPoly.CMlPolynomialEval.inhabited, CompPoly.CMlPolynomialEval.ofArray, CompPoly.CMlPolynomialEval.zero, CompPoly.CMlPolynomialEval.zero_def, CompPoly.CMlPolynomialEval.add, CompPoly.CMlPolynomialEval.neg, CompPoly.CMlPolynomialEval.smul, CompPoly.CMlPolynomialEval.nsmul, CompPoly.CMlPolynomialEval.zsmul, CompPoly.CMlPolynomialEval.lagrangeBasis, CompPoly.CMlPolynomialEval.lagrangeBasis_zero, CompPoly.CMlPolynomialEval.lagrangeBasis_getElem, CompPoly.CMlPolynomialEval.map, CompPoly.CMlPolynomialEval.evalMleStep, CompPoly.CMlPolynomialEval.evalMleLayer, CompPoly.CMlPolynomialEval.evalMleLayer_get, CompPoly.CMlPolynomialEval.evalMleValues, CompPoly.CMlPolynomialEval.evalMle, CompPoly.CMlPolynomialEval.evalMle_zero, CompPoly.CMlPolynomialEval.evalMle_succ, CompPoly.CMlPolynomialEval.eval₂Mle, CompPoly.CMlPolynomialEval.eval, CompPoly.CMlPolynomialEval.eval_smul, CompPoly.CMlPolynomialEval.eval₂, CompPoly.CMlPolynomialEval.eqTilde, CompPoly.CMlPolynomialEval.eval_mle_eq_eval, CompPoly.CMlPolynomialEval.eqTilde_eq_prod, CompPoly.CMlPolynomialEval.eqTilde_append, CompPoly.CMlPolynomialEval.eval₂_mle_eq_eval₂, CompPoly.CMlPolynomialEval.eval_add, CompPoly.CMlPolynomialEval.eval_zero, CompPoly.CMlPolynomial.monoToLagrangeLevel, CompPoly.CMlPolynomial.monoToLagrange, CompPoly.CMlPolynomial.lagrangeToMonoLevel, CompPoly.CMlPolynomial.lagrangeToMono, CompPoly.CMlPolynomial.lagrangeToMonoSpec, CompPoly.CMlPolynomial.monoToLagrangeSpec, CompPoly.CMlPolynomial.forwardRange, CompPoly.CMlPolynomial.forwardRange_length, CompPoly.CMlPolynomial.forwardRange_eq_of_r_eq, CompPoly.CMlPolynomial.forwardRange_getElem, CompPoly.CMlPolynomial.forwardRange_succ_right_ne_empty, CompPoly.CMlPolynomial.forwardRange_pred_le_ne_empty, CompPoly.CMlPolynomial.forwardRange_dropLast, CompPoly.CMlPolynomial.forwardRange_tail, CompPoly.CMlPolynomial.forwardRange_0_eq_finRange, CompPoly.CMlPolynomial.monoToLagrangeSegment, CompPoly.CMlPolynomial.lagrangeToMonoSegment, CompPoly.CMlPolynomial.monoToLagrange_eq_monoToLagrangeSegment, CompPoly.CMlPolynomial.lagrangeToMono_eq_lagrangeToMonoSegment, CompPoly.CMlPolynomial.testBit_of_sub_two_pow_of_bit_1, CompPoly.CMlPolynomial.lagrangeToMonoLevel_monoToLagrangeLevel_id, CompPoly.CMlPolynomial.monoToLagrangeLevel_lagrangeToMonoLevel_id, CompPoly.CMlPolynomial.mobius_apply_zeta_apply_eq_id, CompPoly.CMlPolynomial.zeta_apply_mobius_apply_eq_id, CompPoly.CMlPolynomial.equivMonomialLagrangeRepr
statement: formalized
proof: formalized
---

# Multilinear Polynomials

`CompPoly.Multilinear.Basic`, in [CompPoly/Multilinear/Basic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean), by Quang Dao, Chung Thai Nguyen, Aristotle (Harmonic), Elias Judin.

> This file defines computable representations of **multilinear polynomials**.
>
> The first representation is by their coefficients, and the second representation is by their
> evaluations over the Boolean hypercube `{0,1}^n`. Both representations are defined as `Vector`s of
> length `2^n`, where `n` is the number of variables. We will define operations on these
> representations, and prove equivalence between them, and with the standard Mathlib definition of
> multilinear polynomials, which is the type `R⦃≤ 1⦄[X Fin n]` (notation for
> `MvPolynomial.restrictDegree (Fin n) R 1`).
>
> …

`CompPoly.CMlPolynomial` (definition, [line 39](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L39))

> `CMlPolynomial n R` is the type of multilinear polynomials in `n` variables over a ring `R`.
> It is represented by its monomial coefficients as a `Vector` of length `2^n`.
> The indexing is **little-endian** (i.e. the least significant bit is the first bit).

```lean
def CMlPolynomial (R : Type*) (n : ℕ)
```

`CompPoly.CMlPolynomial.mk` (definition, [line 40](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L40))

```lean
def CMlPolynomial.mk {R : Type*} (n : ℕ) (v : Vector R (2 ^ n)) : CMlPolynomial R n
```

`CompPoly.CMlPolynomialEval` (definition, [line 47](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L47))

> `CMlPolynomialEval n R` is the type of multilinear polynomials in `n` variables over a ring `R`.
> It is represented by its evaluations over the Boolean hypercube `{0,1}^n`,
> i.e. Lagrange basis coefficients.
> The indexing is **little-endian** (i.e. the least significant bit is the first bit).

```lean
def CMlPolynomialEval (R : Type*) (n : ℕ)
```

`CompPoly.CMlPolynomialEval.mk` (definition, [line 48](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L48))

```lean
def CMlPolynomialEval.mk {R : Type*} (n : ℕ) (v : Vector R (2 ^ n)) : CMlPolynomialEval R n
```

`CompPoly.CMlPolynomial.inhabited` (instance, [line 62](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L62))

```lean
instance inhabited [Inhabited R] : Inhabited (CMlPolynomial R n)
```

`CompPoly.CMlPolynomial.ofArray` (definition, [line 68](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L68))

> Conform a list of coefficients to a `CMlPolynomial` with a given number of variables.
> May either pad with zeros or truncate.

```lean
def ofArray [Zero R] (coeffs : Array R) (n : ℕ) : CMlPolynomial R n
```

`CompPoly.CMlPolynomial.zero` (definition, [line 75](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L75))

```lean
def zero [Zero R] : CMlPolynomial R n
```

`CompPoly.CMlPolynomial.zero_def` (lemma, [line 77](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L77))

```lean
lemma zero_def [Zero R] : zero = Vector.replicate (2 ^ n) 0
```

`CompPoly.CMlPolynomial.add` (definition, [line 81](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L81))

> Add two `CMlPolynomial`s

```lean
def add [Add R] (p q : CMlPolynomial R n) : CMlPolynomial R n
```

`CompPoly.CMlPolynomial.neg` (definition, [line 85](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L85))

> Negation of a `CMlPolynomial`

```lean
def neg [Neg R] (p : CMlPolynomial R n) : CMlPolynomial R n
```

`CompPoly.CMlPolynomial.smul` (definition, [line 89](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L89))

> Scalar multiplication of a `CMlPolynomial`

```lean
def smul [Mul R] (r : R) (p : CMlPolynomial R n) : CMlPolynomial R n
```

`CompPoly.CMlPolynomial.nsmul` (definition, [line 93](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L93))

> Scalar multiplication of a `CMlPolynomial` by a natural number

```lean
def nsmul [SMul ℕ R] (m : ℕ) (p : CMlPolynomial R n) : CMlPolynomial R n
```

`CompPoly.CMlPolynomial.zsmul` (definition, [line 98](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L98))

> Scalar multiplication of a `CMlPolynomial` by an integer

```lean
def zsmul [SMul ℤ R] (m : ℤ) (p : CMlPolynomial R n) : CMlPolynomial R n
```

`CompPoly.CMlPolynomial.monomialBasis` (definition, [line 160](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L160))

```lean
def monomialBasis (w : Vector R n) : Vector R (2 ^ n)
```

`CompPoly.CMlPolynomial.map_monomialBasis` (theorem, [line 165](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L165))

> Mapping each monomial-basis value by a ring homomorphism equals evaluating the
> monomial basis at the mapped point.

```lean
theorem map_monomialBasis (f : R →+* S) (x : Vector R n) :
    (monomialBasis x).map f = monomialBasis (x.map f)
```

`CompPoly.CMlPolynomial.monomialBasis_zero` (theorem, [line 172](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L172))

```lean
theorem monomialBasis_zero {w : Vector R 0} : monomialBasis w = #v[1]
```

`CompPoly.CMlPolynomial.monomialBasis_getElem` (theorem, [line 181](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L181))

> The `i`-th element of `monomialBasis w` is the product of `w[j]` if the `j`-th bit of `i` is 1,
> and `1` if the `j`-th bit of `i` is 0.

```lean
theorem monomialBasis_getElem {w : Vector R n} (i : Fin (2 ^ n)) :
    (monomialBasis w)[i] = ∏ j : Fin n, if (BitVec.ofFin i).getLsb j then w[j] else 1
```

`CompPoly.CMlPolynomial.map` (definition, [line 217](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L217))

```lean
def map {R S : Type*} [Semiring R] [Semiring S] (f : R →+* S)
    (p : CMlPolynomial R n) : CMlPolynomial S n
```

`CompPoly.CMlPolynomial.evalHornerStep` (definition, [line 223](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L223))

> One Horner reduction step, eliminating the next little-endian variable.

```lean
def evalHornerStep {n : ℕ}
    (coeffs : Vector R (2 ^ (n + 1))) (x0 : R) : Vector R (2 ^ n)
```

`CompPoly.CMlPolynomial.evalHornerCoeffs` (definition, [line 230](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L230))

> Evaluate dense multilinear coefficients by eliminating one variable at a time.

```lean
def evalHornerCoeffs :
    {n : ℕ} → Vector R (2 ^ n) → Vector R n → R
```

`CompPoly.CMlPolynomial.evalHorner` (definition, [line 238](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L238))

> Evaluate a `CMlPolynomial` at a point using a multilinear Horner method.

```lean
def evalHorner (p : CMlPolynomial R n) (x : Vector R n) : R
```

`CompPoly.CMlPolynomial.eval₂Horner` (definition, [line 243](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L243))

> Evaluate a `CMlPolynomial` using a ring homomorphism and multilinear Horner method.

```lean
def eval₂Horner (p : CMlPolynomial R n) (f : R →+* S) (x : Vector S n) : S
```

`CompPoly.CMlPolynomial.eval` (definition, [line 247](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L247))

> Evaluate a `CMlPolynomial` at a point

```lean
def eval (p : CMlPolynomial R n) (x : Vector R n) : R
```

`CompPoly.CMlPolynomial.map_eval` (theorem, [line 252](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L252))

> Mapping a coefficient-form evaluation by a ring homomorphism equals evaluating the
> mapped coefficients at the mapped point.

```lean
theorem map_eval (f : R →+* S) (p : CMlPolynomial R n) (x : Vector R n) :
    f (eval p x) = eval (map f p) (x.map f)
```

`CompPoly.CMlPolynomial.evalWithProducts` (definition, [line 260](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L260))

> Evaluate monomial coefficients by accumulating their products with the monomial-basis
> values in `W`, starting at zero, then reducing once to a value in `R`.

```lean
def evalWithProducts {W : Type*} [AddZero W] (product : R → R → W) (reduce : W →+ R)
    (p : CMlPolynomial R n) (x : Vector R n) : R
```

`CompPoly.CMlPolynomial.evalWithProducts_eq_eval` (theorem, [line 266](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L266))

> Product accumulation followed by additive reduction agrees with coefficient evaluation
> when reducing each product gives the ordinary product of its two factors.

```lean
theorem evalWithProducts_eq_eval {W : Type*} [AddZero W]
    (product : R → R → W) (reduce : W →+ R)
    (hproduct : ∀ a b, reduce (product a b) = a * b)
    (p : CMlPolynomial R n) (x : Vector R n) :
    evalWithProducts product reduce p x = eval p x
```

`CompPoly.CMlPolynomial.eval₂` (definition, [line 273](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L273))

```lean
def eval₂ (p : CMlPolynomial R n) (f : R →+* S) (x : Vector S n) : S
```

`CompPoly.CMlPolynomial.eval_horner_eq_eval` (theorem, [line 312](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L312))

> Horner evaluation agrees with the dot-product evaluator.

```lean
theorem eval_horner_eq_eval (p : CMlPolynomial R n) (x : Vector R n) :
    evalHorner p x = eval p x
```

`CompPoly.CMlPolynomial.eval₂_horner_eq_eval₂` (theorem, [line 326](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L326))

> Horner evaluation through a ring homomorphism agrees with the dot-product evaluator.

```lean
theorem eval₂_horner_eq_eval₂ (p : CMlPolynomial R n) (f : R →+* S) (x : Vector S n) :
    eval₂Horner p f x = eval₂ p f x
```

`CompPoly.CMlPolynomial.eval_add` (theorem, [line 331](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L331))

> Evaluation is additive in the coefficient vector.

```lean
theorem eval_add (p q : CMlPolynomial R n) (x : Vector R n) :
    eval (p + q) x = eval p x + eval q x
```

`CompPoly.CMlPolynomial.eval_zero` (theorem, [line 342](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L342))

> The zero coefficient vector evaluates to zero.

```lean
theorem eval_zero (x : Vector R n) : eval (0 : CMlPolynomial R n) x = 0
```

`CompPoly.CMlPolynomial.eval_smul` (theorem, [line 351](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L351))

> Evaluation commutes with scalar multiplication of the coefficient vector.

```lean
theorem eval_smul (a : R) (p : CMlPolynomial R n) (x : Vector R n) :
    eval (a • p) x = a * eval p x
```

`CompPoly.CMlPolynomialEval.inhabited` (instance, [line 369](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L369))

```lean
instance inhabited [Inhabited R] : Inhabited (CMlPolynomialEval R n)
```

`CompPoly.CMlPolynomialEval.ofArray` (definition, [line 375](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L375))

> Conform a list of coefficients to a `CMlPolynomialEval` with a given number of variables.
> May either pad with zeros or truncate.

```lean
def ofArray [Zero R] (coeffs : Array R) (n : ℕ) : CMlPolynomialEval R n
```

`CompPoly.CMlPolynomialEval.zero` (definition, [line 382](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L382))

```lean
def zero [Zero R] : CMlPolynomialEval R n
```

`CompPoly.CMlPolynomialEval.zero_def` (lemma, [line 384](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L384))

```lean
lemma zero_def [Zero R] : zero = Vector.replicate (2 ^ n) 0
```

`CompPoly.CMlPolynomialEval.add` (definition, [line 388](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L388))

> Add two `CMlPolynomialEval`s

```lean
def add [Add R] (p q : CMlPolynomialEval R n) : CMlPolynomialEval R n
```

`CompPoly.CMlPolynomialEval.neg` (definition, [line 393](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L393))

> Negation of a `CMlPolynomialEval`

```lean
def neg [Neg R] (p : CMlPolynomialEval R n) : CMlPolynomialEval R n
```

`CompPoly.CMlPolynomialEval.smul` (definition, [line 398](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L398))

> Scalar multiplication of a `CMlPolynomialEval`

```lean
def smul [Mul R] (r : R) (p : CMlPolynomialEval R n) : CMlPolynomialEval R n
```

`CompPoly.CMlPolynomialEval.nsmul` (definition, [line 403](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L403))

> Scalar multiplication of a `CMlPolynomialEval` by a natural number

```lean
def nsmul [SMul ℕ R] (m : ℕ) (p : CMlPolynomialEval R n) : CMlPolynomialEval R n
```

`CompPoly.CMlPolynomialEval.zsmul` (definition, [line 408](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L408))

> Scalar multiplication of a `CMlPolynomialEval` by an integer

```lean
def zsmul [SMul ℤ R] (m : ℤ) (p : CMlPolynomialEval R n) : CMlPolynomialEval R n
```

`CompPoly.CMlPolynomialEval.lagrangeBasis` (definition, [line 472](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L472))

> Lagrange (hypercube) basis at point `w`.
>
> Returns the length-`2^n` vector `v` such that for any `x ∈ {0,1}^n`, letting
> `i = ∑_{j=0}^{n-1} x_j · 2^j` (little‑endian indexing), we have
> `v[i] = ∏_{j < n} (x_j · w[j] + (1 - x_j) · (1 - w[j]))`.
> Equivalently, for `i : Fin (2^n)`,
> `v[i] = ∏_{j < n}, (if the j-th bit of i is 1 then w[j] else 1 - w[j])`.

```lean
def lagrangeBasis (w : Vector R n) : Vector R (2 ^ n)
```

`CompPoly.CMlPolynomialEval.lagrangeBasis_zero` (theorem, [line 476](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L476))

```lean
theorem lagrangeBasis_zero {w : Vector R 0} : lagrangeBasis w = #v[1]
```

`CompPoly.CMlPolynomialEval.lagrangeBasis_getElem` (theorem, [line 485](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L485))

> The `i`-th element of `lagrangeBasis w` is the product of `w[j]` if the `j`-th bit of `i` is 1,
> and `1 - w[j]` if the `j`-th bit of `i` is 0.

```lean
theorem lagrangeBasis_getElem {w : Vector R n} (i : Fin (2 ^ n)) :
    (lagrangeBasis w)[i] = ∏ j : Fin n, if (BitVec.ofFin i).getLsb j then w[j] else 1 - w[j]
```

`CompPoly.CMlPolynomialEval.map` (definition, [line 523](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L523))

> Map a ring homomorphism over a `CMlPolynomialEval`

```lean
def map {R S : Type*} [Semiring R] [Semiring S]
    (f : R →+* S) (p : CMlPolynomialEval R n) : CMlPolynomialEval S n
```

`CompPoly.CMlPolynomialEval.evalMleStep` (definition, [line 529](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L529))

> One multilinear-extension interpolation step, eliminating the next little-endian variable.

```lean
def evalMleStep {n : ℕ}
    (values : Vector R (2 ^ (n + 1))) (x0 : R) : Vector R (2 ^ n)
```

`CompPoly.CMlPolynomialEval.evalMleLayer` (definition, [line 537](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L537))

> Public multilinear-extension interpolation layer.

```lean
def evalMleLayer {n : ℕ}
    (values : CMlPolynomialEval R (n + 1)) (x0 : R) : CMlPolynomialEval R n
```

`CompPoly.CMlPolynomialEval.evalMleLayer_get` (theorem, [line 544](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L544))

> The `j`-th entry after one MLE layer is the affine interpolation of its input pair.

```lean
theorem evalMleLayer_get [CommRing R] {n : ℕ}
    (values : CMlPolynomialEval R (n + 1)) (x0 : R) (j : Fin (2 ^ n)) :
    (evalMleLayer values x0).get j =
      (1 - x0) * values.get ⟨2 * j.val, by omega⟩ +
        x0 * values.get ⟨2 * j.val + 1, by omega⟩
```

`CompPoly.CMlPolynomialEval.evalMleValues` (definition, [line 553](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L553))

> Evaluate hypercube values by recursively interpolating the multilinear extension.

```lean
def evalMleValues :
    {n : ℕ} → Vector R (2 ^ n) → Vector R n → R
```

`CompPoly.CMlPolynomialEval.evalMle` (definition, [line 561](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L561))

> Evaluate a `CMlPolynomialEval` by recursive multilinear-extension interpolation.

```lean
def evalMle (p : CMlPolynomialEval R n) (x : Vector R n) : R
```

`CompPoly.CMlPolynomialEval.evalMle_zero` (theorem, [line 567](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L567))

> Evaluating a zero-variable hypercube table returns its only value.

```lean
theorem evalMle_zero [CommRing R] (p : CMlPolynomialEval R 0) (x : Vector R 0) :
    evalMle p x = p.get ⟨0, by norm_num⟩
```

`CompPoly.CMlPolynomialEval.evalMle_succ` (theorem, [line 574](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L574))

> Recursive MLE evaluation first folds the head variable, then evaluates the tail.

```lean
theorem evalMle_succ [CommRing R] {n : ℕ}
    (p : CMlPolynomialEval R (n + 1)) (x : Vector R (n + 1)) :
    evalMle p x = evalMle (evalMleLayer p x.head) x.tail
```

`CompPoly.CMlPolynomialEval.eval₂Mle` (definition, [line 582](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L582))

> Evaluate a `CMlPolynomialEval` through a ring homomorphism using multilinear-extension
> interpolation.

```lean
def eval₂Mle (p : CMlPolynomialEval R n) (f : R →+* S) (x : Vector S n) : S
```

`CompPoly.CMlPolynomialEval.eval` (definition, [line 586](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L586))

> Evaluate a `CMlPolynomialEval` at a point

```lean
def eval (p : CMlPolynomialEval R n) (x : Vector R n) : R
```

`CompPoly.CMlPolynomialEval.eval_smul` (theorem, [line 590](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L590))

> Evaluation commutes with scalar multiplication of a hypercube table.

```lean
theorem eval_smul (a : R) (p : CMlPolynomialEval R n) (x : Vector R n) :
    eval (a • p) x = a * eval p x
```

`CompPoly.CMlPolynomialEval.eval₂` (definition, [line 602](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L602))

> Evaluate a `CMlPolynomialEval` at a point using a ring homomorphism

```lean
def eval₂ (p : CMlPolynomialEval R n) (f : R →+* S) (x : Vector S n) : S
```

`CompPoly.CMlPolynomialEval.eqTilde` (definition, [line 605](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L605))

> Evaluate the multilinear equality kernel `eq̃(w, x)`.

```lean
def eqTilde (w x : Vector R n) : R
```

`CompPoly.CMlPolynomialEval.eval_mle_eq_eval` (theorem, [line 648](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L648))

> Multilinear-extension interpolation agrees with the dot-product evaluator.

```lean
theorem eval_mle_eq_eval (p : CMlPolynomialEval R n) (x : Vector R n) :
    evalMle p x = eval p x
```

`CompPoly.CMlPolynomialEval.eqTilde_eq_prod` (theorem, [line 662](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L662))

> The multilinear equality kernel is the product of its coordinatewise affine factors.

```lean
theorem eqTilde_eq_prod (w x : Vector R n) :
    eqTilde w x = ∏ i : Fin n, (w[i] * x[i] + (1 - w[i]) * (1 - x[i]))
```

`CompPoly.CMlPolynomialEval.eqTilde_append` (theorem, [line 694](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L694))

> The equality kernel factors across appended coordinate blocks.

```lean
theorem eqTilde_append {m : ℕ} (w₁ x₁ : Vector R n) (w₂ x₂ : Vector R m) :
    eqTilde (w₁ ++ w₂) (x₁ ++ x₂) = eqTilde w₁ x₁ * eqTilde w₂ x₂
```

`CompPoly.CMlPolynomialEval.eval₂_mle_eq_eval₂` (theorem, [line 702](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L702))

> Multilinear-extension interpolation through a ring homomorphism agrees with the
> dot-product evaluator.

```lean
theorem eval₂_mle_eq_eval₂ (p : CMlPolynomialEval R n) (f : R →+* S) (x : Vector S n) :
    eval₂Mle p f x = eval₂ p f x
```

`CompPoly.CMlPolynomialEval.eval_add` (theorem, [line 708](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L708))

> Evaluation is additive in the coefficient vector.

```lean
theorem eval_add (p q : CMlPolynomialEval R n) (x : Vector R n) :
    eval (p + q) x = eval p x + eval q x
```

`CompPoly.CMlPolynomialEval.eval_zero` (theorem, [line 719](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L719))

> The zero coefficient vector evaluates to zero.

```lean
theorem eval_zero (x : Vector R n) : eval (0 : CMlPolynomialEval R n) x = 0
```

`CompPoly.CMlPolynomial.monoToLagrangeLevel` (definition, [line 754](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L754))

> **One level** of the zeta‑transform (coefficient to evaluation).
>
> Processes the `j`-th variable by folding the "partner" index (with bit `j` cleared) into
> every index that has bit `j` set. At output index `i`:
>
> $$ (\text{monoToLagrangeLevel}\ j\ v)[i] \ =\ \begin{cases}
>   v[i] + v[i - 2^j] & \text{if bit } j \text{ of } i \text{ is } 1 \\
>   v[i] & \text{otherwise}
> \end{cases} $$
>
> After applying every level `0, 1, …, n-1` the resulting entry at `i` is
> $\sum_{j \subseteq i} p[j]$ (bitwise subset), which is the hypercube evaluation at the
> Boolean point encoded by `i`. Cost per level: $O(2^n)$ additions, so the full transform
> is $O(n \cdot 2^n)$.
>
> The `stride` is $2^j$, the distance between indices that differ only in bit `j`.

```lean
def monoToLagrangeLevel {n : ℕ} (j : Fin n) : Vector R (2 ^ n) → Vector R (2 ^ n)
```

`CompPoly.CMlPolynomial.monoToLagrange` (definition, [line 771](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L771))

> **Full zeta transform**: coefficients → evaluations.
>
> Applies `monoToLagrangeLevel 0, 1, …, n-1` in that order via `foldl`. The resulting entry
> at each index `i : Fin (2 ^ n)` is $\sum_{j \subseteq i} p[j]$ (the classical zeta
> transform on the Boolean lattice).
>
> **Complexity:** $O(n \cdot 2^n)$ additions — this is the butterfly form. Contrast with
> the naive `monoToLagrangeSpec` which is $O(4^n)$.

```lean
def monoToLagrange (n : ℕ) : CMlPolynomial R n → CMlPolynomialEval R n
```

`CompPoly.CMlPolynomial.lagrangeToMonoLevel` (definition, [line 789](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L789))

> **One level** of the inverse zeta‑transform / Möbius transform (evaluation to
> coefficient).
>
> Processes the `j`-th variable by subtracting the partner entry (bit `j` cleared) from
> every index that has bit `j` set. At output index `i`:
>
> $$ (\text{lagrangeToMonoLevel}\ j\ v)[i] \ =\ \begin{cases}
>   v[i] - v[i - 2^j] & \text{if bit } j \text{ of } i \text{ is } 1 \\
>   v[i] & \text{otherwise}
> \end{cases} $$
>
> Each level is the exact inverse of `monoToLagrangeLevel j` (see
> `lagrangeToMonoLevel_monoToLagrangeLevel_id`).
>
> The `stride` is $2^j$.

```lean
def lagrangeToMonoLevel {n : ℕ} (j : Fin n) : Vector R (2 ^ n) → Vector R (2 ^ n)
```

`CompPoly.CMlPolynomial.lagrangeToMono` (definition, [line 808](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L808))

> **Full inverse / Möbius transform**: evaluations → coefficients.
>
> Applies `lagrangeToMonoLevel (n-1), (n-2), …, 0` via `foldr`. The resulting entry at
> each index `i : Fin (2 ^ n)` is the inclusion-exclusion sum
> $\sum_{j \subseteq i} (-1)^{\mathrm{popCount}(i) - \mathrm{popCount}(j)} \cdot p[j]$ —
> see `lagrangeToMono_eq_lagrangeToMonoSpec`.
>
> **Complexity:** $O(n \cdot 2^n)$ additions/subtractions. Contrast with the naive
> `lagrangeToMonoSpec` which is $O(4^n)$.

```lean
def lagrangeToMono (n : ℕ) :
    Vector R (2 ^ n) → Vector R (2 ^ n)
```

`CompPoly.CMlPolynomial.lagrangeToMonoSpec` (definition, [line 822](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L822))

> The $O(4^n)$ inclusion-exclusion specification for the Möbius transform.
>
> For each output index `i`, this sums over all indices `j` that are bitwise subsets of `i`
> (`i &&& j = j`), with sign
> $(-1)^{\mathrm{popCount}(i) - \mathrm{popCount}(j)}$:
>
> $$ (\text{lagrangeToMonoSpec}\ p)[i]
>   = \sum_{j \subseteq i} (-1)^{\mathrm{popCount}(i) - \mathrm{popCount}(j)} \cdot p[j]. $$
>
> Provable equivalent to the fast `lagrangeToMono` — see `lagrangeToMono_eq_lagrangeToMonoSpec`.

```lean
def lagrangeToMonoSpec (p : CMlPolynomialEval R n) : CMlPolynomialEval R n
```

`CompPoly.CMlPolynomial.monoToLagrangeSpec` (definition, [line 849](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L849))

> The $O(4^n)$ specification for the zeta transform (the mirror of
> `lagrangeToMonoSpec`).
>
> For each output index `i`, this sums `p[j]` over every index `j` that is a bitwise subset
> of `i` (`i &&& j = j`):
>
> $$ (\text{monoToLagrangeSpec}\ p)[i]\ =\ \sum_{j \subseteq i} p[j]. $$
>
> Provable equivalent to the fast `monoToLagrange` — see `monoToLagrange_eq_monoToLagrangeSpec`.

```lean
def monoToLagrangeSpec (p : CMlPolynomial R n) : CMlPolynomialEval R n
```

`CompPoly.CMlPolynomial.forwardRange` (definition, [line 863](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L863))

> Generates a list of indices representing a range of bit positions [l, r] in increasing order.
> Used for optimized recursive transforms that operate on segments of variables.
> Returns a list containing `l, l+1, ..., r`.
> The result is used to fold over dimensions in `monoToLagrangeSegment` and `lagrangeToMonoSegment`.

```lean
def forwardRange (n : ℕ) (r : Fin (n)) (l : Fin (r.val + 1)) : List (Fin n)
```

`CompPoly.CMlPolynomial.forwardRange_length` (lemma, [line 871](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L871))

```lean
lemma forwardRange_length (n : ℕ) (r : Fin n) (l : Fin (r.val + 1)) :
    (forwardRange n r l).length = r.val - l.val + 1
```

`CompPoly.CMlPolynomial.forwardRange_eq_of_r_eq` (lemma, [line 876](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L876))

```lean
lemma forwardRange_eq_of_r_eq (n : ℕ) (r1 r2 : Fin n) (h_r_eq : r1 = r2) (l : Fin (r1.val + 1)) :
    forwardRange n r1 l = forwardRange n r2 ⟨l, by omega⟩
```

`CompPoly.CMlPolynomial.forwardRange_getElem` (lemma, [line 881](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L881))

```lean
lemma forwardRange_getElem (n : ℕ) (r : Fin n) (l : Fin (r.val + 1)) (k : Fin (r.val - l.val + 1)) :
    (forwardRange n r l).get ⟨k, by
    rw [forwardRange]; simp only [List.length_ofFn]; omega⟩ = ⟨l.val + k, by omega⟩
```

`CompPoly.CMlPolynomial.forwardRange_succ_right_ne_empty` (lemma, [line 888](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L888))

```lean
lemma forwardRange_succ_right_ne_empty (n : ℕ) (r : Fin (n - 1)) (l : Fin (r.val + 1)) :
    forwardRange n ⟨r + 1, by omega⟩ ⟨l, by simp only; omega⟩ ≠ []
```

`CompPoly.CMlPolynomial.forwardRange_pred_le_ne_empty` (lemma, [line 894](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L894))

```lean
lemma forwardRange_pred_le_ne_empty (n : ℕ) (r : Fin n) (l : Fin (r.val + 1))
    (h_l_gt_0 : l.val > 0) : forwardRange n r ⟨l.val - 1, by omega⟩ ≠ []
```

`CompPoly.CMlPolynomial.forwardRange_dropLast` (lemma, [line 900](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L900))

```lean
lemma forwardRange_dropLast (n : ℕ) (r : Fin (n - 1)) (l : Fin (r.val + 1)) :
    (forwardRange n ⟨r + 1, by omega⟩ ⟨l, by simp only; omega⟩).dropLast
  = forwardRange n ⟨r, by omega⟩ ⟨l, by simp only [Fin.is_lt]⟩
```

`CompPoly.CMlPolynomial.forwardRange_tail` (lemma, [line 917](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L917))

```lean
lemma forwardRange_tail (n : ℕ) (r : Fin n) (l : Fin (r.val + 1)) (h_l_gt_0 : l.val > 0) :
    (forwardRange n r ⟨l.val - 1, by omega⟩).tail = forwardRange n r l
```

`CompPoly.CMlPolynomial.forwardRange_0_eq_finRange` (lemma, [line 932](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L932))

```lean
lemma forwardRange_0_eq_finRange (n : ℕ) [NeZero n] : forwardRange n ⟨n - 1, by
    have h_ne_zero : n ≠ 0 := NeZero.ne n
    omega
  ⟩ 0 = List.finRange n
```

`CompPoly.CMlPolynomial.monoToLagrangeSegment` (definition, [line 955](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L955))

> Performs the zeta-transform (coefficient to evaluation) on a segment of dimensions from `l` to `r`.
> Iteratively applies `monoToLagrangeLevel` for each dimension in the range.
> `0 ≤ l ≤ r < n`.

```lean
def monoToLagrangeSegment (n : ℕ) (r : Fin n) (l : Fin (r.val + 1)) :
    Vector R (2 ^ n) → Vector R (2 ^ n)
```

`CompPoly.CMlPolynomial.lagrangeToMonoSegment` (definition, [line 971](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L971))

> Performs the inverse zeta-transform (evaluation to coefficient) on a segment of dimensions
>
> from `l` to `r`.
>
> Iteratively applies `lagrangeToMonoLevel` for each dimension in the range (in reverse order).
>
> `0 ≤ l ≤ r < n`.

```lean
def lagrangeToMonoSegment (n : ℕ) (r : Fin n) (l : Fin (r.val + 1)) :

    Vector R (2 ^ n) → Vector R (2 ^ n)
```

`CompPoly.CMlPolynomial.monoToLagrange_eq_monoToLagrangeSegment` (lemma, [line 979](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L979))

```lean
lemma monoToLagrange_eq_monoToLagrangeSegment (n : ℕ) [NeZero n] (v : Vector R (2 ^ n)) :
    have h_n_ne_zero: n ≠ 0 := by exact NeZero.ne n
  monoToLagrange n v = monoToLagrangeSegment n (r:=⟨n - 1, by omega⟩) (l:=⟨0, by omega⟩) v
```

`CompPoly.CMlPolynomial.lagrangeToMono_eq_lagrangeToMonoSegment` (lemma, [line 988](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L988))

```lean
lemma lagrangeToMono_eq_lagrangeToMonoSegment (n : ℕ) [NeZero n] (v : Vector R (2 ^ n)) :
    have h_n_ne_zero: n ≠ 0 := by exact NeZero.ne n
  lagrangeToMono n v = lagrangeToMonoSegment n (r:=⟨n - 1, by omega⟩) (l:=⟨0, by omega⟩) v
```

`CompPoly.CMlPolynomial.testBit_of_sub_two_pow_of_bit_1` (lemma, [line 997](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L997))

```lean
lemma testBit_of_sub_two_pow_of_bit_1 {n i : ℕ} (h_testBit_eq_1 : (n).testBit i = true) :
    (n - 2^i).testBit i = false
```

`CompPoly.CMlPolynomial.lagrangeToMonoLevel_monoToLagrangeLevel_id` (theorem, [line 1008](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L1008))

```lean
theorem lagrangeToMonoLevel_monoToLagrangeLevel_id (v : Vector R (2 ^ n)) (i : Fin n) :
    lagrangeToMonoLevel i (monoToLagrangeLevel i v) = v
```

`CompPoly.CMlPolynomial.monoToLagrangeLevel_lagrangeToMonoLevel_id` (theorem, [line 1028](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L1028))

```lean
theorem monoToLagrangeLevel_lagrangeToMonoLevel_id (v : Vector R (2 ^ n)) (i : Fin n) :
    monoToLagrangeLevel i (lagrangeToMonoLevel i v) = v
```

`CompPoly.CMlPolynomial.mobius_apply_zeta_apply_eq_id` (theorem, [line 1046](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L1046))

```lean
theorem mobius_apply_zeta_apply_eq_id (n : ℕ) [NeZero n] (r : Fin n) (l : Fin (r.val + 1))
    (v : Vector R (2 ^ n)) : lagrangeToMonoSegment n r l (monoToLagrangeSegment n r l v) = v
```

`CompPoly.CMlPolynomial.zeta_apply_mobius_apply_eq_id` (lemma, [line 1090](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L1090))

```lean
lemma zeta_apply_mobius_apply_eq_id (n : ℕ) (r : Fin n) (l : Fin (r.val + 1))
    (v : Vector R (2 ^ n)) :
    monoToLagrangeSegment n r l (lagrangeToMonoSegment n r l v) = v
```

`CompPoly.CMlPolynomial.equivMonomialLagrangeRepr` (definition, [line 1130](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean#L1130))

> The equivalence between the monomial basis representation (`CMlPolynomial`)
> and the Lagrange basis representation (`CMlPolynomialEval`) of a multilinear polynomial.
> The forward map is `monoToLagrange` (zeta transform) and the inverse is `lagrangeToMono`
> (inverse zeta transform/Mobius transform).

```lean
def equivMonomialLagrangeRepr : CMlPolynomial R n ≃ CMlPolynomialEval R n
```

> ### #eval Tests
>
> This section contains tests to verify the functionality of multilinear polynomial operations.

## Depends on

- [Bit operations on natural numbers](../data/nat/bitwise.md)
- [Definitions and lemmas for `Vector`](../data/vector/basic.md)

## Sources

- [CompPoly/Multilinear/Basic.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/Basic.lean)
- [Declaration ledger](../../../sources/comppoly/CompPoly.Multilinear.Basic.json)
