---
declaration: module
origin: cited
lean: WickContraction.signFinset, WickContraction.sign, WickContraction.sign_empty, WickContraction.sign_congr
statement: formalized
proof: formalized
---

# Sign associated with a contraction

The module `Physlib.QFT.PerturbationTheory.WickContraction.Sign.Basic`, [Physlib/QFT/PerturbationTheory/WickContraction/Sign/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/Basic.lean): 4 declarations, 2 with a docstring.

**`WickContraction.signFinset`**, a def, [line 32](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/Basic.lean#L32).

> Given a Wick contraction `c : WickContraction n` and `i1 i2 : Fin n` the finite set
> of elements of `Fin n` between `i1` and `i2` which are either uncontracted
> or are contracted but are contracted with an element occurring after `i1`.
> In other words, the elements of `Fin n` between `i1` and `i2` which are not
> contracted with before `i1`.
> One should assume `i1 < i2` otherwise this finite set is empty.

```lean
def signFinset (c : WickContraction n) (i1 i2 : Fin n) : Finset (Fin n)
```

**`WickContraction.sign`**, a def, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/Basic.lean#L49).

> For a list `φs` of `𝓕.FieldOp`, and a Wick contraction `φsΛ` of `φs`,
>   the complex number `φsΛ.sign` is defined to be the sign (`1` or `-1`) corresponding
>   to the number of `fermionic`-`fermionic` exchanges that must be done to put
>   contracted pairs within `φsΛ` next to one another, starting recursively
>   from the contracted pair
>   whose first element occurs at the left-most position.
>
>   As an example, if `[φ1, φ2, φ3, φ4]` correspond to fermionic fields then the sign
>   associated with
> - `{{0, 1}}` is `1`
> - `{{0, 1}, {2, 3}}` is `1`
> - `{{0, 2}, {1, 3}}` is `-1`

```lean
def sign (φs : List 𝓕.FieldOp) (φsΛ : WickContraction φs.length) : ℂ
```

**`WickContraction.sign_empty`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/Basic.lean#L54).

```lean
lemma sign_empty (φs : List 𝓕.FieldOp) :
    sign φs empty = 1
```

**`WickContraction.sign_congr`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/Basic.lean#L59).

```lean
lemma sign_congr {φs φs' : List 𝓕.FieldOp} (h : φs = φs') (φsΛ : WickContraction φs.length) :
    sign φs' (congr (by simp [h]) φsΛ) = sign φs φsΛ
```

## Depends on

- [Exchange sign for field statistics](../part-01/fieldstatistics-exchangesign.md)
- [Field statistics of a finite set.](../part-01/fieldstatistics-offinset.md)
- [Wick contractions](../part-02/wickcontraction-basic.md)

## Sources

- [Physlib/QFT/PerturbationTheory/WickContraction/Sign/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/Basic.lean)
