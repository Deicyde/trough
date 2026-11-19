---
catalog: module
lean: CompPoly.CPolynomial.toPoly_injective, CompPoly.CPolynomial.eval_eq_eval₂, CompPoly.CPolynomial.CHom, CompPoly.CPolynomial.CHom_apply, CompPoly.CPolynomial.toPolyRingHom, CompPoly.CPolynomial.toPolyRingHom_apply, CompPoly.CPolynomial.ringHom_ext, CompPoly.CPolynomial.eval₂Hom, CompPoly.CPolynomial.eval₂Hom_apply, CompPoly.CPolynomial.eval₂Hom_C, CompPoly.CPolynomial.eval₂Hom_X, CompPoly.CPolynomial.evalHom, CompPoly.CPolynomial.evalHom_apply, CompPoly.CPolynomial.eval_sum, CompPoly.CPolynomial.eval_prod, CompPoly.CPolynomial.mapRingHom, CompPoly.CPolynomial.mapRingHom_C, CompPoly.CPolynomial.mapRingHom_X, CompPoly.CPolynomial.eval_mapRingHom, CompPoly.CPolynomial.toPoly_mapRingHom, CompPoly.CPolynomial.natDegree_mapRingHom_le
statement: formalized
proof: formalized
---

# `C`, `eval₂`, and coefficient-mapping as ring homomorphisms

`CompPoly.Univariate.ToPoly.RingHom`, in [CompPoly/Univariate/ToPoly/RingHom.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/RingHom.lean), by Tobias Rothmann, Julian Sutherland.

> `CPolynomial.C`, `CPolynomial.eval₂` and coefficient-mapping bundled as `RingHom`s, plus a
> ring-hom extensionality principle transported from Mathlib's `Polynomial.ringHom_ext`.
>
> `CHom` and `eval₂Hom` are computable; `toPolyRingHom` is the noncomputable bundling of
> `toPoly` (it is `CPolynomial.ringEquiv`), used in proofs only.  These are the bundled-map
> building blocks behind the computable `finSuccEquivNth` construction for `CMvPolynomial`.

`CompPoly.CPolynomial.toPoly_injective` (theorem, [line 33](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/RingHom.lean#L33))

> `toPoly` is injective — it is the forward map of `CPolynomial.ringEquiv`.

```lean
theorem toPoly_injective : Function.Injective (CPolynomial.toPoly (R := R))
```

`CompPoly.CPolynomial.eval_eq_eval₂` (theorem, [line 38](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/RingHom.lean#L38))

> `CPolynomial.eval` is the identity-coefficient case of `eval₂`.

```lean
theorem eval_eq_eval₂ (x : R) (p : CPolynomial R) :
    CPolynomial.eval x p = p.eval₂ (RingHom.id R) x
```

`CompPoly.CPolynomial.CHom` (definition, [line 43](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/RingHom.lean#L43))

> `CPolynomial.C` bundled as a ring homomorphism.  Computable.

```lean
def CHom : R →+* CPolynomial R
```

`CompPoly.CPolynomial.CHom_apply` (theorem, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/RingHom.lean#L52))

```lean
theorem CHom_apply (r : R) : CHom r = CPolynomial.C r
```

`CompPoly.CPolynomial.toPolyRingHom` (definition, [line 56](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/RingHom.lean#L56))

> `toPoly` bundled as a ring homomorphism (it is `CPolynomial.ringEquiv`).  Noncomputable;
> used in proofs only, e.g. to bring `MvPolynomial.eval₂_comp_left` to bear.

```lean
noncomputable def toPolyRingHom : CPolynomial R →+* Polynomial R
```

`CompPoly.CPolynomial.toPolyRingHom_apply` (theorem, [line 59](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/RingHom.lean#L59))

```lean
theorem toPolyRingHom_apply (p : CPolynomial R) : toPolyRingHom p = p.toPoly
```

`CompPoly.CPolynomial.ringHom_ext` (theorem, [line 65](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/RingHom.lean#L65))

> Two ring homomorphisms out of `CPolynomial R` are equal once they agree on the constants and
> on `X`.

```lean
theorem ringHom_ext {S : Type*} [Semiring S] {f g : CPolynomial R →+* S}
    (hC : ∀ r, f (CPolynomial.C r) = g (CPolynomial.C r)) (hX : f CPolynomial.X = g CPolynomial.X) :
    f = g
```

`CompPoly.CPolynomial.eval₂Hom` (definition, [line 91](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/RingHom.lean#L91))

> `CPolynomial.eval₂` bundled as a ring homomorphism (the coefficient map `f` and the point `x`
> are fixed).  Computable when `S`'s ring operations are.

```lean
def eval₂Hom (f : R →+* S) (x : S) : CPolynomial R →+* S
```

`CompPoly.CPolynomial.eval₂Hom_apply` (theorem, [line 100](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/RingHom.lean#L100))

```lean
theorem eval₂Hom_apply (f : R →+* S) (x : S) (p : CPolynomial R) :
    eval₂Hom f x p = p.eval₂ f x
```

`CompPoly.CPolynomial.eval₂Hom_C` (theorem, [line 103](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/RingHom.lean#L103))

```lean
theorem eval₂Hom_C (f : R →+* S) (x : S) (r : R) :
    eval₂Hom f x (CPolynomial.C r) = f r
```

`CompPoly.CPolynomial.eval₂Hom_X` (theorem, [line 107](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/RingHom.lean#L107))

```lean
theorem eval₂Hom_X (f : R →+* S) (x : S) :
    eval₂Hom f x (CPolynomial.X) = x
```

`CompPoly.CPolynomial.evalHom` (definition, [line 113](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/RingHom.lean#L113))

> Evaluation at a point, bundled as a ring homomorphism. This is what gives evaluation the
> `map_*` API of a `RingHom`, and in particular `map_sum` and `map_prod`.

```lean
def evalHom (x : R) : CPolynomial R →+* R
```

`CompPoly.CPolynomial.evalHom_apply` (theorem, [line 115](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/RingHom.lean#L115))

```lean
theorem evalHom_apply (x : R) (p : CPolynomial R) : evalHom x p = p.eval x
```

`CompPoly.CPolynomial.eval_sum` (theorem, [line 119](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/RingHom.lean#L119))

> Evaluation commutes with finite sums.

```lean
theorem eval_sum {ι : Type*} (s : Finset ι) (f : ι → CPolynomial R) (x : R) :
    (∑ i ∈ s, f i).eval x = ∑ i ∈ s, (f i).eval x
```

`CompPoly.CPolynomial.eval_prod` (theorem, [line 126](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/RingHom.lean#L126))

> Evaluation commutes with finite products.

```lean
theorem eval_prod {ι : Type*} (s : Finset ι) (f : ι → CPolynomial R) (x : R) :
    (∏ i ∈ s, f i).eval x = ∏ i ∈ s, (f i).eval x
```

`CompPoly.CPolynomial.mapRingHom` (definition, [line 138](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/RingHom.lean#L138))

> Map the coefficients of a computable univariate polynomial along a ring homomorphism.
> Computable.

```lean
def mapRingHom (f : R →+* S) : CPolynomial R →+* CPolynomial S
```

`CompPoly.CPolynomial.mapRingHom_C` (theorem, [line 141](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/RingHom.lean#L141))

```lean
theorem mapRingHom_C (f : R →+* S) (r : R) :
    mapRingHom f (CPolynomial.C r) = CPolynomial.C (f r)
```

`CompPoly.CPolynomial.mapRingHom_X` (theorem, [line 145](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/RingHom.lean#L145))

```lean
theorem mapRingHom_X (f : R →+* S) :
    mapRingHom f (CPolynomial.X) = CPolynomial.X
```

`CompPoly.CPolynomial.eval_mapRingHom` (theorem, [line 150](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/RingHom.lean#L150))

> Evaluating a coefficient-mapped polynomial: `eval x (mapRingHom f p) = eval₂ f x p`.

```lean
theorem eval_mapRingHom (f : R →+* S) (x : S) (p : CPolynomial R) :
    CPolynomial.eval x (mapRingHom f p) = p.eval₂ f x
```

`CompPoly.CPolynomial.toPoly_mapRingHom` (theorem, [line 160](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/RingHom.lean#L160))

> `toPoly` commutes with coefficient-mapping.

```lean
theorem toPoly_mapRingHom (f : R →+* S) (p : CPolynomial R) :
    (mapRingHom f p).toPoly = Polynomial.map f p.toPoly
```

`CompPoly.CPolynomial.natDegree_mapRingHom_le` (theorem, [line 175](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/RingHom.lean#L175))

> Coefficient-mapping does not increase the degree.

```lean
theorem natDegree_mapRingHom_le (f : R →+* S) (p : CPolynomial R) :
    (mapRingHom f p).natDegree ≤ p.natDegree
```

## Depends on

- [`toPoly` Equivalence](equiv.md)

## Proof depends on

- [Proofs of Correctness for CPolynomial Operations, wrt Mathlib Specs](impl.md)

## Sources

- [CompPoly/Univariate/ToPoly/RingHom.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ToPoly/RingHom.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.ToPoly.RingHom.json)
