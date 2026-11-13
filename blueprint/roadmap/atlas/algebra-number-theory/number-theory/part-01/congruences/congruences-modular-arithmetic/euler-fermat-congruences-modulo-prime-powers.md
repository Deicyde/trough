---
declaration: section
origin: cited
lean: Nat.euler_fermat_prime_power_congruence_general, Nat.euler_fermat_prime_power_congruence
statement: formalized
proof: formalized
---

# Euler–Fermat congruences modulo prime powers

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/euler-fermat-congruences-modulo-prime-powers/index.html).

## Euler–Fermat congruence modulo prime powers

For every natural number $a$, every prime $p$
and every natural number $r \ge 1$, we have $a^{p^r} \equiv a^{p^{r-1}} \pmod{p^r}$.

Formalized by `Nat.euler_fermat_prime_power_congruence_general`, a theorem declared in [MathlibExt/NumberTheory/EulerFermatPrimePower.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EulerFermatPrimePower.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/euler-fermat-congruences-modulo-prime-powers/index.html#euler-fermat-prime-power-congruence-gene).

## Euler–Fermat congruence modulo prime powers, for positive bases

For every positive natural
number $a$, every prime $p$ and every natural number $r \ge 1$, we have
$a^{p^r} \equiv a^{p^{r-1}} \pmod{p^r}$.

## Sources

- G. Everest, A. J. van der Poorten, Y. Puri, and T. Ward, "Integer Sequences and Periodic Points," Journal of Integer Sequences 5 (2002), Article 02.2.3, Corollary; public TeX: <https://cs.uwaterloo.ca/journals/JIS/VOL5/Ward/ward2.tex>. It follows from `euler_fermat_prime_power_congruence_general`; the hypothesis `ha` is unused and keeps the source's shape.

Formalized by `Nat.euler_fermat_prime_power_congruence`, a theorem declared in [MathlibExt/NumberTheory/EulerFermatPrimePower.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EulerFermatPrimePower.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/euler-fermat-congruences-modulo-prime-powers/index.html#euler-fermat-prime-power-congruence).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Euler–Fermat congruences modulo prime powers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/euler-fermat-congruences-modulo-prime-powers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/euler-fermat-congruences-modulo-prime-powers)
