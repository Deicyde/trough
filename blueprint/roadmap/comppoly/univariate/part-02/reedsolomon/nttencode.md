---
catalog: module
lean: CompPoly.ReedSolomon.nttDomainToRS, CompPoly.ReedSolomon.nttDomainToRS_n, CompPoly.ReedSolomon.forwardImpl_eq_encode, CompPoly.ReedSolomon.nttCodeword, CompPoly.ReedSolomon.nttCodeword_eq_encode
statement: formalized
proof: formalized
---

# NTT Encoding of Reed-Solomon Codewords

`CompPoly.Univariate.ReedSolomon.NTTEncode`, in [CompPoly/Univariate/ReedSolomon/NTTEncode.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/ReedSolomon/NTTEncode.lean), by Abraxas1010 (IAOM / Apoth3osis).

> Over the evaluation domain induced by a radix-2 NTT domain (the node array
> `#[ω⁰, ω¹, …, ω^(n-1)]`, nodup because powers of a primitive `n`-th root below `n` are
> pairwise distinct), the forward NTT of a message polynomial's coefficients **is** the
> Reed-Solomon encoding: `forwardImpl_eq_encode` ties the `O(n log n)` evaluation path
> (`NTT.Forward.forwardImpl`, in natural order) to the definitional encoder
> (`ReedSolomon.encode`) exactly, for every message of length at most the domain size.
> No padding is required: `messagePoly` trims, so the degree bound `k ≤ D.n` suffices.
>
> `nttCodeword` packages the forward-NTT output as a length-indexed vector over the induced
> domain, with `nttCodeword_eq_encode` the packaged form of the equality.
>
> Note the natural-order caveat: `NTTFast.forwardImpl` returns evaluations in bit-reversed
> order (`forwardImpl_eq_bitRevPermute_evalOnDomain`), so the fast variant relates to
> `encode` only after composing with `bitRevPermute`; this file deliberately uses the
> natural-order `NTT.Forward.forwardImpl`.
>
> ## Main definitions
>
> * `ReedSolomon.nttDomainToRS`: the Reed-Solomon evaluation domain induced by an NTT domain.
> * `ReedSolomon.nttCodeword`: the forward-NTT output as a `Vector F (nttDomainToRS D).n`.
>
> ## Main results
>
> * `ReedSolomon.forwardImpl_eq_encode`: the forward NTT of `messagePoly msg` equals
>   `encode (nttDomainToRS D) msg`, as arrays.
> * `ReedSolomon.nttCodeword_eq_encode`: the packaged (vector-level) form.

`CompPoly.ReedSolomon.nttDomainToRS` (definition, [line 56](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/ReedSolomon/NTTEncode.lean#L56))

> The Reed-Solomon evaluation domain induced by a radix-2 NTT domain: the node array
> `#[ω⁰, ω¹, …, ω^(n-1)]`, nodup because powers of a primitive `n`-th root below `n` are
> pairwise distinct.

```lean
def nttDomainToRS (D : CPolynomial.NTT.Domain F) : ReedSolomon.Domain F
```

`CompPoly.ReedSolomon.nttDomainToRS_n` (lemma, [line 64](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/ReedSolomon/NTTEncode.lean#L64))

```lean
lemma nttDomainToRS_n (D : CPolynomial.NTT.Domain F) :
    (nttDomainToRS D).n = D.n
```

`CompPoly.ReedSolomon.forwardImpl_eq_encode` (theorem, [line 71](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/ReedSolomon/NTTEncode.lean#L71))

> **The certified NTT encoder**: over the induced evaluation domain, the forward NTT of
> the message polynomial's coefficients is exactly the Reed-Solomon encoding — the
> `O(n log n)` evaluation path and the definitional encoder agree, with no padding needed.

```lean
theorem forwardImpl_eq_encode (D : CPolynomial.NTT.Domain F) {k : ℕ} (msg : Vector F k)
    (hk : k ≤ D.n) :
    Forward.forwardImpl D (messagePoly msg).val
      = (encode (nttDomainToRS D) msg).toArray
```

`CompPoly.ReedSolomon.nttCodeword` (definition, [line 87](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/ReedSolomon/NTTEncode.lean#L87))

> The forward-NTT output packaged as a length-indexed vector over the induced domain.

```lean
def nttCodeword (D : CPolynomial.NTT.Domain F) {k : ℕ} (msg : Vector F k) (hk : k ≤ D.n) :
    Vector F (nttDomainToRS D).n
```

`CompPoly.ReedSolomon.nttCodeword_eq_encode` (theorem, [line 93](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/ReedSolomon/NTTEncode.lean#L93))

> Vector-level form of `forwardImpl_eq_encode`.

```lean
theorem nttCodeword_eq_encode (D : CPolynomial.NTT.Domain F) {k : ℕ} (msg : Vector F k)
    (hk : k ≤ D.n) : nttCodeword D msg hk = encode (nttDomainToRS D) msg
```

## Depends on

- [Forward NTT](../../part-01/ntt/forward.md)
- [Reed-Solomon Codes](../../part-01/reedsolomon.md)

## Proof depends on

- [NTT and Evaluation](../../part-01/ntt/evaluation.md)

## Sources

- [CompPoly/Univariate/ReedSolomon/NTTEncode.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/ReedSolomon/NTTEncode.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.ReedSolomon.NTTEncode.json)
