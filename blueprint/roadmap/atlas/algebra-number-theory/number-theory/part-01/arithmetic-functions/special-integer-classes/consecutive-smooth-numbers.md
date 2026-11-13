---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.SmoothConsecutiveIntegersWanted.conjecture, MathlibExt.NumberTheory.SmoothConsecutiveIntegersWanted.conjecture_holds
statement: formalized
---

# Consecutive smooth numbers

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/consecutive-smooth-numbers/index.html).

## Erdős Problem 369, location variant

This is the statement that for every real
$\varepsilon > 0$ and every natural number $k \ge 2$ there is a natural number $N$ such that for
every natural number $n \ge N$ there is a natural number $a$ with $\lfloor n/2 \rfloor \le a + 1$
and $a + k \le n$ for which every prime factor $p$ of each of the $k$ consecutive integers
$a + 1, \dots, a + k$ satisfies $p \le n^\varepsilon$.

Erdős Problem 369 as written allows the run anywhere in $\{1, \dots, n\}$, which is trivially
true (take $1, \dots, k$ once $n^\varepsilon \ge k$); here the run must start at or after
$\lfloor n/2 \rfloor$.

Formalized by `MathlibExt.NumberTheory.SmoothConsecutiveIntegersWanted.conjecture`, a definition declared in [WantedExt/NumberTheory/SmoothConsecutiveIntegersWanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SmoothConsecutiveIntegersWanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/consecutive-smooth-numbers/index.html#conjecture).

## Solution of Erdős Problem 369, location variant

For every real $\varepsilon > 0$ and every
natural number $k \ge 2$ there is a natural number $N$ such that for every natural number
$n \ge N$ there is a natural number $a$ with $\lfloor n/2 \rfloor \le a + 1$ and $a + k \le n$
for which every prime factor $p$ of each of the $k$ consecutive integers $a + 1, \dots, a + k$
satisfies $p \le n^\varepsilon$.

## Sources

- Balog-Wooley 1998; Bober-Fretwell-Martin-Wooley 2020.
- Lean proof of EP-369 location variant (plby/lean-proofs), https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos369.lean.

Stated but not proved: `MathlibExt.NumberTheory.SmoothConsecutiveIntegersWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/SmoothConsecutiveIntegersWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SmoothConsecutiveIntegersWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/consecutive-smooth-numbers/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Consecutive smooth numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/consecutive-smooth-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/consecutive-smooth-numbers)
