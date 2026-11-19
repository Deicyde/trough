---
catalog: module
lean: CompPoly.CPolynomial.xgcdAux, CompPoly.CPolynomial.xgcd, CompPoly.CPolynomial.Bezout, CompPoly.CPolynomial.xgcdAux_bezout, CompPoly.CPolynomial.xgcd_bezout, CompPoly.CPolynomial.xgcdAux_toPoly_eq_gcd, CompPoly.CPolynomial.xgcd_toPoly_eq_gcd, CompPoly.CPolynomial.xgcdAux_toPoly_eq_xgcdAux, CompPoly.CPolynomial.xgcd_toPoly_eq_xgcd, CompPoly.CPolynomial.normXgcd, CompPoly.CPolynomial.normXgcd_bezout, CompPoly.CPolynomial.normXgcd_fst_toPoly, CompPoly.CPolynomial.monicNormalize_toPoly_eq_normalize, CompPoly.CPolynomial.gcdMonic_toPoly_eq_normalize_gcd, CompPoly.CPolynomial.gcdMonic_eq_normXgcd_fst, CompPoly.CPolynomial.normXgcd_snd_toPoly, CompPoly.CPolynomial.normXgcd_fst_comm, CompPoly.BezoutDegreeInvariant, CompPoly.BezoutDegreeInvariantOf, CompPoly.BezoutDegreeInvariant.degree_complement, CompPoly.BezoutDegreeInvariant.step, CompPoly.BezoutStopSpec, CompPoly.BezoutStopSpecOf, CompPoly.xgcdAux_stopSpec_of_invariant, CompPoly.xgcd_stopSpec
statement: formalized
proof: formalized
---

# Extended Euclidean Algorithm for `CPolynomial`

`CompPoly.Univariate.EuclideanAlgorithm`, in [CompPoly/Univariate/EuclideanAlgorithm.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/EuclideanAlgorithm.lean), by Juan Conejero, Valerii Huhnin.

> `xgcd p q` returns a triple `(r, s, t)` with `r = s * p + t * q`.
> Early stop when `r.natDegree < threshold`.
> The default `threshold = 0` makes `r` the Greatest Common Divisor of `p` and `q`.
>
> For positive thresholds, `xgcd_stopSpec` characterizes the output: `BezoutStopSpec` packages
> the Bézout identity together with the residue/cofactor degree bounds at the stopping point,
> via the loop invariant `BezoutDegreeInvariant`.

`CompPoly.CPolynomial.xgcdAux` (definition, [line 42](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/EuclideanAlgorithm.lean#L42))

> Extended euclidean algorithm on `p, q`.
>
> Stops when `r.natDegree < threshold`, `r = 0`, or fuel `n` exhausted.
>
> If `threshold > 0` then `xgcdAux` need not compute the greatest common divisor.
>
> Potential optimization: the raw long division behind `r' / r` already computes
> `r' - (r' / r) * r` but it's not exposed through `CPolynomial R`.

```lean
def xgcdAux [Field R] [BEq R] [LawfulBEq R]
    (threshold n : ℕ) (r s t r' s' t' : CPolynomial R) :
    CPolynomial R × CPolynomial R × CPolynomial R
```

`CompPoly.CPolynomial.xgcd` (definition, [line 66](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/EuclideanAlgorithm.lean#L66))

> Extended euclidean algorithm for `(p, q)`.
>
> Returns `(r, s, t)` with `r = s * p + t * q`.
>
> With the default `threshold = 0` returns the gcd of `p` and `q`.
> With `threshold > 0` stops when `r.natDegree < threshold`.
>
> If `threshold > 0` then `xgcdAux` need not compute the greatest common divisor.

```lean
def xgcd [Field R] [BEq R] [LawfulBEq R]
    (p q : CPolynomial R) (threshold : ℕ := 0) :
    CPolynomial R × CPolynomial R × CPolynomial R
```

> ### Bezout-identity correctness

`CompPoly.CPolynomial.Bezout` (definition, [line 74](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/EuclideanAlgorithm.lean#L74))

> Bezout predicate on a triple `(r, s, t)`: `r = s * p + t * q`.

```lean
def Bezout [Semiring R] [BEq R] [LawfulBEq R] (p q : CPolynomial R) :
    CPolynomial R × CPolynomial R × CPolynomial R → Prop
```

`CompPoly.CPolynomial.xgcdAux_bezout` (theorem, [line 79](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/EuclideanAlgorithm.lean#L79))

> `xgcdAux` preserves the Bezout identity.

```lean
theorem xgcdAux_bezout [Field R] [BEq R] [LawfulBEq R]
    (p q : CPolynomial R) (threshold n : ℕ)
    {r r' : CPolynomial R} {s t s' t'}
    (h : Bezout p q (r, s, t)) (h' : Bezout p q (r', s', t')) :
    Bezout p q (xgcdAux threshold n r s t r' s' t')
```

`CompPoly.CPolynomial.xgcd_bezout` (theorem, [line 92](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/EuclideanAlgorithm.lean#L92))

> The output of `xgcd` is a Bezout triple for `(p, q)`.

```lean
theorem xgcd_bezout [Field R] [BEq R] [LawfulBEq R]
    (p q : CPolynomial R) (threshold : ℕ) :
    Bezout p q (xgcd p q threshold)
```

> # `xgcd` correctness (threshold 0)
>
> Correctness theorems for `xgcd` with the default threshold 0.

`CompPoly.CPolynomial.xgcdAux_toPoly_eq_gcd` (lemma, [line 111](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/EuclideanAlgorithm.lean#L111))

> The gcd component of CompPoly's `xgcdAux` at threshold `0` coincides with
> Mathlib's `EuclideanDomain.gcd`.

```lean
lemma xgcdAux_toPoly_eq_gcd
    [Field R] [BEq R] [LawfulBEq R] [DecidableEq R]
    (n : ℕ) (r r' s t s' t' : CPolynomial R)
    (hn : r.toPoly.degree < n) :
    (xgcdAux 0 n r s t r' s' t').1.toPoly =
      EuclideanDomain.gcd r.toPoly r'.toPoly
```

`CompPoly.CPolynomial.xgcd_toPoly_eq_gcd` (theorem, [line 133](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/EuclideanAlgorithm.lean#L133))

> The gcd component of CompPoly's `xgcd` at threshold `0`
> coincides with Mathlib's `EuclideanDomain.gcd`.

```lean
theorem xgcd_toPoly_eq_gcd [Field R] [BEq R] [LawfulBEq R] [DecidableEq R] (p q : CPolynomial R) :
    (xgcd p q).1.toPoly = EuclideanDomain.gcd p.toPoly q.toPoly
```

`CompPoly.CPolynomial.xgcdAux_toPoly_eq_xgcdAux` (lemma, [line 141](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/EuclideanAlgorithm.lean#L141))

> CompPoly's `xgcdAux` at threshold `0` coincides with
> Mathlib's `EuclideanDomain.xgcdAux`.

```lean
lemma xgcdAux_toPoly_eq_xgcdAux
    [Field R] [BEq R] [LawfulBEq R] [DecidableEq R]
    (n : ℕ) (r s t r' s' t' : CPolynomial R)
    (hn : r.toPoly.degree < n) :
    Prod.map (·.toPoly) (·.map (·.toPoly) (·.toPoly))
      (xgcdAux 0 n r s t r' s' t') =
      EuclideanDomain.xgcdAux r.toPoly s.toPoly t.toPoly r'.toPoly s'.toPoly t'.toPoly
```

`CompPoly.CPolynomial.xgcd_toPoly_eq_xgcd` (theorem, [line 167](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/EuclideanAlgorithm.lean#L167))

> The Bezout component of CompPoly's `xgcd` coincides with
> Mathlib's `EuclideanDomain.xgcd`.

```lean
theorem xgcd_toPoly_eq_xgcd
    [Field R] [BEq R] [LawfulBEq R] [DecidableEq R]
    (p q : CPolynomial R) :
    (xgcd p q).2.map (·.toPoly) (·.toPoly) =
      EuclideanDomain.xgcd p.toPoly q.toPoly
```

> ### Normalized `xgcd`

`CompPoly.CPolynomial.normXgcd` (definition, [line 184](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/EuclideanAlgorithm.lean#L184))

> CompPoly's `xgcd p q` scaled by the inverse leading coefficient
> of the gcd component, normalizing it to monic.

```lean
def normXgcd [Field R] [BEq R] [LawfulBEq R]
    (p q : CPolynomial R) (threshold : ℕ := 0) :
    CPolynomial R × CPolynomial R × CPolynomial R
```

`CompPoly.CPolynomial.normXgcd_bezout` (theorem, [line 192](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/EuclideanAlgorithm.lean#L192))

> The normalized extended-gcd output satisfies the Bezout identity.

```lean
theorem normXgcd_bezout [Field R] [BEq R] [LawfulBEq R]
    (p q : CPolynomial R) (threshold : ℕ) :
    Bezout p q (normXgcd p q threshold)
```

`CompPoly.CPolynomial.normXgcd_fst_toPoly` (theorem, [line 206](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/EuclideanAlgorithm.lean#L206))

> The gcd component of CompPoly's `normXgcd` is the normalization
> of Mathlib's `EuclideanDomain.gcd`

```lean
theorem normXgcd_fst_toPoly
    [Field R] [BEq R] [LawfulBEq R] [DecidableEq R]
    (p q : CPolynomial R) :
    (normXgcd p q).1.toPoly = normalize (EuclideanDomain.gcd p.toPoly q.toPoly)
```

`CompPoly.CPolynomial.monicNormalize_toPoly_eq_normalize` (theorem, [line 225](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/EuclideanAlgorithm.lean#L225))

> Monic normalization of computable polynomials agrees with Mathlib normalization.

```lean
theorem monicNormalize_toPoly_eq_normalize
    [Field R] [BEq R] [LawfulBEq R] [DecidableEq R]
    (p : CPolynomial R) :
    (CPolynomial.monicNormalize p).toPoly = normalize p.toPoly
```

`CompPoly.CPolynomial.gcdMonic_toPoly_eq_normalize_gcd` (theorem, [line 317](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/EuclideanAlgorithm.lean#L317))

> The specialized monic gcd has the normalized Mathlib gcd as its `toPoly`
> image.

```lean
theorem gcdMonic_toPoly_eq_normalize_gcd
    [Field R] [BEq R] [LawfulBEq R] [DecidableEq R]
    (p q : CPolynomial R) :
    (CPolynomial.gcdMonic p q).toPoly =
      normalize (EuclideanDomain.gcd p.toPoly q.toPoly)
```

`CompPoly.CPolynomial.gcdMonic_eq_normXgcd_fst` (theorem, [line 338](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/EuclideanAlgorithm.lean#L338))

> The specialized monic gcd agrees with the gcd component of normalized
> extended gcd.

```lean
theorem gcdMonic_eq_normXgcd_fst
    [Field R] [BEq R] [LawfulBEq R] [DecidableEq R]
    (p q : CPolynomial R) :
    CPolynomial.gcdMonic p q = (CPolynomial.normXgcd p q).1
```

`CompPoly.CPolynomial.normXgcd_snd_toPoly` (theorem, [line 349](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/EuclideanAlgorithm.lean#L349))

> The Bezout component of `normXgcd` under `toPoly` is Mathlib's
> `EuclideanDomain.xgcd` scaled by the inverse leading coefficient
> of the gcd

```lean
theorem normXgcd_snd_toPoly
    [Field R] [BEq R] [LawfulBEq R] [DecidableEq R]
    (p q : CPolynomial R) :
    (normXgcd p q).2.map (·.toPoly) (·.toPoly) =
      (EuclideanDomain.gcd p.toPoly q.toPoly).leadingCoeff⁻¹ •
        EuclideanDomain.xgcd p.toPoly q.toPoly
```

`CompPoly.CPolynomial.normXgcd_fst_comm` (theorem, [line 360](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/EuclideanAlgorithm.lean#L360))

> `normXgcd` is commutative for the gcd component

```lean
theorem normXgcd_fst_comm
    [Field R] [BEq R] [LawfulBEq R] [DecidableEq R]
    (p q : CPolynomial R) :
    (normXgcd p q).1 = (normXgcd q p).1
```

> ## Stop specification for positive thresholds
>
> `BezoutDegreeInvariant` is the invariant of the partial-EEA (`xgcd`) loop: each non-stop
> step preserves it (`BezoutDegreeInvariant.step`), and at the stopping threshold it yields
> the output specification `BezoutStopSpec` (`xgcd_stopSpec`).
>
> This is the classical degree theory of the extended Euclidean algorithm — the row identity
> `deg t + deg r' = deg g₀` and the complementary cofactor bound at the stop — i.e. the
> contract behind rational-function reconstruction and Reed-Solomon decoding.

`CompPoly.BezoutDegreeInvariant` (structure, [line 395](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/EuclideanAlgorithm.lean#L395))

> Loop invariant of one partial-EEA (`xgcd`) step.

```lean
structure BezoutDegreeInvariant [Ring F] (g₀ g₁ : F[X]) (threshold : ℕ)
    (r s t r' s' t' : F[X]) : Prop where
  bez : r = s * g₀ + t * g₁
  bez' : r' = s' * g₀ + t' * g₁
  det : IsUnit (s' * t - s * t')
  degt : t'.degree < t.degree
  degr : r.degree < r'.degree
  thr : threshold ≤ r'.degree
```

`CompPoly.BezoutDegreeInvariantOf` (abbreviation, [line 406](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/EuclideanAlgorithm.lean#L406))

> `BezoutDegreeInvariant` on the `toPoly` images of a `CPolynomial` reference pair `g₀, g₁` and
> the two state triples `(r, s, t)`, `(r', s', t')`.

```lean
abbrev BezoutDegreeInvariantOf [Ring F] (g₀ g₁ : CPolynomial F) (threshold : ℕ)
    (r s t r' s' t' : CPolynomial F) : Prop
```

`CompPoly.BezoutDegreeInvariant.degree_complement` (lemma, [line 412](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/EuclideanAlgorithm.lean#L412))

> `BezoutDegreeInvariant` implies `deg t + deg r' = deg g₀`.

```lean
lemma BezoutDegreeInvariant.degree_complement [CommRing F] [NoZeroDivisors F] [Nontrivial F]
    {g₀ g₁ : F[X]} {threshold : ℕ} {r s t r' s' t' : F[X]}
    (h : BezoutDegreeInvariant g₀ g₁ threshold r s t r' s' t') :
    t.degree + r'.degree = g₀.degree
```

`CompPoly.BezoutDegreeInvariant.step` (lemma, [line 432](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/EuclideanAlgorithm.lean#L432))

> A non-stop Euclidean step preserves the invariant.

```lean
lemma BezoutDegreeInvariant.step [Field F]
    {g₀ g₁ : F[X]} {threshold : ℕ} {r s t r' s' t' : F[X]}
    (h : BezoutDegreeInvariant g₀ g₁ threshold r s t r' s' t') (hr : r ≠ 0)
    (hstop : ¬ r.natDegree < threshold) :
    BezoutDegreeInvariant
      g₀ g₁ threshold (r' - r' / r * r) (s' - r' / r * s) (t' - r' / r * t) r s t
```

`CompPoly.BezoutStopSpec` (structure, [line 446](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/EuclideanAlgorithm.lean#L446))

> Stop spec of the partial EEA: `R = S g₀ + T g₁`, residue degree below `threshold`,
> and the cofactor `T` nonzero with complementary degree `deg T + threshold ≤ deg g₀`.

```lean
structure BezoutStopSpec [Semiring F] (g₀ g₁ : F[X]) (threshold : ℕ) (R S T : F[X]) : Prop where
  bez : R = S * g₀ + T * g₁
  resDeg : R.natDegree < threshold
  cofDeg : T.degree + threshold ≤ g₀.degree
  cofNe : T ≠ 0
```

`CompPoly.BezoutStopSpecOf` (abbreviation, [line 454](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/EuclideanAlgorithm.lean#L454))

> `BezoutStopSpec` on the `toPoly` images of a `CPolynomial` reference pair `g₀, g₁` and
> result triple.

```lean
abbrev BezoutStopSpecOf [Semiring F] (g₀ g₁ : CPolynomial F) (threshold : ℕ)
    (result : CPolynomial F × CPolynomial F × CPolynomial F) : Prop
```

`CompPoly.xgcdAux_stopSpec_of_invariant` (lemma, [line 460](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/EuclideanAlgorithm.lean#L460))

> `BezoutDegreeInvariant` implies `xgcdAux`'s output satisfies the stop spec.

```lean
lemma xgcdAux_stopSpec_of_invariant
    [Field F] [BEq F] [LawfulBEq F] (g₀ g₁ : CPolynomial F) (threshold : ℕ) (hthr : 1 ≤ threshold)
    (hg₀ : g₀.toPoly ≠ 0) :
    ∀ (n : ℕ) (r s t r' s' t' : CPolynomial F),
      BezoutDegreeInvariantOf g₀ g₁ threshold r s t r' s' t' →
      r.natDegree < n →
      BezoutStopSpecOf g₀ g₁ threshold (xgcdAux threshold n r s t r' s' t')
```

`CompPoly.xgcd_stopSpec` (lemma, [line 488](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/EuclideanAlgorithm.lean#L488))

> `xgcd`'s output satisfies the stop spec.

```lean
lemma xgcd_stopSpec
    [Field F] [BEq F] [LawfulBEq F] (g₀ g₁ : CPolynomial F) (threshold : ℕ)
    (hdeg : g₁.degree < g₀.degree)
    (hthr : 1 ≤ threshold) (hthr' : threshold ≤ g₀.degree) :
    BezoutStopSpecOf g₀ g₁ threshold (xgcd g₀ g₁ threshold)
```

## Depends on

- [Computable Univariate To `Polynomial`](../part-02/topoly/core.md)

## Proof depends on

- [Strict additive monotonicity on `WithBot ℕ`](../../tomathlib/order/withbot.md)
- [Univariate Division Correctness](divisioncorrectness.md)

## Sources

- [CompPoly/Univariate/EuclideanAlgorithm.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/EuclideanAlgorithm.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Univariate.EuclideanAlgorithm.json)
