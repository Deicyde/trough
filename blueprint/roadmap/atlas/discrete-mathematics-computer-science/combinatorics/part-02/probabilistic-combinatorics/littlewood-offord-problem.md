---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ScottishBook179Wanted.littlewoodOffordSharpBound, MathlibExt.Combinatorics.StrongLittlewoodOffordErdosProblem498Wanted.signedSumsInUnitDiscBound, MathlibExt.Combinatorics.StrongLittlewoodOffordErdosProblem498Wanted.signedSumsInUnitDiscBound_holds
statement: formalized
---

# Littlewood–Offord problem

3 results, 1 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/littlewood-offord-problem/index.html).

## Sharp Littlewood–Offord bound

There is a real constant $A \ge 0$ such that for every
integer $n \ge 1$ and all real numbers $a_0, a_1, \dots, a_n$ with $|a_i| \ge 1$ for every $i$,
the number of sign vectors $(\varepsilon_1, \dots, \varepsilon_n) \in \{-1, 1\}^n$ with
$|a_0 + \varepsilon_1 a_1 + \dots + \varepsilon_n a_n| < 1$ is at most $A \cdot 2^n / \sqrt{n}$.

This answers Offord's Problem 179 from the Scottish Book. In the original notation the bound is
on the exceptional set of signed sums $a_0 + \varepsilon_1 a_1 + \dots + \varepsilon_n a_n$
whose absolute value is below $\min_\nu |a_\nu|$; the statement here is the rescaled form with
$\min_\nu |a_\nu| = 1$.

## Sources

- A. C. Offord, Problem 179 of the Scottish Book; the Littlewood-Offord lemma (Littlewood-Offord, 1938) and Erdős's proof giving the sharp `O(2 ^ n / √n)` bound, attained when all the `a nu` are equal. See the commentary in R. D. Mauldin (ed.), The Scottish Book, 2nd ed. (Birkhäuser, 2015).

Stated but not proved: `MathlibExt.Combinatorics.ScottishBook179Wanted.littlewoodOffordSharpBound` is written with `theorem_wanted` in [WantedExt/Combinatorics/ScottishBook179Wanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ScottishBook179Wanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/littlewood-offord-problem/index.html#littlewood-offord-sharp-bound).

## Strong Littlewood–Offord bound in the plane

The statement that for every natural
number $n$, all complex numbers $z_1, \dots, z_n$ with $|z_i| \ge 1$ for every $i$, and every
open disc $D$ of radius $1$ in $\mathbb{C}$, at most $\binom{n}{\lfloor n/2 \rfloor}$ of the
$2^n$ sign vectors $(\varepsilon_1, \dots, \varepsilon_n) \in \{1, -1\}^n$ satisfy
$\sum_i \varepsilon_i z_i \in D$ (Erdős Problem 498).

Formalized by `MathlibExt.Combinatorics.StrongLittlewoodOffordErdosProblem498Wanted.signedSumsInUnitDiscBound`, a definition declared in [WantedExt/Combinatorics/StrongLittlewoodOffordErdosProblem498Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/StrongLittlewoodOffordErdosProblem498Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/littlewood-offord-problem/index.html#signed-sums-in-unit-disc-bound).

## Kleitman's theorem on signed sums in the plane

For every natural number $n$, all complex
numbers $z_1, \dots, z_n$ with $|z_i| \ge 1$ for every $i$, and every open disc $D$ of radius $1$
in $\mathbb{C}$, at most $\binom{n}{\lfloor n/2 \rfloor}$ of the $2^n$ sign vectors
$(\varepsilon_1, \dots, \varepsilon_n) \in \{1, -1\}^n$ satisfy $\sum_i \varepsilon_i z_i \in D$.

Kleitman proved this bound for complex $z_i$ (later for vectors in any Hilbert space); Erdős had
proved it for real $z_i$.

## Sources

- T. F. Bloom, Erdős Problems, Problem #498, https://www.erdosproblems.com/498 (status PROVED (LEAN)); resolution: D. J. Kleitman, On a lemma of Littlewood and Offord on the distribution of certain sums, Math. Z. (1965), 251-259, erdosproblems.com/498: solved in the affirmative by Kleitman; generalized to Hilbert spaces (Kleitman 1970), https://www.erdosproblems.com/498.

Stated but not proved: `MathlibExt.Combinatorics.StrongLittlewoodOffordErdosProblem498Wanted.signedSumsInUnitDiscBound_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/StrongLittlewoodOffordErdosProblem498Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/StrongLittlewoodOffordErdosProblem498Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/littlewood-offord-problem/index.html#signed-sums-in-unit-disc-bound-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Littlewood–Offord problem](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/littlewood-offord-problem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/probabilistic-combinatorics/littlewood-offord-problem)
