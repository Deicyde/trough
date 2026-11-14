---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.isAssignment_of_assignCheck, MIPRE.Tailored.AnsRed.tableSat_of_identities, MIPRE.Tailored.AnsRed.formula6Sat_of_identities
statement: formalized
proof: formalized
---

# From the identities to the formula and the system; prop:completeness_and_soundness_of_PCP_for_V_n

Over a field of characteristic two, let a PCP satisfy the checks identically for the circuit polynomial of a well-formed circuit with the PCP's inputs. Then every assignment is $0$ or $1$ on the Boolean cube; the tables of $g_{La}$, $g_{Lb}$ and the $g_{L,k}$ satisfy the system that the table of $g_O$ holds; and the tables of the windows, $\pi \cdot g(u)$ at the index of parity $\pi$ and cell $u$ for $g = g_A, g_B, g_O$, with the tables of the $g_{W,k}$, satisfy the decoupled 6SAT formula that the circuit describes.

## Depends on

- [The PCP and its thirteen checks](../part-05/def-ar-pcp.md)
- [Circuit arithmetization with bounded input use](../../structure-of-the-proof/part-07/lem-pcp-circuit-arithmetization.md)
- [Decoupled 6SAT through three windows; prop:explicit-padded-succinct-deciders](../part-05/lem-ar-window-describer.md)

## Proof depends on

- [The table and the output indicator](../part-05/def-ar-indicator.md)

## Proof

On the cube the certificate sums vanish, so an assignment check says $g(1 - g) = 0$. At an index where $g_O$ is one, the system check says that the equation holds in $\mathbb{F}$, hence in $\mathbb{F}_2$, the binary digits of the index being those of its coordinates. For a clause that the circuit accepts, the circuit polynomial is one at the Boolean point holding the clause's input and the gates' values (Lemma [Circuit arithmetization with bounded input use](../../structure-of-the-proof/part-07/lem-pcp-circuit-arithmetization.md)), so a literal factor vanishes there, which says that the literal is true.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.isAssignment_of_assignCheck`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.isAssignment_of_assignCheck), [`MIPRE.Tailored.AnsRed.tableSat_of_identities`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.tableSat_of_identities), [`MIPRE.Tailored.AnsRed.formula6Sat_of_identities`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.formula6Sat_of_identities).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2643](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2643)
