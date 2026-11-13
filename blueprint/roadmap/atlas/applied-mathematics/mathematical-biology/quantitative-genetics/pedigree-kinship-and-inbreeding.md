---
declaration: section
origin: cited
lean: MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree, MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.IsParent, MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.IsAncestor, MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.NoSelfing, MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.Coins, MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.origin, MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.ibd, MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.geneDropKinship
statement: formalized
proof: formalized
---

# Pedigree kinship and inbreeding

44 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html).

## Pedigree

A pedigree on the individuals `Fin n`, numbered so that parents precede their children
(every finite pedigree, a finite DAG, has such a numbering). `parents i = some g` means that
`g 0` is the father and `g 1` the mother of `i`; `parents i = none` means that `i` is a founder.
Founders are unrelated and not inbred (their `2 n_F` gene copies are distinct).

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree`, a structure declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#pedigree).

## Parent relation in a pedigree

`a` is a parent of `b`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.IsParent`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#is-parent).

## Ancestor relation in a pedigree

`a` is an ancestor of `b` (a parent, a parent of a parent, …).

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.IsAncestor`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#is-ancestor).

## Pedigree without selfing

No individual is the offspring of a selfing (father ≠ mother), as in Wright's setting of a
bisexual population.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.NoSelfing`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#no-selfing).

## Gene-dropping outcome

A gene-dropping outcome: `ω i k` is the Mendelian coin of the copy `(i, k)` (`k = 0` the
paternal copy, `k = 1` the maternal copy), saying which copy (`0` or `1`) of the parent `g k`
of `i` it inherits. Under gene dropping all `4 ^ n` outcomes are equally likely.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.Coins`, an abbreviation declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#coins).

## Founder origin of a gene copy

The founder copy from which the gene copy `c = (i, k)` descends under the gene-dropping
outcome `ω`: a founder copy is its own origin; a copy of a non-founder descends from the copy
`ω i k` of its parent `g k`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.origin`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#origin).

## Probability of identity by descent under gene dropping

The probability, under gene dropping (independent fair Mendelian coins), that the gene
copies `c` and `d` are identical by descent, i.e. descend from the same founder copy.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.ibd`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#ibd).

## Kinship coefficient under gene dropping

The kinship (coancestry) coefficient under gene dropping: the probability that a copy drawn
at random from `i` and a copy drawn at random from `j` are identical by descent.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.geneDropKinship`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#gene-drop-kinship).

## Inbreeding coefficient under gene dropping

The inbreeding coefficient under gene dropping: the probability that the two copies of `i`
are identical by descent.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.inbreeding`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#inbreeding).

## Kinship coefficient by Malécot's recursion

The kinship coefficient by Malécot's recursion, computed in the order of the numbering
(the tabular method): for `i < j`, `φ i j = (φ i f + φ i m) / 2` with `f, m` the parents of `j`
and `φ i j = 0` if `j` is a founder; `φ i i = (1 + φ f m) / 2` with `f, m` the parents of `i`
and `φ i i = 1 / 2` for a founder; symmetric for `j < i`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.kinship`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#kinship).

## Inbreeding coefficient by Malécot's recursion

The inbreeding coefficient by Malécot's recursion: `F i = φ f m` for the parents `f, m` of
`i`, and `F i = 0` for a founder.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.kinshipInbreeding`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#kinship-inbreeding).

## Tabular kinship when the second individual is a later non-founder

The tabular recursion for `i < j` with `j` a non-founder.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.kinship_of_lt_of_parents_eq_some`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#kinship-of-lt-of-parents-eq-some).

## Tabular kinship when the second individual is a later founder

The tabular recursion for `i < j` with `j` a founder.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.kinship_of_lt_of_parents_eq_none`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#kinship-of-lt-of-parents-eq-none).

## Tabular self-kinship of a non-founder

The tabular recursion on the diagonal for a non-founder: `φ i i = (1 + φ f m) / 2`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.kinship_self_of_parents_eq_some`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#kinship-self-of-parents-eq-some).

## Tabular self-kinship of a founder

The tabular recursion on the diagonal for a founder: `φ i i = 1 / 2`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.kinship_self_of_parents_eq_none`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#kinship-self-of-parents-eq-none).

## Tabular kinship when the first individual is a later non-founder

The tabular recursion for `j < i` with `i` a non-founder.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.kinship_of_gt_of_parents_eq_some`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#kinship-of-gt-of-parents-eq-some).

## Tabular kinship when the first individual is a later founder

The tabular recursion for `j < i` with `i` a founder.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.kinship_of_gt_of_parents_eq_none`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#kinship-of-gt-of-parents-eq-none).

## Symmetry of tabular kinship

The tabular kinship is symmetric.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.kinship_comm`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#kinship-comm).

## Ancestral paths from an individual

The ancestral paths from `i`: the lists `[i = v₀, v₁, …, v_k]` with each `v_{t+1}` a parent
of `v_t` (`k ≥ 0`; the path `[i]` has no edge).

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.ancPaths`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#anc-paths).

## Ancestral paths ending at a given ancestor

The ancestral paths from `i` that end at `A`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.pathsTo`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#paths-to).

## Ancestral paths are nonempty with the starting individual as head

Every path in `ancPaths i` starts at `i` and is nonempty.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.head?_of_mem_ancPaths`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#head-of-mem-anc-paths).

## A founder gene copy is its own origin

A founder copy is its own origin.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.origin_of_parents_eq_none`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#origin-of-parents-eq-none).

## Origin of a gene copy of a non-founder

A copy of a non-founder descends from the chosen copy of the corresponding parent.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.origin_of_parents_eq_some`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#origin-of-parents-eq-some).

## Ancestors precede their descendants

Ancestors precede their descendants.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.IsAncestor.lt`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#lt).

## Parents are ancestors

A parent is an ancestor.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.isAncestor_of_parents_eq_some`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#is-ancestor-of-parents-eq-some).

## A gene copy is identical by descent with itself

Two copies are identical by descent of themselves with probability `1`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.ibd_self`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 377](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L377). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#ibd-self).

## Symmetry of identity by descent

Identity by descent is symmetric.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.ibd_comm`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 384](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L384). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#ibd-comm).

## Malécot's recursion step for identity by descent

One step of Malécot's recursion for identity by descent.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.ibd_of_parents_eq_some`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 388](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L388). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#ibd-of-parents-eq-some).

## Self-kinship under gene dropping

`φ i i = (1 + F i) / 2` under gene dropping.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.geneDropKinship_self`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 413](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L413). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#gene-drop-kinship-self).

## Founders are not inbred

The inbreeding coefficient of a founder is `0`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.inbreeding_of_parents_eq_none`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 419](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L419). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#inbreeding-of-parents-eq-none).

## Malécot

The inbreeding coefficient of `i` is the kinship of its parents,
`F i = φ f m`, under gene dropping.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.inbreeding_of_parents_eq_some`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 428](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L428). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#inbreeding-of-parents-eq-some).

## Malécot's recursion

**Malécot's recursion** under gene dropping: if `j ≠ i` is not an ancestor of `i` and has
parents `f, m`, then `φ i j = (φ i f + φ i m) / 2`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.geneDropKinship_of_parents_eq_some`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 481](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L481). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#gene-drop-kinship-of-parents-eq-some).

## Zero kinship with an unrelated founder

A founder `j ≠ i` that is not an ancestor of `i` has kinship `0` with `i`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.geneDropKinship_of_parents_eq_none`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 488](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L488). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#gene-drop-kinship-of-parents-eq-none).

## Symmetry of gene-dropping kinship

Gene-dropping kinship is symmetric.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.geneDropKinship_comm`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 504](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L504). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#gene-drop-kinship-comm).

## Malécot's recursion computes gene-dropping kinship

The kinship coefficient computed by Malécot's recursion is the probability of identity by
descent under gene dropping.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.geneDropKinship_eq_kinship`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 510](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L510). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#gene-drop-kinship-eq-kinship).

## Malécot's recursion computes the inbreeding coefficient

The inbreeding coefficient computed by Malécot's recursion is the probability of identity
by descent of the two copies of `i` under gene dropping.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.inbreeding_eq_kinshipInbreeding`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 553](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L553). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#inbreeding-eq-kinship-inbreeding).

## Ancestral paths from a founder

The only ancestral path from a founder is `[i]`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.mem_ancPaths_of_parents_eq_none`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 563](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L563). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#mem-anc-paths-of-parents-eq-none).

## Ancestral paths from a non-founder

The ancestral paths from a non-founder: `[i]` and `i :: q` for a path `q` from a parent.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.mem_ancPaths_of_parents_eq_some`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 568](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L568). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#mem-anc-paths-of-parents-eq-some).

## Individuals on an ancestral path are its start or precede it

Every individual on an ancestral path from `i` is `i` or precedes it.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.le_of_mem_ancPaths`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 587](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L587). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#le-of-mem-anc-paths).

## Ancestral path as its start followed by a tail

Every ancestral path from `i` starts with `i`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.exists_eq_cons_of_mem_ancPaths`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 603](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L603). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#exists-eq-cons-of-mem-anc-paths).

## An ancestral path returning to its start is trivial

A path from `i` ending at `i` is `[i]`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.eq_singleton_of_mem_ancPaths`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 613](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L613). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#eq-singleton-of-mem-anc-paths).

## Trivial ancestral path

`[i]` is an ancestral path from `i`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.singleton_mem_ancPaths`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 717](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L717). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#singleton-mem-anc-paths).

## Wright's path formula

**Wright's path formula** in kinship form: `φ i j` is the sum, over common ancestors `A`
(including `i` or `j` themselves) and pairs of ancestral paths `p` from `i` to `A` and `p'` from
`j` to `A` that share no individual other than `A`, of `(1/2) ^ (n₁ + n₂ + 1) * (1 + F A)`,
where `n₁ + n₂ + 1 = p.length + p'.length - 1` is the number of individuals on the loop.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.kinship_eq_sum_paths`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 818](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L818). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#kinship-eq-sum-paths).

## Wright's path formula

**Wright's path formula** for the inbreeding coefficient (Wright 1922): if `i` has parents
`f = g 0` and `m = g 1`, then `F_i = Σ (1/2) ^ (n₁ + n₂ + 1) (1 + F_A)` over common ancestors `A`
of `f` and `m` (including `f` or `m` themselves) and pairs of ancestral paths from `f` and `m`
to `A` (with `n₁` and `n₂` edges) that share only `A`. Here `F` is the gene-dropping inbreeding
coefficient.

Formalized by `MathlibExt.Biology.StatisticalGenetics.Kinship.Pedigree.inbreeding_eq_sum_paths`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/Kinship.lean, line 831](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/Kinship.lean#L831). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html#inbreeding-eq-sum-paths).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pedigree kinship and inbreeding](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/quantitative-genetics/pedigree-kinship-and-inbreeding)
