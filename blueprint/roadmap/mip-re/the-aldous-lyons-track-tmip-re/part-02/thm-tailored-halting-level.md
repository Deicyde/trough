---
declaration: theorem
origin: cited
lean: MIPRE.Tailored.Halting.halting_tailored, MIPRE.Tailored.Halting.halting_tailored_valStar, MIPRE.Tailored.Halting.hasPerfectZPC_of_halts, MIPRE.Tailored.Halting.valStar_le_of_not_halts, MIPRE.Tailored.Halting.A_step, MIPRE.Tailored.Halting.B_step
statement: formalized
proof: formalized
---

# The tailored halting theorem at a fixed level; II:2021–2066

Let a tailored gap compression be given and $\mathcal{S}'$ a program meeting the search specification. For every machine $\mathcal{M}$ and every $\lambda \geq \Lambda_0 + 4\left\vert {\mathcal{M}} \right\vert$, at the level $C$: if $\mathcal{M}$ halts on the empty input, $\mathsf{V}^{\mathcal{M},\lambda}$ has a perfect ZPC strategy; if it does not, $\mathrm{val}^*(\mathsf{V}^{\mathcal{M},\lambda}_C) \leq \frac12$.

## Depends on

- [The values of the tailored halting verifier; II:1978](lem-tailored-dhalt-values.md)
- [$\lambda$ for the tailored halting verifier; II:2002](lem-tailored-lambda.md)
- [The search program's specification](def-tailored-search-spec.md)
- [ZPC strategies are PCC strategies](../part-01/lem-zpc-pcc.md)

## Proof

Along the levels $C, 2^C, 2^{2^C}, \dots$, compression carries a perfect ZPC strategy at $2^n$ down to $n$, and a value at most $\frac12$, at every level where neither of the first two branches fires, the verifier then having the compressed verifier's games (Lemma [The values of the tailored halting verifier; II:1978](lem-tailored-dhalt-values.md)); the verifier is $\lambda$-bounded by Lemma [$\lambda$ for the tailored halting verifier; II:2002](lem-tailored-lambda.md). If $\mathcal{M}$ halts, the first branch fires from some level on; the search never fires below it, since a firing would put every level below it, the start level among them, at value at most $\frac12$, while the search fires only when the start level's value exceeds $\frac12$; so completeness descends to $C$. If $\mathcal{M}$ does not halt and the value at $C$ exceeded $\frac12$, the search would fire from some level on, and soundness would descend from there to $C$, a contradiction.

## Lean

Formalized as [`MIPRE.Tailored.Halting.halting_tailored`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.halting_tailored), [`MIPRE.Tailored.Halting.halting_tailored_valStar`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.halting_tailored_valStar), [`MIPRE.Tailored.Halting.hasPerfectZPC_of_halts`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.hasPerfectZPC_of_halts), [`MIPRE.Tailored.Halting.valStar_le_of_not_halts`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.valStar_le_of_not_halts), [`MIPRE.Tailored.Halting.A_step`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.A_step), [`MIPRE.Tailored.Halting.B_step`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.B_step).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 669](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L669)
