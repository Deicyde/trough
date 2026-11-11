---
declaration: section
origin: cited
lean: IsAddCyclic.of_squarefree_natCard, MetaMathlibExt.szele_cyclic_number_criterion
statement: formalized
proof: formalized
---

# Cyclic numbers

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/cyclic-numbers/index.html).

## Additive groups of squarefree order are cyclic

An additive commutative group of squarefree cardinality is additively
cyclic.

Formalized by `IsAddCyclic.of_squarefree_natCard`, a theorem declared in [MathlibExt/GroupTheory/AddCyclicSquarefree.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/AddCyclicSquarefree.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/cyclic-numbers/index.html#of-squarefree-nat-card).

## Szele's criterion for cyclic numbers

Let $n$ be a positive integer. Every group of order $n$
is cyclic if and only if $n$ is relatively prime to $\varphi(n)$, that is,
$\gcd(n, \varphi(n)) = 1$, where $\varphi$ is Euler's totient function.

## Sources

- Joel E. Cohen, "Conjectures about Primes and Cyclic Numbers," Journal of Integer Sequences 28 (2025), Article 25.4.7, Szele's criterion, lines 107–114, https://cs.uwaterloo.ca/journals/JIS/VOL28/Cohen/cohen41.tex (citing T. Szele, "Über die endlichen Ordnungszahlen, zu denen nur eine Gruppe gehört," Comment. Math. Helv. 20 (1947), 265–267).

Formalized by `MetaMathlibExt.szele_cyclic_number_criterion`, a theorem declared in [MathlibExt/GroupTheory/SzeleCyclicNumber.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/SzeleCyclicNumber.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/cyclic-numbers/index.html#szele-cyclic-number-criterion).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cyclic numbers](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/cyclic-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/orders-and-spectra/cyclic-numbers)
