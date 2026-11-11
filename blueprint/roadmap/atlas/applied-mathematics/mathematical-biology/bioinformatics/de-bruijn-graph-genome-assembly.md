---
declaration: section
origin: cited
lean: Cslib.Bioinformatics.Assembly.DeBruijn.kmers, Cslib.Bioinformatics.Assembly.DeBruijn.kmersImpl, Cslib.Bioinformatics.Assembly.DeBruijn.kmerEdge, Cslib.Bioinformatics.Assembly.DeBruijn.deBruijnEdges, Cslib.Bioinformatics.Assembly.DeBruijn.spell, Cslib.Bioinformatics.Assembly.DeBruijn.zip_tail_kmers, Cslib.Bioinformatics.Assembly.DeBruijn.zip_tail_kmers_perm, Cslib.Bioinformatics.Assembly.DeBruijn.spell_kmers
statement: formalized
proof: formalized
---

# De Bruijn graph genome assembly

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/de-bruijn-graph-genome-assembly/index.html).

## The k-mers of a string

The `k`-mers of `s` in order of position: the length-`k` windows `(s.drop i).take k`
for `i + k ≤ |s|`.

Formalized by `Cslib.Bioinformatics.Assembly.DeBruijn.kmers`, a definition declared in [CSLibExt/Bioinformatics/Assembly/DeBruijn.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Assembly/DeBruijn.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/de-bruijn-graph-genome-assembly/index.html#kmers).

## Efficient executable computation of k-mers

Executable form of `kmers`: the suffixes of `s` are generated once by `List.tails`, so the
cost is `O(|s| · k)` rather than the `Θ(|s|²)` of recomputing `s.drop i` for every `i`. The
compiler uses it in place of `kmers` (`kmers_eq_kmersImpl`).

Formalized by `Cslib.Bioinformatics.Assembly.DeBruijn.kmersImpl`, a definition declared in [CSLibExt/Bioinformatics/Assembly/DeBruijn.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Assembly/DeBruijn.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/de-bruijn-graph-genome-assembly/index.html#kmers-impl).

## De Bruijn edge of a k-mer

The edge of the de Bruijn multigraph contributed by a `k`-mer `w`: from its prefix
`(k-1)`-mer `w.dropLast` to its suffix `(k-1)`-mer `w.tail`.

Formalized by `Cslib.Bioinformatics.Assembly.DeBruijn.kmerEdge`, a definition declared in [CSLibExt/Bioinformatics/Assembly/DeBruijn.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Assembly/DeBruijn.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/de-bruijn-graph-genome-assembly/index.html#kmer-edge).

## De Bruijn multigraph of a string

The de Bruijn multigraph of `s` (Pevzner–Tang–Waterman 2001) as its list of edge
occurrences: one edge per `k`-mer occurrence, in order of position.

Formalized by `Cslib.Bioinformatics.Assembly.DeBruijn.deBruijnEdges`, a definition declared in [CSLibExt/Bioinformatics/Assembly/DeBruijn.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Assembly/DeBruijn.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/de-bruijn-graph-genome-assembly/index.html#de-bruijn-edges).

## String spelled by a walk of (k-1)-mers

The string spelled by a walk of `(k-1)`-mers: the first vertex followed by the last letter of
each later vertex.

Formalized by `Cslib.Bioinformatics.Assembly.DeBruijn.spell`, a definition declared in [CSLibExt/Bioinformatics/Assembly/DeBruijn.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Assembly/DeBruijn.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/de-bruijn-graph-genome-assembly/index.html#spell).

## The `(k-1)`-mer walk of `s` traverses the de Bruijn multigraph in order

Its steps are
exactly the edges contributed by the `k`-mers of `s`, one per occurrence, in order of position.

Formalized by `Cslib.Bioinformatics.Assembly.DeBruijn.zip_tail_kmers`, a theorem declared in [CSLibExt/Bioinformatics/Assembly/DeBruijn.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Assembly/DeBruijn.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/de-bruijn-graph-genome-assembly/index.html#zip-tail-kmers).

## The `k`-mer walk of `s` is an Eulerian trail

**The `k`-mer walk of `s` is an Eulerian trail** of its de Bruijn multigraph: its steps are a
permutation of the edge occurrences, each traversed once.

Formalized by `Cslib.Bioinformatics.Assembly.DeBruijn.zip_tail_kmers_perm`, a theorem declared in [CSLibExt/Bioinformatics/Assembly/DeBruijn.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Assembly/DeBruijn.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/de-bruijn-graph-genome-assembly/index.html#zip-tail-kmers-perm).

## The (k-1)-mer walk of a string spells the string

The `(k-1)`-mer walk of `s` spells `s` back (`2 ≤ k`, `k - 1 ≤ |s|`).

Formalized by `Cslib.Bioinformatics.Assembly.DeBruijn.spell_kmers`, a theorem declared in [CSLibExt/Bioinformatics/Assembly/DeBruijn.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Assembly/DeBruijn.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/de-bruijn-graph-genome-assembly/index.html#spell-kmers).

## Every Eulerian trail spells a string with the same `k`-mer multiset

**Every Eulerian trail spells a string with the same `k`-mer multiset** (`2 ≤ k`): if `W` is a
walk of `(k-1)`-mers whose steps are a permutation of the edge occurrences of the de Bruijn
multigraph of `s`, then the `k`-mers of the spelled string are a permutation of those of `s`.
(The empty walk is allowed: it is a trail only when `s` has no `k`-mers, and spells `[]`.)

Formalized by `Cslib.Bioinformatics.Assembly.DeBruijn.kmers_spell_perm`, a theorem declared in [CSLibExt/Bioinformatics/Assembly/DeBruijn.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Assembly/DeBruijn.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/de-bruijn-graph-genome-assembly/index.html#kmers-spell-perm).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: De Bruijn graph genome assembly](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/de-bruijn-graph-genome-assembly/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/bioinformatics/de-bruijn-graph-genome-assembly)
