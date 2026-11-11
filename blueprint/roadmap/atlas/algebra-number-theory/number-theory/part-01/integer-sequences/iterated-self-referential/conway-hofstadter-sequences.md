---
declaration: section
origin: cited
lean: MetaMathlibExt.conwayHofstadterResidue, MetaMathlibExt.IsConwayHofstadterLikeSequence
statement: formalized
proof: formalized
---

# Conway–Hofstadter sequences

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/conway-hofstadter-sequences/index.html).

## One-based residue

For natural numbers $a$ and $m$, the one-based residue of $a$ modulo
$m$ is $a \bmod m$ if this is nonzero, and $m$ if $a \bmod m = 0$ (here $a \bmod 0 = a$). This is
the residue convention used in Pelesko's recurrence.

Formalized by `MetaMathlibExt.conwayHofstadterResidue`, a definition declared in [MathlibExt/NumberTheory/ConwayHofstadterLikeSequence.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ConwayHofstadterLikeSequence.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/conway-hofstadter-sequences/index.html#conway-hofstadter-residue).

## Conway–Hofstadter-like sequence

Let $k$ be a natural number. A sequence
$c : \mathbb{N} \to \mathbb{N}$ is a Conway–Hofstadter-like sequence of order $k$ when
$c(1) = c(2) = 1$ and, for every $n \ge 3$,

$$c(n) = c(i_n) + c(n - i_n),$$

where $i_n$ is the one-based residue of $k \, c(n-1)$ modulo $n - 1$: it equals
$k \, c(n-1) \bmod (n-1)$ when this is nonzero, and $n - 1$ otherwise.

The value $c(0)$ is not constrained.

Formalized by `MetaMathlibExt.IsConwayHofstadterLikeSequence`, a definition declared in [MathlibExt/NumberTheory/ConwayHofstadterLikeSequence.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ConwayHofstadterLikeSequence.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/conway-hofstadter-sequences/index.html#is-conway-hofstadter-like-sequence).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Conway–Hofstadter sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/conway-hofstadter-sequences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/integer-sequences/iterated-self-referential/conway-hofstadter-sequences)
