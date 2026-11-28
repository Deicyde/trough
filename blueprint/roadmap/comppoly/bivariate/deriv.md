---
catalog: module
lean: CompPoly.CBivariate.partialDerivX, CompPoly.CBivariate.partialDerivY, CompPoly.CBivariate.outerCoeff_support_monomial, CompPoly.CBivariate.outerCoeff_partialDerivX, CompPoly.CBivariate.coeff_partialDerivX, CompPoly.CBivariate.coeff_partialDerivY, CompPoly.CBivariate.partialDerivX_zero, CompPoly.CBivariate.partialDerivY_zero, CompPoly.CBivariate.partialDerivX_add, CompPoly.CBivariate.partialDerivY_add, CompPoly.CBivariate.partialDerivX_toPoly, CompPoly.CBivariate.partialDerivY_toPoly, CompPoly.CBivariate.partialDerivY_mul, CompPoly.CBivariate.partialDerivX_mul, CompPoly.CBivariate.iterPartialDerivX, CompPoly.CBivariate.iterPartialDerivY, CompPoly.CBivariate.iterPartialDerivX_toPoly, CompPoly.CBivariate.iterPartialDerivY_toPoly, CompPoly.CBivariate.mixedPartialDeriv, CompPoly.CBivariate.partialDerivX_partialDerivY_comm, CompPoly.CBivariate.mixedPartials_comm, CompPoly.CBivariate.shiftY, CompPoly.CBivariate.shiftX, CompPoly.CBivariate.shiftC, CompPoly.CBivariate.hasMultiplicity, CompPoly.CBivariate.checkMultiplicity, CompPoly.CBivariate.shiftY_toPoly, CompPoly.CBivariate.outerCoeff_shiftX, CompPoly.CBivariate.shiftX_toPoly, CompPoly.CBivariate.shiftC_toPoly, CompPoly.CBivariate.eval_C_eq_evalY, CompPoly.CBivariate.coeff_shiftC_zero_zero, CompPoly.CBivariate.hasMultiplicity_one_iff, CompPoly.CBivariate.hasMultiplicity_iff_rootMultiplicity, CompPoly.CBivariate.hasMultiplicity_zero, CompPoly.CBivariate.hasMultiplicity_succ, CompPoly.CBivariate.toPoly_injective, CompPoly.CBivariate.shiftC_add, CompPoly.CBivariate.shiftC_mul, CompPoly.CBivariate.hasMultiplicity_iff_check
statement: formalized
proof: formalized
---

# Partial Derivatives and Multiplicity of Computable Bivariate Polynomials

`CompPoly.Bivariate.Deriv`, in [CompPoly/Bivariate/Deriv.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean), by Dimitris Mitsios.

> This file defines partial derivatives (`partialDerivX`, `partialDerivY`, iterated
> and mixed partials) and the multiplicity condition `hasMultiplicity` used in the
> Guruswami–Sudan interpolation step.
>
> Multiplicity of a root at `(a, b)` is defined through the Taylor shift
> `shiftC a b Q = Q(X + a, Y + b)`. `Q` has multiplicity at least `r` at `(a, b)`
> when every coefficient of the shifted polynomial of total degree less than `r`
> is zero. This is the Hasse-derivative criterion for root multiplicity over a field
> of any characteristic: the coefficient of `Xⁱ Yʲ` in `shiftC a b Q` is the
> order-`(i, j)` Hasse derivative of `Q` evaluated at `(a, b)`. The zero polynomial
> has infinite multiplicity. As an aside, ordinary partial derivatives fail to capture
> this in positive characteristic. The integer factor introduced by differentiation can
> vanish, so its product with a nonzero coefficient may become zero.
>
> `shiftC_toPoly` identifies the computable shift with Mathlib's
> `Polynomial.Bivariate.shift`, and `hasMultiplicity_iff_rootMultiplicity` proves
> that `hasMultiplicity` agrees with the reference `Polynomial.Bivariate.rootMultiplicity`.

`CompPoly.CBivariate.partialDerivX` (definition, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L46))

> Partial derivative with respect to X: differentiate each Y-coefficient in X.

```lean
def partialDerivX [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (f : CBivariate R) : CBivariate R
```

`CompPoly.CBivariate.partialDerivY` (definition, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L52))

> Partial derivative with respect to Y: differentiate in the outer variable.

```lean
def partialDerivY [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (f : CBivariate R) : CBivariate R
```

`CompPoly.CBivariate.outerCoeff_support_monomial` (theorem, [line 58](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L58))

> Outer coefficient of a `support`-sum of monomials whose `Y`-coefficients are mapped by a
> zero-preserving `g`: the `j`-th coefficient is `g` applied to the `j`-th `Y`-coefficient.

```lean
theorem outerCoeff_support_monomial [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    [DecidableEq R] (f : CBivariate R) (g : CPolynomial R → CPolynomial R) (hg : g 0 = 0) (j : ℕ) :
    CPolynomial.coeff ((CPolynomial.support f).sum fun k =>
      CPolynomial.monomial k (g (f.val.coeff k))) j = g (CPolynomial.coeff f j)
```

`CompPoly.CBivariate.outerCoeff_partialDerivX` (theorem, [line 74](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L74))

> Outer coefficient of the X-partial derivative: differentiate the j-th Y-coefficient.

```lean
theorem outerCoeff_partialDerivX [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (f : CBivariate R) (j : ℕ) :
    CPolynomial.coeff (partialDerivX f) j =
      CPolynomial.derivative (CPolynomial.coeff f j)
```

`CompPoly.CBivariate.coeff_partialDerivX` (theorem, [line 81](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L81))

> Coefficient formula for the X-partial derivative.

```lean
theorem coeff_partialDerivX [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (f : CBivariate R) (i j : ℕ) :
    CBivariate.coeff (partialDerivX f) i j =
      CBivariate.coeff f (i + 1) j * (↑(i + 1) : R)
```

`CompPoly.CBivariate.coeff_partialDerivY` (theorem, [line 88](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L88))

> Coefficient formula for the Y-partial derivative.

```lean
theorem coeff_partialDerivY [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (f : CBivariate R) (i j : ℕ) :
    CBivariate.coeff (partialDerivY f) i j =
      CBivariate.coeff f i (j + 1) * (↑(j + 1) : R)
```

`CompPoly.CBivariate.partialDerivX_zero` (theorem, [line 99](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L99))

> The X-partial derivative of zero is zero.

```lean
theorem partialDerivX_zero [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R] :
    partialDerivX (0 : CBivariate R) = 0
```

`CompPoly.CBivariate.partialDerivY_zero` (theorem, [line 112](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L112))

> The Y-partial derivative of zero is zero.

```lean
theorem partialDerivY_zero [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] :
    partialDerivY (0 : CBivariate R) = 0
```

`CompPoly.CBivariate.partialDerivX_add` (theorem, [line 118](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L118))

> The X-partial derivative distributes over addition.

```lean
theorem partialDerivX_add [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (f g : CBivariate R) :
    partialDerivX (f + g) = partialDerivX f + partialDerivX g
```

`CompPoly.CBivariate.partialDerivY_add` (theorem, [line 132](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L132))

> The Y-partial derivative distributes over addition.

```lean
theorem partialDerivY_add [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (f g : CBivariate R) :
    partialDerivY (f + g) = partialDerivY f + partialDerivY g
```

`CompPoly.CBivariate.partialDerivX_toPoly` (theorem, [line 139](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L139))

> The X-partial derivative differentiates each Y-coefficient under `toPoly`.

```lean
theorem partialDerivX_toPoly [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (f : CBivariate R) (j : ℕ) :
    (toPoly (partialDerivX f)).coeff j =
      Polynomial.derivative ((toPoly f).coeff j)
```

`CompPoly.CBivariate.partialDerivY_toPoly` (theorem, [line 147](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L147))

> The Y-partial derivative corresponds to `Polynomial.derivative` under `toPoly`.

```lean
theorem partialDerivY_toPoly [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (f : CBivariate R) :
    toPoly (partialDerivY f) = Polynomial.derivative (toPoly f)
```

`CompPoly.CBivariate.partialDerivY_mul` (theorem, [line 156](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L156))

> The Y-partial derivative satisfies the Leibniz product rule.

```lean
theorem partialDerivY_mul [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (f g : CBivariate R) :
    partialDerivY (f * g) = partialDerivY f * g + f * partialDerivY g
```

`CompPoly.CBivariate.partialDerivX_mul` (theorem, [line 163](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L163))

> The X-partial derivative satisfies the Leibniz product rule.

```lean
theorem partialDerivX_mul [CommSemiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (f g : CBivariate R) :
    partialDerivX (f * g) = partialDerivX f * g + f * partialDerivX g
```

`CompPoly.CBivariate.iterPartialDerivX` (definition, [line 177](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L177))

> Iterated partial derivative with respect to X.

```lean
def iterPartialDerivX [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (n : ℕ) (f : CBivariate R) : CBivariate R
```

`CompPoly.CBivariate.iterPartialDerivY` (definition, [line 182](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L182))

> Iterated partial derivative with respect to Y.

```lean
def iterPartialDerivY [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (n : ℕ) (f : CBivariate R) : CBivariate R
```

`CompPoly.CBivariate.iterPartialDerivX_toPoly` (theorem, [line 187](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L187))

> Iterated X-partial derivative differentiates each Y-coefficient under `toPoly`.

```lean
theorem iterPartialDerivX_toPoly [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (n : ℕ) (f : CBivariate R) (j : ℕ) :
    (toPoly (iterPartialDerivX n f)).coeff j =
      Polynomial.derivative^[n] ((toPoly f).coeff j)
```

`CompPoly.CBivariate.iterPartialDerivY_toPoly` (theorem, [line 198](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L198))

> Iterated Y-partial derivative corresponds to `Polynomial.derivative^[n]` under `toPoly`.

```lean
theorem iterPartialDerivY_toPoly [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (n : ℕ) (f : CBivariate R) :
    toPoly (iterPartialDerivY n f) = Polynomial.derivative^[n] (toPoly f)
```

`CompPoly.CBivariate.mixedPartialDeriv` (definition, [line 208](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L208))

> Mixed partial derivative: i-fold in X, then j-fold in Y.

```lean
def mixedPartialDeriv [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (i j : ℕ) (f : CBivariate R) : CBivariate R
```

`CompPoly.CBivariate.partialDerivX_partialDerivY_comm` (theorem, [line 213](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L213))

> X and Y partial derivatives commute.

```lean
theorem partialDerivX_partialDerivY_comm [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    [DecidableEq R] (f : CBivariate R) :
    partialDerivX (partialDerivY f) = partialDerivY (partialDerivX f)
```

`CompPoly.CBivariate.mixedPartials_comm` (theorem, [line 226](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L226))

> Mixed partial derivatives commute.

```lean
theorem mixedPartials_comm [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (i j : ℕ) (f : CBivariate R) :
    iterPartialDerivX i (iterPartialDerivY j f) =
      iterPartialDerivY j (iterPartialDerivX i f)
```

`CompPoly.CBivariate.shiftY` (definition, [line 234](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L234))

> Shift the outer `Y` variable: `Q(X, Y + b)`.

```lean
def shiftY [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (b : R) (Q : CBivariate R) : CBivariate R
```

`CompPoly.CBivariate.shiftX` (definition, [line 239](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L239))

> Shift the inner `X` variable: `Q(X + a, Y)`, Taylor-shifting each `Y`-coefficient.

```lean
def shiftX [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (a : R) (Q : CBivariate R) : CBivariate R
```

`CompPoly.CBivariate.shiftC` (definition, [line 245](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L245))

> The full shift `Q(X + a, Y + b)`.

```lean
def shiftC [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (a b : R) (Q : CBivariate R) : CBivariate R
```

`CompPoly.CBivariate.hasMultiplicity` (definition, [line 252](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L252))

> `Q` has multiplicity at least `r` at `(a, b)`: every coefficient of the shifted
> polynomial `Q(X + a, Y + b)` of total degree `< r` vanishes.

```lean
def hasMultiplicity [CommSemiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (Q : CBivariate R) (r : ℕ) (a b : R) : Prop
```

`CompPoly.CBivariate.checkMultiplicity` (definition, [line 257](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L257))

> Decidable check for multiplicity.

```lean
def checkMultiplicity [CommSemiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (Q : CBivariate R) (r : ℕ) (a b : R) : Bool
```

`CompPoly.CBivariate.shiftY_toPoly` (theorem, [line 264](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L264))

> The outer (Y) shift corresponds to `Y ↦ Y + b` under `toPoly`.

```lean
theorem shiftY_toPoly [CommSemiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (b : R) (Q : CBivariate R) :
    (shiftY b Q).toPoly = (Q.toPoly).comp (Polynomial.X + Polynomial.C (Polynomial.C b))
```

`CompPoly.CBivariate.outerCoeff_shiftX` (theorem, [line 281](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L281))

> Outer coefficient of the X-shift: Taylor-shift the j-th Y-coefficient.

```lean
theorem outerCoeff_shiftX [CommSemiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (a : R) (P : CBivariate R) (j : ℕ) :
    CPolynomial.coeff (shiftX a P) j = CPolynomial.taylor a (CPolynomial.coeff P j)
```

`CompPoly.CBivariate.shiftX_toPoly` (theorem, [line 287](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L287))

> The inner (X) shift corresponds to `X ↦ X + a` under `toPoly`.

```lean
theorem shiftX_toPoly [CommSemiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (a : R) (P : CBivariate R) :
    (shiftX a P).toPoly
      = (P.toPoly).map (Polynomial.compRingHom (Polynomial.X + Polynomial.C a))
```

`CompPoly.CBivariate.shiftC_toPoly` (theorem, [line 296](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L296))

> The computable shift agrees with `Polynomial.Bivariate.shift` under `toPoly`.

```lean
theorem shiftC_toPoly [CommSemiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (a b : R) (Q : CBivariate R) :
    (shiftC a b Q).toPoly = Polynomial.Bivariate.shift Q.toPoly a b
```

`CompPoly.CBivariate.eval_C_eq_evalY` (theorem, [line 304](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L304))

> Evaluating the outer variable at the constant `C b` agrees with the Horner evaluator `evalY`.

```lean
theorem eval_C_eq_evalY [CommSemiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (b : R) (Q : CBivariate R) :
    CPolynomial.eval (CPolynomial.C b) Q = evalY b Q
```

`CompPoly.CBivariate.coeff_shiftC_zero_zero` (theorem, [line 324](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L324))

> The (0,0) coefficient of the shift is evaluation at the point.

```lean
theorem coeff_shiftC_zero_zero [CommSemiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (a b : R) (Q : CBivariate R) :
    CBivariate.coeff (shiftC a b Q) 0 0 = evalEval a b Q
```

`CompPoly.CBivariate.hasMultiplicity_one_iff` (theorem, [line 336](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L336))

> Multiplicity at least 1 is equivalent to vanishing at the point.

```lean
theorem hasMultiplicity_one_iff [CommSemiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    [DecidableEq R] (Q : CBivariate R) (a b : R) :
    hasMultiplicity Q 1 a b ↔ evalEval a b Q = 0
```

`CompPoly.CBivariate.hasMultiplicity_iff_rootMultiplicity` (theorem, [line 348](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L348))

> `hasMultiplicity` agrees with the reference `Polynomial.Bivariate.rootMultiplicity`,
> where `none` denotes infinite multiplicity (the zero polynomial).

```lean
theorem hasMultiplicity_iff_rootMultiplicity [CommSemiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    [DecidableEq R] (Q : CBivariate R) (r : ℕ) (a b : R) :
    hasMultiplicity Q r a b ↔
      ∀ m ∈ Polynomial.Bivariate.rootMultiplicity Q.toPoly a b, r ≤ m
```

`CompPoly.CBivariate.hasMultiplicity_zero` (theorem, [line 360](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L360))

> Every polynomial has multiplicity at least 0 at any point.

```lean
theorem hasMultiplicity_zero [CommSemiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    [DecidableEq R] (Q : CBivariate R) (a b : R) :
    hasMultiplicity Q 0 a b
```

`CompPoly.CBivariate.hasMultiplicity_succ` (theorem, [line 366](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L366))

> Multiplicity is monotone: higher multiplicity implies lower.

```lean
theorem hasMultiplicity_succ [CommSemiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    [DecidableEq R] (Q : CBivariate R) (r : ℕ) (a b : R) :
    hasMultiplicity Q (r + 1) a b → hasMultiplicity Q r a b
```

`CompPoly.CBivariate.toPoly_injective` (theorem, [line 373](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L373))

> `toPoly` is injective on canonical bivariate polynomials.

```lean
theorem toPoly_injective [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    [DecidableEq R] {P Q : CBivariate R} (h : toPoly P = toPoly Q) : P = Q
```

`CompPoly.CBivariate.shiftC_add` (theorem, [line 378](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L378))

> The generic Taylor shift is additive.

```lean
theorem shiftC_add [CommSemiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (a b : R) (P Q : CBivariate R) :
    shiftC a b (P + Q) = shiftC a b P + shiftC a b Q
```

`CompPoly.CBivariate.shiftC_mul` (theorem, [line 387](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L387))

> The generic Taylor shift is multiplicative.

```lean
theorem shiftC_mul [CommSemiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    [DecidableEq R] (a b : R) (P Q : CBivariate R) :
    shiftC a b (P * Q) = shiftC a b P * shiftC a b Q
```

`CompPoly.CBivariate.hasMultiplicity_iff_check` (theorem, [line 396](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean#L396))

> The decidable check agrees with the propositional multiplicity.

```lean
theorem hasMultiplicity_iff_check [CommSemiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    [DecidableEq R] (Q : CBivariate R) (r : ℕ) (a b : R) :
    hasMultiplicity Q r a b ↔ checkMultiplicity Q r a b = true
```

## Depends on

- [Mathlib-Facing Bivariate Multiplicity Helpers](../tomathlib/polynomial/bivariatemultiplicity.md)
- [Formal Derivative and Taylor Shift of Computable Univariate Polynomials](../univariate/part-01/deriv.md)

## Sources

- [CompPoly/Bivariate/Deriv.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/Deriv.lean)
- [Declaration ledger](../../../sources/comppoly/CompPoly.Bivariate.Deriv.json)
