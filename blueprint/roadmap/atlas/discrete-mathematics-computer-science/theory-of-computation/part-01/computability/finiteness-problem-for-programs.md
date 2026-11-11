---
declaration: section
origin: cited
lean: Cslib.Decidability.FiniteCode, Cslib.Decidability.untilHaltsFun_dom, Cslib.Decidability.manyOneReducible_halting_finite, Cslib.Decidability.not_tm2CoRecognizable_finite, Cslib.Decidability.haltsWithinFun, Cslib.Decidability.haltsWithinFun_dom, Cslib.Decidability.manyOneReducible_not_halting_finite, Cslib.Decidability.not_tm2Recognizable_finite
statement: formalized
proof: formalized
---

# Finiteness problem for programs

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/finiteness-problem-for-programs/index.html).

## Codes with finite domain

A code $c$ of a partial recursive function $\varphi_c$ on
$\mathbb{N}$ is finite when the domain of $\varphi_c$, the set of inputs on which $c$ halts, is
finite. The set of finite codes is denoted $\mathrm{FIN}$.

Formalized by `Cslib.Decidability.FiniteCode`, a definition declared in [CSLibExt/Computability/Decidability/Finiteness.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Finiteness.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/finiteness-problem-for-programs/index.html#finite-code).

## Domain of the until-halts function

For a code $c$ of a partial recursive function, let
$u_c$ be the partial function on $\mathbb{N}$ that on input $j$ is undefined if $c$ halts on input
$0$ within $j$ steps (the step-bounded evaluation of $c$ on input $0$ with bound $j$ returns a
value) and outputs $0$ otherwise. Then for every $k \in \mathbb{N}$, $u_c$ is defined at $k$ if
and only if $c$ does not halt on input $0$ within $k$ steps.

Formalized by `Cslib.Decidability.untilHaltsFun_dom`, a theorem declared in [CSLibExt/Computability/Decidability/Finiteness.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Finiteness.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/finiteness-problem-for-programs/index.html#until-halts-fun-dom).

## Halting reduces to finiteness

The set of codes of partial recursive functions that halt
on input $0$ is many-one reducible to the set of finite codes: there is a computable function $f$
from codes to codes such that, for every code $c$, $c$ halts on input $0$ if and only if the
partial function of $f(c)$ has finite domain.

Formalized by `Cslib.Decidability.manyOneReducible_halting_finite`, a theorem declared in [CSLibExt/Computability/Decidability/Finiteness.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Finiteness.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/finiteness-problem-for-programs/index.html#many-one-reducible-halting-finite).

## Finiteness is not co-recognizable

The set of codes of partial recursive functions with
finite domain is not co-recognizable by multi-stack Turing machines: no finite multi-stack machine
whose input alphabet is identified with $\{0, 1\}$ halts on the binary encoding of the number of
a code $c$ exactly when the partial function of $c$ has infinite domain.

Formalized by `Cslib.Decidability.not_tm2CoRecognizable_finite`, a theorem declared in [CSLibExt/Computability/Decidability/Finiteness.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Finiteness.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/finiteness-problem-for-programs/index.html#not-tm2-co-recognizable-finite).

## Halts-within function

For a code $c$ of a partial recursive function, $h_c$ is the
partial function on $\mathbb{N}$ that on input $k$ outputs $0$ if $c$ halts on input $0$ within
$k$ steps (the step-bounded evaluation of $c$ on input $0$ with bound $k$ returns a value) and
is undefined otherwise.

Formalized by `Cslib.Decidability.haltsWithinFun`, a definition declared in [CSLibExt/Computability/Decidability/Finiteness.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Finiteness.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/finiteness-problem-for-programs/index.html#halts-within-fun).

## Domain of the halts-within function

For a code $c$ of a partial recursive function, let
$h_c$ be the partial function on $\mathbb{N}$ that on input $j$ outputs $0$ if $c$ halts on input
$0$ within $j$ steps (the step-bounded evaluation of $c$ on input $0$ with bound $j$ returns a
value) and is undefined otherwise. Then for every $k \in \mathbb{N}$, $h_c$ is defined at $k$ if
and only if $c$ halts on input $0$ within $k$ steps.

Formalized by `Cslib.Decidability.haltsWithinFun_dom`, a theorem declared in [CSLibExt/Computability/Decidability/Finiteness.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Finiteness.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/finiteness-problem-for-programs/index.html#halts-within-fun-dom).

## Non-halting reduces to finiteness

The set of codes of partial recursive functions that do
not halt on input $0$ is many-one reducible to the set of finite codes: there is a computable
function $f$ from codes to codes such that, for every code $c$, $c$ does not halt on input $0$ if
and only if the partial function of $f(c)$ has finite domain.

Formalized by `Cslib.Decidability.manyOneReducible_not_halting_finite`, a theorem declared in [CSLibExt/Computability/Decidability/Finiteness.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Finiteness.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/finiteness-problem-for-programs/index.html#many-one-reducible-not-halting-finite).

## Finiteness is not recognizable

The set of codes of partial recursive functions with
finite domain is not recognizable by multi-stack Turing machines: no finite multi-stack machine
whose input alphabet is identified with $\{0, 1\}$ halts on the binary encoding of the number of
a code $c$ exactly when the partial function of $c$ has finite domain.

Formalized by `Cslib.Decidability.not_tm2Recognizable_finite`, a theorem declared in [CSLibExt/Computability/Decidability/Finiteness.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Finiteness.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/finiteness-problem-for-programs/index.html#not-tm2-recognizable-finite).

## Finiteness is undecidable

The set of codes of partial recursive functions with finite
domain is not decidable by multi-stack Turing machines: there is no total function
$f : \mathbb{N} \to \mathbb{N}$ computed by a finite multi-stack machine on binary encodings such
that, for every code $c$ with number $n_c$, $f(n_c) = 1$ if and only if the partial function of
$c$ has finite domain.

Formalized by `Cslib.Decidability.not_tm2Decidable_finite`, a theorem declared in [CSLibExt/Computability/Decidability/Finiteness.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Finiteness.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/finiteness-problem-for-programs/index.html#not-tm2-decidable-finite).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finiteness problem for programs](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/finiteness-problem-for-programs/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/computability/finiteness-problem-for-programs)
