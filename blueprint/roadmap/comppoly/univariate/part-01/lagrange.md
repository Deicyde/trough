---
catalog: module
lean: CompPoly.CPolynomial.CLagrange.basisDivisor, CompPoly.CPolynomial.CLagrange.cbasisDivisor_eq_basisDivisor, CompPoly.CPolynomial.CLagrange.basisListRaw, CompPoly.CPolynomial.CLagrange.basisListRaw_trim_perm, CompPoly.CPolynomial.CLagrange.basis, CompPoly.CPolynomial.CLagrange.cbasis_eq_basis, CompPoly.CPolynomial.CLagrange.interpolateListRaw, CompPoly.CPolynomial.CLagrange.interpolateListRaw_trim_perm, CompPoly.CPolynomial.CLagrange.interpolateRaw, CompPoly.CPolynomial.CLagrange.interpolate, CompPoly.CPolynomial.CLagrange.cinterpolate_eq_interpolate, CompPoly.CPolynomial.CLagrange.interpolatePow, CompPoly.CPolynomial.CLagrange.eq_of_pow_eq_pow_of_lt_orderOf, CompPoly.CPolynomial.CLagrange.eval_interpolatePow_at_node
statement: formalized
proof: formalized
---

# Lagrange Interpolation

`CompPoly.Univariate.Lagrange`, in [CompPoly/Univariate/Lagrange.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Lagrange.lean), by Quang Dao, Gregor Mitscha-Baude, Derek Sorensen, Katerina Hristova, Julian Sutherland.

> This file defines computable Lagrange interpolation
> for univariate polynomials, i.e. `CPolynomial`s.

`CompPoly.CPolynomial.CLagrange.basisDivisor` (definition, [line 32](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Lagrange.lean#L32))

> `basisDivisor xᵢ xⱼ` is the unique linear or constant computable polynomial such that
> when evaluated at `xᵢ` it gives `1` and `xⱼ` it gives `0` (where when `xᵢ = xⱼ` it is
> identically `0`). Such polynomials are the building blocks for the Lagrange interpolants.

```lean
def basisDivisor (xᵢ xⱼ : R) : CPolynomial R
```

`CompPoly.CPolynomial.CLagrange.cbasisDivisor_eq_basisDivisor` (lemma, [line 35](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Lagrange.lean#L35))

```lean
lemma cbasisDivisor_eq_basisDivisor {xᵢ xⱼ : R} :
    (basisDivisor xᵢ xⱼ).toPoly = Lagrange.basisDivisor xᵢ xⱼ
```

> ### Helpers for deferred-trim folds
>
> The `basis` product and `interpolate` sum below combine raw arrays with the untrimmed
> `Raw.mulRaw`/`Raw.addRaw` and trim once at the end, rather than paying a trim per factor
> (as `Finset.prod`/`Finset.sum` over the canonical `CPolynomial.Mul`/`.Add` instances
> would). Computability requires bypassing the noncomputable `Finset.toList`, so the folds
> go through `Quotient.liftOn` on the underlying multiset with a permutation-invariance
> proof routed through `toPoly`.

`CompPoly.CPolynomial.CLagrange.basisListRaw` (definition, [line 51](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Lagrange.lean#L51))

> `basisDivisor`-product fold over a list, combining factors with the untrimmed
> `Raw.mulRaw`. The wrapping `basis` definition trims this once.

```lean
def basisListRaw {ι : Type*} (x : ι → R) (i : ι) (l : List ι) :
    CPolynomial.Raw R
```

`CompPoly.CPolynomial.CLagrange.basisListRaw_trim_perm` (lemma, [line 72](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Lagrange.lean#L72))

```lean
lemma basisListRaw_trim_perm {ι : Type*} (x : ι → R) (i : ι)
    {l₁ l₂ : List ι} (h : l₁.Perm l₂) :
    (basisListRaw x i l₁).trim = (basisListRaw x i l₂).trim
```

`CompPoly.CPolynomial.CLagrange.basis` (definition, [line 89](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Lagrange.lean#L89))

> Computable Lagrange basis polynomials indexed by `s : Finset ι`, defined at nodes `x i` for a
> map `x : ι → F`. For `i, j ∈ s`, `basis s x i` evaluates to `0` at `x j` for `i ≠ j`. When
> `x` is injective on `s`, `basis s x i` evaluates to 1 at `x i`.
>
> The product folds `(s.erase i).val` with the untrimmed `Raw.mulRaw` via `Quotient.liftOn`
> and trims once at the end, rather than paying one `Raw.mul` trim per factor (as the
> `Finset.prod` formulation would).

```lean
def basis {ι : Type*} [DecidableEq ι] (s : Finset ι) (x : ι → R) (i : ι) :
    CPolynomial R
```

`CompPoly.CPolynomial.CLagrange.cbasis_eq_basis` (lemma, [line 95](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Lagrange.lean#L95))

```lean
lemma cbasis_eq_basis {ι : Type*} [DecidableEq ι] (s : Finset ι) (x : ι → R) (i : ι) :
    (basis s x i).toPoly = Lagrange.basis s x i
```

> ### Interpolation sum
>
> The `interpolate` sum is folded with the untrimmed `Raw.addRaw`, with each addend itself
> formed by `Raw.mulRaw (Raw.C (y i)) (basis s x i).val` (also untrimmed). One `trim` runs
> at the end of the entire fold.

`CompPoly.CPolynomial.CLagrange.interpolateListRaw` (definition, [line 115](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Lagrange.lean#L115))

```lean
def interpolateListRaw {ι : Type*} [DecidableEq ι]
    (s : Finset ι) (x : ι → R) (y : ι → R) (l : List ι) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.CLagrange.interpolateListRaw_trim_perm` (lemma, [line 143](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Lagrange.lean#L143))

```lean
lemma interpolateListRaw_trim_perm {ι : Type*} [DecidableEq ι]
    (s : Finset ι) (x : ι → R) (y : ι → R) {l₁ l₂ : List ι} (h : l₁.Perm l₂) :
    (interpolateListRaw s x y l₁).trim = (interpolateListRaw s x y l₂).trim
```

`CompPoly.CPolynomial.CLagrange.interpolateRaw` (definition, [line 155](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Lagrange.lean#L155))

> Computable raw-fold form of the interpolation polynomial: defer trimming to the
> end of the `Finset.sum`.

```lean
def interpolateRaw {ι : Type*} [DecidableEq ι]
    (s : Finset ι) (x : ι → R) (y : ι → R) : CPolynomial R
```

`CompPoly.CPolynomial.CLagrange.interpolate` (definition, [line 195](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Lagrange.lean#L195))

> Computable Lagrange interpolation: given a finset `s : Finset ι`, a nodal map `x : ι → F`
> injective on `s` and a value function `y : ι → F`, `interpolate s x y` is the unique computable
> polynomial of degree `< #s` that takes value `y i` on `x i` for all `i` in `s`.

```lean
def interpolate {ι : Type*} [DecidableEq ι] (s : Finset ι) (x : ι → R) :
    (ι → R) →ₗ[R] CPolynomial R
```

`CompPoly.CPolynomial.CLagrange.cinterpolate_eq_interpolate` (lemma, [line 226](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Lagrange.lean#L226))

```lean
lemma cinterpolate_eq_interpolate
    {ι : Type*} [DecidableEq ι] {s : Finset ι} {x : ι → R} {y : ι → R} :
      (interpolate s x y).toPoly = Lagrange.interpolate s x y
```

`CompPoly.CPolynomial.CLagrange.interpolatePow` (definition, [line 237](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Lagrange.lean#L237))

> Produces the unique polynomial of degree at most n-1 that equals r[i] at ω^i
> for i = 0, 1, ..., n-1.
>
> Uses Lagrange interpolation: p(X) = Σᵢ rᵢ · Lᵢ(X)
> where Lᵢ(X) = ∏_{j≠i} (X - ωʲ) / (ωⁱ - ωʲ).

```lean
def interpolatePow {n : ℕ} (ω : R) (r : Vector R n) :
    CPolynomial R
```

`CompPoly.CPolynomial.CLagrange.eq_of_pow_eq_pow_of_lt_orderOf` (theorem, [line 243](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Lagrange.lean#L243))

```lean
theorem eq_of_pow_eq_pow_of_lt_orderOf {G : Type*} [Group G] {ω : G} {n : ℕ}
    (h_order : n ≤ orderOf ω) (a b : Fin n) (h_pow : ω ^ (a : ℕ) = ω ^ (b : ℕ)) : a = b
```

`CompPoly.CPolynomial.CLagrange.eval_interpolatePow_at_node` (lemma, [line 255](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Lagrange.lean#L255))

> Key correctness theorem for `interpolatePow`.

```lean
lemma eval_interpolatePow_at_node {n : ℕ} {ω : Rˣ} {r : Vector R n} : n ≤ orderOf ω →
    ∀ i : Fin n, (interpolatePow ω.1 r).eval (ω.1 ^ i.1) = r.get i
```

## Depends on

- [Computable Univariate To `Polynomial`](../part-02/topoly/core.md)

## Proof depends on

- [Proofs of Correctness for CPolynomial Operations, wrt Mathlib Specs](../part-02/topoly/impl.md)

## Sources

- [CompPoly/Univariate/Lagrange.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Lagrange.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Univariate.Lagrange.json)
