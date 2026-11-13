---
declaration: section
origin: cited
lean: MetaMathlibExt.cook_levin_SAT_np_complete
statement: formalized
---

# Cook–Levin theorem: its own results

1 result, 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/index.html).

The Cook–Levin theorem and its machinery: SAT verifiers, dense and binary CNF encodings and converters between them, tableau formulas and the generator machines that emit them.

## Cook–Levin theorem: SAT is NP-complete

Let SAT be the decision problem on
bitstrings that accepts exactly the encodings of satisfiable CNF formulas. Then SAT belongs to
NP, and every decision problem $L$ in NP is polynomial-time many-one reducible to SAT: there
is a function $f$ from bitstrings to bitstrings, computable in polynomial time, such that
$L(x) = \mathrm{SAT}(f(x))$ for every bitstring $x$.

## Sources

- Stephen A. Cook, "The Complexity of Theorem-Proving Procedures," STOC 1971, 151–158, <https://doi.org/10.1145/800157.805047>; Leonid A. Levin, "Universal Sequential Search Problems," *Problems of Information Transmission* 9.3 (1973), 265–266; and <https://en.wikipedia.org/wiki/Cook%E2%80%93Levin_theorem>.

Stated but not proved: `MetaMathlibExt.cook_levin_SAT_np_complete` is written with `theorem_wanted` in [WantedExt/TheoryOfComputation/CookLevinSATWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/TheoryOfComputation/CookLevinSATWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/index.html#cook-levin-sat-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cook–Levin theorem](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/cook-levin)
