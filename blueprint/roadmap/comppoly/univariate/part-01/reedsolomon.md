---
catalog: module
lean: CompPoly.ReedSolomon.Domain, CompPoly.ReedSolomon.Domain.n, CompPoly.ReedSolomon.Domain.node_injective, CompPoly.ReedSolomon.messagePoly, CompPoly.ReedSolomon.messagePoly_degree_lt, CompPoly.ReedSolomon.messagePoly_ofFn_coeff, CompPoly.ReedSolomon.encode, CompPoly.ReedSolomon.encode_get
statement: formalized
proof: formalized
---

# Reed-Solomon Codes

`CompPoly.Univariate.ReedSolomon`, in [CompPoly/Univariate/ReedSolomon.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon.lean), by Juan Conejero.

> The Reed-Solomon code over a finite field: evaluation domain, message polynomial, and
> encoder. Decoders live in their own files.
>
> A Reed-Solomon code is fixed by an evaluation domain `(a₀, ..., aₙ₋₁) ∈ Fⁿ` of distinct
> points and a message length `k`. The codeword for a message `(m₀, ..., mₖ₋₁) ∈ Fᵏ` is
> `cᵢ = f(aᵢ)` with `f(x) = m₀ + m₁ x + ... + mₖ₋₁ xᵏ⁻¹`. For `1 ≤ k < n ≤ #F` this is an
> `(n, k, d)` code of minimum distance `d = n − k + 1`.
>
> ## Main definitions
>
> * `Domain`: evaluation domain, an array of distinct points of `F`.
> * `messagePoly`, `encode`: the message polynomial of a coefficient vector and the encoder
>   evaluating it on the domain.

`CompPoly.ReedSolomon.Domain` (definition, [line 38](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon.lean#L38))

> Evaluation domain: an array of distinct points in `F`.

```lean
def Domain (F : Type*)
```

`CompPoly.ReedSolomon.Domain.n` (abbreviation, [line 43](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon.lean#L43))

> Block length.

```lean
abbrev n (D : Domain F) : ℕ
```

`CompPoly.ReedSolomon.Domain.node_injective` (lemma, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon.lean#L46))

> Indexing into the (nodup) domain array is injective on `Fin D.n`.

```lean
lemma node_injective (D : Domain F) :
    Function.Injective (fun i : Fin D.n => D.val[i])
```

`CompPoly.ReedSolomon.messagePoly` (definition, [line 54](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon.lean#L54))

> Message polynomial `m₀ + m₁ x + ... + mₖ₋₁ xᵏ⁻¹` from a length-`k`
> coefficient vector `msg`.

```lean
def messagePoly [Zero F] [BEq F] [LawfulBEq F]
    {k : ℕ} (msg : Vector F k) : CPolynomial F
```

`CompPoly.ReedSolomon.messagePoly_degree_lt` (lemma, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon.lean#L60))

> `(messagePoly msg).degree < k`.

```lean
lemma messagePoly_degree_lt [Zero F] [BEq F] [LawfulBEq F] {k : ℕ} (msg : Vector F k) :
    (messagePoly msg).degree < k
```

`CompPoly.ReedSolomon.messagePoly_ofFn_coeff` (lemma, [line 67](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon.lean#L67))

> `messagePoly` recovers a `CPolynomial` of degree `< k` from its bounded coefficient vector.

```lean
lemma messagePoly_ofFn_coeff [Semiring F] [BEq F] [LawfulBEq F] (k : ℕ) (f : CPolynomial F)
    (hf : f.degree < k) : messagePoly (Vector.ofFn fun i : Fin k => f.coeff i) = f
```

`CompPoly.ReedSolomon.encode` (definition, [line 78](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon.lean#L78))

> Encode: the message polynomial `messagePoly msg` evaluated at the domain `D`.

```lean
def encode [Semiring F] [BEq F] [LawfulBEq F]
    (D : Domain F) {k : ℕ} (msg : Vector F k) : Vector F D.n
```

`CompPoly.ReedSolomon.encode_get` (lemma, [line 83](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon.lean#L83))

> The codeword entry at node `i` is `messagePoly msg` evaluated at `D.val[i]`.

```lean
lemma encode_get [Semiring F] [BEq F] [LawfulBEq F] (D : Domain F) {k : ℕ}
    (msg : Vector F k) (i : Fin D.n) :
    (encode D msg).get i = (messagePoly msg).eval (D.val[i])
```

## Depends on

- [Computable Univariate Polynomials](basic.md)

## Proof depends on

- [Proofs of Correctness for CPolynomial Operations, wrt Mathlib Specs](../part-02/topoly/impl.md)

## Sources

- [CompPoly/Univariate/ReedSolomon.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Univariate.ReedSolomon.json)
