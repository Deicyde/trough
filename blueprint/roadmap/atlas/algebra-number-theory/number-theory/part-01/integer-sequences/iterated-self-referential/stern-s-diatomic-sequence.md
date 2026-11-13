---
declaration: section
origin: cited
lean: MetaMathlibExt.sternSequence, MetaMathlibExt.stern_zero, MetaMathlibExt.stern_one, MetaMathlibExt.stern_even, MetaMathlibExt.stern_odd
statement: formalized
proof: formalized
---

# Stern's diatomic sequence

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/stern-s-diatomic-sequence/index.html).

## Stern's diatomic sequence

The Stern sequence is the function
$s : \mathbb{N} \to \mathbb{N}$ defined by $s(0) = 0$, $s(1) = 1$, and, for every $n \ge 1$,
$s(2n) = s(n)$ and $s(2n + 1) = s(n) + s(n + 1)$.

## Sources

- Stern sequence ("Stern diatomic sequence", OEIS A002487); JIS Lansing, lines 92-103; JIS Dennison, lines 80-85.

Formalized by `MetaMathlibExt.sternSequence`, a definition declared in [MathlibExt/NumberTheory/SternSequence.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SternSequence.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/stern-s-diatomic-sequence/index.html#stern-sequence).

## Stern sequence at zero

The Stern sequence $s$ satisfies $s(0) = 0$.

## Sources

- Stern sequence, OEIS A002487; JIS Lansing, lines 92-103.

Formalized by `MetaMathlibExt.stern_zero`, a theorem declared in [MathlibExt/NumberTheory/SternSequence.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SternSequence.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/stern-s-diatomic-sequence/index.html#stern-zero).

## Stern sequence at one

The Stern sequence $s$ satisfies $s(1) = 1$.

## Sources

- Stern sequence, OEIS A002487; JIS Lansing, lines 92-103.

Formalized by `MetaMathlibExt.stern_one`, a theorem declared in [MathlibExt/NumberTheory/SternSequence.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SternSequence.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/stern-s-diatomic-sequence/index.html#stern-one).

## Even-index recurrence for the Stern sequence

For every natural number $n \ge 1$, the
Stern sequence $s$ satisfies $s(2n) = s(n)$.

## Sources

- Stern sequence, OEIS A002487; JIS Lansing, lines 92-103; JIS Dennison, lines 80-85.

Formalized by `MetaMathlibExt.stern_even`, a theorem declared in [MathlibExt/NumberTheory/SternSequence.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SternSequence.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/stern-s-diatomic-sequence/index.html#stern-even).

## Odd-index recurrence for the Stern sequence

For every natural number $n \ge 1$, the
Stern sequence $s$ satisfies $s(2n + 1) = s(n) + s(n + 1)$.

## Sources

- Stern sequence, OEIS A002487; JIS Lansing, lines 92-103; JIS Dennison, lines 80-85.

Formalized by `MetaMathlibExt.stern_odd`, a theorem declared in [MathlibExt/NumberTheory/SternSequence.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SternSequence.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/stern-s-diatomic-sequence/index.html#stern-odd).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Stern's diatomic sequence](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/stern-s-diatomic-sequence/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/integer-sequences/iterated-self-referential/stern-s-diatomic-sequence)
