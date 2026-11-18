---
declaration: module
origin: cited
lean: PureU1.split_equal, PureU1.split_odd, PureU1.VectorLikeEven
statement: formalized
proof: formalized
---

# Vector like charges

The module `Physlib.QFT.QED.AnomalyCancellation.VectorLike`, [Physlib/QFT/QED/AnomalyCancellation/VectorLike.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/VectorLike.lean): 3 declarations, 2 with a docstring.

> For the `n`-even case we define the property of a charge assignment being vector like.

**`PureU1.split_equal`**, a lemma, [line 29](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/VectorLike.lean#L29).

> Given a natural number `n`, this lemma proves that `n + n` is equal to `2 * n`.

```lean
lemma split_equal (n : ℕ) : n + n = 2 * n
```

**`PureU1.split_odd`**, a lemma, [line 31](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/VectorLike.lean#L31).

```lean
lemma split_odd (n : ℕ) : n + 1 + n = 2 * n + 1
```

**`PureU1.VectorLikeEven`**, a def, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/VectorLike.lean#L35).

> A charge configuration for n even is vector like if when sorted the `i`th element
> is equal to the negative of the `n + i`th element.

```lean
def VectorLikeEven (S : (PureU1 (2 * n)).Charges) : Prop
```

## Depends on

- [Sort for Pure U(1) charges](anomalycancellation-sorts.md)

## Sources

- [Physlib/QFT/QED/AnomalyCancellation/VectorLike.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/VectorLike.lean)
