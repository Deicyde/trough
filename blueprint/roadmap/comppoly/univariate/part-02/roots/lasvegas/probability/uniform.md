---
catalog: module
lean: CompPoly.CPolynomial.Roots.FiniteField.uniformFieldIndexPMF, CompPoly.CPolynomial.Roots.FiniteField.uniformFieldElementPMF, CompPoly.CPolynomial.Roots.FiniteField.uniformFieldElementPMF_support_eq_univ, CompPoly.CPolynomial.Roots.FiniteField.uniformFieldElementPMF_apply, CompPoly.CPolynomial.Roots.FiniteField.uniformCoefficientArrayPMF, CompPoly.CPolynomial.Roots.FiniteField.uniformProbePMF, CompPoly.CPolynomial.Roots.FiniteField.uniformProbePMF_support_natDegree_lt, CompPoly.CPolynomial.Roots.FiniteField.uniformProbePMF_eval_pair_apply, CompPoly.CPolynomial.Roots.FiniteField.uniformProbeTablePMF, CompPoly.CPolynomial.Roots.FiniteField.uniformFieldElementPMF_pair_apply, CompPoly.CPolynomial.Roots.FiniteField.uniformProbePMF_map_eval_pair, CompPoly.CPolynomial.Roots.FiniteField.uniformPair_separated_probability_ge_half_of_fiber_card_le
statement: formalized
proof: formalized
---

# Uniform Probe Distributions for Las Vegas Root Splitting

`CompPoly.Univariate.Roots.LasVegas.Probability.Uniform`, in [CompPoly/Univariate/Roots/LasVegas/Probability/Uniform.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/Uniform.lean), by Valerii Huhnin.

> Idealized uniform sources for the Las Vegas probability story: uniform field
> elements induced by a lazy enumeration, independent uniform coefficient arrays,
> and the uniform probe-polynomial distribution they induce.
>
> The deep target of this module is pair-evaluation uniformity: a uniform probe
> with at least two sampled coefficients evaluates at two distinct field points
> to a uniform pair on `F × F`.

`CompPoly.CPolynomial.Roots.FiniteField.uniformFieldIndexPMF` (definition, [line 41](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/Uniform.lean#L41))

> Uniform sampling from enumeration indices.

```lean
noncomputable def uniformFieldIndexPMF {F : Type*} [Zero F]
    (enumeration : FieldEnumeration F) :
    PMF (Fin enumeration.size)
```

`CompPoly.CPolynomial.Roots.FiniteField.uniformFieldElementPMF` (definition, [line 58](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/Uniform.lean#L58))

> Uniform field-element sampling induced by a lazy enumeration.

```lean
noncomputable def uniformFieldElementPMF {F : Type*} [Zero F]
    (enumeration : FieldEnumeration F) :
    PMF F
```

`CompPoly.CPolynomial.Roots.FiniteField.uniformFieldElementPMF_support_eq_univ` (theorem, [line 64](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/Uniform.lean#L64))

> Complete injective enumerations put every field element in the PMF support.

```lean
theorem uniformFieldElementPMF_support_eq_univ {F : Type*} [Zero F] {q : Nat}
    (enumeration : UniformFieldEnumeration F q) :
    (uniformFieldElementPMF enumeration.toFieldEnumeration).support = Set.univ
```

`CompPoly.CPolynomial.Roots.FiniteField.uniformFieldElementPMF_apply` (theorem, [line 72](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/Uniform.lean#L72))

> Every field element has probability `1 / q` under a uniform field enumeration.

```lean
theorem uniformFieldElementPMF_apply {F : Type*} [Zero F] {q : Nat}
    (enumeration : UniformFieldEnumeration F q) (a : F) :
    uniformFieldElementPMF enumeration.toFieldEnumeration a = (q : ℝ≥0∞)⁻¹
```

`CompPoly.CPolynomial.Roots.FiniteField.uniformCoefficientArrayPMF` (definition, [line 96](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/Uniform.lean#L96))

> Uniform PMF over coefficient arrays of fixed length, sampled independently from
> the supplied field enumeration.

```lean
noncomputable def uniformCoefficientArrayPMF {F : Type*} [Zero F]
    (enumeration : FieldEnumeration F) :
    Nat → PMF (Array F)
```

`CompPoly.CPolynomial.Roots.FiniteField.uniformProbePMF` (definition, [line 152](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/Uniform.lean#L152))

> Uniform probe polynomial of degree bounded by the supplied coefficient count.

```lean
noncomputable def uniformProbePMF {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (enumeration : FieldEnumeration F) (coefficientCount : Nat) :
    PMF (CPolynomial F)
```

`CompPoly.CPolynomial.Roots.FiniteField.uniformProbePMF_support_natDegree_lt` (theorem, [line 162](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/Uniform.lean#L162))

> Probes sampled with `coefficientCount` coefficients have degree below that
> bound, unless zero.

```lean
theorem uniformProbePMF_support_natDegree_lt {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (enumeration : FieldEnumeration F) (coefficientCount : Nat)
    {probe : CPolynomial F}
    (hprobe : probe ∈ (uniformProbePMF enumeration coefficientCount).support) :
    CPolynomial.natDegree probe < coefficientCount ∨ probe = 0
```

`CompPoly.CPolynomial.Roots.FiniteField.uniformProbePMF_eval_pair_apply` (theorem, [line 418](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/Uniform.lean#L418))

> Pair-evaluation uniformity: a uniform probe with at least two sampled
> coefficients evaluates at two distinct points to a uniform pair on `F × F`.
>
> For a fixed coefficient tail, the map
> `(c₀, c₁) ↦ (c₀ + c₁ * a + tail(a), c₀ + c₁ * b + tail(b))` is a bijection of
> `F × F` because `a ≠ b`, so exactly one of the `q ^ 2` equally likely
> `(c₀, c₁)` choices hits the target pair `(x, y)`.

```lean
theorem uniformProbePMF_eval_pair_apply {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] {q : Nat}
    (enumeration : UniformFieldEnumeration F q)
    (coefficientCount : Nat) {a b : F} (x y : F)
    (hab : a ≠ b) (hcount : 2 ≤ coefficientCount) :
    eventProbability
        (uniformProbePMF enumeration.toFieldEnumeration coefficientCount)
        {h | CPolynomial.eval a h = x ∧ CPolynomial.eval b h = y} =
      (q : ℝ≥0∞)⁻¹ * (q : ℝ≥0∞)⁻¹
```

`CompPoly.CPolynomial.Roots.FiniteField.uniformProbeTablePMF` (definition, [line 434](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/Uniform.lean#L434))

> Independent uniform probe tables of a fixed length.

```lean
noncomputable def uniformProbeTablePMF {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (enumeration : FieldEnumeration F) (coefficientCount : Nat) :
    Nat → PMF (List (CPolynomial F))
```

`CompPoly.CPolynomial.Roots.FiniteField.uniformFieldElementPMF_pair_apply` (theorem, [line 443](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/Uniform.lean#L443))

> Every pair of field elements is equally likely under two independent uniform draws.

```lean
theorem uniformFieldElementPMF_pair_apply {F : Type*} [Zero F] {q : Nat}
    (enumeration : UniformFieldEnumeration F q) (xy : F × F) :
    ((uniformFieldElementPMF enumeration.toFieldEnumeration).bind
      fun x ↦ (uniformFieldElementPMF enumeration.toFieldEnumeration).map
        fun y ↦ (x, y)) xy = (q : ℝ≥0∞)⁻¹ * (q : ℝ≥0∞)⁻¹
```

`CompPoly.CPolynomial.Roots.FiniteField.uniformProbePMF_map_eval_pair` (theorem, [line 493](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/Uniform.lean#L493))

> The evaluation pair of a uniform probe at two distinct points pushes forward to
> two independent uniform field elements.

```lean
theorem uniformProbePMF_map_eval_pair {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] {q : Nat}
    (enumeration : UniformFieldEnumeration F q) (coefficientCount : Nat) {a b : F}
    (hab : a ≠ b) (hcount : 2 ≤ coefficientCount) :
    (uniformProbePMF enumeration.toFieldEnumeration coefficientCount).map
        (fun h ↦ (CPolynomial.eval a h, CPolynomial.eval b h)) =
      (uniformFieldElementPMF enumeration.toFieldEnumeration).bind
        fun x ↦ (uniformFieldElementPMF enumeration.toFieldEnumeration).map
          fun y ↦ (x, y)
```

`CompPoly.CPolynomial.Roots.FiniteField.uniformPair_separated_probability_ge_half_of_fiber_card_le` (theorem, [line 520](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/Uniform.lean#L520))

> If every fiber of a classifier has at most `m` elements out of `q ≤ 2 * (q - m)`,
> two independent uniform field values are separated by the classifier with
> probability at least `1 / 2`.

```lean
theorem uniformPair_separated_probability_ge_half_of_fiber_card_le {F : Type*}
    [Zero F] [Fintype F] {β : Type*} {q m : Nat}
    (enumeration : UniformFieldEnumeration F q) (f : F → β)
    (hcard : Fintype.card F = q)
    (hfiber : ∀ x : F, ∃ s : Finset F, (∀ y : F, f y = f x → y ∈ s) ∧ s.card ≤ m)
    (hhalf : q ≤ 2 * (q - m)) :
    (2 : ℝ≥0∞)⁻¹ ≤
      eventProbability
        ((uniformFieldElementPMF enumeration.toFieldEnumeration).bind
          fun x ↦ (uniformFieldElementPMF enumeration.toFieldEnumeration).map
            fun y ↦ (x, y))
        {xy : F × F | f xy.1 ≠ f xy.2}
```

## Depends on

- [Probability Basics for Las Vegas Root Splitting](basic.md)

## Sources

- [CompPoly/Univariate/Roots/LasVegas/Probability/Uniform.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/LasVegas/Probability/Uniform.lean)
- [Declaration ledger](../../../../../../../sources/comppoly/CompPoly.Univariate.Roots.LasVegas.Probability.Uniform.json)
