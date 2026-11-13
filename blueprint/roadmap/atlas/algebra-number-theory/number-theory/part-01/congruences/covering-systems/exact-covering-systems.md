---
declaration: section
origin: cited
lean: Int.indexedCoverMultiplicity, Int.IsExactCoverOf, MetaMathlibExt.fraenkel_exact_M_cover_bernoulli_recurrence_general, MetaMathlibExt.fraenkel_exact_M_cover_bernoulli_recurrence
statement: formalized
proof: formalized
---

# Exact covering systems

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-systems/index.html).

## Multiplicity of an indexed system of residue classes

Given $k \in \mathbb{N}$, moduli
$m_0, \dots, m_{k-1} \in \mathbb{N}$ and residues $r_0, \dots, r_{k-1} \in \mathbb{Z}$, the
multiplicity of an integer $z$ is the number of indices $i < k$ with $z \equiv r_i \pmod{m_i}$.

Indices are counted separately, so a residue class listed several times is counted that many
times; a modulus $m_i = 0$ makes the condition $z = r_i$.

Formalized by `Int.indexedCoverMultiplicity`, a definition declared in [MathlibExt/NumberTheory/CoveringSystem/ExactCover.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/CoveringSystem/ExactCover.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-systems/index.html#indexed-cover-multiplicity).

## Exact covers by residue classes

Let $k \in \mathbb{N}$, let
$m_0, \dots, m_{k-1} \in \mathbb{N}$ be moduli and $r_0, \dots, r_{k-1} \in \mathbb{Z}$ residues,
and let $M \in \mathbb{N}$ and $T \subseteq \mathbb{Z}$. The system of residue classes
$r_i \bmod m_i$ is an exact $M$-cover of $T$ when $k \ge 2$, every $m_i$ is positive, every
$z \in T$ satisfies $z \equiv r_i \pmod{m_i}$ for exactly $M$ indices $i < k$, and every integer
$z \notin T$ satisfies $z \equiv r_i \pmod{m_i}$ for no index $i < k$.

Indices are counted separately, so a residue class listed several times counts that many times.

Formalized by `Int.IsExactCoverOf`, a definition declared in [MathlibExt/NumberTheory/CoveringSystem/ExactCover.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/CoveringSystem/ExactCover.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-systems/index.html#is-exact-cover-of).

## Fraenkel's Bernoulli recurrence for exact covers by any number of classes

Let $q$, $M$
and $m \ge 1$ be natural numbers, and for $i = 1, \dots, q$ let $n_i$ be a positive integer and
$a_i$ an integer with $0 \le a_i < n_i$. Suppose the residue classes $a_i \bmod n_i$, counted
with repetition, form an exact $M$-cover of $\mathbb{Z}$: every integer $k$ satisfies
$k \equiv a_i \pmod{n_i}$ for exactly $M$ indices $i$. Then

$$
B_m \Big(M - \sum_{i=1}^{q} n_i^{m-1}\Big) =
\sum_{i=1}^{q} n_i^{m-1} \sum_{s=0}^{m-1} \binom{m}{s} B_s \Big(\frac{a_i}{n_i}\Big)^{m-s},
$$

where $B_s$ is the $s$-th Bernoulli number, with the convention $B_1 = -\frac{1}{2}$.

The source assumes $q \ge 2$; the identity holds without that assumption.

Formalized by `MetaMathlibExt.fraenkel_exact_M_cover_bernoulli_recurrence_general`, a theorem declared in [MathlibExt/NumberTheory/FraenkelCoveringBernoulli.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/FraenkelCoveringBernoulli.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-systems/index.html#fraenkel-exact-m-cover-bernoulli-recurre).

## Fraenkel's Bernoulli recurrence for exact covers

Let $q \ge 2$, $m \ge 1$ and $M$ be
natural numbers, and for $i = 1, \dots, q$ let $n_i$ be a positive integer and $a_i$ an integer
with $0 \le a_i < n_i$. Suppose the residue classes $a_i \bmod n_i$, counted with repetition,
form an exact $M$-cover of $\mathbb{Z}$: every integer $k$ satisfies $k \equiv a_i \pmod{n_i}$
for exactly $M$ indices $i$. Then

$$
B_m \Big(M - \sum_{i=1}^{q} n_i^{m-1}\Big) =
\sum_{i=1}^{q} n_i^{m-1} \sum_{s=0}^{m-1} \binom{m}{s} B_s \Big(\frac{a_i}{n_i}\Big)^{m-s},
$$

where $B_s$ is the $s$-th Bernoulli number, with the convention $B_1 = -\frac{1}{2}$.

Only this direction of the source's equation (23) is stated; the converse, Beebee's variant with
a parameter $x$, and Porubsky's weighted variant are not.

## Sources

- Yevgenya Movshovich, "Raabe's Identity and Covering Systems," Journal of Integer Sequences 23 (2020), Article 20.2.8, <https://cs.uwaterloo.ca/journals/JIS/VOL23/Movshovich/movsho5.tex>. Equation (23); lines 228–241.

Formalized by `MetaMathlibExt.fraenkel_exact_M_cover_bernoulli_recurrence`, a theorem declared in [MathlibExt/NumberTheory/FraenkelCoveringBernoulli.lean, line 498](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/FraenkelCoveringBernoulli.lean#L498). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-systems/index.html#fraenkel-exact-m-cover-bernoulli-recurre-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Exact covering systems](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/exact-covering-systems/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/congruences/covering-systems/exact-covering-systems)
