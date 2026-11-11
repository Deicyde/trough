---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.LucasNumbersModuloMWanted.Statement, MathlibExt.NumberTheory.LucasNumbersModuloMWanted.Statement_holds
statement: formalized
---

# Residues of Lucas numbers

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/residues-of-lucas-numbers/index.html).

## Classification of moduli for which the Lucas numbers attain every residue

The
proposition that for every integer $m > 1$, with $L_n$ the Lucas numbers, every residue modulo
$m$ is attained (for every $r$ with $0 \le r < m$ there is $n \ge 0$ with
$L_n \equiv r \pmod m$) if and only if $m \in \{2, 4, 6, 7, 14\}$ or $m = 3^k$ for some
integer $k \ge 1$.

## Sources

- OPG-37402, Lucas Numbers Modulo m [OpenGarden].

Formalized by `MathlibExt.NumberTheory.LucasNumbersModuloMWanted.Statement`, a definition declared in [WantedExt/NumberTheory/LucasNumbersModuloMWanted.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LucasNumbersModuloMWanted.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/residues-of-lucas-numbers/index.html#statement).

## Avila–Chen theorem on Lucas numbers modulo $m$

Let $L_n$ denote the Lucas numbers. For every
integer $m > 1$, every residue modulo $m$ is attained by the Lucas numbers (for every $r$ with
$0 \le r < m$ there is $n \ge 0$ with $L_n \equiv r \pmod m$) if and only if
$m \in \{2, 4, 6, 7, 14\}$ or $m = 3^k$ for some integer $k \ge 1$.

## Sources

- Brandon Avila and Yongyi Chen, On Moduli For Which the Lucas Numbers Contain a Complete Residue System, Fibonacci Quarterly 51(2) (2013), 151–152, https://doi.org/10.1080/00150517.2013.12427958.

Stated but not proved: `MathlibExt.NumberTheory.LucasNumbersModuloMWanted.Statement_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/LucasNumbersModuloMWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LucasNumbersModuloMWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/residues-of-lucas-numbers/index.html#statement-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Residues of Lucas numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/residues-of-lucas-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/residues-of-lucas-numbers)
