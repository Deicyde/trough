---
catalog: module
lean: Cslib.Crypto.Protocols.PerfectSecrecy.otp, Cslib.Crypto.Protocols.PerfectSecrecy.otp_ciphertextDist_eq_uniform, Cslib.Crypto.Protocols.PerfectSecrecy.otp_perfectlySecret
statement: formalized
proof: formalized
---

# One-Time Pad

`Cslib.Crypto.Protocols.PerfectSecrecy.OneTimePad`, in [Cslib/Crypto/Protocols/PerfectSecrecy/OneTimePad.lean](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Crypto/Protocols/PerfectSecrecy/OneTimePad.lean), by Samuel Schlesinger.

> The one-time pad (Vernam cipher) over `BitVec l`
> ([KatzLindell2020], Construction 2.9).
>
> ## Main definitions
>
> - `Cslib.Crypto.Protocols.PerfectSecrecy.otp`: the one-time pad encryption scheme
>
> ## Main results
>
> - `Cslib.Crypto.Protocols.PerfectSecrecy.otp_perfectlySecret`:
>   the one-time pad is perfectly secret ([KatzLindell2020], Theorem 2.10)
>
> ## References
>
> * [J. Katz, Y. Lindell, *Introduction to Modern Cryptography*][KatzLindell2020]

`Cslib.Crypto.Protocols.PerfectSecrecy.otp` (definition, [line 41](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Crypto/Protocols/PerfectSecrecy/OneTimePad.lean#L41))

> The one-time pad over `l`-bit strings. Encryption and decryption
> are XOR ([KatzLindell2020], Construction 2.9).

```lean
noncomputable def otp (l : ℕ) :
    EncScheme (BitVec l) (BitVec l) (BitVec l)
```

`Cslib.Crypto.Protocols.PerfectSecrecy.otp_ciphertextDist_eq_uniform` (theorem, [line 49](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Crypto/Protocols/PerfectSecrecy/OneTimePad.lean#L49))

> The ciphertext distribution of the OTP is uniform, regardless of the
> message: masking with a uniform key is the permutation `Equiv.xor` of the
> uniform distribution.

```lean
theorem otp_ciphertextDist_eq_uniform (l : ℕ) (m : BitVec l) :
    (otp l).ciphertextDist m = uniformOfFintype (BitVec l)
```

`Cslib.Crypto.Protocols.PerfectSecrecy.otp_perfectlySecret` (theorem, [line 57](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Crypto/Protocols/PerfectSecrecy/OneTimePad.lean#L57))

> The one-time pad is perfectly secret ([KatzLindell2020], Theorem 2.10).

```lean
theorem otp_perfectlySecret (l : ℕ) : (otp l).PerfectlySecret
```

## Depends on

- [Perfect Secrecy: Definitions](defs.md)

## Proof depends on

- [Perfect Secrecy](basic.md)

## Sources

- [Cslib/Crypto/Protocols/PerfectSecrecy/OneTimePad.lean at 7c95c37f](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Crypto/Protocols/PerfectSecrecy/OneTimePad.lean)
- [Declaration ledger](../../../../../sources/cslib/Cslib.Crypto.Protocols.PerfectSecrecy.OneTimePad.json)
