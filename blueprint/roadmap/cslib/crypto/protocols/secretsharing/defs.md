---
catalog: module
lean: Cslib.Crypto.Protocols.SecretSharing.Scheme.shareDist, Cslib.Crypto.Protocols.SecretSharing.Scheme.viewDist, Cslib.Crypto.Protocols.SecretSharing.Scheme.viewDist_eq_of_not_authorized, Cslib.Crypto.Protocols.SecretSharing.Scheme.posteriorSecretDist, Cslib.Crypto.Protocols.SecretSharing.Scheme.posteriorSecretDist_apply, Cslib.Crypto.Protocols.SecretSharing.Scheme.PerfectlyPrivate, Cslib.Crypto.Protocols.SecretSharing.Scheme.perfectlyPrivate
statement: formalized
proof: formalized
---

# Secret Sharing: Definitions

`Cslib.Crypto.Protocols.SecretSharing.Defs`, in [Cslib/Crypto/Protocols/SecretSharing/Defs.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Defs.lean), by Samuel Schlesinger.

> Privacy for secret sharing is part of the `Scheme` interface. This file exposes
> the corresponding view and posterior distributions, plus theorem-friendly
> consequences of the built-in privacy field.
>
> ## Main definitions
>
> - `Cslib.Crypto.Protocols.SecretSharing.Scheme.shareDist`:
>   the full share distribution for one secret
> - `Cslib.Crypto.Protocols.SecretSharing.Scheme.viewDist`:
>   the distribution of the restricted view for one coalition
> - `Cslib.Crypto.Protocols.SecretSharing.Scheme.posteriorSecretDist`:
>   the posterior distribution on secrets after observing one view
> - `Cslib.Crypto.Protocols.SecretSharing.Scheme.PerfectlyPrivate`:
>   posterior equals prior for unauthorized coalitions
> - `Cslib.Crypto.Protocols.SecretSharing.Scheme.perfectlyPrivate`:
>   every scheme has posterior privacy
>
> ## References
>
> * [Adi Shamir, *How to Share a Secret*][Shamir1979]
> * [J. Katz, Y. Lindell, *Introduction to Modern Cryptography*][KatzLindell2020]

`Cslib.Crypto.Protocols.SecretSharing.Scheme.shareDist` (definition, [line 49](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Defs.lean#L49))

> The distribution of the full share assignment for one secret.

```lean
noncomputable def shareDist (scheme : Scheme Secret Randomness Party Share)
    (secret : Secret) : PMF (Party → Share)
```

`Cslib.Crypto.Protocols.SecretSharing.Scheme.viewDist` (definition, [line 54](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Defs.lean#L54))

> The view distribution induced on the coalition `s`.

```lean
noncomputable def viewDist (scheme : Scheme Secret Randomness Party Share)
    (s : Finset Party) (secret : Secret) : PMF (s → Share)
```

`Cslib.Crypto.Protocols.SecretSharing.Scheme.viewDist_eq_of_not_authorized` (theorem, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Defs.lean#L59))

> Unauthorized coalitions receive secret-independent view distributions.

```lean
theorem viewDist_eq_of_not_authorized
    (scheme : Scheme Secret Randomness Party Share)
    {s : Finset Party} (hs : ¬ scheme.authorized s)
    (secret₀ secret₁ : Secret) :
    scheme.viewDist s secret₀ = scheme.viewDist s secret₁
```

`Cslib.Crypto.Protocols.SecretSharing.Scheme.posteriorSecretDist` (definition, [line 68](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Defs.lean#L68))

> The posterior distribution on secrets after observing the coalition view
> `v`.

```lean
noncomputable def posteriorSecretDist
    (scheme : Scheme Secret Randomness Party Share)
    (s : Finset Party) (secretDist : PMF Secret) (v : s → Share)
    (hv : v ∈ (secretDist.bind (scheme.viewDist s)).support) : PMF Secret
```

`Cslib.Crypto.Protocols.SecretSharing.Scheme.posteriorSecretDist_apply` (theorem, [line 75](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Defs.lean#L75))

```lean
theorem posteriorSecretDist_apply
    (scheme : Scheme Secret Randomness Party Share)
    (s : Finset Party) (secretDist : PMF Secret) (v : s → Share)
    (hv : v ∈ (secretDist.bind (scheme.viewDist s)).support) (secret : Secret) :
    scheme.posteriorSecretDist s secretDist v hv secret =
      (secretDist.bind fun secret' =>
        (scheme.viewDist s secret').bind fun v' => PMF.pure (secret', v')) (secret, v) /
        (secretDist.bind (scheme.viewDist s)) v
```

`Cslib.Crypto.Protocols.SecretSharing.Scheme.PerfectlyPrivate` (definition, [line 87](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Defs.lean#L87))

> Perfect privacy for unauthorized coalitions: conditioning on a view does not
> change the prior on secrets.

```lean
def PerfectlyPrivate (scheme : Scheme Secret Randomness Party Share) : Prop
```

`Cslib.Crypto.Protocols.SecretSharing.Scheme.perfectlyPrivate` (theorem, [line 94](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Defs.lean#L94))

> Every scheme has posterior privacy by definition of `Scheme`.

```lean
theorem perfectlyPrivate
    (scheme : Scheme Secret Randomness Party Share) :
    scheme.PerfectlyPrivate
```

## Depends on

- [Secret Sharing Schemes](scheme.md)
- [PMF Utilities](../../../probability/pmf.md)

## Sources

- [Cslib/Crypto/Protocols/SecretSharing/Defs.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Defs.lean)
