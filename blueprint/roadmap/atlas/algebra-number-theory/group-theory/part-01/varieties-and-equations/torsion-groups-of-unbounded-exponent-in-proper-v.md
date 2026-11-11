---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.TorsionUnboundedExponentProperVarietyKourovka17Problem79Wanted.torsionUnboundedExponentProperVariety, MathlibExt.GroupTheory.TorsionUnboundedExponentProperVarietyKourovka17Problem79Wanted.torsionUnboundedExponentProperVariety_holds
statement: formalized
---

# Torsion groups of unbounded exponent in proper varieties

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/torsion-groups-of-unbounded-exponent-in-proper-v/index.html).

## Kourovka Problem 17.79 (torsion groups of unbounded exponent in proper varieties)

The
statement, asked by O. Macedońska, that there exists a finitely generated group $G$ in which every
element has finite order, which has unbounded exponent (there is no $n \ge 1$ with $g^n = 1$ for
all $g \in G$), and which satisfies a nontrivial law, that is, some element $w \ne 1$ of the free
group $F$ on countably infinitely many generators is mapped to $1$ by every homomorphism
$F \to G$ (equivalently, $G$ generates a proper variety of groups).

Formalized by `MathlibExt.GroupTheory.TorsionUnboundedExponentProperVarietyKourovka17Problem79Wanted.torsionUnboundedExponentProperVariety`, a definition declared in [WantedExt/GroupTheory/TorsionUnboundedExponentProperVarietyKourovka17Problem79Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TorsionUnboundedExponentProperVarietyKourovka17Problem79Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/torsion-groups-of-unbounded-exponent-in-proper-v/index.html#torsion-unbounded-exponent-proper-variet).

## Periodic groups of unbounded exponent in a proper variety

Resolved true: the Kourovka Archive answers 17.79 "Yes, moreover, there is a continuum of such
groups" (Atabekyan, 1986), and records Osin's example: a free group of the variety defined by `xⁿ y
= y xⁿ` is a central extension of a free Burnside group of exponent `n` with free abelian centre of
countable rank (Ashmanov-Olshanskii), and adding the relations `xᵢ^i = 1` for a basis `(xᵢ)` of the
centre gives a periodic group of unbounded exponent satisfying that law. Source: E. I. Khukhro and
V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue,
arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 17.79 (O. Macedońska); resolution: V.
S. Atabekyan, Infinite simple groups satisfying an identity, Dep. VINITI no. 5381-V86, Moscow, 1986
(Russian); D. Osin, letter of 31 August 2013, as recorded in the Kourovka Archive, Kourovka Archive,
Problem 17.79 (Yes, moreover there is a continuum of such groups (Atabekyan); Osin: a quotient of a
free group of the variety defined by x^n y = y x^n, by the relations x_i^i = 1 for a basis (x_i) of
its free abelian centre, is a periodic group of unbounded exponent in that variety).

Stated but not proved: `MathlibExt.GroupTheory.TorsionUnboundedExponentProperVarietyKourovka17Problem79Wanted.torsionUnboundedExponentProperVariety_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/TorsionUnboundedExponentProperVarietyKourovka17Problem79Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TorsionUnboundedExponentProperVarietyKourovka17Problem79Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/torsion-groups-of-unbounded-exponent-in-proper-v/index.html#torsion-unbounded-exponent-proper-variet-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Torsion groups of unbounded exponent in proper varieties](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/torsion-groups-of-unbounded-exponent-in-proper-v/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/varieties-and-equations/torsion-groups-of-unbounded-exponent-in-proper-v)
