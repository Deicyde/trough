---
catalog: module
lean: CompPoly.ReedSolomon.Gao.bezout_solutions_cross_mul, CompPoly.ReedSolomon.Gao.disagreement_subset_error_locator_zeros, CompPoly.ReedSolomon.Gao.disagreement_card_le_error_locator_natDegree, CompPoly.ReedSolomon.Gao.hammingDist_le_error_locator_natDegree, CompPoly.ReedSolomon.Gao.receivedInterpolant_eval_node, CompPoly.ReedSolomon.Gao.receivedInterpolant_degree_lt, CompPoly.ReedSolomon.Gao.toPoly_nodalPoly, CompPoly.ReedSolomon.Gao.natDegree_nodalPoly, CompPoly.ReedSolomon.Gao.toPoly_nodalPoly_ne_zero, CompPoly.ReedSolomon.Gao.degree_nodalPoly, CompPoly.ReedSolomon.Gao.nodalPoly_eval_node_eq_zero, CompPoly.ReedSolomon.Gao.partialGcd_stopSpec, CompPoly.ReedSolomon.Gao.decode_sound, CompPoly.ReedSolomon.Gao.decode_eq_none, CompPoly.ReedSolomon.Gao.decode_eq_some, CompPoly.ReedSolomon.Gao.decode_none_farness, CompPoly.ReedSolomon.Gao.decode_eq_none_iff, CompPoly.ReedSolomon.Gao.decode_unique
statement: formalized
proof: formalized
---

# Gao Decoder Correctness

`CompPoly.Univariate.ReedSolomon.GaoCorrectness`, in [CompPoly/Univariate/ReedSolomon/GaoCorrectness.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoCorrectness.lean), by Juan Conejero.

> Correctness of the computable `Gao.decode` decoder from `GaoDecoder.lean`, formalizing
> [Gao02, Theorem 3.3]: `decode` succeeds exactly on received words within the decoding
> radius `⌊(n − k) / 2⌋` (soundness, failure, completeness, and uniqueness).
>
> ## Main results
>
> * `decode_sound`: every success of `Gao.decode` is the message polynomial of a codeword
>   within the decoding radius of the received word.
> * `decode_eq_none`: if no codeword lies within the decoding radius, `Gao.decode` fails.
> * `decode_eq_some`: within the decoding radius, `Gao.decode` recovers the sent message.
> * `decode_unique`: the decoded message polynomial is unique within the decoding radius.
>
> ## References
>
> * [Gao, S., *A New Algorithm for Decoding Reed-Solomon Codes*][Gao02]

> ## Uniqueness of degree-bounded Bézout solutions
>
> Two degree-bounded solutions of the Bézout identity cross-multiply
> (`bezout_solutions_cross_mul`), so the quotient `G / V` is unique.

`CompPoly.ReedSolomon.Gao.bezout_solutions_cross_mul` (theorem, [line 61](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoCorrectness.lean#L61))

> Two degree-bounded Bézout solutions `(U,V,G)`, `(U',V',G')` of `U g₀ + V g₁ = ·`
> (with `deg G, deg G' < d₀` and `deg V + d₀, deg V' + d₀ ≤ deg g₀`) cross-multiply:
> `V * G' = V' * G`.

```lean
theorem bezout_solutions_cross_mul [CommRing F] [NoZeroDivisors F]
    (g₀ g₁ G U V G' U' V' : F[X]) (d₀ : ℕ) (hg₀ : g₀ ≠ 0)
    (hBez : U * g₀ + V * g₁ = G) (hBez' : U' * g₀ + V' * g₁ = G')
    (hG : G.degree < d₀) (hG' : G'.degree < d₀)
    (hV : V.degree + d₀ ≤ g₀.degree) (hV' : V'.degree + d₀ ≤ g₀.degree) :
    V * G' = V' * G
```

> ## Error locators and Hamming distance
>
> A nonzero error locator vanishes on every disagreement node, so its degree bounds the
> Hamming distance between the received word and a candidate codeword.

`CompPoly.ReedSolomon.Gao.disagreement_subset_error_locator_zeros` (lemma, [line 80](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoCorrectness.lean#L80))

> If `V * (f₁ - g₁) = U * g₀` and `g₀` vanishes on aᵢ, then `V` vanishes at every
> aᵢ where `f₁` and `g₁` disagree.

```lean
lemma disagreement_subset_error_locator_zeros [CommRing F] [NoZeroDivisors F]
    {ι : Type*} [DecidableEq F] (s : Finset ι) (a : ι → F) (g₀ g₁ U V f₁ : F[X])
    (hroot : ∀ i ∈ s, g₀.eval (a i) = 0) (hlocator : V * (f₁ - g₁) = U * g₀) :
    {i ∈ s | f₁.eval (a i) ≠ g₁.eval (a i)} ⊆ {i ∈ s | V.eval (a i) = 0}
```

`CompPoly.ReedSolomon.Gao.disagreement_card_le_error_locator_natDegree` (lemma, [line 92](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoCorrectness.lean#L92))

> From the Bézout identity `G = U g₀ + V g₁` and `G = f₁ V` (with `V ≠ 0`,
> `g₀` rooted on the aᵢ), `f₁` disagrees with `g₁` at at most `V.natDegree` nodes.

```lean
lemma disagreement_card_le_error_locator_natDegree [CommRing F] [IsDomain F]
    {ι : Type*} [DecidableEq F] (s : Finset ι) (a : ι → F) (hinj : Set.InjOn a s)
    (g₀ g₁ G U V f₁ : F[X]) (hroot : ∀ i ∈ s, g₀.eval (a i) = 0)
    (hbez : G = U * g₀ + V * g₁) (hsucc : G = f₁ * V) (hV : V ≠ 0) :
    {i ∈ s | f₁.eval (a i) ≠ g₁.eval (a i)}.card ≤ V.natDegree
```

`CompPoly.ReedSolomon.Gao.hammingDist_le_error_locator_natDegree` (lemma, [line 104](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoCorrectness.lean#L104))

> From the Bézout identity `G = U g₀ + V g₁` and `G = f₁ V`
> (with `V ≠ 0`, `g₀` rooted on the aᵢ), a word `b` with `g₁(aᵢ) = b i` satisfies
> `hammingDist b (f₁ ∘ a) ≤ V.natDegree`.

```lean
lemma hammingDist_le_error_locator_natDegree [CommRing F] [IsDomain F]
    {ι : Type*} [Fintype ι] [DecidableEq F] (a : ι → F)
    (hinj : Function.Injective a)
    (g₀ g₁ G U V f₁ : F[X]) (b : ι → F)
    (hroot : ∀ i, g₀.eval (a i) = 0) (hb : ∀ i, g₁.eval (a i) = b i)
    (hbez : G = U * g₀ + V * g₁) (hsucc : G = f₁ * V) (hV : V ≠ 0) :
    hammingDist b (fun i => f₁.eval (a i)) ≤ V.natDegree
```

> ## Decoder components meet their specifications
>
> Transports the abstract `Polynomial` results to the implementation along the decoder
> pipeline:
> the received interpolant interpolates `r`, `nodalPoly = ∏ (X - aᵢ)` is monic of degree
> `D.n`, and `partialGcd` meets the Bézout stop spec.

`CompPoly.ReedSolomon.Gao.receivedInterpolant_eval_node` (lemma, [line 126](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoCorrectness.lean#L126))

> The received interpolant evaluates to `r i` at each domain node.

```lean
lemma receivedInterpolant_eval_node [Field F] (D : Domain F) (r : Vector F D.n) (i : Fin D.n) :
    (receivedInterpolant D r).toPoly.eval (D.val[i]) = r.get i
```

`CompPoly.ReedSolomon.Gao.receivedInterpolant_degree_lt` (lemma, [line 132](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoCorrectness.lean#L132))

> The received interpolant has degree `< D.n`.

```lean
lemma receivedInterpolant_degree_lt [Field F] (D : Domain F) (r : Vector F D.n) :
    (receivedInterpolant D r).toPoly.degree < D.n
```

`CompPoly.ReedSolomon.Gao.toPoly_nodalPoly` (lemma, [line 138](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoCorrectness.lean#L138))

> `(nodalPoly D).toPoly = ∏ i, (X - C D.val[i])`.

```lean
lemma toPoly_nodalPoly [CommRing F] [Nontrivial F] (D : Domain F) :
    (nodalPoly D).toPoly = ∏ i : Fin D.n, (X - C (D.val[i]))
```

`CompPoly.ReedSolomon.Gao.natDegree_nodalPoly` (lemma, [line 147](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoCorrectness.lean#L147))

> `(nodalPoly D).toPoly.natDegree = D.n`.

```lean
lemma natDegree_nodalPoly [CommRing F] [NoZeroDivisors F] [Nontrivial F] (D : Domain F) :
    (nodalPoly D).toPoly.natDegree = D.n
```

`CompPoly.ReedSolomon.Gao.toPoly_nodalPoly_ne_zero` (lemma, [line 154](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoCorrectness.lean#L154))

> `(nodalPoly D).toPoly ≠ 0` (it is monic, a product of distinct linear factors).

```lean
lemma toPoly_nodalPoly_ne_zero [CommRing F] [Nontrivial F] (D : Domain F) :
    (nodalPoly D).toPoly ≠ 0
```

`CompPoly.ReedSolomon.Gao.degree_nodalPoly` (lemma, [line 159](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoCorrectness.lean#L159))

> `(nodalPoly D).toPoly.degree = D.n`.

```lean
lemma degree_nodalPoly [CommRing F] [NoZeroDivisors F] [Nontrivial F] (D : Domain F) :
    (nodalPoly D).toPoly.degree = D.n
```

`CompPoly.ReedSolomon.Gao.nodalPoly_eval_node_eq_zero` (lemma, [line 164](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoCorrectness.lean#L164))

> `nodalPoly D` vanishes at every domain node.

```lean
lemma nodalPoly_eval_node_eq_zero [CommRing F] [Nontrivial F] (D : Domain F) (i : Fin D.n) :
    (nodalPoly D).toPoly.eval (D.val[i]) = 0
```

`CompPoly.ReedSolomon.Gao.partialGcd_stopSpec` (lemma, [line 173](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoCorrectness.lean#L173))

> `partialGcd`'s output satisfies the stop spec for `(nodalPoly D, receivedInterpolant D r)` at
> threshold `(D.n + k + 1) / 2`.

```lean
lemma partialGcd_stopSpec [Field F] (k : ℕ) (D : Domain F) (r : Vector F D.n) (hkn : k < D.n) :
    BezoutStopSpecOf (nodalPoly D) (receivedInterpolant D r) ((D.n + k + 1) / 2)
      (partialGcd k D r)
```

> ## Soundness
>
> A decoder success comes from a codeword within the decoding radius `⌊(D.n - k) / 2⌋` of the
> received word; `decode_eq_none` is the contrapositive.

`CompPoly.ReedSolomon.Gao.decode_sound` (theorem, [line 218](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoCorrectness.lean#L218))

> Soundness: any success of `Gao.decode` returns `messagePoly msg` for
> some `msg` whose codeword is within the decoding radius `⌊(D.n-k)/2⌋ = (d-1)/2` of `r`.

```lean
theorem decode_sound [Field F]
    (k : ℕ) (D : Domain F) (r : Vector F D.n) (hkn : k < D.n)
    (f₁ : CPolynomial F) (h : Gao.decode k D r = some f₁) :
    ∃ msg : Vector F k, messagePoly msg = f₁ ∧
      hammingDist r.get (encode D msg).get ≤ (D.n - k) / 2
```

`CompPoly.ReedSolomon.Gao.decode_eq_none` (theorem, [line 242](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoCorrectness.lean#L242))

> Failure: if `r` is beyond the decoding radius `⌊(D.n-k)/2⌋` of every message,
> `Gao.decode` returns `none` (contrapositive of soundness).

```lean
theorem decode_eq_none [Field F]
    (k : ℕ) (D : Domain F) (r : Vector F D.n) (hkn : k < D.n)
    (h : ∀ msg : Vector F k,
      (D.n - k) / 2 < hammingDist r.get (encode D msg).get) :
    Gao.decode k D r = none
```

> ## Completeness and uniqueness
>
> Within the guaranteed-decoding radius `⌊(D.n-k)/2⌋` the decoder returns exactly
> `messagePoly msg`, and that decoded word is unique (`decode_unique`).

`CompPoly.ReedSolomon.Gao.decode_eq_some` (theorem, [line 257](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoCorrectness.lean#L257))

> Completeness: if `r` is within the guaranteed-decoding radius `⌊(D.n-k)/2⌋`
> (`2 * (error count) ≤ D.n - k`) of `encode D msg`, then `Gao.decode` returns `messagePoly msg`.

```lean
theorem decode_eq_some [Field F]
    (k : ℕ) (D : Domain F) (r : Vector F D.n) (hkn : k < D.n)
    (msg : Vector F k)
    (herr : 2 * hammingDist r.get (encode D msg).get ≤ D.n - k) :
    Gao.decode k D r = some (messagePoly msg)
```

`CompPoly.ReedSolomon.Gao.decode_none_farness` (theorem, [line 310](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoCorrectness.lean#L310))

> **Decoder refusal is a farness certificate**: if the decoder returns `none`, the
> received word is beyond the guaranteed radius `⌊(n-k)/2⌋` of *every* codeword — positive,
> polynomial-time-checkable evidence of farness from the code (the contrapositive of
> `decode_eq_some`).

```lean
theorem decode_none_farness [Field F]
    (k : ℕ) (D : Domain F) (r : Vector F D.n) (hkn : k < D.n)
    (hnone : Gao.decode k D r = none) :
    ∀ msg : Vector F k, D.n - k < 2 * hammingDist r.get (encode D msg).get
```

`CompPoly.ReedSolomon.Gao.decode_eq_none_iff` (theorem, [line 322](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoCorrectness.lean#L322))

> Outcome characterization: `Gao.decode` returns `none` iff the received word is beyond
> the guaranteed radius `⌊(n-k)/2⌋` of every codeword (combines `decode_eq_none` and
> `decode_none_farness`).

```lean
theorem decode_eq_none_iff [Field F]
    (k : ℕ) (D : Domain F) (r : Vector F D.n) (hkn : k < D.n) :
    Gao.decode k D r = none ↔
      ∀ msg : Vector F k, D.n - k < 2 * hammingDist r.get (encode D msg).get
```

`CompPoly.ReedSolomon.Gao.decode_unique` (theorem, [line 331](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoCorrectness.lean#L331))

> Uniqueness: within the guaranteed-decoding radius `⌊(D.n-k)/2⌋`, two messages
> whose codewords lie within that radius of `r` decode to the same polynomial.

```lean
theorem decode_unique [Field F] (k : ℕ) (D : Domain F) (r : Vector F D.n)
    (hkn : k < D.n) (msg₁ msg₂ : Vector F k)
    (h₁ : 2 * hammingDist r.get (encode D msg₁).get ≤ D.n - k)
    (h₂ : 2 * hammingDist r.get (encode D msg₂).get ≤ D.n - k) :
    messagePoly msg₁ = messagePoly msg₂
```

## Depends on

- [Gao Decoder for Reed-Solomon Codes](gaodecoder.md)

## Proof depends on

- [Root sets of products of distinct linear factors](../../../tomathlib/polynomial/roots.md)

## Sources

- [CompPoly/Univariate/ReedSolomon/GaoCorrectness.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ReedSolomon/GaoCorrectness.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.ReedSolomon.GaoCorrectness.json)
