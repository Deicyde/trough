---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Series.ScottishBook5BoundedWanted.HasDensityOne, MathlibExt.Analysis.Series.ScottishBook5BoundedWanted.AsymptoticallyConvergent, MathlibExt.Analysis.Series.ScottishBook5BoundedWanted.MatrixSums, MathlibExt.Analysis.Series.ScottishBook5BoundedWanted.IsPermanent, MathlibExt.Analysis.Series.ScottishBook5BoundedWanted.IsBounded, MathlibExt.Analysis.Series.ScottishBook5BoundedWanted.ScottishBookProblem5Claim, MathlibExt.Analysis.Series.ScottishBook5BoundedWanted.mazur5BoundedRefuted
statement: formalized
---

# Permanent summability methods

7 results, 6 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/summability/permanent-summability-methods/index.html).

## Index sequences of density one

A sequence $s \colon \mathbb{N} \to \mathbb{N}$ has
density one when it is strictly increasing and $s(n+1)/(n+1) \to 1$ as $n \to \infty$.

For a strictly increasing sequence of natural numbers this ratio condition is equivalent to the
usual counting definition of density $1$ for its set of values.

Formalized by `MathlibExt.Analysis.Series.ScottishBook5BoundedWanted.HasDensityOne`, a definition declared in [WantedExt/Analysis/Series/ScottishBook5BoundedWanted.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Series/ScottishBook5BoundedWanted.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/summability/permanent-summability-methods/index.html#has-density-one).

## Asymptotically convergent sequences

A real sequence $(x_n)_{n \in \mathbb{N}}$ is
asymptotically convergent to a real number $S$ when there is an index sequence $s$ of density
one such that $x_{s(n)} \to S$ as $n \to \infty$.

## Sources

- this is the typescript's definition, verbatim in content.

Formalized by `MathlibExt.Analysis.Series.ScottishBook5BoundedWanted.AsymptoticallyConvergent`, a definition declared in [WantedExt/Analysis/Series/ScottishBook5BoundedWanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Series/ScottishBook5BoundedWanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/summability/permanent-summability-methods/index.html#asymptotically-convergent).

## Summation by a matrix method

A real matrix $(a_{ik})_{i,k \in \mathbb{N}}$ sums a real
sequence $(x_k)_{k \in \mathbb{N}}$ to a real number $S$ when for every row $i$ the series
$\sum_k a_{ik} x_k$ converges unconditionally (equivalently, absolutely) and the row sums
$\sum_k a_{ik} x_k$ tend to $S$ as $i \to \infty$.

Formalized by `MathlibExt.Analysis.Series.ScottishBook5BoundedWanted.MatrixSums`, a definition declared in [WantedExt/Analysis/Series/ScottishBook5BoundedWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Series/ScottishBook5BoundedWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/summability/permanent-summability-methods/index.html#matrix-sums).

## Permanent matrix methods

A real matrix $(a_{ik})_{i,k \in \mathbb{N}}$ is a permanent
(regular, or Toeplitz) method when it sums every convergent real sequence to its limit: for every
real sequence $x$ and real number $S$ with $x_n \to S$, the matrix sums $x$ to $S$.

The Silverman–Toeplitz conditions characterise exactly these methods.

## Sources

- "Toeplitz method" is pinned to this standard reading; the typescript does not define it.

Formalized by `MathlibExt.Analysis.Series.ScottishBook5BoundedWanted.IsPermanent`, a definition declared in [WantedExt/Analysis/Series/ScottishBook5BoundedWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Series/ScottishBook5BoundedWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/summability/permanent-summability-methods/index.html#is-permanent).

## Bounded sequences

A real sequence $(x_n)_{n \in \mathbb{N}}$ is bounded when there is a
real number $B$ with $|x_n| \le B$ for all $n$.

Formalized by `MathlibExt.Analysis.Series.ScottishBook5BoundedWanted.IsBounded`, a definition declared in [WantedExt/Analysis/Series/ScottishBook5BoundedWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Series/ScottishBook5BoundedWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/summability/permanent-summability-methods/index.html#is-bounded).

## The bounded case of Scottish Book Problem 5

There is a real matrix
$(a_{ik})_{i,k \in \mathbb{N}}$ that is a permanent matrix method such that for every bounded real
sequence $x$ and every real number $S$, the matrix sums $x$ to $S$ if and only if $x$ is
asymptotically convergent to $S$.

Formalized by `MathlibExt.Analysis.Series.ScottishBook5BoundedWanted.ScottishBookProblem5Claim`, a definition declared in [WantedExt/Analysis/Series/ScottishBook5BoundedWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Series/ScottishBook5BoundedWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/summability/permanent-summability-methods/index.html#scottish-book-problem5-claim).

## Negative answer to Scottish Book Problem 5 for bounded sequences

There is no real matrix
$(a_{ik})_{i,k \in \mathbb{N}}$ that is a permanent matrix method such that for every bounded real
sequence $x$ and every real number $S$, the matrix sums $x$ to $S$ if and only if $x$ is
asymptotically convergent to $S$.

## Sources

- the typescript itself, Ad 5 (Mazur), PDF p.5 / printed p.2, verified against the typescript page. Ad 5 (2) states verbatim: "If a method (a_{ik}) sums all the convergent sequences and every bounded sequence summable by the sequence [sic — the method] is asymptotically convergent, then there exists a sequence of increasing integers {kₙ} with density 1, such that for every bounded sequence {ξₙ} summable by this method, the sequence {ξ_{kₙ}} is convergent." The typescript then draws the corollary verbatim: "from (2) it follows that a permanent method summing all bounded asymptotically convergent sequences must also sum some other bounded sequences" — i.e. no permanent method sums exactly the bounded asymptotically convergent sequences, which refutes the equivalence formalized in `ScottishBookProblem5Claim`. Proof sketch of the corollary from (2): suppose a permanent method `a` summed exactly the bounded asymptotically convergent sequences (to the right limits). Then `a` satisfies both hypotheses of (2) (permanent, and every bounded `a`-summable sequence is asymptotically convergent, by the assumed equivalence), so (2) gives a fixed density-1 sequence {kₙ} along which every bounded `a`-summable sequence converges. Let J = ℕ ∖ {k_{m²} : m ∈ ℕ}; J has density 1 (since k_{m²} ≥ m², the excluded set has density 0), and let ξ be 0 on J and 1 elsewhere. Then ξ is bounded and asymptotically convergent to 0 (via J), so `a` sums ξ to 0; but ξ_{kₙ} equals 1 when n is a square and 0 otherwise, so it diverges — contradicting (2). (Cesàro does not satisfy (2)'s hypothesis — e.g. (-1)^n is Cesàro-summable but not asymptotically convergent — so it is not a counterexample to (2).) Note: the earlier Phase 3c entry recorded only that Ad 5 (1) does not settle the bounded question; Ad 5 (2) and its corollary do.

Stated but not proved: `MathlibExt.Analysis.Series.ScottishBook5BoundedWanted.mazur5BoundedRefuted` is written with `theorem_wanted` in [WantedExt/Analysis/Series/ScottishBook5BoundedWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Series/ScottishBook5BoundedWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/summability/permanent-summability-methods/index.html#mazur5-bounded-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Permanent summability methods](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/summability/permanent-summability-methods/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/sequences-and-series/summability/permanent-summability-methods)
