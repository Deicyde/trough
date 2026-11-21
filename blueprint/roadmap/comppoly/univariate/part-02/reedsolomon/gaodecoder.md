---
catalog: module
lean: CompPoly.ReedSolomon.Gao.nodalPoly, CompPoly.ReedSolomon.Gao.receivedInterpolant, CompPoly.ReedSolomon.Gao.partialGcd, CompPoly.ReedSolomon.Gao.decode
statement: formalized
proof: formalized
---

# Gao Decoder for Reed-Solomon Codes

`CompPoly.Univariate.ReedSolomon.GaoDecoder`, in [CompPoly/Univariate/ReedSolomon/GaoDecoder.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoDecoder.lean), by Juan Conejero.

> Gao's decoding algorithm [Gao02] for the Reed-Solomon code of `ReedSolomon.lean`;
> correctness is proved in `GaoCorrectness.lean`.
>
> ## Main definitions
>
> * `nodalPoly`, `receivedInterpolant`: the decoder's inputs to the partial EEA, the nodal
>   polynomial `g₀ = ∏ (x − aᵢ)` and the interpolant `g₁` of the received word.
> * `partialGcd`: the partial extended Euclidean algorithm on `(g₀, g₁)` with stopping
>   threshold `⌈(n+k)/2⌉`.
> * `decode`: the decoder; returns the recovered message polynomial, or `none`.
>
> ## References
>
> * [Gao, S., *A New Algorithm for Decoding Reed-Solomon Codes*][Gao02]

`CompPoly.ReedSolomon.Gao.nodalPoly` (definition, [line 38](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoDecoder.lean#L38))

> Nodal polynomial of the evaluation domain: `g₀(x) = ∏ a ∈ D, (x − a)`.

```lean
def nodalPoly [Ring F] [BEq F] [LawfulBEq F] [Nontrivial F] (D : Domain F) : CPolynomial F
```

`CompPoly.ReedSolomon.Gao.receivedInterpolant` (definition, [line 43](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoDecoder.lean#L43))

> Unique polynomial `g₁ ∈ 𝔽[X]` of degree < `D.n` such that
> `g₁(aᵢ) = r[i]` for `aᵢ ∈ D`.

```lean
def receivedInterpolant [Field F] [BEq F] [LawfulBEq F]
    (D : Domain F) (r : Vector F D.n) : CPolynomial F
```

`CompPoly.ReedSolomon.Gao.partialGcd` (definition, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoDecoder.lean#L49))

> Partial extended Euclidean algorithm stopping when the remainder
> has degree less than `(n + k + 1)/2 = ⌈(n+k)/2⌉`.

```lean
def partialGcd [Field F] [BEq F] [LawfulBEq F]
    (k : ℕ) (D : Domain F) (r : Vector F D.n) :
    CPolynomial F × CPolynomial F × CPolynomial F
```

`CompPoly.ReedSolomon.Gao.decode` (definition, [line 66](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoDecoder.lean#L66))

> Gao's algorithm.
>
> Apply the partial EEA to the nodal polynomial `g₀` and the interpolant `g₁` of
> the received word, stopping at threshold `(n + k + 1)/2`, where `n = D.n` is the
> block length and `k` the message length. This yields a triple `(g, u, v)`
> satisfying the Bézout identity `g = u * g₀ + v * g₁`, where:
> - `g` is the first residue with degree below the threshold
> - `v` is the error-locator polynomial (`u` is discarded)
>
> Decoding succeeds when `v` divides `g` and `g / v` has degree below `k`, in
> which case the recovered message polynomial is `g / v`.

```lean
def decode [Field F] [BEq F] [LawfulBEq F]
    (k : ℕ) (D : Domain F) (r : Vector F D.n) :
    Option (CPolynomial F)
```

## Depends on

- [Extended Euclidean Algorithm for `CPolynomial`](../../part-01/euclideanalgorithm.md)
- [Lagrange Interpolation](../../part-01/lagrange.md)
- [Reed-Solomon Codes](../../part-01/reedsolomon.md)

## Sources

- [CompPoly/Univariate/ReedSolomon/GaoDecoder.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoDecoder.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.ReedSolomon.GaoDecoder.json)
