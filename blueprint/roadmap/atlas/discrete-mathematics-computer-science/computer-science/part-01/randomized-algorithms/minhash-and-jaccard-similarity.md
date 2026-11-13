---
declaration: section
origin: cited
lean: Cslib.Bioinformatics.Sketching.MinHash.minHash, Cslib.Bioinformatics.Sketching.MinHash.card_minHash_collision, Cslib.Bioinformatics.Sketching.MinHash.uniformOn_minHash_collision
statement: formalized
proof: formalized
---

# MinHash and Jaccard similarity

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/minhash-and-jaccard-similarity/index.html).

## Min-hash of a set under a permutation

The min-hash of `A` under the permutation `π`: the least element of `π(A)`, or `⊤` if `A` is
empty.

Formalized by `Cslib.Bioinformatics.Sketching.MinHash.minHash`, a definition declared in [CSLibExt/Bioinformatics/Sketching/MinHash.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Sketching/MinHash.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/minhash-and-jaccard-similarity/index.html#min-hash).

## MinHash, counting form

The number of permutations of `U` under which `A` and `B` have
the same min-hash, times `|A ∪ B|`, equals `|A ∩ B|` times the number of all permutations.

Formalized by `Cslib.Bioinformatics.Sketching.MinHash.card_minHash_collision`, a theorem declared in [CSLibExt/Bioinformatics/Sketching/MinHash.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Sketching/MinHash.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/minhash-and-jaccard-similarity/index.html#card-min-hash-collision).

## MinHash collision probability

**MinHash collision probability** (Broder 1997): for a uniformly random permutation `π` of
the finite universe `U` (`uniformOn Set.univ` on `Equiv.Perm U`, for any measurable structure in
which singletons are measurable, e.g. `⊤`) and sets `A`, `B` with `A ∪ B` nonempty,
`P(min π(A) = min π(B)) = |A ∩ B| / |A ∪ B|`, the Jaccard similarity of `A` and `B`.

Formalized by `Cslib.Bioinformatics.Sketching.MinHash.uniformOn_minHash_collision`, a theorem declared in [CSLibExt/Bioinformatics/Sketching/MinHash.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Sketching/MinHash.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/minhash-and-jaccard-similarity/index.html#uniform-on-min-hash-collision).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: MinHash and Jaccard similarity](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/minhash-and-jaccard-similarity/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/randomized-algorithms/minhash-and-jaccard-similarity)
