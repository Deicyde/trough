---
catalog: module
lean: MvPolynomial.finSuccEquivNth, MvPolynomial.finSuccEquivNth_eq, MvPolynomial.finSuccEquivNth_apply, MvPolynomial.finSuccEquivNth_comp_C_eq_C, MvPolynomial.finSuccEquivNth_X_same, MvPolynomial.finSuccEquivNth_X_above, MvPolynomial.finSuccEquivNth_X_below, MvPolynomial.finSuccEquivNth_coeff_coeff, MvPolynomial.eval_eq_eval_mv_eval_finSuccEquivNth, MvPolynomial.support_coeff_finSuccEquivNth, MvPolynomial.totalDegree_coeff_finSuccEquivNth_add_le, MvPolynomial.support_finSuccEquivNth, MvPolynomial.mem_support_finSuccEquivNth, MvPolynomial.image_support_finSuccEquivNth, MvPolynomial.mem_image_support_coeff_finSuccEquivNth, MvPolynomial.mem_support_coeff_finSuccEquivNth, MvPolynomial.support_finSuccEquivNth_nonempty, MvPolynomial.degree_finSuccEquivNth, MvPolynomial.natDegree_finSuccEquivNth, MvPolynomial.degreeOf_coeff_finSuccEquivNth, MvPolynomial.finSuccEquivNth_rename_finSuccEquivNth
statement: formalized
proof: formalized
---

# MvPolynomial Equiv

`CompPoly.ToMathlib.MvPolynomial.Equiv`, in [CompPoly/ToMathlib/MvPolynomial/Equiv.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/MvPolynomial/Equiv.lean), by Chung Thai Nguyen, Quang Dao.

> Equivalences for multivariable polynomials, including `finSuccEquivNth`.

`MvPolynomial.finSuccEquivNth` (definition, [line 33](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/MvPolynomial/Equiv.lean#L33))

> The algebra isomorphism between multivariable polynomials in `Fin (n + 1)` and polynomials over
> multivariable polynomials in `Fin n`, where the `p`-th (pivot) variable is the indeterminate `X`.
>
> `finSuccEquiv` is the special case when `p = 0`.

```lean
def finSuccEquivNth : MvPolynomial (Fin (n + 1)) R ≃ₐ[R] Polynomial (MvPolynomial (Fin n) R)
```

`MvPolynomial.finSuccEquivNth_eq` (theorem, [line 36](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/MvPolynomial/Equiv.lean#L36))

```lean
theorem finSuccEquivNth_eq :
    (finSuccEquivNth R p : MvPolynomial (Fin (n + 1)) R →+* Polynomial (MvPolynomial (Fin n) R)) =
      eval₂Hom (Polynomial.C.comp (C : R →+* MvPolynomial (Fin n) R))
        (Fin.insertNth p Polynomial.X (Polynomial.C ∘ X))
```

`MvPolynomial.finSuccEquivNth_apply` (theorem, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/MvPolynomial/Equiv.lean#L46))

```lean
theorem finSuccEquivNth_apply (f : MvPolynomial (Fin (n + 1)) R) :
    finSuccEquivNth R p f =
      eval₂Hom (Polynomial.C.comp (C : R →+* MvPolynomial (Fin n) R))
        (Fin.insertNth p Polynomial.X (Polynomial.C ∘ X)) f
```

`MvPolynomial.finSuccEquivNth_comp_C_eq_C` (theorem, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/MvPolynomial/Equiv.lean#L52))

```lean
theorem finSuccEquivNth_comp_C_eq_C :
    (↑(finSuccEquivNth R p).symm : Polynomial (MvPolynomial (Fin n) R) →+* _).comp
        (Polynomial.C.comp C) = (C : R →+* MvPolynomial (Fin n.succ) R)
```

`MvPolynomial.finSuccEquivNth_X_same` (theorem, [line 65](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/MvPolynomial/Equiv.lean#L65))

```lean
theorem finSuccEquivNth_X_same : finSuccEquivNth R p (X p) = Polynomial.X
```

`MvPolynomial.finSuccEquivNth_X_above` (theorem, [line 69](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/MvPolynomial/Equiv.lean#L69))

```lean
theorem finSuccEquivNth_X_above {i : Fin n} (h : p < i.succ) :
    finSuccEquivNth R p (X i.succ) = Polynomial.C (X i)
```

`MvPolynomial.finSuccEquivNth_X_below` (theorem, [line 74](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/MvPolynomial/Equiv.lean#L74))

```lean
theorem finSuccEquivNth_X_below {i : Fin n} (h : i.castSucc < p) :
    finSuccEquivNth R p (X i.castSucc) = Polynomial.C (X i)
```

`MvPolynomial.finSuccEquivNth_coeff_coeff` (theorem, [line 81](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/MvPolynomial/Equiv.lean#L81))

> The coefficient of `m` in the `i`-th coefficient of `finSuccEquivNth R p f` equals the
> coefficient of `m.insertNth p i` in `f`.

```lean
theorem finSuccEquivNth_coeff_coeff (m : Fin n →₀ ℕ) (f : MvPolynomial (Fin (n + 1)) R) (i : ℕ) :
    ((finSuccEquivNth R p f).coeff i).coeff m = f.coeff (m.insertNth p i)
```

`MvPolynomial.eval_eq_eval_mv_eval_finSuccEquivNth` (theorem, [line 110](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/MvPolynomial/Equiv.lean#L110))

> The evaluation of `f` at `Fin.insertNth p y s` equals the evaluation at `y` of the polynomial
> obtained by partially evaluating `finSuccEquivNth R p f` at `s`.

```lean
theorem eval_eq_eval_mv_eval_finSuccEquivNth (s : Fin n → R) (y : R)
    (f : MvPolynomial (Fin (n + 1)) R) :
      eval (Fin.insertNth p y s : Fin (n + 1) → R) f =
        Polynomial.eval y (Polynomial.map (eval s) (finSuccEquivNth R p f))
```

`MvPolynomial.support_coeff_finSuccEquivNth` (theorem, [line 128](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/MvPolynomial/Equiv.lean#L128))

> A monomial index `m` is in the support of the `i`-th coefficient of `finSuccEquivNth R p f` if
> and only if `m.insertNth p i` is in the support of `f`.

```lean
theorem support_coeff_finSuccEquivNth {f : MvPolynomial (Fin (n + 1)) R} {i : ℕ} {m : Fin n →₀ ℕ} :
    m ∈ ((finSuccEquivNth R p f).coeff i).support ↔ m.insertNth p i ∈ f.support
```

`MvPolynomial.totalDegree_coeff_finSuccEquivNth_add_le` (theorem, [line 138](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/MvPolynomial/Equiv.lean#L138))

> The `totalDegree` of a multivariable polynomial `f` is at least `i` more than the `totalDegree` of
> the `i`th coefficient of `finSuccEquivNth R p` applied to `f`, if this is nonzero.

```lean
theorem totalDegree_coeff_finSuccEquivNth_add_le (f : MvPolynomial (Fin (n + 1)) R) (i : ℕ)
    (hi : (finSuccEquivNth R p f).coeff i ≠ 0) :
      totalDegree ((finSuccEquivNth R p f).coeff i) + i ≤ totalDegree f
```

`MvPolynomial.support_finSuccEquivNth` (theorem, [line 155](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/MvPolynomial/Equiv.lean#L155))

> The support of `finSuccEquivNth R p f` equals the support of `f` projected onto the `p`-th
> variable.

```lean
theorem support_finSuccEquivNth (f : MvPolynomial (Fin (n + 1)) R) :
    (finSuccEquivNth R p f).support = Finset.image (fun m : Fin (n + 1) →₀ ℕ => m p) f.support
```

`MvPolynomial.mem_support_finSuccEquivNth` (theorem, [line 166](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/MvPolynomial/Equiv.lean#L166))

```lean
theorem mem_support_finSuccEquivNth {f : MvPolynomial (Fin (n + 1)) R} {x} :
    x ∈ (finSuccEquivNth R p f).support ↔ x ∈ (fun m : Fin (n + 1) →₀ _ ↦ m p) '' f.support
```

`MvPolynomial.image_support_finSuccEquivNth` (theorem, [line 170](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/MvPolynomial/Equiv.lean#L170))

```lean
theorem image_support_finSuccEquivNth {f : MvPolynomial (Fin (n + 1)) R} {i : ℕ} :
    Finset.image (Finsupp.insertNth p i) ((finSuccEquivNth R p f).coeff i).support =
      f.support.filter fun m => m p = i
```

`MvPolynomial.mem_image_support_coeff_finSuccEquivNth` (lemma, [line 188](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/MvPolynomial/Equiv.lean#L188))

```lean
lemma mem_image_support_coeff_finSuccEquivNth {f : MvPolynomial (Fin (n + 1)) R} {i : ℕ} {x} :
    x ∈ Finsupp.insertNth p i '' ((finSuccEquivNth R p f).coeff i).support ↔
      x ∈ f.support ∧ x p = i
```

`MvPolynomial.mem_support_coeff_finSuccEquivNth` (lemma, [line 193](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/MvPolynomial/Equiv.lean#L193))

```lean
lemma mem_support_coeff_finSuccEquivNth {f : MvPolynomial (Fin (n + 1)) R} {i : ℕ} {x} :
    x ∈ ((finSuccEquivNth R p f).coeff i).support ↔ x.insertNth p i ∈ f.support
```

`MvPolynomial.support_finSuccEquivNth_nonempty` (theorem, [line 199](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/MvPolynomial/Equiv.lean#L199))

```lean
theorem support_finSuccEquivNth_nonempty {f : MvPolynomial (Fin (n + 1)) R} (h : f ≠ 0) :
    (finSuccEquivNth R p f).support.Nonempty
```

`MvPolynomial.degree_finSuccEquivNth` (theorem, [line 204](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/MvPolynomial/Equiv.lean#L204))

> The degree of `finSuccEquivNth R p f` equals the `p`-th degree of `f`.

```lean
theorem degree_finSuccEquivNth {f : MvPolynomial (Fin (n + 1)) R} (h : f ≠ 0) :
    (finSuccEquivNth R p f).degree = degreeOf p f
```

`MvPolynomial.natDegree_finSuccEquivNth` (theorem, [line 214](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/MvPolynomial/Equiv.lean#L214))

> The `natDegree` of `finSuccEquivNth R p f` equals the `p`-th `natDegree` of `f`.

```lean
theorem natDegree_finSuccEquivNth (f : MvPolynomial (Fin (n + 1)) R) :
    (finSuccEquivNth R p f).natDegree = degreeOf p f
```

`MvPolynomial.degreeOf_coeff_finSuccEquivNth` (theorem, [line 223](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/MvPolynomial/Equiv.lean#L223))

> The degree of `j` in the `i`th coefficient of `finSuccEquivNth R p f` is at most the degree of
> `j.succ` in `f`.

```lean
theorem degreeOf_coeff_finSuccEquivNth (f : MvPolynomial (Fin (n + 1)) R) (j : Fin n) (i : ℕ) :
    degreeOf j ((finSuccEquivNth R p f).coeff i) ≤ degreeOf (p.succAbove j) f
```

`MvPolynomial.finSuccEquivNth_rename_finSuccEquivNth` (theorem, [line 241](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/MvPolynomial/Equiv.lean#L241))

> Consider a multivariate polynomial `φ` whose variables are indexed by `Option σ`,
> and suppose that `σ ≃ Fin n`.
> Then one may view `φ` as a polynomial over `MvPolynomial (Fin n) R`, by
>
> 1. renaming the variables via `Option σ ≃ Fin (n+1)`, and then singling out the `p`-th variable
>     via `MvPolynomial.finSuccEquivNth R p`;
> 2. first viewing it as polynomial over `MvPolynomial σ R` via `MvPolynomial.optionEquivLeft`,
>     and then renaming the variables.
>
> This theorem shows that both constructions are the same.

```lean
theorem finSuccEquivNth_rename_finSuccEquivNth (e : σ ≃ Fin n) (φ : MvPolynomial (Option σ) R) :
    ((finSuccEquivNth R p) ((rename ((Equiv.optionCongr e).trans (_root_.finSuccEquiv' p).symm)) φ))
      = Polynomial.map (rename e).toRingHom (optionEquivLeft R σ φ)
```

## Depends on

- [Tuple operations on maps `Fin n →₀ M`](../finsupp/fin.md)

## Sources

- [CompPoly/ToMathlib/MvPolynomial/Equiv.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/ToMathlib/MvPolynomial/Equiv.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.ToMathlib.MvPolynomial.Equiv.json)
