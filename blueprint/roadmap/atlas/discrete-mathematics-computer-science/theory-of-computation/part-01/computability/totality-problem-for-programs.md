---
declaration: section
origin: cited
lean: Cslib.Decidability.TotalCode, Cslib.Decidability.manyOneReducible_halting_total, Cslib.Decidability.not_tm2CoRecognizable_total, Cslib.Decidability.untilHaltsFun, Cslib.Decidability.manyOneReducible_not_halting_total, Cslib.Decidability.not_tm2Recognizable_total, Cslib.Decidability.not_tm2Decidable_total
statement: formalized
proof: formalized
---

# Totality problem for programs

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/totality-problem-for-programs/index.html).

## Total codes

A code $c$ of a partial recursive function is total when it halts on every
input: writing $\varphi_c$ for the partial function on $\mathbb{N}$ that $c$ computes,
$\varphi_c(n)$ is defined for every $n \in \mathbb{N}$.

Formalized by `Cslib.Decidability.TotalCode`, a definition declared in [CSLibExt/Computability/Decidability/Totality.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Totality.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/totality-problem-for-programs/index.html#total-code).

## Halting on zero reduces to totality

Writing $\varphi_c$ for the partial function on
$\mathbb{N}$ computed by a code $c$ of a partial recursive function, the set of codes $c$ with
$\varphi_c(0)$ defined is many-one reducible to the set of total codes, the codes that halt on
every input: there is a computable function $f$ from codes to codes such that, for every code
$c$, $\varphi_c(0)$ is defined if and only if $f(c)$ is total.

Formalized by `Cslib.Decidability.manyOneReducible_halting_total`, a theorem declared in [CSLibExt/Computability/Decidability/Totality.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Totality.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/totality-problem-for-programs/index.html#many-one-reducible-halting-total).

## Totality is not co-recognizable

The set of total codes, the codes of partial recursive
functions that halt on every input, is not co-recognizable by multi-stack machines: no
multi-stack machine halts on the binary encoding of a code $c$ exactly when $c$ is not total.

Formalized by `Cslib.Decidability.not_tm2CoRecognizable_total`, a theorem declared in [CSLibExt/Computability/Decidability/Totality.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Totality.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/totality-problem-for-programs/index.html#not-tm2-co-recognizable-total).

## Diverging once a code halts on zero

For a code $c$ of a partial recursive function, this
is the partial function $\mathbb{N} \to \mathbb{N}$ that on input $k$ is undefined if $c$ halts
on input $0$ within $k$ steps of bounded evaluation, and equals $0$ otherwise.

Formalized by `Cslib.Decidability.untilHaltsFun`, a definition declared in [CSLibExt/Computability/Decidability/Totality.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Totality.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/totality-problem-for-programs/index.html#until-halts-fun).

## Non-halting on zero reduces to totality

Writing $\varphi_c$ for the partial function on
$\mathbb{N}$ computed by a code $c$ of a partial recursive function, the set of codes $c$ with
$\varphi_c(0)$ undefined is many-one reducible to the set of total codes, the codes that halt on
every input: there is a computable function $f$ from codes to codes such that, for every code
$c$, $\varphi_c(0)$ is undefined if and only if $f(c)$ is total.

Formalized by `Cslib.Decidability.manyOneReducible_not_halting_total`, a theorem declared in [CSLibExt/Computability/Decidability/Totality.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Totality.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/totality-problem-for-programs/index.html#many-one-reducible-not-halting-total).

## Totality is not recognizable

The set of total codes, the codes of partial recursive
functions that halt on every input, is not recognizable by multi-stack machines: no multi-stack
machine halts on the binary encoding of a code $c$ exactly when $c$ is total.

Formalized by `Cslib.Decidability.not_tm2Recognizable_total`, a theorem declared in [CSLibExt/Computability/Decidability/Totality.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Totality.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/totality-problem-for-programs/index.html#not-tm2-recognizable-total).

## Totality is undecidable

The set of total codes, the codes of partial recursive functions
that halt on every input, is not decidable by multi-stack machines: no multi-stack machine
computes a total function $f : \mathbb{N} \to \mathbb{N}$ that takes the value $1$ at the number
encoding a code $c$ exactly when $c$ is total.

Formalized by `Cslib.Decidability.not_tm2Decidable_total`, a theorem declared in [CSLibExt/Computability/Decidability/Totality.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Totality.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/totality-problem-for-programs/index.html#not-tm2-decidable-total).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Totality problem for programs](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/totality-problem-for-programs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/computability/totality-problem-for-programs)
