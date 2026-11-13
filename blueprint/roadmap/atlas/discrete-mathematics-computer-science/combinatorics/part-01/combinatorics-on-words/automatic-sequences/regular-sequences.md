---
declaration: section
origin: cited
lean: MetaMathlibExt.IsKRegularSequence, MetaMathlibExt.isKRegularSequence_const, MetaMathlibExt.IsKRegularSequence.two_le
statement: formalized
proof: formalized
---

# Regular sequences

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/regular-sequences/index.html).

## $k$-regular sequence

Let $k$ be a natural number. An integer sequence
$f : \mathbb{N} \to \mathbb{Z}$ is $k$-regular, in the sense of Allouche and Shallit, if
$k \ge 2$ and the $\mathbb{Z}$-submodule of the module of all integer sequences spanned by the
$k$-kernel of $f$ is finitely generated.

## Sources

- John M. Campbell and Benoît Cloitre, *Meta-Automatic Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.1, Lemma 28 (`k`-regular sequences of Allouche and Shallit) and Definition 1 (`k`-kernel).

Formalized by `MetaMathlibExt.IsKRegularSequence`, a definition declared in [MathlibExt/Combinatorics/Words/RegularSequence.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Words/RegularSequence.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/regular-sequences/index.html#is-kregular-sequence).

## Constant sequences are $k$-regular

For every natural number $k \ge 2$ and every integer
$c$, the constant sequence $n \mapsto c$ is $k$-regular.

## Sources

- John M. Campbell and Benoît Cloitre, *Meta-Automatic Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.1, Lemma 28.

Formalized by `MetaMathlibExt.isKRegularSequence_const`, a theorem declared in [MathlibExt/Combinatorics/Words/RegularSequence.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Words/RegularSequence.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/regular-sequences/index.html#is-kregular-sequence-const).

## The base of a $k$-regular sequence is at least 2

Let $k$ be a natural number. If an integer
sequence $f$ is $k$-regular, then $k \ge 2$.

## Sources

- John M. Campbell and Benoît Cloitre, *Meta-Automatic Sequences*, Journal of Integer Sequences 29 (2026), Article 26.4.1, Lemma 28.

Formalized by `MetaMathlibExt.IsKRegularSequence.two_le`, a theorem declared in [MathlibExt/Combinatorics/Words/RegularSequence.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Words/RegularSequence.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/regular-sequences/index.html#two-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Regular sequences](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/regular-sequences/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/regular-sequences)
