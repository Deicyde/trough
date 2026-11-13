---
declaration: section
origin: cited
lean: Int.fermatQuotient, Int.fermatQuotient_eq, Int.natCast_mul_fermatQuotient
statement: formalized
proof: formalized
---

# Fermat quotients

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/fermat-quotients/index.html).

## Fermat quotient

For a prime $p$ and an integer $a$ coprime to $p$, the Fermat quotient
is the integer $q_p(a) = (a^{p-1} - 1)/p$, where $/$ is integer division rounding down. The
division is exact, since $p$ divides $a^{p-1} - 1$ by Fermat's little theorem.

Formalized by `Int.fermatQuotient`, a definition declared in [MathlibExt/NumberTheory/FermatQuotient.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/FermatQuotient.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/fermat-quotients/index.html#fermat-quotient).

## Formula for the Fermat quotient

For a prime $p$ and an integer $a$ coprime to $p$, the
Fermat quotient satisfies $q_p(a) = (a^{p-1} - 1)/p$, where $/$ is integer division rounding
down.

Formalized by `Int.fermatQuotient_eq`, a theorem declared in [MathlibExt/NumberTheory/FermatQuotient.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/FermatQuotient.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/fermat-quotients/index.html#fermat-quotient-eq).

## Fermat quotient times the prime

For a prime $p$ and an integer $a$ coprime to $p$, the
Fermat quotient $q_p(a)$ satisfies $p \, q_p(a) = a^{p-1} - 1$.

Formalized by `Int.natCast_mul_fermatQuotient`, a theorem declared in [MathlibExt/NumberTheory/FermatQuotient.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/FermatQuotient.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/fermat-quotients/index.html#nat-cast-mul-fermat-quotient).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fermat quotients](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/fermat-quotients/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/fermat-quotients)
