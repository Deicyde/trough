---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.NeukirchUchidaWanted.NumberTheory.neukirch_uchida
statement: formalized
---

# Adeles, ideles and class field theory: its own results

1 result, 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/index.html).

Places, adeles and ideles, Arakelov divisors, ray class groups, Artin map, Hilbert class fields, Neukirch–Uchida-type Galois characterization.

## Neukirch–Uchida theorem

Let $K_1$ and $K_2$ be number fields with separable closures
$\overline{K_1}$ and $\overline{K_2}$, and let
$\varphi \colon \mathrm{Gal}(\overline{K_1}/K_1) \to \mathrm{Gal}(\overline{K_2}/K_2)$ be a group
isomorphism that is a homeomorphism for the Krull topologies. Then there is a unique field
isomorphism $\sigma \colon \overline{K_2} \to \overline{K_1}$ that maps the image of $K_2$ in
$\overline{K_2}$ onto the image of $K_1$ in $\overline{K_1}$ and satisfies
$\varphi(g) = \sigma^{-1} \circ g \circ \sigma$ for every $g \in \mathrm{Gal}(\overline{K_1}/K_1)$.

## Sources

- Jürgen Neukirch, Alexander Schmidt, Kay Wingberg. *Cohomology of Number Fields*, Theorem 12.2.1. Problem `neukirch_uchida` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.NeukirchUchidaWanted.NumberTheory.neukirch_uchida` is written with `theorem_wanted` in [WantedExt/NumberTheory/NeukirchUchidaWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NeukirchUchidaWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/index.html#neukirch-uchida).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Adeles, ideles and class field theory](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory)
