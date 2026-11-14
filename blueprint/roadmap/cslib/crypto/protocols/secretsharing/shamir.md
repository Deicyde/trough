---
catalog: module
lean: Cslib.Crypto.Protocols.SecretSharing.Shamir.Params, Cslib.Crypto.Protocols.SecretSharing.Shamir.Randomness, Cslib.Crypto.Protocols.SecretSharing.Shamir.authorized, Cslib.Crypto.Protocols.SecretSharing.Shamir.authorized_univ, Cslib.Crypto.Protocols.SecretSharing.Shamir.share, Cslib.Crypto.Protocols.SecretSharing.Shamir.reconstruct, Cslib.Crypto.Protocols.SecretSharing.Shamir.TailSampler, Cslib.Crypto.Protocols.SecretSharing.Shamir.uniformTailSampler, Cslib.Crypto.Protocols.SecretSharing.Shamir.view_indist_of_tailSampler, Cslib.Crypto.Protocols.SecretSharing.Shamir.schemeWith, Cslib.Crypto.Protocols.SecretSharing.Shamir.scheme, Cslib.Crypto.Protocols.SecretSharing.Shamir.schemeWith_authorized_iff, Cslib.Crypto.Protocols.SecretSharing.Shamir.scheme_authorized_iff, Cslib.Crypto.Protocols.SecretSharing.Shamir.schemeWith_share_eq, Cslib.Crypto.Protocols.SecretSharing.Shamir.reconstruct_view_eq_secret
statement: formalized
proof: formalized
---

# Shamir Secret Sharing

`Cslib.Crypto.Protocols.SecretSharing.Shamir`, in [Cslib/Crypto/Protocols/SecretSharing/Shamir.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Shamir.lean), by Samuel Schlesinger.

> This module presents a secure-by-construction API for finite-party Shamir secret
> sharing through the abstract `SecretSharing.Scheme` interface.
>
> The public constructors require two pieces of data:
>
> - public parameters consisting of a threshold together with distinct, nonzero
>   evaluation points for a finite party set
> - a translation-invariant sampler on the tail coefficients
>
> Translation invariance is exactly the symmetry used in the privacy proof. The
> canonical finite-field instance is obtained by taking the sampler to be uniform.
>
> ## Main definitions
>
> - `Cslib.Crypto.Protocols.SecretSharing.Shamir.Params`:
>   the threshold and public evaluation points
> - `Cslib.Crypto.Protocols.SecretSharing.Shamir.Randomness`:
>   the vector of tail coefficients
> - `Cslib.Crypto.Protocols.SecretSharing.Shamir.TailSampler`:
>   a translation-invariant distribution on tail coefficients
> - `Cslib.Crypto.Protocols.SecretSharing.Shamir.schemeWith`:
>   Shamir's scheme with a privacy-preserving tail sampler
> - `Cslib.Crypto.Protocols.SecretSharing.Shamir.scheme`:
>   the corresponding finite-field scheme with uniform randomness
>
> ## Main results
>
> - `Cslib.Crypto.Protocols.SecretSharing.Shamir.reconstruct_view_eq_secret`:
>   any authorized coalition reconstructs the secret
> - `Cslib.Crypto.Protocols.SecretSharing.Shamir.authorized_univ`:
>   the full party set is always authorized
>
> ## Notes
>
> The public share type is just the field `F`: the evaluation points are fixed in
> `Params`, so one share consists only of the corresponding field value.
>
> ## References
>
> * [Adi Shamir, *How to Share a Secret*][Shamir1979]
> * [J. Katz, Y. Lindell, *Introduction to Modern Cryptography*][KatzLindell2020]

`Cslib.Crypto.Protocols.SecretSharing.Shamir.Params` (structure, [line 72](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Shamir.lean#L72))

> Public parameters for a finite Shamir secret-sharing instance. The threshold
> is bundled with the evaluation points so the API can enforce the standard
> non-vacuous `threshold < number of parties` side condition.

```lean
structure Params (F : Type*) [Zero F] (Party : Type*) [Fintype Party] where
  /-- A coalition of size `threshold + 1` is the first authorized size. -/
  threshold : ℕ
  /-- Standard Shamir sharing requires `threshold < number of parties`. -/
  threshold_lt_card : threshold < Fintype.card Party
  /-- The public evaluation point assigned to each party. -/
  point : Party → F
  /-- Distinct parties receive distinct evaluation points. -/
  point_injective : Function.Injective point
  /-- Standard Shamir sharing forbids the point `0`, which would reveal the
  secret directly. -/
  point_nonzero : ∀ i : Party, point i ≠ 0
```

`Cslib.Crypto.Protocols.SecretSharing.Shamir.Randomness` (abbreviation, [line 86](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Shamir.lean#L86))

> The random coefficients of the degree-`threshold - 1` tail polynomial.

```lean
abbrev Randomness (params : Params F Party)
```

`Cslib.Crypto.Protocols.SecretSharing.Shamir.authorized` (definition, [line 90](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Shamir.lean#L90))

> A coalition is authorized exactly when it contains at least
> `params.threshold + 1` parties.

```lean
def authorized (params : Params F Party) (s : Finset Party) : Prop
```

`Cslib.Crypto.Protocols.SecretSharing.Shamir.authorized_univ` (theorem, [line 95](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Shamir.lean#L95))

> Because `params.threshold < |Party|`, the full party set can always
> reconstruct the secret.

```lean
theorem authorized_univ {F Party : Type*} [Field F] [Fintype Party]
    (params : Params F Party) :
    authorized params (Finset.univ : Finset Party)
```

`Cslib.Crypto.Protocols.SecretSharing.Shamir.share` (definition, [line 101](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Shamir.lean#L101))

> The Shamir share value sent to one party.

```lean
noncomputable def share (params : Params F Party)
    (coeffs : Randomness params) (secretValue : F) (i : Party) : F
```

`Cslib.Crypto.Protocols.SecretSharing.Shamir.reconstruct` (definition, [line 107](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Shamir.lean#L107))

> Reconstruct the secret from one coalition's Shamir shares.

```lean
noncomputable def reconstruct (params : Params F Party)
    (s : Finset Party) (σ : s → F) : F
```

`Cslib.Crypto.Protocols.SecretSharing.Shamir.TailSampler` (structure, [line 114](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Shamir.lean#L114))

> A sampler on Shamir tail coefficients is privacy-compatible when its
> distribution is invariant under translation by any coefficient vector. This is
> the exact symmetry needed in the privacy proof.

```lean
structure TailSampler (params : Params F Party) where
  /-- The underlying coefficient distribution. -/
  gen : PMF (Randomness params)
  /-- Translating the coefficients does not change the distribution. -/
  map_add_eq_self : ∀ δ : Randomness params, gen.map (fun coeffs => coeffs + δ) = gen
```

`Cslib.Crypto.Protocols.SecretSharing.Shamir.uniformTailSampler` (definition, [line 121](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Shamir.lean#L121))

> Uniform tail coefficients form the canonical privacy-compatible sampler.

```lean
noncomputable def uniformTailSampler (params : Params F Party)
    [Fintype F] [Nonempty F] : TailSampler params
```

`Cslib.Crypto.Protocols.SecretSharing.Shamir.view_indist_of_tailSampler` (theorem, [line 207](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Shamir.lean#L207))

> Translation-invariant Shamir tail samplers induce secret-independent views
> for unauthorized coalitions.

```lean
theorem view_indist_of_tailSampler (params : Params F Party)
    (sampler : TailSampler params) :
    ∀ (s : Finset Party), ¬ authorized params s → ∀ secret₀ secret₁ : F,
      viewDistOf sampler.gen (share params) s secret₀ =
        viewDistOf sampler.gen (share params) s secret₁
```

`Cslib.Crypto.Protocols.SecretSharing.Shamir.schemeWith` (definition, [line 242](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Shamir.lean#L242))

> Shamir's scheme built from a privacy-compatible tail sampler.

```lean
noncomputable def schemeWith (params : Params F Party) (sampler : TailSampler params)
    :
    SecretSharing.Scheme F (Randomness params) Party F
```

`Cslib.Crypto.Protocols.SecretSharing.Shamir.scheme` (definition, [line 280](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Shamir.lean#L280))

> The canonical finite-field Shamir scheme with uniformly sampled tail
> coefficients.

```lean
noncomputable def scheme (params : Params F Party)
    [Fintype F] [Nonempty F] :
    SecretSharing.Scheme F (Randomness params) Party F
```

`Cslib.Crypto.Protocols.SecretSharing.Shamir.schemeWith_authorized_iff` (theorem, [line 286](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Shamir.lean#L286))

```lean
theorem schemeWith_authorized_iff (params : Params F Party)
    (sampler : TailSampler params) (s : Finset Party) :
    (schemeWith params sampler).authorized s ↔ params.threshold + 1 ≤ s.card
```

`Cslib.Crypto.Protocols.SecretSharing.Shamir.scheme_authorized_iff` (theorem, [line 292](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Shamir.lean#L292))

```lean
theorem scheme_authorized_iff (params : Params F Party)
    [Fintype F] [Nonempty F] (s : Finset Party) :
    (scheme params).authorized s ↔ params.threshold + 1 ≤ s.card
```

`Cslib.Crypto.Protocols.SecretSharing.Shamir.schemeWith_share_eq` (theorem, [line 298](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Shamir.lean#L298))

```lean
theorem schemeWith_share_eq (params : Params F Party)
    (sampler : TailSampler params) (coeffs : Randomness params)
    (secretValue : F) (i : Party) :
    (schemeWith params sampler).share coeffs secretValue i =
      share params coeffs secretValue i
```

`Cslib.Crypto.Protocols.SecretSharing.Shamir.reconstruct_view_eq_secret` (theorem, [line 306](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Shamir.lean#L306))

> Any authorized coalition reconstructs the secret from the shares it sees.

```lean
theorem reconstruct_view_eq_secret
    (params : Params F Party) (sampler : TailSampler params)
    (coeffs : Randomness params) (secretValue : F) {s : Finset Party}
    (hs : (schemeWith params sampler).authorized s) :
    (schemeWith params sampler).reconstruct s
      ((schemeWith params sampler).view s coeffs secretValue) = secretValue
```

## Depends on

- [Secret Sharing Schemes](scheme.md)
- [Shamir Secret Sharing: Polynomial Utilities](shamir-2/polynomial.md)
- [PMF Utilities](../../../probability/pmf.md)

## Sources

- [Cslib/Crypto/Protocols/SecretSharing/Shamir.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Shamir.lean)
