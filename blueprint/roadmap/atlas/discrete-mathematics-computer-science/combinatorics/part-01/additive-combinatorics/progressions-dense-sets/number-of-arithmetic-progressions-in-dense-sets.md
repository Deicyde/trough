---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ManyThreeTermProgressionsErdosProblem179Wanted.HasAP, MathlibExt.Combinatorics.ManyThreeTermProgressionsErdosProblem179Wanted.apCount, MathlibExt.Combinatorics.ManyThreeTermProgressionsErdosProblem179Wanted.apThreshold, MathlibExt.Combinatorics.ManyThreeTermProgressionsErdosProblem179Wanted.threeAPThresholdForFourAPLittleO, MathlibExt.Combinatorics.ManyThreeTermProgressionsErdosProblem179Wanted.threeAPThresholdExponentTwo, MathlibExt.Combinatorics.ManyThreeTermProgressionsErdosProblem179Wanted.threeAPThresholdForFourAPLittleO_holds, MathlibExt.Combinatorics.ManyThreeTermProgressionsErdosProblem179Wanted.threeAPThresholdExponentTwo_holds
statement: formalized
---

# Number of arithmetic progressions in dense sets

7 results, 5 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/number-of-arithmetic-progressions-in-dense-sets/index.html).

## Containing a $k$-term arithmetic progression

A finite set $A \subseteq \mathbb{N}$
contains a $k$-term arithmetic progression when there are natural numbers $a$ and $d \ge 1$ with
$a + i d \in A$ for every natural number $i < k$, that is, $a, a + d, \dots, a + (k - 1) d$ all
lie in $A$. For $k = 0$ this holds vacuously.

Formalized by `MathlibExt.Combinatorics.ManyThreeTermProgressionsErdosProblem179Wanted.HasAP`, a definition declared in [WantedExt/Combinatorics/ManyThreeTermProgressionsErdosProblem179Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ManyThreeTermProgressionsErdosProblem179Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/number-of-arithmetic-progressions-in-dense-sets/index.html#has-ap).

## Number of $k$-term arithmetic progressions in a set

For a finite set
$A \subseteq \mathbb{N}$ and a natural number $k$, $\mathrm{AP}_k(A)$ is the number of pairs
$(a, d)$ of natural numbers with $a \in A$ and $1 \le d \le \max A$ such that $a + i d \in A$ for
every natural number $i < k$. For $k \ge 2$ the conditions $a \in A$ and $d \le \max A$ follow
from the others, so $\mathrm{AP}_k(A)$ counts the $k$-term progressions
$a, a + d, \dots, a + (k - 1) d$ in $A$ with $d \ge 1$.

Formalized by `MathlibExt.Combinatorics.ManyThreeTermProgressionsErdosProblem179Wanted.apCount`, a definition declared in [WantedExt/Combinatorics/ManyThreeTermProgressionsErdosProblem179Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ManyThreeTermProgressionsErdosProblem179Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/number-of-arithmetic-progressions-in-dense-sets/index.html#ap-count).

## The progression threshold $F_k(N, \ell)$

For natural numbers $k$, $\ell$ and $N$,
$F_k(N, \ell)$ is the least natural number $m$ such that every $N$-element set
$A \subseteq \mathbb{N}$ with $\mathrm{AP}_k(A) \ge m$ contains an $\ell$-term arithmetic
progression, where $\mathrm{AP}_k(A)$ is the number of pairs $(a, d)$ with $a \in A$,
$1 \le d \le \max A$ and $a + i d \in A$ for all $i < k$ (for $k \ge 2$, the number of $k$-term
progressions in $A$ with $d \ge 1$); if no such $m$ exists, $F_k(N, \ell) = 0$.

For $k \ge 2$ such an $m$ always exists, since an $N$-element set has at most $N^2$ $k$-term
progressions.

Formalized by `MathlibExt.Combinatorics.ManyThreeTermProgressionsErdosProblem179Wanted.apThreshold`, a definition declared in [WantedExt/Combinatorics/ManyThreeTermProgressionsErdosProblem179Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ManyThreeTermProgressionsErdosProblem179Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/number-of-arithmetic-progressions-in-dense-sets/index.html#ap-threshold).

## Erdős Problem 179: is $F_3(N, 4) = o(N^2)$?

**Erdős Problem 179: is $F_3(N, 4) = o(N^2)$?** The statement that $F_3(N, 4) = o(N^2)$ as
$N \to \infty$ over the natural numbers, that is, $F_3(N, 4) / N^2 \to 0$, where $F_3(N, 4)$ is the
least $m$ such that every $N$-element set $A \subseteq \mathbb{N}$ containing at least $m$
three-term arithmetic progressions $a, a + d, a + 2d$ with $d \ge 1$ contains a $4$-term
arithmetic progression.

Formalized by `MathlibExt.Combinatorics.ManyThreeTermProgressionsErdosProblem179Wanted.threeAPThresholdForFourAPLittleO`, a definition declared in [WantedExt/Combinatorics/ManyThreeTermProgressionsErdosProblem179Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ManyThreeTermProgressionsErdosProblem179Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/number-of-arithmetic-progressions-in-dense-sets/index.html#three-apthreshold-for-four-aplittle-o).

## Erdős Problem 179: does $\log F_3(N, \ell) / \log N$ tend to $2$?

**Erdős Problem 179: does $\log F_3(N, \ell) / \log N$ tend to $2$?** The statement that for
every natural number $\ell > 3$, $\log F_3(N, \ell) / \log N \to 2$ as $N \to \infty$ over the
natural numbers, where $F_3(N, \ell)$ is the least $m$ such that every $N$-element set
$A \subseteq \mathbb{N}$ containing at least $m$ three-term arithmetic progressions
$a, a + d, a + 2d$ with $d \ge 1$ contains an $\ell$-term arithmetic progression.

Formalized by `MathlibExt.Combinatorics.ManyThreeTermProgressionsErdosProblem179Wanted.threeAPThresholdExponentTwo`, a definition declared in [WantedExt/Combinatorics/ManyThreeTermProgressionsErdosProblem179Wanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ManyThreeTermProgressionsErdosProblem179Wanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/number-of-arithmetic-progressions-in-dense-sets/index.html#three-apthreshold-exponent-two).

## Erdős Problem 179: $F_3(N, 4) = o(N^2)$

As $N \to \infty$ over the natural numbers,
$F_3(N, 4) / N^2 \to 0$, that is, $F_3(N, 4) = o(N^2)$, where $F_3(N, 4)$ is the least natural
number $m$ such that every $N$-element set $A \subseteq \mathbb{N}$ containing at least $m$
three-term arithmetic progressions $a, a + d, a + 2d$ with $d \ge 1$ contains a $4$-term
arithmetic progression.

Write $F_k(N, \ell)$ for the same threshold with $k$-term progressions in place of three-term ones
and $\ell$-term progressions in place of $4$-term ones. Fox and Pohoata bound $F_k(N, \ell)$ above
by $(r_\ell(N) / N)^{O(1)} N^2$, where $r_\ell(N)$ is the largest size of a subset of
$\{1, \dots, N\}$ without $\ell$-term progressions; since $r_\ell(N) = o(N)$ by Szemerédi's
theorem, this bound is $o(N^2)$. erdosproblems.com/179 records
$F_k(N, \ell) \le N^2 / (\log \log N)^{C_\ell}$ for a constant $C_\ell$ depending only on $\ell$.

## Sources

- T. F. Bloom, Erdős Problems, Problem #179, https://www.erdosproblems.com/179 (status PROVED); resolution: J. Fox and C. Pohoata, Sets without k-term progressions can have many shorter progressions, Random Structures Algorithms 58 (2021), 383-389, arXiv:1908.09905, main theorem: for all k > s ≥ 3, log f_{s,k}(n) / log n → 2, where f_{s,k}(n) = F_s(n, k) - 1 is the largest number of s-term progressions in an n-set with no k-term progression; erdosproblems.com/179: F_k(N, ℓ) ≤ N² / (log log N)^{C_ℓ}, https://arxiv.org/abs/1908.09905.

Stated but not proved: `MathlibExt.Combinatorics.ManyThreeTermProgressionsErdosProblem179Wanted.threeAPThresholdForFourAPLittleO_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/ManyThreeTermProgressionsErdosProblem179Wanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ManyThreeTermProgressionsErdosProblem179Wanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/number-of-arithmetic-progressions-in-dense-sets/index.html#three-apthreshold-for-four-aplittle-o-ho).

## Erdős Problem 179: $\log F_3(N, \ell) / \log N$ tends to $2$

For every natural number
$\ell > 3$, $\log F_3(N, \ell) / \log N \to 2$ as $N \to \infty$ over the natural numbers, where
$F_3(N, \ell)$ is the least natural number $m$ such that every $N$-element set
$A \subseteq \mathbb{N}$ containing at least $m$ three-term arithmetic progressions
$a, a + d, a + 2d$ with $d \ge 1$ contains an $\ell$-term arithmetic progression.

Fox and Pohoata prove that $\log f_{s,k}(n) / \log n \to 2$ for all $k > s \ge 3$, where
$f_{s,k}(n)$ is the largest number of $s$-term progressions in an $n$-element set with no
$k$-term progression; since $F_3(N, \ell) = f_{3,\ell}(N) + 1$, taking $s = 3$ and $k = \ell$
gives the statement.

## Sources

- T. F. Bloom, Erdős Problems, Problem #179, https://www.erdosproblems.com/179 (status PROVED); resolution: J. Fox and C. Pohoata, Sets without k-term progressions can have many shorter progressions, Random Structures Algorithms 58 (2021), 383-389, arXiv:1908.09905, main theorem: for all k > s ≥ 3, log f_{s,k}(n) / log n → 2, where f_{s,k}(n) = F_s(n, k) - 1 is the largest number of s-term progressions in an n-set with no k-term progression; erdosproblems.com/179: F_k(N, ℓ) ≤ N² / (log log N)^{C_ℓ}, https://arxiv.org/abs/1908.09905.

Stated but not proved: `MathlibExt.Combinatorics.ManyThreeTermProgressionsErdosProblem179Wanted.threeAPThresholdExponentTwo_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/ManyThreeTermProgressionsErdosProblem179Wanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ManyThreeTermProgressionsErdosProblem179Wanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/number-of-arithmetic-progressions-in-dense-sets/index.html#three-apthreshold-exponent-two-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Number of arithmetic progressions in dense sets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/number-of-arithmetic-progressions-in-dense-sets/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/number-of-arithmetic-progressions-in-dense-sets)
