---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.RunLength.compressFrom, Cslib.Algorithms.Lean.RunLength.compress, Cslib.Algorithms.Lean.RunLength.expandFrom, Cslib.Algorithms.Lean.RunLength.expand, Cslib.Algorithms.Lean.RunLength.compressFrom_le, Cslib.Algorithms.Lean.RunLength.compress_le, Cslib.Algorithms.Lean.RunLength.expandFrom_length, Cslib.Algorithms.Lean.RunLength.expand_length
statement: formalized
proof: formalized
---

# Run-length encoding

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/run-length-encoding/index.html).

## Run-length compression from a pending run

For a bit $c$, a natural number $r$ and a
finite bit list $w$, the compression $C(c, r, w)$ of $w$ from the pending run $(c, r)$ is the
list of natural numbers defined by recursion on $w$. If $w$ is empty, $C(c, r, w)$ is the
one-entry list $(r)$. If $w$ is a bit $b$ followed by a list $w'$, then $C(c, r, w)$ is $r$
followed by $C(\lnot c, 1, w')$ when $b \ne c$; it is $255$, then $0$, followed by
$C(c, 1, w')$ when $b = c$ and $r = 255$; otherwise it is $C(c, r + 1, w')$.

Here $c$ is the bit of the current run and $r$ is its length so far.

Formalized by `Cslib.Algorithms.Lean.RunLength.compressFrom`, a definition declared in [CSLibExt/Algorithms/Lean/Compression/RunLength.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Compression/RunLength.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/run-length-encoding/index.html#compress-from).

## Run-length compression

The run-length compression of a finite bit list $w$ is
$C(0, 0, w)$, the compression of $w$ from an empty pending run of zero bits. It lists the
lengths of the maximal runs of $w$, alternating between zeros and ones and starting with a
possibly empty run of zeros; a run of length $n > 255$ is written as
$255, 0, 255, 0, \dots, 255, 0, m$ with $1 \le m \le 255$.

Formalized by `Cslib.Algorithms.Lean.RunLength.compress`, a definition declared in [CSLibExt/Algorithms/Lean/Compression/RunLength.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Compression/RunLength.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/run-length-encoding/index.html#compress).

## Run-length expansion from a starting bit

For a bit $c$ and a list $(n_1, \dots, n_k)$ of
natural numbers, the expansion $E(c, (n_1, \dots, n_k))$ is the bit list obtained by
concatenating, for $i = 1, \dots, k$ in order, $n_i$ copies of $c$ when $i$ is odd and $n_i$
copies of $\lnot c$ when $i$ is even.

Formalized by `Cslib.Algorithms.Lean.RunLength.expandFrom`, a definition declared in [CSLibExt/Algorithms/Lean/Compression/RunLength.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Compression/RunLength.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/run-length-encoding/index.html#expand-from).

## Run-length expansion

The run-length expansion of a list $(n_1, \dots, n_k)$ of natural
numbers is $E(0, (n_1, \dots, n_k))$, the expansion from the zero bit: the bit list obtained by
concatenating, for $i = 1, \dots, k$ in order, $n_i$ zeros when $i$ is odd and $n_i$ ones when
$i$ is even.

Formalized by `Cslib.Algorithms.Lean.RunLength.expand`, a definition declared in [CSLibExt/Algorithms/Lean/Compression/RunLength.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Compression/RunLength.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/run-length-encoding/index.html#expand).

## Compression from a short pending run emits counts at most 255

For every bit $c$, every
natural number $r \le 255$ and every finite bit list $w$, every entry of the compression
$C(c, r, w)$ of $w$ from the pending run $(c, r)$ is at most $255$.

Formalized by `Cslib.Algorithms.Lean.RunLength.compressFrom_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Compression/RunLength.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Compression/RunLength.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/run-length-encoding/index.html#compress-from-le).

## Run lengths fit in 8 bits

For every finite bit list $w$, every entry of the run-length
compression of $w$ is at most $255$.

Formalized by `Cslib.Algorithms.Lean.RunLength.compress_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Compression/RunLength.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Compression/RunLength.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/run-length-encoding/index.html#compress-le).

## Length of an expansion from a starting bit

For every bit $c$ and every list
$(n_1, \dots, n_k)$ of natural numbers, the expansion $E(c, (n_1, \dots, n_k))$ has length
$n_1 + \dots + n_k$.

Formalized by `Cslib.Algorithms.Lean.RunLength.expandFrom_length`, a theorem declared in [CSLibExt/Algorithms/Lean/Compression/RunLength.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Compression/RunLength.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/run-length-encoding/index.html#expand-from-length).

## Length of a run-length expansion

For every list $(n_1, \dots, n_k)$ of natural numbers,
the run-length expansion of $(n_1, \dots, n_k)$ has length $n_1 + \dots + n_k$.

Formalized by `Cslib.Algorithms.Lean.RunLength.expand_length`, a theorem declared in [CSLibExt/Algorithms/Lean/Compression/RunLength.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Compression/RunLength.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/run-length-encoding/index.html#expand-length).

## Expansion recovers the pending run and the input

For every bit $c$, every natural
number $r$ and every finite bit list $w$, the expansion from the starting bit $c$ of the
compression $C(c, r, w)$ is the list of $r$ copies of $c$ followed by $w$.

Formalized by `Cslib.Algorithms.Lean.RunLength.expandFrom_compressFrom`, a theorem declared in [CSLibExt/Algorithms/Lean/Compression/RunLength.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Compression/RunLength.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/run-length-encoding/index.html#expand-from-compress-from).

## Run-length expansion inverts compression

For every finite bit list $w$, the run-length
expansion of the run-length compression of $w$ is $w$.

Formalized by `Cslib.Algorithms.Lean.RunLength.expand_compress`, a theorem declared in [CSLibExt/Algorithms/Lean/Compression/RunLength.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Compression/RunLength.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/run-length-encoding/index.html#expand-compress).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Run-length encoding](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/run-length-encoding/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/InformationTheory/source-coding/run-length-encoding)
