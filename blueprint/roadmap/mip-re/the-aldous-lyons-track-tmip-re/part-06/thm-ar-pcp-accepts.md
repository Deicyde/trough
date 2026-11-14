---
declaration: theorem
origin: cited
lean: MIPRE.Tailored.AnsRed.accepts_of_identities, MIPRE.Tailored.AnsRed.accepts_of_dense
statement: formalized
proof: formalized
---

# The game accepts the decoded answers; cor:functional_viewpoint_final, item 2

Let a circuit describe the output indicator $L^*$ of a tailored verifier $\mathsf{V}$ at $(n, x, y)$ through windows of index lengths $\ell + 1$, $\ell + 1$ and $|S_0| + 1$ (Lemma [Decoupled 6SAT through three windows; prop:explicit-padded-succinct-deciders](../part-05/lem-ar-window-describer.md)), the parameter program giving $(\ell, \delta)$ at $n$. If a PCP of degree $d$ over $\mathbb{F}_q$, of characteristic two, passes the thirteen checks on a set of points of density more than $m (5 + 6(d + 1))/q$, then the game $\mathsf{V}_n$ accepts at $(x, y)$ the answers whose readable parts are the tables of $g_A$ and $g_B$ and whose linear parts are those of $g_{La}$ and $g_{Lb}$, each cut at its length.

## Depends on

- [From the identities to the formula and the system; prop:completeness_and_soundness_of_PCP_for_V_n](lem-ar-pcp-sound.md)
- [The checks as polynomials, and Schwartz–Zippel](../part-05/lem-ar-pcp-schwartz-zippel.md)

## Proof depends on

- [Decoupled 6SAT through three windows; prop:explicit-padded-succinct-deciders](../part-05/lem-ar-window-describer.md)
- [Properties of the output indicator; claim:properties_of_L\*](../part-05/lem-ar-indicator-properties.md)
- [The output indicator as a program; eq:time_bound_L\*](../part-05/lem-ar-indicator-program.md)

## Proof

By Lemmas [The checks as polynomials, and Schwartz–Zippel](../part-05/lem-ar-pcp-schwartz-zippel.md) and [From the identities to the formula and the system; prop:completeness_and_soundness_of_PCP_for_V_n](lem-ar-pcp-sound.md) the tables of the windows satisfy the formula, so $L^*$ accepts strings $a, b$ whose tape encodings the windows hold. The odd positions of the windows read the strings: the readable answers are the tables of $g_A$ and $g_B$, and the string $O$ that $L^*$ compared is the table of $g_O$. The linear tables satisfy the system that table holds, and item 2 of Lemma [Properties of the output indicator; claim:properties_of_L\*](../part-05/lem-ar-indicator-properties.md) gives the acceptance.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.accepts_of_identities`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.accepts_of_identities), [`MIPRE.Tailored.AnsRed.accepts_of_dense`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.accepts_of_dense).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2669](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2669)
