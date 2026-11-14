---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.lstarFinal_apply, MIPRE.Tailored.AnsRed.lstarProg_accepts, MIPRE.Tailored.AnsRed.lstar_accepts_iff, MIPRE.Tailored.AnsRed.lstarProg_halts, MIPRE.Tailored.AnsRed.lstar_acceptsWithin
statement: formalized
proof: formalized
---

# The output indicator as a program; eq:time_bound_L\*

The check is a polynomial-time function of its input, and decides the check of Definition [The table and the output indicator](def-ar-indicator.md). The output indicator accepts $(n, x, y, a, b)$ exactly when the answer-length calculator gives the four lengths, the processor gives the constraints on the cut readable answers, and the check passes. If the two programs halt within $T (|d| + 1)^k$ on every input $(n, d)$, the output indicator halts on $(n, x, y, a, b)$ within an explicit bound, polynomial in $T$, in the size of the input and in the time bound of the check, and so accepts what it accepts within that bound.

## Depends on

- [The table and the output indicator](def-ar-indicator.md)

## Proof depends on

- [The table holds the decoupled system; fact:polynomial_condition_for_satisfiability](lem-ar-indicator-table.md)
- [The running time of the canonical decider](../part-04/lem-canonical-decider-cost.md)

## Proof

The check writes the readable rows, their triangulation and the table with all indices in unary, and loops over the coordinates of the table. The two powers of two are computed capped: $2^\ell$ at one more than the length of $b$, which it must equal, and $2^{\delta}$ at one more than the length of $O$, which a satisfied length check exceeds, so nothing larger than the input is ever written. The program is that of the canonical decider with the check in place of the constraints' evaluation, and its running time is the sum of the five calls and of the check on a state whose size is bounded by the calls' outputs.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.lstarFinal_apply`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.lstarFinal_apply), [`MIPRE.Tailored.AnsRed.lstarProg_accepts`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.lstarProg_accepts), [`MIPRE.Tailored.AnsRed.lstar_accepts_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.lstar_accepts_iff), [`MIPRE.Tailored.AnsRed.lstarProg_halts`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.lstarProg_halts), [`MIPRE.Tailored.AnsRed.lstar_acceptsWithin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.lstar_acceptsWithin).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2542](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2542)
