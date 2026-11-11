---
declaration: section
origin: cited
lean: Cslib.Bioinformatics.Indexing.BWT.withSentinel, Cslib.Bioinformatics.Indexing.BWT.sortedRotations, Cslib.Bioinformatics.Indexing.BWT.bwt, Cslib.Bioinformatics.Indexing.BWT.countLess, Cslib.Bioinformatics.Indexing.BWT.rank, Cslib.Bioinformatics.Indexing.BWT.lf, Cslib.Bioinformatics.Indexing.BWT.invertAux, Cslib.Bioinformatics.Indexing.BWT.invert
statement: formalized
proof: formalized
---

# Burrows–Wheeler transform and FM-index

32 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html).

## Text with an appended sentinel

The text `t` with the sentinel `⊥` appended: `t.map (↑) ++ [⊥]`. The sentinel is the unique
occurrence of `⊥` and is smaller than every letter.

Formalized by `Cslib.Bioinformatics.Indexing.BWT.withSentinel`, a definition declared in [CSLibExt/Bioinformatics/Indexing/BWT.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Indexing/BWT.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html#with-sentinel).

## Sorted rotations of a sentinel-terminated text

The starting positions `0, …, |t|` of the rotations of `withSentinel t`, sorted by their
rotations in lexicographic order: row `r` of the Burrows–Wheeler matrix is
`(withSentinel t).rotate ((sortedRotations t)[r])`.

Formalized by `Cslib.Bioinformatics.Indexing.BWT.sortedRotations`, a definition declared in [CSLibExt/Bioinformatics/Indexing/BWT.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Indexing/BWT.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html#sorted-rotations).

## Burrows–Wheeler transform

The Burrows–Wheeler transform: the last column of the sorted rotation matrix.

Formalized by `Cslib.Bioinformatics.Indexing.BWT.bwt`, a definition declared in [CSLibExt/Bioinformatics/Indexing/BWT.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Indexing/BWT.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html#bwt).

## Count of smaller letters in the FM-index

`C[c]`: the number of letters of `L` smaller than `c`.

Formalized by `Cslib.Bioinformatics.Indexing.BWT.countLess`, a definition declared in [CSLibExt/Bioinformatics/Indexing/BWT.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Indexing/BWT.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html#count-less).

## Rank of a letter in a prefix of the last column

`rank_c(L, r)`: the number of occurrences of `c` among the first `r` letters of `L`.

Formalized by `Cslib.Bioinformatics.Indexing.BWT.rank`, a definition declared in [CSLibExt/Bioinformatics/Indexing/BWT.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Indexing/BWT.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html#rank).

## LF-mapping from the last column

The LF-mapping computed from the last column alone: `LF(r) = C[L[r]] + rank_{L[r]}(L, r)`.

Formalized by `Cslib.Bioinformatics.Indexing.BWT.lf`, a definition declared in [CSLibExt/Bioinformatics/Indexing/BWT.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Indexing/BWT.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html#lf).

## Steps of the Burrows–Wheeler inversion walk

`k` steps of the inversion walk from row `r`: the letters `L[r], L[LF r], …`.

Formalized by `Cslib.Bioinformatics.Indexing.BWT.invertAux`, a definition declared in [CSLibExt/Bioinformatics/Indexing/BWT.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Indexing/BWT.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html#invert-aux).

## Inversion of the Burrows–Wheeler transform

Inversion of the Burrows–Wheeler transform: walk the LF-mapping `|L| - 1` times from row `0`
(the rotation that starts with the sentinel) and reverse the letters read.

Formalized by `Cslib.Bioinformatics.Indexing.BWT.invert`, a definition declared in [CSLibExt/Bioinformatics/Indexing/BWT.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Indexing/BWT.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html#invert).

## Length of the Burrows–Wheeler transform

The Burrows–Wheeler transform of `t` has length `|t| + 1` (the sentinel adds one letter).

Formalized by `Cslib.Bioinformatics.Indexing.BWT.length_bwt`, a theorem declared in [CSLibExt/Bioinformatics/Indexing/BWT.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Indexing/BWT.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html#length-bwt).

## The sentinel stops every prefix match

A sentinel-free word `P` is a prefix of `u ++ ⊥ :: v` (letters lifted to `WithBot α`) exactly
when it is a prefix of `u`: the sentinel `⊥` stops every match.

Formalized by `Cslib.Bioinformatics.Indexing.BWT.map_coe_prefix_append_bot_cons_iff`, a theorem declared in [CSLibExt/Bioinformatics/Indexing/BWT.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Indexing/BWT.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html#map-coe-prefix-append-bot-cons-iff).

## Rows of the Burrows–Wheeler matrix are sorted

The rows of the Burrows–Wheeler matrix are sorted: the rotations listed by
`sortedRotations t` are in lexicographically nondecreasing order.

Formalized by `Cslib.Bioinformatics.Indexing.BWT.pairwise_sortedRotations`, a theorem declared in [CSLibExt/Bioinformatics/Indexing/BWT.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Indexing/BWT.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html#pairwise-sorted-rotations).

## The LF-mapping property

For every row `r`, row `lf (bwt t) r` holds the rotation of
row `r` rotated right by one position, i.e. starting one position earlier in the text.

Formalized by `Cslib.Bioinformatics.Indexing.BWT.sortedRotations_getD_lf`, a theorem declared in [CSLibExt/Bioinformatics/Indexing/BWT.lean, line 501](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Indexing/BWT.lean#L501). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html#sorted-rotations-get-d-lf).

## Inversion

The Burrows–Wheeler transform is inverted by the LF-mapping walk.

Formalized by `Cslib.Bioinformatics.Indexing.BWT.invert_bwt`, a theorem declared in [CSLibExt/Bioinformatics/Indexing/BWT.lean, line 543](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Indexing/BWT.lean#L543). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html#invert-bwt).

## FM-index backward search

FM-index backward search: the half-open row interval `[sp, ep)` for a pattern, computed from
the last column alone, processing the pattern from its last letter to its first. The interval for
the suffix and `C[c]` are each computed once per letter, so a pattern of length `m` makes `m`
recursive calls.

Formalized by `Cslib.Bioinformatics.Indexing.BWT.backwardSearch`, a definition declared in [CSLibExt/Bioinformatics/Indexing/BWT.lean, line 553](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Indexing/BWT.lean#L553). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html#backward-search).

## Backward search returns a genuine row interval

Backward search always returns a genuine interval of rows, `sp ≤ ep ≤ |L|`, on any list `L`
(so the difference in `backwardSearch_count` involves no truncated subtraction).

Formalized by `Cslib.Bioinformatics.Indexing.BWT.backwardSearch_bounds`, a theorem declared in [CSLibExt/Bioinformatics/Indexing/BWT.lean, line 687](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Indexing/BWT.lean#L687). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html#backward-search-bounds).

## Backward search is correct

After processing `P`, the interval `[sp, ep)` is exactly the
set of rows whose rotation starts with `P`.

Formalized by `Cslib.Bioinformatics.Indexing.BWT.backwardSearch_spec`, a theorem declared in [CSLibExt/Bioinformatics/Indexing/BWT.lean, line 704](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Indexing/BWT.lean#L704). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html#backward-search-spec).

## Counting occurrences

`ep - sp` is the number of positions `i ≤ |t|` at which `P`
occurs in `t`.

Formalized by `Cslib.Bioinformatics.Indexing.BWT.backwardSearch_count`, a theorem declared in [CSLibExt/Bioinformatics/Indexing/BWT.lean, line 728](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Indexing/BWT.lean#L728). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html#backward-search-count).

## Rotations of `t$` compare as suffixes

For `i, j ≤ |t|`, rotation `i` of `withSentinel t`
is smaller than rotation `j` exactly when suffix `i` is smaller than suffix `j`.

Formalized by `Cslib.Bioinformatics.Indexing.SuffixArrayBWT.rotate_lt_rotate_iff`, a theorem declared in [CSLibExt/Bioinformatics/Indexing/SuffixArrayBWT.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Indexing/SuffixArrayBWT.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html#rotate-lt-rotate-iff).

## The Burrows–Wheeler matrix is the suffix array of `t$`

Sorting the rotations of
`withSentinel t` orders the starting positions exactly as sorting its suffixes.

Formalized by `Cslib.Bioinformatics.Indexing.SuffixArrayBWT.sortedRotations_eq_suffixArray`, a theorem declared in [CSLibExt/Bioinformatics/Indexing/SuffixArrayBWT.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Indexing/SuffixArrayBWT.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html#sorted-rotations-eq-suffix-array).

## The transform from the suffix array

`bwt[r] = t$[SA[r] - 1]`, the letter cyclically
before the suffix of row `r` (the sentinel for the row of the whole text, `SA[r] = 0`).

Formalized by `Cslib.Bioinformatics.Indexing.SuffixArrayBWT.bwt_eq_map_suffixArray`, a theorem declared in [CSLibExt/Bioinformatics/Indexing/SuffixArrayBWT.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Indexing/SuffixArrayBWT.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html#bwt-eq-map-suffix-array).

## Backward-search intervals are suffix-array intervals

Row `r ≤ |t|` lies in the interval
`[sp, ep)` computed by backward search on `bwt t` exactly when `P` is a prefix of the suffix of
`t` at position `SA[r]`.

Formalized by `Cslib.Bioinformatics.Indexing.SuffixArrayBWT.backwardSearch_iff_prefix`, a theorem declared in [CSLibExt/Bioinformatics/Indexing/SuffixArrayBWT.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Indexing/SuffixArrayBWT.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html#backward-search-iff-prefix).

## Occurrences of a pattern reported by the FM-index

The occurrences of `P` reported by the FM-index: the suffix-array entries
`SA[sp], …, SA[ep - 1]` of the backward-search interval. The BWT and the interval are
bound once with `let` and reused, so one query builds the BWT and runs the backward search
once, not three times.

Formalized by `Cslib.Bioinformatics.Indexing.SuffixArrayBWT.occurrences`, a definition declared in [CSLibExt/Bioinformatics/Indexing/SuffixArrayBWT.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Indexing/SuffixArrayBWT.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html#occurrences).

## The reported positions are exactly the occurrences

`i` is reported for `P` exactly when
`i ≤ |t|` and `P` is a prefix of `t.drop i` (the empty pattern occurs at all `|t| + 1`
positions).

Formalized by `Cslib.Bioinformatics.Indexing.SuffixArrayBWT.mem_occurrences_iff`, a theorem declared in [CSLibExt/Bioinformatics/Indexing/SuffixArrayBWT.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Indexing/SuffixArrayBWT.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html#mem-occurrences-iff).

## FM-index reports each occurrence once

Each occurrence is reported once.

Formalized by `Cslib.Bioinformatics.Indexing.SuffixArrayBWT.occurrences_nodup`, a theorem declared in [CSLibExt/Bioinformatics/Indexing/SuffixArrayBWT.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Indexing/SuffixArrayBWT.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html#occurrences-nodup).

## Number of FM-index occurrences equals the interval length

The number of reported positions is the length `ep - sp` of the backward-search interval.

Formalized by `Cslib.Bioinformatics.Indexing.SuffixArrayBWT.occurrences_length`, a theorem declared in [CSLibExt/Bioinformatics/Indexing/SuffixArrayBWT.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Indexing/SuffixArrayBWT.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html#occurrences-length).

## LF in suffix-array terms

For a row `r ≤ |t|`, `LF r` is a row and
`SA[LF r] = SA[r] - 1` cyclically (`SA[LF r] = |t|` when `SA[r] = 0`).

Formalized by `Cslib.Bioinformatics.Indexing.SuffixArrayBWT.suffixArray_getD_lf`, a theorem declared in [CSLibExt/Bioinformatics/Indexing/SuffixArrayBWT.lean, line 339](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Indexing/SuffixArrayBWT.lean#L339). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html#suffix-array-get-d-lf).

## The LF step moves one position left in the text

`SA[r] = SA[LF r] + 1` when
`SA[r] > 0`.

Formalized by `Cslib.Bioinformatics.Indexing.SuffixArrayBWT.suffixArray_getD_eq_lf_add_one`, a theorem declared in [CSLibExt/Bioinformatics/Indexing/SuffixArrayBWT.lean, line 348](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Indexing/SuffixArrayBWT.lean#L348). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html#suffix-array-get-d-eq-lf-add-one).

## Step-bounded sampled-suffix-array locate

`k` steps of sampled-suffix-array locate from row `r`: return the stored value of the first
sampled row reached along the LF-mapping, plus the number of LF steps taken. `sample r` is the
stored value `SA[r]` of row `r`, if any.

Formalized by `Cslib.Bioinformatics.Indexing.SuffixArrayBWT.locateAux`, a definition declared in [CSLibExt/Bioinformatics/Indexing/SuffixArrayBWT.lean, line 362](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Indexing/SuffixArrayBWT.lean#L362). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html#locate-aux).

## Sampled-suffix-array locate

Sampled-suffix-array locate (Ferragina and Manzini 2000): the text position of row `r` from
the last column `L` and the samples, with at most `|L|` LF steps.

Formalized by `Cslib.Bioinformatics.Indexing.SuffixArrayBWT.locate`, a definition declared in [CSLibExt/Bioinformatics/Indexing/SuffixArrayBWT.lean, line 371](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Indexing/SuffixArrayBWT.lean#L371). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html#locate).

## Number of LF steps taken by sampled locate

The number of LF steps `locateAux L sample k r` takes.

Formalized by `Cslib.Bioinformatics.Indexing.SuffixArrayBWT.locateSteps`, a definition declared in [CSLibExt/Bioinformatics/Indexing/SuffixArrayBWT.lean, line 375](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Indexing/SuffixArrayBWT.lean#L375). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html#locate-steps).

## Sampled-suffix-array locate is correct

If every stored value is correct
(`sample r = some v → v = SA[r]` for rows `r ≤ |t|`) and every row of text position `0` is
sampled, then `locate` returns `SA[r]` for every row `r ≤ |t|`.

Formalized by `Cslib.Bioinformatics.Indexing.SuffixArrayBWT.locate_eq`, a theorem declared in [CSLibExt/Bioinformatics/Indexing/SuffixArrayBWT.lean, line 413](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Indexing/SuffixArrayBWT.lean#L413). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html#locate-eq).

## Locate takes at most `s - 1` steps

For `0 < s`, if every row whose text position is
a multiple of `s` is sampled, then from row `r ≤ |t|` locate makes at most `SA[r] mod s` LF
steps (for any amount of fuel `k`). At `s = 0` the `s - 1` bound would be `0` while the
proof only gives `SA[r] mod 0 = SA[r]` steps.

Formalized by `Cslib.Bioinformatics.Indexing.SuffixArrayBWT.locateSteps_le`, a theorem declared in [CSLibExt/Bioinformatics/Indexing/SuffixArrayBWT.lean, line 443](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Indexing/SuffixArrayBWT.lean#L443). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html#locate-steps-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Burrows–Wheeler transform and FM-index](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/string-algorithms/burrows-wheeler-transform-and-fm-index)
