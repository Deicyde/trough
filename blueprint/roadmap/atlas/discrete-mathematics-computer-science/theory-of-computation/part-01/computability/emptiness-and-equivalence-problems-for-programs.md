---
declaration: section
origin: cited
lean: Cslib.Decidability.EmptyCode, Cslib.Decidability.not_tm2Decidable_empty, Cslib.Decidability.tm2Recognizable_not_empty, Cslib.Decidability.tm2CoRecognizable_empty, Cslib.Decidability.not_tm2Recognizable_empty, Cslib.Decidability.EqCode, Cslib.Decidability.exists_code_empty, Cslib.Decidability.manyOneReducible_empty_eq
statement: formalized
proof: formalized
---

# Emptiness and equivalence problems for programs

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/emptiness-and-equivalence-problems-for-programs/index.html).

## Codes with empty domain

The set $E$ consists of the codes $c$ of partial recursive
functions on $\mathbb{N}$ that are defined on no input: for every $n \in \mathbb{N}$, the
function computed by $c$ is undefined at $n$.

Formalized by `Cslib.Decidability.EmptyCode`, a definition declared in [CSLibExt/Computability/Decidability/RiceApplications.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RiceApplications.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/emptiness-and-equivalence-problems-for-programs/index.html#empty-code).

## Emptiness is undecidable

The set $E$ of codes of partial recursive functions on
$\mathbb{N}$ that are defined on no input is not decidable by multi-stack machines.

By Rice's theorem: the identity function is defined, the empty function is not.

Formalized by `Cslib.Decidability.not_tm2Decidable_empty`, a theorem declared in [CSLibExt/Computability/Decidability/RiceApplications.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RiceApplications.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/emptiness-and-equivalence-problems-for-programs/index.html#not-tm2-decidable-empty).

## Nonemptiness is recognizable

The set of codes of partial recursive functions
$\mathbb{N} \to \mathbb{N}$ that are defined on at least one input is recognizable by
multi-stack machines: some multi-stack machine halts on the binary encoding of a code $c$ exactly
when the function coded by $c$ is defined on some input.

The machine searches for an input $n$ and a step bound $k$ such that the evaluation of $c$ on $n$
halts within $k$ steps.

Formalized by `Cslib.Decidability.tm2Recognizable_not_empty`, a theorem declared in [CSLibExt/Computability/Decidability/RiceApplications.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RiceApplications.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/emptiness-and-equivalence-problems-for-programs/index.html#tm2-recognizable-not-empty).

## Emptiness is co-recognizable

The set of codes of partial recursive functions
$\mathbb{N} \to \mathbb{N}$ that are defined on no input is co-recognizable by multi-stack
machines: some multi-stack machine halts on the binary encoding of a code $c$ exactly when the
function coded by $c$ is defined on at least one input.

Formalized by `Cslib.Decidability.tm2CoRecognizable_empty`, a theorem declared in [CSLibExt/Computability/Decidability/RiceApplications.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RiceApplications.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/emptiness-and-equivalence-problems-for-programs/index.html#tm2-co-recognizable-empty).

## Emptiness is not recognizable

The set $E$ of codes of partial recursive functions on
$\mathbb{N}$ that are defined on no input is not recognizable by multi-stack machines: no
multi-stack machine, started on the binary encoding of a code, halts exactly when the code is
in $E$.

Since $E$ is co-recognizable, it would otherwise be decidable, by Post's theorem.

Formalized by `Cslib.Decidability.not_tm2Recognizable_empty`, a theorem declared in [CSLibExt/Computability/Decidability/RiceApplications.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RiceApplications.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/emptiness-and-equivalence-problems-for-programs/index.html#not-tm2-recognizable-empty).

## Equivalent codes

The set $EQ$ consists of the pairs $(c_1, c_2)$ of codes of partial
recursive functions on $\mathbb{N}$ that recognize the same language, that is, whose computed
functions have the same domain: for every $n \in \mathbb{N}$, the function computed by $c_1$ is
defined at $n$ if and only if the function computed by $c_2$ is.

Formalized by `Cslib.Decidability.EqCode`, a definition declared in [CSLibExt/Computability/Decidability/RiceApplications.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RiceApplications.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/emptiness-and-equivalence-problems-for-programs/index.html#eq-code).

## A code defined nowhere

There is a code $e$ of a partial recursive function on
$\mathbb{N}$ whose computed function is the empty partial function, undefined at every input.

Formalized by `Cslib.Decidability.exists_code_empty`, a theorem declared in [CSLibExt/Computability/Decidability/RiceApplications.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RiceApplications.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/emptiness-and-equivalence-problems-for-programs/index.html#exists-code-empty).

## Emptiness reduces to equivalence

The set $E$ of codes of partial recursive functions
defined on no input is many-one reducible to the set $EQ$ of pairs of codes with the same
domain: there is a computable map $f$ from codes to pairs of codes such that, for every code $c$,
$c \in E$ if and only if $f(c) \in EQ$.

One can take $f(c) = (c, e)$ for a code $e$ defined nowhere.

Formalized by `Cslib.Decidability.manyOneReducible_empty_eq`, a theorem declared in [CSLibExt/Computability/Decidability/RiceApplications.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RiceApplications.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/emptiness-and-equivalence-problems-for-programs/index.html#many-one-reducible-empty-eq).

## Equivalence is not recognizable

The set $EQ$ of pairs of codes of partial recursive
functions on $\mathbb{N}$ with the same domain is not recognizable by multi-stack machines: no
multi-stack machine, started on the binary encoding of a pair of codes, halts exactly when the
pair is in $EQ$.

Formalized by `Cslib.Decidability.not_tm2Recognizable_eq`, a theorem declared in [CSLibExt/Computability/Decidability/RiceApplications.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RiceApplications.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/emptiness-and-equivalence-problems-for-programs/index.html#not-tm2-recognizable-eq).

## Halting-on-zero code

For a code $c$ of a partial recursive function on $\mathbb{N}$, the
code $h(c)$ is the composition $k_0 \circ c \circ k_0$, where $k_0$ is the code of the constant
function $0$: whatever its input, $h(c)$ runs $c$ on $0$ and, if this halts, outputs $0$.

Formalized by `Cslib.Decidability.haltsOnZeroCode`, a definition declared in [CSLibExt/Computability/Decidability/RiceApplications.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RiceApplications.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/emptiness-and-equivalence-problems-for-programs/index.html#halts-on-zero-code).

## Halting on zero reduces to equivalence

The set of codes $c$ of partial recursive
functions on $\mathbb{N}$ that halt on input $0$ (are defined at $0$) is many-one reducible to
the set $EQ$ of pairs of codes with the same domain: there is a computable map $f$ from codes to
pairs of codes such that, for every code $c$, $c$ halts on $0$ if and only if $f(c) \in EQ$.

One can take $f(c) = (h(c), k_0)$, where $h(c)$ runs $c$ on $0$ and then outputs $0$ whatever
its input, and $k_0$ is the code of the constant function $0$.

Formalized by `Cslib.Decidability.manyOneReducible_halting_eq`, a theorem declared in [CSLibExt/Computability/Decidability/RiceApplications.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RiceApplications.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/emptiness-and-equivalence-problems-for-programs/index.html#many-one-reducible-halting-eq).

## Equivalence is not co-recognizable

The set $EQ$ of pairs of codes of partial recursive
functions on $\mathbb{N}$ with the same domain is not co-recognizable by multi-stack machines:
no multi-stack machine, started on the binary encoding of a pair of codes, halts exactly when
the pair is not in $EQ$.

The complement of halting on $0$ would reduce to the complement of equivalence.

Formalized by `Cslib.Decidability.not_tm2CoRecognizable_eq`, a theorem declared in [CSLibExt/Computability/Decidability/RiceApplications.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RiceApplications.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/emptiness-and-equivalence-problems-for-programs/index.html#not-tm2-co-recognizable-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Emptiness and equivalence problems for programs](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/emptiness-and-equivalence-problems-for-programs/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/computability/emptiness-and-equivalence-problems-for-programs)
