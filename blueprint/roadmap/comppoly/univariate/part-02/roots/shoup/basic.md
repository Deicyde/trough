---
catalog: module
lean: CompPoly.CPolynomial.Roots.FiniteField.tracePowerSum, CompPoly.CPolynomial.Roots.FiniteField.tracePowerSum_eq_sum_range, CompPoly.CPolynomial.Roots.FiniteField.SmallPrimeTraceContext, CompPoly.CPolynomial.Roots.FiniteField.shoupSplitterInput, CompPoly.CPolynomial.Roots.FiniteField.modularXPowersWith, CompPoly.CPolynomial.Roots.FiniteField.traceCoordinatePolynomialFromPowers, CompPoly.CPolynomial.Roots.FiniteField.traceCoordinatePolynomialWith, CompPoly.CPolynomial.Roots.FiniteField.pushNontrivialChild, CompPoly.CPolynomial.Roots.FiniteField.shoupRefineFactorWith, CompPoly.CPolynomial.Roots.FiniteField.shoupRefineFactorsWith, CompPoly.CPolynomial.Roots.FiniteField.ShoupTracePowerCache, CompPoly.CPolynomial.Roots.FiniteField.lookupTracePowers, CompPoly.CPolynomial.Roots.FiniteField.tracePowersWithCache, CompPoly.CPolynomial.Roots.FiniteField.shoupRefineFactorCachedWith, CompPoly.CPolynomial.Roots.FiniteField.shoupRefineFactorsCachedWith, CompPoly.CPolynomial.Roots.FiniteField.shoupRefineBasisCachedWith, CompPoly.CPolynomial.Roots.FiniteField.shoupSplitCandidatesCachedWith, CompPoly.CPolynomial.Roots.FiniteField.representedLinearFactorsOnly, CompPoly.CPolynomial.Roots.FiniteField.representedLinearFactorsOnly_sound, CompPoly.CPolynomial.Roots.FiniteField.representedLinearFactorsOnly_mem_of_mem, CompPoly.CPolynomial.Roots.FiniteField.shoupSplitCandidatesWith, CompPoly.CPolynomial.Roots.FiniteField.ShoupTracePowerCache.Valid, CompPoly.CPolynomial.Roots.FiniteField.ShoupTracePowerCache.valid_nil, CompPoly.CPolynomial.Roots.FiniteField.lookupTracePowers_eq, CompPoly.CPolynomial.Roots.FiniteField.tracePowersWithCache_spec, CompPoly.CPolynomial.Roots.FiniteField.shoupRefineFactorCachedWith_spec, CompPoly.CPolynomial.Roots.FiniteField.shoupRefineFactorsCachedWith_spec, CompPoly.CPolynomial.Roots.FiniteField.shoupRefineBasisCachedWith_eq, CompPoly.CPolynomial.Roots.FiniteField.shoupSplitCandidatesWith_eq_cached, CompPoly.CPolynomial.Roots.FiniteField.shoupSplitLinearFactorsWith, CompPoly.CPolynomial.Roots.FiniteField.shoupSplitLinearFactorsWith_sound
statement: formalized
proof: formalized
---

# Shoup-Style Small-Characteristic Linear-Factor Splitting

`CompPoly.Univariate.Roots.Shoup.Basic`, in [CompPoly/Univariate/Roots/Shoup/Basic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Basic.lean), by Valerii Huhnin.

> Executable trace-coordinate splitter for finite-field root products over fields
> presented as `GF(p^k)` with small base characteristic `p`. The splitter refines a
> valid root product by `k` trace coordinates and the `p` embedded base constants;
> it does not enumerate all `p^k` field elements, following the small-characteristic
> Frobenius-map factoring method of von zur Gathen and Shoup [vzGS92].
>
> ## References
>
> * [J. von zur Gathen and Victor Shoup, *Computing Frobenius maps and factoring
>     polynomials*, Computational Complexity 2, 187-224, 1992][vzGS92]

`CompPoly.CPolynomial.Roots.FiniteField.tracePowerSum` (definition, [line 39](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Basic.lean#L39))

> Trace power sum `z + z^p + ... + z^(p^(k-1))`.

```lean
def tracePowerSum {F : Type*} [Field F] (p k : Nat) (z : F) : F
```

`CompPoly.CPolynomial.Roots.FiniteField.tracePowerSum_eq_sum_range` (theorem, [line 43](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Basic.lean#L43))

> The list-fold trace power sum is the corresponding finite range sum.

```lean
theorem tracePowerSum_eq_sum_range {F : Type*} [Field F] (p k : Nat) (z : F) :
    tracePowerSum p k z = ∑ i ∈ Finset.range k, z ^ (p ^ i)
```

`CompPoly.CPolynomial.Roots.FiniteField.SmallPrimeTraceContext` (structure, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Basic.lean#L60))

> Executable and proof data for a Shoup-style small-characteristic trace splitter.
>
> The field-theoretic facts are carried by the context so the generic executable
> splitter can stay representation-independent. Concrete fields can discharge the
> trace-image and separating-basis obligations using their own basis libraries.

```lean
structure SmallPrimeTraceContext (F : Type*) [Field F] [BEq F] [LawfulBEq F]
    extends FiniteFieldContext F where
  p : Nat
  k : Nat
  p_prime : Nat.Prime p
  q_eq : q = p ^ k
  baseConstants : Array F
  baseConstants_size : baseConstants.size = p
  basis : Array F
  basis_size : basis.size = k
  traceValue : F → F
  traceValue_eq_powerSum : ∀ z, traceValue z = tracePowerSum p k z
  traceValue_mem_base : ∀ z, traceValue z ∈ baseConstants.toList
  trace_separates :
    ∀ {a b : F}, a ≠ b →
      ∃ beta, beta ∈ basis.toList ∧ traceValue (beta * (a - b)) ≠ 0
```

`CompPoly.CPolynomial.Roots.FiniteField.shoupSplitterInput` (definition, [line 84](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Basic.lean#L84))

> Input predicate for the Shoup splitter.
>
> Completeness is only claimed for nonzero products of distinct field-linear
> factors, represented here by divisibility into `X^q - X`. This is the contract
> satisfied by the finite-field root product, not by arbitrary input polynomials.

```lean
def shoupSplitterInput {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (ctx : SmallPrimeTraceContext F) (p : CPolynomial F) : Prop
```

`CompPoly.CPolynomial.Roots.FiniteField.modularXPowersWith` (definition, [line 90](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Basic.lean#L90))

> Modular powers `X^(p^i) mod modulus` for `0 ≤ i < k`.

```lean
def modularXPowersWith {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (modulus : CPolynomial F) (p k : Nat) : Array (CPolynomial F)
```

`CompPoly.CPolynomial.Roots.FiniteField.traceCoordinatePolynomialFromPowers` (definition, [line 96](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Basic.lean#L96))

> `Trace(beta * X) mod modulus`, using precomputed modular Frobenius powers.

```lean
def traceCoordinatePolynomialFromPowers {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (ctx : SmallPrimeTraceContext F) (beta : F)
    (powers : Array (CPolynomial F)) :
    CPolynomial F
```

`CompPoly.CPolynomial.Roots.FiniteField.traceCoordinatePolynomialWith` (definition, [line 107](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Basic.lean#L107))

> `Trace(beta * X) mod modulus`, built from the modular Frobenius powers.

```lean
def traceCoordinatePolynomialWith {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : SmallPrimeTraceContext F) (modulus : CPolynomial F) (beta : F) :
    CPolynomial F
```

`CompPoly.CPolynomial.Roots.FiniteField.pushNontrivialChild` (definition, [line 166](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Basic.lean#L166))

> Drop zero/unit children and keep the remaining monic gcd child.

```lean
def pushNontrivialChild {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (children : Array (CPolynomial F)) (child : CPolynomial F) :
    Array (CPolynomial F)
```

`CompPoly.CPolynomial.Roots.FiniteField.shoupRefineFactorWith` (definition, [line 172](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Basic.lean#L172))

> Refine one current factor by one trace coordinate and all base constants.

```lean
def shoupRefineFactorWith {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : SmallPrimeTraceContext F) (beta : F) (u : CPolynomial F) :
    Array (CPolynomial F)
```

`CompPoly.CPolynomial.Roots.FiniteField.shoupRefineFactorsWith` (definition, [line 192](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Basic.lean#L192))

> Refine all current factors by one trace coordinate.

```lean
def shoupRefineFactorsWith {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : SmallPrimeTraceContext F) (beta : F) (factors : Array (CPolynomial F)) :
    Array (CPolynomial F)
```

`CompPoly.CPolynomial.Roots.FiniteField.ShoupTracePowerCache` (abbreviation, [line 202](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Basic.lean#L202))

> Modular Frobenius powers `X^(p^i) mod u` already computed, keyed by the modulus `u`.

```lean
abbrev ShoupTracePowerCache (F : Type*) [Field F] [BEq F] [LawfulBEq F]
```

`CompPoly.CPolynomial.Roots.FiniteField.lookupTracePowers` (definition, [line 206](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Basic.lean#L206))

> The cached Frobenius powers for `u`, if present.

```lean
def lookupTracePowers {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (u : CPolynomial F) :
    ShoupTracePowerCache F → Option (Array (CPolynomial F))
```

`CompPoly.CPolynomial.Roots.FiniteField.tracePowersWithCache` (definition, [line 217](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Basic.lean#L217))

> The Frobenius powers for `u`, from the cache or computed and added to it.

```lean
def tracePowersWithCache {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : SmallPrimeTraceContext F) (u : CPolynomial F)
    (cache : ShoupTracePowerCache F) :
    Array (CPolynomial F) × ShoupTracePowerCache F
```

`CompPoly.CPolynomial.Roots.FiniteField.shoupRefineFactorCachedWith` (definition, [line 229](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Basic.lean#L229))

> `shoupRefineFactorWith` reading and extending a Frobenius-power cache.

```lean
def shoupRefineFactorCachedWith {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : SmallPrimeTraceContext F) (beta : F)
    (cache : ShoupTracePowerCache F) (u : CPolynomial F) :
    ShoupTracePowerCache F × Array (CPolynomial F)
```

`CompPoly.CPolynomial.Roots.FiniteField.shoupRefineFactorsCachedWith` (definition, [line 253](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Basic.lean#L253))

> `shoupRefineFactorsWith` threading a Frobenius-power cache.

```lean
def shoupRefineFactorsCachedWith {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : SmallPrimeTraceContext F) (beta : F)
    (cache : ShoupTracePowerCache F) (factors : Array (CPolynomial F)) :
    ShoupTracePowerCache F × Array (CPolynomial F)
```

`CompPoly.CPolynomial.Roots.FiniteField.shoupRefineBasisCachedWith` (definition, [line 267](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Basic.lean#L267))

> Refine by every trace coordinate in `basis`, threading a Frobenius-power cache.

```lean
def shoupRefineBasisCachedWith {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : SmallPrimeTraceContext F) (basis : List F)
    (cache : ShoupTracePowerCache F) (factors : Array (CPolynomial F)) :
    Array (CPolynomial F)
```

`CompPoly.CPolynomial.Roots.FiniteField.shoupSplitCandidatesCachedWith` (definition, [line 284](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Basic.lean#L284))

> Compiled form of `shoupSplitCandidatesWith`. A factor that survives a refinement
> round unchanged reuses its Frobenius powers from the cache instead of recomputing
> them. `shoupSplitCandidatesWith_eq_cached` proves the two equal.

```lean
def shoupSplitCandidatesCachedWith {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : SmallPrimeTraceContext F) (p : CPolynomial F) :
    Array (CPolynomial F)
```

`CompPoly.CPolynomial.Roots.FiniteField.representedLinearFactorsOnly` (definition, [line 298](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Basic.lean#L298))

> Final linear-only filter for the splitter interface's unconditional soundness field.

```lean
def representedLinearFactorsOnly {F : Type*} [Field F] [BEq F]
    (factors : Array (CPolynomial F)) : Array (CPolynomial F)
```

`CompPoly.CPolynomial.Roots.FiniteField.representedLinearFactorsOnly_sound` (theorem, [line 337](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Basic.lean#L337))

> The final Shoup filter only keeps represented linear factors.

```lean
theorem representedLinearFactorsOnly_sound {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    {factors : Array (CPolynomial F)} {factor : CPolynomial F}
    (h : factor ∈ (representedLinearFactorsOnly factors).toList) :
    IsLinearFactor factor
```

`CompPoly.CPolynomial.Roots.FiniteField.representedLinearFactorsOnly_mem_of_mem` (theorem, [line 404](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Basic.lean#L404))

> The final linear-factor filter keeps represented factors that were already present.

```lean
theorem representedLinearFactorsOnly_mem_of_mem {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    {factors : Array (CPolynomial F)} {factor : CPolynomial F}
    (hmem : factor ∈ factors.toList)
    (hlin : isRepresentedLinearFactor factor = true) :
    factor ∈ (representedLinearFactorsOnly factors).toList
```

`CompPoly.CPolynomial.Roots.FiniteField.shoupSplitCandidatesWith` (definition, [line 415](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Basic.lean#L415))

> Trace-coordinate refinement candidates before the final linear-only filter.

```lean
def shoupSplitCandidatesWith {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : SmallPrimeTraceContext F) (p : CPolynomial F) :
    Array (CPolynomial F)
```

`CompPoly.CPolynomial.Roots.FiniteField.ShoupTracePowerCache.Valid` (definition, [line 431](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Basic.lean#L431))

> Every cache entry holds the Frobenius powers of its own key.

```lean
def ShoupTracePowerCache.Valid {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : SmallPrimeTraceContext F) (cache : ShoupTracePowerCache F) : Prop
```

`CompPoly.CPolynomial.Roots.FiniteField.ShoupTracePowerCache.valid_nil` (theorem, [line 437](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Basic.lean#L437))

> The empty cache is valid.

```lean
theorem ShoupTracePowerCache.valid_nil {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : SmallPrimeTraceContext F) :
    ShoupTracePowerCache.Valid M D ctx []
```

`CompPoly.CPolynomial.Roots.FiniteField.lookupTracePowers_eq` (theorem, [line 445](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Basic.lean#L445))

> A hit in a valid cache returns the Frobenius powers of the queried modulus.

```lean
theorem lookupTracePowers_eq {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    {M : CPolynomial.Raw.MulContext F} {D : CPolynomial.Raw.ModContext F}
    {ctx : SmallPrimeTraceContext F} {u : CPolynomial F} {powers : Array (CPolynomial F)} :
    ∀ {cache : ShoupTracePowerCache F}, cache.Valid M D ctx →
      lookupTracePowers u cache = some powers →
        powers = modularXPowersWith M D u ctx.p ctx.k
  | [], _, h => by simp [lookupTracePowers] at h
  | (v, vs) :: rest, hvalid, h => by
      unfold lookupTracePowers at h
      by_cases huv : u = v
      · subst huv
        rw [ite_eq_left (beq_self_eq_true u)] at h
        obtain rfl
```

`CompPoly.CPolynomial.Roots.FiniteField.tracePowersWithCache_spec` (theorem, [line 463](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Basic.lean#L463))

> Reading through a valid cache returns the Frobenius powers and keeps the cache valid.

```lean
theorem tracePowersWithCache_spec {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : SmallPrimeTraceContext F) (u : CPolynomial F)
    {cache : ShoupTracePowerCache F} (hvalid : cache.Valid M D ctx) :
    (tracePowersWithCache M D ctx u cache).1 = modularXPowersWith M D u ctx.p ctx.k ∧
      (tracePowersWithCache M D ctx u cache).2.Valid M D ctx
```

`CompPoly.CPolynomial.Roots.FiniteField.shoupRefineFactorCachedWith_spec` (theorem, [line 481](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Basic.lean#L481))

> The cached single-factor refinement matches `shoupRefineFactorWith`.

```lean
theorem shoupRefineFactorCachedWith_spec {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : SmallPrimeTraceContext F) (beta : F) (u : CPolynomial F)
    {cache : ShoupTracePowerCache F} (hvalid : cache.Valid M D ctx) :
    (shoupRefineFactorCachedWith M D ctx beta cache u).2 =
        shoupRefineFactorWith M D ctx beta u ∧
      (shoupRefineFactorCachedWith M D ctx beta cache u).1.Valid M D ctx
```

`CompPoly.CPolynomial.Roots.FiniteField.shoupRefineFactorsCachedWith_spec` (theorem, [line 506](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Basic.lean#L506))

> The cached refinement of a factor array matches `shoupRefineFactorsWith`.

```lean
theorem shoupRefineFactorsCachedWith_spec {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : SmallPrimeTraceContext F) (beta : F) (factors : Array (CPolynomial F))
    {cache : ShoupTracePowerCache F} (hvalid : cache.Valid M D ctx) :
    (shoupRefineFactorsCachedWith M D ctx beta cache factors).2 =
        shoupRefineFactorsWith M D ctx beta factors ∧
      (shoupRefineFactorsCachedWith M D ctx beta cache factors).1.Valid M D ctx
```

`CompPoly.CPolynomial.Roots.FiniteField.shoupRefineBasisCachedWith_eq` (theorem, [line 546](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Basic.lean#L546))

> From a valid cache, the cached basis loop is the uncached fold over the basis.

```lean
theorem shoupRefineBasisCachedWith_eq {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : SmallPrimeTraceContext F) :
    ∀ (basis : List F) {cache : ShoupTracePowerCache F} (factors : Array (CPolynomial F)),
      cache.Valid M D ctx →
      shoupRefineBasisCachedWith M D ctx basis cache factors =
        basis.foldl (fun factors beta ↦ shoupRefineFactorsWith M D ctx beta factors) factors
  | [], _, _, _ => rfl
  | beta :: basis, cache, factors, hvalid => by
      obtain ⟨hfactors, hvalid'⟩
```

`CompPoly.CPolynomial.Roots.FiniteField.shoupSplitCandidatesWith_eq_cached` (theorem, [line 568](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Basic.lean#L568))

> The cached splitter computes the specification; compiled code runs the cached one.

```lean
theorem shoupSplitCandidatesWith_eq_cached :
    @shoupSplitCandidatesWith = @shoupSplitCandidatesCachedWith
```

`CompPoly.CPolynomial.Roots.FiniteField.shoupSplitLinearFactorsWith` (definition, [line 581](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Basic.lean#L581))

> Shoup trace-coordinate splitting, returning only represented linear factors.

```lean
def shoupSplitLinearFactorsWith {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : SmallPrimeTraceContext F) (p : CPolynomial F) :
    Array (CPolynomial F)
```

`CompPoly.CPolynomial.Roots.FiniteField.shoupSplitLinearFactorsWith_sound` (theorem, [line 589](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Basic.lean#L589))

> Soundness of the final Shoup linear-factor array.

```lean
theorem shoupSplitLinearFactorsWith_sound {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : SmallPrimeTraceContext F) {p factor : CPolynomial F}
    (h : factor ∈ (shoupSplitLinearFactorsWith M D ctx p).toList) :
    IsLinearFactor factor
```

## Depends on

- [Linear-Factor Splitter Helpers](../splitter.md)
- [Computable Univariate To `Polynomial`](../../topoly/core.md)

## Sources

- [CompPoly/Univariate/Roots/Shoup/Basic.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Shoup/Basic.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Univariate.Roots.Shoup.Basic.json)
