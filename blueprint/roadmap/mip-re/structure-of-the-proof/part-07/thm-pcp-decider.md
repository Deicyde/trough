---
declaration: theorem
origin: cited
lean: MIPRE.SAT.BinField, MIPRE.SAT.PcpParams, MIPRE.SAT.PcpDecider, MIPRE.TM.CookLevin.Pad.classicalPcpDecider
statement: formalized
proof: formalized
---

# The bespoke PCP for deciders

There is a verifier ${{\mathsf{M}}^{\mathsf{ar}}}$ which, given a valid decider specification $(\mathcal{D}, n, T, Q, \sigma, x, y)$ — validity requiring $\left\vert {\mathcal{D}} \right\vert \leq \sigma$, $\max\{Q, 2\lceil \log n \rceil\} \leq T$ *and* $\left\vert {x} \right\vert, \left\vert {y} \right\vert \leq Q$, as exact inequalities — together with a PCP view $(z, \Xi)$, rejects any invalid specification or misformatted view, runs in time $\mathrm{poly}(\log T, \log n, Q, \sigma)$ and satisfies:

1. (**Completeness**) if $\left\vert {a} \right\vert,\left\vert {b} \right\vert\leq T$ and $\mathcal{D}$ accepts $(n, x, y, a, b)$ within $T$ steps, then the low-degree proof with $g_1, g_2$ the low-degree encodings (Definition [The low-degree code](def-ld-encoding.md)) of the padded answers is accepted with probability $1$ over uniform $z$;
2. (**Soundness**) any low-degree proof accepted with probability greater than $\frac12$ has ${\mathrm{Coded}}(g_1), {\mathrm{Coded}}(g_2)$ equal to the padded encodings of two strings whose prefixes, of length at most $T$, $\mathcal{D}$ accepts within $T$ steps.

Here the parameters are $(q, m, d, m', s) = {\mathrm{pcpparams}}(n, T, Q, \sigma)$ with $q = 2^k$ for an odd $k$, $d = 7$, $m' = 5m + 5 + s$ and $2T \leq 2^m$, computable in time polynomial in the bit lengths of $(n, T, Q, \sigma)$; and *both* variable counts $m$ and $m'$ of the arithmetization must be powers of two dividing $q$ (Remark [Why $m$ is a power of two](../README.md)).

## Depends on

- [Succinct decoupled 5SAT](lem-decoupled-5sat.md)
- [Schwartz–Zippel](../../background-results/part-05/lem-schwartz-zippel.md)
- [Decider](../../foundations/part-03/def-decider.md)
- [The low-degree code](def-ld-encoding.md)
- [Circuit arithmetization with bounded input use](lem-pcp-circuit-arithmetization.md)
- [Effective circuit polynomial evaluation](lem-pcp-circuit-evaluator.md)
- [Boolean-cube zero certificates](lem-pcp-zero-basis.md)
- [The algebraic PCP tests](lem-pcp-algebra-tests.md)
- [PCP answer blocks, honest proof and decoded clauses](lem-pcp-proof-algebra.md)
- [Effective padded descriptions with an explicit output budget](prop-pcp-padded-describer.md)
- [Effective classical PCP parameters](lem-pcp-effective-parameters.md)
- [PCP semantics for a circuit describer](lem-pcp-circuit-semantics.md)
- [Encoded PCP view size and source runtime](lem-pcp-view-size.md)
- [The executable PCP tests](lem-pcp-executable-tests.md)
- [Effective polynomial-basis field arithmetic](../../background-results/part-05/lem-effective-binary-field-arithmetic.md)

## Proof

The verifier checks the arithmetized formula and a certificate that its constraint polynomial vanishes on the Boolean cube. Soundness against the low-degree proofs in the statement follows from Lemma [Schwartz–Zippel](../../background-results/part-05/lem-schwartz-zippel.md). The PCP theorem itself does not run a quantum low-degree test or consume Pauli-test soundness; those belong to its later composition with a nonlocal game. Four obligations are separate in the source and stay separate here: the proof format and query structure, completeness, the zero-testing argument with its error bounds, and the complexity bound the composition consumes.

## Lean

Formalized as [`MIPRE.SAT.BinField`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.BinField), [`MIPRE.SAT.PcpParams`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.PcpParams), [`MIPRE.SAT.PcpDecider`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.PcpDecider), [`MIPRE.TM.CookLevin.Pad.classicalPcpDecider`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.classicalPcpDecider).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 5103](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L5103)
