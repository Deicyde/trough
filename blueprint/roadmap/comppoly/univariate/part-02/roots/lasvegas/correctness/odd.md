---
catalog: module
lean: CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausOddAttemptWith_child_proper, CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausOddAttemptWith_size_ge_two, CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausOddAttemptWith_ne_zero, CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausOddAttemptWith_root_preserved, CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausOddAttemptWith_child_dvd_input, CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausOddAttemptWith_child_normSplitWork_pos, CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausOddAttemptWith_stackWork_le, CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausOddAttemptWith_probe_congr, CompPoly.CPolynomial.Roots.FiniteField.tryOddSplitAttemptsWith_probe_congr, CompPoly.CPolynomial.Roots.FiniteField.tryOddSplitAttemptsWith_eq_some_exists_attempt, CompPoly.CPolynomial.Roots.FiniteField.tryOddSplitAttemptsWith_root, CompPoly.CPolynomial.Roots.FiniteField.tryOddSplitAttemptsWith_child_normSplitWork_pos, CompPoly.CPolynomial.Roots.FiniteField.tryOddSplitAttemptsWith_stackWork_le, CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausOddAttemptWith_success_of_bucket_separated
statement: formalized
proof: formalized
---

# Odd Split Correctness for Las Vegas Splitting

`CompPoly.Univariate.Roots.LasVegas.Correctness.Odd`, in [CompPoly/Univariate/Roots/LasVegas/Correctness/Odd.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/Odd.lean), by Valerii Huhnin.

> Correctness lemmas for the odd-characteristic Cantor-Zassenhaus split attempt
> and retry loop.

`CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausOddAttemptWith_child_proper` (theorem, [line 185](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/Odd.lean#L185))

```lean
theorem cantorZassenhausOddAttemptWith_child_proper {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (q : Nat) (probes : ProbeFamily F) {g child : CPolynomial F}
    {attempt : Nat} {children : Array (CPolynomial F)}
    (htry : cantorZassenhausOddAttemptWith M D q probes g attempt = some children)
    (hmem : child ∈ children.toList) :
    isNontrivialProperChild (CPolynomial.monicNormalize g) child = true
```

`CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausOddAttemptWith_size_ge_two` (theorem, [line 203](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/Odd.lean#L203))

```lean
theorem cantorZassenhausOddAttemptWith_size_ge_two {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (q : Nat) (probes : ProbeFamily F) {g : CPolynomial F}
    {attempt : Nat} {children : Array (CPolynomial F)}
    (htry : cantorZassenhausOddAttemptWith M D q probes g attempt = some children) :
    2 ≤ children.size
```

`CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausOddAttemptWith_ne_zero` (theorem, [line 219](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/Odd.lean#L219))

```lean
theorem cantorZassenhausOddAttemptWith_ne_zero {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (q : Nat) (probes : ProbeFamily F) {g : CPolynomial F}
    {attempt : Nat} {children : Array (CPolynomial F)}
    (htry : cantorZassenhausOddAttemptWith M D q probes g attempt = some children) :
    g ≠ 0
```

`CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausOddAttemptWith_root_preserved` (theorem, [line 238](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/Odd.lean#L238))

```lean
theorem cantorZassenhausOddAttemptWith_root_preserved {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (q : Nat) (probes : ProbeFamily F) {g : CPolynomial F} {a : F}
    {attempt : Nat} {children : Array (CPolynomial F)}
    (htry : cantorZassenhausOddAttemptWith M D q probes g attempt = some children)
    (hroot : CPolynomial.eval a g = 0) :
    ∃ child, child ∈ children.toList ∧ CPolynomial.eval a child = 0
```

`CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausOddAttemptWith_child_dvd_input` (theorem, [line 249](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/Odd.lean#L249))

```lean
theorem cantorZassenhausOddAttemptWith_child_dvd_input {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (q : Nat) (probes : ProbeFamily F) {g child : CPolynomial F}
    {attempt : Nat} {children : Array (CPolynomial F)}
    (htry : cantorZassenhausOddAttemptWith M D q probes g attempt = some children)
    (hmem : child ∈ children.toList) :
    child.toPoly ∣ g.toPoly
```

`CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausOddAttemptWith_child_normSplitWork_pos` (theorem, [line 301](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/Odd.lean#L301))

```lean
theorem cantorZassenhausOddAttemptWith_child_normSplitWork_pos {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (q : Nat) (probes : ProbeFamily F) {g child : CPolynomial F}
    {attempt : Nat} {children : Array (CPolynomial F)}
    (htry : cantorZassenhausOddAttemptWith M D q probes g attempt = some children)
    (hg : g ≠ 0) (hmem : child ∈ children.toList) :
    1 ≤ normSplitWork child
```

`CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausOddAttemptWith_stackWork_le` (theorem, [line 395](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/Odd.lean#L395))

```lean
theorem cantorZassenhausOddAttemptWith_stackWork_le {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (q : Nat) (probes : ProbeFamily F) {g : CPolynomial F}
    {attempt : Nat} {children : Array (CPolynomial F)}
    (htry : cantorZassenhausOddAttemptWith M D q probes g attempt = some children)
    (hg : g ≠ 0) :
    stackWork children.toList ≤ splitWork (CPolynomial.monicNormalize g) - 1
```

`CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausOddAttemptWith_probe_congr` (theorem, [line 624](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/Odd.lean#L624))

> The odd split attempt depends on the probe family only through the probe
> it actually draws.

```lean
theorem cantorZassenhausOddAttemptWith_probe_congr {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (q : Nat) {p1 p2 : ProbeFamily F} {g : CPolynomial F} {a1 a2 : Nat}
    (hprobe : p1.probe q (CPolynomial.monicNormalize g) a1 =
      p2.probe q (CPolynomial.monicNormalize g) a2) :
    cantorZassenhausOddAttemptWith M D q p1 g a1 =
      cantorZassenhausOddAttemptWith M D q p2 g a2
```

`CompPoly.CPolynomial.Roots.FiniteField.tryOddSplitAttemptsWith_probe_congr` (theorem, [line 638](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/Odd.lean#L638))

> The odd retry loop depends on the probe family only through the probes it
> actually draws.

```lean
theorem tryOddSplitAttemptsWith_probe_congr {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (q : Nat) {p1 p2 : ProbeFamily F} {g : CPolynomial F} :
    ∀ (attempts offset1 offset2 : Nat),
      (∀ i, i < attempts →
        p1.probe q (CPolynomial.monicNormalize g) (offset1 + i) =
          p2.probe q (CPolynomial.monicNormalize g) (offset2 + i)) →
      tryOddSplitAttemptsWith M D q p1 g attempts offset1 =
        tryOddSplitAttemptsWith M D q p2 g attempts offset2
```

`CompPoly.CPolynomial.Roots.FiniteField.tryOddSplitAttemptsWith_eq_some_exists_attempt` (theorem, [line 669](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/Odd.lean#L669))

> A successful retry loop result is produced by some single attempt.

```lean
theorem tryOddSplitAttemptsWith_eq_some_exists_attempt {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (q : Nat) (probes : ProbeFamily F) {g : CPolynomial F} :
    ∀ (attempts offset : Nat) {children : Array (CPolynomial F)},
      tryOddSplitAttemptsWith M D q probes g attempts offset = some children →
      ∃ attempt, cantorZassenhausOddAttemptWith M D q probes g attempt = some children
```

`CompPoly.CPolynomial.Roots.FiniteField.tryOddSplitAttemptsWith_root` (theorem, [line 693](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/Odd.lean#L693))

```lean
theorem tryOddSplitAttemptsWith_root {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (q : Nat) (probes : ProbeFamily F) {g : CPolynomial F} {a : F}
    (hg : g ≠ 0) (hroot : CPolynomial.eval a g = 0) :
    ∀ attempts offset {children : Array (CPolynomial F)},
      tryOddSplitAttemptsWith M D q probes g attempts offset = some children →
        ∃ child, child ∈ children.toList ∧ CPolynomial.eval a child = 0
```

`CompPoly.CPolynomial.Roots.FiniteField.tryOddSplitAttemptsWith_child_normSplitWork_pos` (theorem, [line 743](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/Odd.lean#L743))

```lean
theorem tryOddSplitAttemptsWith_child_normSplitWork_pos {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (q : Nat) (probes : ProbeFamily F) {g child : CPolynomial F}
    (hg : g ≠ 0) :
    ∀ attempts offset {children : Array (CPolynomial F)},
      tryOddSplitAttemptsWith M D q probes g attempts offset = some children →
        child ∈ children.toList →
          1 ≤ normSplitWork child
```

`CompPoly.CPolynomial.Roots.FiniteField.tryOddSplitAttemptsWith_stackWork_le` (theorem, [line 770](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/Odd.lean#L770))

```lean
theorem tryOddSplitAttemptsWith_stackWork_le {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (q : Nat) (probes : ProbeFamily F) {g : CPolynomial F}
    (hg : g ≠ 0) :
    ∀ attempts offset {children : Array (CPolynomial F)},
      tryOddSplitAttemptsWith M D q probes g attempts offset = some children →
        stackWork children.toList ≤ splitWork (CPolynomial.monicNormalize g) - 1
```

`CompPoly.CPolynomial.Roots.FiniteField.cantorZassenhausOddAttemptWith_success_of_bucket_separated` (theorem, [line 1049](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/Odd.lean#L1049))

> A fixed probe whose Euler buckets separate two distinct roots of `g` forces the
> odd Cantor-Zassenhaus split attempt to succeed.
>
> The split candidates of `cantorZassenhausOddAttemptWith` are the zero part
> `gcd(g, h)`, the square part `gcd(g / zeroPart, h ^ ((q - 1) / 2) - 1)`, and
> the remaining quotient. Roots in the `zero`, `square`, and `nonsquare` Euler
> buckets of the probe land in these three candidates respectively, so two roots
> in different buckets witness two distinct nontrivial proper children.
>
> The hypothesis `hg : g ≠ 0` is essential: for `g = 0` both root hypotheses hold
> vacuously while the attempt always fails, because no candidate child can have
> representation size strictly below the parent size `0`. No distinctness
> hypothesis on `a` and `b` is needed: bucket separation already forces `a ≠ b`.

```lean
theorem cantorZassenhausOddAttemptWith_success_of_bucket_separated {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (q : Nat) {g h : CPolynomial F} {a b : F} (attempt : Nat)
    (hg : g ≠ 0)
    (hrootA : CPolynomial.eval a g = 0)
    (hrootB : CPolynomial.eval b g = 0)
    (hsep :
      oddCZBucket q (CPolynomial.eval a h) ≠
        oddCZBucket q (CPolynomial.eval b h)) :
    ∃ children,
      cantorZassenhausOddAttemptWith M D q
        ({ probe := fun _q _factor _attempt ↦ h } : ProbeFamily F)
        g attempt = some children
```

## Depends on

- [Shared Correctness Lemmas for Las Vegas Splitting](common.md)
- [Euler Buckets for Odd Cantor-Zassenhaus Splitting](../oddbucket.md)

## Sources

- [CompPoly/Univariate/Roots/LasVegas/Correctness/Odd.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/LasVegas/Correctness/Odd.lean)
- [Declaration ledger](../../../../../../../sources/comppoly/CompPoly.Univariate.Roots.LasVegas.Correctness.Odd.json)
