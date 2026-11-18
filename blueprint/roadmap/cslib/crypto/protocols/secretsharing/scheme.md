---
catalog: module
lean: Cslib.Crypto.Protocols.SecretSharing.viewDistOf, Cslib.Crypto.Protocols.SecretSharing.Scheme, Cslib.Crypto.Protocols.SecretSharing.Scheme.view, Cslib.Crypto.Protocols.SecretSharing.Scheme.view_apply, Cslib.Crypto.Protocols.SecretSharing.Scheme.reconstruct_view_eq_secret, Cslib.Crypto.Protocols.SecretSharing.Scheme.not_authorized_of_subset
statement: formalized
proof: formalized
---

# Secret Sharing Schemes

`Cslib.Crypto.Protocols.SecretSharing.Scheme`, in [Cslib/Crypto/Protocols/SecretSharing/Scheme.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Scheme.lean), by Samuel Schlesinger.

> A secret-sharing scheme bundles the deterministic sharing/reconstruction
> interface, the distribution on randomness, and privacy for unauthorized
> coalitions.
>
> ## Main definitions
>
> - `Cslib.Crypto.Protocols.SecretSharing.Scheme`:
>   a secret-sharing scheme with correctness and privacy
> - `Cslib.Crypto.Protocols.SecretSharing.Scheme.view`:
>   the restricted shares seen by one coalition
>
> ## References
>
> * [Adi Shamir, *How to Share a Secret*][Shamir1979]
> * [J. Katz, Y. Lindell, *Introduction to Modern Cryptography*][KatzLindell2020]

`Cslib.Crypto.Protocols.SecretSharing.viewDistOf` (definition, [line 38](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Scheme.lean#L38))

> The view distribution induced by raw sharing data.

```lean
noncomputable def viewDistOf {Secret Randomness Party Share : Type*}
    (gen : PMF Randomness) (share : Randomness → Secret → Party → Share)
    (s : Finset Party) (secret : Secret) : PMF (s → Share)
```

`Cslib.Crypto.Protocols.SecretSharing.Scheme` (structure, [line 52](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Scheme.lean#L52))

> A secret-sharing scheme over secret space `Secret`, randomness space
> `Randomness`, party set `Party`, and share space `Share`.
>
> Correctness is deterministic: every authorized coalition reconstructs the
> secret from the shares generated using any randomness seed. Privacy is
> distributional: unauthorized coalitions have the same view distribution for all
> secrets.

```lean
structure Scheme (Secret Randomness Party Share : Type*) where
  /-- The distribution used to sample the protocol's randomness. -/
  gen : PMF Randomness
  /-- Sharing algorithm: one randomness seed determines one share per party. -/
  share : Randomness → Secret → Party → Share
  /-- Reconstruction from a coalition's observed shares. -/
  reconstruct (s : Finset Party) : (s → Share) → Secret
  /-- Authorized coalitions. -/
  authorized : Finset Party → Prop
  /-- Authorization is monotone in the coalition. -/
  authorized_mono : Monotone authorized
  /-- Authorized coalitions reconstruct the secret from the restricted view. -/
  correct :
    ∀ (r : Randomness) (secret : Secret) (s : Finset Party),
      authorized s → reconstruct s (fun i => share r secret i) = secret
  /-- Unauthorized coalitions receive secret-independent view distributions. -/
  view_indist :
    ∀ (s : Finset Party), ¬ authorized s → ∀ secret₀ secret₁ : Secret,
      viewDistOf gen share s secret₀ = viewDistOf gen share s secret₁
```

`Cslib.Crypto.Protocols.SecretSharing.Scheme.view` (definition, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Scheme.lean#L77))

> The restricted shares observed by the coalition `s`.

```lean
def view (scheme : Scheme Secret Randomness Party Share) (s : Finset Party)
    (r : Randomness) (secret : Secret) : s → Share
```

`Cslib.Crypto.Protocols.SecretSharing.Scheme.view_apply` (theorem, [line 82](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Scheme.lean#L82))

```lean
theorem view_apply (scheme : Scheme Secret Randomness Party Share) (s : Finset Party)
    (r : Randomness) (secret : Secret) (i : s) :
    scheme.view s r secret i = scheme.share r secret i
```

`Cslib.Crypto.Protocols.SecretSharing.Scheme.reconstruct_view_eq_secret` (theorem, [line 88](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Scheme.lean#L88))

> Authorized coalitions reconstruct the secret from the restricted view.

```lean
theorem reconstruct_view_eq_secret
    (scheme : Scheme Secret Randomness Party Share)
    (r : Randomness) (secret : Secret) {s : Finset Party}
    (hs : scheme.authorized s) :
    scheme.reconstruct s (scheme.view s r secret) = secret
```

`Cslib.Crypto.Protocols.SecretSharing.Scheme.not_authorized_of_subset` (theorem, [line 96](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Scheme.lean#L96))

> Any sub-coalition of an unauthorized coalition is unauthorized as well.

```lean
theorem not_authorized_of_subset
    (scheme : Scheme Secret Randomness Party Share)
    {s t : Finset Party} (hst : s ⊆ t)
    (ht : ¬ scheme.authorized t) :
    ¬ scheme.authorized s
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Crypto/Protocols/SecretSharing/Scheme.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Scheme.lean)
