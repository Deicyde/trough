---
declaration: section
origin: cited
lean: MetaMathlibExt.exists_infinite_finiteSums_monochromatic, MetaMathlibExt.exists_infinite_pairwiseSums_monochromatic, MetaMathlibExt.exists_disjoint_infinite_union_add_monochromatic, MetaMathlibExt.exists_interleaved_sequences_iff_mem_tensor, MetaMathlibExt.weaklyPartitionRegular_iff_exists_ultrafilter, MetaMathlibExt.finiteSums_witness_iff_mem_closure_idempotents, MetaMathlibExt.ramseyWitness_iff_mem_closure_tensor_squares, MetaMathlibExt.pairwiseSums_witness_iff_exists_ramseyWitness
statement: formalized
---

# Pairwise sum theorem

8 results, 8 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/pairwise-sum-theorem/index.html).

## Hindman's finite sums theorem

For every finite coloring of
$\mathbb{N} = \{0, 1, 2, \dots\}$ there is an infinite set $A \subseteq \mathbb{N}$ whose set of
finite sums $\mathrm{FS}(A) = \{\sum_{a \in F} a : F \subseteq A \text{ finite and nonempty}\}$ is
monochromatic.

## Sources

- Mauro Di Nasso and Renling Jin, *From Schur's Theorem to the Pairwise Sum Theorem*, INTEGERS 25 (2025), Article A105, Theorem 1.1.

Stated but not proved: `MetaMathlibExt.exists_infinite_finiteSums_monochromatic` is written with `theorem_wanted` in [WantedExt/Combinatorics/PairwiseSumTheoremWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PairwiseSumTheoremWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/pairwise-sum-theorem/index.html#exists-infinite-finite-sums-monochromati).

## Pairwise sum theorem

For every finite coloring of $\mathbb{N} = \{0, 1, 2, \dots\}$ there
is an infinite set $A \subseteq \mathbb{N}$ such that $A \cup \{a + a' : a, a' \in A, a \ne a'\}$
is monochromatic.

## Sources

- Mauro Di Nasso and Renling Jin, *From Schur's Theorem to the Pairwise Sum Theorem*, INTEGERS 25 (2025), Article A105, Theorem 1.2.

Stated but not proved: `MetaMathlibExt.exists_infinite_pairwiseSums_monochromatic` is written with `theorem_wanted` in [WantedExt/Combinatorics/PairwiseSumTheoremWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PairwiseSumTheoremWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/pairwise-sum-theorem/index.html#exists-infinite-pairwise-sums-monochroma).

## Disjoint infinite sets with monochromatic union and sumset

For every finite coloring of
$\mathbb{N} = \{0, 1, 2, \dots\}$ there are disjoint infinite sets $A, B \subseteq \mathbb{N}$ such
that $A \cup B \cup (A + B)$ is monochromatic, where $A + B = \{a + b : a \in A, b \in B\}$.

## Sources

- Mauro Di Nasso and Renling Jin, *From Schur's Theorem to the Pairwise Sum Theorem*, INTEGERS 25 (2025), Article A105, Theorem 2.2.

Stated but not proved: `MetaMathlibExt.exists_disjoint_infinite_union_add_monochromatic` is written with `theorem_wanted` in [WantedExt/Combinatorics/PairwiseSumTheoremWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PairwiseSumTheoremWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/pairwise-sum-theorem/index.html#exists-disjoint-infinite-union-add-monoc).

## Interleaved sequences and tensor products of ultrafilters

For ultrafilters $U$, $V$ on
$\mathbb{N} = \{0, 1, 2, \dots\}$ and $X \subseteq \mathbb{N} \times \mathbb{N}$, write
$X \in U \otimes V$ when $\{n : \{m : (n, m) \in X\} \in V\} \in U$. For every
$X \subseteq \mathbb{N} \times \mathbb{N}$ the following are equivalent: (1) there are strictly
increasing sequences $(a_i)_{i \in \mathbb{N}}$, $(b_j)_{j \in \mathbb{N}}$ in $\mathbb{N}$ with
disjoint ranges such that $(a_i, b_j) \in X$ whenever $i \le j$ and $(b_j, a_i) \in X$ whenever
$j < i$; (2) there are non-principal ultrafilters $V_1$, $V_2$ on $\mathbb{N}$ with
$X \in V_1 \otimes V_2$ and $X \in V_2 \otimes V_1$.

## Sources

- Mauro Di Nasso and Renling Jin, *From Schur's Theorem to the Pairwise Sum Theorem*, INTEGERS 25 (2025), Article A105, Lemma 2.1.

Stated but not proved: `MetaMathlibExt.exists_interleaved_sequences_iff_mem_tensor` is written with `theorem_wanted` in [WantedExt/Combinatorics/PairwiseSumTheoremWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PairwiseSumTheoremWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/pairwise-sum-theorem/index.html#exists-interleaved-sequences-iff-mem-ten).

## Partition regular families and ultrafilters

Let $\mathcal{F}$ be a family of subsets of a
set $S$. Every finite coloring of $S$ has a monochromatic member of $\mathcal{F}$ (that is,
$\mathcal{F}$ is weakly partition regular) if and only if there is an ultrafilter $U$ on $S$ such
that every $A \in U$ contains some member of $\mathcal{F}$ ($U$ is a PR-witness of $\mathcal{F}$).

## Sources

- Mauro Di Nasso and Renling Jin, *From Schur's Theorem to the Pairwise Sum Theorem*, INTEGERS 25 (2025), Article A105, Proposition 3.1, quoting Hindman and Strauss, Theorem 5.7.

Stated but not proved: `MetaMathlibExt.weaklyPartitionRegular_iff_exists_ultrafilter` is written with `theorem_wanted` in [WantedExt/Combinatorics/PairwiseSumTheoremWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PairwiseSumTheoremWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/pairwise-sum-theorem/index.html#weakly-partition-regular-iff-exists-ultr).

## PR-witnesses of the finite sums family

Let $\beta\mathbb{N}^+$ be the space of
ultrafilters on the positive integers $\mathbb{N}^+$, with the Stone–Čech topology and the sum
for which $A \in U + V$ if and only if $\{n : \{m : n + m \in A\} \in V\} \in U$. For
$X \subseteq \mathbb{N}^+$ let $\mathrm{FS}(X)$ be the set of sums of nonempty finite subsets of
$X$. An ultrafilter $U \in \beta\mathbb{N}^+$ is a PR-witness of the Hindman family, that is,
every $A \in U$ contains $\mathrm{FS}(X)$ for some infinite $X \subseteq \mathbb{N}^+$, if and
only if $U$ lies in the closure of the set of idempotents $\{V \in \beta\mathbb{N}^+ : V + V = V\}$.

## Sources

- Mauro Di Nasso and Renling Jin, *From Schur's Theorem to the Pairwise Sum Theorem*, INTEGERS 25 (2025), Article A105, Proposition 3.3, quoting Hindman and Strauss, Lemma 5.19.

Stated but not proved: `MetaMathlibExt.finiteSums_witness_iff_mem_closure_idempotents` is written with `theorem_wanted` in [WantedExt/Combinatorics/PairwiseSumTheoremWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PairwiseSumTheoremWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/pairwise-sum-theorem/index.html#finite-sums-witness-iff-mem-closure-idem).

## Ramsey's witnesses are the closure of tensor squares

For an ultrafilter $U$ on
$\mathbb{N} = \{0, 1, 2, \dots\}$, the tensor square $U \otimes U$ is the ultrafilter on
$\mathbb{N} \times \mathbb{N}$ whose members are the sets $X$ with
$\{n : \{m : (n, m) \in X\} \in U\} \in U$. An ultrafilter $W$ on $\mathbb{N} \times \mathbb{N}$ is
a Ramsey's witness when every $X \in W$ contains $[H]^2 = \{(h, h') \in H \times H : h < h'\}$ for
some infinite $H \subseteq \mathbb{N}$. An ultrafilter $W$ on $\mathbb{N} \times \mathbb{N}$ is a
Ramsey's witness if and only if $W$ lies in the closure, in the Stone–Čech space
$\beta(\mathbb{N} \times \mathbb{N})$, of the set of tensor squares $U \otimes U$ of non-principal
ultrafilters $U$ on $\mathbb{N}$.

## Sources

- Mauro Di Nasso and Renling Jin, *From Schur's Theorem to the Pairwise Sum Theorem*, INTEGERS 25 (2025), Article A105, Proposition 3.5.

Stated but not proved: `MetaMathlibExt.ramseyWitness_iff_mem_closure_tensor_squares` is written with `theorem_wanted` in [WantedExt/Combinatorics/PairwiseSumTheoremWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PairwiseSumTheoremWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/pairwise-sum-theorem/index.html#ramsey-witness-iff-mem-closure-tensor-sq).

## PR-witnesses of the pairwise sum family

An ultrafilter $W$ on
$\mathbb{N} \times \mathbb{N}$, where $\mathbb{N} = \{0, 1, 2, \dots\}$, is a Ramsey's witness
when every $X \in W$ contains $\{(h, h') \in H \times H : h < h'\}$ for some infinite
$H \subseteq \mathbb{N}$. For an ultrafilter $U$ on $\mathbb{N}$ the following are equivalent:
(1) every $A \in U$ contains an infinite set $B$ together with all sums $b + b'$ of distinct
$b, b' \in B$ ($U$ is a PR-witness of the pairwise sum family); (2) there is a Ramsey's witness
$W$ on $\mathbb{N} \times \mathbb{N}$ whose images under the projections $(a, b) \mapsto a$ and
$(a, b) \mapsto b$ and under the sum map $(a, b) \mapsto a + b$ all equal $U$.

## Sources

- Mauro Di Nasso and Renling Jin, *From Schur's Theorem to the Pairwise Sum Theorem*, INTEGERS 25 (2025), Article A105, Proposition 3.6.

Stated but not proved: `MetaMathlibExt.pairwiseSums_witness_iff_exists_ramseyWitness` is written with `theorem_wanted` in [WantedExt/Combinatorics/PairwiseSumTheoremWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PairwiseSumTheoremWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/pairwise-sum-theorem/index.html#pairwise-sums-witness-iff-exists-ramsey).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pairwise sum theorem](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/pairwise-sum-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/ramsey-theory/structural-ramsey/pairwise-sum-theorem)
