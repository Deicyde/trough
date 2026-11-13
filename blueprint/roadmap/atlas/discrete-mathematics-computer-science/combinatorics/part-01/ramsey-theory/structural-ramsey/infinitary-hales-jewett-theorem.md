---
declaration: section
origin: cited
lean: MetaMathlibExt.infinitary_halesJewett, MetaMathlibExt.infinitary_halesJewett_increasing_alphabets, MetaMathlibExt.exists_variableWord_subst_mem_of_isMulPiecewiseSyndetic, MetaMathlibExt.exists_variableWord_subst_mem_of_isMulJSet, MetaMathlibExt.exists_variableWords_prod_mem_of_isCentralSet, MetaMathlibExt.exists_variableWords_prod_mem_of_isCSet, MetaMathlibExt.exists_variableWords_subst_mem_sum_count_mem_finiteSums_of_isMulJSet, MetaMathlibExt.exists_variableWords_prod_mem_sum_count_mem_finiteSums_of_isCSet
statement: formalized
---

# Infinitary Hales–Jewett theorem

10 results, 10 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/infinitary-hales-jewett-theorem/index.html).

## Infinitary Hales–Jewett theorem

Let $A$ be a finite alphabet, and color the finite words
over $A$ with finitely many colors. A variable word over $A$ is a finite word over $A \cup \{v\}$,
for a variable $v \notin A$, in which $v$ occurs, and $w(a)$ is the word obtained from $w$ by
replacing every occurrence of $v$ by the letter $a$. Then there are a sequence $w_0, w_1, \dots$ of
variable words over $A$ and a color $k$ such that the word
$w_{m_1}(a_1) w_{m_2}(a_2) \cdots w_{m_l}(a_l)$ has color $k$ for all $l \ge 1$, all
$m_1 < m_2 < \cdots < m_l$ in $\mathbb{N}$ and all $a_1, \dots, a_l \in A$.

## Sources

- Aninda Chakraborty and Sayan Goswami, *An Analogue to the Infinitary Hales–Jewett Theorem*, INTEGERS 24 (2024), Article A74, Theorem 1.2 (Bergelson, Blass and Hindman).

Stated but not proved: `MetaMathlibExt.infinitary_halesJewett` is written with `theorem_wanted` in [WantedExt/Combinatorics/InfinitaryHalesJewettWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/InfinitaryHalesJewettWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/infinitary-hales-jewett-theorem/index.html#infinitary-hales-jewett).

## Karagiannis's infinitary Hales–Jewett theorem for increasing alphabets

Let $X$ be a set,
let $A_0 \subseteq A_1 \subseteq \cdots$ be finite subsets of $X$ with union $A$, and color the
finite words over $X$ with finitely many colors. A variable word over $A$ is a finite word over
$A \cup \{v\}$, for a variable $v \notin X$, in which $v$ occurs, and $w(a)$ is the word obtained
from $w$ by replacing every occurrence of $v$ by the letter $a$. Then there are a sequence
$w_0, w_1, \dots$ of variable words over $A$ and a color $k$ such that the word
$w_{m_1}(a_1) w_{m_2}(a_2) \cdots w_{m_l}(a_l)$ has color $k$ for all $l \ge 1$, all
$m_1 < m_2 < \cdots < m_l$ in $\mathbb{N}$ and all $a_i \in A_{m_i}$, $i = 1, \dots, l$.

## Sources

- Aninda Chakraborty and Sayan Goswami, *An Analogue to the Infinitary Hales–Jewett Theorem*, INTEGERS 24 (2024), Article A74, Theorem 1.8 (Karagiannis).

Stated but not proved: `MetaMathlibExt.infinitary_halesJewett_increasing_alphabets` is written with `theorem_wanted` in [WantedExt/Combinatorics/InfinitaryHalesJewettWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/InfinitaryHalesJewettWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/infinitary-hales-jewett-theorem/index.html#infinitary-hales-jewett-increasing-alpha).

## Piecewise syndetic sets contain Hales–Jewett configurations

Let
$A_0 \subseteq A_1 \subseteq \cdots$ be finite sets with union $A$, and let $S_0$ be the semigroup
of nonempty finite words over $A$ under concatenation. For $n \in \mathbb{N}$, an $n$-variable
word over $A$ is a nonempty finite word over $A \cup \{v_0, \dots, v_{n-1}\}$, for distinct
variables $v_i \notin A$, in which every $v_i$ occurs; for $\vec a = (a_0, \dots, a_{n-1})$ in
$A^n$, the word $w(\vec a) \in S_0$ is obtained from $w$ by replacing each $v_i$ by $a_i$. If
$D \subseteq S_0$ is piecewise syndetic, then for all $m, n \in \mathbb{N}$ there is an
$n$-variable word $w$ over $A$ with $w(\vec a) \in D$ for every $\vec a \in A_m^n$.

For $n = 0$ the claim is that $D$ is nonempty.

## Sources

- Aninda Chakraborty and Sayan Goswami, *An Analogue to the Infinitary Hales–Jewett Theorem*, INTEGERS 24 (2024), Article A74, Lemma 3.3.

Stated but not proved: `MetaMathlibExt.exists_variableWord_subst_mem_of_isMulPiecewiseSyndetic` is written with `theorem_wanted` in [WantedExt/Combinatorics/InfinitaryHalesJewettWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/InfinitaryHalesJewettWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/infinitary-hales-jewett-theorem/index.html#exists-variable-word-subst-mem-of-is-mul).

## J-sets contain Hales–Jewett configurations

Let $A_0 \subseteq A_1 \subseteq \cdots$ be
finite sets whose union $A$ is nonempty, and let $S_0$ be the semigroup of nonempty finite words
over $A$ under concatenation. For $n \in \mathbb{N}$, an $n$-variable word over $A$ is a nonempty
finite word over $A \cup \{v_0, \dots, v_{n-1}\}$, for distinct variables $v_i \notin A$, in which
every $v_i$ occurs; for $\vec a = (a_0, \dots, a_{n-1})$ in $A^n$, the word $w(\vec a) \in S_0$
is obtained from $w$ by replacing each $v_i$ by $a_i$. If $D \subseteq S_0$ is a $J$-set, then
for all $m, n \in \mathbb{N}$ there is an $n$-variable word $w$ over $A$ with $w(\vec a) \in D$
for every $\vec a \in A_m^n$.

The alphabet must be nonempty: over the empty alphabet every subset of $S_0 = \emptyset$ is
vacuously a $J$-set, and there is no $0$-variable word.

## Sources

- Aninda Chakraborty and Sayan Goswami, *An Analogue to the Infinitary Hales–Jewett Theorem*, INTEGERS 24 (2024), Article A74, Lemma 3.4.

Stated but not proved: `MetaMathlibExt.exists_variableWord_subst_mem_of_isMulJSet` is written with `theorem_wanted` in [WantedExt/Combinatorics/InfinitaryHalesJewettWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/InfinitaryHalesJewettWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/infinitary-hales-jewett-theorem/index.html#exists-variable-word-subst-mem-of-is-mul-2).

## Infinitary Hales–Jewett configurations in central sets

Let
$A_0 \subseteq A_1 \subseteq \cdots$ be finite sets with union $A$, and let $S_0$ be the semigroup
of nonempty finite words over $A$ under concatenation. For $n \in \mathbb{N}$, an $n$-variable
word over $A$ is a nonempty finite word over $A \cup \{v_0, \dots, v_{n-1}\}$, for distinct
variables $v_i \notin A$, in which every $v_i$ occurs; for $\vec a = (a_0, \dots, a_{n-1})$ in
$A^n$, the word $w(\vec a) \in S_0$ is obtained from $w$ by replacing each $v_i$ by $a_i$. If
$D \subseteq S_0$ is central, then for every $n \in \mathbb{N}$ there is a sequence
$w_0, w_1, \dots$ of $n$-variable words over $A$ such that
$w_{m_0}(\vec a_0) w_{m_1}(\vec a_1) \cdots w_{m_l}(\vec a_l) \in D$ for all $l \in \mathbb{N}$,
all $m_0 < m_1 < \cdots < m_l$ in $\mathbb{N}$ and all $\vec a_j \in A_{m_j}^n$,
$j = 0, \dots, l$.

## Sources

- Aninda Chakraborty and Sayan Goswami, *An Analogue to the Infinitary Hales–Jewett Theorem*, INTEGERS 24 (2024), Article A74, Theorem 3.5.

Stated but not proved: `MetaMathlibExt.exists_variableWords_prod_mem_of_isCentralSet` is written with `theorem_wanted` in [WantedExt/Combinatorics/InfinitaryHalesJewettWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/InfinitaryHalesJewettWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/infinitary-hales-jewett-theorem/index.html#exists-variable-words-prod-mem-of-is-cen).

## Infinitary Hales–Jewett configurations in C-sets

Let
$A_0 \subseteq A_1 \subseteq \cdots$ be finite sets with union $A$, and let $S_0$ be the semigroup
of nonempty finite words over $A$ under concatenation. For $n \in \mathbb{N}$, an $n$-variable
word over $A$ is a nonempty finite word over $A \cup \{v_0, \dots, v_{n-1}\}$, for distinct
variables $v_i \notin A$, in which every $v_i$ occurs; for $\vec a = (a_0, \dots, a_{n-1})$ in
$A^n$, the word $w(\vec a) \in S_0$ is obtained from $w$ by replacing each $v_i$ by $a_i$. If
$D \subseteq S_0$ is a $C$-set, then for every $n \in \mathbb{N}$ there is a sequence
$w_0, w_1, \dots$ of $n$-variable words over $A$ such that
$w_{m_0}(\vec a_0) w_{m_1}(\vec a_1) \cdots w_{m_l}(\vec a_l) \in D$ for all $l \in \mathbb{N}$,
all $m_0 < m_1 < \cdots < m_l$ in $\mathbb{N}$ and all $\vec a_j \in A_{m_j}^n$,
$j = 0, \dots, l$.

## Sources

- Aninda Chakraborty and Sayan Goswami, *An Analogue to the Infinitary Hales–Jewett Theorem*, INTEGERS 24 (2024), Article A74, Corollary 3.6.

Stated but not proved: `MetaMathlibExt.exists_variableWords_prod_mem_of_isCSet` is written with `theorem_wanted` in [WantedExt/Combinatorics/InfinitaryHalesJewettWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/InfinitaryHalesJewettWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/infinitary-hales-jewett-theorem/index.html#exists-variable-words-prod-mem-of-is-cse).

## Variable-count sums of variable words in J-sets

Let $A_0 \subseteq A_1 \subseteq \cdots$
be finite sets with union $A$, and let $S_0$ be the semigroup of nonempty finite words over $A$
under concatenation. A variable word over $A$ is a nonempty finite word over $A \cup \{v\}$, for a
variable $v \notin A$, in which $v$ occurs; for $a \in A$, the word $w(a) \in S_0$ is obtained from
$w$ by replacing each occurrence of $v$ by $a$, and $|w|_v$ is the number of occurrences of $v$ in
$w$. If $D \subseteq S_0$ is a $J$-set and $x_0, x_1, \dots$ are positive integers, then there is
a sequence $w_0, w_1, \dots$ of variable words over $A$ such that $w_k(a) \in D$ for all
$k \in \mathbb{N}$ and $a \in A_k$, and such that for every nonempty finite $G \subseteq \mathbb{N}$
there is a nonempty finite $H \subseteq \mathbb{N}$ with
$\sum_{k \in G} |w_k|_v = \sum_{j \in H} x_j$.

## Sources

- Aninda Chakraborty and Sayan Goswami, *An Analogue to the Infinitary Hales–Jewett Theorem*, INTEGERS 24 (2024), Article A74, Theorem 3.7.

Stated but not proved: `MetaMathlibExt.exists_variableWords_subst_mem_sum_count_mem_finiteSums_of_isMulJSet` is written with `theorem_wanted` in [WantedExt/Combinatorics/InfinitaryHalesJewettWanted.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/InfinitaryHalesJewettWanted.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/infinitary-hales-jewett-theorem/index.html#exists-variable-words-subst-mem-sum-coun).

## Variable-count sums of variable words in C-sets

Let $A_0 \subseteq A_1 \subseteq \cdots$
be finite sets with union $A$, and let $S_0$ be the semigroup of nonempty finite words over $A$
under concatenation. A variable word over $A$ is a nonempty finite word over $A \cup \{v\}$, for a
variable $v \notin A$, in which $v$ occurs; for $a \in A$, the word $w(a) \in S_0$ is obtained from
$w$ by replacing each occurrence of $v$ by $a$, and $|w|_v$ is the number of occurrences of $v$ in
$w$. If $D \subseteq S_0$ is a $C$-set and $x_0, x_1, \dots$ are positive integers, then there is
a sequence $w_0, w_1, \dots$ of variable words over $A$ such that
$w_{m_0}(a_0) w_{m_1}(a_1) \cdots w_{m_l}(a_l) \in D$ for all $l \in \mathbb{N}$, all
$m_0 < m_1 < \cdots < m_l$ in $\mathbb{N}$ and all $a_j \in A_{m_j}$, $j = 0, \dots, l$, and such
that for every nonempty finite $G \subseteq \mathbb{N}$ there is a nonempty finite
$H \subseteq \mathbb{N}$ with $\sum_{k \in G} |w_k|_v = \sum_{j \in H} x_j$.

## Sources

- Aninda Chakraborty and Sayan Goswami, *An Analogue to the Infinitary Hales–Jewett Theorem*, INTEGERS 24 (2024), Article A74, Corollary 3.8.

Stated but not proved: `MetaMathlibExt.exists_variableWords_prod_mem_sum_count_mem_finiteSums_of_isCSet` is written with `theorem_wanted` in [WantedExt/Combinatorics/InfinitaryHalesJewettWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/InfinitaryHalesJewettWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/infinitary-hales-jewett-theorem/index.html#exists-variable-words-prod-mem-sum-count).

## Variable patterns of variable words in J-sets

Let $A_0 \subseteq A_1 \subseteq \cdots$
be finite sets with union $A$, and let $S_0$ be the semigroup of nonempty finite words over $A$
under concatenation. Let $1 \le k < n$. An $n$-variable word over $A$ is a nonempty finite word
over $A \cup \{v_0, \dots, v_{n-1}\}$, for distinct variables $v_i \notin A$, in which every $v_i$
occurs; for $\vec a = (a_0, \dots, a_{n-1})$ in $A^n$, the word $w(\vec a) \in S_0$ is obtained
from $w$ by replacing each $v_i$ by $a_i$, and $\tau(w)$ is the word over
$\{v_0, \dots, v_{k-1}\}$ obtained from $w$ by deleting the letters of $A$ and the variables $v_i$
with $i \ge k$. Let $y_0, y_1, \dots$ be finite words over $\{v_0, \dots, v_{k-1}\}$ in each of
which every $v_i$ with $i < k$ occurs. If $D \subseteq S_0$ is a $J$-set, then there is a
sequence $w_0, w_1, \dots$ of $n$-variable words over $A$ such that $w_m(\vec a) \in D$ for all
$m \in \mathbb{N}$ and $\vec a \in A_m^n$, and such that for all $l \in \mathbb{N}$ and
$m_0 < m_1 < \cdots < m_l$ in $\mathbb{N}$ there are $r \in \mathbb{N}$ and
$t_0 < t_1 < \cdots < t_r$ in $\mathbb{N}$ with
$\tau(w_{m_0}) \tau(w_{m_1}) \cdots \tau(w_{m_l}) = y_{t_0} y_{t_1} \cdots y_{t_r}$, where
juxtaposition is concatenation of words.

## Sources

- Aninda Chakraborty and Sayan Goswami, *An Analogue to the Infinitary Hales–Jewett Theorem*, INTEGERS 24 (2024), Article A74, Theorem 3.9.

Stated but not proved: `MetaMathlibExt.exists_variableWords_subst_mem_prod_pattern_mem_finiteProducts_of_isMulJSet` is written with `theorem_wanted` in [WantedExt/Combinatorics/InfinitaryHalesJewettWanted.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/InfinitaryHalesJewettWanted.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/infinitary-hales-jewett-theorem/index.html#exists-variable-words-subst-mem-prod-pat).

## Variable patterns of variable words in C-sets

Let $A_0 \subseteq A_1 \subseteq \cdots$
be finite sets with union $A$, and let $S_0$ be the semigroup of nonempty finite words over $A$
under concatenation. Let $1 \le k < n$. An $n$-variable word over $A$ is a nonempty finite word
over $A \cup \{v_0, \dots, v_{n-1}\}$, for distinct variables $v_i \notin A$, in which every $v_i$
occurs; for $\vec a = (a_0, \dots, a_{n-1})$ in $A^n$, the word $w(\vec a) \in S_0$ is obtained
from $w$ by replacing each $v_i$ by $a_i$, and $\tau(w)$ is the word over
$\{v_0, \dots, v_{k-1}\}$ obtained from $w$ by deleting the letters of $A$ and the variables $v_i$
with $i \ge k$. Let $y_0, y_1, \dots$ be finite words over $\{v_0, \dots, v_{k-1}\}$ in each of
which every $v_i$ with $i < k$ occurs. If $C \subseteq S_0$ is a $C$-set, then there is a
sequence $w_0, w_1, \dots$ of $n$-variable words over $A$ such that for all $l \in \mathbb{N}$ and
$m_0 < m_1 < \cdots < m_l$ in $\mathbb{N}$, the word
$w_{m_0}(\vec a_0) w_{m_1}(\vec a_1) \cdots w_{m_l}(\vec a_l)$ lies in $C$ for all
$\vec a_j \in A_{m_j}^n$, $j = 0, \dots, l$, and there are $r \in \mathbb{N}$ and
$t_0 < t_1 < \cdots < t_r$ in $\mathbb{N}$ with
$\tau(w_{m_0}) \tau(w_{m_1}) \cdots \tau(w_{m_l}) = y_{t_0} y_{t_1} \cdots y_{t_r}$, where
juxtaposition is concatenation of words.

## Sources

- Aninda Chakraborty and Sayan Goswami, *An Analogue to the Infinitary Hales–Jewett Theorem*, INTEGERS 24 (2024), Article A74, Corollary 3.10.

Stated but not proved: `MetaMathlibExt.exists_variableWords_prod_mem_prod_pattern_mem_finiteProducts_of_isCSet` is written with `theorem_wanted` in [WantedExt/Combinatorics/InfinitaryHalesJewettWanted.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/InfinitaryHalesJewettWanted.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/infinitary-hales-jewett-theorem/index.html#exists-variable-words-prod-mem-prod-patt).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Infinitary Hales–Jewett theorem](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/infinitary-hales-jewett-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/ramsey-theory/structural-ramsey/infinitary-hales-jewett-theorem)
