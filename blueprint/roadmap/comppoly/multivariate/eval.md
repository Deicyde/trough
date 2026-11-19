---
catalog: module
lean: CPoly.CMvPolynomial.evalHom, CPoly.CMvPolynomial.evalHom_apply, CPoly.CMvPolynomial.eval_zero, CPoly.CMvPolynomial.eval_one, CPoly.CMvPolynomial.eval_C, CPoly.CMvPolynomial.eval_X, CPoly.CMvPolynomial.eval_add, CPoly.CMvPolynomial.eval_mul, CPoly.CMvPolynomial.eval_pow, CPoly.CMvPolynomial.eval_neg, CPoly.CMvPolynomial.eval_sub, CPoly.CMvPolynomial.eval_sum, CPoly.CMvPolynomial.eval_prod, CPoly.CMvPolynomial.eval_ext_univariate
statement: formalized
proof: formalized
---

# Evaluation of computable multivariate polynomials, bundled and over `Finset`s

`CompPoly.Multivariate.Eval`, in [CompPoly/Multivariate/Eval.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Eval.lean), by Pablo Martín Vinuelas.

> CompPoly records that `CMvPolynomial.eval vals` respects each ring operation separately
> (`eval_zero`, `eval_one`, `eval_add`, `eval_mul`, `eval_C`, …), which is what `simp`/`grind`
> need to normalize a *fixed* expression. Two things are missing for reasoning about a **family**
> of polynomials: the value of a bare variable, and commutation with `Finset.sum` / `Finset.prod`.
>
> Both follow at once from bundling: `CMvPolynomial.eval vals` is `eval₂Hom (RingHom.id R) vals`,
> so `map_sum` and `map_prod` apply verbatim. `evalHom` records that bundling; the two `Finset`
> lemmas are its immediate corollaries, stated in unbundled form so that call sites can rewrite
> without unfolding.

`CPoly.CMvPolynomial.evalHom` (definition, [line 34](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Eval.lean#L34))

> Evaluation at a fixed point, bundled as a ring homomorphism — the identity-coefficient case
> of `eval₂Hom`. This is what gives evaluation the `map_*` API of a `RingHom`.

```lean
def evalHom : CMvPolynomial n R →+* R
```

`CPoly.CMvPolynomial.evalHom_apply` (theorem, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Eval.lean#L37))

```lean
theorem evalHom_apply (p : CMvPolynomial n R) : evalHom vals p = p.eval vals
```

`CPoly.CMvPolynomial.eval_zero` (lemma, [line 40](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Eval.lean#L40))

```lean
lemma eval_zero : (0 : CMvPolynomial n R).eval vals = 0
```

`CPoly.CMvPolynomial.eval_one` (lemma, [line 44](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Eval.lean#L44))

```lean
lemma eval_one : (1 : CMvPolynomial n R).eval vals = 1
```

`CPoly.CMvPolynomial.eval_C` (lemma, [line 48](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Eval.lean#L48))

```lean
lemma eval_C (c : R) : (CMvPolynomial.C c : CMvPolynomial n R).eval vals = c
```

`CPoly.CMvPolynomial.eval_X` (theorem, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Eval.lean#L52))

```lean
theorem eval_X (i : Fin n) : (X (R := R) i).eval vals = vals i
```

`CPoly.CMvPolynomial.eval_add` (lemma, [line 56](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Eval.lean#L56))

```lean
lemma eval_add (p q : CMvPolynomial n R) :
    (p + q).eval vals = p.eval vals + q.eval vals
```

`CPoly.CMvPolynomial.eval_mul` (lemma, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Eval.lean#L60))

```lean
lemma eval_mul (p q : CMvPolynomial n R) :
    (p * q).eval vals = p.eval vals * q.eval vals
```

`CPoly.CMvPolynomial.eval_pow` (lemma, [line 64](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Eval.lean#L64))

```lean
lemma eval_pow (p : CMvPolynomial n R) (k : ℕ) :
    (p ^ k).eval vals = (p.eval vals) ^ k
```

`CPoly.CMvPolynomial.eval_neg` (lemma, [line 78](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Eval.lean#L78))

```lean
lemma eval_neg (p : CMvPolynomial n R) :
    (-p).eval vals = -(p.eval vals)
```

`CPoly.CMvPolynomial.eval_sub` (lemma, [line 83](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Eval.lean#L83))

```lean
lemma eval_sub (p q : CMvPolynomial n R) :
    (p - q).eval vals = p.eval vals - q.eval vals
```

`CPoly.CMvPolynomial.eval_sum` (theorem, [line 90](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Eval.lean#L90))

> Evaluation commutes with a finite sum of polynomials.

```lean
theorem eval_sum {ι : Type*} (s : Finset ι) (f : ι → CMvPolynomial n R) :
    (∑ i ∈ s, f i).eval vals = ∑ i ∈ s, (f i).eval vals
```

`CPoly.CMvPolynomial.eval_prod` (theorem, [line 95](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Eval.lean#L95))

> Evaluation commutes with a finite product of polynomials.

```lean
theorem eval_prod {ι : Type*} (s : Finset ι) (f : ι → CMvPolynomial n R) :
    (∏ i ∈ s, f i).eval vals = ∏ i ∈ s, (f i).eval vals
```

> ## Transporting a whole polynomial
>
> The lemmas above are enough for statements about *values*. A statement about *degrees* is not
> determined by values (two distinct polynomials agree everywhere over a finite field), so it has to
> cross the representation boundary at the level of the polynomial itself, through
> `fromCMvPolynomial`. That map is the forward direction of `polyRingEquiv`, hence a ring
> homomorphism, so it too commutes with `Finset.sum` and `Finset.prod`.

`CPoly.CMvPolynomial.eval_ext_univariate` (theorem, [line 128](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Eval.lean#L128))

> **Bridge from univariate eval-extensionality.** Two single-variable
> `CMvPolynomial`s over an integral domain that agree on more than $d$ points
> of a `Finset S` are equal, when $d$ bounds the `degreeOf 0` of their
> difference through the `CPolynomial.cmvEquiv` bridge.
>
> The hypothesis form matches Schwartz–Zippel usage at call sites: callers
> typically have a degree bound on the difference polynomial, not on `p` and
> `q` individually.

```lean
theorem eval_ext_univariate
    [CommRing R] [DecidableEq R] [BEq R] [LawfulBEq R] [IsDomain R]
    {p q : CMvPolynomial 1 R} {d : ℕ} {S : Finset R}
    (hdeg : (fromCMvPolynomial p - fromCMvPolynomial q).degreeOf 0 ≤ d)
    (hagree :
      d < (S.filter
              (fun r ↦ p.eval (fun _ ↦ r) = q.eval (fun _ ↦ r))).card) :
    p = q
```

## Depends on

- [`CMvPolynomial`/`MvPolynomial` Evaluation](mvpolyequiv/eval.md)

## Proof depends on

- [Equivalence between `CPolynomial` and `CMvPolynomial 1`](../univariate/part-01/cmvequiv.md)

## Sources

- [CompPoly/Multivariate/Eval.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Eval.lean)
- [Declaration ledger](../../../sources/comppoly/CompPoly.Multivariate.Eval.json)
