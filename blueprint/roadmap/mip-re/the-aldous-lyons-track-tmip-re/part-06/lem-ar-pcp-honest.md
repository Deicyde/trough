---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.honestA, MIPRE.Tailored.AnsRed.honestB, MIPRE.Tailored.AnsRed.honestW, MIPRE.Tailored.AnsRed.honestR, MIPRE.Tailored.AnsRed.honestL, MIPRE.Tailored.AnsRed.lstar_accepts_honest, MIPRE.Tailored.AnsRed.identities_honest, MIPRE.Tailored.AnsRed.honestL_xorBits
statement: formalized
proof: formalized
---

# The honest PCP of accepted answers; cor:functional_viewpoint_final, item 1

Let a circuit describe the output indicator $L^*$ of a tailored verifier $\mathsf{V}$ at $(n, x, y)$ through windows of index lengths $\ell + 1$, $\ell + 1$ and $|S_0| + 1$, the parameter program giving $(\ell, \delta)$ at $n$. To answers $a^R a^L$ and $b^R b^L$ at $(x, y)$ associate the readable tables of the readable answers padded with zeros to $2^\ell$ bits, of the table $O$ of the decoupled triangulated purified system, and of witnesses of the formula for their windows, which depend only on $a^R, b^R$; and the linear tables $\mathsf{Extend}(a^L, b^L)$, which are $\mathbb{F}_2$-linear in $a^L, b^L$. If the game $\mathsf{V}_n$ accepts the answers, the lengths fit $2^\ell$ and $2^\delta$, the programs of $\mathsf{V}$ halt at $x$ and $y$, and $L^*$ accepts the padded strings within the describer's time, then the honest PCP of these tables satisfies the thirteen checks identically.

## Depends on

- [Completeness of the PCP; prop:completeness_and_soundness_of_PCP_for_V_n](lem-ar-pcp-complete.md)
- [Properties of the output indicator; claim:properties_of_L\*](../part-05/lem-ar-indicator-properties.md)
- [Decoupled 6SAT through three windows; prop:explicit-padded-succinct-deciders](../part-05/lem-ar-window-describer.md)

## Proof depends on

- [The output indicator as a program; eq:time_bound_L\*](../part-05/lem-ar-indicator-program.md)

## Proof

By item 1 of Lemma [Properties of the output indicator; claim:properties_of_L\*](../part-05/lem-ar-indicator-properties.md) the output indicator accepts the padded readable answers followed by the table, so by Lemma [Decoupled 6SAT through three windows; prop:explicit-padded-succinct-deciders](../part-05/lem-ar-window-describer.md) their windows, read off the tables at the odd positions of the tape encodings, satisfy the formula with some witnesses. By item 3 of Lemma [Properties of the output indicator; claim:properties_of_L\*](../part-05/lem-ar-indicator-properties.md) the linear tables satisfy the system that the table holds. Lemma [Completeness of the PCP; prop:completeness_and_soundness_of_PCP_for_V_n](lem-ar-pcp-complete.md) concludes.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.honestA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.honestA), [`MIPRE.Tailored.AnsRed.honestB`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.honestB), [`MIPRE.Tailored.AnsRed.honestW`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.honestW), [`MIPRE.Tailored.AnsRed.honestR`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.honestR), [`MIPRE.Tailored.AnsRed.honestL`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.honestL), [`MIPRE.Tailored.AnsRed.lstar_accepts_honest`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.lstar_accepts_honest), [`MIPRE.Tailored.AnsRed.identities_honest`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.identities_honest), [`MIPRE.Tailored.AnsRed.honestL_xorBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.honestL_xorBits).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2784](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2784)
