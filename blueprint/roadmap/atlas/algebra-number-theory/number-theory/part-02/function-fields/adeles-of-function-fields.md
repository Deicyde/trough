---
declaration: section
origin: cited
lean: FunctionFieldAdeleRing, FunctionFieldAdeleRing.ext, FunctionFieldAdeleRing.mem_valuationSubring_cofinitely
statement: formalized
proof: formalized
---

# Adeles of function fields

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/adeles-of-function-fields/index.html).

## Adèle ring of a field with respect to valuation subrings

Let $F$ be a field, $P$ a type
(of places) and, for each $p \in P$, let $O_p$ be a valuation subring of $F$. The adèle ring of
$F$ with respect to $(O_p)_{p \in P}$ is the restricted product of the copies of $F$ with respect
to the subrings $O_p$: its elements are the families $(a_p)_{p \in P}$ with $a_p \in F$ for every
$p$ and $a_p \in O_p$ for all but finitely many $p$.

Formalized by `FunctionFieldAdeleRing`, a definition declared in [MathlibExt/NumberTheory/FunctionField/AdeleRing.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/FunctionField/AdeleRing.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/adeles-of-function-fields/index.html#function-field-adele-ring).

## Extensionality for restricted-product adèles

Let $F$ be a field, $P$ a type and, for
each $p \in P$, let $O_p$ be a valuation subring of $F$. If two adèles $a$ and $b$ of the adèle
ring of $F$ with respect to $(O_p)_{p \in P}$ satisfy $a_p = b_p$ for every $p \in P$, then
$a = b$.

Formalized by `FunctionFieldAdeleRing.ext`, a theorem declared in [MathlibExt/NumberTheory/FunctionField/AdeleRing.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/FunctionField/AdeleRing.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/adeles-of-function-fields/index.html#ext).

## Adèles are integral at almost all places

Let $F$ be a field, $P$ a type and, for each
$p \in P$, let $O_p$ be a valuation subring of $F$. For every adèle $a$ of the adèle ring of $F$
with respect to $(O_p)_{p \in P}$, the component $a_p$ lies in $O_p$ for all but finitely many
$p \in P$.

Formalized by `FunctionFieldAdeleRing.mem_valuationSubring_cofinitely`, a theorem declared in [MathlibExt/NumberTheory/FunctionField/AdeleRing.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/FunctionField/AdeleRing.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/adeles-of-function-fields/index.html#mem-valuation-subring-cofinitely).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Adeles of function fields](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/adeles-of-function-fields/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/function-fields/adeles-of-function-fields)
