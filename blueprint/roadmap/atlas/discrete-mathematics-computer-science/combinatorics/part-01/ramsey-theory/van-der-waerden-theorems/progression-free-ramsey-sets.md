---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ProgressionFreeRamseySetErdosProblem966Wanted.progressionFreeRamseySet, MathlibExt.Combinatorics.ProgressionFreeRamseySetErdosProblem966Wanted.progressionFreeRamseySet_holds
statement: formalized
---

# Progression-free Ramsey sets

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/progression-free-ramsey-sets/index.html).

## Erdős Problem 966: progression-free sets that are Ramsey for shorter progressions

This
is the statement that for all natural numbers $k \ge 2$ and $r \ge 2$ there is a set $A$ of
natural numbers that contains no arithmetic progression of $k + 1$ distinct terms and such that
for every colouring $c$ of the natural numbers with $r$ colours there are a subset
$t \subseteq A$ that is an arithmetic progression of $k$ distinct terms and a colour $i$ with
$c(x) = i$ for every $x \in t$.

Only the colours of elements of $A$ matter, so the colouring condition says that every
colouring of $A$ with $r$ colours has a monochromatic progression of $k$ distinct terms.

Formalized by `MathlibExt.Combinatorics.ProgressionFreeRamseySetErdosProblem966Wanted.progressionFreeRamseySet`, a definition declared in [WantedExt/Combinatorics/ProgressionFreeRamseySetErdosProblem966Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ProgressionFreeRamseySetErdosProblem966Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/progression-free-ramsey-sets/index.html#progression-free-ramsey-set).

## Erdős Problem 966 holds

For all natural numbers $k \ge 2$ and $r \ge 2$ there is a set $A$
of natural numbers that contains no arithmetic progression of $k + 1$ distinct terms and such
that for every colouring $c$ of the natural numbers with $r$ colours there are a subset
$t \subseteq A$ that is an arithmetic progression of $k$ distinct terms and a colour $i$ with
$c(x) = i$ for every $x \in t$.

## Sources

- T. F. Bloom, Erdős Problems, Problem #966, https://www.erdosproblems.com/966 (status PROVED (LEAN)); resolution: formal proof linked from erdosproblems.com/966 (found with Aristotle, posted in the comment thread); P. Erdős, Problems and results in combinatorial number theory (1975), 295-310, reports that Spencer had shown that such a sequence exists, erdosproblems.com/966 status 'proved (Lean)'; formal proof cited by formal-conjectures, https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos966.lean.

Stated but not proved: `MathlibExt.Combinatorics.ProgressionFreeRamseySetErdosProblem966Wanted.progressionFreeRamseySet_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/ProgressionFreeRamseySetErdosProblem966Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ProgressionFreeRamseySetErdosProblem966Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/progression-free-ramsey-sets/index.html#progression-free-ramsey-set-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Progression-free Ramsey sets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/progression-free-ramsey-sets/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/progression-free-ramsey-sets)
