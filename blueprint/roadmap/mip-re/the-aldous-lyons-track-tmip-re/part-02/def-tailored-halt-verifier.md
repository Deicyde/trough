---
declaration: definition
origin: cited
lean: MIPRE.Tailored.Halting.Vhalt, MIPRE.Tailored.Halting.lp, MIPRE.Tailored.Halting.lpProg, MIPRE.Tailored.Halting.F, MIPRE.Tailored.Halting.body, MIPRE.Tailored.Halting.prep, MIPRE.Tailored.Halting.comprLp, MIPRE.Tailored.Halting.acceptProg, MIPRE.Tailored.Halting.rejectProg, MIPRE.Tailored.Halting.W, MIPRE.Tailored.Halting.branch1, MIPRE.Tailored.Halting.branch2
statement: formalized
---

# The tailored halting verifier; II:1900–1925

Let a tailored gap compression be given, with compressed sampler $\mathcal{S}^\lambda$ and answer-length calculator $\mathcal{L}^\lambda$, a machine $\mathcal{M}$, a search program $\mathcal{S}'$ and a parameter $\lambda$. The *tailored halting verifier* $\mathsf{V}^{\mathcal{M},\lambda} = (\mathcal{S}^\lambda, \mathcal{L}^\lambda, \mathcal{P}^{\mathcal{M},\lambda})$ has for linear-constraints processor the efficient Kleene fixed point of the map that sends a processor $\mathcal{P}$ to the program which, on $(n, x, y, a^R, b^R)$:

1. outputs the empty list of constraints if $\mathcal{M}$ halts on the empty input within $\lceil \log_2 (n+1) \rceil$ steps;
2. otherwise outputs the list $\{J\}$ if $\mathcal{S}'$ halts on the description of $(\mathcal{S}^\lambda, \mathcal{L}^\lambda, \mathcal{P})$ within the same budget;
3. otherwise runs the compressed processor of $(\mathcal{S}^\lambda, \mathcal{L}^\lambda, \mathcal{P})$ on the input.

Items 1 and 3 are the paper's map $F$ (II:1900), the empty list accepting and $\{J\}$ rejecting every answer pair; item 2 is the search branch of the paper route of Theorem [Halting reduction](../../structure-of-the-proof/part-09/thm-halting.md), which supplies the base case that the value form of compression lacks.

## Depends on

- [Tailored gap compression, value form; II:1852](def-tailored-compression.md)
- [Efficient Kleene recursion theorem](../../computability/lem-kleene.md)

## Lean

Formalized as [`MIPRE.Tailored.Halting.Vhalt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.Vhalt), [`MIPRE.Tailored.Halting.lp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.lp), [`MIPRE.Tailored.Halting.lpProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.lpProg), [`MIPRE.Tailored.Halting.F`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.F), [`MIPRE.Tailored.Halting.body`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.body), [`MIPRE.Tailored.Halting.prep`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.prep), [`MIPRE.Tailored.Halting.comprLp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.comprLp), [`MIPRE.Tailored.Halting.acceptProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.acceptProg), [`MIPRE.Tailored.Halting.rejectProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.rejectProg), [`MIPRE.Tailored.Halting.W`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.W), [`MIPRE.Tailored.Halting.branch1`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.branch1), [`MIPRE.Tailored.Halting.branch2`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.branch2).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 575](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L575)
