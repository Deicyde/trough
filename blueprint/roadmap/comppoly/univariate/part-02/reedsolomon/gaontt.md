---
catalog: module
lean: CompPoly.ReedSolomon.Gao.decodeFrom, CompPoly.ReedSolomon.Gao.decode_eq_decodeFrom, CompPoly.ReedSolomon.Gao.vanishingRaw, CompPoly.ReedSolomon.Gao.vanishingNTT, CompPoly.ReedSolomon.Gao.toPoly_vanishingNTT, CompPoly.ReedSolomon.Gao.castToRS, CompPoly.ReedSolomon.Gao.nodalPoly_nttDomainToRS, CompPoly.ReedSolomon.Gao.receivedInterpolant_nttDomainToRS, CompPoly.ReedSolomon.Gao.decodeNTT, CompPoly.ReedSolomon.Gao.decodeNTT_eq_decode, CompPoly.ReedSolomon.Gao.decodePlan, CompPoly.ReedSolomon.Gao.decodePlan_eq_decode
statement: formalized
proof: formalized
---

# Gao Decoding on an NTT Domain

`CompPoly.Univariate.ReedSolomon.GaoNTT`, in [CompPoly/Univariate/ReedSolomon/GaoNTT.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoNTT.lean), by Derek Sorensen.

> `Gao.decode` builds its two Euclidean inputs by definition: the nodal polynomial as a fold of
> `n` linear factors, and the received interpolant by Lagrange's formula, `O(n²)` per basis
> polynomial. On the evaluation domain of a radix-2 NTT domain both have fast forms. The nodal
> polynomial is `Xⁿ - 1` (`NTT.Domain.nodal_eq_X_pow_sub_one`), and the interpolant is the
> inverse NTT (`NTT.interpolate`). `decodeNTT` uses both, and `decodeNTT_eq_decode` proves it
> equal to `decode`, so every correctness theorem of `GaoCorrectness.lean` transfers unchanged.
>
> ## Main definitions
>
> * `Gao.decodeFrom`: the Euclidean stage of `decode` on given inputs `(g₀, g₁)`.
> * `Gao.vanishingNTT`: the polynomial `Xⁿ - 1` of an NTT domain.
>
> …
>
> ## Main results
>
> * `Gao.nodalPoly_nttDomainToRS`: the nodal polynomial of the induced domain is `Xⁿ - 1`.
> * `Gao.receivedInterpolant_nttDomainToRS`: the received interpolant is the inverse NTT.
> * `Gao.decodeNTT_eq_decode`, `Gao.decodePlan_eq_decode`: the fast decoders are `decode`.

`CompPoly.ReedSolomon.Gao.decodeFrom` (definition, [line 48](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoNTT.lean#L48))

> The Euclidean stage of Gao's decoder on the inputs `(g₀, g₁)`, for block length `n`.

```lean
def decodeFrom (k n : ℕ) (g₀ g₁ : CPolynomial F) : Option (CPolynomial F)
```

`CompPoly.ReedSolomon.Gao.decode_eq_decodeFrom` (theorem, [line 56](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoNTT.lean#L56))

> `decode` is its Euclidean stage applied to the nodal polynomial and the interpolant.

```lean
theorem decode_eq_decodeFrom (k : ℕ) (D : Domain F) (r : Vector F D.n) :
    decode k D r = decodeFrom k D.n (nodalPoly D) (receivedInterpolant D r)
```

`CompPoly.ReedSolomon.Gao.vanishingRaw` (definition, [line 61](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoNTT.lean#L61))

> The coefficient array `#[-1, 0, …, 0, 1]` of `Xⁿ - 1`, for `n ≥ 1`.

```lean
def vanishingRaw (n : ℕ) : CPolynomial.Raw F
```

`CompPoly.ReedSolomon.Gao.vanishingNTT` (definition, [line 66](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoNTT.lean#L66))

> The vanishing polynomial `Xⁿ - 1` of an NTT domain, written down coefficient by
> coefficient rather than multiplied out of `n` linear factors.

```lean
def vanishingNTT (D : NTT.Domain F) : CPolynomial F
```

`CompPoly.ReedSolomon.Gao.toPoly_vanishingNTT` (theorem, [line 70](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoNTT.lean#L70))

```lean
theorem toPoly_vanishingNTT (D : NTT.Domain F) :
    (vanishingNTT D).toPoly = Polynomial.X ^ D.n - 1
```

`CompPoly.ReedSolomon.Gao.castToRS` (definition, [line 89](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoNTT.lean#L89))

> Transport a received word over the NTT domain to the induced Reed-Solomon domain.

```lean
def castToRS (D : NTT.Domain F) (r : Vector F D.n) : Vector F (nttDomainToRS D).n
```

`CompPoly.ReedSolomon.Gao.nodalPoly_nttDomainToRS` (theorem, [line 100](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoNTT.lean#L100))

> The nodal polynomial of the Reed-Solomon domain induced by an NTT domain is `Xⁿ - 1`.

```lean
theorem nodalPoly_nttDomainToRS (D : NTT.Domain F) :
    nodalPoly (nttDomainToRS D) = vanishingNTT D
```

`CompPoly.ReedSolomon.Gao.receivedInterpolant_nttDomainToRS` (theorem, [line 109](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoNTT.lean#L109))

> The received interpolant on the induced domain is the inverse NTT of the word.

```lean
theorem receivedInterpolant_nttDomainToRS (D : NTT.Domain F) (r : Vector F D.n) :
    receivedInterpolant (nttDomainToRS D) (castToRS D r) = NTT.interpolate D r
```

`CompPoly.ReedSolomon.Gao.decodeNTT` (definition, [line 130](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoNTT.lean#L130))

> Gao's decoder on an NTT domain, with `Xⁿ - 1` as the nodal polynomial and the inverse
> NTT as the interpolant.

```lean
def decodeNTT (k : ℕ) (D : NTT.Domain F) (r : Vector F D.n) :
    Option (CPolynomial F)
```

`CompPoly.ReedSolomon.Gao.decodeNTT_eq_decode` (theorem, [line 135](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoNTT.lean#L135))

> The NTT decoder is Gao's decoder on the induced Reed-Solomon domain.

```lean
theorem decodeNTT_eq_decode (k : ℕ) (D : NTT.Domain F) (r : Vector F D.n) :
    decodeNTT k D r = decode k (nttDomainToRS D) (castToRS D r)
```

`CompPoly.ReedSolomon.Gao.decodePlan` (definition, [line 142](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoNTT.lean#L142))

> Gao's decoder through a reusable NTT plan.

```lean
def decodePlan (k : ℕ) (P : NTTFast.Plan F) (r : Vector F P.domain.n) :
    Option (CPolynomial F)
```

`CompPoly.ReedSolomon.Gao.decodePlan_eq_decode` (theorem, [line 147](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoNTT.lean#L147))

> A well-formed plan decodes as Gao's decoder on the induced Reed-Solomon domain.

```lean
theorem decodePlan_eq_decode (k : ℕ) (P : NTTFast.Plan F)
    (hP : NTTFast.Plan.WellFormed P) (r : Vector F P.domain.n) :
    decodePlan k P r = decode k (nttDomainToRS P.domain) (castToRS P.domain r)
```

## Depends on

- [NTTFast and Interpolation](../../part-01/nttfast/interpolation.md)
- [Gao Decoder for Reed-Solomon Codes](gaodecoder.md)
- [NTT Encoding of Reed-Solomon Codewords](nttencode.md)

## Proof depends on

- [Barycentric Interpolation on an NTT Domain](../../part-01/ntt/barycentric.md)
- [Gao Decoder Correctness](gaocorrectness.md)
- [`C`, `eval₂`, and coefficient-mapping as ring homomorphisms](../topoly/ringhom.md)

## Sources

- [CompPoly/Univariate/ReedSolomon/GaoNTT.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoNTT.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.ReedSolomon.GaoNTT.json)
