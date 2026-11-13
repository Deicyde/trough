---
declaration: section
origin: cited
lean: MathlibExt.Analysis.RisingSunWanted.Analysis.RisingSun.risingSunSet, MathlibExt.Analysis.RisingSunWanted.Analysis.RisingSun.HasRisingSunDecomposition, MathlibExt.Analysis.RisingSunWanted.Analysis.RisingSun.HasRisingSunProperty, MathlibExt.Analysis.RisingSunWanted.Analysis.RisingSun.rising_sun_lemma
statement: formalized
---

# Rising sun lemma

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/rising-sun-lemma/index.html).

## Rising sun set

For real numbers $a, b$ and a function
$f : \mathbb{R} \to \mathbb{R}$, the rising sun set of $f$ on $(a, b)$ is the set of points
$x \in (a, b)$ for which there is some $t$ with $x < t \le b$ and $f(x) < f(t)$.

Formalized by `MathlibExt.Analysis.RisingSunWanted.Analysis.RisingSun.risingSunSet`, a definition declared in [WantedExt/Analysis/RisingSunWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/RisingSunWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/rising-sun-lemma/index.html#rising-sun-set).

## Rising sun decomposition

A set $E \subseteq \mathbb{R}$ has a rising sun
decomposition for a function $f : \mathbb{R} \to \mathbb{R}$ if there are sequences
$(c_n)_{n \in \mathbb{N}}$ and $(d_n)_{n \in \mathbb{N}}$ of real numbers such that $E$ is the
union of the open intervals $(c_n, d_n)$, these intervals are pairwise disjoint, and
$f(c_n) \le f(d_n)$ for every $n$.

No condition $c_n < d_n$ is imposed, so some of the intervals may be empty.

Formalized by `MathlibExt.Analysis.RisingSunWanted.Analysis.RisingSun.HasRisingSunDecomposition`, a definition declared in [WantedExt/Analysis/RisingSunWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/RisingSunWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/rising-sun-lemma/index.html#has-rising-sun-decomposition).

## Rising sun property

Let $a, b$ be real numbers, let $f : \mathbb{R} \to \mathbb{R}$, and
let $S$ be the rising sun set of $f$ on $(a, b)$. Then $f$ has the rising sun property on
$[a, b]$ if $S$ is open, $S$ is empty if and only if $f$ is antitone (non-increasing) on
$[a, b]$, and, whenever $S$ is nonempty, $S$ has a rising sun decomposition for $f$.

Formalized by `MathlibExt.Analysis.RisingSunWanted.Analysis.RisingSun.HasRisingSunProperty`, a definition declared in [WantedExt/Analysis/RisingSunWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/RisingSunWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/rising-sun-lemma/index.html#has-rising-sun-property).

## Riesz's rising sun lemma

Let $a < b$ be real numbers and let
$f : \mathbb{R} \to \mathbb{R}$ be continuous on $[a, b]$. Then $f$ has the rising sun property
on $[a, b]$.

## Sources

- F. Riesz (1932). Knill, §163. Problem `rising_sun_lemma` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.RisingSunWanted.Analysis.RisingSun.rising_sun_lemma` is written with `theorem_wanted` in [WantedExt/Analysis/RisingSunWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/RisingSunWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/rising-sun-lemma/index.html#rising-sun-lemma).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rising sun lemma](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/rising-sun-lemma/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/real-functions/continuity-and-functional-equations/rising-sun-lemma)
