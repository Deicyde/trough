---
navigation: transparent
---

# The Pauli constraints of the… to The checks as polynomials, and…

- [The Pauli constraints of the first hiding edge, as programs](lem-intro-pauli-progs.md)
- [The Pauli constraints, as a program](lem-intro-pauli-cons-prog.md)
- [The introspection answer-length calculator](lem-intro-len-program.md)
- [The constraint lists of the auxiliary checks, as programs](lem-intro-aux-progs.md)
- [The introspection linear-constraints processor](lem-intro-lp-program.md)
- [Reading the construction at $C\lambda$ as one at $\lambda$](lem-intro-rescale.md)
- [Tailored compression from its stages; II:5643, value form](thm-tailored-compression-from-stages.md)
- [$\mathrm{TMIP}^* = \mathrm{RE}$ from tailored answer reduction](cor-tmip-re-from-ar.md)
- [Tailored compression; II:5643, value form](thm-tailored-compression-target.md)

**Remark (The Aldous–Lyons conjecture).** Paper I (BCLV24) associates with a tailored game a subgroup test whose sofic value is $1$ when the game has a perfect ZPC strategy and at most $1 - (C\Lambda^4 2^{6\Lambda})^{-1}$ when the synchronous value of the game is at most $\frac12$, $\Lambda$ being the largest answer length (Theorem 7.3 there, a finitary argument), and shows that under the Aldous–Lyons conjecture the sofic value of a subgroup test is computable to any precision (Main Theorem I there, a weak-$*$ compactness argument). With Theorem [$\mathrm{TMIP}^* = \mathrm{RE}$; II:1505, Theorem 7.4 of (BCLV24)](../part-01/thm-tmip-re.md) the conjecture is false. This is Phase 6 of the plan, after the main theorem.

## Answer reduction: linear systems over $\mathbb{F}_2$

Phase 4 of the plan (`planning/aldous-lyons-track.md`, “Phase 4 slices”) proves Theorem [Answer reduction for tailored verifiers; II:6883](../part-03/thm-tailored-ar.md) with paper II's tailored PCP (II:7736–11074). Before the PCP, the output indicator turns the constraints of the input game at a pair of questions into a *decoupled triangulated system* (II:7751–8316), which the PCP checks against the linear answers. The paper purifies the input verifier first (II:7783); here the indicator purifies on the fly, so the input is not transformed.

- [Purified, triangulated and decoupled systems](def-ar-linear.md)
- [Purification; fact:completeness_and_soundness_purification](lem-ar-purification.md)
- [Triangulation and decoupling; rem:prop_triangulated_system](lem-ar-triangle-decouple.md)
- [The extension; cor:triang_and_decoupling_extend](lem-ar-extend.md)

## Answer reduction: succinct descriptions through three windows

The output indicator of paper II (Definition defn:decider-read, II:8381) reads, besides the input verifier and its parameters, three strings: the two readable answers and the encoding $O$ of the decoupled system of Lemma [The extension; cor:triang_and_decoupling_extend](lem-ar-extend.md). Its succinct description, the formula the PCP checks, must hold each of the three in a block of variables of its own: the isolated player of the PCP holds the second readable answer, and cannot hold a block containing $O$, which depends on both. Lemma [Succinct decoupled 5SAT](../../structure-of-the-proof/part-07/lem-decoupled-5sat.md) has two answer blocks; the description here has three *windows* on the tableau of Theorem [Explicit succinct Cook–Levin](../../background-results/part-04/thm-succinct-sat.md) (prop:explicit-padded-succinct-deciders, II:8676, whose proof the paper sketches, II:8757). The indicator reads $a = a^R O$ and $b = b^R$; it checks the lengths of its inputs, so the windows, which cover them exactly, describe it completely.

- [Decoupled 6SAT through three windows; prop:explicit-padded-succinct-deciders](lem-ar-window-describer.md)

## Answer reduction: the output indicator

The output indicator $L^*$ of paper II (Definition defn:decider-read, II:8381) checks that a string $O$ is the table of the decoupled triangulated purified system of the constraints at a pair of questions; the PCP checks the system through that table (fact:polynomial\_condition\_for\_satisfiability, II:8147). Here the input verifier is neither padded nor purified (II:8377): $L^*$ cuts the readable answers at the readable lengths and purifies on the fly (Lemma [Purification; fact:completeness_and_soundness_purification](lem-ar-purification.md)), so the paper's steps 3 and 4 have nothing to check, and the table size $N = 2^\ell$ and the copy size $D = 2^{\delta}$ come from a polynomial-time parameter program of the index.

- [The table and the output indicator](def-ar-indicator.md)
- [The table holds the decoupled system; fact:polynomial_condition_for_satisfiability](lem-ar-indicator-table.md)
- [Properties of the output indicator; claim:properties_of_L\*](lem-ar-indicator-properties.md)
- [The output indicator as a program; eq:time_bound_L\*](lem-ar-indicator-program.md)

## Answer reduction: the PCP and its soundness

The PCP of paper II (Definitions defn:blocks\_of\_vars\_circuit and defn:PCP\_of\_V\_n\_satisfied, II:8939–9013) certifies that the circuit of Lemma [Decoupled 6SAT through three windows; prop:explicit-padded-succinct-deciders](lem-ar-window-describer.md) describes a satisfiable formula and that the table $O$ of Definition [The table and the output indicator](def-ar-indicator.md) holds a satisfiable system. Its variables are the wires of the circuit: the three windows, each a parity wire followed by the bits of a cell (of the two readable answers, and of an index of $O$), the three witness indices, the six signs, and the gates. The index of $O$ is itself the paper's $S_0$: the bits of the cells of the two linear answers and of the three copies, and the six signs of the decoupled system. Two departures from the paper's text. The windows hold tape encodings ($0 \mapsto 00$, $1 \mapsto 01$), so the literal of a window at $(\pi, u)$ is $\pi \cdot g(u)$ for the polynomial $g$ of the raw table, and the paper's raw-table assignments are kept. And a literal is true when its variable equals its sign, so its factor is $g - \varepsilon$ where the paper writes $g + \varepsilon + 1$ with $\varepsilon$ the negated sign.

- [The PCP and its thirteen checks](def-ar-pcp.md)
- [The checks as polynomials, and Schwartz–Zippel](lem-ar-pcp-schwartz-zippel.md)
