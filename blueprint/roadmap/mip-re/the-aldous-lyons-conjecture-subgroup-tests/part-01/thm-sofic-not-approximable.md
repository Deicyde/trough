---
declaration: theorem
origin: cited
lean: MIPRE.Tailored.Sofic.MainTheoremII, MIPRE.Tailored.Sofic.le_iff_of_gap, MIPRE.Tailored.Sofic.not_sofValueApproximable_of
statement: formalized
proof: formalized
---

# The sofic value is not approximable; Corollary I:2144, measure-free

Given a computable halting reduction to tailored games, and the two clauses of Main Theorem II with a primitive recursive gap function $K(\Lambda)$, the sofic value is not approximable.

## Depends on

- [Approximating the sofic value](def-sofic-approximable.md)
- [The associated test is computable from the game](lem-assoc-test-primrec.md)
- [The tailored halting reduction, as a proposition](../../the-aldous-lyons-track-tmip-re/part-01/def-tailored-halting-reduction.md)
- [Turing](../../background-results/part-03/thm-halting-undecidable.md)
- [A tailored game description as a game description](../../the-aldous-lyons-track-tmip-re/part-02/lem-tailored-conversion.md)

## Proof

Approximate the sofic value of the associated test of the game of a machine at $k = 4K(\Lambda)$. A halting machine gives sofic value $1$, so the approximation is at least $k/(k+1)$; a non-halting one gives sofic value at most $1 - 1/(2K)$, and the approximation is less than $k/(k+1)$. The comparison is computable, and decides the halting problem.

## Lean

Formalized as [`MIPRE.Tailored.Sofic.MainTheoremII`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.MainTheoremII), [`MIPRE.Tailored.Sofic.le_iff_of_gap`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.le_iff_of_gap), [`MIPRE.Tailored.Sofic.not_sofValueApproximable_of`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.not_sofValueApproximable_of).

## Sources

- [MIP* = RE blueprint: content/10_subgroup_tests.tex, line 380](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/10_subgroup_tests.tex#L380)
