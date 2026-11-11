---
declaration: section
origin: cited
lean: Cslib.Decidability.Enumerates, Cslib.Decidability.TM2Recognizable.exists_enumerator, Cslib.Decidability.tm2Recognizable_of_enumerates, Cslib.Decidability.tm2Recognizable_iff_exists_enumerator
statement: formalized
proof: formalized
---

# Enumerators

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/enumerators/index.html).

## Enumerating a predicate

For a type $\alpha$ with a primitive recursive encoding, a
function $e$ assigning to each natural number $n$ either an element $e(n)$ of $\alpha$ or nothing
enumerates a predicate $p$ on $\alpha$ when, for every $a \in \alpha$, $p(a)$ holds if and only if
$e(n) = a$ for some natural number $n$.

Formalized by `Cslib.Decidability.Enumerates`, a definition declared in [CSLibExt/Computability/Decidability/Enumerators.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Enumerators.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/enumerators/index.html#enumerates).

## Recognizable languages are enumerable

For every type $\alpha$ with a primitive recursive
encoding and every predicate $p$ on $\alpha$ that is recognizable by a multi-stack machine, there
is a computable function $e$, assigning to each natural number either an element of $\alpha$ or
nothing, that enumerates $p$.

Formalized by `Cslib.Decidability.TM2Recognizable.exists_enumerator`, a theorem declared in [CSLibExt/Computability/Decidability/Enumerators.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Enumerators.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/enumerators/index.html#exists-enumerator).

## Enumerable languages are recognizable

For every type $\alpha$ with a primitive recursive
encoding, every predicate $p$ on $\alpha$ and every computable function $e$, assigning to each
natural number either an element of $\alpha$ or nothing, that enumerates $p$, the predicate $p$ is
recognizable by a multi-stack machine.

Formalized by `Cslib.Decidability.tm2Recognizable_of_enumerates`, a theorem declared in [CSLibExt/Computability/Decidability/Enumerators.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Enumerators.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/enumerators/index.html#tm2-recognizable-of-enumerates).

## Recognizable languages are exactly the enumerable ones

For every type $\alpha$ with a
primitive recursive encoding, a predicate $p$ on $\alpha$ is recognizable by a multi-stack machine
if and only if some computable function $e$, assigning to each natural number either an element
of $\alpha$ or nothing, enumerates $p$. This is Sipser, Theorem 3.21: a language is
Turing-recognizable if and only if some enumerator enumerates it.

Formalized by `Cslib.Decidability.tm2Recognizable_iff_exists_enumerator`, a theorem declared in [CSLibExt/Computability/Decidability/Enumerators.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/Enumerators.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/enumerators/index.html#tm2-recognizable-iff-exists-enumerator).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Enumerators](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/enumerators/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/computability/enumerators)
