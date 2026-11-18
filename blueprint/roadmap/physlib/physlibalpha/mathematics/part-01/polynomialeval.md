---
declaration: module
origin: cited
lean: Polynomial.eq_zero_of_forall_eval_algebraMap_eq_zero, Polynomial.ext_of_forall_eval_algebraMap, Polynomial.mapCoeffs, Polynomial.coeff_mapCoeffs, Polynomial.mapCoeffs_zero, Polynomial.mapCoeffs_monomial, Polynomial.mapCoeffs_add, Polynomial.eval_algebraMap_mapAlgHom
statement: formalized
proof: formalized
---

# Polynomials with coefficients in an algebra

The module `PhyslibAlpha.Mathematics.PolynomialEval`, [PhyslibAlpha/Mathematics/PolynomialEval.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PolynomialEval.lean): 11 declarations, 7 with a docstring.

## i. Overview

> A polynomial whose coefficients lie in a `k`-algebra `A` can be evaluated at the image
> `algebraMap k A c` of a scalar. This file records that such a polynomial is determined by
> those evaluations alone, when `k` is an infinite field, and defines the polynomial obtained
> by applying a `k`-linear map to every coefficient.
>
> Both are used to transport grading statements between two equivalent descriptions of a
> grading on a jet algebra: the *mass-weight polynomial*, whose `X ^ n` coefficient is the
> weight-`n` part of an element, and the *mass-weight scaling*, the algebra map scaling each
> weight-`n` part by `c ^ n`. The scaling is the evaluation of the polynomial, so a statement
> about one transfers to the other.
>
> The determinacy is not an instance of `Polynomial.funext`: the coefficient ring `A` is
> neither commutative nor a domain in the intended applications. It holds because `A` is a
> `k`-vector space, so its elements are separated by linear functionals, and a polynomial over
> the infinite field `k` is determined by its values.

## ii. Key results

> - `Polynomial.eq_zero_of_forall_eval_algebraMap_eq_zero` : a polynomial vanishing at every
>   scalar is zero.
> - `Polynomial.ext_of_forall_eval_algebraMap` : two polynomials agreeing at every scalar are
>   equal.
> - `Polynomial.mapCoeffs` : apply a linear map to every coefficient.
> - `Polynomial.eval_algebraMap_mapCoeffs` : evaluation commutes with `mapCoeffs`.

## iv. References

> * None.

## A. Determinacy by evaluation at scalars

**`Polynomial.eq_zero_of_forall_eval_algebraMap_eq_zero`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PolynomialEval.lean#L65).

> A polynomial with coefficients in an algebra over an infinite field vanishes as soon as
> it vanishes at the image of every scalar. Linear functionals separate the coefficients,
> and over an infinite field a polynomial is determined by its values.

```lean
lemma eq_zero_of_forall_eval_algebraMap_eq_zero {k A : Type*} [Field k] [Infinite k]
    [Ring A] [Algebra k A] {p : Polynomial A}
    (h : ∀ c : k, p.eval (algebraMap k A c) = 0) : p = 0
```

**`Polynomial.ext_of_forall_eval_algebraMap`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PolynomialEval.lean#L93).

> Two polynomials with coefficients in an algebra over an infinite field are equal as soon
> as they agree at the image of every scalar.

```lean
lemma ext_of_forall_eval_algebraMap {k A : Type*} [Field k] [Infinite k]
    [Ring A] [Algebra k A] {p q : Polynomial A}
    (h : ∀ c : k, p.eval (algebraMap k A c) = q.eval (algebraMap k A c)) : p = q
```

## B. Applying a linear map to the coefficients

**`Polynomial.mapCoeffs`**, a def, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PolynomialEval.lean#L113).

> The polynomial obtained by applying a function to every coefficient. Unlike
> `Polynomial.map` this needs no multiplicativity, so it applies to derivations.
>
> The argument is a bare function rather than a linear map: on an algebra built as a tensor
> product the module structure coming from the algebra and the one coming from the tensor
> product are equal but not syntactically so, and bundling would force the caller to
> reconcile them. The properties needed are taken as hypotheses instead.

```lean
noncomputable def mapCoeffs {A : Type*} [Semiring A] (f : A → A) (p : Polynomial A) :
    Polynomial A
```

**`Polynomial.coeff_mapCoeffs`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PolynomialEval.lean#L117).

```lean
lemma coeff_mapCoeffs {A : Type*} [Semiring A] {f : A → A} (hf0 : f 0 = 0)
    (p : Polynomial A) (n : ℕ) : (mapCoeffs f p).coeff n = f (p.coeff n)
```

**`Polynomial.mapCoeffs_zero`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PolynomialEval.lean#L127).

```lean
lemma mapCoeffs_zero {A : Type*} [Semiring A] (f : A → A) : mapCoeffs f 0 = 0
```

**`Polynomial.mapCoeffs_monomial`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PolynomialEval.lean#L130).

```lean
lemma mapCoeffs_monomial {A : Type*} [Semiring A] {f : A → A} (hf0 : f 0 = 0)
    (n : ℕ) (a : A) :
    mapCoeffs f (Polynomial.monomial n a) = Polynomial.monomial n (f a)
```

**`Polynomial.mapCoeffs_add`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PolynomialEval.lean#L139).

```lean
lemma mapCoeffs_add {A : Type*} [Semiring A] {f : A → A} (hf0 : f 0 = 0)
    (hadd : ∀ a b : A, f (a + b) = f a + f b) (p q : Polynomial A) :
    mapCoeffs f (p + q) = mapCoeffs f p + mapCoeffs f q
```

**`Polynomial.eval_algebraMap_mapAlgHom`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PolynomialEval.lean#L148).

> Evaluation at a scalar commutes with pushing a polynomial along an algebra map: an
> algebra map fixes the scalars.

```lean
lemma eval_algebraMap_mapAlgHom {k A B : Type*} [CommSemiring k] [Semiring A] [Semiring B]
    [Algebra k A] [Algebra k B] (f : A →ₐ[k] B) (p : Polynomial A) (c : k) :
    (Polynomial.mapAlgHom f p).eval (algebraMap k B c) = f (p.eval (algebraMap k A c))
```

**`Polynomial.eval_algebraMap_mapCoeffs`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PolynomialEval.lean#L162).

> Evaluation at a scalar commutes with applying a linear map to the coefficients: the
> powers of the scalar are central, so they pass through the linear map.

```lean
lemma eval_algebraMap_mapCoeffs {k A : Type*} [Field k] [Ring A] [Algebra k A]
    (f : A →ₗ[k] A) (p : Polynomial A) (c : k) :
    (mapCoeffs f p).eval (algebraMap k A c) = f (p.eval (algebraMap k A c))
```

**`Polynomial.eval_one_mapAlgHom`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PolynomialEval.lean#L176).

> Evaluation at one commutes with pushing a polynomial along an algebra map.

```lean
lemma eval_one_mapAlgHom {k A B : Type*} [CommSemiring k] [Semiring A] [Semiring B]
    [Algebra k A] [Algebra k B] (f : A →ₐ[k] B) (p : Polynomial A) :
    (Polynomial.mapAlgHom f p).eval 1 = f (p.eval 1)
```

**`Polynomial.mapCoeffs_mul_of_leibniz`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PolynomialEval.lean#L184).

> A map satisfying the Leibniz rule satisfies it coefficientwise on polynomials. Applied to
> a total derivative this is the Leibniz rule for the mass-weight polynomial.

```lean
lemma mapCoeffs_mul_of_leibniz {A : Type*} [Ring A] {D : A → A} (hD0 : D 0 = 0)
    (hDadd : ∀ a b : A, D (a + b) = D a + D b)
    (hD : ∀ a b : A, D (a * b) = D a * b + a * D b) (p q : Polynomial A) :
    mapCoeffs D (p * q) = mapCoeffs D p * q + p * mapCoeffs D q
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/PolynomialEval.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PolynomialEval.lean)
