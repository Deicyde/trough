---
declaration: section
origin: cited
lean: MetaMathlibExt.NumberTheory.PrimeCounting.dirichlet_density_primes_arithmetic_progression
statement: formalized
proof: formalized
---

# Primes in arithmetic progressions: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/index.html).

Dirichlet density, PNT for progressions, Siegel–Walfisz, Bombieri–Vinogradov, Brun–Titchmarsh, prime races.

## Dirichlet density of primes in an arithmetic progression

Let $a$ and $m$ be natural numbers
with $m > 0$ and $\gcd(a, m) = 1$, and let $\varphi$ be Euler's totient function. As the real
number $s$ tends to $1$ from above,

$$\frac{\sum_{p \equiv a \pmod{m}} p^{-s}}{\sum_{p} p^{-s}} \to \frac{1}{\varphi(m)},$$

where both sums run over primes $p$. That is, the primes congruent to $a$ modulo $m$ have relative
Dirichlet density $1/\varphi(m)$ among all primes.

## Sources

- B. Li, S. J. Miller, T. Popescu, D. Sarnecki, and N. Wattanawanichkul, "Modeling Random Walks to Infinity on Primes in Z[sqrt(2)]", *Journal of Integer Sequences* 25 (2022), Article 22.6.1, [TeX source](https://cs.uwaterloo.ca/journals/JIS/VOL25/Miller/miller11.tex), relative Dirichlet-density definition at lines 281-285 and primes-in-arithmetic- progressions statement at lines 290-292.

Formalized by `MetaMathlibExt.NumberTheory.PrimeCounting.dirichlet_density_primes_arithmetic_progression`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/DirichletDensityArithmeticProgression.lean, line 515](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeCounting/DirichletDensityArithmeticProgression.lean#L515). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/index.html#dirichlet-density-primes-arithmetic-prog).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Primes in arithmetic progressions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions)
