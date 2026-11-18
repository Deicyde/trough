---
catalog: module
lean: Cslib.Crypto.Protocols.Commitment.Scheme.perfectlyHiding_iff_statisticallyHiding_zero, Cslib.Crypto.Protocols.Commitment.Scheme.StatisticallyHiding.mono, Cslib.Crypto.Protocols.Commitment.Scheme.PerfectlyBinding.disjoint_support_commitmentDist, Cslib.Crypto.Protocols.Commitment.Scheme.PerfectlyBinding.dist_commitmentDist_eq_one, Cslib.Crypto.Protocols.Commitment.Scheme.subsingleton_of_statisticallyHiding_of_perfectlyBinding, Cslib.Crypto.Protocols.Commitment.Scheme.subsingleton_of_perfectlyHiding_of_perfectlyBinding
statement: formalized
proof: formalized
---

# Commitment Schemes

`Cslib.Crypto.Protocols.Commitment.Basic`, in [Cslib/Crypto/Protocols/Commitment/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/Commitment/Basic.lean), by Samuel Schlesinger.

> Basic results about information-theoretic commitment schemes.
>
> The main result is the hiding–binding trade-off: a perfectly binding scheme
> places the commitment distributions of distinct messages at the maximum
> statistical distance, so it cannot be statistically hiding for any error below
> one. Hiding and binding can therefore not both hold unconditionally; real
> schemes make at most one side information-theoretic and settle for a
> computational version of the other.
>
> ## Main results
>
> - `Scheme.subsingleton_of_statisticallyHiding_of_perfectlyBinding`: a scheme
>   cannot be both statistically hiding with error below one and perfectly
>   binding unless any two messages are equal
> - `Scheme.PerfectlyBinding.dist_commitmentDist_eq_one`: perfect binding forces
>   distinct messages' commitment distributions to the maximum statistical
>   distance
> - `Scheme.subsingleton_of_perfectlyHiding_of_perfectlyBinding`: the perfect
>   hiding case, with no finiteness assumption on commitments
> - `Scheme.perfectlyHiding_iff_statisticallyHiding_zero`: perfect hiding is
>   statistical hiding with zero error

`Cslib.Crypto.Protocols.Commitment.Scheme.perfectlyHiding_iff_statisticallyHiding_zero` (theorem, [line 47](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/Commitment/Basic.lean#L47))

> Perfect hiding is exactly statistical hiding with zero error.

```lean
theorem perfectlyHiding_iff_statisticallyHiding_zero
    [Fintype Commitment] (scheme : Scheme Message Commitment Opening) :
    scheme.PerfectlyHiding ↔ scheme.StatisticallyHiding 0
```

`Cslib.Crypto.Protocols.Commitment.Scheme.StatisticallyHiding.mono` (theorem, [line 53](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/Commitment/Basic.lean#L53))

> Enlarging the permitted error preserves statistical hiding.

```lean
theorem StatisticallyHiding.mono [Fintype Commitment]
    {scheme : Scheme Message Commitment Opening} :
    Monotone scheme.StatisticallyHiding
```

`Cslib.Crypto.Protocols.Commitment.Scheme.PerfectlyBinding.disjoint_support_commitmentDist` (theorem, [line 61](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/Commitment/Basic.lean#L61))

> Distinct messages of a perfectly binding scheme have disjoint sets of
> possible commitments.

```lean
theorem PerfectlyBinding.disjoint_support_commitmentDist
    {scheme : Scheme Message Commitment Opening} (hbind : scheme.PerfectlyBinding)
    {message₀ message₁ : Message} (hne : message₀ ≠ message₁) :
    Disjoint (scheme.commitmentDist message₀).support
      (scheme.commitmentDist message₁).support
```

`Cslib.Crypto.Protocols.Commitment.Scheme.PerfectlyBinding.dist_commitmentDist_eq_one` (theorem, [line 76](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/Commitment/Basic.lean#L76))

> In a perfectly binding scheme, the commitment distributions of distinct
> messages are at the maximum statistical distance: an unbounded observer can
> read the message off the commitment.

```lean
theorem PerfectlyBinding.dist_commitmentDist_eq_one
    [Fintype Commitment] {scheme : Scheme Message Commitment Opening}
    (hbind : scheme.PerfectlyBinding) {message₀ message₁ : Message}
    (hne : message₀ ≠ message₁) :
    dist (scheme.commitmentDist message₀)
      (scheme.commitmentDist message₁) = 1
```

`Cslib.Crypto.Protocols.Commitment.Scheme.subsingleton_of_statisticallyHiding_of_perfectlyBinding` (theorem, [line 88](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/Commitment/Basic.lean#L88))

> **The hiding–binding trade-off.** A scheme cannot be both statistically
> hiding with error below one and perfectly binding unless any two messages are
> equal. The error bound is sharp: statistical hiding with error one holds
> vacuously for every scheme.

```lean
theorem subsingleton_of_statisticallyHiding_of_perfectlyBinding
    [Fintype Commitment] (scheme : Scheme Message Commitment Opening) {ε : ℝ≥0}
    (hε : ε < 1) (hhide : scheme.StatisticallyHiding ε)
    (hbind : scheme.PerfectlyBinding) : Subsingleton Message
```

`Cslib.Crypto.Protocols.Commitment.Scheme.subsingleton_of_perfectlyHiding_of_perfectlyBinding` (theorem, [line 102](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/Commitment/Basic.lean#L102))

> A scheme cannot be both perfectly hiding and perfectly binding unless any
> two messages are equal. Unlike the statistical version, this needs no
> finiteness assumption on the commitment type.

```lean
theorem subsingleton_of_perfectlyHiding_of_perfectlyBinding
    (scheme : Scheme Message Commitment Opening)
    (hhide : scheme.PerfectlyHiding) (hbind : scheme.PerfectlyBinding) :
    Subsingleton Message
```

## Depends on

- [Commitment Schemes: Information-Theoretic Security](defs.md)

## Sources

- [Cslib/Crypto/Protocols/Commitment/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/Commitment/Basic.lean)
