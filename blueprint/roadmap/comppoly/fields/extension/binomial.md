---
catalog: module
lean: Polynomial.X_pow_sub_C_dvd_X_pow_mul_sub_C_pow, Polynomial.not_X_dvd_X_pow_sub_C, Polynomial.X_pow_sub_C_dvd_X_pow_sub_X, Polynomial.isCoprime_X_pow_sub_C_X_pow_sub_X, Polynomial.eq_one_of_X_pow_sub_C_dvd_X_pow_sub_X, Polynomial.ne_one_of_isCoprime_X_pow_sub_C_X_pow_sub_X, Polynomial.irreducible_X_pow_sub_C_iff, Polynomial.irreducible_X_pow_sub_C, Polynomial.irreducible_X_pow_four_sub_C_iff, Polynomial.irreducible_X_pow_four_sub_C_iff_of_card, Polynomial.irreducible_X_pow_four_sub_C, Polynomial.irreducible_X_pow_four_sub_C_of_card
statement: formalized
proof: formalized
---

# Irreducibility of binomials `X^d - W` over a finite field

`CompPoly.Fields.Extension.Binomial`, in [CompPoly/Fields/Extension/Binomial.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Binomial.lean), by Derek Sorensen.

> Applying Rabin's test (`CompPoly/Data/Polynomial/Rabin.lean`) to a *binomial* defining
> polynomial collapses both conditions into single exponentiations **in the base field**.
>
> The reason is that `X^d ≡ W`, so whenever `d ∣ N - 1`, writing `k = (N-1)/d`,
>
> `X^N - X = X * (X^(d*k) - 1)`  and  `X^(d*k) ≡ W^k  (mod X^d - W)`.
>
> Hence `X^d - W` divides `X^N - X` exactly when `W^k = 1`, and is coprime to it exactly when
> `W^k ≠ 1`: the residue is then `X * C (W^k - 1)`, a unit multiple of `X`, and `X` does not
> divide `X^d - W` because `W ≠ 0`.
>
> Instantiating at `N = q^d` and `N = q^(d/ℓ)` turns Rabin's test into
> `irreducible_X_pow_sub_C_iff`, whose conditions are two base-field exponentiations. Contrast
> the ~2100 lines of hand-generated `BitVec` step certificates in
> `CompPoly/Fields/Binary/BF128Ghash/XPowTwoPow{Mod,Gcd}Certificate.lean`, which is what the
> same test costs when the defining polynomial is not a binomial.
>
> ## Main statements
>
> * `Polynomial.X_pow_sub_C_dvd_X_pow_sub_X` / `Polynomial.isCoprime_X_pow_sub_C_X_pow_sub_X`:
>   the two collapsed Rabin conditions, and their converses.
> * `Polynomial.irreducible_X_pow_sub_C_iff`: the criterion for general `d`.
> * `Polynomial.irreducible_X_pow_four_sub_C`: the `d = 4` corollary, which discharges
>   `Nat.primeFactors` internally. This is the degree used by BabyBear, KoalaBear and Hachi
>   extension fields.
>
> Both take the field size as a numeral `q` together with `Fintype.card F = q`, as everything in
> the Rabin layer does; pass `rfl` if you have no numeral.
>
> ## References
>
> * [Rabin80] Michael O. Rabin, *Probabilistic Algorithms in Finite Fields*,
>   SIAM Journal on Computing 9(2), 1980.
> * [LN97] Rudolf Lidl and Harald Niederreiter, *Finite Fields*, 2nd ed., Theorem 3.75.

> ### Reducing powers of `X` modulo a binomial

`Polynomial.X_pow_sub_C_dvd_X_pow_mul_sub_C_pow` (theorem, [line 63](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Binomial.lean#L63))

> `X^d - C W` divides `X^(d * k) - C (W ^ k)`.
>
> This is the algebraic content of "substituting `X^d = W`": apply `a - b ∣ a^k - b^k` with
> `a = X^d` and `b = C W`.

```lean
theorem X_pow_sub_C_dvd_X_pow_mul_sub_C_pow (W : F) (d k : ℕ) :
    (X ^ d - C W) ∣ X ^ (d * k) - C (W ^ k)
```

`Polynomial.not_X_dvd_X_pow_sub_C` (theorem, [line 84](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Binomial.lean#L84))

> `X` does not divide `X^d - C W` when `W ≠ 0`: the constant coefficient is `-W`.

```lean
theorem not_X_dvd_X_pow_sub_C {W : F} {d : ℕ} (hd : 0 < d) (hW : W ≠ 0) :
    ¬ (X : F[X]) ∣ X ^ d - C W
```

> ### The two collapsed Rabin conditions

`Polynomial.X_pow_sub_C_dvd_X_pow_sub_X` (theorem, [line 96](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Binomial.lean#L96))

> **Rabin condition 1, collapsed.** If `d ∣ N - 1` and `W ^ ((N-1)/d) = 1`, then
> `X^d - C W` divides `X^N - X`.

```lean
theorem X_pow_sub_C_dvd_X_pow_sub_X {W : F} {d N : ℕ} (hd : 0 < d) (hN : 1 ≤ N)
    (hdvd : d ∣ N - 1) (hW : W ^ ((N - 1) / d) = 1) :
    (X ^ d - C W) ∣ X ^ N - X
```

`Polynomial.isCoprime_X_pow_sub_C_X_pow_sub_X` (theorem, [line 113](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Binomial.lean#L113))

> **Rabin condition 2, collapsed.** If `d ∣ N - 1`, `W ≠ 0` and `W ^ ((N-1)/d) ≠ 1`, then
> `X^d - C W` is coprime to `X^N - X`.
>
> Modulo `X^d - C W` the polynomial `X^N - X` reduces to `X * C (W^k - 1)`, a unit multiple of
> `X`, and `X` is coprime to `X^d - C W` by `not_X_dvd_X_pow_sub_C`.

```lean
theorem isCoprime_X_pow_sub_C_X_pow_sub_X {W : F} {d N : ℕ} (hd : 0 < d) (hW0 : W ≠ 0)
    (hN : 1 ≤ N) (hdvd : d ∣ N - 1) (hW : W ^ ((N - 1) / d) ≠ 1) :
    IsCoprime (X ^ d - C W) (X ^ N - X)
```

`Polynomial.eq_one_of_X_pow_sub_C_dvd_X_pow_sub_X` (theorem, [line 132](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Binomial.lean#L132))

> Converse of `X_pow_sub_C_dvd_X_pow_sub_X`: divisibility forces `W ^ ((N-1)/d) = 1`.

```lean
theorem eq_one_of_X_pow_sub_C_dvd_X_pow_sub_X {W : F} {d N : ℕ} (hd : 0 < d) (hW0 : W ≠ 0)
    (hN : 1 ≤ N) (hdvd : d ∣ N - 1) (h : (X ^ d - C W) ∣ X ^ N - X) :
    W ^ ((N - 1) / d) = 1
```

`Polynomial.ne_one_of_isCoprime_X_pow_sub_C_X_pow_sub_X` (theorem, [line 140](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Binomial.lean#L140))

> Converse of `isCoprime_X_pow_sub_C_X_pow_sub_X`: coprimality forces `W ^ ((N-1)/d) ≠ 1`.

```lean
theorem ne_one_of_isCoprime_X_pow_sub_C_X_pow_sub_X {W : F} {d N : ℕ} (hd : 0 < d) (hN : 1 ≤ N)
    (hdvd : d ∣ N - 1) (h : IsCoprime ((X : F[X]) ^ d - C W) (X ^ N - X)) :
    W ^ ((N - 1) / d) ≠ 1
```

> ### The irreducibility criterion
>
> Each statement takes the field size as a numeral `q` with `hcard : Fintype.card F = q`, matching
> `Polynomial.irreducible_of_rabin`; a concrete field supplies `ZMod.card _` and a caller with no
> numeral passes `rfl`. The section comment in `CompPoly/Data/Polynomial/Rabin.lean` says why.

`Polynomial.irreducible_X_pow_sub_C_iff` (theorem, [line 167](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Binomial.lean#L167))

> **Irreducibility criterion for binomials.**
>
> Over a finite field with `q` elements, `X^d - W` is irreducible if and only if
> `W^((q^d - 1)/d) = 1` and `W^((q^(d/ℓ) - 1)/d) ≠ 1` for every prime `ℓ ∣ d`.
>
> The divisibility side conditions `h_top` and `h_mid` hold in every case of interest — for
> `d = 4` and `q ≡ 1 mod 4`, for instance — and are decidable arithmetic facts about `q` and `d`.

```lean
theorem irreducible_X_pow_sub_C_iff {d q : ℕ} {W : F} (hcard : Fintype.card F = q)
    (hd : 0 < d) (hW0 : W ≠ 0)
    (h_top : d ∣ q ^ d - 1)
    (h_mid : ∀ ℓ ∈ d.primeFactors, d ∣ q ^ (d / ℓ) - 1) :
    Irreducible ((X : F[X]) ^ d - C W) ↔
      (W ^ ((q ^ d - 1) / d) = 1 ∧
        ∀ ℓ ∈ d.primeFactors, W ^ ((q ^ (d / ℓ) - 1) / d) ≠ 1)
```

`Polynomial.irreducible_X_pow_sub_C` (theorem, [line 188](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Binomial.lean#L188))

> The `mpr` direction of `irreducible_X_pow_sub_C_iff`, as a standalone lemma.

```lean
theorem irreducible_X_pow_sub_C {d q : ℕ} {W : F} (hcard : Fintype.card F = q)
    (hd : 0 < d) (hW0 : W ≠ 0)
    (h_top : d ∣ q ^ d - 1)
    (h_mid : ∀ ℓ ∈ d.primeFactors, d ∣ q ^ (d / ℓ) - 1)
    (rabin_top : W ^ ((q ^ d - 1) / d) = 1)
    (rabin_mid : ∀ ℓ ∈ d.primeFactors, W ^ ((q ^ (d / ℓ) - 1) / d) ≠ 1) :
    Irreducible ((X : F[X]) ^ d - C W)
```

`Polynomial.irreducible_X_pow_four_sub_C_iff` (theorem, [line 221](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Binomial.lean#L221))

> **Irreducibility criterion for quartic binomials.**
>
> `X^4 - W` is irreducible over a finite field with `q` elements exactly when
> `W^((q^4 - 1)/4) = 1` and `W^((q^2 - 1)/4) ≠ 1`.
>
> This is the shape used by the BabyBear, KoalaBear and Hachi degree-4 extensions. It differs
> from `irreducible_X_pow_sub_C_iff` only in discharging `Nat.primeFactors 4 = {2}` internally,
> so callers never touch `Nat.primeFactors`.
>
> Being an `iff`, a *failed* check proves reducibility rather than merely failing to prove
> irreducibility.
>
> Concrete fields are defined as `ZMod fieldSize` where `fieldSize` is an *expression* such as
> `2 ^ 31 - 2 ^ 24 + 1`, and the hypotheses are stated at the numeral `q`, which is what lets a
> caller discharge them with `norm_num` and `reduce_mod_char`. `reduce_mod_char` still needs to see
> the *type* as `ZMod <numeral>`, so the two exponentiation goals are usually preceded by a `show`;
> see `CompPoly/Fields/KoalaBear/Ext4.lean` for the idiom.

```lean
theorem irreducible_X_pow_four_sub_C_iff {q : ℕ} {W : F} (hcard : Fintype.card F = q)
    (hW0 : W ≠ 0) (h_top : 4 ∣ q ^ 4 - 1) (h_mid : 4 ∣ q ^ 2 - 1) :
    Irreducible ((X : F[X]) ^ 4 - C W) ↔
      (W ^ ((q ^ 4 - 1) / 4) = 1 ∧ W ^ ((q ^ 2 - 1) / 4) ≠ 1)
```

`Polynomial.irreducible_X_pow_four_sub_C_iff_of_card` (alias, [line 233](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Binomial.lean#L233))

```lean
alias irreducible_X_pow_four_sub_C_iff_of_card
```

`Polynomial.irreducible_X_pow_four_sub_C` (theorem, [line 236](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Binomial.lean#L236))

> The `mpr` direction of `irreducible_X_pow_four_sub_C_iff`, as a standalone lemma.

```lean
theorem irreducible_X_pow_four_sub_C {q : ℕ} {W : F} (hcard : Fintype.card F = q)
    (hW0 : W ≠ 0) (h_top : 4 ∣ q ^ 4 - 1) (h_mid : 4 ∣ q ^ 2 - 1)
    (rabin_top : W ^ ((q ^ 4 - 1) / 4) = 1)
    (rabin_mid : W ^ ((q ^ 2 - 1) / 4) ≠ 1) :
    Irreducible ((X : F[X]) ^ 4 - C W)
```

`Polynomial.irreducible_X_pow_four_sub_C_of_card` (alias, [line 244](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Binomial.lean#L244))

```lean
alias irreducible_X_pow_four_sub_C_of_card
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Proof depends on

- [Rabin's irreducibility test](../../data/polynomial/rabin.md)

## Sources

- [CompPoly/Fields/Extension/Binomial.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Binomial.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Extension.Binomial.json)
