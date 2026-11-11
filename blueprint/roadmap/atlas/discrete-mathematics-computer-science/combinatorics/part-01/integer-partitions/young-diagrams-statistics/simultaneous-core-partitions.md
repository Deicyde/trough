---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.SimultaneousCoreContainmentOWR1265Problem006Wanted.IsCore, MathlibExt.Combinatorics.SimultaneousCoreContainmentOWR1265Problem006Wanted.simultaneousCoreContainment, MathlibExt.Combinatorics.SimultaneousCoreContainmentOWR1265Problem006Wanted.simultaneousCoreContainment_holds
statement: formalized
---

# Simultaneous core partitions

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/simultaneous-core-partitions/index.html).

## $s$-cores of Young diagrams

Let $s$ be a natural number and $\mu$ a Young diagram, with
rows and columns numbered from $0$; write $r_i$ for the length of row $i$ of $\mu$ and $c_j$ for
the length of column $j$ of $\mu$. The hook length of the cell $(i, j)$ of $\mu$ (row $i$, column
$j$) is $(r_i - j) + (c_j - i) - 1$: the cells to its right in row $i$, the cells below it in
column $j$, and the cell itself (both differences count the cell, so one is subtracted). The
diagram $\mu$ is an *$s$-core* if no cell of $\mu$ has hook length divisible by $s$.

Formalized by `MathlibExt.Combinatorics.SimultaneousCoreContainmentOWR1265Problem006Wanted.IsCore`, a definition declared in [WantedExt/Combinatorics/SimultaneousCoreContainmentOWR1265Problem006Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SimultaneousCoreContainmentOWR1265Problem006Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/simultaneous-core-partitions/index.html#is-core).

## Containment of simultaneous cores (Olsson–Stanton question)

The proposition that for all
coprime positive integers $s$ and $t$ and every Young diagram $\kappa$ that is both an $s$-core and
a $t$-core and has at least as many cells as every Young diagram that is both an $s$-core and a
$t$-core, every Young diagram that is both an $s$-core and a $t$-core is contained in $\kappa$,
that is, each of its cells is a cell of $\kappa$.

The proposition does not assert that such a $\kappa$ exists. In the report, $\kappa_{s,t}$ is the
partition of maximum size that is both an $s$-core and a $t$-core, and the question is whether
the Young diagram of every such partition is contained in that of $\kappa_{s,t}$.

Formalized by `MathlibExt.Combinatorics.SimultaneousCoreContainmentOWR1265Problem006Wanted.simultaneousCoreContainment`, a definition declared in [WantedExt/Combinatorics/SimultaneousCoreContainmentOWR1265Problem006Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SimultaneousCoreContainmentOWR1265Problem006Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/simultaneous-core-partitions/index.html#simultaneous-core-containment).

## Fayers–Vandehey containment theorem for simultaneous cores

Call a Young diagram an
$s$-core when none of its cells has hook length divisible by $s$. For all coprime positive
integers $s$ and $t$, if $\kappa$ is a Young diagram that is both an $s$-core and a $t$-core and
has at least as many cells as every Young diagram that is both an $s$-core and a $t$-core, then
every Young diagram that is both an $s$-core and a $t$-core is contained in $\kappa$ (each of its
cells is a cell of $\kappa$).

Fayers (Theorem 5.1, first proved by Vandehey) shows that for coprime positive integers $s$ and
$t$ every simultaneous $s$- and $t$-core is contained in $\kappa_{s,t}$, the simultaneous core of
the largest size $(s^2 - 1)(t^2 - 1)/24$, answering the question of Olsson and Stanton. A
simultaneous core $\kappa$ of maximum size is then contained in $\kappa_{s,t}$ and has at least as
many cells, so it equals $\kappa_{s,t}$ and contains every simultaneous core.

## Sources

- J. B. Olsson (joint with D. Stanton, C. Bessenrodt, G. Navarro, P. H. Tiep), On block identities and block inclusions, in Representations of Finite Groups, Oberwolfach Reports 3 (2006), no. 15, p. 912 ff., section 2 (Block identities), DOI 10.4171/OWR/2006/15; resolution: M. Fayers, The t-core of an s-core, J. Combin. Theory Ser. A 118 (2011), 1525-1539, DOI 10.1016/j.jcta.2011.01.004, arXiv:1007.1071, Section 5, Theorem 5.1 ("Suppose s and t are coprime positive integers, and λ is an (s, t)-core. Then [λ] ⊆ [κ_{s,t}]"), proved in Proposition 5.5; Fayers cites the first proof as J. Vandehey, Containment in (s, t)-core partitions, arXiv:0809.2134, Theorem 2.4, https://arxiv.org/abs/1007.1071.

Stated but not proved: `MathlibExt.Combinatorics.SimultaneousCoreContainmentOWR1265Problem006Wanted.simultaneousCoreContainment_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/SimultaneousCoreContainmentOWR1265Problem006Wanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SimultaneousCoreContainmentOWR1265Problem006Wanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/simultaneous-core-partitions/index.html#simultaneous-core-containment-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Simultaneous core partitions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/simultaneous-core-partitions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/simultaneous-core-partitions)
