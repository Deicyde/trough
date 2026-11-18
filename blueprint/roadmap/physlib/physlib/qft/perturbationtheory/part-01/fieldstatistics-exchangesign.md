---
declaration: module
origin: cited
lean: FieldStatistic.exchangeSign, FieldStatistic.exchangeSign_symm, FieldStatistic.exchangeSign_bosonic, FieldStatistic.bosonic_exchangeSign, FieldStatistic.fermionic_exchangeSign_fermionic, FieldStatistic.exchangeSign_eq_if, FieldStatistic.exchangeSign_mul_self, FieldStatistic.exchangeSign_mul_self_swap
statement: formalized
proof: formalized
---

# Exchange sign for field statistics

The module `Physlib.QFT.PerturbationTheory.FieldStatistics.ExchangeSign`, [Physlib/QFT/PerturbationTheory/FieldStatistics/ExchangeSign.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/ExchangeSign.lean): 10 declarations, 3 with a docstring.

> Suppose we have two fields `φ` and `ψ`, and the term `φψ`, if we swap them
> `ψφ`, we may pick up a sign. This sign is called the exchange sign.
> This sign is `-1` if both fields `ψ` and `φ` are fermionic and `1` otherwise.
>
> In this module we define the exchange sign for general field statistics,
> and prove some properties of it. Importantly:
> - It is symmetric `exchangeSign_symm`.
> - When multiplied with itself it is `1` `exchangeSign_mul_self`.
> - It is a cocycle `exchangeSign_cocycle`.

**`FieldStatistic.exchangeSign`**, a def, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/ExchangeSign.lean#L41).

> The exchange sign, `exchangeSign`, is defined as the group homomorphism
>
> `FieldStatistic →* FieldStatistic →* ℂ`,
>
> for which `exchangeSign a b` is `-1` if both `a` and `b` are `fermionic` and `1` otherwise.
> The exchange sign is the sign one picks up on exchanging an operator or field `φ₁` of statistic
> `a` with an operator or field `φ₂` of statistic `b`, i.e. `φ₁φ₂ → φ₂φ₁`.
>
> The notation `𝓢(a, b)` is used for the exchange sign of `a` and `b`.

```lean
def exchangeSign : FieldStatistic →* FieldStatistic →* ℂ
```

**`FieldStatistic.exchangeSign_symm`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/ExchangeSign.lean#L72).

> The exchange sign is symmetric.

```lean
lemma exchangeSign_symm (a b : FieldStatistic) : 𝓢(a, b) = 𝓢(b, a)
```

**`FieldStatistic.exchangeSign_bosonic`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/ExchangeSign.lean#L76).

```lean
lemma exchangeSign_bosonic (a : FieldStatistic) : 𝓢(a, bosonic) = 1
```

**`FieldStatistic.bosonic_exchangeSign`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/ExchangeSign.lean#L80).

```lean
lemma bosonic_exchangeSign (a : FieldStatistic) : 𝓢(bosonic, a) = 1
```

**`FieldStatistic.fermionic_exchangeSign_fermionic`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/ExchangeSign.lean#L84).

```lean
lemma fermionic_exchangeSign_fermionic : 𝓢(fermionic, fermionic) = - 1
```

**`FieldStatistic.exchangeSign_eq_if`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/ExchangeSign.lean#L87).

```lean
lemma exchangeSign_eq_if (a b : FieldStatistic) :
    𝓢(a, b) = if a = fermionic ∧ b = fermionic then - 1 else 1
```

**`FieldStatistic.exchangeSign_mul_self`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/ExchangeSign.lean#L92).

```lean
lemma exchangeSign_mul_self (a b : FieldStatistic) : 𝓢(a, b) * 𝓢(a, b) = 1
```

**`FieldStatistic.exchangeSign_mul_self_swap`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/ExchangeSign.lean#L96).

```lean
lemma exchangeSign_mul_self_swap (a b : FieldStatistic) : 𝓢(a, b) * 𝓢(b, a) = 1
```

**`FieldStatistic.exchangeSign_ofList_cons`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/ExchangeSign.lean#L99).

```lean
lemma exchangeSign_ofList_cons (a : FieldStatistic)
    (s : 𝓕 → FieldStatistic) (φ : 𝓕) (φs : List 𝓕) :
    𝓢(a, ofList s (φ :: φs)) = 𝓢(a, s φ) * 𝓢(a, ofList s φs)
```

**`FieldStatistic.exchangeSign_cocycle`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/ExchangeSign.lean#L105).

> The exchange sign is a cocycle.

```lean
lemma exchangeSign_cocycle (a b c : FieldStatistic) :
    𝓢(a, b * c) * 𝓢(b, c) = 𝓢(a, b) * 𝓢(a * b, c)
```

## Depends on

- [Field statistics](fieldstatistics-basic.md)

## Sources

- [Physlib/QFT/PerturbationTheory/FieldStatistics/ExchangeSign.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldStatistics/ExchangeSign.lean)
