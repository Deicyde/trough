---
catalog: module
lean: Cslib.Crypto.Protocols.Commitment.Scheme.PerfectlyHiding, Cslib.Crypto.Protocols.Commitment.Scheme.StatisticallyHiding, Cslib.Crypto.Protocols.Commitment.Scheme.PerfectlyBinding
statement: formalized
proof: formalized
---

# Commitment Schemes: Information-Theoretic Security

`Cslib.Crypto.Protocols.Commitment.Defs`, in [Cslib/Crypto/Protocols/Commitment/Defs.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/Commitment/Defs.lean), by Samuel Schlesinger.

> Hiding and binding for commitment schemes, in their information-theoretic forms
> ([BonehShoup2023], Section 8.12). Perfect hiding: every message yields the same
> commitment distribution. Statistical hiding: any two commitment distributions
> are within statistical distance `ε`. Perfect binding: no commitment can be
> opened to two different messages, even by an unbounded committer.
>
> Each definition is about a single, fixed scheme; statistical hiding carries an
> explicit error bound, and the perfect notions have no error at all. The
> asymptotic notions in the book — negligible statistical distance for families
> of distributions ([BonehShoup2023], Definition 3.6), or security against
> efficient adversaries (Section 8.12) — can be layered on top of these later.
>
> ## Main definitions
>
> - `Scheme.PerfectlyHiding`: the commitment distributions are equal for every
>   pair of messages
> - `Scheme.StatisticallyHiding`: the commitment distributions are statistically
>   close with error `ε`
> - `Scheme.PerfectlyBinding`: no commitment has accepted openings to two
>   different messages
>
> ## References
>
> * [D. Boneh, V. Shoup, *A Graduate Course in Applied Cryptography*,
>   Version 0.6][BonehShoup2023]

`Cslib.Crypto.Protocols.Commitment.Scheme.PerfectlyHiding` (definition, [line 54](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/Commitment/Defs.lean#L54))

> A scheme is perfectly hiding when every message yields the same commitment
> distribution, so a commitment reveals nothing about the message as long as its
> opening is withheld ([BonehShoup2023], Section 8.12).

```lean
def PerfectlyHiding (scheme : Scheme Message Commitment Opening) : Prop
```

`Cslib.Crypto.Protocols.Commitment.Scheme.StatisticallyHiding` (definition, [line 61](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/Commitment/Defs.lean#L61))

> A scheme is statistically hiding with error `ε` when the commitment
> distributions of any two messages are within statistical distance `ε`
> ([BonehShoup2023], Definition 3.5 and Section 8.12).

```lean
def StatisticallyHiding [Fintype Commitment]
    (scheme : Scheme Message Commitment Opening) (ε : ℝ≥0) : Prop
```

`Cslib.Crypto.Protocols.Commitment.Scheme.PerfectlyBinding` (definition, [line 71](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/Commitment/Defs.lean#L71))

> A scheme is perfectly binding when a commitment can be opened to at most
> one message: any two accepted openings of the same commitment agree on the
> message ([BonehShoup2023], Section 8.12). Different openings of the same
> message are still allowed.

```lean
def PerfectlyBinding (scheme : Scheme Message Commitment Opening) : Prop
```

## Depends on

- [Commitment Schemes: Syntax and Correctness](scheme.md)
- [Statistical Distance of Finite Probability Mass Functions](../../../probability/statisticaldistance.md)

## Sources

- [Cslib/Crypto/Protocols/Commitment/Defs.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/Commitment/Defs.lean)
