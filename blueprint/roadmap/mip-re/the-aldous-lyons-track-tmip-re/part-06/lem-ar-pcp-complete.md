---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.indDeg_induce, MIPRE.Tailored.AnsRed.assignChecks_induce, MIPRE.Tailored.AnsRed.formulaCheck_induce, MIPRE.Tailored.AnsRed.systemCheck_induce, MIPRE.Tailored.AnsRed.identities_induce
statement: formalized
proof: formalized
---

# Completeness of the PCP; prop:completeness_and_soundness_of_PCP_for_V_n

Over a field of characteristic two, the honest PCP has degree $17$ and its assignment checks hold identically. For the circuit polynomial of a well-formed circuit with the PCP's inputs, its formula check holds identically when the window tables, $\pi \cdot t(u)$ at the index of parity $\pi$ and cell $u$, and the witness tables satisfy the formula that the circuit describes; its system check holds identically when the linear tables satisfy the system that the table $O$ holds.

## Depends on

- [The honest PCP; $\mathsf{Induce}_C$](def-ar-induce.md)
- [The table and the output indicator](../part-05/def-ar-indicator.md)
- [Decoupled 6SAT through three windows; prop:explicit-padded-succinct-deciders](../part-05/lem-ar-window-describer.md)

## Proof depends on

- [Circuit arithmetization with bounded input use](../../structure-of-the-proof/part-07/lem-pcp-circuit-arithmetization.md)

## Proof

An encoding is $0$ or $1$ on the cube and multilinear, so $g(1 - g)$ vanishes on the cube and has individual degree at most $2$. At a Boolean point where the circuit polynomial is one, the circuit accepts the clause whose indices and signs the point holds on its input wires (Lemma [Circuit arithmetization with bounded input use](../../structure-of-the-proof/part-07/lem-pcp-circuit-arithmetization.md)), a literal of that clause is true, and its factor vanishes there; so the formula polynomial vanishes on the cube. At an index where $O$ is one, the equation holds in $\mathbb{F}_2$, hence in $\mathbb{F}$. In each case Lemma [Linear certificates for vanishing on the cube](lem-ar-linear-certificates.md) gives the identity.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.indDeg_induce`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.indDeg_induce), [`MIPRE.Tailored.AnsRed.assignChecks_induce`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.assignChecks_induce), [`MIPRE.Tailored.AnsRed.formulaCheck_induce`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.formulaCheck_induce), [`MIPRE.Tailored.AnsRed.systemCheck_induce`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.systemCheck_induce), [`MIPRE.Tailored.AnsRed.identities_induce`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.identities_induce).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2738](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2738)
