---
catalog: module
lean: Polynomial.toImpl, CompPoly.CPolynomial.Raw.toPoly, CompPoly.CPolynomial.Raw.toPoly', CompPoly.CPolynomial.toPoly, CompPoly.CPolynomial.Raw.ofPoly, CompPoly.CPolynomial.Raw.eval_toPoly_eq_eval, CompPoly.CPolynomial.Raw.coeff_toPoly, CompPoly.CPolynomial.Raw.toImpl_elim, CompPoly.CPolynomial.Raw.toPoly_toImpl, CompPoly.CPolynomial.Raw.toPoly_trim, CompPoly.CPolynomial.Raw.toPoly_addRaw, CompPoly.CPolynomial.Raw.toPoly_smulRight, CompPoly.CPolynomial.Raw.toPoly_add, CompPoly.CPolynomial.Raw.toImpl_nonzero, CompPoly.CPolynomial.Raw.getLast_toImpl, CompPoly.CPolynomial.Raw.isCanonical_toImpl, CompPoly.CPolynomial.Raw.trim_toImpl, CompPoly.CPolynomial.toPoly_mk_toImpl, CompPoly.CPolynomial.ofArray_toPoly, CompPoly.CPolynomial.toImpl_toPoly_of_canonical, CompPoly.CPolynomial.Raw.toImpl_toPoly, CompPoly.CPolynomial.Raw.toPoly_natDegree_lt_trim_size_of_pos, CompPoly.CPolynomial.toPoly_inj, CompPoly.CPolynomial.toPoly_eq_zero_iff, CompPoly.CPolynomial.eval_toImpl_eq_eval, CompPoly.CPolynomial.Raw.eval_trim_eq_eval
statement: formalized
proof: formalized
---

# Computable Univariate To `Polynomial`

`CompPoly.Univariate.ToPoly.Core`, in [CompPoly/Univariate/ToPoly/Core.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Core.lean), by Quang Dao, Gregor Mitscha-Baude, Derek Sorensen.

> Conversions between computable univariate polynomials and mathlib `Polynomial`.

`Polynomial.toImpl` (definition, [line 29](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Core.lean#L29))

> Convert a mathlib `Polynomial` to a `CPolynomial.Raw` by extracting coefficients
> up to the degree.

```lean
def Polynomial.toImpl {R : Type*} [Semiring R] (p : R[X]) : CompPoly.CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.toPoly` (definition, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Core.lean#L46))

> Convert a `CPolynomial.Raw` to a (mathlib) `Polynomial`.

```lean
noncomputable def Raw.toPoly [Semiring R] (p : CPolynomial.Raw R) : Polynomial R
```

`CompPoly.CPolynomial.Raw.toPoly'` (definition, [line 50](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Core.lean#L50))

> Alternative definition of `toPoly` using `Finsupp`; currently unused.

```lean
noncomputable def Raw.toPoly' [Semiring R] (p : CPolynomial.Raw R) : Polynomial R
```

`CompPoly.CPolynomial.toPoly` (definition, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Core.lean#L60))

> Convert a canonical polynomial to a (mathlib) `Polynomial`.

```lean
noncomputable def toPoly [Semiring R] (p : CPolynomial R) : Polynomial R
```

`CompPoly.CPolynomial.Raw.ofPoly` (alias, [line 75](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Core.lean#L75))

```lean
alias ofPoly
```

`CompPoly.CPolynomial.Raw.eval_toPoly_eq_eval` (theorem, [line 78](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Core.lean#L78))

> Evaluation is preserved by `toPoly`.

```lean
theorem eval_toPoly_eq_eval (x : Q) (p : CPolynomial.Raw Q) : p.toPoly.eval x = p.eval x
```

`CompPoly.CPolynomial.Raw.coeff_toPoly` (lemma, [line 87](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Core.lean#L87))

> The coefficients of `p.toPoly` match those of `p`.

```lean
lemma coeff_toPoly {p : CPolynomial.Raw Q} {n : ℕ} : p.toPoly.coeff n = p.coeff n
```

`CompPoly.CPolynomial.Raw.toImpl_elim` (lemma, [line 123](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Core.lean#L123))

> Case analysis for `toImpl`: either the polynomial is zero or has a specific form.

```lean
lemma toImpl_elim (p : Q[X]) :
    (p = 0 ∧ p.toImpl = #[])
  ∨ (p ≠ 0 ∧ p.toImpl = .ofFn (fun i : Fin (p.natDegree + 1) => p.coeff i))
```

`CompPoly.CPolynomial.Raw.toPoly_toImpl` (theorem, [line 139](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Core.lean#L139))

> `toImpl` is a right-inverse of `toPoly`: the round-trip from `Polynomial` is the identity.
>
> This shows `toPoly` is surjective and `toImpl` is injective.

```lean
theorem toPoly_toImpl {p : Q[X]} : p.toImpl.toPoly = p
```

`CompPoly.CPolynomial.Raw.toPoly_trim` (lemma, [line 155](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Core.lean#L155))

> Trimming doesn't change the `toPoly` image.

```lean
lemma toPoly_trim [LawfulBEq R] {p : CPolynomial.Raw R} : p.trim.toPoly = p.toPoly
```

`CompPoly.CPolynomial.Raw.toPoly_addRaw` (theorem, [line 161](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Core.lean#L161))

> `toPoly` preserves addition.

```lean
theorem toPoly_addRaw {p q : CPolynomial.Raw Q} : (addRaw p q).toPoly = p.toPoly + q.toPoly
```

`CompPoly.CPolynomial.Raw.toPoly_smulRight` (theorem, [line 168](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Core.lean#L168))

> `toPoly` of a right-scalar multiplication is multiplication by `Polynomial.C r`
> on the right.

```lean
theorem toPoly_smulRight {p : CPolynomial.Raw Q} {r : Q} :
    (smulRight r p).toPoly = p.toPoly * Polynomial.C r
```

`CompPoly.CPolynomial.Raw.toPoly_add` (lemma, [line 179](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Core.lean#L179))

```lean
lemma toPoly_add [LawfulBEq R] (p q : CPolynomial.Raw R) :
    (p + q).toPoly = p.toPoly + q.toPoly
```

`CompPoly.CPolynomial.Raw.toImpl_nonzero` (lemma, [line 185](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Core.lean#L185))

> Non-zero polynomials map to non-empty arrays.

```lean
lemma toImpl_nonzero {p : Q[X]} (hp : p ≠ 0) : p.toImpl.size > 0
```

`CompPoly.CPolynomial.Raw.getLast_toImpl` (lemma, [line 192](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Core.lean#L192))

> The last coefficient of `toImpl p` is the leading coefficient of `p`.

```lean
lemma getLast_toImpl {p : Q[X]} (hp : p ≠ 0) : let h : p.toImpl.size > 0 := toImpl_nonzero hp;
    p.toImpl[p.toImpl.size - 1] = p.leadingCoeff
```

`CompPoly.CPolynomial.Raw.isCanonical_toImpl` (theorem, [line 201](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Core.lean#L201))

> `toImpl` lands in the semantic canonical carrier used by `CPolynomial`.

```lean
theorem isCanonical_toImpl (p : R[X]) : IsCanonical p.toImpl
```

`CompPoly.CPolynomial.Raw.trim_toImpl` (theorem, [line 212](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Core.lean#L212))

> `toImpl` produces canonical polynomials (no trailing zeros).

```lean
theorem trim_toImpl [LawfulBEq R] (p : R[X]) : p.toImpl.trim = p.toImpl
```

`CompPoly.CPolynomial.toPoly_mk_toImpl` (theorem, [line 220](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Core.lean#L220))

> Building a canonical polynomial from `toImpl` and converting it back yields the
> original mathlib polynomial.

```lean
theorem toPoly_mk_toImpl (p : R[X]) :
    CPolynomial.toPoly ⟨p.toImpl, Raw.isCanonical_toImpl p⟩ = p
```

`CompPoly.CPolynomial.ofArray_toPoly` (theorem, [line 225](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Core.lean#L225))

> `ofArray` preserves the raw polynomial's `toPoly` image.

```lean
theorem ofArray_toPoly [LawfulBEq R] (p : CPolynomial.Raw R) :
    (CPolynomial.ofArray p).toPoly = p.toPoly
```

`CompPoly.CPolynomial.toImpl_toPoly_of_canonical` (lemma, [line 234](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Core.lean#L234))

> On canonical polynomials, `toImpl` is a left-inverse of `toPoly`.
>
> This shows `toPoly` is a bijection from `CPolynomial R` to `Polynomial R`.

```lean
lemma toImpl_toPoly_of_canonical [LawfulBEq R] (p : CPolynomial R) : p.toPoly.toImpl = p
```

`CompPoly.CPolynomial.Raw.toImpl_toPoly` (theorem, [line 250](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Core.lean#L250))

> The round-trip from `CPolynomial.Raw` to `Polynomial` and back yields the canonical form.

```lean
theorem Raw.toImpl_toPoly [LawfulBEq R] (p : CPolynomial.Raw R) : p.toPoly.toImpl = p.trim
```

`CompPoly.CPolynomial.Raw.toPoly_natDegree_lt_trim_size_of_pos` (theorem, [line 255](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Core.lean#L255))

> A nonempty trimmed raw polynomial bounds the degree of its `toPoly` image.

```lean
theorem Raw.toPoly_natDegree_lt_trim_size_of_pos [LawfulBEq R]
    (p : CPolynomial.Raw R) (hp : 0 < p.trim.size) :
    p.toPoly.natDegree < p.trim.size
```

`CompPoly.CPolynomial.toPoly_inj` (theorem, [line 271](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Core.lean#L271))

> `toPoly` is injective, with no `Nontrivial` or commutativity assumption.

```lean
theorem toPoly_inj [LawfulBEq R] {p q : CPolynomial R} : p.toPoly = q.toPoly ↔ p = q
```

`CompPoly.CPolynomial.toPoly_eq_zero_iff` (theorem, [line 281](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Core.lean#L281))

> `toPoly` maps a canonical polynomial to `0` iff the polynomial is `0`.

```lean
theorem toPoly_eq_zero_iff [LawfulBEq R] (p : CPolynomial R) :
    p.toPoly = 0 ↔ p = 0
```

`CompPoly.CPolynomial.eval_toImpl_eq_eval` (theorem, [line 297](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Core.lean#L297))

> Evaluation is preserved by `toImpl`.

```lean
theorem eval_toImpl_eq_eval [LawfulBEq R] (x : R) (p : R[X]) : p.toImpl.eval x = p.eval x
```

`CompPoly.CPolynomial.Raw.eval_trim_eq_eval` (lemma, [line 302](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Core.lean#L302))

> Evaluation is unchanged by trimming.

```lean
lemma Raw.eval_trim_eq_eval [LawfulBEq R] (x : R) (p : CPolynomial.Raw R) :
    p.trim.eval x = p.eval x
```

## Depends on

- [Computable Univariate Polynomials](../../part-01/basic.md)

## Sources

- [CompPoly/Univariate/ToPoly/Core.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Core.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.ToPoly.Core.json)
