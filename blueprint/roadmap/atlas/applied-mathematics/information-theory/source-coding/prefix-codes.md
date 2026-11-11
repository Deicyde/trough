---
declaration: section
origin: cited
lean: MathlibExt.InformationTheory.IsPrefixFree, MathlibExt.InformationTheory.IsPrefixFree.eq_of_isPrefix, MathlibExt.InformationTheory.IsPrefixFree.injective, MathlibExt.InformationTheory.IsPrefixFree.eq_of_mem_nil
statement: formalized
proof: formalized
---

# Prefix codes

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/prefix-codes/index.html).

## Prefix-free code

A code $c$ assigning to each source symbol a finite word over an
alphabet is prefix-free if for all distinct symbols $a_1 \ne a_2$ the word $c(a_1)$ is not a
prefix of $c(a_2)$. Since the condition covers all ordered pairs of distinct symbols, both
prefix directions are forbidden.

Formalized by `MathlibExt.InformationTheory.IsPrefixFree`, a definition declared in [MathlibExt/InformationTheory/PrefixFree.lean, line 20](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/PrefixFree.lean#L20). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/prefix-codes/index.html#is-prefix-free).

## Prefix-related codewords come from the same symbol

If $c$ is a prefix-free code and the
codeword $c(a_1)$ is a prefix of $c(a_2)$, then $a_1 = a_2$.

Formalized by `MathlibExt.InformationTheory.IsPrefixFree.eq_of_isPrefix`, a theorem declared in [MathlibExt/InformationTheory/PrefixFree.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/PrefixFree.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/prefix-codes/index.html#eq-of-is-prefix).

## Prefix-free codes are injective

If $c$ is a prefix-free code and $c(a_1) = c(a_2)$,
then $a_1 = a_2$.

Equal codewords are mutually prefix, hence come from equal symbols.

Formalized by `MathlibExt.InformationTheory.IsPrefixFree.injective`, a theorem declared in [MathlibExt/InformationTheory/PrefixFree.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/PrefixFree.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/prefix-codes/index.html#injective).

## A prefix-free code with an empty codeword has one symbol

If a prefix-free code $c$
assigns the empty word to a symbol $a_0$, then every symbol $a$ equals $a_0$.

This holds because the empty word is a prefix of every word.

Formalized by `MathlibExt.InformationTheory.IsPrefixFree.eq_of_mem_nil`, a theorem declared in [MathlibExt/InformationTheory/PrefixFree.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/PrefixFree.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/prefix-codes/index.html#eq-of-mem-nil).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Prefix codes](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/prefix-codes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/InformationTheory/source-coding/prefix-codes)
