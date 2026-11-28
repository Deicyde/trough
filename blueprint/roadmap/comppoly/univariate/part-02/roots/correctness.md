---
catalog: module
lean: CompPoly.CPolynomial.monicNormalize_root_iff, CompPoly.CPolynomial.monicNormalize_root_of_root, CompPoly.CPolynomial.toPoly_monicNormalize_dvd_self, CompPoly.CPolynomial.gcdMonic_root_of_left_right, CompPoly.CPolynomial.toPoly_gcdMonic_dvd_left, CompPoly.CPolynomial.toPoly_gcdMonic_dvd_right, CompPoly.CPolynomial.gcdMonic_root_iff_left_right, CompPoly.CPolynomial.eval_div_eq_zero_of_dvd_of_root_of_ne_root, CompPoly.CPolynomial.monicNormalize_div_root_of_dvd_of_root_of_ne_root, CompPoly.CPolynomial.normXgcd_root_of_left_right, CompPoly.CPolynomial.eval_gcdMonic_eq_zero_iff_normXgcd_fst_eq_zero, CompPoly.CPolynomial.normXgcd_fst_root_of_left_right, CompPoly.CPolynomial.linearRootOfFactor?_sound, CompPoly.CPolynomial.mem_validateRootCandidates_eval_eq_zero, CompPoly.CPolynomial.Roots.FiniteField.raw_eval_powModWith_eq_pow, CompPoly.CPolynomial.Roots.FiniteField.finiteFieldRootProductWith_complete, CompPoly.CPolynomial.Roots.FiniteField.finiteFieldRootProduct_complete, CompPoly.CPolynomial.Roots.FiniteField.finiteFieldRootProduct_validated_sound, CompPoly.CPolynomial.Roots.FiniteField.rootsInFiniteFieldWith_sound, CompPoly.CPolynomial.Roots.FiniteField.rootsInFiniteField_sound, CompPoly.CPolynomial.Roots.FiniteField.linearFactor_isLinearFactor, CompPoly.CPolynomial.Roots.FiniteField.linearFactor_isRepresentedLinearFactor, CompPoly.CPolynomial.Roots.FiniteField.linearFactor_isRootFactorCandidate, CompPoly.CPolynomial.Roots.FiniteField.representedLinearFactor_candidate_of_root, CompPoly.CPolynomial.Roots.FiniteField.eval_xPowModWith_eq_pow, CompPoly.CPolynomial.Roots.FiniteField.rootsInFiniteFieldWith_complete, CompPoly.CPolynomial.Roots.FiniteField.rootsInFiniteField_complete, CompPoly.CPolynomial.Roots.FiniteField.rootsInFiniteField_spec
statement: formalized
proof: formalized
---

# Finite-Field Root Correctness

`CompPoly.Univariate.Roots.Correctness`, in [CompPoly/Univariate/Roots/Correctness.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Correctness.lean), by Valerii Huhnin.

> Theorem statements and certified context constructors for the executable
> finite-field root backend.

`CompPoly.CPolynomial.monicNormalize_root_iff` (theorem, [line 196](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Correctness.lean#L196))

> Monic normalization preserves roots of nonzero polynomials.

```lean
theorem monicNormalize_root_iff {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    {p : CPolynomial F} {a : F} (hp : p ≠ 0) :
    CPolynomial.eval a (monicNormalize p) = 0 ↔ CPolynomial.eval a p = 0
```

`CompPoly.CPolynomial.monicNormalize_root_of_root` (theorem, [line 242](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Correctness.lean#L242))

> Monic normalization preserves roots, including the zero polynomial case.

```lean
theorem monicNormalize_root_of_root {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    {p : CPolynomial F} {a : F} (hp : CPolynomial.eval a p = 0) :
    CPolynomial.eval a (monicNormalize p) = 0
```

`CompPoly.CPolynomial.toPoly_monicNormalize_dvd_self` (theorem, [line 251](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Correctness.lean#L251))

> The normalized polynomial divides the original polynomial.

```lean
theorem toPoly_monicNormalize_dvd_self {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (p : CPolynomial F) :
    (CPolynomial.monicNormalize p).toPoly ∣ p.toPoly
```

`CompPoly.CPolynomial.gcdMonic_root_of_left_right` (theorem, [line 260](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Correctness.lean#L260))

> The monic gcd contains every common root.

```lean
theorem gcdMonic_root_of_left_right {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    {p q : CPolynomial F} {a : F}
    (hp : CPolynomial.eval a p = 0) (hq : CPolynomial.eval a q = 0) :
    CPolynomial.eval a (gcdMonic p q) = 0
```

`CompPoly.CPolynomial.toPoly_gcdMonic_dvd_left` (theorem, [line 271](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Correctness.lean#L271))

> The monic gcd divides its left operand.

```lean
theorem toPoly_gcdMonic_dvd_left {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (p q : CPolynomial F) :
    (CPolynomial.gcdMonic p q).toPoly ∣ p.toPoly
```

`CompPoly.CPolynomial.toPoly_gcdMonic_dvd_right` (theorem, [line 281](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Correctness.lean#L281))

> The monic gcd divides its right operand.

```lean
theorem toPoly_gcdMonic_dvd_right {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (p q : CPolynomial F) :
    (CPolynomial.gcdMonic p q).toPoly ∣ q.toPoly
```

`CompPoly.CPolynomial.gcdMonic_root_iff_left_right` (theorem, [line 291](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Correctness.lean#L291))

> The monic gcd vanishes exactly at common roots.

```lean
theorem gcdMonic_root_iff_left_right {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {p q : CPolynomial F} {a : F} :
    CPolynomial.eval a (gcdMonic p q) = 0 ↔
      CPolynomial.eval a p = 0 ∧ CPolynomial.eval a q = 0
```

`CompPoly.CPolynomial.eval_div_eq_zero_of_dvd_of_root_of_ne_root` (theorem, [line 322](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Correctness.lean#L322))

> A root of a dividend is a root of the exact quotient when the divisor does
> not vanish at that point.

```lean
theorem eval_div_eq_zero_of_dvd_of_root_of_ne_root {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    {p q : CPolynomial F} {a : F}
    (hdiv : q.toPoly ∣ p.toPoly)
    (hp : CPolynomial.eval a p = 0)
    (hq : CPolynomial.eval a q ≠ 0) :
    CPolynomial.eval a (p / q) = 0
```

`CompPoly.CPolynomial.monicNormalize_div_root_of_dvd_of_root_of_ne_root` (theorem, [line 348](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Correctness.lean#L348))

> Monic normalization of an exact quotient preserves the quotient root from
> `eval_div_eq_zero_of_dvd_of_root_of_ne_root`.

```lean
theorem monicNormalize_div_root_of_dvd_of_root_of_ne_root {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    {p q : CPolynomial F} {a : F}
    (hdiv : q.toPoly ∣ p.toPoly)
    (hp : CPolynomial.eval a p = 0)
    (hq : CPolynomial.eval a q ≠ 0) :
    CPolynomial.eval a (CPolynomial.monicNormalize (p / q)) = 0
```

`CompPoly.CPolynomial.normXgcd_root_of_left_right` (theorem, [line 359](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Correctness.lean#L359))

> The normalized extended gcd contains every common root.

```lean
theorem normXgcd_root_of_left_right {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    {p q : CPolynomial F} {a : F}
    (hp : CPolynomial.eval a p = 0) (hq : CPolynomial.eval a q = 0) :
    CPolynomial.eval a (normXgcd p q).1 = 0
```

`CompPoly.CPolynomial.eval_gcdMonic_eq_zero_iff_normXgcd_fst_eq_zero` (theorem, [line 374](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Correctness.lean#L374))

> The specialized monic gcd and normalized extended gcd have the same root
> predicate.

```lean
theorem eval_gcdMonic_eq_zero_iff_normXgcd_fst_eq_zero
    {F : Type*} [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (a : F) (p q : CPolynomial F) :
    CPolynomial.eval a (CPolynomial.gcdMonic p q) = 0 ↔
      CPolynomial.eval a ((CPolynomial.normXgcd p q).1) = 0
```

`CompPoly.CPolynomial.normXgcd_fst_root_of_left_right` (theorem, [line 382](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Correctness.lean#L382))

> The normalized extended-gcd first component contains every common root.

```lean
theorem normXgcd_fst_root_of_left_right
    {F : Type*} [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {a : F} {p q : CPolynomial F}
    (hp : CPolynomial.eval a p = 0)
    (hq : CPolynomial.eval a q = 0) :
    CPolynomial.eval a ((CPolynomial.normXgcd p q).1) = 0
```

`CompPoly.CPolynomial.linearRootOfFactor?_sound` (theorem, [line 391](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Correctness.lean#L391))

> Roots extracted from a linear factor satisfy that factor.

```lean
theorem linearRootOfFactor?_sound {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    {factor : CPolynomial F} {a : F}
    (h : linearRootOfFactor? factor = some a) :
    CPolynomial.eval a factor = 0
```

`CompPoly.CPolynomial.mem_validateRootCandidates_eval_eq_zero` (theorem, [line 412](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Correctness.lean#L412))

> Validation makes returned candidates sound for the original polynomial.

```lean
theorem mem_validateRootCandidates_eval_eq_zero {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    {p : CPolynomial F} {candidates : Array F} {a : F}
    (h : a ∈ (validateRootCandidates p candidates).toList) :
    CPolynomial.eval a p = 0
```

`CompPoly.CPolynomial.Roots.FiniteField.raw_eval_powModWith_eq_pow` (theorem, [line 743](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Correctness.lean#L743))

> Raw modular exponentiation evaluates as ordinary exponentiation at roots of
> the modulus.

```lean
theorem raw_eval_powModWith_eq_pow {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    {modulus base : CPolynomial.Raw F} {a : F}
    (hmod : modulus.eval a = 0) (q : Nat) :
    (CPolynomial.Raw.powModWith M D modulus base q).eval a =
      base.eval a ^ q
```

`CompPoly.CPolynomial.Roots.FiniteField.finiteFieldRootProductWith_complete` (theorem, [line 799](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Correctness.lean#L799))

> Every root of `p` is a root of the finite-field root product.

```lean
theorem finiteFieldRootProductWith_complete {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : FiniteFieldContext F) {p : CPolynomial F} {a : F}
    (hp : p ≠ 0) (hroot : CPolynomial.eval a p = 0) :
    CPolynomial.eval a (finiteFieldRootProductWith M D ctx p) = 0
```

`CompPoly.CPolynomial.Roots.FiniteField.finiteFieldRootProduct_complete` (theorem, [line 829](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Correctness.lean#L829))

> Every root of `p` is a root of the finite-field root product.

```lean
theorem finiteFieldRootProduct_complete {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (ctx : FiniteFieldContext F) {p : CPolynomial F} {a : F}
    (hp : p ≠ 0) (hroot : CPolynomial.eval a p = 0) :
    CPolynomial.eval a (finiteFieldRootProduct ctx p) = 0
```

`CompPoly.CPolynomial.Roots.FiniteField.finiteFieldRootProduct_validated_sound` (theorem, [line 860](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Correctness.lean#L860))

> Every validated root extracted from the root product is a root of `p`.

```lean
theorem finiteFieldRootProduct_validated_sound {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (_ctx : FiniteFieldContext F) {p : CPolynomial F}
    {candidates : Array F} {a : F}
    (h : a ∈ (CPolynomial.validateRootCandidates p candidates).toList) :
    CPolynomial.eval a p = 0
```

`CompPoly.CPolynomial.Roots.FiniteField.rootsInFiniteFieldWith_sound` (theorem, [line 869](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Correctness.lean#L869))

> Returned finite-field roots are roots of the original polynomial.

```lean
theorem rootsInFiniteFieldWith_sound {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : FiniteFieldContext F) (splitter : LinearFactorProductSplitter F)
    {p : CPolynomial F} {a : F}
    (h : a ∈ (rootsInFiniteFieldWith M D ctx splitter p).toList) :
    CPolynomial.eval a p = 0
```

`CompPoly.CPolynomial.Roots.FiniteField.rootsInFiniteField_sound` (theorem, [line 886](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Correctness.lean#L886))

> Returned finite-field roots are roots of the original polynomial.

```lean
theorem rootsInFiniteField_sound {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (ctx : FiniteFieldContext F) (splitter : LinearFactorProductSplitter F)
    {p : CPolynomial F} {a : F}
    (h : a ∈ (rootsInFiniteField ctx splitter p).toList) :
    CPolynomial.eval a p = 0
```

`CompPoly.CPolynomial.Roots.FiniteField.linearFactor_isLinearFactor` (theorem, [line 939](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Correctness.lean#L939))

> Every explicit `X - a` factor is represented as a nonconstant linear factor.

```lean
theorem linearFactor_isLinearFactor {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (a : F) : IsLinearFactor (CPolynomial.linearFactor a)
```

`CompPoly.CPolynomial.Roots.FiniteField.linearFactor_isRepresentedLinearFactor` (theorem, [line 962](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Correctness.lean#L962))

> The represented-linear recognizer accepts every explicit `X - a` factor.

```lean
theorem linearFactor_isRepresentedLinearFactor {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (a : F) : isRepresentedLinearFactor (CPolynomial.linearFactor a) = true
```

`CompPoly.CPolynomial.Roots.FiniteField.linearFactor_isRootFactorCandidate` (theorem, [line 972](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Correctness.lean#L972))

> The explicit `X - a` factor represents the root `a`.

```lean
theorem linearFactor_isRootFactorCandidate {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (a : F) : IsLinearRootFactorCandidate (CPolynomial.linearFactor a) a
```

`CompPoly.CPolynomial.Roots.FiniteField.representedLinearFactor_candidate_of_root` (theorem, [line 987](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Correctness.lean#L987))

> If the represented-linear recognizer accepts `p`, then any root of `p` is its root candidate.

```lean
theorem representedLinearFactor_candidate_of_root {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    {p : CPolynomial F} {a : F}
    (hlin : isRepresentedLinearFactor p = true)
    (hroot : CPolynomial.eval a p = 0) :
    IsLinearRootFactorCandidate p a
```

`CompPoly.CPolynomial.Roots.FiniteField.eval_xPowModWith_eq_pow` (theorem, [line 1011](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Correctness.lean#L1011))

> Evaluation of a modular `X^n` at a root of the modulus agrees with `a^n`.

```lean
theorem eval_xPowModWith_eq_pow {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    {p : CPolynomial F} {a : F} (hroot : CPolynomial.eval a p = 0) (n : Nat) :
    CPolynomial.eval a (xPowModWith M D p n) = a ^ n
```

`CompPoly.CPolynomial.Roots.FiniteField.rootsInFiniteFieldWith_complete` (theorem, [line 1022](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Correctness.lean#L1022))

> Every root of a nonzero polynomial is returned by the finite-field backend.

```lean
theorem rootsInFiniteFieldWith_complete {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : FiniteFieldContext F) (splitter : LinearFactorProductSplitter F)
    (splitterValid :
      ∀ {p : CPolynomial F}, p ≠ 0 →
        splitter.validInput ctx.q (finiteFieldRootProductWith M D ctx p))
    {p : CPolynomial F} {a : F}
    (hp : p ≠ 0) (hroot : CPolynomial.eval a p = 0) :
    a ∈ (rootsInFiniteFieldWith M D ctx splitter p).toList
```

`CompPoly.CPolynomial.Roots.FiniteField.rootsInFiniteField_complete` (theorem, [line 1064](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Correctness.lean#L1064))

> Every root of a nonzero polynomial is returned by the finite-field backend.

```lean
theorem rootsInFiniteField_complete {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (ctx : FiniteFieldContext F) (splitter : LinearFactorProductSplitter F)
    (splitterValid :
      ∀ {p : CPolynomial F}, p ≠ 0 →
        splitter.validInput ctx.q (finiteFieldRootProduct ctx p))
    {p : CPolynomial F} {a : F}
    (hp : p ≠ 0) (hroot : CPolynomial.eval a p = 0) :
    a ∈ (rootsInFiniteField ctx splitter p).toList
```

`CompPoly.CPolynomial.Roots.FiniteField.rootsInFiniteField_spec` (theorem, [line 1081](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Correctness.lean#L1081))

> The complete executable finite-field root pipeline is sound and complete
> for nonzero inputs under the finite-field and splitter contracts.

```lean
theorem rootsInFiniteField_spec {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (ctx : FiniteFieldContext F) (splitter : LinearFactorProductSplitter F)
    (splitterValid :
      ∀ {p : CPolynomial F}, p ≠ 0 →
        splitter.validInput ctx.q (finiteFieldRootProduct ctx p))
    {p : CPolynomial F} {a : F} (hp : p ≠ 0) :
    a ∈ (rootsInFiniteField ctx splitter p).toList ↔
      CPolynomial.eval a p = 0
```

## Depends on

- [Extended Euclidean Algorithm for `CPolynomial`](../../part-01/euclideanalgorithm.md)
- [Finite-Field Root Backend](backend.md)
- [Linear-Factor Splitter Helpers](splitter.md)

## Sources

- [CompPoly/Univariate/Roots/Correctness.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Correctness.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.Roots.Correctness.json)
