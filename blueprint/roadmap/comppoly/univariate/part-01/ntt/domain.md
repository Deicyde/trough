---
catalog: module
lean: CompPoly.CPolynomial.NTT.Domain, CompPoly.CPolynomial.NTT.Domain.n, CompPoly.CPolynomial.NTT.Domain.Idx, CompPoly.CPolynomial.NTT.Domain.node, CompPoly.CPolynomial.NTT.Domain.omegaInv, CompPoly.CPolynomial.NTT.Domain.inverse, CompPoly.CPolynomial.NTT.Domain.nInv, CompPoly.CPolynomial.NTT.Domain.n_pos, CompPoly.CPolynomial.NTT.Domain.n_ne_zero, CompPoly.CPolynomial.NTT.Domain.natCast_ne_zero, CompPoly.CPolynomial.NTT.Domain.requiredLength, CompPoly.CPolynomial.NTT.Domain.requiredLength_eq_zero_of_left_trim_size_zero, CompPoly.CPolynomial.NTT.Domain.requiredLength_eq_zero_of_right_trim_size_zero, CompPoly.CPolynomial.NTT.Domain.requiredLength_eq_of_trim_size_pos, CompPoly.CPolynomial.NTT.Domain.fits, CompPoly.CPolynomial.NTT.Domain.truncate, CompPoly.CPolynomial.NTT.bestLogN, CompPoly.CPolynomial.NTT.loadNaturalArray, CompPoly.CPolynomial.NTT.size_loadNaturalArray, CompPoly.CPolynomial.NTT.getElem_loadNaturalArray, CompPoly.CPolynomial.NTT.loadNaturalVector, CompPoly.CPolynomial.NTT.FittingDomain, CompPoly.CPolynomial.NTT.bestDomainForLength?
statement: formalized
proof: formalized
---

# NTT Domain

`CompPoly.Univariate.NTT.Domain`, in [CompPoly/Univariate/NTT/Domain.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Domain.lean), by Salih Erdem Koçak, Doran Pamukçu, Valerii Huhnin.

> This file defines the radix-2 NTT domain parameters and basic raw-polynomial
> shape helpers used by forward/inverse NTT.

`CompPoly.CPolynomial.NTT.Domain` (structure, [line 29](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Domain.lean#L29))

> Parameters for a radix-2 NTT domain of size `2 ^ logN`.

```lean
structure Domain (R : Type*) [Field R] where
  logN : Nat
  omega : R
  primitive : IsPrimitiveRoot omega (2 ^ logN)
```

`CompPoly.CPolynomial.NTT.Domain.n` (definition, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Domain.lean#L37))

> Domain size.

```lean
def n (D : Domain R) : Nat
```

`CompPoly.CPolynomial.NTT.Domain.Idx` (abbreviation, [line 40](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Domain.lean#L40))

> Index type for vectors over the domain.

```lean
abbrev Idx (D : Domain R)
```

`CompPoly.CPolynomial.NTT.Domain.node` (definition, [line 43](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Domain.lean#L43))

> The `i`-th evaluation node `omega^i`.

```lean
def node (D : Domain R) (i : D.Idx) : R
```

`CompPoly.CPolynomial.NTT.Domain.omegaInv` (definition, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Domain.lean#L46))

> Inverse root of unity.

```lean
def omegaInv (D : Domain R) : R
```

`CompPoly.CPolynomial.NTT.Domain.inverse` (definition, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Domain.lean#L49))

> The domain with the inverse root, used by inverse NTT butterflies.

```lean
def inverse (D : Domain R) : Domain R
```

`CompPoly.CPolynomial.NTT.Domain.nInv` (definition, [line 56](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Domain.lean#L56))

> Multiplicative inverse of the domain size in `R`.

```lean
def nInv (D : Domain R) : R
```

`CompPoly.CPolynomial.NTT.Domain.n_pos` (lemma, [line 58](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Domain.lean#L58))

```lean
lemma n_pos (D : Domain R) : 0 < D.n
```

`CompPoly.CPolynomial.NTT.Domain.n_ne_zero` (lemma, [line 61](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Domain.lean#L61))

```lean
lemma n_ne_zero (D : Domain R) : D.n ≠ 0
```

`CompPoly.CPolynomial.NTT.Domain.natCast_ne_zero` (theorem, [line 65](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Domain.lean#L65))

> The size of an NTT domain is nonzero in its coefficient field.

```lean
theorem natCast_ne_zero (D : Domain R) : ((D.n : Nat) : R) ≠ 0
```

`CompPoly.CPolynomial.NTT.Domain.requiredLength` (definition, [line 74](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Domain.lean#L74))

> Required convolution length for multiplying `p` and `q`.

```lean
def requiredLength (p q : CPolynomial.Raw R) : Nat
```

`CompPoly.CPolynomial.NTT.Domain.requiredLength_eq_zero_of_left_trim_size_zero` (theorem, [line 80](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Domain.lean#L80))

```lean
theorem requiredLength_eq_zero_of_left_trim_size_zero
    (p q : CPolynomial.Raw R) (hp : p.trim.size = 0) :
    requiredLength p q = 0
```

`CompPoly.CPolynomial.NTT.Domain.requiredLength_eq_zero_of_right_trim_size_zero` (theorem, [line 85](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Domain.lean#L85))

```lean
theorem requiredLength_eq_zero_of_right_trim_size_zero
    (p q : CPolynomial.Raw R) (hq : q.trim.size = 0) :
    requiredLength p q = 0
```

`CompPoly.CPolynomial.NTT.Domain.requiredLength_eq_of_trim_size_pos` (theorem, [line 90](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Domain.lean#L90))

```lean
theorem requiredLength_eq_of_trim_size_pos
    (p q : CPolynomial.Raw R) (hp : 0 < p.trim.size) (hq : 0 < q.trim.size) :
    requiredLength p q = p.trim.size + q.trim.size - 1
```

`CompPoly.CPolynomial.NTT.Domain.fits` (definition, [line 98](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Domain.lean#L98))

> Whether domain `D` is large enough for multiplying `p` and `q`.

```lean
def fits (D : Domain R) (p q : CPolynomial.Raw R) : Prop
```

`CompPoly.CPolynomial.NTT.Domain.truncate` (definition, [line 102](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Domain.lean#L102))

> Truncate a polynomial to at most `m` coefficients.

```lean
def truncate (m : Nat) (p : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.NTT.bestLogN` (definition, [line 109](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Domain.lean#L109))

> The smallest radix-2 exponent that can cover a requested convolution length.

```lean
def bestLogN (requiredLen : Nat) : Nat
```

`CompPoly.CPolynomial.NTT.loadNaturalArray` (definition, [line 113](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Domain.lean#L113))

> Load an array in natural order and pad it to a domain-sized array.

```lean
def loadNaturalArray (D : Domain R) (a : Array R) : Array R
```

`CompPoly.CPolynomial.NTT.size_loadNaturalArray` (theorem, [line 116](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Domain.lean#L116))

```lean
theorem size_loadNaturalArray (D : Domain R) (a : Array R) :
    (loadNaturalArray D a).size = D.n
```

`CompPoly.CPolynomial.NTT.getElem_loadNaturalArray` (theorem, [line 120](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Domain.lean#L120))

```lean
theorem getElem_loadNaturalArray (D : Domain R) (a : Array R) (i : Nat)
    (hi : i < (loadNaturalArray D a).size) :
    (loadNaturalArray D a)[i] = a.getD i 0
```

`CompPoly.CPolynomial.NTT.loadNaturalVector` (definition, [line 126](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Domain.lean#L126))

> Load an array in natural order and pad it to a domain-sized vector.

```lean
def loadNaturalVector (D : Domain R) (a : Array R) : Vector R D.n
```

`CompPoly.CPolynomial.NTT.FittingDomain` (abbreviation, [line 130](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Domain.lean#L130))

> An NTT domain bundled with proof that it covers the requested convolution length.

```lean
abbrev FittingDomain (R : Type*) [Field R] (requiredLen : Nat)
```

`CompPoly.CPolynomial.NTT.bestDomainForLength?` (definition, [line 139](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Domain.lean#L139))

> Generic adapter from field-specific radix-2 domain tables to a best-fitting domain lookup.
>
> The adapter chooses `logN = Nat.clog 2 requiredLen`, then returns `none` if that exponent
> is outside the supported table.

```lean
def bestDomainForLength?
    (maxLogN : Nat) (domainOfLogN : (logN : Nat) → logN ≤ maxLogN → Domain R)
    (domainOfLogN_logN : ∀ logN hlogN, (domainOfLogN logN hlogN).logN = logN)
    (requiredLen : Nat) : Option (FittingDomain R requiredLen)
```

## Depends on

- [Raw Computable Univariate Polynomials](../raw/core.md)

## Sources

- [CompPoly/Univariate/NTT/Domain.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Domain.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.NTT.Domain.json)
