---
catalog: module
lean: Cslib.Crypto.Protocols.Commitment.Scheme, Cslib.Crypto.Protocols.Commitment.Scheme.commitmentDist, Cslib.Crypto.Protocols.Commitment.Scheme.mem_support_commitmentDist_iff, Cslib.Crypto.Protocols.Commitment.Scheme.Accepts, Cslib.Crypto.Protocols.Commitment.Scheme.accepts_of_mem_support, Cslib.Crypto.Protocols.Commitment.Scheme.ofPure
statement: formalized
proof: formalized
---

# Commitment Schemes: Syntax and Correctness

`Cslib.Crypto.Protocols.Commitment.Scheme`, in [Cslib/Crypto/Protocols/Commitment/Scheme.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/Commitment/Scheme.lean), by Samuel Schlesinger.

> The syntax of a commitment scheme ([BonehShoup2023], Section 8.12): committing
> to a message samples a commitment-opening pair `(c, o)`, verification of a
> claimed opening is deterministic, and honestly generated pairs always verify.
>
> The algorithms are plain functions, with no efficiency or finiteness
> assumptions. Security notions live in separate definitions, so the same syntax
> can carry perfect, statistical, or computational security.
>
> ## Main definitions
>
> - `Scheme`: commitment syntax with perfect correctness
> - `Scheme.commitmentDist`: the public commitment distribution for a message
> - `Scheme.mem_support_commitmentDist_iff`: a commitment is possible exactly
>   when it has a possible opening
> - `Scheme.Accepts`: the verifier's acceptance relation
>
> ## References
>
> * [D. Boneh, V. Shoup, *A Graduate Course in Applied Cryptography*,
>   Version 0.6][BonehShoup2023]

`Cslib.Crypto.Protocols.Commitment.Scheme` (structure, [line 49](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/Commitment/Scheme.lean#L49))

> A noninteractive, unkeyed commitment scheme over message, commitment, and
> opening types ([BonehShoup2023], Section 8.12).
>
> Committing is randomized and produces the commitment and opening together,
> since the two may be correlated. Correctness requires that every
> commitment-opening pair the honest committer can output is accepted by the
> verifier; for a `PMF`, this says honest openings verify with probability
> one.

```lean
structure Scheme (Message Commitment Opening : Type*) where
  /-- Randomized commitment and opening generation. -/
  commit (message : Message) : PMF (Commitment × Opening)
  /-- Deterministic verification of a claimed opening. -/
  verify (message : Message) (commitment : Commitment) (opening : Opening) : Bool
  /-- Every honestly generated commitment-opening pair verifies. -/
  correct : ∀ message commitment opening,
    (commitment, opening) ∈ (commit message).support →
      verify message commitment opening = true
```

`Cslib.Crypto.Protocols.Commitment.Scheme.commitmentDist` (definition, [line 64](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/Commitment/Scheme.lean#L64))

> The public commitment distribution obtained by forgetting the opening.

```lean
noncomputable def commitmentDist (scheme : Scheme Message Commitment Opening)
    (message : Message) : PMF Commitment
```

`Cslib.Crypto.Protocols.Commitment.Scheme.mem_support_commitmentDist_iff` (theorem, [line 70](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/Commitment/Scheme.lean#L70))

> A commitment lies in the public distribution's support exactly when some
> opening makes the corresponding pair an honest possible output.

```lean
theorem mem_support_commitmentDist_iff
    (scheme : Scheme Message Commitment Opening) {message : Message}
    {commitment : Commitment} :
    commitment ∈ (scheme.commitmentDist message).support ↔
      ∃ opening, (commitment, opening) ∈ (scheme.commit message).support
```

`Cslib.Crypto.Protocols.Commitment.Scheme.Accepts` (definition, [line 78](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/Commitment/Scheme.lean#L78))

> The proposition that an opening is accepted for a commitment and message.

```lean
def Accepts (scheme : Scheme Message Commitment Opening) (message : Message)
    (commitment : Commitment) (opening : Opening) : Prop
```

`Cslib.Crypto.Protocols.Commitment.Scheme.accepts_of_mem_support` (theorem, [line 83](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/Commitment/Scheme.lean#L83))

> Every pair in the support of an honest commitment is accepted.

```lean
theorem accepts_of_mem_support (scheme : Scheme Message Commitment Opening)
    {message : Message} {commitment : Commitment} {opening : Opening}
    (h : (commitment, opening) ∈ (scheme.commit message).support) :
    scheme.Accepts message commitment opening
```

`Cslib.Crypto.Protocols.Commitment.Scheme.ofPure` (definition, [line 90](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/Commitment/Scheme.lean#L90))

> Build a commitment scheme from a deterministic commitment generation.

```lean
noncomputable def ofPure (commit : Message → Commitment × Opening)
    (verify : Message → Commitment → Opening → Bool)
    (correct : ∀ message, verify message (commit message).1 (commit message).2 = true) :
    Scheme Message Commitment Opening
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Crypto/Protocols/Commitment/Scheme.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/Commitment/Scheme.lean)
