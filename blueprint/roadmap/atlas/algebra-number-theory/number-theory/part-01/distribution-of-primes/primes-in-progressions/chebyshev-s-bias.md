---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.ChebyshevSignChangeWanted.NumberTheory.ChebyshevSignChangeProblem.chebyshevLead, MathlibExt.NumberTheory.ChebyshevSignChangeWanted.NumberTheory.ChebyshevSignChangeProblem.chebyshev_sign_change
statement: formalized
---

# Chebyshev's bias

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/chebyshev-s-bias/index.html).

## The set where primes $\equiv 3 \pmod 4$ lead

This is the set of natural numbers $n$
for which the number of primes $p \le n$ with $p \equiv 3 \pmod 4$ is strictly greater than the
number of primes $p \le n$ with $p \equiv 1 \pmod 4$.

Formalized by `MathlibExt.NumberTheory.ChebyshevSignChangeWanted.NumberTheory.ChebyshevSignChangeProblem.chebyshevLead`, a definition declared in [WantedExt/NumberTheory/ChebyshevSignChangeWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ChebyshevSignChangeWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/chebyshev-s-bias/index.html#chebyshev-lead).

## Hardy–Littlewood sign changes in the prime race modulo 4

There are infinitely many
natural numbers $n$ for which the primes $p \le n$ with $p \equiv 3 \pmod 4$ strictly outnumber
the primes $p \le n$ with $p \equiv 1 \pmod 4$, and infinitely many natural numbers $n$ for which
the primes $p \le n$ with $p \equiv 1 \pmod 4$ strictly outnumber the primes $p \le n$ with
$p \equiv 3 \pmod 4$.

## Sources

- G.H. Hardy and J.E. Littlewood, 'Contributions to the theory of the Riemann zeta-function and the theory of the distribution of primes', Acta Math. 41 (1916) 119–196 (announced 1914). Chebyshev's original observation: P. Chebyshev, letter to M. Fuss, 1853, in *Œuvres de P.L. Tchebychef*, vol. I (Saint Petersburg, 1899). Listed as §106 in O. Knill, *Some Fundamental Theorems in Mathematics* (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `chebyshev_sign_change` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.ChebyshevSignChangeWanted.NumberTheory.ChebyshevSignChangeProblem.chebyshev_sign_change` is written with `theorem_wanted` in [WantedExt/NumberTheory/ChebyshevSignChangeWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ChebyshevSignChangeWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/chebyshev-s-bias/index.html#chebyshev-sign-change).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Chebyshev's bias](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/chebyshev-s-bias/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/chebyshev-s-bias)
