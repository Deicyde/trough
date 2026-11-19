---
catalog: module
lean: AdditiveNTT.Coset.point_eq_sum_getBit, AdditiveNTT.Coset.vanishing_eq_eval_W, AdditiveNTT.Coset.normalized_eq_eval_normalizedW, AdditiveNTT.Coset.novel_eq_eval_Xⱼ, AdditiveNTT.Coset.novelEval_eq_eval_polynomialFromNovelCoeffs, AdditiveNTT.Coset.independent_of_linearIndependent, AdditiveNTT.Coset.evaluationPointω_eq_point, AdditiveNTT.Coset.additiveNTT_eq_ntt, AdditiveNTT.Coset.inetwork_additiveNTT
statement: formalized
proof: formalized
---

# The coset transform agrees with the existing additive NTT

`CompPoly.Fields.Binary.AdditiveNTT.CosetBridge`, in [CompPoly/Fields/Binary/AdditiveNTT/CosetBridge.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/CosetBridge.lean), by Thomas Coratger.

> The coset file indexes the basis by natural numbers and evaluates at points.
>
> The existing development works with polynomials over a finite field, and a basis indexed by `Fin r`.
>
> This file shows the two presentations compute the same thing.
>
> A natural-number basis `b` stands for `β` when it agrees with it below `r`.
>
> ## Main results
>
> - `vanishing_eq_eval_W`: the point-indexed W_i is the evaluation of the polynomial W_i.
> - `normalized_eq_eval_normalizedW`: the same for the normalised W^_i.
> - `novel_eq_eval_Xⱼ`: the same for the novel basis polynomial X_j.
> - `novelEval_eq_eval_polynomialFromNovelCoeffs`: the same for a polynomial in the novel basis.
> - `independent_of_linearIndependent`: a linearly independent basis is independent.
> - `additiveNTT_eq_ntt`: the existing transform is the coset transform with zero shift.
> - `inetwork_additiveNTT`: the inverse network undoes the existing transform.

> ## The polynomials

`AdditiveNTT.Coset.point_eq_sum_getBit` (theorem, [line 47](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/CosetBridge.lean#L47))

> Point k below 2^i is the sum the existing code forms from the bits of k.

```lean
theorem point_eq_sum_getBit (hb : ∀ i : Fin r, b i = β i) (i : Fin r) (k : Fin (2 ^ i.val)) :
    point b k = ∑ j : Fin i, if Nat.getBit j k == 1 then β ⟨j, by omega⟩ else 0
```

`AdditiveNTT.Coset.vanishing_eq_eval_W` (theorem, [line 56](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/CosetBridge.lean#L56))

> The point-indexed W_i is the evaluation of the polynomial W_i.

```lean
theorem vanishing_eq_eval_W [Fact (LinearIndependent 𝔽q β)] (hb : ∀ i : Fin r, b i = β i)
    (i : Fin r) (x : L) : vanishing b i x = (W 𝔽q β i).eval x
```

`AdditiveNTT.Coset.normalized_eq_eval_normalizedW` (theorem, [line 63](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/CosetBridge.lean#L63))

> The point-indexed W^_i is the evaluation of the polynomial W^_i.

```lean
theorem normalized_eq_eval_normalizedW [Fact (LinearIndependent 𝔽q β)]
    (hb : ∀ i : Fin r, b i = β i) (i : Fin r) (x : L) :
    normalized b i x = (normalizedW 𝔽q β i).eval x
```

`AdditiveNTT.Coset.novel_eq_eval_Xⱼ` (theorem, [line 70](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/CosetBridge.lean#L70))

> The point-indexed X_j is the evaluation of the novel basis polynomial X_j.

```lean
theorem novel_eq_eval_Xⱼ [Fact (LinearIndependent 𝔽q β)] [Fact (Nat.Prime (ringChar 𝔽q))]
    (hb : ∀ i : Fin r, b i = β i) {ℓ : ℕ} (h_ℓ : ℓ ≤ r) (j : Fin (2 ^ ℓ)) (x : L) :
    novel b ℓ j x = (Xⱼ 𝔽q β ℓ h_ℓ j).eval x
```

`AdditiveNTT.Coset.novelEval_eq_eval_polynomialFromNovelCoeffs` (theorem, [line 81](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/CosetBridge.lean#L81))

> A polynomial in the novel basis has the same value in both presentations.

```lean
theorem novelEval_eq_eval_polynomialFromNovelCoeffs [Fact (LinearIndependent 𝔽q β)]
    [Fact (Nat.Prime (ringChar 𝔽q))] (hb : ∀ i : Fin r, b i = β i) {ℓ : ℕ} (h_ℓ : ℓ ≤ r)
    (a : Fin (2 ^ ℓ) → L) (d : ℕ → L) (hd : ∀ k : Fin (2 ^ ℓ), d k = a k) (x : L) :
    novelEval b ℓ d x = (polynomialFromNovelCoeffs 𝔽q β ℓ h_ℓ a).eval x
```

`AdditiveNTT.Coset.independent_of_linearIndependent` (theorem, [line 90](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/CosetBridge.lean#L90))

> A linearly independent basis is independent in the sense of the coset file.

```lean
theorem independent_of_linearIndependent [Fact (LinearIndependent 𝔽q β)]
    (hb : ∀ i : Fin r, b i = β i) : Independent b r
```

> ## The transforms

`AdditiveNTT.Coset.evaluationPointω_eq_point` (theorem, [line 101](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/CosetBridge.lean#L101))

> With beta_0 = 1, the evaluation points of the existing transform are the points of S.

```lean
theorem evaluationPointω_eq_point [Fact (β 0 = 1)] {ℓ R_rate : ℕ} (hb : ∀ i : Fin r, b i = β i)
    (h : ℓ + R_rate < r) (j : Fin (2 ^ (ℓ + R_rate))) :
    evaluationPointω 𝔽q β h (i := ⟨0, by omega⟩) (h_i := Nat.zero_le ℓ) j = point b j
```

`AdditiveNTT.Coset.additiveNTT_eq_ntt` (theorem, [line 122](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/CosetBridge.lean#L122))

> The existing transform is the coset transform with zero shift.
>
> The coefficients `d` extend `a` past 2^l in any way.

```lean
theorem additiveNTT_eq_ntt (hb : ∀ i : Fin r, b i = β i) (h : ℓ + R_rate < r)
    (a : Fin (2 ^ ℓ) → L) (d : ℕ → L) (hd : ∀ k : Fin (2 ^ ℓ), d k = a k)
    (j : Fin (2 ^ (ℓ + R_rate))) :
    additiveNTT 𝔽q β h a j = ntt b ℓ 0 d j
```

`AdditiveNTT.Coset.inetwork_additiveNTT` (theorem, [line 133](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/CosetBridge.lean#L133))

> The inverse network undoes the existing transform.
>
> It reads the first 2^l outputs and returns the coefficients.

```lean
theorem inetwork_additiveNTT (hb : ∀ i : Fin r, b i = β i) (h : ℓ + R_rate < r)
    (a : Fin (2 ^ ℓ) → L) (d : ℕ → L) (hd : ∀ k : Fin (2 ^ ℓ), d k = a k) (y : ℕ → L)
    (hy : ∀ j : Fin (2 ^ (ℓ + R_rate)), y j = additiveNTT 𝔽q β h a j) {i : ℕ}
    (hi : i < 2 ^ ℓ) : inetwork (twiddle b 0) ℓ y i = d i
```

## Depends on

- [Additive NTT Algorithm](algorithm.md)
- [The additive NTT over a coset, and its inverse](coset.md)

## Proof depends on

- [Additive NTT Correctness](correctness.md)

## Sources

- [CompPoly/Fields/Binary/AdditiveNTT/CosetBridge.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/CosetBridge.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Fields.Binary.AdditiveNTT.CosetBridge.json)
