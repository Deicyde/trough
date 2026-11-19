---
declaration: lemma
origin: cited
lean: MIPRE.sum_re_tracial, MIPRE.re_nonneg_tracial, MIPRE.re_eq_zero_of_tracialValue_eq_one, MIPRE.SyncStrategy.value_eq_tracialValue, MIPRE.SyncStrategy.re_eq_zero_of_value_eq_one
statement: formalized
proof: formalized
---

# A perfect strategy rejects nothing on the support

Let $\mathfrak{G}$ be a synchronous game, $\tau$ a tracial state and $M$ a family of projective measurements with ${\mathrm{val}^{\mathrm{co}}}(\mathfrak{G}, M) = 1$. Then $\tau(M^x_a M^y_b) = 0$ whenever $\mu(x,y) > 0$ and $D(x,y,a,b) = 0$. In particular a value-$1$ synchronous strategy has $\mathrm{Tr}(M^x_a M^y_b) = 0$ at every rejected answer pair of every question pair the verifier asks.

## Depends on

- [Synchronous value](def-sync-value.md)

## Proof

At a fixed question pair the outcome probabilities sum to one, $\sum_{a,b} \tau(M^x_a M^y_b) = \tau(1) = 1$, and each is nonnegative; this is why the value is at most one. The value is the same sum with the rejected terms deleted, so equality with $1$ forces each deleted term to vanish, and $\mu(x,y) > 0$ cancels.

## Lean

Formalized as [`MIPRE.sum_re_tracial`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_re_tracial), [`MIPRE.re_nonneg_tracial`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.re_nonneg_tracial), [`MIPRE.re_eq_zero_of_tracialValue_eq_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.re_eq_zero_of_tracialValue_eq_one), [`MIPRE.SyncStrategy.value_eq_tracialValue`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SyncStrategy.value_eq_tracialValue), [`MIPRE.SyncStrategy.re_eq_zero_of_value_eq_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SyncStrategy.re_eq_zero_of_value_eq_one).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 214](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L214)
