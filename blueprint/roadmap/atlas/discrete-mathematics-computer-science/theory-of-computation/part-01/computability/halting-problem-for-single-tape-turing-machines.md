---
declaration: section
origin: cited
lean: Cslib.Decidability.TM0HaltsOn, Cslib.Decidability.tm2HaltsOn_iff_eval_dom, Cslib.Decidability.primcodableOfFintype, Cslib.Decidability.primrec_trInit_encodeNat, Cslib.Decidability.exists_not_tm2Decidable_tm0HaltsOn
statement: formalized
proof: formalized
---

# Halting problem for single-tape Turing machines

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/halting-problem-for-single-tape-turing-machines/index.html).

## Halting of a single-tape machine

A single-tape Turing machine $M$ halts on an input word
$l$ when its run, started in its start state with $l$ on the tape, reaches a halting
configuration.

Formalized by `Cslib.Decidability.TM0HaltsOn`, a definition declared in [CSLibExt/Computability/Decidability/TM0Halting.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/TM0Halting.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/halting-problem-for-single-tape-turing-machines/index.html#tm0-halts-on).

## Halting agrees with evaluation for multi-stack machines

A multi-stack machine halts on a
word $l$ over the alphabet of its input stack if and only if the evaluation of its transition
function, started at its main label and initial internal state with $l$ on the input stack and
all other stacks empty, is defined.

Formalized by `Cslib.Decidability.tm2HaltsOn_iff_eval_dom`, a theorem declared in [CSLibExt/Computability/Decidability/TM0Halting.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/TM0Halting.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/halting-problem-for-single-tape-turing-machines/index.html#tm2-halts-on-iff-eval-dom).

## Primitive recursive coding of a finite type

A finite type $\alpha$ with $n$ elements gets
the primitive recursive coding transported from $\{0, \dots, n - 1\}$ along a fixed (noncanonically
chosen) bijection between $\alpha$ and $\{0, \dots, n - 1\}$.

Formalized by `Cslib.Decidability.primcodableOfFintype`, a definition declared in [CSLibExt/Computability/Decidability/TM0Halting.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/TM0Halting.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/halting-problem-for-single-tape-turing-machines/index.html#primcodable-of-fintype).

## The input encoding of the single-tape emulation is primitive recursive

Let $M$ be a
multi-stack machine together with a bijection $e$ from the alphabet of its input stack to the
Booleans, and suppose the tape alphabet $\Gamma'$ of the single-tape emulation of $M$ is finite and
carries a primitive recursive coding. Then the map sending $n \in \mathbb{N}$ to the initial tape
of the emulation on the input word $e^{-1}(b_1) \cdots e^{-1}(b_m)$, where $b_1 \cdots b_m$ is the
binary code of $n$, is primitive recursive.

Formalized by `Cslib.Decidability.primrec_trInit_encodeNat`, a theorem declared in [CSLibExt/Computability/Decidability/TM0Halting.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/TM0Halting.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/halting-problem-for-single-tape-turing-machines/index.html#primrec-tr-init-encode-nat).

## The halting problem for single-tape machines is undecidable

There are a finite tape
alphabet $\Gamma$ with a blank symbol, decidable equality and a primitive recursive coding, a type
of states $\Lambda$ with a start state, a single-tape Turing machine $M$ with alphabet $\Gamma$ and
states $\Lambda$, and a finite set $S$ of states that contains the start state and is closed under
the transitions of $M$, such that the set of input words on which $M$ halts is not decidable by a
multi-stack machine.

Formalized by `Cslib.Decidability.exists_not_tm2Decidable_tm0HaltsOn`, a theorem declared in [CSLibExt/Computability/Decidability/TM0Halting.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/TM0Halting.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/halting-problem-for-single-tape-turing-machines/index.html#exists-not-tm2-decidable-tm0-halts-on).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Halting problem for single-tape Turing machines](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/halting-problem-for-single-tape-turing-machines/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/computability/halting-problem-for-single-tape-turing-machines)
