---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.ShannonHardFunction.wireCount, MetaMathlibExt.Complexity.KeyTheorems.ShannonHardFunction.shannon_hard_function
statement: formalized
---

# Shannon's circuit-size lower bound

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/shannon-s-circuit-size-lower-bound/index.html).

## Wire count of a flat circuit

The wire count of a flat Boolean circuit on $n$ inputs,
given as a list of gates, is the sum over its gates of the lengths of their predecessor lists:
every reference of a gate to a gate index is counted, with multiplicity, while input variables
and constants contribute nothing and the modulus of a mod gate is not counted.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.ShannonHardFunction.wireCount`, a definition declared in [WantedExt/Complexity/KeyTheorems/ShannonHardFunctionWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/ShannonHardFunctionWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/shannon-s-circuit-size-lower-bound/index.html#wire-count).

## Shannon: most Boolean functions need exponential circuits

For every natural number
$n \ge 10$, at least $2^{2^n}/2$ of the Boolean functions $f$ on $n$ input bits have the
following property: for every well-formed flat Boolean circuit $C$ on $n$ inputs without mod
gates whose wire count (the total length of the predecessor lists of its gates) is at most
$\lfloor 2^n / (10 n) \rfloor$, there is an input $x \in \{0,1\}^n$ such that $C$ has no
gates or the value of the last gate of $C$ on $x$ differs from $f(x)$.

## Sources

- C. E. Shannon, "The synthesis of two-terminal switching circuits", Bell System Technical Journal 28 (1949), 59-98.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.ShannonHardFunction.shannon_hard_function` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/ShannonHardFunctionWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/ShannonHardFunctionWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/shannon-s-circuit-size-lower-bound/index.html#shannon-hard-function).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Shannon's circuit-size lower bound](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/shannon-s-circuit-size-lower-bound/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/circuit-complexity/shannon-s-circuit-size-lower-bound)
