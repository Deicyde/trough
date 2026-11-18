---
catalog: module
lean: Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.jointDist_eq, Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.jointDist_tsum_fst, Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.perfectlySecret_iff_indep, Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.perfectlySecret_iff_ciphertextIndist, Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.indep_of_ciphertextIndist, Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.perfectlySecret_keySpace_ge
statement: formalized
proof: formalized
---

# Perfect Secrecy

`Cslib.Crypto.Protocols.PerfectSecrecy.Basic`, in [Cslib/Crypto/Protocols/PerfectSecrecy/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/PerfectSecrecy/Basic.lean), by Samuel Schlesinger.

> Characterisation theorems for perfect secrecy following
> [KatzLindell2020], Chapter 2: the equivalence with message-ciphertext
> independence, the ciphertext indistinguishability characterization, and
> Shannon's key-space bound.
>
> ## Main results
>
> - `Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.perfectlySecret_iff_indep`:
>   perfect secrecy is exactly message-ciphertext independence
> - `Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.perfectlySecret_iff_ciphertextIndist`:
>   ciphertext indistinguishability characterization ([KatzLindell2020], Lemma 2.5)
> - `Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.perfectlySecret_keySpace_ge`:
>   Shannon's theorem, `|K| ≥ |M|` ([KatzLindell2020], Theorem 2.12)
>
> ## References
>
> * [J. Katz, Y. Lindell, *Introduction to Modern Cryptography*][KatzLindell2020]

`Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.jointDist_eq` (theorem, [line 43](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/PerfectSecrecy/Basic.lean#L43))

> The joint distribution at `(m, c)` equals `msgDist m * ciphertextDist m c`.

```lean
theorem jointDist_eq (scheme : EncScheme M K C) (msgDist : PMF M)
    (m : M) (c : C) :
    scheme.jointDist msgDist (m, c) = msgDist m * scheme.ciphertextDist m c
```

`Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.jointDist_tsum_fst` (theorem, [line 50](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/PerfectSecrecy/Basic.lean#L50))

> Summing the joint distribution over messages gives the marginal ciphertext
> distribution.

```lean
theorem jointDist_tsum_fst (scheme : EncScheme M K C) (msgDist : PMF M) (c : C) :
    ∑' m, scheme.jointDist msgDist (m, c) = scheme.marginalCiphertextDist msgDist c
```

`Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.perfectlySecret_iff_indep` (theorem, [line 56](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/PerfectSecrecy/Basic.lean#L56))

> Perfect secrecy is equivalent to message-ciphertext independence.
> The two formulations are related by multiplying/dividing by `marginal(c)`.

```lean
theorem perfectlySecret_iff_indep (scheme : EncScheme M K C) :
    scheme.PerfectlySecret ↔
    ∀ (msgDist : PMF M) (m : M) (c : C),
      scheme.jointDist msgDist (m, c) =
        msgDist m * scheme.marginalCiphertextDist msgDist c
```

`Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.perfectlySecret_iff_ciphertextIndist` (theorem, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/PerfectSecrecy/Basic.lean#L77))

> A scheme is perfectly secret iff the ciphertext distribution is
> independent of the plaintext ([KatzLindell2020], Lemma 2.5).

```lean
theorem perfectlySecret_iff_ciphertextIndist (scheme : EncScheme M K C) :
    scheme.PerfectlySecret ↔ scheme.CiphertextIndist
```

`Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.indep_of_ciphertextIndist` (theorem, [line 95](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/PerfectSecrecy/Basic.lean#L95))

> Ciphertext indistinguishability implies message-ciphertext independence.

```lean
theorem indep_of_ciphertextIndist (scheme : EncScheme M K C)
    (h : scheme.CiphertextIndist) (msgDist : PMF M) (m : M) (c : C) :
    scheme.jointDist msgDist (m, c) =
      msgDist m * scheme.marginalCiphertextDist msgDist c
```

`Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.perfectlySecret_keySpace_ge` (theorem, [line 115](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/PerfectSecrecy/Basic.lean#L115))

> Perfect secrecy requires `|K| ≥ |M|` — Shannon's theorem
> ([KatzLindell2020], Theorem 2.12).

```lean
theorem perfectlySecret_keySpace_ge [Finite K]
    (scheme : EncScheme M K C) (h : scheme.PerfectlySecret) :
    Nat.card M ≤ Nat.card K
```

## Depends on

- [Perfect Secrecy: Definitions](defs.md)

## Sources

- [Cslib/Crypto/Protocols/PerfectSecrecy/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/PerfectSecrecy/Basic.lean)
