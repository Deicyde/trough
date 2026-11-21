---
catalog: module
lean: BF128Ghash.irreducible_of_rabin_128_passed_over_GF2, BF128Ghash.ghashPoly_irreducible, BF128Ghash.BF128Ghash, BF128Ghash.instFieldBF128Ghash, BF128Ghash.instCommRingBF128Ghash, BF128Ghash.instNontrivialBF128Ghash, BF128Ghash.ofGF2, BF128Ghash.root, BF128Ghash.root_satisfies_poly, BF128Ghash.BF128Ghash_card
statement: formalized
proof: formalized
---

# BinaryField128Ghash

`CompPoly.Fields.Binary.BF128Ghash.Basic`, in [CompPoly/Fields/Binary/BF128Ghash/Basic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Basic.lean), by Chung Thai Nguyen, Quang Dao.

> Define `GF(2^128)` as a single field extension over `GF(2)` using the GHASH polynomial
> from AES-GCM: `P(X) = X^128 + X^7 + X^2 + X + 1`.
>
> ## Main Definitions
>
> - `ghashPoly`: The defining polynomial `X^128 + X^7 + X^2 + X + 1` over `GF(2)`
> - `BF128Ghash`: The field `GF(2^128)` defined as `GF(2)[X]/(ghashPoly)`
> - `ghashPoly_irreducible`: The irreducibility of the GHASH polynomial
> - `irreducible_of_rabin_128_passed_over_GF2`: The lemma that if the two Rabin conditions
>     hold for a degree 128 polynomial, it MUST be irreducible.
>
> ## Proof Strategy (Rabin's Irreducibility Test)
>
> For a polynomial `P` of degree `n` over `GF(q)`, `P` is irreducible iff:
> 1. `P` divides `X^(q^n) - X`
> 2. `EuclideanDomain.gcd(P, X^(q^(n/l)) - X) = 1` for all prime factors `l` of `n`.
>
> For GHASH (`n=128`, `q=2`), the only prime factor of `128` is `2`.
> Thus, we only need to check:
> 1. `P | (X^(2^128) + X)`   (Note: `-X = +X` in `GF(2)`)
> 2. `EuclideanDomain.gcd(P, X^(2^64) + X) = 1`
>
> ## References
> * [NIST-SP-800-38D] Dworkin, M. Recommendation for Block Cipher Modes of Operation:
>   Galois/Counter Mode (GCM) and GMAC. NIST Special Publication 800-38D.
>   https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf
>
> * [Rabin80] Michael O. Rabin. Probabilistic Algorithms in Finite Fields.
>   SIAM Journal on Computing, 9(2):273-280, 1980. https://doi.org/10.1137/0209024

`BF128Ghash.irreducible_of_rabin_128_passed_over_GF2` (lemma, [line 64](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Basic.lean#L64))

> **Rabin's Irreducibility Test (Specialized for Degree 128)**
>
> This lemma proves that if the two Rabin conditions hold for a degree 128 polynomial,
> it MUST be irreducible. It formalizes Lemma 1 from Rabin's paper.
>
> Hypotheses:
> 1. `h_deg`: P has degree 128.
> 2. `h_trace`: P divides X^(2^128) - X (in GF(2), +X and -X are the same).
> 3. `h_gcd`: EuclideanDomain.gcd(P, X^(2^64) - X) = 1.

```lean
lemma irreducible_of_rabin_128_passed_over_GF2 (P : Polynomial (ZMod 2))
    (h_deg : P.natDegree = 128)
    (h_trace : P ∣ ((X : Polynomial (ZMod 2)) ^ (2 ^ 128) + X))
    (h_gcd : EuclideanDomain.gcd ((X : Polynomial (ZMod 2)) ^ (2 ^ 64) + X) P = 1) :
    Irreducible P
```

`BF128Ghash.ghashPoly_irreducible` (theorem, [line 128](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Basic.lean#L128))

> `ghashPoly` is irreducible, using Rabin's Irreducibility Test:
> - `X_pow_2_pow_128_eq`: X^(2^128) = X (mod ghashPoly)
> - `rabin_gcd_condition_gHashPoly`: EuclideanDomain.gcd(X^(2^64) + X, ghashPoly) = 1

```lean
theorem ghashPoly_irreducible : Irreducible ghashPoly
```

`BF128Ghash.BF128Ghash` (abbreviation, [line 152](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Basic.lean#L152))

> GF(2^128) as the quotient field GF(2)[X]/(P(X)) where P is the GHASH polynomial.

```lean
abbrev BF128Ghash : Type
```

`BF128Ghash.instFieldBF128Ghash` (instance, [line 155](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Basic.lean#L155))

> BF128Ghash is a field.

```lean
instance instFieldBF128Ghash : Field BF128Ghash
```

`BF128Ghash.instCommRingBF128Ghash` (instance, [line 158](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Basic.lean#L158))

> BF128Ghash is a commutative ring.

```lean
instance instCommRingBF128Ghash : CommRing BF128Ghash
```

`BF128Ghash.instNontrivialBF128Ghash` (instance, [line 161](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Basic.lean#L161))

> BF128Ghash is nontrivial.

```lean
instance instNontrivialBF128Ghash : Nontrivial BF128Ghash
```

`BF128Ghash.ofGF2` (definition, [line 175](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Basic.lean#L175))

> The canonical embedding of GF(2) into BF128Ghash.

```lean
def ofGF2 : ZMod 2 →+* BF128Ghash
```

`BF128Ghash.root` (definition, [line 178](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Basic.lean#L178))

> The generator of the field (root of the GHASH polynomial).

```lean
def root : BF128Ghash
```

`BF128Ghash.root_satisfies_poly` (theorem, [line 182](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Basic.lean#L182))

> The root satisfies the GHASH polynomial equation:
> root^128 + root^7 + root^2 + root + 1 = 0

```lean
theorem root_satisfies_poly : root^128 + root^7 + root^2 + root + 1 = 0
```

`BF128Ghash.BF128Ghash_card` (theorem, [line 205](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Basic.lean#L205))

> The cardinality of BF128Ghash is 2^128.

```lean
theorem BF128Ghash_card : Fintype.card BF128Ghash = 2^128
```

## Depends on

- [BinaryField128Ghash Prelude](prelude.md)

## Proof depends on

- [XPowTwoPow Gcd Certificate](xpowtwopowgcdcertificate.md)

## Sources

- [CompPoly/Fields/Binary/BF128Ghash/Basic.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Basic.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Fields.Binary.BF128Ghash.Basic.json)
