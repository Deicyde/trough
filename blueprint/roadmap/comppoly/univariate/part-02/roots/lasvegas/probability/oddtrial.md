---
catalog: module
lean: CompPoly.CPolynomial.Roots.FiniteField.HasTwoDistinctRoots, CompPoly.CPolynomial.Roots.FiniteField.RootProductProbabilityInput, CompPoly.CPolynomial.Roots.FiniteField.RootProductProbabilityInput.hasTwoDistinctRoots, CompPoly.CPolynomial.Roots.FiniteField.rootProductProbabilityInput_of_lasVegasSplitterInput, CompPoly.CPolynomial.Roots.FiniteField.finiteFieldRootProductWith_rootProductProbabilityInput, CompPoly.CPolynomial.Roots.FiniteField.finiteFieldRootProduct_rootProductProbabilityInput, CompPoly.CPolynomial.Roots.FiniteField.IsProperRootPreservingSplit, CompPoly.CPolynomial.Roots.FiniteField.oddSplitTrialPMF, CompPoly.CPolynomial.Roots.FiniteField.oddSplitTrialPMF_support_success_valid, CompPoly.CPolynomial.Roots.FiniteField.OddSplitTrialHalfSuccessModel, CompPoly.CPolynomial.Roots.FiniteField.oddSplitTrial_success_probability_ge_half_of_two_le, CompPoly.CPolynomial.Roots.FiniteField.oddSplitTrial_success_probability_ge_half_linear, CompPoly.CPolynomial.Roots.FiniteField.oddSplitTrialHalfSuccessModel_of_uniformProbe, CompPoly.CPolynomial.Roots.FiniteField.oddSplitTrial_success_probability_ge_half, CompPoly.CPolynomial.Roots.FiniteField.oddSplitTrial_success_probability_ge_half_of_model
statement: formalized
proof: formalized
---

# One Odd Cantor-Zassenhaus Trial Under Uniform Probes

`CompPoly.Univariate.Roots.LasVegas.Probability.OddTrial`, in [CompPoly/Univariate/Roots/LasVegas/Probability/OddTrial.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/OddTrial.lean), by Valerii Huhnin.

> The single-trial probability surface for odd-field Las Vegas splitting: the
> trial PMF induced by uniform probes, the half-success model, and the theorem
> that uniform probes really achieve success probability at least `1 / 2` for
> squarefree root products with at least two distinct roots.

`CompPoly.CPolynomial.Roots.FiniteField.HasTwoDistinctRoots` (definition, [line 38](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/OddTrial.lean#L38))

> The factor has at least two distinct field roots.

```lean
def HasTwoDistinctRoots {F : Type*} [Semiring F] (g : CPolynomial F) : Prop
```

`CompPoly.CPolynomial.Roots.FiniteField.RootProductProbabilityInput` (structure, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/OddTrial.lean#L49))

> Probability-facing root-product model for the recursive fallback analysis: the
> factor is a nonzero squarefree product of linear factors over the field, with
> as many roots as its degree, dividing the Frobenius polynomial `X ^ q - X`.
>
> This intentionally strengthens the runtime splitter contract
> `lasVegasSplitterInput` instead of overloading it with probability details.

```lean
structure RootProductProbabilityInput {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (q : Nat) (g : CPolynomial F) : Prop where
  nonzero : g ≠ 0
  splits_over_field :
    g.toPoly ∣ ((Polynomial.X : Polynomial F) ^ q - Polynomial.X)
  squarefree : Squarefree g.toPoly
  roots_card_eq_degree : g.toPoly.roots.card = g.toPoly.natDegree
```

`CompPoly.CPolynomial.Roots.FiniteField.RootProductProbabilityInput.hasTwoDistinctRoots` (theorem, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/OddTrial.lean#L60))

> A squarefree root product of degree at least two has two distinct field roots.

```lean
theorem RootProductProbabilityInput.hasTwoDistinctRoots {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] {q : Nat} {g : CPolynomial F}
    (hinput : RootProductProbabilityInput q g)
    (hdegree : 2 ≤ CPolynomial.natDegree g) :
    HasTwoDistinctRoots g
```

`CompPoly.CPolynomial.Roots.FiniteField.rootProductProbabilityInput_of_lasVegasSplitterInput` (theorem, [line 95](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/OddTrial.lean#L95))

> Over a field of cardinality `q`, the runtime splitter contract already implies
> the full probability-facing root-product model: every divisor of the Frobenius
> polynomial `X ^ q - X` is squarefree and splits with as many roots as its
> degree.

```lean
theorem rootProductProbabilityInput_of_lasVegasSplitterInput {F : Type*}
    [Field F] [Fintype F] [BEq F] [LawfulBEq F] {q : Nat} {g : CPolynomial F}
    (hvalid : lasVegasSplitterInput q g) (hcard : Fintype.card F = q) :
    RootProductProbabilityInput q g
```

`CompPoly.CPolynomial.Roots.FiniteField.finiteFieldRootProductWith_rootProductProbabilityInput` (theorem, [line 126](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/OddTrial.lean#L126))

> Finite-field root products satisfy the probability-facing root-product model.
> This is the adapter from the concrete `finiteFieldRootProductWith` construction
> to the hypotheses of the half-success and recursive fallback theorems.

```lean
theorem finiteFieldRootProductWith_rootProductProbabilityInput {F : Type*}
    [Field F] [Fintype F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : FiniteFieldContext F) {p : CPolynomial F} (hp : p ≠ 0) :
    RootProductProbabilityInput ctx.q (finiteFieldRootProductWith M D ctx p)
```

`CompPoly.CPolynomial.Roots.FiniteField.finiteFieldRootProduct_rootProductProbabilityInput` (theorem, [line 137](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/OddTrial.lean#L137))

> Default-backend root products satisfy the probability-facing model.

```lean
theorem finiteFieldRootProduct_rootProductProbabilityInput {F : Type*}
    [Field F] [Fintype F] [BEq F] [LawfulBEq F]
    (ctx : FiniteFieldContext F) {p : CPolynomial F} (hp : p ≠ 0) :
    RootProductProbabilityInput ctx.q (finiteFieldRootProduct ctx p)
```

`CompPoly.CPolynomial.Roots.FiniteField.IsProperRootPreservingSplit` (definition, [line 148](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/OddTrial.lean#L148))

> The algebraic validity expected from a successful randomized split: nontrivial
> proper children, divisibility by the parent, and root preservation.

```lean
def IsProperRootPreservingSplit {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (parent : CPolynomial F) (children : Array (CPolynomial F)) : Prop
```

`CompPoly.CPolynomial.Roots.FiniteField.oddSplitTrialPMF` (definition, [line 158](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/OddTrial.lean#L158))

> One odd-field Cantor-Zassenhaus trial under a uniform probe distribution.

```lean
noncomputable def oddSplitTrialPMF {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (enumeration : FieldEnumeration F) (q coefficientCount : Nat)
    (g : CPolynomial F) (attempt : Nat) :
    PMF (TrialResult F)
```

`CompPoly.CPolynomial.Roots.FiniteField.oddSplitTrialPMF_support_success_valid` (theorem, [line 171](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/OddTrial.lean#L171))

> A successful trial in the support of the PMF is an algebraically valid split.

```lean
theorem oddSplitTrialPMF_support_success_valid {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (enumeration : FieldEnumeration F) (q coefficientCount : Nat)
    (g : CPolynomial F) (attempt : Nat) {children : Array (CPolynomial F)}
    (hmem : TrialResult.split children ∈
      (oddSplitTrialPMF M D enumeration q coefficientCount g attempt).support) :
    IsProperRootPreservingSplit g children
```

`CompPoly.CPolynomial.Roots.FiniteField.OddSplitTrialHalfSuccessModel` (definition, [line 205](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/OddTrial.lean#L205))

> Model predicate for the finite-field counting argument behind one odd-field
> Cantor-Zassenhaus trial.

```lean
def OddSplitTrialHalfSuccessModel {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    {q : Nat} (enumeration : UniformFieldEnumeration F q)
    (g : CPolynomial F) (attempt : Nat) : Prop
```

`CompPoly.CPolynomial.Roots.FiniteField.oddSplitTrial_success_probability_ge_half_of_two_le` (theorem, [line 227](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/OddTrial.lean#L227))

> Uniform probe polynomials really make one odd Cantor-Zassenhaus attempt succeed
> with probability at least `1 / 2`.
>
> The proof combines pair-evaluation uniformity of `uniformProbePMF`, the Euler
> bucket separation probability, and the deterministic theorem that a probe whose
> buckets separate two roots forces the executable attempt to succeed.
>
> The hypothesis `hdegree` is essential and not implied by `hroots`: for `g = 0`
> every pair of points consists of roots, yet the trial samples zero-coefficient
> probes and always fails.

```lean
theorem oddSplitTrial_success_probability_ge_half_of_two_le {F : Type*}
    [Field F] [Fintype F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    {q : Nat} (enumeration : UniformFieldEnumeration F q)
    (g : CPolynomial F) (coefficientCount attempt : Nat)
    (hcount : 2 ≤ coefficientCount)
    (hfield : OddUniformFieldModel F q enumeration)
    (hroots : HasTwoDistinctRoots g)
    (hg : g ≠ 0) :
    (2 : ℝ≥0∞)⁻¹ ≤
      trialSuccessProbability
        (oddSplitTrialPMF M D enumeration.toFieldEnumeration q coefficientCount
          g attempt)
```

`CompPoly.CPolynomial.Roots.FiniteField.oddSplitTrial_success_probability_ge_half_linear` (theorem, [line 279](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/OddTrial.lean#L279))

> Random affine probes with both coefficients drawn uniformly and independently
> already achieve the half-success bound: the evaluation pair at two distinct
> roots covers all of `F × F`, so no higher-degree probes are needed.

```lean
theorem oddSplitTrial_success_probability_ge_half_linear {F : Type*}
    [Field F] [Fintype F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    {q : Nat} (enumeration : UniformFieldEnumeration F q)
    (g : CPolynomial F) (attempt : Nat)
    (hfield : OddUniformFieldModel F q enumeration)
    (hroots : HasTwoDistinctRoots g)
    (hg : g ≠ 0) :
    (2 : ℝ≥0∞)⁻¹ ≤
      trialSuccessProbability
        (oddSplitTrialPMF M D enumeration.toFieldEnumeration q 2 g attempt)
```

`CompPoly.CPolynomial.Roots.FiniteField.oddSplitTrialHalfSuccessModel_of_uniformProbe` (theorem, [line 301](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/OddTrial.lean#L301))

> Uniform probe polynomials really make one odd Cantor-Zassenhaus attempt succeed
> with probability at least `1 / 2`.
>
> The hypothesis `hdegree` is essential and not implied by `hroots`: for `g = 0`
> every pair of points consists of roots, yet the trial samples zero-coefficient
> probes and always fails.

```lean
theorem oddSplitTrialHalfSuccessModel_of_uniformProbe {F : Type*}
    [Field F] [Fintype F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    {q : Nat} (enumeration : UniformFieldEnumeration F q)
    (g : CPolynomial F) (attempt : Nat)
    (hfield : OddUniformFieldModel F q enumeration)
    (hroots : HasTwoDistinctRoots g)
    (hdegree : 2 ≤ CPolynomial.natDegree g) :
    OddSplitTrialHalfSuccessModel M D enumeration g attempt
```

`CompPoly.CPolynomial.Roots.FiniteField.oddSplitTrial_success_probability_ge_half` (theorem, [line 327](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/OddTrial.lean#L327))

> For a squarefree finite-field root product over an odd field, one uniform
> Cantor-Zassenhaus trial succeeds with probability at least `1 / 2`.
>
> Unlike the historical model-assisted shape (kept below as
> `oddSplitTrial_success_probability_ge_half_of_model`), this theorem no longer
> accepts the probability bound itself as an input.

```lean
theorem oddSplitTrial_success_probability_ge_half {F : Type*}
    [Field F] [Fintype F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    {q : Nat} (enumeration : UniformFieldEnumeration F q)
    (g : CPolynomial F) (attempt : Nat)
    (hfield : OddUniformFieldModel F q enumeration)
    (hrootProduct : RootProductProbabilityInput q g)
    (hdegree : 2 ≤ CPolynomial.natDegree g) :
    (2 : ℝ≥0∞)⁻¹ ≤
      trialSuccessProbability
        (oddSplitTrialPMF M D enumeration.toFieldEnumeration q
          (CPolynomial.natDegree g) g attempt)
```

`CompPoly.CPolynomial.Roots.FiniteField.oddSplitTrial_success_probability_ge_half_of_model` (theorem, [line 348](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/OddTrial.lean#L348))

> Compatibility shape of the half-success theorem that still accepts the
> half-success model as an assumption. Prefer
> `oddSplitTrial_success_probability_ge_half`, which derives the model from the
> uniform probe source.

```lean
theorem oddSplitTrial_success_probability_ge_half_of_model {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    {q : Nat} (enumeration : UniformFieldEnumeration F q)
    (g : CPolynomial F) (attempt : Nat)
    (hvalid : lasVegasSplitterInput q g)
    (hodd : q % 2 = 1)
    (hdegree : 2 ≤ CPolynomial.natDegree g)
    (hmodel : lasVegasSplitterInput q g →
      q % 2 = 1 →
      2 ≤ CPolynomial.natDegree g →
        OddSplitTrialHalfSuccessModel M D enumeration g attempt) :
    (2 : ℝ≥0∞)⁻¹ ≤
      trialSuccessProbability
        (oddSplitTrialPMF M D enumeration.toFieldEnumeration q
          (CPolynomial.natDegree g) g attempt)
```

## Depends on

- [Las Vegas Linear-Factor Splitting](../basic.md)
- [Uniform Probe Distributions for Las Vegas Root Splitting](uniform.md)
- [Finite-Field Root Products](../../rootproduct.md)

## Proof depends on

- [Odd Split Correctness for Las Vegas Splitting](../correctness/odd.md)
- [Euler Bucket Counting for Odd Cantor-Zassenhaus Splitting](oddbuckets.md)

## Sources

- [CompPoly/Univariate/Roots/LasVegas/Probability/OddTrial.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/OddTrial.lean)
- [Declaration ledger](../../../../../../../sources/comppoly/CompPoly.Univariate.Roots.LasVegas.Probability.OddTrial.json)
