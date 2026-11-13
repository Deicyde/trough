---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.MAJSATPPComplete.majSatDec, MetaMathlibExt.Complexity.KeyTheorems.MAJSATPPComplete.majsat_pp_complete, MetaMathlibExt.Complexity.KeyTheorems.NPSubsetPP.np_subset_pp, MetaMathlibExt.Complexity.KeyTheorems.PPSubsetPSPACE.pp_subset_pspace
statement: formalized
---

# Unbounded-error probabilistic time (PP)

4 results, 1 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/counting-complexity/unbounded-error-probabilistic-time-pp/index.html).

## The MAJSAT language

MAJSAT is the decision problem that accepts a bitstring $x$ exactly
when $x$ decodes, under the canonical bitstring encoding of pairs, to a pair $(u, \varphi)$ of a
bitstring $u$ and a CNF formula $\varphi$ such that, with $n = |u|$, every literal of $\varphi$
has variable index less than $n$, and more than half of the $2^n$ assignments
$a : \{0, \dots, n-1\} \to \{\mathrm{true}, \mathrm{false}\}$ satisfy $\varphi$, that is, twice
their number exceeds $2^n$. Only the length of $u$ matters, and a bitstring that does not decode
is rejected.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.MAJSATPPComplete.majSatDec`, a definition declared in [WantedExt/Complexity/KeyTheorems/MAJSATPPCompleteWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/MAJSATPPCompleteWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/counting-complexity/unbounded-error-probabilistic-time-pp/index.html#maj-sat-dec).

## MAJSAT is PP-complete

The MAJSAT language is in PP, and every decision problem in PP has
a polynomial-time many-one reduction to MAJSAT.

## Sources

- J. Gill, "Computational complexity of probabilistic Turing machines", SIAM Journal on Computing 6 (1977), 675-695.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.MAJSATPPComplete.majsat_pp_complete` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/MAJSATPPCompleteWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/MAJSATPPCompleteWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/counting-complexity/unbounded-error-probabilistic-time-pp/index.html#majsat-pp-complete).

## NP is contained in PP

Every decision problem in NP also belongs to PP, the class of
decision problems decided in probabilistic polynomial time with unbounded error.

## Sources

- J. Gill, "Computational complexity of probabilistic Turing machines" (1977).

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.NPSubsetPP.np_subset_pp` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/NPSubsetPPWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/NPSubsetPPWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/counting-complexity/unbounded-error-probabilistic-time-pp/index.html#np-subset-pp).

## PP is contained in PSPACE

Every decision problem in PP, the class of decision problems
decided with unbounded error in probabilistic polynomial time, belongs to PSPACE.

## Sources

- J. Gill, "Computational complexity of probabilistic Turing machines" (1977); S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009 (PP ⊆ PSPACE).

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.PPSubsetPSPACE.pp_subset_pspace` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/PPSubsetPSPACEWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/PPSubsetPSPACEWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/counting-complexity/unbounded-error-probabilistic-time-pp/index.html#pp-subset-pspace).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Unbounded-error probabilistic time (PP)](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/counting-complexity/unbounded-error-probabilistic-time-pp/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/counting-complexity/unbounded-error-probabilistic-time-pp)
