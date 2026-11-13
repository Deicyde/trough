---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.OeisA022030Wanted.a, MathlibExt.NumberTheory.OeisA022030Wanted.conjecture, MathlibExt.NumberTheory.OeisA022030Wanted.conjecture_holds
statement: formalized
---

# Nonlinear floor recurrences satisfying linear recurrences

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/nonlinear-floor-recurrences-satisfying-linear-re/index.html).

## The sequence OEIS A022030

The sequence of natural numbers with $a(0) = 4$, $a(1) = 16$ and,
for every natural number $n$, $a(n + 2) = \lfloor (a(n + 1)^2 + a(n) - 1) / a(n) \rfloor - 1$ if
$n$ is even and $a(n + 2) = \lfloor a(n + 1)^2 / a(n) \rfloor + 1$ if $n$ is odd.

Formalized by `MathlibExt.NumberTheory.OeisA022030Wanted.a`, a definition declared in [WantedExt/NumberTheory/OeisA022030Wanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OeisA022030Wanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/nonlinear-floor-recurrences-satisfying-linear-re/index.html#a).

## Barker's linear recurrence for A022030

The statement that for every natural number
$n \ge 4$, the sequence $a$ of OEIS A022030 satisfies $a(n) = 4a(n - 1) - a(n - 3) + a(n - 4)$,
with the subtraction taken in the natural numbers (truncated at $0$).

Formalized by `MathlibExt.NumberTheory.OeisA022030Wanted.conjecture`, a definition declared in [WantedExt/NumberTheory/OeisA022030Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OeisA022030Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/nonlinear-floor-recurrences-satisfying-linear-re/index.html#conjecture).

## Barker's linear recurrence for A022030 holds

For every natural number $n \ge 4$, the
sequence $a$ of OEIS A022030 satisfies $a(n) = 4a(n - 1) - a(n - 3) + a(n - 4)$, with the
subtraction taken in the natural numbers (truncated at $0$).

## Sources

- Kenta Kitamura, Lean formal proof of Barker's linear recurrence, https://github.com/KitaKen1/oeis-a022030-lean/blob/f74afc2/lean/OeisA022030FC.lean#L270-L275.

Stated but not proved: `MathlibExt.NumberTheory.OeisA022030Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/OeisA022030Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OeisA022030Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/nonlinear-floor-recurrences-satisfying-linear-re/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Nonlinear floor recurrences satisfying linear recurrences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/nonlinear-floor-recurrences-satisfying-linear-re/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/recurrence-theory/nonlinear-floor-recurrences-satisfying-linear-re)
