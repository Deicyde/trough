---
declaration: section
origin: cited
lean: MetaMathlibExt.shiftedPadovanSequence, MetaMathlibExt.shiftedPadovanSequence_add_three, MetaMathlibExt.perrinSequence
statement: formalized
proof: formalized
---

# Padovan and Perrin sequences

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/padovan-and-perrin-sequences/index.html).

## Shifted Padovan sequence

The shifted Padovan sequence is the sequence of natural numbers
$(a_n)_{n \ge 0}$ with $a_0 = 1$, $a_1 = 0$, $a_2 = 1$ and $a_{n+3} = a_{n+1} + a_n$ for every
$n \ge 0$.

## Sources

- Daniel Birmajer, Juan B. Gil, and Michael D. Weiner, *Linear Recurrence Sequences and Their Convolutions via Bell Polynomials*, <https://cs.uwaterloo.ca/journals/JIS/VOL18/Gil/gil3.tex>, where this shifted version is used.

Formalized by `MetaMathlibExt.shiftedPadovanSequence`, a definition declared in [MathlibExt/NumberTheory/PadovanSequence.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PadovanSequence.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/padovan-and-perrin-sequences/index.html#shifted-padovan-sequence).

## Recurrence of the shifted Padovan sequence

For every natural number $n$, the shifted
Padovan sequence $(a_n)_{n \ge 0}$ satisfies $a_{n+3} = a_{n+1} + a_n$.

Formalized by `MetaMathlibExt.shiftedPadovanSequence_add_three`, a theorem declared in [MathlibExt/NumberTheory/PadovanSequence.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PadovanSequence.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/padovan-and-perrin-sequences/index.html#shifted-padovan-sequence-add-three).

## Perrin sequence

The Perrin sequence $E_n$, for natural numbers $n$, is defined by
$E_0 = 3$, $E_1 = 0$, $E_2 = 2$ and $E_n = E_{n-2} + E_{n-3}$ for every $n \ge 3$.

Formalized by `MetaMathlibExt.perrinSequence`, a definition declared in [MathlibExt/NumberTheory/PerrinSequence.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PerrinSequence.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/padovan-and-perrin-sequences/index.html#perrin-sequence).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Padovan and Perrin sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/padovan-and-perrin-sequences/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/padovan-and-perrin-sequences)
