---
declaration: theorem
origin: cited
lean: Fri.FoldTrace.exists_codeword_of_query_probability, Fri.FoldTrace.exists_unique_codeword_agree_of_query_probability, Fri.FoldTrace.interpolate_accepting_agrees, Fri.FoldTrace.not_accepts_of_disagreement
statement: formalized
proof: formalized
---

# fri-binding

For a safe trace with positive degree bound $d$ and $t>0$, suppose $\delta\leq\theta$ and $\delta\leq 1-d/|D|$. Acceptance probability at least $(1-\delta)^t$ implies that the initial word is within relative distance $\delta$ of its code. A unique codeword agrees with it on every accepting position. Interpolation on any $d$ accepting positions recovers this codeword, and a query at a disagreement position forces rejection.

## Depends on

- [fri-query-error](thm-fri-query-error.md)

## Proof

The rate condition and $d>0$ give $\delta<1$, so positive acceptance implies a valid final word. Positive $t$ gives accepting density at least $1-\delta$. Since $\delta\leq\theta$, agreement lifts to an initial codeword within distance $\delta$. Since $\delta\leq 1-d/|D|$, the accepting set has at least $d$ positions, giving uniqueness. Lagrange interpolation supplies algebraic recovery on any $d$ accepting positions. No extraction running-time bound is asserted.

## Lean

Formalized as [`Fri.FoldTrace.exists_codeword_of_query_probability`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Fri.FoldTrace.exists_codeword_of_query_probability), [`Fri.FoldTrace.exists_unique_codeword_agree_of_query_probability`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Fri.FoldTrace.exists_unique_codeword_agree_of_query_probability), [`Fri.FoldTrace.interpolate_accepting_agrees`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Fri.FoldTrace.interpolate_accepting_agrees), [`Fri.FoldTrace.not_accepts_of_disagreement`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Fri.FoldTrace.not_accepts_of_disagreement).

## Sources

- [ArkLib blueprint: proof_systems/fri.tex, line 77](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/fri.tex#L77)
