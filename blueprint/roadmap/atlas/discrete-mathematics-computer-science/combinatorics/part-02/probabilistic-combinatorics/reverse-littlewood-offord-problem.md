---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ReverseLittlewoodOffordErdosProblem395Wanted.smallSignedSumCount, MathlibExt.Combinatorics.ReverseLittlewoodOffordErdosProblem395Wanted.reverseLittlewoodOffordSqrtTwo, MathlibExt.Combinatorics.ReverseLittlewoodOffordErdosProblem395Wanted.reverseLittlewoodOffordSqrtTwo_holds
statement: formalized
---

# Reverse Littlewood–Offord problem

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/reverse-littlewood-offord-problem/index.html).

## Number of short signed sums

For complex numbers $z_1, \dots, z_n$, this is the number of
sign vectors $(\varepsilon_1, \dots, \varepsilon_n) \in \{-1, 1\}^n$ with
$|\varepsilon_1 z_1 + \dots + \varepsilon_n z_n| \le \sqrt{2}$.

Formalized by `MathlibExt.Combinatorics.ReverseLittlewoodOffordErdosProblem395Wanted.smallSignedSumCount`, a definition declared in [WantedExt/Combinatorics/ReverseLittlewoodOffordErdosProblem395Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ReverseLittlewoodOffordErdosProblem395Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/reverse-littlewood-offord-problem/index.html#small-signed-sum-count).

## Reverse Littlewood–Offord statement of Erdős Problem 395

The statement that there is a
real constant $c > 0$ such that for every natural number $n \ge 1$ and all complex numbers
$z_1, \dots, z_n$ with $|z_i| = 1$ for every $i$, the number $N$ of sign vectors
$(\varepsilon_1, \dots, \varepsilon_n) \in \{-1, 1\}^n$ with
$|\varepsilon_1 z_1 + \dots + \varepsilon_n z_n| \le \sqrt{2}$ satisfies $c/n \le N/2^n$. That is,
for independent uniformly random signs this inequality holds with probability at least $c/n$.

Formalized by `MathlibExt.Combinatorics.ReverseLittlewoodOffordErdosProblem395Wanted.reverseLittlewoodOffordSqrtTwo`, a definition declared in [WantedExt/Combinatorics/ReverseLittlewoodOffordErdosProblem395Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ReverseLittlewoodOffordErdosProblem395Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/reverse-littlewood-offord-problem/index.html#reverse-littlewood-offord-sqrt-two).

## Erdős Problem 395 holds: the reverse Littlewood–Offord bound

There is a real constant
$c > 0$ such that for every natural number $n \ge 1$ and all complex numbers $z_1, \dots, z_n$
with $|z_i| = 1$ for every $i$, at least a $c/n$ fraction of the $2^n$ sign vectors
$(\varepsilon_1, \dots, \varepsilon_n) \in \{-1, 1\}^n$ satisfy
$|\varepsilon_1 z_1 + \dots + \varepsilon_n z_n| \le \sqrt{2}$. That is, for independent uniformly
random signs this inequality holds with probability at least $c/n$.

This was proved by He, Juškevičius, Narayanan and Spiro. The order $1/n$ is sharp: take half of the
$z_i$ equal to $1$ and the rest equal to the imaginary unit $\mathrm{i}$.

## Sources

- T. F. Bloom, Erdős Problems, Problem #395, https://www.erdosproblems.com/395 (status PROVED (LEAN)); resolution: X. He, T. Juškevičius, B. Narayanan and S. Spiro, The reverse Littlewood-Offord problem of Erdős, arXiv:2408.11034 (2024), probability ≫ 1/n, sharp (erdosproblems.com/395), https://arxiv.org/abs/2408.11034.

Stated but not proved: `MathlibExt.Combinatorics.ReverseLittlewoodOffordErdosProblem395Wanted.reverseLittlewoodOffordSqrtTwo_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/ReverseLittlewoodOffordErdosProblem395Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ReverseLittlewoodOffordErdosProblem395Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/reverse-littlewood-offord-problem/index.html#reverse-littlewood-offord-sqrt-two-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Reverse Littlewood–Offord problem](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/reverse-littlewood-offord-problem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/probabilistic-combinatorics/reverse-littlewood-offord-problem)
