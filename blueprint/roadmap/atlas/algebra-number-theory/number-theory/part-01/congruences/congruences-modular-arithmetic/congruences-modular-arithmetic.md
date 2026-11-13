---
declaration: section
origin: cited
lean: MetaMathlibExt.powerSum_vanishing_mod_prime
statement: formalized
proof: formalized
---

# Congruences and modular arithmetic: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/index.html).

Congruences for factorials, quotients and power sums (Wilson, Wolstenholme, Fermat quotients), lifting the exponent, multiplicative order, primitive roots, residue systems.

## Power sums vanish modulo a prime

Let $p$ be a prime and let $e \ge 0$ be an integer such
that $p - 1$ does not divide $e$ whenever $e \ge 1$. Then $p$ divides $\sum_{t=1}^{p} t^e$.

For $e = 0$ the sum is $p$. The source states the lemma for odd primes; for $p = 2$ the
hypothesis forces $e = 0$.

## Sources

- Christian Ballot, "On a Congruence of Kimball and Webb Involving Lucas Sequences," Journal of Integer Sequences 17 (2014), Article 14.1.3, Lemma, lines 223–225, https://cs.uwaterloo.ca/journals/JIS/VOL17/Ballot/ballot7.tex

Formalized by `MetaMathlibExt.powerSum_vanishing_mod_prime`, a theorem declared in [MathlibExt/NumberTheory/PowerSumVanishing.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PowerSumVanishing.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/index.html#power-sum-vanishing-mod-prime).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Congruences and modular arithmetic](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/congruences/congruences-modular-arithmetic)
