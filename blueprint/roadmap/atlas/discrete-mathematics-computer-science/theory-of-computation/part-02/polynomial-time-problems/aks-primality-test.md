---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.PrimesInP.primesDec, MetaMathlibExt.Complexity.KeyTheorems.PrimesInP.primes_in_P
statement: formalized
---

# AKS primality test

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/aks-primality-test/index.html).

## The primality decision problem

The primality decision problem is the decision problem
that accepts a bitstring $x$ exactly when decoding $x$ with the canonical bitstring encoding of
the natural numbers (Mathlib's binary encoding) yields a prime number, and rejects $x$ otherwise.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.PrimesInP.primesDec`, a definition declared in [WantedExt/Complexity/KeyTheorems/PrimesInPWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/PrimesInPWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/aks-primality-test/index.html#primes-dec).

## PRIMES is in P

The primality decision problem, which accepts a bitstring exactly when it
decodes to a prime number under the canonical bitstring encoding of the natural numbers, belongs
to the complexity class P.

## Sources

- M. Agrawal, N. Kayal, and N. Saxena, "PRIMES is in P", Annals of Mathematics 160 (2004), 781-793.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.PrimesInP.primes_in_P` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/PrimesInPWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/PrimesInPWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/aks-primality-test/index.html#primes-in-p).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: AKS primality test](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/aks-primality-test/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/polynomial-time-problems/aks-primality-test)
