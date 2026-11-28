---
catalog: module
lean: Polynomial.prod_X_sub_C_dvd, Polynomial.card_eval_zero_le_natDegree, Polynomial.prod_X_sub_C_dvd_prod_mul_sub
statement: formalized
proof: formalized
---

# Root sets of products of distinct linear factors

`CompPoly.ToMathlib.Polynomial.Roots`, in [CompPoly/ToMathlib/Polynomial/Roots.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/ToMathlib/Polynomial/Roots.lean), by Juan Conejero.

> - `∏ i ∈ s, (X - C (a i))` over injectively indexed points: it divides every polynomial
> vanishing on the points (`prod_X_sub_C_dvd`)
> - A nonzero polynomial vanishes at boundedly many of the points (`card_eval_zero_le_natDegree`)
> - The product divides `(∏ i ∈ E, (X - C (a i))) * (f - b)` whenever `f` and `b` agree off `E`
> (`prod_X_sub_C_dvd_prod_mul_sub`).

`Polynomial.prod_X_sub_C_dvd` (lemma, [line 27](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/ToMathlib/Polynomial/Roots.lean#L27))

> `∏ i ∈ s, (X - aᵢ)` divides `p` when the distinct `aᵢ` are all roots of `p`.

```lean
lemma prod_X_sub_C_dvd [Field R]
    {ι : Type*} (s : Finset ι) (a : ι → R) (hinj : Set.InjOn a s)
    (p : R[X]) (hr : ∀ i ∈ s, p.eval (a i) = 0) :
    (∏ i ∈ s, (X - C (a i))) ∣ p
```

`Polynomial.card_eval_zero_le_natDegree` (lemma, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/ToMathlib/Polynomial/Roots.lean#L37))

> A nonzero `v` vanishes at at most `v.natDegree` of the distinct points.

```lean
lemma card_eval_zero_le_natDegree [CommRing R] [IsDomain R]
    {ι : Type*} [DecidableEq R] (s : Finset ι) (a : ι → R)
    (hinj : Set.InjOn a s) (v : R[X]) (hv : v ≠ 0) :
    {i ∈ s | v.eval (a i) = 0}.card ≤ v.natDegree
```

`Polynomial.prod_X_sub_C_dvd_prod_mul_sub` (lemma, [line 48](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/ToMathlib/Polynomial/Roots.lean#L48))

> When `f, b` agree off `E ⊆ s`, the product `∏_{i∈s}(X−aᵢ)` divides
> `(∏_{i∈E}(X−aᵢ))·(f − b)`.

```lean
lemma prod_X_sub_C_dvd_prod_mul_sub [Field R] {ι : Type*} [DecidableEq ι]
    (s E : Finset ι) (hE : E ⊆ s) (a : ι → R) (hinj : Set.InjOn a s)
    (f b : R[X]) (hagree : ∀ i ∈ s \ E, f.eval (a i) = b.eval (a i)) :
    (∏ i ∈ s, (X - C (a i))) ∣ (∏ i ∈ E, (X - C (a i))) * (f - b)
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/ToMathlib/Polynomial/Roots.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/ToMathlib/Polynomial/Roots.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.ToMathlib.Polynomial.Roots.json)
