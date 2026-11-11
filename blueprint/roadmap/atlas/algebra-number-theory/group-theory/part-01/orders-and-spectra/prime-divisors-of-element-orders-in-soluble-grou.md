---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.SolublePrimeDivisorsLinearBoundKourovka14Problem66Wanted.solublePrimeCountLinearInElementPrimeCount, MathlibExt.GroupTheory.SolublePrimeDivisorsLinearBoundKourovka14Problem66Wanted.solublePrimeCountLinearInElementPrimeCount_holds
statement: formalized
---

# Prime divisors of element orders in soluble groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/prime-divisors-of-element-orders-in-soluble-grou/index.html).

## Linear bound on the prime divisors of a finite soluble group (Kourovka 14.66)

The
statement, posed by A. Moretó, that there are natural numbers $a$ and $b$ such that for every
finite soluble group $G$ and every natural number $m$, if the order of every element of $G$ has at
most $m$ distinct prime divisors, then $|G|$ has at most $am + b$ distinct prime divisors.

Equivalently, $|\pi(G)| \le a\,\nu(G) + b$ for every finite soluble group $G$, where $\pi(G)$ is
the set of primes dividing $|G|$ and $\nu(G)$ is the largest number of distinct primes dividing
the order of a single element of $G$.

Formalized by `MathlibExt.GroupTheory.SolublePrimeDivisorsLinearBoundKourovka14Problem66Wanted.solublePrimeCountLinearInElementPrimeCount`, a definition declared in [WantedExt/GroupTheory/SolublePrimeDivisorsLinearBoundKourovka14Problem66Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SolublePrimeDivisorsLinearBoundKourovka14Problem66Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/prime-divisors-of-element-orders-in-soluble-grou/index.html#soluble-prime-count-linear-in-element-pr).

## Finite soluble groups satisfy a linear prime-divisor bound

There are natural numbers $a$ and
$b$ such that for every finite soluble group $G$ and every natural number $m$, if the order of
every element of $G$ has at most $m$ distinct prime divisors, then $|G|$ has at most $am + b$
distinct prime divisors. That is, Kourovka Problem 14.66 has a positive answer.

Resolved true: the Kourovka Archive answers 14.66 "Yes, it does", citing Keller.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 14.66 (A. Moretó); resolution: T. M. Keller, J. Algebra 178 (1995), no. 2, 643-652, Kourovka Archive, Problem 14.66 (answer: Yes, it does).

Stated but not proved: `MathlibExt.GroupTheory.SolublePrimeDivisorsLinearBoundKourovka14Problem66Wanted.solublePrimeCountLinearInElementPrimeCount_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/SolublePrimeDivisorsLinearBoundKourovka14Problem66Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SolublePrimeDivisorsLinearBoundKourovka14Problem66Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/prime-divisors-of-element-orders-in-soluble-grou/index.html#soluble-prime-count-linear-in-element-pr-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Prime divisors of element orders in soluble groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/prime-divisors-of-element-orders-in-soluble-grou/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/orders-and-spectra/prime-divisors-of-element-orders-in-soluble-grou)
