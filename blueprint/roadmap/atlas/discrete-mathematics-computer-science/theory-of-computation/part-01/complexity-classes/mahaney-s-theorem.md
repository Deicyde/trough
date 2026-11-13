---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.Mahaney.Sparse, MetaMathlibExt.Complexity.KeyTheorems.Mahaney.NPComplete, MetaMathlibExt.Complexity.KeyTheorems.Mahaney.mahaney
statement: formalized
---

# Mahaney's theorem

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/mahaney-s-theorem/index.html).

## Sparse decision problems

A decision problem $L$ is sparse when there is a polynomial $p$
with natural-number coefficients such that, for every natural number $n$, the set of bitstrings
of length at most $n$ accepted by $L$ is finite and has at most $p(n)$ elements.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Mahaney.Sparse`, a definition declared in [WantedExt/Complexity/KeyTheorems/MahaneyWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/MahaneyWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/mahaney-s-theorem/index.html#sparse).

## NP-complete decision problems

A decision problem $L$ is NP-complete when $L$ is in NP
and every decision problem in NP has a polynomial-time many-one reduction to $L$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Mahaney.NPComplete`, a definition declared in [WantedExt/Complexity/KeyTheorems/MahaneyWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/MahaneyWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/mahaney-s-theorem/index.html#npcomplete).

## Mahaney's theorem: sparse NP-complete sets imply P = NP

If some decision problem is both
sparse and NP-complete, then the complexity classes $\mathsf{P}$ and $\mathsf{NP}$ are equal.

## Sources

- S. R. Mahaney, "Sparse complete sets for NP: solution of a conjecture of Berman and Hartmanis", Journal of Computer and System Sciences 25 (1982), 130-143.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.Mahaney.mahaney` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/MahaneyWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/MahaneyWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/mahaney-s-theorem/index.html#mahaney).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Mahaney's theorem](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/mahaney-s-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/complexity-classes/mahaney-s-theorem)
