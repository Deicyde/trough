---
catalog: module
lean: Cslib.Crypto.Protocols.SecretSharing.Shamir.Polynomial.tailPolynomial, Cslib.Crypto.Protocols.SecretSharing.Shamir.Polynomial.tailPolynomial_coeff, Cslib.Crypto.Protocols.SecretSharing.Shamir.Polynomial.tailPolynomial_degree_lt, Cslib.Crypto.Protocols.SecretSharing.Shamir.Polynomial.tailPolynomial_add, Cslib.Crypto.Protocols.SecretSharing.Shamir.Polynomial.sharingPolynomial, Cslib.Crypto.Protocols.SecretSharing.Shamir.Polynomial.sharingPolynomial_eval, Cslib.Crypto.Protocols.SecretSharing.Shamir.Polynomial.coeff_zero_sharingPolynomial, Cslib.Crypto.Protocols.SecretSharing.Shamir.Polynomial.constantCoeff_sharingPolynomial, Cslib.Crypto.Protocols.SecretSharing.Shamir.Polynomial.natDegree_sharingPolynomial_le, Cslib.Crypto.Protocols.SecretSharing.Shamir.Polynomial.degree_sharingPolynomial_lt_succ, Cslib.Crypto.Protocols.SecretSharing.Shamir.Polynomial.degree_sharingPolynomial_tailPolynomial_lt_succ, Cslib.Crypto.Protocols.SecretSharing.Shamir.Polynomial.reconstruct, Cslib.Crypto.Protocols.SecretSharing.Shamir.Polynomial.reconstruct_eq_constantCoeff_of_eval_eq, Cslib.Crypto.Protocols.SecretSharing.Shamir.Polynomial.reconstruct_sharingPolynomial_eq_secret
statement: formalized
proof: formalized
---

# Shamir Secret Sharing: Polynomial Utilities

`Cslib.Crypto.Protocols.SecretSharing.Shamir.Polynomial`, in [Cslib/Crypto/Protocols/SecretSharing/Shamir/Polynomial.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Shamir/Polynomial.lean), by Samuel Schlesinger.

> This file contains the Shamir-specific polynomial and interpolation utilities
> used to prove correctness and privacy of the public scheme construction.

`Cslib.Crypto.Protocols.SecretSharing.Shamir.Polynomial.tailPolynomial` (definition, [line 28](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Shamir/Polynomial.lean#L28))

> The tail polynomial determined by the first `n` coefficients.

```lean
def tailPolynomial (n : ℕ) (coeffs : Fin n → F) : _root_.Polynomial F
```

`Cslib.Crypto.Protocols.SecretSharing.Shamir.Polynomial.tailPolynomial_coeff` (theorem, [line 32](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Shamir/Polynomial.lean#L32))

```lean
theorem tailPolynomial_coeff (n : ℕ) (coeffs : Fin n → F) (i : Fin n) :
    (tailPolynomial (F := F) n coeffs).coeff i = coeffs i
```

`Cslib.Crypto.Protocols.SecretSharing.Shamir.Polynomial.tailPolynomial_degree_lt` (theorem, [line 39](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Shamir/Polynomial.lean#L39))

> `tailPolynomial n coeffs` has degree `< n` by construction.

```lean
theorem tailPolynomial_degree_lt (n : ℕ) (coeffs : Fin n → F) :
    (tailPolynomial (F := F) n coeffs).degree < n
```

`Cslib.Crypto.Protocols.SecretSharing.Shamir.Polynomial.tailPolynomial_add` (theorem, [line 46](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Shamir/Polynomial.lean#L46))

> `tailPolynomial` is additive in its coefficient vector.

```lean
theorem tailPolynomial_add (n : ℕ) (a b : Fin n → F) :
    tailPolynomial (F := F) n (a + b) = tailPolynomial n a + tailPolynomial n b
```

`Cslib.Crypto.Protocols.SecretSharing.Shamir.Polynomial.sharingPolynomial` (definition, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Shamir/Polynomial.lean#L51))

> The standard Shamir sharing polynomial `s + X * q(X)`.

```lean
def sharingPolynomial (secretValue : F) (tail : _root_.Polynomial F) : _root_.Polynomial F
```

`Cslib.Crypto.Protocols.SecretSharing.Shamir.Polynomial.sharingPolynomial_eval` (theorem, [line 55](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Shamir/Polynomial.lean#L55))

```lean
theorem sharingPolynomial_eval (secretValue x : F) (tail : _root_.Polynomial F) :
    (sharingPolynomial secretValue tail).eval x = secretValue + x * tail.eval x
```

`Cslib.Crypto.Protocols.SecretSharing.Shamir.Polynomial.coeff_zero_sharingPolynomial` (theorem, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Shamir/Polynomial.lean#L59))

```lean
theorem coeff_zero_sharingPolynomial (secretValue : F) (tail : _root_.Polynomial F) :
    (sharingPolynomial secretValue tail).coeff 0 = secretValue
```

`Cslib.Crypto.Protocols.SecretSharing.Shamir.Polynomial.constantCoeff_sharingPolynomial` (theorem, [line 63](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Shamir/Polynomial.lean#L63))

```lean
theorem constantCoeff_sharingPolynomial (secretValue : F) (tail : _root_.Polynomial F) :
    (sharingPolynomial secretValue tail).constantCoeff = secretValue
```

`Cslib.Crypto.Protocols.SecretSharing.Shamir.Polynomial.natDegree_sharingPolynomial_le` (theorem, [line 70](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Shamir/Polynomial.lean#L70))

> If the tail polynomial has degree `< n`, then the sharing polynomial has
> natural degree at most `n`.

```lean
theorem natDegree_sharingPolynomial_le (secretValue : F) (tail : _root_.Polynomial F) {n : ℕ}
    (hdeg : tail.degree < n) :
    (sharingPolynomial secretValue tail).natDegree ≤ n
```

`Cslib.Crypto.Protocols.SecretSharing.Shamir.Polynomial.degree_sharingPolynomial_lt_succ` (theorem, [line 90](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Shamir/Polynomial.lean#L90))

> If the tail polynomial has degree `< n`, then the sharing polynomial has
> degree `< n + 1`.

```lean
theorem degree_sharingPolynomial_lt_succ (secretValue : F) (tail : _root_.Polynomial F) {n : ℕ}
    (hdeg : tail.degree < n) :
    (sharingPolynomial secretValue tail).degree < (n + 1 : WithBot ℕ)
```

`Cslib.Crypto.Protocols.SecretSharing.Shamir.Polynomial.degree_sharingPolynomial_tailPolynomial_lt_succ` (theorem, [line 99](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Shamir/Polynomial.lean#L99))

> The coefficient-vector version of `degree_sharingPolynomial_lt_succ`.

```lean
theorem degree_sharingPolynomial_tailPolynomial_lt_succ
    (secretValue : F) (n : ℕ) (coeffs : Fin n → F) :
    (sharingPolynomial secretValue (tailPolynomial n coeffs)).degree <
      (n + 1 : WithBot ℕ)
```

`Cslib.Crypto.Protocols.SecretSharing.Shamir.Polynomial.reconstruct` (definition, [line 110](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Shamir/Polynomial.lean#L110))

> Reconstruct the secret from finitely indexed share values by interpolating
> the unique low-degree polynomial that matches them.

```lean
def reconstruct (x σ : ι → F) : F
```

`Cslib.Crypto.Protocols.SecretSharing.Shamir.Polynomial.reconstruct_eq_constantCoeff_of_eval_eq` (theorem, [line 117](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Shamir/Polynomial.lean#L117))

> Reconstruction recovers the constant coefficient of any low-degree
> polynomial from its values at distinct points.

```lean
theorem reconstruct_eq_constantCoeff_of_eval_eq
    {x : ι → F} {p : _root_.Polynomial F}
    (hx : Function.Injective x)
    (hdeg : p.degree < Fintype.card ι) :
    reconstruct x (fun i => p.eval (x i)) = p.constantCoeff
```

`Cslib.Crypto.Protocols.SecretSharing.Shamir.Polynomial.reconstruct_sharingPolynomial_eq_secret` (theorem, [line 134](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Shamir/Polynomial.lean#L134))

> Reconstruction succeeds on the values of a Shamir sharing polynomial once
> the finite index type is large enough.

```lean
theorem reconstruct_sharingPolynomial_eq_secret
    {x : ι → F} {secretValue : F} {tail : _root_.Polynomial F}
    (hx : Function.Injective x)
    (hdeg : (sharingPolynomial secretValue tail).degree < Fintype.card ι) :
    reconstruct x
      (fun i => (sharingPolynomial secretValue tail).eval (x i)) = secretValue
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Crypto/Protocols/SecretSharing/Shamir/Polynomial.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Protocols/SecretSharing/Shamir/Polynomial.lean)
