---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.PCPTheorem.pcp_theorem
statement: formalized
---

# Probabilistically checkable proofs and inapproximability: its own results

1 result, 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/index.html).

The PCP theorem and Dinur's gap amplification, optimization classes (NPO, APX, MAXSNP), and hardness of approximation results such as Håstad's MAX-3SAT bound and the absence of a PTAS for MAX-CUT.

## The PCP theorem: NP = PCP(O(log n), O(1))

A decision problem belongs to NP if and only
if, for some natural numbers $c$ and $q$, it belongs to $\mathrm{PCP}(r, s)$, where the
randomness bound is $r(n) = c \lfloor \log_2(n + 1) \rfloor$ and the query bound is the constant
function $s(n) = q$.

## Sources

- S. Arora, C. Lund, R. Motwani, M. Sudan, and M. Szegedy, "Proof verification and the hardness of approximation problems", Journal of the ACM 45 (1998), 501-555 (FOCS 1992); S. Arora and S. Safra, "Probabilistic checking of proofs: a new characterization of NP", Journal of the ACM 45 (1998), 70-122.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.PCPTheorem.pcp_theorem` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/PCPTheoremWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/PCPTheoremWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/index.html#pcp-theorem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Probabilistically checkable proofs and inapproximability](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/pcp-and-inapproximability)
