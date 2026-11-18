---
catalog: module
lean: Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.ciphertextDist, Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.jointDist, Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.marginalCiphertextDist, Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.posteriorMsgDist, Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.posteriorMsgDist_apply, Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.PerfectlySecret, Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.CiphertextIndist
statement: formalized
proof: formalized
---

# Perfect Secrecy: Definitions

`Cslib.Crypto.Protocols.PerfectSecrecy.Defs`, in [Cslib/Crypto/Protocols/PerfectSecrecy/Defs.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/PerfectSecrecy/Defs.lean), by Samuel Schlesinger.

> Core definitions for perfect secrecy following [KatzLindell2020], Chapter 2.
>
> ## Main definitions
>
> - `Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.ciphertextDist`:
>   ciphertext distribution for a given message
> - `Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.jointDist`:
>   joint (message, ciphertext) distribution given a message prior
> - `Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.marginalCiphertextDist`:
>   marginal ciphertext distribution given a message prior
> - `Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.posteriorMsgDist`:
>   posterior message distribution `Pr[M | C = c]` as a `PMF`
> - `Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.PerfectlySecret`:
>   perfect secrecy ([KatzLindell2020], Definition 2.3)
> - `Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.CiphertextIndist`:
>   ciphertext indistinguishability ([KatzLindell2020], Lemma 2.5)

`Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.ciphertextDist` (definition, [line 44](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/PerfectSecrecy/Defs.lean#L44))

> The distribution of `Enc_K(m)` when `K ← Gen`.

```lean
noncomputable def ciphertextDist (scheme : EncScheme M K C) (m : M) : PMF C
```

`Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.jointDist` (definition, [line 48](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/PerfectSecrecy/Defs.lean#L48))

> Joint distribution of `(M, C)` given a message prior.

```lean
noncomputable def jointDist (scheme : EncScheme M K C) (msgDist : PMF M) : PMF (M × C)
```

`Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.marginalCiphertextDist` (definition, [line 53](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/PerfectSecrecy/Defs.lean#L53))

> Marginal ciphertext distribution given a message prior.

```lean
noncomputable def marginalCiphertextDist (scheme : EncScheme M K C)
    (msgDist : PMF M) : PMF C
```

`Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.posteriorMsgDist` (definition, [line 60](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/PerfectSecrecy/Defs.lean#L60))

> The posterior message distribution `Pr[M | C = c]` as a probability
> distribution, given a message prior and a ciphertext in the support of
> the marginal distribution.

```lean
noncomputable def posteriorMsgDist (scheme : EncScheme M K C)
    (msgDist : PMF M) (c : C)
    (hc : c ∈ (scheme.marginalCiphertextDist msgDist).support) : PMF M
```

`Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.posteriorMsgDist_apply` (theorem, [line 66](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/PerfectSecrecy/Defs.lean#L66))

```lean
theorem posteriorMsgDist_apply (scheme : EncScheme M K C)
    (msgDist : PMF M) (c : C)
    (hc : c ∈ (scheme.marginalCiphertextDist msgDist).support) (m : M) :
    scheme.posteriorMsgDist msgDist c hc m =
      scheme.jointDist msgDist (m, c) / scheme.marginalCiphertextDist msgDist c
```

`Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.PerfectlySecret` (definition, [line 76](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/PerfectSecrecy/Defs.lean#L76))

> An encryption scheme is perfectly secret if the posterior message
> distribution equals the prior for every ciphertext with positive probability
> ([KatzLindell2020], Definition 2.3).

```lean
def PerfectlySecret (scheme : EncScheme M K C) : Prop
```

`Cslib.Crypto.Protocols.PerfectSecrecy.EncScheme.CiphertextIndist` (definition, [line 83](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/PerfectSecrecy/Defs.lean#L83))

> Ciphertext indistinguishability: the ciphertext distribution is the same
> for all messages ([KatzLindell2020], Lemma 2.5).

```lean
def CiphertextIndist (scheme : EncScheme M K C) : Prop
```

## Depends on

- [Private-Key Encryption Schemes (Information-Theoretic)](encryption.md)
- [PMF Utilities](../../../probability/pmf.md)

## Sources

- [Cslib/Crypto/Protocols/PerfectSecrecy/Defs.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/PerfectSecrecy/Defs.lean)
