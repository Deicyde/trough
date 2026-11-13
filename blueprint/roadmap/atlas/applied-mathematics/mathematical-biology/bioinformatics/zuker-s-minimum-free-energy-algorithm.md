---
declaration: section
origin: cited
lean: Cslib.Bioinformatics.RNA.Zuker.LoopEnergy, Cslib.Bioinformatics.RNA.Zuker.Encloses, Cslib.Bioinformatics.RNA.Zuker.branches, Cslib.Bioinformatics.RNA.Zuker.exteriorBranches, Cslib.Bioinformatics.RNA.Zuker.existsUnique_closing_pair, Cslib.Bioinformatics.RNA.Zuker.loopEnergy, Cslib.Bioinformatics.RNA.Zuker.freeEnergy, Cslib.Bioinformatics.RNA.Zuker.loopEnergy_eq_hairpin
statement: formalized
proof: formalized
---

# Zuker's minimum free energy algorithm

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/zuker-s-minimum-free-energy-algorithm/index.html).

## Nearest-neighbor loop energy model

A loop (nearest-neighbor) energy model: energies of hairpin loops closed by `(i, j)`, of
stacks, bulges and interior loops closed by `(i, j)` with inner pair `(k, l)`, and the affine
multiloop parameters `a` (per multiloop), `b` (per branch) and `c` (per unpaired base). The
exterior loop has energy `0`. Units: free energy, e.g. kcal/mol.

Formalized by `Cslib.Bioinformatics.RNA.Zuker.LoopEnergy`, a structure declared in [CSLibExt/Bioinformatics/RNA/Zuker.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/Zuker.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/zuker-s-minimum-free-energy-algorithm/index.html#loop-energy).

## Strict enclosure of one base pair by another

`q` lies strictly inside the pair `p`: `p.1 < q.1` and `q.2 < p.2`.

Formalized by `Cslib.Bioinformatics.RNA.Zuker.Encloses`, a definition declared in [CSLibExt/Bioinformatics/RNA/Zuker.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/Zuker.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/zuker-s-minimum-free-energy-algorithm/index.html#encloses).

## Branches of a loop closed by a base pair

The branches of the loop closed by `p` in `P`: the pairs of `P` strictly inside `p` that
are not strictly inside another pair of `P` strictly inside `p`.

Formalized by `Cslib.Bioinformatics.RNA.Zuker.branches`, a definition declared in [CSLibExt/Bioinformatics/RNA/Zuker.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/Zuker.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/zuker-s-minimum-free-energy-algorithm/index.html#branches).

## Exterior branches of a secondary structure

The exterior branches of `P`: the pairs not strictly inside any pair of `P`.

Formalized by `Cslib.Bioinformatics.RNA.Zuker.exteriorBranches`, a definition declared in [CSLibExt/Bioinformatics/RNA/Zuker.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/Zuker.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/zuker-s-minimum-free-energy-algorithm/index.html#exterior-branches).

## Unique loop decomposition

In a secondary structure every pair is either an exterior
branch or a branch of exactly one pair of the structure (and not both): each pair is shared by
the loop it closes and exactly one enclosing loop, possibly the exterior loop.

Formalized by `Cslib.Bioinformatics.RNA.Zuker.existsUnique_closing_pair`, a theorem declared in [CSLibExt/Bioinformatics/RNA/Zuker.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/Zuker.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/zuker-s-minimum-free-energy-algorithm/index.html#exists-unique-closing-pair).

## Energy of the loop closed by a base pair

The energy of the loop closed by `p = (i, j)` in `P`: a hairpin with no branch, a stack,
bulge or interior loop with one branch `(k, l)`, and the affine multiloop energy
`a + b · r + c · u` with `r ≥ 2` branches and `u = (j - i - 1) - ∑ (l - k + 1)` unpaired
bases.

Formalized by `Cslib.Bioinformatics.RNA.Zuker.loopEnergy`, a definition declared in [CSLibExt/Bioinformatics/RNA/Zuker.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/Zuker.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/zuker-s-minimum-free-energy-algorithm/index.html#loop-energy-2).

## Free energy of a structure in the loop model

The free energy of a structure in the loop model: the sum of the energies of the loops
closed by its pairs (the exterior loop contributes `0`).

Formalized by `Cslib.Bioinformatics.RNA.Zuker.freeEnergy`, a definition declared in [CSLibExt/Bioinformatics/RNA/Zuker.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/Zuker.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/zuker-s-minimum-free-energy-algorithm/index.html#free-energy).

## A pair with no branch closes a hairpin loop

A pair with no branch closes a hairpin loop.

Formalized by `Cslib.Bioinformatics.RNA.Zuker.loopEnergy_eq_hairpin`, a theorem declared in [CSLibExt/Bioinformatics/RNA/Zuker.lean, line 319](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/Zuker.lean#L319). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/zuker-s-minimum-free-energy-algorithm/index.html#loop-energy-eq-hairpin).

## A pair with one branch closes a stack, bulge or interior loop

A pair with exactly one branch `q` closes a stack, bulge or interior loop with inner pair
`q`.

Formalized by `Cslib.Bioinformatics.RNA.Zuker.loopEnergy_eq_interior`, a theorem declared in [CSLibExt/Bioinformatics/RNA/Zuker.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/Zuker.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/zuker-s-minimum-free-energy-algorithm/index.html#loop-energy-eq-interior).

## A pair with two or more branches closes a multiloop

A pair with at least two branches closes a multiloop with the affine energy.

Formalized by `Cslib.Bioinformatics.RNA.Zuker.loopEnergy_eq_multiloop`, a theorem declared in [CSLibExt/Bioinformatics/RNA/Zuker.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/Zuker.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/zuker-s-minimum-free-energy-algorithm/index.html#loop-energy-eq-multiloop).

## Every position has a unique innermost strict container

**Every position has a unique innermost strict container** (not loop membership): a
position `x` either lies strictly inside no pair, or there is a unique pair `p` with
`p.1 < x < p.2` such that no branch of `p` has `x` strictly inside it. This is an
innermost-container assignment, not the conventional loop decomposition of positions:
endpoints are excluded from the loop they close (a position `x = q.1` or `x = q.2` is
assigned to the loop of which `q` is a branch, never to the loop closed by `q`), and no
`x < s.length` hypothesis is assumed, so positions outside the sequence fall in the
first (exterior) case. In particular do not read this as saying loops uniquely decompose
positions; see `existsUnique_closing_pair` for the closing-pair side of the convention.

Formalized by `Cslib.Bioinformatics.RNA.Zuker.existsUnique_loop_of_pos`, a theorem declared in [CSLibExt/Bioinformatics/RNA/Zuker.lean, line 502](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/Zuker.lean#L502). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/zuker-s-minimum-free-energy-algorithm/index.html#exists-unique-loop-of-pos).

## Zuker's recursion

**Zuker's recursion** on the interval `[i, i + len)`, with `j = i + len - 1`, returning
`(V, WM)`:
* `V = ⊤` unless `(i, j)` can close a loop (`i + m < j`, `CanPair pair s i j`); otherwise `V` is
  the least of the hairpin energy `hairpin i j`, the interior-loop energies
  `interior i j k l + V(k, l)` over `i < k < l < j`, and the multiloop energies
  `a + WM(i + 1, u) + WM(u + 1, j - 1)` over `i < u < j - 1`;
* `WM` (a multiloop fragment with at least one branch, charging `b` per branch and `c` per
  unpaired base) is the least of `V + b`, `WM(i + 1, j) + c` (base `i` unpaired),
  `WM(i, j - 1) + c` (base `j` unpaired) and `WM(i, u) + WM(u + 1, j)` over `i ≤ u < j`.
Intervals are written by start and length.

Formalized by `Cslib.Bioinformatics.RNA.Zuker.zukerVW`, a definition declared in [CSLibExt/Bioinformatics/RNA/Zuker.lean, line 823](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/Zuker.lean#L823). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/zuker-s-minimum-free-energy-algorithm/index.html#zuker-vw).

## Zuker exterior-loop recursion

The exterior-loop recursion on the prefix `[0, len)`: `W(0) = 0` and
`W(len + 1) = min (W(len), min_{i ≤ len} W(i) + V(i, len + 1 - i))` (the last base is unpaired,
or closes an exterior branch `(i, len)`).

Formalized by `Cslib.Bioinformatics.RNA.Zuker.zukerExterior`, a definition declared in [CSLibExt/Bioinformatics/RNA/Zuker.lean, line 857](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/Zuker.lean#L857). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/zuker-s-minimum-free-energy-algorithm/index.html#zuker-exterior).

## Zuker minimum free energy

Zuker's minimum free energy of `s`: the exterior recursion on the whole sequence.

Formalized by `Cslib.Bioinformatics.RNA.Zuker.zukerMFE`, a definition declared in [CSLibExt/Bioinformatics/RNA/Zuker.lean, line 867](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/Zuker.lean#L867). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/zuker-s-minimum-free-energy-algorithm/index.html#zuker-mfe).

## Zuker's algorithm

**Zuker's algorithm** (Zuker and Stiegler 1981; Zuker and Sankoff 1984), here with the affine
multiloop energy of Jaeger, Turner and Zuker (1989): the Zuker recursion computes the minimum
free energy over all secondary structures on `s` with minimum hairpin `m`, for any real loop
energies (of either sign). The minimum ranges over a finite set that contains the empty
structure, so it is never `⊤`.

Formalized by `Cslib.Bioinformatics.RNA.Zuker.zukerMFE_eq_inf`, a theorem declared in [CSLibExt/Bioinformatics/RNA/Zuker.lean, line 1298](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/Zuker.lean#L1298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/zuker-s-minimum-free-energy-algorithm/index.html#zuker-mfe-eq-inf).

## Minimum free energy is at most zero

The minimum free energy is at most `0`, the energy of the open chain (the empty
structure).

Formalized by `Cslib.Bioinformatics.RNA.Zuker.zukerMFE_le_zero`, a theorem declared in [CSLibExt/Bioinformatics/RNA/Zuker.lean, line 1305](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/Zuker.lean#L1305). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/zuker-s-minimum-free-energy-algorithm/index.html#zuker-mfe-le-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Zuker's minimum free energy algorithm](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/zuker-s-minimum-free-energy-algorithm/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/bioinformatics/zuker-s-minimum-free-energy-algorithm)
