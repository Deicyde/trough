---
catalog: module
lean: Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme, Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.ofPure
statement: formalized
proof: formalized
---

# Private-Key Encryption Schemes (Information-Theoretic)

`Cslib.Crypto.Protocols.PerfectSecrecy.Encryption`, in [Cslib/Crypto/Protocols/PerfectSecrecy/Encryption.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/PerfectSecrecy/Encryption.lean), by Samuel Schlesinger.

> An information-theoretic private-key encryption scheme following
> [KatzLindell2020], Definition 2.1. Key generation and encryption are
> probability distributions over arbitrary types, with no computational
> constraints.
>
> ## Main definitions
>
> - `Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme`:
>   a private-key encryption scheme (Gen, Enc, Dec) with correctness
>
> ## References
>
> * [J. Katz, Y. Lindell, *Introduction to Modern Cryptography*][KatzLindell2020]

`Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme` (structure, [line 38](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/PerfectSecrecy/Encryption.lean#L38))

> A private-key encryption scheme over message space `M`, key space `K`,
> and ciphertext space `C` ([KatzLindell2020], Definition 2.1).

```lean
structure EncScheme (Message Key Ciphertext : Type*) where
  /-- Probabilistic key generation. -/
  gen : PMF Key
  /-- (Possibly randomized) encryption. -/
  enc (key : Key) (message : Message) : PMF Ciphertext
  /-- Deterministic decryption. -/
  dec (key : Key) (ciphertext : Ciphertext) : Message
  /-- Decryption inverts encryption for all keys in the support of `gen`. -/
  correct : ∀ key, key ∈ gen.support → ∀ message ciphertext,
    ciphertext ∈ (enc key message).support → dec key ciphertext = message
```

`Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.ofPure` (definition, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/PerfectSecrecy/Encryption.lean#L51))

> Build an encryption scheme from deterministic pure encryption/decryption
> where decryption is a left inverse of encryption for every key.

```lean
noncomputable def EncScheme.ofPure.{u} {Message Key Ciphertext : Type u} (gen : PMF Key)
    (enc : Key → Message → Ciphertext) (dec : Key → Ciphertext → Message)
    (h : ∀ key, Function.LeftInverse (dec key) (enc key)) :
    EncScheme Message Key Ciphertext
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Crypto/Protocols/PerfectSecrecy/Encryption.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/PerfectSecrecy/Encryption.lean)
